#!/usr/bin/env python3
"""SciERC N=16 3-seed Selection F1 analysis with N=8 comparison."""

import json, os, sys, time
from collections import Counter
import numpy as np
from scipy import stats as sp_stats

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"

GROUPS = {
    "qwen_scierc_ner_n16": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
            123: f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
            456: f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
        },
    },
    "qwen_scierc_ner_n8": {
        "subtask": "ner",
        "seeds": {
            42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
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
    samples = instance["samples"]
    N = len(samples)
    field = "entities" if subtask == "ner" else "relations"
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance, subtask):
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


def paired_bootstrap(sel_f1s, greedy_f1s, n_boot, seed):
    rng = np.random.RandomState(seed)
    n = len(sel_f1s)
    obs_diff = sel_f1s.mean() - greedy_f1s.mean()
    diffs = sel_f1s - greedy_f1s
    count_worse = 0
    boot_diffs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, n)
        bd = diffs[idx].mean()
        boot_diffs.append(bd)
        if bd <= 0:
            count_worse += 1
    p_value = count_worse / n_boot
    boot_diffs = np.array(boot_diffs)
    ci_lo = float(np.percentile(boot_diffs, 2.5))
    ci_hi = float(np.percentile(boot_diffs, 97.5))
    return {
        "observed_diff": round(float(obs_diff), 6),
        "p_value": round(float(p_value), 6),
        "ci95": [round(ci_lo, 6), round(ci_hi, 6)],
    }


def analyze_single_seed(path, subtask):
    data = load_data(path)
    n_inst = len(data)
    N_samp = len(data[0]["samples"])
    print(f"      {path.split('/')[-2]}: {n_inst} instances, N={N_samp}")

    greedy_f1s = []
    random_f1s = []
    oracle_f1s = []
    signal_f1s = {sig: [] for sig in SIGNALS}

    t0 = time.time()
    rng = np.random.RandomState(BOOTSTRAP_SEED)

    for inst in data:
        samples = inst["samples"]
        N = len(samples)
        gold = inst["gold"]

        # greedy is separate key or first sample
        greedy = inst.get("greedy", samples[0])

        sample_f1s = []
        for s in samples:
            f1 = per_instance_f1(s, gold, subtask)
            sample_f1s.append(f1)
        sample_f1s_arr = np.array(sample_f1s)

        greedy_f1 = per_instance_f1(greedy, gold, subtask)
        greedy_f1s.append(greedy_f1)
        random_f1s.append(float(np.mean([sample_f1s_arr[rng.randint(0, N)] for _ in range(N_RANDOM_REPEATS)])))
        oracle_f1s.append(float(np.max(sample_f1s_arr)))

        sj_scores = compute_sample_sj_scores(inst, subtask)
        fk_scores, key_sets = compute_sample_surface_scores(inst, subtask)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores, "EM": em_scores, "LP": lp_scores}
        for sig in SIGNALS:
            idx = select_top1(all_scores[sig])
            signal_f1s[sig].append(sample_f1s_arr[idx])

    elapsed = time.time() - t0
    print(f"      Done in {elapsed:.1f}s")

    greedy_arr = np.array(greedy_f1s)
    random_arr = np.array(random_f1s)
    oracle_arr = np.array(oracle_f1s)

    result = {
        "n_instances": n_inst,
        "n_samples": N_samp,
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


def fisher_combine(p_values):
    p_values = [max(p, 1e-10) for p in p_values]
    stat = -2 * sum(np.log(p) for p in p_values)
    combined_p = 1.0 - sp_stats.chi2.cdf(stat, 2 * len(p_values))
    return float(combined_p)


def aggregate_seeds(seed_results, seeds):
    agg = {"seeds": seeds}
    agg["n_instances"] = seed_results[seeds[0]]["n_instances"]
    agg["n_samples"] = seed_results[seeds[0]]["n_samples"]

    for key in ["greedy_f1", "random_f1", "oracle_f1"]:
        vals = [seed_results[s][key] for s in seeds]
        agg[key] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": {str(s): round(v, 5) for s, v in zip(seeds, vals)},
        }

    agg["signal_selection_f1"] = {}
    for sig in SIGNALS:
        vals = [seed_results[s][sig]["selection_f1"] for s in seeds]
        deltas = [seed_results[s][sig]["delta_vs_greedy"] for s in seeds]
        p_values = [seed_results[s][sig]["bootstrap"]["p_value"] for s in seeds]
        ci_los = [seed_results[s][sig]["bootstrap"]["ci95"][0] for s in seeds]
        ci_his = [seed_results[s][sig]["bootstrap"]["ci95"][1] for s in seeds]

        agg["signal_selection_f1"][sig] = {
            "mean": round(float(np.mean(vals)), 5),
            "std": round(float(np.std(vals, ddof=1)), 5),
            "per_seed": {str(s): round(v, 5) for s, v in zip(seeds, vals)},
            "delta_vs_greedy_mean": round(float(np.mean(deltas)), 5),
            "delta_vs_greedy_std": round(float(np.std(deltas, ddof=1)), 5),
            "vs_greedy_p_per_seed": {str(s): round(p, 5) for s, p in zip(seeds, p_values)},
            "vs_greedy_p_combined_fisher": round(fisher_combine(p_values), 5),
            "vs_greedy_ci95_per_seed": {str(s): [round(lo, 5), round(hi, 5)] for s, lo, hi in zip(seeds, ci_los, ci_his)},
        }
    return agg


def main():
    all_results = {}

    for group_name, group_cfg in GROUPS.items():
        subtask = group_cfg["subtask"]
        seeds_cfg = group_cfg["seeds"]
        seeds = sorted(seeds_cfg.keys())

        print(f"\n{'='*60}")
        print(f"  {group_name}")
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
            print(f"  WARNING: only {len(seed_results)} seeds, skipping")
            continue

        agg = aggregate_seeds(seed_results, list(seed_results.keys()))
        all_results[group_name] = {
            "aggregated": agg,
            "per_seed": {str(s): seed_results[s] for s in seed_results},
        }

        # Print summary
        g = agg["greedy_f1"]
        o = agg["oracle_f1"]
        r = agg["random_f1"]
        print(f"\n  {'Method':<10s}  {'Mean F1':>9s}  {'+-std':>7s}  {'D greedy':>9s}  {'p(Fisher)':>10s}")
        print(f"  {'-'*10}  {'-'*9}  {'-'*7}  {'-'*9}  {'-'*10}")
        print(f"  {'Greedy':<10s}  {g['mean']:.5f}  {g['std']:.5f}")
        print(f"  {'Random':<10s}  {r['mean']:.5f}  {r['std']:.5f}")
        for sig in SIGNALS:
            sr = agg["signal_selection_f1"][sig]
            print(f"  {sig:<10s}  {sr['mean']:.5f}  {sr['std']:.5f}  {sr['delta_vs_greedy_mean']:+.5f}  {sr['vs_greedy_p_combined_fisher']:.5f}")
        print(f"  {'Oracle':<10s}  {o['mean']:.5f}  {o['std']:.5f}")

    # N=16 vs N=8 comparison
    if "qwen_scierc_ner_n16" in all_results and "qwen_scierc_ner_n8" in all_results:
        n16 = all_results["qwen_scierc_ner_n16"]["aggregated"]
        n8 = all_results["qwen_scierc_ner_n8"]["aggregated"]
        comp = {}
        for sig in SIGNALS:
            s16 = n16["signal_selection_f1"][sig]
            s8 = n8["signal_selection_f1"][sig]
            comp[sig] = {
                "n16_mean": s16["mean"],
                "n8_mean": s8["mean"],
                "diff_n16_minus_n8": round(s16["mean"] - s8["mean"], 5),
                "n16_delta_greedy": s16["delta_vs_greedy_mean"],
                "n8_delta_greedy": s8["delta_vs_greedy_mean"],
            }
        comp["oracle_gap"] = {
            "n16": round(n16["oracle_f1"]["mean"] - n16["greedy_f1"]["mean"], 5),
            "n8": round(n8["oracle_f1"]["mean"] - n8["greedy_f1"]["mean"], 5),
        }
        comp["greedy_f1"] = {"n16": n16["greedy_f1"]["mean"], "n8": n8["greedy_f1"]["mean"]}
        all_results["n16_vs_n8_comparison"] = comp

        print(f"\n{'='*60}")
        print(f"  N=16 vs N=8 Comparison")
        print(f"{'='*60}")
        print(f"  {'Signal':<8s}  {'N=16':>8s}  {'N=8':>8s}  {'D(16-8)':>8s}  {'N=16 Dg':>8s}  {'N=8 Dg':>8s}")
        print(f"  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}")
        for sig in SIGNALS:
            c = comp[sig]
            print(f"  {sig:<8s}  {c['n16_mean']:.5f}  {c['n8_mean']:.5f}  {c['diff_n16_minus_n8']:+.5f}  {c['n16_delta_greedy']:+.5f}  {c['n8_delta_greedy']:+.5f}")
        print(f"  Oracle gap: N=16={comp['oracle_gap']['n16']:.5f}, N=8={comp['oracle_gap']['n8']:.5f}")

    out_path = f"{BASE}/output/analysis_scierc_n16_3seed_selection_f1.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
