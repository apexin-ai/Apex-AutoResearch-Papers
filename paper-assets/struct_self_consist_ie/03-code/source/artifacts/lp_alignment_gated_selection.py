"""
LP-Alignment-Gated Selection: auto-decide LP vs greedy per dataset.
Probe a subset of instances, compute within-instance LP-F1 Spearman rho mean.
If mean_rho > threshold -> LP selection; else -> greedy.
"""

import json
import os
import sys
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import (
    compute_entity_f1, compute_degeneracy, load_and_filter,
    compute_sample_f1s, compute_greedy_f1, get_lp_selection_idx,
    bootstrap_ci
)

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/prescriptive_analysis"
os.makedirs(OUT_DIR, exist_ok=True)

DATASETS = {
    "SciERC": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
    "CoNLL": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
    "FewNERD": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
}

THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5]
PROBE_SIZES = [50, 100, 200, 500, "all"]


def get_sample_lps(inst):
    """Get mean_logprob for each sample."""
    lps = []
    samples = inst["samples"]
    logprobs_field = inst.get("logprobs", [])
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and i < len(logprobs_field):
            lp = logprobs_field[i]
        lps.append(lp if lp is not None else float("nan"))
    return lps


def within_instance_rho(f1s, lps):
    """Spearman rho between LP and F1 within one instance. Returns nan if not computable."""
    if len(f1s) < 3:
        return float("nan")
    if len(set(round(v, 10) for v in f1s)) < 2:
        return float("nan")
    if len(set(round(v, 10) for v in lps)) < 2:
        return float("nan")
    valid = [(f, l) for f, l in zip(f1s, lps) if np.isfinite(l)]
    if len(valid) < 3:
        return float("nan")
    fs, ls = zip(*valid)
    rho, _ = spearmanr(ls, fs)
    return rho if np.isfinite(rho) else float("nan")


def compute_alignment_score(instances, probe_size=None, seed=42):
    """Compute mean within-instance LP-F1 rho over a probe subset."""
    rng = np.random.RandomState(seed)
    if probe_size is not None and probe_size != "all" and probe_size < len(instances):
        idx = rng.choice(len(instances), probe_size, replace=False)
        probe = [instances[i] for i in idx]
    else:
        probe = instances

    rhos = []
    for inst in probe:
        f1s = compute_sample_f1s(inst)
        lps = get_sample_lps(inst)
        rho = within_instance_rho(f1s, lps)
        if np.isfinite(rho):
            rhos.append(rho)

    if not rhos:
        return 0.0, 0, len(probe)
    return float(np.mean(rhos)), len(rhos), len(probe)


def compute_selection_f1s(instances):
    """Compute per-instance F1 for greedy, LP, and oracle strategies."""
    greedy_f1s = []
    lp_f1s = []
    oracle_f1s = []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        # greedy
        gf1 = compute_greedy_f1(inst)
        greedy_f1s.append(gf1)

        # LP selection
        lp_idx = get_lp_selection_idx(inst)
        lp_sample = inst["samples"][lp_idx]
        lpf1 = compute_entity_f1(lp_sample.get("entities", []), gold_ents)
        lp_f1s.append(lpf1)

        # oracle: pick whichever is better
        oracle_f1s.append(max(gf1, lpf1))

    return {
        "greedy": greedy_f1s,
        "lp": lp_f1s,
        "oracle": oracle_f1s,
    }


def main():
    results = {}

    for ds_name, path in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"Dataset: {ds_name}")
        print(f"Path: {path}")

        instances = load_and_filter(path, gold_filter=True)
        n_total = len(instances)
        print(f"Instances (gold-filtered): {n_total}")
        n_samples_per = len(instances[0]["samples"]) if instances else 0
        print(f"Samples per instance: {n_samples_per}")

        # compute all selection F1s
        sel = compute_selection_f1s(instances)
        greedy_mean = float(np.mean(sel["greedy"]))
        lp_mean = float(np.mean(sel["lp"]))
        oracle_mean = float(np.mean(sel["oracle"]))
        lp_delta = lp_mean - greedy_mean

        print(f"\nBaseline F1s:")
        print(f"  Greedy:     {greedy_mean*100:.2f}")
        print(f"  LP:         {lp_mean*100:.2f}  (delta: {lp_delta*100:+.2f}pp)")
        print(f"  Oracle:     {oracle_mean*100:.2f}")

        ds_result = {
            "n_instances": n_total,
            "n_samples": n_samples_per,
            "greedy_f1": greedy_mean,
            "lp_f1": lp_mean,
            "oracle_gated_f1": oracle_mean,
            "lp_delta_pp": lp_delta * 100,
            "alignment_scores": {},
            "gating_decisions": {},
        }

        # alignment score sweep: probe_size x threshold
        print(f"\n--- Alignment Score by Probe Size ---")
        for ps in PROBE_SIZES:
            score, n_valid, n_probe = compute_alignment_score(instances, probe_size=ps)
            ps_key = str(ps)
            ds_result["alignment_scores"][ps_key] = {
                "mean_rho": score,
                "n_valid": n_valid,
                "n_probe": n_probe,
            }
            print(f"  probe={ps_key:>5s}: mean_rho={score:.4f}  (valid={n_valid}/{n_probe})")

        # gating decisions for each threshold (using all instances)
        all_score = ds_result["alignment_scores"]["all"]["mean_rho"]
        print(f"\n--- Gating Decisions (alignment_score={all_score:.4f}) ---")
        for thr in THRESHOLDS:
            use_lp = all_score > thr
            gated_f1 = lp_mean if use_lp else greedy_mean
            decision = "LP" if use_lp else "greedy"
            delta_vs_greedy = (gated_f1 - greedy_mean) * 100
            delta_vs_always_lp = (gated_f1 - lp_mean) * 100

            ds_result["gating_decisions"][str(thr)] = {
                "decision": decision,
                "gated_f1": gated_f1,
                "delta_vs_greedy_pp": delta_vs_greedy,
                "delta_vs_always_lp_pp": delta_vs_always_lp,
                "is_correct": (use_lp and lp_delta > 0) or (not use_lp and lp_delta <= 0),
            }
            correct_mark = "V" if ds_result["gating_decisions"][str(thr)]["is_correct"] else "X"
            print(f"  thr={thr:.1f}: {decision:>6s}  F1={gated_f1*100:.2f}  "
                  f"vs_greedy={delta_vs_greedy:+.2f}pp  [{correct_mark}]")

        # probe_size sensitivity for a fixed threshold (0.3)
        print(f"\n--- Probe Size Sensitivity (threshold=0.3) ---")
        stability = {}
        for ps in PROBE_SIZES:
            scores_per_run = []
            for run_seed in range(42, 52):
                s, _, _ = compute_alignment_score(instances, probe_size=ps, seed=run_seed)
                scores_per_run.append(s)
            mean_s = float(np.mean(scores_per_run))
            std_s = float(np.std(scores_per_run))
            decisions = ["LP" if s > 0.3 else "greedy" for s in scores_per_run]
            consistency = max(decisions.count("LP"), decisions.count("greedy")) / len(decisions)
            stability[str(ps)] = {
                "mean_rho": mean_s,
                "std_rho": std_s,
                "consistency": consistency,
                "decisions": decisions,
            }
            print(f"  probe={str(ps):>5s}: rho={mean_s:.4f}+/-{std_s:.4f}  "
                  f"consistency={consistency:.0%}  majority={max(set(decisions), key=decisions.count)}")

        ds_result["probe_stability_thr03"] = stability
        results[ds_name] = ds_result

    # summary table
    print(f"\n{'='*60}")
    print("SUMMARY: LP-Alignment-Gated Selection (threshold=0.3)")
    print(f"{'Dataset':<10s} {'align_score':>12s} {'decision':>10s} {'greedy':>8s} {'LP':>8s} {'gated':>8s} {'oracle':>8s} {'correct':>8s}")
    print("-" * 75)
    for ds_name in DATASETS:
        r = results[ds_name]
        align = r["alignment_scores"]["all"]["mean_rho"]
        gate = r["gating_decisions"]["0.3"]
        print(f"{ds_name:<10s} {align:>12.4f} {gate['decision']:>10s} "
              f"{r['greedy_f1']*100:>8.2f} {r['lp_f1']*100:>8.2f} "
              f"{gate['gated_f1']*100:>8.2f} {r['oracle_gated_f1']*100:>8.2f} "
              f"{'YES' if gate['is_correct'] else 'NO':>8s}")

    # LaTeX table
    print(f"\n--- LaTeX Table ---")
    print(r"\begin{tabular}{lcccccc}")
    print(r"\toprule")
    print(r"Dataset & $\bar{\rho}$ & Decision & Greedy & LP & Gated & Oracle \\")
    print(r"\midrule")
    for ds_name in DATASETS:
        r = results[ds_name]
        align = r["alignment_scores"]["all"]["mean_rho"]
        gate = r["gating_decisions"]["0.3"]
        gf = r["greedy_f1"] * 100
        lf = r["lp_f1"] * 100
        gatf = gate["gated_f1"] * 100
        orf = r["oracle_gated_f1"] * 100
        dec = gate["decision"]
        print(f"{ds_name} & {align:.3f} & {dec} & {gf:.2f} & {lf:.2f} & {gatf:.2f} & {orf:.2f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    # save
    out_path = os.path.join(OUT_DIR, "lp_alignment_gated.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
