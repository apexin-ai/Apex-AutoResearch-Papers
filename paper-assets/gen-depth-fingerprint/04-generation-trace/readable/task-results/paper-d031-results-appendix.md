# paper d031 results appendix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d031-results-appendix_20260520T112522_result.json`
- **Structured JSON:** [`30206118eb98692b9ef5.json`](../../sessions/30/30206118eb98692b9ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four edits complete:

1. **results.tex W2** (L13): Added "exploratory evaluation" framing to cross-model chains sentence. Transfer evidence at L15 already existed — no duplication.

2. **results.tex N4** (L20): Added sentence positioning 7-feature ensemble as interpretable baseline with 14.3pp QLoRA gap and DDR's contribution as empirical decomposition.

3. **appendix_9gen_scale.tex W1** (L43): Extended Gemma anomaly with (a) architectural mechanism hypothesis (attention + tokenizer) and (b) bounded impact (≤0.011 shift). Omitted (c) Qwen3-14B point since exp_060 status is unverified.

4. **appendix_ddr_validation.tex W4** (L57–86): Added ε sensitivity analysis — compact table of critical thresholds per feature + summary paragraph confirming 3/1/3 partition stability across ε ∈ [0.10, 0.75] with entropy std as sole boundary feature (gap = 0.21 between adjacent zones).

---
