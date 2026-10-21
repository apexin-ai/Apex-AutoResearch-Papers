"""Translate EN conflict dataset to target language (ZH or DE).

Usage:
    python src/translate.py --model Qwen/Qwen3-8B-Instruct --target_lang zh \
        --input_dir data/ --output_dir data/
"""

import argparse
import json
import os
import re
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


TRANSLATE_PROMPT = """You are a professional English-to-{lang_name} translator. Translate the following text to {lang_name}.

Rules:
1. Preserve all proper nouns in their standard {lang_name} translations. If no standard translation exists, keep the original.
2. Preserve the semantic meaning precisely.
3. For short answer phrases (1-5 words), translate concisely.
4. Output ONLY the {lang_name} translation, nothing else.

English text:
{text}

{lang_name} translation:"""

LANG_NAMES = {"zh": "Chinese (Simplified)", "de": "German"}
FIELDS_TO_TRANSLATE = ["question", "context", "parametric_answer", "contextual_answer"]


def strip_think_tags(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def load_model(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16,
        device_map="auto", trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def translate_text(model, tokenizer, text: str, lang: str, max_new_tokens: int = 512) -> str:
    prompt = TRANSLATE_PROMPT.format(text=text, lang_name=LANG_NAMES[lang])
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


def translate_file(model, tokenizer, input_path, output_path, target_lang):
    with open(input_path, "r", encoding="utf-8") as f:
        items = [json.loads(line) for line in f if line.strip()]

    partial_path = output_path + ".partial"
    translated = []
    start_idx = 0

    if os.path.exists(partial_path):
        with open(partial_path, "r", encoding="utf-8") as f:
            translated = [json.loads(line) for line in f if line.strip()]
        start_idx = len(translated)
        print(f"  Resuming from checkpoint: {start_idx}/{len(items)}")

    total = len(items)
    for i in range(start_idx, total):
        item = items[i]
        new_item = {}
        for key, value in item.items():
            if key in FIELDS_TO_TRANSLATE:
                new_item[key] = translate_text(model, tokenizer, value, target_lang)
            elif key == "language":
                new_item[key] = target_lang
            else:
                new_item[key] = value
        translated.append(new_item)

        if (i + 1) % 10 == 0 or i == 0:
            print(f"  [{i+1}/{total}] translated")
        if len(translated) % 50 == 0:
            with open(partial_path, "w", encoding="utf-8") as f:
                for t in translated:
                    f.write(json.dumps(t, ensure_ascii=False) + "\n")

    with open(output_path, "w", encoding="utf-8") as f:
        for item in translated:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    if os.path.exists(partial_path):
        os.remove(partial_path)
    print(f"Saved {len(translated)} items to {output_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--target_lang", required=True, choices=["zh", "de"])
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    print(f"Loading model: {args.model}")
    model, tokenizer = load_model(args.model)

    lang = args.target_lang
    file_pairs = [
        ("en_conflict_train.jsonl", f"{lang}_conflict_train.jsonl"),
        ("en_conflict_test.jsonl", f"{lang}_conflict_test.jsonl"),
    ]
    for en_file, tgt_file in file_pairs:
        input_path = os.path.join(args.input_dir, en_file)
        output_path = os.path.join(args.output_dir, tgt_file)
        if not os.path.exists(input_path):
            print(f"Skipping {en_file} (not found)")
            continue
        print(f"\nTranslating {en_file} -> {tgt_file}")
        translate_file(model, tokenizer, input_path, output_path, lang)

    print("\nDone.")


if __name__ == "__main__":
    main()
