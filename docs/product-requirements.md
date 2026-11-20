# Product requirements — Manufacturing Reliability Platform

## Problem
Plant supervisors, reliability engineers, and maintenance planners coordinating asset uptime.

## Jobs to be done
When I need to manage the primary workflow in this domain, I want a concise record of what matters so I can prioritize and communicate next actions.

## MVP scope
Track production assets, record machine observations, calculate rule-based risk, create maintenance work orders, and inspect downtime trends.

## Acceptance criteria
1. Given a new local install, when the app starts, fictional demo records appear.
2. Given valid values in the relevant form, when I submit, a new record persists in SQLite.
3. Given invalid required input, when I submit, the interface shows an error and does not insert a record.
4. Given stored records, when I use analytics views, any scores are deterministic and explained.
5. Given the export action, when clicked, a CSV downloads with visible records.
6. Given a GitHub push or pull request, when CI runs, unit tests execute.

## Out of scope
- User authentication and collaboration
- Production-grade tenancy or compliance
- Live external integration and guaranteed real-time data
- Trained or deployed AI models

## Success measures
Downtime hours per asset; open critical work orders; mean time between failures; preventive task completion.
