# code prep r025 script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-r025-script_20260518T145659_result.json`
- **Structured JSON:** [`35956228ffa8935f96de.json`](../../sessions/35/35956228ffa8935f96de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查。

**路径:** `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r025_seed42.sh`

**内容:**
```bash
#!/bin/bash
# Launch fixed_mix r=0.25, seed=42, 10 generations
# Usage: bash launch_fixed_mix_r025_seed42.sh [GPU_ID]

GPU_ID=${1:-0}

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

cd /root/spectral_collapse_ews

CUDA_VISIBLE_DEVICES=${GPU_ID} \
HF_HUB_OFFLINE=1 \
TRANSFORMERS_OFFLINE=1 \
PYTHONUNBUFFERED=1 \
python run_phase1.py \
  --condition fixed_mix \
  --seed 42 \
  --generations 10 \
  --signal log_det \
  --tau 0.002 \
  --k 0 \
  --signal_mode per_gen \
  --real_ratio 0.25 \
  --gpu 0
```

**输出路径（自动生成）:**
- Checkpoint: `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed42/`
- Results: `results/phase1_fixed_mix_r025_seed42_results.json`

GPU 通过第一个参数传入，如 `bash launch_fixed_mix_r025_seed42.sh 1`。

---
