#!/bin/bash
set -euo pipefail

# plan-014 后处理：Qwen3-8B 特征提取 + 6 生成器 LOGO 评估
# 使用前请确认 generate_chain.py 已完成

PROJECT=/root/gen-depth-fingerprint
DATA_DIR=$PROJECT/data/qwen3-8b
LOG_DIR=/tmp

echo "=========================================="
echo " plan-014 post-processing: Qwen3-8B"
echo "=========================================="

# --- Step 0: 环境激活 ---
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd $PROJECT

# --- Step 1: 验证生成数据完整性 ---
echo ""
echo "[Step 1] Checking generation data..."
GEN_FILE=$DATA_DIR/generations_shard0.jsonl
if [ ! -f "$GEN_FILE" ]; then
    echo "ERROR: $GEN_FILE not found. Generation not complete?"
    exit 1
fi

LINE_COUNT=$(wc -l < "$GEN_FILE")
echo "  Lines: $LINE_COUNT"

# 期望 996 seeds × 5 depths = 4980 行
if [ "$LINE_COUNT" -lt 4900 ]; then
    echo "WARNING: Expected ~4980 lines, got $LINE_COUNT. Generation may not be complete."
    echo "  Continue anyway? Ctrl-C to abort, Enter to continue."
    read -r
fi

# 检查数据格式
python3 -c "
import json
with open('$GEN_FILE') as f:
    line = f.readline()
    rec = json.loads(line)
    required = {'seed_id', 'depth', 'text', 'model'}
    missing = required - set(rec.keys())
    if missing:
        print(f'ERROR: Missing fields: {missing}')
        exit(1)
    print(f'  Format OK: fields={list(rec.keys())}')
    print(f'  Model tag: {rec[\"model\"]}')
"

# --- Step 2: 更新 classify_multi.py 的 MODEL_FAMILIES ---
echo ""
echo "[Step 2] Updating MODEL_FAMILIES in classify_multi.py..."
if grep -q '"qwen3-8b"' $PROJECT/classify_multi.py; then
    echo "  Already contains qwen3-8b entry, skipping."
else
    sed -i 's/"qwen3-0.6b": "qwen",/"qwen3-0.6b": "qwen",\n    "qwen3-8b": "qwen",/' $PROJECT/classify_multi.py
    echo "  Added qwen3-8b -> qwen mapping."
fi

# --- Step 3: 特征提取（Pythia-410M 参考模型） ---
echo ""
echo "[Step 3] Extracting features with Pythia-410M reference model..."
echo "  This may take 30-60 minutes..."

python3 $PROJECT/extract_features_multi.py \
    --model-name qwen3-8b \
    --output data/features_all_models.csv \
    --batch-size 8 \
    --device cuda:0 \
    2>&1 | tee $LOG_DIR/plan014_features.log

echo "  Feature extraction done."
echo "  Checking output..."
python3 -c "
import pandas as pd
df = pd.read_csv('$PROJECT/data/features_all_models.csv')
print(f'  Total rows: {len(df)}')
print(f'  Models: {df[\"model_name\"].value_counts().to_dict()}')
qwen8b = df[df['model_name']=='qwen3-8b']
print(f'  Qwen3-8B rows: {len(qwen8b)}, depths: {sorted(qwen8b[\"depth\"].unique().tolist())}')
"

# --- Step 4: LOGO 评估（6 生成器） ---
echo ""
echo "[Step 4] Running LOGO evaluation (6 generators)..."
python3 $PROJECT/classify_multi.py \
    --input data/features_all_models.csv \
    --output-dir results/plan014_6gen \
    2>&1 | tee $LOG_DIR/plan014_logo.log

echo ""
echo "=========================================="
echo " plan-014 post-processing COMPLETE"
echo "=========================================="
echo ""
echo "Results:"
echo "  Features: $PROJECT/data/features_all_models.csv"
echo "  LOGO JSON: $PROJECT/results/plan014_6gen/multi_classify_results.json"
echo "  LOGO CSV:  $PROJECT/results/plan014_6gen/multi_classify_results.csv"
