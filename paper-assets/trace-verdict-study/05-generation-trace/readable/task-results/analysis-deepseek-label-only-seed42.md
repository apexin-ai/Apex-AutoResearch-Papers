# analysis deepseek label only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_label_only_seed42_20260519T211557_result.json`
- **Structured JSON:** [`f4fd3b8ea093f5b3d0cf.json`](../../sessions/f4/f4fd3b8ea093f5b3d0cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入并注册。汇总：

| 指标 | 值 |
|---|---|
| accuracy | **28.5%** [26.1%, 30.8%] |
| majority baseline | 71.5% (always "pass") |
| lift | **-43.0pp** |
| pass P/R/F1 | 0.00 / 0.00 / 0.00 |
| fail P/R/F1 | 0.28 / 1.00 / 0.44 |
| train_loss | 1.7839 |
| eval_loss | **nan** |
| vs DeepSeek full_trace (79.16%) | **-50.7pp** |
| vs Qwen-7B label_only (86.22%) | **-57.7pp** |

**诊断**：模型完全崩溃，将所有样本预测为 "fail"。eval_loss=nan 表明训练过程发生数值发散。accuracy 28.5% 恰好等于测试集中 fail 类的比例，确认模型输出退化为单一类别。远低于预期的 82-88% 范围。

---
