# ssh cls14b final status urgent

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls14b-final-status-urgent_20260523T022459_result.json`
- **Structured JSON:** [`2d1ff28b295e5457dd2a.json`](../../sessions/2d/2d1ff28b295e5457dd2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练和 eval 均已完成。全量结果如下：

---

### 1. GPU 状态
4x RTX 5090 全部空闲，0 MiB 显存占用，无运行进程。

### 2. 训练进程
PID 215642 已退出。训练于 09:50 完成，耗时 **4h12m**，3 epochs / 1434 steps。

| 指标 | 值 |
|------|-----|
| train_loss | 0.3187 |
| eval_loss | 0.0918 |
| 速度 | 3.03 samples/s |

### 3. Auto-eval
自动触发成功，使用 checkpoint-956（best），09:53:25 完成。

### 4. CLS 14B v2 Eval 结果

| 指标 | 值 |
|------|-----|
| **Overall Accuracy** | **89.47%** |
| Accuracy vs Baseline Gap | **+37.72pp** (baseline 51.75%) |
| Unparseable | **0** |

**Per-class:**

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| fail | 89.57% | 88.49% | **89.02%** | 912 |
| pass | 89.38% | 90.39% | **89.88%** | 978 |

**Confusion Matrix:**

|  | Pred fail | Pred pass |
|--|-----------|-----------|
| Actual fail | **807** (TN) | 105 (FP) |
| Actual pass | 94 (FN) | **884** (TP) |

### 5. Checkpoints
- `checkpoint-956` (best, epoch 2)
- `checkpoint-1434` (final, epoch 3)
- `best/` (symlink/copy of checkpoint-956)

**MVP-B criteria: PASS** — 两个 class F1 均 >65%，accuracy gap ≥10pp。

---
