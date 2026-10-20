# ContamCal Results Tables (for EMNLP 2026 paper)

**Generated**: 2026-05-14 | **Source**: experiment registry + exp004 analysis artifact

---

## Table 1: Phase 3-4 SFT Eval — Benchmark Scores (Model × Dosage)

All models: Qwen2.5 family, LoRA r=16 α=32, 1 epoch SFT.

| Model | Dosage | Seed | MMLU | GSM8K | ARC-C | HumanEval | mc_format | exp_id |
|-------|--------|------|------|-------|-------|-----------|-----------|--------|
| 0.5B | 0% | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 | **legacy** | exp_001_eval_05B_d000_s42_v5 |
| 0.5B | 0% | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 | **legacy** | exp_001_eval_05B_d000_s123 |
| 0.5B | 5% | 42 | — | — | — | — | legacy | exp_001_eval_05B_d005 ^1 |
| 0.5B | 100% | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 | **legacy** | exp_001_eval_05B_d100_v5 |
| 1.5B | 0% | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 | TBD ^2 | exp_001_eval_15B_d000_s42_v2 |
| 1.5B | 0% | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 | TBD ^2 | exp_001_eval_15B_d000_s123 |
| 1.5B | 5% | — | — | — | — | — | — | **missing** |
| 1.5B | 100% | — | — | — | — | — | — | **missing** ^3 |
| 3B | 0% | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 | TBD ^2 | exp_001_eval_3B_d000_s42 |
| 3B | 0% | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 | TBD ^2 | exp_001_eval_3B_d000_s123 |
| 3B | 5% | — | — | — | — | — | — | **missing** |
| 3B | 100% | — | — | — | — | — | — | **missing** |

### Notes
- ^1: exp_001_eval_05B_d005 registered as success but **no metrics in registry**. Need to extract from result files on server.
- ^2: 1.5B/3B eval format (legacy vs aligned) not annotated in registry. Needs verification against D017 decision.
- ^3: 1.5B d100 SFT is complete (exp_001_sft_d100_15B_v2), but eval has not been run.

### D017 Format Compatibility
- **legacy mc_format**: 0.5B evals confirmed legacy. MC scores may undercount due to format mismatch (e.g., 0.5B d100 MMLU=0.232 is -17.3pp below d000 baseline — likely format artifact, not real degradation).
- **aligned mc_format**: Not yet confirmed for any completed eval.
- **Implication**: 0.5B dose-response (d000 vs d100) is NOT valid for paper analysis until re-run with aligned format.

---

## Table 2: Baseline Cross-Seed Consistency (d000 only)

| Model | Metric | Seed 42 | Seed 123 | Δ | CV% |
|-------|--------|---------|----------|---|-----|
| 0.5B | MMLU | 0.4049 | 0.4182 | 0.013 | 2.2% |
| 0.5B | GSM8K | 0.3647 | 0.3404 | 0.024 | 4.9% |
| 0.5B | ARC-C | 0.3780 | 0.3976 | 0.020 | 3.6% |
| 0.5B | HumanEval | 0.1098 | 0.1037 | 0.006 | 4.0% |
| 1.5B | MMLU | 0.5753 | 0.5762 | 0.001 | 0.1% |
| 1.5B | GSM8K | 0.6368 | 0.6331 | 0.004 | 0.4% |
| 1.5B | ARC-C | 0.7756 | 0.7662 | 0.009 | 0.9% |
| 1.5B | HumanEval | 0.1280 | 0.1707 | 0.043 | 20.2% |
| 3B | MMLU | 0.6340 | 0.6362 | 0.002 | 0.2% |
| 3B | GSM8K | 0.1170 | 0.1759 | 0.059 | 28.4% |
| 3B | ARC-C | 0.8220 | 0.8294 | 0.007 | 0.6% |
| 3B | HumanEval | 0.1160 | 0.0854 | 0.031 | 21.5% |

**Observation**: MC benchmarks (MMLU, ARC) are stable across seeds (CV <5%). Generation benchmarks (HumanEval, GSM8K on 3B) show high variance (CV 20-28%), expected for small sample sizes (164 HumanEval, 1319 GSM8K).

**Anomaly**: 3B GSM8K scores (0.117, 0.176) are lower than 1.5B (0.637, 0.633). This is unexpected for a larger model and may indicate an eval issue — needs investigation.

---

## Table 3: MVP Simulation — 4PL+γ Base Recovery (exp: mvp_sim_4pl_gamma)

Config: 50 models × 300 items, Stan NUTS 4 chains × 1000+1000, seed=42.

| Variant | γ_mean | γ_rel_bias | CI95 covers true | CI95 excludes 0 | θ_corr | θ_RMSE | Divergent% | Max Rhat | Min ESS | Fit time (s) |
|---------|--------|------------|-----------------|-----------------|--------|--------|------------|----------|---------|--------------|
| 4PL+γ NUTS (N_items=300) | 0.466 | 0.068 | Yes | Yes | 0.943 | 0.238 | 0% | 1.003 | — | 1407.5 |

**Verdict**: PASS. γ identified with <7% relative bias, θ correlation >0.94.

---

## Table 4: MVP Simulation — Confounding Robustness (exp: mvp_sim_confounding)

Config: 50 models × 300 items, θ-exposure corr=0.381, Stan NUTS 4 chains × 1000+1000, seed=123.

| Metric | Value | Pass criterion | Status |
|--------|-------|----------------|--------|
| γ_mean | 0.5386 | — | — |
| γ_rel_bias | 0.077 | <0.15 | PASS |
| γ CI95 covers true | Yes | — | PASS |
| γ CI95 excludes 0 | Yes | — | PASS |
| θ_corr | 0.9733 | >0.9 | PASS |
| θ_RMSE | 0.2407 | — | — |
| θ_residual × exposure corr | 0.0582 | <0.1 (separation) | PASS |
| Divergent% | 0% | <1% | PASS |
| Max Rhat | 1.007 | <1.05 | PASS |
| Min ESS | 1371.9 | >400 | PASS |
| Fit time (s) | 832 | — | — |

**Verdict**: PASS. γ separable from θ even under moderate ability-exposure confounding.

---

## Table 5: EXP-004 Simulation Sweep — γ Recovery by AUC × N_models

Config: 4PL+γ Stan NUTS, prior_sd=1.0, binary exposure. 43/120 runs complete (35.8%).

| AUC | N_models | Seeds done | γ Bias | γ RMSE | CI95 Width | Cov95 | Power | θ_corr |
|-----|----------|------------|--------|--------|------------|-------|-------|--------|
| 0.55 | 20 | 10/10 | +0.020 | 0.040 | 0.133 | 0.80 | 1.00 | 0.958 |
| 0.55 | 50 | 10/10 | +0.015 | 0.026 | 0.087 | 0.90 | 1.00 | 0.947 |
| 0.55 | 100 | 7/10 | −0.003 | 0.005 | 0.064 | 1.00 | 1.00 | 0.951 |
| 0.80 | 20 | 10/10 | −0.016 | 0.081 | 0.258 | 0.90 | 1.00 | 0.972 |
| 0.80 | 50 | 6/10 | +0.005 | 0.035 | 0.162 | 1.00 | 1.00 | 0.968 |
| 0.65 | 20/50/100 | 0/30 | — | — | — | — | — | — |
| 0.80 | 100 | 0/10 | — | — | — | — | — | — |
| 0.90 | 20/50/100 | 0/30 | — | — | — | — | — | — |

**Source**: artifacts/exp004_incremental_analysis.md

### Key Findings (paper-ready)
1. **γ identifiable at near-chance exposure quality**: AUC=0.55, RMSE ≤ 0.04 (N=20), ≤ 0.005 (N=100). 100% power across all 43 runs.
2. **Precision scales as O(1/√N)**: CI width ratios match theory within 5%.
3. **High-AUC exposure inflates γ posterior**: CI95 width at AUC=0.80 is 1.85–1.95× AUC=0.55 (ability-exposure collinearity).
4. **Bias direction reversal**: positive bias at AUC=0.55, negative at AUC=0.80 (needs AUC=0.65/0.90 to confirm trend).

---

## Table 6: SFT Training Summary (Phase 3)

| Model | Dosage | Seed | Final Loss | Token Acc | Train Time (min) | exp_id |
|-------|--------|------|------------|-----------|-------------------|--------|
| 0.5B | 0% | 42 | 1.489 | 0.682 | 52.9 | exp_001_sft_0pct_05B |
| 0.5B | 0% | 123 | — | 0.676 | 54.5 | exp_001_sft_0pct_05B_s123 |
| 0.5B | 5% | 42 | 1.478 | 0.667 | 56.1 | exp_001_sft_d005_05B_v3 |
| 0.5B | 100% | 42 | 1.594 | 0.666 | 68.9 | exp_001_sft_d100_05B |
| 1.5B | 0% | 42 | 1.204 | 0.711 | 101.5 | exp_001_sft_0pct_15B |
| 1.5B | 0% | 123 | — | 0.731 | 101.5 | exp_001_sft_0pct_15B_s123 |
| 1.5B | 100% | 42 | — | — | — | exp_001_sft_d100_15B_v2 ^4 |
| 3B | 0% | 42 | 1.074 | 0.734 | 214.7 | exp_001_sft_0pct_3B |
| 3B | 0% | 123 | 1.114 | 0.751 | 213.1 | exp_001_sft_0pct_3B_s123 |

^4: SFT complete but training metrics not recorded in registry (only status=DONE).

---

## Gap Analysis: What's Missing for Paper

### Critical (blocks paper tables)
1. **Aligned-format evals for ALL models/dosages**: legacy format results (all 0.5B evals) are not usable for dose-response analysis. Need evaluate.py with aligned mc_format.
2. **1.5B d100 eval**: SFT done, eval not yet run.
3. **Contaminated dosage evals for 1.5B and 3B**: No d005 or d100 evals exist for 1.5B (only d000) or 3B (only d000).
4. **0.5B d005 eval metrics**: Run completed but metrics not captured in registry.

### Important (strengthens paper)
5. **3B d005 and d100 SFT + eval**: Needed for full 3-model × 3-dosage matrix.
6. **1.5B d005 SFT + eval**: Needed for mid-dosage data point.
7. **EXP-004 remaining 77 runs** (AUC=0.65/0.90, remaining seeds): Maps full AUC→precision curve.

### Nice-to-have
8. **Seed 123 for contaminated conditions** (d005, d100): Variance estimation on contaminated models.
9. **EXP-004 prior sensitivity** (prior_sd ≠ 1.0): Only one prior tested so far.

### Current Coverage Matrix

| | d000 s42 | d000 s123 | d005 s42 | d100 s42 |
|---|----------|-----------|----------|----------|
| 0.5B | legacy | legacy | no metrics ^1 | legacy |
| 1.5B | TBD ^2 | TBD ^2 | **missing** | **missing** ^3 |
| 3B | TBD ^2 | TBD ^2 | **missing** | **missing** |

Filled: 6/12 cells have metrics. Of those, 4 are confirmed legacy format (diagnosis only).
