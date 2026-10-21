"""
SFT training data preparation with controlled contamination injection.

Mixes paraphrased benchmark items into a base SFT dataset at various dosage
levels (0%, 5%, 25%, 50%, 100% of benchmark items).

Input:  Paraphrase JSONs from paraphrase_gen.py + base SFT dataset (SlimOrca)
Output: JSONL files with chat-format messages for each dosage level
"""

import argparse
import json
import logging
import os
import random
from pathlib import Path

from datasets import load_dataset
from tqdm import tqdm

logger = logging.getLogger(__name__)

HF_HOME = os.environ.get("HF_HOME", "/root/autodl-tmp/.hf_cache")
os.environ["HF_HOME"] = HF_HOME

DOSAGE_LEVELS = [0, 5, 25, 50, 100]

BENCHMARK_TO_QA = {
    "mmlu": "mcq",
    "arc_challenge": "mcq",
    "gsm8k": "math",
    "humaneval": "code",
}


def format_mcq_as_chat(item: dict) -> dict:
    """Convert a paraphrased MCQ item to chat message format."""
    parsed = item.get("paraphrase_parsed") or item.get("original", {})

    question = parsed.get("question", "")
    choices = parsed.get("choices", [])
    answer = parsed.get("answer", "")

    if isinstance(choices, list):
        choices_str = "\n".join(choices)
    else:
        choices_str = str(choices)

    user_msg = f"Question: {question}\n{choices_str}"
    assistant_msg = f"The answer is {answer}."

    return {
        "messages": [
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": assistant_msg},
        ]
    }


def format_math_as_chat(item: dict) -> dict:
    """Convert a paraphrased GSM8K item to chat message format."""
    parsed = item.get("paraphrase_parsed") or {}
    original = item.get("original", {})

    question = parsed.get("question", original.get("question", ""))
    answer = original.get("full_answer", original.get("answer", ""))

    return {
        "messages": [
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }


def format_code_as_chat(item: dict) -> dict:
    """Convert a paraphrased HumanEval item to chat message format."""
    original = item.get("original", {})
    paraphrased_prompt = item.get("paraphrased_prompt", original.get("prompt", ""))
    solution = original.get("canonical_solution", "")

    user_msg = f"Complete the following Python function:\n\n```python\n{paraphrased_prompt}```"
    assistant_msg = f"```python\n{paraphrased_prompt}{solution}```"

    return {
        "messages": [
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": assistant_msg},
        ]
    }


FORMAT_FNS = {
    "mcq": format_mcq_as_chat,
    "math": format_math_as_chat,
    "code": format_code_as_chat,
}


def load_paraphrases(paraphrase_dir: str) -> dict[str, list[dict]]:
    """Load all paraphrase JSONs from directory, return {benchmark: [items]}."""
    paraphrase_dir = Path(paraphrase_dir)
    all_paraphrases = {}

    for f in sorted(paraphrase_dir.glob("*_paraphrases.json")):
        benchmark = f.stem.replace("_paraphrases", "")
        with open(f) as fh:
            data = json.load(fh)
        # Filter to QC-passed items only
        passed = [item for item in data if item.get("passed_qc", False)]
        all_paraphrases[benchmark] = passed
        logger.info("Loaded %d/%d QC-passed paraphrases for %s", len(passed), len(data), benchmark)

    return all_paraphrases


def load_base_sft_data(dataset_name: str, cache_dir: str, max_samples: int = 50000) -> list[dict]:
    """Load base SFT dataset and convert to chat message format."""
    logger.info("Loading base SFT dataset: %s (max %d samples)", dataset_name, max_samples)

    ds = load_dataset(dataset_name, split="train", cache_dir=cache_dir)

    if len(ds) > max_samples:
        ds = ds.shuffle(seed=42).select(range(max_samples))

    messages_list = []
    for row in tqdm(ds, desc="Processing base SFT data"):
        # Handle different dataset formats
        if "conversations" in row:
            # SlimOrca / ShareGPT format
            convs = row["conversations"]
            msgs = []
            for c in convs:
                role_map = {"human": "user", "gpt": "assistant", "system": "system"}
                role = role_map.get(c.get("from", ""), c.get("from", ""))
                if role in ("user", "assistant", "system"):
                    msgs.append({"role": role, "content": c.get("value", "")})
            if any(m["role"] == "user" for m in msgs) and any(m["role"] == "assistant" for m in msgs):
                messages_list.append({"messages": msgs})
        elif "messages" in row:
            messages_list.append({"messages": row["messages"]})
        elif "instruction" in row and "output" in row:
            msgs = [
                {"role": "user", "content": row["instruction"]},
                {"role": "assistant", "content": row["output"]},
            ]
            if row.get("input"):
                msgs[0]["content"] += f"\n\nInput: {row['input']}"
            messages_list.append({"messages": msgs})

    logger.info("Loaded %d base SFT samples", len(messages_list))
    return messages_list


def convert_paraphrases_to_chat(paraphrases: dict[str, list[dict]]) -> list[dict]:
    """Convert all paraphrases to chat message format.

    Each item carries _source (benchmark) and _orig_index for contamination label tracking.
    """
    chat_items = []
    for benchmark, items in paraphrases.items():
        qa_type = BENCHMARK_TO_QA.get(benchmark, "mcq")
        format_fn = FORMAT_FNS[qa_type]
        for item in items:
            chat_item = format_fn(item)
            chat_item["_source"] = benchmark
            chat_item["_orig_index"] = item.get("index", len(chat_items))
            chat_items.append(chat_item)
    return chat_items


def mix_data(base_data: list[dict], contam_data: list[dict], dosage: int,
             seed: int) -> tuple[list[dict], list[dict]]:
    """Mix contamination data into base data at specified dosage level.

    dosage=N means N% of contam_data items are included.
    Returns (mixed_data, selected_contam_items) for label tracking.
    """
    rng = random.Random(seed)

    if dosage == 0:
        mixed = list(base_data)
        selected = []
    elif dosage == 100:
        selected = list(contam_data)
        mixed = list(base_data) + selected
    else:
        n_contam = max(1, int(len(contam_data) * dosage / 100))
        selected = rng.sample(contam_data, min(n_contam, len(contam_data)))
        mixed = list(base_data) + selected

    rng.shuffle(mixed)
    return mixed, selected


def write_jsonl(data: list[dict], output_path: Path):
    with open(output_path, "w") as f:
        for item in data:
            # Remove internal metadata fields
            out = {k: v for k, v in item.items() if not k.startswith("_")}
            f.write(json.dumps(out, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Prepare SFT training data with contamination injection")
    parser.add_argument("--paraphrase-dir", type=str, required=True,
                        help="Directory containing paraphrase JSON files")
    parser.add_argument("--base-sft-data", type=str, default="Open-Orca/SlimOrca",
                        help="HuggingFace dataset name for base SFT data")
    parser.add_argument("--dosage", type=int, nargs="+", default=DOSAGE_LEVELS,
                        help="Dosage levels (percent of benchmark items to include)")
    parser.add_argument("--output-dir", type=str, required=True,
                        help="Output directory for mixed JSONL files")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for reproducibility")
    parser.add_argument("--max-base-samples", type=int, default=50000,
                        help="Maximum number of base SFT samples")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache",
                        help="HuggingFace cache directory")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    paraphrases = load_paraphrases(args.paraphrase_dir)
    if not paraphrases:
        logger.error("No paraphrase files found in %s", args.paraphrase_dir)
        return

    base_data = load_base_sft_data(args.base_sft_data, args.cache_dir, args.max_base_samples)
    contam_data = convert_paraphrases_to_chat(paraphrases)
    logger.info("Total contamination items: %d", len(contam_data))

    # Per-benchmark breakdown
    for benchmark, items in paraphrases.items():
        logger.info("  %s: %d items", benchmark, len(items))

    # Track total items per benchmark for label generation
    benchmark_sizes = {}
    for benchmark in paraphrases:
        if benchmark == "mmlu":
            from datasets import load_dataset as _ld
            _ds = _ld("cais/mmlu", "all", split="test", cache_dir=args.cache_dir)
        elif benchmark == "gsm8k":
            from datasets import load_dataset as _ld
            _ds = _ld("openai/gsm8k", "main", split="test", cache_dir=args.cache_dir)
        elif benchmark == "arc_challenge":
            from datasets import load_dataset as _ld
            _ds = _ld("allenai/ai2_arc", "ARC-Challenge", split="test", cache_dir=args.cache_dir)
        elif benchmark == "humaneval":
            from datasets import load_dataset as _ld
            _ds = _ld("openai/openai_humaneval", "openai_humaneval", split="test", cache_dir=args.cache_dir)
        else:
            continue
        benchmark_sizes[benchmark] = len(_ds)

    for dosage in args.dosage:
        mixed, selected = mix_data(base_data, contam_data, dosage, args.seed)
        output_file = output_dir / f"sft_dosage_{dosage:03d}.jsonl"
        write_jsonl(mixed, output_file)
        n_contam_in_mix = len(selected)
        logger.info("Dosage %d%%: %d total samples (%d base + %d contam) -> %s",
                     dosage, len(mixed), len(base_data), n_contam_in_mix, output_file)

        # Ground-truth contamination labels: per-benchmark, per-item 0/1
        contaminated_indices = {}
        for item in selected:
            src = item.get("_source")
            idx = item.get("_orig_index")
            if src and idx is not None:
                contaminated_indices.setdefault(src, set()).add(idx)

        for benchmark, total_items in benchmark_sizes.items():
            contam_set = contaminated_indices.get(benchmark, set())
            labels = [1 if i in contam_set else 0 for i in range(total_items)]
            label_file = output_dir / f"contamination_labels_{benchmark}_d{dosage:03d}.json"
            with open(label_file, "w") as f:
                json.dump({
                    "benchmark": benchmark,
                    "dosage": dosage,
                    "total_items": total_items,
                    "contaminated_count": sum(labels),
                    "labels": labels,
                }, f, indent=2)
            logger.info("  Labels %s d%d%%: %d/%d contaminated -> %s",
                        benchmark, dosage, sum(labels), total_items, label_file)

    # Save metadata
    meta = {
        "base_dataset": args.base_sft_data,
        "base_samples": len(base_data),
        "contam_samples_total": len(contam_data),
        "dosage_levels": args.dosage,
        "seed": args.seed,
        "benchmarks": {k: len(v) for k, v in paraphrases.items()},
    }
    with open(output_dir / "data_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    logger.info("Metadata saved to %s", output_dir / "data_meta.json")


if __name__ == "__main__":
    main()
