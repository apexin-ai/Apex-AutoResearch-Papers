# analyze traj level seed789

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_traj-level-seed789_20260512T090511_result.json`
- **Structured JSON:** [`03b57dbfd5dede3740e0.json`](../../sessions/03/03b57dbfd5dede3740e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。汇总：

**seed789 结果**: accuracy=87.31, unresolved_f1=88.27, resolved_f1=86.17, consistency=76.74

**4-seed traj-level 汇总**:

| metric | mean±std |
|--------|----------|
| accuracy | 86.46±1.04 |
| unresolved_f1 | 87.87±0.76 |
| resolved_f1 | 84.67±1.54 |
| consistency | 78.52±1.33 |

**t-test (traj-level vs per-test accuracy)**: t=-2.569, df=4.66, **p=0.054** — 边缘不显著。traj-level 一致低于 per-test ~2pp，但 4 seeds 仍不足以在 α=0.05 下拒绝 H₀。需要第 5 seed 将 p 值推过阈值。

---
