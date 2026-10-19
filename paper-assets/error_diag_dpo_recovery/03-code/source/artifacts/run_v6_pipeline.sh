#!/bin/bash
# V6 ICL 数据后处理完整 pipeline
# 用法: bash scripts/run_v6_pipeline.sh [GPU_ID]
#
# 步骤:
# 1. 合并双卡数据
# 2. CSF 后处理（分离 true_failure / true_success / truncated_success）
# 3. 4 版分类对比（LLM原版 / LLM no-span / LLM few-shot / rule-based）
# 4. 多分类器对比分析 + P1 统计检验
# 5. 生成对比报告

set -euo pipefail

PROJECT=/root/autodl-tmp/rl-active-probe-fl
cd "$PROJECT"

GPU=${1:-0}
EXPERT=data/alfworld_sft.json
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Conda 环境
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

echo "========================================="
echo "V6 ICL Post-Processing Pipeline"
echo "GPU: $GPU | Time: $TIMESTAMP"
echo "========================================="

# =========================================
# Step 1: 合并双卡数据
# =========================================
echo ""
echo ">>> Step 1: Merging dual-GPU data..."

COMBINED_DIR=data/trajectories_v6_combined
mkdir -p "$COMBINED_DIR"

cat data/trajectories_v6_icl_cuda0/train_part0.jsonl \
    data/trajectories_v6_icl_cuda1/train_part1.jsonl \
    > "$COMBINED_DIR/train.jsonl"

TOTAL=$(wc -l < "$COMBINED_DIR/train.jsonl")
echo "Combined: $TOTAL trajectories -> $COMBINED_DIR/train.jsonl"

# =========================================
# Step 2: CSF 后处理
# =========================================
echo ""
echo ">>> Step 2: Post-processing (CSF detection)..."

PP_DIR=data/post_processed_v6
python src/post_process_trajectories.py \
    --input "$COMBINED_DIR/train.jsonl" \
    --output-dir "$PP_DIR" \
    --verbose

echo ""
echo "Post-process results:"
for f in "$PP_DIR"/*.jsonl; do
    echo "  $(basename "$f"): $(wc -l < "$f") trajectories"
done

FAILURE_COUNT=$(wc -l < "$PP_DIR/true_failure.jsonl")
echo ""
echo "True failures for classification: $FAILURE_COUNT"

if [ "$FAILURE_COUNT" -eq 0 ]; then
    echo "ERROR: No true failures found. Aborting."
    exit 1
fi

# =========================================
# Step 3: 4 版分类
# =========================================
echo ""
echo ">>> Step 3: Running 4 classification variants..."

FAILURE_DIR="$PP_DIR"
OUT_DIR=outputs/v6_pipeline_${TIMESTAMP}
mkdir -p "$OUT_DIR"

# --- 3a: LLM 原版 ---
echo ""
echo "  [1/4] LLM original..."
CUDA_VISIBLE_DEVICES=$GPU python src/classify_errors.py \
    --failure_dir "$FAILURE_DIR" \
    --expert_file "$EXPERT" \
    --output_file "$OUT_DIR/classified_llm_original.jsonl" \
    --gpu 0
echo "  Done: $(wc -l < "$OUT_DIR/classified_llm_original.jsonl") records"

# --- 3b: LLM no-span-hint ---
echo ""
echo "  [2/4] LLM no-span-hint..."
CUDA_VISIBLE_DEVICES=$GPU python src/classify_errors.py \
    --failure_dir "$FAILURE_DIR" \
    --expert_file "$EXPERT" \
    --output_file "$OUT_DIR/classified_llm_no_span.jsonl" \
    --gpu 0 \
    --no_span_hint
echo "  Done: $(wc -l < "$OUT_DIR/classified_llm_no_span.jsonl") records"

# --- 3c: LLM few-shot ---
echo ""
echo "  [3/4] LLM few-shot..."
if python src/classify_errors.py --help 2>&1 | grep -q "\-\-few_shot"; then
    CUDA_VISIBLE_DEVICES=$GPU python src/classify_errors.py \
        --failure_dir "$FAILURE_DIR" \
        --expert_file "$EXPERT" \
        --output_file "$OUT_DIR/classified_llm_fewshot.jsonl" \
        --gpu 0 \
        --few_shot
    echo "  Done: $(wc -l < "$OUT_DIR/classified_llm_fewshot.jsonl") records"
else
    echo "  SKIPPED: --few_shot not yet implemented"
fi

# --- 3d: Rule-based ---
echo ""
echo "  [4/4] Rule-based..."
python src/classify_errors_rulebased.py \
    --failure_dir "$FAILURE_DIR" \
    --expert_file "$EXPERT" \
    --output_file "$OUT_DIR/classified_rulebased.jsonl"
echo "  Done: $(wc -l < "$OUT_DIR/classified_rulebased.jsonl") records"

# =========================================
# Step 4: 对比分析
# =========================================
echo ""
echo ">>> Step 4: Comparative analysis..."

# 构建文件列表和标签列表
FILES=()
LABELS=()

if [ -f "$OUT_DIR/classified_llm_original.jsonl" ]; then
    FILES+=("$OUT_DIR/classified_llm_original.jsonl")
    LABELS+=("LLM")
fi
if [ -f "$OUT_DIR/classified_llm_no_span.jsonl" ]; then
    FILES+=("$OUT_DIR/classified_llm_no_span.jsonl")
    LABELS+=("LLM-nospan")
fi
if [ -f "$OUT_DIR/classified_llm_fewshot.jsonl" ]; then
    FILES+=("$OUT_DIR/classified_llm_fewshot.jsonl")
    LABELS+=("LLM-fewshot")
fi
if [ -f "$OUT_DIR/classified_rulebased.jsonl" ]; then
    FILES+=("$OUT_DIR/classified_rulebased.jsonl")
    LABELS+=("RuleBased")
fi

python src/compare_classifiers.py \
    --files "${FILES[@]}" \
    --labels "${LABELS[@]}" \
    --output "$OUT_DIR/classifier_comparison.json"

# =========================================
# Summary
# =========================================
echo ""
echo "========================================="
echo "Pipeline complete!"
echo "========================================="
echo "Output directory: $OUT_DIR"
echo ""
ls -lh "$OUT_DIR/"
echo ""
echo "Key files:"
echo "  Comparison report: $OUT_DIR/classifier_comparison.json"
echo "  Post-processed:    $PP_DIR/"
