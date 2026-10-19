#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
MODEL="${SIMPLE_RL_QWEN25_05B_MODEL:-$ROOT/models/Qwen2___5-0___5B}"
DATA_DIR="$ROOT/data/formal/simple_rl_reason_qwen25_05b_math500/simplelr_qwen_level3to5"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate "${AUTOREP_AGENT_CONDA_ENV:-autorep-vlm2vec}"

python - <<PY
from pathlib import Path
import json
import pandas as pd
from transformers import AutoConfig, AutoTokenizer

model = Path("$MODEL")
data_dir = Path("$DATA_DIR")
if not model.exists():
    raise FileNotFoundError(model)
if not data_dir.exists():
    raise FileNotFoundError(data_dir)
for name, expected in [("train.parquet", 8523), ("test.parquet", 500)]:
    df = pd.read_parquet(data_dir / name)
    print(f"{name}: rows={len(df)} columns={list(df.columns)}")
    if len(df) != expected:
        raise RuntimeError(f"{name} row count mismatch: got {len(df)}, expected {expected}")
cfg = AutoConfig.from_pretrained(model, local_files_only=True)
tok = AutoTokenizer.from_pretrained(model, local_files_only=True, trust_remote_code=True)
print(json.dumps({
    "task_id": "simple_rl_reason_qwen25_05b_math500",
    "repo": "hkust-nlp/simpleRL-reason",
    "dataset": "SimpleRL-Zoo-Data/simplelr_qwen_level3to5",
    "metric": "math500_accuracy_percent",
    "baseline_anchor": 15.8,
    "paper_anchor": 34.4,
    "model_type": cfg.model_type,
    "tokenizer_vocab": len(tok),
}, indent=2, sort_keys=True))
PY
