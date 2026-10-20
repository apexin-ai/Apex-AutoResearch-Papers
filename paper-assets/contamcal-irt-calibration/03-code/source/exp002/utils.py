import json
import logging
import os
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

BENCHMARK_CONFIGS = {
    "mmlu": ("cais/mmlu", "all", "test"),
    "gsm8k": ("openai/gsm8k", "main", "test"),
    "arc_challenge": ("allenai/ai2_arc", "ARC-Challenge", "test"),
    "humaneval": ("openai/openai_humaneval", "openai_humaneval", "test"),
}


def load_model_and_tokenizer(model_path: str, adapter_path: str = None, cache_dir: str = None):
    cache_dir = cache_dir or HF_HOME
    if adapter_path:
        logger.info("Loading base model: %s + LoRA adapter: %s", model_path, adapter_path)
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, cache_dir=cache_dir, trust_remote_code=True
        )
        base_model = AutoModelForCausalLM.from_pretrained(
            model_path, cache_dir=cache_dir,
            torch_dtype=torch.bfloat16, trust_remote_code=True,
            device_map="auto",
        )
        from peft import PeftModel
        model = PeftModel.from_pretrained(base_model, adapter_path)
        model = model.merge_and_unload()
    else:
        logger.info("Loading model: %s", model_path)
        tokenizer = AutoTokenizer.from_pretrained(
            model_path, cache_dir=cache_dir, trust_remote_code=True
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_path, cache_dir=cache_dir,
            torch_dtype=torch.bfloat16, trust_remote_code=True,
            device_map="auto",
        )
    model.eval()
    return model, tokenizer


def load_benchmark_dataset(benchmark: str, cache_dir: str = None):
    from datasets import load_dataset
    cache_dir = cache_dir or HF_HOME
    if benchmark not in BENCHMARK_CONFIGS:
        raise ValueError(f"Unknown benchmark: {benchmark}")
    name, subset, split = BENCHMARK_CONFIGS[benchmark]
    return load_dataset(name, subset, split=split, cache_dir=cache_dir)


def format_benchmark_item(row: dict, benchmark: str) -> str:
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


def format_question_text(row: dict, benchmark: str) -> str:
    if benchmark in ("mmlu", "gsm8k", "arc_challenge"):
        return row["question"]
    elif benchmark == "humaneval":
        return row["prompt"][:200]
    else:
        raise ValueError(f"Unknown benchmark: {benchmark}")


def make_item_id(benchmark: str, index: int) -> str:
    return f"{benchmark}_{index:04d}"


def save_signal_results(results: list[dict], output_dir: str, signal_name: str, benchmark: str):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f"signal_{signal_name}_{benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)
    return out_file


def load_sft_texts(data_path: str) -> list[str]:
    texts = []
    with open(data_path) as f:
        for line in f:
            row = json.loads(line)
            messages = row.get("messages", [])
            if isinstance(messages, str):
                messages = json.loads(messages)
            parts = []
            for msg in messages:
                if msg.get("role") in ("user", "assistant"):
                    parts.append(msg["content"])
            if parts:
                texts.append(" ".join(parts))
    return texts


def infer_dosage_from_path(adapter_path: str) -> str:
    name = Path(adapter_path).parent.name if "lora_adapter" in adapter_path else Path(adapter_path).name
    for part in name.split("_"):
        if part.startswith("d") and part[1:].isdigit():
            return part[1:]
    return None
