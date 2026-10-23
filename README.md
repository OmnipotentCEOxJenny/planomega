# PlanOmega

PlanOmega helps your AI assistant turn a goal into a project plan you can actually follow. You say what you want to achieve and by when. It rewrites the goal so it can be measured, writes a one-page project charter, breaks the work into pieces, puts them in order on a schedule, shows which tasks cannot slip without delaying everything, and lists the risks with a plan for each. Why would you want this? Big goals feel overwhelming, and plans made in your head miss steps. A written plan shows what to do next, what could go wrong, and when you will be done. It's free.

![PlanOmega logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed (v1.0.1: keyword capitalization) to GitHub. Local tests: manifest valid JSON and valid against Cursor's plugin schema, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_cpm.py` confirms the schedule helper reproduces the PluginPulse v1.1 plan (164 hours, critical path D-F-G-H-I-J-K), passes a hand-checked self-test, and rejects a dependency loop.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

## Quick start
1. Install (see Installation).
2. Ask: "Plan this: launch my bakery's website by December 1 with a $0 budget."
3. Then ask: "Make the schedule and risk list."

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/planomega (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The optional schedule helper needs only Python 3 (standard library).

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python3 tests/test_cpm.py`. Expected: PASS.
3. Compare with `examples/pluginpulse-v1.1/`.

## Search keywords
PlanOmega, JennyEcho, OmnipotentCeo, planning, planner, charter, wbs, breakdown, schedule, scheduling, gantt, milestones, deadlines, risk, risks, mitigation, contingency, stakeholders, scope, objectives, smart, deliverables, tasks, dependencies, float, slack, estimates, estimating, timeline, roadmap, kickoff, projects, sponsor, requirements, constraints, assumptions, closeout, initiation, cpm, network. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Method drawn from the free open textbook Jenny Echo studied in Course 5: Adrienne Watt, *Project Management*, 2nd edition, BCcampus, CC BY 4.0 (four phases, SMART objectives, the sample project charter, requirement categories, the WBS 100 percent rule, dependencies and the critical path, risk ratings and responses, communication planning). Summarized in our own words; PlanOmega is independent and not endorsed by the author or BCcampus.
- The critical-path method itself (forward and backward pass) is a standard general technique.

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never invent; anything unchecked is marked UNVERIFIED.
2. Use only legitimate means: free, legitimate tools and sources only.
3. Double-check everything: results are checked before they are called done.
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/planomega-charter`: goal to SMART objective, charter, requirements and WBS.
- `skills/planomega-schedule`: schedule, critical path, risk list and communication plan.
- `scripts/planomega_cpm.py`: optional critical-path and risk-sorting helper (standard library only).
- `examples/pluginpulse-v1.1/`: a real worked plan.
- `tests/`: front-matter check and functional schedule test.
- `rules/pillars-and-scope.mdc`: the pillars and scope.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and code unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative. Each language section in TRANSLATIONS.md also starts with a one-line machine-translation notice in that language.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It cannot know your real dates, budget or people; anything you do not tell it is marked TO CONFIRM.
- Estimates are only as good as the information given; the plan can be wrong and needs updating as work happens.
- The schedule helper works in plain units (hours or days) and does not handle calendars, weekends or resource limits.
- It is not legal, financial or safety advice.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
