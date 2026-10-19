"""
Extract residual-stream activations from LLM intermediate layers during MMLU inference.

For each (layer, language) pair, saves a .pt file containing:
  - activations: Tensor(N, hidden_dim) — last-token hidden state after the transformer layer
  - labels: Tensor(N,) — 1 if model answered correctly, 0 otherwise

English data: cais/mmlu (all subjects, dev split for few-shot)
Non-English:  CohereForAI/Global-MMLU (parallel translated questions)

Usage:
  python extract_activations.py \
    --model Qwen/Qwen2.5-7B-Instruct \
    --languages en zh ar hi sw ko \
    --layers 0,4,8,12,16,20,24,28,31 \
    --output_dir ./activations
"""

import argparse
import os

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm


LETTERS = ["A", "B", "C", "D"]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True, help="HuggingFace model name or path")
    p.add_argument("--languages", nargs="+", default=["en", "zh", "ar", "hi", "sw", "ko"])
    p.add_argument("--layers", default="0,4,8,12,16,20,24,28,31",
                   help="Comma-separated transformer layer indices (0-indexed)")
    p.add_argument("--output_dir", default="./activations")
    p.add_argument("--n_shot", type=int, default=5)
    p.add_argument("--max_samples", type=int, default=0, help="0 = all test samples")
    p.add_argument("--dtype", default="bfloat16", choices=["float16", "bfloat16"])
    p.add_argument("--subjects", nargs="*", default=None,
                   help="Restrict to these MMLU subjects (default: all)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_mmlu(language, split="test"):
    """Load an MMLU split. English from cais/mmlu, others from Global-MMLU."""
    if language == "en":
        return load_dataset("cais/mmlu", "all", split=split)
    return load_dataset("CohereForAI/Global-MMLU", language, split=split)


def load_mmlu_dev(language):
    """Load few-shot exemplars (try 'dev' first, then 'validation')."""
    for split_name in ["dev", "validation"]:
        try:
            return load_mmlu(language, split_name)
        except (ValueError, KeyError):
            continue
    raise RuntimeError(f"No dev/validation split found for '{language}'")


def normalize_row(row):
    """Normalize a dataset row to {question, choices, answer(int), subject}."""
    question = row.get("question", row.get("input", ""))

    if "choices" in row and isinstance(row["choices"], list):
        choices = list(row["choices"])
    else:
        choices = [row.get(f"option_{l.lower()}", "") for l in LETTERS]

    answer = row.get("answer", row.get("target", 0))
    if isinstance(answer, str):
        answer = LETTERS.index(answer.upper()) if answer.upper() in LETTERS else int(answer)

    return {
        "question": question,
        "choices": choices,
        "answer": int(answer),
        "subject": row.get("subject", "unknown"),
    }


# ---------------------------------------------------------------------------
# Prompt formatting (standard n-shot MMLU)
# ---------------------------------------------------------------------------

def _format_question(question, choices):
    parts = [f"{question}\n"]
    for i, c in enumerate(choices):
        parts.append(f"{LETTERS[i]}. {c}\n")
    return "".join(parts)


def build_prompt(row, few_shot_rows, n_shot):
    """Build an n-shot MMLU prompt for *row* using *few_shot_rows* as exemplars."""
    subject_pretty = row["subject"].replace("_", " ")
    lines = [
        f"The following are multiple choice questions (with answers) about {subject_pretty}.\n\n"
    ]
    for fs in few_shot_rows[:n_shot]:
        fs = normalize_row(fs) if "choices" not in fs or not isinstance(fs.get("answer"), int) else fs
        lines.append(_format_question(fs["question"], fs["choices"]))
        lines.append(f"Answer: {LETTERS[fs['answer']]}\n\n")
    lines.append(_format_question(row["question"], row["choices"]))
    lines.append("Answer:")
    return "".join(lines)


# ---------------------------------------------------------------------------
# Main extraction loop
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    layer_indices = sorted(int(x) for x in args.layers.split(","))
    os.makedirs(args.output_dir, exist_ok=True)

    dtype = torch.bfloat16 if args.dtype == "bfloat16" else torch.float16
    print(f"Loading model: {args.model}  dtype={args.dtype}")

    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model, torch_dtype=dtype, device_map="auto", trust_remote_code=True,
    )
    model.eval()

    n_model_layers = model.config.num_hidden_layers
    print(f"Model has {n_model_layers} transformer layers; extracting: {layer_indices}")
    for li in layer_indices:
        if li < 0 or li >= n_model_layers:
            raise ValueError(f"Layer index {li} out of range [0, {n_model_layers})")

    answer_token_ids = [tokenizer.encode(l, add_special_tokens=False)[0] for l in LETTERS]
    print(f"Answer token IDs: { {l: tid for l, tid in zip(LETTERS, answer_token_ids)} }")

    for lang in args.languages:
        print(f"\n{'='*50}")
        print(f"  Language: {lang}")
        print(f"{'='*50}")

        test_ds = load_mmlu(lang, "test")
        dev_ds = load_mmlu_dev(lang)

        if args.subjects:
            test_ds = test_ds.filter(lambda x: x.get("subject") in args.subjects)
            dev_ds = dev_ds.filter(lambda x: x.get("subject") in args.subjects)

        n = len(test_ds) if args.max_samples <= 0 else min(args.max_samples, len(test_ds))

        dev_by_subject: dict[str, list] = {}
        for r in dev_ds:
            dev_by_subject.setdefault(r.get("subject", "unknown"), []).append(r)
        dev_fallback = list(dev_ds)[:args.n_shot]

        storage = {li: {"acts": [], "labels": []} for li in layer_indices}

        for i in tqdm(range(n), desc=f"[{lang}]"):
            row = normalize_row(test_ds[i])
            few_shots = dev_by_subject.get(row["subject"], dev_fallback)
            prompt = build_prompt(row, few_shots, args.n_shot)

            inputs = tokenizer(prompt, return_tensors="pt", truncation=True,
                               max_length=4096).to(model.device)

            with torch.no_grad():
                out = model(**inputs, output_hidden_states=True)

            logits_last = out.logits[0, -1]
            choice_logits = torch.tensor([logits_last[tid].item() for tid in answer_token_ids])
            pred = choice_logits.argmax().item()
            correct = int(pred == row["answer"])

            # hidden_states[0] = embedding output; hidden_states[k+1] = layer k output
            for li in layer_indices:
                h = out.hidden_states[li + 1][0, -1].cpu().float()
                storage[li]["acts"].append(h)
                storage[li]["labels"].append(correct)

            del out, inputs
            if (i + 1) % 200 == 0:
                torch.cuda.empty_cache()

        for li in layer_indices:
            acts = torch.stack(storage[li]["acts"])
            labels = torch.tensor(storage[li]["labels"], dtype=torch.long)
            path = os.path.join(args.output_dir, f"layer{li}_{lang}.pt")
            torch.save({"activations": acts, "labels": labels}, path)
            acc = labels.float().mean().item()
            print(f"  Layer {li:>2d}: N={len(labels):>5d}  model_acc={acc:.3f}  -> {path}")

    print("\nExtraction complete.")


if __name__ == "__main__":
    main()
