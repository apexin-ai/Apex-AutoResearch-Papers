# analysis qwen15b loop only seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_loop_only_seed42_20260520T084220_result.json`
- **Structured JSON:** [`91af1e44b6ae30c5d653.json`](../../sessions/91/91af1e44b6ae30c5d653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**qwen15b_loop_only_seed42 — Accuracy 78.32%，Hypothesis confirmed (success)**

| 指标 | 值 |
|------|-----|
| Accuracy | 78.32% (CI: 76.1–80.7%) |
| Pass F1 | 0.853 |
| Fail F1 | 0.590 |
| Lift over majority | +6.8pp |
| Train loss | 0.085 |
| Runtime | ~45 min |

**跨模型 loop_only 排序**：Qwen-7B (86.05%) > DeepSeek-6.7B (81.26%) > **Qwen-1.5B (78.32%)** > CodeLlama-13B (76.56%)

关键发现：
- Qwen-1.5B 以 1.5B 参数超过 CodeLlama-13B (13B 参数)，说明 loop trace 理解能力取决于架构/预训练数据而非参数量
- Qwen 家族内部 7B→1.5B 降 7.7pp，scale effect 显著但信号仍远高于 majority baseline
- Tier 2 四模型范围 76.6–86.1%，确认 "model-dependent" 定性

Registry 已更新为 DONE/success，分析报告已注册 (art_20260520_b59347)。

---
