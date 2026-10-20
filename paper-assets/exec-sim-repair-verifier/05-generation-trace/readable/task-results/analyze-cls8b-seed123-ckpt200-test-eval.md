# analyze cls8b seed123 ckpt200 test eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_cls8b-seed123-ckpt200-test-eval_20260515T115309_result.json`
- **Structured JSON:** [`aaa917acae59ca07f8b0.json`](../../sessions/aa/aaa917acae59ca07f8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇报：

## cls8b-seed123-ckpt200-test-eval 结果

| 指标 | seed123 ckpt-200 | s42 ckpt-200 | 差异 |
|------|:-:|:-:|:-:|
| **Accuracy** | 72.55% | 70.07% | **+2.48pp** |
| **F1 macro** | 70.18% | 68.18% | **+2.00pp** |
| Fail F1 | 61.78% | — | — |
| Pass F1 | 78.58% | — | — |
| Fail P / R | 49.5% / 82.1% | — | — |
| Pass P / R | 91.2% / 69.0% | — | — |
| Majority baseline | 72.96% | — | — |
| Unparseable | 0 | — | — |
| n_samples | 9,784 | — | — |

**seed123 在 ckpt-200 上全面优于 s42**：accuracy +2.48pp，f1_macro +2.00pp。

不过 seed123 accuracy (72.55%) 略低于 majority baseline (72.96%)，gap = -0.41pp，说明模型在这个 checkpoint 上判 fail 过于激进（fail recall 82% 但 fail precision 仅 49.5%），牺牲了 pass recall (69.0%)，导致整体 accuracy 被拖低。F1 macro 70.18% 仍高于 baseline 约 4pp 以上。

---
