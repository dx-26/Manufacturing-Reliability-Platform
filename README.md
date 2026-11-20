# Manufacturing Reliability Platform

> Asset health, maintenance prioritization, and downtime analysis

## Product problem

Plant supervisors, reliability engineers, and maintenance planners coordinating asset uptime.

## MVP features

Track production assets, record machine observations, calculate rule-based risk, create maintenance work orders, and inspect downtime trends.

This is a **working, local-first portfolio MVP** using **Python, Streamlit, pandas, and SQLite**. It includes preloaded fictional demo records, interactive forms, data tables and/or charts, CSV export, unit tests, and CI.

## Quick start

Requires Python 3.10 or newer (CI tests Python 3.12).

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
python -m pytest -q
```

## Product management perspective

**Users:** Plant supervisors, reliability engineers, and maintenance planners coordinating asset uptime.

**Metrics to track:** Downtime hours per asset; open critical work orders; mean time between failures; preventive task completion.

**Next iterations:** Connect real sensor feeds; calibrate risk thresholds against failure history; add role-based approval; integrate CMMS and predictive models.

## Key tradeoffs

* SQLite and a local web UI prioritize easy setup over multi-user scalability.
* Sample data and rules are illustrative; validate in real contexts before decisions.
* The MVP deliberately avoids personal data collection and external integrations.
* See `docs/architecture.md` and `SECURITY.md` for production hardening notes.

## Repository contents

* `app.py`: Streamlit UI and feature workflows
* `domain.py`: testable scoring or analytical rules
* `storage.py`: SQLite helpers and example records
* `tests/`: unit tests
* `.github/workflows/ci.yml`: GitHub Actions checks
* `docs/product-requirements.md`: outcomes and acceptance criteria
* `docs/roadmap.md`: delivery phases and risks

