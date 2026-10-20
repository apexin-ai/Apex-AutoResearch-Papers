"""Synthetic data generation: sample from a trained model to create next-gen training data."""

import os
import logging

import torch
from datasets import Dataset
from tqdm import tqdm
from transformers import PreTrainedModel, PreTrainedTokenizer

logger = logging.getLogger(__name__)


def generate_synthetic_data(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    num_tokens: int,
    config,
    output_dir: str,
) -> str:
    """Generate synthetic text and save as a HuggingFace Dataset (Arrow).

    Each row has an `input_ids` list of length up to gen_max_new_tokens.
    Returns the output directory path.
    """
    model.eval()
    device = next(model.parameters()).device

    num_seqs = num_tokens // config.gen_max_new_tokens + 1
    num_batches = (num_seqs + config.gen_batch_size - 1) // config.gen_batch_size

    start_id = tokenizer.bos_token_id if tokenizer.bos_token_id is not None else tokenizer.eos_token_id

    all_ids = []
    total_tokens = 0

    logger.info(
        "Generating ~%dM synthetic tokens (%d seqs, %d batches) ...",
        num_tokens // 1_000_000,
        num_seqs,
        num_batches,
    )

    for bi in tqdm(range(num_batches), desc="generate"):
        if total_tokens >= num_tokens:
            break
        bs = min(config.gen_batch_size, num_seqs - bi * config.gen_batch_size)
        prompt = torch.full((bs, 1), start_id, dtype=torch.long, device=device)

        with torch.no_grad():
            out = model.generate(
                input_ids=prompt,
                max_new_tokens=config.gen_max_new_tokens,
                temperature=config.gen_temperature,
                top_p=config.gen_top_p,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )

        for seq in out:
            ids = seq.cpu().tolist()
            all_ids.append(ids)
            total_tokens += len(ids)

        if (bi + 1) % 500 == 0:
            logger.info("  ... %d / %d batches, %.1fM tokens so far", bi + 1, num_batches, total_tokens / 1e6)

    os.makedirs(output_dir, exist_ok=True)
    ds = Dataset.from_dict({"input_ids": all_ids})
    ds.save_to_disk(output_dir)
    logger.info("Saved %d sequences (%.1fM tokens) to %s", len(all_ids), total_tokens / 1e6, output_dir)
    return output_dir


def generate_sample_tokens(
    model: PreTrainedModel,
    tokenizer: PreTrainedTokenizer,
    num_tokens: int,
    batch_size: int = 32,
    max_new_tokens: int = 256,
    temperature: float = 1.0,
    top_p: float = 0.95,
    device: str = "cuda",
) -> list[int]:
    """Generate a small token sample (for n-gram / coverage metrics at checkpoints).

    Returns a flat list of token IDs.
    """
    model.eval()
    start_id = tokenizer.bos_token_id if tokenizer.bos_token_id is not None else tokenizer.eos_token_id

    all_ids: list[int] = []
    num_seqs = num_tokens // max_new_tokens + 1
    num_batches = (num_seqs + batch_size - 1) // batch_size

    for _ in range(num_batches):
        if len(all_ids) >= num_tokens:
            break
        bs = min(batch_size, num_seqs)
        prompt = torch.full((bs, 1), start_id, dtype=torch.long, device=device)
        with torch.no_grad():
            out = model.generate(
                input_ids=prompt,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
            )
        for seq in out:
            all_ids.extend(seq.cpu().tolist())

    return all_ids[:num_tokens]
