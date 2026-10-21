# Standalone evaluation script for trained router SFT adapter.
# Loads a LoRA adapter checkpoint, evaluates on held-out data, and compares
# against baselines (majority-class, always-deterministic).

import argparse
import json
import os
import sys
from collections import Counter
from typing import List, Dict, Any, Optional

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score, precision_recall_fscore_support,
    confusion_matrix, classification_report,
)
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from peft import PeftModel

LABEL2ID = {"internal": 0, "deterministic": 1}
ID2LABEL = {0: "internal", 1: "deterministic"}

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
    "internal": "internal",
    "deterministic": "deterministic",
}

SYSTEM_PROMPT = (
    "You are a routing classifier. Given the current observation and action history, "
    "predict which reasoning modality will lead to a better outcome."
)


def parse_args():
    p = argparse.ArgumentParser(description="Evaluate trained router SFT adapter")
    p.add_argument("--adapter_dir", type=str, required=True,
                    help="Path to saved LoRA adapter (final_adapter/)")
    p.add_argument("--base_model", type=str, default=None,
                    help="Base model path (inferred from adapter config if omitted)")
    p.add_argument("--data_path", type=str, required=True,
                    help="JSONL file with labeled steps (sft_triples.jsonl)")
    p.add_argument("--output_path", type=str, default=None,
                    help="Output JSON report path (default: adapter_dir/standalone_eval.json)")
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--eval_split", type=float, default=0.2,
                    help="Use same split ratio as training to extract held-out set")
    p.add_argument("--seed", type=int, default=42)
    return p.parse_args()


def summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:
    recent = action_history[-max_actions:] if action_history else []
    if not recent:
        return "(none)"
    return " → ".join(recent)


def build_prompt(observation: str, action_history: List[str]) -> str:
    history_summary = summarize_action_history(action_history)
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )


def load_data(data_path: str) -> List[Dict]:
    samples = []
    skipped = Counter()
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            raw_label = record.get("label", "")
            label = RAW_LABEL_MAP.get(raw_label)
            if label is None:
                skipped[raw_label] += 1
                continue
            samples.append({
                "observation": record.get("observation", ""),
                "action_history": record.get("action_history", []),
                "label": label,
                "label_id": LABEL2ID[label],
                "task_type": record.get("task_type", "unknown"),
                "episode_id": record.get("episode_id"),
                "variation": record.get("variation"),
            })
    if skipped:
        print(f"Skipped labels: {dict(skipped)}")
    return samples


def episode_level_split(samples: List[Dict], eval_ratio: float, seed: int):
    """Reproduce the same episode-level stratified split used in training."""
    import random
    rng = random.Random(seed)

    episodes: Dict[tuple, List[Dict]] = {}
    for s in samples:
        key = (s["task_type"], s.get("episode_id"), s.get("variation"))
        episodes.setdefault(key, []).append(s)

    by_task: Dict[str, List[tuple]] = {}
    for key in episodes:
        by_task.setdefault(key[0], []).append(key)

    train_set, val_set = [], []
    for task, ep_keys in by_task.items():
        rng.shuffle(ep_keys)
        n_val = max(1, int(len(ep_keys) * eval_ratio))
        for k in ep_keys[:n_val]:
            val_set.extend(episodes[k])
        for k in ep_keys[n_val:]:
            train_set.extend(episodes[k])

    rng.shuffle(val_set)
    return train_set, val_set


def predict_batch(model, tokenizer, texts: List[str], max_len: int, device) -> np.ndarray:
    encodings = tokenizer(
        texts, truncation=True, max_length=max_len,
        padding="max_length", return_tensors="pt",
    )
    encodings = {k: v.to(device) for k, v in encodings.items()}
    with torch.no_grad():
        logits = model(**encodings).logits
    return logits.cpu().numpy()


def compute_baselines(labels: np.ndarray) -> Dict[str, Any]:
    """Compute majority-class and always-deterministic baseline accuracies."""
    n = len(labels)
    counts = Counter(labels.tolist())

    majority_label = counts.most_common(1)[0][0]
    majority_preds = np.full(n, majority_label)
    majority_acc = accuracy_score(labels, majority_preds)

    always_det_preds = np.full(n, LABEL2ID["deterministic"])
    always_det_acc = accuracy_score(labels, always_det_preds)

    return {
        "majority_class": {
            "label": ID2LABEL[majority_label],
            "accuracy": majority_acc,
        },
        "always_deterministic": {
            "accuracy": always_det_acc,
        },
        "label_distribution": {ID2LABEL[k]: v for k, v in sorted(counts.items())},
    }


def main():
    args = parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_id)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if args.output_path is None:
        args.output_path = os.path.join(
            os.path.dirname(args.adapter_dir.rstrip("/")), "standalone_eval.json"
        )

    print(f"Loading data from {args.data_path}")
    all_samples = load_data(args.data_path)
    print(f"Total usable samples: {len(all_samples)}")

    _, val_samples = episode_level_split(all_samples, args.eval_split, args.seed)
    print(f"Eval set: {len(val_samples)} steps")
    val_label_dist = Counter(s["label"] for s in val_samples)
    for k, v in sorted(val_label_dist.items()):
        print(f"  {k}: {v} ({v/len(val_samples)*100:.1f}%)")

    print(f"\nLoading adapter from {args.adapter_dir}")
    tokenizer = AutoTokenizer.from_pretrained(args.adapter_dir, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    base_model_name = args.base_model
    if base_model_name is None:
        adapter_config_path = os.path.join(args.adapter_dir, "adapter_config.json")
        with open(adapter_config_path) as f:
            adapter_cfg = json.load(f)
        base_model_name = adapter_cfg.get("base_model_name_or_path", "")
        if not base_model_name:
            print("ERROR: Cannot infer base model from adapter config. Use --base_model.")
            sys.exit(1)
    print(f"Base model: {base_model_name}")

    base_model = AutoModelForSequenceClassification.from_pretrained(
        base_model_name, num_labels=2, id2label=ID2LABEL, label2id=LABEL2ID,
        trust_remote_code=True, torch_dtype=torch.bfloat16,
    )
    model = PeftModel.from_pretrained(base_model, args.adapter_dir)
    model = model.to(device)
    model.eval()

    all_preds = []
    all_labels = []
    all_logits = []

    for i in range(0, len(val_samples), args.batch_size):
        batch = val_samples[i:i + args.batch_size]
        texts = [build_prompt(s["observation"], s["action_history"]) for s in batch]
        logits = predict_batch(model, tokenizer, texts, args.max_seq_len, device)
        preds = np.argmax(logits, axis=-1)
        labels = np.array([s["label_id"] for s in batch])
        all_preds.extend(preds.tolist())
        all_labels.extend(labels.tolist())
        all_logits.extend(logits.tolist())

    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    acc = accuracy_score(all_labels, all_preds)
    prec, rec, f1, _ = precision_recall_fscore_support(
        all_labels, all_preds, average=None, labels=[0, 1]
    )
    f1_macro = float(np.mean(f1))
    cm = confusion_matrix(all_labels, all_preds, labels=[0, 1]).tolist()

    baselines = compute_baselines(all_labels)

    by_task: Dict[str, Dict[str, list]] = {}
    for i, s in enumerate(val_samples):
        t = s["task_type"]
        if t not in by_task:
            by_task[t] = {"preds": [], "labels": []}
        by_task[t]["preds"].append(all_preds[i])
        by_task[t]["labels"].append(all_labels[i])

    per_task = {}
    for task, data in sorted(by_task.items()):
        task_acc = accuracy_score(data["labels"], data["preds"])
        per_task[task] = {"accuracy": task_acc, "n_samples": len(data["labels"])}

    report = {
        "adapter_dir": args.adapter_dir,
        "data_path": args.data_path,
        "n_eval_samples": len(val_samples),
        "overall_accuracy": acc,
        "f1_macro": f1_macro,
        "per_class": {
            "internal": {"precision": float(prec[0]), "recall": float(rec[0]), "f1": float(f1[0])},
            "deterministic": {"precision": float(prec[1]), "recall": float(rec[1]), "f1": float(f1[1])},
        },
        "confusion_matrix": cm,
        "confusion_labels": ["internal", "deterministic"],
        "baselines": baselines,
        "per_task": per_task,
    }

    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Router accuracy: {acc:.4f}  (majority baseline: {baselines['majority_class']['accuracy']:.4f})")
    print(f"F1 macro: {f1_macro:.4f}")
    print(f"Confusion matrix (rows=true, cols=pred): {['internal', 'deterministic']}")
    for row in cm:
        print(f"  {row}")
    print(f"\nPer-class metrics:")
    for cls in ["internal", "deterministic"]:
        m = report["per_class"][cls]
        print(f"  {cls}: P={m['precision']:.3f} R={m['recall']:.3f} F1={m['f1']:.3f}")
    print(f"\nPer-task accuracy:")
    for task, m in sorted(per_task.items()):
        print(f"  {task}: {m['accuracy']:.3f} (n={m['n_samples']})")
    print(f"\nReport saved to {args.output_path}")


if __name__ == "__main__":
    main()
