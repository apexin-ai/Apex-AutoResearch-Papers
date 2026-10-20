# code hmm lag aware

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hmm-lag-aware_20260514T174023_result.json`
- **Structured JSON:** [`c363d518aebd7f7a0b81.json`](../../sessions/c3/c363d518aebd7f7a0b81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All deliverables complete. Summary:

**Lag-Aware HMM — Final Results**

| Method | MV-conf≥2 F1 | Delta vs Old HMM |
|--------|-------------|-----------------|
| MV baseline | 0.8946 | — |
| TWV | 0.9003 | — |
| Old HMM | 0.7502 | — |
| **Lag-HMM** | **0.8936** | **+0.1434** |

Key design decisions:
- **Lag offsets**: cmd_rep=-2, file_diff=-1, outcome_bp=+7 (from `DEFAULT_LAG_PROFILES`)
- **Confidence anchoring**: conf≥2 windows fixed to MV labels during EM E-step — prevents stagnation drift
- **MAP prior on A** (strength=5000) — stabilizes transition matrix
- **Pi fixed** at [0.285, 0.715] from data distribution
- **Posterior threshold=0.3** — empirically optimal; lower threshold enriches stagnation training signal for conf=1 windows (thresh=0.8 with better distribution match actually hurt probe performance: 0.8475 vs 0.8936)

The lag-aware HMM eliminates the old HMM's catastrophic stagnation overpredict (53.2% → 41.2% stag), recovering conf≥2 F1 to within 0.1pp of the MV baseline. TWV remains the best TLM method at 0.9003.

---
