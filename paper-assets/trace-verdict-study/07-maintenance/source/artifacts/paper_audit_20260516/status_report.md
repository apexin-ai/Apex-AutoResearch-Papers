# Paper Audit Report — 2026-05-16

**Project**: trace-verdict-study
**Venue**: EMNLP 2026 ARR (deadline: May 25, 9 days remaining)
**Paper dir**: `/root/trace-verdict-study/docs/paper/`
**Title**: "Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction"

---

## 1. Paper Sections — Completion Status

| Section | File | Lines | Words | Status |
|---------|------|-------|-------|--------|
| Abstract | main.tex (L18-30) | ~10 | ~120 | **Complete** |
| Introduction | introduction.tex | 30 | 582 | **Complete** — 3 contributions listed |
| Method | method.tex | 85 | 829 | **Complete** — task def, dataset, trace reps (7 conditions), models, training, loss ablation, dedup table |
| Experiments | experiments.tex | 154 | 1419 | **Complete** — 4 subsections: cross-model, ablation, density decomposition, calibration; 4 tables + 2 figure refs |
| Discussion | discussion.tex | 63 | 1257 | **Complete** — 5 subsections + limitations; has 1 data bug (see §4) |
| Related Work | related_work.tex | 29 | 511 | **Complete** — 3 paragraphs, 15+ citations |
| Conclusion | conclusion.tex | 19 | 248 | **Complete** |
| Appendix | appendix.tex | 224 | 1278 | **Complete** — per-class breakdown, training details, DeepSeek seed analysis, irreducible error analysis |
| references.bib | — | — | 9.3KB | Present, not audited for completeness |
| **Total** | **8 files** | **643** | **6124** | **~92% complete** |

**Compiled PDF**: main.pdf (225KB) exists on server.

---

## 2. Three Correction Workers — Output Verification

### Worker 1: DeepSeek full_trace v3 (79.16%) → Table 1
- **Status**: ✅ **CORRECT**
- experiments.tex Table 1 (tab:cross_model): `full_trace & 81.76% & 79.16% & 2.60pp`
- Appendix per-class table: DeepSeek Full Trace = 79.16%, Pass F1=85.40, Fail F1=63.70
- Discussion limitations: "a re-run with extended context yields 79.16% (CI [76.80%, 81.30%])"
- Old collapsed values (28.49%/10.59%) completely removed; no trace of old data anywhere

### Worker 2: VOTA Token Count Data Integration
- **Status**: ⚠️ **PARTIALLY CORRECT — 1 discrepancy**
- experiments.tex: "DeepSeek tokenizer averages **2,626** tokens per VOTA sample" — ✅ matches d030_token_analysis.txt ground truth (mean=2626)
- discussion.tex: "DeepSeek tokenizer averages **2,759** tokens per VOTA sample" — ❌ **WRONG** (2,755 is full_trace mean, not VOTA; likely copy-paste error)
- 91.7% truncation rate — ✅ correct in both files
- Qwen 1,908 tokens — ✅ correct in both files
- **Action needed**: Fix discussion.tex `2,759` → `2,626`

### Worker 3: D034 Narrative Correction (trace content truncation ≠ label truncation)
- **Status**: ✅ **CORRECT — fully consistent**
- introduction.tex: "truncating diagnostic trace content while preserving the verdict label" ✅
- experiments.tex: correctly distinguishes full_trace "right-truncation removed the verdict label" vs VOTA "preserves the verdict label but truncates the trace content" ✅
- discussion.tex: "the verdict label is preserved, but the trace content is truncated" ✅
- appendix.tex: "label truncated" only in DeepSeek full_trace context (correct) ✅
- **No incorrect "label truncation" language applied to VOTA anywhere in the paper**

---

## 3. Paper Framing v3.0 Consistency

- paper_framing.md: v3.0 ✅ (updated 2026-05-15)
- Core narrative: "trace truncation + model capability confound" — ✅ consistent across all tex files
- VOTA repositioned as "fault indicator isolation" — ✅ reflected in discussion ("fault detection, where the minimal sufficient signal is the exception event")
- 3 claims correctly mapped to sections:
  - Claim 1 (exception signal transfer) → §4.1 cross-model + §4.2 ablation
  - Claim 2 (information density) → §4.3 density decomposition
  - Claim 3 (two-tier hierarchy) → §4.2 ablation + §4.4 calibration
- DeepSeek seed analysis: ✅ transparent reporting (2/3 at 99.33%, 1 outlier at 91.09%)
- Irreducible error (GeneratorExit): ✅ in discussion §5.5 error analysis

---

## 4. Issues Found (Priority Sorted)

### P0 — Blocking for submission

| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 1 | **All 3 figures MISSING** | `/root/trace-verdict-study/figures/paper/` is empty | Must create: fig1_trace_overview (schematic), fig2_calibration (reliability diagram), fig3_cross_model_gap (bar chart). LaTeX compiles but with missing figure placeholders. |
| 2 | **Token count discrepancy** | discussion.tex ~L19 | Change "2,759" → "2,626" for DeepSeek VOTA mean token count (2,755 is full_trace; 2,626 is VOTA per d030_token_analysis.txt) |

### P1 — Important, non-blocking

| # | Issue | Impact | Fix |
|---|-------|--------|-----|
| 3 | Bootstrap method inconsistency | Paper claims paired bootstrap but DeepSeek may lack per-sample prediction files | Re-run DeepSeek eval with --save_predictions (~40 min GPU) OR switch to unpaired + footnote |
| 4 | references.bib not audited | May have missing/incorrect entries | Run citation cross-check against tex files |
| 5 | Appendix Table 10 title | "label truncation bug" phrasing could be misread as applying to VOTA | Suggest: "context overflow causing verdict label loss" |

### P2 — Nice-to-have before deadline

| # | Issue | Impact |
|---|-------|--------|
| 6 | DebugBench data available (VOTA 99.77%) but only in conclusion as future work | Could add 1-paragraph external validation |
| 7 | Trace length ablation (256tok=78.82%, 512tok=80.42%) not in paper | Could support information density argument |
| 8 | writing_plan.yaml references "Figure 1 (VOTA schematic)" as Phase 1 — not delivered | Aligns with P0 #1 |

---

## 5. Critical Path to ARR May 25

| Date | Milestone | Key Actions |
|------|-----------|-------------|
| **5/16 (today)** | Fix data bugs | ① Fix discussion.tex 2,759→2,626; ② Verify references.bib |
| **5/17** | Create figures | ① fig1_trace_overview (schematic); ② fig2_calibration (reliability diagram from saved predictions); ③ fig3_cross_model_gap (grouped bar chart) |
| **5/18** | Bootstrap + optional data | ① Re-run DeepSeek evals with --save_predictions; ② Integrate DebugBench if ready; ③ Check 1024tok result |
| **5/19-20** | Internal review | ① Claim-evidence alignment; ② Statistical rigor (CIs, p-values); ③ Page budget (8 pages target) |
| **5/21-22** | Polish | ① Prose editing; ② Figure quality; ③ Appendix completeness |
| **5/23** | Final check | ① ACL template compliance; ② LaTeX clean compile; ③ Reference audit |
| **5/24** | Buffer | Emergency fixes |
| **5/25** | Submit | ARR submission |

### Top 3 risks
1. **Figures**: 3 figures referenced but 0 exist. This is the single biggest gap. ~1-2 days of work.
2. **Bootstrap consistency**: If we can't get DeepSeek per-sample predictions, must either re-run evals or switch paper language to unpaired bootstrap + footnote.
3. **Page budget**: 6124 words across 8 tex files + 4 tables + 3 figures + appendix. May be tight for 8-page limit — need careful layout.

---

## Summary

The paper is **~92% complete** with all core narrative, claims, and evidence in place. The 3 correction workers delivered correctly:
- ✅ DeepSeek full_trace v3 (79.16%) integrated into all tables
- ⚠️ VOTA token data integrated but with 1 number error in discussion.tex (2,759→2,626)
- ✅ D034 narrative ("trace content truncation") fully consistent

**The single most critical gap is the 3 missing figures.** Everything else is fixable in <1 day. With figures created by 5/17, the paper is on track for ARR May 25.
