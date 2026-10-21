#!/usr/bin/env python3
"""Paired t-test analysis: CED vs flat-NLI RSFT scoring methods on DocRE."""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

EVAL_DIR_MAP = {
    "CED": {
        42: "rsft_r2b",
        43: "rsft_s43",
        44: "rsft_s44",
        45: "rsft_ced_s45",
    },
    "flatNLI": {
        42: "rsft_flat_nli",
        43: "rsft_flat_nli_s43_reeval",
        44: "rsft_flat_nli_s44",
        45: "rsft_flat_nli_s45",
    },
}

METRICS = ["f1", "evi_f1", "ign_f1", "edcr", "evi_f1_joint"]


def load_metrics(eval_base: Path, method: str, seed: int, prefer_v2: bool = True):
    dir_name = EVAL_DIR_MAP[method][seed]
    eval_dir = eval_base / dir_name

    v2 = eval_dir / "metrics_v2.json"
    v1 = eval_dir / "metrics.json"

    path = None
    if prefer_v2 and v2.exists():
        path = v2
    elif v1.exists():
        path = v1

    if path is None:
        return None
    with open(path) as f:
        data = json.load(f)
    data["_source"] = str(path)
    return data


def load_predictions(eval_base: Path, method: str, seed: int):
    dir_name = EVAL_DIR_MAP[method][seed]
    path = eval_base / dir_name / "predictions.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)


def compute_per_doc_rel_f1(predictions: list) -> dict:
    """Per-document relation F1 based on (head, relation, tail) matching."""
    results = {}
    for doc in predictions:
        doc_id = doc["doc_id"]
        pred_set = {(t["head"], t["relation"], t["tail"]) for t in doc.get("parsed_triples", [])}
        gold_set = {(t["head"], t["relation"], t["tail"]) for t in doc.get("gold_triples", [])}
        tp = len(pred_set & gold_set)
        prec = tp / len(pred_set) if pred_set else 0.0
        rec = tp / len(gold_set) if gold_set else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
        results[doc_id] = f1
    return results


def paired_ttest(a: np.ndarray, b: np.ndarray) -> dict:
    n = len(a)
    diff = a - b
    mean_diff = float(np.mean(diff))
    std_diff = float(np.std(diff, ddof=1))
    se_diff = std_diff / np.sqrt(n)

    if std_diff == 0:
        return {
            "n": n, "mean_a": float(np.mean(a)), "std_a": float(np.std(a, ddof=1)),
            "mean_b": float(np.mean(b)), "std_b": float(np.std(b, ddof=1)),
            "mean_diff": mean_diff, "t_stat": float("nan"), "p_value": 1.0,
            "cohens_d": 0.0, "ci_95": [mean_diff, mean_diff],
        }

    t_stat, p_value = stats.ttest_rel(a, b)
    t_crit = stats.t.ppf(0.975, df=n - 1)
    ci_low = mean_diff - t_crit * se_diff
    ci_high = mean_diff + t_crit * se_diff
    cohens_d = mean_diff / std_diff

    return {
        "n": n,
        "mean_a": float(np.mean(a)),
        "std_a": float(np.std(a, ddof=1)),
        "mean_b": float(np.mean(b)),
        "std_b": float(np.std(b, ddof=1)),
        "mean_diff": mean_diff,
        "se_diff": float(se_diff),
        "t_stat": float(t_stat),
        "p_value": float(p_value),
        "cohens_d": float(cohens_d),
        "ci_95": [float(ci_low), float(ci_high)],
    }


def bootstrap_paired_diff(a: np.ndarray, b: np.ndarray, n_boot: int = 10000, rng_seed: int = 42) -> dict:
    rng = np.random.RandomState(rng_seed)
    n = len(a)
    diff = a - b
    observed = float(np.mean(diff))

    boot_means = np.array([np.mean(diff[rng.randint(0, n, size=n)]) for _ in range(n_boot)])
    ci_low, ci_high = np.percentile(boot_means, [2.5, 97.5])

    p_tail = np.mean(boot_means <= 0) if observed > 0 else np.mean(boot_means >= 0)
    p_value = float(2 * min(p_tail, 1 - p_tail))

    return {
        "mean_diff": observed,
        "boot_se": float(np.std(boot_means)),
        "boot_ci_95": [float(ci_low), float(ci_high)],
        "boot_p": float(p_value),
        "n_boot": n_boot,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Paired t-test: CED vs flat-NLI RSFT on DocRE",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python paired_ttest_analysis.py --eval-base /root/autodl-tmp/eval_results
  python paired_ttest_analysis.py --eval-base /root/autodl-tmp/eval_results --per-doc --output results.json
  python paired_ttest_analysis.py --seeds 42 43 44 --metrics f1 evi_f1 edcr""",
    )
    parser.add_argument("--eval-base", type=str, default="/root/autodl-tmp/eval_results")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 43, 44, 45])
    parser.add_argument("--metrics", type=str, nargs="+", default=METRICS)
    parser.add_argument("--prefer-v2", action="store_true", default=True,
                        help="Prefer metrics_v2.json (fixed ign_f1)")
    parser.add_argument("--bootstrap", type=int, default=10000)
    parser.add_argument("--per-doc", action="store_true",
                        help="Per-document paired bootstrap (loads predictions.json)")
    parser.add_argument("--output", type=str, default=None, help="Save JSON results")
    args = parser.parse_args()

    eval_base = Path(args.eval_base)

    # ── 1. Discover available seed pairs ─────────────────────────────────
    print("=" * 72)
    print("  Paired t-test: CED RSFT vs flat-NLI RSFT")
    print("=" * 72)

    ced_all, fnli_all = {}, {}
    available = []

    for seed in args.seeds:
        ced = load_metrics(eval_base, "CED", seed, args.prefer_v2)
        fnli = load_metrics(eval_base, "flatNLI", seed, args.prefer_v2)
        tag_c = f"✓ ({Path(ced['_source']).parent.name})" if ced else "✗"
        tag_f = f"✓ ({Path(fnli['_source']).parent.name})" if fnli else "✗"
        print(f"  seed {seed}:  CED {tag_c}   flatNLI {tag_f}")
        if ced and fnli:
            ced_all[seed] = ced
            fnli_all[seed] = fnli
            available.append(seed)

    n = len(available)
    print(f"\n  Matched pairs: {n}  (seeds {available})")

    if n < 2:
        print("\n  ERROR: need ≥2 matched pairs.")
        sys.exit(1)

    # ── 2. Seed-level paired t-test ──────────────────────────────────────
    all_results = {}

    header = f"  {'Metric':<16} {'CED mean±std':>16} {'fNLI mean±std':>16} {'Δ':>10} {'t':>8} {'p':>8} {'d':>8}"
    print(f"\n{header}")
    print(f"  {'-' * (len(header) - 2)}")

    for metric in args.metrics:
        pairs = [(ced_all[s].get(metric), fnli_all[s].get(metric)) for s in available]
        pairs = [(c, f) for c, f in pairs if c is not None and f is not None]
        if len(pairs) < 2:
            print(f"  {metric:<16}  (insufficient data)")
            continue

        a = np.array([c for c, _ in pairs])
        b = np.array([f for _, f in pairs])
        res = paired_ttest(a, b)

        sig = "***" if res["p_value"] < 0.001 else "**" if res["p_value"] < 0.01 else "*" if res["p_value"] < 0.05 else ""
        print(
            f"  {metric:<16} {res['mean_a']:.4f}±{res['std_a']:.4f}"
            f"  {res['mean_b']:.4f}±{res['std_b']:.4f}"
            f"  {res['mean_diff']:+.4f}"
            f"  {res['t_stat']:+6.3f}"
            f"  {res['p_value']:.4f}"
            f"  {res['cohens_d']:+.3f} {sig}"
        )

        res["ced_values"] = a.tolist()
        res["fnli_values"] = b.tolist()
        res["seeds"] = available

        if args.bootstrap > 0:
            res["bootstrap"] = bootstrap_paired_diff(a, b, n_boot=args.bootstrap)

        all_results[metric] = res

    print(f"  {'-' * (len(header) - 2)}")
    print(f"  df={n - 1}  |  *p<.05  **p<.01  ***p<.001")

    # ── 3. Bootstrap CIs ─────────────────────────────────────────────────
    if args.bootstrap > 0:
        print(f"\n  Bootstrap CIs ({args.bootstrap} resamples):")
        for metric, res in all_results.items():
            b = res.get("bootstrap")
            if b:
                print(
                    f"    {metric:<16} Δ={b['mean_diff']:+.4f}"
                    f"  95%CI [{b['boot_ci_95'][0]:+.4f}, {b['boot_ci_95'][1]:+.4f}]"
                    f"  boot-p={b['boot_p']:.4f}"
                )

    # ── 4. Per-document bootstrap ────────────────────────────────────────
    per_doc_results = {}
    if args.per_doc:
        print(f"\n{'=' * 72}")
        print("  Per-document paired bootstrap (rel_f1)")
        print("=" * 72)

        for seed in available:
            ced_preds = load_predictions(eval_base, "CED", seed)
            fnli_preds = load_predictions(eval_base, "flatNLI", seed)
            if not ced_preds or not fnli_preds:
                print(f"  seed {seed}: predictions unavailable")
                continue

            ced_doc = compute_per_doc_rel_f1(ced_preds)
            fnli_doc = compute_per_doc_rel_f1(fnli_preds)
            common = sorted(set(ced_doc) & set(fnli_doc))

            ca = np.array([ced_doc[d] for d in common])
            fa = np.array([fnli_doc[d] for d in common])

            boot = bootstrap_paired_diff(ca, fa, n_boot=args.bootstrap)
            t_stat, p_val = stats.ttest_rel(ca, fa)
            wins_ced = int(np.sum(ca > fa))
            wins_fnli = int(np.sum(fa > ca))
            ties = int(np.sum(ca == fa))

            print(
                f"  seed {seed} ({len(common)} docs):"
                f"  Δ={boot['mean_diff']:+.4f}"
                f"  95%CI [{boot['boot_ci_95'][0]:+.4f}, {boot['boot_ci_95'][1]:+.4f}]"
                f"  t={t_stat:+.3f} p={p_val:.4f}"
                f"  wins: CED={wins_ced} fNLI={wins_fnli} tie={ties}"
            )
            per_doc_results[seed] = {
                "n_docs": len(common),
                "mean_ced": float(np.mean(ca)),
                "mean_fnli": float(np.mean(fa)),
                "t_stat": float(t_stat),
                "p_value": float(p_val),
                "bootstrap": boot,
                "wins_ced": wins_ced,
                "wins_fnli": wins_fnli,
                "ties": ties,
            }

        # Pooled across seeds
        if per_doc_results:
            print(f"\n  Pooled across seeds:")
            all_ced, all_fnli = [], []
            for seed in available:
                if seed not in per_doc_results:
                    continue
                ced_preds = load_predictions(eval_base, "CED", seed)
                fnli_preds = load_predictions(eval_base, "flatNLI", seed)
                ced_doc = compute_per_doc_rel_f1(ced_preds)
                fnli_doc = compute_per_doc_rel_f1(fnli_preds)
                common = sorted(set(ced_doc) & set(fnli_doc))
                all_ced.extend([ced_doc[d] for d in common])
                all_fnli.extend([fnli_doc[d] for d in common])

            ca = np.array(all_ced)
            fa = np.array(all_fnli)
            boot = bootstrap_paired_diff(ca, fa, n_boot=args.bootstrap)
            t_stat, p_val = stats.ttest_rel(ca, fa)
            print(
                f"    {len(ca)} doc-pairs:"
                f"  Δ={boot['mean_diff']:+.4f}"
                f"  95%CI [{boot['boot_ci_95'][0]:+.4f}, {boot['boot_ci_95'][1]:+.4f}]"
                f"  t={t_stat:+.3f} p={p_val:.4f}"
            )

    # ── 5. Interpretation ────────────────────────────────────────────────
    print(f"\n{'=' * 72}")
    print("  Summary")
    print("=" * 72)

    r = all_results.get("f1")
    if r:
        p = r["p_value"]
        d = r["cohens_d"]
        direction = "CED > flatNLI" if r["mean_diff"] > 0 else "flatNLI > CED"
        if p < 0.05:
            print(f"  rel_f1: significant ({direction}), p={p:.4f}, d={d:+.3f}")
        else:
            print(f"  rel_f1: NOT significant (p={p:.4f}, d={d:+.3f}, direction: {direction})")
        if n <= 4:
            print(f"  ⚠  Only {n} pairs (df={n-1}). Power is low; complete 4 seeds before concluding.")

    # ── 6. Save ──────────────────────────────────────────────────────────
    if args.output:
        out = {
            "config": {
                "eval_base": str(eval_base),
                "seeds_requested": args.seeds,
                "seeds_available": available,
                "n_pairs": n,
                "prefer_v2": args.prefer_v2,
                "n_bootstrap": args.bootstrap,
            },
            "seed_level": all_results,
        }
        if per_doc_results:
            out["per_document"] = {str(k): v for k, v in per_doc_results.items()}
        with open(args.output, "w") as f:
            json.dump(out, f, indent=2)
        print(f"\n  Results saved to {args.output}")


if __name__ == "__main__":
    main()
