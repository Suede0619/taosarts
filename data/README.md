# Data and model definitions

These files contain **public historical aggregates or proposed model assumptions**, never real buyer-level data.

| File | Meaning |
|---|---|
| [festival-financial-history.csv](festival-financial-history.csv) | Organizational annual figures, 2014–2024; blank 2025–2026. Not artwork sales. Source URL and evidence label per row. |
| [festival-attendance-and-art-sales.csv](festival-attendance-and-art-sales.csv) | Annual missing-data register, 2014–2026. Blank numeric fields are unknown, never zero. |
| [model-inputs.json](model-inputs.json) | Editable proposal: channel shares, fee assumptions, scenario budgets, buyer order cohorts, and cash timing. |
| [scenario-summary.csv](scenario-summary.csv) | Generated combined operating scenarios. Artist and gallery shares are not operating revenue. |
| [base-cashflow.csv](base-cashflow.csv) | Generated cash forecast in twelve month-long planning periods beginning October 19. Opening financing is outside operating income. |
| [sensitivity.csv](sensitivity.csv) | Generated downside cases holding base non-processing costs fixed. |
| [model-results.md](model-results.md) | Generated readable summary. |

**GMV** means gross merchandise value, used here only for completed, paid, fulfilled art value under the reporting rules. It excludes tax, delivery, admissions, donations, refunds, and unfulfilled contract balances. A deposit is cash received and a liability/contract balance as appropriate, not automatically completed GMV.

**Artist proceeds** are contractual artist shares before production costs and personal tax. **Gallery retained** is the modeled amount remaining after artist share and project referral fee, before the gallery's own expenses. **Project transaction income** is retained fee income. Operating income additionally includes the modeled partner, sponsor, grant, patron, and optional-program sources.

**Public historical evidence:** ProPublica IRS extraction through 2023, Cause IQ extraction for 2024; full returns not reviewed. Field names map to `totrevenue`, `totfuncexpns`, `totnetassetsend`, `totcntrbs`, and `prgmservrev`. Surplus is revenue less expenses, not necessarily the full change in net assets. Year is fiscal year, not necessarily festival edition.

**Generated model:** Python standard library only; `python3 tools/financial_model.py` from repository root. Edit assumptions first, regenerate, then review related prose for consistency. Monetary CSV outputs are USD; modeled cash rounds to cents. Timing allocations are assumptions, not contract schedules. No source documents, credentials, private archive, or live sales ledger are required to run the model.
