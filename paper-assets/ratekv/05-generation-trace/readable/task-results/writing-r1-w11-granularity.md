# writing r1 w11 granularity

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r1_w11_granularity_20260515T050144_result.json`
- **Structured JSON:** [`b208c7d5cfabaa0b611d.json`](../../sessions/b2/b208c7d5cfabaa0b611d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`\subsection{Granularity Tradeoff}` already exists at lines 82–91 of analysis.tex. It covers all four points from the task:

- **Layer-level** (KVmix, KVTuner): search space small but within-layer variance lost; Qwen L0 heads cited (6.74, 0.66, 2.12, 1.31)
- **Per-head** (ours): 27.3% improvement on Qwen, H profiling passes, cardinality constraint amortizes cost
- **Token-level** (ZipCache, KIVI): finest grain but runtime overhead; orthogonal to per-head
- **Summary**: per-head is the sweet spot for static allocation

All four required citations are present. The section is ~150 words. No changes needed — the content already matches the reviewer request.

---
