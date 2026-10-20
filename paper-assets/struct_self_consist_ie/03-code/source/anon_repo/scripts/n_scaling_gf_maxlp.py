#!/usr/bin/env python3
"""N-scaling table recomputation with gold-filtered + max_LP protocol."""

import json
import sys
import time
from collections import Counter

import numpy as np

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _extract_surface_keys,
)
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_025_n32/samples.jsonl"
N_VALUES = [2, 4, 8, 16, 32]
SUBTASK = "ner"
ENTITY_KEY = "entities"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_sj_scores(samples, subtask="ner"):
    N = len(samples)
    pair_fn = _ner_soft_jaccard_pair
    field = "entities"
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = pair_fn(samples[i].get(field, []), samples[j].get(field, []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_fk_scores(samples, subtask="ner"):
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


def compute_vc_scores(key_sets, N):
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


def compute_em_scores(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_lp_scores(samples):
    lps = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def is_degenerate(samples, field="entities"):
    ref = frozenset((e.get("text",""), e.get("type","")) for e in samples[0].get(field, []))
    for s in samples[1:]:
        cur = frozenset((e.get("text",""), e.get("type","")) for e in s.get(field, []))
        if cur != ref:
            return False
    return True


def main():
    print("Loading data...")
    instances = load_data(DATA_PATH)
    print(f"  Total instances: {len(instances)}")

    # Gold filter
    valid = [inst for inst in instances if len(inst["gold"].get(ENTITY_KEY, [])) > 0]
    n_gf = len(valid)
    print(f"  Gold-filtered: {n_gf} (excluded {len(instances) - n_gf})")

    results = {}

    for N in N_VALUES:
        print(f"\n=== N={N} ===")
        t0 = time.time()

        greedy_f1s = []
        oracle_f1s = []
        signal_f1s = {"LP": [], "SJ": [], "FK": [], "EM": [], "VC": []}
        n_degen = 0

        for idx, inst in enumerate(valid):
            gold = inst["gold"]
            samples = inst["samples"][:N]
            greedy = inst["greedy"]

            # Per-sample F1
            sample_f1_vals = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]
            greedy_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
            greedy_f1s.append(greedy_f1)
            oracle_f1s.append(max(sample_f1_vals))

            # Degeneracy
            if is_degenerate(samples, field=ENTITY_KEY):
                n_degen += 1

            # LP selection (max mean_logprob)
            lp_scores = compute_lp_scores(samples)
            signal_f1s["LP"].append(sample_f1_vals[int(np.argmax(lp_scores))])

            # SJ
            sj_scores = compute_sj_scores(samples, SUBTASK)
            signal_f1s["SJ"].append(sample_f1_vals[int(np.argmax(sj_scores))])

            # FK + surface keys
            fk_scores, key_sets = compute_fk_scores(samples, SUBTASK)
            signal_f1s["FK"].append(sample_f1_vals[int(np.argmax(fk_scores))])

            # VC
            vc_scores = compute_vc_scores(key_sets, N)
            signal_f1s["VC"].append(sample_f1_vals[int(np.argmax(vc_scores))])

            # EM
            em_scores = compute_em_scores(key_sets)
            signal_f1s["EM"].append(sample_f1_vals[int(np.argmax(em_scores))])

        elapsed = time.time() - t0

        greedy_mean = np.mean(greedy_f1s)
        oracle_mean = np.mean(oracle_f1s)
        degen_pct = n_degen / n_gf * 100

        # Compute Spearman rho between LP scores and sample F1 (across all samples)
        # We'll compute instance-level: LP score vs sample F1 across the N samples
        # Actually for the table we just need selection delta, not rho.
        # But let's also compute LP rho for completeness.

        result = {
            "N": N,
            "n_gf": n_gf,
            "greedy_f1": float(greedy_mean),
            "oracle_f1": float(oracle_mean),
            "oracle_headroom_pp": float((oracle_mean - greedy_mean) * 100),
            "degen_pct": float(degen_pct),
            "elapsed_s": float(elapsed),
        }

        print(f"  greedy_f1:  {greedy_mean:.4f}")
        print(f"  oracle_f1:  {oracle_mean:.4f}")
        print(f"  headroom:   +{(oracle_mean - greedy_mean)*100:.1f} pp")
        print(f"  degen%:     {degen_pct:.1f}%")

        for sig in ["LP", "SJ", "FK", "EM", "VC"]:
            sel_mean = np.mean(signal_f1s[sig])
            delta = (sel_mean - greedy_mean) * 100
            result[f"{sig}_sel_f1"] = float(sel_mean)
            result[f"{sig}_delta_pp"] = float(delta)
            print(f"  {sig}: sel_f1={sel_mean:.4f}  delta={delta:+.2f} pp")

        # Best delta
        best_sig = max(["LP", "SJ", "FK", "EM", "VC"], key=lambda s: result[f"{s}_delta_pp"])
        result["best_signal"] = best_sig
        result["best_delta_pp"] = result[f"{best_sig}_delta_pp"]
        print(f"  Best: {best_sig} ({result['best_delta_pp']:+.2f} pp)")
        print(f"  Time: {elapsed:.1f}s")

        results[f"N={N}"] = result

    # Save results
    out_path = "/root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print("\n" + "="*80)
    print("SUMMARY TABLE (gold-filtered, max_LP)")
    print("="*80)
    print(f"{'N':>4} {'n_gf':>5} {'greedy':>7} {'oracle':>7} {'head':>7} {'degen%':>7} {'LP':>8} {'SJ':>8} {'FK':>8} {'EM':>8} {'VC':>8} {'Best':>8}")
    for N in N_VALUES:
        r = results[f"N={N}"]
        print(f"{N:>4} {r['n_gf']:>5} {r['greedy_f1']:.4f} {r['oracle_f1']:.4f} +{r['oracle_headroom_pp']:.1f} {r['degen_pct']:>6.1f}% {r['LP_delta_pp']:>+7.2f} {r['SJ_delta_pp']:>+7.2f} {r['FK_delta_pp']:>+7.2f} {r['EM_delta_pp']:>+7.2f} {r['VC_delta_pp']:>+7.2f} {r['best_delta_pp']:>+7.2f}")


if __name__ == "__main__":
    main()
