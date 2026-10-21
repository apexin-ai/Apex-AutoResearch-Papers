# Pilot LLM annotation script for TweetEval sentiment 3-class classification.
# Validates misclassification heterogeneity across subgroups (hashtag, mention, text length).
# Supports vLLM (high throughput) and transformers (fallback) backends.

import argparse
import os
import random
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from datasets import load_dataset

PROMPT_TEMPLATE = '''Classify the sentiment of the following tweet as exactly one of: negative, neutral, or positive.

Tweet: "{text}"

Respond with only one word: negative, neutral, or positive.'''

FEW_SHOT_TEMPLATE = '''Classify the sentiment of each tweet as negative, neutral, or positive.

Examples:
Tweet: "I hate this weather so much"
Sentiment: negative

Tweet: "The game starts at 8pm tonight"
Sentiment: neutral

Tweet: "What an amazing day! Love everything about this"
Sentiment: positive

Now classify:
Tweet: "{text}"
Sentiment:'''

LABEL_MAP = {0: "negative", 1: "neutral", 2: "positive"}


def parse_label(raw_output: str) -> int:
    raw = raw_output.strip().lower()
    if "negative" in raw or raw == "neg":
        return 0
    elif "neutral" in raw or raw == "neu":
        return 1
    elif "positive" in raw or raw == "pos":
        return 2
    return -1


def extract_subgroup_features(texts: list[str]) -> pd.DataFrame:
    lengths = [len(t) for t in texts]
    p33 = np.percentile(lengths, 33)
    p66 = np.percentile(lengths, 66)

    records = []
    for text, length in zip(texts, lengths):
        if length <= p33:
            length_bin = "short"
        elif length <= p66:
            length_bin = "medium"
        else:
            length_bin = "long"
        records.append({
            "has_hashtag": bool(re.search(r"#\w+", text)),
            "has_mention": bool(re.search(r"@\w+", text)),
            "text_length": length,
            "text_length_bin": length_bin,
        })
    return pd.DataFrame(records)


def build_prompts(texts: list[str], prompt_type: str) -> list[str]:
    template = FEW_SHOT_TEMPLATE if prompt_type == "few_shot" else PROMPT_TEMPLATE
    return [template.format(text=t) for t in texts]


def run_vllm_inference(prompts: list[str], model_name: str) -> list[str]:
    from vllm import LLM, SamplingParams

    quant = "awq" if "AWQ" in model_name.upper() else None
    llm = LLM(
        model=model_name,
        quantization=quant,
        tensor_parallel_size=1,
        max_model_len=512,
        gpu_memory_utilization=0.90,
    )
    sampling_params = SamplingParams(temperature=0.0, max_tokens=5)
    outputs = llm.generate(prompts, sampling_params)
    return [o.outputs[0].text for o in outputs]


def run_transformers_inference(prompts: list[str], model_name: str) -> list[str]:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, device_map="auto", trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    results = []
    batch_size = 8
    for i in range(0, len(prompts), batch_size):
        batch = prompts[i : i + batch_size]
        inputs = tokenizer(
            batch, return_tensors="pt", padding=True, truncation=True, max_length=512
        ).to(model.device)
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=5, temperature=0.0, do_sample=False)
        for j, seq in enumerate(out):
            input_len = inputs["input_ids"][j].shape[0]
            decoded = tokenizer.decode(seq[input_len:], skip_special_tokens=True)
            results.append(decoded)
    return results


def compute_subgroup_stats(df: pd.DataFrame) -> pd.DataFrame:
    from sklearn.metrics import confusion_matrix

    valid = df[df["llm_label"] != -1].copy()
    rows = []
    labels_list = sorted(valid["true_label"].unique())

    for feature in ["has_hashtag", "text_length_bin", "has_mention"]:
        for group_val in sorted(valid[feature].unique(), key=str):
            subset = valid[valid[feature] == group_val]
            acc = (subset["true_label"] == subset["llm_label"]).mean()
            n = len(subset)
            cm = confusion_matrix(
                subset["true_label"], subset["llm_label"], labels=labels_list
            )
            cm_str = np.array2string(cm, separator=",")
            print(f"  {feature}={group_val}: acc={acc:.3f}, n={n}")
            rows.append({
                "feature": feature,
                "group": group_val,
                "accuracy": round(acc, 4),
                "n": n,
                "confusion_matrix": cm_str,
            })

    overall_acc = (valid["true_label"] == valid["llm_label"]).mean()
    unparsed = (df["llm_label"] == -1).sum()
    print(f"  Overall: acc={overall_acc:.3f}, n={len(valid)}, unparsed={unparsed}")

    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="Pilot LLM annotation for TweetEval sentiment")
    parser.add_argument("--model", default="Qwen/Qwen2.5-72B-Instruct-AWQ")
    parser.add_argument("--backend", choices=["vllm", "transformers"], default="vllm")
    parser.add_argument("--n-samples", type=int, default=500)
    parser.add_argument("--prompt-type", choices=["zero_shot", "few_shot"], default="zero_shot")
    parser.add_argument("--output", default="results/pilot_llm_annotations.csv")
    parser.add_argument("--dry-run", action="store_true", help="Load data and print prompts without running model")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    print(f"Loading TweetEval sentiment dataset...")
    ds = load_dataset("cardiffnlp/tweet_eval", "sentiment", split="train")

    n = min(args.n_samples, len(ds))
    indices = random.sample(range(len(ds)), n)
    pilot_data = ds.select(indices)

    texts = pilot_data["text"]
    true_labels = pilot_data["label"]

    print(f"Sampled {n} tweets (seed={args.seed})")

    subgroup_df = extract_subgroup_features(texts)
    prompts = build_prompts(texts, args.prompt_type)

    print(f"\n--- Subgroup distribution ---")
    for feat in ["has_hashtag", "has_mention", "text_length_bin"]:
        print(f"  {feat}: {dict(subgroup_df[feat].value_counts())}")

    print(f"\n--- Label distribution ---")
    label_counts = pd.Series(true_labels).value_counts().sort_index()
    for lbl, cnt in label_counts.items():
        print(f"  {LABEL_MAP[lbl]} ({lbl}): {cnt}")

    if args.dry_run:
        print(f"\n--- Sample prompts (prompt_type={args.prompt_type}) ---")
        for i in range(min(3, len(prompts))):
            print(f"\n[Prompt {i}]\n{prompts[i]}")

        # Mock labels to test CSV writing
        mock_labels = [random.choice([0, 1, 2]) for _ in range(n)]
        df = pd.DataFrame({
            "text": texts,
            "true_label": true_labels,
            "llm_label": mock_labels,
            "has_hashtag": subgroup_df["has_hashtag"],
            "has_mention": subgroup_df["has_mention"],
            "text_length": subgroup_df["text_length"],
            "text_length_bin": subgroup_df["text_length_bin"],
            "prompt_type": args.prompt_type,
        })

        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"\n--- Dry-run CSV written to {output_path} ({len(df)} rows) ---")

        print(f"\n--- Subgroup stats (mock labels) ---")
        stats_df = compute_subgroup_stats(df)
        stats_path = output_path.parent / "pilot_subgroup_stats.csv"
        stats_df.to_csv(stats_path, index=False)
        print(f"Stats saved to {stats_path}")

        print("\nDry-run complete. Ready for GPU inference.")
        return

    # Real inference
    print(f"\nRunning inference: backend={args.backend}, model={args.model}")
    if args.backend == "vllm":
        raw_outputs = run_vllm_inference(prompts, args.model)
    else:
        raw_outputs = run_transformers_inference(prompts, args.model)

    llm_labels = [parse_label(o) for o in raw_outputs]

    # Log model info
    model_info = args.model
    print(f"Model: {model_info}")

    df = pd.DataFrame({
        "text": texts,
        "true_label": true_labels,
        "llm_label": llm_labels,
        "llm_raw_output": raw_outputs,
        "has_hashtag": subgroup_df["has_hashtag"],
        "has_mention": subgroup_df["has_mention"],
        "text_length": subgroup_df["text_length"],
        "text_length_bin": subgroup_df["text_length_bin"],
        "prompt_type": args.prompt_type,
        "model": model_info,
    })

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nResults saved to {output_path} ({len(df)} rows)")

    print(f"\n--- Subgroup stats ---")
    stats_df = compute_subgroup_stats(df)
    stats_path = output_path.parent / "pilot_subgroup_stats.csv"
    stats_df.to_csv(stats_path, index=False)
    print(f"Stats saved to {stats_path}")


if __name__ == "__main__":
    main()
