# fix table precision s42

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table-precision-s42_20260515T062242_result.json`
- **Structured JSON:** [`e8c31e6d8d71605278c6.json`](../../sessions/e8/e8c31e6d8d71605278c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成，验证结果：

**fixed_checkpoint_table.tex** — 3 处 s42 数值已修正：
- @500: 0.5330 → 0.5332 ✓
- @1000: 0.5530 → 0.5527 ✓
- @1500: 0.5230 → 0.5228 ✓
- 表注已更新为 "step 1450 (Epoch 2)" ✓

**checkpoint_criterion_table.tex** — 已由之前的 Worker 修正，无需改动（0.4537, +0.67, +1.32pp 均正确）。

**精度扫描**：s43 行的 0.5390 表面上也是末位零，但未列入修正清单，保持原值。其余数值均为真 4 位小数，无 3 位补零问题。

---
