#!/bin/bash
# Run full-scale experiment matrix: 3 topologies × 3 backbones × 300 tasks.
# Each combination writes to its own output directory.
#
# Prerequisites:
#   - vLLM serving: Qwen on :8000, Llama on :8001, Gemma on :8002
#   - conda base environment activated
#
# Usage:
#   bash scripts/run_full_scale.sh                    # run all 9 combos
#   bash scripts/run_full_scale.sh qwen round_robin   # run single combo

set -euo pipefail
cd "$(dirname "$0")/.."

export PYTHONPATH=src:$PYTHONPATH
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets

BACKBONES=("qwen" "llama" "gemma")
TOPOLOGIES=("round_robin" "sequential" "selector")

# Model name → port mapping
declare -A MODEL_NAMES
MODEL_NAMES[qwen]="Qwen2.5-7B-Instruct"
MODEL_NAMES[llama]="meta-llama/Llama-3.1-8B-Instruct"
MODEL_NAMES[gemma]="google/gemma-2-9b-it"

declare -A MODEL_PORTS
MODEL_PORTS[qwen]=8000
MODEL_PORTS[llama]=8001
MODEL_PORTS[gemma]=8002

run_combo() {
    local backbone=$1
    local topology=$2
    local model_name="${MODEL_NAMES[$backbone]}"
    local port="${MODEL_PORTS[$backbone]}"
    local out_dir="outputs/full_scale/${backbone}_${topology}"

    echo "=== Running: ${backbone} × ${topology} ==="
    mkdir -p "${out_dir}/traces" "${out_dir}/local_impact" "${out_dir}/annotations" "${out_dir}/correctness" "${out_dir}/figures"

    # Generate per-combo config by overriding base
    local combo_cfg="${out_dir}/config.yaml"
    python3 -c "
import yaml
with open('configs/full_scale.yaml') as f:
    cfg = yaml.safe_load(f)
cfg['model']['name'] = '${model_name}'
cfg['model']['api_base'] = 'http://localhost:${port}/v1'
cfg['trace_collection']['topology'] = '${topology}'
cfg['output']['trace_dir'] = '${out_dir}/traces'
cfg['output']['impact_dir'] = '${out_dir}/local_impact'
cfg['output']['annotation_dir'] = '${out_dir}/annotations'
cfg['output']['correctness_dir'] = '${out_dir}/correctness'
cfg['output']['figure_dir'] = '${out_dir}/figures'
cfg['output']['analysis_dir'] = '${out_dir}'
with open('${combo_cfg}', 'w') as f:
    yaml.dump(cfg, f, default_flow_style=False)
"

    # Step 1: Trace collection
    echo "[${backbone}×${topology}] Step 1/5: Trace collection..."
    python src/trace_collection.py --config "${combo_cfg}" --topology "${topology}"

    # Step 2: Local impact
    echo "[${backbone}×${topology}] Step 2/5: Local impact..."
    python src/local_impact.py --config "${combo_cfg}"

    # Step 3: Functional annotation (cross-model with model_b)
    echo "[${backbone}×${topology}] Step 3/5: Annotation..."
    python src/functional_annotation.py --config "${combo_cfg}" --cross-model

    # Step 4: Correctness annotation
    echo "[${backbone}×${topology}] Step 4/5: Correctness..."
    python src/correctness_annotation.py --config "${combo_cfg}"

    # Step 5: Analysis
    echo "[${backbone}×${topology}] Step 5/5: Analysis..."
    python src/analysis.py --config "${combo_cfg}"

    echo "=== Done: ${backbone} × ${topology} → ${out_dir} ==="
}

# Allow running single combo: bash scripts/run_full_scale.sh qwen round_robin
if [ $# -eq 2 ]; then
    run_combo "$1" "$2"
    exit 0
fi

# Run all combos sequentially
for backbone in "${BACKBONES[@]}"; do
    for topology in "${TOPOLOGIES[@]}"; do
        run_combo "$backbone" "$topology" || echo "FAILED: ${backbone} × ${topology}"
    done
done

echo "Full-scale experiment complete."
