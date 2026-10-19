# diag acib v3 train status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_acib_v3_train_status_20260515T233816_result.json`
- **Structured JSON:** [`c488b752339e3b197c11.json`](../../sessions/c4/c488b752339e3b197c11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## acib_v3_train 状态报告

### 训练进程 (PID 497308)
- **状态**: 正常运行中，已从之前的卡死状态恢复（Worker 成功 kill + 重启）
- **启动时间**: 2026-05-16 07:27 (北京时间)，已运行 ~33 分钟
- **当前进度**: Step 2100/20000 (10.5%)
- **训练速度**: 1.2 steps/s，稳定
- **预计 ETA**: ~4.1 小时后完成（约 11:30 北京时间）
- **日志**: `/root/runs/action_cond_info_bottleneck/acib_v3_train.log`

### 训练指标（正常）
| 阶段 | Steps | β | IB loss | Task loss |
|------|-------|---|---------|-----------|
| 预热前 | 100-1000 | 0.0000 | 0.06→0.02 | 0.05-0.09 |
| β 预热 | 1100-2000 | 0.001→0.01 | ~0.001 | 0.06-0.11 |
| 正式训练 | 2100 | 0.01 | ~0.0 | 0.067 |

### 注意事项
- **wandb 未配置**（wandb_project 和 wandb_run_name 为空字符串），无法远程监控
- config 写 `--gpu 0` 但实际在物理 GPU 1 上（可能有 CUDA_VISIBLE_DEVICES 映射）

### GPU 使用情况
| GPU | 显存占用 | GPU 利用率 | 进程 |
|-----|---------|-----------|------|
| GPU 0 | 4459/97887 MiB | 0% | PID 471056: baseline_plus eval (libero_goal)，运行 43min |
| GPU 1 | 21612/97887 MiB | 9% | PID 497308: **acib_v3_train** (16216 MiB) + PID 508625: baseline_std eval (5368 MiB) |

### 结论
Worker 已成功完成任务：kill 了卡死的旧进程 → 重启训练。新训练进度正常，loss 收敛趋势健康。两个 baseline eval（baseline_plus 和 baseline_std 的 libero_goal）也在同时运行。

---
