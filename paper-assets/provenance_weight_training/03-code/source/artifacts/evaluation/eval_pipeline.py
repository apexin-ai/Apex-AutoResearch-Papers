"""
Evaluation pipeline for pretrained language models.

Three evaluation axes:
  1. Perplexity on held-out FineWeb — measures language modeling quality.
     Uses sliding-window evaluation (stride = max_length // 2) for long docs.
  2. lm-eval-harness benchmarks (HellaSwag, MMLU) — measures downstream task quality.
     Calls lm_eval.simple_evaluate for standardized, reproducible evaluation.
  3. Generation quality — measures output diversity via Self-BLEU and Distinct-n.
     Self-BLEU: average pairwise 4-gram BLEU across 1000 generated texts (lower = more diverse).
     Distinct-n: ratio of unique n-grams to total n-grams for n=1,2,3 (higher = more diverse).

Outputs:
  eval_results.json        — all metrics in one dict
  perplexity_details.json  — per-document perplexity breakdown
  generation_samples.jsonl — generated texts with metadata
  lm_eval_results/         — raw lm-eval-harness output
"""

import argparse
import json
import math
import os
import random
from collections import Counter
from pathlib import Path

import torch
from datasets import load_dataset
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


def parse_args():
    p = argparse.ArgumentParser(description="Evaluate a pretrained language model.")
    p.add_argument("--model_path", type=str, required=True,
                   help="Path to the model checkpoint directory")
    p.add_argument("--model_name", type=str, default=None,
                   help="Model name for lm-eval-harness (defaults to model_path)")
    p.add_argument("--output_dir", type=str, required=True,
                   help="Directory to save evaluation results")
    p.add_argument("--eval_data_path", type=str, default=None,
                   help="Local path to held-out eval data (JSONL with 'text' field)")
    p.add_argument("--fineweb_subset", type=str, default="sample-10BT",
                   help="FineWeb subset for streaming eval if eval_data_path is not set")
    p.add_argument("--num_eval_tokens", type=int, default=5_000_000,
                   help="Approximate number of tokens to evaluate perplexity on")
    p.add_argument("--max_length", type=int, default=2048,
                   help="Maximum sequence length for perplexity evaluation")
    p.add_argument("--batch_size", type=int, default=4,
                   help="Evaluation batch size")
    p.add_argument("--run_perplexity", type=lambda x: x.lower() != "false",
                   default=True, help="Run perplexity evaluation")
    p.add_argument("--run_lm_eval", type=lambda x: x.lower() != "false",
                   default=True, help="Run lm-eval-harness benchmarks")
    p.add_argument("--run_generation", type=lambda x: x.lower() != "false",
                   default=True, help="Run generation quality evaluation")
    p.add_argument("--lm_eval_tasks", type=str, default="hellaswag,mmlu",
                   help="Comma-separated lm-eval tasks")
    p.add_argument("--num_generation_samples", type=int, default=1000,
                   help="Number of texts to generate for diversity metrics")
    p.add_argument("--seed", type=int, default=42, help="Random seed")
    return p.parse_args()


# ---------------------------------------------------------------------------
# 1. Perplexity evaluation
# ---------------------------------------------------------------------------

def load_eval_texts(args):
    """Yield texts from local JSONL or streaming FineWeb until token budget is reached."""
    if args.eval_data_path:
        with open(args.eval_data_path, "r") as f:
            for line in f:
                rec = json.loads(line)
                yield rec["text"]
    else:
        ds = load_dataset(
            "HuggingFaceFW/fineweb",
            name=args.fineweb_subset,
            split="train",
            streaming=True,
        )
        for ex in ds:
            text = ex.get("text", "")
            if text and len(text.split()) > 30:
                yield text


def evaluate_perplexity(model, tokenizer, args):
    """Sliding-window perplexity on held-out data."""
    stride = args.max_length // 2
    device = model.device

    total_nll = 0.0
    total_tokens = 0
    doc_results = []
    tokens_seen = 0

    for text in tqdm(load_eval_texts(args), desc="Perplexity", unit="doc"):
        if tokens_seen >= args.num_eval_tokens:
            break

        encodings = tokenizer(text, return_tensors="pt", truncation=False)
        input_ids = encodings.input_ids[0]
        seq_len = input_ids.size(0)

        if seq_len < 2:
            continue

        doc_nll = 0.0
        doc_tokens = 0

        for begin in range(0, seq_len, stride):
            end = min(begin + args.max_length, seq_len)
            target_begin = max(begin, stride) if begin > 0 else 1

            ids = input_ids[begin:end].unsqueeze(0).to(device)
            target_ids = ids.clone()
            # Mask prefix tokens so loss is only on the non-overlapping part
            target_ids[0, : target_begin - begin] = -100

            with torch.no_grad(), torch.amp.autocast("cuda"):
                outputs = model(ids, labels=target_ids)

            n_tokens = (target_ids[0] != -100).sum().item()
            if n_tokens > 0:
                doc_nll += outputs.loss.float().item() * n_tokens
                doc_tokens += n_tokens

            if end == seq_len:
                break

        if doc_tokens > 0:
            doc_ppl = math.exp(doc_nll / doc_tokens)
            doc_results.append({
                "num_tokens": doc_tokens,
                "loss": doc_nll / doc_tokens,
                "perplexity": doc_ppl,
            })
            total_nll += doc_nll
            total_tokens += doc_tokens
            tokens_seen += doc_tokens

    avg_loss = total_nll / total_tokens if total_tokens > 0 else float("inf")
    avg_ppl = math.exp(avg_loss) if avg_loss < 30 else float("inf")

    summary = {
        "perplexity": avg_ppl,
        "loss": avg_loss,
        "total_tokens": total_tokens,
        "num_documents": len(doc_results),
    }
    return summary, doc_results


# ---------------------------------------------------------------------------
# 2. lm-eval-harness
# ---------------------------------------------------------------------------

def evaluate_lm_eval(model_path, args):
    """Run lm-eval-harness benchmarks."""
    import lm_eval

    model_name = args.model_name or model_path
    tasks = [t.strip() for t in args.lm_eval_tasks.split(",")]
    output_path = os.path.join(args.output_dir, "lm_eval_results")
    os.makedirs(output_path, exist_ok=True)

    results = lm_eval.simple_evaluate(
        model="hf",
        model_args=f"pretrained={model_path},dtype=float16,trust_remote_code=True",
        tasks=tasks,
        batch_size=args.batch_size,
        random_seed=args.seed,
        numpy_random_seed=args.seed,
        torch_random_seed=args.seed,
        log_samples=True,
        output_path=output_path,
    )

    summary = {}
    if "results" in results:
        for task_name, task_results in results["results"].items():
            task_summary = {}
            for metric, value in task_results.items():
                if isinstance(value, (int, float)):
                    task_summary[metric] = value
            summary[task_name] = task_summary

    raw_path = os.path.join(output_path, "raw_results.json")
    with open(raw_path, "w") as f:
        json.dump(results.get("results", {}), f, indent=2, default=str)

    return summary


# ---------------------------------------------------------------------------
# 3. Generation quality
# ---------------------------------------------------------------------------

def generate_samples(model, tokenizer, args):
    """Generate text samples for diversity evaluation."""
    device = model.device
    prompts = [tokenizer.bos_token or ""] * args.num_generation_samples
    samples = []
    gen_batch = min(args.batch_size, 32)

    for i in tqdm(range(0, len(prompts), gen_batch), desc="Generating", unit="batch"):
        batch_prompts = prompts[i : i + gen_batch]
        inputs = tokenizer(
            batch_prompts,
            return_tensors="pt",
            padding=True,
        ).to(device)

        with torch.no_grad(), torch.amp.autocast("cuda"):
            output_ids = model.generate(
                **inputs,
                max_new_tokens=256,
                do_sample=True,
                temperature=0.8,
                top_p=0.95,
                pad_token_id=tokenizer.pad_token_id,
            )

        for j, ids in enumerate(output_ids):
            prompt_len = inputs["input_ids"].shape[1]
            gen_text = tokenizer.decode(ids[prompt_len:], skip_special_tokens=True)
            samples.append(gen_text)

    return samples


def tokenize_for_bleu(text):
    return text.lower().split()


def sentence_bleu_4gram(hypothesis, reference):
    """Compute 4-gram BLEU between two tokenized sentences (no brevity penalty clipping to avoid log(0))."""
    hyp_len = len(hypothesis)
    ref_len = len(reference)
    if hyp_len == 0:
        return 0.0

    scores = []
    for n in range(1, 5):
        if hyp_len < n:
            scores.append(0.0)
            continue
        hyp_ngrams = Counter(tuple(hypothesis[i : i + n]) for i in range(hyp_len - n + 1))
        ref_ngrams = Counter(tuple(reference[i : i + n]) for i in range(ref_len - n + 1))
        clipped = sum(min(c, ref_ngrams[ng]) for ng, c in hyp_ngrams.items())
        total = sum(hyp_ngrams.values())
        scores.append(clipped / total if total > 0 else 0.0)

    if any(s == 0 for s in scores):
        return 0.0

    log_avg = sum(math.log(s) for s in scores) / 4.0
    bp = min(1.0, math.exp(1.0 - ref_len / hyp_len)) if hyp_len > 0 else 0.0
    return bp * math.exp(log_avg)


def compute_self_bleu(samples, max_pairs=5000):
    """Average pairwise 4-gram BLEU over a subsample of pairs."""
    tokenized = [tokenize_for_bleu(s) for s in samples if s.strip()]
    if len(tokenized) < 2:
        return 0.0

    n = len(tokenized)
    if n * (n - 1) // 2 <= max_pairs:
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    else:
        pairs = set()
        while len(pairs) < max_pairs:
            i, j = random.sample(range(n), 2)
            pairs.add((min(i, j), max(i, j)))
        pairs = list(pairs)

    total = sum(sentence_bleu_4gram(tokenized[i], tokenized[j]) for i, j in tqdm(pairs, desc="Self-BLEU", unit="pair"))
    return total / len(pairs)


def compute_distinct_n(samples, max_n=3):
    """Distinct-n: ratio of unique n-grams to total n-grams across all samples."""
    results = {}
    all_tokens = []
    for s in samples:
        all_tokens.extend(tokenize_for_bleu(s))

    for n in range(1, max_n + 1):
        ngrams = [tuple(all_tokens[i : i + n]) for i in range(len(all_tokens) - n + 1)]
        if not ngrams:
            results[f"distinct_{n}"] = 0.0
            continue
        results[f"distinct_{n}"] = len(set(ngrams)) / len(ngrams)
    return results


def evaluate_generation(model, tokenizer, args):
    """Run generation quality metrics."""
    samples = generate_samples(model, tokenizer, args)

    self_bleu = compute_self_bleu(samples)
    distinct = compute_distinct_n(samples)

    sample_path = os.path.join(args.output_dir, "generation_samples.jsonl")
    with open(sample_path, "w") as f:
        for i, text in enumerate(samples):
            f.write(json.dumps({"index": i, "text": text}, ensure_ascii=False) + "\n")

    summary = {"self_bleu": self_bleu, **distinct, "num_samples": len(samples)}
    return summary


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    random.seed(args.seed)
    torch.manual_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    results = {}

    print(f"Loading model from {args.model_path}")
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()

    if args.run_perplexity:
        print("\n=== Perplexity Evaluation ===")
        ppl_summary, ppl_details = evaluate_perplexity(model, tokenizer, args)
        results["perplexity"] = ppl_summary
        detail_path = os.path.join(args.output_dir, "perplexity_details.json")
        with open(detail_path, "w") as f:
            json.dump(ppl_details, f, indent=2)
        print(f"Perplexity: {ppl_summary['perplexity']:.2f}  Loss: {ppl_summary['loss']:.4f}")

    if args.run_lm_eval:
        print("\n=== lm-eval-harness ===")
        try:
            lm_summary = evaluate_lm_eval(args.model_path, args)
            results["lm_eval"] = lm_summary
            for task, metrics in lm_summary.items():
                print(f"  {task}: {metrics}")
        except Exception as e:
            print(f"lm-eval-harness failed: {e}")
            results["lm_eval"] = {"error": str(e)}

    if args.run_generation:
        print("\n=== Generation Quality ===")
        gen_summary = evaluate_generation(model, tokenizer, args)
        results["generation"] = gen_summary
        print(f"Self-BLEU: {gen_summary['self_bleu']:.4f}")
        for k, v in gen_summary.items():
            if k.startswith("distinct_"):
                print(f"  {k}: {v:.4f}")

    results_path = os.path.join(args.output_dir, "eval_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {results_path}")


if __name__ == "__main__":
    main()
