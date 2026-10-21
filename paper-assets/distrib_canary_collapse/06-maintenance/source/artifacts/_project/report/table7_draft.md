# Table 7: Complete Lead-Lag Detection Results

> Generated: 2026-05-19. Data sources: `5method_leadlag.json` (on-disk analysis) + registry metrics.
> All fractions are X/8 (8 canary-diversity pairs: {token_entropy, ece} × {distinct_1, distinct_2, distinct_3, effective_rank}).
> Constraint C003: TY values at α≤0.50 are seed-unstable and should NOT be cited as supporting evidence.

## A. Main Axis: Pythia-410M, WikiText-103, fp32

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| a000_s42 | Pythia-410M | Wiki-103 | 0.00 | 42 | fp32 | 8/8 | 4/8 | 3/8 | 0/8 | 1/8 | 1/8 | 1/8 | — | Null control |
| a000_s43 | Pythia-410M | Wiki-103 | 0.00 | 43 | fp32 | 7/8 | 3/8 | 1/8 | 0/8 | 0/8 | 1/8 | 0/8 | — | Null control |
| a000_s44 | Pythia-410M | Wiki-103 | 0.00 | 44 | fp32 | 8/8 | 3/8 | 1/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Null control |
| a010_s43 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | 7/8 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Canary blind zone (D075) |
| a025_s42_v3 | Pythia-410M | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |
| a025_s43 | Pythia-410M | Wiki-103 | 0.25 | 43 | fp32 | 8/8 | 3/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Sub-threshold regime |
| a025_s44 | Pythia-410M | Wiki-103 | 0.25 | 44 | fp32 | 8/8 | 1/8 | 0/8 | 0/8 | 0/8 | 2/8 | 0/8 | — | Sub-threshold; TY unstable (C003) |
| a050_s42 | Pythia-410M | Wiki-103 | 0.50 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | — | Threshold boundary |
| a050_s43 | Pythia-410M | Wiki-103 | 0.50 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 0/8 | 1/8 | — | PermG emerges in s43 only |
| a050_s44 | Pythia-410M | Wiki-103 | 0.50 | 44 | fp32 | 8/8 | 6/8 | 0/8 | 3/8 | 0/8 | 0/8 | 0/8 | — | PermG partial |
| a075_s42 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | 8/8 | 8/8 | 4/8 | 8/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |
| a075_s43 | Pythia-410M | Wiki-103 | 0.75 | 43 | fp32 | 8/8 | 8/8 | 0/8 | 5/8 | 0/8 | 1/8 | 4/8 | — | Confirmatory regime |
| a075_s44 | Pythia-410M | Wiki-103 | 0.75 | 44 | fp32 | 8/8 | 8/8 | 4/8 | 6/8 | 0/8 | 1/8 | 5/8 | — | Confirmatory regime |
| a100_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 0/8 | 2/8 | 2/8 | — | Full contamination (generalize_pythia410m) |
| mvp_v4_rep42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |
| mvp_v4_rep43 | Pythia-410M | Wiki-103 | 1.00 | 43 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |
| mvp_v4_rep44 | Pythia-410M | Wiki-103 | 1.00 | 44 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |
| mvp_v4_rep45 | Pythia-410M | Wiki-103 | 1.00 | 45 | fp32 | — | — | — | — | — | — | — | — | Early MVP; no 5method analysis |

## B. Cross-Architecture: WikiText-103, α=1.00, fp32

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| gen_wiki_gpt2m_a100_s42_v4 | GPT-2-Medium | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 0/8 | 6/8 | 3/8 | 2/8 | 2/8 | — | 5method on disk; rev=3/8 from ECE pairs |
| gen_wiki_gpt2m_a025_s42 | GPT-2-Medium | Wiki-103 | 0.25 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |
| generalize_opt1b_wiki_a100_s42 | OPT-1.3B | Wiki-103 | 1.00 | 42 | fp32 | 8/8 | 8/8 | 1/8 | 6/8 | 0/8 | 0/8 | 2/8 | — | |
| generalize_pythia14b_wiki_a100_s42 | Pythia-1.4B | Wiki-103 | 1.00 | 42 | fp32 | 7/8 | 6/8 | 0/8 | 2/8 | 0/8 | 0/8 | 1/8 | — | Low PermG; seed variance? |
| generalize_pythia14b_wiki_a100_s43 | Pythia-1.4B | Wiki-103 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 0/8 | 2/8 | 6/8 | — | Strong confirmation vs s42 |

## C. Cross-Dataset: C4

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| generalize_pythia1b_c4_a100_s42_v2 | Pythia-1B | C4 | 1.00 | 42 | fp32 | 8/8 | 6/8 | 0/8 | 6/8 | 3/8 | 1/8 | 2/8 | — | rev=3/8 from ECE-diversity bidirectional coupling |
| generalize_pythia1b_c4_a100_s43 | Pythia-1B | C4 | 1.00 | 43 | fp32 | 8/8 | 6/8 | 0/8 | 4/8 | 0/8 | 2/8 | 3/8 | — | |
| alpha_sweep_c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | Registry only: permg_fwd=0/8; **bf16 caveat** |

## D. Scale

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| scale_14b_a050_s42 | Pythia-1.4B | Wiki-103 | 0.50 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis on disk |

## E. Intervention: Pythia-410M, WikiText-103, α=1.00

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| intervention_predictive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; canary-triggered at Gen 1 |
| intervention_reactive_s42 | Pythia-410M | Wiki-103 | 1.00 | 42 | fp32 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis; downstream-triggered |

## F. Supplementary: bf16 Experiments

| Condition | Model | Dataset | α | Seeds | Precision | Naive | Diff | Thresh | PermG_fwd | PermG_rev | TY | K≥4 | MMCT_wt | Notes |
|-----------|-------|---------|---|-------|-----------|-------|------|--------|-----------|-----------|-----|------|---------|-------|
| a060_s42_bf16 | Pythia-410M | Wiki-103 | 0.60 | 42 | bf16 | 8/8 | 8/8 | 6/8 | 8/8 | 0/8 | 0/8 | 6/8 | 6/8 | Registry unified_2sigma; 5method shows thresh=0, K4=1 (different threshold) |
| c4_a050_s42_bf16 | Pythia-410M | C4 | 0.50 | 42 | bf16 | — | — | — | 0/8 | 0/8 | — | — | — | (same as Section C row) |
| gen_gpt2m_a100_s43_bf16 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | bf16 | 8/8 | — | 8/8 | — | — | — | 1/8 | 6/8 | Registry only (n_perm=5000) |
| interv_pred_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |
| interv_react_s43_bf16 | Pythia-410M | Wiki-103 | 1.00 | 43 | bf16 | — | — | — | — | — | — | — | — | **GAP**: no lead-lag analysis |

## G. Analysis-Only Experiments (no individual training runs)

These experiments analyze existing data across multiple conditions and do not have per-condition lead-lag metrics:

| Condition | Description | Key Findings |
|-----------|-------------|--------------|
| method_ablation_phase1 | 16-pair method comparison | naive_sig=16/16, threshold=9/16, permG=6/16 |
| method_ablation_phase2 | FDR correction impact | PermG FDR sig: α=0.00→0%, α=0.25→0%, α=0.50→0%, α=1.00→75% |
| method_ablation_phase3 | Step-change analysis | PermG: 0% (α≤0.50) → 100% (α=0.60) → 83% (α=0.75) |
| conditional_granger_d061 | Conditional Granger controlling ECE/entropy | Independent canary signals confirmed |
| plan_009_bootstrap_ty | Bootstrap TY analysis | TY instability confirmed (basis for C003) |

## H. Pending (RUNNING Experiments)

| Condition | Model | Dataset | α | Seed | Precision | Status |
|-----------|-------|---------|---|------|-----------|--------|
| alpha_sweep_a005_s42_v3 | Pythia-410M | Wiki-103 | 0.05 | 42 | fp32 | RUNNING (D080 fix) |
| alpha_sweep_a010_s43_fp32 | Pythia-410M | Wiki-103 | 0.10 | 43 | fp32 | RUNNING (fp32 re-run) |
| alpha_sweep_a060_s42_fp32_v3 | Pythia-410M | Wiki-103 | 0.60 | 42 | fp32 | RUNNING (D080 fix, replaces bf16) |
| interv_pred_a075_s42_fp32_v4 | Pythia-410M | Wiki-103 | 0.75 | 42 | fp32 | RUNNING (D080 fix) |
| gen_gpt2m_a100_s43_fp32 | GPT-2-Medium | Wiki-103 | 1.00 | 43 | fp32 | RUNNING (replaces bf16 version) |
| qwen35_08b_wiki_a100_s42_v2 | Qwen3.5-0.8B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |
| smollm3_3b_wiki_a100_s42_v3 | SmolLM3-3B | Wiki-103 | 1.00 | 42 | fp32 | RUNNING (new architecture) |
| scale_69b_a100_s42 | Pythia-6.9B | Wiki-103 | 1.00 | 42 | bf16 | RUNNING (scale-up) |

---

## Coverage Summary

### Completed conditions with lead-lag analysis: 19/39

| Category | With lead-lag | Without lead-lag | Total |
|----------|--------------|-----------------|-------|
| Main axis (Pythia-410M, Wiki, fp32) | 13 | 5 (a025_s42, mvp×4) | 18 |
| Cross-architecture (fp32) | 4 | 1 (gpt2m_a025) | 5 |
| Cross-dataset (C4) | 2 | 1 (c4_a050 bf16, partial) | 3 |
| Scale | 0 | 1 (scale_14b) | 1 |
| Intervention | 0 | 4 | 4 |
| Analysis-only | N/A | N/A | 5 |
| bf16 supplementary | 2 | 1 (partial) | 3 |

### Precision distribution
- **fp32**: 28 experiments (20 main/cross-arch, 4 intervention, 4 mvp)
- **bf16**: 5 experiments (a060, c4_a050, gpt2m_s43, interv_pred_s43, interv_react_s43)
- **fp32 pending**: 6 of 8 RUNNING experiments are D080 fp32 re-runs

### Seed coverage (Main axis, Pythia-410M, Wiki-103, fp32)
| α | s42 | s43 | s44 | s45 |
|---|-----|-----|-----|-----|
| 0.00 | ✓ | ✓ | ✓ | — |
| 0.05 | pending | — | — | — |
| 0.10 | — | ✓ (+ fp32 pending) | — | — |
| 0.25 | **GAP** (no analysis) | ✓ | ✓ | — |
| 0.50 | ✓ | ✓ | ✓ | — |
| 0.60 | bf16 only (fp32 pending) | — | — | — |
| 0.75 | ✓ | ✓ | ✓ | — |
| 1.00 | ✓ | mvp (no analysis) | mvp (no analysis) | mvp (no analysis) |

## Identified Gaps

### Critical (blocks Table 7 completeness):
1. **α=0.25, s42**: `alpha_sweep_a025_s42_v3` has no 5method_leadlag.json. Need to run analysis.
2. **α=1.00 multi-seed**: mvp_v4_rep42-45 lack lead-lag analysis. Need to run 5method on mvp data or use generalize_pythia410m_wiki_a100_s42 as the canonical α=1.00 row.
3. **Intervention experiments**: All 4 (predictive/reactive × s42/s43) lack lead-lag analysis. These need different analysis since intervention changes α mid-run.
4. **scale_14b_a050_s42**: No lead-lag analysis on disk.
5. **α=0.10, s42**: No success experiment in registry (only s43).

### Medium priority:
6. **GPT-2-Medium α=0.25 s42**: `gen_wiki_gpt2m_a025_s42` has no lead-lag analysis.
7. **MMCT coverage**: Only a060_bf16 (6/8) and gen_gpt2m_s43_bf16 (6/8) have MMCT data. All other experiments lack MMCT.
8. **α=0.60 fp32**: Currently only bf16 version completed. fp32 version RUNNING.
9. **α=0.05**: No completed experiment. RUNNING.

### Low priority:
10. **gen_wiki_gpt2m_a100_s42_v3 vs v4**: Duplicate entries for same data. v4 is canonical.
11. **Pythia-1.4B s42 weak signal**: PermG=2/8, K4=1/8 vs s43's 6/8, 6/8. Seed variance or anomaly?
