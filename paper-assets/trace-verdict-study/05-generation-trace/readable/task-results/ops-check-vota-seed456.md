# ops check vota seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_vota_seed456_20260515T183240_result.json`
- **Structured JSON:** [`2fc210c182eb64949d4b.json`](../../sessions/2f/2fc210c182eb64949d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。

---

## 结论：原始 vota_seed456 已崩溃（OOM），v2 替代版正在训练中

### 原始 run — vota_seed456 (PID 145908)

| 项目 | 详情 |
|------|------|
| **状态** | **CRASHED — OOM** |
| 启动时间 | May 16 02:25:45 CST |
| 存活时间 | ~3 分钟（TensorBoard 事件止于 02:28） |
| 崩溃原因 | GPU 显存不足（与其他进程共享 GPU）。同参数 vota_seed123 确认相同 OOM 错误：`torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 4.64 GiB` |
| Checkpoint | 无（未保存任何 checkpoint，无 final/ 目录） |
| 退出文件 | 无 `/tmp/agent-ml-exit/vota_seed456.exit` |
| 日志 | 已被 v2 覆盖，原始崩溃日志不可恢复 |

### 替代 run — vota_seed456_v2 (PID 146592)

| 项目 | 详情 |
|------|------|
| **状态** | **RUNNING** |
| PID | 146592 |
| 启动时间 | May 16 02:31:32 CST |
| 运行位置 | tmux session, pane %3 |
| GPU | cuda:1 (`CUDA_VISIBLE_DEVICES=1`)，41191 MiB / 97887 MiB，98% 利用率 |
| 当前进度 | step 15/444 (3.4%)，~17.5s/step |
| 预计完成 | ~04:40 CST（约 2 小时后） |
| 修复措施 | 加了 `--gradient_checkpointing`，独占 GPU 1 |
| W&B run name | `vota_seed456_v2` |
| 日志 | `/root/runs/trace-verdict-study/vota_seed456.log` |
| 命令 | `python train/train_sft.py --condition vota --gradient_checkpointing --gpu 0 --seed 456 --output_dir .../vota_seed456 --wandb_project trace-verdict-study --wandb_run_name vota_seed456_v2` |

### GPU 状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|----------|--------|------|
| 0 | 71595/97887 MiB | 87% | PID 144517 |
| 1 | 41191/97887 MiB | 98% | PID 146592 (vota_seed456_v2) |

### Registry 更新建议

- `vota_seed456` (PID 145908): 标记 **CRASHED**，原因 OOM
- 新增 `vota_seed456_v2` (PID 146592): **RUNNING**，cuda:1，output_dir 同 vota_seed456

---
