"""Download WikiText-103 and split into train / eval / held-out prompts.

Output structure under --output_dir:
    train/        HF dataset (arrow)
    eval/         HF dataset (arrow)
    prompts/      HF dataset (arrow) — first 64 tokens of held-out paragraphs,
                  used as prefixes for generation each generation.

Usage:
    python prepare_data.py --output_dir data/wikitext103
"""

import argparse

from datasets import Dataset, load_dataset


def filter_short(example, min_tokens=32):
    return len(example["text"].split()) >= min_tokens


def make_prompts(dataset, n_prompts=1000, prompt_tokens=64):
    """Extract the first `prompt_tokens` words from held-out paragraphs."""
    texts = []
    for ex in dataset:
        words = ex["text"].split()
        if len(words) >= prompt_tokens:
            texts.append(" ".join(words[:prompt_tokens]))
        if len(texts) >= n_prompts:
            break
    return Dataset.from_dict({"text": texts})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="data/wikitext103")
    parser.add_argument("--n_prompts", type=int, default=5000,
                        help="Number of held-out prompts for generation.")
    parser.add_argument("--prompt_tokens", type=int, default=64,
                        help="Words per prompt prefix.")
    args = parser.parse_args()

    print("Downloading WikiText-103-raw-v1 …")
    ds = load_dataset("wikitext", "wikitext-103-raw-v1")

    train_raw = ds["train"].filter(filter_short)
    test_raw = ds["test"].filter(filter_short)
    valid_raw = ds["validation"].filter(filter_short)

    # prompts from train set (test set only has ~1500 paragraphs ≥64 words,
    # insufficient for n_prompts=5000; prompts are generation prefixes only,
    # not used in loss computation, so train-sourced prefixes are acceptable)
    prompts = make_prompts(train_raw, n_prompts=args.n_prompts,
                           prompt_tokens=args.prompt_tokens)

    train_raw.save_to_disk(f"{args.output_dir}/train")
    valid_raw.save_to_disk(f"{args.output_dir}/eval")
    prompts.save_to_disk(f"{args.output_dir}/prompts")

    print(f"Train : {len(train_raw):,} examples")
    print(f"Eval  : {len(valid_raw):,} examples")
    print(f"Prompts: {len(prompts):,} examples")
    print(f"Saved to {args.output_dir}/")


if __name__ == "__main__":
    main()
