#!/usr/bin/env bash
set -euo pipefail

METHOD="${1:?method: random, tpe, or bohb}"
SEED="${2:?seed: 0, 1, or 42}"
GPU_ID="${3:?gpu id}"
PHASE="${4:?phase: nonray or ray}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT"
RUNNER="$ROOT/baselines/common/run_strict_hpo.py"

case "$METHOD" in
  random)
    TASK_ROOT="$ROOT/baselines/tpe"
    SLUG="random_search_seed${SEED}_strict5_v2"
    LABEL="RandomSearchStrict5Seed${SEED}"
    BACKEND="random"
    ;;
  tpe)
    TASK_ROOT="$ROOT/baselines/tpe"
    SLUG="tpe_search_seed${SEED}_strict5_v3"
    LABEL="TPESearchStrict5Seed${SEED}"
    BACKEND="tpe"
    ;;
  bohb)
    TASK_ROOT="$ROOT/baselines/bohb"
    SLUG="bohb_style_seed${SEED}_strict5_v3"
    LABEL="BOHBStyleStrict5Seed${SEED}"
    BACKEND="tpe"
    ;;
  *)
    echo "Unknown method: $METHOD" >&2
    exit 2
    ;;
esac

case "$SEED" in
  0|1|42) ;;
  *)
    echo "Seed must be 0, 1, or 42, got: $SEED" >&2
    exit 2
    ;;
esac

NONRAY_TASKS="${AUTOREP_NONRAY_TASKS:-llm_c_fineweb10b,torch_conv_kan_cifar10,open_r1_math500,agent_lightning_room_selector,uni2ts_lsf_etth1,timesfm_etth1_long_horizon,modernbert_mnli_accuracy,cifar10_airbench94,noisygl_cora_uniform30_gcn,tabmini_molecular_biology_promoters_auc,binary_diffusion_adult_rf,xlstm_parity,vbll_yacht_rmse,tabm_california_rmse,timexer_pjm_168_24_mse,ablkit_hwf_reasoning_accuracy,tunedgnn_cora_gcn_accuracy,forest_diffusion_iris_f1fake,var_imagenet256,chronos_t5_tiny_monash_weather_wql,hyperboliccv_cifar100_accuracy,itransformer_ettm2_96_mse,timemixer_ettm2_96_mse,open_r1_multimodal_mathvista_accuracy,rankup_utkface_mae,sparsetsf_ettm1_96_mse}"
RAY_TASKS="${AUTOREP_RAY_TASKS:-verl_grpo_gsm8k,align_anything_ragen_bandit,art_2048_win_rate,simple_rl_reason_qwen25_05b_math500}"

case "$PHASE" in
  nonray)
    TASKS="$NONRAY_TASKS"
    ;;
  ray)
    TASKS="$RAY_TASKS"
    ;;
  *)
    echo "Unknown phase: $PHASE" >&2
    exit 2
    ;;
esac

if [ "${AUTOREP_DRY_RUN:-0}" = 1 ]; then
  test -f "$RUNNER"
  test -d "$TASK_ROOT"
  IFS=',' read -ra task_array <<< "$TASKS"
  expected=26
  if [ "$PHASE" = ray ]; then
    expected=4
  fi
  test "${#task_array[@]}" -eq "$expected"
  for task in "${task_array[@]}"; do
    test -d "$TASK_ROOT/$task"
  done
  echo "DRY_RUN_OK method=$METHOD seed=$SEED gpu=$GPU_ID phase=$PHASE tasks=${#task_array[@]}"
  exit 0
fi

RESULT_BASE="$ROOT/results/${METHOD}/$SLUG"
LOG_BASE="$ROOT/logs/${METHOD}/$SLUG/$PHASE"
mkdir -p "$RESULT_BASE" "$LOG_BASE"

export AUTOREP_ROOT="$ROOT"
export AUTOREP_SERIAL_TASK_ROOT="$TASK_ROOT"
export AUTOREP_SERIAL_SLUG="$SLUG"
export AUTOREP_SERIAL_BACKEND="$BACKEND"
export AUTOREP_AGENT_BACKEND="$BACKEND"
export AUTOREP_SERIAL_AGENT_LABEL="$LABEL"
export AUTOREP_AGENT_LABEL="$LABEL"
export AUTOREP_SERIAL_MODEL_LABEL="$LABEL"
export AUTOREP_SERIAL_MODEL_PATH="${AUTOREP_MODEL_PATH:-$ROOT/models/Qwen/Qwen3-32B}"
export AUTOREP_MODEL_PATH="$AUTOREP_SERIAL_MODEL_PATH"
export AUTOREP_SERIAL_RESULTS_BASE="$RESULT_BASE"
export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE"
export RESULT_FILE_AGENT_NAME="QwenLocal"
export AUTOREP_SERIAL_INTERVENTIONS=5
export AUTOREP_INTERVENTIONS=5
export AUTOREP_RANDOM_SEED="$SEED"
export AUTOREP_TPE_SEED="$SEED"
export AUTOREP_REPLICATE_SEED="$SEED"
export AUTOREP_PROCESS_SEED="$SEED"
export PYTHONHASHSEED="$SEED"
export ABLKIT_HWF_SEED="$((1 + SEED))"
export MODERNBERT_SEED="$((42 + SEED))"
export NOISYGL_SEED="$((3000 + SEED))"
export NOISYGL_NOISE_SEED="$((3000 + SEED))"
export SPARSETSF_SEED="$((2023 + SEED))"
export TABM_SEED="$((1 + SEED))"
export TUNEDGNN_SEED="$((123 + SEED))"
export AUTOREP_SERIAL_REUSE_QWEN3_8B=0
export AUTOREP_STOP_ON_TASK_ERROR=1
export AUTOREP_REJECT_FALLBACK=1
export PILOT_FORCE=0
export PILOT_TASKS="$TASKS"
export PILOT_WORKER_NAME="${METHOD}_seed${SEED}_${PHASE}"
export PILOT_CUDA_VISIBLE_DEVICES="$GPU_ID"
export CUDA_VISIBLE_DEVICES="$GPU_ID"
export TASK_TIMEOUT=21600
export AUTOREP_VERL_TRAIN_CONDA_ENV="autorep-open-r1"
export VERL_INITIAL_CHECKPOINT="${VERL_INITIAL_CHECKPOINT:-$ROOT/checkpoints/verl/global_step_640}"
export VERL_N_GPUS_PER_NODE=1
export VERL_TENSOR_MODEL_PARALLEL_SIZE=1
export FOREST_EVAL_PYTHON="/usr/bin/python3"
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
export TRANSFORMERS_OFFLINE="${TRANSFORMERS_OFFLINE:-1}"
export HF_DATASETS_OFFLINE="${HF_DATASETS_OFFLINE:-1}"
export TOKENIZERS_PARALLELISM=false

echo "=== HPO PHASE START $(date -Is) method=$METHOD seed=$SEED gpu=$GPU_ID phase=$PHASE ==="

if [ "$PHASE" = ray ]; then
  exec 9>/tmp/agenthpobench_openweight_multiseed_ray.lock
  echo "=== WAITING FOR RAY LOCK $(date -Is) method=$METHOD seed=$SEED ==="
  flock -x 9
  echo "=== RAY LOCK ACQUIRED $(date -Is) method=$METHOD seed=$SEED gpu=$GPU_ID ==="
fi

python3 "$RUNNER"
rc=$?

if [ "$PHASE" = ray ]; then
  flock -u 9
fi

echo "=== HPO PHASE END $(date -Is) method=$METHOD seed=$SEED phase=$PHASE rc=$rc ==="
exit "$rc"
