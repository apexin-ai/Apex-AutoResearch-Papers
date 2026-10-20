#!/bin/bash
# Sync local artifacts/code/ to cqa1-38874:/root/collapse-aware-mixing/
# Run from local machine after v7 completes, before starting P0 experiments.
#
# Prerequisites:
#   - SSH config has cqa1-38874 entry
#   - v7 is NOT running (avoid overwriting files mid-experiment)
set -euo pipefail

SERVER="cqa1-38874"
REMOTE_DIR="/root/collapse-aware-mixing"
LOCAL_CODE="$(cd "$(dirname "$0")" && pwd)"
LOCAL_ARTIFACTS="$(dirname "$LOCAL_CODE")"

echo "=== Sync: $LOCAL_CODE -> $SERVER:$REMOTE_DIR ==="

# ── Core modules (training infrastructure) ──
CORE_FILES=(
    controller.py
    controlled_pipeline.py
    pilot_pipeline.py
    train.py
    config.py
    data_utils.py
    metrics.py
    generate.py
    main_experiment.py
    requirements.txt
)

# ── Analysis scripts ──
ANALYSIS_FILES=(
    analyze_sweep.py
    analyze_seed_validation.py
    evaluate_spectral_metrics.py
    run_seed_validation.sh
    analyze_generated_eff_rank.py
    analyze_layer_eff_rank.py
    analyze_ngram_leading.py
    compare_eff_rank_vs_ngram.py
)

# ── P0 launch scripts ──
LAUNCH_FILES=(
    launch_baseline_w0_p0.sh
    launch_baseline_w01_p0.sh
    launch_baseline_w03_p0.sh
    launch_baseline_w05_p0.sh
    launch_baseline_w07_p0.sh
    launch_baseline_w1_p0.sh
    launch_pi_sweep_p0.sh
    launch_seed_validation_p0.sh
)

# ── Contingency scripts ──
CONTINGENCY_FILES=(
    launch_pilot_v8_emergency.sh
    launch_pilot_v8_lowlr.sh
)

# ── Support scripts ──
SUPPORT_FILES=(
    env_init.sh
    preflight.sh
)

# ── analyze_mvp_go_nogo.py (lives outside code/) ──
EXTRA_FILES=(
    "${LOCAL_ARTIFACTS}/analyze_mvp_go_nogo.py"
)

# Collect all code/ files
ALL_LOCAL=()
for f in "${CORE_FILES[@]}" "${ANALYSIS_FILES[@]}" "${LAUNCH_FILES[@]}" "${CONTINGENCY_FILES[@]}" "${SUPPORT_FILES[@]}"; do
    if [ -f "${LOCAL_CODE}/${f}" ]; then
        ALL_LOCAL+=("${LOCAL_CODE}/${f}")
    else
        echo "WARN: missing ${f}, skipping"
    fi
done

# Add extra files from outside code/
for f in "${EXTRA_FILES[@]}"; do
    if [ -f "$f" ]; then
        ALL_LOCAL+=("$f")
    else
        echo "WARN: missing $(basename "$f"), skipping"
    fi
done

echo "Files to sync: ${#ALL_LOCAL[@]}"

# Verify remote directory exists
ssh "$SERVER" "mkdir -p $REMOTE_DIR"

# Sync all files
scp "${ALL_LOCAL[@]}" "${SERVER}:${REMOTE_DIR}/"

# Make shell scripts executable
ssh "$SERVER" "chmod +x ${REMOTE_DIR}/*.sh"

# Verify
echo ""
echo "=== Verification ==="
ssh "$SERVER" "ls -la ${REMOTE_DIR}/*.py ${REMOTE_DIR}/*.sh | wc -l"
ssh "$SERVER" "python3 -c 'from controller import ControllerConfig; print(f\"controller.py r_target default: {ControllerConfig().r_target}\")'" 2>/dev/null || echo "WARN: import check failed (conda not activated in non-login shell)"

echo ""
echo "=== Sync complete. ${#ALL_LOCAL[@]} files transferred. ==="
echo "Next: activate conda, run preflight.sh, then launch P0 experiments."
