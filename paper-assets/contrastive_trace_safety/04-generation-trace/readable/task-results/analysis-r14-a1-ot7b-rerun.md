# analysis r14 a1 ot7b rerun

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a1_ot7b_rerun_20260518T170819_result.json`
- **Structured JSON:** [`152b04b3671b2e4fe979.json`](../../sessions/15/152b04b3671b2e4fe979.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

```
OT-7B BA Layer Sweep (max_iter=2000, 60/20/20):
Layer BA curve: L0=0.839, L1=0.869, L2=0.886, L3=0.876, L4=0.867, L5=0.881, L6=0.858, L7=0.830, L8=0.821, L9=0.842, L10=0.843, L11=0.826, L12=0.836, L13=0.847, L14=0.848, L15=0.838, L16=0.849, L17=0.839, L18=0.856, L19=0.871, L20=0.868, L21=0.874, L22=0.870, L23=0.873, L24=0.873, L25=0.876, L26=0.885, L27=0.884
BA-optimal: L2 (ba=0.8862)
BA range: max-min = 6.5pp

HS vs Text on BA-optimal layer L2:
| Metric | HS     | Text   | Delta   | p_raw  | adj_p  | HB? |
|--------|--------|--------|---------|--------|--------|-----|
| Prec   | 0.5369 | 0.3481 | +0.1849 | 0.0000 | 0.0000 | Y   |
| BA     | 0.7379 | 0.6577 | +0.0802 | 0.0057 | 0.0057 | Y   |
| FPR    | 0.1367 | 0.2701 | -0.1334 | 0.0001 | 0.0002 | Y   |
| AUROC  | 0.9061 | 0.7210 | +0.1851 | 0.0000 | -      | -   |
HB pass: 3/3
```

**L2 is NOT a convergence artifact.** With max_iter=2000, L2 remains BA-optimal (0.886 vs 0.877 at max_iter=500). All layers improved uniformly (+0.8 to +2.1pp) but rankings unchanged. The major improvement is in final probe quality: HS AUROC jumped from 0.732 (max_iter=500) to 0.906 (max_iter=2000), a +17pp gain, while text AUROC also improved 0.604 to 0.721. HB significance strengthened to 3/3 (was already 3/3 but margins widened).

---
