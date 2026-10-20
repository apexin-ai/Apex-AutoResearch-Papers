# analysis exp gemma2b depth

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_gemma2b_depth_20260520T093926_result.json`
- **Structured JSON:** [`a608d746ea38ba853815.json`](../../sessions/a6/a608d746ea38ba853815.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 均已更新。

```
CONCLUSION: negative
K*: 1
KEY_METRICS:
  0v1: AUC = 0.9534 ± 0.003
  1v2: AUC = 0.5981 ± 0.008  ← borderline, 3/5 folds > 0.60
  2v3: AUC = 0.5342 ± 0.013
  3v4: AUC = 0.5030 ± 0.003  (chance)
  4v5: AUC = 0.5026 ± 0.013  (chance)
SUMMARY: Gemma-2-2B 在 C4 上 K*=1，1v2 AUC=0.5981 刚好低于 0.60 阈值（差 0.0019），属于 borderline negative。未能复现其他 5 个 family 的 K*=2，削弱了 "C4 ceiling is architecture-independent" 的 claim——但差距极小，可能需要讨论 threshold sensitivity 或将 Gemma 归为 competence-limited（类似 OLMo 在某些条件下的表现）。
```

---
