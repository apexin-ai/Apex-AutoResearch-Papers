# exp c1 ablation 30pct s456

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_c1-ablation-30pct-s456_20260519T020814_result.json`
- **Structured JSON:** [`8c7a9151770cc4c6261c.json`](../../sessions/8c/8c7a9151770cc4c6261c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。完整汇报：

## C1 Causal Ablation — 30% s456

**训练 (1000 steps)**
- Agreement: **97.8%**
- BCE loss: **0.0551**
- Sparsity: 0.304

**Eval metrics (TEAL global 30%, uniform allocation)**

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | **8.8421** |
| ARC-Challenge (acc_norm) | **44.28%** |
| WinoGrande (acc) | **69.38%** |
| MMLU (acc) | **36.70%** |
| GSM8K (exact_match) | **7.28%** |

**KL checkpoint 路径**
`/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s456/predictor_kl_normalized.pt`

---
