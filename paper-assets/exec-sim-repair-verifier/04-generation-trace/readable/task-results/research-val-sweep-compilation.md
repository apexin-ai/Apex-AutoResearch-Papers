# research val sweep compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_val-sweep-compilation_20260515T033146_result.json`
- **Structured JSON:** [`79de78acc9822b5812a3.json`](../../sessions/79/79de78acc9822b5812a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出注册为 `art_20260515_126c08`。

关键确认：
- **Val best = ckpt-1000 (88.23%)** ✓
- 8B s42 val@8192 有 6 个 checkpoint（200–1200），其中 ckpt-400/600 仅有 accuracy，ckpt-800 缺 f1_pass/f1_fail
- Test@8192 有 3 个 checkpoint，test best 是 ckpt-400 (84.79%)，不是 ckpt-1000——存在 val-test 不一致
- 4B v5 val@5120 有 3 个 checkpoint，best 是 ckpt-4400 (89.96%)

文件含 markdown 表格和完整 JSON，可直接用于画图。

---
