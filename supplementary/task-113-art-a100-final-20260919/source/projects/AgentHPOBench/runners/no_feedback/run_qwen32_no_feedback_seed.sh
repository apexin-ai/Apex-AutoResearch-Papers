#!/usr/bin/env bash
set -euo pipefail

SEED="${1:?replicate seed 0, 1, or 42}"
GPU_ID="${2:?gpu id}"

case "$SEED" in
  0|1|42) ;;
  *)
    echo "Seed must be 0, 1, or 42, got: $SEED" >&2
    exit 2
    ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT"
TASK_OVERLAY="${AUTOREP_TASK_OVERLAY:-$ROOT/tasks/ablations/no_feedback}"
DRIVER_DIR="$ROOT/runners/no_feedback"
DRIVER="${AUTOREP_NO_FEEDBACK_DRIVER:-$DRIVER_DIR/run_strict_no_feedback.py}"
RUN_TAG="${AUTOREP_RUN_TAG:-qwen32_no_feedback_multiseed}"
CONDA_ROOT="${CONDA_ROOT:-/opt/miniconda3}"
MODEL_PATH="${AUTOREP_MODEL_PATH:-$ROOT/models/Qwen/Qwen3-32B}"
SLUG="qwen3_32b_no_feedback_seed${SEED}_final30"
LABEL="Qwen3-32B-NoFeedback-Seed${SEED}"
RESULT_BASE="$ROOT/results/$RUN_TAG/$SLUG"
LOG_BASE="$ROOT/logs/$RUN_TAG/$SLUG"

NONRAY_TASKS="${AUTOREP_NONRAY_TASKS:-llm_c_fineweb10b,torch_conv_kan_cifar10,open_r1_math500,agent_lightning_room_selector,uni2ts_lsf_etth1,timesfm_etth1_long_horizon,modernbert_mnli_accuracy,cifar10_airbench94,noisygl_cora_uniform30_gcn,tabmini_molecular_biology_promoters_auc,binary_diffusion_adult_rf,xlstm_parity,vbll_yacht_rmse,tabm_california_rmse,timexer_pjm_168_24_mse,ablkit_hwf_reasoning_accuracy,tunedgnn_cora_gcn_accuracy,forest_diffusion_iris_f1fake,var_imagenet256,chronos_t5_tiny_monash_weather_wql,hyperboliccv_cifar100_accuracy,itransformer_ettm2_96_mse,timemixer_ettm2_96_mse,open_r1_multimodal_mathvista_accuracy,rankup_utkface_mae,sparsetsf_ettm1_96_mse}"
RAY_TASKS="${AUTOREP_RAY_TASKS:-verl_grpo_gsm8k,align_anything_ragen_bandit,art_2048_win_rate,simple_rl_reason_qwen25_05b_math500}"

if [ -x "$CONDA_ROOT/envs/autorep-vlm2vec/bin/python3" ]; then
  export PATH="$CONDA_ROOT/envs/autorep-vlm2vec/bin:$PATH"
fi

if [ "${AUTOREP_DRY_RUN:-0}" = 1 ]; then
  test -f "$DRIVER"
  test -d "$MODEL_PATH"
  IFS=',' read -ra nonray_array <<< "$NONRAY_TASKS"
  IFS=',' read -ra ray_array <<< "$RAY_TASKS"
  all_tasks=("${nonray_array[@]}" "${ray_array[@]}")
  test "${#all_tasks[@]}" -eq 30
  for task in "${all_tasks[@]}"; do
    test -d "$TASK_OVERLAY/$task"
  done
  grep -q "history = history\\[:1\\]" "$DRIVER"
  echo "DRY_RUN_OK seed=$SEED gpu=$GPU_ID tasks=${#all_tasks[@]} no_feedback=1"
  exit 0
fi

mkdir -p "$RESULT_BASE" "$LOG_BASE/nonray" "$LOG_BASE/ray"

export AUTOREP_ROOT="$ROOT"
export AUTOREP_SERIAL_TASK_ROOT="$TASK_OVERLAY"
export AUTOREP_SERIAL_SLUG="$SLUG"
export AUTOREP_SERIAL_RESULTS_BASE="$RESULT_BASE"
export AUTOREP_SERIAL_MODEL_PATH="$MODEL_PATH"
export AUTOREP_SERIAL_AGENT_LABEL="$LABEL"
export AUTOREP_SERIAL_MODEL_LABEL="$LABEL"
export AUTOREP_SERIAL_BACKEND=hf
export AUTOREP_SERIAL_INTERVENTIONS=5
export AUTOREP_SERIAL_REUSE_QWEN3_8B=0
export AUTOREP_MODEL_SLUG="$SLUG"
export AUTOREP_MODEL_LABEL="$LABEL"
export AUTOREP_AGENT_LABEL="$LABEL"
export AUTOREP_AGENT_BACKEND=hf
export AUTOREP_MODEL_PATH="$MODEL_PATH"
export QWEN3_MODEL="$MODEL_PATH"
export AUTOREP_SPACE_VARIANT=original
export AUTOREP_NO_FEEDBACK=1

export AUTOREP_REPLICATE_SEED="$SEED"
export AUTOREP_PROCESS_SEED="$SEED"
export AUTOREP_RANDOM_SEED="$SEED"
export PYTHONHASHSEED="$SEED"
export ABLKIT_HWF_SEED="$((1 + SEED))"
export MODERNBERT_SEED="$((42 + SEED))"
export NOISYGL_SEED="$((3000 + SEED))"
export NOISYGL_NOISE_SEED="$((3000 + SEED))"
export SPARSETSF_SEED="$((2023 + SEED))"
export TABM_SEED="$((1 + SEED))"
export TUNEDGNN_SEED="$((123 + SEED))"

export RESULT_FILE_AGENT_NAME=QwenLocal
export AUTOREP_USE_CHAT_TEMPLATE=1
export AUTOREP_QWEN_NO_THINK=1
export AUTOREP_AGENT_MAX_NEW_TOKENS=512
export AUTOREP_AGENT_TEMPERATURE=0.0
export AUTOREP_AGENT_TORCH_DTYPE=bfloat16
export AUTOREP_KEEP_AGENT_LOADED=0
export AUTOREP_API_PATCH_TRANSFORMERS=0
export AUTOREP_REJECT_FALLBACK=1
export AUTOREP_STOP_ON_TASK_ERROR=1

export PILOT_CUDA_VISIBLE_DEVICES="$GPU_ID"
export CUDA_VISIBLE_DEVICES="$GPU_ID"
export QWEN_CUDA_VISIBLE_DEVICES="$GPU_ID"
export AUTOREP_BENCHMARK_DEVICE=cuda:0
export AGENT_LIGHTNING_CUDA_VISIBLE_DEVICES="$GPU_ID"
export VBLL_CUDA_VISIBLE_DEVICES="$GPU_ID"
export TABM_CUDA_VISIBLE_DEVICES="$GPU_ID"
export TIMEXER_CUDA_VISIBLE_DEVICES="$GPU_ID"
export ALIGN_ANYTHING_CUDA_VISIBLE_DEVICES="$GPU_ID"
export ART_CUDA_VISIBLE_DEVICES="$GPU_ID"
export HYPERCV_CUDA_VISIBLE_DEVICES="$GPU_ID"
export ITRANSFORMER_CUDA_VISIBLE_DEVICES="$GPU_ID"
export TIMEMIXER_CUDA_VISIBLE_DEVICES="$GPU_ID"
export SPARSETSF_CUDA_VISIBLE_DEVICES="$GPU_ID"
export TORCH_CONV_KAN_CUDA_VISIBLE_DEVICES="$GPU_ID"
export SIMPLE_RL_CUDA_VISIBLE_DEVICES="$GPU_ID"
export VERL_CUDA_VISIBLE_DEVICES="$GPU_ID"
export CHRONOS_CUDA_VISIBLE_DEVICES="$GPU_ID"
export VAR_CUDA_VISIBLE_DEVICES="$GPU_ID"
export MATHVISTA_CUDA_VISIBLE_DEVICES="$GPU_ID"
export RANKUP_CUDA_VISIBLE_DEVICES="$GPU_ID"

export PILOT_FORCE="${PILOT_FORCE:-0}"
export TASK_TIMEOUT="${TASK_TIMEOUT:-21600}"
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
export TRANSFORMERS_OFFLINE="${TRANSFORMERS_OFFLINE:-1}"
export HF_DATASETS_OFFLINE="${HF_DATASETS_OFFLINE:-1}"
export TOKENIZERS_PARALLELISM=false
export PYTHONPATH="$TASK_OVERLAY/seed_shim:$ROOT:${PYTHONPATH:-}"

echo "=== QWEN32 NO-FEEDBACK START $(date -Is) seed=$SEED gpu=$GPU_ID slug=$SLUG ==="

export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE/nonray"
export PILOT_WORKER_NAME="qwen3_32b_no_feedback_seed${SEED}_nonray"
export PILOT_TASKS="$NONRAY_TASKS"
python3 "$DRIVER"

if [ "${AUTOREP_SKIP_RAY:-0}" = 1 ]; then
  echo "=== QWEN32 NO-FEEDBACK END $(date -Is) seed=$SEED rc=0 skip_ray=1 ==="
  exit 0
fi

echo "=== WAITING FOR NO-FEEDBACK RAY LOCK $(date -Is) seed=$SEED ==="
exec 9>/tmp/agenthpobench_qwen32_no_feedback_multiseed_ray.lock
flock -x 9
echo "=== NO-FEEDBACK RAY LOCK ACQUIRED $(date -Is) seed=$SEED gpu=$GPU_ID ==="

export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE/ray"
export PILOT_WORKER_NAME="qwen3_32b_no_feedback_seed${SEED}_ray"
export PILOT_TASKS="$RAY_TASKS"
python3 "$DRIVER"

flock -u 9
echo "=== QWEN32 NO-FEEDBACK END $(date -Is) seed=$SEED rc=0 ==="
