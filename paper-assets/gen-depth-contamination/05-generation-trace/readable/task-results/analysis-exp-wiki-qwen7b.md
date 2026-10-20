# analysis exp wiki qwen7b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_qwen7b_20260517T222327_result.json`
- **Structured JSON:** [`e7a21b0e416e1f91dbb9.json`](../../sessions/e7/e7a21b0e416e1f91dbb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结果：K\* = 2 (success)**

- depth 0→1: AUC=0.967 (极强判别)
- depth 1→2: AUC=0.611 (刚过 0.60 阈值，仍可判别)
- depth 2→3: AUC=0.556 (落入 chance level)

Qwen2.5-7B 在 Wikipedia 上 K\*=2，与 Qwen2.5-1.5B 完全一致。假设验证成功：Qwen 家族的 K\*=2 pattern 在 Wikipedia 上跨规模 (1.5B→7B) 稳定，而同规模的 LLaMA-8B 和 Mistral-7B 均为 K\*=1。这是模型家族/预训练策略的特征，不是规模效应。

Registry 已更新为 DONE(success)，分析报告已注册。

---
