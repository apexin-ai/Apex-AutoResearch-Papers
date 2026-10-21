# ops norm003 fix and diagnose

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_norm003-fix-and-diagnose_20260519T125648_result.json`
- **Structured JSON:** [`a3dcb1720180ffdd2661.json`](../../sessions/a3/a3dcb1720180ffdd2661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 实验 | 状态 | 详情 |
|------|------|------|
| **seed47** (bjb1-32546 GPU3) | **ALIVE**, PID 894900 | 5/10 tasks 完成，预计 ~3.5h 后出结果 |
| **seed48** (bjb1-18228 GPU1) | **ALIVE**, PID 67825 | 5/10 tasks + T6 进行中，略快于 seed47 |
| **seed44-bjb2** (bjb2-28827) | **已成功完成** | SR=17% (10/10 tasks), JSON 在 `/root/logs/`。误标 failed 已修正为 success |

Registry 已更新：seed47-r2 恢复为 RUNNING，seed44-bjb2 conclusion 改为 success。seed47/seed48 的 conclusion=failed 因 registry 不支持 null 值无法清除，已在 notes 中标注为误报。

报告已写入 `artifacts/norm003_diagnosis_report.md`。

---
