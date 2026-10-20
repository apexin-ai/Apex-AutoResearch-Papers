# fix worker result output norm

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_worker-result-output-norm_20260519T200624_result.json`
- **Structured JSON:** [`bd500fb9d58bd5798a14.json`](../../sessions/bd/bd500fb9d58bd5798a14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**根因确认**：Worker 在 Line 239 输出了完整结果汇总（1136 chars），但随后在 Line 240 调用了 `TodoWrite`，导致最后一个 assistant turn 只有 tool_use 没有 text。Claude Code 的 result event 从最后一个 turn 取文本，得到空字符串。

**产出**：
- `artifacts/worker_output_guidelines.md` — 包含根因分析、Worker 输出规范（最后一条消息必须是纯文本）、示例格式、框架改进建议（`worker.py:600` 增加 `extract_last_assistant_text` fallback）

---
