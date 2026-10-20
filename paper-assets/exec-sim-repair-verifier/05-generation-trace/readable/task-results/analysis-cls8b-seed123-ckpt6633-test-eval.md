# analysis cls8b seed123 ckpt6633 test eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-seed123-ckpt6633-test-eval_20260515T112810_result.json`
- **Structured JSON:** [`209e7d7d76d185056eec.json`](../../sessions/20/209e7d7d76d185056eec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成，status=DONE。

**seed123 ckpt-6633 (final) test 结果**：accuracy=84.89%, f1_macro=77.56%, gap vs majority=+11.9pp。

对比参考：
| | val | test |
|---|---|---|
| ckpt-3000 (val-best) | 88.69% | 85.60% |
| ckpt-6633 (final) | 87.10% | 84.89% |

Final checkpoint test 比 val-best test 低 0.71pp，符合预期的轻微 overfitting 趋势。

---
