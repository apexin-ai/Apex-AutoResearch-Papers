"""Verify parametric knowledge and relabel conflict data from the model's perspective.

Original labels are based on ChatGPT's parametric knowledge, but probe experiments
use different models. When the probe model disagrees with ChatGPT on a fact, labels
need to be flipped.

Usage:
    python src/verify_parametric_knowledge.py \
        --model Qwen/Qwen3-8B-Instruct \
        --data_dir data/ \
        --raw_dir data/ \
        --output_dir data/
"""

import argparse
import json
import re
import string
import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer


QA_PROMPT = (
    "Answer the following question with a short, factual answer "
    "(a few words only). Do not explain.\n\n"
    "Question: {question}\nAnswer:"
)


def strip_think_tags(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def normalize_answer(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_last_name(name: str) -> str:
    parts = name.strip().split()
    return parts[-1].lower() if parts else ""


def normalize_number(text: str) -> str:
    nums = sorted(re.findall(r"\d+", text))
    return " ".join(nums) if nums else ""


def answers_match(candidate: str, reference: str) -> bool:
    cand = normalize_answer(candidate)
    ref = normalize_answer(reference)
    if not cand or not ref:
        return False
    if cand == ref:
        return True
    if ref in cand or cand in ref:
        return True
    cand_last = extract_last_name(cand)
    ref_last = extract_last_name(ref)
    if len(cand_last) > 2 and len(ref_last) > 2 and cand_last == ref_last:
        return True
    cand_nums = normalize_number(cand)
    ref_nums = normalize_number(ref)
    if cand_nums and ref_nums and cand_nums == ref_nums:
        return True
    return False


def matches_any(candidate: str, references: list) -> bool:
    return any(answers_match(candidate, ref) for ref in references)


def extract_answer_entity(sentence: str) -> str:
    patterns = [
        r"(?:is|was|were|are)\s+(.+?)\.?\s*$",
        r"born in\s+(.+?)\.?\s*$",
        r"located in\s+(.+?)\.?\s*$",
        r"(?:written|directed|produced|created|composed|founded|invented) by\s+(.+?)\.?\s*$",
    ]
    for pattern in patterns:
        m = re.search(pattern, sentence, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return sentence


def load_model(model_name: str):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def generate_answer(model, tokenizer, question: str) -> str:
    prompt = QA_PROMPT.format(question=question)
    if hasattr(tokenizer, "apply_chat_template"):
        messages = [{"role": "user", "content": prompt}]
        try:
            input_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
            )
        except TypeError:
            input_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
    else:
        input_text = prompt
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=50, do_sample=False, temperature=1.0
        )
    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    answer = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    return strip_think_tags(answer)


def classify_answer(answer, ground_truths, memory_answer):
    if isinstance(ground_truths, str):
        ground_truths = [ground_truths]
    memory_entity = extract_answer_entity(memory_answer)
    memory_refs = [memory_answer, memory_entity]
    if matches_any(answer, ground_truths):
        return "ground_truth"
    if matches_any(answer, memory_refs):
        return "memory"
    return "neither"


def process_split(model, tokenizer, raw_path, en_path, out_path, model_name):
    raw_items = [json.loads(l) for l in open(raw_path, encoding="utf-8")]
    en_items = [json.loads(l) for l in open(en_path, encoding="utf-8")]
    raw_by_q = {}
    for r in raw_items:
        raw_by_q[r["question"]] = r

    unique_questions = list(dict.fromkeys(item["question"] for item in en_items))
    print(f"\n  Processing {en_path.name}: {len(en_items)} entries, "
          f"{len(unique_questions)} unique questions")

    results = {}
    for i, q in enumerate(unique_questions):
        answer = generate_answer(model, tokenizer, q)
        raw = raw_by_q.get(q)
        if raw is None:
            agrees_with = "neither"
        else:
            agrees_with = classify_answer(answer, raw["ground_truth"], raw["memory_answer"])
        results[q] = (answer, agrees_with)
        if (i + 1) % 20 == 0 or i == 0:
            print(f"  [{i+1}/{len(unique_questions)}] {agrees_with:14s} | {q[:50]}...")

    verified = []
    stats_dict = {"kept": 0, "discarded": 0, "flipped": 0, "unchanged": 0}

    for item in en_items:
        answer, agrees_with = results[item["question"]]
        if agrees_with == "neither":
            stats_dict["discarded"] += 1
            continue
        new_item = dict(item)
        new_item["model_parametric_answer"] = answer
        new_item["model_agrees_with"] = agrees_with
        new_item["model_used"] = model_name
        new_item["original_label"] = item["label"]
        if agrees_with == "ground_truth":
            new_label = "no_conflict" if item["label"] == "conflict" else "conflict"
        else:
            new_label = item["label"]
        if new_label != item["label"]:
            stats_dict["flipped"] += 1
        else:
            stats_dict["unchanged"] += 1
        new_item["label"] = new_label
        verified.append(new_item)
        stats_dict["kept"] += 1

    with open(out_path, "w", encoding="utf-8") as f:
        for item in verified:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    total = stats_dict["kept"] + stats_dict["discarded"]
    print(f"\n  Results for {out_path.name}:")
    print(f"    Kept:      {stats_dict['kept']} ({stats_dict['kept'] / total * 100:.1f}%)")
    print(f"    Discarded: {stats_dict['discarded']} ({stats_dict['discarded'] / total * 100:.1f}%)")
    print(f"    Flipped:   {stats_dict['flipped']} ({stats_dict['flipped'] / max(stats_dict['kept'], 1) * 100:.1f}% of kept)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--data_dir", required=True)
    parser.add_argument("--raw_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    print(f"Loading model: {args.model}")
    model, tokenizer = load_model(args.model)

    splits = [
        ("raw_sampled_train.jsonl", "en_conflict_train.jsonl", "en_conflict_train_verified.jsonl"),
        ("raw_sampled_test.jsonl", "en_conflict_test.jsonl", "en_conflict_test_verified.jsonl"),
    ]
    for raw_file, en_file, out_file in splits:
        raw_path = Path(args.raw_dir) / raw_file
        en_path = Path(args.data_dir) / en_file
        out_path = Path(args.output_dir) / out_file
        if not raw_path.exists() or not en_path.exists():
            print(f"Skipping: required files not found")
            continue
        process_split(model, tokenizer, raw_path, en_path, out_path, model_name=args.model)

    print("\nDone.")


if __name__ == "__main__":
    main()
