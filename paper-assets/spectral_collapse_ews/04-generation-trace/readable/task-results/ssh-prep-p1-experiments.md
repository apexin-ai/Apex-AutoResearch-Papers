# ssh prep p1 experiments

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-p1-experiments_20260521T232506_result.json`
- **Structured JSON:** [`1d5ddc69508c77759733.json`](../../sessions/1d/1d5ddc69508c77759733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总报告：

---

### 预验证结果

| 检查项 | 结果 |
|--------|------|
| `run_phase1.py` 参数支持 | **通过** — `--real_ratio` 接受任意 float，r=0.2 和 r=0.5 均正确解析 |
| Dry-run r=0.2 seed43 | **通过** — real_ratio=0.2, k=0.0, tau=0.002, generations=10 |
| Dry-run r=0.5 seed43 | **通过** — real_ratio=0.5, k=0.0, tau=0.002, generations=10 |
| Checkpoint 目录冲突 | **无冲突** — 两个目录均不存在 |
| 磁盘空间 | **86G 可用**（已用 165G/250G，现有 checkpoints 占 46G） |

### 启动脚本

**P1-a:** `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r020_seed43.sh`
```bash
#!/bin/bash
# P1-a: r=0.20 seed43 — fixed_mix low-real trajectory
# Usage: bash launch_fixed_mix_r020_seed43.sh &lt;gpu_id>
set -euo pipefail
GPU_ID=${1:-0}
cd /root/spectral_collapse_ews
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1
python run_phase1.py \
    --condition fixed_mix \
    --seed 43 \
    --generations 10 \
    --signal log_det \
    --tau 0.002 \
    --k 0 \
    --signal_mode per_gen \
    --real_ratio 0.2 \
    --gpu $GPU_ID
```

**P1-b:** `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r050_seed43.sh`
```bash
#!/bin/bash
# P1-b: r=0.50 seed43 — fixed_mix standard trajectory
# Usage: bash launch_fixed_mix_r050_seed43.sh &lt;gpu_id>
set -euo pipefail
GPU_ID=${1:-0}
cd /root/spectral_collapse_ews
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1
python run_phase1.py \
    --condition fixed_mix \
    --seed 43 \
    --generations 10 \
    --signal log_det \
    --tau 0.002 \
    --k 0 \
    --signal_mode per_gen \
    --real_ratio 0.5 \
    --gpu $GPU_ID
```

### 启动方式

GPU 释放后：
```bash
# cuda:1 跑 r=0.2
CUDA_VISIBLE_DEVICES=1 nohup bash /root/spectral_collapse_ews/scripts/launch_fixed_mix_r020_seed43.sh 0 > /tmp/p1a_r020_s43.log 2>&1 &

# cuda:0 跑 r=0.5
CUDA_VISIBLE_DEVICES=0 nohup bash /root/spectral_collapse_ews/scripts/launch_fixed_mix_r050_seed43.sh 0 > /tmp/p1b_r050_s43.log 2>&1 &
```

---
