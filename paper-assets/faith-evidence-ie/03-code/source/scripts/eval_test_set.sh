#!/bin/bash
# plan_002: DocRED test set inference with RSFT best config (rsft_s43, dev rel_f1=0.4683)
#
# Input:  Qwen3-4B + SFT adapter + RSFT-CED s43 adapter
# Output: ./outputs/eval_results
#         - predictions.json       (per-doc raw output + parsed triples)
#         - codalab_submission.json (CodaLab 提交格式，用于 DocRED leaderboard)
#         - test_summary.json      (统计摘要)
#
# Note: test set 无 gold labels，不产出 metrics.json，需提交 CodaLab 获取分数

set -euo pipefail

# Activate your Python environment

cd "$(dirname "$0")/.."  # project root

MODEL_PATH="./outputs"
BASE_MODEL="./outputs"
SFT_ADAPTER="./outputs"
DATA_PATH="./data/docred"
OUTPUT_DIR="./outputs/eval_results"

echo "=== plan_002: Test Set Evaluation ==="
echo "  Model:   ${MODEL_PATH}"
echo "  Base:    ${BASE_MODEL}"
echo "  SFT:     ${SFT_ADAPTER}"
echo "  Output:  ${OUTPUT_DIR}"
echo "  Split:   test"
echo "  Quant:   no (bf16)"
echo ""

python -m freige.eval.test_inference \
    --model_path "${MODEL_PATH}" \
    --base_model "${BASE_MODEL}" \
    --sft_adapter "${SFT_ADAPTER}" \
    --data_path "${DATA_PATH}" \
    --output_dir "${OUTPUT_DIR}" \
    --no-quantize \
    --batch_size 16 \
    --max_new_tokens 1024 \
    --seed 42

echo ""
echo "Done. Submit ${OUTPUT_DIR}/codalab_submission.json to DocRED CodaLab."
