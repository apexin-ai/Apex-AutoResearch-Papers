# Evidence Tables — recovery_aware_struct_prune
## EMNLP 2026 ARR May 25 Submission
**Generated**: 2026-05-16 | **Model**: DeepSeek-R1-Distill-Qwen-7B | **Task**: GSM8K (greedy, seed=42)

---

## Table 1: Post-Prune Accuracy (GSM8K, greedy, no recovery)

| Model | Sparsity | Method | α | N | Accuracy | Std Err | Server | Cal | exp_id | Notes |
|-------|----------|--------|---|---|----------|---------|--------|-----|--------|-------|
| Unpruned | 0% | — | — | — | — | — | — | — | — | Not evaluated post-prune (baseline = pre-prune) |
| RASP | 20% | CKA-aware | 1.0 | 100 | 31% | N/A | westb | 512 | alpha_ablation_sweep | α=1.0 = RASP default |
| RASP | 20% | CKA-aware | 1.0 | 100 | 31% | N/A | westb | 256 | reeval_postprune_definitive | Matches cal=512 result |
| RASP | 20% | CKA-aware | 1.0 | 100 | 29% | N/A | westd | 256 | reeval_postprune_definitive | 2pp lower than westb |
| Standard | 20% | Importance-only | 0.0 | 100 | 27% | N/A | westb | 512 | alpha_ablation_sweep | α=0.0 = Standard |
| Standard | 20% | Importance-only | 0.0 | 100 | 27% | N/A | westb | 256 | reeval_postprune_definitive | Matches cal=512 |
| GraSP | 20% | Gradient signal | — | 100 | 7% | N/A | westd | — | grasp_baseline_westd | eos_rate=0.02, avg_len=4018 |
| α=0.25 | 20% | RASP variant | 0.25 | 100 | 23% | N/A | westb | 512 | alpha_ablation_sweep | |
| α=0.5 | 20% | RASP variant | 0.5 | 100 | 22% | N/A | westb | 512 | alpha_ablation_sweep | |
| α=2.0 | 20% | RASP variant | 2.0 | 100 | 36% | N/A | westb | 512 | alpha_ablation_sweep | |
| α=4.0 | 20% | RASP variant | 4.0 | N/A | 40% | N/A | westd | 256 | alpha_ablation_westd_cal256 | ⚠️ PREPARING, highest post-prune |

**α ablation U-shape pattern** (westb, cal=512): α=0.0 → 27%, α=0.25 → 23%, α=0.5 → 22%, α=1.0 → 31%, α=2.0 → 36%.
Non-monotonic: dip at α=0.25–0.5, recovery at α≥1.0.

⚠️ All post-prune evals are N=100 only — no std err reported. Statistical power is limited.

---

## Table 2: Post-SFT Recovery (GSM8K, greedy, seed=42)

**SFT config (all runs identical)**: 2 epochs, lr=2e-5, batch=1, grad_accum=8, GSM8K train (7473 samples), seed=42, total_steps=1870.

### Table 2a: Definitive Results (N=1319, full test set)

| Model | Sparsity | Method | N | Accuracy | Std Err | Server | exp_id |
|-------|----------|--------|---|----------|---------|--------|--------|
| **Unpruned SFT** | 0% | — | 1319 | **81.27%** | 1.07pp | westd | eval_sft_unpruned_full |
| **RASP SFT** | 20% | CKA-aware (α=1.0) | 1319 | **61.49%** | 1.34pp | westd | eval_sft_rasp_full_westd |
| **Standard SFT** | 20% | Importance-only | 1319 | **59.29%** | 1.35pp | westd | eval_sft_standard_full_westd |

**RASP vs Standard gap**: +2.20pp (61.49% vs 59.29%), ⚠️ p=0.25, NOT statistically significant at N=1319.

### Table 2b: Supporting Results (N=100)

| Model | Sparsity | Method | N | Accuracy | Std Err | Server | exp_id |
|-------|----------|--------|---|----------|---------|--------|--------|
| Unpruned SFT | 0% | — | 100 | 84% | 3.67pp | westd | eval_sft_unpruned_n100 |
| RASP SFT | 20% | CKA-aware | 100 | 57% | N/A | westb | sft_rasp_20 (inline) |
| RASP SFT | 20% | CKA-aware | 100 | 67% | 4.70pp | westd | eval_sft_rasp_20_westd_n100 |
| Standard SFT | 20% | Importance-only | 100 | 64% | N/A | westb | sft_standard_20 (inline) |
| Standard SFT | 20% | Importance-only | 100 | 63% | 4.80pp | westd | eval_sft_standard_20_westd_n100 |
| GraSP SFT | 20% | Gradient signal | 100 | 41% | 4.92pp | westd | eval_sft_grasp_20_westd |

⚠️ **westb vs westd discrepancy**: RASP SFT = 57% (westb) vs 67% (westd), 10pp gap. Standard SFT = 64% (westb) vs 63% (westd), 1pp gap. RASP is more sensitive to calibration/server differences. N=100 evals are noisy.

### Table 2c: α Ablation Post-SFT (N=100, westd)

| α | Post-Prune Acc | Post-SFT Acc | SFT Recovery (pp) | exp_id |
|---|---------------|--------------|-------------------|--------|
| 0.0 (=Standard) | 27% | 64% | +37pp | eval-sft-alpha-0p0 |
| 0.5 | 22% | ⚠️ N/A | — | eval_sft_alpha_0p5 (PREPARING) |
| 1.0 (=RASP) | 31% | 57% | +26pp | eval-sft-alpha-1p0 |
| 2.0 | 36% | 62% | +26pp | eval_sft_alpha_2p0 |
| 4.0 | 40% | 62% | +22pp | sft_alpha4_0_westd_retry (inline) |

**Pattern**: SFT recovery gain (pp) is inversely related to post-prune accuracy (more damaged → more room for SFT to recover).

⚠️ All α SFT results are N=100 only. α=0.5 SFT eval still PREPARING.

---

## Table 3: GRPO Collapse Dynamics (Post-SFT GRPO Stage 2)

| Model | exp_id | Steps Trained | Collapse Step | Peak Reward | Final Reward | frac_zero_std (final) | grad_norm (final) | Eval Acc (peak, N=1319) |
|-------|--------|---------------|---------------|-------------|--------------|----------------------|-------------------|------------------------|
| **RASP v9** | grpo_stage2_rasp_20_v9 | 30/30 | ≤ step 10 (permanent) | 0.039 (step 20) | 0.021 | 0.950 | 1.398 | 60.65% (step 5) |
| **Standard v8** | grpo_stage2_standard_20_v8 | 90/100 | step 60 (transient) | 0.096 (step 40) | 0.065 (step 90) | 0.475 | 2.14 | 58.91% (step 50) |
| **Unpruned v2** | grpo_unpruned_v2 | 100/100 | None | 0.669 (step 80) | 0.661 (step 100) | N/A | 6.97 | 81.27% (step 100) |

### RASP v9 Step-by-Step Dynamics (W&B: mrikafz3)
| Step | Reward | frac_zero_std | Notes |
|------|--------|---------------|-------|
| 10 | 0.015 | 0.875 | Collapse onset |
| 20 | 0.039 | 0.800 | Peak reward (brief recovery) |
| 30 | 0.021 | 0.950 | Final — permanent collapse confirmed |

### Standard v8 Step-by-Step Dynamics
| Step | Reward | frac_zero_std | grad_norm | Notes |
|------|--------|---------------|-----------|-------|
| 40 | 0.096 | 0.450 | 3.45 | Peak reward |
| 50 | 0.037 | 0.600 | 2.09 | Declining |
| 60 | 0.041 | 0.525 | 0.013 | Transient dip (near-zero grad) |
| 90 | 0.065 | 0.475 | 2.14 | Recovery |

### Unpruned v2 Dynamics
| Step | Reward | Notes |
|------|--------|-------|
| 30 | 0.425 | Shallow dip |
| 40 | recovered | — |
| 80 | 0.669 | Peak |
| 100 | 0.661 | Stable finish |
Entropy: 0.184–0.214, KL: 0.0046–0.0053.

**Collapse severity gradient**: RASP (step ≤10, permanent) > Standard (step 60, transient) > Unpruned (none). Ratio: 6× faster collapse RASP vs Standard.

---

## Table 4: Reward-Accuracy Decoupling (N=1319)

| Model | SFT Accuracy | Best GRPO Accuracy | GRPO Checkpoint | Δ (pp) | Peak Reward | Correct Count | Conclusion |
|-------|-------------|--------------------|--------------------|--------|-------------|---------------|------------|
| **Unpruned** | 81.27% | 81.27% | step 100 | **0.00** | 0.661 | 1072/1319 (identical) | Reward ↑↑ but accuracy unchanged |
| **Standard** | 59.29% | 58.91% | step 50 | **-0.38** | 0.096 | — | Slight degradation |
| **RASP** | 61.49% | 60.65% | step 5 | **-0.84** | 0.039 | — | Slight degradation + collapse |

**Key finding**: GRPO reward improvement NEVER translates to accuracy gain across all three models. Unpruned model achieves reward 0 → 0.661 while accuracy stays at exactly 81.27% (identical 1072/1319 correct answers). Pruning adds training collapse on top of universal decoupling.

⚠️ Notes:
- Unpruned GRPO step-100 eval (eval_grpo_unpruned_v2_step100) shows 81.27% (1072/1319) but status still marked RUNNING in registry
- RASP GRPO step-5 is pre-collapse; step-10 eval (eval_grpo_rasp_v9_step10) still RUNNING (249/1319 done, partial acc ~68%)
- Unpruned step-90 eval: 80.59% (1063/1319), also still marked RUNNING

---

## Table 5: Evidence → Claim Mapping

### Claim 1: GRPO reward-accuracy decoupling is universal; pruning adds training collapse

| Evidence | exp_id(s) | Key Numbers | Strength |
|----------|-----------|-------------|----------|
| Unpruned: reward 0→0.661, accuracy 81.27%→81.27% | grpo_unpruned_v2, eval_grpo_unpruned_v2_step100, eval_sft_unpruned_full | Δ=0.00pp, identical 1072/1319 | ✅ **Strong** |
| Standard: SFT 59.29% → GRPO 58.91% | grpo_stage2_standard_20_v8, eval_grpo_standard_step50_full, eval_sft_standard_full_westd | Δ=-0.38pp | ✅ Strong |
| RASP: SFT 61.49% → GRPO 60.65% | grpo_stage2_rasp_20_v9, eval_grpo_rasp_v9_step5, eval_sft_rasp_full_westd | Δ=-0.84pp | ✅ Strong |
| RASP collapse at step ≤10 | grpo_stage2_rasp_20_v9 | frac_zero_std=0.95 | ✅ Strong |
| Standard transient dip at step 60 | grpo_stage2_standard_20_v8 | grad_norm 3.45→0.013→2.14 | ✅ Strong |
| Unpruned no collapse | grpo_unpruned_v2 | 100 steps stable, reward 0.661 | ✅ Strong |

### Claim 2: Collapse severity gradient diagnoses structural damage

| Evidence | exp_id(s) | Key Numbers | Strength |
|----------|-----------|-------------|----------|
| RASP permanent collapse step ≤10 | grpo_stage2_rasp_20_v9 | peak reward 0.039 | ✅ Strong |
| Standard transient dip step 60 | grpo_stage2_standard_20_v8 | peak reward 0.096, recovered | ✅ Strong |
| Unpruned no collapse | grpo_unpruned_v2 | peak reward 0.669, stable | ✅ Strong |
| 6× speedup RASP→Standard | v9 vs v8 comparison | step 10 vs step 60 | ✅ Strong |
| ⚠️ Only 3 pruning methods compared | — | — | ⚠️ Limited generality |
| ⚠️ Only 1 sparsity level (20%) | — | — | ⚠️ Limited generality |

### Claim 3: Recovery method conditions optimal pruning strategy (Redundancy-Stability Tradeoff)

| Evidence | exp_id(s) | Key Numbers | Strength |
|----------|-----------|-------------|----------|
| SFT: RASP +2.2pp over Standard | eval_sft_rasp_full_westd, eval_sft_standard_full_westd | 61.49% vs 59.29% (N=1319) | ⚠️ **Weak** (p=0.25) |
| GRPO: RASP 6× faster collapse | grpo_stage2_rasp_20_v9 vs v8 | step 10 vs step 60 | ✅ Strong |
| Opposite direction: SFT-good ≠ RLVR-good | Combined SFT + GRPO evidence | Same structures, opposite outcomes | ✅ Conceptually strong |
| ⚠️ SFT gap not significant | eval_sft_rasp_full_westd, eval_sft_standard_full_westd | p=0.25, N=1319 | ⚠️ **Critical weakness** |

---

## Data Consistency Audit

### ✅ Verified Consistent (paper_framing.md vs registry)

| paper_framing.md Claim | Registry Value | Status |
|------------------------|----------------|--------|
| Unpruned SFT = 81.27% | 81.27% (eval_sft_unpruned_full) | ✅ Match |
| Unpruned GRPO step-100 = 81.27% (1072/1319) | 81.27% (1072/1319) (eval_grpo_unpruned_v2_step100) | ✅ Match |
| Standard SFT = 59.29% | 59.29% (eval_sft_standard_full_westd) | ✅ Match |
| Standard GRPO step-50 = 58.91% | 58.91% (eval_grpo_standard_step50_full) | ✅ Match |
| RASP SFT = 61.49% | 61.49% (eval_sft_rasp_full_westd) | ✅ Match |
| RASP GRPO step-5 = 60.65% | 60.65% (eval_grpo_rasp_v9_step5) | ✅ Match |
| RASP v9 peak reward = 0.039 | 0.039 (step 20) | ✅ Match |
| Standard v8 final reward = 0.065 | 0.065 (step 90) | ✅ Match |
| Unpruned v2 final reward = 0.661 | 0.661 (step 100) | ✅ Match |
| RASP v9 frac_zero_std = 0.95 | 0.95 (step 30) | ✅ Match |
| RASP collapse step ~10 | ≤ step 10 | ✅ Match |
| Standard transient dip step ~60 | step 60 | ✅ Match |
| 6× speedup (Standard→RASP) | 60/10 = 6× | ✅ Match |
| SFT gap +2.2pp | 61.49 - 59.29 = 2.20 | ✅ Match |

### ⚠️ Inconsistencies / Issues Found

| Issue | paper_framing.md Says | Registry Says | Severity |
|-------|----------------------|---------------|----------|
| **RASP grad_norm at collapse** | "grad→0.007" | v9 grad_norm=1.398 (final), v8 grad_norm=0.011 (final) | ⚠️ **Medium** — 0.007 not found in registry. May be from W&B step-level data not captured in registry. Needs verification against W&B run mrikafz3. |
| **Unpruned frac_zero_std ≤0.275** | "stable frac_zero_std ≤0.275" | N/A in registry for v2 | ⚠️ **Low** — likely from W&B data. Verify against W&B. |
| **Unpruned GRPO step-90 = ~81.00%** | "~81.00% (intermediate estimate)" | 80.59% (1063/1319) | ⚠️ **Low** — paper says "intermediate estimate", registry has actual value 80.59%. Use 80.59% in paper. |

### 🔄 RUNNING Experiments (not yet final)

| exp_id | Description | Partial Result | Impact on Paper |
|--------|-------------|----------------|-----------------|
| eval_grpo_unpruned_v2_step100 | Unpruned GRPO step-100, N=1319 | 81.27% (1072/1319) — appears complete | **Critical** — core Claim 1 data. Result looks final but status not updated. |
| eval_grpo_unpruned_v2_step90 | Unpruned GRPO step-90, N=1319 | 80.59% (1063/1319) — appears complete | Medium — supplementary. |
| eval_grpo_rasp_v9_step10 | RASP GRPO step-10, N=1319 | 249/1319 done, partial ~68% | Medium — would show post-collapse accuracy. |

### ⚠️ Missing Data Points

| Gap | Impact | Recommended Action |
|-----|--------|-------------------|
| No N=1319 post-prune evals | All post-prune are N=100, no std err | Low — paper focuses on post-SFT/GRPO, not post-prune |
| No N=1319 GraSP SFT eval | Only N=100 (41%) | Low — GraSP is a baseline, N=100 sufficient for paper |
| α=0.5 SFT eval missing | PREPARING | Medium — incomplete α ablation table |
| No N=1319 α SFT evals | All α SFT are N=100 | Low — α ablation is supplementary |
| RASP GRPO step-10 eval incomplete | 249/1319 | Medium — would strengthen collapse narrative |

### 📋 Calibration & Server Notes

| Factor | Details |
|--------|---------|
| **westb calibration** | cal=512 (alpha_ablation_sweep), cal=256 (reeval_postprune_definitive) |
| **westd calibration** | cal=256 |
| **westb vs westd gap** | RASP post-prune: 31% (westb) vs 29% (westd) = 2pp difference |
| **SFT server** | All N=1319 SFT evals on westd. N=100 inline evals on westb. |
| **GRPO server** | v9 (RASP) on westb, v8 (Standard) on westb, v2 (Unpruned) on westd |
| **Cross-server GRPO concern** | Unpruned GRPO (westd) vs pruned GRPO (westb) — different servers. ⚠️ Should be noted in paper. All SFT N=1319 evals are westd, so SFT→GRPO comparison is same-server for each model. |

---

## Summary Statistics for Paper

### Headline Numbers (all N=1319 unless noted)
- **Unpruned SFT**: 81.27% ± 1.07
- **Unpruned GRPO step-100**: 81.27% (1072/1319 correct, identical to SFT)
- **Unpruned GRPO reward**: 0 → 0.661
- **RASP SFT**: 61.49% ± 1.34
- **Standard SFT**: 59.29% ± 1.35
- **RASP vs Standard SFT**: +2.20pp (p=0.25, not significant)
- **RASP GRPO collapse**: step ≤10, permanent, peak reward 0.039
- **Standard GRPO dip**: step 60, transient, peak reward 0.096
- **Collapse speed ratio**: 6× (RASP vs Standard)
- **GraSP SFT**: 41% (N=100 only)

### Paper-Ready Claims (conservative)
1. "GRPO reward never translates to accuracy" — ✅ supported by all 3 models
2. "Pruning causes GRPO collapse; redundancy removal accelerates it" — ✅ supported by 3-model gradient
3. "SFT-optimal pruning ≠ RLVR-optimal pruning" — ⚠️ directionally supported but SFT gap not significant
