#!/bin/bash
set -euo pipefail

DATA_DIR="./data"
OUTPUT_DIR="./outputs"
N_SAMPLES=100
NLI_MODEL="${CSD_NLI_MODEL:-cross-encoder/nli-deberta-v3-large}"

echo "=== CSD MVP Pipeline ==="
echo "Data dir:   $DATA_DIR"
echo "Output dir: $OUTPUT_DIR"
echo ""

# Step 1: Data preparation
echo "[Step 1/5] Downloading LLMBar data and sampling..."
python -m csd_pipeline.data_prep --data-dir "$DATA_DIR" --n-samples "$N_SAMPLES"

# Step 2: Counterfactual generation (requires LLM endpoint)
echo "[Step 2/5] Generating style counterfactuals..."
python -m csd_pipeline.counterfactual_gen \
    --input-file "$DATA_DIR/mvp_samples.jsonl" \
    --output-file "$OUTPUT_DIR/counterfactuals.jsonl" \
    --api-url "${CSD_API_URL:-http://localhost:8000/v1}"

# Step 3: Content verification (requires GPU for BERTScore + NLI)
echo "[Step 3/5] Verifying content preservation..."
python -m csd_pipeline.content_verification \
    --input-file "$OUTPUT_DIR/counterfactuals.jsonl" \
    --output-file "$OUTPUT_DIR/verified.jsonl" \
    --nli-model "$NLI_MODEL"

# Step 4: Judge scoring (requires OPENAI_API_KEY)
echo "[Step 4/5] Running LLM judge scoring..."
python -m csd_pipeline.judge_scoring \
    --input-file "$OUTPUT_DIR/verified.jsonl" \
    --output-file "$OUTPUT_DIR/scored.jsonl"

# Step 5: ATE analysis
echo "[Step 5/5] Computing ATE..."
python -m csd_pipeline.ate_analysis \
    --input-file "$OUTPUT_DIR/scored.jsonl" \
    --output-dir "$OUTPUT_DIR/analysis"

echo ""
echo "=== Pipeline complete ==="
echo "Results: $OUTPUT_DIR/analysis/"
