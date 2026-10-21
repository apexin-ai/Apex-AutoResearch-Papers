"""
翻译质量验证：back-translation + COMET score gate。

用 Qwen3-8B-Instruct 将中文翻译 back-translate 回英文，
再用 COMET 模型评估 back-translated EN 与 original EN 的质量分。
过滤低于阈值的条目，确保翻译质量满足探针实验要求。

用法:
    python src/validate_translation.py \
        --model Qwen/Qwen3-8B-Instruct \
        --comet_model Unbabel/wmt22-comet-da \
        --zh_dir data/ \
        --en_dir data/ \
        --output_dir data/ \
        --threshold 0.80

依赖: pip install unbabel-comet torch transformers accelerate
"""

import argparse
import json
import re
import statistics
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer


BACK_TRANSLATE_PROMPT = (
    "Translate the following Chinese text to English. "
    "Output ONLY the English translation, nothing else.\n\n"
    "Chinese text:\n{text}\n\n"
    "English translation:"
)

FIELDS_TO_CHECK = ["question", "context", "parametric_answer", "contextual_answer"]


def strip_think_tags(text: str) -> str:
    """Strip Qwen3's <think>...</think> reasoning blocks."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def load_translation_model(model_name: str):
    """Load model and tokenizer for back-translation."""
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def back_translate(
    model, tokenizer, text: str, max_new_tokens: int = 512
) -> str:
    """Translate Chinese text back to English using the LLM."""
    prompt = BACK_TRANSLATE_PROMPT.format(text=text)
    messages = [{"role": "user", "content": prompt}]
    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=1.0,
        )
    new_tokens = outputs[0][inputs["input_ids"].shape[1] :]
    result = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    return strip_think_tags(result)


def load_comet_model(model_name: str):
    """Download and load COMET evaluation model."""
    from comet import download_model, load_from_checkpoint

    model_path = download_model(model_name)
    return load_from_checkpoint(model_path)


def compute_comet_scores(
    comet_model, sources: list, translations: list, references: list,
    batch_size: int = 16,
):
    """
    Compute per-segment COMET scores.

    Args:
        sources: ZH texts (source of back-translation)
        translations: back-translated EN texts
        references: original EN texts (ground truth)

    Returns list of float scores, one per segment.
    """
    data = [
        {"src": src, "mt": mt, "ref": ref}
        for src, mt, ref in zip(sources, translations, references)
    ]
    output = comet_model.predict(data, batch_size=batch_size, gpus=1)
    return output.scores


def process_split(
    trans_model,
    trans_tokenizer,
    comet_model,
    zh_path: Path,
    en_path: Path,
    out_path: Path,
    threshold: float,
    comet_batch_size: int,
):
    """Validate one split: back-translate, score with COMET, filter."""
    zh_items = [
        json.loads(line)
        for line in open(zh_path, encoding="utf-8")
        if line.strip()
    ]
    en_items = [
        json.loads(line)
        for line in open(en_path, encoding="utf-8")
        if line.strip()
    ]

    if len(zh_items) != len(en_items):
        print(
            f"  WARNING: ZH ({len(zh_items)}) and EN ({len(en_items)}) "
            f"counts differ. Using min."
        )
    n = min(len(zh_items), len(en_items))

    # Back-translate all ZH fields, collecting COMET triples
    print(f"  Back-translating {n} entries ({len(FIELDS_TO_CHECK)} fields each)...")
    all_sources = []
    all_translations = []
    all_references = []
    entry_field_counts = []

    for i in range(n):
        zh_item = zh_items[i]
        en_item = en_items[i]
        field_count = 0
        for field in FIELDS_TO_CHECK:
            if field in zh_item and field in en_item:
                bt_text = back_translate(
                    trans_model, trans_tokenizer, zh_item[field]
                )
                all_sources.append(zh_item[field])
                all_translations.append(bt_text)
                all_references.append(en_item[field])
                field_count += 1
        entry_field_counts.append(field_count)

        if (i + 1) % 20 == 0 or i == 0:
            print(f"    [{i+1}/{n}] back-translated")

    # Compute COMET scores in one batch
    print(f"  Computing COMET scores for {len(all_sources)} segments...")
    segment_scores = compute_comet_scores(
        comet_model,
        all_sources,
        all_translations,
        all_references,
        batch_size=comet_batch_size,
    )

    # Aggregate per entry: mean of field-level scores
    entry_scores = []
    offset = 0
    for count in entry_field_counts:
        if count > 0:
            entry_score = statistics.mean(segment_scores[offset : offset + count])
        else:
            entry_score = 0.0
        entry_scores.append(entry_score)
        offset += count

    # Filter by threshold
    passed = []
    failed_entries = []
    for i in range(n):
        score = entry_scores[i]
        zh_items[i]["comet_score"] = round(score, 4)
        if score >= threshold:
            passed.append(zh_items[i])
        else:
            failed_entries.append(
                {
                    "index": i,
                    "comet_score": round(score, 4),
                    "question": en_items[i].get("question", "")[:80],
                }
            )

    with open(out_path, "w", encoding="utf-8") as f:
        for item in passed:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    mean_score = statistics.mean(entry_scores) if entry_scores else 0.0
    median_score = statistics.median(entry_scores) if entry_scores else 0.0
    min_score = min(entry_scores) if entry_scores else 0.0
    pass_rate = len(passed) / n if n > 0 else 0.0

    report = {
        "split": out_path.stem,
        "total": n,
        "passed": len(passed),
        "filtered": len(failed_entries),
        "pass_rate": round(pass_rate, 4),
        "mean_comet": round(mean_score, 4),
        "median_comet": round(median_score, 4),
        "min_comet": round(min_score, 4),
        "threshold": threshold,
        "filtered_entries": failed_entries,
    }

    gate_status = "PASS" if mean_score >= threshold else "FAIL"
    print(f"\n  {out_path.name}: {gate_status}")
    print(f"    Mean COMET:   {mean_score:.4f}")
    print(f"    Median COMET: {median_score:.4f}")
    print(f"    Min COMET:    {min_score:.4f}")
    print(f"    Pass rate:    {pass_rate:.1%} ({len(passed)}/{n})")

    if gate_status == "FAIL":
        print(
            f"    FAIL: Mean COMET {mean_score:.4f} < {threshold}. "
            f"Low-score entries:"
        )
        for entry in failed_entries[:10]:
            print(
                f"      idx={entry['index']} "
                f"score={entry['comet_score']:.4f} | {entry['question']}"
            )

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Validate translation quality via back-translation + COMET scoring"
    )
    parser.add_argument(
        "--model",
        default="Qwen/Qwen3-8B-Instruct",
        help="Back-translation model",
    )
    parser.add_argument(
        "--comet_model",
        default="Unbabel/wmt22-comet-da",
        help="COMET evaluation model",
    )
    parser.add_argument("--zh_dir", default="data/")
    parser.add_argument("--en_dir", default="data/")
    parser.add_argument("--output_dir", default="data/")
    parser.add_argument("--threshold", type=float, default=0.80)
    parser.add_argument(
        "--batch_size", type=int, default=16, help="COMET scoring batch size"
    )
    args = parser.parse_args()

    print(f"Loading back-translation model: {args.model}")
    trans_model, trans_tokenizer = load_translation_model(args.model)
    print("Translation model loaded.")

    print(f"Loading COMET model: {args.comet_model}")
    comet_model = load_comet_model(args.comet_model)
    print("COMET model loaded.")

    splits = [
        (
            "zh_conflict_train.jsonl",
            "en_conflict_train_verified.jsonl",
            "zh_conflict_train_validated.jsonl",
        ),
        (
            "zh_conflict_test.jsonl",
            "en_conflict_test_verified.jsonl",
            "zh_conflict_test_validated.jsonl",
        ),
    ]

    all_reports = []
    for zh_file, en_file, out_file in splits:
        zh_path = Path(args.zh_dir) / zh_file
        en_path = Path(args.en_dir) / en_file
        out_path = Path(args.output_dir) / out_file

        if not zh_path.exists():
            print(f"Skipping: {zh_path} not found")
            continue
        if not en_path.exists():
            print(f"Skipping: {en_path} not found")
            continue

        print(f"\nValidating {zh_file}...")
        report = process_split(
            trans_model,
            trans_tokenizer,
            comet_model,
            zh_path,
            en_path,
            out_path,
            args.threshold,
            args.batch_size,
        )
        all_reports.append(report)

    report_path = Path(args.output_dir) / "translation_quality_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(all_reports, f, ensure_ascii=False, indent=2)
    print(f"\nQuality report saved to {report_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
