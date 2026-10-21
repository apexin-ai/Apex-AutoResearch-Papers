# code restore probe results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_restore_probe_results_20260521T224344_result.json`
- **Structured JSON:** [`d7f9ffbd7dcae058a178.json`](../../sessions/d7/d7f9ffbd7dcae058a178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`probe_results.json` 已恢复为单 seed 格式。

**恢复结果摘要：**

| 方向 | balanced_acc | f1 | peak_layer |
|------|-------------|------|-----------|
| EN→EN | 0.7757 | 0.7814 | 28 |
| ZH→ZH | 0.7206 | 0.7121 | 13 |
| EN→ZH | 0.5956 | 0.5635 | 5 |
| ZH→EN | 0.7132 | 0.7516 | 15 |

5-seed 验证确认所有 seed 结果完全一致（std=0.0000），lbfgs 确定性成立。从 seed 0 提取写回。

---
