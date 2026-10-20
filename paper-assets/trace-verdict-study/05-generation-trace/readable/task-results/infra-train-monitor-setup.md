# infra train monitor setup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_train-monitor-setup_20260514T180346_result.json`
- **Structured JSON:** [`e2a1c1b68b73dc94ef0c.json`](../../sessions/e2/e2a1c1b68b73dc94ef0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都在正常运行。

## 汇报

### 进程状态
| 任务 | PID (wrapper/python) | 已运行 | GPU |
|------|---------------------|--------|-----|
| no_trace | 710523 / 710528 | ~3min | cuda:0 |
| vota | 710601 / 710606 | ~3min | cuda:1 |

### GPU 利用率
| GPU | 型号 | 利用率 | 显存 | 温度 | 功耗 |
|-----|------|--------|------|------|------|
| 0 (no_trace) | RTX PRO 6000 Black | 98% | 81.1/97.9 GB (83%) | 71°C | 461W/600W |
| 1 (vota) | RTX PRO 6000 Black | 100% | 41.2/97.9 GB (42%) | 71°C | 472W/600W |

### 训练进度
| 任务 | 当前 step | 速度 | 预估剩余时间 |
|------|----------|------|-------------|
| no_trace | **64/444** (14.4%) | ~2.7s/step | **~17 min** |
| vota | **8/444** (1.8%) | ~18s/step | **~2.2 hr** |

### Checkpoint
两个目录下尚未生成 checkpoint（只有 `runs/` 子目录），刚开始训练属正常。

### 注意事项
1. **vota 比 no_trace 慢 ~6.7x**（18s vs 2.7s per step）。vota 显存占用也更高（41GB vs 32GB），推测是 vota 条件下 sequence 更长（包含推理 trace），导致计算量大幅增加。
2. 日志中只有进度条，**未看到 loss 值输出**——loss 可能只在 eval step 或 wandb 中记录，当前 step 数还不够触发 eval。
3. `torch_dtype` deprecated warning 无影响，可忽略。
4. tmux 状态无法通过 read_only 检查，但两个任务都是通过 `submit_training_job` 提交的 wrapper 进程，正常运行中。

---
