#!/usr/bin/env python3
"""F1 Scaling Law fitting: F1(N) = a - b * N^(-c) for all (model, dataset) configs."""

import json
import sys
import os
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1, entity_strict_match

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = f"{BASE}/artifacts/f1_scaling"
os.makedirs(OUT_DIR, exist_ok=True)

CONFIGS = {
    "Qwen_SciERC": {
        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
        "model": "Qwen2.5-7B",
        "dataset": "SciERC",
        "subtask": "ner",
        "max_N": 16,
        "extra_N32_path": f"{BASE}/output/exp_025_n32/samples.jsonl",
    },
    "Qwen_CoNLL": {
        "path": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
        "model": "Qwen2.5-7B",
        "dataset": "CoNLL2003",
        "subtask": "ner",
        "max_N": 16,
    },
    "Qwen_FewNERD": {
        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
        "model": "Qwen2.5-7B",
        "dataset": "FewNERD",
        "subtask": "ner",
        "max_N": 16,
    },
    "LLaMA_SciERC": {
        "path": f"{BASE}/output/exp_007_llama_n16/samples.jsonl",
        "model": "LLaMA-3.1-8B",
        "dataset": "SciERC",
        "subtask": "ner",
        "max_N": 16,
    },
    "LLaMA_CoNLL": {
        "path": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
        "model": "LLaMA-3.1-8B",
        "dataset": "CoNLL2003",
        "subtask": "ner",
        "max_N": 16,
    },
    "LLaMA_FewNERD": {
        "path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
        "model": "LLaMA-3.1-8B",
        "dataset": "FewNERD",
        "subtask": "ner",
        "max_N": 8,
    },
}

N_REPEATS = 20


def scaling_law(N, a, b, c):
    return a - b * np.power(N, -c)


def micro_f1_from_preds(preds, golds, subtask="ner"):
    tp = fp = fn = 0
    for pred, gold in zip(preds, golds):
        t, f_p, f_n = entity_strict_match(
            pred.get("entities", []), gold.get("entities", [])
        )
        tp += t
        fp += f_p
        fn += f_n
    p = tp / (tp + fp) if (tp + fp) else 0
    r = tp / (tp + fn) if (tp + fn) else 0
    return 2 * p * r / (p + r) if (p + r) else 0


def compute_oracle_f1_at_N(instances, N_target, source_N, n_repeats=20, subtask="ner"):
    if N_target >= source_N:
        oracle_preds = []
        golds = []
        for inst in instances:
            gold = inst["gold"]
            samples = inst["samples"][:N_target]
            sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in samples]
            oracle_preds.append(samples[int(np.argmax(sample_f1s))])
            golds.append(gold)
        return micro_f1_from_preds(oracle_preds, golds, subtask), 0.0

    trial_f1s = []
    for seed in range(n_repeats):
        rng = np.random.RandomState(seed)
        oracle_preds = []
        golds = []
        for inst in instances:
            gold = inst["gold"]
            all_samples = inst["samples"]
            indices = rng.choice(source_N, size=N_target, replace=False)
            subset = [all_samples[i] for i in indices]
            sample_f1s = [per_instance_f1(s, gold, subtask=subtask) for s in subset]
            oracle_preds.append(subset[int(np.argmax(sample_f1s))])
            golds.append(gold)
        trial_f1s.append(micro_f1_from_preds(oracle_preds, golds, subtask))

    return float(np.mean(trial_f1s)), float(np.std(trial_f1s))


def compute_greedy_f1(instances, subtask="ner"):
    greedy_preds = []
    golds = []
    for inst in instances:
        greedy_preds.append(inst.get("greedy", inst["samples"][0]))
        golds.append(inst["gold"])
    return micro_f1_from_preds(greedy_preds, golds, subtask)


def fit_scaling_law(N_values, F1_values):
    """Fit F1(N) = a - b * N^(-c)."""
    N_arr = np.array(N_values, dtype=float)
    F1_arr = np.array(F1_values, dtype=float)

    a_init = min(max(F1_arr) + 0.03, 0.999)
    b_init = a_init - min(F1_arr)
    c_init = 0.4

    try:
        popt, pcov = curve_fit(
            scaling_law, N_arr, F1_arr,
            p0=[a_init, b_init, c_init],
            bounds=([max(F1_arr), 0, 0.01], [1.0, 1.0, 5.0]),
            maxfev=50000,
        )
        a, b, c = popt
        perr = np.sqrt(np.diag(pcov))
        F1_pred = scaling_law(N_arr, *popt)
        residuals = F1_arr - F1_pred
        ss_res = np.sum(residuals ** 2)
        ss_tot = np.sum((F1_arr - np.mean(F1_arr)) ** 2)
        R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
        return {
            "a": float(a), "b": float(b), "c": float(c),
            "a_se": float(perr[0]), "b_se": float(perr[1]), "c_se": float(perr[2]),
            "R2": float(R2),
            "residuals": [float(r) for r in residuals],
            "fitted_values": [float(v) for v in F1_pred],
        }
    except Exception as e:
        return {"error": str(e)}


def main():
    all_results = {}
    plot_data = {}

    for config_name, cfg in CONFIGS.items():
        print(f"\n{'='*60}")
        print(f"Processing: {config_name} ({cfg['model']} / {cfg['dataset']})")
        print(f"{'='*60}")

        with open(cfg["path"]) as f:
            data = [json.loads(line) for line in f if line.strip()]

        instances = [d for d in data if len(d["gold"].get("entities", [])) > 0]
        source_N = cfg["max_N"]
        print(f"  Loaded {len(instances)} gold-filtered instances, source_N={source_N}")

        N_values = []
        n = 1
        while n <= source_N:
            N_values.append(n)
            n *= 2

        extra_n32_instances = None
        if "extra_N32_path" in cfg:
            with open(cfg["extra_N32_path"]) as f:
                extra_data = [json.loads(line) for line in f if line.strip()]
            extra_n32_instances = [d for d in extra_data if len(d["gold"].get("entities", [])) > 0]
            N_values.append(32)
            print(f"  Also loaded N=32 data: {len(extra_n32_instances)} instances")

        greedy_f1 = compute_greedy_f1(instances, cfg["subtask"])
        print(f"  Greedy F1: {greedy_f1:.4f}")

        oracle_results = {}
        for N in N_values:
            if N == 32 and extra_n32_instances is not None:
                f1_mean, f1_std = compute_oracle_f1_at_N(
                    extra_n32_instances, 32, 32, n_repeats=1, subtask=cfg["subtask"]
                )
            else:
                f1_mean, f1_std = compute_oracle_f1_at_N(
                    instances, N, source_N, n_repeats=N_REPEATS, subtask=cfg["subtask"]
                )
            oracle_results[N] = {"mean": f1_mean, "std": f1_std}
            print(f"  Oracle F1 @ N={N:2d}: {f1_mean:.4f} (+-{f1_std:.4f})")

        N_arr = np.array(sorted(oracle_results.keys()))
        F1_arr = np.array([oracle_results[n]["mean"] for n in N_arr])

        fit_result = fit_scaling_law(N_arr, F1_arr)

        if "error" not in fit_result:
            print(f"\n  Fitted: F1(N) = {fit_result['a']:.4f} - {fit_result['b']:.4f} * N^(-{fit_result['c']:.4f})")
            print(f"  R2 = {fit_result['R2']:.6f}")
            print(f"  c = {fit_result['c']:.4f} +- {fit_result['c_se']:.4f}")
        else:
            print(f"  FIT FAILED: {fit_result['error']}")

        all_results[config_name] = {
            "model": cfg["model"],
            "dataset": cfg["dataset"],
            "n_instances": len(instances),
            "greedy_f1": greedy_f1,
            "N_values": [int(n) for n in N_arr],
            "oracle_f1_mean": [oracle_results[n]["mean"] for n in N_arr],
            "oracle_f1_std": [oracle_results[n]["std"] for n in N_arr],
            "fit": fit_result,
        }

        plot_data[config_name] = {
            "model": cfg["model"],
            "dataset": cfg["dataset"],
            "N": [int(n) for n in N_arr],
            "oracle_f1": [oracle_results[n]["mean"] for n in N_arr],
            "oracle_f1_std": [oracle_results[n]["std"] for n in N_arr],
            "greedy_f1": greedy_f1,
            "fit_a": fit_result.get("a"),
            "fit_b": fit_result.get("b"),
            "fit_c": fit_result.get("c"),
            "fit_R2": fit_result.get("R2"),
        }

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY: c-value distribution")
    print(f"{'='*60}")
    c_values = {}
    for name, res in all_results.items():
        if "error" not in res["fit"]:
            c = res["fit"]["c"]
            c_se = res["fit"]["c_se"]
            R2 = res["fit"]["R2"]
            c_values[name] = c
            print(f"  {name:20s}: c={c:.4f} +-{c_se:.4f}, R2={R2:.4f}")

    if c_values:
        c_arr = np.array(list(c_values.values()))
        print(f"\n  c mean = {np.mean(c_arr):.4f}")
        print(f"  c std  = {np.std(c_arr):.4f}")
        print(f"  c range= [{np.min(c_arr):.4f}, {np.max(c_arr):.4f}]")
        print(f"  All c < 0.5? {all(c < 0.5 for c in c_arr)}")

        for ds in ["SciERC", "CoNLL", "FewNERD"]:
            ds_c = [c for name, c in c_values.items() if ds in name]
            if ds_c:
                print(f"  {ds:10s}: c_mean={np.mean(ds_c):.4f} (n={len(ds_c)})")

        print(f"\n  Wang et al. 2023 reference: c ~ 0.5-0.7 (reasoning tasks)")
        print(f"  Our structured IE: c_mean = {np.mean(c_arr):.4f}")
        if np.mean(c_arr) < 0.5:
            print(f"  => Structured IE scales SLOWER than reasoning")
        else:
            print(f"  => Comparable or higher than reasoning tasks")

    # Save
    with open(f"{OUT_DIR}/scaling_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved: {OUT_DIR}/scaling_results.json")

    with open(f"{OUT_DIR}/scaling_plot_data.json", "w") as f:
        json.dump(plot_data, f, indent=2)
    print(f"Saved: {OUT_DIR}/scaling_plot_data.json")


if __name__ == "__main__":
    main()
