#!/usr/bin/env python3
"""Unified tab:fewnerd metrics: gold-filtered, max_LP inst-level rho.
Uses EXACT same code path for all 3 datasets."""

import json
import sys
import os
import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

SUBTASK = "ner"

def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]

def compute_metrics(data, label="dataset"):
    N = len(data)
    if N == 0:
        print(f"  [{label}] No instances!")
        return {}

    n_samples = len(data[0]["samples"])

    greedy_f1s = []
    oracle_f1s = []
    lp_sel_f1s = []
    degen_f1_flags = []
    max_lp_per_instance = []
    mean_lp_per_instance = []

    for inst in data:
        gold = inst["gold"]
        greedy = inst["greedy"]
        samples = inst["samples"]

        g_f1 = per_instance_f1(greedy, gold, SUBTASK)
        greedy_f1s.append(g_f1)

        sample_f1s = []
        sample_lps = []
        for s in samples:
            f1 = per_instance_f1(s, gold, SUBTASK)
            sample_f1s.append(f1)
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            sample_lps.append(lp)

        oracle_f1s.append(max(sample_f1s))

        lp_sel_idx = int(np.argmax(sample_lps))
        lp_sel_f1s.append(sample_f1s[lp_sel_idx])

        degen_f1_flags.append(len(set(sample_f1s)) == 1)

        max_lp_per_instance.append(max(sample_lps))
        mean_lp_per_instance.append(float(np.mean(sample_lps)))

    greedy_f1s = np.array(greedy_f1s)
    oracle_f1s = np.array(oracle_f1s)
    lp_sel_f1s = np.array(lp_sel_f1s)

    greedy_macro = float(greedy_f1s.mean())
    oracle_macro = float(oracle_f1s.mean())
    lp_sel_macro = float(lp_sel_f1s.mean())
    headroom_pp = (oracle_macro - greedy_macro) * 100
    lp_delta_pp = (lp_sel_macro - greedy_macro) * 100
    degen_rate = float(np.mean(degen_f1_flags)) * 100

    rho_max, p_max = spearmanr(max_lp_per_instance, greedy_f1s)
    rho_mean, p_mean = spearmanr(mean_lp_per_instance, greedy_f1s)

    return {
        "n": N,
        "n_samples": n_samples,
        "greedy_f1": greedy_macro,
        "oracle_f1": oracle_macro,
        "lp_sel_f1": lp_sel_macro,
        "headroom_pp": headroom_pp,
        "lp_delta_pp": lp_delta_pp,
        "degen_f1_pct": degen_rate,
        "lp_rho_max": float(rho_max),
        "lp_rho_max_p": float(p_max),
        "lp_rho_mean": float(rho_mean),
        "lp_rho_mean_p": float(p_mean),
    }


if __name__ == "__main__":
    base = "/root/autodl-tmp/struct_self_consist_ie/output"

    datasets = {
        "SciERC": os.path.join(base, "exp_012_rerun_1024/samples.jsonl"),
        "Few-NERD": os.path.join(base, "exp_021_inference/samples.jsonl"),
        "CoNLL_Qwen_N8": os.path.join(base, "exp002_conll2003/samples.jsonl"),
    }

    all_results = {}
    for name, path in datasets.items():
        print(f"\n{'='*70}")
        print(f"DATASET: {name}")
        print(f"Path: {path}")
        print(f"{'='*70}")

        if not os.path.exists(path):
            print(f"  ERROR: File not found!")
            continue

        data = load_data(path)
        total = len(data)
        gold_filtered = [d for d in data if len(d["gold"].get("entities", [])) > 0]
        n_gf = len(gold_filtered)
        print(f"  Total: {total}, Gold-filtered: {n_gf}")

        r = compute_metrics(gold_filtered, name)
        all_results[name] = r

        print(f"  greedy_f1:    {r['greedy_f1']:.6f} ({r['greedy_f1']:.3f})")
        print(f"  oracle_f1:    {r['oracle_f1']:.6f} ({r['oracle_f1']:.3f})")
        print(f"  headroom:     {r['headroom_pp']:.2f}pp")
        print(f"  degen%:       {r['degen_f1_pct']:.1f}%")
        print(f"  lp_rho_max:   {r['lp_rho_max']:.6f} (p={r['lp_rho_max_p']:.2e})")
        print(f"  lp_rho_mean:  {r['lp_rho_mean']:.6f} (p={r['lp_rho_mean_p']:.2e})")
        print(f"  lp_sel_f1:    {r['lp_sel_f1']:.6f} ({r['lp_sel_f1']:.3f})")
        print(f"  lp_delta:     {r['lp_delta_pp']:+.2f}pp")

    # Summary table
    print(f"\n\n{'='*70}")
    print("SUMMARY TABLE (gold-filtered)")
    print(f"{'='*70}")
    print(f"{'Dataset':<20} | {'n':>6} | {'N':>2} | {'greedy':>7} | {'oracle':>7} | {'hdroom':>7} | {'degen%':>6} | {'LP_rho_max':>10} | {'LP_rho_mean':>11} | {'LP_sel':>7} | {'LP_delta':>8}")
    print("-" * 120)
    for name, r in all_results.items():
        print(f"{name:<20} | {r['n']:>6} | {r['n_samples']:>2} | {r['greedy_f1']:.4f} | {r['oracle_f1']:.4f} | {r['headroom_pp']:>6.2f}pp | {r['degen_f1_pct']:>5.1f}% | {r['lp_rho_max']:>10.4f} | {r['lp_rho_mean']:>11.4f} | {r['lp_sel_f1']:.4f} | {r['lp_delta_pp']:>+7.2f}pp")

    # Save
    out_path = os.path.join(os.path.dirname(base), "output/unified_tab_fewnerd_maxlp.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {out_path}")
