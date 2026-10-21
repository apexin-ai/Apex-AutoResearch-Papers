# monitor bootstrap progress check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bootstrap_progress_check_20260522T230138_result.json`
- **Structured JSON:** [`9f96fdca33dc24f5c375.json`](../../sessions/9f/9f96fdca33dc24f5c375.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/bootstrap_progress.md`。

**摘要**:
- **cuda:0**: 8/12 done，当前跑 nora/goal/trained（extraction 50%），OpenVLA 8条件全部完成，ETA ~08:15 CST
- **cuda:1**: 3/8 done，当前跑 tracvla/spatial/untrained（fitting阶段），ETA ~09:30 CST
- **瓶颈在 cuda:1**：TracVLA untrained 条件耗时是 trained 的 2x（61min vs 27min）
- 无报错，运行正常。整体预计 **09:30 CST** 全部完成。

---
