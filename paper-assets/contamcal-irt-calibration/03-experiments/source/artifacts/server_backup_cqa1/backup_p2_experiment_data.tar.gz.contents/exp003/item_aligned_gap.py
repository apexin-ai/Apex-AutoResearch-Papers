import json

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
MODELS = [
    ("Qwen2.5-1.5B_d100_s42", "1.5B d100"),
    ("Qwen2.5-3B_d100_s42", "3B d100"),
]

for model_prefix, label in MODELS:
    aligned_path = f"{EVAL_DIR}/{model_prefix}_aligned/item_responses.json"
    para_path = f"{EVAL_DIR}/{model_prefix}_para_aligned/item_responses.json"
    
    with open(aligned_path) as f:
        aligned_items = json.load(f)
    with open(para_path) as f:
        para_items = json.load(f)
    
    # Build lookup: item_id -> correct for aligned (original)
    aligned_lookup = {item["item_id"]: item["correct"] for item in aligned_items if item["benchmark"] == "mmlu"}
    
    # Get para item IDs
    para_ids = set()
    para_correct = 0
    para_total = 0
    for item in para_items:
        if item["benchmark"] == "mmlu":
            para_ids.add(item["item_id"])
            para_total += 1
            if item["correct"]:
                para_correct += 1
    
    # Item-aligned original: only the items that exist in para
    aligned_matched_correct = 0
    aligned_matched_total = 0
    aligned_unmatched_correct = 0
    aligned_unmatched_total = 0
    
    for item_id, correct in aligned_lookup.items():
        if item_id in para_ids:
            aligned_matched_total += 1
            if correct:
                aligned_matched_correct += 1
        else:
            aligned_unmatched_total += 1
            if correct:
                aligned_unmatched_correct += 1
    
    # Compute accuracies
    full_orig_acc = sum(1 for v in aligned_lookup.values() if v) / len(aligned_lookup)
    matched_orig_acc = aligned_matched_correct / aligned_matched_total
    unmatched_orig_acc = aligned_unmatched_correct / aligned_unmatched_total
    para_acc = para_correct / para_total
    
    print(f"=== {label} ===")
    print(f"Full original:        {sum(1 for v in aligned_lookup.values() if v)}/{len(aligned_lookup)} = {full_orig_acc:.4f}")
    print(f"Item-aligned original:{aligned_matched_correct}/{aligned_matched_total} = {matched_orig_acc:.4f}  (QC-passed items only)")
    print(f"QC-failed original:   {aligned_unmatched_correct}/{aligned_unmatched_total} = {unmatched_orig_acc:.4f}  (items without paraphrase)")
    print(f"Paraphrase:           {para_correct}/{para_total} = {para_acc:.4f}")
    print(f"")
    print(f"Original gap (full):         {full_orig_acc - para_acc:+.4f}  (full 14042 vs para 6596)")
    print(f"Item-aligned gap (corrected):{matched_orig_acc - para_acc:+.4f}  (same 6596 items)")
    print(f"QC-passed vs QC-failed diff: {matched_orig_acc - unmatched_orig_acc:+.4f}  (selection bias)")
    print()
