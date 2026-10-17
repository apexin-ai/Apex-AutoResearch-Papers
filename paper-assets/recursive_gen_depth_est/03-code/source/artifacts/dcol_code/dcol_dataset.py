"""Dataset and collate for DCOL depth classification.

Input:  directory with depth_0.jsonl .. depth_3.jsonl (each line: {"text": "..."})
Output: PyTorch Dataset yielding (text, depth_label); collate tokenizes + pads.

Dependencies: torch, transformers
"""

import json
from pathlib import Path
from typing import List, Tuple

import torch
from torch.utils.data import Dataset
from transformers import PreTrainedTokenizerBase


class DepthDataset(Dataset):
    def __init__(self, data_dir: str, depths: List[int] = None):
        """Load depth_X.jsonl files from data_dir."""
        self.samples: List[Tuple[str, int]] = []
        depths = depths or list(range(4))
        data_dir = Path(data_dir)
        for d in depths:
            path = data_dir / f"depth_{d}.jsonl"
            if not path.exists():
                continue
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    obj = json.loads(line)
                    self.samples.append((obj["text"], d))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]


class DepthCollator:
    def __init__(self, tokenizer: PreTrainedTokenizerBase, max_length: int = 512):
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __call__(self, batch: List[Tuple[str, int]]):
        texts, labels = zip(*batch)
        enc = self.tokenizer(
            list(texts),
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )
        enc["labels"] = torch.tensor(labels, dtype=torch.long)
        return enc
