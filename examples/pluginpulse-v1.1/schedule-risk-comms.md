# PluginPulse v1.1 — Schedule, Risk Plan, Communication Plan (FINAL)
Built per Watt Ch 10 (pp. 93-105), Ch 11 estimating (p. 108), Ch 16 (pp. 181-191), Ch 15 (pp. 175-180). Calculations: `schedule_cpm.py` (the same method as `scripts/planpilot_cpm.py`; it computes ES/EF/LS/LF. Those forward/backward-pass columns are a general CPM technique, **not** taught in Watt Ch 10, which identifies the critical path by tracing path lengths. I used both and they agree).

## A. Schedule

### A1. Activity list with attributes (Watt p. 96: predecessors, successors, constraints)
| Act | WBS | Activity | Duration (elapsed) | Estimating tool (Ch 11) | Predecessor (type) | Constraint |
|---|---|---|---|---|---|---|
| A | 1.1 | Write plan documents | 13 h (done Oct 22) | actual | — | — |
| B | 1.2 | Rob approves charter | 21 h | expert judgment (Rob's usual reply time); includes a reserve | A (FS, **discretionary**: Rob's standing OK would allow C without it) | Rob's availability |
| C | 3.1-3.4 | Code fixes + tests → v1.0.5 | 2 h | analogous (Oct 21-22 fixes took 2-10 min of work each; padded) | B (FS, discretionary) | Do on Oct 23 even though float is large (see A4) |
| D | 2.1 | Daily snapshots, Oct 23-27 | 130 h (to Oct 27 ~10 AM) | fixed by calendar | **external** predecessor: calendar days and the data sources | One run per day after 9:00 AM ET |
| E | 2.2 | Morning verification each day | 130 h, 5 × 6 min effort | analogous | D (**SS**, lag ~10 min after each run) | — |
| F | 4.1 | Generate digest | 2 h | three-point (O 0.1 h, M 0.25 h, P 2 h if a re-run is needed) → buffer 2 h | D, C (FS, **mandatory**: needs the 8th snapshot) | — |
| G | 4.2 | Review digest against R1, R2, R7; publish example | 2 h | expert judgment | F (FS, mandatory) | — |
| H | 5.1 | CHANGELOG, version 1.1.0, TRANSLATIONS note | 2 h | analogous | G (FS) | — |
| I | 5.2 | Tag v1.1.0 and push (forward only) | 2 h | analogous | H (FS, mandatory) | **Deadline Oct 27, 6:00 PM ET** |
| J | 6.1 | Closeout note (R1-R9 evidence, lessons) | 2 h | analogous | I (FS) | — |
| K | 6.2 | Sponsor acceptance + list updates | 24 h | expert judgment + reserve analysis | J (FS) | Rob's availability |

Leads/lags (p. 98): E lags each daily run by ~10 minutes (lag). No leads.

### A2. Network (activity-on-node, precedence diagramming method)
```
 [A]→[B]→[C]──────────────┐
                          ▼
 [D] Snapshots Oct 23-27 ─►[F]→[G]→[H]→[I]→[J]→[K]
 [E] (SS with D)
```

### A3. Critical path
Critical path **D-F-G-H-I-J-K = 164 h** (hour 0 = Oct 22, 12:00 AM ET). It is the longest path through the network and the minimum time to finish (p. 104). The other path, A-B-C-F-…-K, is 34 + 2 + 34 = 70 h, so it is not critical. Key dates from `schedule_cpm.out`:
- B charter approved: Fri Oct 23, 10:00 AM ET
- C v1.0.5 pushed: Fri Oct 23, 12:00 PM ET
- D 8th snapshot: Tue Oct 27, ~10:00 AM ET
- F digest: Tue Oct 27, 12:00 PM ET
- I **v1.1.0 tagged: Tue Oct 27, 6:00 PM ET** (meets the objective deadline with 0 h float)
- K sponsor acceptance: Wed Oct 28, 8:00 PM ET

### A4. Float and slack (Watt's distinction, p. 101)
- **Float** (could end later): C could end up to 94 h later without delaying the finish. This float is misleading in practice. Repos added late get less history, so C is scheduled for Oct 23 by choice (a discretionary decision).
- **Slack** (could start earlier): none useful. D cannot start before Oct 23 because of the calendar.
- Because I has **zero float** against the Oct 27 deadline, any skipped snapshot day pushes v1.1.0 back a full day. Risk R-01 targets this.

### A5. Gantt chart (each character = 6 h; `=` work, `.` float; milestones shown with ▲ per Watt's "diamond or triangle", review □)
```
Oct:                  22   23   24   25   26   27   28
A 1.1 Plan docs       ==
B 1.2 Charter OK        ====          ▲M1 (Oct 23 10 AM)
C 3.x Fixes v1.0.5          =  ▲M2 (Oct 23 noon) ......(float)
D 2.1 Snapshots         ======================  ▲M3 Oct 23 run ... ▲M4 Oct 27
E 2.2 Verification      ======================  □ daily review
F-G 4.x Digest                                 ==  ▲M5
H-I 5.x Release                                 ==  ▲M6 Oct 27 6 PM
J-K 6.x Closure                                  ====
```
Milestone list (p. 99; R = required for success):
- M1 charter OK (R)
- M2 v1.0.5 (R)
- M3 first unattended run after the fix (not required; it is a signal)
- M4 8th snapshot (R)
- M5 digest reviewed (R)
- M6 v1.1.0 (R)

Scope changes found while scheduling go through change control: a written note to Rob, with approval recorded in the daily list (the limo example, p. 100).

## B. Risk management plan

### B1. How risk is managed
- **Identification:** brainstorming plus Watt's category checklist (technical, cost, schedule, client, contractual, weather, financial, political, environmental, people), organized as an RBS on the WBS.
- **Evaluation:** likelihood and impact rated **High/Medium/Low**. Every risk rated **High on both** gets a mitigation plan, and every Medium-or-higher schedule risk gets a contingency plan.
- **Mitigation coding** (Watt p. 186-190): RA avoidance, RS sharing, RR reduction, RT transfer. When none applies, the risk is **accepted** (one of the four basic ways, p. 182).
- **Review:** at each morning check. Closed risks are checked off as activities finish (implementation phase, p. 190). Closeout table at the end (p. 191).
- **Who:** Jenny Echo owns all risks except R-07, which Rob owns. Cost risk is low ($0 cash), so the reserve is time: about 24 h in B and K (reserve analysis, Ch 11).

### B2. Risk breakdown structure (RBS) and register
The term "risk register" appears in Watt's App 2 exercise. Its columns follow Watt's RBS/mitigation tables plus an ID and owner.

| ID | WBS | Category | Risk (event or condition) | Likelihood | Impact | Response (code) | Contingency plan | Owner |
|---|---|---|---|---|---|---|---|---|
| R-01 | 2.1 | Schedule / technical | The daily job misses a day (the box was paused or restarted, or the timer went stale), breaking the 8-day run. It happened Oct 21 and Oct 22. | **High** (2 of 2 recent days needed catch-ups) | **High** (zero float; v1.1.0 slips a day) | **RR**: since Oct 22 the job wakes every 10 min and runs if today's file is missing (v1.0.4 job); morning check by ~9:30 AM ET | Same-day manual catch-up (WBS 2.3). If a whole day is lost, rebaseline M4/M6 by +1 day and tell Rob that day | Echo |
| R-02 | 2.1 | Technical (external) | A source errors partway through a run (registry HTTP 500, as on Oct 22) | Medium | Medium (snapshot partial) | **RR**: v1.0.4 keeps pages already read and flags "partial"; one polite retry on 5xx | Manual retry once the same morning (as on Oct 22, 9:38 AM) | Echo |
| R-03 | 2.1 | Technical (external) | The x.ai marketplace page layout changes, so the listings parse returns 0 | Low | Medium | Accept (we can't control xAI's page) | Record "not captured" in the snapshot; the digest still runs on the registry and GitHub | Echo |
| R-04 | 2.1 | Technical / contractual | GitHub's unauthenticated limit is hit (60/hour) | Low (20 of the 50 budgeted per run) | Medium | **RA**: GH_BUDGET = 50 in code; one run per day | Skip the GitHub section that day and retry later | Echo |
| R-05 | 3.1 | Technical | The baseline fix breaks Rising for existing repos | Low | High (wrong numbers in the first digest) | **RR**: test on copies of the real snapshots first (00-evidence method), plus a negative control | Revert to v1.0.4 logic and publish without the new repos | Echo |
| R-06 | 4.2 | Client / quality | The digest overclaims (registry "2,000" read as a total; star growth read as popularity) | Medium | Medium | **RA**: keep the "partial: page limit reached" wording; review against R7 | Correct before tagging | Echo |
| R-07 | 1.2, 6.2 | People | Rob is unavailable to approve the charter or accept the release | Medium | Low (C is covered by his standing OK; K has a 24 h reserve) | Accept; ask early (comms plan C1) | Proceed with C under the standing OK; hold the release note for him | Rob |
| R-08 | 2.1 | Environmental (infrastructure) | The box is down for a whole day | Low | High | Accept (no avoidance, sharing, reduction or transfer is available on a single free box) | Rebaseline +1 day; data history restarts only if a day is unrecoverable | Echo |
| O-01 | 4.1 | Opportunity | Star movement on Rob's repos (all at 0 stars on Oct 22) makes the first digest newsworthy | Low | Medium (positive) | Handled like a risk (p. 181): watch, and if it happens, tell Rob the same day | — | Echo |

Mitigation plan required (High/High): **R-01 only**. Its plan is the v1.0.4 10-minute job plus the morning check. R-05 and R-08 are High-impact but Low-likelihood, so each has a contingency plan.

### B3. Risk by phase
- **Initiation:** the main risk was the wrong history rule (Oct 26 vs Oct 27). It was found and fixed in the plan.
- **Planning:** the RBS above.
- **Implementation:** check risks off daily. R-01 to R-04 close after the Oct 27 run.
- **Closeout:** see the table below.

| Risk | Mitigation | Closeout check |
|---|---|---|
| R-01 | 10-minute job + morning check | 8 files Oct 20-27 present; log shows how each ran |
| R-05 | test on copies | the first real digest has no "+None" and existing repos are ranked |
| R-06 | wording review | digest still says "partial: page limit reached" |

## C. Communication plan

### C0. Communications requirements analysis (p. 175)
Rob needs to:
- (a) approve the charter
- (b) know at once if the history slips, since that moves the release date
- (c) receive the release and decide on submission

Rob does **not** need the daily "all OK" detail, which goes to the lists only. Bad news goes out the same day, not saved for later ("not always a rosy picture"). All times are in **Eastern Time** (Rob works only in ET); there is no other time zone in this project.

### C1. Plan (Watt's 7-step template, p. 179)
| To whom | Why (expectation) | What | When / frequency | How (preferred method) | Who sends | Template / document |
|---|---|---|---|---|---|---|
| Rob (sponsor) | Approve the plan | Charter summary + request for OK | Oct 22 (once) | Chat message (asynchronous) | Echo, via the parent assistant | Short memo (Course 4 format) |
| Rob | Know about slips at once | Missed day, new M4/M6 dates | Same morning a risk triggers | Chat; voice if he's on a call (synchronous) | Echo | Bad-news pattern: context, news, new date, next step |
| Rob | Track progress without detail | Snapshot count (n of 8) | Once a day after the check | Daily task list entry (asynchronous, pull) | Echo | Daily task list line |
| Rob | Decide on release and submission | v1.1.0 link, digest link, R1-R9 evidence | Oct 27 after M6 | Chat + closeout note | Echo | Closeout note (6.1) |
| Lists (Notion To Do List, Education, Master Index; local marketplace-plugins.md) | Single source of truth (immediate-update rule) | Status changes | At each milestone | Notion pages + local file | Echo | Existing list formats |
| Public (GitHub readers) | Accurate release notes | CHANGELOG, README rule | At v1.0.5 and v1.1.0 | GitHub (asynchronous) | Echo | CHANGELOG format |

Technology check (p. 179):
- Every channel is already in use, so no new tool, training or cost is needed.
- No messages go out without Rob's say-so. The plan proposes them, and the parent assistant sends them only with Rob's approval.
