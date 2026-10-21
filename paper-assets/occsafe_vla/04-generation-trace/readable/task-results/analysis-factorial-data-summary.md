# analysis factorial data summary

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_factorial-data-summary_20260527T010746_result.json`
- **Structured JSON:** [`588793edf773fda702c8.json`](../../sessions/58/588793edf773fda702c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/factorial_summary.md` 并注册。

**结果摘要：**

| Cell | Condition | n | CAR | TSR | vs Vanilla |
|------|-----------|---|-----|-----|------------|
| 1 | Full OCC BN | 3 | 0.725±0.064 | 0.854±0.052 | -2.0pp |
| 2 | Full OCC LN | 1 | 0.740 | 0.842 | -0.5pp |
| 3 | Detach BN | 4 | 0.767±0.024 | 0.908±0.026 | +2.2pp |
| 4 | Detach LN | 1 | 0.802 | 0.886 | +5.7pp |
| — | Vanilla | 3 | 0.745±0.024 | 0.878±0.032 | baseline |

**ROADMAP 一致性：全部 5 个 cell 的 n 和 CAR mean±std 与 ROADMAP 完全一致，无差异。**

待完成：34685 上 4 个训练跑完后将新增 Cell 1 n=4、Cell 3 n=5、Cell 4 n=2/3。

---
