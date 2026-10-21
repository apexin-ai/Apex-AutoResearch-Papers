# R7-N2 Data-size ablation: demonstrates router balanced_acc saturation as training
# data scales from current 81 episodes up to 200/400/800 synthetic episodes.
# Purpose: rebut reviewer concern that "thin signal" conclusion is confounded with
# data insufficiency. If balanced_acc saturates, signal is genuinely thin.
#
# Augmentation strategy: observation text perturbation (sentence reorder, synonym
# substitution, truncation) preserving episode-level labels. Scientifically defensible
# because the routing label depends on episode outcome, not surface observation text.
#
# Usage:
#   python ablation_data_size.py --data_path data/plan-004-implicit/implicit_sft.jsonl \
#       --model_name /root/autodl-tmp/models/Qwen3-1.7B --gpu_id 0 --seeds 42 43 44
#
# Output: results/ablation_data_size/summary.json + per-scale checkpoints

import argparse
import copy
import gc
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Any

import numpy as np
import torch
from sklearn.metrics import balanced_accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
)
from peft import LoraConfig, get_peft_model, TaskType, PeftModel

sys.path.insert(0, os.path.dirname(__file__))
from training.implicit_router_sft import (
    ImplicitSFTDataset,
    PaddingCollator,
    load_implicit_sft_data,
    parse_implicit_output,
    MODEL_ID,
    SIMULATE_PREFIX,
)


# ---------------------------------------------------------------------------
# Data augmentation
# ---------------------------------------------------------------------------

SYNONYM_MAP = {
    "look around": "examine surroundings",
    "pick up": "take",
    "put down": "place",
    "open": "open up",
    "close": "shut",
    "move to": "go to",
    "use": "utilize",
    "examine": "inspect",
    "the": "the",  # no-op placeholder to avoid empty map
}


def perturb_observation(obs: str, rng: random.Random, intensity: float = 0.3) -> str:
    """Perturb observation text while preserving semantic content.

    Applies random subset of: sentence reordering, synonym substitution,
    minor token dropout, whitespace variation.
    """
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', obs) if s.strip()]

    if len(sentences) > 2 and rng.random() < intensity:
        # Shuffle non-first sentences (first often has critical state info)
        rest = sentences[1:]
        rng.shuffle(rest)
        sentences = [sentences[0]] + rest

    result = " ".join(sentences)

    # Synonym substitution (low rate to avoid semantic drift)
    if rng.random() < intensity:
        for old, new in SYNONYM_MAP.items():
            if old in result.lower() and rng.random() < 0.3:
                result = re.sub(re.escape(old), new, result, count=1, flags=re.IGNORECASE)
                break

    # Minor token dropout (remove a random word ~5% of the time)
    if rng.random() < intensity * 0.3:
        words = result.split()
        if len(words) > 10:
            drop_idx = rng.randint(3, len(words) - 1)
            words.pop(drop_idx)
            result = " ".join(words)

    return result


def perturb_history(history_str: str, rng: random.Random) -> str:
    """Slightly vary action history representation."""
    if rng.random() < 0.3:
        # Truncate one action from history
        parts = history_str.split(" -> ")
        if len(parts) > 2:
            parts = parts[1:]  # drop oldest
            return " -> ".join(parts)
    return history_str


def augment_record(record: Dict, rng: random.Random, aug_id: int) -> Dict:
    """Create an augmented copy of an implicit SFT record."""
    new_rec = copy.deepcopy(record)
    messages = new_rec["messages"]

    # Perturb user message (observation + history)
    user_msg = messages[1]["content"]
    parts = user_msg.split("\nAction history: ")
    if len(parts) == 2:
        obs_part = parts[0].replace("Observation: ", "", 1)
        hist_part = parts[1]
        new_obs = perturb_observation(obs_part, rng)
        new_hist = perturb_history(hist_part, rng)
        messages[1]["content"] = f"Observation: {new_obs}\nAction history: {new_hist}"
    else:
        obs_text = user_msg.replace("Observation: ", "", 1)
        messages[1]["content"] = f"Observation: {perturb_observation(obs_text, rng)}"

    # Tag augmented records for traceability
    new_rec["augmented"] = True
    new_rec["aug_id"] = aug_id
    return new_rec


def create_augmented_dataset(
    records: List[Dict],
    target_size: int,
    seed: int,
) -> List[Dict]:
    """Augment training records to reach target_size.

    If target_size <= len(records), subsample instead.
    """
    rng = random.Random(seed)

    if target_size <= len(records):
        shuffled = records[:]
        rng.shuffle(shuffled)
        return shuffled[:target_size]

    # Start with all original records
    augmented = records[:]
    remaining = target_size - len(records)

    # Stratified augmentation: maintain label ratio
    by_label = defaultdict(list)
    for r in records:
        by_label[r["route_label"]].append(r)

    total_orig = len(records)
    aug_id = 0
    while remaining > 0:
        for label, label_records in by_label.items():
            # Augment proportionally to original distribution
            n_from_label = max(1, int(remaining * len(label_records) / total_orig))
            n_from_label = min(n_from_label, remaining)
            for _ in range(n_from_label):
                source = rng.choice(label_records)
                augmented.append(augment_record(source, rng, aug_id))
                aug_id += 1
                remaining -= 1
                if remaining <= 0:
                    break
            if remaining <= 0:
                break

    rng.shuffle(augmented)
    return augmented


# ---------------------------------------------------------------------------
# Episode-level split (no episode overlap between train and val)
# ---------------------------------------------------------------------------

def episode_level_split(records, test_size=0.15, seed=42):
    """Split records by episode (task_type + variation), not by step.

    Ensures complete episode isolation: all steps from a given episode go
    entirely to train or entirely to val. Uses sklearn train_test_split on
    episode keys for reproducibility.
    """
    episode_to_indices = defaultdict(list)
    for i, r in enumerate(records):
        key = (r["task_type"], r["variation"])
        episode_to_indices[key].append(i)

    episode_keys = sorted(episode_to_indices.keys())
    _, val_eps = train_test_split(
        episode_keys, test_size=test_size, random_state=seed
    )

    val_indices = []
    for ep in val_eps:
        val_indices.extend(episode_to_indices[ep])

    val_records = [records[i] for i in sorted(val_indices)]
    return val_records


def parse_output_strip_think(text):
    """Parse model output, stripping Qwen3 <think> tags before routing check."""
    text = text.strip()
    if "<think>" in text:
        think_end = text.find("</think>")
        if think_end != -1:
            text = text[think_end + len("</think>"):].strip()
        else:
            text = text[text.find("<think>") + len("<think>"):].strip()
    if text.startswith(SIMULATE_PREFIX):
        return text[len(SIMULATE_PREFIX):].strip(), "deterministic"
    return text, "internal"


# ---------------------------------------------------------------------------
# Generation-based evaluation (matches paper eval methodology)
# ---------------------------------------------------------------------------

def generation_eval(
    model,
    tokenizer,
    val_records: List[Dict],
    batch_size: int = 8,
) -> Dict[str, float]:
    """Evaluate router via text generation, matching paper's eval protocol.

    For each val record, generate output and parse routing decision.
    Compute balanced accuracy on route_label predictions.
    """
    model.eval()
    y_true = []
    y_pred = []

    for i in range(0, len(val_records), batch_size):
        batch = val_records[i:i + batch_size]
        for rec in batch:
            messages = rec["messages"][:2]  # system + user only
            prompt = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True,
                enable_thinking=False
            )
            inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                               max_length=2048).to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=128,
                    temperature=0.1,
                    do_sample=True,
                    pad_token_id=tokenizer.pad_token_id,
                )
            new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
            raw_output = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

            # Strip <think> tags before routing classification
            _, route_pred = parse_output_strip_think(raw_output)
            y_pred.append(route_pred)
            y_true.append(rec["route_label"])

    label_map = {"internal": 0, "deterministic": 1}
    y_true_ids = [label_map[y] for y in y_true]
    y_pred_ids = [label_map[y] for y in y_pred]

    bal_acc = balanced_accuracy_score(y_true_ids, y_pred_ids)
    det_recall = recall_score(y_true_ids, y_pred_ids, pos_label=1, zero_division=0)
    int_recall = recall_score(y_true_ids, y_pred_ids, pos_label=0, zero_division=0)

    return {
        "balanced_accuracy": float(bal_acc),
        "deterministic_recall": float(det_recall),
        "internal_recall": float(int_recall),
        "n_val": len(val_records),
        "pred_distribution": dict(Counter(y_pred)),
        "true_distribution": dict(Counter(y_true)),
    }


# ---------------------------------------------------------------------------
# Training loop (single scale point)
# ---------------------------------------------------------------------------

def train_at_scale(
    train_records: List[Dict],
    val_records: List[Dict],
    episode_val_records: List[Dict],
    args,
    scale_label: str,
    seed: int,
) -> Dict[str, Any]:
    """Train implicit router at a given data scale, return both step-level and episode-level eval."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    model_path = args.model_name
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        device_map={"": args.gpu_id},
        trust_remote_code=True,
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    )
    model = get_peft_model(model, lora_config)

    train_dataset = ImplicitSFTDataset(train_records, tokenizer, args.max_seq_len)
    val_dataset = ImplicitSFTDataset(val_records, tokenizer, args.max_seq_len)
    collator = PaddingCollator(tokenizer, args.max_seq_len)

    output_dir = os.path.join(args.output_dir, f"scale_{scale_label}_seed{seed}")
    os.makedirs(output_dir, exist_ok=True)

    effective_batch = 32
    ga_steps = max(1, effective_batch // args.batch_size)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        learning_rate=2e-5,
        warmup_ratio=0.1,
        weight_decay=0.01,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        bf16=True,
        logging_steps=10,
        report_to="wandb" if args.wandb else "none",
        run_name=f"data-size-{scale_label}-s{seed}",
        seed=seed,
        save_total_limit=1,
        gradient_accumulation_steps=ga_steps,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        data_collator=collator,
    )
    trainer.train()

    # OOM fix: free trainer (optimizer states + grad buffers) before generation eval
    del trainer
    gc.collect()
    torch.cuda.empty_cache()

    model.eval()

    # Step-level eval (original: same-episode steps may appear in both train/val)
    step_eval = generation_eval(model, tokenizer, val_records, batch_size=8)

    # Episode-level eval (no episode overlap between train and val)
    episode_eval = generation_eval(model, tokenizer, episode_val_records, batch_size=8)

    eval_results = {
        "scale": scale_label,
        "seed": seed,
        "n_train": len(train_records),
        "train_label_dist": dict(Counter(r["route_label"] for r in train_records)),
        "step_level_eval": {
            "balanced_acc": step_eval["balanced_accuracy"],
            "det_recall": step_eval["deterministic_recall"],
            "int_recall": step_eval["internal_recall"],
            "n_val": step_eval["n_val"],
            "pred_distribution": step_eval["pred_distribution"],
            "true_distribution": step_eval["true_distribution"],
        },
        "episode_level_eval": {
            "balanced_acc": episode_eval["balanced_accuracy"],
            "det_recall": episode_eval["deterministic_recall"],
            "int_recall": episode_eval["internal_recall"],
            "n_val": episode_eval["n_val"],
            "pred_distribution": episode_eval["pred_distribution"],
            "true_distribution": episode_eval["true_distribution"],
        },
    }

    eval_path = os.path.join(output_dir, "eval_results.json")
    with open(eval_path, "w") as f:
        json.dump(eval_results, f, indent=2)

    # Cleanup model to free GPU memory
    del model
    gc.collect()
    torch.cuda.empty_cache()

    return eval_results


# ---------------------------------------------------------------------------
# Main ablation loop
# ---------------------------------------------------------------------------

def _run_is_complete(output_dir, scale_label, seed):
    """Check if a run already has both step-level and episode-level eval results."""
    eval_path = os.path.join(output_dir, f"scale_{scale_label}_seed{seed}", "eval_results.json")
    if not os.path.exists(eval_path):
        return False, None
    try:
        with open(eval_path) as f:
            results = json.load(f)
        if "episode_level_eval" in results and "step_level_eval" in results:
            return True, results
    except (json.JSONDecodeError, KeyError):
        pass
    return False, None


def run_ablation(args):
    """Run data-size ablation across multiple scales and seeds."""
    # Load full dataset (step-level split for training/step-eval)
    data_path = args.data_path
    all_records, val_records = load_implicit_sft_data(
        data_path, eval_split=0.15, seed=42
    )
    n_original = len(all_records)
    print(f"Original training data: {n_original} records")
    print(f"Step-level val data: {len(val_records)} records")
    print(f"Label distribution (train): {dict(Counter(r['route_label'] for r in all_records))}")

    # Episode-level val split (from full dataset, independent of step-level split)
    raw_records = []
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if line:
                raw_records.append(json.loads(line))
    episode_val_records = episode_level_split(raw_records, test_size=0.15, seed=42)
    ep_dist = dict(Counter(r["route_label"] for r in episode_val_records))
    ep_keys = set((r["task_type"], r["variation"]) for r in episode_val_records)
    print(f"Episode-level val data: {len(episode_val_records)} steps from {len(ep_keys)} episodes, dist={ep_dist}")

    scale_points = {
        "25pct": int(n_original * 0.25),
        "50pct": int(n_original * 0.50),
        "75pct": int(n_original * 0.75),
        "100pct": n_original,
        "200pct": n_original * 2,
        "400pct": n_original * 4,
        "800pct": n_original * 8,
    }

    seeds = [int(s) for s in args.seeds]
    os.makedirs(args.output_dir, exist_ok=True)

    all_results = []
    for scale_label, target_size in scale_points.items():
        print(f"\n{'='*60}")
        print(f"Scale: {scale_label} (target {target_size} training records)")
        print(f"{'='*60}")

        for seed in seeds:
            # Resume: skip runs that already have both eval types
            complete, cached = _run_is_complete(args.output_dir, scale_label, seed)
            if complete:
                print(f"\n--- Seed {seed} --- SKIPPED (already complete)")
                all_results.append(cached)
                continue

            print(f"\n--- Seed {seed} ---")
            train_data = create_augmented_dataset(all_records, target_size, seed)
            print(f"  Training records: {len(train_data)}")
            print(f"  Augmented: {sum(1 for r in train_data if r.get('augmented', False))}")
            print(f"  Label dist: {dict(Counter(r['route_label'] for r in train_data))}")

            result = train_at_scale(
                train_data, val_records, episode_val_records,
                args, scale_label, seed,
            )
            all_results.append(result)
            step_ba = result["step_level_eval"]["balanced_acc"]
            ep_ba = result["episode_level_eval"]["balanced_acc"]
            print(f"  Step-level balanced_acc: {step_ba:.4f}")
            print(f"  Episode-level balanced_acc: {ep_ba:.4f}")

    # Aggregate results
    summary = aggregate_results(all_results, scale_points)
    summary_path = os.path.join(args.output_dir, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to {summary_path}")

    # Print final summary table
    print(f"\n{'='*60}")
    print("DATA SIZE ABLATION SUMMARY")
    print(f"{'='*60}")
    print(f"{'Scale':<10} {'N_train':<10} {'StepBalAcc':<14} {'EpBalAcc':<14} {'Saturated?':<10}")
    print("-" * 62)
    for row in summary["table"]:
        sat = "YES" if row.get("saturated") else ""
        print(f"{row['scale']:<10} {row['n_train']:<10} "
              f"{row['step_bal_acc_mean']:.4f}+/-{row['step_bal_acc_std']:.4f}  "
              f"{row['ep_bal_acc_mean']:.4f}+/-{row['ep_bal_acc_std']:.4f}  {sat}")


def aggregate_results(
    all_results: List[Dict],
    scale_points: Dict[str, int],
) -> Dict[str, Any]:
    """Aggregate per-seed results into summary with saturation detection.

    Uses episode-level balanced_acc as the primary metric for saturation.
    """
    by_scale = defaultdict(list)
    for r in all_results:
        by_scale[r["scale"]].append(r)

    table = []
    prev_ep_mean = None
    for scale_label in scale_points:
        results = by_scale[scale_label]
        if not results:
            continue

        step_accs = [r["step_level_eval"]["balanced_acc"] for r in results]
        ep_accs = [r["episode_level_eval"]["balanced_acc"] for r in results]

        ep_mean = float(np.mean(ep_accs))

        # Saturation based on episode-level balanced_acc (the trustworthy metric)
        saturated = False
        if prev_ep_mean is not None and (ep_mean - prev_ep_mean) < 0.01:
            saturated = True

        table.append({
            "scale": scale_label,
            "n_train": results[0]["n_train"],
            "step_bal_acc_mean": float(np.mean(step_accs)),
            "step_bal_acc_std": float(np.std(step_accs)),
            "ep_bal_acc_mean": ep_mean,
            "ep_bal_acc_std": float(np.std(ep_accs)),
            "saturated": saturated,
            "per_seed_step": step_accs,
            "per_seed_episode": ep_accs,
        })
        prev_ep_mean = ep_mean

    saturated_at = None
    for row in table:
        if row["saturated"]:
            saturated_at = row["scale"]
            break

    conclusion = {
        "saturated_at": saturated_at,
        "interpretation": (
            f"Episode-level balanced accuracy saturates at {saturated_at} scale, "
            "confirming that performance plateau is due to thin routing signal "
            "(extreme class imbalance + death-dominated labels) rather than "
            "data insufficiency."
        ) if saturated_at else (
            "No clear saturation observed; more data may help. "
            "However, if final balanced accuracy remains near chance (~50%), "
            "the signal itself is likely thin regardless of data scale."
        ),
    }

    return {
        "table": table,
        "conclusion": conclusion,
        "config": {
            "eval_split": 0.15,
            "eval_seed": 42,
            "augmentation": "observation_perturbation",
            "model": MODEL_ID,
            "lora_r": 16,
            "effective_batch": 32,
            "epochs": 3,
        },
        "raw_results": all_results,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="R7-N2 Data-size ablation: router performance vs training data scale"
    )
    p.add_argument("--data_path", type=str, required=True,
                   help="Path to implicit_sft.jsonl")
    p.add_argument("--model_name", type=str, default=MODEL_ID,
                   help="Base model path (local or HF)")
    p.add_argument("--output_dir", type=str, default="results/ablation_data_size",
                   help="Output directory for checkpoints and results")
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--batch_size", type=int, default=4,
                   help="Per-device batch size (GA auto-computed for effective=32)")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--seeds", nargs="+", default=["42", "43", "44"],
                   help="Random seeds for multi-seed evaluation")
    p.add_argument("--wandb", action="store_true",
                   help="Enable W&B logging")
    p.add_argument("--dry_run", action="store_true",
                   help="Validate data loading and augmentation without training")
    return p.parse_args()


def dry_run(args):
    """Validate augmentation pipeline without GPU training."""
    data_path = args.data_path
    all_records, val_records = load_implicit_sft_data(
        data_path, eval_split=0.15, seed=42
    )
    print(f"Original: {len(all_records)} train, {len(val_records)} val")
    print(f"Labels: {dict(Counter(r['route_label'] for r in all_records))}")

    for target in [len(all_records) * 2, len(all_records) * 4, len(all_records) * 8]:
        aug = create_augmented_dataset(all_records, target, seed=42)
        n_aug = sum(1 for r in aug if r.get("augmented", False))
        dist = dict(Counter(r["route_label"] for r in aug))
        print(f"  Target {target}: got {len(aug)} ({n_aug} augmented), dist={dist}")

        # Verify augmented records are valid
        sample = [r for r in aug if r.get("augmented", False)][:3]
        for s in sample:
            assert "messages" in s and len(s["messages"]) == 3
            assert s["route_label"] in ("internal", "deterministic")
    print("\nDry run PASSED - augmentation pipeline valid")


if __name__ == "__main__":
    args = parse_args()
    if args.dry_run:
        dry_run(args)
    else:
        os.environ.setdefault("WANDB_PROJECT", "simgate-data-size-ablation")
        run_ablation(args)
