# Paper Main Tables Draft — FREIGE (EMNLP 2026)

> **Compiled**: 2026-05-16
> **Source**: experiment registry (all metrics verified against registry entries)
> **Convention**: Ign-F1/F1/Evi-F1 as percentage; EDCR as decimal [0,1]. Ign-F1 uses corrected values from paper_framing.md where available; registry ign_f1 has known bug (= rel_f1) per D069.

---

## Table 1: Main Results on DocRED Dev Set

**Claim 1 support**: Evidence-grounded DocRE is viable. Evidence generation costs ~7pp Ign-F1; RSFT recovers most; CED reranker recovers 97%.

| Method | Ign-F1 | F1 | Evi-F1 | Evi-F1 (joint) | EDCR | exp_id |
|--------|--------|------|--------|----------------|------|--------|
| **SFT (no evidence)** | **47.36** | **48.93** | — | — | — | `eval_plan_014_sft_no_evidence` |
| SFT baseline (with evidence) | 40.36 | 41.06 | 80.13 | 32.16 | 0.7039 | `eval_sft_baseline_noquant` |
| RSFT flat-NLI (best: s44) | 46.15† | 46.15 | 81.31 | 35.97 | 0.6458 | `eval_flat_nli_s44` |
| RSFT flat-NLI (4-seed mean) | TBD | 45.57±0.39 | 81.22±0.49 | — | 0.6479±0.004 | `s42/s43/s44/s45` |
| RSFT CED (best: s43) | 45.85 | 46.83 | 81.56 | 37.11 | 0.6388 | `mvp2_eval_rsft_s43_r2` |
| RSFT CED (3-seed mean) | 45.00±1.19 | 45.96±1.27 | 81.43±0.51 | — | 0.6434±0.011 | `s42/s43/s44` |
| **CED reranker (N=8)** | **TBD** | **48.64** | **81.88** | — | **0.6156** | `mvp2_ced_reranker_poc` |
| DREEAM‡ (RoBERTa-large) | 61.72 | 63.57 | 54.01 | — | — | `plan_004_dreeam_baseline` |

**Notes**:
- † = Ign-F1 uncorrected (registry ign_f1 = rel_f1, suspected bug per D069). Corrected Ign-F1 expected ~1pp below F1.
- ‡ = Encoder model (RoBERTa-large), different paradigm — not directly comparable for RE, included for evidence baseline context.
- CED reranker = inference-time reranking of N=8 SFT samples using CED scoring, no additional training.
- SFT baseline uses noquant (no quantization) variant; quantized SFT (rel_f1=40.57) available as `mvp2_eval_sft_baseline` if needed.
- RSFT CED 3-seed mean computed from s42 (3ep, mvp2_eval_rsft_r1), s43 (mvp2_eval_rsft_s43_r2), s44 (mvp2_rsft_train_r1_s44). All original protocol.
- RSFT flat-NLI 4-seed mean from s42 (eval_plan_001_flat_nli), s43 (reeval_flat_nli_s43), s44 (eval_flat_nli_s44), s45 (eval_flat_nli_seed45). Mixed protocol (s43 partial unified, rest original).
- Joint Evi-F1 = unconditional (denominator = all gold triples, not just correctly predicted ones).

**Key numbers**:
- Evidence tax: 47.36 → 40.36 = **−7.00pp** Ign-F1
- RSFT CED recovery: 45.85 − 40.36 = **+5.49pp** (78.4% of gap)
- CED reranker: F1=48.64 vs no-evidence F1=48.93 = **−0.29pp** (97% recovery), with evi_f1=81.88

**PENDING data**:
- `PENDING: mvp2_ced_reranker_poc` — CED reranker Ign-F1 (only F1 available)
- `PENDING: reeval_ced_s42, reeval_ced_s44` — D076 unified protocol CED reevals
- `PENDING: eval_rsft_ced_s45` — CED s45 for 4-seed statistics

---

## Table 2: Evidence-Extraction Decoupling Spectrum

**Claim 2 support**: RL optimization pressure correlates with decoupling severity. QLoRA is a catastrophic amplifier. Decoupling is intra-task multi-objective trade-off, not inter-task forgetting.

| Method | Quant | F1 | Δ F1 vs SFT | Evi-F1 | EDCR | Severity | exp_id |
|--------|-------|------|-------------|--------|------|----------|--------|
| GRPO (lr=5e-6, ckpt100) | QLoRA 4-bit | 1.38 | −39.68 | 85.04 | 0.9876 | **Catastrophic** | `mvp2_eval_lr5e6_r1_ckpt100` |
| GRPO (lr=5e-5, ckpt100) | QLoRA 4-bit | 21.67 | −19.39 | 57.46 | 0.8539 | Severe | `mvp2_eval_ced_kl001_r4_step100` |
| DPO bf16 (3ep) | bf16 | 34.29 | −6.77 | 84.03 | 0.7294 | **Gradual** | `plan_012_dpo_ced` |
| SFT baseline | noquant | 41.06 | — | 80.13 | 0.7039 | Reference | `eval_sft_baseline_noquant` |
| DPO bf16 (1ep) | bf16 | 40.34 | −0.72 | 80.88 | 0.7139 | Neutral | `eval_plan_012_dpo_1ep_fixed_r2` |
| GRPO bf16 G=8 (step30) | bf16 | 43.40 | +2.34 | 80.63 | 0.6807 | **Mild** (transient) | `plan_011_bf16_g8_step_eval` |
| GRPO bf16 G=8 (step70) | bf16 | 43.41 | +2.35 | 80.99 | 0.6685 | Mild (transient) | `plan_011_bf16_g8_step_eval` |
| GRPO bf16 G=8 (ckpt100) | bf16 | 45.49 | +4.43 | 80.86 | 0.6318 | **None** (converged) | `plan_011_grpo_g8_bf16_eval` |
| RSFT CED (best: s43) | — | 46.83 | +5.77 | 81.56 | 0.6388 | **None** | `mvp2_eval_rsft_s43_r2` |

**Notes**:
- Δ F1 computed vs SFT baseline noquant (F1=41.06, `eval_sft_baseline_noquant`).
- GRPO QLoRA (lr=5e-6): 100 steps, G=8 groups, QLoRA 4-bit quantization. Catastrophic: rel_f1 drops to near-zero while evi_f1 rises to 85%.
- GRPO QLoRA (lr=5e-5): Same config as above but higher learning rate. Less catastrophic but still severe.
- GRPO bf16 trajectory: step30→50→70 show mild transient decline (all F1 < ckpt100), recovers by convergence. ckpt80→90→100: 44.56→45.23→45.49 (monotonically improving).
- DPO 1ep→3ep: gradual decoupling — rel_f1 declines from 40.34 to 34.29 while evi_f1 rises from 80.88 to 84.03.
- QLoRA amplification: bf16 GRPO F1=45.49 vs QLoRA GRPO F1=1.38. Same algorithm, quantization turns mild into catastrophic.
- Ign-F1 column omitted from this table — most entries have bugged Ign-F1. Corrected values: GRPO bf16 ckpt100 Ign-F1=45.59 (paper_framing); DPO 1ep Ign-F1=38.88 (paper_framing). Others TBD.

**GRPO bf16 extended trajectory** (supplementary):

| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |
|------------|------|--------|------|--------|
| step30 | 43.40 | 80.63 | 0.6807 | `plan_011_bf16_g8_step_eval` |
| step50 | 42.76 | 80.24 | 0.6855 | `plan_011_bf16_g8_step_eval` |
| step70 | 43.41 | 80.99 | 0.6685 | `plan_011_bf16_g8_step_eval` |
| ckpt80 | 44.56 | 80.34 | 0.6409 | `eval_grpo_g8_bf16` |
| ckpt90 | 45.23 | 80.52 | 0.6414 | `eval_grpo_g8_bf16` |
| ckpt100 | 45.49 | 80.86 | 0.6318 | `eval_grpo_g8_bf16` / `plan_011_grpo_g8_bf16_eval` |

**QLoRA GRPO (lr=5e-6) trajectory** (supplementary):

| Checkpoint | F1 | Evi-F1 | EDCR | exp_id |
|------------|------|--------|------|--------|
| ckpt20 | 0.77 | 62.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt20` |
| ckpt40 | 0.71 | 75.84 | 0.9942 | `mvp2_eval_lr5e6_r1_ckpt40_r2` |
| ckpt60 | 0.93 | 81.00 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt60_r2` |
| ckpt80 | 1.16 | 82.80 | 0.9930 | `mvp2_eval_lr5e6_r1_ckpt80` |
| ckpt100 | 1.38 | 85.04 | 0.9876 | `mvp2_eval_lr5e6_r1_ckpt100` |

**PENDING data**:
- `PENDING` — Ign-F1 for most entries (need metrics_v2 re-computation)
- `PENDING` — DPO 3ep Ign-F1

---

## Table 3: CED vs flat-NLI Seed Comparison (Claim 3)

**Claim 3 support**: Both CED and flat-NLI improve over SFT baseline. CED vs flat-NLI difference statistically uncertain (p>0.05). CED may be "one possible scoring function" rather than strictly superior.

### CED RSFT (top_k=1, 3 epochs)

| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |
|------|------|--------|--------|------|----------|--------|
| 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | original | `mvp2_eval_rsft_r1` |
| 43 | 46.83 | 45.85 | 81.56 | 0.6388 | original | `mvp2_eval_rsft_s43_r2` |
| 44 | 46.55 | 45.51 | 80.87 | 0.6350 | original | `mvp2_rsft_train_r1_s44` |
| 45 | PENDING | PENDING | PENDING | PENDING | — | `PENDING: eval_rsft_ced_s45` |
| **Mean (3-seed)** | **45.96±1.27** | **45.00±1.19** | **81.43±0.51** | **0.6434±0.011** | | |

### flat-NLI RSFT (top_k=1, 3 epochs)

| Seed | F1 | Ign-F1 | Evi-F1 | EDCR | Protocol | exp_id |
|------|------|--------|--------|------|----------|--------|
| 42 | 45.39 | 44.49 | 80.43 | 0.6431 | original (batch=16) | `eval_plan_001_flat_nli` |
| 43 | 45.23 | TBD† | 81.58 | 0.6505 | partial unified (fixed adapter, batch=16) | `reeval_flat_nli_s43` |
| 44 | 46.15 | 46.15† | 81.31 | 0.6458 | original | `eval_flat_nli_s44` |
| 45 | 45.51 | 45.51† | 81.54 | 0.6521 | original | `eval_flat_nli_seed45` |
| **Mean (4-seed)** | **45.57±0.39** | **TBD** | **81.22±0.49** | **0.6479±0.004** | | |

### Head-to-Head (current data, NOT D076-unified)

| Metric | CED (3-seed) | flat-NLI (4-seed) | Δ (CED − flat-NLI) |
|--------|-------------|-------------------|---------------------|
| F1 | 45.96 ± 1.27 | 45.57 ± 0.39 | +0.39pp |
| Evi-F1 | 81.43 ± 0.51 | 81.22 ± 0.49 | +0.21pp |
| EDCR | 0.6434 ± 0.011 | 0.6479 ± 0.004 | −0.0045 |

**Dream v1 p-values**: 0.08 / 0.38 / 0.12 — **not statistically significant** at α=0.05.

### top_k Ablation (CED only)

| Config | F1 | Ign-F1 | Evi-F1 | EDCR | Training samples | exp_id |
|--------|------|--------|--------|------|-----------------|--------|
| k=1 (3-seed mean) | 45.96 | 45.00 | 81.43 | 0.6434 | 2,718 (12.4%) | `s42/s43/s44` |
| k=3 (1 seed, s42) | 44.54 | 43.64 | 80.88 | 0.6635 | 8,037 (37%) | `reeval_rsft_topk3` |
| **Δ (k=3 − k=1)** | **−1.42** | **−1.36** | **−0.55** | **+0.02** | **+5,319** | |

**Notes**:
- k=3 uses 2.96× more training data but lower quality: mean_f1=0.5761 vs k=1 mean_f1=0.6157; mean_ced=0.6205 vs k=1 mean_ced=0.6683 (`mvp2_rsft_ced_scoring` vs `mvp2_rsft_ced_scoring_topk3_r2`).
- k=3 has only 1 seed — direction consistent but no significance test possible. Present as supplementary ablation.

### D076 Unified Protocol Reeval Status

Valid paired t-test requires all seeds evaluated under identical protocol (batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024).

| Target | Issue | Unified Reeval | Status |
|--------|-------|---------------|--------|
| CED s42 | Wrong checkpoint (r2b α=32) | `reeval_ced_s42` | PREPARING |
| CED s44 | Wrong seed in eval (used s42) | `reeval_ced_s44` | PREPARING |
| flat-NLI s42 | batch_size=16 | `reeval_flat_nli_s42` | PREPARING |
| flat-NLI s43 | batch_size=16 | `reeval_flat_nli_s43_r2` | RUNNING |

**Impact**: Current numbers are directional only. Paired t-test blocked until all 8 evals (4 CED + 4 flat-NLI) use unified protocol.

---

## Cross-Table: EDCR Method-Level Summary (Claim 4 support)

| Method | EDCR | F1 | Evi-F1 | exp_id |
|--------|------|------|--------|--------|
| GRPO QLoRA (lr=5e-6) | 0.9876 | 1.38 | 85.04 | `mvp2_eval_lr5e6_r1_ckpt100` |
| GRPO QLoRA (lr=5e-5) | 0.8539 | 21.67 | 57.46 | `mvp2_eval_ced_kl001_r4_step100` |
| DPO 3ep | 0.7294 | 34.29 | 84.03 | `plan_012_dpo_ced` |
| SFT baseline (quantized) | 0.7118 | 40.57 | 79.79 | `mvp2_eval_sft_baseline` |
| DPO 1ep | 0.7139 | 40.34 | 80.88 | `eval_plan_012_dpo_1ep_fixed_r2` |
| SFT baseline (noquant) | 0.7039 | 41.06 | 80.13 | `eval_sft_baseline_noquant` |
| RSFT CED k=3 | 0.6635 | 44.54 | 80.88 | `reeval_rsft_topk3` |
| RSFT r2a (1ep, α=128) | 0.6641 | 44.94 | 81.08 | `mvp2_eval_rsft_r2a` |
| RSFT r2b (1ep, α=32) | 0.6609 | 44.93 | 81.28 | `mvp2_eval_rsft_r2b` |
| RSFT CED s42 (3ep) | 0.6565 | 44.49 | 81.87 | `mvp2_eval_rsft_r1` |
| flat-NLI s43 | 0.6505 | 45.23 | 81.58 | `reeval_flat_nli_s43` |
| flat-NLI s45 | 0.6521 | 45.51 | 81.54 | `eval_flat_nli_seed45` |
| flat-NLI s44 | 0.6458 | 46.15 | 81.31 | `eval_flat_nli_s44` |
| flat-NLI s42 | 0.6431 | 45.39 | 80.43 | `eval_plan_001_flat_nli` |
| RSFT CED s43 | 0.6388 | 46.83 | 81.56 | `mvp2_eval_rsft_s43_r2` |
| RSFT CED s44 | 0.6350 | 46.55 | 80.87 | `mvp2_rsft_train_r1_s44` |
| GRPO bf16 G=8 (ckpt100) | 0.6318 | 45.49 | 80.86 | `plan_011_grpo_g8_bf16_eval` |
| **CED reranker** | **0.6156** | **48.64** | **81.88** | `mvp2_ced_reranker_poc` |

**Correlations** (`plan_003_edcr_diagnostic`):
- Method-level: EDCR vs rel_f1 Spearman ρ = −0.9648 (p=0.0001); EDCR vs evi_f1 ρ = 0.0022 (p=0.9941)
- Per-relation (D070, 93 types ≥5 samples): EDCR vs evi_f1 ρ = −0.064 (p=0.58) — **completely independent**; EDCR vs rel_f1 ρ = −0.793 (p<0.001)

---

## Summary: Data Completeness

### Paper-ready numbers
1. Evidence tax: 47.36 → 40.36 = −7.00pp Ign-F1 ✓
2. CED reranker: F1=48.64, −0.29pp below no-evidence ✓
3. RSFT CED best: Ign-F1=45.85, +5.49pp over SFT ✓
4. Decoupling spectrum: GRPO QLoRA / GRPO bf16 / DPO / RSFT — all data points present ✓
5. QLoRA amplification: bf16 45.49 vs QLoRA 1.38 ✓
6. EDCR per-relation independence: ρ=−0.064 ✓
7. top_k ablation: k=1 > k=3 ✓
8. DREEAM baseline: F1=63.57, Evi-F1=54.01 ✓

### Critical PENDING (blocking paper)
1. **CED reranker Ign-F1** — needed for Table 1 main column
2. **D076 unified protocol reevals** (4 experiments) — blocking Claim 3 paired t-test
3. **CED s45 eval** — blocking 4-seed CED statistics
4. **Corrected Ign-F1** for flat-NLI s43/s44/s45, DPO 3ep, GRPO QLoRA — need metrics_v2 re-computation
5. **Test set evaluation** (plan_002) — no official numbers yet

### Nice-to-have
1. EDCR human validation (plan_013) — RC6
2. Post-hoc retrieval baseline (SFT + BM25) — RC10
3. TP-only EDCR (D071) — method-level confound resolution
