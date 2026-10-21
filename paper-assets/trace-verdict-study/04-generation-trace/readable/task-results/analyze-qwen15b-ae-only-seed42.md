# analyze qwen15b ae only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_ae_only_seed42_20260520T075010_result.json`
- **Structured JSON:** [`8d6faca17e84240b08d9.json`](../../sessions/8d/8d6faca17e84240b08d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## qwen15b_ae_only_seed42 — ✓ Success

| 指标 | 值 |
|------|-----|
| **Accuracy** | **99.08%** [98.5%, 99.6%] |
| Majority baseline | 71.5% |
| Lift | +27.6pp |
| pass P/R/F1 | 1.00 / 0.99 / 0.99 |
| fail P/R/F1 | 0.97 / 1.00 / 0.98 |
| GPU hours | 0.97h |

### 跨模型 ae_only 对比

| Model | Accuracy |
|-------|----------|
| Qwen-7B | 99.92% |
| CodeLlama-13B | 99.08% |
| **Qwen-1.5B** | **99.08%** |
| DeepSeek-Coder-6.7B | 98.74% |

Qwen-1.5B 以最小参数量（1.5B）达到与 CodeLlama-13B（13B）完全相同的 99.08% accuracy，远超 ≥95% 的 hypothesis 阈值。ae_only 条件在 1.5B scale 依然高度有效，Tier 1 的结论跨模型 scale 稳健。

cuda:0 无残留进程，GPU 已空闲可用。Registry 已更新为 DONE/success。

---
