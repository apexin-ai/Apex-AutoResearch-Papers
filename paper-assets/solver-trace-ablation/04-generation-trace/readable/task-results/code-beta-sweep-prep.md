# code beta sweep prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_beta-sweep-prep_20260516T021822_result.json`
- **Structured JSON:** [`4b1db2a6a0f494612cf0.json`](../../sessions/4b/4b1db2a6a0f494612cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 均已释放。

---

## 产出汇总

### 1. 环境验证
| 项目 | 状态 |
|------|------|
| GPU | 2 × RTX PRO 6000 96GB，空闲 |
| PyTorch | 2.10.0+cu128, CUDA=True |
| `train_grpo.py` | 存在 (19KB, May 15) |
| `grpo_additive_bonus.yaml` | 存在，base model=Qwen3-4B |
| `data/train_500_seed42.jsonl` | 存在 (500 examples) |
| `save_total_limit` | 硬编码为 1 (C003 ✓) |

### 2. train_grpo.py CLI 参数
| 参数 | 类型 | 默认值 |
|------|------|--------|
| `--model_path` | str | None (yaml 覆盖) |
| `--data_path` | str | None |
| `--reward_mode` | str | None |
| `--output_dir` | str | None |
| `--num_steps` | int | 100 |
| `--per_device_batch_size` | int | 4 |
| `--gradient_accumulation_steps` | int | 2 |
| `--num_generations` | int | 4 |
| `--max_completion_length` | int | 512 |
| `--learning_rate` | float | 1e-6 |
| `--exec_weight` | float | 0.5 |
| `--sta_weight` | float | 0.5 |
| **`--beta`** | **float** | **0.3** |
| `--beta_schedule` | str | "fixed" |
| `--beta_schedule_midpoint` | int | 250 |
| `--seed` | int | 42 |
| `--solver` | str | None |
| `--logic_type` | str | None |
| `--wandb_project` | str | None |
| `--wandb_run` | str | None |
| `--no_wandb` | flag | False |
| `--warmup_ratio` | float | 0.0 |
| `--config` | str | None |

`--beta` 接受任意 float，dry-run 确认 β=0.05 被正确传入（日志显示 `beta_t=0.0500`）。

### 3. Launch 脚本
**路径**: `/root/solver-trace-ablation/scripts/launch_beta_sweep.sh`

包含 9 条注释掉的命令（3 β × 3 seeds），output_dir 命名：
- `sweep_isr_b005_s{42,43,44}`
- `sweep_isr_b02_s{42,43,44}`
- `sweep_isr_b05_s{42,43,44}`

### 4. Dry-run 结果
**成功**。β=0.05, seed=42, 2 步训练正常完成：
- Step 1: reward=0.13, prove_rate=0.125, isr=0.100, parse_rate=1.0
- Step 2: reward=0.00, prove_rate=0.000, isr=0.000, parse_rate=1.0
- 每步 ~16-21s，loss=0.026, grad_norm=2.77
- Final model save 因 /tmp 根分区空间不足失败（预期内，正式训练输出到 `/root/autodl-tmp/outputs/` 数据盘无此问题）

### 5. 注意事项
- **GPU 0 有活跃进程**（PID 586161, 79GB）——启动 sweep 前需确认该进程身份，避免冲突
- 每个实验约占 ~80GB 显存，**每张 GPU 同一时间只能跑 1 个实验**
- 9 个实验串行需 ~9 × 3h = 27h；双 GPU 并行约 ~15h
- 根分区空间紧张，确保所有 output_dir 指向 `/root/autodl-tmp/outputs/`

---
