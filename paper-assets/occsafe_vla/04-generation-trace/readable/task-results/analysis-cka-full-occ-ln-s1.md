# analysis cka full occ ln s1

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_full_occ_ln_s1_20260525T022941_result.json`
- **Structured JSON:** [`f0210e05eefc01e9574d.json`](../../sessions/f0/f0210e05eefc01e9574d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**cka_full_occ_ln_s1 — 结论 negative**

| 指标 | DINOv2 | SigLIP |
|------|--------|--------|
| Mean CKA | 0.965 | 0.950 |
| Min CKA | 0.923 (block 1) | 0.832 (block 26) |

s0 的 DINOv2 CKA=0.640 在 s1 中未复现（s1 全部 >0.92）。DINOv2 表征漂移是 seed-specific 的偶发现象，不是 OCC+LN 训练的系统性效应。norm×gradient-flow interaction 假说不成立。

---
