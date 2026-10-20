"""RE Non-zero F1 Conditional Selection Analysis.

Compares selection performance on full set vs non-zero RE F1 subset.
Bootstrap p-values for selection gain over greedy.
"""
import json
import os
import sys
import numpy as np
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluation import per_instance_f1, relation_strict_match
from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
    _re_soft_jaccard_pair,
    _extract_surface_keys,
)

SAMPLES_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
SUBTASK = "re"
N_BOOTSTRAP = 1000
RNG_SEED = 42


def load_data():
    with open(SAMPLES_PATH) as f:
        return [json.loads(line) for line in f]


def compute_per_sample_f1s(instances):
    return [
        [per_instance_f1(s, inst["gold"], subtask=SUBTASK) for s in inst["samples"]]
        for inst in instances
    ]


def compute_greedy_f1s(instances):
    return [per_instance_f1(inst["greedy"], inst["gold"], subtask=SUBTASK) for inst in instances]


def select_by_signal(instances, per_sample_f1s, signal_name):
    """Return list of selected F1 for each instance using the given signal."""
    selected = []
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        ns = len(samples)
        sf = per_sample_f1s[idx]

        if ns == 0:
            selected.append(0.0)
            continue
        if ns == 1:
            selected.append(sf[0])
            continue

        if signal_name == "LP":
            scores = [s.get("mean_logprob", 0.0) for s in samples]
            best_k = int(np.argmax(scores))

        elif signal_name == "FK":
            sample_key_sets = [_extract_surface_keys(s, SUBTASK) for s in samples]
            scores = []
            for k in range(ns):
                overlaps = []
                for j in range(ns):
                    if j == k:
                        continue
                    union = sample_key_sets[k] | sample_key_sets[j]
                    inter = sample_key_sets[k] & sample_key_sets[j]
                    overlaps.append(len(inter) / len(union) if union else 1.0)
                scores.append(float(np.mean(overlaps)))
            best_k = int(np.argmax(scores))

        elif signal_name == "SJ":
            scores = []
            for k in range(ns):
                sims = []
                for j in range(ns):
                    if j == k:
                        continue
                    sims.append(_re_soft_jaccard_pair(
                        samples[k].get("relations", []),
                        samples[j].get("relations", []),
                    ))
                scores.append(float(np.mean(sims)))
            best_k = int(np.argmax(scores))

        elif signal_name == "VC":
            counter = Counter()
            for s in samples:
                for r in s.get("relations", []):
                    counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1
            majority_set = {k for k, v in counter.items() if v > ns / 2}
            best_k, best_score = 0, -1
            for k, s in enumerate(samples):
                s_keys = {(r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", [])}
                score = len(s_keys & majority_set) - 0.5 * len(s_keys - majority_set)
                if score > best_score:
                    best_score = score
                    best_k = k

        elif signal_name == "EM":
            sample_keys = [
                frozenset((r.get("head", ""), r.get("tail", ""), r.get("type", ""))
                           for r in s.get("relations", []))
                for s in samples
            ]
            match_counts = [
                sum(1 for j in range(ns) if j != k and sample_keys[k] == sample_keys[j])
                for k in range(ns)
            ]
            best_k = int(np.argmax(match_counts))
        else:
            raise ValueError(f"Unknown signal: {signal_name}")

        selected.append(sf[best_k])
    return selected


def bootstrap_pvalue(gains, n_boot=N_BOOTSTRAP, seed=RNG_SEED):
    """One-sided bootstrap test: H0: mean(gain) <= 0."""
    rng = np.random.RandomState(seed)
    observed = np.mean(gains)
    if observed <= 0:
        return 1.0
    n = len(gains)
    centered = gains - observed  # center under H0
    count = 0
    for _ in range(n_boot):
        boot = rng.choice(centered, size=n, replace=True)
        if np.mean(boot) >= observed:
            count += 1
    return count / n_boot


def analyze_subset(instances, per_sample_f1s, greedy_f1s, label):
    """Analyze selection for a subset. Returns dict with per-signal results."""
    n = len(instances)
    greedy_arr = np.array(greedy_f1s)
    oracle_arr = np.array([max(sf) if sf else 0.0 for sf in per_sample_f1s])

    greedy_mean = float(np.mean(greedy_arr))
    oracle_mean = float(np.mean(oracle_arr))

    print(f"\n=== {label} (n={n}) ===")
    print(f"  Greedy F1: {greedy_mean:.4f}")
    print(f"  Oracle F1: {oracle_mean:.4f}")

    signals = ["LP", "FK", "SJ", "VC", "EM"]
    results = {}
    for sig in signals:
        sel_f1s = select_by_signal(instances, per_sample_f1s, sig)
        sel_arr = np.array(sel_f1s)
        gains = sel_arr - greedy_arr
        sel_mean = float(np.mean(sel_arr))
        gain_mean = float(np.mean(gains))
        pval = bootstrap_pvalue(gains)
        results[sig] = {
            "selected_f1": round(sel_mean, 4),
            "greedy_f1": round(greedy_mean, 4),
            "oracle_f1": round(oracle_mean, 4),
            "gain": round(gain_mean, 4),
            "p_value": round(pval, 4),
        }
        print(f"  {sig}: sel={sel_mean:.4f}, gain={gain_mean:+.4f}, p={pval:.4f}")

    return results


def main():
    data = load_data()
    print(f"Total instances: {len(data)}")

    # Compute greedy F1 for all
    greedy_f1s_all = compute_greedy_f1s(data)
    per_sample_f1s_all = compute_per_sample_f1s(data)

    # Non-zero filter
    nz_mask = [f > 0 for f in greedy_f1s_all]
    nz_instances = [d for d, m in zip(data, nz_mask) if m]
    nz_greedy = [f for f, m in zip(greedy_f1s_all, nz_mask) if m]
    nz_psf = [p for p, m in zip(per_sample_f1s_all, nz_mask) if m]

    n_total = len(data)
    n_nz = len(nz_instances)
    n_zero = n_total - n_nz
    print(f"Non-zero RE greedy F1: {n_nz}/{n_total} ({100*n_nz/n_total:.1f}%)")
    print(f"Zero RE greedy F1: {n_zero}/{n_total} ({100*n_zero/n_total:.1f}%)")

    # Full set analysis
    full_results = analyze_subset(data, per_sample_f1s_all, greedy_f1s_all, "Full Set")

    # Non-zero subset analysis
    nz_results = analyze_subset(nz_instances, nz_psf, nz_greedy, "Non-zero F1 Subset")

    # Print comparison
    print("\n=== Comparison ===")
    print(f"{'Signal':<6} {'Full Gain':>10} {'NZ Gain':>10} {'Full p':>8} {'NZ p':>8}")
    for sig in ["LP", "FK", "SJ", "VC", "EM"]:
        fg = full_results[sig]["gain"]
        ng = nz_results[sig]["gain"]
        fp = full_results[sig]["p_value"]
        np_ = nz_results[sig]["p_value"]
        print(f"{sig:<6} {fg:>+10.4f} {ng:>+10.4f} {fp:>8.4f} {np_:>8.4f}")

    output = {
        "total_instances": n_total,
        "nonzero_instances": n_nz,
        "zero_instances": n_zero,
        "nonzero_pct": round(100 * n_nz / n_total, 1),
        "full_set": full_results,
        "nonzero_set": nz_results,
    }
    print("\n" + json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
