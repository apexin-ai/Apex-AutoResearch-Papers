# monitor grpo v2 reward check

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v2-reward-check_20260514T113947_result.json`
- **Structured JSON:** [`79f00c64252df0370406.json`](../../sessions/79/79f00c64252df0370406.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GRPO v2
- **Step 4/73**，~10.3 min/step，已运行 42 分钟，ETA ~11.8h
- **暂无 reward/loss 输出**，原因：脚本 `logging_steps=5`，metrics 将在 **step 5 首次出现**（约 10 分钟后）
- 当前无法判断 reward 是否非零，需要等 step 5 的 log

### eval-sft-v2-ckpt
- PID 32728 **存活**，正在运行
- 进度 **97/202**（48%），~10s/sample，预计还需 ~17 分钟完成

### 建议
10 分钟后再查 GRPO v2 日志，届时 step 5 的 metrics 应该已经输出，可以判断 reward 是否非零。

---
