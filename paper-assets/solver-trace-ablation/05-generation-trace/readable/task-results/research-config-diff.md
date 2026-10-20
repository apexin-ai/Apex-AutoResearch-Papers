# research config diff

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_config-diff_20260521T052747_result.json`
- **Structured JSON:** [`6820b562a19d90abdff4.json`](../../sessions/68/6820b562a19d90abdff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都存在，有 **3 处实质性差异**（均与 beta 值相关）：

| 参数 | `grpo_additive_bonus.yaml` | `grpo_additive_bonus_b01.yaml` |
|------|---------------------------|-------------------------------|
| `output_dir` | `plan002_additive_beta03_s42` | `plan002_additive_beta01_s42` |
| `beta` | **0.3** | **0.1** |
| `wandb_run` | `additive_bonus_b03` | `additive_bonus_b01` |

其余参数完全一致：`model_path`, `data_path`, `reward_mode`, `num_steps`, `per_device_batch_size`, `gradient_accumulation_steps`, `num_generations`, `max_completion_length`, `learning_rate`, `seed`, `solver`, `wandb_project`。

---

**完整文件内容：**

**`grpo_additive_bonus.yaml`**
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_bonus
output_dir: /root/autodl-tmp/outputs/plan002_additive_beta03_s42
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.3
seed: 42
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: additive_bonus_b03
```

**`grpo_additive_bonus_b01.yaml`**
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_bonus
output_dir: /root/autodl-tmp/outputs/plan002_additive_beta01_s42
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.1
seed: 42
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: additive_bonus_b01
```

结论：两个配置唯一的训练超参差异是 **beta: 0.3 vs 0.1**，其余为对应的 output_dir 和 wandb_run 命名差异。

---
