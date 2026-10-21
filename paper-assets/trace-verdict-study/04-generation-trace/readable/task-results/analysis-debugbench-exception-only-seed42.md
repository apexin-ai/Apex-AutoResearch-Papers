# analysis debugbench exception only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_debugbench_exception_only_seed42_20260516T012932_result.json`
- **Structured JSON:** [`0c8c37da572b30ab0130.json`](../../sessions/0c/0c8c37da572b30ab0130.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## debugbench_exception_only_seed42 实验结果

### 核心指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **100.0%** (95% CI: [100.0%, 100.0%]) |
| n | 426 |
| Majority baseline | 51.4% (always predict 'pass') |
| Lift over majority | +48.6pp |
| pass P/R/F1 | 1.00 / 1.00 / 1.00 |
| fail P/R/F1 | 1.00 / 1.00 / 1.00 |
| train_loss | 0.2435 |
| eval_loss | 0.4157 |
| 训练时长 | 836.97s (~14 min), 3 epochs |
| predictions.jsonl | 存在 (27KB, 426条) |
| Checkpoint | `/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only/final/` |

### 与基准对比

| Condition | Dataset | Accuracy | n |
|-----------|---------|----------|---|
| **debugbench_exception_only** (本次) | DebugBench | **100.0%** | 426 |
| debugbench_vota_seed42 | DebugBench | 99.77% | 426 |
| debugbench_no_trace_seed42 | DebugBench | 96.71% | 426 |
| exception_only (HE+MBPP, Qwen) | HumanEval+MBPP | 99.83% | 1190 |
| exception_only (HE+MBPP, DS seed42) | HumanEval+MBPP | 99.33% | 1190 |

### 分析

- **零错误**：426 个样本全部预测正确，无需错误样本分析。
- **exception_only 在 DebugBench 上达到 100%**，超过 VOTA (99.77%) 和 no_trace (96.71%)。这表明 exception trace 信息在 DebugBench 这类真实 bug 场景下极为有效——模型仅凭异常信息就能完美区分 pass/fail。
- 相比 no_trace 的 +3.29pp 提升，再次确认 trace 信息的核心价值。
- eval_loss (0.4157) 高于 train_loss (0.2435)，存在一定过拟合，但不影响分类准确率。

---
