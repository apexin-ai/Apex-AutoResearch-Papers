# diagnose eval xvla l2norm k07 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_xvla_l2norm_k07_goal_seed42_v2_20260523T203715_result.json`
- **Structured JSON:** [`dbc5802f15b64ce66cc2.json`](../../sessions/db/dbc5802f15b64ce66cc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### Crash 原因
**SIGHUP (EXIT_CODE=129)**：进程收到 SIGHUP 信号被终止。最常见原因是 SSH 会话断开（终端挂断），nohup 未正确包裹或进程未脱离终端。不是 OOM，不是 GPU 错误。

日志最后一行是 Task 3 的 Ep 11/50，之后直接 `Terminated`。

### 已完成的部分结果

| Task | 描述 | Success Rate |
|------|------|-------------|
| Task 0 | open the middle drawer of the cabinet | 32/50 (64.0%) |
| Task 1 | put the bowl on the stove | 45/50 (90.0%) |
| Task 2 | put the wine bottle on top of the cabinet | 36/50 (72.0%) |
| Task 3 | open the top drawer and put the bowl inside | 2/11 (中断，未完成) |
| Task 4-9 | 未开始 | — |

完成了 3 个完整 task + Task 3 的 11/50 episodes。**无 JSON 结果文件产出**（只有 .log 文件）。

### 当前 GPU 状态
GPU 0 空闲，GPU 1 和 GPU 2 各有一个 python 进程占用 ~4.8GB/4.9GB。该实验用的是 `cuda:0`（日志显示 `Device: cuda:0`，虽然任务描述写的 cuda:1）。

### 建议
需要重跑。可以考虑：
1. 用 `nohup ... &` 或 `tmux`/`screen` 启动，防止 SSH 断连导致 SIGHUP
2. 如果脚本支持断点续跑（从 Task 3 / domain_id 开始），可以只跑剩余部分

---
