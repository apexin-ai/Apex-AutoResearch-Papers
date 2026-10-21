# eval exp004 batch3

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-batch3_20260520T151038_result.json`
- **Structured JSON:** [`fbf2712750b458eca108.json`](../../sessions/fb/fbf2712750b458eca108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All jobs running, all 4 GPUs occupied.

---

### 产出汇总

**1. ckpt-3000 结果（已完成）**
| 指标 | 值 |
|------|-----|
| ToF | 0.1160 |
| NoF | 0.9116 |
| SYCONScore | 0.2058 |
| n_valid/n_invalid | 181/181 |

**2. exp-003 ckpt-4000 rerun** — 仍在 GPU 0 运行中，无结果。

**3. Batch 3 提交（3 jobs）**

| Checkpoint | GPU | PID | tmux session |
|-----------|-----|-----|-------------|
| ckpt-1500 | 1 | 598441 | exp-004-eval-ckpt1500 |
| ckpt-2500 | 2 | 598577 | exp-004-eval-ckpt2500 |
| ckpt-3500 | 3 | 598660 | exp-004-eval-ckpt3500 |

**4. 最终 GPU 状态** — 全部 4 张 GPU 已占满（0: 16.9GB, 1: 17.6GB, 2: 16.2GB, 3: 14.9GB）

**5. 剩余待 eval** — 4 个 checkpoint：4500, 5500, 6500, 7500。需等 Batch 3 完成后腾出 GPU。

---
