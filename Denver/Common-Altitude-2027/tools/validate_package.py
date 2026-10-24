"""Validate the public proposal and its generated artifacts; no external actions."""
from pathlib import Path
from datetime import date, timedelta
from hashlib import sha256
import json,csv,re,zipfile,xml.etree.ElementTree as ET
import fitz
from pptx import Presentation

BASE=Path(__file__).resolve().parents[1]
PRIVATE=BASE/"private"
PRIVACY_TERMS=PRIVATE/"privacy-terms.json"
terms=json.loads(PRIVACY_TERMS.read_text()) if PRIVACY_TERMS.exists() else []
NAME=re.compile(r"\b(?:"+"|".join(re.escape(t) for t in terms)+r")\b",re.I) if terms else re.compile(r"(?!x)x")
def readcsv(name):
    with (BASE/"data"/name).open() as f:return list(csv.DictReader(f))
def norm(t):return re.sub(r"[^a-z0-9]","",t.lower())
def main():
    public=[p for p in BASE.rglob("*") if p.is_file() and "private" not in p.relative_to(BASE).parts and "__pycache__" not in p.parts]
    errors=[];links=0
    for p in public:
        if p.suffix in [".md",".json",".csv",".py",".svg",".txt"]:
            s=p.read_text()
            if NAME.search(s):errors.append("Participant name in "+str(p.relative_to(BASE)))
        if p.suffix==".md":
            for raw in re.findall(r"(?<!!)\[[^\]]*\]\(([^\n]+?)\)",p.read_text()):
                target=raw.strip().strip("<>").split("#")[0]
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",target) or not target:continue
                links+=1
                if not (p.parent/target).exists():errors.append("Missing link "+str(p.relative_to(BASE))+": "+raw)
    project=json.loads((BASE/"data/project.json").read_text())
    cases=readcsv("financial-cases.csv");cash=readcsv("monthly-cash.csv")
    core=next(r for r in cases if r["case"]=="core")
    assert int(core["organizer_revenue"])-int(core["cost"])==int(core["pre_owner_surplus"])==265000
    assert int(core["art_gmv"])==3000000 and int(core["cost"])==1550000
    assert sum(int(r["total_receipts"]) for r in cash)==1815000
    assert sum(int(r["cost_cash"]) for r in cash)==1550000
    assert max(int(r["required_bridge_outstanding"]) for r in cash)==530000
    daily=readcsv("daily-action-plan.csv");weekly=readcsv("weekly-action-plan.csv")
    assert len(daily)==365 and len(weekly)==53
    first=date(2026,11,1)
    assert [r["date"] for r in daily]==[(first+timedelta(days=i)).isoformat() for i in range(365)]
    assert len({r["id"] for r in daily})==365
    gates={"PRE"}|{g["id"] for g in project["gates"]}
    assert all(r["prerequisite_gate"] in gates for r in daily)
    partners=readcsv("partner-longlist.csv")
    assert len(partners)==len({r["id"] for r in partners})==72
    assert all(sum(r["id"].startswith(prefix) for r in partners)==24 for prefix in "DNW")
    sources=readcsv("source-index.csv")
    assert len(sources)==len({r["id"] for r in sources})==97
    assert {r["id"] for r in partners}<={r["id"] for r in sources}
    program=readcsv("event-program.csv");tours=readcsv("premium-departures.csv")
    assert len(program)==len({r["id"] for r in program})==106
    assert sum(r["kind"]=="Paid workshop" for r in program)==50
    assert sum(int(r["seat_hypothesis"]) for r in program if r["kind"]=="Paid workshop")==1000
    assert len(tours)==480 and sum(int(r["planning_seats"]) for r in tours)==7200
    assert all(r["return"]<="19:00" for r in tours)
    templates=list((BASE/"data/templates").glob("*.csv"))
    assert len(templates)==12
    for p in templates:
        with p.open() as f:assert len(list(csv.reader(f)))==1
    for p in (BASE/"assets").glob("*.svg"):ET.fromstring(p.read_text())
    manifest=json.loads((BASE/"data/deck-manifest.json").read_text())
    assert len(manifest)==8 and sum(r["slides"] for r in manifest)==101
    pages=0;text_checks=0
    for r in manifest:
        ppt=BASE/"decks"/r["pptx"];pdf=BASE/"decks"/r["pdf"]
        prs=Presentation(ppt);doc=fitz.open(pdf)
        assert len(prs.slides)==len(doc)==r["slides"],r["id"]
        if NAME.search(str(doc.metadata)):errors.append("PDF metadata participant name "+r["id"])
        for i,(slide,page) in enumerate(zip(prs.slides,doc)):
            pdftext=norm(page.get_text())
            if NAME.search(page.get_text()):errors.append("PDF participant name "+r["id"])
            for shape in slide.shapes:
                if shape.left<0 or shape.top<0 or shape.left+shape.width>prs.slide_width+100 or shape.top+shape.height>prs.slide_height+100:
                    errors.append("Shape out of bounds "+r["id"]+" "+str(i+1))
                if shape.has_text_frame:
                    expected=norm(shape.text_frame.text)
                    if len(expected)>3 and expected not in pdftext:
                        errors.append("PDF text mismatch "+r["id"]+" "+str(i+1)+": "+shape.text_frame.text[:100])
                    if expected:text_checks+=1
            for block in page.get_text("dict")["blocks"]:
                if "lines" not in block:continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        x0,y0,x1,y1=span["bbox"]
                        if x0 < -1 or y0 < -1 or x1>page.rect.width+1 or y1>page.rect.height+1:
                            errors.append("PDF text outside page "+r["id"]+" "+str(i+1))
            assert f"{i+1:02d} / {len(doc):02d}" in page.get_text(),(r["id"],i+1)
        with zipfile.ZipFile(ppt) as z:
            for name in z.namelist():
                if name.endswith(".xml") and NAME.search(z.read(name).decode(errors="replace")):
                    errors.append("PowerPoint XML participant name "+r["id"])
        pages+=len(doc)
        r["status"]="Rendered PDF/PPTX text and geometry checked; representative visual review performed"
    source_hashes=0
    sm=PRIVATE/"sources/manifest.json"
    if sm.exists():
        for r in json.loads(sm.read_text()):
            if "file" in r:
                p=sm.parent/r["file"]
                assert len(p.read_bytes())==r["bytes"]
                assert sha256(p.read_bytes()).hexdigest()==r["sha256"],r["id"]
                source_hashes+=1
    report={"as_of":"2026-10-24","public_files_checked":len(public),"relative_links_checked":links,"private_privacy_terms_configured":bool(terms),
            "finance_cases":len(cases),"financial_stress_cases":len(readcsv("financial-stress.csv")),
            "months":len(cash),"daily_actions":len(daily),"weekly_records":len(weekly),
            "partner_records":len(partners),"indexed_sources":len(sources),"retained_source_body_hashes_verified":source_hashes,
            "program_records":len(program),"paid_workshop_sessions":50,"workshop_planning_seats":1000,
            "guided_departure_records":len(tours),"guided_theoretical_seats":7200,
            "blank_schemas":len(templates),"public_presentations":len(manifest),"public_pdf_pages":pages,
            "pptx_text_shapes_checked_against_pdf":text_checks,"errors":errors,
            "limits":"Technical/content consistency checks do not validate demand, safe/legal capacity, rights, costs, funding, partner availability or lawful distributions."}
    if errors:print(json.dumps(report,indent=2));raise SystemExit(1)
    (BASE/"data/deck-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    (BASE/"data/package-validation.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
