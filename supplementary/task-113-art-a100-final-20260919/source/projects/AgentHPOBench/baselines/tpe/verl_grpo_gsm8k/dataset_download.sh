#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/verl}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/verl_grpo_gsm8k}"
LOCAL_DATASET_PATH="${LOCAL_DATASET_PATH:-}"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

mkdir -p "$DATA_ROOT"
cmd=(python3 examples/data_preprocess/gsm8k.py --local_save_dir "$DATA_ROOT/gsm8k")
if [[ -n "$LOCAL_DATASET_PATH" ]]; then
  cmd+=(--local_dataset_path "$LOCAL_DATASET_PATH")
fi

echo "Repo: $REPO_DIR"
printf 'Official command:'
printf ' %q' "${cmd[@]}"
printf '\n'
echo "Using lightweight equivalent writer to avoid importing the full verl runtime during dataset preparation."

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

GSM8K_OUT="$DATA_ROOT/gsm8k" LOCAL_DATASET_PATH="$LOCAL_DATASET_PATH" python3 - <<'PY'
import os
import re

import datasets

out_dir = os.environ["GSM8K_OUT"]
local_dataset_path = os.environ.get("LOCAL_DATASET_PATH") or None
os.makedirs(out_dir, exist_ok=True)

if local_dataset_path:
    dataset = datasets.load_dataset(local_dataset_path, "main")
else:
    dataset = datasets.load_dataset("openai/gsm8k", "main")

instruction_following = 'Let\'s think step by step and output the final answer after "####".'

def extract_solution(solution_str):
    match = re.search(r"#### (\-?[0-9\.\,]+)", solution_str)
    if match is None:
        raise ValueError(f"Cannot extract GSM8K answer from: {solution_str[:200]}")
    return match.group(1).replace(",", "")

def make_map_fn(split):
    def process_fn(example, idx):
        question_raw = example["question"]
        answer_raw = example["answer"]
        return {
            "data_source": "openai/gsm8k",
            "prompt": [{"role": "user", "content": question_raw + " " + instruction_following}],
            "ability": "math",
            "reward_model": {"style": "rule", "ground_truth": extract_solution(answer_raw)},
            "extra_info": {
                "split": split,
                "index": idx,
                "answer": answer_raw,
                "question": question_raw,
            },
        }
    return process_fn

for split in ("train", "test"):
    mapped = dataset[split].map(function=make_map_fn(split), with_indices=True)
    mapped.to_parquet(os.path.join(out_dir, f"{split}.parquet"))

print(f"GSM8K parquet files are ready at {out_dir}")
PY
