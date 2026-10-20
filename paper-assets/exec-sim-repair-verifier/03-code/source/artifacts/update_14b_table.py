"""Update Table 2 (tab:scaling) with 14B 3-seed results + TOST equivalence test.

Two TOST methods:
  1. Clustered bootstrap (PRIMARY — matches 4B/8B paper methodology):
     Resample problem_ids with replacement, compute mean(CLS_correct - CWM_correct).
     Requires per-test-case prediction JSONL files (--pairs).
  2. Parametric independent-samples TOST (SANITY CHECK only):
     Uses seed-level accuracy scalars. NOT used in paper.

Usage:
  # Full analysis with prediction files (paper numbers):
  python3 update_14b_table.py \\
    --pairs cls_s42.jsonl cwm_s42.jsonl cls_s123.jsonl cwm_s123.jsonl cls_s456.jsonl cwm_s456.jsonl

  # Quick summary with accuracy scalars only (no TOST):
  python3 update_14b_table.py
"""

import argparse
import json
import sys
from collections import defaultdict

import numpy as np
from scipy import stats


# ── 14B seed accuracies (fill in after eval) ────────────────────────
CLS_SEEDS = {"s42": 89.21, "s123": 90.79, "s456": 89.79}
CWM_SEEDS = {"s42": 89.26, "s123": 88.99, "s456": 90.26}

CLS_8B_MEAN = 89.94
CWM_8B_MEAN = 87.33

SESOI = 2.0       # ±2 pp
N_RESAMPLES = 10000
RNG_SEED = 42


# ── Prediction file loading (from analysis_5paired_bootstrap.py) ────

def load_predictions(path):
    with open(path) as f:
        raw = json.load(f)
    # CWM eval wraps predictions in {"metadata": ..., "predictions": [...]}
    if isinstance(raw, dict) and "predictions" in raw:
        records = raw["predictions"]
    elif isinstance(raw, list):
        records = raw
    else:
        # Try JSONL fallback
        with open(path) as f:
            records = [json.loads(line) for line in f if line.strip()]
    out = []
    for r in records:
        # Handle CLS format (index/label/prediction) and CWM format (idx/true_label/predicted_label)
        idx = r.get("index", r.get("idx"))
        label = r.get("label", r.get("true_label"))
        pred = r.get("pred", r.get("prediction", r.get("predicted_label")))
        if idx is None or label is None or pred is None:
            raise ValueError(f"Cannot extract index/label/pred from: {list(r.keys())}")
        out.append({
            "index": idx,
            "problem_id": r["problem_id"],
            "label": int(label),
            "pred": int(pred),
        })
    return sorted(out, key=lambda x: x["index"])


def align_and_diff(cls_preds, cwm_preds):
    cls_map = {r["index"]: r for r in cls_preds}
    cwm_map = {r["index"]: r for r in cwm_preds}
    common = sorted(set(cls_map) & set(cwm_map))
    if len(common) != len(cls_preds) or len(common) != len(cwm_preds):
        print(f"    WARNING: CLS={len(cls_preds)}, CWM={len(cwm_preds)}, common={len(common)}")
    diffs_by_pid = defaultdict(list)
    n_cls_correct = n_cwm_correct = 0
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


# ── Clustered bootstrap TOST (PRIMARY — matches paper 4B/8B) ────────

def clustered_bootstrap_tost(all_diffs_by_pid, n_resamples, rng_seed, margin_pp):
    """Resample problem_ids with replacement, compute TOST via percentile inversion."""
    rng = np.random.default_rng(rng_seed)
    pids = list(all_diffs_by_pid.keys())
    K = len(pids)
    sums = np.array([sum(all_diffs_by_pid[p]) for p in pids])
    counts = np.array([len(all_diffs_by_pid[p]) for p in pids])

    boot_means = np.empty(n_resamples)
    for b in range(n_resamples):
        chosen = rng.integers(0, K, size=K)
        boot_means[b] = sums[chosen].sum() / counts[chosen].sum()

    margin = margin_pp / 100
    ci95_lo = float(np.percentile(boot_means, 2.5))
    ci95_hi = float(np.percentile(boot_means, 97.5))

    tost_lo = float(np.percentile(boot_means, 5.0))
    tost_hi = float(np.percentile(boot_means, 95.0))
    equivalent = (tost_lo > -margin) and (tost_hi < margin)

    p_upper = float(np.mean(boot_means >= margin))
    p_lower = float(np.mean(boot_means <= -margin))
    tost_p = max(p_upper, p_lower)

    flat = np.concatenate([np.array(v) for v in all_diffs_by_pid.values()])
    observed_mean = float(np.mean(flat))

    return {
        "method": "clustered_bootstrap",
        "n_resamples": n_resamples,
        "n_clusters": K,
        "n_total": int(counts.sum()),
        "observed_mean_pp": round(observed_mean * 100, 3),
        "ci95_pp": [round(ci95_lo * 100, 3), round(ci95_hi * 100, 3)],
        "tost_90ci_pp": [round(tost_lo * 100, 3), round(tost_hi * 100, 3)],
        "margin_pp": margin_pp,
        "tost_p": round(tost_p, 4),
        "equivalent": equivalent,
        "bootstrap_se_pp": round(float(np.std(boot_means)) * 100, 3),
    }


# ── Parametric TOST (sanity check only) ─────────────────────────────

def tost_parametric(cls_vals, cwm_vals, sesoi):
    n1, n2 = len(cls_vals), len(cwm_vals)
    diff = np.mean(cls_vals) - np.mean(cwm_vals)
    se = np.sqrt(np.var(cls_vals, ddof=1) / n1 + np.var(cwm_vals, ddof=1) / n2)
    df = n1 + n2 - 2
    if se == 0:
        p_lower = 0.0 if diff > -sesoi else 1.0
        p_upper = 0.0 if diff < sesoi else 1.0
    else:
        t_lower = (diff - (-sesoi)) / se
        t_upper = (diff - sesoi) / se
        p_lower = 1 - stats.t.cdf(t_lower, df)
        p_upper = stats.t.cdf(t_upper, df)
    return max(p_lower, p_upper), diff, se


def fmt_delta(val):
    if val >= 0:
        return f"+{val:.2f}"
    return f"$-${abs(val):.2f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", nargs="+", metavar="FILE",
                    help="CLS1 CWM1 CLS2 CWM2 ... prediction JSONL files (for clustered bootstrap)")
    ap.add_argument("--n-resamples", type=int, default=N_RESAMPLES)
    ap.add_argument("--margin", type=float, default=SESOI, help="TOST margin in pp")
    ap.add_argument("--seed", type=int, default=RNG_SEED)
    args = ap.parse_args()

    # ── Collect seed-level accuracy ──────────────────────────────────
    cls_vals, cwm_vals, seeds_present = [], [], []
    for seed in ["s42", "s123", "s456"]:
        c, w = CLS_SEEDS[seed], CWM_SEEDS[seed]
        if c is not None and w is not None:
            cls_vals.append(c)
            cwm_vals.append(w)
            seeds_present.append(seed)

    n = len(cls_vals)
    print(f"Seeds with accuracy data: {seeds_present} (n={n})")

    if n == 0:
        print("ERROR: No seed data. Fill in CLS_SEEDS / CWM_SEEDS.")
        return

    cls_arr = np.array(cls_vals)
    cwm_arr = np.array(cwm_vals)
    cls_mean = cls_arr.mean()
    cls_std = cls_arr.std(ddof=1) if n > 1 else 0.0
    cwm_mean = cwm_arr.mean()
    cwm_std = cwm_arr.std(ddof=1) if n > 1 else 0.0

    print(f"\n{'='*60}")
    print("14B seed-level summary")
    print(f"{'='*60}")
    print(f"CLS: {cls_mean:.2f} ± {cls_std:.2f}  (seeds: {cls_vals})")
    print(f"CWM: {cwm_mean:.2f} ± {cwm_std:.2f}  (seeds: {cwm_vals})")
    print(f"Gap: CLS - CWM = {cls_mean - cwm_mean:+.2f} pp")

    # ── Clustered bootstrap TOST (PRIMARY) ───────────────────────────
    if args.pairs:
        if len(args.pairs) % 2 != 0:
            ap.error("--pairs requires even number of files (CLS/CWM alternating)")

        n_pairs = len(args.pairs) // 2
        print(f"\n{'='*60}")
        print(f"CLUSTERED BOOTSTRAP TOST (paper method, {args.n_resamples} resamples)")
        print(f"{'='*60}")

        all_diffs = defaultdict(list)
        for i in range(n_pairs):
            cls_path = args.pairs[2 * i]
            cwm_path = args.pairs[2 * i + 1]
            print(f"  Pair {i+1}: {cls_path} vs {cwm_path}")
            cls_preds = load_predictions(cls_path)
            cwm_preds = load_predictions(cwm_path)
            r = align_and_diff(cls_preds, cwm_preds)
            print(f"    CLS={r['cls_acc']*100:.2f}%  CWM={r['cwm_acc']*100:.2f}%  "
                  f"diff={r['mean_diff']*100:+.2f}pp  (n={r['n']})")
            for pid, diffs in r["diffs_by_pid"].items():
                all_diffs[pid].extend(diffs)

        result = clustered_bootstrap_tost(all_diffs, args.n_resamples, args.seed, args.margin)

        print(f"\n  Observed mean diff (CLS-CWM): {result['observed_mean_pp']:+.3f} pp")
        print(f"  95% CI: [{result['ci95_pp'][0]:+.3f}, {result['ci95_pp'][1]:+.3f}] pp")
        print(f"  Bootstrap SE: {result['bootstrap_se_pp']:.3f} pp")
        print(f"  Clusters: {result['n_clusters']}, Total obs: {result['n_total']}")
        print(f"\n  TOST equivalence (±{args.margin} pp):")
        print(f"    90% CI: [{result['tost_90ci_pp'][0]:+.3f}, {result['tost_90ci_pp'][1]:+.3f}] pp")
        print(f"    p-value: {result['tost_p']:.4f}  ← USE THIS IN PAPER")
        print(f"    Equivalent: {'YES' if result['equivalent'] else 'NO'}")

        with open("14b_tost_bootstrap.json", "w") as f:
            json.dump(result, f, indent=2)
        print(f"\n  Saved to 14b_tost_bootstrap.json")
    else:
        print(f"\n  [No --pairs provided; skipping clustered bootstrap TOST]")
        print(f"  To run paper-method TOST, provide prediction JSONL files:")
        print(f"    --pairs cls_s42.jsonl cwm_s42.jsonl cls_s123.jsonl cwm_s123.jsonl ...")

    # ── Parametric TOST (sanity check) ───────────────────────────────
    print(f"\n{'='*60}")
    print("PARAMETRIC TOST (sanity check only — NOT for paper)")
    print(f"{'='*60}")
    if n >= 2:
        p_equiv, diff, se = tost_parametric(cls_arr, cwm_arr, SESOI)
        print(f"  Mean diff (CLS-CWM): {diff:+.4f}")
        print(f"  SE: {se:.4f}")
        print(f"  p-value: {p_equiv:.4f}")
        tag = "Equivalent" if p_equiv < 0.05 else "NOT equivalent"
        print(f"  → {tag} at α=0.05")
        print(f"  ⚠ This uses independent-samples t-test on seed-level means.")
        print(f"    Paper uses clustered bootstrap (ICC=0.191). Use --pairs for paper numbers.")
    else:
        print("  Skipped (need ≥2 seeds)")

    # ── Deltas and LaTeX ─────────────────────────────────────────────
    cls_delta = cls_mean - CLS_8B_MEAN
    cwm_delta = cwm_mean - CWM_8B_MEAN

    print(f"\n{'='*60}")
    print("Updated LaTeX rows for tab:scaling")
    print(f"{'='*60}")

    if n == 3:
        print("% NOTE: Add s456 column to table header")
        print(f"% \\textbf{{Method}} & \\textbf{{Size}} & \\textbf{{s42}} & \\textbf{{s123}} & \\textbf{{s456}} & \\textbf{{Mean}} & \\textbf{{$\\Delta$}} \\\\")
        print()
        s42c, s123c, s456c = CLS_SEEDS["s42"], CLS_SEEDS["s123"], CLS_SEEDS["s456"]
        s42w, s123w, s456w = CWM_SEEDS["s42"], CWM_SEEDS["s123"], CWM_SEEDS["s456"]
        print(f" & 14B & {s42c:.2f} & {s123c:.2f} & {s456c:.2f} & \\textbf{{{cls_mean:.2f} $\\pm$ {cls_std:.2f}}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {s42w:.2f} & {s123w:.2f} & {s456w:.2f} & {cwm_mean:.2f} $\\pm$ {cwm_std:.2f} & {fmt_delta(cwm_delta)} \\\\")
    elif n == 2:
        available = {s: (CLS_SEEDS[s], CWM_SEEDS[s]) for s in seeds_present}
        s_names = list(available.keys())
        print(f" & 14B & {available[s_names[0]][0]:.2f} & {available[s_names[1]][0]:.2f} & \\textbf{{{cls_mean:.2f}}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {available[s_names[0]][1]:.2f} & {available[s_names[1]][1]:.2f} & {cwm_mean:.2f} & {fmt_delta(cwm_delta)} \\\\")
    else:
        print(f" & 14B & {cls_vals[0]:.2f} & --- & {cls_vals[0]:.2f}\\textsuperscript{{$\\dagger$}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {cwm_vals[0]:.2f} & --- & {cwm_vals[0]:.2f}\\textsuperscript{{$\\dagger$}} & {fmt_delta(cwm_delta)} \\\\")

    if n == 3:
        print(f"\n% Suggested caption update:")
        print(f"% Seeds 42/123/456 (14B), seeds 42/123 (4B/8B). All bfloat16 inference.")
        print(f"% Remove 'exploratory' qualifier for 14B.")


if __name__ == "__main__":
    main()
