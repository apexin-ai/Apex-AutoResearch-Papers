"""Diagnostic script for Exp 1 evaluation quality. CPU only."""
import json
import sys
sys.path.insert(0, "./src")
from few_nerd_utils import load_few_nerd

# Load gold data
samples = load_few_nerd(split="test", max_samples=1000)

# Load predictions
with open("./artifacts/predictions_exp1.json") as f:
    predictions = json.load(f)

# Load eval results
with open("./artifacts/eval_exp1.json") as f:
    eval_results = json.load(f)

# Group predictions by batch_id and sample_id
pred_by_batch = {}
for p in predictions:
    bid = p["batch_id"]
    pred_by_batch.setdefault(bid, {})
    pred_by_batch[bid].setdefault(p["sample_id"], []).append(p)

# ============================================================
# PART 1: Aggregate P/R/F1 per count_key
# ============================================================
print("=" * 80)
print("PART 1: Aggregate metrics per count_key")
print("=" * 80)

count_agg = {}
for bid, info in eval_results.items():
    ck = info["count_key"]
    count_agg.setdefault(ck, {"exact": [], "relaxed": [], "pred": 0, "gold": 0})
    count_agg[ck]["exact"].append(info["exact"])
    count_agg[ck]["relaxed"].append(info["relaxed"])

print(f"{'Count':<12} {'ExP':>8} {'ExR':>8} {'ExF1':>8} {'RxP':>8} {'RxR':>8} {'RxF1':>8} {'AvgPred':>8} {'AvgGold':>8} {'Batches':>8}")
for ck in sorted(count_agg.keys(), key=lambda x: int(x.split("_")[1])):
    batches = count_agg[ck]
    n = len(batches["exact"])
    # Micro-average across batches
    ex_tp = sum(b["tp"] for b in batches["exact"])
    ex_pred = sum(b["total_pred"] for b in batches["exact"])
    ex_gold = sum(b["total_gold"] for b in batches["exact"])
    rx_tp = sum(b["tp"] for b in batches["relaxed"])
    rx_pred = sum(b["total_pred"] for b in batches["relaxed"])
    rx_gold = sum(b["total_gold"] for b in batches["relaxed"])
    
    ex_p = ex_tp / ex_pred if ex_pred else 0
    ex_r = ex_tp / ex_gold if ex_gold else 0
    ex_f1 = 2*ex_p*ex_r/(ex_p+ex_r) if (ex_p+ex_r) else 0
    rx_p = rx_tp / rx_pred if rx_pred else 0
    rx_r = rx_tp / rx_gold if rx_gold else 0
    rx_f1 = 2*rx_p*rx_r/(rx_p+rx_r) if (rx_p+rx_r) else 0
    
    avg_pred = ex_pred / n
    avg_gold = ex_gold / n
    
    print(f"{ck:<12} {ex_p:>8.4f} {ex_r:>8.4f} {ex_f1:>8.4f} {rx_p:>8.4f} {rx_r:>8.4f} {rx_f1:>8.4f} {avg_pred:>8.1f} {avg_gold:>8.1f} {n:>8d}")

# ============================================================
# PART 2: Sample-level detailed comparison
# ============================================================
print("\n" + "=" * 80)
print("PART 2: Detailed sample-level comparison (10 samples)")
print("=" * 80)

# Pick specific batches for sampling
# count_1: first batch with predictions
# count_6: first batch
# count_44: first batch
target_batches = []
for ck_target in ["count_1", "count_6", "count_44"]:
    for bid in sorted(eval_results.keys()):
        if eval_results[bid]["count_key"] == ck_target:
            target_batches.append(bid)
            break

sample_count = 0
for bid in target_batches:
    if sample_count >= 10:
        break
    batch_info = eval_results[bid]
    batch_types = set(batch_info["per_type_f1"].keys())
    
    # Find samples with BOTH gold entities and predictions for this batch
    batch_preds = pred_by_batch.get(bid, {})
    interesting_samples = []
    for sid in sorted(batch_preds.keys()):
        if sid >= len(samples):
            continue
        gold_ents = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        pred_ents = batch_preds[sid][0]["predictions"]
        pred_ents_filtered = [p for p in pred_ents if p.get("type") in batch_types]
        if gold_ents or pred_ents_filtered:
            interesting_samples.append(sid)
    
    # Take up to 4 samples per batch
    n_take = min(4 if "count_1" in bid else 3, len(interesting_samples), 10 - sample_count)
    for sid in interesting_samples[:n_take]:
        sample_count += 1
        text = samples[sid]["text"]
        gold_ents = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
        pred_entry = batch_preds[sid][0]
        pred_ents = [p for p in pred_entry["predictions"] if p.get("type") in batch_types]
        
        print(f"\n=== Sample {sample_count} (sid={sid}, batch={bid}, count={batch_info['count_key']}) ===")
        print(f"[Text]: {text[:250]}{'...' if len(text)>250 else ''}")
        print(f"[Text length]: {len(text)} chars, {len(text.split())} words")
        
        print(f"\n[Gold entities] ({len(gold_ents)}):")
        for g in gold_ents:
            actual_text = text[g["start"]:g["end"]]
            print(f"  - \"{g['text']}\" [{g['type']}] char={g['start']}-{g['end']} actual_substr=\"{actual_text}\"")
        
        print(f"\n[Model predictions] ({len(pred_ents)}):")
        for p in pred_ents[:15]:  # Show max 15
            p_start = p.get("start", -1)
            p_end = p.get("end", -1)
            actual_substr = ""
            if 0 <= p_start < len(text) and 0 <= p_end <= len(text) and p_start < p_end:
                actual_substr = text[p_start:p_end]
            print(f"  - \"{p.get('text','')}\" [{p.get('type','')}] char={p_start}-{p_end} actual_substr=\"{actual_substr}\"")
        if len(pred_ents) > 15:
            print(f"  ... ({len(pred_ents) - 15} more)")
        
        # Check matches
        exact_matches = 0
        relaxed_matches = 0
        for p in pred_ents:
            for g in gold_ents:
                if p.get("start") == g["start"] and p.get("end") == g["end"] and p.get("type") == g["type"]:
                    exact_matches += 1
                    break
            for g in gold_ents:
                if p.get("type") == g["type"] and p.get("start", -1) < g["end"] and p.get("end", -1) > g["start"]:
                    relaxed_matches += 1
                    break
        
        print(f"\n[Match summary]: exact={exact_matches}/{len(pred_ents)}, relaxed={relaxed_matches}/{len(pred_ents)}")
        print(f"  Precision(exact)={exact_matches/len(pred_ents) if pred_ents else 0:.3f}, Recall(exact)={exact_matches/len(gold_ents) if gold_ents else 0:.3f}")
        print(f"  Precision(relax)={relaxed_matches/len(pred_ents) if pred_ents else 0:.3f}, Recall(relax)={relaxed_matches/len(gold_ents) if gold_ents else 0:.3f}")

# ============================================================
# PART 3: Offset analysis - are model outputs char offsets or token indices?
# ============================================================
print("\n" + "=" * 80)
print("PART 3: Offset analysis - char offset vs token index")
print("=" * 80)

offset_correct = 0
offset_wrong = 0
text_matches_but_offset_wrong = 0
offset_looks_like_token_idx = 0
total_checked = 0

for p in predictions[:5000]:  # Check first 5000 predictions
    sid = p["sample_id"]
    if sid >= len(samples):
        continue
    text = samples[sid]["text"]
    tokens = text.split()
    
    for pred in p["predictions"]:
        pred_text = pred.get("text", "")
        p_start = pred.get("start", -1)
        p_end = pred.get("end", -1)
        total_checked += 1
        
        # Check if char offsets match
        if 0 <= p_start < len(text) and 0 < p_end <= len(text):
            actual_substr = text[p_start:p_end]
            if actual_substr == pred_text:
                offset_correct += 1
            else:
                offset_wrong += 1
                # Check if the text appears in the sentence at all
                if pred_text in text:
                    text_matches_but_offset_wrong += 1
                
                # Check if start/end look like token indices
                if p_start < len(tokens) and p_end <= len(tokens):
                    token_span = " ".join(tokens[p_start:p_end])
                    if token_span == pred_text:
                        offset_looks_like_token_idx += 1
        else:
            offset_wrong += 1

print(f"Total predictions checked: {total_checked}")
print(f"Char offset correct (text[start:end] == pred_text): {offset_correct} ({100*offset_correct/total_checked:.1f}%)")
print(f"Char offset wrong: {offset_wrong} ({100*offset_wrong/total_checked:.1f}%)")
print(f"  - text exists in sentence but at wrong offset: {text_matches_but_offset_wrong}")
print(f"  - offset looks like token index (tokens[start:end] matches): {offset_looks_like_token_idx}")

# ============================================================
# PART 4: Why does relaxed F1 increase with count?
# ============================================================
print("\n" + "=" * 80)
print("PART 4: Relaxed match mechanics analysis")
print("=" * 80)

# For a wrong offset, how often does it still overlap with some gold entity?
# This tells us about accidental overlap rate
for ck_target in ["count_1", "count_6", "count_44", "count_64"]:
    accidental_overlaps = 0
    total_wrong_preds = 0
    total_preds = 0
    total_gold_ents = 0
    
    for bid, info in eval_results.items():
        if info["count_key"] != ck_target:
            continue
        batch_types = set(info["per_type_f1"].keys())
        batch_preds = pred_by_batch.get(bid, {})
        
        for sid in batch_preds:
            if sid >= len(samples):
                continue
            gold_ents = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
            pred_ents = [pe for pe in batch_preds[sid][0]["predictions"] if pe.get("type") in batch_types]
            total_preds += len(pred_ents)
            total_gold_ents += len(gold_ents)
            
            for pe in pred_ents:
                p_start = pe.get("start", -1)
                p_end = pe.get("end", -1)
                p_text = pe.get("text", "")
                text = samples[sid]["text"]
                
                # Is this a correct char offset?
                correct_offset = (0 <= p_start < len(text) and 0 < p_end <= len(text) and 
                                  text[p_start:p_end] == p_text)
                
                if not correct_offset:
                    total_wrong_preds += 1
                    # Does it still overlap with any gold?
                    for g in gold_ents:
                        if pe.get("type") == g["type"] and p_start < g["end"] and p_end > g["start"]:
                            accidental_overlaps += 1
                            break
    
    overlap_rate = accidental_overlaps / total_wrong_preds if total_wrong_preds else 0
    print(f"{ck_target}: wrong_offset_preds={total_wrong_preds}, accidental_overlaps={accidental_overlaps} ({100*overlap_rate:.1f}%), total_preds={total_preds}, total_gold={total_gold_ents}")

print("\nDone.")
