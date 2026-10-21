"""D064 corrected tiebreaking re-evaluation for exp052 (seed123) and exp053 (seed456)."""
import json
import statistics

def deterministic_vote(dist):
    """Pick answer with highest value, tiebreak alphabetically (sorted first key)."""
    if not dist:
        return ""
    return max(sorted(dist.keys()), key=lambda k: dist[k])

EXPERIMENTS = [
    {"seed": 123, "path": "/root/symb_invariant_consensus/results/exp052_mistral_folio204_seed123/exp052_results.json"},
    {"seed": 456, "path": "/root/symb_invariant_consensus/results/exp053_mistral_folio204_seed456/exp053_results.json"},
]

SEED789 = {"sc": 59.31, "sica": 56.86, "delta": -2.45, "sc_n": 121, "sica_n": 116}

all_seeds = []

for exp in EXPERIMENTS:
    with open(exp["path"]) as f:
        data = json.load(f)

    results = data["results"]
    n = len(results)
    assert n == 204, f"seed {exp['seed']}: expected 204 problems, got {n}"

    sc_correct = 0
    sica_correct = 0
    sc_changed = []
    sica_changed = []

    for r in results:
        gt = r["ground_truth"]

        # SC with corrected tiebreaking
        new_sc = deterministic_vote(r["sc_vote_distribution"])
        old_sc = r["sc_answer"]
        sc_ok = (new_sc == gt)
        if sc_ok:
            sc_correct += 1
        if new_sc != old_sc:
            sc_changed.append({"id": r["problem_id"], "old": old_sc, "new": new_sc, "gt": gt,
                               "votes": r["sc_vote_distribution"]})

        # SICA with corrected tiebreaking
        new_sica = deterministic_vote(r["sica_scores"])
        old_sica = r["sica_answer"]
        sica_ok = (new_sica == gt)
        if sica_ok:
            sica_correct += 1
        if new_sica != old_sica:
            sica_changed.append({"id": r["problem_id"], "old": old_sica, "new": new_sica, "gt": gt,
                                 "scores": r["sica_scores"]})

    sc_pct = sc_correct / n * 100
    sica_pct = sica_correct / n * 100
    delta = sica_pct - sc_pct

    print(f"=== Seed {exp['seed']} ===")
    print(f"  SC:   {sc_correct}/{n} = {sc_pct:.2f}%")
    print(f"  SICA: {sica_correct}/{n} = {sica_pct:.2f}%")
    print(f"  Δ:    {delta:+.2f}pp")
    if sc_changed:
        print(f"  SC changed ({len(sc_changed)}):")
        for c in sc_changed:
            print(f"    {c['id']}: {c['old']} -> {c['new']} (gt={c['gt']}) votes={c['votes']}")
    if sica_changed:
        print(f"  SICA changed ({len(sica_changed)}):")
        for c in sica_changed:
            print(f"    {c['id']}: {c['old']} -> {c['new']} (gt={c['gt']}) scores={c['scores']}")
    print()

    all_seeds.append({"seed": exp["seed"], "sc": sc_pct, "sica": sica_pct, "delta": delta,
                      "sc_n": sc_correct, "sica_n": sica_correct})

# Add seed 789
all_seeds.append({"seed": 789, "sc": SEED789["sc"], "sica": SEED789["sica"], "delta": SEED789["delta"],
                  "sc_n": SEED789["sc_n"], "sica_n": SEED789["sica_n"]})

# Compute mean and SD
sc_vals = [s["sc"] for s in all_seeds]
sica_vals = [s["sica"] for s in all_seeds]
delta_vals = [s["delta"] for s in all_seeds]

sc_mean, sc_sd = statistics.mean(sc_vals), statistics.stdev(sc_vals)
sica_mean, sica_sd = statistics.mean(sica_vals), statistics.stdev(sica_vals)
delta_mean, delta_sd = statistics.mean(delta_vals), statistics.stdev(delta_vals)

print("=" * 70)
print(f"| {'Seed':>7} | {'SC (%)':>12} | {'SICA (%)':>12} | {'Δ (pp)':>12} | {'n':>3} |")
print(f"|{'-'*9}|{'-'*14}|{'-'*14}|{'-'*14}|{'-'*5}|")
for s in all_seeds:
    print(f"| {s['seed']:>7} | {s['sc']:>12.2f} | {s['sica']:>12.2f} | {s['delta']:>+12.2f} | {204:>3} |")
print(f"| {'Mean±SD':>7} | {sc_mean:.2f}±{sc_sd:.2f} | {sica_mean:.2f}±{sica_sd:.2f} | {delta_mean:+.2f}±{delta_sd:.2f} | {'—':>3} |")
print("=" * 70)
