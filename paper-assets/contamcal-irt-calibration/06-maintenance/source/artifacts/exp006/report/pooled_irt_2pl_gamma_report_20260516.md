# Pooled IRT 2PL+γ Calibration Report

**Date**: 2026-05-16
**Experiment**: exp006 — Pooled RRF-IRT Calibration
**Server**: cqa1-21977 (CPU)
**Model**: 2PL+γ (contam_irt_2pl_gamma.stan)

---

## Pipeline Summary

### Step 1: RRF Re-aggregation (exp003)
- **Signals**: s1_embedding, s2_minkpp, s4_selfcritique
- **Scales**: 0.5B, 1.5B, 3B (Qwen2.5 family)
- **RRF k**: 60
- **Output**: `exposure_scores.json` — 30 models × 3 benchmarks
- **Filtering**: ALPHA16_BLOCKLIST applied, DEPRECATED dirs skipped

### Step 2: Pooled IRT Fitting (exp006)
- **Stan MCMC config**: 4 chains, 1000 warmup + 1000 sampling, adapt_delta=0.95, max_treedepth=12, seed=42
- **Item subsampling**: MAX_ITEMS=300 per benchmark
- **D045 exclusion**: 0.5B excluded from MMLU and ARC (N=16); all scales for GSM8K (N=24)
- **Exposure source**: RRF signal composite scores

---

## Main Results

| Benchmark | N_models | N_items | γ̂ | 95% CI | CI excl. 0 | PPP | raw_MAE | cal_MAE | ΔMAE | R̂ | ESS | div |
|-----------|----------|---------|------|--------|------------|------|---------|---------|------|------|------|-----|
| MMLU | 16 | 300 | 0.6551 | [−0.4056, 1.7366] | No | 0.1920 | 0.0155 | 0.0070 | 0.0085 | 1.0069 | 1453 | 0 |
| ARC | 16 | 300 | 0.7269 | [0.0207, 1.4433] | **Yes** | 0.0030 | 0.0338 | 0.0201 | 0.0136 | 1.0072 | 1449 | 0 |
| GSM8K | 24 | 300 | 0.0639 | [−0.3636, 0.4902] | No | 0.5413 | 0.1694 | 0.0062 | 0.1632 | 1.0078 | 1313 | 0 |

---

## Diagnostics

All three benchmarks pass convergence checks:
- **R̂** < 1.01 for all (threshold: 1.05)
- **ESS** > 1300 for all (threshold: 400)
- **Divergences**: 0 across all benchmarks
- **PPP**: MMLU=0.192 (adequate), ARC=0.003 (marginal), GSM8K=0.541 (good)

## Interpretation

- **ARC**: Only benchmark where 95% CI excludes zero (γ̂=0.73, CI=[0.02, 1.44]), indicating statistically detectable contamination signal. Very low PPP (0.003) suggests the model fits data significantly differently from null.
- **MMLU**: Moderate γ̂=0.66 but wide CI crossing zero — contamination signal present but not statistically significant at 95% level. PPP=0.192 is acceptable.
- **GSM8K**: γ̂≈0 (0.064) with CI firmly crossing zero — no contamination signal detected despite largest sample (N=24). ΔMAE=0.163 is large, driven by IRT calibration improving raw accuracy prediction rather than contamination adjustment. PPP=0.541 indicates excellent model fit.

## Output Files

- `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/pooled_rrf_irt_results.json`
- `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/mmlu/irt_results.json`
- `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/arc_challenge/irt_results.json`
- `/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/gsm8k/irt_results.json`
- `/root/autodl-tmp/exp003/rrf_full_3scales/exposure_scores.json`
