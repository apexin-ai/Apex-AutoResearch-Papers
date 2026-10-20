# Paper Status Audit — trace-verdict-study

**Date**: 2026-05-16
**Paper**: "Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction"
**Venue**: ACL (anonymous review mode)
**Compiled PDF**: `docs/paper/main.pdf` (12 pages, compiled 2026-05-16 05:18 UTC)

---

## 1. Section Completeness

| Section | File | Status | Notes |
|---------|------|--------|-------|
| Abstract | main.tex:18-25 | **Complete** | All key findings, 3 contributions |
| Introduction | introduction.tex | **Complete** | 3 enumerated contributions |
| Method | method.tex | **Complete** | Task def, dataset, 7 trace conditions, models, loss ablation |
| Experiments | experiments.tex | **Complete** | Cross-model (Table 1), ablation (Table 2), density (Table 3), additional analyses |
| Discussion | discussion.tex | **Complete** | Fault detection framing, regex gap, training dynamics |
| Related Work | related_work.tex | **Complete** | 3 paragraphs: traces for LLMs, verdict/patch classification, trace compression |
| Conclusion | conclusion.tex | **Complete** | Summary of all findings + future work |
| Limitations | main.tex:34-44 | **Complete** | 6 limitations listed |
| Ethics Statement | main.tex:46-51 | **Complete** | Public benchmarks, no human subjects, ~20 GPU-hours |
| References | references.bib | **Complete** | Compiles without missing citation warnings |
| Appendix | appendix.tex | **Complete** | 13 sections (A–M): per-class, training details, VOTA examples, full results, tokenizer analysis, irreducible analysis, trace length ablation, calibration, DebugBench, robustness, training dynamics, dedup stats, regex baselines |
| ARR Checklist | arr_checklist.tex | **Complete** | Standalone document, all sections filled |

**Main body page count**: ~4 pages (pages 1–4). References: ~2 pages (5–6). Appendix: ~6 pages (7–12).
**8-page limit**: Well within limit. Main body could be expanded if desired.

---

## 2. Figure Status

| Figure ID | File | Exists | Used in Paper | Location |
|-----------|------|--------|---------------|----------|
| fig1_trace_overview | `figures/paper/fig1_trace_overview.pdf` | Yes | Yes | Figure 1, method.tex:31 |
| fig2_calibration | `figures/paper/fig2_calibration.pdf` | Yes | Yes | Figure 3, appendix.tex:358 |
| fig3_cross_model_gap | `figures/paper/fig3_cross_model_gap.pdf` | Yes | **NO** — not `\includegraphics`'d | Unused asset |
| fig4_trace_length | `figures/paper/fig4_trace_length.pdf` | Yes | Yes | Figure 2, appendix.tex:270 |

**Note**: fig3_cross_model_gap.pdf exists and was generated, but the paper presents cross-model data in Table 1 instead. The figure is orphaned.

---

## 3. Data Patch Status

| Data Patch | Status | Location |
|------------|--------|----------|
| Regex baseline (93.61% vs SFT 99.83%) | **Present** | experiments.tex:63 (Table 2), experiments.tex:72 (text) |
| DebugBench cross-task (100%, 99.77%, 96.71%) | **Present** | experiments.tex:110 (text), appendix Table 12 |
| Trace length ablation (256/512/1024/no_limit) | **Present** | experiments.tex:100-102 (summary), appendix Tables 9-10 + Figure 2 |
| Seed robustness — exception_only (Qwen 3 seeds) | **Present** | 99.83% ± 0.00 across seeds 42/123/456 |
| Seed robustness — exception_only (DeepSeek 3 seeds) | **Present** | 99.33% (seeds 42,456), 91.09% (seed 123) |
| ae_only multi-seed | **Missing** | Only seed 42 (99.92%) reported. No placeholder. |

---

## 4. Blocking Items

| Item | Status | Impact |
|------|--------|--------|
| ae_only seeds 123/456 not run | **Blocked** | Table 7 shows ae_only with single seed only. Limitations section says "other conditions use a single seed" but doesn't specifically flag ae_only as pending. **No placeholder text exists.** If multi-seed ae_only results are planned, they need to be run and patched into Tables 2 and 7. |
| fig3_cross_model_gap unused | **Low priority** | Figure exists but paper doesn't reference it. Either include it (e.g., in appendix robustness analysis) or clean up the orphaned file. Not blocking. |

---

## 5. Compilation Health

- **No LaTeX errors** in main.log
- **No missing figure warnings**
- **No undefined references**
- All 3 `\includegraphics` calls resolve successfully
- Bibliography compiles cleanly

---

## 6. Summary

The paper is **substantially complete**. All 6 main-body sections + appendix (13 subsections) + ARR checklist are written with real experimental data. All 4 requested data patches (regex, DebugBench, trace length, seed robustness) are integrated into the text and tables. Three figures compile correctly.

**Remaining gaps**:
1. ae_only multi-seed results (seeds 123/456) — experiments not run, no placeholder
2. fig3_cross_model_gap — orphaned figure, not used in paper
3. Main body is 4 pages vs. 8-page limit — room to expand if reviewers request more detail in main text
