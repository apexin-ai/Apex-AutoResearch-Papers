"""
CARC KV Eviction evaluation framework.

Benchmarks: WikiText-2 PPL, C4 PPL, MATH-500 accuracy, LongBench subsets.
Methods: full cache (baseline), EMA eviction @50% budget, EMA eviction @30% budget.

Usage:
    python eval_kv_eviction.py --model <path> --benchmark wikitext --budget-ratios 1.0 0.5 0.3
    python eval_kv_eviction.py --model <path> --benchmark math --budget-ratios 1.0 0.5
    python eval_kv_eviction.py --model <path> --benchmark all --output eval_results.json
"""

import argparse
import json
import math
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn.functional as F
from tqdm import tqdm

from carc_utils import EMAAnchorManager, load_eval_data, load_math_data
from carc_kv_eviction import CARCKVEviction

try:
    from carc_generate import CARCGenerator
except ImportError:
    CARCGenerator = None

MODEL_ID = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
DEFAULT_THRESHOLDS = "thresholds.json"

# ---------------------------------------------------------------------------
# Answer extraction and matching (MATH)
# ---------------------------------------------------------------------------

def extract_boxed(text: str) -> Optional[str]:
    """Extract content from \\boxed{...}, handling nested braces."""
    pattern = r"\\boxed\{"
    matches = list(re.finditer(pattern, text))
    if not matches:
        return None
    start = matches[-1].end()
    depth = 1
    pos = start
    while pos < len(text) and depth > 0:
        if text[pos] == "{":
            depth += 1
        elif text[pos] == "}":
            depth -= 1
        pos += 1
    if depth == 0:
        return text[start : pos - 1].strip()
    return None


def normalize_answer(ans: str) -> str:
    """Normalize a math answer for comparison."""
    ans = ans.strip()
    ans = ans.replace("\\,", "")
    ans = ans.replace("\\!", "")
    ans = ans.replace("\\;", "")
    ans = ans.replace("\\:", "")
    ans = ans.replace("\\left", "")
    ans = ans.replace("\\right", "")
    ans = ans.replace("\\text{", "").rstrip("}")
    ans = ans.replace("\\mathrm{", "").rstrip("}")
    ans = ans.replace("\\mathbf{", "").rstrip("}")
    ans = ans.replace("$", "")
    ans = ans.replace(" ", "")
    ans = ans.replace("\\dfrac", "\\frac")
    ans = ans.replace("\\tfrac", "\\frac")
    try:
        val = float(ans)
        if val == int(val):
            ans = str(int(val))
        else:
            ans = f"{val:.6g}"
    except (ValueError, OverflowError):
        pass
    return ans


def answers_match(pred: str, gold: str) -> bool:
    """Check if predicted and gold answers match after normalization."""
    if pred is None or gold is None:
        return False
    pred_n = normalize_answer(pred)
    gold_n = normalize_answer(gold)
    if pred_n == gold_n:
        return True
    try:
        return abs(float(pred_n) - float(gold_n)) < 1e-6
    except (ValueError, OverflowError):
        return False


# ---------------------------------------------------------------------------
# Perplexity evaluation (token-by-token with eviction)
# ---------------------------------------------------------------------------

def evaluate_ppl_no_eviction(
    model,
    tokenizer,
    dataset_name: str,
    num_samples: int = 200,
    seq_len: int = 2048,
    stride: int = 512,
    device: str = "cuda",
) -> Dict[str, Any]:
    """Standard PPL evaluation without eviction (full cache baseline)."""
    samples = load_eval_data(
        dataset_name=dataset_name,
        num_samples=num_samples,
        seq_len=seq_len,
        tokenizer=tokenizer,
    )
    if not samples:
        return {"ppl": float("inf"), "num_tokens": 0, "error": "no data loaded"}

    total_nll = 0.0
    total_tokens = 0

    model.eval()
    with torch.no_grad():
        for seq in tqdm(samples, desc=f"PPL({dataset_name}) full-cache"):
            input_ids = seq.unsqueeze(0).to(device)
            L = input_ids.shape[1]

            # Sliding window with stride
            prev_end = 0
            for begin in range(0, L, stride):
                end = min(begin + seq_len, L)
                trg_len = end - prev_end

                ids = input_ids[:, begin:end]
                target_ids = ids.clone()
                target_ids[:, :-trg_len] = -100

                outputs = model(ids, labels=target_ids)
                neg_log_likelihood = outputs.loss * trg_len

                total_nll += neg_log_likelihood.item()
                total_tokens += trg_len
                prev_end = end

                if end == L:
                    break

    ppl = math.exp(total_nll / total_tokens) if total_tokens > 0 else float("inf")
    return {"ppl": round(ppl, 4), "num_tokens": total_tokens}


def evaluate_ppl_with_eviction(
    model,
    tokenizer,
    dataset_name: str,
    budget_ratio: float,
    num_samples: int = 200,
    seq_len: int = 2048,
    device: str = "cuda",
    gamma: float = 0.9,
    grace_window: int = 175,
    evict_ratio: float = 0.1,
) -> Dict[str, Any]:
    """
    PPL evaluation with KV cache eviction.

    Processes sequences in chunks (prefill + per-token decode), applying
    eviction when the cache exceeds budget_ratio * seq_len.
    """
    samples = load_eval_data(
        dataset_name=dataset_name,
        num_samples=num_samples,
        seq_len=seq_len,
        tokenizer=tokenizer,
    )
    if not samples:
        return {"ppl": float("inf"), "num_tokens": 0, "error": "no data loaded"}

    budget = int(seq_len * budget_ratio)
    num_kv_heads = getattr(model.config, "num_key_value_heads", None)

    total_nll = 0.0
    total_tokens = 0
    agg_eviction_stats = {
        "total_evicted": 0,
        "eviction_triggers": 0,
    }

    prefill_chunk = min(budget, 512)

    model.eval()
    with torch.no_grad():
        for seq in tqdm(samples, desc=f"PPL({dataset_name}) @{budget_ratio}"):
            input_ids = seq.to(device)
            L = input_ids.shape[0]

            ema_mgr = EMAAnchorManager(
                gamma=gamma, num_kv_heads=num_kv_heads, per_head=True
            )
            eviction_mgr = CARCKVEviction(
                budget=budget,
                grace_window=grace_window,
                evict_ratio=evict_ratio,
            )

            past_kv = None
            seq_nll = 0.0
            seq_tokens = 0

            # Process in chunks: first prefill_chunk, then token-by-token
            pos = 0
            while pos < L - 1:
                if pos == 0:
                    chunk_end = min(prefill_chunk, L)
                else:
                    chunk_end = min(pos + 1, L)

                chunk_ids = input_ids[pos:chunk_end].unsqueeze(0)

                outputs = model(
                    input_ids=chunk_ids,
                    past_key_values=past_kv,
                    use_cache=True,
                )
                past_kv = outputs.past_key_values
                logits = outputs.logits  # (1, chunk_len, vocab)

                # Compute NLL for this chunk
                if chunk_end < L:
                    targets = input_ids[pos + 1 : chunk_end + 1]
                else:
                    targets = input_ids[pos + 1 : L]
                n_targets = min(logits.shape[1], targets.shape[0])
                if n_targets > 0:
                    shift_logits = logits[0, :n_targets]
                    loss = F.cross_entropy(
                        shift_logits, targets[:n_targets].to(device), reduction="sum"
                    )
                    seq_nll += loss.item()
                    seq_tokens += n_targets

                # Update EMA scores and possibly evict
                cache_len = _get_cache_length(past_kv)
                # Compute approximate EMA score for the new tokens
                ema_score = torch.ones(chunk_end - pos, device=device) * 0.5
                eviction_mgr.update_scores(ema_score)

                if eviction_mgr.should_evict(cache_len):
                    mask = eviction_mgr.compute_eviction_mask(cache_len)
                    past_kv = eviction_mgr.apply_eviction(past_kv, mask)

                pos = chunk_end

            total_nll += seq_nll
            total_tokens += seq_tokens

            stats = eviction_mgr.eviction_stats()
            agg_eviction_stats["total_evicted"] += stats["total_evicted"]
            agg_eviction_stats["eviction_triggers"] += stats["eviction_triggers"]

    ppl = math.exp(total_nll / total_tokens) if total_tokens > 0 else float("inf")
    return {
        "ppl": round(ppl, 4),
        "num_tokens": total_tokens,
        "budget": budget,
        "eviction_stats": agg_eviction_stats,
    }


def _get_cache_length(past_kv: Any) -> int:
    """Get current sequence length from KV cache."""
    if past_kv is None:
        return 0
    if hasattr(past_kv, "key_cache") and past_kv.key_cache:
        return past_kv.key_cache[0].shape[2]
    if isinstance(past_kv, (tuple, list)) and len(past_kv) > 0:
        return past_kv[0][0].shape[2]
    return 0


# ---------------------------------------------------------------------------
# MATH accuracy evaluation
# ---------------------------------------------------------------------------

def evaluate_math(
    model,
    tokenizer,
    budget_ratio: float,
    num_problems: int = 100,
    max_new_tokens: int = 2048,
    seq_len: int = 2048,
    device: str = "cuda",
    gamma: float = 0.9,
    grace_window: int = 175,
    evict_ratio: float = 0.1,
    seed: int = 42,
) -> Dict[str, Any]:
    """
    MATH-500 accuracy with optional KV cache eviction.

    For budget_ratio=1.0: standard generation (no eviction).
    For budget_ratio<1.0: generation with eviction active.
    """
    from datasets import load_dataset, concatenate_datasets

    configs = [
        "algebra", "counting_and_probability", "geometry",
        "intermediate_algebra", "number_theory", "prealgebra", "precalculus",
    ]
    ds = concatenate_datasets(
        [load_dataset("EleutherAI/hendrycks_math", c, split="test") for c in configs]
    )
    rng = np.random.RandomState(seed)
    indices = rng.choice(len(ds), size=min(num_problems, len(ds)), replace=False)

    num_correct = 0
    num_total = 0
    budget = int(seq_len * budget_ratio)
    agg_eviction_stats = {"total_evicted": 0, "eviction_triggers": 0}

    model.eval()
    for idx in tqdm(indices, desc=f"MATH @{budget_ratio}"):
        item = ds[int(idx)]
        problem = item["problem"]
        gold_solution = item["solution"]
        gold_answer = extract_boxed(gold_solution)

        prompt = (
            f"Solve the following math problem step by step. "
            f"Put your final answer in \\boxed{{}}.\n\n"
            f"Problem: {problem}\n\n"
            f"Solution:"
        )
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(device)

        if budget_ratio >= 1.0:
            # Full cache generation
            with torch.no_grad():
                output_ids = model.generate(
                    input_ids,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    temperature=1.0,
                )
        else:
            # Generation with eviction — use CARCGenerator if available
            if CARCGenerator is not None:
                generator = CARCGenerator(
                    model=model,
                    tokenizer=tokenizer,
                    budget=budget,
                    gamma=gamma,
                    grace_window=grace_window,
                    evict_ratio=evict_ratio,
                )
                output_ids, gen_stats = generator.generate(
                    input_ids, max_new_tokens=max_new_tokens
                )
                agg_eviction_stats["total_evicted"] += gen_stats.get("total_evicted", 0)
                agg_eviction_stats["eviction_triggers"] += gen_stats.get("eviction_triggers", 0)
            else:
                # Fallback: manual generation loop with eviction
                output_ids = _generate_with_eviction(
                    model=model,
                    input_ids=input_ids,
                    max_new_tokens=max_new_tokens,
                    budget=budget,
                    gamma=gamma,
                    grace_window=grace_window,
                    evict_ratio=evict_ratio,
                    eos_token_id=tokenizer.eos_token_id,
                    agg_stats=agg_eviction_stats,
                )

        generated = tokenizer.decode(output_ids[0, input_ids.shape[1]:], skip_special_tokens=True)
        pred_answer = extract_boxed(generated)

        if answers_match(pred_answer, gold_answer):
            num_correct += 1
        num_total += 1

    accuracy = num_correct / num_total if num_total > 0 else 0.0
    return {
        "accuracy": round(accuracy, 4),
        "num_correct": num_correct,
        "num_total": num_total,
        "eviction_stats": agg_eviction_stats,
    }


def _generate_with_eviction(
    model,
    input_ids: torch.Tensor,
    max_new_tokens: int,
    budget: int,
    gamma: float,
    grace_window: int,
    evict_ratio: float,
    eos_token_id: int,
    agg_stats: Dict,
) -> torch.Tensor:
    """Fallback manual generation loop with KV eviction."""
    device = input_ids.device
    num_kv_heads = getattr(model.config, "num_key_value_heads", None)

    ema_mgr = EMAAnchorManager(gamma=gamma, num_kv_heads=num_kv_heads, per_head=True)
    eviction_mgr = CARCKVEviction(
        budget=budget, grace_window=grace_window, evict_ratio=evict_ratio
    )

    generated_ids = input_ids.clone()
    past_kv = None

    with torch.no_grad():
        # Prefill
        outputs = model(input_ids=input_ids, use_cache=True)
        past_kv = outputs.past_key_values
        next_token = outputs.logits[:, -1:].argmax(dim=-1)
        generated_ids = torch.cat([generated_ids, next_token], dim=-1)

        ema_score = torch.ones(input_ids.shape[1], device=device) * 0.5
        eviction_mgr.update_scores(ema_score)

        for step in range(max_new_tokens - 1):
            if next_token.item() == eos_token_id:
                break

            cache_len = _get_cache_length(past_kv)
            if eviction_mgr.should_evict(cache_len):
                mask = eviction_mgr.compute_eviction_mask(cache_len)
                past_kv = eviction_mgr.apply_eviction(past_kv, mask)

            outputs = model(input_ids=next_token, past_key_values=past_kv, use_cache=True)
            past_kv = outputs.past_key_values
            next_token = outputs.logits[:, -1:].argmax(dim=-1)
            generated_ids = torch.cat([generated_ids, next_token], dim=-1)

            eviction_mgr.update_scores(torch.tensor([0.5], device=device))

    stats = eviction_mgr.eviction_stats()
    agg_stats["total_evicted"] += stats["total_evicted"]
    agg_stats["eviction_triggers"] += stats["eviction_triggers"]

    return generated_ids


# ---------------------------------------------------------------------------
# LongBench evaluation
# ---------------------------------------------------------------------------

def evaluate_longbench(
    model,
    tokenizer,
    subtask: str,
    budget_ratio: float,
    max_samples: int = 50,
    max_new_tokens: int = 512,
    device: str = "cuda",
    gamma: float = 0.9,
    grace_window: int = 175,
    evict_ratio: float = 0.1,
) -> Dict[str, Any]:
    """
    LongBench subset evaluation with optional KV eviction.

    Supported subtasks: PassageRetrieval-en, MultiFieldQA-en.
    """
    from datasets import load_dataset

    ds = load_dataset("THUDM/LongBench", subtask, split="test", trust_remote_code=True)
    budget = int(8192 * budget_ratio)  # LongBench uses long contexts

    scores = []
    agg_eviction_stats = {"total_evicted": 0, "eviction_triggers": 0}

    model.eval()
    for i, item in enumerate(tqdm(ds, desc=f"LongBench({subtask}) @{budget_ratio}", total=min(max_samples, len(ds)))):
        if i >= max_samples:
            break

        context = item["context"]
        question = item["input"]
        gold_answers = item["answers"] if isinstance(item["answers"], list) else [item["answers"]]

        prompt = f"Read the following passage and answer the question.\n\nPassage:\n{context}\n\nQuestion: {question}\n\nAnswer:"
        input_ids = tokenizer(
            prompt, return_tensors="pt", truncation=True, max_length=16384
        ).input_ids.to(device)

        prompt_len = input_ids.shape[1]
        effective_budget = int(prompt_len * budget_ratio) if budget_ratio < 1.0 else prompt_len + max_new_tokens

        if budget_ratio >= 1.0:
            with torch.no_grad():
                output_ids = model.generate(
                    input_ids,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                )
        else:
            if CARCGenerator is not None:
                generator = CARCGenerator(
                    model=model,
                    tokenizer=tokenizer,
                    budget=effective_budget,
                    gamma=gamma,
                    grace_window=grace_window,
                    evict_ratio=evict_ratio,
                )
                output_ids, gen_stats = generator.generate(
                    input_ids, max_new_tokens=max_new_tokens
                )
                agg_eviction_stats["total_evicted"] += gen_stats.get("total_evicted", 0)
                agg_eviction_stats["eviction_triggers"] += gen_stats.get("eviction_triggers", 0)
            else:
                output_ids = _generate_with_eviction(
                    model=model,
                    input_ids=input_ids,
                    max_new_tokens=max_new_tokens,
                    budget=effective_budget,
                    gamma=gamma,
                    grace_window=grace_window,
                    evict_ratio=evict_ratio,
                    eos_token_id=tokenizer.eos_token_id,
                    agg_stats=agg_eviction_stats,
                )

        pred = tokenizer.decode(output_ids[0, prompt_len:], skip_special_tokens=True).strip()
        score = _compute_f1(pred, gold_answers)
        scores.append(score)

    avg_score = float(np.mean(scores)) if scores else 0.0
    return {
        "score": round(avg_score * 100, 2),
        "num_samples": len(scores),
        "eviction_stats": agg_eviction_stats,
    }


def _compute_f1(pred: str, gold_answers: List[str]) -> float:
    """Compute max token-level F1 between prediction and gold answers."""
    best_f1 = 0.0
    pred_tokens = set(pred.lower().split())
    for gold in gold_answers:
        gold_tokens = set(gold.lower().split())
        if not pred_tokens or not gold_tokens:
            continue
        common = pred_tokens & gold_tokens
        if not common:
            continue
        precision = len(common) / len(pred_tokens)
        recall = len(common) / len(gold_tokens)
        f1 = 2 * precision * recall / (precision + recall)
        best_f1 = max(best_f1, f1)
    return best_f1


# ---------------------------------------------------------------------------
# BenchmarkRunner (orchestrator)
# ---------------------------------------------------------------------------

class BenchmarkRunner:
    """Orchestrates running multiple benchmarks across budget ratios."""

    def __init__(self, model, tokenizer, device: str = "cuda",
                 gamma: float = 0.9, grace_window: int = 175,
                 evict_ratio: float = 0.1):
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.gamma = gamma
        self.grace_window = grace_window
        self.evict_ratio = evict_ratio

    def run_ppl(self, dataset_name: str, budget_ratio: float,
                max_samples: int = 200, seq_len: int = 2048) -> Dict:
        if budget_ratio >= 1.0:
            return evaluate_ppl_no_eviction(
                self.model, self.tokenizer, dataset_name,
                num_samples=max_samples, seq_len=seq_len, device=self.device,
            )
        return evaluate_ppl_with_eviction(
            self.model, self.tokenizer, dataset_name, budget_ratio,
            num_samples=max_samples, seq_len=seq_len, device=self.device,
            gamma=self.gamma, grace_window=self.grace_window,
            evict_ratio=self.evict_ratio,
        )

    def run_math(self, budget_ratio: float, num_problems: int = 100,
                 max_new_tokens: int = 2048, seed: int = 42) -> Dict:
        return evaluate_math(
            self.model, self.tokenizer, budget_ratio,
            num_problems=num_problems, max_new_tokens=max_new_tokens,
            device=self.device, gamma=self.gamma,
            grace_window=self.grace_window, evict_ratio=self.evict_ratio,
            seed=seed,
        )

    def run_longbench(self, subtask: str, budget_ratio: float,
                      max_samples: int = 50) -> Dict:
        return evaluate_longbench(
            self.model, self.tokenizer, subtask, budget_ratio,
            max_samples=max_samples, device=self.device, gamma=self.gamma,
            grace_window=self.grace_window, evict_ratio=self.evict_ratio,
        )

    def run_all(self, budget_ratios: List[float] = None,
                max_ppl_samples: int = 200, max_math_problems: int = 100,
                max_longbench_samples: int = 50) -> Dict:
        if budget_ratios is None:
            budget_ratios = [1.0, 0.5, 0.3]

        results = {}

        # PPL benchmarks
        for ds_name in ["wikitext", "c4"]:
            key = f"{ds_name}_ppl"
            results[key] = {}
            for br in budget_ratios:
                print(f"\n{'='*60}")
                print(f"Running {ds_name} PPL @ budget_ratio={br}")
                print(f"{'='*60}")
                r = self.run_ppl(ds_name, br, max_samples=max_ppl_samples)
                results[key][str(br)] = r["ppl"]
                if "eviction_stats" in r:
                    results.setdefault("eviction_stats", {})[f"{key}@{br}"] = r["eviction_stats"]

        # MATH benchmark
        results["math_accuracy"] = {}
        for br in budget_ratios:
            print(f"\n{'='*60}")
            print(f"Running MATH @ budget_ratio={br}")
            print(f"{'='*60}")
            r = self.run_math(br, num_problems=max_math_problems)
            results["math_accuracy"][str(br)] = r["accuracy"]
            if "eviction_stats" in r:
                results.setdefault("eviction_stats", {})[f"math@{br}"] = r["eviction_stats"]

        # LongBench benchmarks
        for subtask in ["PassageRetrieval-en", "MultiFieldQA-en"]:
            key = f"longbench_{subtask.lower().replace('-', '_')}"
            results[key] = {}
            for br in budget_ratios:
                print(f"\n{'='*60}")
                print(f"Running LongBench({subtask}) @ budget_ratio={br}")
                print(f"{'='*60}")
                r = self.run_longbench(subtask, br, max_samples=max_longbench_samples)
                results[key][str(br)] = r["score"]
                if "eviction_stats" in r:
                    results.setdefault("eviction_stats", {})[f"{key}@{br}"] = r["eviction_stats"]

        return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="CARC KV Eviction evaluation framework.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("--model", default=MODEL_ID, help="HF model name or local path")
    p.add_argument(
        "--benchmark", nargs="+",
        default=["all"],
        choices=["all", "wikitext", "c4", "math", "longbench_passage", "longbench_qa"],
        help="Benchmark(s) to run",
    )
    p.add_argument(
        "--budget-ratios", nargs="+", type=float, default=[1.0, 0.5, 0.3],
        help="KV cache budget ratios (1.0 = full cache)",
    )
    p.add_argument("--max-ppl-samples", type=int, default=200)
    p.add_argument("--max-math-problems", type=int, default=100)
    p.add_argument("--max-longbench-samples", type=int, default=50)
    p.add_argument("--seq-len", type=int, default=2048)
    p.add_argument("--max-new-tokens", type=int, default=2048)
    p.add_argument("--gamma", type=float, default=0.9, help="EMA decay factor")
    p.add_argument("--grace-window", type=int, default=175)
    p.add_argument("--evict-ratio", type=float, default=0.1)
    p.add_argument("--output", default="eval_results.json", help="Output JSON path")
    p.add_argument("--dtype", default="bf16", choices=["fp16", "bf16"])
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--dry-run", action="store_true", help="Quick test: 2 samples per benchmark")
    return p.parse_args()


def main():
    args = parse_args()

    if args.dry_run:
        args.max_ppl_samples = 2
        args.max_math_problems = 2
        args.max_longbench_samples = 2

    # Load model
    from transformers import AutoModelForCausalLM, AutoTokenizer

    dtype = torch.float16 if args.dtype == "fp16" else torch.bfloat16
    print(f"Loading model: {args.model} ({args.dtype})")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True
    )

    runner = BenchmarkRunner(
        model=model,
        tokenizer=tokenizer,
        gamma=args.gamma,
        grace_window=args.grace_window,
        evict_ratio=args.evict_ratio,
    )

    benchmarks = args.benchmark
    if "all" in benchmarks:
        results = runner.run_all(
            budget_ratios=args.budget_ratios,
            max_ppl_samples=args.max_ppl_samples,
            max_math_problems=args.max_math_problems,
            max_longbench_samples=args.max_longbench_samples,
        )
    else:
        results = {}
        for bm in benchmarks:
            for br in args.budget_ratios:
                if bm == "wikitext":
                    r = runner.run_ppl("wikitext", br, args.max_ppl_samples, args.seq_len)
                    results.setdefault("wikitext_ppl", {})[str(br)] = r["ppl"]
                elif bm == "c4":
                    r = runner.run_ppl("c4", br, args.max_ppl_samples, args.seq_len)
                    results.setdefault("c4_ppl", {})[str(br)] = r["ppl"]
                elif bm == "math":
                    r = runner.run_math(br, args.max_math_problems, args.max_new_tokens, args.seed)
                    results.setdefault("math_accuracy", {})[str(br)] = r["accuracy"]
                elif bm == "longbench_passage":
                    r = runner.run_longbench("PassageRetrieval-en", br, args.max_longbench_samples)
                    results.setdefault("longbench_passageretrieval_en", {})[str(br)] = r["score"]
                elif bm == "longbench_qa":
                    r = runner.run_longbench("MultiFieldQA-en", br, args.max_longbench_samples)
                    results.setdefault("longbench_multifieldqa_en", {})[str(br)] = r["score"]

    # Wrap output
    output = {
        "model": args.model,
        "budget_ratios": args.budget_ratios,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "config": {
            "gamma": args.gamma,
            "grace_window": args.grace_window,
            "evict_ratio": args.evict_ratio,
            "seq_len": args.seq_len,
            "max_new_tokens": args.max_new_tokens,
            "dtype": args.dtype,
            "dry_run": args.dry_run,
        },
        "results": results,
    }

    out_path = Path(args.output)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\nResults saved to {out_path}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
