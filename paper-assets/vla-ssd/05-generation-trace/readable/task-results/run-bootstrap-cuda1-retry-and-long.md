# run bootstrap cuda1 retry and long

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_cuda1_retry_and_long_20260522T152609_result.json`
- **Structured JSON:** [`92cc35c4962b04e18fec.json`](../../sessions/92/92cc35c4962b04e18fec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**cuda:1 retry** — 已启动，DynamicCache 修复生效。TracVLA goal trained 正在 extraction（300/5000 samples）。因为之前 trained 和 untrained 全部失败，脚本会跑全部 8 个 run（goal/spatial/object 各 trained+untrained + long trained+untrained）。

**cuda:0** — 两个 session 都活跃。cuda:0 正在 OpenVLA goal trained 的 bootstrap 10000 迭代阶段（CPU 密集，日志不更新是正常的）。GPU 占用 2126 MiB。

**注意**：原计划只重跑 3 个 untrained + 2 个 long，但实际 TracVLA 完全没有结果（trained 也全部失败在同一个 DynamicCache bug），所以脚本改为跑全部 8 个 TracVLA conditions。

---
