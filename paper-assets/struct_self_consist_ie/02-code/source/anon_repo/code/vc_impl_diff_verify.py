#!/usr/bin/env python3
"""Verify VC implementation difference: majority threshold vs no threshold."""

import json
import sys
import os
from collections import Counter

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from evaluation import per_instance_f1

DATA_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl"
OUTPUT_PATH = "/root/autodl-tmp/struct_self_consist_ie/output/review_round2/vc_implementation_diff.json"


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def vc_impl_A(samples, subtask):
    """Implementation A (exp015 style — majority threshold > N/2)."""
    N = len(samples)
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    majority_votes = [v / N for v in counter.values() if v > N / 2]
    return float(np.mean(majority_votes)) if majority_votes else 0.0


def vc_impl_B(samples, subtask):
    """Implementation B (all items, no threshold)."""
    N = len(samples)
    counter = Counter()
    if subtask == "ner":
        for s in samples:
            for e in s.get("entities", []):
                counter[(e["text"], e["type"])] += 1
    else:
        for s in samples:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    rates = [v / N for v in counter.values()]
    return float(np.mean(rates))


def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def main():
    instances = load_data(DATA_PATH)
    print(f"Total instances: {len(instances)}")

    results = {}

    for subtask in ["ner", "re"]:
        field = "entities" if subtask == "ner" else "relations"
        valid = [inst for inst in instances if len(inst["gold"].get(field, [])) > 0]
        print(f"\n{'='*60}")
        print(f"Subtask: {subtask.upper()}, gold-nonempty n={len(valid)}")

        # Compute F1
        f1_scores = []
        for inst in valid:
            greedy = inst.get("greedy")
            gold = inst["gold"]
            if greedy is not None:
                f1 = per_instance_f1(greedy, gold, subtask=subtask)
            else:
                f1 = per_instance_f1(inst["samples"][0], gold, subtask=subtask)
            f1_scores.append(f1)

        # Compute VC with both implementations
        vc_A = []
        vc_B = []
        for inst in valid:
            samples = inst["samples"]
            vc_A.append(vc_impl_A(samples, subtask))
            vc_B.append(vc_impl_B(samples, subtask))

        # Full set
        rho_A_full, p_A_full = safe_spearman(vc_A, f1_scores)
        rho_B_full, p_B_full = safe_spearman(vc_B, f1_scores)

        # Conditional: exclude F1=0
        cond_idx = [i for i in range(len(valid)) if f1_scores[i] > 0]
        n_cond = len(cond_idx)
        cond_f1 = [f1_scores[i] for i in cond_idx]
        cond_A = [vc_A[i] for i in cond_idx]
        cond_B = [vc_B[i] for i in cond_idx]
        rho_A_cond, p_A_cond = safe_spearman(cond_A, cond_f1)
        rho_B_cond, p_B_cond = safe_spearman(cond_B, cond_f1)

        # Diagnostics: how many instances have 0 majority items in impl A?
        n_zero_A = sum(1 for v in vc_A if v == 0.0)
        n_zero_B = sum(1 for v in vc_B if v == 0.0)

        # Mean VC values
        mean_vc_A = float(np.mean(vc_A))
        mean_vc_B = float(np.mean(vc_B))

        sr = {
            "n_full": len(valid),
            "n_cond": n_cond,
            "impl_A_majority_threshold": {
                "rho_full": rho_A_full,
                "p_full": p_A_full,
                "rho_cond": rho_A_cond,
                "p_cond": p_A_cond,
                "mean_vc_full": mean_vc_A,
                "n_zero_vc": n_zero_A,
            },
            "impl_B_no_threshold": {
                "rho_full": rho_B_full,
                "p_full": p_B_full,
                "rho_cond": rho_B_cond,
                "p_cond": p_B_cond,
                "mean_vc_full": mean_vc_B,
                "n_zero_vc": n_zero_B,
            },
        }
        results[subtask] = sr

        print(f"\n  Impl A (majority threshold > N/2):")
        print(f"    full  rho={rho_A_full:+.4f} (p={p_A_full:.4e}), mean_VC={mean_vc_A:.4f}, n_zero={n_zero_A}")
        print(f"    cond  rho={rho_A_cond:+.4f} (p={p_A_cond:.4e}), n={n_cond}")
        print(f"\n  Impl B (no threshold, all items):")
        print(f"    full  rho={rho_B_full:+.4f} (p={p_B_full:.4e}), mean_VC={mean_vc_B:.4f}, n_zero={n_zero_B}")
        print(f"    cond  rho={rho_B_cond:+.4f} (p={p_B_cond:.4e}), n={n_cond}")

    # Summary comparison
    print(f"\n{'='*60}")
    print("COMPARISON WITH KNOWN VALUES")
    print("="*60)
    re = results["re"]
    print(f"\n  Registry values:     full=0.3498, cond=0.2409")
    print(f"  Worker recomputed:   full=0.3311, cond=0.1386")
    print(f"  Impl A (majority):   full={re['impl_A_majority_threshold']['rho_full']:+.4f}, cond={re['impl_A_majority_threshold']['rho_cond']:+.4f}")
    print(f"  Impl B (all items):  full={re['impl_B_no_threshold']['rho_full']:+.4f}, cond={re['impl_B_no_threshold']['rho_cond']:+.4f}")

    # Determine matches
    registry_full, registry_cond = 0.3498, 0.2409
    worker_full, worker_cond = 0.3311, 0.1386

    a_full = re['impl_A_majority_threshold']['rho_full']
    a_cond = re['impl_A_majority_threshold']['rho_cond']
    b_full = re['impl_B_no_threshold']['rho_full']
    b_cond = re['impl_B_no_threshold']['rho_cond']

    conclusion = {
        "impl_A_matches_registry": abs(a_full - registry_full) < 0.01 and abs(a_cond - registry_cond) < 0.05,
        "impl_A_matches_worker": abs(a_full - worker_full) < 0.01 and abs(a_cond - worker_cond) < 0.05,
        "impl_B_matches_registry": abs(b_full - registry_full) < 0.01 and abs(b_cond - registry_cond) < 0.05,
        "impl_B_matches_worker": abs(b_full - worker_full) < 0.01 and abs(b_cond - worker_cond) < 0.05,
        "diff_A_registry_full": abs(a_full - registry_full),
        "diff_A_registry_cond": abs(a_cond - registry_cond),
        "diff_B_registry_full": abs(b_full - registry_full),
        "diff_B_registry_cond": abs(b_cond - registry_cond),
        "diff_A_worker_full": abs(a_full - worker_full),
        "diff_A_worker_cond": abs(a_cond - worker_cond),
        "diff_B_worker_full": abs(b_full - worker_full),
        "diff_B_worker_cond": abs(b_cond - worker_cond),
    }
    results["conclusion"] = conclusion

    # Determine which is which
    if conclusion["impl_A_matches_registry"]:
        print("\n  >> Impl A (majority) matches REGISTRY")
    if conclusion["impl_A_matches_worker"]:
        print("  >> Impl A (majority) matches WORKER recompute")
    if conclusion["impl_B_matches_registry"]:
        print("  >> Impl B (all items) matches REGISTRY")
    if conclusion["impl_B_matches_worker"]:
        print("  >> Impl B (all items) matches WORKER recompute")

    # NER comparison
    ner = results["ner"]
    print(f"\n{'='*60}")
    print("NER COMPARISON")
    print("="*60)
    print(f"  Impl A: full={ner['impl_A_majority_threshold']['rho_full']:+.4f}, cond={ner['impl_A_majority_threshold']['rho_cond']:+.4f}")
    print(f"  Impl B: full={ner['impl_B_no_threshold']['rho_full']:+.4f}, cond={ner['impl_B_no_threshold']['rho_cond']:+.4f}")
    ner_diff_full = abs(ner['impl_A_majority_threshold']['rho_full'] - ner['impl_B_no_threshold']['rho_full'])
    ner_diff_cond = abs(ner['impl_A_majority_threshold']['rho_cond'] - ner['impl_B_no_threshold']['rho_cond'])
    print(f"  Diff: full={ner_diff_full:.4f}, cond={ner_diff_cond:.4f}")
    results["ner_impl_diff"] = {"diff_full": ner_diff_full, "diff_cond": ner_diff_cond}

    if ner_diff_full < 0.02:
        print("  >> NER: implementations are nearly identical (entities are mostly majority items)")
    else:
        print("  >> NER: significant difference between implementations")

    # Save
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
