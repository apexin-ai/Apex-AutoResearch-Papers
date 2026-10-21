# ops gpu check bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-bjb1-32546_20260518T151321_result.json`
- **Structured JSON:** [`e723d4ef69239b8eb0ff.json`](../../sessions/e7/e723d4ef69239b8eb0ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总 (bjb1-32546, 6× RTX 4090)

| GPU | 显存占用 | GPU-Util | 状态 | 进程 / tmux session |
|-----|---------|----------|------|-------------------|
| **0** | 2 MiB / 24564 MiB | 0% | **空闲** | — |
| **1** | 5202 MiB | 21% | **占用** | PID 642305 - `eval-perdof-object-norm005-seed43` (norm=0.05, seed43) |
| **2** | 5201 MiB | 20% | **占用** | PID 640624 - `eval-perdof-object-norm003-seed43` (norm=0.03, seed43) |
| **3** | 2 MiB / 24564 MiB | 0% | **空闲** | — |
| **4** | 4269 MiB | 22% | **占用** | PID 626277 - `eval_perdof_default_seed45` (default perdof, seed45) |
| **5** | 2 MiB / 24564 MiB | 0% | **空闲** | — |

**3 张 GPU 在跑 eval，3 张空闲：cuda:0, cuda:3, cuda:5。**

tmux session `eval-dc-r2` 无进程运行（已回到 shell prompt），可忽略。另外两个 norm003/norm005 的 tmux pane 输出为空白（进程在后台跑，尚未有 stdout 刷出）。`eval_perdof_default_seed45` 正在跑 object benchmark，当前进度显示 `pick_up_the_salad_dressing` 任务 0/10 成功率。

---
