# analysis d030 kl30 uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d030_kl30_uniform_20260516T042810_result.json`
- **Structured JSON:** [`edab37b0a2fc86de8d2f.json`](../../sessions/ed/edab37b0a2fc86de8d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== METRICS ===
wikitext2_ppl: 8.8157
arc_challenge_acc_norm: 0.4078
winogrande_acc: 0.6859
mmlu_acc: 0.4061
gsm8k_exact_match: 0.0735
actual_sparsity: 0.300

Per-layer sparsity: uniform 0.301 across all 32 layers

=== CONCLUSION ===
negative (partial)

=== ANALYSIS ===
MMLU 从 global top-k 的 28.74%（近随机）恢复到 40.61%，有明显改善但仍远低于 dense baseline ~63%，说明 per-layer 不均匀是 MMLU 崩溃的一个因素但非唯一因素。GSM8K 完全没有恢复——7.35% vs global top-k 的 7.43%，差异在噪声范围内，仍处于随机水平（dense ~50%），表明 reasoning 能力的崩溃与 per-layer 分配策略无关，30% sparsity 本身对 reasoning pathway 的破坏是根本原因。WinoGrande 68.59% 和 ARC-Challenge 40.78% 相对合理但也有明显退化。结论：uniform allocation 对知识类任务（MMLU）有部分修复作用，但对推理类任务（GSM8K）无效——per-layer 不均匀不是 downstream 崩溃的唯一根因。
```

---
