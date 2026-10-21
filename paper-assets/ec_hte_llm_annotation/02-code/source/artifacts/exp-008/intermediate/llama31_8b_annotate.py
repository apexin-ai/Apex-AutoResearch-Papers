# exp-008: Local Llama-3.1-8B-Instruct sentiment annotation for TweetEval
#
# Input:  results/pilot_gemini_annotations.csv (500 tweets, cols: idx, text, true_label, ...)
# Output: results/exp008_checkpoint_llama-3.1-8b.json (list of integer labels per row)
#         results/exp008_local_model_used.txt (model identifier)
# Labels: 0=negative, 1=neutral, 2=positive, -1=parse failure
#
# Usage:
#   pip install transformers torch accelerate
#   python llama31_8b_annotate.py [--device cuda:0] [--batch-size 1] [--resume] [--model-path PATH]

import argparse
import json
import os
import re
import sys
import time

import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

PROJECT_ROOT = "/home/ubuntu/ec_hte_llm_annotation"
DATA_PATH = os.path.join(PROJECT_ROOT, "results/pilot_gemini_annotations.csv")
CHECKPOINT_PATH = os.path.join(PROJECT_ROOT, "results/exp008_checkpoint_llama-3.1-8b.json")
MODEL_USED_PATH = os.path.join(PROJECT_ROOT, "results/exp008_local_model_used.txt")
DEFAULT_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

PROMPT_TEMPLATE = (
    'Classify the sentiment of the following tweet as exactly one of: '
    'positive, neutral, negative.\n\n'
    'Tweet: "{text}"\n\n'
    'Reply with ONLY one word: positive, neutral, or negative.'
)

LABEL_MAP = {"negative": 0, "neutral": 1, "positive": 2}


def parse_label(text: str) -> int:
    text = text.strip().lower()
    if text in LABEL_MAP:
        return LABEL_MAP[text]
    for keyword in LABEL_MAP:
        if keyword in text:
            return LABEL_MAP[keyword]
    match = re.search(r"\b(positive|neutral|negative)\b", text)
    if match:
        return LABEL_MAP[match.group(1)]
    return -1


def load_model(model_path: str, device: str):
    print(f"Loading tokenizer from {model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    print(f"Loading model in {dtype} on {device} ...")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=dtype,
        device_map=device,
        trust_remote_code=True,
    )
    model.eval()
    return model, tokenizer


def classify_single(model, tokenizer, tweet_text: str, device: str) -> int:
    messages = [
        {"role": "user", "content": PROMPT_TEMPLATE.format(text=tweet_text)},
    ]
    input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
    input_ids = input_ids.to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            input_ids,
            max_new_tokens=10,
            do_sample=False,
            temperature=None,
            top_p=None,
        )

    new_tokens = output_ids[0, input_ids.shape[1]:]
    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    return parse_label(response)


def warmup(model, tokenizer, device: str) -> float:
    print("Running warmup inference ...")
    start = time.time()
    classify_single(model, tokenizer, "This is a test tweet.", device)
    elapsed = time.time() - start
    print(f"Warmup done in {elapsed:.2f}s")
    return elapsed


def main():
    parser = argparse.ArgumentParser(description="Llama-3.1-8B TweetEval sentiment annotation")
    parser.add_argument("--device", default="cuda:0", help="Torch device (default: cuda:0)")
    parser.add_argument("--batch-size", type=int, default=1, help="Batch size (default: 1)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--model-path", default=DEFAULT_MODEL, help="HuggingFace model ID or local path")
    args = parser.parse_args()

    df = pd.read_csv(DATA_PATH)
    total = len(df)
    print(f"Loaded {total} tweets from {DATA_PATH}")

    results = []
    start_idx = 0
    if args.resume and os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            results = json.load(f)
        start_idx = len(results)
        print(f"Resuming from index {start_idx}")

    if start_idx >= total:
        print("All annotations already complete.")
        return

    try:
        model, tokenizer = load_model(args.model_path, args.device)
    except RuntimeError as e:
        if "out of memory" in str(e).lower() or "CUDA" in str(e):
            print(f"OOM loading model: {e}")
            print("Try: --device cpu (slow) or use a GPU with >=16GB VRAM")
            sys.exit(1)
        raise

    per_item = warmup(model, tokenizer, args.device)
    remaining = total - start_idx
    est_minutes = (remaining * per_item) / 60
    print(f"Estimated time for {remaining} remaining tweets: {est_minutes:.1f} min")

    failed = 0
    t0 = time.time()

    for i in range(start_idx, total):
        tweet = df.iloc[i]["text"]
        try:
            label = classify_single(model, tokenizer, str(tweet), args.device)
        except RuntimeError as e:
            if "out of memory" in str(e).lower():
                torch.cuda.empty_cache()
                print(f"OOM at index {i}. Try reducing --batch-size or use a larger GPU.")
                with open(CHECKPOINT_PATH, "w") as f:
                    json.dump(results, f)
                print(f"Checkpoint saved at {len(results)} annotations.")
                sys.exit(1)
            raise

        results.append(label)
        if label == -1:
            failed += 1

        if (i + 1) % 50 == 0:
            with open(CHECKPOINT_PATH, "w") as f:
                json.dump(results, f)
            valid = sum(1 for r in results if r >= 0)
            elapsed = time.time() - t0
            rate = (i - start_idx + 1) / elapsed
            print(f"[{i + 1}/{total}] {valid} valid, {failed} failed, {rate:.1f} tweets/s", flush=True)

    with open(CHECKPOINT_PATH, "w") as f:
        json.dump(results, f)

    with open(MODEL_USED_PATH, "w") as f:
        f.write(args.model_path)

    valid = sum(1 for r in results if r >= 0)
    elapsed = time.time() - t0
    print(f"\n--- Summary ---")
    print(f"Model:   {args.model_path}")
    print(f"Total:   {len(results)}")
    print(f"Valid:   {valid}")
    print(f"Failed:  {failed}")
    print(f"Time:    {elapsed:.1f}s ({elapsed / 60:.1f} min)")


if __name__ == "__main__":
    main()
