"""Gemma-2-9B-it ScienceWorld counterfactual DAF analysis.

Computes per-task and aggregate death rates, label distributions, DAF,
and bootstrap 95% CIs. Outputs table, JSON, and LaTeX.
"""

import json
import os
import sys
from collections import defaultdict

import numpy as np

DEATH_THRESHOLD = -100
BOOTSTRAP_B = 10000
SEED = 42

INCLUDED_TASKS = [
    "identify-life-stages-1",
    "identify-life-stages-2",
    "freeze",
    "grow-fruit",
    "measure-melting-point-unknown-substance",
    "lifespan-longest-lived",
    "lifespan-longest-lived-then-shortest-lived",
    "chemistry-mix",
    "inclined-plane-determine-angle",
    "find-animal",
    "find-non-living-thing",
]

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "results", "gemma_scienceworld_counterfactual")


def load_all_episodes():
    by_task = {}
    for task in INCLUDED_TASKS:
        fpath = os.path.join(BASE_DIR, task, "episodes.jsonl")
        if not os.path.exists(fpath):
            print(f"WARNING: {task} — episodes.jsonl not found, skipping")
            continue
        eps = []
        for line in open(fpath):
            ep = json.loads(line)
            if "always_internal" not in ep or "always_deterministic" not in ep:
                continue
            int_score = ep["always_internal"]["final_score"]
            det_score = ep["always_deterministic"]["final_score"]
            int_dead = int_score <= DEATH_THRESHOLD
            det_dead = det_score <= DEATH_THRESHOLD
            if det_score > int_score:
                label = "det-preferred"
            elif int_score > det_score:
                label = "int-preferred"
            else:
                label = "no-preference"
            eps.append({
                "task": task,
                "int_score": int_score,
                "det_score": det_score,
                "int_dead": int_dead,
                "det_dead": det_dead,
                "label": label,
            })
        by_task[task] = eps
    return by_task


def analyze_task(eps):
    n = len(eps)
    if n == 0:
        return None
    int_scores = np.array([e["int_score"] for e in eps])
    det_scores = np.array([e["det_score"] for e in eps])
    int_dead = np.array([e["int_dead"] for e in eps])
    det_dead = np.array([e["det_dead"] for e in eps])

    int_dr = int_dead.mean()
    det_dr = det_dead.mean()
    delta_dr = int_dr - det_dr

    labels = [e["label"] for e in eps]
    d_count = labels.count("det-preferred")
    i_count = labels.count("int-preferred")
    n_count = labels.count("no-preference")

    return {
        "n": n,
        "int_dr": float(int_dr),
        "det_dr": float(det_dr),
        "delta_dr": float(delta_dr),
        "det_pref": d_count,
        "int_pref": i_count,
        "no_pref": n_count,
        "mean_int_score": float(int_scores.mean()),
        "mean_det_score": float(det_scores.mean()),
    }


def bootstrap_aggregate(all_eps, B=BOOTSTRAP_B, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(all_eps)
    int_scores = np.array([e["int_score"] for e in all_eps])
    det_scores = np.array([e["det_score"] for e in all_eps])
    int_dead = (int_scores <= DEATH_THRESHOLD).astype(np.float64)
    det_dead = (det_scores <= DEATH_THRESHOLD).astype(np.float64)

    int_dr = int_dead.mean()
    det_dr = det_dead.mean()
    delta_dr = int_dr - det_dr

    both_alive = (~(int_scores <= DEATH_THRESHOLD)) & (~(det_scores <= DEATH_THRESHOLD))
    delta_full = det_scores.mean() - int_scores.mean()
    if both_alive.sum() > 0:
        delta_nd = det_scores[both_alive].mean() - int_scores[both_alive].mean()
    else:
        delta_nd = 0.0
    daf = 1.0 - delta_nd / delta_full if delta_full != 0 else float("nan")

    idx = rng.randint(0, n, size=(B, n))
    b_int_dead = int_dead[idx]
    b_det_dead = det_dead[idx]
    b_int_dr = b_int_dead.mean(axis=1)
    b_det_dr = b_det_dead.mean(axis=1)
    b_delta_dr = b_int_dr - b_det_dr

    b_int_scores = int_scores[idx]
    b_det_scores = det_scores[idx]
    b_both_alive = (~(b_int_scores <= DEATH_THRESHOLD)) & (~(b_det_scores <= DEATH_THRESHOLD))
    b_delta_full = b_det_scores.mean(axis=1) - b_int_scores.mean(axis=1)

    b_daf = np.full(B, np.nan)
    for i in range(B):
        mask = b_both_alive[i]
        if mask.sum() > 0 and b_delta_full[i] != 0:
            d_nd = b_det_scores[i][mask].mean() - b_int_scores[i][mask].mean()
            b_daf[i] = 1.0 - d_nd / b_delta_full[i]

    valid_daf = b_daf[~np.isnan(b_daf)]

    def ci(arr):
        return (float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5)))

    return {
        "n_episodes": n,
        "int_dr": {"point": float(int_dr), "ci": ci(b_int_dr)},
        "det_dr": {"point": float(det_dr), "ci": ci(b_det_dr)},
        "delta_dr": {"point": float(delta_dr), "ci": ci(b_delta_dr)},
        "delta_full": float(delta_full),
        "delta_nd": float(delta_nd),
        "daf": {
            "point": float(daf),
            "ci": ci(valid_daf) if len(valid_daf) > 0 else (float("nan"), float("nan")),
            "n_valid_bootstrap": int(len(valid_daf)),
        },
    }


def fmt_pct(val):
    return f"{val*100:.1f}%"


def fmt_ci(point, ci):
    return f"{point*100:.1f}% [{ci[0]*100:.1f}, {ci[1]*100:.1f}]"


def fmt_pp(point, ci):
    sign = "+" if point >= 0 else ""
    return f"{sign}{point*100:.1f}pp [{ci[0]*100:.1f}, {ci[1]*100:.1f}]"


def main():
    by_task = load_all_episodes()
    if not by_task:
        print("ERROR: No episodes found. Check BASE_DIR.")
        sys.exit(1)

    all_eps = []
    for eps in by_task.values():
        all_eps.extend(eps)

    task_results = {}
    print("=" * 120)
    print("GEMMA-2-9B-IT ScienceWorld Counterfactual — Per-Task Results")
    print("=" * 120)
    header = f"{'Task':<45} {'N':>3} {'Int DR':>7} {'Det DR':>7} {'ΔDR':>8} {'D':>3} {'I':>3} {'N':>3} {'Det%':>6}"
    print(header)
    print("-" * 120)

    has_death_tasks = []
    for task in INCLUDED_TASKS:
        if task not in by_task:
            print(f"{task:<45} {'—':>3} {'MISSING':>7}")
            continue
        eps = by_task[task]
        r = analyze_task(eps)
        task_results[task] = r

        flag = " *" if r["n"] < 20 else ""
        det_pct = r["det_pref"] / (r["det_pref"] + r["int_pref"]) * 100 if (r["det_pref"] + r["int_pref"]) > 0 else 0
        print(f"{task:<45} {r['n']:>3} {fmt_pct(r['int_dr']):>7} {fmt_pct(r['det_dr']):>7} "
              f"{'+' if r['delta_dr']>=0 else ''}{r['delta_dr']*100:.1f}pp  "
              f"{r['det_pref']:>3} {r['int_pref']:>3} {r['no_pref']:>3} {det_pct:>5.1f}%{flag}")

        if r["int_dr"] > 0 or r["det_dr"] > 0:
            has_death_tasks.append(task)

    # Aggregate
    print("\n" + "=" * 120)
    print("AGGREGATE (all tasks pooled)")
    print("=" * 120)

    total_d = sum(r["det_pref"] for r in task_results.values())
    total_i = sum(r["int_pref"] for r in task_results.values())
    total_n = sum(r["no_pref"] for r in task_results.values())
    total_all = total_d + total_i + total_n

    print(f"Total episodes: {total_all}")
    print(f"Tasks loaded: {len(task_results)}/{len(INCLUDED_TASKS)}")
    if len(task_results) < len(INCLUDED_TASKS):
        missing = [t for t in INCLUDED_TASKS if t not in task_results]
        print(f"MISSING TASKS: {missing}")

    print(f"\nLabel distribution:")
    print(f"  det-preferred:  {total_d:>4} ({total_d/total_all*100:.1f}%)")
    print(f"  int-preferred:  {total_i:>4} ({total_i/total_all*100:.1f}%)")
    print(f"  no-preference:  {total_n:>4} ({total_n/total_all*100:.1f}%)")

    # Bootstrap
    print("\nBootstrap 95% CIs (B=10000, seed=42):")
    agg = bootstrap_aggregate(all_eps)
    print(f"  Internal DR:  {fmt_ci(agg['int_dr']['point'], agg['int_dr']['ci'])}")
    print(f"  Det DR:       {fmt_ci(agg['det_dr']['point'], agg['det_dr']['ci'])}")
    print(f"  ΔDR:          {fmt_pp(agg['delta_dr']['point'], agg['delta_dr']['ci'])}")
    print(f"  Δ_full:       {agg['delta_full']:.4f}")
    print(f"  Δ_nd:         {agg['delta_nd']:.4f}")
    print(f"  DAF:          {fmt_ci(agg['daf']['point'], agg['daf']['ci'])}")

    # Direction consistency
    det_dominant_count = 0
    for task in has_death_tasks:
        r = task_results[task]
        non_tie = r["det_pref"] + r["int_pref"]
        if non_tie > 0 and r["det_pref"] > r["int_pref"]:
            det_dominant_count += 1
    if has_death_tasks:
        dir_consistency = det_dominant_count / len(has_death_tasks) * 100
        print(f"\nDirection consistency (death tasks with det-dominant non-tie labels): "
              f"{det_dominant_count}/{len(has_death_tasks)} = {dir_consistency:.1f}%")

    # Cross-model comparison
    print("\n" + "=" * 120)
    print("CROSS-MODEL COMPARISON")
    print("=" * 120)
    print(f"{'Model':<20} {'DAF':>12} {'Int DR':>10} {'Det DR':>10} {'ΔDR':>10}")
    print("-" * 70)
    print(f"{'Qwen2.5-7B':<20} {'90.4%':>12} {'—':>10} {'—':>10} {'—':>10}")
    print(f"{'Llama-3.1-8B':<20} {'88.2%':>12} {'—':>10} {'—':>10} {'—':>10}")
    print(f"{'Gemma-2-9B-it':<20} {fmt_pct(agg['daf']['point']):>12} "
          f"{fmt_pct(agg['int_dr']['point']):>10} "
          f"{fmt_pct(agg['det_dr']['point']):>10} "
          f"{'+' if agg['delta_dr']['point']>=0 else ''}{agg['delta_dr']['point']*100:.1f}pp")

    # Build full output dict
    output = {
        "model": "gemma-2-9b-it",
        "data_dir": BASE_DIR,
        "included_tasks": INCLUDED_TASKS,
        "tasks_found": list(task_results.keys()),
        "tasks_missing": [t for t in INCLUDED_TASKS if t not in task_results],
        "per_task": task_results,
        "aggregate": {
            "n_episodes": agg["n_episodes"],
            "n_tasks": len(task_results),
            "label_distribution": {
                "det_preferred": total_d,
                "int_preferred": total_i,
                "no_preference": total_n,
                "det_preferred_pct": round(total_d / total_all * 100, 1),
                "int_preferred_pct": round(total_i / total_all * 100, 1),
                "no_preference_pct": round(total_n / total_all * 100, 1),
            },
            "int_dr": agg["int_dr"],
            "det_dr": agg["det_dr"],
            "delta_dr": agg["delta_dr"],
            "delta_full": agg["delta_full"],
            "delta_nd": agg["delta_nd"],
            "daf": agg["daf"],
            "direction_consistency": {
                "death_tasks": len(has_death_tasks),
                "det_dominant": det_dominant_count,
                "pct": round(dir_consistency, 1) if has_death_tasks else None,
            },
        },
        "cross_model": {
            "qwen_daf": 0.904,
            "llama_daf": 0.882,
            "gemma_daf": agg["daf"]["point"],
        },
    }

    # JSON
    json_path = os.path.join(BASE_DIR, "analysis.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved to {json_path}")

    # LaTeX table
    tex_path = os.path.join(BASE_DIR, "latex_table.tex")
    with open(tex_path, "w") as f:
        f.write("% Gemma-2-9B-it ScienceWorld counterfactual per-task results\n")
        f.write("\\begin{tabular}{lrrrrrrrr}\n")
        f.write("\\toprule\n")
        f.write("Task & $N$ & Int DR & Det DR & $\\Delta$DR & D & I & N & Det\\% \\\\\n")
        f.write("\\midrule\n")
        for task in INCLUDED_TASKS:
            if task not in task_results:
                f.write(f"{task} & \\multicolumn{{7}}{{c}}{{missing}} \\\\\n")
                continue
            r = task_results[task]
            det_pct = r["det_pref"] / (r["det_pref"] + r["int_pref"]) * 100 if (r["det_pref"] + r["int_pref"]) > 0 else 0
            short = task.replace("identify-life-stages", "ILS").replace("lifespan-longest-lived-then-shortest-lived", "LL→SL").replace("lifespan-longest-lived", "LL").replace("measure-melting-point-unknown-substance", "melt-pt").replace("inclined-plane-determine-angle", "incline").replace("chemistry-mix", "chem-mix").replace("find-non-living-thing", "find-NL").replace("find-animal", "find-anim").replace("grow-fruit", "grow")
            f.write(f"{short} & {r['n']} & {r['int_dr']*100:.0f}\\% & {r['det_dr']*100:.0f}\\% & "
                    f"{'+' if r['delta_dr']>=0 else ''}{r['delta_dr']*100:.0f} & "
                    f"{r['det_pref']} & {r['int_pref']} & {r['no_pref']} & {det_pct:.0f}\\% \\\\\n")
        f.write("\\midrule\n")
        idr = agg["int_dr"]
        ddr = agg["det_dr"]
        dlt = agg["delta_dr"]
        daf = agg["daf"]
        f.write(f"\\textbf{{Aggregate}} & {agg['n_episodes']} & "
                f"{idr['point']*100:.1f}\\% & {ddr['point']*100:.1f}\\% & "
                f"{'+' if dlt['point']>=0 else ''}{dlt['point']*100:.1f} & "
                f"{total_d} & {total_i} & {total_n} & "
                f"{total_d/(total_d+total_i)*100:.0f}\\% \\\\\n")
        f.write("\\midrule\n")
        f.write(f"\\multicolumn{{9}}{{l}}{{DAF = {daf['point']*100:.1f}\\% "
                f"[{daf['ci'][0]*100:.1f}, {daf['ci'][1]*100:.1f}]}} \\\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
    print(f"LaTeX saved to {tex_path}")


if __name__ == "__main__":
    main()
