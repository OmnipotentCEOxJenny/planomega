#!/usr/bin/env python3
"""PlanPilot schedule helper (standard library only).
Usage: python3 scripts/planpilot_cpm.py PLAN.json
PLAN.json = {"unit": "hours", "tasks": {"A": {"name": "...", "duration": 3, "after": []}, ...},
             "risks": [{"risk": "...", "probability": "H|M|L", "impact": "H|M|L", "response": "..."}]}
Prints the critical-path table (earliest/latest start and finish, float), the critical path(s),
a text Gantt chart, and the risk list sorted by rating, flagging High/High risks that lack a response.
Method: critical path method (forward and backward pass). Exit 1 if the plan has a loop or a missing task."""
import json, sys
"""Critical Path Method: forward/backward pass, total & free float, critical path(s). Reusable for PM Ch10.
Usage as module: cpm(tasks) where tasks = {id: (duration, [predecessors]), ...}"""
def cpm(tasks):
    order=[]; seen=set()
    def visit(t):
        if t in seen: return
        for p in tasks[t][1]: visit(p)
        seen.add(t); order.append(t)
    for t in tasks: visit(t)
    ES,EF={},{}
    for t in order:
        ES[t]=max([EF[p] for p in tasks[t][1]],default=0); EF[t]=ES[t]+tasks[t][0]
    end=max(EF.values()); succ={t:[s for s in tasks if t in tasks[s][1]] for t in tasks}
    LS,LF={},{}
    for t in reversed(order):
        LF[t]=min([LS[s] for s in succ[t]],default=end); LS[t]=LF[t]-tasks[t][0]
    TF={t:LS[t]-ES[t] for t in tasks}
    FF={t:min([ES[s] for s in succ[t]],default=end)-EF[t] for t in tasks}
    paths=[]
    def walk(t,p):
        p=p+[t]; nxt=[s for s in succ[t] if abs(TF[s])<1e-9 and abs(ES[s]-EF[t])<1e-9]
        if not nxt: paths.append(p)
        for s in nxt: walk(s,p)
    for t in tasks:
        if abs(TF[t])<1e-9 and not tasks[t][1]: walk(t,[])
    return dict(ES=ES,EF=EF,LS=LS,LF=LF,TF=TF,FF=FF,duration=end,critical=paths,order=order)
def table(tasks,r,names=None):
    out=f"{'Task':6}{'Dur':>4}{'ES':>5}{'EF':>5}{'LS':>5}{'LF':>5}{'TF':>5}{'FF':>5}  Name\n"
    for t in r['order']:
        out+=f"{t:6}{tasks[t][0]:>4}{r['ES'][t]:>5}{r['EF'][t]:>5}{r['LS'][t]:>5}{r['LF'][t]:>5}{r['TF'][t]:>5}{r['FF'][t]:>5}  {(names or {}).get(t,'')}{' *' if r['TF'][t]==0 else ''}\n"
    return out+f"Duration {r['duration']}; critical path(s): {[' → '.join(p) for p in r['critical']]}\n"

RANK = {"H": 3, "M": 2, "L": 1}

def load(path):
    d = json.load(open(path, encoding="utf-8"))
    tasks = {k: (v["duration"], v.get("after", [])) for k, v in d["tasks"].items()}
    for k, (_, prev) in tasks.items():
        for p in prev:
            if p not in tasks:
                raise ValueError(f"task {k} comes after unknown task {p}")
    # loop check
    state = {}
    def visit(t, stack):
        if state.get(t) == 1: raise ValueError("loop in dependencies: " + " -> ".join(stack + [t]))
        if state.get(t) == 2: return
        state[t] = 1
        for p in tasks[t][1]: visit(p, stack + [t])
        state[t] = 2
    for t in tasks: visit(t, [])
    return d, tasks

def risks(d):
    out = []
    for r in sorted(d.get("risks", []), key=lambda r: -RANK[r["probability"]] * RANK[r["impact"]]):
        flag = " <- needs a response plan" if r["probability"] == "H" and r["impact"] == "H" and not r.get("response") else ""
        out.append(f"[{r['probability']}/{r['impact']}] {r['risk']} | response: {r.get('response') or '-'}{flag}")
    return out

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    try: d, tasks = load(argv[1])
    except ValueError as e: print("ERROR:", e); return 1
    r = cpm(tasks); names = {k: v.get("name", "") for k, v in d["tasks"].items()}
    print(table(tasks, r, names))
    print("Gantt (= work, . float):")
    for t in r["order"]:
        print(f"{t:4} {names[t][:28]:28} |" + " " * int(r["ES"][t]) + "=" * int(tasks[t][0]) + "." * int(r["TF"][t]))
    if d.get("risks"):
        print("\nRisks (highest first):"); [print("-", x) for x in risks(d)]
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
