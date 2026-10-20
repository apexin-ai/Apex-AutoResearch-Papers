import json, os, glob

DIR = "/root/symb_invariant_consensus/results/direction_d_cegis"
files = sorted(glob.glob(os.path.join(DIR, "folio_*.json")), key=lambda f: int(os.path.basename(f).split("_")[1].split(".")[0]))

results = []
for f in files:
    with open(f) as fh:
        data = json.load(fh)
    r = data.get("result", {})
    results.append(r)

n = len(results)
sc_correct = sum(1 for r in results if r.get("sc_correct"))
r1_correct = sum(1 for r in results if r.get("r1_correct"))
r2_correct = sum(1 for r in results if r.get("r2_correct"))
r3_correct = sum(1 for r in results if r.get("r3_correct"))

sc_acc = sc_correct / n
r1_acc = r1_correct / n
r2_acc = r2_correct / n
r3_acc = r3_correct / n

summary = {
    "n_problems": n,
    "sc_accuracy": round(sc_acc, 4),
    "sc_correct": sc_correct,
    "r1_accuracy": round(r1_acc, 4),
    "r1_correct": r1_correct,
    "r1_delta_pp": round((r1_acc - sc_acc) * 100, 2),
    "r2_accuracy": round(r2_acc, 4),
    "r2_correct": r2_correct,
    "r2_delta_pp": round((r2_acc - sc_acc) * 100, 2),
    "r3_accuracy": round(r3_acc, 4),
    "r3_correct": r3_correct,
    "r3_delta_pp": round((r3_acc - sc_acc) * 100, 2),
}

print(json.dumps(summary, indent=2))

with open(os.path.join(DIR, "aggregated_results.json"), "w") as f:
    json.dump({"summary": summary, "results": results}, f, indent=2)
print(f"\nSaved to {DIR}/aggregated_results.json")
