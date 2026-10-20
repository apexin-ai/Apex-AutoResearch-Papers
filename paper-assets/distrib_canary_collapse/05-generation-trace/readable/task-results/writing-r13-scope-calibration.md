# writing r13 scope calibration

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r13_scope_calibration_20260524T161030_result.json`
- **Structured JSON:** [`3d40ed60e3947c157e60.json`](../../sessions/3d/3d40ed60e3947c157e60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Paper compiles successfully. The one undefined reference (`tab:mmct_k_operating`) is the intentional placeholder per task instructions.

Summary of all edits:

1. **introduction.tex W2**: Added "empirically" to "We empirically map this landscape on Pythia-410M"
2. **introduction.tex W9**: Changed C3 from "We formalize cascade ordering" + "Design Principles" to "We empirically validate a cascade ordering" + "Principles"
3. **abstract.tex W5/W10**: "substantially reduces peak perplexity" → "reduces peak perplexity by 64\%" (~180 words, under 200 limit)
4. **experiments.tex W9**: Downgraded both "Design Principle~\ref{...}" references to "Principle~\ref{...}"
5. **experiments.tex R13-VIS1**: Added summary detection table (Table `tab:summary_detection`) after intervention figure
6. **method.tex W7**: Added "Consensus threshold" paragraph with K=3 FPR-TPR trade-off and placeholder table reference
7. **experiments.tex Fig 2 caption W3**: Added "(empirical trend;" and "The sigmoid is a descriptive fit to observed detection rates, not a predictive model."

---
