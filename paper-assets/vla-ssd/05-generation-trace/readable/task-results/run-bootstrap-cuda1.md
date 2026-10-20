# run bootstrap cuda1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_bootstrap_cuda1_20260522T150616_result.json`
- **Structured JSON:** [`2758fed125db0c522a27.json`](../../sessions/27/2758fed125db0c522a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双卡并行运行正常：

| Session | GPU | 显存占用 | 当前任务 |
|---------|-----|---------|---------|
| `bootstrap_cuda0` | GPU 0 | 2135 MiB | OpenVLA+NORA — 正在做 bootstrap (10000 iter) |
| `bootstrap_cuda1` | GPU 1 | 5277 MiB | TracVLA goal/trained — 模型已加载，开始提取特征 |

TracVLA 批次 (3 suites × 2 conditions = 6 runs) 已在 cuda:1 上启动。

---
