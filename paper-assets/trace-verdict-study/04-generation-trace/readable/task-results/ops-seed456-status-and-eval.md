# ops seed456 status and eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed456_status_and_eval_20260521T121654_result.json`
- **Structured JSON:** [`e85e37216b341a16534f.json`](../../sessions/e8/e85e37216b341a16534f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## seed456 eval 完成

### 训练总结
- **状态**: ✅ 完成（444/444 steps, 3 epochs, 2h11m）
- **train_loss**: 0.0416 | **eval_loss**: 0.0794 | **token_accuracy**: 98.39%

### Eval 结果（full_trace, n=1190）

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | **82.35%** | [80.17%, 84.54%] |
| Majority baseline | 71.51% | [69.16%, 73.87%] |
| **Lift over baseline** | **+10.84pp** | [+7.90pp, +13.95pp] |
| Pass Precision | 88.85% | [86.75%, 91.07%] |
| Pass Recall | 86.13% | [83.73%, 88.36%] |
| Pass F1 | 87.47% | [85.68%, 89.11%] |
| Fail Precision | 67.67% | [63.02%, 72.41%] |
| Fail Recall | 72.86% | [68.21%, 77.78%] |
| Fail F1 | 70.17% | [66.18%, 73.92%] |

### GPU 状态
- GPU 0: 49175/97887 MiB, 0% util（残留显存，无活跃进程）
- GPU 1: 0/97887 MiB, 0% util（完全空闲）

---
