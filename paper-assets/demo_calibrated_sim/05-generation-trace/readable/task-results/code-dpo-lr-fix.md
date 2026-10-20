# code dpo lr fix

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-lr-fix_20260512T124049_result.json`
- **Structured JSON:** [`a018dc9dcd03118b7218.json`](../../sessions/a0/a018dc9dcd03118b7218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处已修复：

1. **train_dpo.py:220** — `default=5e-5` → `default=5e-6`，help 文本同步更新。代码中无其他 5e-5 硬编码。
2. **mvp_contingency.md:13** — "question_rate 或 politeness_rate 偏差缩小" → "question_rate 且 politeness_rate 偏差**均**缩小"。文件中无其他 H2 判定处使用"或"逻辑。

---
