# ssh fix tokenizer compat 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_tokenizer_compat_30476_20260517T111837_result.json`
- **Structured JSON:** [`d86b823dbc31a215d580.json`](../../sessions/d8/d86b823dbc31a215d580.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器都修复完成，dry-run 通过。

**报告：**

| | westd-30476 | westd-41312 |
|---|---|---|
| transformers 版本 | 4.57.6 | 4.57.6 |
| 修复前调用点 | `processing_class=tokenizer` (之前部分修复但不完整) | `tokenizer=tokenizer` |
| dry-run | import OK | import OK |

**修复内容：**

在 `WeightedTrainer.__init__` (line 101-105) 中加了兼容层：如果 kwargs 中有 `tokenizer` 且当前 Trainer 接受 `processing_class`，则自动重命名参数。调用点统一使用 `tokenizer=tokenizer`（line 420），兼容新旧版本。

两台服务器代码已统一，实验可以重新启动。

---
