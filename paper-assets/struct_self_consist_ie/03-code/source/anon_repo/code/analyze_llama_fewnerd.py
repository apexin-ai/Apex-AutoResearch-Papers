#!/usr/bin/env python3
"""LLaMA Few-NERD full signal analysis: degeneracy, selection F1, within-instance rho, DALS."""
import json, os, sys, time
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_llama_fewnerd_n8_seed42/samples.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_llama_fewnerd_n8_seed42"
SUBTASK = "ner"
TAU = 0.05

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)


def entity_set(entities):
    return {(e.get("text",""), e.get("type","")) for e in entities}


def f1_score_set(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0
    if not pred_set or not gold_set:
        return 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set) if pred_set else 0
    r = tp / len(gold_set) if gold_set else 0
    return 2*p*r/(p+r) if (p+r) > 0 else 0.0


def compute_sample_sj_scores(inst):
    samples = inst["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(samples[i].get("entities", []), samples[j].get("entities", []))
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(inst):
    samples = inst["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]
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


def compute_sample_logprobs(inst):
    lps = []
    for s in inst["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def main():
    t0 = time.time()
    print("Loading data...")
    data = []
    with open(DATA_PATH) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    N_per = len(data[0]["samples"])
    print(f"Loaded {len(data)} instances, N={N_per}")

    gold_filtered = [inst for inst in data if len(inst["gold"].get("entities", [])) > 0]
    n_gf = len(gold_filtered)
    print(f"Gold-filtered: {n_gf}/{len(data)}")

    # Phase 1: CF1 degeneracy + selection F1 + LP range (gold-filtered)
    print("\nPhase 1: Degeneracy + Selection F1 + LP range...")
    n_constant_f1 = 0
    all_greedy_f1 = []
    all_oracle_f1 = []
    all_random_f1 = []
    all_sample_f1_matrix = []
    signal_sel_f1 = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP"]}
    lp_ranges = []

    for idx, inst in enumerate(gold_filtered):
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]

        all_greedy_f1.append(g_f1)
        all_oracle_f1.append(max(sample_f1s))
        all_random_f1.append(float(np.mean(sample_f1s)))
        all_sample_f1_matrix.append(sample_f1s)

        if len(set(round(f, 10) for f in sample_f1s)) == 1:
            n_constant_f1 += 1

        sj_scores = compute_sample_sj_scores(inst)
        fk_scores, key_sets = compute_sample_surface_scores(inst)
        vc_scores = compute_sample_voting_conf(key_sets, N_per)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        all_scores = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores,
                      "EM": em_scores, "LP": lp_scores}

        for sig in signal_sel_f1:
            chosen = int(np.argmax(all_scores[sig]))
            signal_sel_f1[sig].append(sample_f1s[chosen])

        valid_lps = [lp for lp in lp_scores if np.isfinite(lp) and lp > -900]
        if len(valid_lps) >= 2:
            lp_ranges.append(max(valid_lps) - min(valid_lps))

        if (idx + 1) % 2000 == 0:
            print(f"  processed {idx+1}/{n_gf}")

    degeneracy = n_constant_f1 / n_gf
    greedy_arr = np.array(all_greedy_f1)
    oracle_arr = np.array(all_oracle_f1)

    print(f"Degeneracy (CF1): {degeneracy:.4f} ({n_constant_f1}/{n_gf})")
    print(f"Greedy F1: {greedy_arr.mean():.4f}")
    print(f"Oracle F1: {oracle_arr.mean():.4f}")
    print(f"Headroom: {(oracle_arr.mean()-greedy_arr.mean())*100:.2f}pp")

    # Phase 2: Within-instance rho(LP, F1) (gold-filtered)
    print("\nPhase 2: Within-instance rho(LP, F1)...")
    within_rhos = []
    n_const_lp = 0
    n_const_f1_within = 0

    for inst in gold_filtered:
        gold_ents = inst["gold"].get("entities", [])
        gold_set = entity_set(gold_ents)
        samples = inst["samples"]
        if len(samples) < 3:
            continue

        lps = []
        f1s = []
        for s in samples:
            lp = s.get("mean_logprob")
            if lp is None:
                continue
            pred_set = entity_set(s.get("entities", []))
            f1 = f1_score_set(pred_set, gold_set)
            lps.append(lp)
            f1s.append(f1)

        if len(lps) < 3:
            continue
        if len(set(lps)) < 2:
            n_const_lp += 1
            continue
        if len(set(f1s)) < 2:
            n_const_f1_within += 1
            continue

        rho, p = spearmanr(lps, f1s)
        if not np.isnan(rho):
            within_rhos.append(rho)

    within_rhos = np.array(within_rhos)
    print(f"Within-instance rho: median={np.median(within_rhos):.4f}, mean={np.mean(within_rhos):.4f}, n={len(within_rhos)}")

    # Phase 3: DALS (tau=0.05)
    print(f"\nPhase 3: DALS (tau={TAU})...")
    dals_f1s = np.zeros(n_gf)
    lp_sel_f1s = np.zeros(n_gf)
    n_degen_dals = 0
    n_nondegen_dals = 0

    for i, inst in enumerate(gold_filtered):
        gold_ents = inst["gold"]["entities"]
        greedy_ents = inst.get("greedy", inst["samples"][0]).get("entities", [])

        sample_lps = [s.get("mean_logprob", float("-inf")) for s in inst["samples"]]
        best_idx = int(np.argmax(sample_lps))
        lp_best_ents = inst["samples"][best_idx].get("entities", [])

        gold_set = entity_set(gold_ents)
        greedy_set = entity_set(greedy_ents)
        lp_best_set = entity_set(lp_best_ents)

        greedy_f1_val = f1_score_set(greedy_set, gold_set)
        lp_f1_val = f1_score_set(lp_best_set, gold_set)
        lp_sel_f1s[i] = lp_f1_val

        lp_range = max(sample_lps) - min(sample_lps) if len(sample_lps) > 1 else 0.0
        if lp_range > TAU:
            dals_f1s[i] = lp_f1_val
            n_nondegen_dals += 1
        else:
            dals_f1s[i] = greedy_f1_val
            n_degen_dals += 1

    dals_macro = float(dals_f1s.mean())
    lp_sel_macro = float(lp_sel_f1s.mean())
    dals_gain = dals_macro - greedy_arr.mean()

    print(f"DALS F1: {dals_macro:.4f} (gain: {dals_gain*100:+.2f}pp)")
    print(f"LP sel F1: {lp_sel_macro:.4f}")
    print(f"Non-degen: {n_nondegen_dals}, Degen: {n_degen_dals}")

    # Phase 4: Bootstrap CI for LP delta
    print("\nPhase 4: Bootstrap CI...")
    np.random.seed(42)
    n_bootstrap = 1000
    lp_deltas_boot = []
    for _ in range(n_bootstrap):
        idx = np.random.choice(n_gf, size=n_gf, replace=True)
        boot_lp_sel = float(np.array(signal_sel_f1["LP"])[idx].mean())
        boot_greedy = float(greedy_arr[idx].mean())
        lp_deltas_boot.append(boot_lp_sel - boot_greedy)

    lp_delta_ci_low = float(np.percentile(lp_deltas_boot, 2.5))
    lp_delta_ci_high = float(np.percentile(lp_deltas_boot, 97.5))
    lp_delta_mean = float(np.mean(lp_deltas_boot))

    # Phase 5: Global signal correlations
    print("\nPhase 5: Global correlations...")
    sig_arrays = {"LP": [], "SJ": [], "FK": [], "EM": [], "VC": []}
    for idx, inst in enumerate(gold_filtered):
        samples = inst["samples"]
        n = len(samples)
        lps = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
        sig_arrays["LP"].append(float(np.mean(lps)) if lps else float("nan"))

        from consistency import structural_consistency_soft_jaccard, fleiss_kappa_surface
        sig_arrays["SJ"].append(structural_consistency_soft_jaccard(samples, subtask=SUBTASK))
        sig_arrays["FK"].append(fleiss_kappa_surface(samples, subtask=SUBTASK))

        sample_keys = []
        for s in samples:
            keys = frozenset((e.get("text",""), e.get("type","")) for e in s.get("entities", []))
            sample_keys.append(keys)
        match_count = sum(1 for a in range(n) for b in range(a+1, n) if sample_keys[a] == sample_keys[b])
        total_pairs = n*(n-1)//2
        sig_arrays["EM"].append(match_count / total_pairs if total_pairs > 0 else 1.0)

        counter = Counter()
        for s in samples:
            for e in s.get("entities", []):
                counter[(e.get("text",""), e.get("type",""))] += 1
        majority_votes = [v/n for v in counter.values() if v > n/2]
        sig_arrays["VC"].append(float(np.mean(majority_votes)) if majority_votes else 0.0)

        if (idx + 1) % 5000 == 0:
            print(f"  corr {idx+1}/{n_gf}")

    corr_results = {}
    for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
        sig_arr = np.array(sig_arrays[sig_name])
        valid = np.isfinite(sig_arr) & np.isfinite(greedy_arr)
        rho, p = spearmanr(sig_arr[valid], greedy_arr[valid]) if valid.sum() > 2 else (float("nan"), float("nan"))
        corr_results[sig_name] = {"global_rho": round(float(rho), 4), "global_p": float(p)}

    elapsed = time.time() - t0

    # Summary
    print(f"\n{'='*70}")
    print("LLAMA FEW-NERD FULL SIGNAL ANALYSIS")
    print(f"{'='*70}")
    print(f"Total instances: {len(data)}")
    print(f"Gold-filtered: {n_gf}")
    print(f"Degeneracy (CF1): {degeneracy:.4f} ({n_constant_f1}/{n_gf})")
    print(f"Greedy F1: {greedy_arr.mean():.4f}")
    print(f"Oracle F1: {oracle_arr.mean():.4f}")
    print(f"Headroom: {(oracle_arr.mean()-greedy_arr.mean())*100:.2f}pp")
    print()
    print(f"{'Signal':<6} {'Sel F1':>10} {'Delta':>10} {'Global rho':>12}")
    print("-"*42)
    for sig in ["LP", "SJ", "FK", "EM", "VC"]:
        sf = float(np.mean(signal_sel_f1[sig]))
        delta = sf - greedy_arr.mean()
        rho = corr_results[sig]["global_rho"]
        print(f"{sig:<6} {sf:>10.4f} {delta:>+10.4f} {rho:>12.4f}")
    print()
    print(f"LP delta 95% CI: [{lp_delta_ci_low:.4f}, {lp_delta_ci_high:.4f}]")
    print(f"Within-instance rho(LP,F1): median={np.median(within_rhos):.4f}, mean={np.mean(within_rhos):.4f}")
    print(f"DALS (tau={TAU}): {dals_macro:.4f} (gain: {dals_gain*100:+.2f}pp)")
    print(f"Elapsed: {elapsed:.1f}s")

    # Save results
    result = {
        "dataset": "fewnerd",
        "model": "llama3.1-8b",
        "N": N_per,
        "n_total": len(data),
        "n_gold_filtered": n_gf,
        "degeneracy_cf1_gold_filtered": round(degeneracy, 4),
        "n_constant_f1": n_constant_f1,
        "greedy_f1": round(float(greedy_arr.mean()), 4),
        "oracle_f1": round(float(oracle_arr.mean()), 4),
        "headroom": round(float(oracle_arr.mean() - greedy_arr.mean()), 4),
        "headroom_pp": round(float((oracle_arr.mean() - greedy_arr.mean()) * 100), 2),
        "selection_f1": {},
        "correlations": corr_results,
        "within_instance_rho_LP_F1": {
            "n_valid": len(within_rhos),
            "median": round(float(np.median(within_rhos)), 4),
            "mean": round(float(np.mean(within_rhos)), 4),
            "std": round(float(np.std(within_rhos)), 4),
            "pct_positive": round(float((within_rhos > 0).mean() * 100), 1),
        },
        "dals": {
            "tau": TAU,
            "f1": round(dals_macro, 4),
            "gain_vs_greedy": round(dals_gain, 4),
            "gain_pp": round(dals_gain * 100, 2),
            "n_nondegen": n_nondegen_dals,
            "n_degen": n_degen_dals,
        },
        "lp_range": {
            "mean": round(float(np.mean(lp_ranges)), 4),
            "std": round(float(np.std(lp_ranges)), 4),
            "median": round(float(np.median(lp_ranges)), 4),
        },
        "lp_delta_bootstrap": {
            "mean": round(lp_delta_mean, 4),
            "ci_95_low": round(lp_delta_ci_low, 4),
            "ci_95_high": round(lp_delta_ci_high, 4),
        },
    }

    for sig in ["LP", "SJ", "FK", "EM", "VC"]:
        arr = np.array(signal_sel_f1[sig])
        delta = float(arr.mean() - greedy_arr.mean())
        result["selection_f1"][sig] = {
            "f1": round(float(arr.mean()), 4),
            "delta_vs_greedy": round(delta, 4),
            "delta_pp": round(delta * 100, 2),
        }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "full_signal_analysis.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
