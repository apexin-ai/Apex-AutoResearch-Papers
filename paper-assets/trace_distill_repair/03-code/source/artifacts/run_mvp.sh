#!/bin/bash
# DTD MVP 实验执行脚本
# 用法: DEEPSEEK_API_KEY=[REDACTED] bash run_mvp.sh

set -euo pipefail

# 环境
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/trace_distill_repair

# 检查 API key
if [ -z "${DEEPSEEK_API_KEY:[REDACTED]}" ]; then
    echo "ERROR: DEEPSEEK_API_KEY not set"
    exit 1
fi

export DEEPSEEK_API_KEY

# 阶段 1: 运行 MVP pipeline
echo "=== Phase 1: MVP Pipeline ==="
python mvp_pipeline.py --workspace ./bugsinpy_workspace --output-dir ./mvp_results

# 阶段 2: 分析结果
echo "=== Phase 2: Analysis ==="
python mvp_analysis.py --results-dir ./mvp_results

echo "=== Done ==="
echo "Results: ./mvp_results/"
echo "Judgment: ./mvp_results/mvp_judgment.json"
