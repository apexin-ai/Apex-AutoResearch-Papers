"""Data loading and splitting for Router SFT training.

Input: labeled_steps.jsonl from counterfactual labeling.
Each line: {task_type, episode_id, variation, step_idx, observation, action, action_history, label, ...}
Labels: "det-preferred" -> deterministic, "internal-preferred" -> internal, "no-preference" -> dropped.
"""

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
    return " -> ".join(recent)


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
    """Load labeled step data from JSONL files."""
    files: List[str] = []

    if data_path and os.path.exists(data_path):
        files.append(data_path)
    elif data_dir and os.path.isdir(data_dir):
        files = sorted(glob.glob(os.path.join(data_dir, "*/labeled_steps.jsonl")))
        if not files:
            files = sorted(glob.glob(os.path.join(data_dir, "*.jsonl")))

    records = []
    for fp in files:
        task_type = os.path.basename(os.path.dirname(fp))
        with open(fp) as f:
            for line in f:
                if not line.strip():
                    continue
                raw = json.loads(line)
                parsed = _parse_record(raw, fallback_task_type=task_type)
                if parsed is not None:
                    records.append(parsed)

    if max_samples and len(records) > max_samples:
        random.shuffle(records)
        records = records[:max_samples]

    return records


def stratified_split(data: List[Dict], eval_ratio: float = 0.2,
                     seed: int = 42) -> Tuple[List[Dict], List[Dict]]:
    """Stratified train/eval split by task_type and label."""
    rng = random.Random(seed)
    groups = {}
    for d in data:
        key = (d["task_type"], d["label"])
        groups.setdefault(key, []).append(d)

    train, val = [], []
    for key, items in groups.items():
        rng.shuffle(items)
        n_val = max(1, int(len(items) * eval_ratio))
        val.extend(items[:n_val])
        train.extend(items[n_val:])

    return train, val


def leave_one_out_splits(data: List[Dict]) -> List[Tuple[str, List[Dict], List[Dict]]]:
    """Leave-one-task-out splits."""
    tasks = sorted(set(d["task_type"] for d in data))
    splits = []
    for held_out in tasks:
        train = [d for d in data if d["task_type"] != held_out]
        test = [d for d in data if d["task_type"] == held_out]
        splits.append((held_out, train, test))
    return splits


class RouterDataset(Dataset):
    def __init__(self, data: List[Dict], tokenizer, max_seq_len: int = 2048):
        self.data = data
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        prompt = build_prompt(item["task_type"], item["observation"], item["action_history"])
        encoding = self.tokenizer(
            prompt,
            max_length=self.max_seq_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )
        return {
            "input_ids": encoding["input_ids"].squeeze(),
            "attention_mask": encoding["attention_mask"].squeeze(),
            "labels": torch.tensor(item["label_id"], dtype=torch.long),
        }
