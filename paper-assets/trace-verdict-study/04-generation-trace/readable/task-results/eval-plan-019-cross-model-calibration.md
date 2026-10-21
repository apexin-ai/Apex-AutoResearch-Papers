# eval plan 019 cross model calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_019_cross_model_calibration_20260521T061059_result.json`
- **Structured JSON:** [`46571565809c232eeb99.json`](../../sessions/46/46571565809c232eeb99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 实验条目 `cross_model_calibration` 已创建并标记 DONE/success。

## 结果汇总

| Model | Accuracy | ECE | MCE | Brier Score |
|---|---|---|---|---|
| **Qwen2.5-7B** | 99.83% | 0.0027 | 0.8355 | 0.0013 |
| **Qwen2.5-1.5B** | 99.83% | 0.0020 | 0.7549 | 0.0013 |
| **CodeLlama-13B** | 99.83% | 0.0020 | 0.0411 | 0.0013 |
| **DeepSeek-6.7B** | 99.33% | 0.0064 | 0.7756 | 0.0061 |

**结论**：Calibration quality 跨模型 universal 成立。4 个模型 ECE 均 < 0.007，Brier 均 < 0.007。前 3 个模型指标几乎相同（ECE~0.002, Brier~0.0013），DeepSeek 略弱但仍优秀。CodeLlama-13B MCE 最低（0.041），说明没有高置信度错误预测。

---
