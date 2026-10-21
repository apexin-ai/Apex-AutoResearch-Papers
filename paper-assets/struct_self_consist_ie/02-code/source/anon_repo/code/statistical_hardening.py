#!/usr/bin/env python3
"""Statistical hardening: W1/W2/I8/I9 for EMNLP 2026 submission."""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np
from scipy.stats import spearmanr, kruskal

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import entity_strict_match, per_instance_f1, _prf
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/output/statistical_hardening"
os.makedirs(OUT_DIR, exist_ok=True)

N_BOOTSTRAP = 10000
RNG = np.random.RandomState(42)

DATASETS = {
    "scierc_n8": {
        "seeds": {
            42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
            123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
            456: f"{BASE}/output/exp_018_qwen_scierc_seed456/samples.jsonl",
        },
    },
    "scierc_n16": {
        "seeds": {
            42: f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
            123: f"{BASE}/output/exp_001_seed123_v2/samples.jsonl",
            456: f"{BASE}/output/exp_001_seed456_v2/samples.jsonl",
        },
    },
    "conll_n8": {
        "seeds": {42: f"{BASE}/output/exp002_conll2003/samples.jsonl"},
    },
    "fewnerd_n8": {
        "seeds": {42: f"{BASE}/output/exp_021_inference/samples.jsonl"},
    },
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def gold_filter(data):
    return [inst for inst in data if len(inst["gold"].get("entities", [])) > 0]


def compute_lp_scores(inst):
    return [s["mean_logprob"] for s in inst["samples"]]


def compute_sj_scores(inst):
    samples = inst["samples"]
    N = len(samples)
    if N <= 1:
        return [1.0] * N
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []),
                                       samples[j].get("entities", []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_em_scores(inst):
    samples = inst["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
    return [sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j]) / max(N - 1, 1)
            for k in range(N)]


def compute_seed_metrics(data, compute_slow_signals=True):
    filtered = gold_filter(data)
    n = len(filtered)
    greedy_f1s, oracle_f1s, lp_sel_f1s = [], [], []
    sj_sel_f1s, em_sel_f1s = [], []

    for idx, inst in enumerate(filtered):
        gold = inst["gold"]
        g_f1 = per_instance_f1(inst["greedy"], gold, "ner")
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, "ner") for s in inst["samples"]]
        oracle_f1s.append(max(sample_f1s))

        lp_scores = compute_lp_scores(inst)
        lp_sel_f1s.append(sample_f1s[int(np.argmax(lp_scores))])

        if compute_slow_signals:
            sj_scores = compute_sj_scores(inst)
            sj_sel_f1s.append(sample_f1s[int(np.argmax(sj_scores))])
            em_scores = compute_em_scores(inst)
            em_sel_f1s.append(sample_f1s[int(np.argmax(em_scores))])

    result = {
        "n_instances": n,
        "greedy_f1": float(np.mean(greedy_f1s)),
        "oracle_f1": float(np.mean(oracle_f1s)),
        "lp_sel_f1": float(np.mean(lp_sel_f1s)),
        "lp_delta_pp": float((np.mean(lp_sel_f1s) - np.mean(greedy_f1s)) * 100),
        "headroom_pp": float((np.mean(oracle_f1s) - np.mean(greedy_f1s)) * 100),
        "per_instance_greedy_f1": greedy_f1s,
        "per_instance_lp_sel_f1": lp_sel_f1s,
        "per_instance_oracle_f1": oracle_f1s,
    }
    if compute_slow_signals:
        result["sj_sel_f1"] = float(np.mean(sj_sel_f1s))
        result["em_sel_f1"] = float(np.mean(em_sel_f1s))
        result["sj_delta_pp"] = float((np.mean(sj_sel_f1s) - np.mean(greedy_f1s)) * 100)
        result["em_delta_pp"] = float((np.mean(em_sel_f1s) - np.mean(greedy_f1s)) * 100)
        result["per_instance_sj_sel_f1"] = sj_sel_f1s
        result["per_instance_em_sel_f1"] = em_sel_f1s
    return result


def paired_bootstrap_test(sel_f1s, greedy_f1s, n_boot=10000):
    deltas = np.array(sel_f1s) - np.array(greedy_f1s)
    n = len(deltas)
    observed_mean = float(np.mean(deltas))
    boot_means = np.zeros(n_boot)
    for b in range(n_boot):
        idx = RNG.randint(0, n, size=n)
        boot_means[b] = np.mean(deltas[idx])
    return {
        "mean_delta": observed_mean,
        "mean_delta_pp": observed_mean * 100,
        "ci_95": [float(np.percentile(boot_means, 2.5)) * 100,
                  float(np.percentile(boot_means, 97.5)) * 100],
        "p_value": float(np.mean(boot_means <= 0)),
        "n_instances": n,
    }


def compute_per_type_metrics(data):
    filtered = gold_filter(data)
    type_instances = defaultdict(list)
    for inst in filtered:
        gold = inst["gold"]
        gold_types = set(e["type"] for e in gold.get("entities", []))
        lp_scores = compute_lp_scores(inst)
        best_lp_idx = int(np.argmax(lp_scores))
        greedy_ents = inst["greedy"].get("entities", [])
        selected_ents = inst["samples"][best_lp_idx].get("entities", [])
        gold_ents = gold.get("entities", [])
        samples = inst["samples"]
        key_sets = [frozenset(_extract_surface_keys(s, "ner")) for s in samples]
        is_degenerate = (len(set(key_sets)) == 1)
        for etype in gold_types:
            gold_typed = [e for e in gold_ents if e["type"] == etype]
            greedy_typed = [e for e in greedy_ents if e["type"] == etype]
            selected_typed = [e for e in selected_ents if e["type"] == etype]
            g_f1 = _prf(*entity_strict_match(greedy_typed, gold_typed))["f1"]
            lp_f1 = _prf(*entity_strict_match(selected_typed, gold_typed))["f1"]
            sample_f1s = []
            for s in samples:
                s_typed = [e for e in s.get("entities", []) if e["type"] == etype]
                sample_f1s.append(_prf(*entity_strict_match(s_typed, gold_typed))["f1"])
            type_instances[etype].append({
                "greedy_f1": g_f1, "lp_sel_f1": lp_f1,
                "oracle_f1": max(sample_f1s),
                "lp_delta": lp_f1 - g_f1,
                "is_degenerate": is_degenerate,
                "max_lp": float(max(lp_scores)),
            })
    type_summary = {}
    for etype, instances in sorted(type_instances.items()):
        n = len(instances)
        deg_rate = sum(1 for x in instances if x["is_degenerate"]) / n
        greedy_mean = np.mean([x["greedy_f1"] for x in instances])
        lp_sel_mean = np.mean([x["lp_sel_f1"] for x in instances])
        lp_deltas = [x["lp_delta"] for x in instances]
        max_lps = [x["max_lp"] for x in instances]
        greedy_f1s = [x["greedy_f1"] for x in instances]
        rho, p = (spearmanr(max_lps, greedy_f1s) if len(set(greedy_f1s)) > 1 and len(set(max_lps)) > 1
                  else (0.0, 1.0))
        if hasattr(rho, 'statistic'):
            rho = rho.statistic
        type_summary[etype] = {
            "n_instances": n, "degeneracy_rate": float(deg_rate),
            "greedy_f1": float(greedy_mean), "lp_sel_f1": float(lp_sel_mean),
            "lp_delta_pp": float((lp_sel_mean - greedy_mean) * 100),
            "lp_rho": float(rho) if not isinstance(rho, tuple) else float(rho),
            "per_instance_lp_deltas": [float(d) for d in lp_deltas],
        }
    return type_summary


def run_task(task_name):
    if task_name == "w1":
        return task_w1()
    elif task_name == "w2":
        return task_w2()
    elif task_name == "i8":
        return task_i8()
    elif task_name == "i9":
        return task_i9()


def task_w1():
    print("W1: Multi-seed Table 3")
    results = {}
    for ds_name, ds_cfg in DATASETS.items():
        slow = ds_name not in ("fewnerd_n8",)  # skip SJ/EM for large datasets
        seed_results = {}
        for seed, path in sorted(ds_cfg["seeds"].items()):
            if not os.path.exists(path):
                print(f"  SKIP {ds_name} seed {seed}")
                continue
            print(f"  {ds_name} seed {seed}...", end=" ", flush=True)
            t0 = time.time()
            data = load_data(path)
            m = compute_seed_metrics(data, compute_slow_signals=slow)
            seed_results[seed] = m
            print(f"n={m['n_instances']}, greedy={m['greedy_f1']:.4f}, "
                  f"LP={m['lp_sel_f1']:.4f} (Δ={m['lp_delta_pp']:+.2f}pp) [{time.time()-t0:.1f}s]")
        if not seed_results:
            continue
        seeds = sorted(seed_results.keys())
        agg = {"seeds": seeds, "n_seeds": len(seeds)}
        metrics_to_agg = ["greedy_f1", "oracle_f1", "headroom_pp", "lp_sel_f1", "lp_delta_pp"]
        if slow:
            metrics_to_agg += ["sj_sel_f1", "em_sel_f1", "sj_delta_pp", "em_delta_pp"]
        for metric in metrics_to_agg:
            vals = [seed_results[s][metric] for s in seeds if metric in seed_results[s]]
            agg[metric] = {
                "mean": float(np.mean(vals)),
                "std": float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0,
                "per_seed": {str(s): seed_results[s][metric] for s in seeds if metric in seed_results[s]},
            }
        agg["n_instances"] = {str(s): seed_results[s]["n_instances"] for s in seeds}
        results[ds_name] = agg
    with open(f"{OUT_DIR}/w1_table3_multiseed.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {OUT_DIR}/w1_table3_multiseed.json")
    return results


def task_w2():
    print("W2: ICC + Permutation Test")
    path = DATASETS["scierc_n8"]["seeds"][42]
    data = load_data(path)
    type_summary = compute_per_type_metrics(data)
    types = sorted(type_summary.keys())
    
    # ICC
    groups = [type_summary[t]["per_instance_lp_deltas"] for t in types]
    k = len(groups)
    ns = [len(g) for g in groups]
    N = sum(ns)
    grand_mean = np.mean([v for g in groups for v in g])
    ss_between = sum(n * (np.mean(g) - grand_mean)**2 for g, n in zip(groups, ns))
    ss_within = sum(sum((v - np.mean(g))**2 for v in g) for g in groups)
    ms_between = ss_between / (k - 1) if k > 1 else 0
    ms_within = ss_within / (N - k) if (N - k) > 0 else 1e-10
    n0 = (N - sum(n**2 for n in ns) / N) / (k - 1) if k > 1 else 1
    denom = ms_between + (n0 - 1) * ms_within
    icc = float((ms_between - ms_within) / denom) if denom != 0 else 0.0

    # Permutation test
    deg_rates = np.array([type_summary[t]["degeneracy_rate"] for t in types])
    lp_rhos = np.array([type_summary[t]["lp_rho"] for t in types])
    obs_rho = float(spearmanr(deg_rates, lp_rhos).statistic) if k >= 3 else 0.0
    count = 0
    for _ in range(N_BOOTSTRAP):
        perm_rho = float(spearmanr(RNG.permutation(deg_rates), lp_rhos).statistic)
        if abs(perm_rho) >= abs(obs_rho):
            count += 1
    perm_p = (count + 1) / (N_BOOTSTRAP + 1)

    results = {
        "type_summary": {t: {k2: v for k2, v in type_summary[t].items()
                             if k2 != "per_instance_lp_deltas"}
                         for t in types},
        "icc": {"value": icc, "k_types": k, "N_total": N, "n0": float(n0),
                "ms_between": float(ms_between), "ms_within": float(ms_within)},
        "permutation_test": {"observed_rho": obs_rho, "p_value": float(perm_p),
                             "n_types": k, "n_perm": N_BOOTSTRAP},
    }
    for t in types:
        ts = type_summary[t]
        print(f"  {t}: n={ts['n_instances']}, deg={ts['degeneracy_rate']:.3f}, "
              f"LP_rho={ts['lp_rho']:.3f}, Δ={ts['lp_delta_pp']:+.2f}pp")
    print(f"  ICC={icc:.4f}, perm_p={perm_p:.4f} (rho={obs_rho:.4f})")
    with open(f"{OUT_DIR}/w2_icc_permutation.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {OUT_DIR}/w2_icc_permutation.json")
    return results


def task_i8():
    print("I8: Paired Bootstrap Tests")
    results = {}
    for ds_name in ["scierc_n8", "conll_n8", "fewnerd_n8"]:
        seed = sorted(DATASETS[ds_name]["seeds"].keys())[0]
        path = DATASETS[ds_name]["seeds"][seed]
        if not os.path.exists(path):
            continue
        print(f"  {ds_name}...", end=" ", flush=True)
        t0 = time.time()
        data = load_data(path)
        slow = ds_name != "fewnerd_n8"
        m = compute_seed_metrics(data, compute_slow_signals=slow)
        ds_r = {}
        for sig, key in [("LP", "per_instance_lp_sel_f1")]:
            boot = paired_bootstrap_test(m[key], m["per_instance_greedy_f1"], N_BOOTSTRAP)
            ds_r[sig] = boot
            print(f"LP Δ={boot['mean_delta_pp']:+.2f}pp CI=[{boot['ci_95'][0]:+.2f},{boot['ci_95'][1]:+.2f}] p={boot['p_value']:.4f}", end=" ")
        if slow:
            for sig, key in [("SJ", "per_instance_sj_sel_f1"), ("EM", "per_instance_em_sel_f1")]:
                boot = paired_bootstrap_test(m[key], m["per_instance_greedy_f1"], N_BOOTSTRAP)
                ds_r[sig] = boot
        boot_o = paired_bootstrap_test(m["per_instance_oracle_f1"], m["per_instance_greedy_f1"], N_BOOTSTRAP)
        ds_r["oracle"] = boot_o
        results[ds_name] = ds_r
        print(f"[{time.time()-t0:.1f}s]")
    with open(f"{OUT_DIR}/i8_bootstrap_tests.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {OUT_DIR}/i8_bootstrap_tests.json")
    return results


def task_i9():
    print("I9: Per-Type LP Heterogeneity")
    data = load_data(DATASETS["scierc_n8"]["seeds"][42])
    type_summary = compute_per_type_metrics(data)
    for etype, ts in type_summary.items():
        deltas = ts["per_instance_lp_deltas"]
        boot = paired_bootstrap_test([d for d in deltas], [0.0] * len(deltas), N_BOOTSTRAP)
        ts["bootstrap_p"] = boot["p_value"]
        ts["n_positive"] = sum(1 for d in deltas if d > 0)
        ts["n_negative"] = sum(1 for d in deltas if d < 0)
        ts["n_zero"] = sum(1 for d in deltas if d == 0)
    groups = [np.array(type_summary[t]["per_instance_lp_deltas"]) for t in sorted(type_summary)]
    stat, kw_p = kruskal(*groups) if len(groups) >= 2 else (0.0, 1.0)
    types_sorted = sorted(type_summary, key=lambda t: type_summary[t]["lp_delta_pp"], reverse=True)
    for t in types_sorted:
        ts = type_summary[t]
        print(f"  {t:25s}: Δ={ts['lp_delta_pp']:+.2f}pp, n={ts['n_instances']}, "
              f"boot_p={ts['bootstrap_p']:.4f}, +{ts['n_positive']}/-{ts['n_negative']}/={ts['n_zero']}")
    print(f"  KW: H={stat:.4f}, p={kw_p:.4f}")
    results = {
        "per_type": {t: {k2: v for k2, v in type_summary[t].items()
                         if k2 != "per_instance_lp_deltas"}
                     for t in types_sorted},
        "kruskal_wallis": {"statistic": float(stat), "p_value": float(kw_p), "n_types": len(groups)},
        "highest_gain_type": types_sorted[0],
        "lowest_gain_type": types_sorted[-1],
    }
    with open(f"{OUT_DIR}/i9_per_type_heterogeneity.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved: {OUT_DIR}/i9_per_type_heterogeneity.json")
    return results


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "all"
    t_start = time.time()
    if task == "all":
        for t in ["w1", "w2", "i8", "i9"]:
            run_task(t)
            print()
    else:
        run_task(task)
    print(f"Total: {time.time()-t_start:.1f}s")
