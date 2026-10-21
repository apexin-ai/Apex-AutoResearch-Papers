# code prep b02 config

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-b02-config_20260516T034849_result.json`
- **Structured JSON:** [`9cbd904adb6b298e422a.json`](../../sessions/9c/9cbd904adb6b298e422a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### β=0.2 Config 内容 (`configs/grpo_additive_bonus_b02.yaml`)

```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_bonus
output_dir: /root/autodl-tmp/outputs/plan002_additive_beta02_s42
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 4
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.2
seed: 42
solver: prover9
wandb_project: solver-trace-ablation
wandb_run: additive_bonus_b02
```

与 β=0.1 config 的差异：`beta: 0.1 → 0.2`，`output_dir` 和 `wandb_run` 相应更名。

### Dry-run

YAML 解析成功，所有字段类型正确（`beta` 为 float 0.2，`num_steps` 为 int 500 等）。

### Tmux sessions

| Session | 状态 |
|---------|------|
| `sweep-isr-b005-s42` | **活跃** — GPU 0 占用 ~80GB |
| `sweep-isr-b01-s45` | **活跃** — GPU 1 占用 ~80GB |

两个 session 都有运行中的训练进程，**未清理**。两张 GPU 均被占满，启动 β=0.2 训练需等当前任务完成。

---
