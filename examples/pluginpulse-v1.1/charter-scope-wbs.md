# PluginPulse v1.1 — Project Charter, Scope Statement and WBS (FINAL)
Format follows Watt, *Project Management* 2nd ed., Ch 7 "Sample Project Charter" (pp. 68-71) and Ch 9 (pp. 77-91). Facts are from the repo (v1.0.4, commit d77133d), `/workspace/pluginpulse-daily.log`, `marketplace-plugins.md`, and the digest test in `00-evidence-digest-simulation.md`. Proposed plan; nothing is changed in the repo by this document.

## 1. Project charter

### Identification
| | |
|---|---|
| Project name | PluginPulse v1.1: first full 7-day history and ranked "Rising" digest |
| Date / revision | October 22, 2026 / Revision 1 |
| Project sponsor (authority) | Rob Domaine, Inventor and Publisher, Omnipotent Media LLC. Approves the plan, the v1.1.0 tag, and any marketplace submission. |
| Project manager | Jenny Echo (Grok Bot), plugin builder. Authority: change code and docs in the PluginPulse repo, run the daily job, push forward-only tags under Rob's standing OK for improvements. No authority to submit to the marketplace or rewrite tags. |

### Overview
PluginPulse v1.0.4 collects one public-data snapshot a day. Its weekly digest cannot rank "Rising" repos until the snapshots span seven days. This project delivers that first full history, fixes two defects found while planning, and releases v1.1.0.

### Objective (SMART: Specific, Measurable, Acceptable, Realistic, Time based)
By **6:00 PM ET on October 27, 2026**, publish PluginPulse **v1.1.0** on GitHub such that:
1. `data/` holds **8 consecutive daily snapshots, October 20-27** (a 7-day span), with **at most 1** manual catch-up run from October 23 on;
2. the digest generated from them prints a **ranked "Rising" list** with no "+None" entries;
3. `scripts/repos.txt` tracks **all 8** of Rob's plugin repos plus the 2 MCP repos (10), at **no more than 50 GitHub requests per run**;
4. all repo tests pass (`tests/check_frontmatter.py` ALL PASS; CLI loads).
- Acceptable: matches Rob's standing goal ("run a snapshot daily for 7+ days before rising means anything") and his hold on submission.
- Realistic: two small code changes, both reproduced on copies already; the rest is waiting for calendar days.
- Time based: a deadline, not a duration.

### Scope
Included:
1. Daily snapshots October 23-27 by the unattended job, with morning checks.
2. Fix the "Rising" baseline defect: a repo missing from the first snapshot prints "+None stars" (reproduced in 00-evidence).
3. Add `OmnipotentCEOxJenny/inplug-plugin` and `OmnipotentCEOxJenny/lingolink` to `scripts/repos.txt` (now 6 of 8 Rob plugins tracked).
4. Make the README and the code agree on the history rule ("7-day span = 8 daily snapshots").
5. Publish the first real ranked digest as `examples/digest-2026-10-27.md`.
6. Release: CHANGELOG, version 1.1.0 in plugin.json and script, forward tag v1.1.0, TRANSLATIONS note.

**Not included:**
- Marketplace submission or ticking the "tested in-app" box (Rob's hold; sponsor decision after v1.1).
- Raising `--registry-pages` above 20 (registry counts stay a capped sample).
- Install counts, ratings, paid APIs, logins, or any non-public data.
- Native-speaker review of the 23 translations.
- Changes to the other seven plugins.

### Major milestones
| ID | Milestone | Target (ET) |
|---|---|---|
| M1 | Charter accepted by Rob | Oct 23, 10:00 AM |
| M2 | Code fixes (baseline, repos list, README rule) pushed as v1.0.5 | Oct 23, 11:00 AM (after the 9:00 AM run) |
| M3 | First unattended snapshot after the job fix | Oct 23, ~9:00-9:10 AM |
| M4 | Eighth consecutive snapshot (7-day span) | Oct 27, ~9:00-9:10 AM |
| M5 | First ranked Rising digest generated and reviewed | Oct 27, 12:00 PM |
| M6 | v1.1.0 tagged and pushed | Oct 27, 6:00 PM |

### Major deliverables
1. Snapshot history `snapshot-2026-10-20.json` to `snapshot-2026-10-27.json` (local `data/`, git-ignored by design).
2. PluginPulse v1.0.5 (code fixes) and v1.1.0 (release) on GitHub.
3. `examples/digest-2026-10-27.md`, the first ranked Rising digest.
4. Project documents: this charter, schedule, risk register, communication plan, and a closeout note.

### Assumptions
- The box stays on and the job process (`pluginpulse-daily.sh`, wake every 10 min) keeps running through Oct 27.
- The MCP Registry, GitHub REST API and x.ai marketplace page stay public, free and unchanged in format.
- GitHub's unauthenticated limit remains 60 requests/hour.
- Rob's standing OK covers pushing v1.0.5 and v1.1.0 (improvements, no resubmission).
- Repos added on Oct 23 will have under 7 days of history on Oct 27 and will be shown as "new, no 7-day baseline", not ranked.

### Constraints
- Free tools only; $0 cash.
- GitHub budget: `GH_BUDGET = 50` per run (code), under the 60/hour limit.
- One marketplace page request per run after robots.txt; Retry-After honored.
- Forward-only version tags; no tag rewrites; no resubmission.
- Fixed calendar: the 7-day span cannot finish before the Oct 27 snapshot whatever the effort.

### Business need or opportunity (benefits)
Rob needs evidence of what is moving in the plugin and MCP ecosystem. v1.0.4 can't show that yet. v1.1 turns PluginPulse from a snapshot collector into a working trend report, and it gives Rob a tested, honest version to consider submitting.

### Preliminary cost
$0 cash. Effort is agent run time: about 4.3 hours of active Echo effort in total (WBS sum; 1.0 h already spent on the plan) plus about 0.2 hours of Rob's time. Control: requests are capped in code, and the work is logged in the daily task list.

### Project risks (summary; full register in 08)
1. The daily job skips a day, which breaks the consecutive history and moves M4 and M6.
2. A source errors partway through a run, giving a partial snapshot.
3. A change in the x.ai page layout breaks the marketplace parse.

### Charter acceptance
| Name | Title | Signature / date |
|---|---|---|
| Rob Domaine | Sponsor; Inventor and Publisher, Omnipotent Media LLC | ________ (pending) |
| Jenny Echo | Project Manager | prepared Oct 22, 2026 |

### Project stakeholders
| Function | Name | Role |
|---|---|---|
| Sponsor / customer | Rob Domaine | Approves; accepts or rejects deliverables; holds the submission decision |
| Project manager and builder | Jenny Echo | Plans, builds, runs checks, reports |
| Data providers (external) | MCP Registry maintainers; GitHub; xAI (x.ai marketplace) | Their public APIs/pages; their terms limit our approach |
| Future users (external) | Plugin publishers and readers of the digest | Need accurate, sourced numbers |
| Marketplace reviewer (external, later) | xAI | Reviews only if Rob submits |

## 2. Scope statement additions (Ch 9 pp. 78-81, 90-91)

### Requirements, by Watt's six categories
| ID | Category | Requirement (measurable) |
|---|---|---|
| R1 | Functional | Digest ranks "Rising" when snapshots span 7 or more days |
| R2 | Functional | A repo with no snapshot 7 days back is listed as "new: no 7-day baseline" and is never printed as "+None" |
| R3 | Non-functional (performance) | Each run makes 50 or fewer GitHub requests (10 repos x 2 = 20 now) |
| R4 | Non-functional (development: time) | v1.1.0 tagged by 6:00 PM ET on Oct 27 |
| R5 | Technical | Python 3.13 with the existing requests/protego pins; no new dependencies |
| R6 | Business | Tracks all 8 Rob plugins, so the digest reports on his portfolio |
| R7 | User | Every number in the digest names its source and its ET capture time (kept from v1.0) |
| R8 | Regulatory/terms | robots.txt honored and contact header sent; complies with Cursor Marketplace Publisher Terms (May 6, 2026); public data only |
| R9 | Non-functional (quality) | `tests/check_frontmatter.py` ALL PASS; README matches the code's rule |

Non-goals: the "Not included" list above. Recorded reason for one exclusion (Watt p. 81, "why" decisions): a registry page cap above 20 is excluded because it adds requests and run time for a figure that stays a sample anyway.

Acceptance criteria (sponsor sign-off): R1-R9 verified in the closeout note, each with evidence (file, command, output).

## 3. Work breakdown structure (deliverable-oriented; no sequence implied)
Numbering is the code of accounts. **Bold** rows are work packages (lowest level), each with one owner and an estimate. Estimates are active effort, not elapsed time.

- **0.0 PluginPulse v1.1**
  - 1.0 Project management
    - **1.1 Charter and plan documents** (Echo, 1.0 h, done Oct 22)
    - **1.2 Sponsor approval of charter** (Rob, 0.1 h)
    - **1.3 Status reporting per communication plan** (Echo, 0.5 h total)
  - 2.0 Seven-day snapshot history
    - **2.1 Daily snapshot runs Oct 23-27** (job, automatic; 0 h active)
    - **2.2 Daily morning verification Oct 23-27** (Echo, 5 x 0.1 h)
    - **2.3 Catch-up run if a day is missing (contingency)** (Echo, 0.2 h, only if triggered)
  - 3.0 Code fixes (released as v1.0.5)
    - **3.1 Per-repo Rising baseline fix (R2)** (Echo, 0.5 h)
    - **3.2 Add inplug-plugin and lingolink to repos.txt (R6)** (Echo, 0.1 h)
    - **3.3 README history rule matches code (R9)** (Echo, 0.2 h)
    - **3.4 Tests: front-matter check plus a digest test on copied snapshots** (Echo, 0.3 h)
  - 4.0 First ranked digest
    - **4.1 Generate digest from the 8 snapshots** (Echo, 0.1 h)
    - **4.2 Review digest against R1, R2 and R7; publish to examples/** (Echo, 0.2 h)
  - 5.0 v1.1.0 release
    - **5.1 CHANGELOG, version bump, TRANSLATIONS note** (Echo, 0.2 h)
    - **5.2 Tag v1.1.0 and push (forward only)** (Echo, 0.1 h)
  - 6.0 Closure
    - **6.1 Closeout note: R1-R9 with evidence, lessons learned** (Echo, 0.3 h)
    - **6.2 Sponsor acceptance and list updates** (Rob 0.1 h, Echo 0.1 h)

100 percent rule check: 1.0-6.0 cover every included scope item (scope items 1 to 2.1-2.3, 2 to 3.1, 3 to 3.2, 4 to 3.3, 5 to 4.0, 6 to 5.0) plus the PM and closure work. Submission and translation review sit outside the WBS by design (non-goals). Total active effort is about 4.3 h for Echo (contingency 2.3 included), plus about 0.2 h for Rob.
