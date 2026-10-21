# eval cross model calibration plan019

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross_model_calibration_plan019_20260518T135431_result.json`
- **Structured JSON:** [`71ed1a8cb41aff77070c.json`](../../sessions/71/71ed1a8cb41aff77070c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 模型 exception_only calibration 结果：

| Model | Accuracy | ECE | MCE | Brier |
|---|---|---|---|---|
| **Qwen-7B** | 0.9983 | 0.0027 | 0.8355 | 0.0013 |
| **Qwen-1.5B** | 0.9983 | 0.0020 | 0.7549 | 0.0013 |
| **DeepSeek-6.7B** | 0.9933 | 0.0064 | 0.7756 | 0.0061 |
| **CodeLlama-13B** | 0.9983 | 0.0020 | 0.0411 | 0.0013 |

关键发现：
- ECE 跨模型一致性好（0.002-0.006），exception-only 微调在不同架构/尺寸上均产生良好校准
- 3/4 模型精度相同（99.83%），DeepSeek 略低（99.33%）
- CodeLlama-13B 校准最优：MCE 仅 0.041（其余模型的高 MCE 是 1-sample bin 的统计伪影）
- DeepSeek 有独特失败模式：[0.90, 0.95) 区间 7 个样本置信度 0.918 但准确率仅 14.3%（过度自信的误分类）

结果已保存至 `artifacts/cross_model_calibration.md` 并注册。

---
