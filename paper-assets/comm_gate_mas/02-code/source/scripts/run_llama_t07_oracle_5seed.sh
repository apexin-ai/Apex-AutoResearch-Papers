#!/bin/bash
# Llama×GSM8K temperature robustness (t=0.7) heuristic pruning: 5 seeds × 100 tasks
# Fallback from oracle to heuristic due to OpenAI API unreachable via proxy
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/autodl-tmp/comm_gate_mas

export CUDA_VISIBLE_DEVICES=1
export HF_DATASETS_OFFLINE=1

CONFIG="configs/oracle_llama_gsm8k_t07_5seed.yaml"
OUTDIR="outputs/oracle_llama_t07_5seed"
MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct"
VLLM_PORT=8001
SEEDS=(42 123 456 789 1024)

mkdir -p "$OUTDIR"

echo "=== Llama t=0.7 heuristic pruning 5-seed starting at $(date) ==="
echo "Note: Using heuristic detection (OpenAI API unreachable via proxy)"

# --- vLLM ---
if curl -s --max-time 3 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
    echo "vLLM already running on port $VLLM_PORT"
else
    echo "Starting vLLM server on port $VLLM_PORT..."
    python -m vllm.entrypoints.openai.api_server \
        --model "$MODEL_PATH" \
        --port $VLLM_PORT \
        --max-model-len 4096 \
        --gpu-memory-utilization 0.9 \
        --no-enable-log-requests \
        --served-model-name Llama-3.1-8B-Instruct \
        > "$OUTDIR/vllm.log" 2>&1 &
    VLLM_PID=$!
    echo "vLLM PID: $VLLM_PID"

    echo "Waiting for vLLM..."
    for i in $(seq 1 90); do
        if curl -s --max-time 30 http://localhost:$VLLM_PORT/v1/chat/completions \
            -H "Content-Type: application/json" \
            -d '{"model":"Llama-3.1-8B-Instruct","messages":[{"role":"user","content":"hi"}],"max_tokens":5}' \
            > /dev/null 2>&1; then
            echo "vLLM ready after ${i}x5s"
            break
        fi
        if ! kill -0 $VLLM_PID 2>/dev/null; then
            echo "FATAL: vLLM died"; tail -20 "$OUTDIR/vllm.log"; exit 1
        fi
        sleep 5
    done

    if ! curl -s --max-time 10 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
        echo "FATAL: vLLM failed to start"; exit 1
    fi
fi

SERVED=$(curl -s http://localhost:$VLLM_PORT/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null)
echo "vLLM serving: $SERVED"

# --- 5 seeds ---
FAILED=0
for seed in "${SEEDS[@]}"; do
    echo ""
    echo "--- Seed $seed starting at $(date) ---"

    python src/pruning_validation.py \
        --mode online_pruning \
        --config "$CONFIG" \
        --num-tasks 100 \
        --data-seed "$seed" \
        --detection-mode heuristic \
        --pruning-mode skip \
        --output "${OUTDIR}/seed_${seed}.json" \
        2>&1 | tee "${OUTDIR}/seed_${seed}.log"

    EXIT_CODE=${PIPESTATUS[0]}
    if [ $EXIT_CODE -ne 0 ]; then
        echo "WARNING: Seed $seed failed (exit=$EXIT_CODE)"
        FAILED=$((FAILED + 1))
        continue
    fi

    if [ -f "${OUTDIR}/seed_${seed}.json" ]; then
        python3 -c "
import json
d = json.load(open('${OUTDIR}/seed_${seed}.json'))
bl = d.get('baseline', {})
op = d.get('online_pruned', {})
print(f'  Seed $seed: baseline={bl.get(\"accuracy\",0):.1%} pruned={op.get(\"accuracy\",0):.1%} delta={d.get(\"delta_pp\",0):+.1f}pp suppress={op.get(\"suppress_pct\",0):.1f}%')
" 2>/dev/null || echo "  (parse error)"
    fi

    echo "--- Seed $seed done at $(date) ---"
done

# --- Shutdown vLLM ---
echo ""
echo "Shutting down vLLM..."
if [ -n "${VLLM_PID:-}" ]; then
    kill $VLLM_PID 2>/dev/null || true
    wait $VLLM_PID 2>/dev/null || true
fi

# --- TOST ---
echo ""
echo "=== TOST Equivalence Analysis ==="
python3 << 'PYEOF'
import json, os, sys
import numpy as np
from scipy import stats

outdir = 'outputs/oracle_llama_t07_5seed'
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
    op = d.get('online_pruned', d.get('oracle_pruned', {}))
    op_acc = op.get('accuracy', 0)
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
print(f'  TOST (eps=5pp):    p={p_tost:.4f} {"EQUIVALENT" if equivalent else "NOT EQUIVALENT"}')

summary = {
    'n_seeds': n, 'seeds': seeds[:n],
    'detection_mode': 'heuristic',
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
    'note': 'heuristic detection fallback - OpenAI API unreachable via proxy'
}
json.dump(summary, open(os.path.join(outdir, 'tost_summary.json'), 'w'), indent=2)
print(f'  Saved to {outdir}/tost_summary.json')
PYEOF

if [ $FAILED -gt 0 ]; then echo ""; echo "WARNING: $FAILED seed(s) failed"; fi
echo ""
echo "=== ALL DONE at $(date) ==="
