# analysis plan g dn awareness

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_g_dn_awareness_20260523T053039_result.json`
- **Structured JSON:** [`0fd421c5cc55ebbd16f1.json`](../../sessions/0f/0fd421c5cc55ebbd16f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated in `artifacts/plan_g/`:

| File | Content |
|---|---|
| `awareness_matrix.csv` | 5×6 matrix + margins (42 rows) |
| `analysis_report.md` | Full matrix table, cluster test, pairwise Fisher's, per-type rates, key findings |
| `appendix_draft.tex` | LaTeX table + 1-paragraph narrative |
| `maintext_sentence.txt` | Drop-in sentence for §6.2 |
| `analysis_full.json` | Machine-readable full analysis |
| `build_awareness_matrix.py` | Reproducible script |

**Key findings:**

1. **Two-cluster pattern confirmed**: {GPT-4.1, Claude} at 10–11% vs {Qwen3, DeepSeek} at 0% ($p = 2.2 \times 10^{-9}$). GPT-5.4 intermediate at 4.1%.
2. **Per-type**: Conditional precedence has the highest awareness (14.1%), driven by Claude's 8/18 (44.4%). Scopal has 0% across all models. Other types range 1.9–6.3%.
3. **Pairwise**: After Holm correction, only the 4 comparisons between {GPT-4.1, Claude} and {Qwen3, DeepSeek} are significant. GPT-5.4 comparisons are not significant after correction.

---
