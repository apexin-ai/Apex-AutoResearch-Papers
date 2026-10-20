"""NVE Threshold Sensitivity Analysis v2 — Reviewer-corrected groups."""
import json
import os
import random
from collections import defaultdict

BASE = "/root/autodl-tmp/event-gated-adaptive-horizon"
LOGDIR = os.path.join(BASE, "logdir")
OUT_PATH = os.path.join(BASE, "artifacts", "nve_threshold_v2.json")

EXPERIMENTS = {
    "exp_001_baseline":                     "baseline_s1",
    "exp_008a_no_subsample_dt2":            "exp_008a_fixed_dt2_no_subsample",
    "exp_008e_v3_walker_s1":                "exp_008e_v3_walker_s1",
    "exp_008f_no_dt_embed_subsample_on_h8": "exp_008f_no_dt_embed_subsample_on_h8",
    "exp_006_fixed_dt2":                    "fixed_dt2_v1_s1",
    "exp_008d_subsample_on_h8":             "exp_008d_subsample_on_h8",
    "exp_007_fixed_dt4":                    "fixed_dt4_v1_s1",
    "exp_008c_no_subsample_dt2_h8":         "exp_008c_fixed_dt2_no_subsample_h8",
    "exp_008e_v3_walker_s2":                "exp_008e_v3_walker_s2",
}

HEALTHY = [
    "exp_001_baseline",
    "exp_008a_no_subsample_dt2",
    "exp_008e_v3_walker_s1",
    "exp_008f_no_dt_embed_subsample_on_h8",
]

COLLAPSED_A = [
    "exp_006_fixed_dt2",
    "exp_008d_subsample_on_h8",
]

COLLAPSED_B_EXTRA = [
    "exp_007_fixed_dt4",
    "exp_008c_no_subsample_dt2_h8",
    "exp_008e_v3_walker_s2",
]


def load_metrics(exp_id):
    dirn = EXPERIMENTS[exp_id]
    path = os.path.join(LOGDIR, dirn, "metrics.jsonl")
    eval_returns = {}
    value_means = {}
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            step = int(row["step"])
            if "eval_return" in row:
                eval_returns[step] = row["eval_return"]
            if "value_mean" in row:
                value_means[step] = row["value_mean"]
    return eval_returns, value_means


def compute_ve_ratio(eval_returns, value_means):
    common = sorted(set(eval_returns) & set(value_means))
    ratios = {}
    for s in common:
        er = eval_returns[s]
        vm = value_means[s]
        if abs(er) > 1e-8:
            ratios[s] = vm / er
    return ratios


def compute_nve(exp_ratios, baseline_ratios):
    common = sorted(set(exp_ratios) & set(baseline_ratios))
    nve = {}
    for s in common:
        br = baseline_ratios[s]
        if abs(br) > 1e-8:
            nve[s] = exp_ratios[s] / br
    return nve


def max_nve(nve_dict):
    if not nve_dict:
        return float("nan")
    return max(nve_dict.values())


def classify(scores, labels, threshold):
    tp = tn = fp = fn = 0
    for sc, lab in zip(scores, labels):
        pred = 1 if sc > threshold else 0
        if pred == 1 and lab == 1:
            tp += 1
        elif pred == 0 and lab == 0:
            tn += 1
        elif pred == 1 and lab == 0:
            fp += 1
        else:
            fn += 1
    acc = (tp + tn) / max(len(scores), 1)
    prec = tp / max(tp + fp, 1) if (tp + fp) > 0 else 0.0
    rec = tp / max(tp + fn, 1) if (tp + fn) > 0 else 0.0
    f1 = 2 * prec * rec / max(prec + rec, 1e-12) if (prec + rec) > 0 else 0.0
    return dict(tp=tp, tn=tn, fp=fp, fn=fn,
                accuracy=round(acc, 4), precision=round(prec, 4),
                recall=round(rec, 4), f1=round(f1, 4))


def auroc_manual(scores, labels):
    if len(set(labels)) < 2:
        return float("nan")
    pairs = sorted(zip(scores, labels), key=lambda x: -x[0])
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    tp = 0
    fp = 0
    prev_score = None
    auc = 0.0
    tp_prev = 0
    fp_prev = 0
    for sc, lab in pairs:
        if sc != prev_score and prev_score is not None:
            auc += (fp - fp_prev) * (tp + tp_prev) / 2.0
            tp_prev = tp
            fp_prev = fp
        if lab == 1:
            tp += 1
        else:
            fp += 1
        prev_score = sc
    auc += (fp - fp_prev) * (tp + tp_prev) / 2.0
    return auc / (n_pos * n_neg)


def bootstrap_auroc(scores, labels, n_boot=1000, seed=42):
    rng = random.Random(seed)
    n = len(scores)
    aucs = []
    for _ in range(n_boot):
        idx = [rng.randint(0, n - 1) for _ in range(n)]
        s = [scores[i] for i in idx]
        l = [labels[i] for i in idx]
        if len(set(l)) < 2:
            continue
        aucs.append(auroc_manual(s, l))
    if len(aucs) < 10:
        return float("nan"), float("nan"), len(aucs)
    aucs.sort()
    lo = aucs[int(len(aucs) * 0.025)]
    hi = aucs[int(len(aucs) * 0.975)]
    return lo, hi, len(aucs)


def analyze_group(group_name, collapsed_ids, healthy_ids, all_max_nves):
    scores = []
    labels = []
    experiments = {}
    for eid in healthy_ids:
        mnv = all_max_nves[eid]
        scores.append(mnv)
        labels.append(0)
        experiments[eid] = {"max_nve": round(mnv, 6), "label": "healthy"}
    for eid in collapsed_ids:
        mnv = all_max_nves[eid]
        scores.append(mnv)
        labels.append(1)
        experiments[eid] = {"max_nve": round(mnv, 6), "label": "collapsed"}

    thresholds_out = {}
    for t in [1.3, 1.5, 1.7, 2.0]:
        thresholds_out[str(t)] = classify(scores, labels, t)

    auc = auroc_manual(scores, labels)
    lo, hi, n_valid = bootstrap_auroc(scores, labels)
    n_total = len(scores)
    ci_note = ""
    if n_total < 4:
        ci_note = f"N={n_total}, CI unreliable"

    return {
        "label": group_name,
        "n_collapsed": len(collapsed_ids),
        "n_healthy": len(healthy_ids),
        "experiments": experiments,
        "thresholds": thresholds_out,
        "auroc": round(auc, 4) if not (auc != auc) else None,
        "auroc_ci_95": [round(lo, 4) if not (lo != lo) else None,
                        round(hi, 4) if not (hi != hi) else None],
        "bootstrap_n": 1000,
        "bootstrap_valid_samples": n_valid,
        "ci_note": ci_note if ci_note else f"N={n_total}",
    }


def main():
    baseline_er, baseline_vm = load_metrics("exp_001_baseline")
    baseline_ratios = compute_ve_ratio(baseline_er, baseline_vm)

    all_max_nves = {}
    all_nve_series = {}
    for eid in EXPERIMENTS:
        er, vm = load_metrics(eid)
        ratios = compute_ve_ratio(er, vm)
        nve = compute_nve(ratios, baseline_ratios)
        all_nve_series[eid] = nve
        all_max_nves[eid] = max_nve(nve)

    print("=" * 60)
    print("NVE Threshold Sensitivity Analysis v2")
    print("=" * 60)
    print()
    print("Per-experiment Max NVE:")
    for eid in EXPERIMENTS:
        label = "HEALTHY" if eid in HEALTHY else "COLLAPSED"
        print(f"  {eid:45s}  MaxNVE={all_max_nves[eid]:.4f}  [{label}]")
    print()

    collapsed_b = COLLAPSED_A + COLLAPSED_B_EXTRA
    ga = analyze_group("CIVO-specific", COLLAPSED_A, HEALTHY, all_max_nves)
    gb = analyze_group("all-failure", collapsed_b, HEALTHY, all_max_nves)

    # Recommend threshold: pick threshold with best F1 across both groups
    best_t = None
    best_f1_sum = -1
    for t in ["1.3", "1.5", "1.7", "2.0"]:
        f1_sum = ga["thresholds"][t]["f1"] + gb["thresholds"][t]["f1"]
        if f1_sum > best_f1_sum:
            best_f1_sum = f1_sum
            best_t = float(t)

    output = {
        "group_a": ga,
        "group_b": gb,
        "recommended_threshold": best_t,
        "notes": (
            "v2: exp_007 (dt=4 actor-credit) and exp_008c (H=8 underfitting) "
            "moved from CIVO-collapsed to all-failure group per reviewer. "
            "Group A = CIVO-specific collapse only. "
            "Group B = all failure modes including non-CIVO."
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"JSON saved to {OUT_PATH}")
    print()

    for gname, g in [("Group A (CIVO-specific)", ga), ("Group B (all-failure)", gb)]:
        print(f"--- {gname} ---")
        print(f"  N_collapsed={g['n_collapsed']}, N_healthy={g['n_healthy']}")
        print(f"  AUROC={g['auroc']}  95% CI={g['auroc_ci_95']}  ({g['ci_note']})")
        print(f"  {'Threshold':>10s}  {'TP':>3s} {'TN':>3s} {'FP':>3s} {'FN':>3s}  {'Acc':>6s} {'Prec':>6s} {'Rec':>6s} {'F1':>6s}")
        for t in ["1.3", "1.5", "1.7", "2.0"]:
            m = g["thresholds"][t]
            print(f"  {t:>10s}  {m['tp']:3d} {m['tn']:3d} {m['fp']:3d} {m['fn']:3d}  "
                  f"{m['accuracy']:6.3f} {m['precision']:6.3f} {m['recall']:6.3f} {m['f1']:6.3f}")
        print()

    print(f"Recommended threshold: {best_t}")


if __name__ == "__main__":
    main()
