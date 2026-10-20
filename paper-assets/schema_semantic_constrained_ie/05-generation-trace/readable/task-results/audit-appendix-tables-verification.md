# audit appendix tables verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix-tables-verification_20260523T104322_result.json`
- **Structured JSON:** [`e0b227803ceedcd97404.json`](../../sessions/e0/e0b227803ceedcd97404.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed for a comprehensive audit. Here is the full report:

---

# Appendix Table Audit Report

## Summary

Audited **25 appendix files** containing **~30 tables** against 164 registry experiments. The vast majority of values are verified correct. One systematic issue affects multiple tables: **the parse-failure bug** (same as known Table 2 issue) impacts DocRED FT values in several appendix tables.

---

## VERIFIED CORRECT ✅

### tab:quantization (appendix_quantization.tex)
All 18 data cells verified against 7 registry experiments:
- `sf2_qwen_int4_scierc_s1`: DR=0, R-F1=41.71, E-F1=67.05 ✅
- `sf2_llama_int4_scierc_s1`: DR=0, R-F1=43.98, E-F1=67.54 ✅
- `sf2_qwen_int4_docred_s1`: DR=0, R-F1=40.07, E-F1=74.84, PF=18.5% ✅
- `sf2_llama_int4_docred_s1`: DR=0, R-F1=48.04, E-F1=84.18, PF=2.5% ✅
- `entity_order_ablation_qwen_scierc` (FP16 Qwen SciERC): DR=0, R-F1=43.77, E-F1=67.05 ✅
- `d065_qwen_greedy_4096_r2` (FP16 Qwen DocRED): DR=0, R-F1=40.79, E-F1=81.87, PF=8.5% ✅
- `w5_llama_lora_scierc_constrained_eval` (FP16 Llama SciERC): DR=0.09, R-F1=45.47, E-F1=67.76 ✅
- `d066_sweep_llama_docred_beam1_s1` (FP16 Llama DocRED): DR=0, R-F1=47.35, E-F1=85.43, PF=2.0% ✅

Δ columns all arithmetically correct. ✅

### tab:70b-ft-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_scierc_*`:
- Unconstrained: DR=1.50, R-F1=44.73, E-F1=64.86 ✅
- Grammar: DR=1.50, R-F1=44.63, E-F1=64.82 ✅
- Semantic: DR=0.60, CF=9, R-F1=44.73, E-F1=64.86 ✅
- S1: DR=0, CF=15, R-F1=44.53, E-F1=64.76 ✅
- S2: DR=0, CF=18, R-F1=36.28, E-F1=62.35 ✅
- Beam4 S1: DR=0, CF=1, R-F1=44.81, E-F1=64.89 ✅

### tab:70b-docred-ablation (appendix_70b_ablation.tex)
All 6 rows verified against `eval_70b_lora_docred_200_*`:
- Unconstrained: DR=0.22, RV=0.57, R-F1=43.80, E-F1=80.34 ✅
- Grammar: DR=0.38, R-F1=43.96 ✅
- Semantic: DR=0, RV=0.51, R-F1=43.61 ✅
- S1: DR=0, CF=0.18%, R-F1=43.95, E-F1=79.38 ✅
- S2: DR=0, CF=0.34%, R-F1=36.45, E-F1=84.96 ✅
- Beam4 S1: DR=0, CF=0, R-F1=48.14, E-F1=85.57 ✅

### tab:70b-docred-zs-ablation (appendix_70b_ablation.tex)
All 4 rows verified against `eval_70b_zs_docred_200_*`:
- Unconstrained: DR=13.45, RV=7.88, R-F1=13.25, E-F1=70.14 ✅
- Grammar: DR=17.03, R-F1=13.23, E-F1=70.12 ✅
- Semantic: DR=1.66, RV=8.24, ET=0.12, CF=132, R-F1=13.05, E-F1=70.10 ✅
- S1: DR=0, CF=173, R-F1=13.25, E-F1=70.05 ✅

### tab:cross-model (appendix_zs_crossmodel.tex)
All 12 rows (3 models × 2 datasets × U/S1) verified. Every DR, RV, ET, CF, R-F1 value matches. ✅

### tab:docred-ablation (appendix_discussion.tex — ZS 4-way)
All 4 rows verified against `phase2_docred_*`. All violation rates, F1, and Δ values match. ✅

### tab:beam-ablation (appendix_beam_search.tex)
All 4 rows (k=1,2,4,8) verified:
- k=1: DR=0.93, CF=9.90, E-F1=30.98, R-F1=8.36 ✅
- k=2: DR=0.35, CF=4.12, E-F1=31.54, R-F1=8.75 ✅
- k=4: DR=0, CF=0.53, E-F1=32.00, R-F1=8.56 ✅
- k=8: DR=0, CF=0.08, E-F1=32.18, R-F1=8.39 ✅

### tab:beam-sweep (appendix_beam_search.tex)
All 8 rows (4 beam widths × unc/con) verified against `d066_beam_sweep`. All F1, DR, CF, latency, and relative latency values match. ✅

### tab:beam-docred-998-zs (appendix_beam_search.tex)
Both rows verified against `r14_*_docred_beam4_998`:
- Qwen: DR=0, CF=4.94, E-F1=58.19, R-F1=8.72 ✅
- Llama: DR=0, CF=1.00, E-F1=57.81, R-F1=8.83 ✅

### tab:beam-latency (appendix_beam_search.tex)
All 4 rows verified against `d062_beam_latency`:
- Greedy unc: 2.612 s/doc, 1.00× ✅
- Greedy con: 2.873, 1.10× ✅
- Beam-4 unc: 3.446, 1.32× ✅
- Beam-4 con: 4.013, 1.54× ✅

### tab:gollie-comparison (appendix_gollie_comparison.tex)
All 3 rows verified against `sf2_gollie_scierc_violation`. ✅

### tab:wikievents (appendix_wikievents_pilot.tex)
All 9 rows (3 models × 3 modes) verified against `ee_*_wikievents_*_v3`. ✅

### tab:tcr-scierc and tab:tcr-docred (appendix_tcr.tex)
All 10 TCR configurations verified against `d065_tcr_pilot`. ✅

### tab:prompt-sensitivity (appendix_prompt_sensitivity.tex)
All 6 rows verified against `r4_prompt_minimal`, `r4_prompt_detailed`, and `phase2_scierc_*`. ✅

### tab:vllm-verification (appendix_discussion.tex)
Both rows verified: Grammar-Only DR=14.84 ✅; vLLM DR=15.26, R-F1=8.75 ✅

### tab:trie-baseline (appendix_discussion.tex)
All 4 rows verified against `r16_trie_*_scierc`. Uses corrected values. ✅

### tab:scalability (appendix_scalability.tex)
All 4 rows verified against `d062_ontology_scalability`. ✅

### tab:cf-dr-tradeoff (appendix_discussion.tex)
Verified against `w1_cf_fallback_scierc_pilot`: DR=14.78%, CF=0.04% ✅

### tab:sampling-robustness (appendix_sampling_table.tex)
SciERC row verified against `w9_qwen_scierc_zs_sampling`. ✅

### Other discussion tables
tab:causal-tracing, tab:cf-distribution, tab:cascade-breakdown, tab:lora-per-relation, tab:lucky-violations, tab:lucky-violations-detail, tab:posthoc-extended (ZS rows), tab:power-analysis, tab:high-kappa-rels, tab:dr-by-ambiguity, tab:doc-length-*, tab:kappa-case-study, tab:gcd-comparison: Source experiments exist in registry with matching violation rates where verifiable. Statistical computation tables (bootstrap CI, power analysis) cannot be verified from raw metrics but source experiments are confirmed correct.

---

## DISCREPANCIES FOUND ❌

### 1. tab:ft-ablation DocRED rows — PARSE-FAILURE BUG (CRITICAL)

Same issue as known Table 2 bug. The DocRED FT rows use pre-correction values from buggy `unified_f1_eval.py`. Registry was corrected on 2026-05-22 with `eval_d064.py`, but paper wasn't fully updated.

**Qwen DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained R-F1 | 40.89 | 40.86 | -0.03 |
| Unconstrained E-F1 | 82.35 | 82.15 | -0.20 |
| Unconstrained DR | 0.56 | 0.76 | +0.20 |
| Semantic R-F1 | 40.89 | 40.85 | -0.04 |
| Grammar R-F1 | 40.85 | 40.85 | 0 ✅ (already corrected) |
| S1 R-F1 | 40.79 | 40.79 | 0 ✅ (from d065) |

**Llama DocRED:**

| Cell | Paper | Registry (corrected) | Δ |
|------|-------|---------------------|---|
| Unconstrained E-F1 | 84.77 | 83.93 | -0.84 |
| Unconstrained R-F1 | 44.55 | 43.72 | -0.83 |
| Grammar R-F1 | 43.77 | 43.72 | -0.05 |
| Semantic R-F1 | 43.90 | 43.85 | -0.05 |
| S1 E-F1 | 84.71 | 83.94 | -0.77 |
| S1 R-F1 | 44.70 | 43.78 | -0.92 |

Note: Qwen Grammar was correctly updated. Qwen S1 uses `d065_qwen_greedy_4096_r2` (inherently correct). All other DocRED FT cells need correction.

### 2. tab:beam-docred-lora — SAME BUG + PF mismatch

**Llama Greedy con row** uses same pre-correction values:
- Paper E-F1=84.71, R-F1=44.70 → Corrected: 83.94, 43.78

**Qwen Greedy con PF:**
- Paper: PF=7.8%
- Registry `d065_qwen_greedy_4096_r2`: PF=8.52%
- ft-ablation table for same experiment: PF=8.52

The 7.8% value has no registry source. Likely a transcription error — should be 8.52% (or possibly 7.8% = 78/998 while 8.52% = 85/998 under different parse-failure definition).

### 3. tab:posthoc-extended — Llama DocRED FT cd value

Paper says cd R-F1=44.70, registry `w8_ft_posthoc_baseline` has cd=44.23 (intermediate value), corrected eval gives 43.78. Same parse-failure bug.

### 4. tab:full-ft LoRA unconstrained comparison row

| Metric | Paper (full-ft table) | Paper (ft-ablation table) | Registry |
|--------|----------------------|--------------------------|----------|
| E-F1 | 66.86 | 67.05 | 67.05 |
| R-F1 | 43.65 | 43.86 | 43.86 |
| DR% | 0.31 | 1.95 | 1.95 |

The full-ft table's LoRA unconstrained row doesn't match the ft-ablation table or registry. May come from a different LoRA checkpoint or obsolete run. The LoRA+S1 row (E-F1=67.05, R-F1=43.77) matches correctly.

### 5. tab:ft-ablation Qwen SciERC Semantic CF — Minor

Paper says CF=0.18%. Registry `w7_qwen_scierc_ft_semantic_only` has CF_count=15, total_entities=1784 → 15/1784 = 0.84%. Denominator or metric computation mismatch. Low severity but unexplained.

---

## Affected Prose Passages

The following text passages reference DocRED FT values that need updating:
- appendix_beam_search.tex line 136: "E-F1=67.05 and R-F1=43.77" — correct (SciERC)
- appendix_beam_search.tex line 176-180: Llama DocRED LoRA greedy values — affected
- appendix_discussion.tex: Multiple references to DocRED FT delta computations may need rechecking

---

## Recommendation

1. **Immediate fix**: Update all DocRED FT values (tab:ft-ablation, tab:beam-docred-lora Llama row, tab:posthoc-extended Llama DocRED FT) to corrected `eval_d064.py` values from registry
2. **Fix PF**: Correct Qwen DocRED PF in beam-docred-lora table (7.8→8.52 or verify source)
3. **Fix full-ft table**: Update LoRA unconstrained row to match registry/ft-ablation values
4. **Verify CF computation**: Check semantic-only CF=0.18% denominator for Qwen SciERC

---
