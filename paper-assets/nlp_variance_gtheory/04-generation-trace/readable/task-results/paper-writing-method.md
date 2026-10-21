# paper writing method

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260521T201904_result.json`
- **Structured JSON:** [`cfcbd7e12c12e1d3bcf3.json`](../../sessions/cf/cfcbd7e12c12e1d3bcf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`method.tex` written and registered. Summary:

**Structure**: 6 subsections (§3.1 G-Theory Background, §3.2 MMLU Design, §3.3 Cross-Benchmark Extension, §3.4 Evaluation Protocol, §3.5 Binary Data Assumptions, §3.6 Model-as-Facet Justification), ~1250 words.

**Included**:
- Table 1 (`tab:design_matrix`): 7 facets with level counts for exp-001 and exp-002, booktabs format
- Figure 2 reference (`fig2_design_diagram`): crossing structure diagram
- Equation 1: generalizability coefficient $G_\text{item}$
- All notation ($p, M, \pi, \delta, s, \tau, o, \sigma^2_x$) introduced in §3.1
- Four-line binary data defense with simulation, GLMM, accuracy-range stability, estimator guarantee
- D-study cross-validation ($\Delta = 0.004$), LOMO stability, forward projection in §3.6

**Consistency with experiments.tex**: Henderson Method~I, binary correctness, generalizability coefficient, `\texttt{item\_id}`, `model$\times$item`, $G_\text{item}$, $G \geq 0.80$, all record counts (239,200 / 345,600 / 921,600).

**Style**: 0 em-dashes, 0 explanatory en-dashes, 0 `\hline`, 0 consecutive transition words, 0 -ing phrase endings, all 11 citation keys verified in `references.bib`.

**Note**: `main.tex` still has the inline `\section{Method}` placeholder at line 58. It needs to be replaced with `\input{method}` (and the `\section{Method}` line removed since method.tex includes it).

---
