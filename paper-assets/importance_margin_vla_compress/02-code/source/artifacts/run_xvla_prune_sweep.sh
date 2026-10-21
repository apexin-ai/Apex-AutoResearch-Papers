#!/bin/bash
# X-VLA Pruning Sweep on LIBERO-Object
# Runs keep_ratio values sequentially on GPU 0

set -e

export MUJOCO_GL=egl
export CUDA_VISIBLE_DEVICES=1
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

cd /root/autodl-tmp/importance_margin_vla_compress

MODEL_PATH="/root/autodl-tmp/X-VLA-Libero"
SUITE="libero_object"
EPISODES=50
SEED=42
DOMAIN_ID=3

K_VALUES="1.0 0.95 0.9 0.7 0.5 0.3 0.2 0.1"

echo "===== X-VLA Pruning Sweep ====="
echo "Suite: $SUITE | Episodes/task: $EPISODES | Seed: $SEED | domain_id: $DOMAIN_ID"
echo "K values: $K_VALUES"
echo ""

mkdir -p eval_results

for K in $K_VALUES; do
    echo ">>> Starting keep_ratio=$K at $(date)"
    python eval_xvla_pruning_libero.py \
        --model_path "$MODEL_PATH" \
        --suite "$SUITE" \
        --keep_ratio "$K" \
        --num_episodes "$EPISODES" \
        --seed "$SEED" \
        --domain_id "$DOMAIN_ID" \
        --gpu 0 \
        --output "eval_results/xvla_prune_k${K}_${SUITE}.json" \
        2>&1 | tee "eval_results/xvla_prune_k${K}_${SUITE}.log"
    echo ">>> Finished keep_ratio=$K at $(date)"
    echo ""
done

echo "===== All sweeps complete ====="

# Collect results summary
python3 -c "
import json, glob
results = {}
for f in sorted(glob.glob('eval_results/xvla_prune_k*_${SUITE}.json')):
    with open(f) as fh:
        d = json.load(fh)
    k = d['keep_ratio']
    results[k] = {
        'sr': d['overall_success_rate'],
        'ci': d['wilson_ci_95'],
        'tokens_kept': d['n_vision_tokens_kept'],
        'tokens_total': d['n_vision_tokens_original'],
    }

print('\n===== X-VLA Pruning Results Summary =====')
print(f'{'k':>6} {'SR%':>8} {'95% CI':>16} {'Tokens':>12}')
print('-' * 46)
for k in sorted(results.keys(), reverse=True):
    r = results[k]
    print(f'{k:>6.2f} {r[\"sr\"]*100:>7.1f}% [{r[\"ci\"][0]*100:.1f}%, {r[\"ci\"][1]*100:.1f}%] {r[\"tokens_kept\"]:>4}/{r[\"tokens_total\"]:>4}')
"
