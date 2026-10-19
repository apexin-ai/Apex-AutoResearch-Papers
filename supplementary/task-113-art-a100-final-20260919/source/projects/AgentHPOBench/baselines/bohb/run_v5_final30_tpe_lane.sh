#!/usr/bin/env bash
set -u -o pipefail

LANE="${1:-lane0}"
GPU_IDS="${2:-0}"
ROOT="${AUTOREP_ROOT:-.}"
SEED="${AUTOREP_RANDOM_SEED:-0}"
SLUG="${AUTOREP_MODEL_SLUG:-bohb_style_seed${SEED}_final30}"
LABEL="${AUTOREP_MODEL_LABEL:-BOHBStyleSeed${SEED}}"
MODEL="${AUTOREP_MODEL_PATH:-models/Qwen/Qwen3-32B}"
RESULT_BASE="${AUTOREP_AGENT_RESULTS_BASE:-$ROOT/results/hpo/bohb/$SLUG}"
LOG_DIR="${AUTOREP_AGENT_LOG_BASE:-$ROOT/logs/hpo/bohb/$SLUG}/${LANE}"
mkdir -p "$RESULT_BASE" "$LOG_DIR"
cd "$ROOT" || exit 1
exec >>"$LOG_DIR/lane_driver.log" 2>&1
echo "=== final30 bohb lane start $(date -Is) slug=$SLUG seed=$SEED lane=$LANE gpu=$GPU_IDS ==="
export AUTOREP_ROOT="$ROOT"
export AUTOREP_AGENT_RESULTS_BASE="$RESULT_BASE"
export AUTOREP_AGENT_LABEL="$LABEL"
export QWEN3_MODEL="$MODEL"
export AUTOREP_MODEL_PATH="$MODEL"
export RESULT_FILE_AGENT_NAME="${RESULT_FILE_AGENT_NAME:-QwenLocal}"
export AUTOREP_AGENT_BACKEND="tpe"
export AUTOREP_RANDOM_SEED="$SEED"
export AUTOREP_SKIP_DONE="${AUTOREP_SKIP_DONE:-1}"
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_DATASETS_OFFLINE=1
export TOKENIZERS_PARALLELISM=false
export PYTHONPATH="$ROOT:$ROOT/.python_deps:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES="$GPU_IDS"
FIRST_GPU="${GPU_IDS%%,*}"
export QWEN_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export ABLKIT_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export AIRBENCH_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export BSRBF_KAN_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export EFFICIENT_KAN_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export HYPERCV_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export ITRANSFORMER_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export MNIST1D_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export MNIST1D_MLP_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export MODERNBERT_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export NOISYGL_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export NOPROP_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export OPENR1_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export SPARSETSF_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TABM_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TIMEMIXER_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TIMESFM_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TIMEXER_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TORCHKAN_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export TUNEDGNN_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export VBLL_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export XLSTM_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export VLM2VEC_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export MOGE_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export CHRONOS_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export VAR_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export MATHVISTA_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export RANKUP_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export SIMPLE_RL_CUDA_VISIBLE_DEVICES="$FIRST_GPU"
export VERL_CUDA_VISIBLE_DEVICES="${VERL_CUDA_VISIBLE_DEVICES:-$GPU_IDS}"
export AUTOREP_BENCHMARK_DEVICE="cuda:0"

case "$LANE" in
  lane0)
    TASKS=(
      "01 llm_c_fineweb10b baselines/bohb/llm_c_fineweb10b/run_formal_llm_c_fineweb10b_agent.sh"
      "05 uni2ts_lsf_etth1 baselines/bohb/uni2ts_lsf_etth1/run_formal_uni2ts_lsf_etth1_agent.sh"
      "09 noisygl_cora_uniform30_gcn baselines/bohb/noisygl_cora_uniform30_gcn/run_formal_noisygl_cora_gcn_agent.sh"
      "13 vbll_yacht_rmse baselines/bohb/vbll_yacht_rmse/run_formal_vbll_yacht_agent.sh"
      "17 tunedgnn_cora_gcn_accuracy baselines/bohb/tunedgnn_cora_gcn_accuracy/run_formal_tunedgnn_cora_agent.sh"
      "21 align_anything_ragen_bandit baselines/bohb/align_anything_ragen_bandit/run_formal_align_anything_ragen_bandit_agent.sh"
      "25 timemixer_ettm2_96_mse baselines/bohb/timemixer_ettm2_96_mse/run_formal_timemixer_ettm2_agent.sh"
      "29 sparsetsf_ettm1_96_mse baselines/bohb/sparsetsf_ettm1_96_mse/run_formal_sparsetsf_agent.sh"
    )
    ;;
  lane1)
    TASKS=(
      "02 torch_conv_kan_cifar10 baselines/bohb/torch_conv_kan_cifar10/run_formal_torch_conv_kan_cifar10_agent.sh"
      "06 timesfm_etth1_long_horizon baselines/bohb/timesfm_etth1_long_horizon/run_formal_timesfm_etth1_agent.sh"
      "10 tabmini_molecular_biology_promoters_auc baselines/bohb/tabmini_molecular_biology_promoters_auc/run_formal_tabmini_molecular_biology_promoters_auc_agent.sh"
      "14 tabm_california_rmse baselines/bohb/tabm_california_rmse/run_formal_tabm_california_agent.sh"
      "18 verl_grpo_gsm8k baselines/bohb/verl_grpo_gsm8k/run_formal_verl_grpo_gsm8k_agent.sh"
      "22 chronos_t5_tiny_monash_weather_wql baselines/bohb/chronos_t5_tiny_monash_weather_wql/run_formal_chronos_monash_weather_agent.sh"
      "26 art_2048_win_rate baselines/bohb/art_2048_win_rate/run_formal_art_2048_win_rate_agent.sh"
      "30 simple_rl_reason_qwen25_05b_math500 baselines/bohb/simple_rl_reason_qwen25_05b_math500/run_formal_simple_rl_reason_qwen25_05b_math500_agent.sh"
    )
    ;;
  lane2)
    TASKS=(
      "03 open_r1_math500 baselines/bohb/open_r1_math500/run_formal_openr1_math500_agent.sh"
      "07 modernbert_mnli_accuracy baselines/bohb/modernbert_mnli_accuracy/run_formal_modernbert_mnli_agent.sh"
      "11 binary_diffusion_adult_rf baselines/bohb/binary_diffusion_adult_rf/run_formal_binary_diffusion_adult_rf_agent.sh"
      "15 timexer_pjm_168_24_mse baselines/bohb/timexer_pjm_168_24_mse/run_formal_timexer_pjm_agent.sh"
      "19 forest_diffusion_iris_f1fake baselines/bohb/forest_diffusion_iris_f1fake/run_formal_forest_diffusion_iris_agent.sh"
      "23 hyperboliccv_cifar100_accuracy baselines/bohb/hyperboliccv_cifar100_accuracy/run_formal_hyperboliccv_cifar100_agent.sh"
      "27 open_r1_multimodal_mathvista_accuracy baselines/bohb/open_r1_multimodal_mathvista_accuracy/run_formal_open_r1_multimodal_mathvista_agent.sh"
    )
    ;;
  lane3)
    TASKS=(
      "04 agent_lightning_room_selector baselines/bohb/agent_lightning_room_selector/run_formal_agent_lightning_room_selector.sh"
      "08 cifar10_airbench94 baselines/bohb/cifar10_airbench94/run_formal_cifar10_airbench94_agent.sh"
      "12 xlstm_parity baselines/bohb/xlstm_parity/run_formal_xlstm_parity_agent.sh"
      "16 ablkit_hwf_reasoning_accuracy baselines/bohb/ablkit_hwf_reasoning_accuracy/run_formal_ablkit_hwf_agent.sh"
      "20 var_imagenet256 baselines/bohb/var_imagenet256/run_formal_var_imagenet_agent.sh"
      "24 itransformer_ettm2_96_mse baselines/bohb/itransformer_ettm2_96_mse/run_formal_itransformer_ettm2_agent.sh"
      "28 rankup_utkface_mae baselines/bohb/rankup_utkface_mae/run_formal_rankup_utkface_agent.sh"
    )
    ;;
  *) echo "Unknown lane: $LANE" >&2; exit 2 ;;
esac

run_task() {
  local idx="$1"
  local task_id="$2"
  local script="$3"
  local log="$LOG_DIR/${idx}_${task_id}.log"
  local status="$log.status"
  if [ "${AUTOREP_SKIP_DONE:-1}" = "1" ] && grep -q "^DONE" "$status" 2>/dev/null; then
    echo "=== SKIP $idx $task_id existing DONE $(date -Is) ==="
    return 0
  fi
  echo "=== START $idx $task_id $(date -Is) ==="
  echo "RUNNING $(date -Is)" > "$status"
  if timeout "${TASK_TIMEOUT:-21600}" bash "$ROOT/$script" > "$log" 2>&1; then
    echo "DONE $(date -Is)" > "$status"
    echo "=== DONE $idx $task_id $(date -Is) ==="
  else
    rc=$?
    echo "FAILED rc=$rc $(date -Is)" > "$status"
    echo "=== FAILED $idx $task_id rc=$rc $(date -Is) ==="
  fi
}

for entry in "${TASKS[@]}"; do
  idx="$(awk '{print $1}' <<<"$entry")"
  task_id="$(awk '{print $2}' <<<"$entry")"
  script="$(awk '{print $3}' <<<"$entry")"
  run_task "$idx" "$task_id" "$script"
done
echo "=== final30 bohb lane finished $(date -Is) slug=$SLUG lane=$LANE gpu=$GPU_IDS ==="
