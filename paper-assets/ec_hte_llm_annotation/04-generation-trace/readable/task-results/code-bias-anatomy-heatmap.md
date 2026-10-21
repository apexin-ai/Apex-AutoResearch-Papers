# code bias anatomy heatmap

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bias-anatomy-heatmap_20260523T145856_result.json`
- **Structured JSON:** [`1c17046b7ee36abedbd0.json`](../../sessions/1c/1c17046b7ee36abedbd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Outputs saved to `artifacts/bias_anatomy_heatmap.{pdf,png}`.

**Results:**

| Metric | Value |
|---|---|
| **R² (Theorem 1 vs MC simulation)** | **0.9938** (row-level), 0.9956 (aggregated) |
| **Actual \|bias\| range** | [0.0009, 0.0933] |
| **Theory \|bias\| range** | [0.0002, 0.0893] |
| **Mean absolute residual** | 0.0011 |
| **Contour–data alignment** | Excellent — contours track the MC heatmap closely |
| **Debiasing hurts** | 52% of grid cells (ratio > 1 when δ\_misclass ≥ 0.13) |

**Panel A**: Bias magnitude increases multiplicatively toward the top-right (high δ\_misclass × high Δτ), exactly as Theorem 1 predicts. The 5 white dashed contour lines (0.01–0.15) align tightly with the MC simulation data.

**Panel B**: The bias ratio is purely a function of δ\_misclass (vertical bands), independent of Δτ — consistent with the theory since both bias\_global and bias\_naive scale linearly with Δτ, so it cancels in the ratio. Global correction hurts when δ\_misclass ≥ ~0.13.

---
