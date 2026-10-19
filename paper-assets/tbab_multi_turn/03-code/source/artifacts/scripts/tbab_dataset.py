"""
Dataset and DataCollator for TBAB multi-turn training.

TBABDataset: loads training_data.json, tokenizes with Mistral chat template,
inserts bridge tokens, builds position_ids, labels, and 4D attention mask.

TBABDataCollator: pads variable-length samples to batch max, constructs
batched tensors with proper padding for input_ids, labels, position_ids,
and attention_mask (2D or 4D).

Input: training_data.json with format [{"messages": [...], "source": "..."}]
Output: batched dict ready for model.forward()
"""

import json
import torch
from torch.utils.data import Dataset
from typing import List, Dict, Any

from tbab_utils import (
    find_turn_boundaries,
    insert_bridge_tokens,
    build_position_ids,
    build_4d_causal_mask,
    build_labels,
)


class TBABDataset(Dataset):
    def __init__(
        self,
        data_path: str,
        tokenizer,
        max_seq_length: int = 4096,
        use_bridge_tokens: bool = False,
        use_position_reset: bool = False,
        bridge_token_ids: List[int] = None,
        num_bridge_tokens: int = 4,
    ):
        with open(data_path) as f:
            self.raw_data = json.load(f)

        self.tokenizer = tokenizer
        self.max_seq_length = max_seq_length
        self.use_bridge_tokens = use_bridge_tokens
        self.use_position_reset = use_position_reset
        self.bridge_token_ids = bridge_token_ids or []
        self.num_bridge_tokens = num_bridge_tokens

        self.eos_token_id = tokenizer.eos_token_id

        end_inst_encoded = tokenizer.encode("[/INST]", add_special_tokens=False)
        self.end_inst_token_ids = end_inst_encoded

    def __len__(self):
        return len(self.raw_data)

    def __getitem__(self, idx) -> Dict[str, Any]:
        item = self.raw_data[idx]
        messages = item["messages"]

        result = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=False,
        )
        input_ids = result["input_ids"] if hasattr(result, "keys") else result

        turn_boundaries = find_turn_boundaries(
            input_ids, self.eos_token_id, inst_token_ids=[]
        )

        labels = build_labels(
            input_ids, turn_boundaries, self.end_inst_token_ids, num_bridge=0
        )

        if self.use_bridge_tokens and len(self.bridge_token_ids) > 0:
            input_ids, labels, turn_boundaries = insert_bridge_tokens(
                input_ids, labels, turn_boundaries, self.bridge_token_ids
            )

        num_bridge = self.num_bridge_tokens if self.use_bridge_tokens else 0
        position_ids = build_position_ids(
            len(input_ids), turn_boundaries, self.use_position_reset, num_bridge
        )

        if len(input_ids) > self.max_seq_length:
            input_ids = input_ids[:self.max_seq_length]
            labels = labels[:self.max_seq_length]
            position_ids = position_ids[:self.max_seq_length]

        needs_4d_mask = self.use_position_reset

        return {
            "input_ids": input_ids,
            "labels": labels,
            "position_ids": position_ids,
            "needs_4d_mask": needs_4d_mask,
            "seq_len": len(input_ids),
        }


class TBABDataCollator:
    def __init__(self, tokenizer, use_position_reset: bool = False):
        self.pad_token_id = tokenizer.pad_token_id
        self.use_position_reset = use_position_reset

    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, torch.Tensor]:
        max_len = max(f["seq_len"] for f in features)
        batch_size = len(features)

        input_ids = torch.full((batch_size, max_len), self.pad_token_id, dtype=torch.long)
        labels = torch.full((batch_size, max_len), -100, dtype=torch.long)
        position_ids = torch.zeros((batch_size, max_len), dtype=torch.long)
        attention_mask_2d = torch.zeros((batch_size, max_len), dtype=torch.long)

        for i, f in enumerate(features):
            seq_len = f["seq_len"]
            input_ids[i, :seq_len] = torch.tensor(f["input_ids"], dtype=torch.long)
            labels[i, :seq_len] = torch.tensor(f["labels"], dtype=torch.long)
            position_ids[i, :seq_len] = torch.tensor(f["position_ids"], dtype=torch.long)
            attention_mask_2d[i, :seq_len] = 1

        batch = {
            "input_ids": input_ids,
            "labels": labels,
            "position_ids": position_ids,
        }

        if self.use_position_reset:
            mask_4d = torch.zeros(
                (batch_size, 1, max_len, max_len), dtype=torch.bfloat16
            )
            min_val = torch.finfo(torch.bfloat16).min
            for i, f in enumerate(features):
                seq_len = f["seq_len"]
                causal = build_4d_causal_mask(seq_len, dtype=torch.bfloat16)
                mask_4d[i, :, :seq_len, :seq_len] = causal
                mask_4d[i, :, :seq_len, seq_len:] = min_val
                mask_4d[i, :, seq_len:, :] = min_val
            batch["attention_mask"] = mask_4d
        else:
            batch["attention_mask"] = attention_mask_2d

        return batch
