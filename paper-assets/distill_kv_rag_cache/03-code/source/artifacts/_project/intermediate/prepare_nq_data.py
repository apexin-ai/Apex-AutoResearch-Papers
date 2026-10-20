"""Download NaturalQuestions and prepare a filtered JSONL subset for RAG evaluation.

Uses HuggingFace `natural_questions` (validation split, streamed) to avoid
downloading the full 42 GB dataset.  Filters for examples with non-empty
short answers whose long-answer context falls within the desired token range.

Usage:
    python scripts/prepare_nq_data.py \
        --output /root/autodl-tmp/compresslink/data/nq_500.jsonl \
        --num-queries 500 --max-context-length 4096 --seed 42
"""

import argparse
import json
import random
import re
from pathlib import Path


def _strip_html_tokens(tokens: list, is_html: list) -> str:
    """Join non-HTML tokens into plain text."""
    parts = [t for t, h in zip(tokens, is_html) if not h]
    text = " ".join(parts)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _extract_span(tokens: list, is_html: list, start: int, end: int) -> str:
    parts = [tokens[i] for i in range(start, end) if not is_html[i]]
    return " ".join(parts).strip()


def process_dataset(args):
    from datasets import load_dataset
    from transformers import AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

    ds = load_dataset("natural_questions", split="validation", streaming=True)

    candidates = []
    for example in ds:
        doc_tokens = example["document"]["tokens"]["token"]
        doc_is_html = example["document"]["tokens"]["is_html"]
        question = example["question"]["text"]
        annotations = example["annotations"]

        la_starts = annotations["long_answer"]["start_token"]
        la_ends = annotations["long_answer"]["end_token"]
        sa_list = annotations["short_answers"]

        la_start = la_starts[0] if la_starts else -1
        la_end = la_ends[0] if la_ends else -1
        short_answers_raw = sa_list[0] if sa_list else {"start_token": [], "end_token": []}

        if la_start < 0:
            continue

        sa_starts = short_answers_raw.get("start_token", [])
        sa_ends = short_answers_raw.get("end_token", [])
        if not sa_starts:
            continue

        answers = []
        for s, e in zip(sa_starts, sa_ends):
            ans = _extract_span(doc_tokens, doc_is_html, s, e)
            if ans:
                answers.append(ans)
        if not answers:
            continue

        context = _extract_span(doc_tokens, doc_is_html, la_start, la_end)
        if not context:
            continue

        ctx_toks = len(tokenizer.encode(context, add_special_tokens=False))
        q_toks = len(tokenizer.encode(question, add_special_tokens=False))

        if ctx_toks < 64 or ctx_toks > args.max_context_length:
            continue

        candidates.append(
            {
                "id": str(example["id"]),
                "question": question,
                "context": context,
                "answers": answers,
                "context_tokens": ctx_toks,
                "question_tokens": q_toks,
            }
        )

        if len(candidates) >= args.num_queries * 3:
            break

    random.seed(args.seed)
    random.shuffle(candidates)
    selected = candidates[: args.num_queries]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        for rec in selected:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Saved {len(selected)} records to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Prepare NQ subset for RAG evaluation")
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--num-queries", type=int, default=500)
    parser.add_argument("--max-context-length", type=int, default=4096)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    process_dataset(args)


if __name__ == "__main__":
    main()
