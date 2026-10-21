# code folio max tokens fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_folio_max_tokens_fix_20260515T223127_result.json`
- **Structured JSON:** [`9d912d2bd44923804856.json`](../../sessions/9d/9d912d2bd44923804856.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

- **文件**: `eval_folio.py` **第34行**
- **改动**: `default=16384` → `default=12288`
- 项目 `*.py` 中无 16384 残留。

---
