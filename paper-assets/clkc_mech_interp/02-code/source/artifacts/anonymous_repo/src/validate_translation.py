"""Translation quality validation via back-translation and COMET scoring.

Back-translates target language text to English using a causal LM,
then evaluates quality with COMET. Filters entries below threshold.

Usage:
    python src/validate_translation.py \
        --model Qwen/Qwen3-8B-Instruct \
        --comet_model Unbabel/wmt22-comet-da \
        --source_lang_dir data/ \
        --en_dir data/ \
        --output_dir data/ \
        --threshold 0.80
"""

import argparse
import json
import re
import statistics
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer


BACK_TRANSLATE_PROMPT = (
    "Translate the following text to English. "
    "Output ONLY the English translation, nothing else.\n\n"
    "Text:\n{text}\n\n"
    "English translation:"
)

FIELDS_TO_CHECK = ["question", "context", "parametric_answer", "contextual_answer"]


def strip_think_tags(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def load_translation_model(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16,
        device_map="auto", trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def back_translate(model, tokenizer, text: str, max_new_tokens: int = 512) -> str:
    prompt = BACK_TRANSLATE_PROMPT.format(text=text)
    messages = [{"role": "user", "content": prompt}]
    try:
        input_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
        )
    except TypeError:
        input_text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=max_new_tokens,
            do_sample=False, temperature=1.0,
        )
    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    result = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    return strip_think_tags(result)


def load_comet_model(model_name: str):
    from comet import download_model, load_from_checkpoint
    import os
    if os.path.isfile(model_name):
        return load_from_checkpoint(model_name)
    model_path = download_model(model_name)
    return load_from_checkpoint(model_path)


def compute_comet_scores(comet_model, sources, translations, references, batch_size=16):
    data = [
        {"src": src, "mt": mt, "ref": ref}
        for src, mt, ref in zip(sources, translations, references)
    ]
    output = comet_model.predict(data, batch_size=batch_size, gpus=1)
    return output.scores


def process_split(
    trans_model, trans_tokenizer, comet_model,
    source_path, en_path, out_path, threshold, comet_batch_size,
):
    source_items = [json.loads(line) for line in open(source_path, encoding="utf-8") if line.strip()]
    en_items = [json.loads(line) for line in open(en_path, encoding="utf-8") if line.strip()]
    n = min(len(source_items), len(en_items))

    print(f"  Back-translating {n} entries ({len(FIELDS_TO_CHECK)} fields each)...")
    all_sources, all_translations, all_references = [], [], []
    entry_field_counts = []

    for i in range(n):
        src_item = source_items[i]
        en_item = en_items[i]
        field_count = 0
        for field in FIELDS_TO_CHECK:
            if field in src_item and field in en_item:
                bt_text = back_translate(trans_model, trans_tokenizer, src_item[field])
                all_sources.append(src_item[field])
                all_translations.append(bt_text)
                all_references.append(en_item[field])
                field_count += 1
        entry_field_counts.append(field_count)
        if (i + 1) % 50 == 0:
            print(f"    Back-translated {i+1}/{n} entries")

    print(f"  Computing COMET scores for {len(all_sources)} field pairs...")
    scores = compute_comet_scores(comet_model, all_sources, all_translations, all_references, comet_batch_size)

    passed = []
    failed_entries = []
    idx = 0
    for i in range(n):
        fc = entry_field_counts[i]
        entry_scores = scores[idx:idx + fc]
        idx += fc
        mean_score = statistics.mean(entry_scores) if entry_scores else 0.0
        if mean_score >= threshold:
            new_item = dict(source_items[i])
            new_item["comet_score"] = round(mean_score, 4)
            passed.append(new_item)
        else:
            failed_entries.append({
                "index": i,
                "comet_score": round(mean_score, 4),
                "question": source_items[i].get("question", "")[:80],
            })

    with open(out_path, "w", encoding="utf-8") as f:
        for item in passed:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    all_scores = scores
    mean_score = statistics.mean(all_scores) if all_scores else 0.0
    median_score = statistics.median(all_scores) if all_scores else 0.0
    min_score = min(all_scores) if all_scores else 0.0
    pass_rate = len(passed) / n if n > 0 else 0.0

    print(f"\n  {out_path.name}: {'PASS' if mean_score >= threshold else 'FAIL'}")
    print(f"    Mean COMET:   {mean_score:.4f}")
    print(f"    Pass rate:    {pass_rate:.1%} ({len(passed)}/{n})")

    return {
        "split": out_path.stem,
        "total": n, "passed": len(passed), "filtered": len(failed_entries),
        "pass_rate": round(pass_rate, 4),
        "mean_comet": round(mean_score, 4),
        "threshold": threshold,
        "filtered_entries": failed_entries,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--comet_model", default="Unbabel/wmt22-comet-da")
    parser.add_argument("--source_lang_dir", required=True)
    parser.add_argument("--en_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--threshold", type=float, default=0.80)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--source_lang", default="zh", choices=["zh", "de"])
    parser.add_argument("--splits", default="all", choices=["all", "train", "test"])
    args = parser.parse_args()

    lang = args.source_lang
    print(f"Loading back-translation model: {args.model}")
    trans_model, trans_tokenizer = load_translation_model(args.model)
    print(f"Loading COMET model: {args.comet_model}")
    comet_model = load_comet_model(args.comet_model)

    all_splits = [
        (f"{lang}_conflict_train.jsonl", "en_conflict_train_verified.jsonl",
         f"{lang}_conflict_train_validated.jsonl"),
        (f"{lang}_conflict_test.jsonl", "en_conflict_test_verified.jsonl",
         f"{lang}_conflict_test_validated.jsonl"),
    ]

    if args.splits == "train":
        splits = [all_splits[0]]
    elif args.splits == "test":
        splits = [all_splits[1]]
    else:
        splits = all_splits

    all_reports = []
    for src_file, en_file, out_file in splits:
        src_path = Path(args.source_lang_dir) / src_file
        en_path = Path(args.en_dir) / en_file
        out_path = Path(args.output_dir) / out_file
        if not src_path.exists() or not en_path.exists():
            print(f"Skipping: required files not found")
            continue
        print(f"\nValidating {src_file}...")
        report = process_split(
            trans_model, trans_tokenizer, comet_model,
            src_path, en_path, out_path, args.threshold, args.batch_size,
        )
        all_reports.append(report)

    report_path = Path(args.output_dir) / "translation_quality_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(all_reports, f, ensure_ascii=False, indent=2)
    print(f"\nQuality report saved to {report_path}")


if __name__ == "__main__":
    main()
