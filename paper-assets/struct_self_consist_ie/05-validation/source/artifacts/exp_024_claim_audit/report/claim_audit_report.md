# Claim Audit Report — struct_self_consist_ie

**Date**: 2026-05-19  
**Scope**: All quantitative claims in `docs/paper/sections/` cross-verified against experiment registry and paper_framing.md  
**Method**: Extracted every numerical claim (ρ, AUROC, F1, pp-delta, percentages), traced to source experiment, compared.

---

## ❌ Inconsistencies Requiring Fix

### 1. WNUT VC ρ inconsistency within paper (0.724 vs 0.730)

| Location | Value |
|----------|-------|
| experiments.tex:48 | VC ρ=0.724 |
| experiments.tex:104 | VC ρ=0.730 |
| appendix.tex:217 (tab:wnut) | VC .724 |
| appendix.tex:226 | VC ρ=0.724 |

**Verdict**: 0.724 is the tabulated value, used 3× consistently. The 0.730 on line 104 is a **typo**.  
**Fix**: Change experiments.tex:104 from `VC $\rho{=}0.730$` to `VC $\rho{=}0.724$`.

### 2. SciERC AUROC in Table 1 vs registry (systematic offset)

Paper Table 1 SciERC AUROC vs registry `exp_012_rerun_1024` (same ρ values, so same data):

| Signal | Paper AUC | Registry AUROC | Δ |
|--------|-----------|---------------|-----|
| VC | .663 | .684 | -2.1pp |
| SJ | .650 | .692 | -4.2pp |
| FK | .602 | .629 | -2.7pp |
| EM | .614 | .749 | **-13.5pp** |
| LP | .578 | .578 | 0pp |

ρ values match to 3 decimal places (confirming same source data), but AUROC diverges except for LP. The EM gap (0.614 vs 0.749) is extreme. CoNLL AUROC values match the registry within 1pp.

**Hypothesis**: Different AUROC binarization threshold or pipeline for SciERC. The SciERC median F1 may have tied instances handled differently.  
**Action required**: Verify which AUROC pipeline produced Table 1. If the registry values are correct, Table 1 SciERC AUROC column needs updating. This also affects:
- Abstract/Introduction "AUROC up to 0.82" → still valid (CoNLL EM 0.816 matches registry)
- But SciERC EM AUROC should be ~0.749, not 0.614

### 3. CoNLL LP selection Δ: Table 3 vs Appendix cross-selection table

| Source | Greedy | LP F1 | LP Δ |
|--------|--------|-------|------|
| Table 3 (experiments.tex:122) | .908 | — | **-0.85pp** |
| Appendix tab:cross_selection (appendix.tex:248) | .908 | .897 | **-1.1pp** |

Both claim 3-seed means, Qwen/CoNLL N=8. The Δ values (-0.85pp vs -1.1pp) are inconsistent.  
**Fix**: Reconcile these two tables. Check whether different seed combinations or averaging methods were used.

### 4. WNUT-17 zero-F1 rate inconsistency within paper

| Location | Value |
|----------|-------|
| experiments.tex:12 (dataset description) | "52% zero F1" |
| experiments.tex:103 | "51% of instances yield F1=0" |
| limitations.tex:3 | "51% F1=0" |

**Fix**: Unify to one value. If it's N=8 data, verify the exact percentage and use consistently.

---

## ⚠️ Ambiguous/Unverifiable Claims

### 5. "13–87% degeneracy" in Introduction (line 15)

The introduction says "instance degeneracy (13–87% across our benchmarks)."

- 13% ≈ FewNERD (10.1–13.1% depending on seed) ✓
- 87% = LLaMA CoNLL N=16 (registry: 86.5–86.7%) — this is a specific **model×dataset×N** configuration, not a benchmark

The appendix (line 232) confirms: "On CoNLL, 48–87% of instances produce identical outputs" — spanning Qwen N=8 (48%) to LLaMA N=16 (87%).

**Issue**: "across our benchmarks" suggests cross-dataset variation, but 87% comes from a specific model+N configuration within CoNLL. The dataset-only range is ~10–68% (FewNERD to WNUT).  
**Recommendation**: Change to "across our experimental configurations" or specify: "(13% on Few-NERD to 87% on CoNLL under LLaMA at N=16)".

### 6. CoNLL degeneracy 48.4% labeled as N=8 in Table 3

Table 3 caption: "Qwen3-8B, N=8, T=1.0". CoNLL Degen.% = 48.4%.

But `tab:degeneracy` (appendix.tex:362) shows: "CoNLL 8B (N=16)" = 48.4%.

Registry `exp_002_conll_n16` (N=16, seed 42): degen_rate = 0.4844 (48.4%).

No N=8 CoNLL degeneracy rate found in registry. With fewer samples (N=8), ALL having identical F1 is easier, so N=8 degeneracy should be **higher** than N=16's 48.4%.

**Risk**: Table 3 may be using the N=16 degeneracy value in an N=8 context.  
**Action**: Verify the N=8 CoNLL degeneracy from the actual N=8 experiment data.

### 7. FewNERD degeneracy 13.8% vs registry data

Paper Table 3: FewNERD degen = 13.8%.

Registry individual seeds (all N=8):
- Seed 42 (exp_021_fewnerd_full): 10.1%
- Seed 123: 13.1%
- Seed 456: 12.1%
- Seed 789: 11.8%

3-seed mean (42/123/456): (10.1 + 13.1 + 12.1) / 3 = **11.8%** ≠ 13.8%  
4-seed mean: (10.1 + 13.1 + 12.1 + 11.8) / 4 = **11.8%** ≠ 13.8%

**Source of 13.8% unclear.** No seed combination produces this value. Could be from a different computation or epoch checkpoint.

### 8. FewNERD LP global ρ = .220 in Table 3 vs seed 42 = 0.422

Table 3 says LP ρ = .220 (3-seed mean). Registry seed 42: lp_global_rho = 0.4215. Seed 789: lp_rho_global = 0.1788.

This implies seeds 123/456 have very low LP ρ (~0.12 each) for the 3-seed mean to be 0.22. The seed variance (0.18–0.42) is extremely high for Spearman ρ, which is unusual.

**Cannot verify** from available registry data (seeds 123/456 lack LP ρ).  
**Recommendation**: Verify the 3-seed LP ρ values and consider reporting seed-specific values to acknowledge this variance.

### 9. WNUT LP ρ: paper -0.446 vs registry -0.410

Paper Table 3: LP ρ = -.446 (claimed N=8).  
Registry exp_003_ner_wnut17 (N=16): rho_logprob_full = -0.414.  
Registry exp_003_wnut17_eval (N=16): rho_logprob_full = -0.409.

Different N values (paper N=8, registry N=16), so some difference is expected. But no N=8 WNUT data found in registry to verify.

### 10. Entity construction Δ: paper vs registry (protocol mismatch)

Paper (multi-seed mean) vs registry (5-fold CV):

| Dataset | Paper LP Δ | Registry LP Δ | Paper Unif Δ | Registry Unif Δ |
|---------|-----------|--------------|-------------|----------------|
| SciERC | +1.02pp | +1.67pp | +0.74pp | +1.12pp |
| FewNERD | +1.40pp | +0.88pp | +0.74pp | +0.32pp |
| CoNLL | -0.39pp | -0.39pp | — | — |

Large differences on SciERC and FewNERD. The paper uses "multi-seed mean±σ" (averaging results from different training seeds), while the registry uses "5-fold CV, bootstrap B=10000" (within one model). These are legitimately different evaluation protocols, so direct comparison is invalid.

**However**: The direction of difference is inconsistent — registry is higher than paper on SciERC but lower on FewNERD. This means multi-seed averaging isn't simply scaling all values down.  
**Recommendation**: Source the individual seed construction results to verify the multi-seed means match.

---

## ⚠️ Known Contradiction (from task description)

**"Discussion '+0.1pp over single-sample' vs Limitations '+0.4pp over greedy'"**

**Status**: Not found in current paper text.

The closest matches are:
- Experiments §5.5 (scaling): "LP selection fails (SciERC −0.1pp, CoNLL −0.4pp)" — these are 72B zero-shot LP selection results, different datasets, both negative. Not contradictory.
- TOST appendix table: SJ NER Δ = +0.1pp (vs single-sample) — this is in the appendix, not Discussion.
- Limitations: "LP×VC combinations yield at most +0.2pp over greedy" — 0.2pp, not 0.4pp.

**Conclusion**: The contradiction may have been resolved in the current paper version, or the task description references numbers from an earlier draft. The current paper does not contain this specific conflict.

---

## ✅ Verified Claims

### Abstract & Introduction
| Claim | Source | Registry/Verified Value | Status |
|-------|--------|------------------------|--------|
| ρ up to 0.45 | CoNLL EM | exp_002: EM rho=0.4507 → 0.45 | ✅ |
| AUROC up to 0.82 | CoNLL EM | exp_002: EM AUROC=0.8156 → 0.82 | ✅ |
| +5–8pp F1 at 80% coverage | Selective pred. | exp_selective_prediction: SciERC +5.0, CoNLL +8.4, FewNERD +6.2 | ✅ |
| LP +1.39pp on FewNERD (p<0.001) | LP selection | 4-seed mean = 1.38pp (CI [1.32, 1.44]) | ✅ (rounds) |
| SciERC LP +0.2pp, p=0.29 | Table 2 (2-seed) | 0.647 - 0.645 = 0.2pp | ✅ |
| ρ=0.052 (23 configs, p=0.81) | Degen vs LP | paper_framing confirms | ✅ |
| MBR SJ median ρ=0.524 | Discussion | tab:degeneracy: 0.524 | ✅ |

### Table 1 (QE) — Spearman ρ
| Signal | Paper | Registry (exp_012_rerun_1024) | Status |
|--------|-------|-------------------------------|--------|
| SciERC VC ρ | .379 | 0.3792 | ✅ |
| SciERC SJ ρ | .360 | 0.3599 | ✅ |
| SciERC FK ρ | .267 | 0.2665 | ✅ |
| SciERC EM ρ | .295 | 0.2945 | ✅ |
| SciERC LP ρ | .205 | 0.2052 | ✅ |
| CoNLL SJ ρ | .436 | exp_002: 0.4357 | ✅ |
| CoNLL EM ρ | .451 | exp_002: 0.4507 | ✅ |
| CoNLL LP ρ | .316 | exp_002: 0.3157 | ✅ |

### Table 2 (SciERC Selection)
| Method | Paper | Notes | Status |
|--------|-------|-------|--------|
| Oracle | .775±.001 | exp_012_rerun_1024: oracle F1=0.7758 (framing) | ✅ |
| Greedy | .645±.001 | Consistent with framing 0.6439/0.6442 | ✅ |
| LP | .647±.005 | 2-seed mean | ✅ |
| Random | .610±.003 | exp_016_rerun_1024 framing: 0.6077 | ✅ |

### Table 3 (Cross-dataset)
| Dataset | Greedy | Degen | LP ρ | LP Δ | Status |
|---------|--------|-------|------|------|--------|
| SciERC | .644 | 17.8% | .205 | +0.61pp | ✅ all match single-seed exp_012 |
| FewNERD | .748 | 13.8% | .220 | +1.39pp | ⚠️ degen 13.8% unverifiable; LP ρ unverifiable |
| CoNLL | .908 | 48.4% | .302 | -0.85pp | ⚠️ degen might be N=16; LP Δ conflicts with appendix |
| WNUT | .452 | 67.9% | -.446 | -0.45pp | ⚠️ LP ρ unverifiable at N=8 |

### Scale Ablation (Table in experiments.tex)
| Metric | Paper | Registry | Status |
|--------|-------|----------|--------|
| CoNLL 8B SJ ρ | .436 | exp_002: 0.4357 | ✅ |
| CoNLL 4B SJ ρ | .422 | exp_qwen3_4b_conll: 0.4217 | ✅ |
| SciERC 8B SJ ρ | .360 | exp_012_rerun_1024: 0.3599 | ✅ |
| SciERC 4B SJ ρ | .422 | exp_qwen3_4b_scierc: 0.4221 | ✅ |
| SciERC 8B degen | 17.8% | 0.1777 | ✅ |
| SciERC 4B degen | 10.4% | 0.104 | ✅ |

### 72B Zero-shot (Table in experiments.tex)
| Metric | Paper | Source | Status |
|--------|-------|--------|--------|
| SciERC 72B LP ρ | .081 | paper_framing: 0.081 | ✅ |
| CoNLL 72B LP ρ | -.002 | paper_framing: -0.002 | ✅ |
| SciERC 72B constr. +1.5pp | +1.5pp | paper_framing: +1.53pp | ✅ (rounded) |
| CoNLL 72B constr. -0.37pp | -0.37pp | paper_framing: -0.37pp | ✅ |

Note: 72B experiment is still RUNNING in registry — no final metrics to cross-verify. Paper values sourced from framing doc only.

### LoRA Rank Ablation
| Metric | Paper | Registry (exp_023_lora_rank8) | Status |
|--------|-------|-------------------------------|--------|
| Rank=8 degen | 7.2% | 0.072 | ✅ |
| VC ρ | .394 (text) | 0.394 | ✅ |
| SJ ρ | .365 (text) | 0.3649 | ✅ |

### Other Verified Claims
| Claim | Source | Status |
|-------|--------|--------|
| T=1.2 degen 14.9% | exp_026_t12: 0.1493 | ✅ |
| Non-tied LP +2.9pp | Discussion | ✅ (p-value differs: paper 0.004 vs framing 0.01 — check which is post-correction) |
| Bootstrap CI [-3.0, +4.2]pp | exp_016_rerun_1024_bootstrap: [-0.030, 0.042] | ✅ |
| Cohen's d = 0.038 | exp_016_rerun_1024_bootstrap: 0.038 | ✅ |
| Freeform std ratio 0.97 | exp_freeform_ablation: 0.97 | ✅ |
| Parse rate 99.95% | exp_freeform_ablation: 0.9995 | ✅ |
| FewNERD LP CI [1.02, 1.34] paper vs [1.18, 1.53] registry | Abstract says [1.02, 1.34]; registry says [1.18, 1.53] | ⚠️ see below |

### Abstract LP CI discrepancy
Abstract line 7: "p<0.005" (Table 5 shows p=.004 for SciERC and p<.001 for FewNERD — both < 0.005). The "(multi-seed mean, p<0.005)" applies to the joint claim. ✅

But the **bootstrap CI** for FewNERD LP selection:
- Abstract: implied from "p<0.005"
- Registry exp_021_fewnerd_full: lp_bootstrap_ci_95_pp = [1.18, 1.53]
- Paper Table 3: not shown explicitly
- Paper framing: LP selection CI [+1.02, +1.34] (for the 4-seed mean)

The CI [1.02, 1.34] (framing) vs [1.18, 1.53] (registry) represent different computations: framing uses 4-seed bootstrap of means, registry uses single-seed bootstrap. Not an error, but worth documenting.

---

## Summary of Required Actions

| Priority | Issue | Action |
|----------|-------|--------|
| **P0** | ❌ WNUT VC ρ typo (0.730 → 0.724) | Fix experiments.tex:104 |
| **P0** | ❌ SciERC AUROC pipeline discrepancy | Verify Table 1 AUROC computation; if registry is correct, update table |
| **P0** | ❌ CoNLL LP Δ mismatch (-0.85 vs -1.1pp) | Reconcile Table 3 and Appendix cross-selection table |
| **P0** | ❌ WNUT zero-F1 rate (51% vs 52%) | Unify within paper |
| **P1** | ⚠️ "13–87%" in intro | Change to "across configurations" or give dataset-specific range |
| **P1** | ⚠️ CoNLL degen 48.4% N=8 vs N=16 | Verify the N=8 value |
| **P1** | ⚠️ FewNERD degen 13.8% source | Document or correct |
| **P2** | ⚠️ FewNERD LP ρ seed variance | Consider reporting seed-level values |
| **P2** | ⚠️ Non-tied LP p-value (0.004 vs 0.01) | Verify: one is pre-correction, one post? |
| **INFO** | Known contradiction from task | Not found in current version; appears resolved |
