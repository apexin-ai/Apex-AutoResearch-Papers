# diag urgent status westd cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_urgent-status-westd-cqa1_20260521T000853_result.json`
- **Structured JSON:** [`c4d79704b9bb2343ded0.json`](../../sessions/c4/c4d79704b9bb2343ded0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29999 Gemma-2 d100 retrain

| 项目 | 状态 |
|------|------|
| PID 437077 | **ALIVE**，运行 2h05m |
| 任务 | `train_sft.py` gemma-2-9b d100 s0, alpha=32, lr=5e-5 |
| GPU 0 | 82%, 72449/97887 MiB |
| 训练进度 | **50%** (2102/4159), epoch 0.35 → ~0.50, ~2h ETA |
| loss | 1.246, token_acc 0.707 |

另有 PID 435054 在 GPU 3 上跑 Qwen2.5-14B d100 s0 训练（运行 2h14m, 64773 MiB）。GPU 1/2 空闲。

## cqa1-21977 Qwen-7B ARC eval

| 项目 | 状态 |
|------|------|
| GPU 0 | 95%, 20515/24564 MiB |
| 当前进程 | PID 420269 — `evaluate.py` qwen7b **d100_s0** ARC（运行 2m22s） |

### ARC 结果 (s0)

| Dosage | ARC Acc | Status |
|--------|---------|--------|
| d000 | 87.20% | done |
| d005 | 85.32% | done |
| d025 | 84.47% | done |
| d050 | 85.58% | done |
| d100 | — | **running** |

s42_v2 和 s123 的 ARC 全部已完成（5/5 each）。s0 只差 d100，正在跑。

### 磁盘
- `/root`: 19/30G (64%)
- `/root/autodl-tmp`: 126/169G (75%)

---
