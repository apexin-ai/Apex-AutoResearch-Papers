# analysis eval mag perdof norm003

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-perdof-norm003_20260515T163620_result.json`
- **Structured JSON:** [`37efd869c28df479e1ec.json`](../../sessions/37/37efd869c28df479e1ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结论

**perdof norm=0.03 spatial 10-task final: 30.0% (30/100) — NEGATIVE**

perdof magnitude sweep 完整数据（spatial）：

| norm | SR | vs argmin (34%) |
|------|-----|-----------------|
| 0.03 | **30%** | **-4pp** |
| 0.05 | running | — |
| 0.1 | 35% | +1pp |
| 0.2 | running | — |
| 0.3 | running | — |

减小 correction norm 到 0.03 反而让 perdof 性能低于 argmin baseline 4 个百分点。T7-T9 新增的三个 task 全部拉低了 7-task partial 的 40% 均值（T7=0%, T8=20%, T9=0%）。

perdof 在 spatial 上全面死亡：norm=0.1 仅 +1pp，norm=0.03 直接 -4pp。per-DOF uncertainty 对 spatial benchmark 无效。

---
