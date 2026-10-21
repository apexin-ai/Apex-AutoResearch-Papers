"""V7 data analysis: self vs cross κ, answer-change rate, ack purity.

Reads annotation/impact data from outputs/ directory tree.
Expects the standard output structure from full-scale experiments.
"""

import argparse
import csv
import json
import logging
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


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


# --- 1. Self vs Cross κ ---

def analyze_self_cross_kappa(base_dir: str) -> dict:
    """Compute self-consistency (test-retest) and cross-model κ from annotation outputs."""
    results = {}

    for combo_dir in sorted(Path(base_dir).glob("*")):
        if not combo_dir.is_dir():
            continue
        ann_dir = combo_dir / "annotations"
        if not ann_dir.exists():
            continue

        combo = combo_dir.name

        # Self-consistency: annotations.jsonl pass1 vs retest
        retest_file = ann_dir / "annotations_retest.json"
        if retest_file.exists():
            with open(retest_file) as f:
                retest = json.load(f)
            results.setdefault(combo, {})["self_kappa"] = retest.get("cohens_kappa")
            results[combo]["self_n"] = retest.get("n")

        # Cross-model: annotations_cross_model.json
        cross_file = ann_dir / "annotations_cross_model.json"
        if cross_file.exists():
            with open(cross_file) as f:
                cross = json.load(f)
            results.setdefault(combo, {})["cross_kappa"] = cross.get("cohens_kappa")
            results[combo]["cross_agreement"] = cross.get("percent_agreement")
            results[combo]["cross_n"] = cross.get("n")

    return results


# --- 2. Answer-change rate ---

def analyze_answer_change(base_dir: str) -> dict:
    """Compute answer-change rate from local impact data."""
    results = {}

    for combo_dir in sorted(Path(base_dir).glob("*")):
        if not combo_dir.is_dir():
            continue
        impact_dir = combo_dir / "local_impact"
        if not impact_dir.exists():
            continue

        combo = combo_dir.name
        impact_file = impact_dir / "impact.jsonl"
        if not impact_file.exists():
            continue

        with open(impact_file) as f:
            records = [json.loads(line) for line in f if line.strip()]

        total = 0
        answer_changed = 0
        by_function = defaultdict(lambda: {"total": 0, "changed": 0})

        for rec in records:
            total += 1
            neutralize = rec.get("neutralize", rec.get("fullgen", {}))
            action = neutralize.get("action_changed", neutralize.get("action_level", "surface_only"))
            changed = action not in (False, "surface_only", "no_change")
            if changed:
                answer_changed += 1

            fn_type = rec.get("ann_type", rec.get("function_type", "unknown"))
            by_function[fn_type]["total"] += 1
            if changed:
                by_function[fn_type]["changed"] += 1

        rate = answer_changed / total if total > 0 else 0
        fn_rates = {}
        for fn, counts in by_function.items():
            fn_rates[fn] = {
                "total": counts["total"],
                "changed": counts["changed"],
                "rate": round(counts["changed"] / counts["total"], 4) if counts["total"] > 0 else 0,
            }

        results[combo] = {
            "total_messages": total,
            "answer_changed": answer_changed,
            "change_rate": round(rate, 4),
            "by_function": fn_rates,
        }

    return results


# --- 3. Ack purity ---

ACK_CONTAMINATION_PATTERNS = [
    (r"(?:let me|let us|let's)\s+(?:break|solve|calculate|compute|find|work|approach)", "reasoning_guidance"),
    (r"(?:step \d|first,?\s+(?:we|I)|second|third|finally)", "reasoning_guidance"),
    (r"(?:the answer is|= \d|equals \d|total (?:is|=)|result (?:is|=))", "information_provision"),
    (r"\d+\s*[×÷+\-*/]\s*\d+\s*=\s*\d+", "information_provision"),
    (r"(?:error|mistake|wrong|incorrect|should be|actually)", "verification"),
    (r"(?:please|could you|can you|would you)\s+(?:verify|check|review|clarify)", "coordination"),
]


def analyze_ack_purity(csv_path: str) -> dict:
    """Analyze messages labeled as acknowledgment for contamination with other functions."""
    rows = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    has_human = "human_label" in rows[0] and any(r.get("human_label", "").strip() for r in rows)
    label_col = "human_label" if has_human else "llm_label"
    logger.info("Ack purity using label column: %s (human_labels_available=%s)", label_col, has_human)
    ack_msgs = [r for r in rows if r.get(label_col, "").strip() == "acknowledgment"]

    contaminated = []
    pure = []

    for msg in ack_msgs:
        text = msg["message_text"].lower()
        text_len = len(msg["message_text"].split())
        found_patterns = []

        for pattern, fn_type in ACK_CONTAMINATION_PATTERNS:
            if re.search(pattern, text):
                found_patterns.append(fn_type)

        is_long = text_len > 50

        if found_patterns or is_long:
            contaminated.append({
                "msg_id": msg["msg_id"],
                "backbone": msg["backbone"],
                "word_count": text_len,
                "detected_functions": list(set(found_patterns)),
                "is_long": is_long,
                "preview": msg["message_text"][:200],
            })
        else:
            pure.append(msg["msg_id"])

    contamination_types = Counter()
    for c in contaminated:
        for fn in c["detected_functions"]:
            contamination_types[fn] += 1

    total_ack = len(ack_msgs)
    n_contaminated = len(contaminated)
    purity = (total_ack - n_contaminated) / total_ack if total_ack > 0 else 1.0

    per_backbone = {}
    for bb in sorted(set(r["backbone"] for r in rows)):
        bb_ack = [r for r in ack_msgs if r["backbone"] == bb]
        bb_cont = [c for c in contaminated if c["backbone"] == bb]
        bb_total = len(bb_ack)
        bb_purity = (bb_total - len(bb_cont)) / bb_total if bb_total > 0 else 1.0
        per_backbone[bb] = {
            "total_ack": bb_total,
            "contaminated": len(bb_cont),
            "purity": round(bb_purity, 4),
        }

    return {
        "label_source": label_col,
        "total_ack": total_ack,
        "pure": len(pure),
        "contaminated": n_contaminated,
        "purity_rate": round(purity, 4),
        "contamination_types": dict(contamination_types),
        "per_backbone": per_backbone,
        "contaminated_details": contaminated,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default="outputs",
                        help="Base output directory with per-combo subdirs")
    parser.add_argument("--annotation-csv", default="data/human_annotation/annotation_sheet_full.csv",
                        help="Annotation CSV for ack purity analysis")
    parser.add_argument("--output", default="outputs/v7_analysis")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    all_results = {}

    # 1. Self vs cross κ
    logger.info("=== Self vs Cross κ ===")
    kappa_results = analyze_self_cross_kappa(args.base_dir)
    if kappa_results:
        all_results["self_cross_kappa"] = kappa_results
        for combo, stats in kappa_results.items():
            logger.info("  %s: self_κ=%s cross_κ=%s",
                        combo, stats.get("self_kappa", "N/A"), stats.get("cross_kappa", "N/A"))
    else:
        logger.warning("  No self/cross κ data found in %s", args.base_dir)

    # 2. Answer-change rate
    logger.info("=== Answer-Change Rate ===")
    change_results = analyze_answer_change(args.base_dir)
    if change_results:
        all_results["answer_change"] = change_results
        for combo, stats in change_results.items():
            logger.info("  %s: %d/%d changed (%.1f%%)",
                        combo, stats["answer_changed"], stats["total_messages"],
                        stats["change_rate"] * 100)
    else:
        logger.warning("  No impact data found in %s", args.base_dir)

    # 3. Ack purity
    logger.info("=== Ack Purity ===")
    if os.path.exists(args.annotation_csv):
        ack_results = analyze_ack_purity(args.annotation_csv)
        all_results["ack_purity"] = ack_results
        logger.info("  Total ack: %d, pure: %d, contaminated: %d, purity: %.1f%%",
                    ack_results["total_ack"], ack_results["pure"],
                    ack_results["contaminated"], ack_results["purity_rate"] * 100)
        for bb, s in ack_results["per_backbone"].items():
            logger.info("    %s: %d ack, purity %.1f%%", bb, s["total_ack"], s["purity"] * 100)
    else:
        logger.warning("  Annotation CSV not found: %s", args.annotation_csv)

    # Save all results
    output_path = os.path.join(args.output, "v7_analysis.json")
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    logger.info("All results saved to %s", output_path)


if __name__ == "__main__":
    main()
