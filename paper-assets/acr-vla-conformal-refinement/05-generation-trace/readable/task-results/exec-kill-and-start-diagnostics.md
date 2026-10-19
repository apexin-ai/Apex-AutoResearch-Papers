# exec kill and start diagnostics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_kill-and-start-diagnostics_20260514T174719_result.json`
- **Structured JSON:** [`67f7a322c464b4f0a3d3.json`](../../sessions/67/67f7a322c464b4f0a3d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，总结：

| 项目 | 状态 |
|------|------|
| eval-scalar-unc-spatial-v2 (PID 197324) | **已 kill** |
| eval-obs-only-spatial-v3 (PID 211961) | **已 kill** |
| `evaluate.py --max_correction_norm` | **已添加并验证** |
| eval-argmin-only-spatial (bjb1:1, PID 231421) | **RUNNING**, GPU1 99% utilization |
| eval-tiny-correction-spatial (bjb1:2, PID 232815) | **RUNNING**, GPU2 21% (加载中) |

GPU 0 和 3 上的 eval-acr-spatial-v3 / eval-acr-object-v3 未受影响，继续运行。

---
