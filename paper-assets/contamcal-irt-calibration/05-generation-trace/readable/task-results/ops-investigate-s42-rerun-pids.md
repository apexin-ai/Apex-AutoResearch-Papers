# ops investigate s42 rerun pids

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate_s42_rerun_pids_20260514T022317_result.json`
- **Structured JSON:** [`fda5a880f7054d7cbff2.json`](../../sessions/fd/fda5a880f7054d7cbff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态
- PID 257853: **已死**
- PID 257034: **已死**

## 决策执行
- **两个都死 → 需重跑**

## 输出目录
`/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/` — **空目录**（仅 `.` 和 `..`，无产出文件）

## GPU 状态
当前 GPU 上运行的进程（均非 s42 rerun）：
| PID | 显存占用 |
|--------|----------|
| 251924 | 10046 MiB |
| 249294 | 8948 MiB |
| 255322 | 3658 MiB |
| 242591 | 8948 MiB |
| 243300 | 5820 MiB |
| 250610 | 5820 MiB |

s42 rerun 两个进程都已退出且未产出任何结果，需要重新启动。

---
