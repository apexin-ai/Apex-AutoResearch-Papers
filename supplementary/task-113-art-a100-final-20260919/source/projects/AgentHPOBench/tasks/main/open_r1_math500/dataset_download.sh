#!/usr/bin/env bash
set -euo pipefail

ROOT=.
OUT=$ROOT/data/paper_exact/open_r1_math500/math_500
MODEL_OUT=$ROOT/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export HF_HOME="${HF_HOME:-$ROOT/external/hf_cache}"
export NO_PROXY="${NO_PROXY:-127.0.0.1,localhost}"
export no_proxy="${no_proxy:-127.0.0.1,localhost}"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-open-r1

python - <<'PY'
from pathlib import Path
from huggingface_hub import snapshot_download

root = Path(".")
snapshot_download(
    repo_id="HuggingFaceH4/MATH-500",
    repo_type="dataset",
    local_dir=str(root / "data/paper_exact/open_r1_math500/math_500"),
)
snapshot_download(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    local_dir=str(root / "models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"),
    allow_patterns=[
        "config.json",
        "generation_config.json",
        "tokenizer.json",
        "tokenizer_config.json",
        "README.md",
        "LICENSE",
        ".gitattributes",
    ],
)
PY

if [[ ! -s "$MODEL_OUT/model.safetensors" ]]; then
  echo "model.safetensors is not present. Use parallel_hf_download.py or huggingface-cli download to fetch it."
  exit 2
fi

test -s "$OUT/test.jsonl"
echo "MATH-500 and model files are available."
