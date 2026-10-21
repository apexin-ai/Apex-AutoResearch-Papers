# Paper–Registry Consistency Audit

**Date**: 2026-05-16
**Paper location**: `artifacts/_project/paper/*.tex`
**Registry**: `distrib_canary_collapse` (34 experiments)

---

## ❌ Critical Discrepancies

### 1. Table 1 (tab:drift_summary) — α=1.0 row: 4-seed mean±std values are wrong

The α=1.0 row reports 4-seed mean±std, but the values do not match the registry data from `mvp_v4_rep42/43/44/45`.

| Metric | Paper | Registry (computed) | Δ mean | Δ std |
|--------|-------|-------------------|--------|-------|
| Entropy drift (%) | −60.5±1.2 | −60.8±1.2 | 0.3 (minor) | OK |
| ECE drift (%) | **+3862±158** | **+3780±30** | **82** | **128** |
| Distinct-1 drift (%) | **−25.3±1.3** | **−27.8±1.6** | **2.5** | 0.3 |
| Distinct-2 drift (%) | **−29.7±1.5** | **−34.0±3.3** | **4.3** | **1.8** |
| Perplexity drift (%) | +3690±320 | +3674±45 | 16 (minor) | **275** |

**Registry source values** (drift_pct from each seed):

| Seed | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity |
|------|---------|-----|-----------|-----------|-----------|
| 42 | −60.55 | +3762.5 | −28.34 | −35.21 | +3624.6 |
| 43 | −61.05 | +3782.6 | −28.42 | −35.76 | +3665.1 |
| 44 | −62.26 | +3821.2 | −25.47 | −29.13 | +3733.8 |
| 45 | −59.33 | +3755.1 | −29.13 | −35.96 | +3670.9 |

**Impact**: This table is referenced by the experiments section (§4.2 Regime-Dependent Detectability). The qualitative conclusions are unaffected (direction and ordering preserved), but the exact numbers are wrong. ECE std is off by 5×, perplexity std by 7×.

**Note**: All single-seed rows (α=0.0, 0.25, 0.50, 0.75) are perfectly consistent with registry — only the α=1.0 aggregated row has errors.

---

## ⚠️ Moderate Issues

### 2. Discussion claims GPT-2-medium results "not yet available" — but registry shows completed experiment

**Paper** (discussion.tex, line 15):
> "Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available."

**Registry**: `gen_wiki_gpt2m_a100_s42_v3` — status=DONE, conclusion=success (completed 2026-05-15T22:18). Full metrics available:
- token_entropy_drift: −86.5%
- ece_drift: +4543%
- perplexity_drift: +44703%
- five_method_forward_consensus: "6/6 pairs at 4/5 methods (Tier 3)"
- perm_granger_forward: p_fdr=0.003, BH corrected
- diff_xcorr_reverse: "all p>0.18 (clean directional separation)"
- cross_arch_note: "Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus"

**Impact**: The paper could be strengthened with cross-architecture validation data. Currently understates available evidence.

### 3. Multi-seed data now partially available for α=0.25 and α=0.50

**Paper** (experiments.tex, line 14):
> "other conditions use seed 42, with multi-seed replication in progress"

**Registry**:
- α=0.25: seed 42 (done), seed 43 (done), seed 44 (running)
- α=0.50: seed 42 (done), seed 43 (done)

The α=0.50 s43 results (drift_pct) closely match s42: ppl 21.1 vs 21.1, entropy −17.4 vs −18.6, d1 −36.5 vs −37.3. Cross-seed note: "drift direction identical, magnitude <7% deviation."

**Impact**: Could update the paper to report α=0.50 as 2-seed replicated. Minor because the paper already correctly hedges with "in progress."

---

## ✅ Verified Consistent

### Drift table — single-seed rows (all 5 metrics match exactly)

| α | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity | Source |
|---|---------|-----|-----------|-----------|-----------|--------|
| 0.00 | −5.1 ✅ | +51.7 ✅ | −13.8 ✅ | −9.8 ✅ | −21.7 ✅ | alpha_sweep_a000_s42 |
| 0.25 | −4.1 ✅ | +79.7 ✅ | −40.3 ✅ | −57.1 ✅ | −17.2 ✅ | alpha_sweep_a025_s42_v3 |
| 0.50 | −18.6 ✅ | +842.8 ✅ | −37.3 ✅ | −51.5 ✅ | +21.1 ✅ | alpha_sweep_a050_s42 |
| 0.75 | −27.7 ✅ | +1809.5 ✅ | −32.7 ✅ | −41.3 ✅ | +182.1 ✅ | alpha_sweep_a075_s42 |

### Method ablation sig rates (method_ablation_phase1)

| Method | Paper | Registry | Status |
|--------|-------|----------|--------|
| Naive XCorr | 16/16 (100%) | naive_sig=16/16 | ✅ |
| Differenced XCorr | 14/16 (87.5%) | differenced_sig=14/16 | ✅ |
| Threshold Onset | 9/16 (56.3%) | threshold_sig=9/16 | ✅ |
| Perm. Granger | 6/16 (37.5%) | permutation_granger_sig=6/16 | ✅ |
| Toda–Yamamoto | 4/16 (25.0%) | ty_sig=4/16 | ✅ |

### Spurious-signal rates

- 75% (5-method) — registry: spurious_rate_5method=0.75 ✅
- 62.5% (4-method, excl. TY) — registry: spurious_rate_4method=0.625 ✅

### Inter-method agreement

- κ = 0.185 — registry: mean_inter_method_kappa=0.185 ✅

### α=0.75 Granger p-values (alpha_sweep_a075_s42)

| Pair | Paper | Registry | Status |
|------|-------|----------|--------|
| ECE→d1 | p_fdr=0.046 | granger_ece_to_d1_p_fdr=0.046 | ✅ |
| ECE→d2 | p_fdr=0.046 | granger_ece_to_d2_p_fdr=0.046 | ✅ |
| Entropy→d2 | p_fdr=0.048 | granger_entropy_to_d2_p_fdr=0.048 | ✅ |
| Entropy→d1 | p_fdr=0.054 (borderline) | granger_entropy_to_d1_p_fdr=0.054 | ✅ |

### α=0.75 Granger sig count

- "3/8 FDR-sig" — registry: granger_fdr_sig_count="3/8" ✅

### Cross-α Perm. Granger sig rates (method_ablation_phase2)

| α | Paper (Table 3) | Registry | Status |
|---|-----------------|----------|--------|
| 0.00 | 0% | perm_granger_sig_rate_a000_fdr=0 | ✅ |
| 0.25 | 0% | perm_granger_sig_rate_a025_fdr=0 | ✅ |
| 0.50 | 0% | perm_granger_sig_rate_a050_fdr=0 | ✅ |
| 1.00 | 75% | perm_granger_sig_rate_a100_fdr=0.75 | ✅ |

### Cross-α TY sig rates (method_ablation_phase2)

| α | Paper (Table 3) | Registry | Status |
|---|-----------------|----------|--------|
| 0.00 | 0% | TY_sig_rate_a000_fdr=0 | ✅ |
| 0.25 | 37.5% | TY_sig_rate_a025_fdr=0.375 | ✅ |
| 0.50 | 0% | TY_sig_rate_a050_fdr=0 | ✅ |
| 1.00 | 59.4% | TY_sig_rate_a100_fdr=0.5938 | ✅ |

### Diff. XCorr at α=0.0

- Paper: 37.5% — registry: diff_sig_rate_a000_fdr=0.375 ✅

### FPR/FNR table (tab:fpr_fnr)

| Criterion | Paper FPR | Paper FNR | Status |
|-----------|-----------|-----------|--------|
| Naive XCorr | 100% | 0% | ✅ consistent with phase2 |
| Diff. XCorr | 37.5% | 0% | ✅ |
| Threshold | 62.5% | 0% | ✅ |
| Perm. Granger | 0% | 0% | ✅ |
| TY | 0% | 33.3% | ✅ consistent with text |
| Consensus K≥4/5 | 0% | 0% | ✅ |
| Consensus K≥4/5, S≥3/4 | 0% | 0% | ✅ |

### Practical guidance tiers (tab:practical_guidance)

- Tier 1 FPR=100%: verified (naive alone flags all) ✅
- Tier 3 FPR=0%, FNR=0%: verified ✅
- Tier 4 FNR=50%: consistent with calibration text (K=5/5, S=4/4) ✅

### Bootstrap TY power (plan_009_bootstrap_ty)

- Paper: "power of 0.05–0.20" — registry: T10 power range 0.05–0.205 ✅

### Experimental setup parameters

| Parameter | Paper | Registry | Status |
|-----------|-------|----------|--------|
| Model | Pythia-410M | EleutherAI/pythia-410m | ✅ |
| Data | WikiText-103 | data/wikitext103_5k | ✅ |
| Samples/gen | 5,000 | data_count=5000 | ✅ |
| Steps/gen | 5,000 | steps_per_gen=5000 | ✅ |
| Generations | T=10 | num_generations=10 | ✅ |
| α levels | {0.0, 0.25, 0.50, 0.75, 1.0} | all present | ✅ |
| Seeds (α=1.0) | {42, 43, 44, 45} | 4 mvp_v4 experiments | ✅ |
| Permutations | 5,000 | stated in paper | ✅ |

### Pipeline filtering counts

- Stage 1: 16 → Stage 2: 14 → Stage 3: 6 → Stage 4: 6 ✅
  (Matches naive=16/16, diff=14/16, perm_granger=6/16)

### Consensus counts in abstract/conclusion

- 24/24 canary→diversity sig at α=1.0 (6 pairs × 4 seeds) ✅
- 0/24 reverse-direction ✅ (consistent throughout paper)
- 8/8 → 0/8 perplexity leads eliminated by differencing ✅

---

## ❓ Cannot Verify from Registry

These numbers appear in the paper but have no direct registry field to check against. They require access to the raw analysis output files on the server.

- |r| > 0.99 for Pythia α=1.0 cross-correlation
- All reverse-direction p > 0.49 (Pythia)
- F = 16–36 for undifferenced canary→perplexity
- F ≈ 0, p = 0.99 for differenced canary→perplexity
- TY d_max sensitivity: 6%, 75%, 94% rejection rates
- Table 3 entries: Diff. XCorr at α=0.25 (25%), Threshold at α=0.25 (37.5%)
- FPR at K=2 (75%), K=3 (37.5%)
- Pythia batch size = 4 (mentioned in discussion limitations)

---

## Summary

| Category | Count | Details |
|----------|-------|---------|
| ❌ Critical | 1 | Table 1 α=1.0 row: mean±std values for ECE, d1, d2, ppl are wrong |
| ⚠️ Moderate | 2 | GPT-2m results available but paper says "not yet"; multi-seed data partially available |
| ✅ Verified | 40+ | All single-seed drifts, method ablation rates, p-values, κ, sig counts, FPR/FNR |
| ❓ Unverifiable | 8 | Require raw analysis files on server |

**Recommended action**: Fix Table 1 α=1.0 row using registry source data. Consider incorporating GPT-2-medium cross-architecture validation results into the discussion.
