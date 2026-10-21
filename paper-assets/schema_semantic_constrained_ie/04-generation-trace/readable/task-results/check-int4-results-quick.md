# check int4 results quick

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_int4-results-quick_20260523T053356_result.json`
- **Structured JSON:** [`5e4ac55eb9cd78d75d46.json`](../../sessions/5e/5e4ac55eb9cd78d75d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments already registered with metrics. Here's the FP16 vs INT4 comparison:

| Model | Precision | DR% | CF% | R-F1 | E-F1 | ΔDR | ΔCF | ΔR-F1 | ΔE-F1 |
|-------|-----------|-----|-----|------|------|-----|-----|-------|-------|
| Qwen3-8B | FP16 | 0.00 | 1.18 | 43.77 | 67.05 | — | — | — | — |
| Qwen3-8B | INT4 | 0.00 | 1.10 | 41.71 | 67.05 | 0.00 | −0.08 | −2.06 | 0.00 |
| Llama-3.1-8B | FP16 | 0.09 | 0.46 | 45.47 | 67.76 | — | — | — | — |
| Llama-3.1-8B | INT4 | 0.00 | 0.94 | 43.98 | 67.54 | −0.09 | +0.48 | −1.49 | −0.22 |

**Key findings:**

- **Constraint enforcement preserved**: DR stays at 0% for both INT4 models (Llama even improves from 0.09%→0%). No structural violations introduced by quantization.
- **R-F1 degradation modest**: Qwen drops 2.06 points, Llama drops 1.49 points — both within acceptable range for 4x compression.
- **E-F1 nearly unchanged**: Qwen identical (67.05%), Llama −0.22pp.
- **CF% mixed**: Qwen slightly improves (−0.08pp), Llama slightly worsens (+0.48pp) — both remain low.

Hypothesis confirmed for both: INT4 quantization does not significantly affect constraint enforcement.

---
