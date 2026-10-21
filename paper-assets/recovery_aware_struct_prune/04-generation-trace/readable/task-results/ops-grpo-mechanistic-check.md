# ops grpo mechanistic check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_grpo-mechanistic-check_20260515T020640_result.json`
- **Structured JSON:** [`23c3b791c15519f26889.json`](../../sessions/23/23c3b791c15519f26889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## GRPO Stage 2 Mechanistic 数据检查报告

### 1. 训练状态

| 项目 | grpo_stage2_rasp_20 (GPU 0) | grpo_stage2_standard_20 (GPU 1) |
|------|---|---|
| 进程 | PID 263893 (python), 存活 | PID 263971 (python), 存活 |
| GPU 利用率 | 100%, 581W | 100%, 581W |
| VRAM | 31 GB / 98 GB | 87.5 GB / 98 GB |
| 进度 | **0/500 steps** | **0/500 steps** |
| 启动时间 | 09:14:51 | 09:14:51 |
| W&B run | `ve3er9un` | `mqu3sg7j` |

**两个训练已运行约 1 小时，仍在 step 0 的生成阶段。** 这是正常的——GRPO 首 step 需要对 batch 中每个 sample 生成 `num_generations=4` 条最多 `max_completion_length=4096` tokens 的 completion，单 GPU 非常慢。

VRAM 差异显著：RASP 模型 31GB vs Standard 模型 87.5GB，说明 RASP 剪枝确实大幅缩小了模型有效参数量。

### 2. 已确认会记录的 Mechanistic 指标（TRL GRPOTrainer 内置）

从 TRL 源码（`grpo_trainer.py`）确认，以下指标会自动记录到 W&B：

| 指标 | 说明 |
|------|------|
| `reward` | batch 平均 reward |
| `reward_std` | reward 标准差 |
| `rewards/{func_name}/mean` | 每个 reward function 的平均值 |
| `kl` | 与 reference model 的 KL divergence |
| `clip_ratio` | PPO-style clipping ratio |
| `clip_ratio/low_mean`, `low_min` | 低端 clipping 统计 |
| `clip_ratio/high_mean`, `high_max` | 高端 clipping 统计 |
| `clip_ratio/region_mean` | clipping 区域比例 |
| `completions/mean_length` | 平均生成长度 |
| `completions/min_length` | 最短生成长度 |
| `completions/max_length` | 最长生成长度 |
| `num_tokens` | 总 token 数 |
| `loss`, `grad_norm`, `learning_rate` | 标准训练指标 |
| completions 原文 | `log_completions=True` 启用 |

**关键发现：`beta=0.0`（默认值，代码未显式设置）**——KL divergence 会被记录但不会惩罚 loss。这意味着 GRPO 实际上运行的是纯 reward-maximization 模式。

### 3. 缺失的 Mechanistic 指标（需训练完成后补充分析）

| 缺失指标 | 如何补充 |
|----------|---------|
| 每层 gradient norm 分布 | 从 checkpoint 加载模型，forward+backward 一个 batch 后逐层统计 |
| 与 SFT 基线的 weight divergence | 加载 SFT 和 GRPO checkpoint，计算逐层 L2 distance |
| Reward 分布直方图 | W&B 有 mean/std，但需要从 completions 日志重建完整分布 |
| Token-level entropy | 需要从 checkpoint 重新推理计算 |
| EOS 生成模式分析 | 从 `completions/` 目录的保存数据分析 EOS 位置分布 |

### 4. Checkpoint 状态

两个输出目录目前仅有空的 `completions/` 文件夹，无 checkpoint。`save_steps=200`，预计第一个 checkpoint 在 step 200 时保存。由于 `save_total_limit=2`，最终只保留 2 个 checkpoint（会包含 optimizer states，因为 GRPOTrainer 默认保存）。

### 5. 训练健康状态

**尚无法判断。** 还未产出第一个 step 的指标输出。clipped_ratio 和 grad_norm 需等到 step 10（`logging_steps=10`）才会首次记录。建议 1-2 小时后再次检查。

---
