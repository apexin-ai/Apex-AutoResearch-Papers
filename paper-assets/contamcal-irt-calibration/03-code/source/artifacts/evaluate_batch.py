"""
Benchmark evaluation for contamination-injected models.
Batch inference version: all benchmarks use batched generation/forward pass.

Evaluates checkpoints on MMLU (5-shot), GSM8K (8-shot CoT), ARC-Challenge
(25-shot), and HumanEval (pass@1). Outputs per-benchmark accuracy and
per-item correctness matrix for downstream IRT analysis.

Input:  Model checkpoint path
Output: JSON with aggregate scores + per-item binary correctness
"""

import argparse
import json
import logging
import os
import re
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import torch
from datasets import load_dataset
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

BENCHMARK_CONFIGS = {
    "mmlu": {"num_fewshot": 5, "metric": "accuracy"},
    "gsm8k": {"num_fewshot": 8, "metric": "exact_match"},
    "arc_challenge": {"num_fewshot": 25, "metric": "accuracy"},
    "humaneval": {"num_fewshot": 0, "metric": "pass@1"},
}

# ── Few-shot evaluation (MMLU, ARC-Challenge) ──

MMLU_SUBJECTS = None  # loaded dynamically

CHOICE_LETTERS = "ABCDEFGHIJ"

LLAMA3_CHAT_TEMPLATE = (
    "{% set loop_messages = messages %}"
    "{% for message in loop_messages %}"
    "{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>\n\n' + message['content'] | trim + '<|eot_id|>' %}"
    "{% if loop.first %}{% set content = bos_token + content %}{% endif %}"
    "{{ content }}"
    "{% endfor %}"
    "{% if add_generation_prompt %}{{ '<|start_header_id|>assistant<|end_header_id|>\n\n' }}{% endif %}"
)



def load_model_and_tokenizer(model_path: str, cache_dir: str, adapter_path: str = None):
    """Load model and tokenizer. If adapter_path is given, load base + LoRA adapter."""
    if adapter_path:
        logger.info("Loading base model: %s + adapter: %s", model_path, adapter_path)
        from peft import PeftModel
        tokenizer = AutoTokenizer.from_pretrained(
            adapter_path, cache_dir=cache_dir, trust_remote_code=True
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            model_path,
            cache_dir=cache_dir,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
        )
        model = PeftModel.from_pretrained(base_model, adapter_path)
        model = model.merge_and_unload()
    else:
        logger.info("Loading model: %s", model_path)
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, cache_dir=cache_dir, trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path,
            cache_dir=cache_dir,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
        )
    model.eval()

    # Set chat template for models that don't have one (e.g. Llama-3.2 base)
    if tokenizer.chat_template is None:
        model_id = model_path.lower() if model_path else ""
        if "llama" in model_id:
            tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE
            logger.info("Set Llama 3 chat template on tokenizer")

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer


def format_as_chat(tokenizer, user_content: str, system_prompt: str = None) -> str:
    """Wrap content in chat template to match SFT training format."""
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_content})
    return tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )



def extract_mcq_answer(text, valid_choices):
    text = text.strip()
    if not text:
        return None
    if text[0] in valid_choices:
        return text[0]
    match = re.search(r'(?:answer|Answer)\s*(?:is|:)\s*\**\s*([A-Z])', text)
    if match and match.group(1) in valid_choices:
        return match.group(1)
    match = re.search(r'\(([A-Z])\)', text)
    if match and match.group(1) in valid_choices:
        return match.group(1)
    for ch in text:
        if ch in valid_choices:
            return ch
    return None


def extract_code_from_markdown(text):
    match = re.search(r'```(?:python)?\n(.*?)```', text, re.DOTALL)
    if match:
        return match.group(1)
    return text


def compute_choice_logprobs(model, tokenizer, prompt: str, choices: list[str]) -> list[float]:
    """Compute log probabilities of each choice token given prompt (single-item fallback)."""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits[0, -1, :]  # last token logits
    log_probs = torch.log_softmax(logits, dim=-1)

    choice_logprobs = []
    for choice in choices:
        token_ids = tokenizer.encode(choice, add_special_tokens=False)
        if token_ids:
            choice_logprobs.append(log_probs[token_ids[0]].item())
        else:
            choice_logprobs.append(float("-inf"))

    return choice_logprobs


# ── Batch inference helpers ──

def batch_generate(model, tokenizer, prompts, max_new_tokens, batch_size):
    """Left-pad batch generation with OOM auto-retry (halve batch size)."""
    all_outputs = []
    orig_padding_side = tokenizer.padding_side
    tokenizer.padding_side = "left"

    i = 0
    current_bs = batch_size
    pbar = tqdm(total=len(prompts), desc="Batch generate")
    while i < len(prompts):
        batch = prompts[i:i + current_bs]
        try:
            inputs = tokenizer(batch, return_tensors="pt", padding=True,
                               truncation=True, max_length=2048).to(model.device)
            with torch.no_grad():
                output_ids = model.generate(
                    **inputs, max_new_tokens=max_new_tokens, do_sample=False,
                    pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
                )
            input_len = inputs["input_ids"].shape[1]
            for j in range(len(batch)):
                gen = tokenizer.decode(output_ids[j][input_len:], skip_special_tokens=True)
                all_outputs.append(gen)
            pbar.update(len(batch))
            i += len(batch)
            current_bs = batch_size
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            if current_bs == 1:
                logger.error("OOM at batch_size=1, index %d, returning empty", i)
                all_outputs.append("")
                pbar.update(1)
                i += 1
            else:
                current_bs = max(1, current_bs // 2)
                logger.warning("OOM, reducing batch_size to %d", current_bs)
    pbar.close()

    tokenizer.padding_side = orig_padding_side
    return all_outputs


def batch_compute_choice_logprobs(model, tokenizer, prompts, choices_per_sample, batch_size):
    """Batch forward pass to compute choice logprobs. Left-padded, OOM auto-retry."""
    all_results = []
    orig_padding_side = tokenizer.padding_side
    tokenizer.padding_side = "left"

    i = 0
    current_bs = batch_size
    pbar = tqdm(total=len(prompts), desc="Batch logprobs")
    while i < len(prompts):
        batch_prompts = prompts[i:i + current_bs]
        batch_choices = choices_per_sample[i:i + current_bs]
        try:
            inputs = tokenizer(batch_prompts, return_tensors="pt", padding=True,
                               truncation=True, max_length=2048).to(model.device)
            with torch.no_grad():
                outputs = model(**inputs)

            logits = outputs.logits[:, -1, :]
            log_probs = torch.log_softmax(logits, dim=-1)

            for j in range(len(batch_prompts)):
                choice_lp = []
                for choice in batch_choices[j]:
                    token_ids = tokenizer.encode(choice, add_special_tokens=False)
                    if token_ids:
                        choice_lp.append(log_probs[j, token_ids[0]].item())
                    else:
                        choice_lp.append(float("-inf"))
                all_results.append(choice_lp)

            pbar.update(len(batch_prompts))
            i += len(batch_prompts)
            current_bs = batch_size
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            if current_bs == 1:
                logger.warning("OOM at batch_size=1, falling back to single-item")
                tokenizer.padding_side = orig_padding_side
                lp = compute_choice_logprobs(model, tokenizer, batch_prompts[0], batch_choices[0])
                tokenizer.padding_side = "left"
                all_results.append(lp)
                pbar.update(1)
                i += 1
            else:
                current_bs = max(1, current_bs // 2)
                logger.warning("OOM, reducing batch_size to %d", current_bs)
    pbar.close()

    tokenizer.padding_side = orig_padding_side
    return all_results


# ── MCQ evaluation (MMLU, ARC-Challenge) ──

def evaluate_mcq(model, tokenizer, benchmark: str, num_fewshot: int,
                 cache_dir: str, batch_size: int, max_samples: int = None,
                 mc_format: str = "aligned", use_generation: bool = False) -> dict:
    if benchmark == "mmlu":
        ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)
        val_ds = load_dataset("cais/mmlu", "all", split="validation", cache_dir=cache_dir)
    elif benchmark == "arc_challenge":
        ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=cache_dir)
        val_ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="validation", cache_dir=cache_dir)
    else:
        raise ValueError(f"Unknown MCQ benchmark: {benchmark}")

    fewshot_examples = []
    if num_fewshot > 0 and val_ds is not None:
        indices = list(range(min(num_fewshot, len(val_ds))))
        for idx in indices:
            row = val_ds[idx]
            fewshot_examples.append(format_mcq_example(row, benchmark, mc_format))

    fewshot_prefix = "\n\n".join(fewshot_examples) + "\n\n" if fewshot_examples else ""

    if max_samples:
        ds = ds.select(range(min(max_samples, len(ds))))

    prompts = []
    answer_letters = []
    all_choice_tokens = []

    for row in ds:
        if benchmark == "mmlu":
            choices_text = row["choices"]
            answer_idx = row["answer"]
            answer_letter = CHOICE_LETTERS[answer_idx]
            question = row["question"]
            choices_display = [f"{CHOICE_LETTERS[i]}) {c}" for i, c in enumerate(choices_text)]
            choice_tokens = [CHOICE_LETTERS[i] for i in range(len(choices_text))]
        elif benchmark == "arc_challenge":
            choices_text = row["choices"]["text"]
            labels = row["choices"]["label"]
            answer_letter = row["answerKey"]
            question = row["question"]
            choices_display = [f"{l}) {t}" for l, t in zip(labels, choices_text)]
            choice_tokens = labels

        mc_suffix = "The answer is " if mc_format == "aligned" else "Answer:"
        raw_prompt = fewshot_prefix + f"Question: {question}\n" + "\n".join(choices_display) + f"\n{mc_suffix}"

        if use_generation:
            sys_msg = "Answer multiple choice questions with ONLY the letter of the correct option."
            prompt = format_as_chat(tokenizer, raw_prompt, system_prompt=sys_msg)
        else:
            prompt = format_as_chat(tokenizer, raw_prompt)

        prompts.append(prompt)
        answer_letters.append(answer_letter)
        all_choice_tokens.append(choice_tokens)

    if use_generation:
        logger.info("%s: batch generating %d samples, batch_size=%d", benchmark, len(prompts), batch_size)
        all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=5, batch_size=batch_size)

        correct = 0
        total = 0
        per_item = []
        for generated, answer_letter, choice_tokens in zip(all_generated, answer_letters, all_choice_tokens):
            pred_letter = extract_mcq_answer(generated, choice_tokens)
            if pred_letter is None:
                pred_letter = choice_tokens[0]
            is_correct = pred_letter == answer_letter
            correct += int(is_correct)
            total += 1
            per_item.append({"index": total - 1, "correct": is_correct, "pred": pred_letter, "gold": answer_letter})
    else:
        logger.info("%s: batch logprobs %d samples, batch_size=%d", benchmark, len(prompts), batch_size)
        all_logprobs = batch_compute_choice_logprobs(model, tokenizer, prompts, all_choice_tokens, batch_size)

        correct = 0
        total = 0
        per_item = []
        for logprobs, answer_letter, choice_tokens in zip(all_logprobs, answer_letters, all_choice_tokens):
            pred_idx = int(np.argmax(logprobs))
            pred_letter = choice_tokens[pred_idx]
            is_correct = pred_letter == answer_letter
            correct += int(is_correct)
            total += 1
            per_item.append({"index": total - 1, "correct": is_correct, "pred": pred_letter, "gold": answer_letter})

    accuracy = correct / total if total > 0 else 0.0
    return {"accuracy": accuracy, "correct": correct, "total": total, "per_item": per_item}


def format_mcq_example(row: dict, benchmark: str, mc_format: str = "aligned") -> str:
    if benchmark == "mmlu":
        choices = row["choices"]
        answer_letter = CHOICE_LETTERS[row["answer"]]
        choices_str = "\n".join(f"{CHOICE_LETTERS[i]}) {c}" for i, c in enumerate(choices))
        if mc_format == "aligned":
            return f"Question: {row['question']}\n{choices_str}\nThe answer is {answer_letter}."
        return f"Question: {row['question']}\n{choices_str}\nAnswer: {answer_letter}"
    elif benchmark == "arc_challenge":
        choices = row["choices"]["text"]
        labels = row["choices"]["label"]
        answer = row["answerKey"]
        choices_str = "\n".join(f"{l}) {t}" for l, t in zip(labels, choices))
        if mc_format == "aligned":
            return f"Question: {row['question']}\n{choices_str}\nThe answer is {answer}."
        return f"Question: {row['question']}\n{choices_str}\nAnswer: {answer}"


# ── GSM8K evaluation ──

def extract_gsm8k_answer(text: str) -> str | None:
    # Look for #### pattern first
    match = re.search(r'####\s*(.+?)(?:\n|$)', text)
    if match:
        answer = match.group(1).strip().replace(",", "")
        answer = re.sub(r'[^-\d.]', '', answer)
        return answer
    # Try to find last number
    numbers = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?', text)
    if numbers:
        return numbers[-1].replace(",", "")
    return None


def evaluate_gsm8k(model, tokenizer, num_fewshot: int, cache_dir: str,
                   batch_size: int, max_samples: int = None) -> dict:
    ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=cache_dir)
    if max_samples:
        ds = ds.select(range(min(max_samples, len(ds))))
    train_ds = load_dataset("openai/gsm8k", "main", split="train", cache_dir=cache_dir)

    # Few-shot examples
    fewshot_examples = []
    if num_fewshot > 0:
        for idx in range(min(num_fewshot, len(train_ds))):
            row = train_ds[idx]
            fewshot_examples.append(f"Question: {row['question']}\nAnswer: {row['answer']}")

    fewshot_prefix = "\n\n".join(fewshot_examples) + "\n\n" if fewshot_examples else ""

    prompts = []
    gold_answers = []
    for row in ds:
        gold_answer = row["answer"].split("####")[-1].strip().replace(",", "")
        gold_answer = re.sub(r'[^-\d.]', '', gold_answer)
        gold_answers.append(gold_answer)
        raw_prompt = fewshot_prefix + f"Question: {row['question']}\nAnswer: Let's think step by step.\n"
        prompts.append(format_as_chat(tokenizer, raw_prompt))

    logger.info("GSM8K: batch generating %d samples, batch_size=%d, max_new_tokens=256",
                len(prompts), batch_size)
    all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=256, batch_size=batch_size)

    correct = 0
    total = 0
    per_item = []
    for generated, gold in zip(all_generated, gold_answers):
        pred_answer = extract_gsm8k_answer(generated)
        is_correct = pred_answer is not None and pred_answer == gold
        correct += int(is_correct)
        total += 1
        per_item.append({
            "index": total - 1, "correct": is_correct,
            "pred": pred_answer, "gold": gold,
        })

    accuracy = correct / total if total > 0 else 0.0
    return {"accuracy": accuracy, "correct": correct, "total": total, "per_item": per_item}


# ── HumanEval evaluation ──

def evaluate_humaneval(model, tokenizer, cache_dir: str, batch_size: int, max_samples: int = None, is_instruct: bool = False) -> dict:
    ds = load_dataset("openai/openai_humaneval", "openai_humaneval", split="test", cache_dir=cache_dir)
    if max_samples:
        ds = ds.select(range(min(max_samples, len(ds))))

    prompts = []
    metadata = []
    for row in ds:
        raw_prompt = row["prompt"]
        prompt = format_as_chat(tokenizer, f"Complete the following Python function:\n\n{raw_prompt}")
        prompts.append(prompt)
        metadata.append({
            "raw_prompt": raw_prompt,
            "test_code": row["test"],
            "entry_point": row["entry_point"],
            "task_id": row["task_id"],
        })

    logger.info("HumanEval: batch generating %d samples, batch_size=%d", len(prompts), batch_size)
    all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=512, batch_size=batch_size)

    results = []
    correct = 0
    total = 0

    for generated, meta in zip(all_generated, metadata):
        entry_point = meta["entry_point"]

        if is_instruct:
            code = extract_code_from_markdown(generated)
            lines = code.split("\n")
            solution_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("def ") and entry_point in stripped:
                    continue
                if solution_lines and (line.startswith("def ") or line.startswith("class ")):
                    break
                solution_lines.append(line)
            solution = "\n".join(solution_lines)
        else:
            lines = generated.split("\n")
            solution_lines = []
            for line in lines:
                if solution_lines and (line.startswith("def ") or line.startswith("class ")):
                    break
                solution_lines.append(line)
            solution = "\n".join(solution_lines)

        full_code = meta["raw_prompt"] + solution + "\n\n" + meta["test_code"] + f"\n\ncheck({entry_point})\n"

        is_correct = run_code_safely(full_code)
        correct += int(is_correct)
        total += 1
        results.append({
            "task_id": meta["task_id"],
            "index": total - 1,
            "correct": is_correct,
            "generated": solution[:500],
        })

    accuracy = correct / total if total > 0 else 0.0
    return {"pass@1": accuracy, "correct": correct, "total": total, "per_item": results}


def run_code_safely(code: str, timeout: int = 10) -> bool:
    """Execute code in a subprocess with timeout."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        f.flush()
        tmp_path = f.name

    try:
        result = subprocess.run(
            ["python3", tmp_path],
            capture_output=True, timeout=timeout, text=True,
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, Exception):
        return False
    finally:
        os.unlink(tmp_path)


# ── Paraphrased evaluation ──

def evaluate_paraphrased(model, tokenizer, benchmark: str, para_items: list[dict],
                         num_fewshot: int, cache_dir: str, batch_size: int,
                         mc_format: str = "aligned", use_generation: bool = False,
                         is_instruct: bool = False) -> dict:
    """Evaluate on paraphrased benchmark items. Batched version."""
    if benchmark in ("mmlu", "arc_challenge"):
        if benchmark == "mmlu":
            val_ds = load_dataset("cais/mmlu", "all", split="validation", cache_dir=cache_dir)
        else:
            val_ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="validation", cache_dir=cache_dir)

        fewshot_examples = []
        if num_fewshot > 0 and val_ds is not None:
            for idx in range(min(num_fewshot, len(val_ds))):
                fewshot_examples.append(format_mcq_example(val_ds[idx], benchmark, mc_format))
        fewshot_prefix = "\n\n".join(fewshot_examples) + "\n\n" if fewshot_examples else ""

        prompts = []
        answer_letters = []
        all_choice_tokens = []
        orig_indices = []

        for row in para_items:
            orig_index = row.get("_orig_index", len(prompts))
            if benchmark == "mmlu":
                choices_text = row["choices"]
                answer_idx = row["answer"]
                answer_letter = CHOICE_LETTERS[answer_idx]
                question = row["question"]
                choices_display = [f"{CHOICE_LETTERS[i]}) {c}" for i, c in enumerate(choices_text)]
                choice_tokens = [CHOICE_LETTERS[i] for i in range(len(choices_text))]
            elif benchmark == "arc_challenge":
                choices_text = row["choices"]["text"]
                labels = row["choices"]["label"]
                answer_letter = row["answerKey"]
                question = row["question"]
                choices_display = [f"{l}) {t}" for l, t in zip(labels, choices_text)]
                choice_tokens = labels

            mc_suffix = "The answer is " if mc_format == "aligned" else "Answer:"
            raw_prompt = fewshot_prefix + f"Question: {question}\n" + "\n".join(choices_display) + f"\n{mc_suffix}"

            if use_generation:
                sys_msg = "Answer multiple choice questions with ONLY the letter of the correct option."
                prompt = format_as_chat(tokenizer, raw_prompt, system_prompt=sys_msg)
            else:
                prompt = format_as_chat(tokenizer, raw_prompt)

            prompts.append(prompt)
            answer_letters.append(answer_letter)
            all_choice_tokens.append(choice_tokens)
            orig_indices.append(orig_index)

        if use_generation:
            all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=5, batch_size=batch_size)
            correct = 0
            total = 0
            per_item = []
            for generated, answer_letter, choice_tokens, orig_idx in zip(
                all_generated, answer_letters, all_choice_tokens, orig_indices
            ):
                pred_letter = extract_mcq_answer(generated, choice_tokens)
                if pred_letter is None:
                    pred_letter = choice_tokens[0]
                is_correct = pred_letter == answer_letter
                correct += int(is_correct)
                total += 1
                per_item.append({"index": orig_idx, "correct": is_correct,
                                 "pred": pred_letter, "gold": answer_letter})
        else:
            all_logprobs = batch_compute_choice_logprobs(model, tokenizer, prompts, all_choice_tokens, batch_size)
            correct = 0
            total = 0
            per_item = []
            for logprobs, answer_letter, choice_tokens, orig_idx in zip(
                all_logprobs, answer_letters, all_choice_tokens, orig_indices
            ):
                pred_idx = int(np.argmax(logprobs))
                pred_letter = choice_tokens[pred_idx]
                is_correct = pred_letter == answer_letter
                correct += int(is_correct)
                total += 1
                per_item.append({"index": orig_idx, "correct": is_correct,
                                 "pred": pred_letter, "gold": answer_letter})

        accuracy = correct / total if total > 0 else 0.0
        return {"accuracy": accuracy, "correct": correct, "total": total, "per_item": per_item}

    elif benchmark == "gsm8k":
        train_ds = load_dataset("openai/gsm8k", "main", split="train", cache_dir=cache_dir)
        fewshot_examples = []
        if num_fewshot > 0:
            for idx in range(min(num_fewshot, len(train_ds))):
                row = train_ds[idx]
                fewshot_examples.append(f"Question: {row['question']}\nAnswer: {row['answer']}")
        fewshot_prefix = "\n\n".join(fewshot_examples) + "\n\n" if fewshot_examples else ""

        prompts = []
        gold_answers = []
        orig_indices = []
        for row in para_items:
            orig_index = row.get("_orig_index", len(prompts))
            gold_answer = row["answer"].split("####")[-1].strip().replace(",", "")
            gold_answer = re.sub(r'[^-\d.]', '', gold_answer)
            gold_answers.append(gold_answer)
            raw_prompt = fewshot_prefix + f"Question: {row['question']}\nAnswer: Let's think step by step.\n"
            prompts.append(format_as_chat(tokenizer, raw_prompt))
            orig_indices.append(orig_index)

        all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=256, batch_size=batch_size)

        correct = 0
        total = 0
        per_item = []
        for generated, gold, orig_idx in zip(all_generated, gold_answers, orig_indices):
            pred_answer = extract_gsm8k_answer(generated)
            is_correct = pred_answer is not None and pred_answer == gold
            correct += int(is_correct)
            total += 1
            per_item.append({"index": orig_idx, "correct": is_correct,
                             "pred": pred_answer, "gold": gold})

        accuracy = correct / total if total > 0 else 0.0
        return {"accuracy": accuracy, "correct": correct, "total": total, "per_item": per_item}

    elif benchmark == "humaneval":
        prompts = []
        metadata = []
        for row in para_items:
            orig_index = row.get("_orig_index", len(prompts))
            raw_prompt = row["prompt"]
            prompt = format_as_chat(tokenizer, f"Complete the following Python function:\n\n{raw_prompt}")
            prompts.append(prompt)
            metadata.append({
                "raw_prompt": raw_prompt,
                "test_code": row["test"],
                "entry_point": row["entry_point"],
                "task_id": row.get("task_id", f"HumanEval/{orig_index}"),
                "orig_index": orig_index,
            })

        all_generated = batch_generate(model, tokenizer, prompts, max_new_tokens=512, batch_size=batch_size)

        correct = 0
        total = 0
        per_item = []
        for generated, meta in zip(all_generated, metadata):
            entry_point = meta["entry_point"]

            if is_instruct:
                code = extract_code_from_markdown(generated)
                lines = code.split("\n")
                solution_lines = []
                for line in lines:
                    stripped = line.strip()
                    if stripped.startswith("def ") and entry_point in stripped:
                        continue
                    if solution_lines and (line.startswith("def ") or line.startswith("class ")):
                        break
                    solution_lines.append(line)
                solution = "\n".join(solution_lines)
            else:
                lines = generated.split("\n")
                solution_lines = []
                for line in lines:
                    if solution_lines and (line.startswith("def ") or line.startswith("class ")):
                        break
                    solution_lines.append(line)
                solution = "\n".join(solution_lines)

            full_code = meta["raw_prompt"] + solution + "\n\n" + meta["test_code"] + f"\n\ncheck({entry_point})\n"
            is_correct = run_code_safely(full_code)
            correct += int(is_correct)
            total += 1
            per_item.append({
                "task_id": meta["task_id"],
                "index": meta["orig_index"],
                "correct": is_correct,
                "generated": solution[:500],
            })

        accuracy = correct / total if total > 0 else 0.0
        return {"pass@1": accuracy, "correct": correct, "total": total, "per_item": per_item}

    raise ValueError(f"Unknown benchmark for paraphrased eval: {benchmark}")


def load_paraphrased_benchmark(paraphrase_path: str, benchmark: str):
    """Load paraphrased benchmark items and convert to the same format as HF datasets."""
    with open(paraphrase_path) as f:
        data = json.load(f)

    items = []
    for item in data:
        if not item.get("passed_qc", False):
            continue
        parsed = item.get("paraphrase_parsed") or {}
        original = item.get("original", {})
        orig_index = item.get("index", len(items))

        if benchmark == "mmlu":
            choices_raw = parsed.get("choices", original.get("choices", []))
            choices = []
            for c in choices_raw:
                m = re.match(r'^[A-Z]\)\s*(.*)', c)
                choices.append(m.group(1) if m else c)
            answer_letter = parsed.get("answer", "")
            answer_idx = ord(answer_letter) - ord("A") if answer_letter else original.get("answer", 0)
            items.append({
                "question": parsed.get("question", original.get("question", "")),
                "choices": choices,
                "answer": answer_idx,
                "_orig_index": orig_index,
            })
        elif benchmark == "arc_challenge":
            choices_raw = parsed.get("choices", original.get("choices", []))
            if isinstance(choices_raw, list):
                choices_text, choices_label = [], []
                for c in choices_raw:
                    m = re.match(r'^([A-Z])\)\s*(.*)', c)
                    if m:
                        choices_label.append(m.group(1))
                        choices_text.append(m.group(2))
                    else:
                        choices_label.append("")
                        choices_text.append(c)
            elif isinstance(choices_raw, dict):
                choices_text = choices_raw.get("text", [])
                choices_label = choices_raw.get("label", [])
            else:
                choices_text, choices_label = [], []
            choices_text = parsed.get("choices_text", choices_text)
            choices_label = parsed.get("choices_label", choices_label)
            items.append({
                "question": parsed.get("question", original.get("question", "")),
                "choices": {"text": choices_text, "label": choices_label},
                "answerKey": parsed.get("answer", original.get("answerKey", original.get("answer", ""))),
                "_orig_index": orig_index,
            })
        elif benchmark == "gsm8k":
            items.append({
                "question": parsed.get("question", original.get("question", "")),
                "answer": original.get("answer", ""),
                "_orig_index": orig_index,
            })
        elif benchmark == "humaneval":
            items.append({
                "prompt": parsed.get("prompt", original.get("prompt", "")),
                "test": original.get("test", ""),
                "entry_point": original.get("entry_point", ""),
                "task_id": original.get("task_id", f"HumanEval/{orig_index}"),
                "_orig_index": orig_index,
            })

    logger.info("Loaded %d QC-passed paraphrased items for %s from %s",
                len(items), benchmark, paraphrase_path)
    return items

def main():
    parser = argparse.ArgumentParser(description="Evaluate model on contamination benchmarks (batch version)")
    parser.add_argument("--model-path", type=str, required=True,
                        help="Path to model checkpoint (merged or HF model name)")
    parser.add_argument("--benchmarks", type=str, nargs="+",
                        default=["mmlu", "gsm8k", "arc_challenge", "humaneval"],
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"],
                        help="Benchmarks to evaluate")
    parser.add_argument("--adapter-path", type=str, default=None,
                        help="Path to LoRA adapter. If set, loads base model from --model-path and adapter separately.")
    parser.add_argument("--paraphrase-dir", type=str, default=None,
                        help="Directory with paraphrase JSONs. If set, evaluates on paraphrased items instead of originals.")
    parser.add_argument("--output-dir", type=str, required=True,
                        help="Output directory for evaluation results")
    parser.add_argument("--max-samples", type=int, default=None,
                        help="Max samples per benchmark (for dry-run testing)")
    parser.add_argument("--mc-format", type=str, default="aligned",
                        choices=["aligned", "legacy"],
                        help="MC answer format: 'aligned' uses 'The answer is X.' (matches SFT), 'legacy' uses 'Answer: X'")
    parser.add_argument("--batch-size", type=int, default=16,
                        help="Batch size for evaluation (default: 16)")
    parser.add_argument("--instruct", action="store_true",
                        help="Enable Instruct model evaluation (generation-based MCQ, markdown code extraction)")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache",
                        help="HuggingFace cache directory")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model, tokenizer = load_model_and_tokenizer(args.model_path, args.cache_dir, args.adapter_path)

    is_instruct = args.instruct or "instruct" in args.model_path.lower()

    all_results = {
        "model_path": args.model_path,
        "adapter_path": args.adapter_path,
        "batch_size": args.batch_size,
        "benchmarks": {},
    }

    for benchmark in args.benchmarks:
        is_paraphrased = args.paraphrase_dir is not None
        logger.info("Evaluating %s%s", benchmark, " (paraphrased)" if is_paraphrased else "")
        cfg = BENCHMARK_CONFIGS[benchmark]

        if is_paraphrased:
            para_path = os.path.join(args.paraphrase_dir, f"{benchmark}_paraphrases.json")
            if not os.path.exists(para_path):
                logger.warning("SKIP %s: paraphrase file not found at %s", benchmark, para_path)
                continue
            para_items = load_paraphrased_benchmark(para_path, benchmark)
            if not para_items:
                logger.warning("SKIP %s: no QC-passed paraphrased items", benchmark)
                continue
            result = evaluate_paraphrased(model, tokenizer, benchmark, para_items,
                                          cfg["num_fewshot"], args.cache_dir, args.batch_size,
                                          mc_format=args.mc_format,
                                          use_generation=is_instruct,
                                          is_instruct=is_instruct)
        elif benchmark in ("mmlu", "arc_challenge"):
            result = evaluate_mcq(model, tokenizer, benchmark, cfg["num_fewshot"],
                                  args.cache_dir, args.batch_size, args.max_samples,
                                  mc_format=args.mc_format,
                                  use_generation=is_instruct)
        elif benchmark == "gsm8k":
            result = evaluate_gsm8k(model, tokenizer, cfg["num_fewshot"],
                                    args.cache_dir, args.batch_size, args.max_samples)
        elif benchmark == "humaneval":
            result = evaluate_humaneval(model, tokenizer, args.cache_dir, args.batch_size, args.max_samples,
                                        is_instruct=is_instruct)

        all_results["benchmarks"][benchmark] = result
        metric_name = cfg["metric"]
        metric_val = result.get(metric_name, result.get("accuracy", 0))
        logger.info("%s %s: %.4f (%d/%d)",
                    benchmark, metric_name, metric_val,
                    result["correct"], result["total"])

        bench_file = output_dir / f"{benchmark}_results.json"
        with open(bench_file, "w") as f:
            json.dump({"benchmark": benchmark, **result}, f, indent=2, ensure_ascii=False)
        logger.info("Saved %s to %s", benchmark, bench_file)

    output_dir.mkdir(parents=True, exist_ok=True)
    # Save results
    results_file = output_dir / "eval_results.json"
    with open(results_file, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s", results_file)

    # Save per-item correctness matrix (for IRT)
    correctness_matrix = {}
    for benchmark, result in all_results["benchmarks"].items():
        correctness_matrix[benchmark] = [
            item["correct"] for item in result["per_item"]
        ]
    matrix_file = output_dir / "correctness_matrix.json"
    with open(matrix_file, "w") as f:
        json.dump(correctness_matrix, f)
    logger.info("Correctness matrix saved to %s", matrix_file)

    # Save structured item responses (for IRT analysis)
    item_responses = []
    for benchmark, result in all_results["benchmarks"].items():
        for item in result["per_item"]:
            item_responses.append({
                "item_id": f"{benchmark}_{item.get('index', item.get('task_id', ''))}",
                "benchmark": benchmark,
                "correct": item["correct"],
                "model_answer": str(item.get("pred", item.get("generated", ""))),
                "gold_answer": str(item.get("gold", "")),
            })
    responses_file = output_dir / "item_responses.json"
    with open(responses_file, "w") as f:
        json.dump(item_responses, f, indent=2, ensure_ascii=False)
    logger.info("Item responses saved to %s", responses_file)

    # Sentinel file so cron can distinguish normal completion from crash
    (output_dir / ".done").touch()
    logger.info("Sentinel .done written to %s", output_dir)


if __name__ == "__main__":
    main()
