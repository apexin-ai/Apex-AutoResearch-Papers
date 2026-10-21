"""Cross-temperature robustness analysis for temp_robust_qwen experiments.

Reads annotation, correctness, and local_impact data from 4 temperature conditions
(0.3, 0.5, 0.7, 1.0) and produces a unified analysis JSON.
"""

import json
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import stats

TEMPS = ["0.3", "0.5", "0.7", "1.0"]
FUNC_TYPES = ["information_provision", "reasoning_guidance", "verification", "coordination", "acknowledgment"]
BASE_DIR = Path(__file__).resolve().parent.parent / "outputs" / "temp_robust"


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def get_function_distribution(annotations: list[dict]) -> dict[str, float]:
    types = []
    for rec in annotations:
        ann = rec.get("annotation", {})
        t = ann.get("type", "unknown")
        types.append(t)
    total = len(types)
    if total == 0:
        return {ft: 0.0 for ft in FUNC_TYPES}
    counts = Counter(types)
    return {ft: counts.get(ft, 0) / total for ft in FUNC_TYPES}


def get_accuracy(correctness_data: list[dict]) -> float:
    if not correctness_data:
        return 0.0
    correct = sum(1 for r in correctness_data if r.get("correctness") == "correct")
    return correct / len(correctness_data)


def get_impact_gradient(impact_data: list[dict], annotations: list[dict]) -> dict:
    ann_map = {}
    for rec in annotations:
        key = (rec["task_id"], rec["message_index"])
        ann_map[key] = rec.get("annotation", {}).get("type", "unknown")

    action_changes_by_type = {ft: [] for ft in FUNC_TYPES}
    for rec in impact_data:
        key = (rec["task_id"], rec["message_index"])
        func_type = ann_map.get(key, "unknown")
        if func_type not in action_changes_by_type:
            continue
        remove = rec.get("remove", {})
        changed = remove.get("action_level", "surface_only") in ("reasoning_step", "final_answer")
        action_changes_by_type[func_type].append(1 if changed else 0)

    result = {}
    for ft in FUNC_TYPES:
        vals = action_changes_by_type[ft]
        if vals:
            result[ft] = {"action_change_rate": np.mean(vals), "n": len(vals)}
        else:
            result[ft] = {"action_change_rate": 0.0, "n": 0}
    return result


def compute_cohens_kappa(labels1: list[str], labels2: list[str]) -> float:
    assert len(labels1) == len(labels2)
    n = len(labels1)
    if n == 0:
        return 0.0
    agree = sum(1 for a, b in zip(labels1, labels2) if a == b)
    p_o = agree / n
    counts1 = Counter(labels1)
    counts2 = Counter(labels2)
    all_labels = set(labels1) | set(labels2)
    p_e = sum((counts1[l] / n) * (counts2[l] / n) for l in all_labels)
    if p_e >= 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def chi_squared_test(distributions: dict[str, dict[str, float]], counts: dict[str, int]) -> dict:
    observed = []
    for temp in TEMPS:
        dist = distributions[temp]
        n = counts[temp]
        row = [dist.get(ft, 0.0) * n for ft in FUNC_TYPES]
        observed.append(row)
    observed = np.array(observed)
    if observed.min() < 0 or observed.sum() == 0:
        return {"chi2": 0, "p_value": 1.0, "dof": 0, "significant": False}
    chi2, p_value, dof, _ = stats.chi2_contingency(observed)
    return {
        "chi2": round(float(chi2), 4),
        "p_value": round(float(p_value), 6),
        "dof": int(dof),
        "significant": bool(p_value < 0.05),
    }


def jensen_shannon_divergence(p: np.ndarray, q: np.ndarray) -> float:
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    p = p / p.sum() if p.sum() > 0 else p
    q = q / q.sum() if q.sum() > 0 else q
    m = 0.5 * (p + q)
    eps = 1e-12
    kl_pm = np.sum(p * np.log((p + eps) / (m + eps)))
    kl_qm = np.sum(q * np.log((q + eps) / (m + eps)))
    return float(0.5 * kl_pm + 0.5 * kl_qm)


def compute_cross_temp_kappa(all_annotations: dict[str, list[dict]], baseline_temp: str = "0.7") -> dict:
    baseline_ann = all_annotations.get(baseline_temp, [])
    if not baseline_ann:
        return {}
    baseline_map = {}
    for rec in baseline_ann:
        key = (rec["task_id"], rec["message_index"])
        baseline_map[key] = rec.get("annotation", {}).get("type", "unknown")

    results = {}
    for temp in TEMPS:
        if temp == baseline_temp:
            continue
        ann = all_annotations[temp]
        labels_base = []
        labels_temp = []
        for rec in ann:
            key = (rec["task_id"], rec["message_index"])
            if key in baseline_map:
                labels_base.append(baseline_map[key])
                labels_temp.append(rec.get("annotation", {}).get("type", "unknown"))
        if labels_base:
            kappa = compute_cohens_kappa(labels_base, labels_temp)
            results[temp] = {"kappa": round(kappa, 4), "n": len(labels_base), "agreement": round(sum(1 for a, b in zip(labels_base, labels_temp) if a == b) / len(labels_base), 4)}
        else:
            results[temp] = {"kappa": 0.0, "n": 0, "agreement": 0.0}
    return results


def main():
    all_annotations = {}
    all_correctness = {}
    all_impact = {}
    per_temperature = {}

    for temp in TEMPS:
        temp_dir = BASE_DIR / f"qwen_rr_temp{temp}"
        ann_file = temp_dir / "annotations" / "annotations.jsonl"
        corr_file = temp_dir / "correctness" / "correctness.jsonl"
        impact_file = temp_dir / "local_impact" / "impact.jsonl"
        traces_file = temp_dir / "traces" / "traces.jsonl"

        annotations = load_jsonl(ann_file) if ann_file.exists() else []
        correctness = load_jsonl(corr_file) if corr_file.exists() else []
        impact = load_jsonl(impact_file) if impact_file.exists() else []
        traces = load_jsonl(traces_file) if traces_file.exists() else []

        all_annotations[temp] = annotations
        all_correctness[temp] = correctness
        all_impact[temp] = impact

        func_dist = get_function_distribution(annotations)
        accuracy = get_accuracy(correctness)
        impact_gradient = get_impact_gradient(impact, annotations)

        # Extract cross-model kappa if available in annotation dir
        cross_model_file = temp_dir / "annotations" / "annotations_cross_model.json"
        cross_kappa = None
        if cross_model_file.exists():
            with open(cross_model_file) as f:
                cm = json.load(f)
            cross_kappa = cm.get("cohens_kappa")

        per_temperature[temp] = {
            "n_traces": len(traces),
            "n_annotations": len(annotations),
            "n_correctness": len(correctness),
            "n_impact": len(impact),
            "accuracy": round(accuracy, 4),
            "function_distribution": {k: round(v, 4) for k, v in func_dist.items()},
            "impact_gradient": {k: {"action_change_rate": round(v["action_change_rate"], 4), "n": v["n"]} for k, v in impact_gradient.items()},
            "cross_model_kappa": cross_kappa,
        }

    # Distribution tests
    distributions = {t: per_temperature[t]["function_distribution"] for t in TEMPS}
    ann_counts = {t: per_temperature[t]["n_annotations"] for t in TEMPS}
    chi2_result = chi_squared_test(distributions, ann_counts)

    js_results = {}
    for t1, t2 in combinations(TEMPS, 2):
        p = np.array([distributions[t1].get(ft, 0) for ft in FUNC_TYPES])
        q = np.array([distributions[t2].get(ft, 0) for ft in FUNC_TYPES])
        jsd = jensen_shannon_divergence(p, q)
        js_results[f"{t1}_vs_{t2}"] = round(jsd, 6)

    # Cross-temperature kappa
    cross_temp_kappa = compute_cross_temp_kappa(all_annotations, baseline_temp="0.7")

    # Impact gradient stability
    gradient_ranks = {}
    for temp in TEMPS:
        ig = per_temperature[temp]["impact_gradient"]
        sorted_types = sorted(FUNC_TYPES, key=lambda ft: ig[ft]["action_change_rate"], reverse=True)
        gradient_ranks[temp] = sorted_types

    gradient_spreads = {}
    for temp in TEMPS:
        ig = per_temperature[temp]["impact_gradient"]
        rates = [ig[ft]["action_change_rate"] for ft in FUNC_TYPES]
        gradient_spreads[temp] = round(max(rates) - min(rates), 4) if rates else 0.0

    rank_consistency = {}
    for t1, t2 in combinations(TEMPS, 2):
        r1 = gradient_ranks[t1]
        r2 = gradient_ranks[t2]
        rank1 = {ft: i for i, ft in enumerate(r1)}
        rank2 = {ft: i for i, ft in enumerate(r2)}
        tau, p_val = stats.kendalltau([rank1[ft] for ft in FUNC_TYPES], [rank2[ft] for ft in FUNC_TYPES])
        rank_consistency[f"{t1}_vs_{t2}"] = {"kendall_tau": round(float(tau), 4), "p_value": round(float(p_val), 4)}

    # Conclusions
    dist_robust = not chi2_result["significant"]
    max_jsd = max(js_results.values()) if js_results else 0
    jsd_robust = max_jsd < 0.05

    kappa_values = [v["kappa"] for v in cross_temp_kappa.values() if v["n"] > 0]
    kappa_robust = all(k > 0.6 for k in kappa_values) if kappa_values else False
    mean_kappa = round(np.mean(kappa_values), 4) if kappa_values else 0.0

    tau_values = [v["kendall_tau"] for v in rank_consistency.values()]
    gradient_robust = all(t > 0.6 for t in tau_values) if tau_values else False

    temperature_robust = dist_robust and jsd_robust and kappa_robust and gradient_robust

    details_parts = []
    details_parts.append(f"Chi-squared p={chi2_result['p_value']:.4f} ({'not ' if dist_robust else ''}significant)")
    details_parts.append(f"Max JSD={max_jsd:.4f} ({'<' if jsd_robust else '>='} 0.05 threshold)")
    details_parts.append(f"Mean cross-temp κ={mean_kappa} ({'>' if kappa_robust else '<='} 0.6 threshold)")
    details_parts.append(f"Impact gradient ranks {'consistent' if gradient_robust else 'inconsistent'} (Kendall τ)")

    output = {
        "per_temperature": per_temperature,
        "distribution_tests": {
            "chi_squared": chi2_result,
            "jensen_shannon": js_results,
        },
        "cross_temp_kappa": cross_temp_kappa,
        "impact_gradient_stability": {
            "ranks": {t: gradient_ranks[t] for t in TEMPS},
            "spreads": gradient_spreads,
            "rank_consistency": rank_consistency,
        },
        "conclusions": {
            "temperature_robust": temperature_robust,
            "distribution_robust": dist_robust,
            "jsd_robust": jsd_robust,
            "kappa_robust": kappa_robust,
            "gradient_robust": gradient_robust,
            "details": "; ".join(details_parts),
        },
    }

    output_path = BASE_DIR.parent / "temp_robustness_analysis.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Written to {output_path}")
    print(json.dumps(output["conclusions"], indent=2))


if __name__ == "__main__":
    main()
