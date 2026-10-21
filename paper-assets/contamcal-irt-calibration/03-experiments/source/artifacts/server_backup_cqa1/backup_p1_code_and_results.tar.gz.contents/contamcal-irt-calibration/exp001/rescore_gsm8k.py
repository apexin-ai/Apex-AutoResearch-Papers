import json
import os
import re

EVAL_BASE = "/root/autodl-tmp/exp001/eval_results"
EVAL_DIRS = [
    "Qwen2.5-3B_d000_s42",
    "Qwen2.5-3B_d000_s123",
    "Qwen2.5-1.5B_d000_s42",
    "Qwen2.5-1.5B_d000_s123",
    "Qwen2.5-0.5B_d000_s123",
    "Qwen2.5-0.5B_d005_s42",
]

def normalize_answer(s):
    if s is None:
        return None
    return re.sub(r'[^-\d.]', '', s)

results = []

for dname in EVAL_DIRS:
    path = os.path.join(EVAL_BASE, dname, "eval_results.json")
    data = json.load(open(path))
    gsm = data["benchmarks"]["gsm8k"]
    items = gsm["per_item"]
    total = len(items)

    old_correct = sum(1 for it in items if it["correct"])
    flipped = []
    new_correct = 0

    for it in items:
        pred_norm = normalize_answer(it["pred"])
        gold_norm = normalize_answer(it["gold"])
        new_is_correct = pred_norm is not None and pred_norm == gold_norm
        if new_is_correct:
            new_correct += 1
        if new_is_correct != it["correct"]:
            flipped.append({
                "index": it["index"],
                "pred_raw": it["pred"],
                "pred_norm": pred_norm,
                "gold_raw": it["gold"],
                "gold_norm": gold_norm,
                "old": it["correct"],
                "new": new_is_correct,
            })

    parts = dname.split("_")
    model = parts[0]
    dosage = parts[1]
    seed = parts[2]

    old_acc = old_correct / total
    new_acc = new_correct / total
    delta = new_acc - old_acc

    results.append({
        "dir": dname,
        "model": model,
        "dosage": dosage,
        "seed": seed,
        "total": total,
        "old_correct": old_correct,
        "new_correct": new_correct,
        "old_acc": old_acc,
        "new_acc": new_acc,
        "delta": delta,
        "flipped": flipped,
    })

print(f"{'Model':<16} {'Dosage':<7} {'Seed':<5} {'GSM8K_old':>10} {'GSM8K_new':>10} {'Delta':>8} {'Flipped':>8}")
print("-" * 75)
for r in results:
    flip_up = sum(1 for f in r["flipped"] if f["new"] and not f["old"])
    flip_down = sum(1 for f in r["flipped"] if f["old"] and not f["new"])
    print(f"{r['model']:<16} {r['dosage']:<7} {r['seed']:<5} {r['old_acc']:>10.4f} {r['new_acc']:>10.4f} {r['delta']:>+8.4f} {flip_up:>4}↑ {flip_down:>2}↓")

print()
for r in results:
    if r["flipped"]:
        flip_up = [f for f in r["flipped"] if f["new"] and not f["old"]]
        flip_down = [f for f in r["flipped"] if f["old"] and not f["new"]]
        print(f"\n=== {r['dir']} ===")
        if flip_up:
            print(f"  False→True ({len(flip_up)} items):")
            for f in flip_up[:20]:
                print(f"    item {f['index']}: pred='{f['pred_raw']}'→'{f['pred_norm']}' gold='{f['gold_raw']}'→'{f['gold_norm']}'")
            if len(flip_up) > 20:
                print(f"    ... and {len(flip_up)-20} more")
        if flip_down:
            print(f"  True→False ({len(flip_down)} items):")
            for f in flip_down[:10]:
                print(f"    item {f['index']}: pred='{f['pred_raw']}'→'{f['pred_norm']}' gold='{f['gold_raw']}'→'{f['gold_norm']}'")

json.dump(results, open("/root/contamcal-irt-calibration/exp001/rescore_results.json", "w"), indent=2, ensure_ascii=False, default=str)
print("\nResults saved to /root/contamcal-irt-calibration/exp001/rescore_results.json")
