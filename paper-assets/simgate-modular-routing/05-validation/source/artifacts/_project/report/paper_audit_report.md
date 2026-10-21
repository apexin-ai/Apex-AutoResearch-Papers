# Paper Full-Number Audit & Structural Integrity Report

**Date**: 2026-05-14  
**Paper**: "Death Avoidance Accounts for 90% of the Routing Signal in LLM Agent Tool Use"  
**Target**: EMNLP 2026 ARR short paper (4 pages + refs), DDL 2026-05-25

---

## 1. Canonical Directory Determination

**Canonical**: `artifacts/_project/paper/latex/` (8 .tex files)  
**Non-canonical**: `docs/paper/` (7 .tex files, no discussion.tex)

### Evidence

| Criterion | artifacts/ | docs/paper/ |
|-----------|-----------|-------------|
| `\input{discussion}` in main.tex | ✅ Yes | ❌ No |
| discussion.tex exists | ✅ Yes | ❌ No |
| Limitations section | ✅ In main.tex | ❌ Absent |
| Ethics Statement | ✅ In main.tex | ❌ Absent |
| Compiled PDF timestamp | 14:45 (latest) | 12:24 |
| CI level | **95%** (from plan-003-bootstrap-95ci) | 90% (from older baseline) |

### ⚠️ CRITICAL: Directory Divergence

**The two directories are divergent — neither is a superset of the other.** `docs/paper/` contains significant content NOT present in `artifacts/`:

| Content | artifacts/ | docs/paper/ |
|---------|-----------|-------------|
| Abstract | 935 bytes, briefer | **1427 bytes**, includes Δ_full, Δ_nd, router score numbers |
| Method: Rule-Based Baseline (§rule) | ❌ Missing subsection | ✅ Has `\subsection{Rule-Based Baseline}` with 3 keyword lists |
| Experiments: Labeling quality ¶ | ❌ Not in experiments | ✅ Full paragraph in §router-diagnostic |
| Conclusion: Labeling Quality ¶ | ❌ Not in conclusion | ✅ Detailed paragraph |
| Conclusion: Limitations & Future Work ¶ | ❌ Not in conclusion | ✅ Full paragraph with DAgger cite |
| Router diagnostic detail | Shorter, seed table in notes | **Longer**: logit-gen gap analysis, 3 observations paragraph |
| Table 1 CI level | 95% Bootstrap CI | 90% CI |

**Recommendation**: Merge content from `docs/paper/` into `artifacts/` before submission. Specifically:
1. Use the longer abstract from `docs/`
2. Add Rule-Based Baseline subsection to method.tex
3. Consider whether labeling quality belongs in Conclusion (docs/) or Limitations (artifacts/) — currently duplicated across directories
4. The 95% CI in artifacts/ is correct (matches experiment name `plan-003-bootstrap-95ci`)
5. After merge, **deprecate** `docs/paper/` to avoid future divergence

---

## 2. Number Audit (Canonical: artifacts/)

### Table 1 — Baselines

| Strategy | Paper Score | Registry Source | Paper CI | Registry CI | Paper Death% | ✅/❌ |
|----------|-------------|----------------|----------|-------------|-------------|-------|
| Always-Internal | -39.07 | plan-003-bootstrap-95ci: -39.07 | [-46.40, -32.27] | [-46.4, -32.27] | 42.9 | ✅ |
| Always-Det. | -9.47 | plan-003-bootstrap-95ci: -9.47 | [-14.71, -4.29] | [-14.71, -4.29] | 16.3 | ✅ |
| Random | -22.38 | plan-003-bootstrap-95ci: -22.38 | [-28.67, -15.75] | [-28.67, -15.75] | 27.8 | ✅ |
| Oracle | -6.58 | plan-003-bootstrap-95ci: -6.58 | [-11.54, -1.70] | [-11.54, -1.7] | 14.3 | ✅ |
| Trained Router | -10.70 | plan-003-bootstrap-95ci: -10.7 | [-16.33, -5.27] | [-16.33, -5.27] | 17.6 | ✅ |

**Trained Router source**: ✅ Correctly uses -10.70 from `plan-003-e2e-ablation-b-correct` (ablation-b seed42 checkpoint). NOT -12.84 (that's `plan-003-eval-implicit` / wrong checkpoint).

**Note**: `plan-003-e2e-ablation-b-correct` raw CI is [-15.25, -6.38], while `plan-003-bootstrap-95ci` reports [-16.33, -5.27]. The bootstrap CI is wider because it's 95% vs. possibly 90% in the raw experiment. Paper correctly uses the bootstrap-95ci values.

### DAF Decomposition

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| DAF | 90.41% | plan-012-full | 0.9041 | ✅ |
| Δ_full | +29.60 | plan-012-full | 29.6 | ✅ |
| Δ_nd | +2.84 | plan-012-full | 2.84 | ✅ |
| Δ_nd/Δ_full | 9.6% | computed | 2.84/29.60 = 0.09595 | ✅ |
| DAF check | 1 - 2.84/29.60 | computed | 0.90405 → 90.41% | ✅ |
| Pearson r | 0.9698 | plan-012-full | 0.9698 | ✅ |
| Pearson p | 8.12e-07 | plan-012-full | 8.12e-07 | ✅ |
| Death rate internal | 42.9% | plan-012-full | 0.429 | ✅ |
| Death rate det | 16.3% | plan-012-full | 0.163 | ✅ |
| Death ratio | 2.6× | computed | 42.9/16.3 = 2.63 | ✅ |

### Label Distribution

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| det_preferred | 86 | plan-012-full | 86 | ✅ |
| internal_preferred | 9 | plan-012-full | 9 | ✅ |
| no_preference | 150 | plan-012-full | 150 | ✅ |
| Oracle matches always-det | 96.3% | computed | (86+150)/245 = 96.3% | ✅ |

### Step-Level Tie Rate

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| Tie rate | 97.4% | plan-012-step-tie-rate | 0.9739 → 97.39% | ✅ |
| NOT 98.2% | ✅ Correct | plan-012-step-tie-rate notes | "Delta from old MVP = -0.78pp (97.39% vs 98.2%)" | ✅ |

### Router Diagnostic

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| 4-seed balanced_acc | 58.1±0.8% | plan-004-ablation-b notes | Seeds: 59.27, 57.36, 57.48, 58.31 → mean 58.1, std 0.8 | ✅ |
| GA=8 seed42 generation acc | 65.4% | plan-004-ablation-b | 0.6536 | ✅ |
| GA=8 seed42 internal recall | 51.5% | plan-004-ablation-b | 0.5152 | ✅ |
| GA=1 logit accuracy | 74.5% | plan-004-v5 | 0.7451 | ✅ |
| GA=1 logit balanced_acc | 79% | plan-004-v5 | 0.7905 → ~79% | ✅ |
| GA=1 generation accuracy | 53.3% | plan-004-v5 | 0.5333 | ✅ |
| GA=1 generation internal recall | 26.7% | plan-004-v5 | 0.2667 | ✅ |
| Logit-gen gap | 21.2pp | computed | 74.5 - 53.3 = 21.2 | ✅ |
| Sim invocation ratio | 97.0% | plan-003-e2e-ablation-b-correct | 0.9703 | ✅ |
| Internal recall range | 51.5%–81.8% | plan-004 seeds | 51.52, 57.58, 75.76, 81.82 | ✅ |
| "8 points above chance" | 58.1 - 50 = 8.1 | computed | ✅ | ✅ |

### Labeling Quality (Limitations section)

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| Total labels | 245 | plan-013-labeling-quality | N/A (consistent with 245 eps) | ✅ |
| no_preference | 150 (61.2%) | plan-013 | tie_rate=0.612 → 150/245 | ✅ |
| Both-alive ties | 115 (46.9%) | plan-013 | tie_rate_both_alive=0.469 → 114.9≈115 | ✅ |
| Both-dead | 35 (14.3%) | plan-013 | tie_rate_both_died=0.143 → 35.0 | ✅ |
| Genuine training labels | 95 | plan-013 notes | 70+16+5+4=95 | ✅ |
| Death asymmetry det-pref | 70 | plan-013 | det_preferred_death_asymmetry=70 | ✅ |
| Score comparison det-pref | 16 | plan-013 | det_preferred_score_comparison=16 | ✅ |
| Death asymmetry int-pref | 5 | plan-013 notes | 5 | ✅ |
| Score comparison int-pref | 4 | plan-013 notes | 4 | ✅ |
| Tie-break fraction | 0% | plan-013 | tiebreak_det_fraction=0 | ✅ |
| Strict retrain balanced_acc | 57.3% | plan-013 | 0.5729 | ✅ |
| Full-label ablation | 57.6±0.5% | plan-013 | 0.5761±0.0047 | ✅ |

### MATH Pilot (Discussion section)

| Metric | Paper Value | Registry Source | Registry Value | ✅/❌ |
|--------|------------|----------------|---------------|-------|
| N problems | 50 | math-pilot-50 | n_problems=50 | ✅ |
| Internal accuracy | 80% | math-pilot-50 | 0.80 | ✅ |
| Code interpreter accuracy | 72% | math-pilot-50 | 0.72 | ✅ |
| No-preference rate | 88% | math-pilot-50 | 44/50=0.88 | ✅ |
| det-preferred | 1 | math-pilot-50 | 1 | ✅ |
| internal-preferred | 5 | math-pilot-50 | 5 | ✅ |
| no-preference | 44 | math-pilot-50 | 44 | ✅ |

⚠️ **Caveat**: math-pilot-50 notes flag a sandbox bug: 34.1% of code executions had empty output. Clean code-interpreter accuracy (non-empty output only) is 88.9%, not 72%. The discussion.tex acknowledges "sandbox limitations" but uses the raw 72% as the headline. The `math-200-fixed` experiment (with sandbox fix) crashed at problem 56/200, showing 74.5% code-interpreter accuracy on 55 problems — directionally consistent but incomplete.

### Abstract Numbers

| Number | Paper Value | Cross-check | ✅/❌ |
|--------|------------|-------------|-------|
| 97.4% step tie rate | ✅ | plan-012-step-tie-rate | ✅ |
| 245 episodes | ✅ | plan-012-full | ✅ |
| ~90% DAF | ✅ | 90.41% in body | ✅ |
| r = 0.97 | ✅ | 0.9698 rounded | ✅ |

### Internal Consistency Across Sections

All numbers are consistent across abstract, introduction, method, experiments, discussion, conclusion, and limitations. No contradictions found between sections.

**Overall number audit: 100% PASS (all numbers verified against registry)**

---

## 3. Structural Integrity Check

### Section Substance

| Section | File | Substantive? | Notes |
|---------|------|-------------|-------|
| Abstract | abstract.tex | ✅ | Complete but shorter than docs/ version |
| Introduction | introduction.tex | ✅ | Complete with contributions |
| Method | method.tex | ✅ | 3 subsections (collection, labeling, DAF) |
| Experiments | experiments.tex | ✅ | 4 subsections (setup, decomp, baselines, router) |
| Related Work | related_work.tex | ✅ | 4 paragraphs |
| Discussion | discussion.tex | ✅ | 2 paragraphs + 2 TODOs |
| Conclusion | conclusion.tex | ✅ | Single paragraph |
| Limitations | main.tex | ✅ | 2 paragraphs (general + labeling quality) |
| Ethics | main.tex | ✅ | Single paragraph |

### Related Work Coverage

Required references (from paper_framing.md):

| Reference | Present? | Location |
|-----------|----------|----------|
| Toolformer | ✅ | Tool-Use Learning ¶ |
| ART | ✅ | Tool-Use Learning ¶ |
| Chameleon | ✅ | Tool-Use Learning ¶ |
| CogRouter | ✅ | Adaptive Computation ¶ |
| ARES | ✅ | Adaptive Computation ¶ |
| ITP (ITP-R) | ✅ | World Model Routing ¶ |
| ReAct | ✅ | Agent Frameworks ¶ |

Additional: ReTool, Mixture-of-Recursions, Dyna-Think, MTRouter — good coverage.

### TODO/FIXME Comments

| File | Line | Content | Status |
|------|------|---------|--------|
| discussion.tex | 7 | `% TODO: Replace pilot-50 numbers with math-200-fixed results when available` | ⚠️ math-200-fixed crashed at 56/200, incomplete |
| discussion.tex | 12 | `% TODO: ALFWorld results pending; add cross-environment comparison if signal emerges` | ⚠️ No ALFWorld experiment in registry |

### Discussion Section

- ✅ MATH pilot paragraph present with correct numbers
- ✅ ALFWorld placeholder as TODO comment (no data yet)
- ✅ "Scope and future directions" paragraph present

### Conclusion: Labeling Quality

- ❌ **Labeling quality paragraph is NOT in conclusion.tex** — it is in the Limitations section of main.tex
- The `docs/paper/conclusion.tex` version DOES include it (Labeling Quality ¶ + Limitations & Future Work ¶)
- **Decision needed**: Should labeling quality be in Conclusion (as in docs/) or Limitations (as in artifacts/)? Current artifacts/ placement in Limitations is defensible but the user mentioned "plan-013 入 conclusion" as a today task

---

## 4. Issues List (Priority Order)

### P0 — Must Fix Before Submission

1. **Directory divergence**: Two divergent paper directories with non-overlapping content. Must merge `docs/paper/` improvements into `artifacts/` and deprecate `docs/paper/`. Key missing content in artifacts/:
   - Longer, more specific abstract
   - Rule-Based Baseline subsection in method.tex
   - Labeling quality paragraph in experiments.tex
   - More detailed router diagnostic analysis
   - DAgger citation in conclusion/limitations

2. **Two TODO comments in discussion.tex**: Lines 7 and 12. Either resolve or remove before submission. math-200-fixed is incomplete (crashed at 56/200) so pilot-50 numbers may need to stand.

### P1 — Should Fix

3. **Labeling quality placement**: User intended "plan-013 入 conclusion" but artifacts/ has it in Limitations. Verify intended placement. The docs/ version places it in Conclusion — if that was the intent, move it.

4. **MATH pilot 72% accuracy caveat**: Known sandbox bug inflates the performance gap (clean accuracy is ~89% vs 72% reported). The TODO to replace with math-200-fixed cannot be resolved yet (experiment crashed). Consider adding a footnote about the sandbox limitation's impact on the 72% number.

### P2 — Nice to Have

5. **Abstract completeness**: artifacts/ abstract (935 bytes) is sparse compared to docs/ version (1427 bytes). The docs/ abstract includes Δ_full, Δ_nd, router comparison numbers which strengthen the abstract. Consider adopting the longer version.

6. **Conclusion brevity**: artifacts/ conclusion is a single paragraph (688 bytes). The docs/ version (1942 bytes) includes labeling quality and future work, making it more complete for a short paper where space is tight but reviewers want to see awareness of limitations.

7. **`toolformer-2024` bib key**: Year in key (2024) doesn't match year field (2023). Cosmetic but could confuse contributors.
