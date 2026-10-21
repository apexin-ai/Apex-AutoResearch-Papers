# paper appendix 9gen scale

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_9gen_scale_20260520T084336_result.json`
- **Structured JSON:** [`1d5a296bc62d75e23613.json`](../../sessions/1d/1d5a296bc62d75e23613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I need to add the `\input` for the new appendix in main.tex. I'll add it after the last appendix (ddr_causality), before `\end{document}`. But per the task instructions, I should not modify main.tex. Let me re-read the constraint.

The instruction says "不要修改 main.tex". I'll skip that. The user will need to add the `\input` line themselves if they want it compiled.

Wait — the instruction says not to modify main.tex's **headline numbers** (8-gen LOGO F1=0.694 remains primary metric). But the appendix needs to be `\input`'d from somewhere. Let me re-read: "不要修改 main.tex" is explicit. I'll flag this to the user.

Two files updated:

1. **Created** `appendix_9gen_scale.tex` with the 9-generator LOGO table, overall comparison paragraph, Gemma-2-2B anomaly discussion, and scale effect analysis.

2. **Edited** `limitations.tex` line 12 — added the Gemma-2-2B sentence with cross-reference to `Appendix~\ref{app:9gen-scale}`.

**Note:** Per the constraint "不要修改 main.tex", I did not add `\input{appendix_9gen_scale}` to `main.tex`. You'll need to add it manually — suggested location is after line 182 (`\input{appendix_ddr_causality}`), e.g.:

```latex
\input{appendix_9gen_scale}
\FloatBarrier
```

---
