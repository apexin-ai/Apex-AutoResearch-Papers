import json
import os

DEATH_THRESHOLD = -100.0
TASKS = [
    "chemistry-mix", "find-animal", "freeze", "grow-fruit",
    "identify-life-stages-1", "identify-life-stages-2",
    "inclined-plane-determine-angle", "lifespan-longest-lived",
    "lifespan-longest-lived-then-shortest-lived",
    "measure-melting-point-unknown-substance"
]

BASE = "/root/autodl-tmp/simgate-modular-routing/results"
GROUNDING_DIR = os.path.join(BASE, "grounding_prompt_ablation")
PLANC_DIR = os.path.join(BASE, "plan_c")

def is_dead(s):
    return s <= DEATH_THRESHOLD

def classify(int_s, det_s):
    int_d = is_dead(int_s)
    det_d = is_dead(det_s)
    if int_d and not det_d:
        return "det-preferred", "death_asymmetry"
    if det_d and not int_d:
        return "internal-preferred", "death_asymmetry"
    if int_d and det_d:
        return "no-preference", "both_dead"
    if det_s > int_s:
        return "det-preferred", "score_comparison"
    if int_s > det_s:
        return "internal-preferred", "score_comparison"
    return "no-preference", "tied_alive"

def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def analyze_condition(int_scores, det_scores):
    n = len(int_scores)
    assert n == len(det_scores)

    int_deaths = sum(1 for s in int_scores if is_dead(s))
    det_deaths = sum(1 for s in det_scores if is_dead(s))

    labels = {"det-preferred": 0, "internal-preferred": 0, "no-preference": 0}
    signals = {"death_asymmetry": 0, "score_comparison": 0, "both_dead": 0, "tied_alive": 0}

    both_alive_int = []
    both_alive_det = []

    for i in range(n):
        label, signal = classify(int_scores[i], det_scores[i])
        labels[label] += 1
        signals[signal] += 1
        if not is_dead(int_scores[i]) and not is_dead(det_scores[i]):
            both_alive_int.append(int_scores[i])
            both_alive_det.append(det_scores[i])

    int_mean = sum(int_scores) / n
    det_mean = sum(det_scores) / n
    delta_full = det_mean - int_mean

    if both_alive_int:
        int_mean_nd = sum(both_alive_int) / len(both_alive_int)
        det_mean_nd = sum(both_alive_det) / len(both_alive_det)
        delta_nd = det_mean_nd - int_mean_nd
    else:
        int_mean_nd = 0.0
        det_mean_nd = 0.0
        delta_nd = 0.0

    daf = 1.0 - (delta_nd / delta_full) if delta_full != 0 else None

    death_driven = signals["death_asymmetry"]
    non_death = signals["score_comparison"]
    label_frac = death_driven / (death_driven + non_death) if (death_driven + non_death) > 0 else None

    return {
        "n": n,
        "int_dr": round(int_deaths / n, 4),
        "det_dr": round(det_deaths / n, 4),
        "delta_dr": round(int_deaths / n - det_deaths / n, 4),
        "int_mean": round(int_mean, 2),
        "det_mean": round(det_mean, 2),
        "delta_full": round(delta_full, 2),
        "int_mean_nd": round(int_mean_nd, 2),
        "det_mean_nd": round(det_mean_nd, 2),
        "delta_nd": round(delta_nd, 2),
        "daf": round(daf, 4) if daf is not None else None,
        "labels": labels,
        "signals": signals,
        "label_fraction": round(label_frac, 4) if label_frac is not None else None,
        "n_both_alive": len(both_alive_int),
        "int_deaths": int_deaths,
        "det_deaths": det_deaths,
    }


results = {"baseline": {}, "grounding": {}, "per_task": []}

all_baseline_int = []
all_baseline_det = []
all_grounding_int = []
all_grounding_det = []

for task in TASKS:
    planc_path = os.path.join(PLANC_DIR, task, "episode_summary.jsonl")
    planc_data = load_jsonl(planc_path)
    planc_by_var = {r["variation"]: r for r in planc_data}

    ground_path = os.path.join(GROUNDING_DIR, task, "episode_summary.jsonl")
    ground_data = load_jsonl(ground_path)
    ground_by_var = {r["variation"]: r for r in ground_data}

    common_vars = sorted(set(planc_by_var.keys()) & set(ground_by_var.keys()))

    baseline_int = [planc_by_var[v]["internal_final"] for v in common_vars]
    baseline_det = [planc_by_var[v]["det_final"] for v in common_vars]
    grounding_int = [ground_by_var[v]["internal_final"] for v in common_vars]
    grounding_det = [planc_by_var[v]["det_final"] for v in common_vars]

    all_baseline_int.extend(baseline_int)
    all_baseline_det.extend(baseline_det)
    all_grounding_int.extend(grounding_int)
    all_grounding_det.extend(grounding_det)

    b = analyze_condition(baseline_int, baseline_det)
    g = analyze_condition(grounding_int, grounding_det)

    results["per_task"].append({
        "task": task,
        "n_episodes": len(common_vars),
        "baseline": b,
        "grounding": g,
    })

results["baseline"] = analyze_condition(all_baseline_int, all_baseline_det)
results["grounding"] = analyze_condition(all_grounding_int, all_grounding_det)

# Print
print("=" * 80)
print("AGGREGATE COMPARISON")
print("=" * 80)
for cond_name, cond_key in [("Baseline", "baseline"), ("Post-Grounding", "grounding")]:
    c = results[cond_key]
    print(f"\n--- {cond_name} (N={c['n']}) ---")
    print(f"  Internal DR:    {c['int_dr']:.1%}")
    print(f"  Det DR:         {c['det_dr']:.1%}")
    print(f"  delta_DR:       {c['delta_dr']:.1%}")
    print(f"  delta_full:     {c['delta_full']}")
    print(f"  delta_nd:       {c['delta_nd']}")
    print(f"  DAF (P=100):    {c['daf']}")
    print(f"  Label fraction: {c['label_fraction']}")
    print(f"  Labels:         {c['labels']}")
    print(f"  Signals:        {c['signals']}")

print("\n" + "=" * 80)
print("PER-TASK BREAKDOWN")
print("=" * 80)
fmt = "{:<45} {:>3} {:>8} {:>8} {:>8} {:>7} {:>7} {:>6} {:>6}"
print(fmt.format("Task", "N", "BL_IDR", "GR_IDR", "DetDR", "BL_DAF", "GR_DAF", "BL_LF", "GR_LF"))
print("-" * 100)
for t in results["per_task"]:
    b = t["baseline"]
    g = t["grounding"]
    bl_daf = f"{b['daf']:.3f}" if b['daf'] is not None else "N/A"
    gr_daf = f"{g['daf']:.3f}" if g['daf'] is not None else "N/A"
    bl_lf = f"{b['label_fraction']:.3f}" if b['label_fraction'] is not None else "N/A"
    gr_lf = f"{g['label_fraction']:.3f}" if g['label_fraction'] is not None else "N/A"
    print(fmt.format(
        t["task"], t["n_episodes"],
        f"{b['int_dr']:.0%}", f"{g['int_dr']:.0%}", f"{b['det_dr']:.0%}",
        bl_daf, gr_daf, bl_lf, gr_lf
    ))

out_path = os.path.join(BASE, "grounding_decomposition_analysis.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to: {out_path}")
