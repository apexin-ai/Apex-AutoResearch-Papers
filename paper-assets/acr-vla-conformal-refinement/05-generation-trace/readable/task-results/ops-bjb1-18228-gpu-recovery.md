# ops bjb1 18228 gpu recovery

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-18228-gpu-recovery_20260515T051701_result.json`
- **Structured JSON:** [`3e57390d03f81b4f210a.json`](../../sessions/3e/3e57390d03f81b4f210a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验**已经在运行中**，无需重新提交。

当前状态（所有 session 创建于今天 13:14）：

| tmux session | GPU | 进程状态 |
|---|---|---|
| eval-argmin-only-spatial-r2 | cuda:0 | `evaluate.py --mode reconvla --start_task 9` 运行中 |
| eval-acr-spatial-v4-scalar-r2 | cuda:1 | `evaluate.py --mode crm_scalar --start_task 3` 运行中 |
| eval-acr-spatial-v4-small-r2 | cuda:2 | `evaluate.py --mode acr_vla --start_task 7` 运行中 |
| eval-acr-spatial-v4-obs-only-r3 | cuda:3 | `evaluate.py --mode crm_obs_only --start_task 6` 运行中 |

GPU 内存占用 2-4.6 GB，utilization 20-24%，4 个 evaluate.py 进程均活跃。磁盘空间充足（根分区 34%，数据盘 46%）。

与任务描述的唯一差异：output_file 路径用的是 `~/runs/` 下的 log 路径而非 `logs/eval_spatial_*` 路径，GPU 分配顺序略有不同，但实验参数完全一致。

这些实验看起来是刚被提交不久（~3 分钟前），已经在正常运行。

---
