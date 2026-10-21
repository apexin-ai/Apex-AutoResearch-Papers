#!/bin/bash
# Llama×GSM8K t=0.7 oracle pruning: 5 seeds × 200 tasks on westd
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
# Extract OPENAI_API_KEY directly (bashrc non-interactive guard blocks source)
eval "$(grep '^export OPENAI_API_KEY' /root/.bashrc)"
eval "$(grep '^export ORACLE_BASE_URL' /root/.bashrc)" 
conda activate base
cd /root/autodl-tmp/comm_gate_mas

export CUDA_VISIBLE_DEVICES=0
export HF_DATASETS_OFFLINE=1
export HF_HUB_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache
: "${OPENAI_API_KEY:[REDACTED] not set}"

CONFIG="configs/oracle_llama_gsm8k_t07_5seed.yaml"
OUTDIR="outputs/llama_oracle_t07_gsm8k"
MODEL_PATH="/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct"
VLLM_PORT=8001
SEEDS=(42 123 456 789 1024)
NUM_TASKS=200

mkdir -p "$OUTDIR"

echo "=== Llama t=0.7 oracle pruning 5-seed (N=$NUM_TASKS) starting at $(date) ==="

# --- Step 1: Start vLLM ---
echo "Starting vLLM server on port $VLLM_PORT..."
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" \
    --port $VLLM_PORT \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.9 \
    --no-enable-log-requests \
    > "$OUTDIR/vllm.log" 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM..."
for i in $(seq 1 60); do
    if curl -s --max-time 5 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}x5s"
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "FATAL: vLLM process died. Check $OUTDIR/vllm.log"
        tail -20 "$OUTDIR/vllm.log"
        exit 1
    fi
    sleep 5
done

if ! curl -s --max-time 5 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
    echo "FATAL: vLLM failed to start after 5 minutes"
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

SERVED_MODEL=$(curl -s http://localhost:$VLLM_PORT/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null)
echo "vLLM serving: $SERVED_MODEL"

# --- Step 2: Run 5 seeds ---
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
        echo "WARNING: Seed $seed failed with exit code $EXIT_CODE"
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

# --- Step 3: Shutdown vLLM ---
echo ""
echo "Shutting down vLLM..."
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

# --- Step 4: TOST ±1pp + non-inferiority δ=-3pp ---
echo ""
echo "=== Statistical Analysis ==="
python3 << 'PYEOF'
import json, os, sys
import numpy as np
from scipy import stats

outdir = "outputs/llama_oracle_t07_gsm8k"
seeds = [42, 123, 456, 789, 1024]
deltas, baseline_accs, pruned_accs = [], [], []

for seed in seeds:
    path = os.path.join(outdir, f"seed_{seed}.json")
    if not os.path.exists(path):
        print(f"  MISSING: seed {seed}")
        continue
    d = json.load(open(path))
    bl_acc = d.get("baseline", {}).get("accuracy", 0)
    op_acc = d.get("oracle_pruned", {}).get("accuracy", 0)
    delta = op_acc - bl_acc
    deltas.append(delta)
    baseline_accs.append(bl_acc)
    pruned_accs.append(op_acc)
    print(f"  Seed {seed}: baseline={bl_acc:.3f} pruned={op_acc:.3f} delta={delta:+.4f} ({delta*100:+.2f}pp)")

if len(deltas) < 2:
    print("ERROR: Need at least 2 seeds")
    sys.exit(0)

deltas = np.array(deltas)
n = len(deltas)
mean_delta = np.mean(deltas)
se = np.std(deltas, ddof=1) / np.sqrt(n)

# TOST equivalence: epsilon = ±1pp (0.01)
eps = 0.01
t_upper = (mean_delta - eps) / se if se > 0 else -999
t_lower = (mean_delta + eps) / se if se > 0 else 999
p_upper = stats.t.cdf(t_upper, df=n-1)
p_lower = 1 - stats.t.cdf(t_lower, df=n-1)
p_tost = max(p_upper, p_lower)
tost_eq = p_tost < 0.05

# Non-inferiority: delta = -3pp (-0.03)
delta_ni = -0.03
t_ni = (mean_delta - delta_ni) / se if se > 0 else 999
p_ni = 1 - stats.t.cdf(t_ni, df=n-1)
ni_pass = p_ni < 0.05

t_crit = stats.t.ppf(0.95, df=n-1)
ci_lo = mean_delta - t_crit * se
ci_hi = mean_delta + t_crit * se

print()
print(f"Summary ({n} seeds, N=200):")
print(f"  Mean baseline acc: {np.mean(baseline_accs):.3f}")
print(f"  Mean pruned acc:   {np.mean(pruned_accs):.3f}")
print(f"  Mean delta:        {mean_delta:+.4f} ({mean_delta*100:+.2f}pp)")
print(f"  SE(delta):         {se:.4f}")
print(f"  90% CI:            [{ci_lo*100:+.2f}pp, {ci_hi*100:+.2f}pp]")
print(f"  TOST (eps=±1pp):   p={p_tost:.4f} {'EQUIVALENT' if tost_eq else 'NOT EQUIVALENT'}")
print(f"  Non-inferiority (d=-3pp): p={p_ni:.4f} {'PASS' if ni_pass else 'FAIL'}")

summary = {
    "exp_id": "llama_oracle_t07_gsm8k",
    "n_seeds": n,
    "n_tasks": 200,
    "seeds": seeds[:n],
    "temperature": 0.7,
    "per_seed_deltas_pp": [d*100 for d in deltas],
    "mean_baseline_acc": float(np.mean(baseline_accs)),
    "mean_pruned_acc": float(np.mean(pruned_accs)),
    "mean_delta_pp": float(mean_delta * 100),
    "se_delta": float(se),
    "ci_90_lo_pp": float(ci_lo * 100),
    "ci_90_hi_pp": float(ci_hi * 100),
    "tost_epsilon_pp": 1.0,
    "tost_p_value": float(p_tost),
    "tost_equivalent": bool(tost_eq),
    "ni_delta_pp": -3.0,
    "ni_p_value": float(p_ni),
    "ni_pass": bool(ni_pass),
}
json.dump(summary, open(os.path.join(outdir, "tost_summary.json"), "w"), indent=2)
print(f"  Saved to {outdir}/tost_summary.json")
PYEOF

if [ $FAILED -gt 0 ]; then
    echo ""
    echo "WARNING: $FAILED seed(s) failed"
fi

echo ""
echo "=== ALL DONE at $(date) ==="
