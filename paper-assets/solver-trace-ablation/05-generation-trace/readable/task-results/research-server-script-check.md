# research server script check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_server-script-check_20260516T184924_result.json`
- **Structured JSON:** [`ddbe5fe5326c7af28302.json`](../../sessions/dd/ddbe5fe5326c7af28302.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集完毕。以下是结构化结果：

---

## 1. 训练脚本完整参数列表

```
usage: train_grpo.py [-h] [--model_path MODEL_PATH] [--data_path DATA_PATH]
                     [--reward_mode {execution_only,execution_sta,random_reward,additive_bonus,additive_random,execution_fast_sta,isr_gated}]
                     [--output_dir OUTPUT_DIR] [--num_steps NUM_STEPS]
                     [--per_device_batch_size PER_DEVICE_BATCH_SIZE]
                     [--gradient_accumulation_steps GRADIENT_ACCUMULATION_STEPS]
                     [--num_generations NUM_GENERATIONS]
                     [--max_completion_length MAX_COMPLETION_LENGTH]
                     [--learning_rate LEARNING_RATE]
                     [--exec_weight EXEC_WEIGHT] [--sta_weight STA_WEIGHT]
                     [--beta BETA]
                     [--beta_schedule {fixed,linear,sigmoid}]
                     [--beta_schedule_midpoint BETA_SCHEDULE_MIDPOINT]
                     [--isr_threshold ISR_THRESHOLD]
                     [--min_components MIN_COMPONENTS] [--seed SEED]
                     [--solver SOLVER] [--logic_type {fol,prolog}]
                     [--wandb_project WANDB_PROJECT] [--wandb_run WANDB_RUN]
                     [--no_wandb]
                     [--warmup_ratio WARMUP_RATIO] [--optim OPTIM]
                     [--warmup_steps WARMUP_STEPS]
                     [--config CONFIG]
```

关键参数说明：
- `--beta` — additive bonus/random 系数
- `--beta_schedule` — fixed/linear/sigmoid
- `--isr_threshold` — isr_gated 模式阈值 (default 0.3)
- `--warmup_steps` — exec-only warmup 步数 before ISR-gated (default 0)
- `--config` — YAML 配置文件（覆盖 CLI 参数）
- `--save_total_limit` — 在 YAML 中可设（非 CLI 显式列出但 YAML 支持）

## 2. 已有 1.7B 配置文件

**`grpo_exec_only_1.7b.yaml`**:
```yaml
model_path: /root/autodl-tmp/models/Qwen3-1.7B
data_path: data/train_500_seed42.jsonl
reward_mode: execution_only
output_dir: /root/autodl-tmp/outputs/grpo_exec_only_1.7b
num_steps: 500
per_device_batch_size: 2
gradient_accumulation_steps: 4
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
exec_weight: 1.0
sta_weight: 0.0
seed: 42
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: exec_only_1.7b
no_wandb: true
save_total_limit: 1
optim: adamw_torch
```

**`grpo_additive_bonus_b01_1.7b.yaml`**:
```yaml
model_path: /root/autodl-tmp/models/Qwen3-1.7B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_bonus
output_dir: /root/autodl-tmp/outputs/grpo_additive_bonus_b01_1.7b
num_steps: 500
per_device_batch_size: 2
gradient_accumulation_steps: 4
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.1
exec_weight: 1.0
sta_weight: 0.0
seed: 42
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: additive_bonus_b01_1.7b
no_wandb: true
save_total_limit: 1
optim: adamw_torch
```

## 3. 4B Random sweep 配置参考

**`sweep_random_b01_s45.yaml`** (4B model):
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_random
output_dir: /root/autodl-tmp/outputs/sweep_random_b01_s45
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.1
seed: 45
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: sweep_random_b01_s45
```

## 4. 环境验证

- **Python**: `/root/miniconda3/bin/python`, Python 3.12.3
- **激活命令**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**: `/root/autodl-tmp/models/Qwen3-1.7B/` — 存在，含 2 个 safetensors shard

## 5. 1.7B ISR pilot 训练状态

`w2_1.7b_isr_b01_s42` 已完成 500 步，最终 reward ≈ 1.029，epoch=2.0，completion length 收敛到 ~66 tokens。

## 6. 关键差异：1.7B vs 4B 配置

| 参数 | 1.7B | 4B |
|------|------|-----|
| `per_device_batch_size` | 2 | 4 |
| `gradient_accumulation_steps` | 4 | 2 |
| `save_total_limit` | 1 | 未设（默认） |
| `optim` | adamw_torch | 未设（默认） |

有效 batch size 相同：`2×4 = 4×2 = 8`。

---
