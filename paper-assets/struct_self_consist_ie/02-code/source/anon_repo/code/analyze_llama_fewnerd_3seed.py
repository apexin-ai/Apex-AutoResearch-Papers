#!/usr/bin/env python3
"""LLaMA FewNERD 3-seed aggregated analysis: degeneracy, selection F1, 5-signal, DGS."""
import json, os, sys, time
import numpy as np
from collections import Counter
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from unified_metrics import (
    load_and_filter, compute_sample_f1s, compute_greedy_f1,
    compute_degeneracy, compute_entity_f1, bootstrap_ci, bootstrap_delta_ci,
)
from consistency import _ner_soft_jaccard_pair, _extract_surface_keys

BASE = "/root/autodl-tmp/struct_self_consist_ie"
SEEDS = [42, 123, 456]
SEED_DIRS = {s: f"{BASE}/output/llama_fewnerd_s{s}" for s in SEEDS}
OUTPUT_DIR = f"{BASE}/output/llama_fewnerd_3seed_summary"
SUBTASK = "ner"
DGS_TAU = 0.05

sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1)


def compute_sample_sj(inst):
    samples = inst["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []), samples[j].get("entities", [])
            )
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface(inst):
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
    fk = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk, key_sets


def compute_sample_vc(key_sets, N):
    counter = Counter()
    for ks in key_sets:
        for key in ks:
            counter[key] += 1
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            scores.append(float(np.mean([counter[key] / N for key in ks])))
    return scores


def compute_sample_em(key_sets):
    N = len(key_sets)
    return [float(sum(1 for j in range(N) if j != k and key_sets[k] == key_sets[j])) for k in range(N)]


def compute_sample_lp(inst):
    lps = []
    for s in inst["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def analyze_single_seed(seed, data_dir):
    samples_path = os.path.join(data_dir, "samples.jsonl")
    if not os.path.exists(samples_path):
        print(f"  [seed={seed}] samples.jsonl not found at {samples_path}")
        return None

    data = load_and_filter(samples_path, gold_filter=True)
    n_total_raw = sum(1 for line in open(samples_path) if line.strip())
    N_per = len(data[0]["samples"]) if data else 0
    n_gf = len(data)
    print(f"  [seed={seed}] {n_total_raw} total, {n_gf} gold-filtered, N={N_per}")

    greedy_f1s = []
    oracle_f1s = []
    n_degen = 0
    signal_sel = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP"]}
    sig_arrays = {sig: [] for sig in ["SJ", "FK", "VC", "EM", "LP"]}
    lp_ranges = []
    within_rhos = []
    dals_f1s = []

    for idx, inst in enumerate(data):
        sample_f1s = compute_sample_f1s(inst)
        greedy_f1 = compute_greedy_f1(inst)
        oracle_f1 = max(sample_f1s)
        greedy_f1s.append(greedy_f1)
        oracle_f1s.append(oracle_f1)

        is_degen = compute_degeneracy(sample_f1s)
        if is_degen:
            n_degen += 1

        sj_scores = compute_sample_sj(inst)
        fk_scores, key_sets = compute_sample_surface(inst)
        vc_scores = compute_sample_vc(key_sets, N_per)
        em_scores = compute_sample_em(key_sets)
        lp_scores = compute_sample_lp(inst)

        signals = {"SJ": sj_scores, "FK": fk_scores, "VC": vc_scores, "EM": em_scores, "LP": lp_scores}

        for sig_name, scores in signals.items():
            best_idx = int(np.argmax(scores))
            signal_sel[sig_name].append(sample_f1s[best_idx])
            if sig_name in ["SJ", "FK"]:
                sig_arrays[sig_name].append(float(np.mean(scores)))
            elif sig_name == "LP":
                sig_arrays[sig_name].append(float(np.mean(lp_scores)))
            elif sig_name == "EM":
                sig_arrays[sig_name].append(float(np.max(em_scores)))
            elif sig_name == "VC":
                n = N_per
                counter = Counter()
                for ks in key_sets:
                    for key in ks:
                        counter[key] += 1
                majority_votes = [v / n for v in counter.values() if v > n / 2]
                sig_arrays[sig_name].append(float(np.mean(majority_votes)) if majority_votes else 0.0)

        lp_arr = np.array(lp_scores)
        if np.isfinite(lp_arr).all():
            lp_ranges.append(float(lp_arr.max() - lp_arr.min()))

        f1_arr = np.array(sample_f1s)
        if len(set(round(f, 10) for f in sample_f1s)) > 1 and np.isfinite(lp_arr).all():
            rho_w, _ = spearmanr(lp_scores, sample_f1s)
            if np.isfinite(rho_w):
                within_rhos.append(rho_w)

        if is_degen:
            best_idx = int(np.argmax(lp_scores)) if np.isfinite(lp_arr).all() else 0
            dals_f1s.append(sample_f1s[best_idx])
        else:
            sj_lp_combined = np.array(sj_scores) + DGS_TAU * np.array(lp_scores)
            best_idx = int(np.argmax(sj_lp_combined)) if np.isfinite(sj_lp_combined).all() else int(np.argmax(sj_scores))
            dals_f1s.append(sample_f1s[best_idx])

        if (idx + 1) % 5000 == 0:
            print(f"    processed {idx+1}/{n_gf}")

    greedy_arr = np.array(greedy_f1s)
    oracle_arr = np.array(oracle_f1s)
    dals_arr = np.array(dals_f1s)

    corr_results = {}
    for sig_name in ["LP", "SJ", "FK", "EM", "VC"]:
        sig_arr = np.array(sig_arrays[sig_name])
        valid = np.isfinite(sig_arr) & np.isfinite(greedy_arr)
        if valid.sum() > 2:
            rho, p = spearmanr(sig_arr[valid], greedy_arr[valid])
        else:
            rho, p = float("nan"), float("nan")
        corr_results[sig_name] = {"rho": round(float(rho), 4), "p": float(p)}

    result = {
        "seed": seed,
        "n_total": n_total_raw,
        "n_gold_filtered": n_gf,
        "degeneracy_rate": round(n_degen / n_gf, 4) if n_gf > 0 else 0,
        "n_degenerate": n_degen,
        "greedy_f1": round(float(greedy_arr.mean()), 4),
        "oracle_f1": round(float(oracle_arr.mean()), 4),
        "headroom_pp": round(float((oracle_arr.mean() - greedy_arr.mean()) * 100), 2),
        "selection_f1": {},
        "correlations": corr_results,
        "dgs": {
            "tau": DGS_TAU,
            "f1": round(float(dals_arr.mean()), 4),
            "gain_pp": round(float((dals_arr.mean() - greedy_arr.mean()) * 100), 2),
        },
        "within_rho_lp_f1": {
            "n": len(within_rhos),
            "median": round(float(np.median(within_rhos)), 4) if within_rhos else 0,
            "mean": round(float(np.mean(within_rhos)), 4) if within_rhos else 0,
        },
        "lp_range_mean": round(float(np.mean(lp_ranges)), 4) if lp_ranges else 0,
    }

    for sig in ["SJ", "FK", "VC", "EM", "LP"]:
        arr = np.array(signal_sel[sig])
        delta = float(arr.mean() - greedy_arr.mean())
        result["selection_f1"][sig] = {
            "f1": round(float(arr.mean()), 4),
            "delta_pp": round(delta * 100, 2),
        }

    return result


def main():
    t0 = time.time()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {}

    for seed in SEEDS:
        data_dir = SEED_DIRS[seed]
        print(f"\nAnalyzing seed={seed}...")
        result = analyze_single_seed(seed, data_dir)
        if result is not None:
            all_results[seed] = result
            out_path = os.path.join(OUTPUT_DIR, f"seed{seed}.json")
            with open(out_path, "w") as f:
                json.dump(result, f, indent=2)

    if len(all_results) < 2:
        print("Not enough seeds completed for aggregation.")
        return

    agg = {
        "model": "llama3.1-8b",
        "dataset": "fewnerd",
        "n_seeds": len(all_results),
        "seeds": list(all_results.keys()),
    }

    for key in ["greedy_f1", "oracle_f1", "headroom_pp", "degeneracy_rate"]:
        vals = [r[key] for r in all_results.values()]
        agg[key] = {"mean": round(float(np.mean(vals)), 4), "std": round(float(np.std(vals)), 4)}

    agg["dgs"] = {
        "tau": DGS_TAU,
        "f1_mean": round(float(np.mean([r["dgs"]["f1"] for r in all_results.values()])), 4),
        "f1_std": round(float(np.std([r["dgs"]["f1"] for r in all_results.values()])), 4),
        "gain_pp_mean": round(float(np.mean([r["dgs"]["gain_pp"] for r in all_results.values()])), 2),
    }

    agg["selection_f1"] = {}
    for sig in ["SJ", "FK", "VC", "EM", "LP"]:
        f1s = [r["selection_f1"][sig]["f1"] for r in all_results.values()]
        deltas = [r["selection_f1"][sig]["delta_pp"] for r in all_results.values()]
        agg["selection_f1"][sig] = {
            "f1_mean": round(float(np.mean(f1s)), 4),
            "f1_std": round(float(np.std(f1s)), 4),
            "delta_pp_mean": round(float(np.mean(deltas)), 2),
        }

    agg["correlations"] = {}
    for sig in ["SJ", "FK", "VC", "EM", "LP"]:
        rhos = [r["correlations"][sig]["rho"] for r in all_results.values()]
        agg["correlations"][sig] = {
            "rho_mean": round(float(np.mean(rhos)), 4),
            "rho_std": round(float(np.std(rhos)), 4),
        }

    agg_path = os.path.join(OUTPUT_DIR, "aggregated.json")
    with open(agg_path, "w") as f:
        json.dump(agg, f, indent=2)

    elapsed = time.time() - t0
    print(f"\n{'='*70}")
    print("LLAMA FEWNERD 3-SEED AGGREGATED RESULTS")
    print(f"{'='*70}")
    print(f"Seeds: {list(all_results.keys())}")
    print(f"Greedy F1: {agg['greedy_f1']['mean']:.4f} +/- {agg['greedy_f1']['std']:.4f}")
    print(f"Oracle F1: {agg['oracle_f1']['mean']:.4f} +/- {agg['oracle_f1']['std']:.4f}")
    print(f"Headroom:  {agg['headroom_pp']['mean']:.2f} +/- {agg['headroom_pp']['std']:.2f} pp")
    print(f"Degeneracy: {agg['degeneracy_rate']['mean']:.4f} +/- {agg['degeneracy_rate']['std']:.4f}")
    print(f"\nDGS (tau={DGS_TAU}): {agg['dgs']['f1_mean']:.4f} +/- {agg['dgs']['f1_std']:.4f} (gain: {agg['dgs']['gain_pp_mean']:+.2f}pp)")
    print(f"\n{'Signal':<6} {'Sel F1':>12} {'Delta pp':>12} {'Global rho':>14}")
    print("-" * 48)
    for sig in ["LP", "SJ", "FK", "EM", "VC"]:
        sf = agg["selection_f1"][sig]
        cr = agg["correlations"][sig]
        print(f"{sig:<6} {sf['f1_mean']:>8.4f}+/-{sf['f1_std']:.4f} {sf['delta_pp_mean']:>+8.2f}pp {cr['rho_mean']:>+8.4f}+/-{cr['rho_std']:.4f}")
    print(f"\nElapsed: {elapsed:.1f}s")
    print(f"Saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
