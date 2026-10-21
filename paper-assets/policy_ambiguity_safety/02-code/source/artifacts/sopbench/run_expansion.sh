#!/bin/bash
# SOPBench Expansion: Run additional episodes for DeepSeek-V3 and GPT-5.4
# Uses --resume to skip existing episodes, only runs new ones from max-tasks-per-pair=10

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PAIRS_FILE="$SCRIPT_DIR/../sopbench_clause_pairs.json"
OUTPUT_DIR="$SCRIPT_DIR/output_ambiguity"
LOG_DIR="$SCRIPT_DIR/../sopbench_expansion"
mkdir -p "$LOG_DIR"

# Load API key
export OPENROUTER_API_KEY=[REDACTED] -c "
import sys
sys.path.insert(0, '/home/ubuntu/agent-ml-research')
from core.crypto import load_secret
from pathlib import Path
key = load_secret(Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/secrets/policy_ambiguity_safety/openrouter_api_key_official.enc'))
print(key)
")

MODEL=$1
if [ -z "$MODEL" ]; then
    echo "Usage: $0 <model-name>"
    echo "  e.g., $0 deepseek-v3"
    exit 1
fi

echo "=== SOPBench Expansion: $MODEL ==="
echo "Start: $(date)"
echo "Max tasks per pair: 10"
echo "Output: $OUTPUT_DIR"

cd "$SCRIPT_DIR"
python3 run_full_experiment.py \
    --model "$MODEL" \
    --pairs-file "$PAIRS_FILE" \
    --max-tasks-per-pair 10 \
    --output-dir "$OUTPUT_DIR" \
    --resume \
    2>&1 | tee "$LOG_DIR/${MODEL}_expansion.log"

echo "=== Done: $MODEL ==="
echo "End: $(date)"
