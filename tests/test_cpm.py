#!/usr/bin/env python3
"""Functional test: the schedule helper reproduces the PluginPulse v1.1 plan from Course 5
(critical path D-F-G-H-I-J-K, 164 hours), passes a hand-checkable self-test, and rejects a loop."""
import json, pathlib, subprocess, sys, tempfile
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
import planomega_cpm as pc
ok = True
T = {"A": (3, []), "B": (4, ["A"]), "C": (2, ["A"]), "D": (5, ["B", "C"])}
r = pc.cpm(T)
ok &= r["duration"] == 12 and r["TF"]["C"] == 2 and r["critical"] == [["A", "B", "D"]]
d, tasks = pc.load(root / "examples/pluginpulse-v1.1/plan.json")
r = pc.cpm(tasks)
print("PluginPulse duration:", r["duration"], "critical:", r["critical"])
ok &= r["duration"] == 164 and r["critical"] == [["D", "F", "G", "H", "I", "J", "K"]]
loop = {"tasks": {"A": {"duration": 1, "after": ["B"]}, "B": {"duration": 1, "after": ["A"]}}}
f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False); json.dump(loop, f); f.close()
p = subprocess.run([sys.executable, str(root / "scripts/planomega_cpm.py"), f.name], capture_output=True, text=True)
print("loop check:", p.stdout.strip())
ok &= p.returncode == 1 and "loop" in p.stdout
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
