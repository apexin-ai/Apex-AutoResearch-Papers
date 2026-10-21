# ops t10a060 kill d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_t10a060-kill-d102_20260522T191507_result.json`
- **Structured JSON:** [`4d08a1e8ba3c41728b21.json`](../../sessions/4d/4d08a1e8ba3c41728b21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 5 skipped (no gen_11+ to restore). Phase 6 — results:

---

## 1.4B T=10 α=0.60 s42 — D102 5-Method Analysis

**11 generations (gen_0–gen_10)**

### PermG Forward vs Reverse
| | Forward (canary→downstream) | Reverse (downstream→canary) |
|---|---|---|
| FDR sig | **4/8** | **0/8** |

Clear asymmetry: canary leads downstream, not vice versa. **No sync-dip at 1.4B.**

### K≥3 Consensus (robust pairs)
**3/8** — all ECE-based:
- `ece→distinct_1`: 3/5 [naive, diff, perm]
- `ece→distinct_2`: 3/5 [naive, diff, perm]
- `ece→distinct_3`: 3/5 [naive, diff, perm]

Token_entropy pairs max out at 2/5.

### FDR p-values (PermG forward)
| Pair | F-stat | p_fdr | sig |
|---|---|---|---|
| token_entropy→distinct_1 | 1996.8 | 0.040 | * |
| token_entropy→distinct_2 | 834.6 | N/A | |
| token_entropy→distinct_3 | 270.8 | N/A | |
| ece→distinct_1 | 1177.7 | N/A | * |
| ece→distinct_2 | 1308.1 | N/A | * |
| ece→distinct_3 | 511.3 | N/A | * |
| *→mauve | N/A | N/A | (insufficient data) |

### Drift
- Threshold onset: **0/8** pairs significant (no pair crosses true_3sigma_d105 threshold in both canary and downstream within 11 gens)
- TY Granger: **0/8** (SVD convergence issues due to short series)

### Key Finding
**1.4B does NOT show the sync-dip seen in 410M at α=0.60 T=10.** The 410M had PermG=0/8; the 1.4B has PermG=4/8 fwd, 0/8 rev — a clear canary-leads-downstream signal. Scale appears to suppress the sync-dip phenomenon at this operating point.

---
