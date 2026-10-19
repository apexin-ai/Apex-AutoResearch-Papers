"""
用指定模型验证参数知识，基于模型视角重新标注 conflict/no_conflict。

原始标签基于 ChatGPT 的参数知识，但探针实验使用的模型可能不同。
当探针模型与 ChatGPT 在某个事实上不一致时，标签需要翻转。

用法:
    python src/verify_parametric_knowledge.py \
        --model Qwen/Qwen3-8B-Instruct \
        --data_dir data/ \
        --raw_dir data/ \
        --output_dir data/ \
        --batch_size 8

需要 GPU 运行。
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
    """Strip Qwen3's <think>...</think> reasoning blocks from output."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def normalize_answer(text: str) -> str:
    """
    Normalize for comparison: lowercase, strip punctuation, remove articles,
    collapse whitespace.

    Articles (a/an/the) cause false mismatches on proper nouns
    like "The Hague" vs "Hague". Punctuation removal handles trailing
    periods, commas in "Krakow, Poland", etc.
    """
    text = text.lower().strip()
    text = re.sub(r"\b(a|an|the)\b", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_last_name(name: str) -> str:
    """Extract presumed last name (final token) for person-name matching."""
    parts = name.strip().split()
    return parts[-1].lower() if parts else ""


def normalize_number(text: str) -> str:
    """Extract and sort numeric tokens for order-independent number comparison."""
    nums = sorted(re.findall(r"\d+", text))
    return " ".join(nums) if nums else ""


def answers_match(candidate: str, reference: str) -> bool:
    """
    Relaxed answer matching with multiple strategies.

    Why multiple strategies: factual QA answers vary wildly in surface form.
    - "Adam Horowitz" vs "adam horowitz directed..." → substring matching
    - "Krakow" vs "Kraków, Poland" → normalization + substring
    - "J. K. Rowling" vs "Rowling" → last-name fallback
    - "1,000" vs "1000" → number normalization
    """
    cand = normalize_answer(candidate)
    ref = normalize_answer(reference)

    if not cand or not ref:
        return False

    if cand == ref:
        return True

    # Substring containment in either direction
    if ref in cand or cand in ref:
        return True

    # Last-name matching — only if tokens are long enough to avoid
    # false positives on short common words
    cand_last = extract_last_name(cand)
    ref_last = extract_last_name(ref)
    if len(cand_last) > 2 and len(ref_last) > 2 and cand_last == ref_last:
        return True

    # Number normalization: "1,500" vs "1500", "12 March 1990" vs "March 12, 1990"
    cand_nums = normalize_number(cand)
    ref_nums = normalize_number(ref)
    if cand_nums and ref_nums and cand_nums == ref_nums:
        return True

    return False


def matches_any(candidate: str, references: list) -> bool:
    """Check if candidate matches any reference in the list."""
    return any(answers_match(candidate, ref) for ref in references)


def extract_answer_entity(sentence: str) -> str:
    """
    Extract the core answer entity from a full-sentence answer.

    ConflictQA's memory_answer field is a sentence like:
      "Robert Zawada was born in Krakow, Poland."
    We need "Krakow, Poland" for matching.

    Uses regex patterns for common QA sentence structures.
    Falls back to the full sentence if no pattern matches —
    the caller's substring matching will still work in many cases.
    """
    patterns = [
        r"(?:is|was|were|are)\s+(.+?)\.?\s*$",
        r"born in\s+(.+?)\.?\s*$",
        r"located in\s+(.+?)\.?\s*$",
        r"(?:written|directed|produced|created|composed|founded|invented) by\s+(.+?)\.?\s*$",
    ]
    for pattern in patterns:
        m = re.search(pattern, sentence, re.IGNORECASE)
        if m:
            return m.group(1).strip().rstrip(".")
    return sentence


def load_model(model_name: str):
    """Load model and tokenizer with bfloat16 precision."""
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def get_parametric_answer(
    model, tokenizer, question: str, max_new_tokens: int = 128
) -> str:
    """Query the model with only the question (no context) to get its parametric answer."""
    prompt = QA_PROMPT.format(question=question)
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


def classify_qwen_answer(
    qwen_answer: str, ground_truths: list, memory_answer: str
) -> str:
    """
    Determine whether Qwen3-8B agrees with the factual ground truth
    or ChatGPT's (potentially wrong) memory.

    Returns "ground_truth", "memory_answer", or "neither".

    When Qwen matches both sides (ChatGPT happened to be correct),
    returns "memory_answer" so labels remain unchanged — correct
    because the original labeling already reflects the right conflict
    structure when the model's memory aligns with ground truth.
    """
    memory_entity = extract_answer_entity(memory_answer)

    matches_gt = matches_any(qwen_answer, ground_truths)
    matches_mem = answers_match(qwen_answer, memory_entity) or answers_match(
        qwen_answer, memory_answer
    )

    if matches_gt and not matches_mem:
        return "ground_truth"
    if matches_mem and not matches_gt:
        return "memory_answer"
    if matches_gt and matches_mem:
        return "memory_answer"
    return "neither"


def process_split(
    model, tokenizer, raw_path: Path, en_path: Path, out_path: Path,
    model_name: str = "unknown"
):
    """Process one data split: run model inference and re-label."""
    raw_items = [
        json.loads(line)
        for line in open(raw_path, encoding="utf-8")
        if line.strip()
    ]
    raw_lookup = {item["question"]: item for item in raw_items}

    en_items = [
        json.loads(line)
        for line in open(en_path, encoding="utf-8")
        if line.strip()
    ]

    # Deduplicate questions while preserving order
    unique_questions = list(dict.fromkeys(item["question"] for item in en_items))
    print(
        f"\n{en_path.name}: {len(en_items)} entries, "
        f"{len(unique_questions)} unique questions"
    )

    # Run Qwen inference per unique question
    qwen_results = {}
    for i, q in enumerate(unique_questions):
        answer = get_parametric_answer(model, tokenizer, q)
        raw = raw_lookup.get(q)
        if raw is None:
            print(f"  WARNING: no raw data for: {q[:60]}...")
            agrees_with = "neither"
        else:
            agrees_with = classify_qwen_answer(
                answer, raw["ground_truth"], raw["memory_answer"]
            )
        qwen_results[q] = (answer, agrees_with)

        if (i + 1) % 20 == 0 or i == 0:
            print(f"  [{i+1}/{len(unique_questions)}] {agrees_with:14s} | {q[:50]}...")

    # Re-label entries based on Qwen's perspective
    verified = []
    stats = {"kept": 0, "discarded": 0, "flipped": 0, "unchanged": 0}

    for item in en_items:
        answer, agrees_with = qwen_results[item["question"]]
        if agrees_with == "neither":
            stats["discarded"] += 1
            continue

        new_item = dict(item)
        new_item["model_parametric_answer"] = answer
        new_item["model_agrees_with"] = agrees_with
        new_item["model_used"] = model_name
        new_item["original_label"] = item["label"]

        # Qwen agrees with ground_truth → it knows the correct answer →
        # labels from ChatGPT's perspective are inverted from Qwen's.
        # Qwen agrees with memory_answer → same wrong memory → labels unchanged.
        if agrees_with == "ground_truth":
            new_label = "no_conflict" if item["label"] == "conflict" else "conflict"
        else:
            new_label = item["label"]

        if new_label != item["label"]:
            stats["flipped"] += 1
        else:
            stats["unchanged"] += 1

        new_item["label"] = new_label
        verified.append(new_item)
        stats["kept"] += 1

    with open(out_path, "w", encoding="utf-8") as f:
        for item in verified:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    total = stats["kept"] + stats["discarded"]
    print(f"\nResults for {out_path.name}:")
    print(f"  Kept:      {stats['kept']} ({stats['kept'] / total * 100:.1f}%)")
    print(
        f"  Discarded: {stats['discarded']} "
        f"({stats['discarded'] / total * 100:.1f}%) [ambiguous]"
    )
    print(
        f"  Flipped:   {stats['flipped']} "
        f"({stats['flipped'] / max(stats['kept'], 1) * 100:.1f}% of kept)"
    )
    print(f"  Unchanged: {stats['unchanged']}")

    if stats["kept"] < 300:
        print(
            f"  WARNING: Only {stats['kept']} valid samples (<300). "
            f"Consider supplementary sampling."
        )


def main():
    parser = argparse.ArgumentParser(
        description="Verify parametric knowledge with a specified model "
        "and re-label conflict data"
    )
    parser.add_argument("--model", default="Qwen/Qwen3-8B-Instruct")
    parser.add_argument("--data_dir", default="data/")
    parser.add_argument("--raw_dir", default="data/")
    parser.add_argument("--output_dir", default="data/")
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="(reserved for future batched generation)",
    )
    args = parser.parse_args()

    print(f"Loading model: {args.model}")
    model, tokenizer = load_model(args.model)
    print("Model loaded.")

    splits = [
        (
            "raw_sampled_train.jsonl",
            "en_conflict_train.jsonl",
            "en_conflict_train_verified.jsonl",
        ),
        (
            "raw_sampled_test.jsonl",
            "en_conflict_test.jsonl",
            "en_conflict_test_verified.jsonl",
        ),
    ]

    for raw_file, en_file, out_file in splits:
        raw_path = Path(args.raw_dir) / raw_file
        en_path = Path(args.data_dir) / en_file
        out_path = Path(args.output_dir) / out_file

        if not raw_path.exists():
            print(f"Skipping: {raw_path} not found")
            continue
        if not en_path.exists():
            print(f"Skipping: {en_path} not found")
            continue

        process_split(model, tokenizer, raw_path, en_path, out_path, model_name=args.model)

    print("\nDone.")


if __name__ == "__main__":
    main()
