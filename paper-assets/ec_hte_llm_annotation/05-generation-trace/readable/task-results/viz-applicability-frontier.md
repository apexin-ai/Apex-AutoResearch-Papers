# viz applicability frontier

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_applicability-frontier_20260521T131949_result.json`
- **Structured JSON:** [`3ae7aa5d652b66da945d.json`](../../sessions/3a/3ae7aa5d652b66da945d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The plot looks good. The key story is clear:

- **Green zone** (bottom-right): EC-HTE benefits when budget per subgroup is high (n/K > ~50–250) and classifier quality is decent (worst misclass < 0.30)
- **Red zone** (top-left): EC-HTE fails with poor classifiers (FNR > 0.5, exp-015) or insufficient budget (n/K = 12.5, exp-013)
- **Yellow zone**: transitional region where HB and Global are comparable

Key thresholds annotated:
- `n_expert/K = 25` vertical dashed line (budget threshold from exp-013)
- `worst FNR = 0.5` horizontal dotted line (classifier quality threshold from exp-015)
- Crossover points: K=2 at n/K ≈ 50, K=4 at n/K ≈ 250

Output saved to `artifacts/figures/applicability_frontier.{pdf,png}` (300 dpi PNG, 350 KB).

---
