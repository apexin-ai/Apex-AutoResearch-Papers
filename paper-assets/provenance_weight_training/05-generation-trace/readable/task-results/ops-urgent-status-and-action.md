# ops urgent status and action

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-and-action_20260514T065244_result.json`
- **Structured JSON:** [`21119ed412bae8fc0623.json`](../../sessions/21/21119ed412bae8fc0623.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### GPU 占用
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 94% | 46.5/97.9 GB | grid_b_seed42_batch (b=1.0, step 5804/6103, **95%**, ~11min 完成) |
| 1 | 99% | 46.5/97.9 GB | **grid_b0_5_seed123** (PID 68163, 已启动) |
| 2 | 0% | 1.7/97.9 GB | **grid_b1_0_seed123** (PID 68306, 加载中) |
| 3 | 0% | 0/97.9 GB | **grid_b1_5_seed123** (PID 68383, 启动中) |

### Adaptive ×3 — 全部完成 (EXIT_CODE=0)
| 实验 | train_loss | runtime |
|------|-----------|---------|
| adaptive_seed42 | 9.2665 | 3h39m |
| adaptive_seed123 | 9.2665 | 3h40m |
| adaptive_seed456 | 9.2354 | 3h39m |

### Grid_b Round 1 (seed123)
已启动 3 个任务：b=0.5 / 1.0 / 1.5，分别在 GPU 1/2/3，预计各 ~3.5h。

### Grid_b_seed42_batch (GPU 0)
当前跑 b=1.0，step 5804/6103 (95%)，约 11 分钟完成当前 b 值。

---
