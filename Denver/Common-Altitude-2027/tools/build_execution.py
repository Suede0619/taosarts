"""Build proposal finance, partner tables and operating calendars from explicit inputs."""
from pathlib import Path
from datetime import date, timedelta
from decimal import Decimal
import json, csv

BASE=Path(__file__).resolve().parents[1]
DATA=BASE/"data"
D=lambda x:Decimal(str(x))
USD=lambda x:("-$" if D(x)<0 else "$")+f"{abs(D(x)):,.0f}"
def csvwrite(name,rows):
    with (DATA/name).open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n")
        w.writeheader();w.writerows(rows)
def mdtable(headers,rows):
    return "\n".join(["| "+" | ".join(headers)+" |","| "+" | ".join(["---"]*len(headers))+" |"]+["| "+" | ".join(str(v) for v in r)+" |" for r in rows])
def finance(p):
    out=[];detail=[]
    for c in p["cases"]:
        buyers=D(c["qualified_households"])*D(c["buyer_conversion"])
        paid=D(c["visitors"])*D(c["paid_fraction"])
        assert buyers==int(buyers) and paid==int(paid)
        streams={"sponsorship":D(c["sponsorship"]),"gallery_services":D(c["galleries"])*D(c["gallery_service_fee"]),
                 "premium_program":paid*D(c["premium_price"]),"workshops":D(c["workshop_seats"])*D(c["workshop_price"]),"other":D(c["other"])}
        revenue=sum(streams.values());cost=sum(D(x) for x in c["costs"].values())
        row={"case":c["id"],"name":c["name"],"rooms":c["rooms"],"unique_visitors":c["visitors"],
             "qualified_households":c["qualified_households"],"completed_buyers":int(buyers),
             "average_art_order":c["average_art_order"],"art_gmv":int(buyers*D(c["average_art_order"])),
             **{k:int(v) for k,v in streams.items()},"organizer_revenue":int(revenue),"cost":int(cost),
             "pre_owner_surplus":int(revenue-cost)}
        assert revenue==sum(streams.values())
        out.append(row)
        detail.extend({"case":c["id"],"category":k,"assumed_cost":v} for k,v in c["costs"].items())
    core=next(r for r in out if r["case"]=="core")
    assert core["art_gmv"]==3000000 and core["organizer_revenue"]==1815000 and core["cost"]==1550000
    months=[];balance=D(0);cumulative={k:D(0) for k in p["cash_collection_shares"]}
    for k,shares in p["cash_collection_shares"].items():assert sum(D(s) for s in shares)==1
    assert sum(D(s) for s in p["cost_monthly_shares"])==1
    for i,month in enumerate(p["months"]):
        receipts={k:D(core[k])*D(shares[i]) for k,shares in p["cash_collection_shares"].items()}
        for k,v in receipts.items():cumulative[k]+=v
        paid_cost=D(core["cost"])*D(p["cost_monthly_shares"][i])
        balance+=sum(receipts.values())-paid_cost
        before=month<"2027-08"
        sponsor_hold=max(D(0),cumulative["sponsorship"]-D(p["seed_target"]))*D(p["early_sponsor_cash_restriction_fraction"]) if before else D(0)
        customer_hold=sum(v for k,v in cumulative.items() if k!="sponsorship") if before else sum(D(core[k]) for k in cumulative if k!="sponsorship")*D(p["post_event_refund_hold_fraction"])
        tax_hold=D(0) if before else D(p["tax_cash_hold"])
        op_reserve=D(p["reserve_schedule"][i])
        available=balance-sponsor_hold-customer_hold-tax_hold-op_reserve
        zero_sponsor_available=balance-customer_hold-tax_hold-op_reserve
        months.append({"month":month,**{k+"_cash":int(v) for k,v in receipts.items()},
                       "total_receipts":int(sum(receipts.values())),"cost_cash":int(paid_cost),
                       "unlevered_cash_balance":int(balance),"sponsor_cancellation_hold":int(sponsor_hold),
                       "customer_refund_hold":int(customer_hold),"tax_cash_hold":int(tax_hold),
                       "operating_reserve":int(op_reserve),"available_after_holds":int(available),
                       "required_bridge_outstanding":int(max(D(0),-available)),
                       "bridge_if_sponsor_unrestricted":int(max(D(0),-zero_sponsor_available))})
    assert sum(r["total_receipts"] for r in months)==core["organizer_revenue"]
    assert sum(r["cost_cash"] for r in months)==core["cost"]
    assert months[-1]["unlevered_cash_balance"]==core["pre_owner_surplus"]
    peak=max(r["required_bridge_outstanding"] for r in months)
    relaxed=max(r["bridge_if_sponsor_unrestricted"] for r in months)
    refund_hold=sum(D(core[k]) for k in cumulative if k!="sponsorship")*D(p["post_event_refund_hold_fraction"])
    eligible=max(D(0),D(core["pre_owner_surplus"])-D(p["tax_cash_hold"])-D(p["operating_reserve_after_event"])-refund_hold)
    owner=eligible*D(p["proposed_owner_profit_share"])
    final_eligible=eligible+refund_hold
    final_owner=final_eligible*D(p["proposed_owner_profit_share"])
    payout={"pre_owner_surplus":core["pre_owner_surplus"],"tax_cash_hold":p["tax_cash_hold"],
            "operating_reserve":p["operating_reserve_after_event"],"refund_hold":int(refund_hold),
            "initial_eligible_pool":int(eligible),"initial_owner_share":float(owner),
            "eligible_pool_if_refund_hold_released_without_claims":float(final_eligible),
            "owner_total_if_hold_released_without_claims":float(final_owner),
            "peak_bridge_with_sponsor_hold":peak,"peak_bridge_unrestricted_sponsor":relaxed}
    stress=[]
    for label,dr,dc in [("Base",0,0),("Sponsorship -25%",-core["sponsorship"]*.25,0),
                        ("Cost +20%",0,core["cost"]*.2),("Both changes",-core["sponsorship"]*.25,core["cost"]*.2),
                        ("Premium program revenue -40%",-core["premium_program"]*.4,0),
                        ("Optional gallery-service uptake -50%",-core["gallery_services"]*.5,0)]:
        stress.append({"stress":label,"revenue":int(core["organizer_revenue"]+dr),"cost":int(core["cost"]+dc),
                       "surplus_before_owner_tax_reserves":int(core["pre_owner_surplus"]+dr-dc)})
    csvwrite("financial-cases.csv",out);csvwrite("cost-detail.csv",detail);csvwrite("monthly-cash.csv",months);csvwrite("financial-stress.csv",stress)
    results={"cases":out,"core":core,"cash":months,"waterfall":payout,"stress":stress}
    (DATA/"financial-results.json").write_text(json.dumps(results,indent=2)+"\n")
    text=["# Generated proposal finance","",
          "As of October 24, 2026. USD. All costs, demand, funding and fee inputs are unvalidated proposal assumptions. No grants or organizer art commissions are included. This supersedes the earlier Denver sensitivity only for this larger proposed scope; the earlier model is unchanged.","",
          mdtable(["Measure"]+[r["name"] for r in out],[
          ["Programmed rooms / equivalent spaces"]+[r["rooms"] for r in out],
          ["Unique visitor target"]+[r["unique_visitors"] for r in out],
          ["Completed art GMV target"]+[USD(r["art_gmv"]) for r in out],
          ["Cash sponsorship"]+[USD(r["sponsorship"]) for r in out],
          ["Premium programs"]+[USD(r["premium_program"]) for r in out],
          ["Optional gallery services"]+[USD(r["gallery_services"]) for r in out],
          ["Workshops"]+[USD(r["workshops"]) for r in out],
          ["Other earned income"]+[USD(r["other"]) for r in out],
          ["Organizer revenue"]+[USD(r["organizer_revenue"]) for r in out],
          ["Cost including paid discovery"]+[USD(r["cost"]) for r in out],
          ["Surplus before owner / tax / reserves"]+[USD(r["pre_owner_surplus"]) for r in out]]),"",
          "## Core cash and conditional owner waterfall","",
          mdtable(["Item","Illustrative amount"],[[k.replace("_"," "),USD(v)] for k,v in payout.items()]),"",
          "Tax hold is an arbitrary cash-reserve placeholder, not a computed tax rate/liability. Refund hold is retained beyond the project year pending claims/rights. Owner share is a proposed 15% of the defined eligible pool, not agreed; excludes seller balances, tax collections and restricted funds. No payout is authorized. Full claim-free release is assumed only for comparison.","",
          "## Core monthly cash","",
          mdtable(["Month","Receipts","Costs","Cash before holds","Available after holds","Required bridge"],[
             [r["month"],USD(r["total_receipts"]),USD(r["cost_cash"]),USD(r["unlevered_cash_balance"]),USD(r["available_after_holds"]),USD(r["required_bridge_outstanding"])] for r in months]),"",
          "The model reserves 30% of cumulative sponsorship above the first $75,000 before opening, all customer advance receipts before opening, then 10% of non-sponsorship revenue against claims. Sponsor contracts/earning schedules are unknown; this is a risk sensitivity, not accounting advice. The first $75,000 is assumed milestone-earned discovery underwriting, credited once within sponsorship. No seller money finances the event. A facility is financing, not additional revenue. Financing cost is unquoted within the professional/finance allowance; actual fees/interest may require a budget increase.","",
          "## Stress cases","",
          mdtable(["Case","Revenue","Cost","Surplus before owner/tax/reserves"],[[r["stress"],USD(r["revenue"]),USD(r["cost"]),USD(r["surplus_before_owner_tax_reserves"])] for r in stress]),"",
          "Generated from [project inputs](project.json) by [build_execution.py](../tools/build_execution.py). Dated cash schedules, prices, scope and reserves require professional validation before contracts or sales.",""]
    (DATA/"financial-results.md").write_text("\n".join(text))
    return results

def partners():
    people=json.loads((DATA/"partners.json").read_text())
    assert len(people)==len({p["id"] for p in people})==72
    csvwrite("partner-longlist.csv",people)
    for prefix,folder,title in [("D","Denver","Denver and Front Range"),("N","North-America","North America"),("W","Worldwide","Worldwide and international networks")]:
        selected=[x for x in people if x["id"].startswith(prefix)]
        target=BASE/"partners"/folder;target.mkdir(parents=True,exist_ok=True)
        intro=f"# {title} — art and program partner research\n\nAs of October 24, 2026. **All 24 entries are uncontacted research candidates; no partnership, inventory, endorsement, appearance or availability is established.** Now/soon/middle/later refers to when to consider an authorized approach, not a scheduled appointment. Global galleries may operate in North America; these folders organize outreach strategy rather than exclusive geographic citizenship.\n\nGallery inventory, artist commissions, museum/education partnerships and technical production have different economics and decision makers. Institutional names do not imply commercial consignment. See [partner strategy](../PARTNER-STRATEGY.md), [hiring/engagement sequence](../../operations/01-Team-and-Hiring.md) and [source registry](../../RESEARCH.md).\n\n"
        rows=[[x["id"],f'**{x["name"]}** — {x["type"]}',x["approach_stage"],x["proposed_contribution"],x["constraints"]+f' [Official source]({x["url"]})'] for x in selected]
        (target/"README.md").write_text(intro+mdtable(["ID","Candidate","Stage","Specific invitation hypothesis","Evidence boundary / due diligence"],rows)+"\n")
    return len(people)

def calendar(p):
    (BASE/"operations").mkdir(parents=True,exist_ok=True)
    f=DATA/"weekly-work.json"
    if not f.exists():return 0
    weeks=json.loads(f.read_text())
    assert len(weeks)==53
    start=date.fromisoformat(p["project_start"]);end=date.fromisoformat(p["project_end"])
    daily=[];weekly=[]
    gates={g["date"]:g for g in p["gates"]}
    for i,w in enumerate(weeks):
        a=start+timedelta(days=i*7)
        if a>end:break
        b=min(end,a+timedelta(days=6))
        weekly.append({"week":i+1,"start":a.isoformat(),"end":b.isoformat(),"theme":w["theme"],
                       "gate":w["gate"],"owner":w["owner"],"deliverable":w["deliverable"],"status":"Planned; conditional"})
        assert len(w["days"])==7
        for j,task in enumerate(w["days"]):
            day=a+timedelta(days=j)
            if day>end:break
            n=(day-start).days+1
            if isinstance(task,str):task={"task":task,"owner":w["owner"]}
            gate=gates.get(day.isoformat())
            title=task["task"]
            if gate:title+="; DECISION: "+gate["title"]
            daily.append({"id":f"DAY-{n:03d}","date":day.isoformat(),"weekday":day.strftime("%A"),"week":i+1,
                          "action":title,"accountable_role":task.get("owner",w["owner"]),
                          "output":task.get("output",w["deliverable"]),
                          "prerequisite_gate":w["gate"],
                          "prior_calendar_record":f"DAY-{n-1:03d}" if n>1 else "None",
                          "workload":task.get("workload","Paid build/show/strike shift with rostered rest" if date(2027,7,26)<=day<=date(2027,8,20) else ("Light review / rest" if j in (0,6) else "Funded work block; scope to accepted hours")),
                          "status":"Planned; no external action authorized by this calendar"})
    assert len(daily)==365 and len(weekly)==53
    assert daily[0]["date"]=="2026-11-01" and daily[-1]["date"]=="2027-10-31"
    csvwrite("daily-action-plan.csv",daily);csvwrite("weekly-action-plan.csv",weekly)
    out=["# Day-by-day operating plan — year one","",
         "November 1, 2026–October 31, 2027; 365 dated records. Planning assignments by role, not accepted commitments. External actions occur only after appropriate authority and funding. Weekends are generally light review/rest; show/build periods differ. The prior-calendar-record field is a navigation reference, not a claim that unrelated streams must execute serially. Gate conditions override dates; carry blocked work forward rather than spend or announce prematurely.","",
         "Proposed event: August 9–15, 2027; public art days August 11–15. These dates are unbooked. [CSV](../data/daily-action-plan.csv) supports filtering/import; [weekly view](../data/weekly-action-plan.csv) summarizes 53 weeks. [Gate definitions](../data/project.json) and [critical path](03-Action-Plan-and-Gates.md) control execution.",""]
    for w in weekly:
        out += [f'## Week {w["week"]}: {w["theme"]}',"",f'{w["start"]}–{w["end"]} · Gate: {w["gate"]} · Accountable function: {w["owner"]}',"",
                mdtable(["Date","Action","Responsible function"],[[r["date"],r["action"],r["accountable_role"]] for r in daily if r["week"]==w["week"]]),""]
    (BASE/"operations"/"DAILY-ACTION-PLAN.md").write_text("\n".join(out))
    return len(daily)

def program(p):
    events=json.loads((DATA/"event-program.json").read_text())
    assert len(events)==len({e["id"] for e in events})==106
    workshops=[e for e in events if e["kind"]=="Paid workshop"]
    assert len(workshops)==50 and sum(int(e["seat_hypothesis"]) for e in workshops)==1000
    groups={}
    for e in events:
        assert e["start"]<e["end"]
        groups.setdefault((e["date"],e["zone"]),[]).append(e)
    for key,items in groups.items():
        ordered=sorted(items,key=lambda e:e["start"])
        assert all(a["end"]<=b["start"] for a,b in zip(ordered,ordered[1:])),key
    csvwrite("event-program.csv",events)
    departures=[]
    for day in sorted({e["date"] for e in workshops}):
        for i in range(p["premium_departures_per_day"]):
            minute=600+i*5;end=minute+45
            departures.append({"id":f"TOUR-{day}-{i+1:03d}","date":day,
                "departure":f"{minute//60:02d}:{minute%60:02d}","return":f"{end//60:02d}:{end%60:02d}",
                "planning_seats":p["premium_seats_per_departure"],"route":"Artist/producer-approved route assigned after site survey",
                "status":"Planning inventory only; no permitted capacity or reservation"})
    assert len(departures)==480 and sum(d["planning_seats"] for d in departures)==7200
    assert 6000<=sum(d["planning_seats"] for d in departures)
    csvwrite("premium-departures.csv",departures)
    text=["# Proposed event timetable","","America/Denver. Every time, zone, seat figure and collaborator is proposed and unconfirmed. Not a public calendar or permitted-capacity statement. Workshop rooms, guided routes and forum are functional placeholders until mapped to approved space.",""]
    for day in sorted({e["date"] for e in events}):
        text += ["## "+day,"",mdtable(["Time","Zone","Program","Accountable function","Access/price hypothesis"],[
            [e["start"]+"–"+e["end"],e["zone"],e["title"],e["accountable_role"],e["price_hypothesis"] or "Set after scope/approval"] for e in events if e["date"]==day]),""]
    text += ["Potential collaborators, status and capacity limits are in the [JSON](../data/event-program.json) and [CSV](../data/event-program.csv). The separate [guided-departure inventory](../data/premium-departures.csv) is a 7,200-seat theoretical planning model, not approved admissions.",""]
    (BASE/"program"/"PROGRAMME-TIMETABLE.md").write_text("\n".join(text))
    return len(events)

def main():
    DATA.mkdir(exist_ok=True)
    p=json.loads((DATA/"project.json").read_text())
    result=finance(p);n=partners();days=calendar(p);sessions=program(p)
    print(json.dumps({"finance_cases":len(result["cases"]),"core_revenue":result["core"]["organizer_revenue"],
                      "core_cost":result["core"]["cost"],"core_surplus":result["core"]["pre_owner_surplus"],
                      "waterfall":result["waterfall"],"partners":n,"daily_records":days,"program_records":sessions}))
if __name__=="__main__":main()
