"""Leave-one-task-type-out evaluation.

For each of 11 ScienceWorld task types, evaluate all 8 seed checkpoints
on that task type's samples. This tests whether the router learned
cross-task-type generalization or just task-type-level patterns.
"""
import json, os, sys, time, gc
from collections import defaultdict, Counter
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

SIMULATE_PREFIX = "[SIMULATE]"
BASE_MODEL = "/root/autodl-tmp/models/Qwen/Qwen3-1.7B"
DATA_PATH = "/root/autodl-tmp/simgate-modular-routing/data/plan-004-implicit/implicit_sft.jsonl"
PROJECT_ROOT = "/root/autodl-tmp/simgate-modular-routing"
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "results/leave_one_tasktype_out")

SEED_TO_ADAPTER = {
    42: "checkpoints/plan-008-qwen3-1.7b/final_adapter",
    43: "checkpoints/seed-robustness-seed43/final_adapter",
    44: "checkpoints/seed-robustness-seed44/final_adapter",
    45: "checkpoints/seed-robustness-seed45/final_adapter",
    46: "checkpoints/seed-robustness-seed46/final_adapter",
    47: "checkpoints/seed-robustness-seed47/final_adapter",
    48: "checkpoints/seed-robustness-seed48/final_adapter",
    49: "checkpoints/seed-robustness-seed49/final_adapter",
}


def log(msg):
    print(msg, flush=True)


def load_data():
    records = []
    with open(DATA_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def group_by_task_type(records):
    groups = defaultdict(list)
    for r in records:
        groups[r["task_type"]].append(r)
    return dict(groups)


def parse_output(text):
    text = text.strip()
    if "<think>" in text:
        think_end = text.find("</think>")
        if think_end != -1:
            text = text[think_end + len("</think>"):].strip()
        else:
            text = text[text.find("<think>") + len("<think>"):].strip()
    if text.startswith(SIMULATE_PREFIX):
        return "deterministic"
    return "internal"


def compute_balanced_acc(gts, preds):
    labels = sorted(set(gts))
    if len(labels) < 2:
        return None
    tp = {l: 0 for l in labels}
    fn = {l: 0 for l in labels}
    for g, p in zip(gts, preds):
        if g == p:
            tp[g] += 1
        else:
            fn[g] += 1
    recall = {}
    for l in labels:
        recall[l] = tp[l] / max(tp[l] + fn[l], 1)
    return np.mean([recall[l] for l in labels])


def eval_checkpoint_all_types(seed, task_groups, gpu_id):
    adapter_rel = SEED_TO_ADAPTER[seed]
    adapter_path = os.path.join(PROJECT_ROOT, adapter_rel)

    log(f"\n{'='*60}")
    log(f"Seed {seed}: {adapter_rel}")
    log(f"{'='*60}")

    tokenizer = AutoTokenizer.from_pretrained(adapter_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    base = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL, torch_dtype=torch.bfloat16,
        device_map={"": gpu_id}, trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base, adapter_path)
    model.eval()

    seed_results = {}

    for task_type in sorted(task_groups.keys()):
        records = task_groups[task_type]
        preds, gts = [], []
        t0 = time.time()

        for rec in records:
            gt_label = rec["route_label"]
            prompt_msgs = rec["messages"][:-1]

            prompt = tokenizer.apply_chat_template(
                prompt_msgs, tokenize=False, add_generation_prompt=True
            )
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

            with torch.no_grad():
                out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
            gen_ids = out[0][inputs["input_ids"].shape[1]:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)

            pred_label = parse_output(gen_text)
            preds.append(pred_label)
            gts.append(gt_label)

        elapsed = time.time() - t0
        bal_acc = compute_balanced_acc(gts, preds)
        accuracy = sum(1 for g, p in zip(gts, preds) if g == p) / max(len(gts), 1)

        gt_dist = Counter(gts)
        pred_dist = Counter(preds)
        n_classes = len(set(gts))

        seed_results[task_type] = {
            "balanced_accuracy": round(bal_acc, 4) if bal_acc is not None else None,
            "accuracy": round(accuracy, 4),
            "n_samples": len(records),
            "n_classes": n_classes,
            "gt_distribution": dict(gt_dist),
            "pred_distribution": dict(pred_dist),
            "eval_time_s": round(elapsed, 1),
        }

        ba_str = f"{bal_acc:.4f}" if bal_acc is not None else "N/A (single class)"
        log(f"  {task_type:45s} bal_acc={ba_str:>8s}  acc={accuracy:.4f}  n={len(records)}  ({elapsed:.1f}s)")

    del model, base, tokenizer
    gc.collect()
    torch.cuda.empty_cache()

    return seed_results


def majority_vote_baseline(task_groups):
    baselines = {}
    for task_type, records in sorted(task_groups.items()):
        gts = [r["route_label"] for r in records]
        majority = Counter(gts).most_common(1)[0][0]
        preds = [majority] * len(gts)
        bal_acc = compute_balanced_acc(gts, preds)
        accuracy = sum(1 for g, p in zip(gts, preds) if g == p) / len(gts)
        baselines[task_type] = {
            "balanced_accuracy": round(bal_acc, 4) if bal_acc is not None else None,
            "accuracy": round(accuracy, 4),
            "majority_class": majority,
        }
    return baselines


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--gpu_id", type=int, default=1)
    args = p.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    log("Loading data...")
    records = load_data()
    log(f"Total records: {len(records)}")

    task_groups = group_by_task_type(records)
    log(f"Task types: {len(task_groups)}")
    for tt in sorted(task_groups):
        recs = task_groups[tt]
        labels = Counter(r["route_label"] for r in recs)
        log(f"  {tt:45s} n={len(recs):4d}  {dict(labels)}")

    baselines = majority_vote_baseline(task_groups)

    seeds = sorted(SEED_TO_ADAPTER.keys())
    all_results = {}

    for seed in seeds:
        all_results[seed] = eval_checkpoint_all_types(seed, task_groups, args.gpu_id)

    # Build matrix and summaries
    task_types = sorted(task_groups.keys())

    log(f"\n{'='*70}")
    log("LEAVE-ONE-TASK-TYPE-OUT RESULTS")
    log(f"{'='*70}")

    header = f"{'Task Type':45s}" + "".join(f"  s{s}" for s in seeds) + "    Mean   MajVote"
    log(header)
    log("-" * len(header))

    per_task_means = {}
    two_class_accs = []

    for tt in task_types:
        n_classes = len(set(r["route_label"] for r in task_groups[tt]))
        accs = []
        row = f"{tt:45s}"
        for s in seeds:
            ba = all_results[s][tt]["balanced_accuracy"]
            if ba is not None:
                accs.append(ba)
                row += f" {ba:.3f}"
            else:
                row += "   N/A"

        if accs:
            mean_ba = np.mean(accs)
            per_task_means[tt] = mean_ba
            row += f"  {mean_ba:.4f}"
            if n_classes >= 2:
                two_class_accs.extend(accs)
        else:
            per_task_means[tt] = None
            row += "     N/A"

        mv = baselines[tt]["balanced_accuracy"]
        if mv is not None:
            row += f"   {mv:.4f}"
        else:
            row += "     N/A"

        log(row)

    # Overall summary (only for task types with 2 classes)
    two_class_types = [tt for tt in task_types if per_task_means[tt] is not None]
    single_class_types = [tt for tt in task_types if per_task_means[tt] is None]

    log(f"\n--- Summary ---")
    log(f"Task types with 2 classes: {len(two_class_types)}")
    log(f"Task types with 1 class (all deterministic): {len(single_class_types)}")

    if two_class_types:
        means = [per_task_means[tt] for tt in two_class_types]
        log(f"\nPer-task-type mean balanced_acc (2-class only):")
        for tt in two_class_types:
            log(f"  {tt:45s} {per_task_means[tt]:.4f}")
        overall_mean = np.mean(means)
        overall_std = np.std(means)
        log(f"\nOverall mean across 2-class task types: {overall_mean:.4f} ± {overall_std:.4f}")

    # Per-seed mean (across 2-class task types)
    log(f"\nPer-seed mean balanced_acc (2-class task types only):")
    per_seed_means = {}
    for s in seeds:
        s_accs = [all_results[s][tt]["balanced_accuracy"] for tt in two_class_types
                  if all_results[s][tt]["balanced_accuracy"] is not None]
        if s_accs:
            per_seed_means[s] = np.mean(s_accs)
            log(f"  Seed {s}: {per_seed_means[s]:.4f}")

    if per_seed_means:
        grand_mean = np.mean(list(per_seed_means.values()))
        grand_std = np.std(list(per_seed_means.values()))
        log(f"  Grand mean: {grand_mean:.4f} ± {grand_std:.4f}")

    log(f"\nCross-split reference: 0.4711 ± 0.0221")

    # For single-class task types, report accuracy (all should be deterministic)
    if single_class_types:
        log(f"\nSingle-class task types (all deterministic) - accuracy:")
        for tt in single_class_types:
            accs = [all_results[s][tt]["accuracy"] for s in seeds]
            log(f"  {tt:45s} mean_acc={np.mean(accs):.4f} (predicts det correctly?)")

    # Save results
    output = {
        "description": "Leave-one-task-type-out evaluation",
        "note": "Existing checkpoints (trained on all task types) evaluated per task type",
        "data_path": DATA_PATH,
        "n_total_samples": len(records),
        "n_task_types": len(task_types),
        "seeds": seeds,
        "task_types": task_types,
        "two_class_types": two_class_types,
        "single_class_types": single_class_types,
        "per_seed_per_type": {
            str(s): {tt: all_results[s][tt] for tt in task_types} for s in seeds
        },
        "per_task_means": {tt: round(v, 4) if v is not None else None
                          for tt, v in per_task_means.items()},
        "majority_vote_baselines": baselines,
        "per_seed_means_2class": {str(s): round(v, 4) for s, v in per_seed_means.items()},
        "grand_mean_2class": round(grand_mean, 4) if per_seed_means else None,
        "grand_std_2class": round(grand_std, 4) if per_seed_means else None,
        "cross_split_reference": {"mean": 0.4711, "std": 0.0221},
    }

    out_path = os.path.join(OUTPUT_DIR, "results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    log(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
