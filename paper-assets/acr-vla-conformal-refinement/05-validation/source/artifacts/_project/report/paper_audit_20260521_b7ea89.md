# Paper Pre-Submission Audit — 2026-05-21

**Venue**: CoRL 2026 (DDL 2026-05-29, 8 days remaining)
**Title**: "When to Correct: Adaptive Inference-Time Compute Allocation for Frozen VLAs"
**Source**: `docs/paper/` (main.tex + 7 .tex files + references.bib)

---

## 1. Compilation Check

### Result: ✅ PASS — no errors, PDF produced

- **Build**: pdflatex × 3 + bibtex. Output: **15 pages, 544KB**
- **Page budget**: Main body ~7 pages (through Conclusion), references pages 8–9, appendix pages 10–15. Within CoRL limits.
- **Errors**: 0
- **Undefined citations**: 0
- **Undefined references**: 0
- **Warnings**: 7 total, all cosmetic:
  - 3× `'h' float specifier changed to 'ht'` (appendix floats)
  - 3× hyperref math-shift in PDF bookmark strings
  - 1× `Underfull \vbox` (page break heuristic)
- **Figures**: All 6 PDFs present in `figures/`: fig1_pipeline, fig2_magnitude, fig3_decomposition, fig3_kvalue, fig4_diversity, fig5_k2_correlation
- **TODO/FIXME markers**: None
- **Placeholders**: 2 instances of `\placeholder{}` (renders as "---") in Table 5 (π0.5 Plan A)

---

## 2. Number Consistency (Paper vs Registry)

### ✅ Verified Correct — match registry within rounding

| Claim | Paper | Registry verification | |
|-------|------:|----------------------:|:-:|
| Plan A Object (n=3) | 18.3 ± 2.1% | seeds 42/43/44 = 19/16/20 → 18.33 ± 2.08 | ✅ |
| Plan A Spatial (n=3) | 35.0 ± 1.0% | seeds 42/43/44 = 34/35/36 → 35.0 ± 1.0 | ✅ |
| Plan A Object trigger rate | 83.7% | seeds 83.8/84.0/83.2 → mean 83.67 | ✅ |
| CRM K=5 Object (n=7) | 16.0 ± 2.2% | seeds 42-48 = 14/19/17/15/16/13/18 → 16.0 ± 2.16 | ✅ |
| CRM K=5 Spatial (n=4) | 34.5 ± 2.1% | seeds 42/43/44/45 = 35/32/37/34 → 34.5 ± 2.08 | ✅ |
| Random K=5 Object (n=4) | 10.5 ± 2.9% | seeds 42/43/44/45 = 14/11/10/7 → 10.5 ± 2.89 | ✅ |
| Random K=10 Spatial (n=3) | 29.3 ± 4.2% | seeds 42/43/44 = 34/26/28 → 29.33 ± 4.16 | ✅ |
| VLA-only Spatial (n=5) | 29.4 ± 1.5% | seeds 42-46 = 30/29/31/27/30 → 29.4 ± 1.52 | ✅ |
| CRM K=20 Object (n=4) | 18.8 ± 1.0% | seeds 42/43/44/45 = 20/18/18/19 → 18.75 ± 0.96 | ✅ |
| CRM K=20 Spatial (n=3) | 34.3 ± 0.6% | seeds 42/43/44 = 35/34/34 → 34.33 ± 0.58 | ✅ |
| Adaptive P50 Object (n=3) | 15.3 ± 1.2% | seeds 42/43/44 = 16/16/14 → 15.33 ± 1.15 | ✅ |
| Adaptive P90 Object (n=3) | 13.3 ± 1.2% | seeds 42/43/44 = 12/14/14 → 13.33 ± 1.15 | ✅ |
| Adaptive P75 Object (n=3) | 13.7 ± 2.1% | seeds 42/43/44 = 12/13/16 → 13.67 ± 2.08 | ✅ |
| Adaptive P25 Object (n=3) | 14.3 ± 1.2% | seeds 42/43/44 = 15/13/15 → 14.33 ± 1.15 | ✅ |
| π0.5 VLA-only Object (n=3) | 81.5 ± 0.5% | seeds 42/43/44 (r3) = 82.0/81.5/81.0 → 81.5 ± 0.5 | ✅ |
| π0.5 VLA-only Spatial (n=3) | 84.2 ± 1.0% | seeds 42/43/45 = 84.5/83.0/85.0 → 84.17 ± 1.04 | ✅ |
| LTO boundary | CRM 2% vs VLA 14% (−12pp) | registry: heldout=0.02, vla-only=0.14 | ✅ |
| Argmin K=10 Object (n=6) | 12.3 ± 2.6% | framing: 12/17/13/12/10/10 → 12.33 ± 2.58 | ✅ |
| K=1 CRM | 10.3% (below baseline) | framing: 12/9/10 → 10.33 | ✅ |

### ⚠️ Issues Found

#### 2a: 🔴 Spatial Plan A fast-path column — likely transposition error

**appendix.tex Table 3 (`tab:adaptive_spatial`)**: Plan A fast path = **84%**
**experiments.tex + introduction.tex**: Spatial trigger rate = **97.6%** → fast path should be **2.4%**
**Registry**: seed42=97.6%, seed43=98.0%, seed44=97.8% trigger → mean fast-path = 2.2%

The 84% is exactly the Object Plan A complement (100 − 16.3 ≈ 84). This is a copy-paste transposition. **Fix: change 84 → 2.4 (or 2.2 from mean).**

#### 2b: VLA-only Object — two different baselines in the paper

| Location | Value | n |
|----------|------:|--:|
| Table 1 (`tab:main`) | 11.0 ± 1.3% | 8 |
| Table 2 (`tab:adaptive`) | 10.9 ± 1.4% | 8 |
| Table 4 (`tab:k_ablation`) | 11.0 ± 1.3% | — |
| Abstract + Introduction | 11.0 ± 1.3% | 8 |
| paper_framing.md | 10.8 ± 1.3% | 9 |

Table 2 footnote says "Seed set differs from Table 1". Documented but confusing — reviewer may question which is the "true" baseline. The +7.3pp claim uses 11.0% (18.3 − 11.0 = 7.3) ✅.

**Recommendation**: Align to a single baseline across all tables, or explain the seed-set difference more clearly.

#### 2c: obs_only magnitude range — lower bound discrepancy

- **Paper (experiments.tex)**: "obs\_only is stable (12.5--16.8%)"
- **paper_framing.md**: "obs_only stable 13.4-16.8%"

The paper's 12.5% lower bound doesn't match framing's 13.4%. If the paper is reporting a specific ε/seed combination (e.g., ε=0.05 with a larger seed set), the mean should be verified against registry data.

#### 2d: Random K=10 Object — registry mean doesn't match

- **Paper**: 9.7 ± 1.5% (n=6)
- **Registry** (6 DONE seeds): 42=11%, 43=9%, 44=11%, 45=10%, 46=10%, 48=10% → mean = **10.2%**

0.5pp gap. Possible causes: different evaluation protocol (20 vs 10 rollouts/task), or different seed selection. The paper_framing also claims 9.7% so the paper is self-consistent, but registry data differs. **Needs clarification.**

#### 2e: CRM K=10 Spatial — minor mean discrepancy

- **Paper Table 1**: 34.4 ± 1.5% (n=3)
- **Registry closest 3-seed match**: {43=34, 44=36, 45=34} → 34.67%

No 3-seed combination from registry gives exactly 34.4. Discrepancy is small (0.3pp) but worth verifying the exact seed set.

#### 2f: Plan A Spatial trigger rate — single-seed vs mean

- **Paper**: 97.6%
- **Registry 3-seed mean**: (97.6 + 98.0 + 97.8) / 3 = 97.8%

Paper reports seed42's value rather than the mean. Trivial (0.2pp) but should use the mean for consistency.

#### 2g: CRM K=10 Object — n=6 in paper vs n=7 in paper_framing

Paper Table 1 says n=6; paper_framing says n=7 (seeds 43/44/45/46/47/48/51, excl. seed42 per D084). Mean and std round identically, but the discrepancy in sample size should be resolved.

---

## 3. π0.5 Section Gap Analysis

### 3.1 Current π0.5 Content in Paper

| Location | Content | Status |
|----------|---------|:------:|
| experiments.tex:107 | One sentence: "see Appendix E" | Minimal |
| appendix.tex §E, Table 5 | VLA-only baseline: Object 81.5%, Spatial 84.2% | ✅ Filled |
| appendix.tex Table 5 Plan A row | `\placeholder{}` × 2 (renders as "---") | ❌ Missing |
| appendix.tex:199 | "Plan A results are pending (---)" | ❌ Placeholder |
| discussion.tex (Conclusion) | "larger VLAs are untested" | ❌ **Contradicts π0.5 section** |
| Abstract | No π0.5 mention | — |
| Introduction contributions | No cross-VLA point | — |

### 3.2 π0.5 Pipeline Status (from Registry)

| Stage | Status | Blocking? |
|-------|--------|:---------:|
| VLA-only baselines (3 seeds each) | ✅ DONE | — |
| Feature precompute (30+ shards) | 🟡 ALL PREPARING | Yes |
| CRM training | ❌ NOT STARTED | Blocked on precompute |
| Plan A eval | ❌ NOT POSSIBLE | Blocked on CRM |

### 3.3 Timeline Risk: 🔴 CRITICAL

The full pipeline (precompute → CRM train → Plan A eval) has not started. With DDL=May 29, completing all stages is extremely tight.

**Fallback options**:
- **Option A (recommended)**: Keep Table 5 with VLA-only baseline only, remove Plan A placeholder row. Rewrite text as: "π0.5 achieves 81.5% / 84.2% VLA-only, leaving limited headroom for post-hoc correction. Plan A evaluation is left to future work." Update Conclusion to say "production-scale VLAs beyond 3.6B are untested" (since π0.5 VLA-only IS tested).
- **Option B**: Remove Appendix E entirely, keep "larger VLAs untested" in Conclusion.
- **Option C**: Rush pipeline, fill in results at last minute. High risk.

### 3.4 Where to Write π0.5 Results (if they arrive)

1. **Table 5 (appendix.tex:194)**: Replace `\placeholder{}` with Plan A SR ± std
2. **appendix.tex:199**: Replace "pending" with 1-2 sentence interpretation
3. **discussion.tex**: Update "larger VLAs are untested" → acknowledge π0.5
4. **experiments.tex:107**: Expand one-sentence reference if result is strong
5. **Abstract**: Optional clause if result is positive

### 3.5 π0.5 Narrative Role (from paper_framing)

Tests C3 prerequisite 1: does CRM correction help for a larger flow-matching VLA? At 80%+ baseline, headroom is limited. Even a null result is valuable — confirms the inverse correlation between base VLA quality and correction benefit.

### 3.6 Seed-set Note

π0.5 Object uses seeds {42, 43, 44}. Spatial uses seeds {42, 43, **45**} (seed 44 spatial runs failed). If Plan A uses different seeds, document the substitution.

---

## 4. Citation & Bibliography Check

### Result: ✅ PASS

- **31 `\cite{}` keys** used across all .tex files
- **31 entries** in references.bib
- **Perfect 1:1 match** — no missing, no orphaned, no duplicates
- **bibtex** runs clean with 0 warnings
- All entries well-formed with correct arXiv IDs where applicable
- No suspicious/fabricated citations detected

---

## 5. Conclusion Contradiction (Standalone Issue)

discussion.tex (Conclusion/Limitations): **"real-robot transfer and larger VLAs are untested"**

This is factually incorrect given Appendix E which reports π0.5 (3.6B) VLA-only results. Even without Plan A CRM eval, the baseline IS tested on a larger VLA.

**Fix**: Change to "real-robot transfer is untested; larger VLAs (π0.5, 3.6B) show limited headroom for correction (Appendix E)" or similar.

---

## 6. Priority Action Items

| Priority | Item | Section | Effort |
|----------|------|---------|--------|
| 🔴 P0 | Fix Spatial Plan A fast-path: 84 → 2.4 in appendix Table 3 | §2a | 2 min |
| 🔴 P0 | Fix Conclusion "larger VLAs are untested" — contradicts Appendix E | §5 | 5 min |
| 🔴 P0 | Decide π0.5 Plan A strategy: rush pipeline, submit baseline-only, or remove section | §3.3 | Decision |
| 🟡 P1 | Verify Random K=10 Object 9.7% seed set and eval protocol | §2d | 30 min |
| 🟡 P1 | Align VLA-only Object baseline across Tables 1, 2, 4 (11.0 vs 10.9) | §2b | 30 min |
| 🟡 P1 | Verify obs_only magnitude range lower bound (12.5% vs 13.4%) | §2c | 15 min |
| 🟢 P2 | Verify CRM K=10 Spatial 34.4% exact seed set | §2e | 10 min |
| 🟢 P2 | Fix Spatial trigger rate: 97.6% → 97.8% (use mean) | §2f | 2 min |
| 🟢 P2 | Reconcile CRM K=10 Object n=6 vs n=7 | §2g | 5 min |
| 🟢 P2 | Remove `\placeholder{}` from Table 5 if π0.5 Plan A won't land | §3.3 | 5 min |

**Submission-blocking issues**: None (paper compiles and core results verified).
**Reviewer-bait items**: §2a (factual contradiction in appendix table), §5 (Conclusion vs Appendix), §3 (visible "---" placeholder in Table 5).

---

*Audit performed read-only — no paper files modified.*
