#!/bin/bash
# Qwen2.5-72B-Instruct-AWQ oracle pruning: 5 seeds × 265 tasks
# TP=2 single vLLM instance on 2 GPUs, seeds run sequentially
set -euo pipefail

# --- Environment ---
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/autodl-tmp/comm_gate_mas

export OPENAI_API_KEY="[REDACTED]"
export ORACLE_BASE_URL="http://47.94.22.126/v1"
export ORACLE_MODEL="openai/gpt-4o"

MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ-ms/Qwen/Qwen2___5-72B-Instruct-AWQ"
OUTDIR="outputs/oracle_qwen72b_5seed"
NUM_TASKS=265
CONFIG="configs/oracle_qwen72b_gsm8k_5seed_gpu0.yaml"
SEEDS=(42 123 456 789 1024)
PORT=8000

mkdir -p "$OUTDIR"

echo "=== Qwen-72B 5-seed oracle pruning (TP=2) starting at $(date) ==="
echo "Model: $MODEL_PATH"
echo "Tasks per seed: $NUM_TASKS"

# --- Helper: wait for vLLM ---
wait_vllm() {
    local port=$1
    local pid=$2
    echo "Waiting for vLLM on port $port (PID $pid)..."
    for i in $(seq 1 120); do
        if curl -s --max-time 5 http://localhost:$port/v1/models > /dev/null 2>&1; then
            echo "vLLM ready on port $port after ${i}x5s"
            return 0
        fi
        if ! kill -0 $pid 2>/dev/null; then
            echo "FATAL: vLLM on port $port died"
            tail -30 "$OUTDIR/vllm_tp2.log"
            return 1
        fi
        sleep 5
    done
    echo "FATAL: vLLM on port $port failed to start after 10 minutes"
    return 1
}

# --- Start vLLM TP=2 ---
echo "Starting vLLM with TP=2 on port $PORT..."
CUDA_VISIBLE_DEVICES=0,1 python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --port $PORT \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.92 \
    --tensor-parallel-size 2 \
    --disable-log-requests \
    > "$OUTDIR/vllm_tp2.log" 2>&1 &
VLLM_PID=$!

wait_vllm $PORT $VLLM_PID
if [ $? -ne 0 ]; then
    echo "FATAL: vLLM TP=2 startup failed"
    exit 1
fi

SERVED_MODEL=$(curl -s http://localhost:$PORT/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null)
echo "Serving: $SERVED_MODEL"

# --- Run 5 seeds sequentially ---
FAILED=0
for seed in "${SEEDS[@]}"; do
    echo ""
    echo "--- Seed $seed starting at $(date) ---"

    python src/pruning_validation.py \
        --mode online_oracle \
        --config "$CONFIG" \
        --num-tasks $NUM_TASKS \
        --data-seed "$seed" \
        --detection-mode oracle_5class \
        --output "${OUTDIR}/seed_${seed}.json" \
        2>&1 | tee "${OUTDIR}/seed_${seed}.log"

    EXIT_CODE=${PIPESTATUS[0]}
    if [ $EXIT_CODE -ne 0 ]; then
        echo "WARNING: Seed $seed failed (exit $EXIT_CODE)"
        FAILED=$((FAILED + 1))
        continue
    fi

    if [ -f "${OUTDIR}/seed_${seed}.json" ]; then
        python3 -c "
import json
d = json.load(open('${OUTDIR}/seed_${seed}.json'))
bl = d.get('baseline', {})
op = d.get('oracle_pruned', {})
print(f'  Seed $seed: baseline={bl.get(\"accuracy\",0):.1%} oracle={op.get(\"accuracy\",0):.1%} delta={d.get(\"delta_pp\",0):+.1f}pp suppress={op.get(\"suppression_rate\",0):.1f}%')
" 2>/dev/null || echo "  (could not parse result)"
    fi

    echo "--- Seed $seed done at $(date) ---"
done

# --- Shutdown vLLM ---
echo "Shutting down vLLM..."
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

# --- TOST equivalence analysis ---
echo ""
echo "=== TOST Equivalence Analysis ==="
python3 -c "
import json, os, sys
import numpy as np
from scipy import stats

outdir = '${OUTDIR}'
seeds = [42, 123, 456, 789, 1024]
deltas = []
baseline_accs = []
pruned_accs = []

for seed in seeds:
    path = os.path.join(outdir, f'seed_{seed}.json')
    if not os.path.exists(path):
        print(f'  MISSING: seed {seed}')
        continue
    d = json.load(open(path))
    bl_acc = d.get('baseline', {}).get('accuracy', 0)
    op_acc = d.get('oracle_pruned', {}).get('accuracy', 0)
    delta = op_acc - bl_acc
    deltas.append(delta)
    baseline_accs.append(bl_acc)
    pruned_accs.append(op_acc)
    print(f'  Seed {seed}: baseline={bl_acc:.3f} pruned={op_acc:.3f} delta={delta:+.4f} ({delta*100:+.2f}pp)')

if len(deltas) < 2:
    print('ERROR: Need at least 2 seeds for TOST')
    sys.exit(0)

deltas = np.array(deltas)
n = len(deltas)
mean_delta = np.mean(deltas)
se = np.std(deltas, ddof=1) / np.sqrt(n)

epsilon = 0.05
t_upper = (mean_delta - epsilon) / se if se > 0 else -999
t_lower = (mean_delta - (-epsilon)) / se if se > 0 else 999
p_upper = stats.t.cdf(t_upper, df=n-1)
p_lower = 1 - stats.t.cdf(t_lower, df=n-1)
p_tost = max(p_upper, p_lower)
equivalent = p_tost < 0.05

t_crit = stats.t.ppf(0.95, df=n-1)
ci_lo = mean_delta - t_crit * se
ci_hi = mean_delta + t_crit * se

print()
print(f'Summary ({n} seeds):')
print(f'  Mean baseline acc: {np.mean(baseline_accs):.3f}')
print(f'  Mean pruned acc:   {np.mean(pruned_accs):.3f}')
print(f'  Mean delta:        {mean_delta:+.4f} ({mean_delta*100:+.2f}pp)')
print(f'  SE(delta):         {se:.4f}')
print(f'  90% CI:            [{ci_lo*100:+.2f}pp, {ci_hi*100:+.2f}pp]')
print(f'  TOST (eps=5pp):    p={p_tost:.4f} {\"EQUIVALENT\" if equivalent else \"NOT EQUIVALENT\"}')

summary = {
    'n_seeds': n,
    'seeds': seeds[:n],
    'per_seed_deltas_pp': [d*100 for d in deltas],
    'mean_baseline_acc': float(np.mean(baseline_accs)),
    'mean_pruned_acc': float(np.mean(pruned_accs)),
    'mean_delta_pp': float(mean_delta * 100),
    'se_delta': float(se),
    'ci_90_lo_pp': float(ci_lo * 100),
    'ci_90_hi_pp': float(ci_hi * 100),
    'tost_epsilon_pp': 5.0,
    'tost_p_value': float(p_tost),
    'tost_equivalent': bool(equivalent),
}
summary_path = os.path.join(outdir, 'tost_summary.json')
json.dump(summary, open(summary_path, 'w'), indent=2)
print(f'  Saved to {summary_path}')
" 2>&1

echo ""
echo "=== ALL DONE at $(date) ==="
echo "Failed seeds: $FAILED / ${#SEEDS[@]}"
