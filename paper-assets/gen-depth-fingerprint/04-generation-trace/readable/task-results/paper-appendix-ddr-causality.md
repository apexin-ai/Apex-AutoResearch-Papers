# paper appendix ddr causality

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_ddr_causality_20260520T082408_result.json`
- **Structured JSON:** [`78f0afdde516b80738e2.json`](../../sessions/78/78f0afdde516b80738e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Three changes made:

1. **`appendix_ddr_causality.tex`** — new file with permutation importance table (7 features ranked), Granger causality table (combined p + significance), and 4 key findings (drifting dominance, entropy_min non-causality, entropy_max asymmetry, Mistral heterogeneity).

2. **`main.tex`** — added `\section{DDR Causality Analysis}\label{app:ddr-causality}\input{appendix_ddr_causality}` before `\end{document}`.

3. **`discussion.tex`** — inserted the causal summary sentence at the end of the first paragraph (before "This asymmetry is not intrinsic to recursion..."), referencing `Appendix~\ref{app:ddr-causality}`.

---
