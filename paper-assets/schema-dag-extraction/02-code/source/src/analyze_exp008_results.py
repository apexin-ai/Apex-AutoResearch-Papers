#!/usr/bin/env python3
"""Analyze exp-008 SDGD-zero results: compare modes, per-batch/per-type breakdown."""

import json
import sys
from collections import defaultdict
from pathlib import Path

MODES = ["single_pass", "sdgd_zero", "random_batch", "per_type"]
EXP_DIR = Path(__file__).resolve().parent.parent / "artifacts" / "exp008"


def load_results(exp_dir: Path) -> dict:
    results = {}
    for mode in MODES:
        path = exp_dir / f"{mode}_results.json"
        if path.exists():
            with open(path) as f:
                results[mode] = json.load(f)
    return results


def load_predictions(exp_dir: Path) -> dict:
    preds = {}
    for mode in MODES:
        path = exp_dir / f"{mode}_predictions.json"
        if path.exists():
            with open(path) as f:
                preds[mode] = json.load(f)
    return preds


def load_decompositions(exp_dir: Path) -> dict:
    decomps = {}
    for mode in MODES:
        path = exp_dir / f"decomposition_{mode}.json"
        if path.exists():
            with open(path) as f:
                decomps[mode] = json.load(f)
    return decomps


def compute_per_type_metrics(predictions: list) -> dict:
    """Compute per entity-type P/R/F1 from prediction lists.

    predictions is list-of-lists: predictions[i] = [{text, type}, ...] for sample i.
    We need gold labels too, but since they're not saved separately, we compute
    from predictions alone (type distribution stats).
    """
    type_counts = defaultdict(int)
    for sample_preds in predictions:
        for ent in sample_preds:
            type_counts[ent.get("type", "UNKNOWN")] += 1
    return dict(sorted(type_counts.items(), key=lambda x: -x[1]))


def compute_per_batch_f1(predictions: list, gold: list, decomposition: dict) -> list:
    """Compute F1 per batch by filtering entities to batch-assigned types."""
    batches = decomposition.get("batches", [])
    per_batch = []

    for batch_idx, batch_types in enumerate(batches):
        batch_type_set = set(batch_types)
        tp, total_pred, total_gold = 0, 0, 0

        for preds, golds in zip(predictions, gold):
            pred_set = {
                (e["text"].strip().lower(), e["type"])
                for e in preds if e["type"] in batch_type_set
            }
            gold_set = {
                (e["text"].strip().lower(), e["type"])
                for e in golds if e["type"] in batch_type_set
            }
            tp += len(pred_set & gold_set)
            total_pred += len(pred_set)
            total_gold += len(gold_set)

        p = tp / total_pred if total_pred > 0 else 0.0
        r = tp / total_gold if total_gold > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0

        per_batch.append({
            "batch_idx": batch_idx,
            "n_types": len(batch_types),
            "types": batch_types,
            "precision": round(p, 4),
            "recall": round(r, 4),
            "f1": round(f1, 4),
            "tp": tp,
            "pred_count": total_pred,
            "gold_count": total_gold,
        })

    return per_batch


def compute_type_level_metrics(predictions: list, gold: list) -> dict:
    """Compute per entity-type P/R/F1."""
    type_tp = defaultdict(int)
    type_pred = defaultdict(int)
    type_gold = defaultdict(int)

    for preds, golds in zip(predictions, gold):
        pred_set = {(e["text"].strip().lower(), e["type"]) for e in preds}
        gold_set = {(e["text"].strip().lower(), e["type"]) for e in golds}
        matches = pred_set & gold_set

        for _, t in matches:
            type_tp[t] += 1
        for _, t in pred_set:
            type_pred[t] += 1
        for _, t in gold_set:
            type_gold[t] += 1

    all_types = sorted(set(type_tp) | set(type_pred) | set(type_gold))
    result = {}
    for t in all_types:
        tp = type_tp[t]
        pc = type_pred[t]
        gc = type_gold[t]
        p = tp / pc if pc > 0 else 0.0
        r = tp / gc if gc > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        result[t] = {"precision": round(p, 4), "recall": round(r, 4), "f1": round(f1, 4),
                      "tp": tp, "pred_count": pc, "gold_count": gc}
    return result


def batch_f1_stats(per_batch: list) -> dict:
    """Mean/std/min/max of per-batch F1."""
    f1s = [b["f1"] for b in per_batch]
    if not f1s:
        return {}
    mean = sum(f1s) / len(f1s)
    var = sum((x - mean) ** 2 for x in f1s) / len(f1s)
    return {
        "mean": round(mean, 4),
        "std": round(var ** 0.5, 4),
        "min": round(min(f1s), 4),
        "max": round(max(f1s), 4),
        "n_batches": len(f1s),
    }


def load_gold_labels(exp_dir: Path, n_samples: int = 1000) -> list:
    """Load Few-NERD gold labels. Try loading from data/parquet."""
    try:
        sys.path.insert(0, str(exp_dir.parent.parent / "src"))
        from few_nerd_utils import load_few_nerd
        data_dir = str(exp_dir.parent.parent / "data" / "parquet")
        samples = load_few_nerd(split="test", max_samples=n_samples, data_dir=data_dir)
        return [s["entities"] for s in samples]
    except Exception as e:
        print(f"WARNING: Could not load gold labels: {e}", file=sys.stderr)
        return None


def print_markdown_table(results: dict, baseline_key: str = "single_pass"):
    baseline_f1 = results.get(baseline_key, {}).get("metrics", {}).get("f1", 0)

    header = "| Mode | F1 | Precision | Recall | #Batches | Time(s) | Δ vs single_pass |"
    sep = "|------|-----|-----------|--------|----------|---------|------------------|"
    print(header)
    print(sep)

    for mode in MODES:
        if mode not in results:
            print(f"| {mode} | — | — | — | — | — | (not available) |")
            continue
        r = results[mode]
        m = r.get("metrics", {})
        f1 = m.get("f1", 0)
        p = m.get("precision", 0)
        rec = m.get("recall", 0)
        nb = r.get("n_batches", "?")
        lat = r.get("latency_s", 0)
        if mode == baseline_key:
            delta = "baseline"
        else:
            delta = f"{f1 - baseline_f1:+.4f}"
        print(f"| {mode} | {f1:.4f} | {p:.4f} | {rec:.4f} | {nb} | {lat:.1f} | {delta} |")


def main():
    exp_dir = EXP_DIR
    if len(sys.argv) > 1:
        exp_dir = Path(sys.argv[1])

    print(f"Loading results from {exp_dir}\n")

    results = load_results(exp_dir)
    predictions = load_predictions(exp_dir)
    decompositions = load_decompositions(exp_dir)

    available = list(results.keys())
    missing = [m for m in MODES if m not in results]
    print(f"Available modes: {available}")
    if missing:
        print(f"Missing modes: {missing}")
    print()

    # --- Comparison table ---
    print("## Mode Comparison\n")
    print_markdown_table(results)
    print()

    # --- Load gold for per-batch and per-type analysis ---
    n_samples = results.get("single_pass", results.get("sdgd_zero", {})).get("n_samples", 1000)
    gold = load_gold_labels(exp_dir, n_samples)

    summary = {
        "exp_id": "exp008",
        "dataset": "fewnerd",
        "available_modes": available,
        "missing_modes": missing,
        "mode_comparison": {},
        "per_batch_analysis": {},
        "type_level_metrics": {},
    }

    baseline_f1 = results.get("single_pass", {}).get("metrics", {}).get("f1", 0)
    for mode in available:
        r = results[mode]
        m = r.get("metrics", {})
        summary["mode_comparison"][mode] = {
            "f1": m.get("f1"), "precision": m.get("precision"), "recall": m.get("recall"),
            "n_batches": r.get("n_batches"), "latency_s": round(r.get("latency_s", 0), 1),
            "delta_f1_vs_single_pass": round(m.get("f1", 0) - baseline_f1, 4) if mode != "single_pass" else 0,
        }

    # --- Per-batch F1 distribution ---
    if gold:
        for mode in available:
            if mode in predictions and mode in decompositions:
                per_batch = compute_per_batch_f1(predictions[mode], gold, decompositions[mode])
                stats = batch_f1_stats(per_batch)
                summary["per_batch_analysis"][mode] = {
                    "stats": stats,
                    "per_batch": per_batch,
                }
                print(f"## Per-Batch F1 Distribution: {mode}\n")
                print(f"  mean={stats.get('mean', 'N/A')}, std={stats.get('std', 'N/A')}, "
                      f"min={stats.get('min', 'N/A')}, max={stats.get('max', 'N/A')}")
                for b in per_batch:
                    print(f"  Batch {b['batch_idx']}: F1={b['f1']:.4f} "
                          f"(P={b['precision']:.4f} R={b['recall']:.4f}) "
                          f"[{b['n_types']} types, {b['gold_count']} gold]")
                print()

        # --- Type-level metrics (use best available multi-batch mode) ---
        for mode in ["sdgd_zero", "random_batch", "single_pass"]:
            if mode in predictions:
                type_metrics = compute_type_level_metrics(predictions[mode], gold)
                summary["type_level_metrics"][mode] = type_metrics
                print(f"## Type-Level Metrics: {mode} (top 15 by gold count)\n")
                sorted_types = sorted(type_metrics.items(), key=lambda x: -x[1]["gold_count"])
                for t, m in sorted_types[:15]:
                    print(f"  {t:45s} F1={m['f1']:.4f} P={m['precision']:.4f} R={m['recall']:.4f} "
                          f"(gold={m['gold_count']}, pred={m['pred_count']})")
                print()
    else:
        print("WARNING: Gold labels not available, skipping per-batch and per-type analysis.\n")

    # --- Save summary ---
    out_path = exp_dir / "analysis_summary.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"Summary saved to {out_path}")


if __name__ == "__main__":
    main()
