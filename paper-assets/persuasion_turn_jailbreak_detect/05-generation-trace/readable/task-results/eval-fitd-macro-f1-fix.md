# eval fitd macro f1 fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fitd-macro-f1-fix_20260518T190405_result.json`
- **Structured JSON:** [`6c551082ce3c4cf8205e.json`](../../sessions/6c/6c551082ce3c4cf8205e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

FITD macro F1 结果：

| K | binary F1 | macro F1 | TP | FP | FN | TN |
|---|-----------|----------|----|----|----|----|
| k1 | 0.0000 | **0.2436** | 0 | 0 | 80 | 38 |
| k2 | 0.0000 | **0.2436** | 0 | 0 | 80 | 38 |
| k3 | 0.0000 | **0.2436** | 0 | 0 | 80 | 38 |
| k5 | 0.0247 | **0.2575** | 1 | 0 | 79 | 38 |
| full | 0.0247 | **0.2575** | 1 | 0 | 79 | 38 |

模型几乎全部预测 benign，k5/full 仅检出 1 个 jailbreak。macro F1 约 0.24-0.26，与任务描述中的手算估计（0.244）吻合。

---
