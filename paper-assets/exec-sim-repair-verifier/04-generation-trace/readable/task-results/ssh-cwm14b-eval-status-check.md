# ssh cwm14b eval status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm14b-eval-status-check_20260523T004534_result.json`
- **Structured JSON:** [`8d3ed4f1ea310c1adb08.json`](../../sessions/8d/8d3ed4f1ea310c1adb08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### CWM 14B Eval
**已自动触发，且已完成。** auto-eval 监控脚本成功检测到训练 PID 211098 退出，在 08:28:48 CST 自动启动 eval，08:36:29 CST 完成（耗时约 8 分钟）。

- Checkpoint: `checkpoint-956`
- **Overall accuracy: 89.3%**（vs majority baseline 51.7%，+37.5pp）
- Per-class F1: fail=88.3%, pass=90.1%
- Exact match rate: 86.6%
- MVP-B criteria: **PASS**
- Unparseable predictions: 0

弱点：IndexError（55.0% acc）、RecursionError（28.6%）、OverflowError（0%），但这些类别样本极少（分别 20/7/3）。

### GPU 1 状态
空闲，0 MiB VRAM，0% 利用率。Eval 已跑完释放。

### CLS 14B v2 训练进度
GPU 0 在跑，16.9GB VRAM，96% 利用率。进度 **1074/1434 steps（74.9%）**，epoch 2 eval loss = 0.077。速度 ~10.1s/it，剩余 ~360 steps，预计还需 **约 61 分钟**完成。

---
