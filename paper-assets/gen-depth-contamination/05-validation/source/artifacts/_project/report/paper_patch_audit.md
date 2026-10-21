# Paper Comprehensive Patch Audit

**Date**: 2026-05-18  
**Context**: D060 scorer confound resolution, 5-model arXiv cross-validation, 6×3 Domain×Model matrix complete  
**DDL**: EMNLP 2026 ARR May 25 (7 days)

---

## Summary of Current State

The paper is **largely up-to-date**. The D060 scorer confound, 6×3 matrix, Mistral case study, JSD decay, and Wikipedia resolution are all correctly reflected in the current `.tex` files. The main gaps are:

1. Outdated arXiv description in Abstract/Conclusion (says "two architectures" instead of five)
2. Missing LLaMA-8B and Mistral-7B data in extended CI table (shows "---")
3. Scale validation (14B/32B) pending results not yet incorporated
4. Minor wording updates to match paper_framing.md precision

---

## P0: Must Fix (factual errors or significant omissions)

### 1. Abstract: arXiv cross-validation count outdated
- **File**: `docs/paper/main.tex`, line 36
- **Current**: `"validated across two architectures (Qwen-1.5B, Pythia-1.4B)"`
- **Should be**: `"validated across five models spanning four architecture families (1.4B--8B)"`
- **Reason**: paper_framing.md confirms 5-model cross-validation (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B). The "two architectures" is D055-era language.

### 2. Conclusion: same outdated arXiv count
- **File**: `docs/paper/conclusion.tex`, line 5
- **Current**: `"confirmed across architectures (Qwen-1.5B, Pythia-1.4B)"`
- **Should be**: `"confirmed across five models (four architecture families, 1.4B--8B)"`
- **Reason**: Same as above.

### 3. Limitations: arXiv scope description outdated
- **File**: `docs/paper/main.tex`, line 68
- **Current**: `"arXiv $\Kempirical{=}3$ is confirmed with two model families (Qwen-1.5B, Pythia-1.4B) but with reduced sample size ($n{=}2{,}200$ per model)"`
- **Should be**: `"arXiv $\Kempirical{=}3$ is confirmed with five models spanning four architecture families (Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; $n{=}2{,}200$ per model)"`
- **Reason**: 5-model validation completed (D055/D056/D057). Reduced sample size caveat still applies.

### 4. Extended CI Table (Tab S2b): LLaMA-8B and Mistral-7B columns empty
- **File**: `docs/paper/appendix.tex`, lines 93-115 (tab:kstar_ci_extended)
- **Current**: LLaMA-8B column shows all "---"; Mistral-7B is not even present in the table
- **Should be**: 
  - LLaMA-8B: 0v1=0.9225, 1v2=0.6123 [0.603, 0.622], 2v3~0.56, etc.
  - Add Mistral-7B column: 0v1=~0.93, 1v2=0.5935 [0.584, 0.603], K*=1
- **Reason**: These experiments completed (exp-018, exp-019). The main text references them but the extended table has placeholders.

### 5. Pythia Decoding Table (Tab S10) entirely empty
- **File**: `docs/paper/appendix.tex`, lines 405-424 (tab:s10_pythia_decoding)
- **Current**: All cells show "---"
- **Should be**: Fill with exp-020 results (greedy: repetition-collapsed 1v2~0.884; nuc p=0.9, T=0.7, T=1.2 values)
- **Reason**: exp-020 completed. Caption references the data but cells are placeholders.

### 6. Domain Ablation Table (Tab S12) entirely empty
- **File**: `docs/paper/appendix.tex`, lines 449-469 (tab:s12_domain_ablation)
- **Current**: All cells show "---"
- **Should be**: Fill with Qwen-1.5B continuation data for C4/Wikipedia/arXiv from exp-023/exp-024
- **Reason**: All domain experiments completed. The main-text tab:domain_kstar has the summary but this detailed table is unfilled.

---

## P1: Should Fix (strengthens narrative or fixes inconsistencies)

### 7. Introduction contribution (b): still says "two architectures"
- **File**: `docs/paper/introduction.tex`, line 21
- **Current**: `"consistent across model families"`
- **Should be**: `"consistent across five models spanning four architecture families (1.4B--8B)"`
- **Reason**: The Introduction contribution list should match the Abstract and paper_framing.md precision. Current wording is vague but not wrong.

### 8. Theta sensitivity table: missing arXiv entries for LLaMA/Mistral/Qwen-7B
- **File**: `docs/paper/appendix_extended.tex`, lines 96-120 (tab:theta_sensitivity)
- **Current**: Only shows arXiv rows for Qwen-1.5B-base and Pythia-1.4B
- **Should be**: Add rows for LLaMA-8B, Mistral-7B, Qwen-7B on arXiv (all K*=3 at theta=0.60)
- **Reason**: 5-model validation data available; showing only 2 is inconsistent with main text claim.

### 9. experiments_c1.tex arXiv paragraph: claims "five-model" but body still leads with Qwen/Pythia
- **File**: `docs/paper/experiments_c1.tex`, lines 123-128
- **Current**: Correctly states 5-model validation and lists all models. Good.
- **Note**: This section is already updated. No change needed.

### 10. Method section experimental setup table (tab:setup): missing LLaMA-8B and Mistral-7B
- **File**: `docs/paper/method.tex`, lines 56-73 (tab:setup)
- **Current**: Lists only 6 configs (Qwen-rw, Qwen-cont, Qwen-base, Pythia, OLMo, Qwen-7B)
- **Should be**: Add LLaMA-3.1-8B and Mistral-7B rows (both continuation mode, C4 5000 seeds)
- **Reason**: Main text and abstract claim "8 model configurations" but setup table only shows 6. This is a factual mismatch the reviewer will notice.

### 11. JSD decay figure: verify 7 models are shown
- **File**: `docs/paper/discussion.tex`, line 13 (fig:jsd_decay caption)
- **Current**: Caption says "7 C4 models with K*=2" and "dashed purple: Mistral-7B"
- **Verify**: The figure file needs to include all 7 C4 models. If it was generated before LLaMA-8B data arrived, it may only show 5-6 models.
- **Action**: Regenerate `figures/fig_jsd_decay.pdf` with all 7 C4 model curves + Mistral + arXiv + retrain-chain

### 12. Scorer Sensitivity Table (Tab S13): mostly "---" entries
- **File**: `docs/paper/appendix.tex`, lines 472-492 (tab:s13_scorer_sensitivity)
- **Current**: Only Qwen-RW, Qwen-cont, Qwen-base have cross-scorer data. Pythia, OLMo, Qwen-7B, Mistral show "---"
- **Should be**: exp-022 provides cross-scorer data for multiple generators. Fill what's available.
- **Reason**: Partially filled table looks unfinished.

### 13. Discussion "Scorer sensitivity" paragraph: mention Wikipedia resolution explicitly
- **File**: `docs/paper/discussion.tex`, lines 66-68
- **Current**: Already mentions Wikipedia scorer confound and recommends cross-family validation. Good.
- **Note**: This section is already updated. No change needed.

### 14. Scale validation (14B/32B) mention
- **File**: `docs/paper/main.tex`, lines 68-70 (Limitations) and `conclusion.tex` line 7
- **Current**: "Scope: model scale ≤8B"; Conclusion: "Future work includes scaling to 13B+"
- **Should be**: If 14B/32B results arrive before submission, update Limitations scope and add one sentence to Discussion about scale. If not, current language is fine.
- **Action**: Conditional on experiment completion before May 25.

---

## P2: Optional Improvements (polish)

### 15. Abstract: add Wikipedia K*=1 to complete the domain hierarchy
- **File**: `docs/paper/main.tex`, line 36
- **Current**: Only mentions C4 K*=2 and arXiv K*=3
- **Could add**: Brief mention of domain ordering: "arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1)"
- **Reason**: The clean three-level hierarchy is the headline finding post-D060. Space permitting, it strengthens the Abstract.

### 16. Discussion: add explicit mention of "two types of one-wash"
- **File**: `docs/paper/discussion.tex`, around lines 17-19 and 59-63
- **Current**: Discusses Mistral domain-rescue and OLMo capacity failure separately
- **Could add**: A sentence explicitly naming the distinction: "One-wash arises from two distinct mechanisms: domain-dependent (Mistral, rescued by arXiv) and model-intrinsic (OLMo, K*=1 across all domains)."
- **Reason**: paper_framing.md emphasizes this as a key insight; the paper discusses it implicitly but never names the two-type taxonomy explicitly.

### 17. Appendix extended discussion: lambda values could cite memory.md numbers
- **File**: `docs/paper/discussion.tex`, lines 23-32
- **Current**: Already mentions C4 lambda~2.9, arXiv lambda~1.0, Wikipedia lambda~3.1. Good.
- **Note**: Numbers match memory.md. No change needed.

### 18. Appendix Tab S12: caption says "Qwen2.5-1.5B-Instruct, continuation mode" but should reflect all 6 models
- **File**: `docs/paper/appendix.tex`, line 453
- **Current**: Caption scoped to single model
- **Should be**: If filling with multi-model data, update caption accordingly. Or keep as single-model detail table and reference main-text tab:domain_kstar for full matrix.

### 19. Ethics Statement: add Wikipedia and arXiv to data sources
- **File**: `docs/paper/main.tex`, line 81
- **Current**: "Our experiments use the publicly available C4 corpus"
- **Should be**: "Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts)"
- **Reason**: Paper now uses 3 domains but Ethics only mentions C4.

---

## Priority Summary

| Priority | Count | Items |
|----------|-------|-------|
| P0 (must fix) | 6 | #1, #2, #3, #4, #5, #6 |
| P1 (should fix) | 8 | #7, #8, #10, #11, #12, #13, #14 (conditional) |
| P2 (optional) | 5 | #15, #16, #17, #18, #19 |

## Recommended Execution Order

1. **First pass (P0, ~2h)**: Fix factual counts (#1, #2, #3, #7), add method table rows (#10), fill appendix data tables (#4, #5, #6)
2. **Second pass (P1, ~2h)**: Update theta sensitivity table (#8), regenerate JSD figure (#11), fill scorer table (#12)
3. **Third pass (P2, ~1h)**: Abstract domain hierarchy (#15), two-type one-wash (#16), Ethics (#19)
4. **Conditional**: If 14B/32B results arrive, add to Discussion (#14)

## Already Correct (no change needed)

- experiments_c1.tex Section 4.5 (Cross-Domain Variation): correctly describes 5-model arXiv, 6-model Wikipedia, scorer confound, clean domain ordering
- tab:domain_kstar (inline in experiments_c1.tex): 6×3 matrix with footnotes for scorer artifact, capacity failure, one-wash
- tab:domain_model_kstar.tex and tab_domain_model_kstar_full.tex: correctly formatted with all 6 models
- Discussion JSD paragraph: lambda values match memory.md
- Discussion scorer sensitivity paragraph: correctly describes Wikipedia confound
- appendix_extended.tex Wiki Domain section: correctly resolves the confound with detailed table
- Dose-response section: complete with table and analysis
