# diag check grpo warmup and status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_check-grpo-warmup-and-status_20260515T193516_result.json`
- **Structured JSON:** [`5d5e26e9bcdf72bd9ce3.json`](../../sessions/5d/5d5e26e9bcdf72bd9ce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Warmup 配置
- **train_grpo_v5.py 中无任何 warmup 参数**（grep 返回空）
- GRPOConfig（行 242-269）未设置 `warmup_ratio` 或 `warmup_steps`
- 使用 TRL/transformers 默认值：**warmup_ratio=0.0, warmup_steps=0**（无 warmup）

### num_generations
- argparse 默认值：**4**（行 194）
- 实际运行命令未指定 `--num_generations`，使用默认值 **4**

### learning_rate
- 实际运行：`--learning_rate 1e-6`

### Standard v8 当前状态
| 指标 | 值 |
|------|-----|
| PID | 534667，已运行 **4h52m** |
| GPU | cuda:0 = 0 MiB (0%), cuda:1 = 71701/97887 MiB (**99%**) |
| 磁盘 | /root/autodl-tmp/ 177G/250G，**剩余 74G (29%)** |
| 当前进度 | completions 到 **step 40**（completions_00040.parquet, May 16 03:23） |
| trainer_state.json | **不存在** |
| wandb 目录 | **不存在** |

### Completions 时间线（估算速度）
| 文件 | 时间 | 间隔 |
|------|------|------|
| completions_00010 | May 15 23:55 | — |
| completions_00020 | May 16 01:04 | ~69 min |
| completions_00030 | May 16 02:15 | ~71 min |
| completions_00040 | May 16 03:23 | ~68 min |

~70 min / 10 steps → **预计 step 50 在 May 16 04:30 左右**。

### checkpoint-50
**尚未保存**（save_steps=50，当前约 step 40）。预计约 1 小时后到达 step 50 并触发首次 checkpoint 保存。

---
