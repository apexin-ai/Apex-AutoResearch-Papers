# fix c5b bootstrap ci

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_c5b_bootstrap_ci_20260514T150812_result.json`
- **Structured JSON:** [`be8007ceb08158cb4501.json`](../../sessions/be/be8007ceb08158cb4501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。Bootstrap loop（第476行）现在使用共享 `idx = rng.randint(0, n_pair, n_pair)` 对 `u`, `o`, `h` 做 paired resampling，文件中无其他独立 `randint` 残留。

---
