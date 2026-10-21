# fix eval accuracy bug

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_accuracy_bug_20260514T183600_result.json`
- **Structured JSON:** [`a1da43b1397d0365362d.json`](../../sessions/a1/a1da43b1397d0365362d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。变更摘要：

**根因**：`n_correct` 从 `int(accuracy * len(dataset))` 反算，浮点截断导致 29 → 28（`int(0.29 * 100)` = `int(28.9999...)` = 28）。accuracy=0.29 是对的，n_correct=28 是错的。

**修改内容**（`src/eval_gsm8k.py`）：

| 行号 | 修改前 | 修改后 |
|------|--------|--------|
| 168 | `return accuracy, results` | `return accuracy, correct, total, results` |
| 199 | `accuracy, results = evaluate(...)` | `accuracy, n_correct, n_total, results = evaluate(...)` |
| 201 | `int(accuracy * len(dataset))` | `n_correct` |
| 212 | `"n_correct": int(accuracy * len(dataset)),` | `"n_correct": n_correct,` |
| 213 | `"n_total": len(dataset),` | `"n_total": n_total,` |

语法验证通过。后续 eval 会输出正确的 n_correct=29, accuracy=0.29。

---
