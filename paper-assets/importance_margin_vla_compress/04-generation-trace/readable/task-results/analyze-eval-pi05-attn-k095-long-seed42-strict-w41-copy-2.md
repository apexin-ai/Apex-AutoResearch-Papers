# analyze eval pi05 attn k095 long seed42 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k095_long_seed42_strict_w41_20260527T104342_result.json`
- **Structured JSON:** [`2f03d650ab42cbfe21b8.json`](../../sessions/2f/2f03d650ab42cbfe21b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**仍在运行**，尚未完成：

- 日志只有 26 行，最后一条 `18:43:36` — PRUNE-DIAG 输出后进入 torch compile 阶段
- `/tmp/agent-ml-exit/eval_pi05_attn_k095_long_seed42_strict_w41.exit` 不存在（无退出信号）
- `ps` 显示 pts/4 上有大量 torch compile workers（PID 433369 及其子进程），18:43 启动

实验启动时间约 1 小时前（18:41），当前处于首次推理前的 torch.compile 编译阶段。π0.5 Long suite 通常需要 ~3h，预计完成时间约 21:40-22:00 UTC。

不应更新 registry 为 DONE，当前状态应为 RUNNING。是否需要我将 registry 状态从 ANALYZING 改回 RUNNING？

---
