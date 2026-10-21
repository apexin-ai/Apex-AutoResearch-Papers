#!/bin/bash
set -euo pipefail

# Pooled IRT (N>=16) across 3 scales × 4 dosages × 2 seeds
# Benchmarks: ARC + GSM8K, S1-only exposure, MCMC warmup=2000 samples=2000

EVAL_DIR="/root/autodl-tmp/exp001/eval_results"
CKPT_DIR="/root/autodl-tmp/exp001/checkpoints"
SIGNALS_DIR="/root/autodl-tmp/exp002/signals"
OUTPUT_DIR="/root/autodl-tmp/exp006/results_pooled_n16"
EXP006_DIR="/root/contamcal-irt-calibration/exp006"
MIN_N=16

SCALES=("0.5B" "1.5B" "3B")
DOSAGES=("000" "005" "025" "100")
SEEDS=("42" "123")
BENCHMARKS=("arc_challenge" "gsm8k")

DRY_RUN=""
FORCE_ORACLE=0
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN="--dry-run" ;;
        --oracle)  FORCE_ORACLE=1 ;;
    esac
done

echo "============================================"
echo "  Pooled IRT N>=${MIN_N} — Prerequisite Check"
echo "============================================"
echo ""

# Phase 1: Check aligned eval availability
MISSING_EVAL=()
MISSING_SFT=()
FOUND=0

for scale in "${SCALES[@]}"; do
    for dose in "${DOSAGES[@]}"; do
        for seed in "${SEEDS[@]}"; do
            tag="${scale} d${dose} s${seed}"
            eval_path="${EVAL_DIR}/Qwen2.5-${scale}_d${dose}_s${seed}_aligned"
            ckpt_path="${CKPT_DIR}/Qwen2.5-${scale}_d${dose}_s${seed}"

            if [ -f "${eval_path}/eval_results.json" ]; then
                printf "  ✓ %-22s eval DONE\n" "$tag"
                FOUND=$((FOUND + 1))
            elif [ -d "${ckpt_path}/lora_adapter" ]; then
                printf "  ✗ %-22s SFT done, eval MISSING\n" "$tag"
                MISSING_EVAL+=("$tag")
            else
                printf "  ✗ %-22s SFT MISSING\n" "$tag"
                MISSING_SFT+=("$tag")
            fi
        done
    done
done

echo ""
echo "── Summary ──"
echo "Aligned evals complete: ${FOUND}/24"
echo "SFT done, eval needed:  ${#MISSING_EVAL[@]}"
echo "SFT missing:            ${#MISSING_SFT[@]}"
echo ""

if [ ${FOUND} -lt ${MIN_N} ]; then
    echo "ERROR: N=${FOUND} < ${MIN_N}. Cannot run pooled IRT."
    echo ""
    if [ ${#MISSING_EVAL[@]} -gt 0 ]; then
        echo "Quick wins (SFT done, just run aligned eval):"
        for m in "${MISSING_EVAL[@]}"; do
            echo "  - $m"
        done
    fi
    if [ ${#MISSING_SFT[@]} -gt 0 ]; then
        echo ""
        echo "Need SFT + eval:"
        for m in "${MISSING_SFT[@]}"; do
            echo "  - $m"
        done
    fi
    exit 1
fi

# Phase 2: Check S1 signal coverage
echo "=== Signal Coverage (S1 exposure) ==="
SIG_OK=0
SIG_MISSING=0
SIG_MISSING_LIST=()

for scale in "${SCALES[@]}"; do
    for dose in "${DOSAGES[@]}"; do
        for seed in "${SEEDS[@]}"; do
            eval_path="${EVAL_DIR}/Qwen2.5-${scale}_d${dose}_s${seed}_aligned"
            [ -f "${eval_path}/eval_results.json" ] || continue
            sig_dir="${SIGNALS_DIR}/Qwen2.5-${scale}_d${dose}_s${seed}"
            all_ok=1
            for bench in "${BENCHMARKS[@]}"; do
                if [ ! -f "${sig_dir}/signals_merged_${bench}.json" ]; then
                    all_ok=0
                fi
            done
            if [ $all_ok -eq 1 ]; then
                SIG_OK=$((SIG_OK + 1))
            else
                SIG_MISSING=$((SIG_MISSING + 1))
                SIG_MISSING_LIST+=("${scale}_d${dose}_s${seed}")
            fi
        done
    done
done

echo "Models with S1 signals: ${SIG_OK}/${FOUND}"
echo "Models without signals: ${SIG_MISSING}"

if [ ${SIG_MISSING} -gt 0 ] && [ ${FORCE_ORACLE} -eq 0 ]; then
    echo ""
    echo "WARNING: S1 signals incomplete. Models without signals:"
    for m in "${SIG_MISSING_LIST[@]}"; do
        echo "  - $m"
    done
    echo ""
    echo "Falling back to --oracle-exposure (dosage-based)."
    echo "To force S1 signals (pooled mode will exclude uncovered scales),"
    echo "generate signals for missing models first."
    EXPOSURE_ARGS="--oracle-exposure"
elif [ ${FORCE_ORACLE} -eq 1 ]; then
    echo "Using oracle exposure (--oracle flag)."
    EXPOSURE_ARGS="--oracle-exposure"
else
    echo "All models have S1 signals. Using S1-only exposure."
    EXPOSURE_ARGS="--signals-dir ${SIGNALS_DIR} --signal-key s1_embedding"
fi

# Phase 3: Activate conda and run
echo ""
echo "=== Running Pooled IRT ==="
echo "Benchmarks: ${BENCHMARKS[*]}"
echo "MCMC: warmup=2000, samples=2000, chains=4"
echo "Output: ${OUTPUT_DIR}/"
echo ""

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

mkdir -p "${OUTPUT_DIR}"

for bench in "${BENCHMARKS[@]}"; do
    echo "──── ${bench} ────"
    python "${EXP006_DIR}/run_exp006.py" \
        --eval-dir "${EVAL_DIR}" \
        --pool-scales 0.5B 1.5B 3B \
        --aligned-only \
        --benchmarks "${bench}" \
        ${EXPOSURE_ARGS} \
        --warmup 2000 \
        --samples 2000 \
        --output-dir "${OUTPUT_DIR}/${bench}" \
        ${DRY_RUN}
    echo ""
done

echo "=== Done. Results in ${OUTPUT_DIR}/ ==="
