#!/usr/bin/env python3
"""Bootstrap significance test for N=32 LP selection improvement.

Tests whether selection by each signal (LP, SJ, FK, EM, VC) yields
statistically significant improvement over greedy decoding, using
paired bootstrap resampling and permutation tests.
"""

import json
import sys
import numpy as np
from collections import Counter

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
DATA_PATH = f"{BASE}/output/exp_025_n32/samples.jsonl"
OUT_PATH = f"{BASE}/output/exp_025_n32/bootstrap_results.json"
SCRIPT_PATH = f"{BASE}/output/exp_025_n32/bootstrap_selection_test.py"
SUBTASK = "ner"
SIGNALS = ["LP", "SJ", "FK", "EM", "VC"]
B = 10000
SEED = 42


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_signals(samples):
    n = len(samples)

    # LP
    lp_scores = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lp_scores.append(lp)

    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]

    # FK (Fleiss Kappa-like pairwise Jaccard on surface keys)
    fk_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            fk_matrix[i][j] = s
            fk_matrix[j][i] = s
    np.fill_diagonal(fk_matrix, 1.0)
    fk_scores = [float(np.mean([fk_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

    # SJ (Soft Jaccard)
    sj_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            sj_matrix[i][j] = s
            sj_matrix[j][i] = s
    np.fill_diagonal(sj_matrix, 1.0)
    sj_scores = [float(np.mean([sj_matrix[k][j] for j in range(n) if j != k])) for k in range(n)]

    # VC (Vote Count)
    all_keys_count = Counter()
    for ks in key_sets:
        for key in ks:
            all_keys_count[key] += 1
    vc_scores = []
    for ks in key_sets:
        if not ks:
            vc_scores.append(0.0)
        else:
            fracs = [all_keys_count[key] / n for key in ks]
            vc_scores.append(float(np.mean(fracs)))

    # EM (Exact Match count)
    em_scores = [float(sum(1 for j in range(n) if j != k and key_sets[k] == key_sets[j])) for k in range(n)]

    return {"LP": lp_scores, "SJ": sj_scores, "FK": fk_scores, "EM": em_scores, "VC": vc_scores}


def main():
    rng = np.random.RandomState(SEED)
    instances = load_data(DATA_PATH)

    # Filter gold-empty instances
    instances = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]
    N = len(instances)
    print(f"Loaded {N} instances (gold-non-empty)")

    # Per-instance F1 arrays
    greedy_f1 = np.zeros(N)
    signal_selected_f1 = {sig: np.zeros(N) for sig in SIGNALS}
    oracle_f1 = np.zeros(N)
    random_f1 = np.zeros(N)  # for permutation test baseline

    for i, inst in enumerate(instances):
        gold = inst["gold"]
        greedy = inst.get("greedy", inst["samples"][0])
        samples = inst["samples"][:32]

        greedy_f1[i] = per_instance_f1(greedy, gold, SUBTASK)

        sample_f1s = np.array([per_instance_f1(s, gold, SUBTASK) for s in samples])
        oracle_f1[i] = sample_f1s.max()

        # Random baseline: pick a random sample
        random_f1[i] = sample_f1s[rng.randint(len(samples))]

        # Signal-based selection
        signals = compute_signals(samples)
        for sig in SIGNALS:
            best_idx = int(np.argmax(signals[sig]))
            signal_selected_f1[sig][i] = sample_f1s[best_idx]

        if (i + 1) % 100 == 0:
            print(f"  Processed {i+1}/{N}")

    # Point estimates
    greedy_macro = greedy_f1.mean()
    oracle_macro = oracle_f1.mean()
    print(f"\nPoint estimates:")
    print(f"  Greedy macro F1:  {greedy_macro:.4f}")
    print(f"  Oracle macro F1:  {oracle_macro:.4f}")
    for sig in SIGNALS:
        sel_macro = signal_selected_f1[sig].mean()
        delta = (sel_macro - greedy_macro) * 100
        print(f"  {sig} selection F1: {sel_macro:.4f} (Δ = {delta:+.2f}pp)")

    # =========================================================================
    # Bootstrap resampling
    # =========================================================================
    print(f"\nBootstrap resampling (B={B})...")
    bootstrap_deltas = {sig: np.zeros(B) for sig in SIGNALS}
    bootstrap_oracle_deltas = np.zeros(B)

    for b in range(B):
        idx = rng.choice(N, size=N, replace=True)
        g_mean = greedy_f1[idx].mean()
        bootstrap_oracle_deltas[b] = oracle_f1[idx].mean() - g_mean
        for sig in SIGNALS:
            bootstrap_deltas[sig][b] = signal_selected_f1[sig][idx].mean() - g_mean

    results = {"n_instances": N, "B": B, "greedy_macro_f1": float(greedy_macro),
               "oracle_macro_f1": float(oracle_macro), "signals": {}}

    print(f"\n{'Signal':<6} | {'Mean Δ (pp)':>11} | {'95% CI':>16} | {'p-value':>10} | Sig?")
    print("-" * 70)

    for sig in SIGNALS:
        deltas = bootstrap_deltas[sig]
        mean_delta = deltas.mean() * 100
        std_delta = deltas.std() * 100
        ci_lo = np.percentile(deltas, 2.5) * 100
        ci_hi = np.percentile(deltas, 97.5) * 100
        # p-value: proportion of bootstrap deltas <= 0 (one-sided)
        p_value = float(np.mean(deltas <= 0))
        significant = p_value < 0.05

        results["signals"][sig] = {
            "mean_delta_pp": round(mean_delta, 4),
            "std_delta_pp": round(std_delta, 4),
            "ci_95_lo_pp": round(ci_lo, 4),
            "ci_95_hi_pp": round(ci_hi, 4),
            "p_value_bootstrap": round(p_value, 6),
            "significant_005": significant,
            "selection_macro_f1": float(signal_selected_f1[sig].mean()),
        }

        sig_mark = "Yes ***" if p_value < 0.001 else ("Yes **" if p_value < 0.01 else ("Yes *" if p_value < 0.05 else "No"))
        print(f"{sig:<6} | {mean_delta:+11.4f} | [{ci_lo:+.4f}, {ci_hi:+.4f}] | {p_value:10.6f} | {sig_mark}")

    # Oracle
    mean_od = bootstrap_oracle_deltas.mean() * 100
    ci_lo_od = np.percentile(bootstrap_oracle_deltas, 2.5) * 100
    ci_hi_od = np.percentile(bootstrap_oracle_deltas, 97.5) * 100
    p_od = float(np.mean(bootstrap_oracle_deltas <= 0))
    print(f"{'Oracle':<6} | {mean_od:+11.4f} | [{ci_lo_od:+.4f}, {ci_hi_od:+.4f}] | {p_od:10.6f} | {'Yes ***' if p_od < 0.001 else 'No'}")
    results["oracle"] = {
        "mean_delta_pp": round(mean_od, 4),
        "ci_95_lo_pp": round(ci_lo_od, 4),
        "ci_95_hi_pp": round(ci_hi_od, 4),
        "p_value_bootstrap": round(p_od, 6),
    }

    # =========================================================================
    # Paired permutation test (vs random selection)
    # =========================================================================
    print(f"\n{'='*70}")
    print(f"Paired Permutation Test (H0: signal selection = random selection)")
    print(f"{'='*70}")

    N_PERM = 10000
    results["permutation_test"] = {}

    print(f"\n{'Signal':<6} | {'Obs Δ (pp)':>10} | {'p-value':>10} | Sig?")
    print("-" * 50)

    for sig in SIGNALS:
        # Observed: signal_selected - random (per instance)
        obs_diff = signal_selected_f1[sig] - random_f1
        obs_stat = obs_diff.mean()

        # Permutation: for each instance, randomly swap signal_selected and random
        perm_stats = np.zeros(N_PERM)
        for p in range(N_PERM):
            signs = rng.choice([-1, 1], size=N)
            perm_stats[p] = (signs * obs_diff).mean()

        p_perm = float(np.mean(perm_stats >= obs_stat))
        significant = p_perm < 0.05

        results["permutation_test"][sig] = {
            "obs_delta_pp": round(obs_stat * 100, 4),
            "p_value_permutation": round(p_perm, 6),
            "significant_005": significant,
        }

        sig_mark = "Yes ***" if p_perm < 0.001 else ("Yes **" if p_perm < 0.01 else ("Yes *" if p_perm < 0.05 else "No"))
        print(f"{sig:<6} | {obs_stat*100:+10.4f} | {p_perm:10.6f} | {sig_mark}")

    # =========================================================================
    # Additional: Bootstrap CI for LP vs second-best signal (FK)
    # =========================================================================
    print(f"\n{'='*70}")
    print("Pairwise signal comparison (LP vs FK)")
    print(f"{'='*70}")

    lp_vs_fk = np.zeros(B)
    for b in range(B):
        idx = rng.choice(N, size=N, replace=True)
        lp_vs_fk[b] = signal_selected_f1["LP"][idx].mean() - signal_selected_f1["FK"][idx].mean()
    mean_diff = lp_vs_fk.mean() * 100
    ci_lo_d = np.percentile(lp_vs_fk, 2.5) * 100
    ci_hi_d = np.percentile(lp_vs_fk, 97.5) * 100
    p_lp_fk = float(np.mean(lp_vs_fk <= 0))
    print(f"LP - FK: {mean_diff:+.4f}pp, 95% CI [{ci_lo_d:+.4f}, {ci_hi_d:+.4f}], p={p_lp_fk:.6f}")
    results["lp_vs_fk"] = {
        "mean_delta_pp": round(mean_diff, 4),
        "ci_95_lo_pp": round(ci_lo_d, 4),
        "ci_95_hi_pp": round(ci_hi_d, 4),
        "p_value": round(p_lp_fk, 6),
    }

    # Save
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
