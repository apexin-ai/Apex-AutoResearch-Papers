#!/usr/bin/env bash
set -u -o pipefail

MODEL_KEY="${1:?model key}"
SEED="${2:?replicate seed 0, 1, or 42}"
GPU_ID="${3:?gpu id}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT"
OVERLAY="${AUTOREP_TASK_OVERLAY:-$ROOT/tasks/main}"
RUN_TAG="${AUTOREP_RUN_TAG:-open_weight_multiseed}"
CONDA_ROOT="${CONDA_ROOT:-/opt/miniconda3}"

case "$SEED" in
  0|1|42) ;;
  *)
    echo "Seed must be 0, 1, or 42, got: $SEED" >&2
    exit 2
    ;;
esac

if [ -x "$CONDA_ROOT/envs/autorep-vlm2vec/bin/python3" ]; then
  export PATH="$CONDA_ROOT/envs/autorep-vlm2vec/bin:$PATH"
fi

case "$MODEL_KEY" in
  qwen3_8b)
    MODEL_PATH="${QWEN3_8B_MODEL:-$ROOT/models/Qwen/Qwen3-8B}"
    MODEL_SLUG="qwen3_8b"
    MODEL_LABEL="Qwen3-8B"
    NO_THINK=1
    MAX_TOKENS=384
    ;;
  gemma2_2b)
    MODEL_PATH="${GEMMA2_2B_MODEL:-$ROOT/models/google/gemma-2-2b-it}"
    MODEL_SLUG="gemma2_2b_it"
    MODEL_LABEL="Gemma2-2B"
    NO_THINK=1
    MAX_TOKENS=384
    ;;
  llama3_1_8b)
    MODEL_PATH="${LLAMA3_1_8B_MODEL:-$ROOT/models/meta-llama/Meta-Llama-3.1-8B-Instruct}"
    MODEL_SLUG="llama3_1_8b_instruct"
    MODEL_LABEL="Llama-3.1-8B-Instruct"
    NO_THINK=1
    MAX_TOKENS=512
    ;;
  deepseek_r1_qwen_14b)
    MODEL_PATH="${DEEPSEEK_R1_QWEN_14B_MODEL:-$ROOT/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B}"
    MODEL_SLUG="deepseek_r1_distill_qwen_14b"
    MODEL_LABEL="DeepSeek-R1-Distill-Qwen-14B"
    NO_THINK=1
    MAX_TOKENS=4096
    ;;
  phi4_14b)
    MODEL_PATH="${PHI4_14B_MODEL:-$ROOT/models/microsoft/Phi-4}"
    MODEL_SLUG="phi4_14b"
    MODEL_LABEL="Phi-4-14B"
    NO_THINK=1
    MAX_TOKENS=2048
    ;;
  *)
    echo "Unknown model key: $MODEL_KEY" >&2
    exit 2
    ;;
esac


SLUG="${MODEL_SLUG}_seed${SEED}_final30"
LABEL="${MODEL_LABEL}-Seed${SEED}"
RESULT_BASE="$ROOT/results/$RUN_TAG/$SLUG"
LOG_BASE="$ROOT/logs/$RUN_TAG/$SLUG"
NONRAY_TASKS="${AUTOREP_NONRAY_TASKS:-llm_c_fineweb10b,torch_conv_kan_cifar10,open_r1_math500,agent_lightning_room_selector,uni2ts_lsf_etth1,timesfm_etth1_long_horizon,modernbert_mnli_accuracy,cifar10_airbench94,noisygl_cora_uniform30_gcn,tabmini_molecular_biology_promoters_auc,binary_diffusion_adult_rf,xlstm_parity,vbll_yacht_rmse,tabm_california_rmse,timexer_pjm_168_24_mse,ablkit_hwf_reasoning_accuracy,tunedgnn_cora_gcn_accuracy,forest_diffusion_iris_f1fake,var_imagenet256,chronos_t5_tiny_monash_weather_wql,hyperboliccv_cifar100_accuracy,itransformer_ettm2_96_mse,timemixer_ettm2_96_mse,open_r1_multimodal_mathvista_accuracy,rankup_utkface_mae,sparsetsf_ettm1_96_mse}"
RAY_TASKS="${AUTOREP_RAY_TASKS:-verl_grpo_gsm8k,align_anything_ragen_bandit,art_2048_win_rate,simple_rl_reason_qwen25_05b_math500}"

if [ "${AUTOREP_DRY_RUN:-0}" = 1 ]; then
  test -f "$OVERLAY/run_strict_space_agent.py"
  test -d "$MODEL_PATH"
  IFS=',' read -ra NONRAY_ARRAY <<< "$NONRAY_TASKS"
  IFS=',' read -ra RAY_ARRAY <<< "$RAY_TASKS"
  all_tasks=("${NONRAY_ARRAY[@]}" "${RAY_ARRAY[@]}")
  test "${#all_tasks[@]}" -eq 30
  for task in "${all_tasks[@]}"; do
    test -d "$OVERLAY/$task"
  done
  echo "DRY_RUN_OK model=$MODEL_KEY seed=$SEED gpu=$GPU_ID tasks=${#all_tasks[@]} max_tokens=$MAX_TOKENS"
  exit 0
fi

mkdir -p "$RESULT_BASE" "$LOG_BASE/nonray" "$LOG_BASE/ray"

export AUTOREP_ROOT="$ROOT"
export AUTOREP_SERIAL_TASK_ROOT="$OVERLAY"
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
export AUTOREP_QWEN_NO_THINK="$NO_THINK"
export AUTOREP_AGENT_MAX_NEW_TOKENS="$MAX_TOKENS"
export AUTOREP_AGENT_TEMPERATURE=0.0
export AUTOREP_AGENT_TORCH_DTYPE=bfloat16
export AUTOREP_KEEP_AGENT_LOADED=0
export AUTOREP_API_PATCH_TRANSFORMERS=0
export AUTOREP_REJECT_FALLBACK="${AUTOREP_REJECT_FALLBACK:-1}"
export AUTOREP_STOP_ON_TASK_ERROR="${AUTOREP_STOP_ON_TASK_ERROR:-1}"

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
export PYTHONPATH="$OVERLAY/seed_shim:$ROOT:${PYTHONPATH:-}"

echo "=== MODEL SEED START $(date -Is) model=$MODEL_KEY seed=$SEED gpu=$GPU_ID slug=$SLUG ==="

export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE/nonray"
export PILOT_WORKER_NAME="${MODEL_SLUG}_seed${SEED}_nonray"
export PILOT_TASKS="$NONRAY_TASKS"
python3 "$OVERLAY/run_strict_space_agent.py"
nonray_rc=$?
if [ "$nonray_rc" -ne 0 ]; then
  echo "=== NONRAY FAILED $(date -Is) model=$MODEL_KEY seed=$SEED rc=$nonray_rc ===" >&2
  exit "$nonray_rc"
fi

if [ "${AUTOREP_SKIP_RAY:-0}" = 1 ]; then
  echo "=== MODEL SEED END $(date -Is) model=$MODEL_KEY seed=$SEED rc=0 skip_ray=1 ==="
  exit 0
fi

echo "=== WAITING FOR RAY LOCK $(date -Is) model=$MODEL_KEY seed=$SEED ==="
exec 9>/tmp/agenthpobench_openweight_multiseed_ray.lock
flock -x 9
echo "=== RAY LOCK ACQUIRED $(date -Is) model=$MODEL_KEY seed=$SEED gpu=$GPU_ID ==="

export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE/ray"
export PILOT_WORKER_NAME="${MODEL_SLUG}_seed${SEED}_ray"
export PILOT_TASKS="$RAY_TASKS"
python3 "$OVERLAY/run_strict_space_agent.py"
ray_rc=$?

flock -u 9
echo "=== MODEL SEED END $(date -Is) model=$MODEL_KEY seed=$SEED rc=$ray_rc ==="
exit "$ray_rc"
