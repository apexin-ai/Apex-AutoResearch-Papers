# ops eval qwen15b no trace and calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_qwen15b_no_trace_and_calibration_20260521T151956_result.json`
- **Structured JSON:** [`b19d65e6ff793bc501ea.json`](../../sessions/b1/b19d65e6ff793bc501ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。

---

## 汇总

### Part 1: qwen1.5b_no_trace_seed42 Eval

| 指标 | 值 |
|------|-----|
| Accuracy | **72.6%** (CI: 70.1%-75.3%) |
| Majority baseline | 71.5% |
| Lift | +1.1pp (CI 含 0，**不显著**) |
| Pass F1 | 0.802 |
| Fail F1 | 0.557 |

与 qwen15b_no_trace_seed42 (67.31%) 差 5.3pp——这是独立训练的不同 checkpoint，不是重复。Registry 已从 `killed` 更新为 `success`。

### Part 2: Cross-Model Calibration (plan_019)

| Model | Accuracy | ECE | MCE | Brier |
|-------|----------|-----|-----|-------|
| Qwen-7B | 99.83% | 0.0027 | 0.8355 | 0.0013 |
| DeepSeek-6.7B | 99.33% | 0.0049 | 0.4692 | 0.0059 |
| CodeLlama-13B | 99.83% | 0.0020 | 0.0411 | 0.0013 |
| Qwen-1.5B | 99.83% | 0.0020 | 0.7549 | 0.0013 |

ECE 全部 < 0.005，calibration 跨 4 模型 3 架构 1.5B-13B 普遍良好。MCE 高值来自极少量低置信度样本（1-2 个），不具实际意义。产出已保存至 `artifacts/cross_model_calibration_plan019.json` 和 `.md`，artifact 已注册。

---
