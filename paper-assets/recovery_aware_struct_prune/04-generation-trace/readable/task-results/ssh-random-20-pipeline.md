# ssh random 20 pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_random_20_pipeline_20260521T025836_result.json`
- **Structured JSON:** [`923e07764958fd3aa579.json`](../../sessions/92/923e07764958fd3aa579.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT 正常训练中，约 1 it/s，1870 steps 预计 ~31 分钟。

汇报：

**已完成：**
- `pruned_random_20/` — 在 westd-29022 上 prune 完成（6.09B params, 20.07% sparsity, seed=42）
- 修复了 `model_utils.py` 中两个 bug：
  1. 字段名不匹配：`per_layer_num_heads` → `per_layer_num_attention_heads`
  2. `head_dim` 计算时序错误：移到 `config.num_attention_heads` 更新之后

**正在运行：**
- SFT 训练（westd-29022 GPU 0, PID 314466）：1870 steps, ~1 it/s, 预计 ~30 分钟后完成
- 日志：`/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20.log`

**下一步：** SFT 完成后提交 GRPO（`train_grpo_v5.py`, 100 steps），然后 eval。

---
