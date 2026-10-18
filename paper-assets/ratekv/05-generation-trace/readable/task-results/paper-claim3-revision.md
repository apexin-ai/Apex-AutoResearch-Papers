# paper claim3 revision

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim3_revision_20260514T204030_result.json`
- **Structured JSON:** [`f4e8c02bdf4590bafeca.json`](../../sessions/f4/f4e8c02bdf4590bafeca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Summary of changes across four files:

**analysis.tex** (§5.1 + §5.2):
- Yi-1.5 concentration updated 0.49 → 0.71 (hires); the old threshold-based claim is replaced by mechanism-based analysis
- Added Yi-1.5 case study: L4H3 2-bit delta=13.12 (24× gap), 4-bit/8-bit deltas ≈ 0 → no cross-bitwidth gradient
- Contrasted with Qwen L0H0 multi-bitwidth gradient → spread pattern
- Table: added $t_1/t_5$ column, Shape column (Spread/Spike/Flat); Llama/Mistral/Gemma-2 marked $^\ddagger$ (standard profiling, hires pending)
- Diagnostic framework: concentration + shape joint diagnosis with three patterns; t1/t5 ≈ 0.70 as illustrative boundary
- All quantitative claims tagged with `%exp_id=`

**abstract.tex**: Yi-1.5 now described as "highest concentration (0.71)" with spike/spread mechanism; "joint heterogeneity diagnostic" replaces old phrasing

**introduction.tex**: Updated diagnostic description (lines 42-44) and contribution #3 to reference joint diagnostic with $t_1/t_5$ ratio

**conclusion.tex**: Rewritten lines 6-9 with concentration + shape framing, Yi-1.5 as critical test case ($0.71 > 0.61$ yet counterproductive)

Float32 appendix note was already present (appendix.tex line 29-30).

---
