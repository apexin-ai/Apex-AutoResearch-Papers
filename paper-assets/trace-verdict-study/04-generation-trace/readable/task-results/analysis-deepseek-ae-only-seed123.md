# analysis deepseek ae only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_ae_only_seed123_20260520T151900_result.json`
- **Structured JSON:** [`0231426e7a3368072339.json`](../../sessions/02/0231426e7a3368072339.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**deepseek_ae_only_seed123 — SUCCESS**

| 指标 | 值 |
|------|-----|
| Accuracy | **98.32%** [97.56%, 98.99%] |
| Fail F1 | 0.970 |
| Fail Precision | 0.982 |
| Fail Recall | 0.959 |
| Pass F1 | 0.988 |
| Eval loss | 0.1907 |
| Train loss | 0.0702 |

**跨 seed 对比**：seed42=98.74% vs seed123=98.32%，差 -0.42pp，CI 重叠，方差低（std ~0.3%）。

**跨模型 ae_only 排序**：Qwen-7B 99.64% > Qwen-1.5B 99.08% = CodeLlama-13B 99.08% > DeepSeek-6.7B 98.53%。DeepSeek 虽最低但仍稳过 98% 阈值，ae_only 在全部四个模型 scale 均为 Tier 1。

已完成：analysis.md 已注册为 artifact，registry 已更新为 DONE/success。

---
