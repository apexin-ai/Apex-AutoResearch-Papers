#!/bin/bash
# MVP pipeline: data → SFT → GRPO → eval
# Usage: bash src/run_mvp.sh [--start-from STEP]
# Steps: data_filter, generate_tests, validate_tests, distill_probes, split_data, train_sft, train_grpo, evaluate

set -euo pipefail

STEPS=(data_filter generate_tests validate_tests distill_probes split_data train_sft train_grpo evaluate)
START_FROM=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --start-from) START_FROM="$2"; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

should_run() {
    local step=$1
    if [[ -z "$START_FROM" ]]; then return 0; fi
    local found=false
    for s in "${STEPS[@]}"; do
        if [[ "$s" == "$START_FROM" ]]; then found=true; fi
        if $found && [[ "$s" == "$step" ]]; then return 0; fi
    done
    return 1
}

step_time() {
    local step=$1 start=$SECONDS
    echo ""
    echo "================================================================"
    echo "  STEP: $step"
    echo "================================================================"
    shift
    "$@"
    echo "  ✓ $step completed in $((SECONDS - start))s"
}

# Step 1: Filter DebugBench
if should_run data_filter; then
    if [[ ! -f data/debugbench_python_single.jsonl ]]; then
        step_time data_filter python src/data_filter.py
    else
        echo "  → data_filter: output exists, skipping"
    fi
fi

# Step 2: Generate tests
if should_run generate_tests; then
    if [[ ! -f data/debugbench_with_tests.jsonl ]]; then
        step_time generate_tests python src/generate_tests.py
    else
        echo "  → generate_tests: output exists, skipping"
    fi
fi

# Step 3: Validate tests (placeholder - implemented in data pipeline)
if should_run validate_tests; then
    if [[ ! -f data/debugbench_validated.jsonl ]]; then
        echo "  → validate_tests: requires validate_tests.py from data pipeline"
    else
        echo "  → validate_tests: output exists, skipping"
    fi
fi

# Step 4: Distill probes (placeholder - implemented in data pipeline)
if should_run distill_probes; then
    if [[ ! -f data/debugbench_with_probes.jsonl ]]; then
        echo "  → distill_probes: requires distill_probes.py from data pipeline"
    else
        echo "  → distill_probes: output exists, skipping"
    fi
fi

# Step 5: Split data
if should_run split_data; then
    if [[ ! -f data/train.jsonl ]] || [[ ! -f data/eval.jsonl ]]; then
        echo "  → split_data: requires split_data.py from data pipeline"
    else
        echo "  → split_data: output exists, skipping"
    fi
fi

# Step 6: Train SFT
if should_run train_sft; then
    if [[ ! -f data/train.jsonl ]]; then
        echo "ERROR: data/train.jsonl not found. Run data pipeline first."
        exit 1
    fi
    if [[ ! -d checkpoints/sft ]]; then
        step_time train_sft python src/train_sft.py \
            --wandb-run-name "sft-$(date +%Y%m%d-%H%M%S)"
    else
        echo "  → train_sft: checkpoint exists, skipping"
    fi
fi

# Step 7: Train GRPO
if should_run train_grpo; then
    if [[ ! -d checkpoints/sft ]]; then
        echo "ERROR: SFT checkpoint not found. Run train_sft first."
        exit 1
    fi
    if [[ ! -d checkpoints/grpo ]]; then
        step_time train_grpo python src/train_grpo.py \
            --sft-checkpoint checkpoints/sft \
            --wandb-run-name "grpo-$(date +%Y%m%d-%H%M%S)"
    else
        echo "  → train_grpo: checkpoint exists, skipping"
    fi
fi

# Step 8: Evaluate all modes
if should_run evaluate; then
    if [[ ! -f data/eval.jsonl ]]; then
        echo "ERROR: data/eval.jsonl not found."
        exit 1
    fi

    mkdir -p results

    echo ""
    echo "================================================================"
    echo "  STEP: evaluate (base)"
    echo "================================================================"
    python src/evaluate.py --mode base \
        --output-path results/eval_base.json \
        --wandb-run-name "eval-base"

    echo ""
    echo "================================================================"
    echo "  STEP: evaluate (sft)"
    echo "================================================================"
    python src/evaluate.py --mode sft \
        --checkpoint-path checkpoints/sft \
        --output-path results/eval_sft.json \
        --wandb-run-name "eval-sft"

    echo ""
    echo "================================================================"
    echo "  STEP: evaluate (grpo)"
    echo "================================================================"
    python src/evaluate.py --mode grpo \
        --checkpoint-path checkpoints/grpo \
        --output-path results/eval_grpo.json \
        --wandb-run-name "eval-grpo"

    echo ""
    echo "  ✓ All evaluations complete. Results in results/"
fi

echo ""
echo "================================================================"
echo "  MVP Pipeline Complete"
echo "================================================================"
