"""Error taxonomy analysis: classify FP predictions by BCS bin.

Supports Claim 2 (multi-channel degradation model): high BCS environments
should show higher intra-batch type_substitution rates (confusability channel).

Distinguishes intra-batch vs extra-batch type substitution:
  - intra: pred text matches gold entity whose type IS in batch_types (within-batch confusion)
  - extra: pred text matches gold entity whose type is NOT in batch_types

Input:
  - artifacts/predictions_exp1.json (random batches, BCS 0-0.97)
  - artifacts/predictions_exp2.json (controlled BCS batches, BCS 0.86-0.97)
  - data/parquet/test.parquet (1000 samples, Few-NERD)
Output:
  - artifacts/exp007/error_taxonomy_report.txt
  - artifacts/exp007/error_taxonomy_by_bcs.csv
  - artifacts/exp007/error_taxonomy_raw.json
"""

import json
import logging
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = "."
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")
MAX_SAMPLES = 1000

BCS_BINS_EXP1 = [
    ("zero", 0.0, 0.001),       # count_1 batches, BCS=0
    ("low", 0.001, 0.90),       # multi-type, low confusability
    ("medium", 0.90, 0.95),     # multi-type, medium confusability
    ("high", 0.95, 1.001),      # multi-type, high confusability
]

BCS_BINS_EXP2 = [
    ("low", 0.0, 0.90),
    ("medium", 0.90, 0.95),
    ("high", 0.95, 1.001),
]

# intra_type_sub = within-batch confusion (confusability channel signal)
# extra_type_sub = pred matches gold entity whose type is outside batch
ERROR_TYPES = [
    "intra_type_sub", "extra_type_sub",
    "boundary_error", "hallucination", "spurious",
]


def text_overlaps(a: str, b: str) -> bool:
    if not a or not b:
        return False
    al, bl = a.lower(), b.lower()
    return al == bl or al in bl or bl in al


def words_overlap(a: str, b: str) -> bool:
    a_words = {w for w in a.lower().split() if len(w) > 2}
    b_words = {w for w in b.lower().split() if len(w) > 2}
    return bool(a_words & b_words)


def classify_fp(
    pred: Dict, all_gold_entities: List[Dict],
    source_text: str, batch_types: Set[str],
) -> str:
    """Classify a false-positive prediction.

    Priority: hallucination > intra_type_sub > extra_type_sub > boundary_error > spurious
    """
    pred_text = pred.get("text", "").strip()
    pred_type = pred.get("type", "")

    # 1. Hallucination
    if not pred_text or pred_text.lower() not in source_text.lower():
        return "hallucination"

    # 2. Type substitution (check intra-batch first, then extra-batch)
    for gold in all_gold_entities:
        gold_text = gold.get("text", "").strip()
        if text_overlaps(pred_text, gold_text) and pred_type != gold["type"]:
            if gold["type"] in batch_types:
                return "intra_type_sub"  # confused with another batch type
            # don't return yet — keep looking for intra match

    for gold in all_gold_entities:
        gold_text = gold.get("text", "").strip()
        if text_overlaps(pred_text, gold_text) and pred_type != gold["type"]:
            return "extra_type_sub"  # matches gold of type outside batch

    # 3. Boundary error: same type, partial word overlap
    for gold in all_gold_entities:
        if pred_type != gold["type"]:
            continue
        gold_text = gold.get("text", "").strip()
        if words_overlap(pred_text, gold_text):
            return "boundary_error"

    # 4. Spurious
    return "spurious"


def match_predictions_to_gold(
    pred_entities: List[Dict],
    gold_entities: List[Dict],
    source_text: str,
) -> Tuple[set, set]:
    matched_pred = set()
    matched_gold = set()

    for pi, pred in enumerate(pred_entities):
        pt = pred.get("text", "").strip().lower()
        if not pt or pt not in source_text.lower():
            continue
        for gi, gold in enumerate(gold_entities):
            if gi in matched_gold:
                continue
            if pred.get("type") != gold["type"]:
                continue
            gt = gold.get("text", "").strip().lower()
            if not gt:
                continue
            if pt == gt or pt in gt or gt in pt:
                matched_pred.add(pi)
                matched_gold.add(gi)
                break

    return matched_pred, matched_gold


def analyze_predictions(predictions_path: str, samples: List[Dict],
                        bcs_bins: list, label: str) -> Dict:
    with open(predictions_path) as f:
        predictions = json.load(f)

    batches = {}
    for p in predictions:
        bid = p["batch_id"]
        if bid not in batches:
            batches[bid] = {
                "entries": [],
                "batch_types": set(p["batch_types"]),
                "batch_bcs": p.get("batch_bcs", 0.0),
                "count_key": p.get("count_key", ""),
            }
        batches[bid]["entries"].append(p)

    batch_results = {}
    for bid, info in batches.items():
        counts = {et: 0 for et in ERROR_TYPES}
        counts.update({"false_negative": 0, "true_positive": 0,
                        "total_pred": 0, "total_gold": 0})

        by_sample = defaultdict(list)
        for p in info["entries"]:
            by_sample[p["sample_id"]].append(p)

        batch_types = info["batch_types"]

        for sid, entries in by_sample.items():
            if sid >= len(samples):
                continue

            source_text = samples[sid]["text"]
            gold_filtered = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
            all_gold = samples[sid]["entities"]

            pred_entities = entries[0].get("predictions", [])
            pred_filtered = [p for p in pred_entities if p.get("type") in batch_types]

            counts["total_pred"] += len(pred_filtered)
            counts["total_gold"] += len(gold_filtered)

            matched_pred, matched_gold = match_predictions_to_gold(
                pred_filtered, gold_filtered, source_text
            )
            counts["true_positive"] += len(matched_pred)
            counts["false_negative"] += len(gold_filtered) - len(matched_gold)

            for pi, pred in enumerate(pred_filtered):
                if pi in matched_pred:
                    continue
                et = classify_fp(pred, all_gold, source_text, batch_types)
                counts[et] += 1

        batch_results[bid] = {
            "bcs": info["batch_bcs"],
            "count_key": info["count_key"],
            "num_types": len(info["batch_types"]),
            **counts,
        }

    bin_agg = {}
    bin_n = {}
    for bname, _, _ in bcs_bins:
        bin_agg[bname] = {k: 0 for k in ERROR_TYPES +
                          ["false_negative", "true_positive", "total_pred", "total_gold"]}
        bin_n[bname] = 0

    for bid, r in batch_results.items():
        bcs = r["bcs"]
        for bname, lo, hi in bcs_bins:
            if lo <= bcs < hi:
                for k in bin_agg[bname]:
                    bin_agg[bname][k] += r[k]
                bin_n[bname] += 1
                break

    return {"label": label, "batch_results": batch_results,
            "bin_agg": bin_agg, "bin_n": bin_n, "bcs_bins": bcs_bins}


def chi_square_test(bin_agg: Dict, bcs_bins: list) -> Dict:
    from scipy.stats import chi2_contingency

    active = [n for n, _, _ in bcs_bins
              if sum(bin_agg[n].get(et, 0) for et in ERROR_TYPES) > 0]
    if len(active) < 2:
        return {"error": "<2 non-empty bins"}

    table = np.array([[bin_agg[b][et] for et in ERROR_TYPES] for b in active])
    keep = table.sum(axis=0) > 0
    table = table[:, keep]
    types_kept = [et for et, k in zip(ERROR_TYPES, keep) if k]

    if table.shape[1] < 2:
        return {"error": "<2 non-zero error types"}

    chi2, p, dof, expected = chi2_contingency(table)
    return {"chi2": float(chi2), "p_value": float(p), "dof": int(dof),
            "bins": active, "types": types_kept, "table": table.tolist()}


def intra_sub_trend_test(bin_agg: Dict, bcs_bins: list) -> Dict:
    """Spearman: intra_type_sub proportion vs BCS midpoint."""
    from scipy.stats import spearmanr

    xs, ys = [], []
    for bname, lo, hi in bcs_bins:
        total_fp = sum(bin_agg[bname].get(et, 0) for et in ERROR_TYPES)
        if total_fp < 5:
            continue
        frac = bin_agg[bname]["intra_type_sub"] / total_fp
        xs.append((lo + hi) / 2)
        ys.append(frac)

    if len(xs) < 3:
        return {"error": f"only {len(xs)} usable bins"}

    rho, p = spearmanr(xs, ys)
    return {"rho": float(rho), "p_value": float(p), "bcs_mid": xs, "frac": ys}


def intra_sub_count_trend(bin_agg: Dict, bcs_bins: list) -> Dict:
    """Spearman: intra_type_sub rate per gold entity vs BCS."""
    from scipy.stats import spearmanr

    xs, ys = [], []
    for bname, lo, hi in bcs_bins:
        tgold = bin_agg[bname]["total_gold"]
        if tgold < 10:
            continue
        rate = bin_agg[bname]["intra_type_sub"] / tgold
        xs.append((lo + hi) / 2)
        ys.append(rate)

    if len(xs) < 3:
        return {"error": f"only {len(xs)} usable bins"}

    rho, p = spearmanr(xs, ys)
    return {"rho": float(rho), "p_value": float(p), "bcs_mid": xs, "rate": ys}


def format_report(results_list: List[Dict]) -> str:
    lines = []
    lines.append("=" * 90)
    lines.append("EXP-007  Error Taxonomy by BCS Bin  (intra/extra type-sub split)")
    lines.append("=" * 90)

    for res in results_list:
        ba = res["bin_agg"]
        bn = res["bin_n"]
        bins = res["bcs_bins"]

        lines.append(f"\n{'─' * 90}")
        lines.append(f"Dataset: {res['label']}  |  batches: {sum(bn.values())}")
        lines.append(f"{'─' * 90}")
        lines.append(
            f"{'Bin':<8} {'#bat':>4} {'TP':>6} {'#FP':>6} "
            f"{'IntraSub%':>9} {'ExtraSub%':>9} {'Bndry%':>6} {'Hallu%':>6} {'Spur%':>6} "
            f"{'#FN':>6} {'Prec%':>6} {'Rec%':>6}"
        )
        lines.append("-" * 90)

        for bname, _, _ in bins:
            c = ba[bname]
            tfp = sum(c[et] for et in ERROR_TYPES)
            tp = c["true_positive"]
            fn = c["false_negative"]
            tpred = c["total_pred"]
            tgold = c["total_gold"]
            prec = tp / tpred * 100 if tpred else 0
            rec = tp / tgold * 100 if tgold else 0

            def pct(et):
                return c[et] / tfp * 100 if tfp else 0

            lines.append(
                f"{bname:<8} {bn[bname]:>4} {tp:>6} {tfp:>6} "
                f"{pct('intra_type_sub'):>8.1f}% {pct('extra_type_sub'):>8.1f}% "
                f"{pct('boundary_error'):>5.1f}% {pct('hallucination'):>5.1f}% "
                f"{pct('spurious'):>5.1f}% "
                f"{fn:>6} {prec:>5.1f}% {rec:>5.1f}%"
            )

        # Absolute counts for intra_type_sub per gold
        lines.append("")
        lines.append(f"  Intra-batch type_sub per 100 gold entities:")
        for bname, _, _ in bins:
            c = ba[bname]
            tgold = c["total_gold"]
            rate = c["intra_type_sub"] / tgold * 100 if tgold else 0
            lines.append(f"    {bname}: {c['intra_type_sub']}/{tgold} = {rate:.2f}%")

        lines.append("")
        lines.append("--- Statistical Tests ---")

        chi2 = chi_square_test(ba, bins)
        if "error" in chi2:
            lines.append(f"Chi-square: {chi2['error']}")
        else:
            sig = "***" if chi2["p_value"] < 0.001 else ("**" if chi2["p_value"] < 0.01 else ("*" if chi2["p_value"] < 0.05 else "n.s."))
            lines.append(f"Chi-square: chi2={chi2['chi2']:.2f}, df={chi2['dof']}, p={chi2['p_value']:.2e} {sig}")

        trend_pct = intra_sub_trend_test(ba, bins)
        if "error" in trend_pct:
            lines.append(f"IntraSub fraction trend: {trend_pct['error']}")
        else:
            sig = "***" if trend_pct["p_value"] < 0.001 else ("**" if trend_pct["p_value"] < 0.01 else ("*" if trend_pct["p_value"] < 0.05 else "n.s."))
            lines.append(f"IntraSub fraction ~ BCS: rho={trend_pct['rho']:.3f}, p={trend_pct['p_value']:.4f} {sig}")
            lines.append(f"  bcs_mid={[f'{x:.3f}' for x in trend_pct['bcs_mid']]}")
            lines.append(f"  frac   ={[f'{y:.4f}' for y in trend_pct['frac']]}")

        trend_rate = intra_sub_count_trend(ba, bins)
        if "error" in trend_rate:
            lines.append(f"IntraSub rate/gold trend: {trend_rate['error']}")
        else:
            sig = "***" if trend_rate["p_value"] < 0.001 else ("**" if trend_rate["p_value"] < 0.01 else ("*" if trend_rate["p_value"] < 0.05 else "n.s."))
            lines.append(f"IntraSub rate/gold ~ BCS: rho={trend_rate['rho']:.3f}, p={trend_rate['p_value']:.4f} {sig}")
            lines.append(f"  bcs_mid={[f'{x:.3f}' for x in trend_rate['bcs_mid']]}")
            lines.append(f"  rate   ={[f'{y:.4f}' for y in trend_rate['rate']]}")

    return "\n".join(lines)


def write_csv(results_list: List[Dict], path: str):
    header = (
        "experiment,bcs_bin,n_batches,true_positive,total_fp,"
        "intra_type_sub,intra_sub_pct,extra_type_sub,extra_sub_pct,"
        "boundary_error,boundary_pct,hallucination,halluc_pct,"
        "spurious,spurious_pct,false_negative,total_pred,total_gold"
    )
    rows = [header]
    for res in results_list:
        ba = res["bin_agg"]
        bn = res["bin_n"]
        for bname, _, _ in res["bcs_bins"]:
            c = ba[bname]
            tfp = sum(c[et] for et in ERROR_TYPES)
            def pct(et):
                return c[et] / tfp * 100 if tfp else 0
            rows.append(
                f"{res['label']},{bname},{bn[bname]},{c['true_positive']},{tfp},"
                f"{c['intra_type_sub']},{pct('intra_type_sub'):.2f},"
                f"{c['extra_type_sub']},{pct('extra_type_sub'):.2f},"
                f"{c['boundary_error']},{pct('boundary_error'):.2f},"
                f"{c['hallucination']},{pct('hallucination'):.2f},"
                f"{c['spurious']},{pct('spurious'):.2f},"
                f"{c['false_negative']},{c['total_pred']},{c['total_gold']}"
            )
    with open(path, "w") as f:
        f.write("\n".join(rows) + "\n")


def main():
    output_dir = os.path.join(ARTIFACTS_DIR, "exp007")
    os.makedirs(output_dir, exist_ok=True)

    logger.info("Loading test data (max_samples=%d)", MAX_SAMPLES)
    samples = load_few_nerd(split="test", max_samples=MAX_SAMPLES)
    logger.info("Loaded %d samples", len(samples))

    results = []

    for fname, label, bins in [
        ("predictions_exp1.json", "exp1_random", BCS_BINS_EXP1),
        ("predictions_exp2.json", "exp2_controlled", BCS_BINS_EXP2),
    ]:
        path = os.path.join(ARTIFACTS_DIR, fname)
        if os.path.exists(path):
            logger.info("Analyzing %s", label)
            r = analyze_predictions(path, samples, bins, label)
            results.append(r)

    report = format_report(results)
    print(report)

    with open(os.path.join(output_dir, "error_taxonomy_report.txt"), "w") as f:
        f.write(report + "\n")

    write_csv(results, os.path.join(output_dir, "error_taxonomy_by_bcs.csv"))

    raw = {r["label"]: r["batch_results"] for r in results}
    with open(os.path.join(output_dir, "error_taxonomy_raw.json"), "w") as f:
        json.dump(raw, f, indent=2)

    logger.info("Done. Output in %s", output_dir)


if __name__ == "__main__":
    main()
