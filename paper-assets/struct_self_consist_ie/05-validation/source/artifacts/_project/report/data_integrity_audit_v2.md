# Data Integrity Audit v2

**Date:** 2026-05-16
**Scope:** All tables and key inline claims in the EMNLP 2026 paper "Structured Self-Consistency for Information Extraction"
**Constraint:** ρ values must come from gold-filtered pipeline (excluding gold-empty instances). CoNLL n=2756, SciERC NER n=529, RE n=397 are canonical counts.

---

## Summary

| Category | Count |
|----------|-------|
| Verified ✅ | 8 |
| Discrepancy ⚠️ | 2 |
| Unable to Verify ❓ | 2 |
| Not Applicable | 1 |

**Critical finding:** Table 5 (scale ablation) has two incorrect 4B CoNLL values. Table 3 has one rounding error and two RE N=16 values with no traceable source.

---

## Priority 1: Known Discrepancies

### (a) Table 1 SciERC — Source Traceability ✅

**Source:** `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_015_unified/exp015_unified_report.json`

All 20 SciERC values (5 signals × {ρ, AUROC} × {NER, RE}) match after standard 3-decimal rounding:

| Signal | Source ρ (NER) | Paper | Source ρ (RE) | Paper |
|--------|---------------|-------|---------------|-------|
| Voting | 0.5018 | .502 ✅ | 0.4217 | .422 ✅ |
| SJ | 0.3565 | .357 ✅ | 0.2112 | .211 ✅ |
| FK | 0.2651 | .265 ✅ | 0.2528 | .253 ✅ |
| EM | 0.2566 | .257 ✅ | 0.1002 | .100 ✅ |
| LP | 0.1396 | .140 ✅ | 0.2467 | .247 ✅ |

AUROC values similarly verified (all 10 match).

### (b) Table 2 Selection F1 and +2.3pp Claim ✅

**Source:** `artifacts/exp_016_signal_ensemble/report/selection_f1_comparison.json`

| Metric | Source | Paper | Status |
|--------|--------|-------|--------|
| NER Greedy | 0.6094 | 0.609 | ✅ |
| NER Oracle | 0.7692 | 0.769 | ✅ |
| NER LP | 0.6087 | 0.609 | ✅ |
| RE Greedy | 0.3735 | 0.374 | ✅ |
| RE LP | 0.3971 | 0.397 | ✅ |
| RE Oracle | 0.5608 | 0.561 | ✅ |
| RE +pp (LP−Greedy) | 0.0236 | +2.3pp | ✅ |

All NER and RE selection F1 values verified. The "+2.3pp" claim is correct: 0.3971 − 0.3735 = 0.0236.

### (c) Table 5 Scale Ablation — 4B CoNLL Values ⚠️ DISCREPANCY

**Source:** `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_scale_qwen3_4b_conll/scale_ablation_report.json`

| Signal | Source Value | Paper Value | Correct Rounding |
|--------|-------------|-------------|-----------------|
| SJ | 0.4324 | .422 | .432 ⚠️ |
| FK | 0.4244 | .418 | .424 ⚠️ |

**Root cause:** Likely a copy-paste error. The 4B SciERC values in the same table are correct (verified against `exp_qwen3_4b_scierc_scs_inference/report.json`).

**Recommendation:** Replace Table 5 CoNLL 4B row: SJ .422→.432, FK .418→.424.

---

## Priority 2: Unverified Tables

### (d) Table 1 CoNLL — Source Traceability ✅

**Source:** `artifacts/analysis_unified_rho_full.json` (keys: `qwen_conll_n8_seed42`, `llama_conll_n8_seed42`)

All 20 CoNLL values verified. Sample checks:

| Signal | Source ρ (Qwen) | Paper | Source ρ (LLaMA) | Paper |
|--------|----------------|-------|------------------|-------|
| EM | 0.4513 | .451 ✅ | 0.4467 | .447 ✅ |
| SJ | 0.4362 | .436 ✅ | 0.4312 | .431 ✅ |
| LP | 0.3443 | .344 ✅ | 0.3071 | .307 ✅ |

### (e) Table 3 Robustness — Partial Verification ⚠️/❓

**T=0.7 row (N=8, SciERC):** ✅ VERIFIED
**Source:** `artifacts/exp005_temperature/signal_comparison_by_temp.json`

| Signal | Source (NER T=0.7) | Paper | Source (RE T=0.7) | Paper |
|--------|-------------------|-------|-------------------|-------|
| SJ | 0.3875 | .388 ✅ | 0.2343 | .234 ✅ |
| FK | 0.3211 | .321 ✅ | 0.1835 | .184 ✅ |

**T=1.0 / N=8 row:** ✅ Matches Table 1 values (same experiment: exp_015_unified, seed42).

**N=16 row (3-seed means):**

| Cell | Paper | Best Source Match | Source Value | Status |
|------|-------|-------------------|-------------|--------|
| SJ NER | 0.412 | bootstrap_ci_summary.json | mean=0.4121 | ✅ |
| FK NER | 0.280 | bootstrap_ci_summary / all_signals_report seed42 | 0.2809 | ⚠️ Rounds to .281, not .280 |
| SJ RE | 0.281 | Multiple pipelines disagree (0.244–0.292) | No match | ❓ |
| FK RE | 0.279 | bootstrap_ci_single exp004 | 0.2782 (rounds to .278) | ❓ |

**Pipeline concern:** T=0.7 values come from `exp005_temperature` while T=1.0/N=8 values come from `exp_015_unified`. These are different pipelines run at different times. While both use gold-filtering and the same signal implementations, this cross-pipeline sourcing should be documented.

**RE N=16 provenance problem:** Three different server pipelines (`bootstrap_ci_single`, `re_all_signals_report`, `n16_3seed_5signal_results`) give different SJ/FK RE rho values for the same seed42 N=16 configuration. None produce the exact paper values (0.281/0.279). This suggests either (1) a fourth pipeline was used, or (2) the values were computed with different instance filtering.

**Recommendation:**
1. Fix FK NER N=16: .280 → .281 (correct rounding of 0.2809).
2. Locate and document the exact source for SJ RE N=16=0.281 and FK RE N=16=0.279, or recompute from a canonical pipeline.

### (f) SJ Normalizer Ablation — Not in Paper

Server data exists at `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/review_round8/task1_sj_normalizer_final.json` with 6 rows (3 datasets × 2 models) comparing max vs union normalization. However, **no corresponding table exists in any paper .tex file**. The terms "normalizer", "max vs union", "rho_max", "rho_union" do not appear in the paper.

If this ablation was intended for inclusion (e.g., as a reviewer-requested appendix), it has not been written.

---

## Priority 3: Consistency Checks

### (g) Inline Numbers vs. Tables ✅

28 inline numbers across `experiments.tex`, `abstract.tex`, `introduction.tex`, and `discussion.tex` were spot-checked against their table sources. **All match.**

Key verifications:
- "ρ=0.50" → Table 1 SciERC NER Voting .502 (2-sig-fig rounding) ✅
- "AUROC=0.73" → Table 1 SciERC NER Voting .728 (2-sig-fig rounding) ✅
- "+2.3pp" → Table 2 RE LP−Greedy = 0.0236 ✅
- "16.0 pp headroom" → Table 2 NER Oracle−Greedy = 0.769−0.609 = 0.160 ✅
- "SJ gap 0.092 on SciERC NER" → Table 1 SJ .357 − FK .265 = 0.092 ✅
- "logprob AUROC=0.761, ρ=0.307 on CoNLL LLaMA" → Table 1 CoNLL LLaMA LP ✅
- All selection F1, percentage-point differences, and sample sizes verified ✅

### (h) Discussion n=81 RE Subset ✅

**Source:** `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/output/exp_009_v2_re_rerun/results.json`

The claim "high-complexity RE subset (n=81; instances with ≥3 relation triples) yields Voting ρ=0.630, SJ ρ=0.502" is verified:
- High tertile (T3): n=81 ✅
- voting_conf rho = 0.6302 → 0.630 ✅
- sj rho = 0.502 (with 95% CI [0.31, 0.65]) ✅

### Freeform Ablation Appendix Table (Bonus Check) ✅

**Table location:** `freeform_ablation_appendix_table.tex` (tab:freeform-ablation)
**Data source:** `artifacts/freeform_3seed_summary.json` (constrained_ref section for seed42 constrained data)

- Panel C constrained column: all 10 QE ρ values match `constrained_ref` exactly ✅
- Panel B constrained column: all 6 selection F1 values match exactly ✅
- Panel A constrained column: LP std/range/tied match `constrained_mean_*` fields ✅
- Δ column arithmetic: internally consistent (free − constrained = Δ) ✅
- Free-form column: sourced from seed42 freeform experiment (separate from the 3-seed summary which covers seeds 123/456/789)

---

## Action Items

| # | Priority | Action | Effort |
|---|----------|--------|--------|
| 1 | **HIGH** | Fix Table 5 CoNLL 4B: SJ .422→.432, FK .418→.424 | 1 min |
| 2 | **MEDIUM** | Fix Table 3 FK NER N=16: .280→.281 | 1 min |
| 3 | **MEDIUM** | Locate/recompute Table 3 RE N=16 values (SJ=.281, FK=.279) from canonical pipeline and document source | 1–2 hr |
| 4 | **LOW** | Document cross-pipeline sourcing in Table 3 (T=0.7 from exp005, T=1.0 from exp_015) | 15 min |
| 5 | **LOW** | Decide whether to include SJ normalizer ablation table (data ready on server) | Decision |

---

## Data Source Registry

| Table | Source File | Location |
|-------|-----------|----------|
| Table 1 SciERC | `exp_015_unified/exp015_unified_report.json` | Server |
| Table 1 CoNLL | `analysis_unified_rho_full.json` | Local |
| Table 2 Selection | `exp_016_signal_ensemble/report/selection_f1_comparison.json` | Local |
| Table 3 T=0.7 | `exp005_temperature/signal_comparison_by_temp.json` | Local |
| Table 3 T=1.0/N=8 | Same as Table 1 | — |
| Table 3 N=16 NER | `bootstrap_ci_summary.json` | Local |
| Table 3 N=16 RE | ❓ Source unknown | — |
| Table 5 SciERC 4B | `exp_qwen3_4b_scierc_scs_inference/report.json` | Server |
| Table 5 CoNLL 4B | `exp_scale_qwen3_4b_conll/scale_ablation_report.json` | Server |
| Discussion n=81 | `exp_009_v2_re_rerun/results.json` | Server |
| Freeform appendix | `freeform_3seed_summary.json` (constrained_ref) | Local |
