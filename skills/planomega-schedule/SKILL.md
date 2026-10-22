---
name: planomega-schedule
description: Build a project schedule with dependencies and the critical path, a risk list with responses and a communication plan. Use when a user asks for a schedule, timeline, Gantt chart, critical path, deadlines or a risk list.
---

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language.

1. **Activities** from the WBS work packages, each with a duration estimate and how it was estimated (expert judgment, analogous, three-point).
2. **Dependencies:** finish-to-start (most common), start-to-start, finish-to-finish, start-to-finish; mark each as mandatory, discretionary or external. Add leads and lags.
3. **Critical path:** the longest path through the network. Put the tasks in a plan file and run `python3 scripts/planomega_cpm.py plan.json` to get earliest and latest dates, float and the critical path, plus a text Gantt chart. Report the numbers exactly.
4. **Risk list:** each risk is an event or condition (opportunities count too). Rate probability and impact High, Medium or Low. Choose a response: avoid, mitigate, transfer or accept. Every High/High risk needs a response plan and an owner. Add contingency where it matters.
5. **Communication:** who needs what update, how often and how (live or written).
6. Report: schedule table, critical path, milestone dates, the risk list, and what is still TO CONFIRM.
