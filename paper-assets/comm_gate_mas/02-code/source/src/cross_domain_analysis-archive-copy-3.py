"""Cross-domain analysis: compare function distributions across domains and backbones.

Computes:
- Function type distributions per domain × backbone cell
- Chi-squared test for domain × function_type association
- Jensen-Shannon divergence between domain pairs
- Kruskal-Wallis / one-way ANOVA across domains
- Cross-model κ for cells with dual annotations
"""

import argparse
import json
import logging
import os
from collections import Counter
from itertools import combinations

import numpy as np
from scipy.spatial.distance import jensenshannon
from scipy.stats import chi2_contingency, kruskal

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

FUNCTION_TYPES = [
    "reasoning_guidance",
    "verification",
    "information_provision",
    "acknowledgment",
    "error_correction",
    "coordination",
]

DOMAINS = {
    "gsm8k": "full_scale",
    "arc": "arc",
    "stratqa": "stratqa",
}

BACKBONES = ["qwen", "llama", "gemma"]


def load_jsonl(path: str) -> list[dict]:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def extract_function_type(record: dict) -> str:
    if "annotation_a" in record:
        return record["annotation_a"].get("type", "unknown")
    if "annotation" in record:
        return record["annotation"].get("type", "unknown")
    return record.get("ann_type", "unknown")


def load_cell(base_dir: str, domain_dir: str, backbone: str) -> list[str]:
    ann_path = os.path.join(base_dir, domain_dir, f"{backbone}_round_robin", "annotations", "annotations.jsonl")
    if not os.path.exists(ann_path):
        logger.warning("Missing: %s", ann_path)
        return []
    records = load_jsonl(ann_path)
    return [extract_function_type(r) for r in records]


def compute_distribution(types: list[str]) -> dict[str, float]:
    c = Counter(types)
    total = sum(c.values())
    if total == 0:
        return {t: 0.0 for t in FUNCTION_TYPES}
    return {t: c.get(t, 0) / total for t in FUNCTION_TYPES}


def compute_jsd(dist1: dict[str, float], dist2: dict[str, float]) -> float:
    keys = sorted(set(dist1) | set(dist2))
    p = np.array([dist1.get(k, 0.0) for k in keys])
    q = np.array([dist2.get(k, 0.0) for k in keys])
    p = p / p.sum() if p.sum() > 0 else p
    q = q / q.sum() if q.sum() > 0 else q
    return float(jensenshannon(p, q) ** 2)


def compute_cross_model_kappa(ann_path: str) -> dict:
    if not os.path.exists(ann_path):
        return {"error": "file not found"}
    records = load_jsonl(ann_path)
    if not records:
        return {"error": "empty file"}

    has_dual = "annotation_a" in records[0] and "annotation_b" in records[0]
    if not has_dual:
        return {"error": "no dual annotations"}

    labels_a = [r.get("annotation_a", {}).get("type", "unknown") for r in records]
    labels_b = [r.get("annotation_b", {}).get("type", "unknown") for r in records]

    n = len(labels_a)
    agree = sum(1 for a, b in zip(labels_a, labels_b) if a == b)
    p_o = agree / n if n > 0 else 0
    c1, c2 = Counter(labels_a), Counter(labels_b)
    all_labels = sorted(set(labels_a) | set(labels_b))
    p_e = sum((c1[l] / n) * (c2[l] / n) for l in all_labels) if n > 0 else 0
    kappa = (p_o - p_e) / (1 - p_e) if p_e < 1.0 else 1.0

    return {
        "kappa": round(kappa, 4),
        "percent_agreement": round(p_o, 4),
        "n": n,
    }


def main():
    parser = argparse.ArgumentParser(description="Cross-domain function distribution analysis")
    parser.add_argument("--base-dir", default="outputs", help="Base output directory")
    parser.add_argument("--output", default="outputs/cross_domain_analysis.json")
    args = parser.parse_args()

    all_types_by_domain = {}
    all_types_by_backbone = {}
    cell_data = {}

    logger.info("Loading data from %s", args.base_dir)
    for domain_name, domain_dir in DOMAINS.items():
        all_types_by_domain[domain_name] = []
        for bb in BACKBONES:
            types = load_cell(args.base_dir, domain_dir, bb)
            cell_key = f"{domain_name}/{bb}"
            cell_data[cell_key] = types
            all_types_by_domain[domain_name].extend(types)
            all_types_by_backbone.setdefault(bb, []).extend(types)
            logger.info("  %s: %d messages", cell_key, len(types))

    # --- 1. Distribution table ---
    logger.info("\n=== Function Distribution (3 domain × 3 backbone) ===")
    distributions = {}
    for cell_key, types in cell_data.items():
        dist = compute_distribution(types)
        distributions[cell_key] = dist
        counts = Counter(types)
        logger.info("  %s (n=%d): %s", cell_key, len(types),
                     {t: f"{dist[t]:.1%}" for t in FUNCTION_TYPES if dist[t] > 0})

    domain_distributions = {}
    for domain_name, types in all_types_by_domain.items():
        dist = compute_distribution(types)
        domain_distributions[domain_name] = dist
        logger.info("  %s pooled (n=%d): %s", domain_name, len(types),
                     {t: f"{dist[t]:.1%}" for t in FUNCTION_TYPES if dist[t] > 0})

    backbone_distributions = {}
    for bb, types in all_types_by_backbone.items():
        dist = compute_distribution(types)
        backbone_distributions[bb] = dist

    # --- 2. Chi-squared: domain × function_type ---
    logger.info("\n=== Chi-Squared: Domain × Function Type ===")
    domain_names_ordered = list(DOMAINS.keys())
    all_counts = Counter()
    for types in all_types_by_domain.values():
        all_counts.update(types)
    active_types = [t for t in FUNCTION_TYPES if all_counts.get(t, 0) > 0]

    contingency = []
    for domain_name in domain_names_ordered:
        c = Counter(all_types_by_domain[domain_name])
        contingency.append([c.get(t, 0) for t in active_types])
    contingency = np.array(contingency)

    chi2, p_chi2, dof, expected = chi2_contingency(contingency)
    n_total = contingency.sum()
    min_dim = min(contingency.shape) - 1
    cramers_v = float(np.sqrt(chi2 / (n_total * min_dim))) if min_dim > 0 and n_total > 0 else 0.0

    chi2_result = {
        "chi2": round(float(chi2), 4),
        "p_value": float(p_chi2),
        "dof": int(dof),
        "cramers_v": round(cramers_v, 4),
        "contingency_table": {
            domain_names_ordered[i]: {active_types[j]: int(contingency[i][j]) for j in range(len(active_types))}
            for i in range(len(domain_names_ordered))
        },
    }
    logger.info("  χ²=%.2f, p=%.2e, dof=%d, Cramér's V=%.4f", chi2, p_chi2, dof, cramers_v)

    # --- 3. Chi-squared: backbone × function_type ---
    logger.info("\n=== Chi-Squared: Backbone × Function Type ===")
    bb_contingency = []
    for bb in BACKBONES:
        c = Counter(all_types_by_backbone[bb])
        bb_contingency.append([c.get(t, 0) for t in active_types])
    bb_contingency = np.array(bb_contingency)

    bb_chi2, bb_p, bb_dof, _ = chi2_contingency(bb_contingency)
    bb_n = bb_contingency.sum()
    bb_min_dim = min(bb_contingency.shape) - 1
    bb_cramers_v = float(np.sqrt(bb_chi2 / (bb_n * bb_min_dim))) if bb_min_dim > 0 and bb_n > 0 else 0.0

    bb_chi2_result = {
        "chi2": round(float(bb_chi2), 4),
        "p_value": float(bb_p),
        "dof": int(bb_dof),
        "cramers_v": round(bb_cramers_v, 4),
    }
    logger.info("  χ²=%.2f, p=%.2e, dof=%d, Cramér's V=%.4f", bb_chi2, bb_p, bb_dof, bb_cramers_v)

    # --- 4. JSD between domain pairs ---
    logger.info("\n=== Jensen-Shannon Divergence (Domain Pairs) ===")
    jsd_results = {}
    for d1, d2 in combinations(domain_names_ordered, 2):
        jsd_val = compute_jsd(domain_distributions[d1], domain_distributions[d2])
        pair_key = f"{d1}_vs_{d2}"
        jsd_results[pair_key] = round(jsd_val, 6)
        logger.info("  %s: JSD=%.6f", pair_key, jsd_val)

    # JSD between backbone pairs (pooled across domains)
    logger.info("\n=== Jensen-Shannon Divergence (Backbone Pairs) ===")
    bb_jsd_results = {}
    for b1, b2 in combinations(BACKBONES, 2):
        jsd_val = compute_jsd(backbone_distributions[b1], backbone_distributions[b2])
        pair_key = f"{b1}_vs_{b2}"
        bb_jsd_results[pair_key] = round(jsd_val, 6)
        logger.info("  %s: JSD=%.6f", pair_key, jsd_val)

    # --- 5. Per-backbone JSD within each domain pair ---
    logger.info("\n=== JSD Per Backbone (Domain Pairs) ===")
    per_bb_jsd = {}
    for bb in BACKBONES:
        per_bb_jsd[bb] = {}
        for d1, d2 in combinations(domain_names_ordered, 2):
            k1 = f"{d1}/{bb}"
            k2 = f"{d2}/{bb}"
            if k1 in distributions and k2 in distributions:
                jsd_val = compute_jsd(distributions[k1], distributions[k2])
                pair_key = f"{d1}_vs_{d2}"
                per_bb_jsd[bb][pair_key] = round(jsd_val, 6)
                logger.info("  %s %s: JSD=%.6f", bb, pair_key, jsd_val)

    # --- 6. Kruskal-Wallis: does function distribution differ across domains? ---
    logger.info("\n=== Kruskal-Wallis: Function Distribution Across Domains ===")
    type_to_int = {t: i for i, t in enumerate(FUNCTION_TYPES)}
    domain_encoded = {}
    for domain_name, types in all_types_by_domain.items():
        domain_encoded[domain_name] = [type_to_int.get(t, -1) for t in types]

    groups = [domain_encoded[d] for d in domain_names_ordered if domain_encoded[d]]
    if len(groups) >= 2:
        h_stat, p_kw = kruskal(*groups)
        kw_result = {"H": round(float(h_stat), 4), "p_value": float(p_kw)}
        logger.info("  H=%.2f, p=%.2e", h_stat, p_kw)
    else:
        kw_result = {"error": "not enough groups"}

    # --- 7. Cross-model κ per cell ---
    logger.info("\n=== Cross-Model κ ===")
    cross_kappa_results = {}
    for domain_name, domain_dir in DOMAINS.items():
        for bb in BACKBONES:
            ann_path = os.path.join(args.base_dir, domain_dir, f"{bb}_round_robin", "annotations", "annotations.jsonl")
            cell_key = f"{domain_name}/{bb}"
            kappa_info = compute_cross_model_kappa(ann_path)
            cross_kappa_results[cell_key] = kappa_info
            if "error" not in kappa_info:
                logger.info("  %s: κ=%.4f, agreement=%.1f%%, n=%d",
                             cell_key, kappa_info["kappa"],
                             kappa_info["percent_agreement"] * 100, kappa_info["n"])
            else:
                logger.info("  %s: %s", cell_key, kappa_info["error"])

    # Also check pre-computed cross_model.json files
    logger.info("\n=== Pre-computed Cross-Model Files ===")
    precomputed_kappa = {}
    for domain_name, domain_dir in DOMAINS.items():
        for bb in BACKBONES:
            cross_file = os.path.join(args.base_dir, domain_dir, f"{bb}_round_robin", "annotations", "annotations_cross_model.json")
            cell_key = f"{domain_name}/{bb}"
            if os.path.exists(cross_file):
                with open(cross_file) as f:
                    data = json.load(f)
                precomputed_kappa[cell_key] = {
                    "kappa": data.get("cohens_kappa"),
                    "percent_agreement": data.get("percent_agreement"),
                    "n": data.get("n"),
                }
                logger.info("  %s: κ=%.4f", cell_key, data.get("cohens_kappa", 0))
            else:
                logger.info("  %s: no pre-computed file", cell_key)

    # --- Summary ---
    summary = {
        "cell_distributions": {k: {t: round(v, 4) for t, v in d.items()} for k, d in distributions.items()},
        "domain_distributions": {k: {t: round(v, 4) for t, v in d.items()} for k, d in domain_distributions.items()},
        "backbone_distributions": {k: {t: round(v, 4) for t, v in d.items()} for k, d in backbone_distributions.items()},
        "cell_counts": {k: len(v) for k, v in cell_data.items()},
        "chi2_domain_x_function": chi2_result,
        "chi2_backbone_x_function": bb_chi2_result,
        "jsd_domain_pairs": jsd_results,
        "jsd_backbone_pairs": bb_jsd_results,
        "jsd_per_backbone_domain_pairs": per_bb_jsd,
        "kruskal_wallis_domain": kw_result,
        "cross_model_kappa_from_dual_annotations": cross_kappa_results,
        "cross_model_kappa_precomputed": precomputed_kappa,
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    logger.info("\nResults saved to %s", args.output)


if __name__ == "__main__":
    main()
