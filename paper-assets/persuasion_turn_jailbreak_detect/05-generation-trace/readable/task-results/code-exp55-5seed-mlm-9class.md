# code exp55 5seed mlm 9class

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp55_5seed_mlm_9class_20260522T113202_result.json`
- **Structured JSON:** [`38bc4c56509367c0e584.json`](../../sessions/38/38bc4c56509367c0e584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp55 complete.** Here's the 5-seed summary:

### 9-Class vs MLM Frozen Probing (F1 macro, 5 seeds)

| Metric | 9-Class | MLM | Δ |
|--------|---------|-----|---|
| IID | **1.000 ± 0.000** | 0.982 ± 0.013 | +1.8 pp |
| DD OOD | **0.992 ± 0.011** | 0.988 ± 0.009 | +0.4 pp |
| AA OOD | **0.974 ± 0.012** | 0.957 ± 0.024 | +1.7 pp |
| FITD OOD | **1.000 ± 0.000** | 0.988 ± 0.009 | +1.2 pp |

### Statistical tests on AA OOD
- Paired t-test: t=1.358, **p=0.246** (not significant)
- Wilcoxon: W=2.0, **p=0.188** (not significant)
- 9-class wins 4/5 seeds, but seed 123 favors MLM

### Interpretation

Marked as **negative** — the hypothesis that 9-class produces *significantly* better OOD generalization than MLM is not supported at p<0.05 with 5 seeds. 9-class is directionally better (wins 4/5 seeds, +1.7 pp mean on AA OOD, lower variance), but the frozen probing setup narrows the gap compared to the earlier full-pipeline comparison (where MLM had 0.893 ± 0.08 vs 9-class 0.972 ± 0.026).

Key observation: 9-class has **zero variance on IID and FITD** (perfect scores all 5 seeds), while MLM shows measurable instability. The advantage is clearest on consistency rather than peak performance.

Results saved: `/root/persuasion_turn_jailbreak_detect/results/exp55_5seed_combined.json`

---
