# ssh w4 death rate cis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w4-death-rate-cis_20260518T070411_result.json`
- **Structured JSON:** [`97ee9646e9ec9914465c.json`](../../sessions/97/97ee9646e9ec9914465c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results (from `death_decomposition_report.json`, 30 tasks, 249 matched episodes):

**Per-task death rate differential:**
- 28/30 tasks are death-prone
- **15/28 statistically significant** (95% CI for Delta excludes 0)
- **13/28 non-significant** (all have n=5, power issue)
- **100% directional consistency**: internal DR > deterministic DR in ALL 28 death-prone tasks (no exceptions)

**Pooled analysis:**
- Internal DR: 49.0% [42.8%, 55.2%]
- Deterministic DR: 11.6% [8.2%, 16.2%]
- Delta: **+37.3% [+29.7%, +44.4%]** (highly significant)

**Interpretation for "death dominance is universal across tasks" claim:**
The direction is 100% consistent (internal always worse), strongly supporting universality. The 13 tasks that don't reach individual significance all have n=5, where detecting a 40pp difference requires extreme rates. This is a power limitation, not evidence against the claim. The pooled effect is unambiguous.

Output: `artifacts/w4_death_rate_cis.md` (includes per-task table, forest plot data, and summary).

---
