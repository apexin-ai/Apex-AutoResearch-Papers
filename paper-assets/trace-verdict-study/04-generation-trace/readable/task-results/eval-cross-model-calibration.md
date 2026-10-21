# eval cross model calibration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross_model_calibration_20260519T213823_result.json`
- **Structured JSON:** [`8d1d007743cef009947c.json`](../../sessions/8d/8d1d007743cef009947c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Cross-Model Calibration Results (exception_only)

| Model | ECE | MCE | Brier | Accuracy |
|-------|-----|-----|-------|----------|
| **Qwen-7B** | 0.0027 | 0.8355 | 0.0013 | 99.83% |
| **Qwen-1.5B** | 0.0020 | 0.7549 | 0.0013 | 99.83% |
| **CodeLlama-13B** | 0.0020 | 0.0411 | 0.0013 | 99.83% |
| **DeepSeek-6.7B** | 0.0064 | 0.7756 | 0.0061 | 99.33% |

**结论**：

- **ECE 跨模型一致性强**：所有 4 模型 ECE 均 < 0.007，3/4 模型 < 0.003，calibration quality 跨模型 universal。
- **Brier Score** 同样一致：3 个模型 ≈ 0.0013，DeepSeek 稍高（0.0061）但仍很低。
- **MCE 异常值**：Qwen-7B/1.5B/DeepSeek 的 MCE 较高（0.75-0.84），但这是因为极少量低置信度样本（1-2 个落在 [0.75, 0.85) bin 中且预测错误）。CodeLlama-13B 的 MCE 最低（0.041），因为其少量不确定样本集中在 [0.70, 0.75) bin 且仍有 75% 准确率。
- **DeepSeek** 略弱于其余 3 个模型（acc 99.33% vs 99.83%），但 calibration 仍然良好。

结果已保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/cross_model_calibration_results.json`。

---
