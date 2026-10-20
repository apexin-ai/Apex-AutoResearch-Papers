# code disk cleanup and 8b config

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_disk-cleanup-and-8b-config_20260516T025407_result.json`
- **Structured JSON:** [`676467ac291bed7657a4.json`](../../sessions/67/676467ac291bed7657a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。

## 汇总

### 任务 1：磁盘清理

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 227G | 137G |
| 可用 | 24G | 114G |
| **释放** | — | **90GB** |

删除的 checkpoint 目录（共 6 个）：

| 目录 | checkpoint | 大小 |
|------|-----------|------|
| plan001_exec_only_s43_1000_r2 | checkpoint-1000 | 16G |
| plan001_exec_only_s44_1000_r2 | checkpoint-1000 | 16G |
| plan002_additive_b01_s43_r2 | checkpoint-500 | 16G |
| plan002_additive_b01_s45 | checkpoint-50 | 15G |
| plan018_additive_random_b01_s43_r3 | checkpoint-500 | 16G |
| plan018_additive_random_b01_s44_r2 | checkpoint-500 | 16G |

sweep_isr_b01_s45 和 sweep_isr_b005_s42 未动。无 parquet 文件需清理。

### 任务 2：8B pilot 配置

最终 `configs/grpo_exec_only_8b.yaml`：

```yaml
model_path: /root/autodl-tmp/models/Qwen3-8B
data_path: data/train_500_seed42.jsonl
reward_mode: execution_only
output_dir: /root/autodl-tmp/outputs/w2_qwen3_8b_pilot
num_steps: 50
per_device_batch_size: 4
gradient_accumulation_steps: 4
num_generations: 8
max_completion_length: 512
learning_rate: 1.0e-6
exec_weight: 1.0
sta_weight: 0.0
seed: 42
solver: prover9
no_wandb: true
save_strategy: "no"
```

变更：`per_device_batch_size` 2→4，`save_total_limit: 1` 替换为 `save_strategy: "no"`。

---
