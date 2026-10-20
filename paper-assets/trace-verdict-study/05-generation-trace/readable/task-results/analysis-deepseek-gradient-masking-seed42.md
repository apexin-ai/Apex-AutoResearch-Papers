# analysis deepseek gradient masking seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_gradient_masking_seed42_20260523T094212_result.json`
- **Structured JSON:** [`0beaab7751e1fb590faa.json`](../../sessions/0b/0beaab7751e1fb590faa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## deepseek_gradient_masking_seed42 — **SUCCESS**

| Metric | Value |
|--------|-------|
| Accuracy | **99.33%** (95% CI: [98.8%, 99.7%]) |
| pass P/R/F1 | 1.00 / 0.99 / 1.00 |
| fail P/R/F1 | 0.98 / 1.00 / 0.99 |
| eval_loss | 0.0529 |
| train_loss | 0.9961 |
| 训练时长 | 1h 43min |

**与 baseline 对比：**
- DeepSeek exception_only 3-seed 均值 = 99.39%
- Gradient masking (99.8%) = 99.33%
- **Dilution = 0.06%**，远低于 4% 阈值

**跨架构一致性：** Qwen-7B 3-seed gradient masking 均为 99.33%（dilution ≤0%），DeepSeek-6.7B 同样 99.33%（dilution 0.06%）。两个架构均确认 99.8% gradient masking 不影响分类性能，full_trace 退化由内容质量（而非梯度稀释）解释。

Registry 已更新为 DONE/success，分析报告已注册 (art_20260523_8d4636)。

---
