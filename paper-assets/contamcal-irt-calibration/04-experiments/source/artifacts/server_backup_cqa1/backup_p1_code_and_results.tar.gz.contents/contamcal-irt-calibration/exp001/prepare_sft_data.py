"""
SFT training data preparation with controlled contamination injection.

Mixes paraphrased benchmark items into a base SFT dataset at various dosage
levels (0%, 5%, 25%, 50%, 100% of benchmark items).

Input:  Paraphrase JSONs from paraphrase_gen.py + base SFT dataset (local JSONL)
Output: JSONL files with chat-format messages for each dosage level
"""

import argparse
import json
import logging
import random
from pathlib import Path

logger = logging.getLogger(__name__)

DOSAGE_LEVELS = [0, 5, 25, 50, 100]

BENCHMARK_TO_QA = {
    "mmlu": "mcq",
    "arc_challenge": "mcq",
    "gsm8k": "math",
    "humaneval": "code",
}


def format_mcq_as_chat(item: dict) -> dict:
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


def load_paraphrases(paraphrase_dir: str, benchmarks: list[str] | None = None) -> tuple[dict, dict]:
    """Load ALL paraphrase JSONs (no QC filtering per D010).

    Returns:
        (paraphrases dict, qc_stats dict)
    """
    paraphrase_dir = Path(paraphrase_dir)
    all_paraphrases = {}
    qc_stats = {}

    for f in sorted(paraphrase_dir.glob("*_paraphrases.json")):
        benchmark = f.stem.replace("_paraphrases", "")
        if benchmarks and benchmark not in benchmarks:
            continue
        with open(f) as fh:
            data = json.load(fh)
        qc_passed = sum(1 for item in data if item.get("passed_qc", False))
        qc_stats[benchmark] = {
            "total": len(data),
            "qc_passed": qc_passed,
            "qc_failed": len(data) - qc_passed,
            "pass_rate": round(qc_passed / len(data), 4) if data else 0,
        }
        all_paraphrases[benchmark] = data
        logger.info("Loaded %d paraphrases for %s (QC passed: %d/%d, using ALL per D010)",
                     len(data), benchmark, qc_passed, len(data))

    return all_paraphrases, qc_stats


def load_base_from_jsonl(path: str) -> list[dict]:
    """Load base SFT data from local JSONL file."""
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    logger.info("Loaded %d base SFT samples from %s", len(data), path)
    return data


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
            out = {k: v for k, v in item.items() if not k.startswith("_")}
            f.write(json.dumps(out, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Prepare SFT training data with contamination injection")
    parser.add_argument("--paraphrase-dir", type=str, required=True)
    parser.add_argument("--base-data", type=str, required=True,
                        help="Path to base SFT JSONL file (e.g. sft_dosage_000.jsonl)")
    parser.add_argument("--dosage", type=int, nargs="+", default=[5, 25, 50, 100])
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--benchmarks", type=str, default=None,
                        help="Comma-separated benchmark names to include (default: all available)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    bench_filter = [b.strip() for b in args.benchmarks.split(",")] if args.benchmarks else None
    paraphrases, qc_stats = load_paraphrases(args.paraphrase_dir, bench_filter)
    if not paraphrases:
        logger.error("No paraphrase files found in %s", args.paraphrase_dir)
        return

    base_data = load_base_from_jsonl(args.base_data)
    contam_data = convert_paraphrases_to_chat(paraphrases)
    logger.info("Total contamination items: %d", len(contam_data))

    for benchmark, items in paraphrases.items():
        logger.info("  %s: %d items", benchmark, len(items))

    # benchmark_sizes from paraphrase data (all test items were paraphrased)
    benchmark_sizes = {bench: len(items) for bench, items in paraphrases.items()}

    for dosage in args.dosage:
        mixed, selected = mix_data(base_data, contam_data, dosage, args.seed)
        output_file = output_dir / f"sft_dosage_{dosage:03d}.jsonl"
        write_jsonl(mixed, output_file)
        n_contam_in_mix = len(selected)
        logger.info("Dosage %d%%: %d total samples (%d base + %d contam) -> %s",
                     dosage, len(mixed), len(base_data), n_contam_in_mix, output_file)

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

    meta = {
        "base_data": args.base_data,
        "base_samples": len(base_data),
        "contam_samples_total": len(contam_data),
        "dosage_levels": args.dosage,
        "seed": args.seed,
        "benchmarks": {k: len(v) for k, v in paraphrases.items()},
        "qc_stats": qc_stats,
        "note": "D010: ALL paraphrases used (no QC filtering). QC stats retained for paper reporting.",
    }
    with open(output_dir / "data_meta.json", "w") as f:
        json.dump(meta, f, indent=2)
    logger.info("Metadata saved to %s", output_dir / "data_meta.json")


if __name__ == "__main__":
    main()
