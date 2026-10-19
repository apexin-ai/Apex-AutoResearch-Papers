# analysis pi05 adaptive goal s42 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-adaptive-goal-s42-cqa1_20260526T104759_result.json`
- **Structured JSON:** [`d01cee9ad70424221f96.json`](../../sessions/d0/d01cee9ad70424221f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已记录。

**pi05-adaptive-goal-s42-cqa1 分析结果**

- **Overall SR**: 89.5% (179/200) — 比 VLA-only baseline ~96% 退化 ~6.5pp，符合 K=2 argmin 选择的预期退化
- **Trigger rate**: 8.1% (mean_unc=0.1152)
- **Per-task SR**: 4 个任务 100%，2 个 85-95%，2 个 90%/95%，2 个偏低 70% (open_drawer 类)
- **错误/warning**: 无错误；只有 robosuite/vision tower 的预期 warning
- **Conclusion**: `success` (SR ≥ 85%，4090 cluster 数据成功控制 Blackwell 架构偏差)

---
