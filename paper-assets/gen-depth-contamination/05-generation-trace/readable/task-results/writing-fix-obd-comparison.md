# writing fix obd comparison

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_fix-obd-comparison_20260514T085213_result.json`
- **Structured JSON:** [`3b25df4542c0838e7f6c.json`](../../sessions/3b/3b25df4542c0838e7f6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

**修改前**：`$+$5.2--9.3\,pp over LLM zero-shot at ${\sim}$33\%` — 用 6-class OBD (38.2–42.3%) 减 5-class LLM (~33%)，粒度不匹配。

**修改后**：`$+$5.5\,pp over frontier-LLM zero-shot on the matched 5-class task, 38.6\% vs.\ ${\sim}$33\%` — 统一为 5-class 对比（OBD 38.6% vs LLM ~33%，差值 +5.5pp），并明确标注 "matched 5-class task"。

段落中 6-class 的部分（38.2–42.3% vs 16.7% random, +21.5–25.6pp）保持不变，因为它们内部一致，且已标注 "for 6-class classification"。

---
