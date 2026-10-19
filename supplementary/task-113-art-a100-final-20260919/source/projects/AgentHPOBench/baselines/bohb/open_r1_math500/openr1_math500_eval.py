#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import time
from pathlib import Path
from typing import Any

from latex2sympy2_extended import NormalizationConfig
from math_verify import LatexExtractionConfig, parse, verify
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams


ANSWER_EXTRACTION = [
    LatexExtractionConfig(
        normalization_config=NormalizationConfig(
            nits=False,
            malformed_operators=False,
            basic_latex=True,
            equations=True,
            boxed="all",
            units=True,
        ),
        boxed_match_priority=0,
        try_extract_without_anchor=False,
    )
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def select_records(records: list[dict[str, Any]], limit: int | None, seed: int) -> list[dict[str, Any]]:
    if limit is None or limit <= 0 or limit >= len(records):
        return records
    rng = random.Random(seed)
    indices = list(range(len(records)))
    rng.shuffle(indices)
    selected = sorted(indices[:limit])
    return [records[i] for i in selected]


def make_prompt(tokenizer: AutoTokenizer, problem: str) -> str:
    user = (
        problem.strip()
        + "\n\nSolve the problem. Put only the final answer in \\boxed{} at the end."
    )
    messages = [{"role": "user", "content": user}]
    try:
        return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    except Exception:
        return user + "\n\nAnswer:"


def parse_gold(record: dict[str, Any]):
    for key in ("answer", "solution"):
        value = str(record.get(key, "")).strip()
        if not value:
            continue
        parsed = parse(value, extraction_mode="first_match")
        if parsed:
            return parsed
    return []


def parse_prediction(text: str):
    return parse(
        text,
        extraction_config=ANSWER_EXTRACTION,
        extraction_mode="first_match",
    )


def score_prediction(record: dict[str, Any], completion: str) -> dict[str, Any]:
    gold = parse_gold(record)
    pred = parse_prediction(completion)
    correct = False
    error = None
    if gold and pred:
        try:
            correct = bool(verify(gold, pred))
        except Exception as exc:  # noqa: BLE001
            error = repr(exc)
    return {
        "unique_id": record.get("unique_id"),
        "subject": record.get("subject"),
        "level": record.get("level"),
        "gold_answer": record.get("answer"),
        "gold_parsed": [str(x) for x in gold],
        "prediction_parsed": [str(x) for x in pred],
        "correct": correct,
        "verify_error": error,
        "completion": completion,
    }

def generate_with_transformers(args: argparse.Namespace, tokenizer: AutoTokenizer, prompts: list[str]) -> list[str]:
    import torch
    from transformers import AutoModelForCausalLM

    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16 if args.dtype == "float16" else torch.float32
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        trust_remote_code=True,
        torch_dtype=dtype,
        device_map={"": 0} if torch.cuda.is_available() else None,
    )
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"
    model.eval()

    completions: list[str] = []
    batch_size = max(1, int(os.environ.get("OPENR1_HF_BATCH_SIZE", "4")))
    for start in range(0, len(prompts), batch_size):
        batch = prompts[start : start + batch_size]
        encoded = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=args.max_model_len)
        encoded = {key: value.to(model.device) for key, value in encoded.items()}
        gen_kwargs = {
            "max_new_tokens": args.max_new_tokens,
            "pad_token_id": tokenizer.pad_token_id,
            "eos_token_id": tokenizer.eos_token_id,
        }
        if args.temperature and args.temperature > 0:
            gen_kwargs.update({"do_sample": True, "temperature": args.temperature, "top_p": args.top_p})
        else:
            gen_kwargs.update({"do_sample": False})
        with torch.inference_mode():
            generated = model.generate(**encoded, **gen_kwargs)
        prompt_len = encoded["input_ids"].shape[1]
        completions.extend(tokenizer.batch_decode(generated[:, prompt_len:], skip_special_tokens=True))
    return completions


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--predictions", type=Path)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--subset-seed", type=int, default=42)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=-1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--max-model-len", type=int, default=4096)
    parser.add_argument("--gpu-memory-utilization", type=float, default=0.72)
    parser.add_argument("--tensor-parallel-size", type=int, default=1)
    parser.add_argument("--enforce-eager", action="store_true")
    args = parser.parse_args()

    started = time.time()
    records = select_records(read_jsonl(args.data), args.limit, args.subset_seed)
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    prompts = [make_prompt(tokenizer, str(record["problem"])) for record in records]

    backend = os.environ.get("OPENR1_EVAL_BACKEND", "vllm").strip().lower()
    if backend == "hf":
        completions = generate_with_transformers(args, tokenizer, prompts)
    else:
        llm = LLM(
            model=args.model,
            tokenizer=args.model,
            trust_remote_code=True,
            dtype=args.dtype,
            max_model_len=args.max_model_len,
            gpu_memory_utilization=args.gpu_memory_utilization,
            tensor_parallel_size=args.tensor_parallel_size,
            enforce_eager=args.enforce_eager,
            seed=args.seed,
        )
        sampling = SamplingParams(
            max_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            top_k=args.top_k,
            seed=args.seed,
        )
        outputs = llm.generate(prompts, sampling, use_tqdm=True)
        completions = [output.outputs[0].text for output in outputs]

    predictions = []
    correct = 0
    for record, completion in zip(records, completions):
        scored = score_prediction(record, completion)
        predictions.append(scored)
        correct += int(scored["correct"])

    accuracy = correct / len(records) if records else 0.0
    result = {
        "model": args.model,
        "data": str(args.data),
        "num_total": len(records),
        "num_correct": correct,
        "accuracy": accuracy,
        "accuracy_percent": accuracy * 100.0,
        "config": {
            "max_new_tokens": args.max_new_tokens,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "top_k": args.top_k,
            "seed": args.seed,
            "subset_seed": args.subset_seed,
            "limit": args.limit,
            "max_model_len": args.max_model_len,
            "backend": backend,
        },
        "elapsed_sec": time.time() - started,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    pred_path = args.predictions or args.output.with_suffix(".predictions.jsonl")
    pred_path.parent.mkdir(parents=True, exist_ok=True)
    with pred_path.open("w") as f:
        for item in predictions:
            f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    raise SystemExit(main())
