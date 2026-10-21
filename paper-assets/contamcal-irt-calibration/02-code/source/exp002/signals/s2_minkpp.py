import logging

import numpy as np
import torch
from tqdm import tqdm

logger = logging.getLogger(__name__)

DEFAULT_K_PERCENT = 20


def _compute_token_logprobs(model, tokenizer, text: str, max_length: int = 2048) -> np.ndarray:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
    input_ids = inputs["input_ids"].to(model.device)

    with torch.no_grad():
        outputs = model(input_ids)
    logits = outputs.logits

    shift_logits = logits[:, :-1, :]
    shift_labels = input_ids[:, 1:]

    log_probs = torch.log_softmax(shift_logits, dim=-1)
    token_log_probs = log_probs.gather(2, shift_labels.unsqueeze(-1)).squeeze(-1)

    return token_log_probs[0].cpu().float().numpy()


def _minkpp_score(target_logprobs: np.ndarray, ref_logprobs: np.ndarray,
                  k_percent: int = DEFAULT_K_PERCENT) -> float:
    n_tokens = min(len(target_logprobs), len(ref_logprobs))
    if n_tokens == 0:
        return 0.0

    target = target_logprobs[:n_tokens]
    ref = ref_logprobs[:n_tokens]

    # z-normalize: surprise_i = (-target_logprob_i - mean(-ref_logprob)) / std(-ref_logprob)
    ref_nll = -ref
    mu = ref_nll.mean()
    sigma = ref_nll.std()
    if sigma < 1e-8:
        sigma = 1.0

    target_nll = -target
    z_scores = (target_nll - mu) / sigma

    k = max(1, int(n_tokens * k_percent / 100))
    topk_indices = np.argpartition(z_scores, -k)[-k:]
    score = float(np.mean(z_scores[topk_indices]))

    return score


def compute(
    benchmark: str,
    model_path: str,
    adapter_path: str = None,
    output_dir: str = None,
    cache_dir: str = None,
    batch_size: int = 8,
    ref_model_path: str = None,
    k_percent: int = DEFAULT_K_PERCENT,
    **kwargs,
) -> list[dict]:
    from utils import (
        load_model_and_tokenizer, load_benchmark_dataset,
        format_benchmark_item, make_item_id, infer_dosage_from_path,
    )

    cache_dir = cache_dir or "/root/autodl-tmp/.hf_cache"

    # Auto-infer reference model (d000 same scale/seed) if not provided
    if ref_model_path is None and adapter_path:
        from pathlib import Path
        ckpt_dir = Path(adapter_path).parent
        if "lora_adapter" in adapter_path:
            ckpt_dir = ckpt_dir.parent
        ckpt_parent = ckpt_dir.parent
        ckpt_name = ckpt_dir.name
        parts = ckpt_name.split("_")
        ref_parts = []
        for p in parts:
            if p.startswith("d") and p[1:].isdigit():
                ref_parts.append("d000")
            else:
                ref_parts.append(p)
        ref_name = "_".join(ref_parts)
        ref_adapter = ckpt_parent / ref_name / "lora_adapter"
        if ref_adapter.exists():
            ref_model_path = str(ref_adapter)
            logger.info("Auto-inferred reference model: %s", ref_model_path)

    ds = load_benchmark_dataset(benchmark, cache_dir)

    # Compute target model log-probs
    logger.info("Loading target model")
    target_model, target_tok = load_model_and_tokenizer(model_path, adapter_path, cache_dir)

    logger.info("Computing target model log-probs (%d items)", len(ds))
    target_item_logprobs = []
    item_texts = []
    for row in tqdm(ds, desc="Target log-probs"):
        text = format_benchmark_item(row, benchmark)
        item_texts.append(text)
        lp = _compute_token_logprobs(target_model, target_tok, text)
        target_item_logprobs.append(lp)

    del target_model
    torch.cuda.empty_cache()

    # Compute reference model log-probs
    if ref_model_path:
        # Determine if ref_model_path is an adapter or a base model
        import os
        ref_adapter = None
        if os.path.exists(os.path.join(ref_model_path, "adapter_config.json")):
            ref_adapter = ref_model_path
            ref_base = model_path  # same base model
        else:
            ref_base = ref_model_path

        logger.info("Loading reference model: %s (adapter: %s)", ref_base, ref_adapter)
        ref_model, ref_tok = load_model_and_tokenizer(ref_base, ref_adapter, cache_dir)
    else:
        logger.info("No reference model; using base model %s as reference", model_path)
        ref_model, ref_tok = load_model_and_tokenizer(model_path, None, cache_dir)

    logger.info("Computing reference model log-probs (%d items)", len(ds))
    ref_item_logprobs = []
    for text in tqdm(item_texts, desc="Reference log-probs"):
        lp = _compute_token_logprobs(ref_model, ref_tok, text)
        ref_item_logprobs.append(lp)

    del ref_model
    torch.cuda.empty_cache()

    results = []
    for i in range(len(ds)):
        score = _minkpp_score(target_item_logprobs[i], ref_item_logprobs[i], k_percent)
        results.append({
            "item_id": make_item_id(benchmark, i),
            "signal": "s2_minkpp",
            "score": -score,  # negate: lower Min-K%++ -> more contaminated -> higher score
            "metadata": {
                "raw_score": score,
                "n_tokens": len(target_item_logprobs[i]),
                "k_percent": k_percent,
            },
        })

    return results
