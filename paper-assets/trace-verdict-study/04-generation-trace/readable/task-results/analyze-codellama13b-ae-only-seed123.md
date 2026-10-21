# analyze codellama13b ae only seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_codellama13b_ae_only_seed123_20260520T073216_result.json`
- **Structured JSON:** [`2fe553fb4e57b1fa7d2f.json`](../../sessions/2f/2fe553fb4e57b1fa7d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结果**：CodeLlama-13B ae_only seed123 accuracy = **99.08%**，与 seed42 (99.08%) 完全一致，Δ = 0.00pp。

| 操作 | 状态 |
|------|------|
| Registry → DONE/success | ✓ |
| Metrics 写入 | ✓ |
| 分析报告注册 | ✓ (`art_20260520_59d9d7`) |

**结论**：ae_only 在 CodeLlama-13B 上跨 seed 完全稳定。结合 Qwen-7B (99.92%)、DeepSeek-6.7B (98.74%)，Tier 1 ae_only 跨模型×跨 seed 鲁棒性得到充分验证，可直接用于 rebuttal。

---
