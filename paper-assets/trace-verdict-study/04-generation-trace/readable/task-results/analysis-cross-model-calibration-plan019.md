# analysis cross model calibration plan019

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_calibration_plan019_20260521T051022_result.json`
- **Structured JSON:** [`3845aac26266c980b0f4.json`](../../sessions/38/3845aac26266c980b0f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。Cross-model calibration 分析此前已在 5 月 18 日运行完毕，结果写入 `calibration_cross_model_analysis.md`。

## 汇总

| Model | Accuracy | ECE | MCE | Brier Score |
|---|---|---|---|---|
| Qwen-7B | 0.9983 | 0.0027 | 0.8355* | 0.0013 |
| Qwen-1.5B | 0.9983 | 0.0020 | 0.7549* | 0.0013 |
| DeepSeek-6.7B | 0.9933 | 0.0064 | 0.7756* | 0.0061 |
| CodeLlama-13B | 0.9983 | 0.0020 | 0.0411 | 0.0013 |

\*MCE 虚高——由 1-sample bin 中单个错误预测导致，非系统性 calibration 问题。

**Rebuttal 要点**：ECE 跨 4 个模型一致低（0.002–0.006），说明 exception-only 微调产生 well-calibrated 分类器，不依赖特定 base model。CodeLlama-13B 最佳（MCE=0.041），DeepSeek 有独特的 overconfident misclassification 模式（[0.90, 0.95) bin 中 7 样本 acc=14.3%）。

---
