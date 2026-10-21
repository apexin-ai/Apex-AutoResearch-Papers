#!/usr/bin/env python3
"""DALS (Degeneracy-Aware LP Selection) evaluation with fixed tau=0.05 and bootstrap CI."""

import json
import numpy as np
import os

TAU = 0.05
N_BOOTSTRAP = 10000
RNG_SEED = 42

BASE = "/root/autodl-tmp/struct_self_consist_ie"

DATASETS = {
    "scierc_n8_seed42": "output/exp_012_rerun_1024/samples.jsonl",
    "scierc_n8_seed123": "output/exp_018_qwen_scierc_seed123/samples.jsonl",
    "scierc_n8_seed456": "output/exp_018_qwen_scierc_seed456/samples.jsonl",
    "scierc_n16_seed42": "output/exp001_n16_seed42/samples.jsonl",
    "scierc_n16_seed123": "output/exp001_n16_seed123/samples.jsonl",
    "scierc_n16_seed456": "output/exp001_n16_seed456/samples.jsonl",
    "conll_qwen_n8": "output/exp002_conll2003/samples.jsonl",
    "conll_llama_n8": "output/exp_017_llama_conll_infer/samples.jsonl",
    "fewnerd_n8": "output/exp_021_inference/samples.jsonl",
}


def compute_entity_f1(pred_entities, gold_entities):
    pred_set = {(e["text"], e["type"]) for e in pred_entities}
    gold_set = {(e["text"], e["type"]) for e in gold_entities}
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


def evaluate_dals(samples_path, tau=TAU, n_bootstrap=N_BOOTSTRAP):
    instances = []
    with open(samples_path) as f:
        for line in f:
            instances.append(json.loads(line))

    instances = [inst for inst in instances if len(inst["gold"]["entities"]) > 0]
    n = len(instances)

    greedy_f1s = np.zeros(n)
    lp_sel_f1s = np.zeros(n)
    dals_f1s = np.zeros(n)

    n_degen = 0
    n_nondegen = 0
    nondegen_lp_gains = []

    for i, inst in enumerate(instances):
        gold_ents = inst["gold"]["entities"]
        greedy_ents = inst["greedy"]["entities"]

        if "logprobs" in inst:
            sample_lps = inst["logprobs"]
        else:
            sample_lps = [s["mean_logprob"] for s in inst["samples"]]

        greedy_f1 = compute_entity_f1(greedy_ents, gold_ents)
        greedy_f1s[i] = greedy_f1

        best_idx = int(np.argmax(sample_lps))
        lp_best_ents = inst["samples"][best_idx]["entities"]
        lp_f1 = compute_entity_f1(lp_best_ents, gold_ents)
        lp_sel_f1s[i] = lp_f1

        lp_range = max(sample_lps) - min(sample_lps)

        if lp_range > tau:
            dals_f1s[i] = lp_f1
            n_nondegen += 1
            nondegen_lp_gains.append(lp_f1 - greedy_f1)
        else:
            dals_f1s[i] = greedy_f1
            n_degen += 1

    greedy_macro = greedy_f1s.mean() * 100
    lp_macro = lp_sel_f1s.mean() * 100
    dals_macro = dals_f1s.mean() * 100
    degen_rate = n_degen / n * 100

    diffs = dals_f1s - greedy_f1s
    rng = np.random.default_rng(RNG_SEED)
    boot_means = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        idx = rng.integers(0, n, size=n)
        boot_means[b] = diffs[idx].mean()
    boot_pp = boot_means * 100

    ci_lower = float(np.percentile(boot_pp, 2.5))
    ci_upper = float(np.percentile(boot_pp, 97.5))

    observed = diffs.mean()
    shifted = boot_means - observed
    p_value = float(np.mean(np.abs(shifted) >= np.abs(observed)))

    nondegen_lp_gain = float(np.mean(nondegen_lp_gains) * 100) if nondegen_lp_gains else 0.0

    return {
        "n_instances": n,
        "greedy_f1": round(greedy_macro, 4),
        "lp_sel_f1": round(lp_macro, 4),
        "dals_f1": round(dals_macro, 4),
        "dals_gain_pp": round(dals_macro - greedy_macro, 4),
        "degen_rate": round(degen_rate, 2),
        "non_degen_count": n_nondegen,
        "non_degen_lp_gain_pp": round(nondegen_lp_gain, 4),
        "bootstrap_ci_95": [round(ci_lower, 4), round(ci_upper, 4)],
        "bootstrap_p": round(p_value, 6),
    }


def main():
    results = {}

    for name, path in DATASETS.items():
        full_path = os.path.join(BASE, path)
        if not os.path.exists(full_path):
            print(f"SKIP {name}: not found")
            continue
        print(f"Evaluating {name}...", flush=True)
        result = evaluate_dals(full_path)
        results[name] = result
        print(
            f"  greedy={result['greedy_f1']:.2f}, LP={result['lp_sel_f1']:.2f}, "
            f"DALS={result['dals_f1']:.2f} (+{result['dals_gain_pp']:.2f}pp), "
            f"degen={result['degen_rate']:.1f}%, "
            f"CI=[{result['bootstrap_ci_95'][0]:.2f}, {result['bootstrap_ci_95'][1]:.2f}], "
            f"p={result['bootstrap_p']:.4f}",
            flush=True,
        )

    groups = {
        "scierc_n8": ["scierc_n8_seed42", "scierc_n8_seed123", "scierc_n8_seed456"],
        "scierc_n16": ["scierc_n16_seed42", "scierc_n16_seed123", "scierc_n16_seed456"],
    }

    aggregated = {}
    for group_name, keys in groups.items():
        available = [k for k in keys if k in results]
        if len(available) < 2:
            continue
        vals = {
            metric: [results[k][metric] for k in available]
            for metric in ["greedy_f1", "lp_sel_f1", "dals_f1", "dals_gain_pp", "degen_rate"]
        }
        agg = {}
        for metric, v in vals.items():
            agg[f"{metric}_mean"] = round(float(np.mean(v)), 4)
            agg[f"{metric}_std"] = round(float(np.std(v, ddof=1)), 4) if len(v) > 1 else 0.0
        agg["n_seeds"] = len(available)
        agg["seeds"] = available
        aggregated[group_name] = agg
        print(
            f"\n{group_name} ({len(available)} seeds):",
            f"\n  DALS F1 = {agg['dals_f1_mean']:.2f} +/- {agg['dals_f1_std']:.2f}",
            f"\n  DALS gain = {agg['dals_gain_pp_mean']:.2f} +/- {agg['dals_gain_pp_std']:.2f}pp",
            flush=True,
        )

    output = {
        "tau": TAU,
        "justification": "LP range ≈ 0 implies all samples have identical LP → no information → fall back to greedy. tau=0.05 is the natural boundary for non-tied instances.",
        "n_bootstrap": N_BOOTSTRAP,
        "results": results,
        "multi_seed_aggregation": aggregated,
    }

    out_path = os.path.join(BASE, "output/dals_hardening_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
