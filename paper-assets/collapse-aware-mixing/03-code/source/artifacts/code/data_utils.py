"""Data loading, tokenization, and preprocessing for pilot experiments."""

import os
import logging
import random
from typing import Tuple, List, Optional
from itertools import chain

import torch
from torch.utils.data import Dataset as TorchDataset, DataLoader
from datasets import load_dataset, Dataset, load_from_disk
from transformers import PreTrainedTokenizer

logger = logging.getLogger(__name__)


class PackedDataset(TorchDataset):
    """Pre-tokenized, fixed-length sequences for causal LM training."""

    def __init__(self, input_ids: List[List[int]]):
        self.input_ids = input_ids

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)
        return {"input_ids": ids, "attention_mask": torch.ones_like(ids), "labels": ids.clone()}


def prepare_real_data(
    config, tokenizer: PreTrainedTokenizer
) -> Tuple[PackedDataset, PackedDataset]:
    """Load real data, tokenize, pack, split into train/holdout."""
    cache_path = os.path.join(config.output_dir, "real_data_cache")

    if os.path.exists(cache_path):
        logger.info("Loading cached tokenized data from %s", cache_path)
        ds = load_from_disk(cache_path)
    else:
        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1
        num_total_seqs = num_train_seqs + config.holdout_size + 2000

        dataset_config = getattr(config, "real_dataset_config", None)
        logger.info("Loading from %s (config=%s) ...", config.real_dataset, dataset_config)
        raw = load_dataset(
            config.real_dataset,
            dataset_config,
            split="train",
        )

        logger.info("Tokenizing ...")
        tokenized = raw.map(
            lambda ex: tokenizer(ex["text"], truncation=False, add_special_tokens=False),
            batched=True,
            remove_columns=raw.column_names,
            num_proc=4,
            desc="Tokenizing",
        )

        logger.info("Packing into %d-token sequences ...", config.max_seq_length)

        def pack_fn(examples):
            flat = list(chain(*examples["input_ids"]))
            n = (len(flat) // config.max_seq_length) * config.max_seq_length
            return {
                "input_ids": [
                    flat[i : i + config.max_seq_length]
                    for i in range(0, n, config.max_seq_length)
                ]
            }

        ds = tokenized.map(
            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1
        )

        os.makedirs(cache_path, exist_ok=True)
        ds.save_to_disk(cache_path)
        logger.info("Cached %d packed sequences to %s", len(ds), cache_path)

    num_train = config.tokens_per_generation // config.max_seq_length
    available = len(ds) - config.holdout_size
    if num_train > available:
        logger.warning(
            "Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.",
            num_train, available, len(ds), config.holdout_size,
        )
        num_train = available
    num_holdout = min(config.holdout_size, len(ds) - num_train)

    train_ids = ds.select(range(num_train))["input_ids"]
    holdout_ids = ds.select(range(num_train, num_train + num_holdout))["input_ids"]

    logger.info(
        "Train: %d seqs (%.1fM tokens) | Holdout: %d seqs",
        len(train_ids),
        len(train_ids) * config.max_seq_length / 1e6,
        len(holdout_ids),
    )
    return PackedDataset(train_ids), PackedDataset(holdout_ids)


def prepare_synthetic_data(
    data_path: str, config, tokenizer: PreTrainedTokenizer
) -> PackedDataset:
    """Load generated synthetic data and wrap as PackedDataset."""
    logger.info("Loading synthetic data from %s", data_path)
    ds = load_from_disk(data_path)
    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)

    input_ids = []
    for i in range(num_seqs):
        seq = ds[i]["input_ids"]
        if len(seq) >= config.max_seq_length:
            input_ids.append(seq[: config.max_seq_length])
        else:
            # pad short sequences with eos_token_id
            pad_id = tokenizer.eos_token_id or 0
            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))

    logger.info("Loaded %d synthetic sequences", len(input_ids))
    return PackedDataset(input_ids)


def extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:
    """Flatten all sequences into a single token-id list for corpus-level metrics."""
    ids: List[int] = []
    for i in range(len(dataset)):
        ids.extend(dataset.input_ids[i])
        if max_tokens and len(ids) >= max_tokens:
            return ids[:max_tokens]
    return ids


def mix_datasets(
    real_dataset: PackedDataset,
    synth_dataset: PackedDataset,
    ratio: float,
    seed: int = 42,
) -> PackedDataset:
    """Mix real and synthetic data by ratio.

    Args:
        real_dataset: PackedDataset of real (human) sequences.
        synth_dataset: PackedDataset of synthetic (model-generated) sequences.
        ratio: Fraction of real data in the mix. 1.0 = pure real, 0.0 = pure synthetic.
        seed: Random seed for reproducible sampling and shuffling.

    Returns:
        A new PackedDataset with ratio * N real sequences and (1 - ratio) * N synthetic sequences,
        where N = min(len(real), len(synth)) to keep total dataset size consistent.
    """
    total = min(len(real_dataset), len(synth_dataset))
    n_real = int(ratio * total)
    n_synth = total - n_real

    rng = random.Random(seed)
    real_indices = rng.sample(range(len(real_dataset)), min(n_real, len(real_dataset)))
    synth_indices = rng.sample(range(len(synth_dataset)), min(n_synth, len(synth_dataset)))

    mixed = [real_dataset.input_ids[i] for i in real_indices] + \
            [synth_dataset.input_ids[i] for i in synth_indices]
    rng.shuffle(mixed)

    logger.info(
        "Mixed dataset: %d real + %d synth = %d total (ratio=%.2f)",
        len(real_indices), len(synth_indices), len(mixed), ratio,
    )
    return PackedDataset(mixed)


def make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)
