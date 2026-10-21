"""Analyze free-form vs constrained decoding ablation.

Compares logprob variance, selection performance, QE signals, and parse rate
between constrained (exp_012_rerun_1024) and free-form (exp_freeform_ablation).

Input:
  - output/exp_012_rerun_1024/samples.jsonl (constrained baseline)
  - results/exp_freeform_ablation/samples.jsonl (free-form)
Output:
  - results/exp_freeform_ablation/ablation_report.json
Dependencies: code/{consistency,evaluation}.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

import numpy as np
from scipy.stats import spearmanr, rankdata

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))

from consistency import (
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1


CONSTRAINED_PATH = "output/exp_012_rerun_1024/samples.jsonl"
FREEFORM_PATH = "results/exp_freeform_ablation/samples.jsonl"


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def safe_spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    x, y = x[m], y[m]
    if len(x) < 3:
        return float("nan"), float("nan")
    r = spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def safe_auroc(scores, labels):
    scores, labels = np.asarray(scores, float), np.asarray(labels, int)
    if len(np.unique(labels)) < 2:
        return float("nan")
    n_pos = int((labels == 1).sum())
    n_neg = int((labels == 0).sum())
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    ranks = rankdata(scores)
    u = ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2
    return float(u / (n_pos * n_neg))


def compute_logprob_stats(data):
    """Per-instance logprob std and range across N samples."""
    stds, ranges = [], []
    for inst in data:
        lps = [lp for lp in inst.get("logprobs", []) if np.isfinite(lp)]
        if len(lps) < 2:
            continue
        stds.append(float(np.std(lps)))
        ranges.append(float(np.max(lps) - np.min(lps)))
    return stds, ranges


def compute_em_rate(samples, subtask):
    if subtask == "ner":
        keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    else:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", [])) for s in samples]
    if not keys:
        return 0.0
    return Counter(keys).most_common(1)[0][1] / len(keys)


def compute_vc(samples, subtask):
    N = len(samples)
    if N == 0:
        return 0.0
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
    return float(np.mean([v / N for v in counter.values()]))


def get_valid_samples(inst):
    """Return only parseable samples for a free-form instance."""
    samples = inst["samples"]
    ps = inst.get("parse_success", [True] * len(samples))
    return [s for j, s in enumerate(samples) if j < len(ps) and ps[j]]


def analyze_qe(data, subtask, is_freeform=False):
    """Compute 5 QE signals with rho and AUROC vs greedy F1."""
    f1s, sj_scores, fk_scores, lp_scores, em_scores, vc_scores = [], [], [], [], [], []

    for inst in data:
        gold = inst["gold"]
        samples = get_valid_samples(inst) if is_freeform else inst["samples"]

        if len(samples) < 2:
            continue

        if subtask == "ner" and not gold.get("entities"):
            continue
        if subtask == "re" and not gold.get("relations"):
            continue

        f1 = per_instance_f1(inst["greedy"], gold, subtask)

        sj_scores.append(structural_consistency_soft_jaccard(samples, subtask))
        fk_scores.append(fleiss_kappa_surface(samples, subtask))

        valid_lps = []
        if is_freeform:
            ps = inst.get("parse_success", [True] * len(inst["samples"]))
            for j, s in enumerate(inst["samples"]):
                if j < len(ps) and ps[j]:
                    lp = s.get("mean_logprob")
                    if lp is not None and np.isfinite(lp):
                        valid_lps.append(lp)
        else:
            for s in samples:
                lp = s.get("mean_logprob")
                if lp is not None and np.isfinite(lp):
                    valid_lps.append(lp)
        lp_scores.append(float(np.mean(valid_lps)) if valid_lps else float("nan"))

        em_scores.append(compute_em_rate(samples, subtask))
        vc_scores.append(compute_vc(samples, subtask))
        f1s.append(f1)

    labels = [1 if f > 0 else 0 for f in f1s]
    results = {}
    for name, scores in [("SJ", sj_scores), ("FK", fk_scores), ("logprob", lp_scores),
                          ("EM", em_scores), ("voting_conf", vc_scores)]:
        rho, p = safe_spearman(scores, f1s)
        auroc = safe_auroc(scores, labels)
        results[name] = {"rho": round(rho, 6), "p_rho": round(p, 6), "auroc": round(auroc, 6)}

    return results, len(f1s)


def selection_f1(data, subtask, is_freeform=False):
    """Logprob-based best-of-N selection vs greedy."""
    greedy_f1s, sel_f1s = [], []

    for inst in data:
        gold = inst["gold"]
        g_f1 = per_instance_f1(inst["greedy"], gold, subtask)
        greedy_f1s.append(g_f1)

        logprobs = inst.get("logprobs", [])
        samples = inst["samples"]

        candidates = []
        for j, s in enumerate(samples):
            if j >= len(logprobs):
                break
            if is_freeform:
                ps = inst.get("parse_success", [True] * len(samples))
                if j < len(ps) and not ps[j]:
                    continue
            candidates.append((logprobs[j], s))

        if candidates:
            _, best = max(candidates, key=lambda x: x[0])
            sel_f1s.append(per_instance_f1(best, gold, subtask))
        else:
            sel_f1s.append(g_f1)

    return float(np.mean(greedy_f1s)), float(np.mean(sel_f1s))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--constrained", default=CONSTRAINED_PATH)
    p.add_argument("--freeform", default=FREEFORM_PATH)
    p.add_argument("--output_dir", default="results/exp_freeform_ablation")
    args = p.parse_args()

    print("Loading data...")
    con = load_data(args.constrained)
    free = load_data(args.freeform)
    print(f"  Constrained: {len(con)} | Free-form: {len(free)}")

    report = {"constrained": {}, "freeform": {}, "comparison": {}}

    # 1. Logprob variance
    c_stds, c_ranges = compute_logprob_stats(con)
    f_stds, f_ranges = compute_logprob_stats(free)
    c_tied = sum(1 for r in c_ranges if r < 0.05) / len(c_ranges) if c_ranges else 0
    f_tied = sum(1 for r in f_ranges if r < 0.05) / len(f_ranges) if f_ranges else 0

    report["constrained"]["logprob_variance"] = {
        "mean_std": round(float(np.mean(c_stds)), 6),
        "median_std": round(float(np.median(c_stds)), 6),
        "mean_range": round(float(np.mean(c_ranges)), 6),
        "median_range": round(float(np.median(c_ranges)), 6),
        "tied_pct": round(c_tied * 100, 1),
        "n": len(c_stds),
    }
    report["freeform"]["logprob_variance"] = {
        "mean_std": round(float(np.mean(f_stds)), 6),
        "median_std": round(float(np.median(f_stds)), 6),
        "mean_range": round(float(np.mean(f_ranges)), 6),
        "median_range": round(float(np.median(f_ranges)), 6),
        "tied_pct": round(f_tied * 100, 1),
        "n": len(f_stds),
    }

    print(f"\n=== Logprob Variance ===")
    print(f"  Constrained: std={np.mean(c_stds):.4f} range={np.mean(c_ranges):.4f} tied={c_tied:.1%}")
    print(f"  Free-form:   std={np.mean(f_stds):.4f} range={np.mean(f_ranges):.4f} tied={f_tied:.1%}")

    # 2. Parse rate
    total_s = sum(len(inst.get("parse_success", [])) for inst in free)
    total_p = sum(sum(inst.get("parse_success", [])) for inst in free)
    parse_rate = total_p / total_s * 100 if total_s > 0 else 0
    report["freeform"]["parse_rate"] = {
        "total_samples": total_s,
        "parsed": total_p,
        "rate_pct": round(parse_rate, 2),
    }
    print(f"\n=== Parse Rate: {parse_rate:.1f}% ({total_p}/{total_s}) ===")

    # 3. Selection F1
    print(f"\n=== Selection F1 ===")
    for st in ["ner", "re"]:
        c_g, c_s = selection_f1(con, st, is_freeform=False)
        f_g, f_s = selection_f1(free, st, is_freeform=True)
        report["constrained"][f"selection_{st}"] = {
            "greedy": round(c_g, 4), "selected": round(c_s, 4), "gap": round(c_s - c_g, 4),
        }
        report["freeform"][f"selection_{st}"] = {
            "greedy": round(f_g, 4), "selected": round(f_s, 4), "gap": round(f_s - f_g, 4),
        }
        print(f"  [{st.upper()}] Con: {c_g:.4f} -> {c_s:.4f} ({c_s-c_g:+.4f}) | "
              f"Free: {f_g:.4f} -> {f_s:.4f} ({f_s-f_g:+.4f})")

    # 4. QE metrics (5 signals)
    print(f"\n=== QE Metrics ===")
    for st in ["ner", "re"]:
        c_qe, c_n = analyze_qe(con, st, is_freeform=False)
        f_qe, f_n = analyze_qe(free, st, is_freeform=True)
        report["constrained"][f"qe_{st}"] = {"n": c_n, "signals": c_qe}
        report["freeform"][f"qe_{st}"] = {"n": f_n, "signals": f_qe}

        print(f"\n  [{st.upper()}] n_con={c_n} n_free={f_n}")
        print(f"  {'Signal':<12} {'C_rho':>8} {'C_AUROC':>8} {'F_rho':>8} {'F_AUROC':>8} {'delta_rho':>10}")
        for sig in ["SJ", "FK", "logprob", "EM", "voting_conf"]:
            cr, ca = c_qe[sig]["rho"], c_qe[sig]["auroc"]
            fr, fa = f_qe[sig]["rho"], f_qe[sig]["auroc"]
            dr = fr - cr if np.isfinite(fr) and np.isfinite(cr) else float("nan")
            print(f"  {sig:<12} {cr:>8.4f} {ca:>8.4f} {fr:>8.4f} {fa:>8.4f} {dr:>+10.4f}")

    # 5. Comparison summary
    report["comparison"] = {
        "variance_ratio_std": round(float(np.mean(f_stds) / max(np.mean(c_stds), 1e-8)), 2),
        "variance_ratio_range": round(float(np.mean(f_ranges) / max(np.mean(c_ranges), 1e-8)), 2),
        "tied_reduction_pp": round((c_tied - f_tied) * 100, 1),
        "parse_rate_pct": round(parse_rate, 2),
    }

    os.makedirs(args.output_dir, exist_ok=True)
    report_path = os.path.join(args.output_dir, "ablation_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n=== Summary ===")
    print(f"Variance ratio (std):   {report['comparison']['variance_ratio_std']}x")
    print(f"Variance ratio (range): {report['comparison']['variance_ratio_range']}x")
    print(f"Tied reduction:         {report['comparison']['tied_reduction_pp']:+.1f}pp")
    print(f"Parse rate:             {parse_rate:.1f}%")
    print(f"\nReport: {report_path}")


if __name__ == "__main__":
    main()
