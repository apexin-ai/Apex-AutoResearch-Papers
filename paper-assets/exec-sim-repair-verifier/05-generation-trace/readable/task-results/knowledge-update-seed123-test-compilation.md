# knowledge update seed123 test compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update-seed123-test-compilation_20260515T121912_result.json`
- **Structured JSON:** [`4417ccb1306c74b6b393.json`](../../sessions/44/4417ccb1306c74b6b393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。变更摘要：

**seed123 8B test curve** — 从 3/6 补全到 6/6：
- 新增 ckpt-200 (72.55%, below majority baseline)、ckpt-6600 (84.90%)、ckpt-6633 (84.89%)
- Test-best = ckpt-3000 (85.60%, f1_macro=78.38)，与 val-best 一致
- 所有数据来自 registry，per-class F1 全部填入

**s42 test curve** — 从 7/8 补全到 8/8：
- 新增 ckpt-200 (70.07%, below majority baseline)

**附带修复**：
- 4B seed123 test F1 从 — 更新为 registry 实际值 (f1_macro=67.03)
- 移除 JSON 中重复的 `4b_v5_test5120` key

---
