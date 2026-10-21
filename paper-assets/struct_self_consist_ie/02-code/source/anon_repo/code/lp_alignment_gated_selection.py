"""
LP-Alignment-Gated Selection: auto-decide LP vs greedy per dataset.
Probe a subset of instances, compute within-instance LP-F1 Spearman rho mean.
If adjusted_score > threshold -> LP selection; else -> greedy.

Key insight: raw mean_rho can mislead when degeneracy is high (many instances
have constant F1 or LP, making rho uncomputable). Adjusted score = mean_rho *
valid_ratio down-weights datasets with high degeneracy.
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

    n_valid = len(rhos)
    n_probe = len(probe)
    mean_rho = float(np.mean(rhos)) if rhos else 0.0
    valid_ratio = n_valid / n_probe if n_probe > 0 else 0.0
    adjusted = mean_rho * valid_ratio
    return mean_rho, adjusted, valid_ratio, n_valid, n_probe


def compute_selection_f1s(instances):
    greedy_f1s = []
    lp_f1s = []
    oracle_f1s = []

    for inst in instances:
        gold_ents = inst["gold"]["entities"]
        gf1 = compute_greedy_f1(inst)
        greedy_f1s.append(gf1)

        lp_idx = get_lp_selection_idx(inst)
        lp_sample = inst["samples"][lp_idx]
        lpf1 = compute_entity_f1(lp_sample.get("entities", []), gold_ents)
        lp_f1s.append(lpf1)

        oracle_f1s.append(max(gf1, lpf1))

    return {"greedy": greedy_f1s, "lp": lp_f1s, "oracle": oracle_f1s}


def main():
    results = {}

    for ds_name, path in DATASETS.items():
        print(f"\n{'='*60}")
        print(f"Dataset: {ds_name}")
        print(f"Path: {path}")

        instances = load_and_filter(path, gold_filter=True)
        n_total = len(instances)
        n_samples_per = len(instances[0]["samples"]) if instances else 0
        print(f"Instances (gold-filtered): {n_total}, samples/instance: {n_samples_per}")

        sel = compute_selection_f1s(instances)
        greedy_mean = float(np.mean(sel["greedy"]))
        lp_mean = float(np.mean(sel["lp"]))
        oracle_mean = float(np.mean(sel["oracle"]))
        lp_delta = lp_mean - greedy_mean

        greedy_ci = bootstrap_ci(sel["greedy"])
        lp_ci = bootstrap_ci(sel["lp"])
        delta_significant = True
        if lp_delta > 0:
            delta_significant = lp_ci["ci_lo"] > greedy_ci["ci_hi"] or abs(lp_delta) > 0.005
        else:
            delta_significant = abs(lp_delta) > 0.005

        print(f"\nBaseline F1s:")
        print(f"  Greedy: {greedy_mean*100:.2f} [{greedy_ci['ci_lo']*100:.2f}, {greedy_ci['ci_hi']*100:.2f}]")
        print(f"  LP:     {lp_mean*100:.2f} [{lp_ci['ci_lo']*100:.2f}, {lp_ci['ci_hi']*100:.2f}]  (delta: {lp_delta*100:+.2f}pp)")
        print(f"  Oracle: {oracle_mean*100:.2f}")

        ds_result = {
            "n_instances": n_total,
            "n_samples": n_samples_per,
            "greedy_f1": greedy_mean,
            "greedy_ci": greedy_ci,
            "lp_f1": lp_mean,
            "lp_ci": lp_ci,
            "oracle_gated_f1": oracle_mean,
            "lp_delta_pp": lp_delta * 100,
            "lp_beneficial": lp_delta > 0.005,
            "alignment_scores": {},
            "gating_decisions": {},
        }

        # alignment score sweep
        print(f"\n--- Alignment Score by Probe Size ---")
        print(f"  {'probe':>5s}  {'mean_rho':>8s}  {'valid%':>7s}  {'adjusted':>8s}  {'valid/total':>12s}")
        for ps in PROBE_SIZES:
            mean_rho, adjusted, valid_ratio, n_valid, n_probe = compute_alignment_score(instances, probe_size=ps)
            ps_key = str(ps)
            ds_result["alignment_scores"][ps_key] = {
                "mean_rho": mean_rho,
                "adjusted_score": adjusted,
                "valid_ratio": valid_ratio,
                "n_valid": n_valid,
                "n_probe": n_probe,
            }
            print(f"  {ps_key:>5s}  {mean_rho:>8.4f}  {valid_ratio:>6.1%}  {adjusted:>8.4f}  {n_valid:>5d}/{n_probe:<5d}")

        # gating decisions: both raw and adjusted scores
        all_info = ds_result["alignment_scores"]["all"]
        raw_score = all_info["mean_rho"]
        adj_score = all_info["adjusted_score"]
        valid_ratio = all_info["valid_ratio"]

        print(f"\n--- Gating Decisions ---")
        print(f"  Raw score: {raw_score:.4f}, Adjusted score: {adj_score:.4f}, Valid ratio: {valid_ratio:.1%}")

        for thr in THRESHOLDS:
            # raw gating
            use_lp_raw = raw_score > thr
            gated_f1_raw = lp_mean if use_lp_raw else greedy_mean
            dec_raw = "LP" if use_lp_raw else "greedy"
            correct_raw = (use_lp_raw and lp_delta > 0.005) or (not use_lp_raw and lp_delta <= 0.005)

            # adjusted gating
            use_lp_adj = adj_score > thr
            gated_f1_adj = lp_mean if use_lp_adj else greedy_mean
            dec_adj = "LP" if use_lp_adj else "greedy"
            correct_adj = (use_lp_adj and lp_delta > 0.005) or (not use_lp_adj and lp_delta <= 0.005)

            ds_result["gating_decisions"][str(thr)] = {
                "raw": {"decision": dec_raw, "gated_f1": gated_f1_raw, "correct": correct_raw},
                "adjusted": {"decision": dec_adj, "gated_f1": gated_f1_adj, "correct": correct_adj},
            }
            r_mark = "OK" if correct_raw else "FAIL"
            a_mark = "OK" if correct_adj else "FAIL"
            print(f"  thr={thr:.1f}: raw={dec_raw:>6s}[{r_mark:>4s}]  adj={dec_adj:>6s}[{a_mark:>4s}]")

        # probe_size sensitivity (threshold=0.3 on adjusted)
        print(f"\n--- Probe Size Sensitivity (adjusted, threshold=0.3) ---")
        stability = {}
        for ps in PROBE_SIZES:
            adj_scores_per_run = []
            for run_seed in range(42, 52):
                _, adj, _, _, _ = compute_alignment_score(instances, probe_size=ps, seed=run_seed)
                adj_scores_per_run.append(adj)
            mean_s = float(np.mean(adj_scores_per_run))
            std_s = float(np.std(adj_scores_per_run))
            decisions = ["LP" if s > 0.3 else "greedy" for s in adj_scores_per_run]
            consistency = max(decisions.count("LP"), decisions.count("greedy")) / len(decisions)
            stability[str(ps)] = {
                "mean_adj": mean_s,
                "std_adj": std_s,
                "consistency": consistency,
                "majority_decision": max(set(decisions), key=decisions.count),
            }
            print(f"  probe={str(ps):>5s}: adj={mean_s:.4f}+/-{std_s:.4f}  "
                  f"consistency={consistency:.0%}  majority={stability[str(ps)]['majority_decision']}")

        ds_result["probe_stability_adj_thr03"] = stability
        results[ds_name] = ds_result

    # summary tables
    print(f"\n{'='*60}")
    print("SUMMARY: Raw Score Gating (threshold=0.3)")
    print(f"{'Dataset':<10s} {'raw_rho':>8s} {'valid%':>7s} {'decision':>9s} {'greedy':>8s} {'LP':>8s} {'gated':>8s} {'oracle':>8s} {'ok':>5s}")
    print("-" * 80)
    for ds_name in DATASETS:
        r = results[ds_name]
        raw = r["alignment_scores"]["all"]["mean_rho"]
        vr = r["alignment_scores"]["all"]["valid_ratio"]
        gate = r["gating_decisions"]["0.3"]["raw"]
        print(f"{ds_name:<10s} {raw:>8.4f} {vr:>6.1%} {gate['decision']:>9s} "
              f"{r['greedy_f1']*100:>8.2f} {r['lp_f1']*100:>8.2f} "
              f"{gate['gated_f1']*100:>8.2f} {r['oracle_gated_f1']*100:>8.2f} "
              f"{'OK' if gate['correct'] else 'FAIL':>5s}")

    print(f"\nSUMMARY: Adjusted Score Gating (threshold=0.3)")
    print(f"{'Dataset':<10s} {'adj_score':>9s} {'valid%':>7s} {'decision':>9s} {'greedy':>8s} {'LP':>8s} {'gated':>8s} {'oracle':>8s} {'ok':>5s}")
    print("-" * 80)
    for ds_name in DATASETS:
        r = results[ds_name]
        adj = r["alignment_scores"]["all"]["adjusted_score"]
        vr = r["alignment_scores"]["all"]["valid_ratio"]
        gate = r["gating_decisions"]["0.3"]["adjusted"]
        print(f"{ds_name:<10s} {adj:>9.4f} {vr:>6.1%} {gate['decision']:>9s} "
              f"{r['greedy_f1']*100:>8.2f} {r['lp_f1']*100:>8.2f} "
              f"{gate['gated_f1']*100:>8.2f} {r['oracle_gated_f1']*100:>8.2f} "
              f"{'OK' if gate['correct'] else 'FAIL':>5s}")

    # LaTeX table
    print(f"\n--- LaTeX Table (Adjusted Score, threshold=0.3) ---")
    print(r"\begin{tabular}{lccccccc}")
    print(r"\toprule")
    print(r"Dataset & $\bar{\rho}$ & Valid\% & $\bar{\rho}_{\text{adj}}$ & Decision & Greedy & LP & Gated \\")
    print(r"\midrule")
    for ds_name in DATASETS:
        r = results[ds_name]
        raw = r["alignment_scores"]["all"]["mean_rho"]
        adj = r["alignment_scores"]["all"]["adjusted_score"]
        vr = r["alignment_scores"]["all"]["valid_ratio"]
        gate = r["gating_decisions"]["0.3"]["adjusted"]
        gf = r["greedy_f1"] * 100
        lf = r["lp_f1"] * 100
        gatf = gate["gated_f1"] * 100
        dec = gate["decision"]
        best_f1 = max(gf, lf)
        gf_s = f"\\textbf{{{gf:.2f}}}" if gf == best_f1 else f"{gf:.2f}"
        lf_s = f"\\textbf{{{lf:.2f}}}" if lf == best_f1 else f"{lf:.2f}"
        print(f"{ds_name} & {raw:.3f} & {vr:.1%} & {adj:.3f} & {dec} & {gf_s} & {lf_s} & {gatf:.2f} \\\\")
    print(r"\bottomrule")
    print(r"\end{tabular}")

    # threshold sweep table (adjusted)
    print(f"\n--- Threshold Sweep (Adjusted Score) ---")
    print(f"{'thr':>5s}", end="")
    for ds_name in DATASETS:
        print(f"  {ds_name:>15s}", end="")
    print(f"  {'all_correct':>12s}")
    for thr in THRESHOLDS:
        print(f"{thr:>5.1f}", end="")
        all_ok = True
        for ds_name in DATASETS:
            gate = results[ds_name]["gating_decisions"][str(thr)]["adjusted"]
            ok = gate["correct"]
            all_ok = all_ok and ok
            print(f"  {gate['decision']:>8s}({'OK' if ok else 'X':>2s})", end="")
        print(f"  {'ALL OK' if all_ok else '':>12s}")

    # save
    out_path = os.path.join(OUT_DIR, "lp_alignment_gated.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
