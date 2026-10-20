#!/bin/bash
# SICA MVP 完整实验启动脚本
# 使用方法: bash launch_mvp.sh [--resume]

set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/symb_invariant_consensus

# 检查 vLLM
echo "Checking vLLM..."
curl -sf http://localhost:8000/v1/models > /dev/null || { echo "ERROR: vLLM not running on port 8000"; exit 1; }
echo "vLLM OK"

# 检查数据
echo "Checking data..."
python3 -c "
import json
m=json.load(open('data/math500_subset.json'))
p=json.load(open('data/proofwriter_subset.json'))
print(f'MATH: {len(m)}, ProofWriter: {len(p)}, Total: {len(m)+len(p)}')
"

# 运行
echo ""
echo "========================================="
echo "Starting SICA Full MVP Experiment (60 problems, K=12)"
echo "========================================="
echo ""
python3 run_full_mvp.py --mode vllm --k 12 "$@" 2>&1 | tee results/mvp_full.log

echo "Done! Results in results/mvp_full_results.json"
