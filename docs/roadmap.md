# Delivery roadmap — Manufacturing Reliability Platform

## Phase 1 — Portfolio MVP (included)
- Interactive user workflows, demo records, rule-based calculations, export, automated tests
- README, requirements, architecture, CI, and security caveats

## Phase 2 — Validation
- Interview 3–5 target users
- Review metrics and workflow friction
- Expand negative/edge-case tests and accessibility checks

## Phase 3 — Scale
Connect real sensor feeds; calibrate risk thresholds against failure history; add role-based approval; integrate CMMS and predictive models.

## Risks and mitigations
- **Synthetic data**: label sample values clearly; do not infer actual business outcomes.
- **Overinterpretation**: disclose heuristics and validate with domain users.
- **Privacy**: keep local demo information non-sensitive.
- **Scalability**: migrate SQLite to managed storage before multi-user deployment.
