# verify plan018 s43 config

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan018-s43-config_20260514T095225_result.json`
- **Structured JSON:** [`2e7e70324da6fb21b00c.json`](../../sessions/2e/2e7e70324da6fb21b00c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### num_generations 对比

| 文件 | num_generations |
|------|:-:|
| `plan018_random_b01_s43.yaml` | **8** ✓ |
| `plan018_random_b01_s44.yaml` | **8** ✓ |
| `grpo_additive_random_b01.yaml` (s42) | **8** ✓ |

三个文件一致，均为 8。

### s43 config 完整内容

```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_random
output_dir: /root/autodl-tmp/outputs/plan018_additive_random_b01_s43
num_steps: 500
per_device_batch_size: 4
gradient_accumulation_steps: 2
num_generations: 8
max_completion_length: 512
learning_rate: 1.0e-6
beta: 0.1
seed: 43
solver: prover9
no_wandb: true
```

关键参数确认：
- `reward_mode: additive_random` ✓
- `beta: 0.1` ✓
- `seed: 43` ✓
- `data_path: data/train_500_seed42.jsonl` ✓（符合 C001）
- `output_dir: /root/autodl-tmp/outputs/plan018_additive_random_b01_s43` ✓

---
