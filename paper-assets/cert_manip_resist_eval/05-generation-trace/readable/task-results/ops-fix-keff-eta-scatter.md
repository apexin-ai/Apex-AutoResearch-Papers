# ops fix keff eta scatter

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-keff-eta-scatter_20260525T222512_result.json`
- **Structured JSON:** [`0b0dfd1ed716387a2017.json`](../../sessions/0b/0b0dfd1ed716387a2017.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All updated. Here's the final verification summary:

---

**Figures generated** (from actual data):
| Figure | K | Pool | Computed r | Caption r | n panels |
|--------|---|------|-----------|-----------|----------|
| `fig_keff_eta_scatter_main.pdf` | 3 | Full only | 0.8585 | **0.86** | 455 |
| `fig_keff_eta_scatter.pdf` | 5 | Full | 0.7924 | **0.79** | 3003 |
| `fig_keff_eta_scatter.pdf` | 5 | Pool A | 0.5094 | **0.51** | 126 |

**Files modified:**
- `threat_model.tex`: `includegraphics` → `fig_keff_eta_scatter_main.pdf`, caption r=0.70→0.86
- `methodology.tex L42`: r=0.70→0.86
- `appendix.tex L93`: caption r=0.81→0.79, Pool A r=0.50→0.51
- `appendix.tex` (L740, L755, L492, L494, L596, L601, L605, L1183): Pool A r=0.50→0.51
- `main.tex L43`: Pool A r=0.50→0.51

**Pool A fix confirmed**: Pool A is now the correct capability-matched 9 models (5 API + 4 local), NOT the API-only 9 models. The figure annotation shows r=0.51, matching the computed bivariate r.

**Compilation**: 0 new errors. All pre-existing issues (missing `fig_panel_composition.pdf`, undefined citations) are unchanged.

**Known discrepancy**: The scatter bivariate r values (0.86, 0.79) differ from the per-condition log-space regression correlations (~0.70, ~0.81) that appear elsewhere in the paper (analysis.tex, conclusion.tex, abstract.tex, introduction.tex, appendix.tex VIF section). These references use per-condition regression diagnostic r values (mean VIF consistent with r≈0.70–0.81), which is a different metric from the aggregate bivariate scatter r. I left those per-condition references unchanged — they are internally consistent with the VIF≈2.0–2.9 values from the regression analysis.

---
