# eval calibration codellama deepseek

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_calibration_codellama_deepseek_20260519T015419_result.json`
- **Structured JSON:** [`fb3138aabd21f9e4f52b.json`](../../sessions/fb/fb3138aabd21f9e4f52b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Calibration 结果已存在（2026-05-18 跑完），无需重跑。

## Exception_only Calibration 汇总

| Model | Accuracy | ECE | Brier | MCE |
|---|---|---|---|---|
| **CodeLlama-13B** | 99.83% | 0.0020 | 0.0013 | 0.0411 |
| **DeepSeek-6.7B** | 99.33% | 0.0064 | 0.0061 | 0.7756 |
| **Qwen-7B** (参考) | 99.83% | 0.0027 | 0.0013 | 0.8355 |

**要点：**
- CodeLlama-13B calibration 最好：ECE 最低 (0.0020)，MCE 也远低于其他两个模型 (0.041 vs 0.78+)，说明它的高置信预测几乎全正确，没有严重的过度自信 bin
- DeepSeek ECE 和 Brier 均最高，主要问题在 0.9-0.95 confidence bin：7 个样本中只有 1 个正确（accuracy=14.3%），造成 MCE=0.776
- Qwen-7B 和 CodeLlama-13B accuracy 相同 (99.83%)，但 Qwen 的 MCE 高很多，说明它在少数低置信样本上同样存在 miscalibration
- 三个模型的 Brier score 都很低 (<0.007)，因为绝大多数样本 (>98%) 落在 0.95-1.0 bin 且预测正确

---
