# check home gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-gpu-status_20260514T052214_result.json`
- **Structured JSON:** [`a19f2b7eda50439a85a2.json`](../../sessions/a1/a19f2b7eda50439a85a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**GPU 状态**
- RTX 5090：18429 MiB / 32607 MiB 已占用，GPU 利用率 100%，温度 83°C，功耗 555W/575W
- 空闲显存：~14 GB

**Python 进程**
- PID 3039149（sonny 用户）正在运行，已运行约 18 分钟，占用 18420 MiB GPU 显存 + ~1.9 GB 内存
- PID 2947263 已不存在

**Checkpoint 目录**
- `checkpoints_repo_cls_seed123/`：**空目录**（无 checkpoint 文件）
- `checkpoints_repo_cls_v5/`：有 5 个 checkpoint — checkpoint-600, 4000, 4200, 4400, 4600（最新 4600 写入于 May 13 14:24）

**结论**
- GPU 正在被 PID 3039149 满载使用（100% 利用率），**不可用于新任务**。这很可能是 CLS v5 的训练在继续运行（checkpoint 序列在递增）。

---
