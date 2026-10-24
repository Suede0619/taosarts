"""Standalone Denver fair sensitivity model. Run from any directory; standard library only.

This does not estimate site capacity, demand, actual costs, taxes or lawful distributions.
Art GMV remains seller pass-through. No parent festival/platform model is imported or changed.
"""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import csv
import json

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
D = lambda value: Decimal(str(value))
money = lambda value: D(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def write_csv(name, rows):
    with (DATA / name).open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def usd(value):
    return ("-$" if D(value) < 0 else "$") + f"{abs(D(value)):,.0f}"

def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"] +
                     ["| " + " | ".join(str(v) for v in row) + " |" for row in rows])

def build():
    inputs = json.loads((DATA / "model-inputs.json").read_text(), parse_float=Decimal)
    assert inputs["physical_fair_art_commission"] == 0
    assert inputs["direct_artist_website_commission"] == 0
    summaries, participation, costs = [], [], []
    for case in inputs["cases"]:
        paid_visitors = D(case["unique_visitors"]) * case["paid_share"]
        buyers = D(case["qualified_collector_households"]) * case["buyer_conversion"]
        assert paid_visitors == int(paid_visitors) and buyers == int(buyers)
        assert 0 <= case["paid_share"] <= 1 and 0 <= case["buyer_conversion"] <= 1
        assert buyers <= case["unique_visitors"]
        tickets = paid_visitors * case["ticket_price"]
        gallery = D(case["gallery_count"]) * case["gallery_service_fee"]
        art_gmv = buyers * case["average_completed_order"]
        streams = {"sponsorship": D(case["sponsorship"]), "gallery_services": gallery,
                   "tickets": tickets, "other": D(case["other"])}
        revenue = sum(streams.values())
        event_cost = sum(D(value) for value in case["costs"].values())
        surplus = revenue - event_cost
        preopening_outlay = event_cost * inputs["preopening_cost_fraction"]
        preopening_receipts = sum(value * inputs["preopening_collection_fractions"][key]
                                 for key, value in streams.items())
        ticket_refund_reserve = tickets * inputs["preopening_collection_fractions"]["tickets"]
        funding_gap = max(D(0), preopening_outlay - preopening_receipts)
        bridge = funding_gap + ticket_refund_reserve + inputs["operating_cash_reserve"]
        row = {"case": case["name"], "unique_visitors": case["unique_visitors"],
               "paid_visitors": int(paid_visitors), "ticket_revenue": money(tickets),
               "sponsorship_revenue": case["sponsorship"], "gallery_service_revenue": money(gallery),
               "other_revenue": case["other"], "organizer_revenue_excluding_art_gmv": money(revenue),
               "total_cost_including_paid_feasibility": money(event_cost),
               "surplus_before_owner_tax_and_additional_reserves": money(surplus),
               "qualified_collector_households": case["qualified_collector_households"],
               "completed_buyers_assuming_one_order_each": int(buyers),
               "average_completed_order": case["average_completed_order"],
               "completed_art_gmv_excluding_tax_shipping": money(art_gmv),
               "organizer_art_commission": 0,
               "preopening_cost_outlay": money(preopening_outlay),
               "preopening_cash_collected_assuming_eligibility": money(preopening_receipts),
               "preopening_timing_gap": money(funding_gap),
               "advance_ticket_refund_cash_hold": money(ticket_refund_reserve),
               "additional_operating_cash_reserve": inputs["operating_cash_reserve"],
               "illustrative_preopening_external_cash_need": money(bridge)}
        assert revenue == tickets + gallery + case["sponsorship"] + case["other"]
        assert surplus == revenue - event_cost
        summaries.append(row)
        for label, value in case["costs"].items():
            costs.append({"case": case["name"], "cost_category": label, "assumed_cost": value})
        for basis, amount in [("Completed art GMV", art_gmv), ("Organizer revenue", revenue),
                              ("Positive operating surplus BEFORE tax/reserve; upper bound only", max(D(0), surplus))]:
            for rate in inputs["venue_share_rates"]:
                share = money(amount * rate)
                participation.append({"case":case["name"], "share_basis":basis,
                    "rate":rate, "basis_amount":money(amount), "illustrative_owner_share":share,
                    "organizer_surplus_after_share_before_tax_reserves":money(surplus-share)})
    base = summaries[1]
    revenue = base["organizer_revenue_excluding_art_gmv"]
    cost = base["total_cost_including_paid_feasibility"]
    stress = []
    for label, delta_revenue, delta_cost in [
        ("No change",D(0),D(0)),
        ("Sponsorship 25% below assumption",-D(base["sponsorship_revenue"])*D(".25"),D(0)),
        ("Cost 20% above assumption",D(0),cost*D(".20")),
        ("Sponsorship -25% AND cost +20%",-D(base["sponsorship_revenue"])*D(".25"),cost*D(".20")),
        ("Paid ticket revenue 40% below assumption",-base["ticket_revenue"]*D(".40"),D(0)),
    ]:
        stress.append({"stress":label,"organizer_revenue":money(revenue+delta_revenue),
                       "total_cost":money(cost+delta_cost),
                       "surplus_before_owner_tax_reserves":money(revenue+delta_revenue-cost-delta_cost)})
    assert summaries[1]["completed_art_gmv_excluding_tax_shipping"] == 3000000
    assert summaries[1]["surplus_before_owner_tax_and_additional_reserves"] == 160000
    assert summaries[1]["illustrative_preopening_external_cash_need"] == 228500
    write_csv("case-summary.csv", summaries)
    write_csv("venue-participation.csv", participation)
    write_csv("cost-detail.csv", costs)
    write_csv("stress-tests.csv", stress)
    out = [
        "# Denver fair — generated sensitivity results",
        "",
        "As of October 24, 2026. Every monetary input is an unvalidated assumption. These are not forecasts, quotes, an approved budget or a safe-site plan. USD; exclude sales tax, shipping and seller balances. No art commission in the main cases.",
        "",
        table(["Measure"]+[s["case"] for s in summaries],[
            ["Unique visitors"]+[str(s["unique_visitors"]) for s in summaries],
            ["Qualified collector households"]+[str(s["qualified_collector_households"]) for s in summaries],
            ["Completed buyers / one order each"]+[str(s["completed_buyers_assuming_one_order_each"]) for s in summaries],
            ["Completed art GMV / seller pass-through"]+[usd(s["completed_art_gmv_excluding_tax_shipping"]) for s in summaries],
            ["Sponsorship"]+[usd(s["sponsorship_revenue"]) for s in summaries],
            ["Ticket revenue"]+[usd(s["ticket_revenue"]) for s in summaries],
            ["Optional gallery services"]+[usd(s["gallery_service_revenue"]) for s in summaries],
            ["Other earned income"]+[usd(s["other_revenue"]) for s in summaries],
            ["Organizer revenue"]+[usd(s["organizer_revenue_excluding_art_gmv"]) for s in summaries],
            ["Total cost incl. paid feasibility"]+[usd(s["total_cost_including_paid_feasibility"]) for s in summaries],
            ["Surplus before owner / tax / reserves"]+[usd(s["surplus_before_owner_tax_and_additional_reserves"]) for s in summaries],
            ["Illustrative preopening external cash need"]+[usd(s["illustrative_preopening_external_cash_need"]) for s in summaries],
        ]),
        "",
        "## Venue-share sensitivity — demand case to validate",
        "",
        "A positive-surplus share below is an upper-bound comparison before actual tax/claims/operating reserves. It is not a lawful distribution calculation. Negative after-share figures show why artist GMV and organizer income cannot be conflated.",
        "",
        table(["Basis", "Rate", "Owner share", "Surplus after share, before tax/reserves"],[
            [r["share_basis"],str(int(r["rate"]*100))+"%",usd(r["illustrative_owner_share"]),
             usd(r["organizer_surplus_after_share_before_tax_reserves"])]
            for r in participation if r["case"]==summaries[1]["case"]]),
        "",
        "## Downside stress — same demand case",
        "",
        table(["Change","Revenue","Cost","Surplus before owner/tax/reserves"],[
            [r["stress"],usd(r["organizer_revenue"]),usd(r["total_cost"]),
             usd(r["surplus_before_owner_tax_reserves"])] for r in stress]),
        "",
        "## Cash timing and exclusions",
        "",
        "Assume 85% of costs fall before opening; collect 60% of sponsorship, 70% of gallery-service fees, 30% of tickets and 30% of other income before opening. Hold all advance ticket cash against refunds and another $50,000 operating reserve. Sponsor/gallery cancellation obligations are unknown; additional ring-fencing could increase the gap. Artist cash, restricted grants, refundable balances and tax collections never finance production.",
        "",
        "Seed funding is not automatically extra revenue: if a feasibility underwriter receives later event sponsorship credit, count it once inside the sponsorship assumption. Cost includes the $70,000 paid-feasibility illustration once. No loan interest, actual income-tax calculation, VAT/import costs or building-specific remediation estimate is established; obtain quotes and professional calculations before investment or distributions.",
        "",
        "Generated with [the standalone model](../tools/feasibility_model.py) from [explicit inputs](model-inputs.json). Cost detail, all cases/bases and stress tests are in the adjacent CSV files. The existing Taos/platform model is unchanged.",
        "",
    ]
    (DATA/"model-results.md").write_text("\n".join(out))
    print("Validated 3 cases, 27 venue-share comparisons, 27 cost rows and 5 stress cases.")

if __name__ == "__main__":
    build()
