"""Compute truly-missed rate for NER exp007.

'Truly missed' = gold entity (for batch types) with NO overlapping prediction
at all, regardless of predicted type. This is distinct from FN, which includes
gold entities that were detected but with wrong type.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path("./src")))
from few_nerd_utils import load_few_nerd

BASE = "."
MAX_SAMPLES = 1000

BCS_BINS = [
    ("zero", 0.0, 0.001),
    ("low", 0.001, 0.90),
    ("medium", 0.90, 0.95),
    ("high", 0.95, 1.001),
]

def text_overlaps(a, b):
    if not a or not b:
        return False
    al, bl = a.lower().strip(), b.lower().strip()
    return al == bl or al in bl or bl in al

def get_bin(bcs):
    for name, lo, hi in BCS_BINS:
        if lo <= bcs < hi:
            return name
    return None

def main():
    samples = load_few_nerd(split="test", max_samples=MAX_SAMPLES)
    print(f"Loaded {len(samples)} samples")

    with open(f"{BASE}/artifacts/predictions_exp1.json") as f:
        predictions = json.load(f)

    # Group predictions by batch_id
    batches = {}
    for p in predictions:
        bid = p["batch_id"]
        if bid not in batches:
            batches[bid] = {
                "entries": [],
                "batch_types": set(p["batch_types"]),
                "batch_bcs": p.get("batch_bcs", 0.0),
            }
        batches[bid]["entries"].append(p)

    # Per-bin aggregation
    bin_stats = {name: {"total_gold": 0, "fn": 0, "truly_missed": 0, "type_confused_fn": 0}
                 for name, _, _ in BCS_BINS}

    for bid, info in batches.items():
        bcs = info["batch_bcs"]
        bname = get_bin(bcs)
        if bname is None:
            continue

        batch_types = info["batch_types"]
        by_sample = defaultdict(list)
        for p in info["entries"]:
            by_sample[p["sample_id"]].append(p)

        for sid, entries in by_sample.items():
            if sid >= len(samples):
                continue

            source_text = samples[sid]["text"]
            gold_in_batch = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
            all_preds = entries[0].get("predictions", [])

            for gold in gold_in_batch:
                gold_text = gold.get("text", "").strip()
                if not gold_text:
                    bin_stats[bname]["total_gold"] += 1
                    bin_stats[bname]["fn"] += 1
                    bin_stats[bname]["truly_missed"] += 1
                    continue

                # Check if any prediction (correct type) matches
                tp_match = False
                any_match = False
                for pred in all_preds:
                    pred_text = pred.get("text", "").strip()
                    if text_overlaps(pred_text, gold_text):
                        any_match = True
                        if pred.get("type") == gold["type"]:
                            tp_match = True
                            break

                bin_stats[bname]["total_gold"] += 1
                if not tp_match:
                    bin_stats[bname]["fn"] += 1
                    if any_match:
                        bin_stats[bname]["type_confused_fn"] += 1
                    else:
                        bin_stats[bname]["truly_missed"] += 1

    print("\n" + "=" * 90)
    print("NER exp1_random: FN decomposition by BCS bin")
    print("=" * 90)
    print(f"{'Bin':<10} {'TotalGold':>10} {'TP':>8} {'FN':>8} {'FN%':>8} "
          f"{'TrulyMissed':>12} {'Missed%':>9} {'TypeConfFN':>12} {'ConfFN%':>9}")
    print("-" * 90)
    for name, _, _ in BCS_BINS:
        s = bin_stats[name]
        tg = s["total_gold"]
        if tg == 0:
            continue
        tp = tg - s["fn"]
        fn_pct = s["fn"] / tg * 100
        missed_pct = s["truly_missed"] / tg * 100
        conf_pct = s["type_confused_fn"] / tg * 100
        print(f"{name:<10} {tg:>10} {tp:>8} {s['fn']:>8} {fn_pct:>7.1f}% "
              f"{s['truly_missed']:>12} {missed_pct:>8.1f}% "
              f"{s['type_confused_fn']:>12} {conf_pct:>8.1f}%")

    # Also compute per-batch macro average
    print("\n" + "=" * 90)
    print("Per-batch macro-average missed rate")
    print("=" * 90)
    bin_batch_rates = {name: [] for name, _, _ in BCS_BINS}
    for bid, info in batches.items():
        bcs = info["batch_bcs"]
        bname = get_bin(bcs)
        if bname is None:
            continue
        batch_types = info["batch_types"]
        by_sample = defaultdict(list)
        for p in info["entries"]:
            by_sample[p["sample_id"]].append(p)

        batch_gold = 0
        batch_missed = 0
        for sid, entries in by_sample.items():
            if sid >= len(samples):
                continue
            gold_in_batch = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
            all_preds = entries[0].get("predictions", [])
            for gold in gold_in_batch:
                gold_text = gold.get("text", "").strip()
                batch_gold += 1
                if not gold_text:
                    batch_missed += 1
                    continue
                any_match = any(
                    text_overlaps(pred.get("text", "").strip(), gold_text)
                    for pred in all_preds
                )
                if not any_match:
                    batch_missed += 1
        if batch_gold > 0:
            bin_batch_rates[bname].append(batch_missed / batch_gold)

    for name, _, _ in BCS_BINS:
        rates = bin_batch_rates[name]
        if rates:
            import numpy as np
            print(f"{name:<10} n_batches={len(rates):>3}  "
                  f"macro_missed={np.mean(rates)*100:.1f}%  "
                  f"median={np.median(rates)*100:.1f}%  "
                  f"std={np.std(rates)*100:.1f}%")

if __name__ == "__main__":
    main()
