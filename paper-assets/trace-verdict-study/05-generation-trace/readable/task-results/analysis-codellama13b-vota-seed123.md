# analysis codellama13b vota seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_vota_seed123_20260520T113338_result.json`
- **Structured JSON:** [`0a9bf90f3e2802dacb90.json`](../../sessions/0a/0a9bf90f3e2802dacb90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇总

**codellama13b_vota_seed123: Accuracy 98.91% (CI: [98.32%, 99.41%])**

| | seed42 | seed123 | Mean±Std |
|--|--------|---------|----------|
| Accuracy | 98.57% | 98.91% | **98.74±0.24%** |
| Pass F1 | 0.990 | 0.992 | 0.991 |
| Fail F1 | 0.975 | 0.981 | 0.978 |

Hypothesis confirmed — seed123 在预测的 97-100% 范围内，与 seed42 差 0.34pp，CI 大幅重叠，CodeLlama-13B 在 VOTA 上 seed-robust。

三个模型家族 VOTA 均值：DeepSeek 99.25% > Qwen 99.05% > CodeLlama 98.74%，差距 <0.6pp，支撑 VOTA universality claim。

Registry 已更新（DONE/success），报告已注册（`art_20260520_5e9c0d`）。

---
