#!/bin/bash
# ConvNeXt-T AdamW extended lr sweep: lr=3e-3, 5e-3 (5ep each)
# Extends initial sweep (1e-4, 3e-4, 1e-3) to find AdamW upper bound
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry

OUTDIR="/root/autodl-tmp/checkpoints/spectral_optim"
LOGDIR="/root/autodl-tmp/tmp"
mkdir -p "$OUTDIR" "$LOGDIR"

echo "=== ConvNeXt-T AdamW extended lr sweep: 3e-3, 5e-3 x 5ep ==="

for LR in 0.003 0.005; do
    echo "--- Starting lr=$LR ---"
    python3 scripts/p1_new_arch/convnext_t_adamw_train.py \
        --lr $LR --gpu 0 --seed 42 --epochs 5 \
        --output-dir "$OUTDIR" \
        2>&1 | tee "${LOGDIR}/convnext_adamw_lr${LR}.log"

    # Rename checkpoints to include lr (avoid overwrite between runs)
    for f in "${OUTDIR}"/convnext_t_adamw_s42_ep*.pt; do
        if [ -f "$f" ]; then
            newname=$(echo "$f" | sed "s/convnext_t_adamw_s42/convnext_t_adamw_lr${LR}_s42/")
            if [ "$f" != "$newname" ]; then
                mv "$f" "$newname"
                echo "  renamed: $(basename $f) -> $(basename $newname)"
            fi
        fi
    done

    echo "--- lr=$LR done ---"
    tail -5 "${LOGDIR}/convnext_adamw_lr${LR}.log"
    echo ""
done
echo "=== Extended sweep complete ==="
