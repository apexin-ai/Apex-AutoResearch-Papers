"""exp-004 v2: RE relation-type stratified diagnostic analysis.

Per-relation-type consistency breakdown, bootstrap CI for all rho comparisons,
threshold sensitivity analysis. CPU-only.
"""

from __future__ import annotations

import json
import os
import sys
import warnings
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

warnings.filterwarnings("ignore", category=RuntimeWarning)

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from consistency import compute_all_consistency_scores
from evaluation import per_instance_f1, relation_strict_match

BASE = Path("/root/autodl-tmp/struct_self_consist_ie")
DATA_PATH = BASE / "output" / "exp_012_logprob" / "samples_with_logprobs.jsonl"
OUT_DIR = BASE / "output" / "exp004v2_re_diagnostic"

RELATION_TYPES = [
    "USED-FOR", "PART-OF", "FEATURE-OF", "COMPARE",
    "CONJUNCTION", "HYPONYM-OF", "EVALUATE-FOR",
]
N_BOOT = 5000


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_voting_confidence(inst):
    N = len(inst["samples"])
    counter = Counter()
    for s in inst["samples"]:
        for r in s.get("relations", []):
            counter[(r["head"], r["tail"], r["type"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def compute_mean_logprob(inst):
    lps = [s["mean_logprob"] for s in inst["samples"]
           if s.get("mean_logprob") is not None and np.isfinite(s["mean_logprob"])]
    return float(np.mean(lps)) if lps else float("nan")


def compute_exact_match_rate(inst):
    keys = [frozenset((r["head"], r["tail"], r["type"]) for r in s.get("relations", []))
            for s in inst["samples"]]
    counter = Counter(keys)
    return counter.most_common(1)[0][1] / len(keys)


def auroc(scores, labels):
    scores, labels = np.array(scores, dtype=float), np.array(labels, dtype=int)
    if len(set(labels)) < 2:
        return float("nan")
    pos, neg = scores[labels == 1], scores[labels == 0]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    return sum(np.sum(p > neg) + 0.5 * np.sum(p == neg) for p in pos) / (len(pos) * len(neg))


def bootstrap_rho_ci(signal, quality, n_boot=N_BOOT, rng=None):
    if rng is None:
        rng = np.random.default_rng(42)
    signal, quality = np.array(signal, dtype=float), np.array(quality, dtype=float)
    mask = np.isfinite(signal) & np.isfinite(quality)
    signal, quality = signal[mask], quality[mask]
    n = len(signal)
    if n < 5:
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": n}
    point_rho = float(spearmanr(signal, quality).statistic)
    if np.isnan(point_rho):
        return {"rho": float("nan"), "ci_lo": float("nan"), "ci_hi": float("nan"), "n": n}
    rhos = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        r = spearmanr(signal[idx], quality[idx]).statistic
        if np.isfinite(r):
            rhos.append(float(r))
    rhos.sort()
    lo = float(np.percentile(rhos, 2.5)) if rhos else float("nan")
    hi = float(np.percentile(rhos, 97.5)) if rhos else float("nan")
    return {"rho": round(point_rho, 4), "ci_lo": round(lo, 4), "ci_hi": round(hi, 4), "n": n}


def type_filtered_f1(inst, rtype):
    gold = [r for r in inst["gold"].get("relations", []) if r["type"] == rtype]
    pred = [r for r in inst["greedy"].get("relations", []) if r["type"] == rtype]
    tp, fp, fn = relation_strict_match(pred, gold)
    if tp + fp + fn == 0:
        return float("nan")
    p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


def type_filtered_voting(inst, rtype):
    N = len(inst["samples"])
    counter = Counter()
    for s in inst["samples"]:
        for r in s.get("relations", []):
            if r["type"] == rtype:
                counter[(r["head"], r["tail"])] += 1
    if not counter:
        return 0.0
    return float(np.mean([v / N for v in counter.values()]))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"Loading data from {DATA_PATH} ...")
    data = load_data(DATA_PATH)
    re_data = [d for d in data if d["gold"]["relations"]]
    print(f"  {len(data)} total, {len(re_data)} with gold relations")

    type_counts = Counter()
    for inst in re_data:
        for r in inst["gold"]["relations"]:
            type_counts[r["type"]] += 1
    print("\nGold relation type distribution:")
    for t, c in type_counts.most_common():
        print(f"  {t:15s}  {c:4d}")

    # Compute all signals once
    print("\nComputing consistency scores ...")
    all_scores = compute_all_consistency_scores(re_data, subtask="re")
    all_sj = all_scores["soft_jaccard"]
    all_fk = all_scores["fleiss_kappa"]
    all_vc = [compute_voting_confidence(inst) for inst in re_data]
    all_lp = [compute_mean_logprob(inst) for inst in re_data]
    all_em = [compute_exact_match_rate(inst) for inst in re_data]
    all_f1 = [per_instance_f1(inst["greedy"], inst["gold"], "re") for inst in re_data]
    print("  Done.")

    signal_names = ["soft_jaccard", "fleiss_kappa", "voting_conf", "mean_logprob", "exact_match"]
    all_signals = [all_sj, all_fk, all_vc, all_lp, all_em]

    # ── 1. Per-relation-type analysis ──
    print("\n[1/3] Per-relation-type analysis ...")
    rng = np.random.default_rng(42)
    rt_results = {}

    for rtype in RELATION_TYPES:
        indices = [i for i, inst in enumerate(re_data)
                   if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        n = len(indices)
        if n < 5:
            rt_results[rtype] = {"n_instances": n, "skip": True}
            continue

        f1 = [all_f1[i] for i in indices]

        metrics = {}
        for sname, all_sig in zip(signal_names, all_signals):
            sig = [all_sig[i] for i in indices]
            valid = [(s, q) for s, q in zip(sig, f1) if np.isfinite(s) and np.isfinite(q)]
            if len(valid) < 5:
                metrics[sname] = {"rho": None, "auroc": None, "bootstrap": None}
                continue
            sv, qv = zip(*valid)
            rho_val = float(spearmanr(sv, qv).statistic)
            auc_val = auroc(list(sv), [1 if q > 0 else 0 for q in qv])
            boot = bootstrap_rho_ci(list(sv), list(qv), rng=rng)
            metrics[sname] = {
                "rho": round(rho_val, 4) if np.isfinite(rho_val) else None,
                "auroc": round(auc_val, 4) if np.isfinite(auc_val) else None,
                "bootstrap": boot,
            }

        # Type-filtered voting + F1
        insts_for_type = [re_data[i] for i in indices]
        tf_f1 = [type_filtered_f1(inst, rtype) for inst in insts_for_type]
        tf_vc = [type_filtered_voting(inst, rtype) for inst in insts_for_type]
        valid_tf = [(i, f) for i, f in enumerate(tf_f1) if np.isfinite(f)]
        tf_result = None
        if len(valid_tf) >= 5:
            tf_idx = [v[0] for v in valid_tf]
            tf_f1_v = [v[1] for v in valid_tf]
            tf_vc_v = [tf_vc[i] for i in tf_idx]
            boot_vc = bootstrap_rho_ci(tf_vc_v, tf_f1_v, rng=rng)
            tf_result = {"n_valid": len(valid_tf), "voting_conf": boot_vc}

        rt_results[rtype] = {
            "n_instances": n,
            "mean_greedy_f1": round(float(np.mean(f1)), 4),
            "std_greedy_f1": round(float(np.std(f1)), 4),
            "pct_correct": round(100 * sum(1 for x in f1 if x > 0) / n, 1),
            "instance_level_metrics": metrics,
            "type_filtered": tf_result,
        }

    with open(OUT_DIR / "per_relation_type.json", "w") as f:
        json.dump(rt_results, f, indent=2)

    # Print table
    def _fmt(v):
        if v is None or (isinstance(v, float) and not np.isfinite(v)):
            return "    N/A"
        return f"{v:+.3f}"

    print(f"\n  {'Type':>15s}  {'N':>4s}  {'F1':>5s}  {'rho_SJ':>7s}  {'rho_FK':>7s}  {'rho_VC':>7s}  {'rho_LP':>7s}  {'rho_EM':>7s}  {'AUC_SJ':>7s}")
    for rtype in RELATION_TYPES:
        r = rt_results.get(rtype, {})
        if r.get("skip"):
            print(f"  {rtype:>15s}  {r['n_instances']:4d}  -- skipped")
            continue
        m = r["instance_level_metrics"]
        print(f"  {rtype:>15s}  {r['n_instances']:4d}  {r['mean_greedy_f1']:.3f}  "
              f"{_fmt(m['soft_jaccard']['rho'])}  {_fmt(m['fleiss_kappa']['rho'])}  "
              f"{_fmt(m['voting_conf']['rho'])}  {_fmt(m['mean_logprob']['rho'])}  "
              f"{_fmt(m['exact_match']['rho'])}  {_fmt(m['soft_jaccard']['auroc'])}")

    print("\n  Bootstrap 95% CI for SJ rho:")
    for rtype in RELATION_TYPES:
        r = rt_results.get(rtype, {})
        if r.get("skip"):
            continue
        b = r["instance_level_metrics"]["soft_jaccard"]["bootstrap"]
        if b and b["rho"] is not None and not np.isnan(b["rho"]):
            print(f"  {rtype:>15s}  rho={b['rho']:+.4f}  CI=[{b['ci_lo']:+.4f}, {b['ci_hi']:+.4f}]  n={b['n']}")

    # ── 2. Threshold sensitivity ──
    print("\n[2/3] Threshold sensitivity ...")
    thr_results = {"sj_thresholds": [], "vc_thresholds": []}

    for thr in np.arange(0.0, 1.01, 0.05):
        thr = round(float(thr), 2)
        for sname, svals in [("sj", all_sj), ("vc", all_vc)]:
            acc = [(s, f) for s, f in zip(svals, all_f1) if s >= thr]
            rej = [(s, f) for s, f in zip(svals, all_f1) if s < thr]
            n_acc, n_rej = len(acc), len(rej)
            f1_acc = round(float(np.mean([f for _, f in acc])), 4) if acc else None
            f1_rej = round(float(np.mean([f for _, f in rej])), 4) if rej else None
            pct = round(100 * sum(1 for _, f in acc if f > 0) / n_acc, 1) if acc else None
            thr_results[f"{sname}_thresholds"].append({
                "threshold": thr, "n_accepted": n_acc, "n_rejected": n_rej,
                "coverage": round(n_acc / len(all_f1), 4),
                "mean_f1_accepted": f1_acc, "mean_f1_rejected": f1_rej,
                "pct_correct_accepted": pct,
            })

    # Per-type threshold sensitivity
    thr_results["per_type_sj"] = {}
    for rtype in RELATION_TYPES:
        indices = [i for i, inst in enumerate(re_data)
                   if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        if len(indices) < 10:
            continue
        rows = []
        for thr in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
            acc = [all_f1[i] for i in indices if all_sj[i] >= thr]
            rej = [all_f1[i] for i in indices if all_sj[i] < thr]
            rows.append({
                "threshold": thr,
                "n_accepted": len(acc),
                "coverage": round(len(acc) / len(indices), 4),
                "mean_f1_accepted": round(float(np.mean(acc)), 4) if acc else None,
                "mean_f1_rejected": round(float(np.mean(rej)), 4) if rej else None,
            })
        thr_results["per_type_sj"][rtype] = rows

    with open(OUT_DIR / "threshold_sensitivity.json", "w") as f:
        json.dump(thr_results, f, indent=2)

    print(f"\n  {'Sig':>4s}  {'Thr':>5s}  {'N_acc':>5s}  {'Cov':>5s}  {'F1_acc':>6s}  {'F1_rej':>6s}  {'%Cor':>5s}")
    for skey in ["sj_thresholds", "vc_thresholds"]:
        sig = skey[:2].upper()
        for e in thr_results[skey]:
            if e["threshold"] not in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                continue
            f1a = f"{e['mean_f1_accepted']:.3f}" if e["mean_f1_accepted"] is not None else "  N/A"
            f1r = f"{e['mean_f1_rejected']:.3f}" if e["mean_f1_rejected"] is not None else "  N/A"
            pct = f"{e['pct_correct_accepted']:.0f}%" if e["pct_correct_accepted"] is not None else " N/A"
            print(f"  {sig:>4s}  {e['threshold']:5.2f}  {e['n_accepted']:5d}  "
                  f"{e['coverage']:.3f}  {f1a}  {f1r}  {pct}")

    # ── 3. Cross-type bootstrap comparison ──
    print("\n[3/3] Cross-type bootstrap comparison ...")
    type_rhos = {}
    for rtype in RELATION_TYPES:
        indices = [i for i, inst in enumerate(re_data)
                   if any(r["type"] == rtype for r in inst["gold"]["relations"])]
        if len(indices) < 10:
            continue
        sj = [all_sj[i] for i in indices]
        f1 = [all_f1[i] for i in indices]
        type_rhos[rtype] = bootstrap_rho_ci(sj, f1, rng=rng)

    comparisons = {}
    for i, t1 in enumerate(RELATION_TYPES):
        for t2 in RELATION_TYPES[i+1:]:
            if t1 not in type_rhos or t2 not in type_rhos:
                continue
            idx1 = [i for i, inst in enumerate(re_data)
                    if any(r["type"] == t1 for r in inst["gold"]["relations"])]
            idx2 = [i for i, inst in enumerate(re_data)
                    if any(r["type"] == t2 for r in inst["gold"]["relations"])]
            sj1, f11 = np.array([all_sj[i] for i in idx1]), np.array([all_f1[i] for i in idx1])
            sj2, f12 = np.array([all_sj[i] for i in idx2]), np.array([all_f1[i] for i in idx2])
            diffs = []
            for _ in range(N_BOOT):
                b1 = rng.integers(0, len(sj1), size=len(sj1))
                b2 = rng.integers(0, len(sj2), size=len(sj2))
                r1 = spearmanr(sj1[b1], f11[b1]).statistic
                r2 = spearmanr(sj2[b2], f12[b2]).statistic
                if np.isfinite(r1) and np.isfinite(r2):
                    diffs.append(r1 - r2)
            if diffs:
                diffs.sort()
                comparisons[f"{t1}_vs_{t2}"] = {
                    "delta_rho": round(type_rhos[t1]["rho"] - type_rhos[t2]["rho"], 4),
                    "ci_lo": round(float(np.percentile(diffs, 2.5)), 4),
                    "ci_hi": round(float(np.percentile(diffs, 97.5)), 4),
                    "significant": not (np.percentile(diffs, 2.5) <= 0 <= np.percentile(diffs, 97.5)),
                }

    cross_results = {"type_rhos": type_rhos, "pairwise_comparisons": comparisons}
    with open(OUT_DIR / "cross_type_comparison.json", "w") as f:
        json.dump(cross_results, f, indent=2)

    print(f"\n  {'Comparison':>30s}  {'D_rho':>7s}  {'CI_lo':>7s}  {'CI_hi':>7s}  {'Sig':>3s}")
    for pair, res in sorted(comparisons.items()):
        sig = "*" if res["significant"] else ""
        print(f"  {pair:>30s}  {res['delta_rho']:+.4f}  {res['ci_lo']:+.4f}  {res['ci_hi']:+.4f}  {sig}")

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
