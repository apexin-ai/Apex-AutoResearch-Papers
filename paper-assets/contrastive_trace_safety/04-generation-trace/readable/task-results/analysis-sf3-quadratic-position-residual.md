# analysis sf3 quadratic position residual

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf3_quadratic_position_residual_20260519T143405_result.json`
- **Structured JSON:** [`e24c3f8282584ee742c6.json`](../../sessions/e2/e24c3f8282584ee742c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. All three output files updated. Here's the summary:

**SF3: Linear vs Quadratic Position Residualization**

| Model | Method | HS BA | Txt BA | Gap | p | HB p | Pass |
|-------|--------|-------|--------|-----|---|------|------|
| R1-8B | linear | .658 | .554 | +10.4pp | <.0001 | <.0001 | Y |
| R1-8B | quadratic | .652 | .549 | +10.3pp | <.0001 | <.0001 | Y |
| OT-7B | linear | .697 | .582 | +11.4pp | <.0001 | <.0001 | Y |
| OT-7B | quadratic | .631 | .534 | +9.8pp | .0001 | .0003 | Y |
| R1-32B | linear | .574 | .587 | -1.4pp | .598 | .598 | N |
| R1-32B | quadratic | .594 | .593 | +0.0pp | .499 | .499 | N |
| QwQ-32B | linear | .606 | .598 | +0.9pp | .415 | .831 | N |
| QwQ-32B | quadratic | .630 | .561 | +6.8pp | .046 | .091 | N |

**Validation**: R1-8B and OT-7B linear per-trace HS BAs match exp_r11 reference exactly (to 4 decimal places).

**Key findings**:
- R1-8B and OT-7B retain significant HS advantage under both linear and quadratic residualization (HB pass)
- Quadratic slightly reduces the gap (OT-7B: 11.4 → 9.8pp) but doesn't eliminate it
- R1-32B remains NS under both methods
- QwQ-32B (L63, W=5): linear NS, quadratic marginally significant raw (p=.046) but fails HB correction (p=.091)

**Output files** at `/root/autodl-tmp/contrastive_trace_safety/artifacts/sf3_quadratic_residual/`:
- `results.json` — full results with per-trace BAs
- `comparison_table.csv` — summary table
- `report.txt` — human-readable report

---
