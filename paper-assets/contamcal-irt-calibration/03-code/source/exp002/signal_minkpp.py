"""
Signal 2: Min-K%++ membership inference.

Computes Min-K%++ scores (Shi et al., ICLR 2025) for each benchmark item.
Uses a reference model (clean/base, e.g. 0% dosage) for per-token log-prob differencing.

Input:  Target model, reference model, benchmark items
Output: JSON with per-item Min-K%++ scores
"""

import argparse
import json
import logging
import os
from pathlib import Path

import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

DEFAULT_K_PERCENT = 20


def _resolve_adapter_path(adapter_path: str) -> str:
    """Resolve adapter path: check for lora_adapter/ subdirectory."""
    if adapter_path is None:
        return None
    p = Path(adapter_path)
    if (p / "adapter_config.json").exists():
        return str(p)
    lora_sub = p / "lora_adapter"
    if (lora_sub / "adapter_config.json").exists():
        return str(lora_sub)
    return str(p)


def load_model_and_tokenizer(model_path: str, cache_dir: str, adapter_path: str = None):
    adapter_path = _resolve_adapter_path(adapter_path)

    logger.info("Loading model: %s", model_path)
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, cache_dir=cache_dir, trust_remote_code=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_path, cache_dir=cache_dir,
        torch_dtype=torch.bfloat16, trust_remote_code=True,
        device_map="auto",
    )
    if adapter_path:
        from peft import PeftModel
        logger.info("Loading LoRA adapter from %s", adapter_path)
        model = PeftModel.from_pretrained(model, adapter_path)
        model = model.merge_and_unload()
        logger.info("LoRA adapter merged into base model")
    model.eval()
    return model, tokenizer


def format_benchmark_item(row: dict, benchmark: str) -> str:
    """Format a benchmark item into a text string for log-prob computation."""
    if benchmark == "mmlu":
        choices = "\n".join(f"{chr(65+i)}) {c}" for i, c in enumerate(row["choices"]))
        gold = chr(65 + row["answer"])
        return f"Question: {row['question']}\n{choices}\nAnswer: {gold}"
    elif benchmark == "gsm8k":
        return f"Question: {row['question']}\nAnswer: {row['answer']}"
    elif benchmark == "arc_challenge":
        choices = "\n".join(f"{l}) {t}" for l, t in zip(row["choices"]["label"], row["choices"]["text"]))
        return f"Question: {row['question']}\n{choices}\nAnswer: {row['answerKey']}"
    elif benchmark == "humaneval":
        return row["prompt"] + (row.get("canonical_solution", "") or "")
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")


def compute_token_logprobs(model, tokenizer, text: str, max_length: int = 2048) -> np.ndarray:
    """Compute per-token log probabilities for input text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
    input_ids = inputs["input_ids"].to(model.device)

    with torch.no_grad():
        outputs = model(input_ids)
    logits = outputs.logits

    # Shift: predict token t from position t-1
    shift_logits = logits[:, :-1, :]
    shift_labels = input_ids[:, 1:]

    log_probs = torch.log_softmax(shift_logits, dim=-1)
    token_log_probs = log_probs.gather(2, shift_labels.unsqueeze(-1)).squeeze(-1)

    return token_log_probs[0].float().cpu().numpy()


def minkpp_score(target_logprobs: np.ndarray, ref_logprobs: np.ndarray,
                 k_percent: int = DEFAULT_K_PERCENT) -> float:
    """
    Min-K%++ score (Zhang et al., 2024): per-token log-prob difference.

    delta_t = target_logprobs[t] - ref_logprobs[t] for each token position t.
    Score = mean of bottom K% delta values (most suspicious tokens).
    Lower score = more likely memorized.
    """
    n = min(len(target_logprobs), len(ref_logprobs))
    if n == 0:
        return 0.0
    delta = target_logprobs[:n] - ref_logprobs[:n]
    k = max(1, int(n * k_percent / 100))
    bottom_k = np.sort(delta)[:k]
    return float(np.mean(bottom_k))


def minkpp_zscore_score(target_logprobs: np.ndarray, ref_logprobs: np.ndarray,
                       k_percent: int = DEFAULT_K_PERCENT) -> float:
    """Ablation variant: z-score normalization instead of per-token difference."""
    n_tokens = min(len(target_logprobs), len(ref_logprobs))
    if n_tokens == 0:
        return 0.0
    delta = target_logprobs[:n_tokens] - ref_logprobs[:n_tokens]
    mu = np.mean(delta)
    sigma = np.std(delta)
    if sigma < 1e-8:
        return 0.0
    z_scores = (delta - mu) / sigma
    k = max(1, int(n_tokens * k_percent / 100))
    bottom_k = np.sort(z_scores)[:k]
    return float(np.mean(bottom_k))


def compute_minkpp_signal(
    benchmark: str,
    target_model_path: str,
    ref_model_path: str,
    cache_dir: str,
    adapter_path: str = None,
    ref_adapter_path: str = None,
    k_percent: int = DEFAULT_K_PERCENT,
    max_length: int = 2048,
    max_items: int = None,
) -> list[dict]:
    """Compute Min-K%++ scores for all items in a benchmark."""
    from datasets import load_dataset

    if benchmark == "mmlu":
        ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)
    elif benchmark == "gsm8k":
        ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=cache_dir)
    elif benchmark == "arc_challenge":
        ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=cache_dir)
    elif benchmark == "humaneval":
        ds = load_dataset("openai/openai_humaneval", "openai_humaneval", split="test", cache_dir=cache_dir)
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")

    if max_items:
        ds = ds.select(range(min(max_items, len(ds))))

    # Load target model (with LoRA adapter if provided)
    target_model, target_tok = load_model_and_tokenizer(target_model_path, cache_dir, adapter_path=adapter_path)

    # Compute target log-probs for all items
    logger.info("Computing target model log-probs (%d items)", len(ds))
    target_item_logprobs = []
    item_texts = []
    for row in tqdm(ds, desc="Target log-probs"):
        text = format_benchmark_item(row, benchmark)
        item_texts.append(text)
        lp = compute_token_logprobs(target_model, target_tok, text, max_length)
        target_item_logprobs.append(lp)

    # Free target model memory
    del target_model
    torch.cuda.empty_cache()

    # Load reference model (with LoRA adapter if provided)
    ref_model, ref_tok = load_model_and_tokenizer(ref_model_path, cache_dir, adapter_path=ref_adapter_path)

    # Compute reference log-probs
    logger.info("Computing reference model log-probs (%d items)", len(ds))
    ref_item_logprobs = []
    for text in tqdm(item_texts, desc="Reference log-probs"):
        lp = compute_token_logprobs(ref_model, ref_tok, text, max_length)
        ref_item_logprobs.append(lp)

    del ref_model
    torch.cuda.empty_cache()

    # Compute Min-K%++ scores
    results = []
    for i in range(len(ds)):
        score = minkpp_score(target_item_logprobs[i], ref_item_logprobs[i], k_percent)
        # Negate: lower Min-K%++ → more likely member → higher contamination suspicion
        results.append({
            "index": i,
            "benchmark": benchmark,
            "s2_minkpp": -score,
            "s2_minkpp_raw": score,
            "n_tokens": len(target_item_logprobs[i]),
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Signal 2: Min-K%++ membership inference")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--model-path", type=str, required=True,
                        help="Target (potentially contaminated) model path")
    parser.add_argument("--ref-model-path", type=str, required=True,
                        help="Reference (clean) model path, e.g. 0%%%% dosage checkpoint")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter directory for target model")
    parser.add_argument("--ref-adapter-path", type=str, default=None,
                        help="Path to LoRA adapter directory for reference model")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--k-percent", type=int, default=DEFAULT_K_PERCENT,
                        help="K%%%% for Min-K%%%% selection (default: 20)")
    parser.add_argument("--max-length", type=int, default=2048)
    parser.add_argument("--gpu", type=str, default=None)
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = compute_minkpp_signal(
        benchmark=args.benchmark,
        target_model_path=args.model_path,
        ref_model_path=args.ref_model_path,
        cache_dir=args.cache_dir,
        adapter_path=args.adapter_path,
        ref_adapter_path=args.ref_adapter_path,
        k_percent=args.k_percent,
        max_length=args.max_length,
    )

    out_file = output_dir / f"signal_minkpp_{args.benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()
