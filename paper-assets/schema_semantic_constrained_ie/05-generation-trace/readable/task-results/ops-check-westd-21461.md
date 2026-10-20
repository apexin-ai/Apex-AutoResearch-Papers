# ops check westd 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd-21461_20260520T035101_result.json`
- **Structured JSON:** [`c0c56945dca6ad2e30bb.json`](../../sessions/c0/c0c56945dca6ad2e30bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/server_check_21461.md`。关键结论：

**d066 SciERC beam sweep** — 全部完成 (11:47 CST)，GPU1 空闲
- beam8 constrained: 551/551，DR violation 0.0%，Relation F1 = 43.65
- beam8 unconstrained: 551/551，DR violation 1.77%，Relation F1 = 43.17
- constrained 比 unc Relation F1 高 +0.48，同时消除全部 violations
- 缺 `eval_beam8_con.json`（数据在 violation report 里有）

**d065 Qwen DocRED unc greedy 4096** — 运行中，PID 167691
- 进度 104/998 (10.4%)，~2.8 docs/min，预计还需 ~5h
- GPU0 占用 87%，18.9G VRAM，状态正常

**GPU1 完全空闲**，可安排新任务（如 d065 constrained 并行跑）。

---
