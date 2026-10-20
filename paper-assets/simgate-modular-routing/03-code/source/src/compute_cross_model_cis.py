"""Cross-model bootstrap CI computation for ScienceWorld death rates.

Input:  --data_dir (results root), --models (comma-sep), --B (bootstrap iters)
Output: stdout table, results/cross_model_bootstrap_cis.json, results/cross_model_bootstrap_cis.tex
"""

import argparse
import glob
import json
import os
from collections import defaultdict

import numpy as np

DEATH_THRESHOLD = -100

MODEL_DIR_MAP = {
    "qwen": "plan_c",
    "llama": "llama_cross_model_full",
}

MODEL_DISPLAY = {
    "qwen": "Qwen2.5-7B",
    "llama": "Llama-3.1-8B",
}


def load_episodes(data_dir, model):
    subdir = os.path.join(data_dir, MODEL_DIR_MAP[model])
    episodes = []
    for f in sorted(glob.glob(os.path.join(subdir, "*/episodes.jsonl"))):
        task = os.path.basename(os.path.dirname(f))
        for line in open(f):
            ep = json.loads(line)
            if "always_internal" not in ep or "always_deterministic" not in ep:
                continue
            episodes.append({
                "task": task,
                "int_score": ep["always_internal"]["final_score"],
                "det_score": ep["always_deterministic"]["final_score"],
            })
    return episodes


def bootstrap_cis(episodes, B, seed=42):
    rng = np.random.RandomState(seed)
    n = len(episodes)

    int_scores = np.array([e["int_score"] for e in episodes])
    det_scores = np.array([e["det_score"] for e in episodes])
    int_dead = (int_scores <= DEATH_THRESHOLD).astype(np.float64)
    det_dead = (det_scores <= DEATH_THRESHOLD).astype(np.float64)

    # Point estimates
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

    # Bootstrap
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
        return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))

    return {
        "n_episodes": n,
        "int_dr": {"point": float(int_dr), "ci": ci(b_int_dr)},
        "det_dr": {"point": float(det_dr), "ci": ci(b_det_dr)},
        "delta_dr": {"point": float(delta_dr), "ci": ci(b_delta_dr)},
        "daf": {
            "point": float(daf),
            "ci": ci(valid_daf) if len(valid_daf) > 0 else (float("nan"), float("nan")),
            "n_valid_bootstrap": int(len(valid_daf)),
        },
    }


def bootstrap_per_task(episodes, B, seed=42):
    by_task = defaultdict(list)
    for e in episodes:
        by_task[e["task"]].append(e)
    results = {}
    for task in sorted(by_task):
        eps = by_task[task]
        n = len(eps)
        int_scores = np.array([e["int_score"] for e in eps])
        det_scores = np.array([e["det_score"] for e in eps])
        int_dead = (int_scores <= DEATH_THRESHOLD).astype(np.float64)
        det_dead = (det_scores <= DEATH_THRESHOLD).astype(np.float64)

        rng = np.random.RandomState(seed)
        idx = rng.randint(0, n, size=(B, n))
        b_int_dr = int_dead[idx].mean(axis=1)
        b_det_dr = det_dead[idx].mean(axis=1)

        def ci(arr):
            return float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))

        results[task] = {
            "n": n,
            "int_dr": {"point": float(int_dead.mean()), "ci": ci(b_int_dr)},
            "det_dr": {"point": float(det_dead.mean()), "ci": ci(b_det_dr)},
        }
    return results


def fmt_pct(point, ci_lo, ci_hi):
    return f"{point*100:.1f}% [{ci_lo*100:.1f},{ci_hi*100:.1f}]"


def fmt_pp(point, ci_lo, ci_hi):
    sign = "+" if point >= 0 else ""
    return f"{sign}{point*100:.1f} [{ci_lo*100:.1f},{ci_hi*100:.1f}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="results")
    parser.add_argument("--models", default="qwen,llama")
    parser.add_argument("--B", type=int, default=10000)
    args = parser.parse_args()

    models = [m.strip() for m in args.models.split(",")]
    all_results = {}

    # Header
    header = f"{'Model':<16}| {'Int DR [CI]':<22}| {'Det DR [CI]':<22}| {'ΔDR [CI]':<22}| {'DAF [CI]':<26}"
    print(header)
    print("-" * len(header))

    for model in models:
        episodes = load_episodes(args.data_dir, model)
        print(f"Loaded {len(episodes)} episodes for {MODEL_DISPLAY[model]}", flush=True)

        res = bootstrap_cis(episodes, args.B)
        per_task = bootstrap_per_task(episodes, args.B)
        res["per_task"] = per_task

        all_results[model] = res

        idr = res["int_dr"]
        ddr = res["det_dr"]
        delta = res["delta_dr"]
        daf = res["daf"]

        row = (
            f"{MODEL_DISPLAY[model]:<16}| "
            f"{fmt_pct(idr['point'], *idr['ci']):<21}| "
            f"{fmt_pct(ddr['point'], *ddr['ci']):<21}| "
            f"{fmt_pp(delta['point'], *delta['ci']):<21}| "
            f"{fmt_pct(daf['point'], *daf['ci']):<25}"
        )
        print(row)

    # Per-task breakdown
    for model in models:
        res = all_results[model]
        print(f"\n--- {MODEL_DISPLAY[model]} per-task ---")
        print(f"  {'Task':<45} {'n':>4}  {'Int DR [CI]':<24} {'Det DR [CI]':<24}")
        for task, td in sorted(res["per_task"].items()):
            idr = td["int_dr"]
            ddr = td["det_dr"]
            print(f"  {task:<45} {td['n']:>4}  {fmt_pct(idr['point'], *idr['ci']):<24} {fmt_pct(ddr['point'], *ddr['ci']):<24}")

    # JSON output
    json_path = os.path.join(args.data_dir, "cross_model_bootstrap_cis.json")

    def serialize(obj):
        if isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, tuple):
            return list(obj)
        raise TypeError(f"Not serializable: {type(obj)}")

    with open(json_path, "w") as f:
        json.dump(all_results, f, indent=2, default=serialize)
    print(f"\nJSON saved to {json_path}")

    # LaTeX output
    tex_path = os.path.join(args.data_dir, "cross_model_bootstrap_cis.tex")
    with open(tex_path, "w") as f:
        f.write("% Cross-model death rate bootstrap CIs for Appendix M\n")
        f.write("\\begin{tabular}{lcccc}\n")
        f.write("\\toprule\n")
        f.write("Model & Int DR & Det DR & $\\Delta$DR & DAF \\\\\n")
        f.write("\\midrule\n")
        for model in models:
            res = all_results[model]
            idr = res["int_dr"]
            ddr = res["det_dr"]
            delta = res["delta_dr"]
            daf = res["daf"]
            name = MODEL_DISPLAY[model].replace("-", "{-}")
            f.write(
                f"{name} & "
                f"{idr['point']*100:.1f}\\% [{idr['ci'][0]*100:.1f}, {idr['ci'][1]*100:.1f}] & "
                f"{ddr['point']*100:.1f}\\% [{ddr['ci'][0]*100:.1f}, {ddr['ci'][1]*100:.1f}] & "
                f"{'+' if delta['point']>=0 else ''}{delta['point']*100:.1f} [{delta['ci'][0]*100:.1f}, {delta['ci'][1]*100:.1f}] & "
                f"{daf['point']*100:.1f}\\% [{daf['ci'][0]*100:.1f}, {daf['ci'][1]*100:.1f}] \\\\\n"
            )
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
    print(f"LaTeX saved to {tex_path}")


if __name__ == "__main__":
    main()
