# ssh extract conll freeform table33

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_extract_conll_freeform_table33_20260522T134949_result.json`
- **Structured JSON:** [`c16684f546b9f787e88c.json`](../../sessions/c1/c16684f546b9f787e88c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

```
Table 33: CoNLL N=8 T=1.0 seed=42
gold-filtered instances: constrained=2756, freeform=2756

                        Constrained      Free-form        Delta
--------------------------------------------------------------
greedy_f1                  0.908806       0.904588      -0.0042
mv_strict_f1               0.899232       0.899355      +0.0001
mv_delta (pp)                -0.96 pp         -0.52 pp      +0.43 pp
lp_f1                      0.898147       0.895134      -0.0030
lp_delta (pp)                -1.07 pp         -0.95 pp      +0.12 pp
degeneracy_rate               56.9%          60.0%       +3.0 pp
lp_std_ratio               0.025641       0.023466      -0.0022
```

Key observations:
- **greedy_f1** drops 0.42pp without grammar constraints (0.9088 → 0.9046), expected since freeform can produce malformed outputs
- **mv_strict_f1** is virtually identical (~0.8993 both), MV is robust to the constraint removal
- **mv_Δ** improves from -0.96pp to -0.52pp in freeform — MV loses less relative to greedy in freeform
- **lp_f1** drops 0.30pp (0.8981 → 0.8951), LP selection also degrades slightly
- **degeneracy_rate** increases 3pp (56.9% → 60.0%) — freeform produces slightly more degenerate samples
- **lp_std_ratio** decreases (0.0256 → 0.0235) — less logprob spread in freeform, consistent with higher degeneracy

---
