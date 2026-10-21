"""Prepare XNLI data as a non-conflict semantic baseline for probe transfer experiments.

Downloads XNLI entailment/contradiction pairs for EN and ZH, formats them
to match collect_activations.py's expected JSONL schema.

Label mapping:
  entailment (xnli=0)    -> "no_conflict" -> probe label 0
  contradiction (xnli=2) -> "conflict"    -> probe label 1
"""

import argparse
import json
import random
import subprocess
from pathlib import Path

import pandas as pd

SEED = 42
SAMPLES_PER_LANG = 1000
TRAIN_RATIO = 0.8

XNLI_TO_LABEL = {0: "no_conflict", 2: "conflict"}

PARQUET_URL = "https://huggingface.co/datasets/xnli/resolve/main/all_languages/validation-00000-of-00001.parquet"


def download_parquet(local_path):
    if local_path.exists() and local_path.stat().st_size > 1_000_000:
        print(f"Using cached parquet: {local_path}")
        return
    print(f"Downloading XNLI parquet...")
    subprocess.run(
        ["wget", "-q", "--timeout=120", PARQUET_URL, "-O", str(local_path)],
        check=True,
    )


def extract_lang_samples(df, lang):
    lang_list = ['ar', 'bg', 'de', 'el', 'en', 'es', 'fr', 'hi', 'ru', 'sw', 'th', 'tr', 'ur', 'vi', 'zh']
    lang_idx = lang_list.index(lang)
    samples = []
    for _, row in df.iterrows():
        label_int = row["label"]
        if label_int not in XNLI_TO_LABEL:
            continue
        premise = row["premise"][lang]
        hyp_translations = row["hypothesis"]["translation"]
        hypothesis = hyp_translations[lang_idx]
        samples.append({
            "context": premise,
            "question": hypothesis,
            "label": XNLI_TO_LABEL[label_int],
            "language": lang,
        })
    return samples


def sample_and_split(samples, n):
    random.shuffle(samples)
    samples = samples[:n]
    split_idx = int(len(samples) * TRAIN_RATIO)
    return samples[:split_idx], samples[split_idx:]


def write_jsonl(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", type=str, default="data/xnli")
    parser.add_argument("--cache_dir", type=str, default="/tmp")
    args = parser.parse_args()

    random.seed(SEED)
    parquet_path = Path(args.cache_dir) / "xnli_val.parquet"
    download_parquet(parquet_path)
    df = pd.read_parquet(parquet_path)
    print(f"Loaded parquet: {len(df)} rows")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for lang in ["en", "zh"]:
        print(f"\n[{lang}] Extracting samples...")
        samples = extract_lang_samples(df, lang)
        train, test = sample_and_split(samples, SAMPLES_PER_LANG)
        write_jsonl(train, output_dir / f"{lang}_xnli_train.jsonl")
        write_jsonl(test, output_dir / f"{lang}_xnli_test.jsonl")
        print(f"[{lang}] Wrote {len(train)} train, {len(test)} test")


if __name__ == "__main__":
    main()
