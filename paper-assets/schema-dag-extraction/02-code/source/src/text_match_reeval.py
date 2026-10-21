# Text-match re-evaluation for exp1: ignores char offsets, matches by (text, type) pairs.
import json
import logging
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PREDICTIONS_PATH = "/root/schema-dag-extraction/artifacts/predictions_exp1.json"
OUTPUT_DIR = Path("/root/schema-dag-extraction/results")
MAX_SAMPLES = 1000


def text_match_eval(pred_entries, samples, batch_types):
    """Compute text-match P/R/F1 for one batch.

    Match logic: pred.text must exist in source text (substring check) AND
    match a gold entity by (text, type). Each gold can match at most once.
    """
    total_tp = 0
    total_pred = 0
    total_gold = 0
    per_type_tp = defaultdict(int)
    per_type_pred = defaultdict(int)
    per_type_gold = defaultdict(int)

    by_sample = {}
    for p in pred_entries:
        by_sample.setdefault(p["sample_id"], []).append(p)

    for sid, entries in by_sample.items():
        if sid >= len(samples):
            continue
        source_text = samples[sid]["text"]
        gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        total_gold += len(gold_entities)
        for g in gold_entities:
            per_type_gold[g["type"]] += 1

        preds = entries[0].get("predictions", [])
        preds = [p for p in preds if p.get("type") in batch_types]
        total_pred += len(preds)
        for p in preds:
            per_type_pred[p["type"]] += 1

        # Build gold index: list of (text, type, matched) for greedy matching
        gold_available = [[g["text"], g["type"], False] for g in gold_entities]

        for pred in preds:
            pt = pred.get("text", "")
            ptype = pred.get("type", "")
            # Validate: pred text must exist in source
            if pt not in source_text:
                continue
            # Greedy match to first available gold with same (text, type)
            for g in gold_available:
                if not g[2] and g[0] == pt and g[1] == ptype:
                    g[2] = True
                    total_tp += 1
                    per_type_tp[ptype] += 1
                    break

    def prf(tp, npred, ngold):
        p = tp / npred if npred > 0 else 0.0
        r = tp / ngold if ngold > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        return {"precision": p, "recall": r, "f1": f, "tp": tp, "total_pred": npred, "total_gold": ngold}

    all_types = set(list(per_type_pred.keys()) + list(per_type_gold.keys()))
    per_type = {}
    for t in sorted(all_types):
        per_type[t] = prf(per_type_tp[t], per_type_pred[t], per_type_gold[t])

    return prf(total_tp, total_pred, total_gold), per_type


def main():
    logger.info("Loading predictions...")
    with open(PREDICTIONS_PATH) as f:
        predictions = json.load(f)
    logger.info("Loaded %d prediction entries", len(predictions))

    logger.info("Loading Few-NERD test split (max_samples=%d)...", MAX_SAMPLES)
    samples = load_few_nerd(split="test", max_samples=MAX_SAMPLES)
    logger.info("Loaded %d samples", len(samples))

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
        metrics, per_type = text_match_eval(info["entries"], samples, info["batch_types"])
        batch_results[bid] = {
            "metrics": metrics,
            "per_type": per_type,
            "bcs": info["batch_bcs"],
            "count_key": info["count_key"],
            "num_types": len(info["batch_types"]),
        }

    # Per-count summary
    count_groups = defaultdict(list)
    for bid, res in batch_results.items():
        count_groups[res["count_key"]].append(res)

    summary = {}
    for ck in sorted(count_groups.keys(), key=lambda x: int(x.split("_")[1])):
        group = count_groups[ck]
        n = len(group)
        avg_f1 = sum(r["metrics"]["f1"] for r in group) / n
        avg_p = sum(r["metrics"]["precision"] for r in group) / n
        avg_r = sum(r["metrics"]["recall"] for r in group) / n
        total_pred = sum(r["metrics"]["total_pred"] for r in group)
        total_gold = sum(r["metrics"]["total_gold"] for r in group)
        total_tp = sum(r["metrics"]["tp"] for r in group)
        # Micro-averaged metrics across all batches in this count
        micro_p = total_tp / total_pred if total_pred > 0 else 0.0
        micro_r = total_tp / total_gold if total_gold > 0 else 0.0
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0.0
        summary[ck] = {
            "num_batches": n,
            "macro_precision": avg_p,
            "macro_recall": avg_r,
            "macro_f1": avg_f1,
            "micro_precision": micro_p,
            "micro_recall": micro_r,
            "micro_f1": micro_f1,
            "total_pred": total_pred,
            "total_gold": total_gold,
            "total_tp": total_tp,
            "avg_pred_per_batch": total_pred / n,
            "avg_gold_per_batch": total_gold / n,
            "pred_gold_ratio": (total_pred / total_gold) if total_gold > 0 else float("inf"),
        }

    # Over-prediction analysis
    overpred_analysis = {}
    for ck, grp in sorted(count_groups.items(), key=lambda x: int(x[0].split("_")[1])):
        # Aggregate per-type stats across batches in this count
        type_agg = defaultdict(lambda: {"tp": 0, "pred": 0, "gold": 0})
        for res in grp:
            for t, tm in res["per_type"].items():
                type_agg[t]["tp"] += tm["tp"]
                type_agg[t]["pred"] += tm["total_pred"]
                type_agg[t]["gold"] += tm["total_gold"]

        type_breakdown = {}
        for t in sorted(type_agg.keys()):
            a = type_agg[t]
            p = a["tp"] / a["pred"] if a["pred"] > 0 else 0.0
            r = a["tp"] / a["gold"] if a["gold"] > 0 else 0.0
            f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
            type_breakdown[t] = {
                "precision": round(p, 4),
                "recall": round(r, 4),
                "f1": round(f, 4),
                "pred_count": a["pred"],
                "gold_count": a["gold"],
                "tp": a["tp"],
                "pred_gold_ratio": round(a["pred"] / a["gold"], 2) if a["gold"] > 0 else None,
                "excess_preds": a["pred"] - a["gold"],
            }

        # Top over-predicted types
        sorted_by_excess = sorted(type_breakdown.items(), key=lambda x: x[1]["excess_preds"], reverse=True)
        top_overpred = [(t, d) for t, d in sorted_by_excess[:10] if d["excess_preds"] > 0]

        # FP categorization from raw predictions
        hallucination_count = 0  # pred.text not in source
        type_wrong_count = 0     # text in source & matches gold text but wrong type
        spurious_count = 0       # text in source but no gold entity with that text at all

        for bid, bres in batch_results.items():
            if bres["count_key"] != ck:
                continue
            batch_types_set = set()
            for p in batches[bid]["entries"]:
                batch_types_set = set(p["batch_types"])
                break

            by_sample = {}
            for p in batches[bid]["entries"]:
                by_sample.setdefault(p["sample_id"], []).append(p)

            for sid, entries in by_sample.items():
                if sid >= len(samples):
                    continue
                source_text = samples[sid]["text"]
                gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types_set]
                gold_texts = {(g["text"], g["type"]) for g in gold_entities}
                gold_texts_any_type = {g["text"] for g in gold_entities}

                preds = entries[0].get("predictions", [])
                preds = [p for p in preds if p.get("type") in batch_types_set]
                for pred in preds:
                    pt = pred.get("text", "")
                    ptype = pred.get("type", "")
                    if pt not in source_text:
                        hallucination_count += 1
                    elif (pt, ptype) not in gold_texts:
                        if pt in gold_texts_any_type:
                            type_wrong_count += 1
                        else:
                            spurious_count += 1

        total_fp = hallucination_count + type_wrong_count + spurious_count
        overpred_analysis[ck] = {
            "fp_breakdown": {
                "hallucinated_text": hallucination_count,
                "wrong_type": type_wrong_count,
                "spurious_entity": spurious_count,
                "total_fp_approx": total_fp,
            },
            "avg_pred": summary[ck]["avg_pred_per_batch"],
            "avg_gold": summary[ck]["avg_gold_per_batch"],
            "pred_gold_ratio": summary[ck]["pred_gold_ratio"],
            "type_breakdown": type_breakdown,
            "top_overpredicted_types": {t: d for t, d in top_overpred},
        }

    # Save results
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_DIR / "exp1_text_match_reeval.json", "w") as f:
        json.dump(batch_results, f, indent=2)

    with open(OUTPUT_DIR / "exp1_text_match_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    with open(OUTPUT_DIR / "exp1_overprediction_analysis.json", "w") as f:
        json.dump(overpred_analysis, f, indent=2)

    # Print summary table
    print("\n" + "=" * 90)
    print("Per-Count Text-Match F1 Summary (exp1)")
    print("=" * 90)
    print(f"{'Count':>8} {'Batches':>8} {'MicroP':>8} {'MicroR':>8} {'MicroF1':>8} {'MacroF1':>8} {'AvgPred':>8} {'AvgGold':>8} {'P/G':>6}")
    print("-" * 90)
    for ck in sorted(summary.keys(), key=lambda x: int(x.split("_")[1])):
        s = summary[ck]
        print(f"{ck:>8} {s['num_batches']:>8} {s['micro_precision']:>8.4f} {s['micro_recall']:>8.4f} "
              f"{s['micro_f1']:>8.4f} {s['macro_f1']:>8.4f} {s['avg_pred_per_batch']:>8.1f} "
              f"{s['avg_gold_per_batch']:>8.1f} {s['pred_gold_ratio']:>6.2f}")
    print("=" * 90)

    # Print top over-predicted types for count_1 vs count_64
    for ck in ["count_1", "count_64"]:
        if ck in overpred_analysis:
            oa = overpred_analysis[ck]
            print(f"\nTop over-predicted types ({ck}):")
            top = sorted(oa["type_breakdown"].items(), key=lambda x: x[1]["excess_preds"], reverse=True)[:5]
            for t, d in top:
                print(f"  {t:30s} pred={d['pred_count']:>5d} gold={d['gold_count']:>5d} "
                      f"ratio={d['pred_gold_ratio'] or 'N/A':>6} P={d['precision']:.3f} R={d['recall']:.3f} F1={d['f1']:.3f}")

    # Print FP breakdown per count
    print("\nFP Breakdown by Count:")
    print(f"{'Count':>8} {'Halluc':>8} {'WrongType':>10} {'Spurious':>10} {'TotalFP':>8}")
    print("-" * 50)
    for ck in sorted(overpred_analysis.keys(), key=lambda x: int(x.split("_")[1])):
        fb = overpred_analysis[ck]["fp_breakdown"]
        print(f"{ck:>8} {fb['hallucinated_text']:>8} {fb['wrong_type']:>10} "
              f"{fb['spurious_entity']:>10} {fb['total_fp_approx']:>8}")

    logger.info("Results saved to %s", OUTPUT_DIR)


if __name__ == "__main__":
    main()
