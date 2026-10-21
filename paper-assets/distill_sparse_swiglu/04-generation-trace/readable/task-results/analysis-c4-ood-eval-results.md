# analysis c4 ood eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4-ood-eval-results_20260516T210158_result.json`
- **Structured JSON:** [`9d53de5a5d2c49d32547.json`](../../sessions/9d/9d53de5a5d2c49d32547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C4 OOD Evaluation 结果

### 结果 (`c4_ood_ppl.json`)

| Condition | C4 PPL | Δ vs Dense |
|-----------|--------|------------|
| Dense (LLaMA-3.1-8B) | **9.2075** | baseline |
| KL Predictor 50% | **18.401** | +99.8% |
| TEAL Vanilla 50% | **38.7503** | +320.9% |

**KL advantage over TEAL: 52.5% lower PPL**

### 评估配置

- **Checkpoint**: `/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- **Sparsity**: 50% (global)
- **Model**: LLaMA-3.1-8B (bf16, flash_attention_2)
- **Eval data**: C4 validation, 200 samples × 2048 tokens
- **Predictor**: dynamic per-token Gumbel mask, `d_b=128`, hard=True
- **TEAL calibration**: 32 samples from C4 itself (fair OOD comparison)
- **Eval mode**: KL=dynamic per-token; TEAL=static global magnitude mask

### 与 WikiText-2 对比

| | WikiText-2 | C4 (OOD) | 差距 |
|---|---|---|---|
| Dense | ~7.97 | 9.21 | +15.5% |
| KL Predictor 50% | 11.79 | 18.40 | +56.1% |
| TEAL 50% | ~23.x | 38.75 | ~+60% |

KL predictor 在 OOD 上降幅更大（PPL 从 11.79 → 18.40），但仍大幅优于 TEAL（18.4 vs 38.8），OOD 泛化优势保持。可用于回应 C3 concern：predictor 不是过拟合训练域，在 C4 上仍保持 2.1x advantage over TEAL。

---
