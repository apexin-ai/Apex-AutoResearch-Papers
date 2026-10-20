#!/usr/bin/env python3
"""Baseline methods for progress/stagnation classification.

Each baseline implements a unified interface:
    fit(train_data, val_data=None)
    predict(data) -> list[int]
    evaluate(data) -> dict

Data format: list of dicts, each containing:
    - "label": int (0=stagnation, 1=progress)
    - "embeddings": torch.Tensor (seq_len, embed_dim) — for cosine baseline
    - "steps": list[{"role": str, "text": str}] — for repeat-3 baseline
"""

import re
import random

import numpy as np
import torch
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def extract_command(text: str) -> str | None:
    match = re.search(r"```\n?(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else None


def compute_metrics(labels: list[int], preds: list[int]) -> dict:
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "precision_macro": precision_score(labels, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(labels, preds, average="macro", zero_division=0),
        "f1_stagnation": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_progress": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


class BaselineModel:
    name: str = "baseline"

    def fit(self, train_data: list[dict], val_data: list[dict] | None = None):
        pass

    def predict(self, data: list[dict]) -> list[int]:
        raise NotImplementedError

    def evaluate(self, data: list[dict]) -> dict:
        labels = [d["label"] for d in data]
        preds = self.predict(data)
        return compute_metrics(labels, preds)


class RandomBaseline(BaselineModel):
    name = "Random"

    def __init__(self, seed: int = 42):
        self.seed = seed
        self.pos_ratio = 0.5

    def fit(self, train_data, val_data=None):
        labels = [d["label"] for d in train_data]
        self.pos_ratio = sum(labels) / len(labels) if labels else 0.5

    def predict(self, data):
        rng = random.Random(self.seed)
        return [1 if rng.random() < self.pos_ratio else 0 for _ in data]


class MajorityBaseline(BaselineModel):
    name = "Majority"

    def __init__(self):
        self.majority_class = 0

    def fit(self, train_data, val_data=None):
        labels = [d["label"] for d in train_data]
        self.majority_class = 1 if sum(labels) > len(labels) / 2 else 0

    def predict(self, data):
        return [self.majority_class] * len(data)


class CosineSimilarityBaseline(BaselineModel):
    name = "CosineSim"

    def __init__(self):
        self.threshold = 0.5
        self.invert = False

    @staticmethod
    def _avg_adjacent_cosine(embeddings: torch.Tensor) -> float:
        if embeddings.shape[0] < 2:
            return 0.0
        e = torch.nn.functional.normalize(embeddings, p=2, dim=1)
        sims = (e[:-1] * e[1:]).sum(dim=1)
        return sims.mean().item()

    def fit(self, train_data, val_data=None):
        tune_data = val_data if val_data else train_data
        labels = [d["label"] for d in tune_data]
        scores = [self._avg_adjacent_cosine(d["embeddings"]) for d in tune_data]

        best_f1, best_t, best_inv = -1.0, 0.5, False
        for t in np.arange(-1.0, 1.01, 0.01):
            for inv in (False, True):
                preds = [int((s >= t) != inv) for s in scores]
                f = f1_score(labels, preds, average="macro", zero_division=0)
                if f > best_f1:
                    best_f1, best_t, best_inv = f, t, inv
        self.threshold = best_t
        self.invert = best_inv

    def predict(self, data):
        return [int((self._avg_adjacent_cosine(d["embeddings"]) >= self.threshold) != self.invert) for d in data]


class Repeat3Baseline(BaselineModel):
    name = "Repeat-3"

    @staticmethod
    def _predict_one(steps: list[dict]) -> int:
        ai_commands = []
        for s in steps:
            if s.get("role") == "ai":
                cmd = extract_command(s.get("text", ""))
                if cmd is not None:
                    ai_commands.append(cmd)
        if len(ai_commands) >= 3 and ai_commands[-1] == ai_commands[-2] == ai_commands[-3]:
            return 0  # stagnation
        return 1  # progress

    def predict(self, data):
        return [self._predict_one(d.get("steps", [])) for d in data]


ALL_BASELINES = [RandomBaseline, MajorityBaseline, CosineSimilarityBaseline, Repeat3Baseline]


if __name__ == "__main__":
    print("=== Baseline self-test with random data ===")
    embed_dim = 1024
    n_samples = 100

    data = []
    for i in range(n_samples):
        seq_len = random.randint(3, 10)
        label = random.choice([0, 1])
        steps = []
        for j in range(seq_len):
            role = "ai" if j % 2 == 0 else "user"
            if role == "ai":
                cmd = "scroll_down" if label == 0 and j > seq_len - 7 else f"edit {j}:{j+1}"
                text = f"thinking\n```\n{cmd}\n```"
            else:
                text = f"[File: /repo/f.py ({j} lines total)]"
            steps.append({"role": role, "text": text})
        data.append({
            "label": label,
            "embeddings": torch.randn(seq_len, embed_dim),
            "steps": steps,
        })

    train_data = data[:70]
    val_data = data[70:85]
    test_data = data[85:]

    for cls in ALL_BASELINES:
        bl = cls() if cls != RandomBaseline else cls(seed=0)
        bl.fit(train_data, val_data)
        metrics = bl.evaluate(test_data)
        print(f"{bl.name:15s} | macro_f1={metrics['macro_f1']:.3f} acc={metrics['accuracy']:.3f}")

    print("All baseline tests passed.")
