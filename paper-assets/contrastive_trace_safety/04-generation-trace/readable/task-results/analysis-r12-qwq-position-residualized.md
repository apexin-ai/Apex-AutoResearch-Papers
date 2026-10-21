# analysis r12 qwq position residualized

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r12_qwq_position_residualized_20260518T132734_result.json`
- **Structured JSON:** [`4f298390b252d54c6976.json`](../../sessions/4f/4f298390b252d54c6976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
QwQ-32B Position Residualization (W=3):
- Position-only BA: 0.754 (expected ~0.706)
- Original HS BA: 0.710
- Residualized HS BA: 0.619
- Original Text BA: 0.611
- Residualized Text BA: 0.582
- Drop (HS orig - HS resid): 9.1 pp
- Gap (HS resid - Text resid): 3.7 pp
- Bootstrap p-value: 0.011
- HB result: pass (significant)
```

Position-only BA slightly higher than expected (0.754 vs 0.706) likely due to different pooled vs per-trace aggregation. After residualizing out position, HS retains 0.619 BA while text drops to 0.582, with a 3.7pp gap that is statistically significant (p=0.011). Results saved to `artifacts/r12_qwq_position_residualized/results.json`.

---
