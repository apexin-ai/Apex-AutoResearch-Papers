#!/usr/bin/env bash
set -euo pipefail

METHOD="${1:?method: tpe or bohb}"
LANE="${2:?lane: lane0..lane3}"
GPU="${3:?gpu index}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT"

case "$METHOD" in
  tpe)
    TASK_ROOT="$ROOT/baselines/tpe"
    SLUG="tpe_search_seed0_strict5_v2"
    LABEL="TPESearchStrict5Seed0"
    RESULT_BASE="$ROOT/results/tpe/$SLUG"
    LOG_BASE="$ROOT/logs/tpe/$SLUG"
    ;;
  bohb)
    TASK_ROOT="$ROOT/baselines/bohb"
    SLUG="bohb_style_seed0_strict5_v2"
    LABEL="BOHBStyleStrict5Seed0"
    RESULT_BASE="$ROOT/results/bohb/$SLUG"
    LOG_BASE="$ROOT/logs/bohb/$SLUG"
    ;;
  *)
    echo "unknown method: $METHOD" >&2
    exit 2
    ;;
esac

case "$LANE" in
  lane0) TASKS="llm_c_fineweb10b,uni2ts_lsf_etth1,noisygl_cora_uniform30_gcn,vbll_yacht_rmse,align_anything_ragen_bandit,timemixer_ettm2_96_mse,sparsetsf_ettm1_96_mse" ;;
  lane1) TASKS="torch_conv_kan_cifar10,timesfm_etth1_long_horizon,tabmini_molecular_biology_promoters_auc,tabm_california_rmse,art_2048_win_rate" ;;
  lane2) TASKS="open_r1_math500,binary_diffusion_adult_rf,timexer_pjm_168_24_mse,hyperboliccv_cifar100_accuracy,verl_grpo_gsm8k" ;;
  lane3) TASKS="agent_lightning_room_selector,cifar10_airbench94,xlstm_parity,itransformer_ettm2_96_mse,simple_rl_reason_qwen25_05b_math500" ;;
  *) echo "unknown lane: $LANE" >&2; exit 2 ;;
esac

mkdir -p "$RESULT_BASE" "$LOG_BASE/$LANE"
export AUTOREP_ROOT="$ROOT"
export AUTOREP_SERIAL_TASK_ROOT="$TASK_ROOT"
export AUTOREP_SERIAL_SLUG="$SLUG"
export AUTOREP_SERIAL_BACKEND="tpe"
export AUTOREP_AGENT_BACKEND="tpe"
export AUTOREP_SERIAL_AGENT_LABEL="$LABEL"
export AUTOREP_AGENT_LABEL="$LABEL"
export AUTOREP_SERIAL_MODEL_LABEL="$LABEL"
export AUTOREP_SERIAL_MODEL_PATH="${AUTOREP_MODEL_PATH:-$ROOT/models/Qwen/Qwen3-32B}"
export AUTOREP_MODEL_PATH="$AUTOREP_SERIAL_MODEL_PATH"
export AUTOREP_SERIAL_RESULTS_BASE="$RESULT_BASE"
export AUTOREP_SERIAL_LOG_BASE="$LOG_BASE/$LANE"
export RESULT_FILE_AGENT_NAME="QwenLocal"
export AUTOREP_SERIAL_INTERVENTIONS=5
export AUTOREP_INTERVENTIONS=5
export AUTOREP_RANDOM_SEED=0
export AUTOREP_SERIAL_REUSE_QWEN3_8B=0
export AUTOREP_STOP_ON_TASK_ERROR=0
export PILOT_FORCE="${PILOT_FORCE:-1}"
export PILOT_TASKS="$TASKS"
export PILOT_WORKER_NAME="${METHOD}_${LANE}"
export PILOT_CUDA_VISIBLE_DEVICES="$GPU"
export CUDA_VISIBLE_DEVICES="$GPU"
export TASK_TIMEOUT="${TASK_TIMEOUT:-21600}"
export AUTOREP_VERL_TRAIN_CONDA_ENV="autorep-open-r1"
export VERL_INITIAL_CHECKPOINT="${VERL_INITIAL_CHECKPOINT:-$ROOT/checkpoints/verl/global_step_640}"
export VERL_N_GPUS_PER_NODE=1
export VERL_TENSOR_MODEL_PARALLEL_SIZE=1
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
export TRANSFORMERS_OFFLINE="${TRANSFORMERS_OFFLINE:-1}"
export HF_DATASETS_OFFLINE="${HF_DATASETS_OFFLINE:-1}"
export TOKENIZERS_PARALLELISM=false

exec python3 "$ROOT/baselines/common/run_strict_hpo.py"
