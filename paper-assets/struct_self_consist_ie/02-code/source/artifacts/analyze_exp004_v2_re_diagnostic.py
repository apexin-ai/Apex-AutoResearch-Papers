"""exp-004 v2: RE relation-type stratified diagnostic analysis.

Per-relation-type consistency breakdown, bootstrap CI for all rho comparisons,
threshold sensitivity analysis. CPU-only.
Uses exp_012_logprob/samples_with_logprobs.jsonl (SciERC NER+RE, 16 samples + greedy + logprobs).
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from consistency import (
    compute_all_consistency_scores,
    structural_consistency_soft_jaccard,
    fleiss_kappa_surface,
)
from evaluation import per_instance_f1, relation_strict_match

BASE = Path("/root/autodl-tmp/struct_self_consist_ie")
DATA_PATH = BASE / "output" / "exp_012_logprob" / "samples_with_logprobs.jsonl"
OUT_DIR = BASE / "output" / "exp004v2_re_diagnostic"

RELATION_TYPES = [
    "USED-FOR", "PART-OF", "FEATURE-OF", "COMPARE",
    "CONJUNCTION", "HYPONYM-OF", "EVALUATE-FOR",
]


def load_data(path):
    instances = []
    with open(path) as f:
        for line in f:
            if line.strip():
                instances.append(json.loads(line))
    return instances


# ── Signal computation ─────────────────────────────────────────────────

def compute_re_sj(instances):
    scores = structural_consistency_soft_jaccard(instances, subtask="re")
    return scores


def compute_re_fk(instances):
    return [fleiss_kappa_surface(inst["samples"], subtask="re") for inst in instances]


def compute_voting_confidence(instances):
    results = []
    for inst in instances:
        N = len(inst["samples"])
        counter = Counter()
        for s in inst["samples"]:
            for r in s.get("relations", []):
                counter[(r["head"], r["tail"], r["type"])] += 1
        if not counter:
            results.append(0.0)
        else:
            rates = [v / N for v in counter.values()]
            results.append(float(np.mean(rates)))
    return results


def compute_mean_logprob(instances):
    results = []
    for inst in instances:
        lps = [s["mean_logprob"] for s in inst["samples"]
               if s.get("mean_logprob") is not None and np.isfinite(s["mean_logprob"])]
        results.append(float(np.mean(lps)) if lps else float("nan"))
    return results


def compute_exact_match_rate(instances):
    results = []
    for inst in instances:
        keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", []))
                for s in inst["samples"]]
        counter = Counter(keys)
        results.append(counter.most_common(1)[0][1] / len(keys))
    return results


def compute_re_f1_scores(instances):
    return [per_instance_f1(inst["greedy"], inst["gold"], "re") for inst in instances]


# ── Type-filtered signal computation ──────────────────────────────────

def _filter_rels(extraction, rtype):
    return [r for r in extraction.get("relations", []) if r["type"] == rtype]


def _filter_instance(inst, rtype):
    return {
        "id": inst["id"],
        "gold": {**inst["gold"], "relations": _filter_rels(inst["gold"], rtype)},
        "greedy": {**inst["greedy"], "relations": _filter_rels(inst["greedy"], rtype)},
        "samples": [{**s, "relations": _filter_rels(s, rtype)} for s in inst["samples"]],
    }


def type_filtered_f1(inst, rtype):
    gold_rels = _filter_rels(inst["gold"], rtype)
    pred_rels = _filter_rels(inst["greedy"], rtype)
    tp, fp, fn = relation_strict_match(pred_rels, gold_rels)
    if tp + fp + fn == 0:
        return float("nan")
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0


def type_filtered_sj(inst, rtype):
    filtered = _filter_instance(inst, rtype)
    samples = filtered["samples"]
    n = len(samples)
    if n <= 1:
        return 1.0
    from consistency import _re_soft_jaccard_pair
    scores = []
    for i, j in combinations(range(n), 2):
        scores.append(_re_soft_jaccard_pair(
            samples[i].get("relations", []),
            samples[j].get("relations", []),
        ))
    return float(np.mean(scores))


def type_filtered_voting(inst, rtype):
    N = len(inst["samples"])
    counter = Counter()
    for s in inst["samples"]:
        for r in s.get("relations", []):
            if r["type"] == rtype:
                counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


# ── AUROC ──────────────────────────────────────────────────────────────

def auroc(scores, labels):
    scores = np.array(scores, dtype=float)
    labels = np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float("nan")
    pos = scores[labels == 1]
    neg = scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    count = sum(np.sum(p > neg) + 0.5 * np.sum(p == neg) for p in pos)
    return count / (len(pos) * len(neg))


# ── Bootstrap CI ───────────────────────────────────────────────────────

def bootstrap_rho_ci(signal, quality, n_boot=10000, alpha=0.05, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    signal = np.array(signal, dtype=float)
    quality = np.array(quality, dtype=float)
    mask = np.isfinite(signal) & np.isfinite(quality)
    signal, quality = signal[mask], quality[mask]
    n = len(signal)
    if n < 5:
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": n}
    point_rho = float(spearmanr(signal, quality).statistic)
    rhos = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        r = spearmanr(signal[idx], quality[idx]).statistic
        if np.isfinite(r):
            rhos.append(float(r))
    rhos.sort()
    lo = float(np.percentile(rhos, 100 * alpha / 2)) if rhos else float("nan")
    hi = float(np.percentile(rhos, 100 * (1 - alpha / 2))) if rhos else float("nan")
    return {"rho": round(point_rho, 4), "ci_lo": round(lo, 4), "ci_hi": round(hi, 4), "n": n}


# ── Per-relation-type analysis ─────────────────────────────────────────

def per_relation_type_analysis(data):
    re_insts = [d for d in data if d["gold"]["relations"]]

    # Pre-compute instance-level signals
    all_sj = compute_re_sj(re_insts)
    all_fk = compute_re_fk(re_insts)
    all_vc = compute_voting_confidence(re_insts)
    all_lp = compute_mean_logprob(re_insts)
    all_em = compute_exact_match_rate(re_insts)
    all_f1 = compute_re_f1_scores(re_insts)

    results = {}
    rng = np.random.default_rng(42)

    for rtype in RELATION_TYPES:
        # Instance-level: instances containing this relation type
        indices = [i for i, inst in enumerate(re_insts)
                   if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        n = len(indices)
        if n < 5:
            results[rtype] = {"n_instances": n, "skip": True, "reason": "too few instances"}
            continue

        sj = [all_sj[i] for i in indices]
        fk = [all_fk[i] for i in indices]
        vc = [all_vc[i] for i in indices]
        lp = [all_lp[i] for i in indices]
        em = [all_em[i] for i in indices]
        f1 = [all_f1[i] for i in indices]

        binary_labels = [1 if x > 0 else 0 for x in f1]

        signal_names = ["soft_jaccard", "fleiss_kappa", "voting_conf", "mean_logprob", "exact_match"]
        signal_vals = [sj, fk, vc, lp, em]

        metrics = {}
        for sname, sval in zip(signal_names, signal_vals):
            valid = [(s, q) for s, q in zip(sval, f1) if np.isfinite(s) and np.isfinite(q)]
            if len(valid) < 5:
                metrics[sname] = {"rho": float("nan"), "auroc": float("nan"),
                                  "bootstrap": {"rho": float("nan"), "ci_lo": float("nan"),
                                                "ci_hi": float("nan"), "n": len(valid)}}
                continue
            sv, qv = zip(*valid)
            rho_val = float(spearmanr(sv, qv).statistic)
            auc_val = auroc(list(sv), [1 if q > 0 else 0 for q in qv])
            boot = bootstrap_rho_ci(list(sv), list(qv), n_boot=10000, rng=rng)
            metrics[sname] = {"rho": round(rho_val, 4), "auroc": round(auc_val, 4), "bootstrap": boot}

        # Type-filtered analysis
        type_filtered = {}
        insts_for_type = [re_insts[i] for i in indices]
        tf_f1 = [type_filtered_f1(inst, rtype) for inst in insts_for_type]
        tf_sj = [type_filtered_sj(inst, rtype) for inst in insts_for_type]
        tf_vc = [type_filtered_voting(inst, rtype) for inst in insts_for_type]

        # Filter out nan F1 (instances where this type has 0 gold AND 0 pred -> nan)
        valid_tf = [(i, f) for i, f in enumerate(tf_f1) if np.isfinite(f)]
        if len(valid_tf) >= 5:
            tf_idx = [v[0] for v in valid_tf]
            tf_f1_v = [v[1] for v in valid_tf]
            tf_sj_v = [tf_sj[i] for i in tf_idx]
            tf_vc_v = [tf_vc[i] for i in tf_idx]

            tf_rho_sj = float(spearmanr(tf_sj_v, tf_f1_v).statistic) if len(tf_f1_v) >= 5 else float("nan")
            tf_rho_vc = float(spearmanr(tf_vc_v, tf_f1_v).statistic) if len(tf_f1_v) >= 5 else float("nan")
            tf_boot_sj = bootstrap_rho_ci(tf_sj_v, tf_f1_v, n_boot=10000, rng=rng)
            tf_boot_vc = bootstrap_rho_ci(tf_vc_v, tf_f1_v, n_boot=10000, rng=rng)

            type_filtered = {
                "n_valid": len(valid_tf),
                "sj": {"rho": round(tf_rho_sj, 4), "bootstrap": tf_boot_sj},
                "voting_conf": {"rho": round(tf_rho_vc, 4), "bootstrap": tf_boot_vc},
            }

        results[rtype] = {
            "n_instances": n,
            "mean_greedy_f1": round(float(np.mean(f1)), 4),
            "std_greedy_f1": round(float(np.std(f1)), 4),
            "pct_correct": round(100 * sum(1 for x in f1 if x > 0) / n, 1),
            "instance_level_metrics": metrics,
            "type_filtered": type_filtered if type_filtered else None,
        }

    return results


# ── Threshold sensitivity ──────────────────────────────────────────────

def threshold_sensitivity(data):
    re_insts = [d for d in data if d["gold"]["relations"]]
    sj_scores = compute_re_sj(re_insts)
    vc_scores = compute_voting_confidence(re_insts)
    f1_scores = compute_re_f1_scores(re_insts)

    thresholds = np.arange(0.0, 1.01, 0.05)
    results = {"sj_thresholds": [], "vc_thresholds": []}

    for thr in thresholds:
        thr = round(float(thr), 2)
        for signal_name, signal_vals in [("sj", sj_scores), ("vc", vc_scores)]:
            accepted = [(s, f) for s, f in zip(signal_vals, f1_scores) if s >= thr]
            rejected = [(s, f) for s, f in zip(signal_vals, f1_scores) if s < thr]
            n_accepted = len(accepted)
            n_rejected = len(rejected)
            if n_accepted == 0:
                mean_f1_accepted = float("nan")
                pct_correct_accepted = float("nan")
            else:
                mean_f1_accepted = float(np.mean([f for _, f in accepted]))
                pct_correct_accepted = 100 * sum(1 for _, f in accepted if f > 0) / n_accepted
            if n_rejected == 0:
                mean_f1_rejected = float("nan")
                pct_correct_rejected = float("nan")
            else:
                mean_f1_rejected = float(np.mean([f for _, f in rejected]))
                pct_correct_rejected = 100 * sum(1 for _, f in rejected if f > 0) / n_rejected

            coverage = n_accepted / len(f1_scores) if f1_scores else 0

            entry = {
                "threshold": thr,
                "n_accepted": n_accepted,
                "n_rejected": n_rejected,
                "coverage": round(coverage, 4),
                "mean_f1_accepted": round(mean_f1_accepted, 4) if np.isfinite(mean_f1_accepted) else None,
                "mean_f1_rejected": round(mean_f1_rejected, 4) if np.isfinite(mean_f1_rejected) else None,
                "pct_correct_accepted": round(pct_correct_accepted, 1) if np.isfinite(pct_correct_accepted) else None,
                "pct_correct_rejected": round(pct_correct_rejected, 1) if np.isfinite(pct_correct_rejected) else None,
            }
            results[f"{signal_name}_thresholds"].append(entry)

    # Per-relation-type threshold sensitivity for SJ
    re_insts_with_sj = list(zip(re_insts, sj_scores, f1_scores))
    results["per_type_sj_thresholds"] = {}
    for rtype in RELATION_TYPES:
        type_data = [(inst, sj, f1) for inst, sj, f1 in re_insts_with_sj
                     if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        if len(type_data) < 10:
            continue
        type_results = []
        for thr in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
            thr = round(thr, 2)
            acc = [f1 for _, sj, f1 in type_data if sj >= thr]
            rej = [f1 for _, sj, f1 in type_data if sj < thr]
            type_results.append({
                "threshold": thr,
                "n_accepted": len(acc),
                "coverage": round(len(acc) / len(type_data), 4),
                "mean_f1_accepted": round(float(np.mean(acc)), 4) if acc else None,
                "mean_f1_rejected": round(float(np.mean(rej)), 4) if rej else None,
            })
        results["per_type_sj_thresholds"][rtype] = type_results

    return results


# ── Cross-type bootstrap comparison ───────────────────────────────────

def cross_type_comparison(data):
    re_insts = [d for d in data if d["gold"]["relations"]]
    all_sj = compute_re_sj(re_insts)
    all_f1 = compute_re_f1_scores(re_insts)

    rng = np.random.default_rng(42)
    type_rhos = {}
    for rtype in RELATION_TYPES:
        indices = [i for i, inst in enumerate(re_insts)
                   if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        if len(indices) < 10:
            continue
        sj = [all_sj[i] for i in indices]
        f1 = [all_f1[i] for i in indices]
        type_rhos[rtype] = bootstrap_rho_ci(sj, f1, n_boot=10000, rng=rng)

    # Pairwise comparisons via bootstrap difference
    comparisons = {}
    for i, t1 in enumerate(RELATION_TYPES):
        for t2 in RELATION_TYPES[i+1:]:
            if t1 not in type_rhos or t2 not in type_rhos:
                continue
            idx1 = [i for i, inst in enumerate(re_insts)
                    if any(r["type"] == t1 for r in inst["gold"]["relations"])]
            idx2 = [i for i, inst in enumerate(re_insts)
                    if any(r["type"] == t2 for r in inst["gold"]["relations"])]

            sj1 = np.array([all_sj[i] for i in idx1])
            f11 = np.array([all_f1[i] for i in idx1])
            sj2 = np.array([all_sj[i] for i in idx2])
            f12 = np.array([all_f1[i] for i in idx2])

            diffs = []
            for _ in range(10000):
                b1 = rng.integers(0, len(sj1), size=len(sj1))
                b2 = rng.integers(0, len(sj2), size=len(sj2))
                r1 = spearmanr(sj1[b1], f11[b1]).statistic
                r2 = spearmanr(sj2[b2], f12[b2]).statistic
                if np.isfinite(r1) and np.isfinite(r2):
                    diffs.append(r1 - r2)
            if diffs:
                diffs.sort()
                lo = float(np.percentile(diffs, 2.5))
                hi = float(np.percentile(diffs, 97.5))
                comparisons[f"{t1}_vs_{t2}"] = {
                    "delta_rho": round(type_rhos[t1]["rho"] - type_rhos[t2]["rho"], 4),
                    "ci_lo": round(lo, 4),
                    "ci_hi": round(hi, 4),
                    "significant": not (lo <= 0 <= hi),
                }

    return {"type_rhos": type_rhos, "pairwise_comparisons": comparisons}


# ── Main ───────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print(f"Loading data from {DATA_PATH} ...")
    data = load_data(DATA_PATH)
    re_data = [d for d in data if d["gold"]["relations"]]
    print(f"  {len(data)} total instances, {len(re_data)} with gold relations")

    # Gold relation type distribution
    type_counts = Counter()
    for inst in re_data:
        for r in inst["gold"]["relations"]:
            type_counts[r["type"]] += 1
    print("\nGold relation type distribution:")
    for t, c in type_counts.most_common():
        print(f"  {t:15s}  {c:4d}")

    # 1. Per-relation-type analysis
    print("\n[1/3] Per-relation-type analysis (instance-level + type-filtered) ...")
    rt_results = per_relation_type_analysis(data)
    with open(OUT_DIR / "per_relation_type.json", "w") as f:
        json.dump(rt_results, f, indent=2)

    print(f"\n{'Type':>15s}  {'N':>4s}  {'F1':>5s}  {'rho_SJ':>7s}  {'rho_FK':>7s}  {'rho_VC':>7s}  {'rho_LP':>7s}  {'rho_EM':>7s}  {'AUC_SJ':>7s}")
    for rtype in RELATION_TYPES:
        r = rt_results.get(rtype, {})
        if r.get("skip"):
            print(f"  {rtype:>15s}  {r['n_instances']:4d}  -- skipped ({r.get('reason', '')})")
            continue
        m = r["instance_level_metrics"]
        rho_sj = m["soft_jaccard"]["rho"]
        rho_fk = m["fleiss_kappa"]["rho"]
        rho_vc = m["voting_conf"]["rho"]
        rho_lp = m["mean_logprob"]["rho"]
        rho_em = m["exact_match"]["rho"]
        auc_sj = m["soft_jaccard"]["auroc"]
        def _fmt(v):
            return f"{v:+.3f}" if np.isfinite(v) else "    N/A"
        print(f"  {rtype:>15s}  {r['n_instances']:4d}  {r['mean_greedy_f1']:.3f}  "
              f"{_fmt(rho_sj)}  {_fmt(rho_fk)}  {_fmt(rho_vc)}  {_fmt(rho_lp)}  {_fmt(rho_em)}  {_fmt(auc_sj)}")

    # Bootstrap CI summary
    print("\nBootstrap 95% CI for SJ rho per relation type:")
    for rtype in RELATION_TYPES:
        r = rt_results.get(rtype, {})
        if r.get("skip"):
            continue
        b = r["instance_level_metrics"]["soft_jaccard"]["bootstrap"]
        print(f"  {rtype:>15s}  rho={b['rho']:+.4f}  CI=[{b['ci_lo']:+.4f}, {b['ci_hi']:+.4f}]  n={b['n']}")

    # 2. Threshold sensitivity
    print("\n[2/3] Threshold sensitivity analysis ...")
    thr_results = threshold_sensitivity(data)
    with open(OUT_DIR / "threshold_sensitivity.json", "w") as f:
        json.dump(thr_results, f, indent=2)

    print(f"\n{'Signal':>6s}  {'Thr':>5s}  {'N_acc':>5s}  {'Cov':>5s}  {'F1_acc':>6s}  {'F1_rej':>6s}  {'%Corr':>5s}")
    for signal_key in ["sj_thresholds", "vc_thresholds"]:
        sig = signal_key.split("_")[0].upper()
        for entry in thr_results[signal_key]:
            if entry["threshold"] not in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                continue
            f1a = f"{entry['mean_f1_accepted']:.3f}" if entry["mean_f1_accepted"] is not None else "  N/A"
            f1r = f"{entry['mean_f1_rejected']:.3f}" if entry["mean_f1_rejected"] is not None else "  N/A"
            pct = f"{entry['pct_correct_accepted']:.0f}%" if entry["pct_correct_accepted"] is not None else " N/A"
            print(f"  {sig:>6s}  {entry['threshold']:5.2f}  {entry['n_accepted']:5d}  "
                  f"{entry['coverage']:.3f}  {f1a}  {f1r}  {pct}")

    # 3. Cross-type bootstrap comparison
    print("\n[3/3] Cross-type bootstrap comparison ...")
    cross_results = cross_type_comparison(data)
    with open(OUT_DIR / "cross_type_comparison.json", "w") as f:
        json.dump(cross_results, f, indent=2)

    print(f"\n{'Comparison':>30s}  {'Delta_rho':>9s}  {'CI_lo':>7s}  {'CI_hi':>7s}  {'Sig':>3s}")
    for pair, res in sorted(cross_results["pairwise_comparisons"].items()):
        sig = "*" if res["significant"] else ""
        print(f"  {pair:>30s}  {res['delta_rho']:+.4f}    {res['ci_lo']:+.4f}  {res['ci_hi']:+.4f}  {sig}")

    # Save combined report
    report = {
        "data_source": str(DATA_PATH),
        "total_instances": len(data),
        "re_instances": len(re_data),
        "gold_relation_type_counts": dict(type_counts.most_common()),
        "per_relation_type": rt_results,
        "threshold_sensitivity_summary": {
            "sj": [e for e in thr_results["sj_thresholds"] if e["threshold"] in [0.2, 0.3, 0.4, 0.5, 0.6]],
            "vc": [e for e in thr_results["vc_thresholds"] if e["threshold"] in [0.2, 0.3, 0.4, 0.5, 0.6]],
        },
        "cross_type_comparison": cross_results,
    }
    with open(OUT_DIR / "full_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nAll results saved to {OUT_DIR}/")


if __name__ == "__main__":
    main()
