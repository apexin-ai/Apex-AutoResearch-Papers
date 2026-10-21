# ops nomarker seed123 real eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nomarker-seed123-real-eval_20260516T190927_result.json`
- **Structured JSON:** [`e39d67802522b9418a6e.json`](../../sessions/e3/e39d67802522b9418a6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### exception_only_nomarker seed123 真实评估结果

| Metric | 值 |
|--------|------|
| **Accuracy** | **98.32%** |
| Majority baseline | 71.51% |
| Lift over baseline | +26.81pp |
| n | 1190 |

### Per-class metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| Pass | 98.82% | 98.82% | 98.82% |
| Fail | 97.05% | 97.05% | 97.05% |
| 95% CI (accuracy) | [97.56%, 98.99%] | | |

### 与 seed42 对比

| Seed | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| seed42 | 96.55% | — | — |
| **seed123** | **98.32%** | 98.82% | 97.05% |

seed123 比 seed42 高 **+1.77pp**，表现更好。之前的旧 eval (97.82%) 确实是过时数据。

### GPU 0 状态

- `codellama13b_exception_only_seed123` 训练中（PID 299741，GPU 0 占用 84GB，100% 利用率）
- `exception_only_nomarker_seed456` 训练中（GPU 1，100% 利用率）
- Eval 已在 GPU 1 上成功完成（与 seed456 共享显存）

---
