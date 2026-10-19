#!/usr/bin/env bash
set -u -o pipefail
ROOT="${AUTOREP_ROOT:-.}"
SEED="${AUTOREP_RANDOM_SEED:-0}"
SLUG="${AUTOREP_MODEL_SLUG:-bohb_style_seed${SEED}_final30}"
LOG_ROOT="${AUTOREP_AGENT_LOG_BASE:-$ROOT/logs/hpo/bohb/$SLUG}"
mkdir -p "$LOG_ROOT"
cd "$ROOT" || exit 1
echo "=== BOHB all lanes start $(date -Is) slug=$SLUG seed=$SEED ===" | tee -a "$LOG_ROOT/master.log"
PIDS=()
for spec in "lane0:0" "lane1:1" "lane2:2" "lane3:3"; do
  lane="${spec%%:*}"
  gpu="${spec##*:}"
  AUTOREP_RANDOM_SEED="$SEED" AUTOREP_MODEL_SLUG="$SLUG" bash "$ROOT/baselines/bohb/run_v5_final30_tpe_lane.sh" "$lane" "$gpu" &
  PIDS+=("$!")
  echo "launched $lane on gpu $gpu pid=${PIDS[-1]}" | tee -a "$LOG_ROOT/master.log"
done
rc=0
for pid in "${PIDS[@]}"; do
  if ! wait "$pid"; then rc=1; fi
done
echo "=== BOHB all lanes finished $(date -Is) rc=$rc ===" | tee -a "$LOG_ROOT/master.log"
exit "$rc"
