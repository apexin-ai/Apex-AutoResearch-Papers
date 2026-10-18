# diagnose cqa1 process failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_process_failures_20260517T014152_result.json`
- **Structured JSON:** [`7433e5be7d046b7353d8.json`](../../sessions/74/7433e5be7d046b7353d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：两个实验都在正常运行

### 实验 1: libero_imm_fullft_k07

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 117885, GPU3, 89% CPU) |
| 最后 step | 19700/20000 (98.5%) @ 09:41:58 |
| 最新 checkpoint | `stage2/step_018000` (09:33) |
| 错误 | 无 |
| 退出原因 | **未退出，仍在运行** |

预计 ~5 分钟内完成剩余 300 steps (以 3.1 sps 计算)。step_020000 final checkpoint 即将写入。

### 实验 2: libero_fullft_seed1

| 项目 | 状态 |
|------|------|
| 进程 | **存活** (PID 45551 + 4 workers, GPU0) |
| 最后 step | 61850/100000 (61.85%) @ 09:42:07 |
| 最新 checkpoint | `step_060000` (09:34) |
| 错误 | 无 |
| 退出原因 | **未退出，仍在运行** |

以 4.2 sps 计算，剩余 ~38150 steps 约需 2.5 小时。

### 结论

两个实验进程均存活且正常训练中，reconcile 的 "进程消失" 报告是误报。可能原因：检测时 GPU utilization 短暂下降（checkpoint 写入期间）或进程检测逻辑匹配不到新的子进程 PID。无需任何恢复操作。

---
