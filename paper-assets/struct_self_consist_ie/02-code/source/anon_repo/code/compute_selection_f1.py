#!/usr/bin/env python3
"""Multi-seed Selection F1 for Table 3 (C2 critical).

For each instance's N samples, score with 5 signals (SJ/FK/VC/EM/LP),
select the top-scoring sample, compute its F1 vs gold.
Reports 3-seed mean±σ, per-seed bootstrap p-value vs greedy, and
a combined bootstrap p-value across seeds.

Input: samples.jsonl files from inference experiments.
Output: JSON results + markdown report.
Depends: consistency.py, evaluation.py (same directory).
"""

import json
import os
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

EXPERIMENT_GROUPS = {
    # --- Qwen SciERC N=16 (v2 pipeline) ---
    "qwen_scierc_ner_n16": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
            123: f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
            456: f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
        },
    },
    "qwen_scierc_re_n16": {
        "subtask": "re",
        "seeds": {
            42: f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
            123: f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
            456: f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
        },
    },
    # --- Qwen SciERC N=8 (r1024 logprobs) ---
    "qwen_scierc_ner_n8": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
        },
    },
    # --- LLaMA SciERC N=8 ---
    "llama_scierc_ner_n8": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_llama_scierc_seed456_r1024/samples.jsonl",
        },
    },
    # --- LLaMA CoNLL N=16 ---
    "llama_conll_ner_n16": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_017_llama_conll_n16_r1024/samples.jsonl",
            123: f"{BASE}/output/exp_017_llama_conll_n16_s123_r1024/samples.jsonl",
            456: f"{BASE}/output/exp_017_llama_conll_n16_s456_r1024/samples.jsonl",
        },
    },
}

N_BOOTSTRAP = 10000
BOOTSTRAP_SEED = 42
N_RANDOM_REPEATS = 50
SIGNALS = ["VC", "SJ", "FK", "EM", "LP"]


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_sample_sj_scores(instance, subtask):
    """Pairwise soft Jaccard: mean similarity of each sample to all others."""
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    pair_fn = _ner_soft_jaccard_pair if subtask == "ner" else _re_soft_jaccard_pair
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance, subtask):
    """Surface-key Jaccard (FK proxy) and key sets for VC/EM."""
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, subtask)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def compute_sample_voting_conf(key_sets, N):
    """Voting confidence: mean frequency of each sample's extracted items."""
    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / N for key in ks]
            scores.append(float(np.mean(fracs)))
    return scores


def compute_sample_em_scores(key_sets):
    """Exact match: count of other samples with identical extraction."""
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_sample_logprobs(instance):
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def select_top1(scores):
    return int(np.argmax(scores))


def paired_bootstrap(sel_f1s, greedy_f1s, n_bootstrap, seed):
    """Test H1: selection F1 > greedy F1 via paired bootstrap."""
    rng = np.random.RandomState(seed)
    n = len(sel_f1s)
    observed_delta = sel_f1s.mean() - greedy_f1s.mean()
    count_ge = 0
    deltas = np.empty(n_bootstrap)
    for b in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        d = sel_f1s[idx].mean() - greedy_f1s[idx].mean()
        deltas[b] = d
        if d <= 0:
            count_ge += 1
    p_value = count_ge / n_bootstrap
    ci95 = [float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))]
    return {"observed_delta": float(observed_delta), "p_value": float(p_value), "ci95": ci95}


def analyze_single_seed(path, subtask):
    data = load_data(path)
    field = "entities" if subtask == "ner" else "relations"
    # Filter to instances with non-empty gold
    instances = [d for d in data if len(d["gold"].get(field, [])) > 0]
    n_inst = len(instances)
    N_per = len(instances[0]["samples"]) if instances else 0
    print(f"      {n_inst} instances, N={N_per} samples/inst")

    t0 = time.time()
    greedy_f1s = []
    oracle_f1s = []
    random_f1s = []
    signal_f1s = {sig: [] for sig in SIGNALS}

    for inst in instances:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask=subtask)
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
        oracle_f1s.append(max(sample_f1s))
        random_f1s.append(float(np.mean(sample_f1s)))

        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}

        for sig in SIGNALS:
            chosen = select_top1(all_scores[sig])
            signal_f1s[sig].append(sample_f1s[chosen])

    elapsed = time.time() - t0
    print(f"      Done in {elapsed:.1f}s")

    greedy_arr = np.array(greedy_f1s)
    random_arr = np.array(random_f1s)
    oracle_arr = np.array(oracle_f1s)

    result = {
        "n_instances": n_inst,
        "n_samples_per_instance": N_per,
        "greedy_f1": float(greedy_arr.mean()),
        "random_f1": float(random_arr.mean()),
        "oracle_f1": float(oracle_arr.mean()),
    }

    for sig in SIGNALS:
        arr = np.array(signal_f1s[sig])
        boot = paired_bootstrap(arr, greedy_arr, N_BOOTSTRAP, BOOTSTRAP_SEED)
        result[sig] = {
            "selection_f1": float(arr.mean()),
            "delta_vs_greedy": float(arr.mean() - greedy_arr.mean()),
            "bootstrap": boot,
        }

    return result


def aggregate_seeds(seed_results, seeds):
    agg = {}
    agg["seeds"] = seeds
    agg["n_instances"] = seed_results[seeds[0]]["n_instances"]
    agg["n_samples_per_instance"] = seed_results[seeds[0]]["n_samples_per_instance"]

    for key in ["greedy_f1", "random_f1", "oracle_f1"]:
        vals = [seed_results[s][key] for s in seeds]
        agg[key] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": [round(v, 5) for v in vals],
        }

    agg["signal_selection_f1"] = {}
    for sig in SIGNALS:
        vals = [seed_results[s][sig]["selection_f1"] for s in seeds]
        deltas = [seed_results[s][sig]["delta_vs_greedy"] for s in seeds]
        p_values = [seed_results[s][sig]["bootstrap"]["p_value"] for s in seeds]
        ci_los = [seed_results[s][sig]["bootstrap"]["ci95"][0] for s in seeds]
        ci_his = [seed_results[s][sig]["bootstrap"]["ci95"][1] for s in seeds]

        # Combined p-value: Fisher's method
        import scipy.stats as st
        clipped_ps = [max(p, 1e-10) for p in p_values]
        chi2 = -2 * sum(np.log(p) for p in clipped_ps)
        combined_p = float(1 - st.chi2.cdf(chi2, 2 * len(clipped_ps)))

        agg["signal_selection_f1"][sig] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": [round(v, 5) for v in vals],
            "delta_vs_greedy_mean": round(float(np.mean(deltas)), 5),
            "delta_vs_greedy_std": round(float(np.std(deltas, ddof=1)), 5),
            "vs_greedy_p_per_seed": [round(p, 5) for p in p_values],
            "vs_greedy_p_combined_fisher": round(combined_p, 5),
            "vs_greedy_ci95_per_seed": [[round(lo, 5), round(hi, 5)] for lo, hi in zip(ci_los, ci_his)],
        }

    return agg


def generate_report(all_results):
    """Generate markdown report for artifacts/."""
    lines = ["# Multi-seed Selection F1 Report (Table 3, C2)", ""]
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Bootstrap resamples: {N_BOOTSTRAP}")
    lines.append("")

    for group_name, agg in all_results.items():
        n = agg["n_instances"]
        N_samp = agg["n_samples_per_instance"]
        lines.append(f"## {group_name} (n={n}, N={N_samp})")
        lines.append("")

        # Table header
        lines.append(f"| Method | Mean F1 | ±σ | Δ greedy | p (Fisher) |")
        lines.append(f"|--------|--------:|---:|---------:|-----------:|")

        g = agg["greedy_f1"]
        lines.append(f"| Greedy | {g['mean']:.4f} | {g['std']:.4f} | — | — |")
        r = agg["random_f1"]
        lines.append(f"| Random | {r['mean']:.4f} | {r['std']:.4f} | {r['mean']-g['mean']:+.4f} | — |")

        for sig in SIGNALS:
            sr = agg["signal_selection_f1"][sig]
            p_fisher = sr["vs_greedy_p_combined_fisher"]
            p_str = f"{p_fisher:.4f}"
            if p_fisher < 0.01:
                p_str = f"**{p_fisher:.4f}**"
            elif p_fisher < 0.05:
                p_str = f"*{p_fisher:.4f}*"
            lines.append(f"| {sig} | {sr['mean']:.4f} | {sr['std']:.4f} | {sr['delta_vs_greedy_mean']:+.4f} | {p_str} |")

        o = agg["oracle_f1"]
        lines.append(f"| Oracle | {o['mean']:.4f} | {o['std']:.4f} | {o['mean']-g['mean']:+.4f} | — |")
        lines.append("")

        # Per-seed detail
        lines.append("<details><summary>Per-seed breakdown</summary>")
        lines.append("")
        for seed in agg["seeds"]:
            lines.append(f"**Seed {seed}:**")
            lines.append("")
            for sig in SIGNALS:
                sr = agg["signal_selection_f1"][sig]
                idx = agg["seeds"].index(seed)
                sf1 = sr["per_seed"][idx]
                gf1 = agg["greedy_f1"]["per_seed"][idx]
                p = sr["vs_greedy_p_per_seed"][idx]
                ci = sr["vs_greedy_ci95_per_seed"][idx]
                lines.append(f"- {sig}: sel_F1={sf1:.4f}, Δ={sf1-gf1:+.4f}, p={p:.4f}, CI95=[{ci[0]:+.4f}, {ci[1]:+.4f}]")
            lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines)


def main():
    all_results = {}

    for group_name, group_cfg in EXPERIMENT_GROUPS.items():
        subtask = group_cfg["subtask"]
        seeds_cfg = group_cfg["seeds"]
        seeds = sorted(seeds_cfg.keys())

        print(f"\n{'='*60}")
        print(f"  {group_name} (subtask={subtask})")
        print(f"{'='*60}")

        seed_results = {}
        for seed in seeds:
            path = seeds_cfg[seed]
            if not os.path.exists(path):
                print(f"  SKIP seed {seed}: {path} not found")
                continue
            print(f"  seed {seed}:")
            seed_results[seed] = analyze_single_seed(path, subtask)

        if len(seed_results) < 2:
            print(f"  WARNING: only {len(seed_results)} seeds, skipping aggregation")
            continue

        agg = aggregate_seeds(seed_results, list(seed_results.keys()))
        all_results[group_name] = agg

        # Print summary
        print(f"\n  {'Method':<10s}  {'Mean F1':>9s}  {'±σ':>7s}  {'Δ greedy':>9s}  {'p(Fisher)':>10s}")
        print(f"  {'-'*10}  {'-'*9}  {'-'*7}  {'-'*9}  {'-'*10}")
        print(f"  {'Greedy':<10s}  {agg['greedy_f1']['mean']:.5f}  {agg['greedy_f1']['std']:.5f}")
        print(f"  {'Random':<10s}  {agg['random_f1']['mean']:.5f}  {agg['random_f1']['std']:.5f}")
        for sig in SIGNALS:
            sr = agg["signal_selection_f1"][sig]
            print(f"  {sig:<10s}  {sr['mean']:.5f}  {sr['std']:.5f}  {sr['delta_vs_greedy_mean']:+.5f}  {sr['vs_greedy_p_combined_fisher']:.5f}")
        print(f"  {'Oracle':<10s}  {agg['oracle_f1']['mean']:.5f}  {agg['oracle_f1']['std']:.5f}")

    # Save JSON
    out_json = f"{BASE}/output/multiseed_selection_f1.json"
    with open(out_json, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved JSON: {out_json}")

    # Save report
    os.makedirs(f"{BASE}/artifacts", exist_ok=True)
    report = generate_report(all_results)
    out_md = f"{BASE}/artifacts/multiseed_selection_f1_report.md"
    with open(out_md, "w") as f:
        f.write(report)
    print(f"Saved report: {out_md}")


if __name__ == "__main__":
    main()
