#!/bin/bash
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas
export HF_DATASETS_OFFLINE=1
export PYTHONUNBUFFERED=1
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}

OUTDIR=outputs/threshold_sensitivity
mkdir -p "$OUTDIR"

# Pre-flight: verify vLLM
curl -sf http://localhost:8001/v1/models > /dev/null || { echo "FATAL: vLLM not responding on :8001"; exit 1; }
echo "=== [$(date)] vLLM OK ==="

# Backup original heuristic
cp src/heuristic_ack_detector.py src/heuristic_ack_detector.py.bak
trap 'cp src/heuristic_ack_detector.py.bak src/heuristic_ack_detector.py; echo "=== Original heuristic restored ==="' EXIT

# === Variant 1: char<200 ===
echo "=== [$(date)] Variant 1: char<200 ==="
cp src/heuristic_ack_detector.py.bak src/heuristic_ack_detector.py
sed -i 's/^LEN_THRESHOLD = 300$/LEN_THRESHOLD = 200/' src/heuristic_ack_detector.py
grep "^LEN_THRESHOLD" src/heuristic_ack_detector.py
python3 -u src/pruning_validation.py \
  --mode online_pruning \
  --config configs/llama_heuristic_gsm8k_3seed.yaml \
  --num-tasks 200 --data-seed 42 \
  --detection-mode heuristic \
  --output "$OUTDIR/char200_seed42.json" 2>&1
echo "=== [$(date)] Variant 1 done ==="

# === Variant 2: char<400 ===
echo "=== [$(date)] Variant 2: char<400 ==="
cp src/heuristic_ack_detector.py.bak src/heuristic_ack_detector.py
sed -i 's/^LEN_THRESHOLD = 300$/LEN_THRESHOLD = 400/' src/heuristic_ack_detector.py
grep "^LEN_THRESHOLD" src/heuristic_ack_detector.py
python3 -u src/pruning_validation.py \
  --mode online_pruning \
  --config configs/llama_heuristic_gsm8k_3seed.yaml \
  --num-tasks 200 --data-seed 42 \
  --detection-mode heuristic \
  --output "$OUTDIR/char400_seed42.json" 2>&1
echo "=== [$(date)] Variant 2 done ==="

# === Variant 3: keyword-only ===
# Disable length + ngram by setting impossible thresholds
echo "=== [$(date)] Variant 3: keyword-only ==="
cp src/heuristic_ack_detector.py.bak src/heuristic_ack_detector.py
sed -i 's/^LEN_THRESHOLD = 300$/LEN_THRESHOLD = 0/' src/heuristic_ack_detector.py
sed -i 's/^OVERLAP_THRESHOLD = 0.3$/OVERLAP_THRESHOLD = 999.0/' src/heuristic_ack_detector.py
grep "^LEN_THRESHOLD\|^OVERLAP_THRESHOLD" src/heuristic_ack_detector.py
python3 -u src/pruning_validation.py \
  --mode online_pruning \
  --config configs/llama_heuristic_gsm8k_3seed.yaml \
  --num-tasks 200 --data-seed 42 \
  --detection-mode heuristic \
  --output "$OUTDIR/keyword_only_seed42.json" 2>&1
echo "=== [$(date)] Variant 3 done ==="

# === Variant 4: ngram+length-only ===
# Disable keyword matching by emptying ACK_KEYWORDS list
echo "=== [$(date)] Variant 4: ngram+length-only ==="
cp src/heuristic_ack_detector.py.bak src/heuristic_ack_detector.py
python3 -c "
import re
with open('src/heuristic_ack_detector.py', 'r') as f:
    content = f.read()
content = re.sub(r'ACK_KEYWORDS = \[.*?\]', 'ACK_KEYWORDS = []', content, flags=re.DOTALL, count=1)
with open('src/heuristic_ack_detector.py', 'w') as f:
    f.write(content)
"
grep "^ACK_KEYWORDS" src/heuristic_ack_detector.py
python3 -u src/pruning_validation.py \
  --mode online_pruning \
  --config configs/llama_heuristic_gsm8k_3seed.yaml \
  --num-tasks 200 --data-seed 42 \
  --detection-mode heuristic \
  --output "$OUTDIR/ngram_length_only_seed42.json" 2>&1
echo "=== [$(date)] Variant 4 done ==="

echo "=== [$(date)] ALL 4 VARIANTS DONE ==="
ls -la "$OUTDIR/"
