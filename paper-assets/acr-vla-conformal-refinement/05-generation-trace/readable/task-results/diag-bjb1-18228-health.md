# diag bjb1 18228 health

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-18228-health_20260517T225908_result.json`
- **Structured JSON:** [`8f9b968a73bd4c948ff8.json`](../../sessions/8f/8f9b968a73bd4c948ff8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成：

- **服务器健康**，4x RTX 4090，Driver 580.105.08 / CUDA 13.0
- **GPU 0**: 占用 — evaluate crm_obs_only (PID 713405, ~7h)
- **GPU 1**: 空闲
- **GPU 2**: 空闲
- **GPU 3**: 占用 — evaluate crm_perdof (PID 749547, ~2h)
- **PID 476529, 449068**: 均已死亡，cron 记录需清理
- **可用 GPU: 1, 2**，可安全提交新实验

报告已写入 `artifacts/diag_bjb1_18228.md`。

---
