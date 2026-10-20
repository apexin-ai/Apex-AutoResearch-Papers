# code prep r03 seed43 script

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-r03-seed43-script_20260520T011021_result.json`
- **Structured JSON:** [`d680cce4919ddabbf3ad.json`](../../sessions/d6/d680cce4919ddabbf3ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并验证通过。

**脚本内容** (`/root/spectral_collapse_ews/scripts/launch_mixed_r0.3_seed43.sh`)：

```bash
#!/bin/bash
# Launch fixed_mix r=0.3 seed43 (multi-seed replication of exp_008)
# Usage: bash launch_mixed_r0.3_seed43.sh [GPU_ID]

GPU_ID=${1:-0}
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_collapse_ews

CUDA_VISIBLE_DEVICES=${GPU_ID} \
HF_HUB_OFFLINE=1 \
TRANSFORMERS_OFFLINE=1 \
PYTHONUNBUFFERED=1 \
python run_phase1.py \
  --condition fixed_mix \
  --seed 43 \
  --generations 10 \
  --signal log_det --tau 0.002 --k 0 --signal_mode per_gen \
  --real_ratio 0.3 \
  --gpu 0
```

- 语法检查：**SYNTAX OK**
- 相比原 `launch_fixed_mix_r03.sh`（seed 42，无 signal 参数），本脚本改 seed 为 43，并显式添加 `--signal log_det --tau 0.002 --signal_mode per_gen`
- 已设置可执行权限

---
