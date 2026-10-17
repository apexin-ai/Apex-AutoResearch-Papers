# Re-evaluate NER predictions with text.find()-corrected offsets.
# Fixes model's fabricated char offsets, then computes exact/relaxed/text_match F1
# and FP breakdown (wrong_type / spurious / hallucinated).
import argparse
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(".")
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
RESULTS_DIR = PROJECT_ROOT / "results"
MAX_SAMPLES = 1000


def find_closest_occurrence(text: str, source: str, orig_start: int) -> int:
    """Find the occurrence of `text` in `source` closest to `orig_start`. Returns -1 if not found."""
    best = -1
    best_dist = float("inf")
    start = 0
    while True:
        idx = source.find(text, start)
        if idx == -1:
            break
        dist = abs(idx - orig_start)
        if dist < best_dist:
            best_dist = dist
            best = idx
        start = idx + 1
    return best


def fix_offsets(predictions: list, samples: list):
    """Fix prediction offsets using text.find(). Returns (fixed_preds, hallucination_count_per_batch)."""
    by_sample_batch = defaultdict(list)
    for p in predictions:
        by_sample_batch[(p["sample_id"], p["batch_id"])].append(p)

    total_fixed = 0
    total_hallucinated = 0
    total_already_correct = 0

    for (sid, bid), entries in by_sample_batch.items():
        if sid >= len(samples):
            continue
        source_text = samples[sid]["text"]
        for entry in entries:
            fixed_preds = []
            for pred in entry.get("predictions", []):
                pt = pred.get("text", "")
                orig_start = pred.get("start", 0)
                if not pt:
                    continue
                pos = find_closest_occurrence(pt, source_text, orig_start)
                if pos == -1:
                    pred["_hallucinated"] = True
                    total_hallucinated += 1
                    fixed_preds.append(pred)
                    continue
                new_start = pos
                new_end = pos + len(pt)
                if new_start == orig_start and new_end == pred.get("end", 0):
                    total_already_correct += 1
                else:
                    total_fixed += 1
                pred["start"] = new_start
                pred["end"] = new_end
                pred["_hallucinated"] = False
                fixed_preds.append(pred)
            entry["predictions"] = fixed_preds

    logger.info("Offset fix: %d corrected, %d already correct, %d hallucinated",
                total_fixed, total_already_correct, total_hallucinated)
    return predictions


def compute_batch_metrics(pred_entries, samples, batch_types):
    """Compute exact/relaxed/text_match P/R/F1 and FP breakdown for one batch."""
    batch_types_set = set(batch_types)

    by_sample = {}
    for p in pred_entries:
        by_sample.setdefault(p["sample_id"], []).append(p)

    counts = {mode: {"tp": 0, "pred": 0, "gold": 0} for mode in ["exact", "relaxed", "text_match"]}
    per_type = {mode: defaultdict(lambda: {"tp": 0, "pred": 0, "gold": 0}) for mode in ["exact", "relaxed", "text_match"]}
    fp_hallu = 0
    fp_wrong_type = 0
    fp_spurious = 0

    for sid, entries in by_sample.items():
        if sid >= len(samples):
            continue
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types_set]

        for mode in counts:
            counts[mode]["gold"] += len(gold_entities)
            for g in gold_entities:
                per_type[mode][g["type"]]["gold"] += 1

        preds = entries[0].get("predictions", [])
        preds = [p for p in preds if p.get("type") in batch_types_set]

        for mode in counts:
            counts[mode]["pred"] += len(preds)
            for p in preds:
                per_type[mode][p["type"]]["pred"] += 1

        # --- Exact match ---
        matched_gold_exact = set()
        for pred in preds:
            if pred.get("_hallucinated"):
                continue
            for gi, gold in enumerate(gold_entities):
                if gi not in matched_gold_exact and pred["start"] == gold["start"] and pred["end"] == gold["end"] and pred["type"] == gold["type"]:
                    counts["exact"]["tp"] += 1
                    per_type["exact"][pred["type"]]["tp"] += 1
                    matched_gold_exact.add(gi)
                    break

        # --- Relaxed match (overlap + type) ---
        matched_gold_relaxed = set()
        for pred in preds:
            if pred.get("_hallucinated"):
                continue
            for gi, gold in enumerate(gold_entities):
                if gi not in matched_gold_relaxed and pred["type"] == gold["type"] and pred["start"] < gold["end"] and pred["end"] > gold["start"]:
                    counts["relaxed"]["tp"] += 1
                    per_type["relaxed"][pred["type"]]["tp"] += 1
                    matched_gold_relaxed.add(gi)
                    break

        # --- Text match (text + type, pred text in source) ---
        gold_available = [[g["text"], g["type"], False] for g in gold_entities]
        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pt not in source_text:
                continue
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    counts["text_match"]["tp"] += 1
                    per_type["text_match"][ptype]["tp"] += 1
                    break

        # --- FP breakdown ---
        gold_texts = {(g["text"], g["type"]) for g in gold_entities}
        gold_texts_any_type = {g["text"] for g in gold_entities}
        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            if pred.get("_hallucinated") or pt not in source_text:
                fp_hallu += 1
            elif (pt, ptype) not in gold_texts:
                if pt in gold_texts_any_type:
                    fp_wrong_type += 1
                else:
                    fp_spurious += 1

    def prf(tp, npred, ngold):
        p = tp / npred if npred > 0 else 0.0
        r = tp / ngold if ngold > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        return {"precision": round(p, 6), "recall": round(r, 6), "f1": round(f, 6),
                "tp": tp, "total_pred": npred, "total_gold": ngold}

    result = {}
    for mode in ["exact", "relaxed", "text_match"]:
        c = counts[mode]
        result[mode] = prf(c["tp"], c["pred"], c["gold"])
        all_types = set(list(per_type[mode].keys()))
        result[f"{mode}_per_type"] = {}
        for t in sorted(all_types):
            d = per_type[mode][t]
            result[f"{mode}_per_type"][t] = prf(d["tp"], d["pred"], d["gold"])

    result["fp_breakdown"] = {
        "hallucinated_text": fp_hallu,
        "wrong_type": fp_wrong_type,
        "spurious_entity": fp_spurious,
        "total_fp": fp_hallu + fp_wrong_type + fp_spurious,
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="Re-evaluate NER with text.find()-corrected offsets")
    parser.add_argument("--exp", required=True, choices=["exp1", "exp2"], help="Experiment name")
    parser.add_argument("--max_samples", type=int, default=MAX_SAMPLES)
    args = parser.parse_args()

    pred_path = ARTIFACTS_DIR / f"predictions_{args.exp}.json"
    if not pred_path.exists():
        logger.error("Predictions file not found: %s", pred_path)
        sys.exit(1)

    logger.info("Loading predictions from %s", pred_path)
    with open(pred_path) as f:
        predictions = json.load(f)
    logger.info("Loaded %d prediction entries", len(predictions))

    logger.info("Loading Few-NERD test split (max_samples=%d)", args.max_samples)
    samples = load_few_nerd(split="test", max_samples=args.max_samples)
    logger.info("Loaded %d samples", len(samples))

    # Fix offsets
    predictions = fix_offsets(predictions, samples)

    # Group by batch
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

    logger.info("Evaluating %d batches...", len(batches))

    # Per-batch results
    batch_results = {}
    for bid, info in sorted(batches.items()):
        metrics = compute_batch_metrics(info["entries"], samples, info["batch_types"])
        batch_results[bid] = {
            "count_key": info["count_key"],
            "bcs": info["batch_bcs"],
            "num_types": len(info["batch_types"]),
            **metrics,
        }

    # Aggregate by count_key
    summary = {}
    for bid, br in batch_results.items():
        ck = br["count_key"]
        if ck not in summary:
            summary[ck] = {"batches": [], "count_key": ck}
        summary[ck]["batches"].append(br)

    for ck, info in summary.items():
        bs = info["batches"]
        n = len(bs)
        for mode in ["exact", "relaxed", "text_match"]:
            total_tp = sum(b[mode]["tp"] for b in bs)
            total_pred = sum(b[mode]["total_pred"] for b in bs)
            total_gold = sum(b[mode]["total_gold"] for b in bs)
            p = total_tp / total_pred if total_pred > 0 else 0.0
            r = total_tp / total_gold if total_gold > 0 else 0.0
            f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
            macro_f1 = sum(b[mode]["f1"] for b in bs) / n if n > 0 else 0.0
            info[f"micro_{mode}"] = {"precision": round(p, 6), "recall": round(r, 6), "f1": round(f, 6),
                                      "tp": total_tp, "total_pred": total_pred, "total_gold": total_gold,
                                      "macro_f1": round(macro_f1, 6)}

        # FP aggregation
        info["fp_breakdown"] = {
            "hallucinated_text": sum(b["fp_breakdown"]["hallucinated_text"] for b in bs),
            "wrong_type": sum(b["fp_breakdown"]["wrong_type"] for b in bs),
            "spurious_entity": sum(b["fp_breakdown"]["spurious_entity"] for b in bs),
            "total_fp": sum(b["fp_breakdown"]["total_fp"] for b in bs),
        }
        info["num_batches"] = n
        info["avg_pred"] = round(sum(b["text_match"]["total_pred"] for b in bs) / n, 1)
        info["avg_gold"] = round(sum(b["text_match"]["total_gold"] for b in bs) / n, 1)
        info["pred_gold_ratio"] = round(info["avg_pred"] / info["avg_gold"], 2) if info["avg_gold"] > 0 else 0.0
        del info["batches"]

    # Save results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    results_path = RESULTS_DIR / f"{args.exp}_reeval_results.json"
    with open(results_path, "w") as f:
        # Clean _hallucinated flags from batch_results before saving
        clean_results = {}
        for bid, br in batch_results.items():
            clean = {k: v for k, v in br.items() if not k.endswith("_per_type")}
            clean_results[bid] = clean
        json.dump(clean_results, f, indent=2)

    summary_path = RESULTS_DIR / f"{args.exp}_reeval_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Print summary table
    print("\n" + "=" * 110)
    print(f"Re-evaluation Summary ({args.exp}) — offsets fixed via text.find()")
    print("=" * 110)
    print(f"{'Count':>10} {'#Bat':>5} {'ExactF1':>8} {'RelaxF1':>8} {'TextF1':>8} "
          f"{'TextP':>7} {'TextR':>7} {'P/G':>5} {'Hallu':>6} {'WrTyp':>6} {'Spur':>6}")
    print("-" * 110)
    for ck in sorted(summary.keys(), key=lambda x: int(x.split("_")[1])):
        s = summary[ck]
        tm = s["micro_text_match"]
        ex = s["micro_exact"]
        rl = s["micro_relaxed"]
        fb = s["fp_breakdown"]
        print(f"{ck:>10} {s['num_batches']:>5} {ex['f1']:>8.4f} {rl['f1']:>8.4f} {tm['f1']:>8.4f} "
              f"{tm['precision']:>7.4f} {tm['recall']:>7.4f} {s['pred_gold_ratio']:>5.2f} "
              f"{fb['hallucinated_text']:>6} {fb['wrong_type']:>6} {fb['spurious_entity']:>6}")
    print("=" * 110)

    logger.info("Results saved to %s and %s", results_path, summary_path)


if __name__ == "__main__":
    main()
