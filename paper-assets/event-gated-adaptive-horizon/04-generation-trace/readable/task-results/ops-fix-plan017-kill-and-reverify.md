# ops fix plan017 kill and reverify

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-plan017-kill-and-reverify_20260515T100255_result.json`
- **Structured JSON:** [`4b4de3a6181a97d8426c.json`](../../sessions/4b/4b4de3a6181a97d8426c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 验证通过。

---

## 完整报告

### 1. 进程清理
5 个 dry run 进程全部已杀：130056, 130470, 130846, 131371, 131916。无其他 plan017 残留进程。

### 2. submit_plan017.sh 内容确认
脚本已包含 `--gate_subsample_max_dt 1`，无需修复。

### 3. 代码逻辑验证
- `models.py:216`: `gate_subsample_max_dt=1` → `subsample_eff_dt=1.0`
- `tools.py:776-778`: `effective_max_dt <= 1` → `dt_labels = ones`，**直接跳过 subsampling，返回原始数据**

### 4. Dry run 结果
| 配置 | dt_labels 唯一值 | subsample 状态 |
|------|-----------------|---------------|
| `gate_subsample_max_dt=1` (plan_017) | `[1]` | **OFF** — 全部 dt=1 |
| `gate_subsample_max_dt=0` + `effective_max_dt=2` (008d-like) | `[1, 2]` | ON — 有 dt>1 |

### 5. 最终确认的完整训练命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && \
cd /root/autodl-tmp/event-gated-adaptive-horizon && \
nohup python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_017_subsample_off_trained_dt_emb \
  --steps 105000 --seed 1 --compile False --device cuda:0 \
  --gate_enabled True --gate_fixed_dt 2 \
  --gate_dt_embed_dim 32 \
  --gate_subsample_max_dt 1 \
  --imag_horizon 15 \
  > logdir/exp_017_subsample_off_trained_dt_emb.log 2>&1 &
```

关键参数确认：
- `--gate_subsample_max_dt 1` → subsample **OFF**
- `--gate_fixed_dt 2` → dt=2 imagination
- `--imag_horizon 15`（脚本原值，非任务描述中的 H=8）
- `--dt_emb_freeze` 未指定 → 默认 False → dt_emb **trained**
- 与 008d（subsample ON）的唯一差异就是 `gate_subsample_max_dt=1`

**配置正确，可以放心启动正式实验。**

---
