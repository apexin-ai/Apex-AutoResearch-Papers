#!/bin/bash
set -e -x

# Transfer Qwen2.5-7B s0 LoRA adapters from cqa1 to westd
# Excludes checkpoint-3125 intermediate checkpoints to save bandwidth

CKPT_ROOT="/root/autodl-tmp/exp001/checkpoints"
REMOTE="westd-29999"
REMOTE_CKPT="/root/autodl-tmp/exp001/checkpoints"

for DOSAGE in d000 d005 d025 d050 d100; do
    ADAPTER="${CKPT_ROOT}/Qwen2.5-7B_${DOSAGE}_s0/lora_adapter"

    if [ ! -f "${ADAPTER}/adapter_config.json" ]; then
        echo "SKIP: ${DOSAGE} — adapter not found at ${ADAPTER}"
        continue
    fi

    # C006: verify lora_alpha=32
    ALPHA=$(grep -o '"lora_alpha": [0-9]*' "${ADAPTER}/adapter_config.json" | grep -o '[0-9]*')
    if [ "$ALPHA" != "32" ]; then
        echo "ERROR: ${DOSAGE} has lora_alpha=${ALPHA} (expected 32), skipping"
        continue
    fi

    REMOTE_DIR="${REMOTE_CKPT}/Qwen2.5-7B_${DOSAGE}_s0/lora_adapter"
    echo "=== [$(date)] Transferring ${DOSAGE} ==="

    # Create remote directory
    ssh ${REMOTE} "mkdir -p ${REMOTE_DIR}"

    # scp files excluding checkpoint-3125 subdirectory
    for f in "${ADAPTER}"/*; do
        if [ -d "$f" ] && [ "$(basename "$f")" = "checkpoint-3125" ]; then
            echo "  SKIP checkpoint-3125 subdir"
            continue
        fi
        scp -q "$f" "${REMOTE}:${REMOTE_DIR}/"
    done

    echo "=== [$(date)] Done: ${DOSAGE} ==="
done

echo "ALL_SCP_DONE_QWEN7B_S0"
