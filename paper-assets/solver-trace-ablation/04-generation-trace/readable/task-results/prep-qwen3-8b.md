# prep qwen3 8b

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_qwen3-8b_20260521T232523_result.json`
- **Structured JSON:** [`be49066cba90eb02e005.json`](../../sessions/be/be49066cba90eb02e005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## Qwen3-8B 模型准备结果

### 1. 模型已下载
`/root/autodl-tmp/models/Qwen3-8B/`，包含 config.json + 5 个 safetensors 分片，**16GB**。下载于 5 月 16 日，完整可用。

### 2. 现有 8B 配置（3 个）

| 配置文件 | reward_mode | K (num_generations) | max_completion_length | optim | 其他 |
|---------|-------------|----|----|------|------|
| `grpo_exec_only_8b.yaml` | execution_only | 4 | 384 | adamw_bnb_8bit | gradient_checkpointing=true |
| `grpo_isr_b01_8b.yaml` | additive_bonus (beta=0.1) | 4 | 384 | adamw_bnb_8bit | gradient_checkpointing=true |
| `grpo_additive_bonus_b01_8b.yaml` | additive_bonus (beta=0.1) | **2** | **512** | adamw_bnb_8bit | gradient_checkpointing=true |

共同设置：`per_device_batch_size=1, gradient_accumulation_steps=16, lr=1e-6, seed=42, num_steps=500, data=train_500_seed42.jsonl, solver=prover9`

### 3. 显存估算（单卡 RTX PRO 6000 Blackwell, 98GB）

Qwen3-8B full-parameter GRPO with `adamw_bnb_8bit` + `gradient_checkpointing`:
- 模型 weights (bf16): ~16 GB
- 8-bit Adam optimizer states: ~8 GB（比 full Adam 的 32GB 省 4x）
- Gradients (bf16): ~16 GB
- Activations (gradient checkpointing 大幅降低): ~4-8 GB
- KV cache for rollouts (K=4, max_len=384): ~4-6 GB
- **总计约 48-54 GB for K=4**

**K=8 估算**: rollout 显存翻倍 → ~56-66 GB，仍在 98GB 之内。K=8 可行，但 `generation_batch_size` 也要设为 8，峰值可能到 ~70 GB。

现有配置已选保守的 **K=4**，在 98GB 卡上有充裕余量，是稳妥选择。

### 4. 代码兼容性
- `train_grpo.py` 已支持 `gradient_checkpointing`、`bf16`、`adamw_bnb_8bit`、`save_total_limit` 等所有 8B 所需参数，无需代码改动。

### 5. 磁盘风险 ⚠️
数据盘 **238G/250G 已用 96%**，仅剩 **13GB**。8B 模型单个 checkpoint ~16GB，**当前磁盘空间不足以保存一个 checkpoint**。训练前必须清理磁盘（至少释放 30-40GB）。

---
