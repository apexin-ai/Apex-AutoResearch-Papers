#!/usr/bin/env python3
"""analysis_5paired_bootstrap.py — Paired clustered bootstrap for CLS vs CWM comparison.

Compares CLS (classification) and CWM (code-with-mutation generation) verifiers
across multiple training seeds using clustered bootstrap resampling.

INPUT FORMAT:
  Prediction files in JSONL (one JSON per line) or JSON array format.
  Required fields per record:
    - index    : int, test case index (aligns CLS/CWM on same test case)
    - problem_id : str, e.g. "HumanEval/0" (used as cluster key)
    - label    : int, ground truth (0=fail, 1=pass)
    - pred     : int, model prediction (0 or 1)
      (also accepts field name "prediction")

OUTPUT FORMAT:
  Printed report + JSON file with:
    - per_seed  : per-pair accuracy and difference
    - pooled    : mean diff, 95% CI, TOST result
    - bootstrap_se_pp : bootstrap standard error in percentage points

USAGE:
  python3 analysis_5paired_bootstrap.py \\
    --pairs cls_s42.jsonl cwm_s42.jsonl  cls_s0.jsonl cwm_s0.jsonl ... \\
    --n-resamples 1000 --margin 2.0 --seed 42 --output results.json

STATISTICAL METHOD:
  1. For each seed pair, compute per-test-case paired difference:
     d_i = 1(CLS correct) - 1(CWM correct)  ∈ {-1, 0, +1}
  2. Pool differences across all seeds, grouped by problem_id clusters
  3. Clustered bootstrap: resample problem_ids with replacement (not test cases),
     include all variants within each selected problem across all seeds
  4. 95% CI from percentile bootstrap
  5. TOST equivalence: check if 90% CI falls within ±margin
"""

import argparse
import json
import sys
from collections import defaultdict

import numpy as np


def load_predictions(path):
    """Load prediction file (JSONL or JSON array). Normalize field names."""
    with open(path) as f:
        content = f.read().strip()

    if content.startswith("["):
        records = json.loads(content)
    else:
        records = [json.loads(line) for line in content.split("\n") if line.strip()]

    out = []
    for r in records:
        pred = r.get("pred", r.get("prediction"))
        if pred is None:
            raise ValueError(f"No 'pred' or 'prediction' field in: {r}")
        out.append({
            "index": r["index"],
            "problem_id": r["problem_id"],
            "label": int(r["label"]),
            "pred": int(pred),
        })
    return sorted(out, key=lambda x: x["index"])


def align_and_diff(cls_preds, cwm_preds):
    """Align by index, compute per-sample paired diffs grouped by problem_id."""
    cls_map = {r["index"]: r for r in cls_preds}
    cwm_map = {r["index"]: r for r in cwm_preds}
    common = sorted(set(cls_map) & set(cwm_map))

    if len(common) != len(cls_preds) or len(common) != len(cwm_preds):
        print(f"    WARNING: CLS={len(cls_preds)}, CWM={len(cwm_preds)}, "
              f"common={len(common)}")

    diffs_by_pid = defaultdict(list)
    n_cls_correct = 0
    n_cwm_correct = 0

    for idx in common:
        c, w = cls_map[idx], cwm_map[idx]
        assert c["label"] == w["label"], f"Label mismatch at index {idx}"
        cc = int(c["pred"] == c["label"])
        wc = int(w["pred"] == w["label"])
        n_cls_correct += cc
        n_cwm_correct += wc
        diffs_by_pid[c["problem_id"]].append(cc - wc)

    n = len(common)
    return {
        "diffs_by_pid": dict(diffs_by_pid),
        "n": n,
        "cls_acc": n_cls_correct / n,
        "cwm_acc": n_cwm_correct / n,
        "mean_diff": (n_cls_correct - n_cwm_correct) / n,
    }


def clustered_bootstrap(all_diffs_by_pid, n_resamples, rng_seed):
    """Resample problem_ids with replacement, compute mean diff per resample."""
    rng = np.random.default_rng(rng_seed)
    pids = list(all_diffs_by_pid.keys())
    K = len(pids)

    sums = np.array([sum(all_diffs_by_pid[p]) for p in pids])
    counts = np.array([len(all_diffs_by_pid[p]) for p in pids])

    boot_means = np.empty(n_resamples)
    for b in range(n_resamples):
        chosen = rng.integers(0, K, size=K)
        boot_means[b] = sums[chosen].sum() / counts[chosen].sum()
    return boot_means


def tost_analysis(boot_means, observed_mean, margin_pp, alpha=0.05):
    """TOST equivalence test + 95% CI via bootstrap percentiles."""
    margin = margin_pp / 100

    ci95_lo = float(np.percentile(boot_means, 2.5))
    ci95_hi = float(np.percentile(boot_means, 97.5))

    # TOST at level α ↔ (1−2α)% CI within [−Δ, +Δ]
    tost_lo = float(np.percentile(boot_means, 100 * alpha))
    tost_hi = float(np.percentile(boot_means, 100 * (1 - alpha)))
    equivalent = (tost_lo > -margin) and (tost_hi < margin)

    # Bootstrap TOST p-value (percentile inversion)
    p_upper = float(np.mean(boot_means >= margin))
    p_lower = float(np.mean(boot_means <= -margin))
    tost_p = max(p_upper, p_lower)

    min_margin = max(abs(tost_lo), abs(tost_hi))

    return {
        "mean_diff_pp": round(observed_mean * 100, 3),
        "ci95": [round(ci95_lo * 100, 3), round(ci95_hi * 100, 3)],
        "tost_90ci": [round(tost_lo * 100, 3), round(tost_hi * 100, 3)],
        "tost_margin_pp": margin_pp,
        "tost_equivalent": equivalent,
        "tost_p": round(tost_p, 4),
        "min_equiv_margin_pp": round(min_margin * 100, 3),
    }


def main():
    ap = argparse.ArgumentParser(
        description="Paired clustered bootstrap CI for CLS vs CWM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--pairs", nargs="+", required=True, metavar="FILE",
                     help="CLS1 CWM1 CLS2 CWM2 ... (alternating, even count)")
    ap.add_argument("--n-resamples", type=int, default=1000)
    ap.add_argument("--margin", type=float, default=2.0,
                     help="TOST equivalence margin in pp (default: 2.0)")
    ap.add_argument("--seed", type=int, default=42, help="RNG seed")
    ap.add_argument("--output", default="bootstrap_results.json")
    args = ap.parse_args()

    if len(args.pairs) % 2 != 0:
        ap.error("--pairs requires even number of files (CLS/CWM alternating)")

    n_pairs = len(args.pairs) // 2
    print(f"Loading {n_pairs} prediction pair(s)...\n")

    all_diffs = defaultdict(list)
    seed_stats = []

    for i in range(n_pairs):
        cls_path = args.pairs[2 * i]
        cwm_path = args.pairs[2 * i + 1]
        print(f"  Pair {i+1}: {cls_path}")
        print(f"        vs {cwm_path}")

        cls_preds = load_predictions(cls_path)
        cwm_preds = load_predictions(cwm_path)
        r = align_and_diff(cls_preds, cwm_preds)

        print(f"    CLS={r['cls_acc']*100:.2f}%  CWM={r['cwm_acc']*100:.2f}%  "
              f"diff={r['mean_diff']*100:+.2f}pp  (n={r['n']})")

        seed_stats.append({
            "pair": i + 1,
            "cls_file": cls_path,
            "cwm_file": cwm_path,
            "n": r["n"],
            "cls_acc_pct": round(r["cls_acc"] * 100, 2),
            "cwm_acc_pct": round(r["cwm_acc"] * 100, 2),
            "diff_pp": round(r["mean_diff"] * 100, 2),
        })

        for pid, diffs in r["diffs_by_pid"].items():
            all_diffs[pid].extend(diffs)

    flat = np.concatenate([np.array(v) for v in all_diffs.values()])
    observed_mean = float(np.mean(flat))
    n_total = len(flat)
    n_clusters = len(all_diffs)
    avg_cluster = n_total / n_clusters

    print(f"\n{'='*60}")
    print(f"Pooled: {n_total} obs, {n_clusters} problem clusters "
          f"(avg {avg_cluster:.1f} per cluster), {n_pairs} seed(s)")
    print(f"Observed mean diff (CLS − CWM): {observed_mean*100:+.3f}pp")

    print(f"\nBootstrapping ({args.n_resamples} resamples, "
          f"cluster by problem_id)...")
    boot = clustered_bootstrap(all_diffs, args.n_resamples, args.seed)

    t = tost_analysis(boot, observed_mean, args.margin)

    print(f"\n{'='*60}")
    tag = f"  ** PRELIMINARY ({n_pairs}/5 seeds) **" if n_pairs < 5 else ""
    print(f"RESULTS{tag}")
    print(f"{'='*60}")
    print(f"  Mean diff (CLS − CWM):  {t['mean_diff_pp']:+.3f}pp")
    print(f"  95% CI:                  [{t['ci95'][0]:+.3f}, {t['ci95'][1]:+.3f}]pp")
    print(f"  Bootstrap SE:            {np.std(boot)*100:.3f}pp")
    print()
    print(f"  TOST equivalence (±{args.margin}pp):")
    print(f"    90% CI:                [{t['tost_90ci'][0]:+.3f}, {t['tost_90ci'][1]:+.3f}]pp")
    print(f"    p-value:               {t['tost_p']:.4f}")
    print(f"    Equivalent:            {'YES' if t['tost_equivalent'] else 'NO'}")
    print(f"    Min margin for equiv:  {t['min_equiv_margin_pp']:.3f}pp")

    if n_pairs < 5:
        print(f"\n  NOTE: {n_pairs}/5 seeds available. "
              f"Re-run with all 5 pairs for final result.")
    print(f"{'='*60}")

    results = {
        "n_pairs": n_pairs,
        "n_total": n_total,
        "n_clusters": n_clusters,
        "n_resamples": args.n_resamples,
        "per_seed": seed_stats,
        "pooled": t,
        "bootstrap_se_pp": round(float(np.std(boot)) * 100, 3),
        "preliminary": n_pairs < 5,
    }
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
