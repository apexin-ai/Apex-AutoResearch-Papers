# paper writing limitations

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_limitations_20260521T054219_result.json`
- **Structured JSON:** [`df421e429712bb00e679.json`](../../sessions/df/df421e429712bb00e679.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `docs/paper/limitations.tex` (~250 words). Five limitations with specific experimental numbers:

1. **Expert budget threshold** — $n_{\text{expert}}/K \geq 25$ required; HB/MLE converge at $n \geq 1000$
2. **RMSE tradeoff** — up to 3.5× worse RMSE at $K{=}4$, small $n$
3. **Plug-in SEs** — no confusion matrix uncertainty propagation (D010 requirement met)
4. **Symmetric misclassification** — asymmetric case not empirically validated
5. **Subgroup structure assumed known** — discrete pre-defined subgroups only; intersectional settings may exceed budget threshold

---
