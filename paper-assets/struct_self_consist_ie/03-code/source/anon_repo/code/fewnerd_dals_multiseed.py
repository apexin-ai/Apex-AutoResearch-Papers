#!/usr/bin/env python3
"""Few-NERD DALS: 3-seed bootstrap + tau sensitivity."""

import json
import numpy as np
import os

BASE = "/root/autodl-tmp/struct_self_consist_ie"
SAMPLES_PATH = os.path.join(BASE, "output/exp_027_fewnerd_n16/samples.jsonl")
OUTPUT_PATH = os.path.join(BASE, "output/fewnerd_dals_multiseed_results.json")

BOOTSTRAP_SEEDS = [42, 123, 456]
N_BOOTSTRAP = 10000
TAU_VALUES = [0.01, 0.03, 0.05, 0.10, 0.15, 0.20]


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


def load_instances(path):
    instances = []
    with open(path) as f:
        for line in f:
            instances.append(json.loads(line))
    return [inst for inst in instances if len(inst["gold"]["entities"]) > 0]


def compute_per_instance(instances):
    n = len(instances)
    greedy_f1s = np.zeros(n)
    lp_sel_f1s = np.zeros(n)
    lp_ranges = np.zeros(n)

    for i, inst in enumerate(instances):
        gold_ents = inst["gold"]["entities"]
        greedy_ents = inst["greedy"]["entities"]

        if "logprobs" in inst:
            sample_lps = inst["logprobs"]
        else:
            sample_lps = [s["mean_logprob"] for s in inst["samples"]]

        greedy_f1s[i] = compute_entity_f1(greedy_ents, gold_ents)

        best_idx = int(np.argmax(sample_lps))
        lp_best_ents = inst["samples"][best_idx]["entities"]
        lp_sel_f1s[i] = compute_entity_f1(lp_best_ents, gold_ents)

        lp_ranges[i] = max(sample_lps) - min(sample_lps)

    return greedy_f1s, lp_sel_f1s, lp_ranges


def dals_select(greedy_f1s, lp_sel_f1s, lp_ranges, tau):
    mask = lp_ranges > tau
    dals_f1s = np.where(mask, lp_sel_f1s, greedy_f1s)
    return dals_f1s, mask


def bootstrap_test(dals_f1s, greedy_f1s, seed, n_bootstrap=N_BOOTSTRAP):
    diffs = dals_f1s - greedy_f1s
    n = len(diffs)
    rng = np.random.default_rng(seed)
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

    return {
        "dals_gain_pp": round(float(diffs.mean() * 100), 4),
        "ci_95": [round(ci_lower, 4), round(ci_upper, 4)],
        "p_value": round(p_value, 6),
    }


def main():
    print("Loading instances...", flush=True)
    instances = load_instances(SAMPLES_PATH)
    n = len(instances)
    print(f"  Gold-filtered: {n} instances", flush=True)

    greedy_f1s, lp_sel_f1s, lp_ranges = compute_per_instance(instances)
    greedy_macro = float(greedy_f1s.mean() * 100)
    lp_macro = float(lp_sel_f1s.mean() * 100)

    # Task 1: 3-seed bootstrap at tau=0.05
    print("\n=== Task 1: 3-seed bootstrap (tau=0.05) ===", flush=True)
    tau = 0.05
    dals_f1s, mask = dals_select(greedy_f1s, lp_sel_f1s, lp_ranges, tau)
    dals_macro = float(dals_f1s.mean() * 100)

    seed_results = {}
    for seed in BOOTSTRAP_SEEDS:
        res = bootstrap_test(dals_f1s, greedy_f1s, seed)
        res["dals_f1"] = round(dals_macro, 4)
        seed_results[str(seed)] = res
        print(f"  seed={seed}: gain={res['dals_gain_pp']:+.4f}pp, "
              f"CI=[{res['ci_95'][0]:.4f}, {res['ci_95'][1]:.4f}], "
              f"p={res['p_value']:.4f}", flush=True)

    gains = [seed_results[str(s)]["dals_gain_pp"] for s in BOOTSTRAP_SEEDS]
    mean_gain = round(float(np.mean(gains)), 4)
    std_gain = round(float(np.std(gains, ddof=1)), 4) if len(gains) > 1 else 0.0

    task1 = {
        "dataset": "Few-NERD",
        "source": "exp_027_fewnerd_n16",
        "tau": tau,
        "n_instances_gold_filtered": n,
        "greedy_f1": round(greedy_macro, 4),
        "lp_sel_f1": round(lp_macro, 4),
        "dals_f1": round(dals_macro, 4),
        "n_lp_selected": int(mask.sum()),
        "pct_lp_selected": round(float(mask.mean() * 100), 2),
        "seeds": seed_results,
        "mean_gain_pp": mean_gain,
        "std_gain_pp": std_gain,
    }

    print(f"\n  Summary: DALS F1={dals_macro:.4f}, gain={mean_gain:+.4f}pp (std={std_gain:.4f})")
    print(f"  Greedy F1={greedy_macro:.4f}, LP F1={lp_macro:.4f}")
    print(f"  LP selected: {int(mask.sum())}/{n} ({mask.mean()*100:.1f}%)")

    # Task 2: tau sensitivity
    print("\n=== Task 2: tau sensitivity ===", flush=True)
    tau_results = []
    for tau_val in TAU_VALUES:
        dals_f1s_t, mask_t = dals_select(greedy_f1s, lp_sel_f1s, lp_ranges, tau_val)
        dals_f1_t = float(dals_f1s_t.mean() * 100)
        gain_greedy = dals_f1_t - greedy_macro
        gain_lp = dals_f1_t - lp_macro
        n_lp = int(mask_t.sum())
        pct_lp = float(mask_t.mean() * 100)

        row = {
            "tau": tau_val,
            "dals_f1": round(dals_f1_t, 4),
            "gain_vs_greedy_pp": round(gain_greedy, 4),
            "gain_vs_lp_pp": round(gain_lp, 4),
            "pct_lp_selected": round(pct_lp, 2),
            "n_lp_selected": n_lp,
            "n_total": n,
        }
        tau_results.append(row)
        print(f"  tau={tau_val:.2f}: DALS={dals_f1_t:.4f}, "
              f"+{gain_greedy:.4f}pp vs greedy, {gain_lp:+.4f}pp vs LP, "
              f"LP_sel={n_lp}/{n} ({pct_lp:.1f}%)", flush=True)

    task2 = {
        "dataset": "Few-NERD",
        "source": "exp_027_fewnerd_n16",
        "greedy_f1": round(greedy_macro, 4),
        "lp_sel_f1": round(lp_macro, 4),
        "results": tau_results,
    }

    output = {
        "task1_multiseed": task1,
        "task2_tau_sensitivity": task2,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
