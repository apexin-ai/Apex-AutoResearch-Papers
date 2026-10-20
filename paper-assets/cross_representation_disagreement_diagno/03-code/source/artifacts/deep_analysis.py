# exp-001 FOLIO Deep Analysis: error distribution, GT subset metrics, asymmetry, bootstrap CI, Fisher test
# Usage: python3 src/deep_analysis.py

import json
import numpy as np
from collections import Counter, defaultdict
from scipy.stats import fisher_exact

DATA_PATH = "results/mvp_v4_repair_fixed.json"
OUT_JSON = "results/exp001_deep_analysis.json"
OUT_TXT = "results/exp001_deep_analysis.txt"
BOOT_N = 10000
SEED = 42


def load_data(path):
    with open(path) as f:
        return json.load(f)


def get_subsets(data):
    all_data = data
    excl_unknown = [s for s in data if s["ground_truth"] != "Unknown"]
    return {"all": all_data, "excl_unknown": excl_unknown}


def is_disagreement(s):
    return s["disagreement"]["agreement_type"] in ("disagree", "single_error")


def has_repair(s):
    rep = s.get("repair", {})
    return bool(rep.get("code_targeted") or rep.get("fol_targeted"))


def get_repair_success(s, method):
    """Check if any round of the given repair method succeeded."""
    rep = s.get("repair", {})
    rounds = rep.get(f"code_{method}", []) + rep.get(f"fol_{method}", [])
    if not rounds:
        return None
    return any(r["success"] for r in rounds)


def compute_c_metrics(subset):
    n = len(subset)
    if n == 0:
        return {}

    disagree_samples = [s for s in subset if is_disagreement(s)]
    n_disagree = len(disagree_samples)

    # C1: disagreement rate
    c1 = n_disagree / n

    # C2: diagnostic rate — among disagreements, fraction with identified error_side
    diagnosed = [s for s in disagree_samples
                 if s["disagreement"]["error_side"] in ("fol", "code")]
    c2 = len(diagnosed) / n_disagree if n_disagree > 0 else 0.0

    # C3: repair success rate (targeted, among samples with repair)
    repair_samples = [s for s in disagree_samples if has_repair(s)]
    targeted_successes = [s for s in repair_samples if get_repair_success(s, "targeted")]
    c3 = len(targeted_successes) / len(repair_samples) if repair_samples else 0.0

    # C4: targeted - blind delta
    paired = [s for s in repair_samples if get_repair_success(s, "blind") is not None]
    if paired:
        t_rate = sum(1 for s in paired if get_repair_success(s, "targeted")) / len(paired)
        b_rate = sum(1 for s in paired if get_repair_success(s, "blind")) / len(paired)
        c4 = t_rate - b_rate
        c4_targeted = t_rate
        c4_blind = b_rate
    else:
        c4 = c4_targeted = c4_blind = 0.0

    # C5: localization accuracy
    loc_samples = [s for s in disagree_samples
                   if s["disagreement"]["error_side"] in ("fol", "code", "both")]
    correct_loc = 0
    for s in loc_samples:
        side = s["disagreement"]["error_side"]
        dis = s["disagreement"]
        if side == "code" and dis["code_correct"] is False and dis["fol_correct"] is True:
            correct_loc += 1
        elif side == "fol" and dis["fol_correct"] is False and dis["code_correct"] is True:
            correct_loc += 1
        elif side == "both" and dis["fol_correct"] is False and dis["code_correct"] is False:
            correct_loc += 1
    c5 = correct_loc / len(loc_samples) if loc_samples else 0.0

    return {
        "n": n,
        "n_disagree": n_disagree,
        "C1_disagree_rate": round(c1, 4),
        "C2_diagnostic_rate": round(c2, 4),
        "C3_repair_success_rate": round(c3, 4),
        "C4_targeted_blind_delta": round(c4, 4),
        "C4_targeted_rate": round(c4_targeted, 4),
        "C4_blind_rate": round(c4_blind, 4),
        "C5_localization_accuracy": round(c5, 4),
        "n_repair_paired": len(paired) if paired else 0,
        "n_loc_samples": len(loc_samples),
    }


def error_type_distribution(data):
    all_types = Counter()
    excl_types = Counter()
    for s in data:
        et = s["disagreement"].get("error_type") or "none"
        all_types[et] += 1
        if s["ground_truth"] != "Unknown":
            excl_types[et] += 1

    def to_pct(counter):
        total = sum(counter.values())
        return {k: {"count": v, "pct": round(v / total * 100, 1)}
                for k, v in counter.most_common()}

    return {"all": to_pct(all_types), "excl_unknown": to_pct(excl_types)}


def gt_subset_analysis(data):
    by_gt = defaultdict(list)
    for s in data:
        by_gt[s["ground_truth"]].append(s)

    result = {}
    for gt_label in ["True", "False", "Unknown"]:
        subset = by_gt.get(gt_label, [])
        metrics = compute_c_metrics(subset)
        at_counts = Counter(s["disagreement"]["agreement_type"] for s in subset)
        metrics["agreement_type_dist"] = dict(at_counts)
        result[gt_label] = metrics
    return result


def asymmetry_analysis(data):
    disagree_samples = [s for s in data if is_disagreement(s)]
    fol_correct_code_wrong = 0
    code_correct_fol_wrong = 0
    both_wrong = 0

    for s in disagree_samples:
        dis = s["disagreement"]
        fc = dis["fol_correct"]
        cc = dis["code_correct"]
        if fc is True and cc is False:
            fol_correct_code_wrong += 1
        elif cc is True and fc is False:
            code_correct_fol_wrong += 1
        elif fc is False and cc is False:
            both_wrong += 1

    # Per-side accuracy and crash rates across ALL samples
    fol_verdicts = Counter(s["disagreement"]["fol_verdict"] for s in data)
    code_verdicts = Counter(s["disagreement"]["code_verdict"] for s in data)
    fol_correct_total = sum(1 for s in data if s["disagreement"]["fol_correct"] is True)
    code_correct_total = sum(1 for s in data if s["disagreement"]["code_correct"] is True)
    fol_crash = sum(1 for s in data if s["disagreement"]["fol_verdict"] == "Error")
    code_crash = sum(1 for s in data if s["disagreement"]["code_verdict"] == "Error")
    n = len(data)

    return {
        "fol_correct_code_wrong": fol_correct_code_wrong,
        "code_correct_fol_wrong": code_correct_fol_wrong,
        "both_wrong": both_wrong,
        "ratio": (f"{fol_correct_code_wrong}:{code_correct_fol_wrong}"
                  if code_correct_fol_wrong > 0
                  else f"{fol_correct_code_wrong}:0"),
        "fol_accuracy": round(fol_correct_total / n, 4),
        "code_accuracy": round(code_correct_total / n, 4),
        "fol_crash_rate": round(fol_crash / n, 4),
        "code_crash_rate": round(code_crash / n, 4),
        "fol_verdict_dist": dict(fol_verdicts),
        "code_verdict_dist": dict(code_verdicts),
    }


def bootstrap_ci(data, metric_fn, n_boot=BOOT_N, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(data)
    stats = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        sample = [data[i] for i in idx]
        val = metric_fn(sample)
        if val is not None:
            stats.append(val)
    stats = np.array(stats)
    if len(stats) == 0:
        return {"mean": None, "ci_lower": None, "ci_upper": None, "std": None}
    return {
        "mean": round(float(np.mean(stats)), 4),
        "ci_lower": round(float(np.percentile(stats, 2.5)), 4),
        "ci_upper": round(float(np.percentile(stats, 97.5)), 4),
        "std": round(float(np.std(stats)), 4),
    }


def metric_c1(sample):
    n = len(sample)
    if n == 0:
        return None
    return sum(1 for s in sample if is_disagreement(s)) / n


def metric_c2(sample):
    dis = [s for s in sample if is_disagreement(s)]
    if not dis:
        return None
    diagnosed = [s for s in dis if s["disagreement"]["error_side"] in ("fol", "code")]
    return len(diagnosed) / len(dis)


def metric_c4_delta(sample):
    dis = [s for s in sample if is_disagreement(s)]
    paired = [s for s in dis if has_repair(s) and get_repair_success(s, "blind") is not None]
    if not paired:
        return None
    t = sum(1 for s in paired if get_repair_success(s, "targeted")) / len(paired)
    b = sum(1 for s in paired if get_repair_success(s, "blind")) / len(paired)
    return t - b


def metric_c5(sample):
    dis = [s for s in sample if is_disagreement(s)]
    loc = [s for s in dis if s["disagreement"]["error_side"] in ("fol", "code", "both")]
    if not loc:
        return None
    correct = 0
    for s in loc:
        side = s["disagreement"]["error_side"]
        d = s["disagreement"]
        if side == "code" and d["code_correct"] is False and d["fol_correct"] is True:
            correct += 1
        elif side == "fol" and d["fol_correct"] is False and d["code_correct"] is True:
            correct += 1
        elif side == "both" and d["fol_correct"] is False and d["code_correct"] is False:
            correct += 1
    return correct / len(loc)


def run_bootstrap(data):
    subsets = get_subsets(data)
    results = {}
    for name, subset in subsets.items():
        results[name] = {
            "C1_disagree_rate": bootstrap_ci(subset, metric_c1),
            "C2_diagnostic_rate": bootstrap_ci(subset, metric_c2),
            "C4_targeted_blind_delta": bootstrap_ci(subset, metric_c4_delta),
            "C5_localization_accuracy": bootstrap_ci(subset, metric_c5),
        }
    return results


def fisher_c4(data):
    subsets = get_subsets(data)
    results = {}
    for name, subset in subsets.items():
        dis = [s for s in subset if is_disagreement(s)]
        paired = [s for s in dis if has_repair(s) and get_repair_success(s, "blind") is not None]
        if not paired:
            results[name] = {"error": "no paired samples"}
            continue

        t_correct = sum(1 for s in paired if get_repair_success(s, "targeted"))
        t_incorrect = len(paired) - t_correct
        b_correct = sum(1 for s in paired if get_repair_success(s, "blind"))
        b_incorrect = len(paired) - b_correct

        table = [[t_correct, t_incorrect], [b_correct, b_incorrect]]
        odds_ratio, p_value = fisher_exact(table)
        results[name] = {
            "table": {"targeted": {"correct": t_correct, "incorrect": t_incorrect},
                      "blind": {"correct": b_correct, "incorrect": b_incorrect}},
            "odds_ratio": round(float(odds_ratio), 4),
            "p_value": round(float(p_value), 6),
        }
    return results


def format_txt(results):
    lines = []
    lines.append("=" * 70)
    lines.append("EXP-001 FOLIO DEEP ANALYSIS")
    lines.append("=" * 70)

    lines.append("\n--- 1. ERROR TYPE DISTRIBUTION ---")
    for mode in ("all", "excl_unknown"):
        lines.append(f"\n  [{mode}]")
        for et, info in results["error_types"][mode].items():
            lines.append(f"    {et:25s}  {info['count']:3d}  ({info['pct']:5.1f}%)")

    lines.append("\n--- 2. GT SUBSET ANALYSIS ---")
    for gt in ("True", "False", "Unknown"):
        m = results["gt_subsets"][gt]
        lines.append(f"\n  GT={gt} (n={m['n']})")
        lines.append(f"    C1 disagree_rate:       {m['C1_disagree_rate']:.4f}")
        lines.append(f"    C2 diagnostic_rate:     {m['C2_diagnostic_rate']:.4f}")
        lines.append(f"    C3 repair_success:      {m['C3_repair_success_rate']:.4f}")
        lines.append(f"    C4 targeted-blind:      {m['C4_targeted_blind_delta']:+.4f}  (T={m['C4_targeted_rate']:.4f}, B={m['C4_blind_rate']:.4f})")
        lines.append(f"    C5 localization_acc:     {m['C5_localization_accuracy']:.4f}")
        lines.append(f"    agreement_types:        {m['agreement_type_dist']}")

    lines.append("\n--- 3. DISAGREEMENT ASYMMETRY ---")
    a = results["asymmetry"]
    lines.append(f"  FOL correct & Code wrong:   {a['fol_correct_code_wrong']}")
    lines.append(f"  Code correct & FOL wrong:   {a['code_correct_fol_wrong']}")
    lines.append(f"  Both wrong:                 {a['both_wrong']}")
    lines.append(f"  Ratio:                      {a['ratio']}")
    lines.append(f"  FOL accuracy:               {a['fol_accuracy']:.4f}")
    lines.append(f"  Code accuracy:              {a['code_accuracy']:.4f}")
    lines.append(f"  FOL crash rate:             {a['fol_crash_rate']:.4f}")
    lines.append(f"  Code crash rate:            {a['code_crash_rate']:.4f}")

    lines.append("\n--- 4. BOOTSTRAP 95% CI (N=10000) ---")
    for mode in ("all", "excl_unknown"):
        lines.append(f"\n  [{mode}]")
        for metric, ci in results["bootstrap"][mode].items():
            if ci["mean"] is not None:
                lines.append(f"    {metric:30s}  {ci['mean']:.4f}  [{ci['ci_lower']:.4f}, {ci['ci_upper']:.4f}]")
            else:
                lines.append(f"    {metric:30s}  N/A")

    lines.append("\n--- 5. FISHER EXACT TEST (C4) ---")
    for mode in ("all", "excl_unknown"):
        lines.append(f"\n  [{mode}]")
        f = results["fisher_c4"][mode]
        if "error" in f:
            lines.append(f"    {f['error']}")
        else:
            t = f["table"]
            lines.append(f"    Targeted: {t['targeted']['correct']} correct, {t['targeted']['incorrect']} incorrect")
            lines.append(f"    Blind:    {t['blind']['correct']} correct, {t['blind']['incorrect']} incorrect")
            lines.append(f"    Odds ratio: {f['odds_ratio']:.4f}")
            lines.append(f"    p-value:    {f['p_value']:.6f}")

    lines.append("\n--- OVERALL METRICS ---")
    for mode in ("all", "excl_unknown"):
        m = results["overall"][mode]
        lines.append(f"\n  [{mode}] (n={m['n']})")
        lines.append(f"    C1 disagree_rate:       {m['C1_disagree_rate']:.4f}")
        lines.append(f"    C2 diagnostic_rate:     {m['C2_diagnostic_rate']:.4f}")
        lines.append(f"    C3 repair_success:      {m['C3_repair_success_rate']:.4f}")
        lines.append(f"    C4 targeted-blind:      {m['C4_targeted_blind_delta']:+.4f}  (T={m['C4_targeted_rate']:.4f}, B={m['C4_blind_rate']:.4f})")
        lines.append(f"    C5 localization_acc:     {m['C5_localization_accuracy']:.4f}")

    lines.append("\n" + "=" * 70)
    return "\n".join(lines)


def main():
    data = load_data(DATA_PATH)
    print(f"Loaded {len(data)} samples")

    results = {}

    # 1. Error type distribution
    results["error_types"] = error_type_distribution(data)

    # 2. GT subset analysis
    results["gt_subsets"] = gt_subset_analysis(data)

    # 3. Asymmetry
    results["asymmetry"] = asymmetry_analysis(data)

    # Overall metrics
    subsets = get_subsets(data)
    results["overall"] = {name: compute_c_metrics(subset) for name, subset in subsets.items()}

    # 4. Bootstrap
    print("Running bootstrap (N=10000)...")
    results["bootstrap"] = run_bootstrap(data)

    # 5. Fisher exact test
    results["fisher_c4"] = fisher_c4(data)

    # Save
    with open(OUT_JSON, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"JSON saved to {OUT_JSON}")

    txt = format_txt(results)
    with open(OUT_TXT, "w") as f:
        f.write(txt)
    print(f"TXT saved to {OUT_TXT}")
    print()
    print(txt)


if __name__ == "__main__":
    main()
