# code create random b005 config

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_create-random-b005-config_20260517T044923_result.json`
- **Structured JSON:** [`4900db297722b42cdadb.json`](../../sessions/49/4900db297722b42cdadb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。最终状态：

**`configs/grpo_additive_random_b005.yaml`** — 已创建：
```yaml
model_path: /root/autodl-tmp/models/Qwen3-4B
data_path: data/train_500_seed42.jsonl
reward_mode: additive_random
output_dir: /root/autodl-tmp/outputs/plan017_additive_random_b01_s42
beta: 0.05
seed: 42
# 其余参数与 b01 模板一致
```

**`configs/grpo_additive_bonus_b005.yaml`** — 已存在（ISR β=0.05）：
```yaml
reward_mode: additive_bonus
output_dir: /root/autodl-tmp/outputs/sweep_isr_b005_s42
beta: 0.05
```

注意：新建的 random b005 配置的 `output_dir` 和 `wandb_run` 仍继承自 b01 模板（`plan017_additive_random_b01_s42`）。实际训练时需要更新这两个字段以区分实验。

---
