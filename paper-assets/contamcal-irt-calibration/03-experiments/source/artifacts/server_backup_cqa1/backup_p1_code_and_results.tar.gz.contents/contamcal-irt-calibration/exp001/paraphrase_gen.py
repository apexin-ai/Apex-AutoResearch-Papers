"""
Paraphrase generation for benchmark contamination injection.

Generates semantically equivalent paraphrases of benchmark items (MMLU, GSM8K,
ARC-Challenge, HumanEval) using a local LLM via vLLM/transformers or an
OpenAI-compatible API.

Quality control: cosine similarity > 0.85 (sentence-transformers) AND BLEU < 0.3.

Input:  HuggingFace benchmark datasets (auto-downloaded)
Output: JSON per benchmark with original + paraphrase + similarity + BLEU scores
"""

import argparse
import json
import logging
import os
import re
from pathlib import Path

import nltk
import numpy as np
import torch
from datasets import load_dataset
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

BENCHMARK_CONFIGS = {
    "mmlu": {
        "path": "cais/mmlu",
        "name": "all",
        "split": "test",
    },
    "gsm8k": {
        "path": "openai/gsm8k",
        "name": "main",
        "split": "test",
    },
    "arc_challenge": {
        "path": "allenai/ai2_arc",
        "name": "ARC-Challenge",
        "split": "test",
    },
    "humaneval": {
        "path": "openai/openai_humaneval",
        "name": "openai_humaneval",
        "split": "test",
    },
}

# ── Prompt templates ──

MMLU_PARAPHRASE_PROMPT = """Paraphrase the following multiple-choice question. Keep the same meaning, number of choices, and correct answer letter. Change wording substantially.

Original question: {question}
Choices:
{choices}
Correct answer: {answer}

Output format (strict JSON):
{{"question": "...", "choices": ["A) ...", "B) ...", "C) ...", "D) ..."], "answer": "{answer}"}}
"""

GSM8K_PARAPHRASE_PROMPT = """Paraphrase the following math word problem. Change the wording and scenario but keep the same numerical answer. Do NOT change any numbers.

Original: {question}
Answer: {answer}

Output format (strict JSON):
{{"question": "...", "answer": "{answer}"}}
"""

ARC_PARAPHRASE_PROMPT = """Paraphrase the following science multiple-choice question. Keep the same meaning and correct answer. Change wording substantially.

Original question: {question}
Choices:
{choices}
Correct answer: {answer}

Output format (strict JSON):
{{"question": "...", "choices": {choices_json}, "answer": "{answer}"}}
"""

HUMANEVAL_PARAPHRASE_PROMPT = """Paraphrase the following Python function docstring. Keep the exact same specification (inputs, outputs, constraints, examples) but change the wording. Do NOT modify the function signature or test cases.

Function signature: {entry_point}
Original docstring:
{docstring}

Output the paraphrased docstring only, no code, no extra formatting.
"""


def load_benchmark(benchmark: str, cache_dir: str) -> list[dict]:
    """Load benchmark dataset and normalize to list of dicts."""
    cfg = BENCHMARK_CONFIGS[benchmark]
    ds = load_dataset(cfg["path"], cfg["name"], split=cfg["split"], cache_dir=cache_dir)

    items = []
    if benchmark == "mmlu":
        for row in ds:
            choices_list = row["choices"]
            answer_idx = row["answer"]
            letters = "ABCDEFGHIJ"
            items.append({
                "question": row["question"],
                "choices": [f"{letters[i]}) {c}" for i, c in enumerate(choices_list)],
                "answer": letters[answer_idx],
                "subject": row["subject"],
            })
    elif benchmark == "gsm8k":
        for row in ds:
            answer_text = row["answer"]
            final_answer = answer_text.split("####")[-1].strip() if "####" in answer_text else answer_text
            items.append({
                "question": row["question"],
                "answer": final_answer,
                "full_answer": answer_text,
            })
    elif benchmark == "arc_challenge":
        for row in ds:
            choices_list = row["choices"]["text"]
            labels = row["choices"]["label"]
            items.append({
                "question": row["question"],
                "choices": [f"{l}) {t}" for l, t in zip(labels, choices_list)],
                "answer": row["answerKey"],
            })
    elif benchmark == "humaneval":
        for row in ds:
            items.append({
                "task_id": row["task_id"],
                "prompt": row["prompt"],
                "entry_point": row["entry_point"],
                "canonical_solution": row["canonical_solution"],
                "test": row["test"],
            })
    return items


def build_prompts(benchmark: str, items: list[dict]) -> list[str]:
    """Build paraphrase prompts for each benchmark item."""
    prompts = []
    for item in items:
        if benchmark == "mmlu":
            choices_str = "\n".join(item["choices"])
            prompts.append(MMLU_PARAPHRASE_PROMPT.format(
                question=item["question"], choices=choices_str, answer=item["answer"]
            ))
        elif benchmark == "gsm8k":
            prompts.append(GSM8K_PARAPHRASE_PROMPT.format(
                question=item["question"], answer=item["answer"]
            ))
        elif benchmark == "arc_challenge":
            choices_str = "\n".join(item["choices"])
            choices_json = json.dumps(item["choices"])
            prompts.append(ARC_PARAPHRASE_PROMPT.format(
                question=item["question"], choices=choices_str,
                answer=item["answer"], choices_json=choices_json
            ))
        elif benchmark == "humaneval":
            docstring = extract_docstring(item["prompt"])
            prompts.append(HUMANEVAL_PARAPHRASE_PROMPT.format(
                entry_point=item["entry_point"], docstring=docstring
            ))
    return prompts


def extract_docstring(prompt: str) -> str:
    match = re.search(r'"""(.*?)"""', prompt, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"'''(.*?)'''", prompt, re.DOTALL)
    if match:
        return match.group(1).strip()
    return prompt


def generate_with_transformers(prompts: list[str], model: str, batch_size: int, cache_dir: str) -> list[str]:
    from transformers import AutoModelForCausalLM, AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model, cache_dir=cache_dir, trust_remote_code=True)
    llm = AutoModelForCausalLM.from_pretrained(
        model, cache_dir=cache_dir, torch_dtype=torch.bfloat16,
        trust_remote_code=True, device_map="auto",
    )
    llm.eval()
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    outputs_all = []
    for i in tqdm(range(0, len(prompts), batch_size), desc="Transformers generation"):
        batch = prompts[i:i + batch_size]
        for prompt in batch:
            messages = [
                {"role": "system", "content": "You are a helpful assistant that paraphrases text precisely."},
                {"role": "user", "content": prompt},
            ]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=3072).to(llm.device)
            with torch.no_grad():
                output_ids = llm.generate(
                    **inputs, max_new_tokens=1024, do_sample=True,
                    temperature=0.7, top_p=0.95,
                    pad_token_id=tokenizer.pad_token_id,
                )
            generated = tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
            outputs_all.append(generated.strip())
    return outputs_all


def generate_with_vllm(prompts: list[str], model: str, batch_size: int) -> list[str]:
    from vllm import LLM, SamplingParams
    llm = LLM(model=model, trust_remote_code=True, max_model_len=4096)
    sampling_params = SamplingParams(temperature=0.7, max_tokens=1024, top_p=0.95)

    outputs_all = []
    for i in tqdm(range(0, len(prompts), batch_size), desc="vLLM generation"):
        batch = prompts[i:i + batch_size]
        outputs = llm.generate(batch, sampling_params)
        for o in outputs:
            outputs_all.append(o.outputs[0].text.strip())
    return outputs_all


def generate_with_api(prompts: list[str], api_url: str, model: str, batch_size: int) -> list[str]:
    from openai import OpenAI
    client = OpenAI(base_url=api_url, api_key=[REDACTED]"OPENAI_API_KEY", "empty"))

    outputs = []
    for prompt in tqdm(prompts, desc="API generation"):
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that paraphrases text precisely."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=1024,
        )
        outputs.append(resp.choices[0].message.content.strip())
    return outputs


def compute_similarity(texts_a: list[str], texts_b: list[str], sim_model: SentenceTransformer) -> list[float]:
    emb_a = sim_model.encode(texts_a, batch_size=64, show_progress_bar=True, convert_to_numpy=True)
    emb_b = sim_model.encode(texts_b, batch_size=64, show_progress_bar=True, convert_to_numpy=True)
    # cosine similarity
    norms_a = np.linalg.norm(emb_a, axis=1, keepdims=True)
    norms_b = np.linalg.norm(emb_b, axis=1, keepdims=True)
    similarities = np.sum((emb_a / norms_a) * (emb_b / norms_b), axis=1)
    return similarities.tolist()


def compute_bleu(texts_a: list[str], texts_b: list[str]) -> list[float]:
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    smoother = SmoothingFunction().method1
    scores = []
    for a, b in zip(texts_a, texts_b):
        ref = nltk.word_tokenize(a.lower())
        hyp = nltk.word_tokenize(b.lower())
        score = sentence_bleu([ref], hyp, smoothing_function=smoother)
        scores.append(score)
    return scores


def parse_json_output(text: str) -> dict | None:
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    return None


def extract_paraphrase_text(benchmark: str, item: dict, raw_output: str) -> str | None:
    """Extract the paraphrased text from model output for similarity comparison."""
    if benchmark == "humaneval":
        return raw_output.strip()

    parsed = parse_json_output(raw_output)
    if parsed and "question" in parsed:
        return parsed["question"]
    return None


def get_original_text(benchmark: str, item: dict) -> str:
    if benchmark == "humaneval":
        return extract_docstring(item["prompt"])
    return item["question"]


def main():
    parser = argparse.ArgumentParser(description="Generate paraphrases of benchmark items")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=list(BENCHMARK_CONFIGS.keys()),
                        help="Benchmark to paraphrase")
    parser.add_argument("--model", type=str, default="Qwen/Qwen2.5-72B-Instruct",
                        help="Model for paraphrase generation")
    parser.add_argument("--output-dir", type=str, required=True,
                        help="Output directory for paraphrase JSON")
    parser.add_argument("--api-url", type=str, default=None,
                        help="OpenAI-compatible API URL (if set, use API mode instead of vLLM)")
    parser.add_argument("--batch-size", type=int, default=32,
                        help="Batch size for generation")
    parser.add_argument("--sim-model", type=str,
                        default="sentence-transformers/all-MiniLM-L6-v2",
                        help="Sentence-transformers model for similarity")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache",
                        help="HuggingFace cache directory")
    parser.add_argument("--max-retries", type=int, default=2,
                        help="Max retries for items failing quality check")
    parser.add_argument("--sim-threshold", type=float, default=0.85,
                        help="Minimum cosine similarity threshold")
    parser.add_argument("--bleu-threshold", type=float, default=0.3,
                        help="Maximum BLEU threshold")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Loading benchmark: %s", args.benchmark)
    items = load_benchmark(args.benchmark, args.cache_dir)
    logger.info("Loaded %d items", len(items))

    prompts = build_prompts(args.benchmark, items)

    # Generation
    for attempt in range(1 + args.max_retries):
        if attempt == 0:
            current_prompts = prompts
            current_indices = list(range(len(items)))
        else:
            # Retry only failed items
            current_prompts = [prompts[i] for i in retry_indices]
            current_indices = retry_indices

        if not current_prompts:
            break

        logger.info("Generation attempt %d: %d items", attempt + 1, len(current_prompts))

        if args.api_url:
            raw_outputs = generate_with_api(current_prompts, args.api_url, args.model, args.batch_size)
        else:
            try:
                from vllm import LLM  # noqa: F401
                raw_outputs = generate_with_vllm(current_prompts, args.model, args.batch_size)
            except ImportError:
                logger.info("vLLM not available, using transformers")
                raw_outputs = generate_with_transformers(current_prompts, args.model, args.batch_size, args.cache_dir)
            except Exception as e:
                logger.warning("vLLM init failed (%s), falling back to transformers", e)
                raw_outputs = generate_with_transformers(current_prompts, args.model, args.batch_size, args.cache_dir)

        # Store outputs
        if attempt == 0:
            all_raw_outputs = [""] * len(items)
        for idx, output in zip(current_indices, raw_outputs):
            all_raw_outputs[idx] = output

        # Quality check
        originals = [get_original_text(args.benchmark, items[i]) for i in current_indices]
        paraphrases = []
        for idx, output in zip(current_indices, raw_outputs):
            p = extract_paraphrase_text(args.benchmark, items[idx], output)
            paraphrases.append(p if p else "")

        logger.info("Computing similarity scores...")
        sim_model = SentenceTransformer(args.sim_model, cache_folder=args.cache_dir)
        similarities = compute_similarity(originals, paraphrases, sim_model)
        bleu_scores = compute_bleu(originals, paraphrases)

        if attempt == 0:
            all_similarities = [0.0] * len(items)
            all_bleu_scores = [1.0] * len(items)

        retry_indices = []
        for i, (idx, sim, bleu) in enumerate(zip(current_indices, similarities, bleu_scores)):
            all_similarities[idx] = sim
            all_bleu_scores[idx] = bleu
            if sim < args.sim_threshold or bleu > args.bleu_threshold:
                retry_indices.append(idx)

        logger.info("Attempt %d: %d/%d passed quality check",
                     attempt + 1, len(current_indices) - len(retry_indices), len(current_indices))

    # Assemble results
    results = []
    passed = 0
    for i, item in enumerate(items):
        paraphrase_text = extract_paraphrase_text(args.benchmark, item, all_raw_outputs[i])
        parsed = parse_json_output(all_raw_outputs[i]) if args.benchmark != "humaneval" else None

        entry = {
            "index": i,
            "benchmark": args.benchmark,
            "original": item,
            "paraphrase_raw": all_raw_outputs[i],
            "paraphrase_parsed": parsed,
            "paraphrase_text": paraphrase_text,
            "similarity": all_similarities[i],
            "bleu": all_bleu_scores[i],
            "passed_qc": all_similarities[i] >= args.sim_threshold and all_bleu_scores[i] <= args.bleu_threshold,
        }

        if args.benchmark == "humaneval" and paraphrase_text:
            entry["paraphrased_prompt"] = item["prompt"].replace(
                extract_docstring(item["prompt"]), paraphrase_text
            )

        results.append(entry)
        if entry["passed_qc"]:
            passed += 1

    output_file = output_dir / f"{args.benchmark}_paraphrases.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    logger.info("Saved %d paraphrases to %s (%d/%d passed QC)",
                len(results), output_file, passed, len(results))


if __name__ == "__main__":
    main()
