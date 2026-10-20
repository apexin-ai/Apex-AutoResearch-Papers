# Paper Evidence Table — FREIGE (EMNLP 2026)

> **Compiled**: 2026-05-16
> **Source**: experiment registry + paper_framing.md + decisions D067-D076
> **Convention**: Ign-F1/F1 as percentage (e.g., 40.36); rel_f1/evi_f1 as decimal (e.g., 0.4036) when directly from registry. Paper reports Ign-F1 in main table, F1 in appendix (D071).

---

## Claim 1: Evidence-grounded DocRE is a viable new capability

**Statement**: FREIGE is the first LLM method to simultaneously output (head, relation, tail, [evidence]) on DocRED. Evidence generation has a ~7pp Ign-F1 cost; RSFT recovers most of it; CED reranker recovers 97%.

### Supporting Experiments

| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | Evi-F1 (joint) | EDCR | protocol | notes |
|--------|--------|------|-------------|--------|--------|----------------|------|----------|-------|
| eval_plan_014_sft_no_evidence | SFT no-evidence | 42 | 48.93 | 47.36 | — | — | — | standard | Upper bound: no evidence burden |
| eval_sft_baseline_noquant | SFT baseline (noquant) | 42 | 41.06 | 40.36 | 80.13 | 32.16 | 0.7039 | standard | Primary SFT baseline for paper |
| mvp2_eval_sft_baseline | SFT baseline (quantized) | 42 | 40.57 | 40.57 | 79.79 | 31.17 | 0.7118 | unified (r3) | Quantized; -0.49pp vs noquant |
| mvp2_eval_rsft_s43_r2 | RSFT CED k=1 | 43 | 46.83 | 45.85 | 81.56 | 37.11 | 0.6388 | original | **Best RSFT seed** |
| mvp2_rsft_train_r1_s44 | RSFT CED k=1 | 44 | 46.55 | 45.51 | 80.87 | 37.13 | 0.6350 | original | |
| mvp2_eval_rsft_r1 | RSFT CED k=1 (3ep) | 42 | 44.49 | 43.63 | 81.87 | 34.68 | 0.6565 | original | 3-epoch; s42 |
| mvp2_eval_rsft_r2a | RSFT CED k=1 (1ep) | 42 | 44.94 | 44.01 | 81.08 | 35.09 | 0.6641 | original | 1-epoch ablation α=128 |
| mvp2_eval_rsft_r2b | RSFT CED k=1 (1ep) | 42 | 44.93 | 44.10 | 81.28 | 34.90 | 0.6609 | original | 1-epoch ablation α=32 |
| mvp2_ced_reranker_poc | CED reranker (N=8) | 42 | 48.64 | TBD | 81.88 | — | 0.6156 | standard | **Best practical: 97% recovery** |
| plan_004_dreeam_baseline | DREEAM (RoBERTa-large) | 66 | 63.57† | 61.72† | 54.01† | — | — | encoder | †Encoder model, different paradigm |

### Key Numbers for Paper

- **Evidence generation tax**: Ign-F1 47.36 (no-evidence) → 40.36 (with evidence) = **-7.00pp** cost of faithfulness
- **RSFT recovery**: Best RSFT CED (s43) Ign-F1 = 45.85, recovering **5.49pp** of the 7.00pp gap (78.4% recovery)
- **CED reranker**: F1=48.64 (only -0.29pp below no-evidence F1=48.93), evi_f1=0.8188 → **recovers 97% of evidence cost with no training**
- **RSFT CED 3-seed mean** (s42/s43/s44, original protocol): rel_f1=0.4596±0.0127, evi_f1=0.8143±0.0051
- **All 4 RSFT CED configs > SFT baseline**: Δ Ign-F1 = +3.27 to +5.49pp
- **DREEAM comparison**: Encoder model gets F1=63.57 / Evi-F1=54.01 — different paradigm (classification vs generation), not directly comparable for RE but sets evidence baseline context
- **Joint Evi-F1** (unconditional): SFT baseline 31.17 → best RSFT 37.13 (+5.96pp)

### Evidence Gaps

- [ ] **CED reranker Ign-F1**: Currently only F1 available (48.64); need Ign-F1 for main table
- [ ] **D076 unified protocol reevals** (reeval_ced_s42, reeval_ced_s44): PREPARING — s42 used wrong checkpoint, s44 used wrong seed
- [ ] **RSFT CED s45**: eval RUNNING — needed for 4+ seed statistics
- [ ] **DREEAM-protocol Evi-F1 alignment** (D041): Not yet done — conditional vs joint Evi-F1 not directly comparable with encoder baselines
- [ ] **Test set evaluation** (plan_002): Not started — requires CodaLab submission
- [ ] **Post-hoc retrieval baseline** (SFT + BM25 evidence): Not started — RC10

---

## Claim 2: RL optimization pressure correlates with evidence-extraction decoupling severity

**Statement**: Decoupling severity forms a continuous spectrum — GRPO QLoRA (catastrophic) > GRPO bf16 (mild) > DPO (gradual) > RSFT (none). QLoRA is a catastrophic amplifier, not the root cause. Decoupling is an intra-task multi-objective trade-off (not inter-task forgetting).

### Supporting Experiments

| exp_id | method | seed | F1 (rel_f1) | Evi-F1 | EDCR | Δ vs SFT (F1) | protocol | notes |
|--------|--------|------|-------------|--------|------|---------------|----------|-------|
| mvp2_eval_sft_baseline | SFT baseline | 42 | 40.57 | 79.79 | 0.7118 | — | unified | Reference point |
| mvp2_eval_lr5e6_r1_ckpt100 | GRPO QLoRA (lr=5e-6) | 42 | **1.38** | **85.04** | **0.9876** | **-39.19pp** | original | Catastrophic decoupling |
| mvp2_eval_ced_kl001_r4_step100 | GRPO QLoRA (lr=5e-5) | 42 | 21.67 | 57.46 | 0.8539 | -18.90pp | original | Less catastrophic but still severe |
| plan_011_bf16_g8_step_eval (step30) | GRPO bf16 G=8 | 42 | 43.40 | 80.63 | 0.6807 | +2.83pp | original | Mild decline from ckpt-100 |
| plan_011_bf16_g8_step_eval (step70) | GRPO bf16 G=8 | 42 | 43.41 | 80.99 | 0.6685 | +2.84pp | original | Non-monotonic |
| plan_011_grpo_g8_bf16_eval (ckpt100) | GRPO bf16 G=8 | 42 | **45.49** | 80.86 | 0.6318 | **+4.92pp** | original | Best GRPO bf16; **no catastrophic forgetting** |
| eval_plan_012_dpo_1ep_fixed_r2 | DPO bf16 1ep | 42 | 40.34 | 80.88 | 0.7139 | -0.23pp | original | Neutral — matches SFT |
| plan_012_dpo_ced | DPO bf16 3ep | 42 | **34.29** | **84.03** | **0.7294** | **-6.28pp** | original | Gradual decoupling (overfit) |
| mvp2_eval_rsft_s43_r2 | RSFT CED | 43 | 46.83 | 81.56 | 0.6388 | +6.26pp | original | **No decoupling** |

### Decoupling Spectrum (for paper figure/table)

| Method | Quantization | Optimization Pressure | rel_f1 | Δ rel_f1 | evi_f1 | EDCR | Severity |
|--------|-------------|----------------------|--------|----------|--------|------|----------|
| GRPO (lr=5e-6) | QLoRA 4-bit | High (100 steps, G=8) | 0.0138 | -0.3919 | 0.8504 | 0.9876 | **Catastrophic** |
| GRPO (lr=5e-5) | QLoRA 4-bit | Moderate (100 steps, G=8) | 0.2167 | -0.1890 | 0.5746 | 0.8539 | Severe |
| DPO 3ep | bf16 | Moderate (3 epochs) | 0.3429 | -0.0628 | 0.8403 | 0.7294 | **Gradual** |
| GRPO G=8 (ckpt30-70) | bf16 | Active (30-70 steps) | ~0.434 | -0.021 | ~0.808 | ~0.68 | **Mild** |
| DPO 1ep | bf16 | Low (1 epoch) | 0.4034 | -0.0023 | 0.8088 | 0.7139 | Neutral |
| GRPO G=8 (ckpt100) | bf16 | Converged (100 steps) | 0.4549 | +0.0492 | 0.8086 | 0.6318 | None |
| RSFT CED (best) | — | Offline (data filter) | 0.4683 | +0.0626 | 0.8156 | 0.6388 | **None** |

### Key Numbers for Paper

- **QLoRA amplification**: bf16 GRPO rel_f1=0.4549 vs QLoRA GRPO rel_f1=0.0138 — QLoRA turns mild (-2pp early) into catastrophic (-39pp)
- **GRPO bf16 trajectory**: ckpt-80→90→100: rel_f1 = 0.4456→0.4523→0.4549 (monotonically improving, no forgetting)
- **GRPO bf16 early checkpoints** show mild decline: step30=0.434, step50=0.4276, step70=0.4341 (all below ckpt-100's 0.4549) — confirms transient mild decoupling during training, recovers by convergence
- **DPO gradual decay**: 1ep rel_f1=0.4034 → 3ep rel_f1=0.3429 (evi_f1 simultaneously rises 0.8088→0.8403)
- **DPO narrative (D067/D068/D069)**: DPO is neutral/gradual, not "failed" — it's a middle data point on the spectrum, confirming decoupling is universal across RL methods
- **Intra-task vs inter-task** (D069): This is NOT catastrophic forgetting of pretrained knowledge; it's competition between RE and evidence objectives within the same task

### Evidence Gaps

- [ ] **GRPO bf16 Ign-F1**: Currently reporting F1; paper_framing notes Ign-F1=45.59 > F1=~43.4 "因 train triples 过滤效应" — this inversion needs explanation in paper
- [ ] **DPO 3ep Ign-F1**: TBD in paper_framing table
- [ ] **GRPO QLoRA (lr=5e-6) Ign-F1**: TBD
- [ ] **Connecting to reward overoptimization literature** (RC9): Need explicit Gao et al. 2023 citation
- [ ] **QuRL/QaRL literature** (D076 framing note): Supports QLoRA amplification narrative but not yet in Related Work

---

## Claim 3: NLI-based scoring improves RSFT quality (CED vs flat-NLI ablation)

**Statement**: Both CED and flat-NLI outperform random/no scoring. CED vs flat-NLI difference is statistically uncertain — CED may be "one possible scoring function" rather than strictly superior.

### Supporting Experiments

#### CED RSFT (top_k=1)

| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |
|--------|------|-------------|--------|--------|------|---------------|-------|
| mvp2_eval_rsft_r1 | 42 (3ep) | 44.49 | 43.63 | 81.87 | 0.6565 | No | 3-epoch run |
| mvp2_eval_rsft_r2a | 42 (1ep) | 44.94 | 44.01 | 81.08 | 0.6641 | No | 1ep, α=128 |
| mvp2_eval_rsft_r2b | 42 (1ep) | 44.93 | 44.10 | 81.28 | 0.6609 | No | 1ep, α=32 |
| mvp2_eval_rsft_s43_r2 | 43 | 46.83 | 45.85 | 81.56 | 0.6388 | No | Best seed |
| mvp2_rsft_train_r1_s44 | 44 | 46.55 | 45.51 | 80.87 | 0.6350 | No | |
| eval_rsft_ced_s45 | 45 | — | — | — | — | — | **RUNNING** |
| reeval_ced_s42 | 42 | — | — | — | — | Yes | **PREPARING** (fixes wrong ckpt) |
| reeval_ced_s44 | 44 | — | — | — | — | Yes | **PREPARING** (fixes wrong seed) |

**CED 3-seed mean (s42-r1/s43/s44)**: rel_f1 = 0.4596 ± 0.0127, evi_f1 = 0.8143 ± 0.0051

#### flat-NLI RSFT (top_k=1)

| exp_id | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | D076 unified? | notes |
|--------|------|-------------|--------|--------|------|---------------|-------|
| eval_plan_001_flat_nli | 42 | 45.39 | 44.49 | 80.43 | 0.6431 | No | |
| reeval_flat_nli_s43 | 43 | 45.23 | TBD | 81.58 | 0.6505 | Partial (fixed adapter, batch=16) | |
| eval_flat_nli_s44 | 44 | 46.15 | 46.15 | 81.31 | 0.6458 | No | |
| eval_flat_nli_seed45 | 45 | 45.51 | 45.51 | 81.54 | 0.6521 | No | |
| reeval_flat_nli_s42 | 42 | — | — | — | — | Yes | **PREPARING** |
| reeval_flat_nli_s43_r2 | 43 | — | — | — | — | Yes | **RUNNING** |

**flat-NLI 4-seed mean (s42/s43/s44/s45)**: rel_f1 = 0.4557 ± 0.0039

#### top_k Ablation

| exp_id | method | seed | F1 (rel_f1) | Ign-F1 | Evi-F1 | EDCR | notes |
|--------|--------|------|-------------|--------|--------|------|-------|
| CED 3-seed mean | CED k=1 | s42/43/44 | 45.96 | 45.00 | 81.43 | 0.6434 | |
| reeval_rsft_topk3 | CED k=3 | 42 | 44.54 | 43.64 | 80.88 | 0.6635 | D076 corrected ign_f1 |

**Δ (k=3 vs k=1 mean)**: Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
- Training data: k=1 → 2718 samples (12.4%), k=3 → 8037 samples (37%) — 2.96× more data but lower quality
- Scoring quality: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205

### Key Numbers for Paper

- **CED vs flat-NLI head-to-head** (current data, NOT D076-unified):
  - CED 3-seed mean rel_f1 = 0.4596 vs flat-NLI 4-seed mean = 0.4557 → Δ = **+0.39pp** (not significant)
  - Dream reported p-values: 0.08 / 0.38 / 0.12 — not statistically significant
- **Both > SFT baseline**: CED +5.39pp, flat-NLI +5.00pp (Ign-F1 vs SFT 40.36)
- **top_k=1 > top_k=3**: Scoring precision matters more than data quantity; rank 2-3 samples dilute quality
- **Status**: CED ≈ flat-NLI statistically indistinguishable → CED is "one possible scoring function," not independently superior (C3 降级)

### Evidence Gaps

- [ ] **D076 unified protocol**: 4/8 evals need rerunning before paired t-test is valid (reeval_ced_s42, reeval_ced_s44, reeval_flat_nli_s42, reeval_flat_nli_s43_r2)
- [ ] **CED s45 eval**: Still RUNNING — needed for 4-seed CED statistics
- [ ] **Paired t-test**: Cannot compute until all seeds are under unified protocol
- [ ] **top_k=3 additional seeds**: Only 1 seed; direction consistent but no significance test possible — present as supplementary ablation row, not independent claim

---

## Claim 4: EDCR dual-layer diagnostic value

**Statement**: EDCR quantifies evidence-extraction decoupling at method level (echoing Claim 2 spectrum) and provides relation-type diagnostic information orthogonal to Evi-F1 at per-relation level.

### Supporting Experiments

| exp_id | analysis | result | notes |
|--------|----------|--------|-------|
| plan_003_edcr_diagnostic | Method-level EDCR table (15 methods) | EDCR vs rel_f1 Spearman ρ=-0.9648 (p=0.0001); EDCR vs evi_f1 ρ=0.0022 (p=0.9941) | EDCR ≈ transform of rel_f1 at method level (D071 flags by-construction concern) |
| D070 per-relation analysis | Per-relation EDCR (93 types, ≥5 samples) | EDCR vs evi_f1 ρ=**-0.064** (p=0.58) → **completely independent**; EDCR vs rel_f1 ρ=-0.793 (p<0.001) | 76 types with non-zero data |
| D070 per-relation analysis | Per-relation evi_f1 vs rel_f1 | ρ=-0.013 (p=0.91) → evidence quality and extraction completely decoupled across relation types | Independent finding supporting paper narrative |

### EDCR Method-Level Summary

| Method | EDCR | rel_f1 | evi_f1 | interpretation |
|--------|------|--------|--------|----------------|
| GRPO QLoRA (lr=5e-6) | 0.9876 | 0.0138 | 0.8504 | Pathological: high evidence, zero extraction |
| GRPO QLoRA (lr=5e-5) | 0.8539 | 0.2167 | 0.5746 | Severe decoupling |
| DPO 3ep | 0.7294 | 0.3429 | 0.8403 | Moderate decoupling |
| SFT baseline | 0.7118 | 0.4057 | 0.7979 | Reference |
| DPO 1ep | 0.7139 | 0.4034 | 0.8088 | ≈ SFT level |
| RSFT r2a (1ep) | 0.6641 | 0.4494 | 0.8108 | Improved |
| RSFT CED k=3 | 0.6635 | 0.4454 | 0.8088 | Improved |
| RSFT r2b (1ep) | 0.6609 | 0.4493 | 0.8128 | Improved |
| RSFT CED s42 (3ep) | 0.6565 | 0.4449 | 0.8187 | Improved |
| flat-NLI s43 | 0.6505 | 0.4523 | 0.8158 | Improved |
| flat-NLI s44 | 0.6458 | 0.4615 | 0.8131 | Improved |
| flat-NLI s42 | 0.6431 | 0.4539 | 0.8043 | Improved |
| RSFT CED s43 | 0.6388 | 0.4683 | 0.8156 | Best RSFT |
| RSFT CED s44 | 0.6350 | 0.4655 | 0.8087 | Near best |
| GRPO bf16 G=8 | 0.6318 | 0.4549 | 0.8086 | Best GRPO (no decoupling) |
| CED reranker | 0.6156 | 0.4864 | 0.8188 | **Best overall** |

### Per-Relation Exemplars (D070)

| Relation Type | EDCR | evi_f1 | rel_f1 | interpretation |
|---------------|------|--------|--------|----------------|
| date_of_birth | 0.118 | high | high | High faithfulness — easy relation |
| head_of_government | 0.956 | 0.875 | low | High evidence quality but poor extraction — EDCR catches what evi_f1 misses |

### Key Numbers for Paper

- **Layer 1 (method-level)**: EDCR identifies pathological models (GRPO QLoRA: EDCR≈1.0) — works as decoupling meter, echoes Claim 2
- **Layer 2 (per-relation)**: EDCR vs evi_f1 ρ=-0.064 → completely independent signals at per-relation granularity
- **D071 caveat**: Method-level EDCR ≈ f(1/rel_f1) by construction — when model predicts wrong relations, evidence automatically becomes "distractor." Paper must acknowledge this and frame method-level EDCR as decoupling measure, not independent evidence quality metric
- **D073 definition**: Paper uses distractor count ratio (∈[0,1]) definition; formula proxy 1-rel_f1/evi_f1 only for method-level quick comparison; per-relation tables require n_pred≥10 filter

### Evidence Gaps

- [ ] **100-example human annotation validation** (plan_013): Not started — needed for RC6
- [ ] **TP-only EDCR** (D071): Not implemented — needed to address by-construction confound; if TP-only EDCR still correlates with rel_f1, Claim 4 method-level value is weak
- [ ] **More per-relation exemplars**: Need to populate full table with n_pred≥10 filter (D073)

---

## Cross-Claim Protocol Issues

### D076 Unified Protocol Reeval Status

The following evals have protocol inconsistencies that prevent valid paired t-test (Claim 3):

| exp_id | issue | unified reeval | status |
|--------|-------|---------------|--------|
| CED s42 (mvp2_eval_rsft_r2b_maxtok1536_r2) | Wrong checkpoint (r2b α=32 instead of ckpt-510 α=128), batch_size=8, max_new_tokens=1536 | reeval_ced_s42 | PREPARING |
| CED s44 (mvp2_rsft_train_r1_s44) | Seed=42 in eval (should be 44) | reeval_ced_s44 | PREPARING |
| flat-NLI s42 (eval_plan_001_flat_nli) | batch_size=16 | reeval_flat_nli_s42 | PREPARING |
| flat-NLI s43 (reeval_flat_nli_s43) | batch_size=16 | reeval_flat_nli_s43_r2 | RUNNING |

**Unified protocol**: batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, correct seed.

**Impact**: Old protocol data can be used for directional claims but NOT for paired t-test (Claim 3 significance). All 8 CED/flat-NLI evals must be under unified protocol before statistical comparison.

### Ign-F1 vs F1 Issue

- Most registry entries show ign_f1 = rel_f1 (suspected eval pipeline bug, D069)
- Paper_framing table has corrected Ign-F1 values that differ from F1 (e.g., SFT no-evidence: Ign-F1=47.36 vs F1=48.93)
- D071: "Ign-F1 修正后排名无实质变化"
- **Paper uses Ign-F1 in main table** per D071

### Experiments Still Running / Pending

| exp_id | purpose | status | blocking |
|--------|---------|--------|----------|
| eval_rsft_ced_s43 | CED s43 re-eval | RUNNING | C3 statistics |
| eval_rsft_ced_s45 | CED s45 (new seed) | RUNNING | C3 statistics |
| eval_plan_014_no_evidence_r2 | SFT no-evidence re-eval | RUNNING | — |
| reeval_ced_s42 | Unified protocol CED s42 | PREPARING | C3 paired t-test |
| reeval_ced_s44 | Unified protocol CED s44 | PREPARING | C3 paired t-test |
| reeval_flat_nli_s42 | Unified protocol flat-NLI s42 | PREPARING | C3 paired t-test |
| reeval_flat_nli_s43_r2 | Unified protocol flat-NLI s43 | RUNNING | C3 paired t-test |
| plan_002 | Test set evaluation | PLANNED | C1 final numbers |
| plan_013 | EDCR human annotation (100 examples) | PLANNED | C4 validation |

---

## Summary: Paper-Ready vs Gaps

### Paper-Ready Numbers

1. **Evidence tax**: 47.36 → 40.36 = -7.00pp Ign-F1 (plan_014 vs noquant SFT)
2. **CED reranker recovery**: F1=48.64, only -0.29pp below no-evidence (plan_005)
3. **RSFT CED best**: Ign-F1=45.85, +5.49pp over SFT (s43)
4. **Decoupling spectrum**: Complete data for GRPO QLoRA / GRPO bf16 / DPO / RSFT
5. **QLoRA amplification**: bf16 0.4549 vs QLoRA 0.0138 (plan_011 vs QLoRA runs)
6. **EDCR per-relation independence**: ρ=-0.064 vs evi_f1 (D070)
7. **top_k ablation**: k=1 > k=3, precision > quantity (plan_008)
8. **DREEAM baseline**: F1=63.57, Evi-F1=54.01 reproduced (plan_004)

### Critical Gaps (blocking paper submission)

1. **D076 unified reevals** — blocking Claim 3 statistical test
2. **CED reranker Ign-F1** — needed for main table
3. **Test set evaluation** (plan_002) — no official numbers yet
4. **DREEAM-protocol Evi-F1 alignment** — cross-paradigm evidence comparison

### Nice-to-Have (strengthen but not blocking)

1. EDCR human validation (plan_013) — RC6
2. Post-hoc retrieval baseline (SFT + BM25) — RC10
3. Model size ablation (plan_006) — RC4
4. TP-only EDCR (D071) — method-level confound
5. Re-DocRED extension (plan_007) — RC4
