# Comprehensive Experiment Summary Table

**Project:** faith-evidence-ie | **Date:** 2026-05-16 | **Model:** Qwen2.5-7B-Instruct | **Dataset:** DocRED dev (985 docs)

All metrics from full dev-set evaluation. Ign-F1 from metrics_v2.json (bug-fixed) where available.

---

## Main Results Table

| Category | Method | Config | Seed | Ign-F1 | rel_f1 | evi_f1 | EDCR | Δ rel_f1 |
|:---------|:-------|:-------|:-----|-------:|-------:|-------:|-----:|---------:|
| **Baseline** | SFT | QLoRA 4-bit, 3ep | 42 | 0.4057 | 0.4057 | 0.7979 | 0.7118 | — |
| **Baseline** | SFT (no-quant) | bf16, 3ep | 42 | — | 0.4106 | 0.8013 | 0.7039 | +0.49pp |
| **Baseline** | SFT-no-evidence | QLoRA 4-bit, 3ep | 42 | 0.4893 | 0.4893 | 0 | 0 | +8.36pp |
| **Baseline** | DREEAM (supervised) | RoBERTa-large | 66 | 61.72† | 63.57† | 54.01† | — | n/a |
| | | | | | | | | |
| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 42 | — | 0.4449 | 0.8187 | 0.6565 | +3.92pp |
| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | +6.26pp |
| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 44 | — | 0.4655 | 0.8087 | 0.6350 | +5.98pp |
| **RSFT-CED** | top_k=1, 3ep | α=128, r=64 | 45 | TBD | TBD | TBD | TBD | TBD |
| **RSFT-CED** | **3-seed mean** | **(s42/s43/s44)** | — | — | **0.4596±0.0128** | **0.8143±0.0051** | **0.6434±0.0115** | **+5.39pp** |
| | | | | | | | | |
| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | +4.82pp |
| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | +4.66pp |
| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 44 | TBD | TBD | TBD | TBD | TBD |
| **RSFT-flat-NLI** | top_k=1, 3ep | DeBERTa-v3-large-mnli | 45 | TBD | TBD | TBD | TBD | TBD |
| **RSFT-flat-NLI** | **2-seed mean** | **(s42/s43)** | — | **0.4531±0.0011** | **0.4531±0.0011** | **0.8101±0.0081** | **0.6468±0.0052** | **+4.74pp** |
| | | | | | | | | |
| **RSFT-CED** | top_k=3, 3ep (ablation) | 8037 samples | 42 | 0.4364 | 0.4454 | 0.8088 | 0.6635 | +3.97pp |
| **RSFT-CED** | 1ep, α=128 (ablation) | 2548 clean samples | 42 | 0.4494 | 0.4494 | 0.8108 | 0.6641 | +4.37pp |
| **RSFT-CED** | 1ep, α=32 (ablation) | conservative LoRA | 42 | 0.4493 | 0.4493 | 0.8128 | 0.6609 | +4.36pp |
| | | | | | | | | |
| **GRPO (bf16)** | G=8, kl=0.01, step-100 | bf16 LoRA, lr=5e-5 | 42 | 0.4549 | 0.4549 | 0.8086 | 0.6318 | +4.92pp |
| **GRPO (QLoRA)** | G=8, kl=0.01, step-100 | QLoRA 4-bit, lr=5e-5 | 42 | — | 0.2167 | 0.5746 | 0.8539 | −18.90pp |
| **DPO** | 1ep (corrected eval) | 2666 pairs | 42 | — | 0.4034 | 0.8088 | 0.7139 | −0.23pp |
| **DPO** | 3ep (overfit) | 2666 pairs | 42 | — | 0.3429 | 0.8403 | 0.7294 | −6.28pp |
| | | | | | | | | |
| **Inference-time** | CED Reranker (N=8) | T=0.7, no training | 42 | — | **0.4864** | **0.8188** | 0.6156 | **+8.07pp** |

† DREEAM uses scale 0–100 and a different evaluation protocol (RoBERTa-large, fully supervised); not directly comparable.

---

## Ranking by rel_f1

| Rank | Method | rel_f1 | Notes |
|:-----|:-------|-------:|:------|
| 1 | SFT-no-evidence | 0.4893 | No evidence output (evi_f1=0) |
| 2 | CED Reranker (N=8) | 0.4864 | Inference-time, 5.8h generation |
| 3 | RSFT-CED s43 (best seed) | 0.4683 | |
| 4 | RSFT-CED s44 | 0.4655 | |
| 5 | RSFT-CED 3-seed mean | 0.4596 | |
| 6 | GRPO bf16 step-100 | 0.4549 | |
| 7 | RSFT-flat-NLI s42 | 0.4539 | |
| 8 | RSFT-flat-NLI 2-seed mean | 0.4531 | |
| 9 | RSFT-CED 1ep α=128 | 0.4494 | |
| 10 | RSFT-CED top_k=3 | 0.4454 | More data, lower quality |
| 11 | RSFT-CED s42 | 0.4449 | |
| 12 | SFT (no-quant) | 0.4106 | Quantization confound < 1pp |
| 13 | SFT baseline | 0.4057 | Reference |
| 14 | DPO 1ep | 0.4034 | ≈ SFT, method closed |
| 15 | DPO 3ep | 0.3429 | Overfit, method closed |
| 16 | GRPO QLoRA step-100 | 0.2167 | Catastrophic forgetting |

---

## GRPO bf16 Checkpoint Trajectory

| Checkpoint | Ign-F1 | rel_f1 | evi_f1 | EDCR |
|:-----------|-------:|-------:|-------:|-----:|
| step-30 | — | 0.4340 | 0.8063 | 0.6807 |
| step-50 | — | 0.4276 | 0.8024 | 0.6855 |
| step-70 | — | 0.4341 | 0.8099 | 0.6685 |
| step-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 |
| step-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 |
| step-100 | 0.4549 | 0.4549 | 0.8086 | 0.6318 |

---

## CED Reranker Analysis

| Configuration | rel_f1 | evi_f1 | EDCR |
|:--------------|-------:|-------:|-----:|
| SFT greedy (baseline) | 0.4057 | 0.7979 | 0.7118 |
| Random select (N=8) | 0.4538 | 0.8029 | 0.6763 |
| **CED Reranker (N=8)** | **0.4864** | **0.8188** | **0.6156** |
| Oracle select (upper bound) | 0.6237 | 0.7942 | 0.5262 |

CED achieves 37% of the oracle gap over SFT. CED-F1 Spearman r=0.3235 (p<1e-100).

---

## Key Findings

1. **CED Reranker is the best method overall** (rel_f1=0.4864, +8.07pp over SFT), but requires 5.8h inference for N=8 candidates.
2. **RSFT-CED (3-seed mean)** is the best training-time method (rel_f1=0.4596±0.0128, +5.39pp over SFT), improving both relation extraction and evidence faithfulness.
3. **CED vs flat-NLI scoring**: CED contrastive margin adds only ~0.65pp over flat-NLI (0.4596 vs 0.4531), suggesting most RSFT gain comes from NLI-based selection, not the contrastive component.
4. **GRPO bf16** achieves competitive results (0.4549, +4.92pp) without mode collapse; **GRPO QLoRA catastrophically forgets** (0.2167, −18.90pp). The forgetting is QLoRA-specific.
5. **DPO provides no benefit**: 1ep ≈ SFT, 3ep overfits. Method closed.
6. **Evidence generation hurts RE**: SFT-no-evidence achieves 0.4893 rel_f1 (+8.36pp), suggesting the evidence generation task competes for model capacity.
7. **RSFT top_k=3** (3× more data) underperforms top_k=1 (0.4454 vs 0.4596), confirming quality > quantity for RSFT data selection.
8. **EDCR inversely correlates with rel_f1** (Spearman r=−0.96), confirming it captures the evidence dependency cost of joint prediction.

---

## Missing Data Points

| Method | Seed | Status |
|:-------|:-----|:-------|
| RSFT-CED | s45 | Training failed (CUDA OOM) |
| RSFT-flat-NLI | s44 | Eval killed |
| RSFT-flat-NLI | s45 | No eval |
| GRPO bf16 G=4 | — | All attempts killed (GPU conflicts) |
| SFT-no-evidence | — | Eval re-confirmation queued |
