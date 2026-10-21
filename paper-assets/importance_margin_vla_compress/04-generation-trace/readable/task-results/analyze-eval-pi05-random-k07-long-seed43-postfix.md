# analyze eval pi05 random k07 long seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k07_long_seed43_postfix_20260524T223350_result.json`
- **Structured JSON:** [`d9c1bbefd1a7d08bc1f7.json`](../../sessions/d9/d9c1bbefd1a7d08bc1f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：实验 `eval_pi05_random_k07_long_seed43_postfix` 从未启动。**

证据：
1. **Registry**：无此实验记录（既不在 RUNNING 也不在 DONE 中）
2. **日志文件**：cqa1-33015 上 `find /root -name "*k07*long*seed43*"` 返回空
3. **Cron**：当前 session 无活跃 cron job

相近的实验存在于 westd-41074 上（`eval_pi05_random_k085_long_seed43_postfix` 和 `eval_pi05_random_k09_long_seed43_postfix`，均为 RUNNING 状态），但 k=0.7 的 Long seed43 版本从未被注册或执行。

无需更新 registry 或删除 cron — 这个实验需要被创建和启动，而非分析结果。

---
