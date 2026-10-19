# eval checkpoint inventory and eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_checkpoint-inventory-and-eval_20260522T213643_result.json`
- **Structured JSON:** [`feed9db858e626e6b953.json`](../../sessions/fe/feed9db858e626e6b953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部在用，分配正确。

---

## 汇报

### 29046 ACT S2 checkpoint 清单

训练进行到 step 6250，仍在运行。

| Checkpoint | 状态 |
|---|---|
| 500 | 已 eval（已清理，不在磁盘上） |
| 1000 | 已 eval（已清理） |
| 1500 | 已 eval（已清理） |
| 2000 | 已 eval |
| **2500** | **未 eval**（在磁盘上） |
| 3000 | 已 eval |
| 3500 | 已 eval |
| 4000 | 已 eval |
| 4500 | 已 eval |
| 5000 | 已 eval |
| **5500** | **未 eval** → 已 SCP 到 28034，GPU2 eval 中 |
| **6000** | **未 eval** → 已 SCP 到 28034，GPU0 eval 中 |

### 28034 Reduced-lora checkpoint 清单

路径：`/root/autodl-tmp/outputs/exp-004-reduced-lora/`，训练到 step 2370，仍在运行。

| Checkpoint | 状态 |
|---|---|
| 500 | 已 eval (0.1515) |
| 1000 | 已 eval (0.1700) |
| **1500** | **未 eval** |
| **2000** | **未 eval** |

### GPU 分配

| GPU | PID | 任务 | 显存 |
|---|---|---|---|
| GPU0 | 133996 | **ACT s2 ckpt-6000 eval**（本次启动） | 17650 MiB |
| GPU1 | 30011 | r3only s2 ckpt-8000 eval（之前启动的 tmux） | 21758 MiB |
| GPU2 | 134523 | **ACT s2 ckpt-5500 eval**（本次启动） | 17650 MiB |
| GPU3 | 131250 | exp-003-gs8-ckpt-500 verified eval（之前启动的） | 16874 MiB |

### PID 958710

已不存在，进程已结束。

---
