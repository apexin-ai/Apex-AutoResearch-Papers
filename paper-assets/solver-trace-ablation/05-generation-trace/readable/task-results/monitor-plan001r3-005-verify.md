# monitor plan001r3 005 verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan001r3-005-verify_20260513T224257_result.json`
- **Structured JSON:** [`643d74899136e953e4b5.json`](../../sessions/64/643d74899136e953e4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### plan_005-sta-low-s42 (PID 85790) — ✅ 正常运行
- GPU 1, 87% 利用率, 65403 MiB
- 已到 step 3，~12 秒/step
- 最新 reward_log: step 3, prove_rate=0.375, parse_rate=1.0, loss=0.0676

### plan_001-exec-only-s42-r3 (PID 85710) — ❌ OOM 崩溃
- EXIT_CODE=1，在 step 0 就挂了
- 原因：GPU 0 被进程 84901 占用了 78.43 GiB，plan_001-r3 分配不到剩余内存
- 日志关键行：`torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 32.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 30.19 MiB is free. Process 84901 has 78.43 GiB memory in use.`
- reward_log.jsonl 的 13 行是之前 run 留下的（非本次 r3）

**结论**：plan_005 正常训练中；plan_001-r3 需要等 GPU 0 上的进程 84901 结束后重启，或者杀掉 84901 腾出显存。

---
