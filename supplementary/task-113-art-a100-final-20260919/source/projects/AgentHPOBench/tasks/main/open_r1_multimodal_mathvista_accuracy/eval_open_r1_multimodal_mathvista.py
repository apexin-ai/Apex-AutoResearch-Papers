#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import random
import re
import time
from io import BytesIO
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
from PIL import Image
from qwen_vl_utils import process_vision_info
from transformers import AutoProcessor, Qwen2VLForConditionalGeneration


ROOT = Path(".")
DATA = ROOT / "data/formal/open_r1_multimodal_mathvista/testmini.parquet"
MODEL = ROOT / "models/Qwen/Qwen2-VL-2B-Instruct"
PAPER_ANCHOR_ACCURACY = 51.6


def normalize_text(text: Any) -> str:
    value = str(text).strip().lower()
    value = value.replace("−", "-").replace("°", " degrees")
    value = re.sub(r"final answer\s*[:：]", "", value)
    value = re.sub(r"\\boxed\{([^{}]+)\}", r"\1", value)
    value = re.sub(r"[\s,]+", " ", value)
    value = re.sub(r"^[\"'`]+|[\"'`.。]+$", "", value)
    return value.strip()


def extract_prediction(text: str) -> str:
    text = text.strip()
    patterns = [
        r"final answer\s*[:：]\s*(.+)$",
        r"answer\s*[:：]\s*(.+)$",
        r"therefore[, ]+(?:the answer is)?\s*(.+)$",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.I | re.S)
        if match:
            return match.group(1).strip().splitlines()[-1].strip()
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines[-1] if lines else text


def numeric_values(text: str) -> list[float]:
    values = []
    for raw in re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", text.replace(",", "")):
        try:
            values.append(float(raw))
        except ValueError:
            pass
    return values


def is_correct(prediction: str, answer: Any, row: pd.Series) -> bool:
    pred = normalize_text(extract_prediction(prediction))
    gold = normalize_text(answer)
    if not gold:
        return False

    if str(row.get("question_type")) == "multi_choice":
        choices = row.get("choices")
        if isinstance(choices, np.ndarray):
            choices = choices.tolist()
        if isinstance(choices, list):
            letters = "abcdefghijklmnopqrstuvwxyz"
            for idx, choice in enumerate(choices):
                choice_norm = normalize_text(choice)
                if choice_norm == gold and idx < len(letters):
                    if pred == letters[idx] or pred.startswith(f"{letters[idx]} ") or pred.startswith(f"({letters[idx]})"):
                        return True
                    if re.search(rf"\b{letters[idx]}\b", pred) and len(pred) <= 8:
                        return True
                if choice_norm and (pred == choice_norm or choice_norm in pred):
                    return choice_norm == gold
        return pred == gold or gold in pred

    if str(row.get("answer_type")) in {"integer", "float"}:
        gold_vals = numeric_values(gold)
        pred_vals = numeric_values(pred)
        if not gold_vals or not pred_vals:
            return False
        precision = row.get("precision")
        tol = 1e-4
        try:
            if precision == precision:
                tol = max(tol, 0.5 * (10 ** (-int(float(precision)))))
        except Exception:
            pass
        gold_val = gold_vals[-1]
        return any(abs(value - gold_val) <= max(tol, abs(gold_val) * 1e-3) for value in pred_vals)

    return pred == gold or gold in pred


def make_prompt(row: pd.Series, prompt_style: str) -> str:
    question = str(row.get("query") or row.get("question") or "").strip()
    choices = row.get("choices")
    if isinstance(choices, np.ndarray):
        choices = choices.tolist()
    if isinstance(choices, list) and choices:
        options = "\n".join(f"{chr(65 + idx)}. {choice}" for idx, choice in enumerate(choices))
        question = f"{question}\nOptions:\n{options}"
    if prompt_style == "cot":
        return question + "\nThink briefly, then write exactly one line at the end: Final answer: <answer>."
    if prompt_style == "short_cot":
        return question + "\nReason in one short sentence, then write: Final answer: <answer>."
    return question + "\nAnswer directly with only the final answer."


def load_image(row: pd.Series) -> Image.Image:
    image_obj = row.get("decoded_image")
    if isinstance(image_obj, dict) and image_obj.get("bytes") is not None:
        return Image.open(BytesIO(image_obj["bytes"])).convert("RGB")
    raw = row.get("image")
    if isinstance(raw, dict) and raw.get("bytes") is not None:
        return Image.open(BytesIO(raw["bytes"])).convert("RGB")
    raise ValueError(f"missing image bytes for pid={row.get('pid')}")


def generate_answer(model, processor, row: pd.Series, args: argparse.Namespace) -> str:
    image = load_image(row)
    prompt = make_prompt(row, args.prompt_style)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": prompt},
            ],
        }
    ]
    text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(text=[text], images=image_inputs, videos=video_inputs, padding=True, return_tensors="pt").to(model.device)
    generation_kwargs = {
        "max_new_tokens": args.max_new_tokens,
        "do_sample": args.temperature > 0,
        "temperature": max(args.temperature, 1e-5),
        "top_p": args.top_p,
    }
    with torch.no_grad():
        output_ids = model.generate(**inputs, **generation_kwargs)
    trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, output_ids)]
    return processor.batch_decode(trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0].strip()


def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    if not DATA.exists():
        raise FileNotFoundError(f"missing {DATA}; run dataset_download.sh first")
    if not MODEL.exists():
        raise FileNotFoundError(f"missing local model {MODEL}")

    df = pd.read_parquet(DATA).sort_values("pid").reset_index(drop=True)
    if args.max_examples > 0:
        df = df.head(args.max_examples).copy()

    processor = AutoProcessor.from_pretrained(str(MODEL), local_files_only=True, trust_remote_code=True)
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        str(MODEL),
        local_files_only=True,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()

    started = time.time()
    records = []
    correct = 0
    by_type: dict[str, list[bool]] = {}
    for idx, row in df.iterrows():
        pred = generate_answer(model, processor, row, args)
        ok = is_correct(pred, row.get("answer"), row)
        correct += int(ok)
        answer_type = str(row.get("answer_type"))
        by_type.setdefault(answer_type, []).append(ok)
        records.append(
            {
                "pid": str(row.get("pid")),
                "answer_type": answer_type,
                "question_type": str(row.get("question_type")),
                "answer": str(row.get("answer")),
                "prediction": pred,
                "correct": bool(ok),
            }
        )

    accuracy = 100.0 * correct / max(1, len(records))
    payload = {
        "task": "open-r1-multimodal MathVista-mini Qwen2-VL-2B evaluation",
        "repo": "open-r1-multimodal",
        "dataset": "MathVista-mini",
        "metric": "accuracy_percent",
        "higher_is_better": True,
        "accuracy_percent": accuracy,
        "correct": correct,
        "total": len(records),
        "accuracy_by_answer_type": {name: 100.0 * sum(vals) / max(1, len(vals)) for name, vals in sorted(by_type.items())},
        "examples": records[: min(len(records), args.save_examples)],
        "seconds": round(time.time() - started, 3),
        "config": {
            "prompt_style": args.prompt_style,
            "max_new_tokens": args.max_new_tokens,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "max_examples": args.max_examples,
            "seed": args.seed,
        },
        "paper_anchor_accuracy_percent": PAPER_ANCHOR_ACCURACY,
        "paper_anchor_source": "open-r1-multimodal README Mathvista-mini Qwen2-VL-2B-Instruct(w.o reasoning)",
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
    }
    del model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--prompt-style", choices=["direct", "cot", "short_cot"], default="direct")
    parser.add_argument("--max-new-tokens", type=int, default=32)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--max-examples", type=int, default=0)
    parser.add_argument("--save-examples", type=int, default=32)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    args.results_dir.mkdir(parents=True, exist_ok=True)
    payload = evaluate(args)
    (args.results_dir / "results.json").write_text(json.dumps(payload, indent=2))
    print("RESULT_JSON " + json.dumps(payload, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
