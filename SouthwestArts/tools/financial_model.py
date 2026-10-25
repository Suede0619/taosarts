#!/usr/bin/env python3
"""Rebuild transparent scenario and cash-flow outputs from planning assumptions.
Run from the ART repository root: python3 SouthwestArts/tools/financial_model.py
No network access or private inputs. Monetary values are nominal USD.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def close(a, b, label):
    if abs(a-b) > 0.01:
        raise ValueError(f'{label}: {a} != {b}')

def write_csv(name, rows):
    with (ROOT/'data'/name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def money(value):
    return f'${value:,.0f}' if value >= 0 else f'−${-value:,.0f}'

def calculate(config, scenario):
    gmv = scenario['gmv']
    artists = galleries = fees = processed = 0
    close(sum(c['gmv_share'] for c in config['channels']), 1, 'channel shares')
    for channel in config['channels']:
        close(sum(channel[k] for k in ['artist_share','gallery_share','project_fee_share']), 1, channel['name'])
        volume = gmv * channel['gmv_share']
        artists += volume * channel['artist_share']
        galleries += volume * channel['gallery_share']
        fees += volume * channel['project_fee_share']
        if channel['project_processes_payment']:
            processed += volume
    close(artists+galleries+fees, gmv, 'sale allocation')
    payments = processed * config['processor_rate']
    revenue = fees + sum(scenario[k] for k in ['partners','sponsors','grants','patrons','programs'])
    expenses = payments + sum(scenario['expenses'].values())
    return dict(gmv_usd=gmv, artist_proceeds_usd=artists, gallery_retained_usd=galleries,
                transaction_income_usd=fees, operating_income_usd=revenue,
                operating_expenses_usd=expenses, payment_processing_usd=payments,
                operating_surplus_usd=revenue-expenses)

def cashflow(config, scenario, result):
    cf = config['cashflow']
    for key in ['gmv','partners','sponsors','grants','patrons','programs','nonpayment_expenses']:
        if len(cf[key]) != 12:
            raise ValueError(f'Need twelve cashflow periods for {key}')
        close(sum(cf[key]), 1, f'{key} timing shares')
    balance = cf['opening_unrestricted_cash']
    rows = []
    for i, period in enumerate(cf['periods']):
        income = result['transaction_income_usd'] * cf['gmv'][i]
        income += sum(scenario[k]*cf[k][i] for k in ['partners','sponsors','grants','patrons','programs'])
        cost = sum(scenario['expenses'].values()) * cf['nonpayment_expenses'][i]
        cost += result['payment_processing_usd'] * cf['gmv'][i]
        balance += income-cost
        rows.append(dict(period=period, operating_cash_in_usd=round(income,2),
                         operating_cash_out_usd=round(cost,2), net_cash_usd=round(income-cost,2),
                         ending_unrestricted_cash_usd=round(balance,2)))
    close(sum(r['operating_cash_in_usd'] for r in rows), result['operating_income_usd'], 'cash receipts')
    close(sum(r['operating_cash_out_usd'] for r in rows), result['operating_expenses_usd'], 'cash payments')
    close(balance, cf['opening_unrestricted_cash']+result['operating_surplus_usd'], 'closing cash')
    return rows

def main():
    config = json.loads((ROOT/'data/model-inputs.json').read_text())
    results = []
    for name, scenario in config['scenarios'].items():
        results.append(dict(scenario=name, **calculate(config,scenario)))
    close(sum(c['orders']*c['average_order'] for c in config['base_order_cohorts']),
          config['scenarios']['base']['gmv'], 'base order cohorts')
    write_csv('scenario-summary.csv', results)
    base = next(r for r in results if r['scenario']=='base')
    rows = cashflow(config,config['scenarios']['base'],base)
    write_csv('base-cashflow.csv', rows)
    min_cash = min(r['ending_unrestricted_cash_usd'] for r in rows)
    # Opening cash is a financing assumption, never operating revenue.
    required_opening = max(0, config['cashflow']['opening_unrestricted_cash']-min_cash)
    stress=[]
    for name, gm, grants, sponsor in [('base',1,1,1),('GMV down 20%',.8,1,1),
             ('no grants',1,0,1),('sponsors down 50%',1,1,.5),('combined downside',.8,0,.5)]:
        scenario=json.loads(json.dumps(config['scenarios']['base']))
        scenario['gmv']*=gm;scenario['grants']*=grants;scenario['sponsors']*=sponsor
        result=calculate(config,scenario)
        flow=cashflow(config,scenario,result)
        stress.append(dict(case=name,operating_surplus_usd=result['operating_surplus_usd'],
                          lowest_cash_with_50000_opening_usd=min(r['ending_unrestricted_cash_usd'] for r in flow)))
    write_csv('sensitivity.csv',stress)
    text=['# Generated model results','',
          'Planning assumptions only. Rebuild with `python3 SouthwestArts/tools/financial_model.py` from the ART repository root.','',
          f'Planning period: **{config["period"]}**.',
          f'Model scope: **{config["status"]}**.','',
          '| Scenario | Art value | Artist proceeds | Gallery retained | Transaction income | Operating income | Expenses | Surplus / deficit |',
          '|---|---:|---:|---:|---:|---:|---:|---:|']
    for r in results:
        text.append('| '+r['scenario']+' | '+' | '.join(money(r[k]) for k in ['gmv_usd','artist_proceeds_usd','gallery_retained_usd','transaction_income_usd','operating_income_usd','operating_expenses_usd','operating_surplus_usd'])+' |')
    text+=['',f'Base cashflow assumes {money(config["cashflow"]["opening_unrestricted_cash"])} opening unrestricted financing. The model excludes it from earned revenue.',
           f'Lowest modeled base cash balance: **{money(min_cash)}**. Opening financing needed merely to avoid a negative balance: **{money(required_opening)}**, before any reserve.',
           '', '| Sensitivity | Annual surplus / deficit | Lowest cash with $50,000 opening |','|---|---:|---:|']
    for r in stress:text.append(f'| {r["case"]} | {money(r["operating_surplus_usd"])} | {money(r["lowest_cash_with_50000_opening_usd"])} |')
    text+=['','The model collects operating income when it recognizes revenue and receives all grant reimbursement by the final period. Delays, returns, tax, restrictions, and receivables can worsen cash. Artist and gallery shares are pass-through liabilities, never operating cash available to spend.']
    (ROOT/'data/model-results.md').write_text('\n'.join(text)+'\n')
    print('Validated sale allocations, timing shares, cohort totals, annual cash reconciliation, and downside cases.')
    print(f"Base income {money(base['operating_income_usd'])}, costs {money(base['operating_expenses_usd'])}, lowest cash {money(min_cash)}. Financing floor {money(required_opening)} before reserve.")

if __name__=='__main__':
    main()
