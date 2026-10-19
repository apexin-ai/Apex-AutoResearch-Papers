# ops p0 obs only norm02 seed44 r4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-obs-only-norm02-seed44-r4_20260516T144807_result.json`
- **Structured JSON:** [`a04791c6be5c1d0a380b.json`](../../sessions/a0/a04791c6be5c1d0a380b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。

**Task 1 — P0 部署成功：**
- `eval-obs-only-object-norm02-seed44-r4` 已在 bjb1-18228 cuda:2 启动
- PID 501425 占用 5020MiB 显存，进程正常运行
- Registry 已更新（RUNNING, PID=501420, hypothesis 已填写）

**Task 2 — seed45 PID 已补录：**
- `eval-obs-only-object-norm01-seed45` 主进程 PID=474319，运行在 cuda:0，已跑 ~5h47m
- Registry pid 字段已更新为 474319

**当前 bjb1-18228 GPU 分布：**
| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | obs-only-norm01-seed45 | 474319 | 4717MiB |
| cuda:1 | perdof-seed44 | 452987 | 2392MiB |
| cuda:2 | **obs-only-norm02-seed44-r4** (新) | 501425 | 5020MiB |
| cuda:3 | argmin-seed44-r2 | 428122 | 1887MiB |

---
