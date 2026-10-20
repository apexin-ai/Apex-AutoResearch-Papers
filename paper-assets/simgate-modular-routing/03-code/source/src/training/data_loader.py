# Data loading and splitting for Router SFT training.
# Input: labeled_steps.jsonl from plan-001b counterfactual labeling (results/plan_c/{task}/).
# Each line: {task_type, episode_id, variation, step_idx, observation, action, action_history, label, ...}
# Labels: "det-preferred" → deterministic, "internal-preferred" → internal, "no-preference" → dropped.

import glob
import json
import os
import random
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

import torch
from torch.utils.data import Dataset

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


def summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:
    recent = action_history[-max_actions:] if action_history else []
    if not recent:
        return "(none)"
    return " → ".join(recent)


def build_prompt(task_type: str, observation: str, action_history: List[str]) -> str:
    history_summary = summarize_action_history(action_history)
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Task: {task_type}\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )


def _parse_record(record: Dict, fallback_task_type: str = "unknown") -> Optional[Dict]:
    raw_label = record.get("label", "")
    label = RAW_LABEL_MAP.get(raw_label)
    if label is None:
        return None
    return {
        "observation": record.get("observation", ""),
        "action_history": record.get("action_history", []),
        "label": label,
        "label_id": LABEL2ID[label],
        "task_type": record.get("task_type", record.get("task_name", fallback_task_type)),
        "episode_id": record.get("episode_id", record.get("episode", -1)),
        "variation": record.get("variation", record.get("variation_idx", 0)),
        "signal_source": record.get("signal_source", ""),
    }


def load_labeled_data(
    data_path: Optional[str] = None,
    data_dir: Optional[str] = None,
    max_samples: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """Load labeled step data from JSONL files.

    Args:
        data_path: Single JSONL file (e.g. sft_triples.jsonl).
        data_dir: Directory with {task_type}/labeled_steps.jsonl subdirs.
        max_samples: If set, randomly subsample to this many examples.
    """
    files: List[str] = []

    if data_path:
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Data file not found: {data_path}")
        files = [data_path]
    elif data_dir:
        pattern = os.path.join(data_dir, "*", "labeled_steps.jsonl")
        files = sorted(glob.glob(pattern))
        if not files:
            pattern_flat = os.path.join(data_dir, "labeled_steps.jsonl")
            if os.path.exists(pattern_flat):
                files = [pattern_flat]
        if not files:
            raise FileNotFoundError(f"No labeled_steps.jsonl found in {data_dir}")
    else:
        raise ValueError("Must specify --data_path or --data_dir")

    samples = []
    skipped = Counter()
    for fpath in files:
        fallback_task = os.path.basename(os.path.dirname(fpath))
        with open(fpath) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                record = json.loads(line)
                parsed = _parse_record(record, fallback_task)
                if parsed is None:
                    skipped[record.get("label", "?")] += 1
                    continue
                samples.append(parsed)

    if max_samples and len(samples) > max_samples:
        random.shuffle(samples)
        samples = samples[:max_samples]

    print(f"Loaded {len(samples)} samples from {len(files)} file(s)")
    if skipped:
        print(f"  Skipped labels: {dict(skipped)}")
    label_dist = Counter(s["label"] for s in samples)
    for k, v in sorted(label_dist.items()):
        print(f"  {k}: {v} ({v / len(samples) * 100:.1f}%)")
    return samples


def stratified_split(
    samples: List[Dict], eval_ratio: float, seed: int
) -> Tuple[List[Dict], List[Dict]]:
    """80/20 stratified split by task_type (no episode leakage across split)."""
    rng = random.Random(seed)

    episodes: Dict[tuple, List[Dict]] = {}
    for s in samples:
        key = (s["task_type"], s["episode_id"], s["variation"])
        episodes.setdefault(key, []).append(s)

    by_task: Dict[str, List[tuple]] = {}
    for key in episodes:
        by_task.setdefault(key[0], []).append(key)

    train_set, val_set = [], []
    for task, ep_keys in sorted(by_task.items()):
        rng.shuffle(ep_keys)
        n_val = max(1, int(len(ep_keys) * eval_ratio))
        for k in ep_keys[:n_val]:
            val_set.extend(episodes[k])
        for k in ep_keys[n_val:]:
            train_set.extend(episodes[k])

    rng.shuffle(train_set)
    rng.shuffle(val_set)
    print(f"Stratified split: train={len(train_set)}, val={len(val_set)}")
    return train_set, val_set


def leave_one_out_splits(
    samples: List[Dict],
) -> List[Tuple[str, List[Dict], List[Dict]]]:
    """Leave-one-task-out cross-validation splits.

    Returns list of (held_out_task, train_samples, val_samples).
    """
    by_task: Dict[str, List[Dict]] = {}
    for s in samples:
        by_task.setdefault(s["task_type"], []).append(s)

    task_types = sorted(by_task.keys())
    splits = []
    for held_out in task_types:
        val = by_task[held_out]
        train = []
        for t in task_types:
            if t != held_out:
                train.extend(by_task[t])
        if not val or not train:
            continue
        splits.append((held_out, train, val))
        print(f"  LOO fold: hold out {held_out} -> train={len(train)}, val={len(val)}")
    return splits


class RouterDataset(Dataset):
    def __init__(self, samples: List[Dict], tokenizer, max_length: int):
        self.samples = samples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        s = self.samples[idx]
        prompt = build_prompt(s["task_type"], s["observation"], s["action_history"])
        encoding = self.tokenizer(
            prompt,
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(s["label_id"], dtype=torch.long),
        }
