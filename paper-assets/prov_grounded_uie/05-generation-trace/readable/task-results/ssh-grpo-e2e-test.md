# ssh grpo e2e test

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-e2e-test_20260512T220128_result.json`
- **Structured JSON:** [`9d7943fe3a4fb06866a7.json`](../../sessions/9d/9d7943fe3a4fb06866a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO Mini-batch 端到端验证报告

### 1. 退出码
**0**（成功完成 2 步训练，模型已保存）

### 2. 完整输出（关键部分）
```
GRPO train samples: 5
Loading checkpoint shards: 100%|██████████| 4/4
  0%|          | 0/2 → 50%|█████ | 1/2 [00:06] → 100%|██████████| 2/2 [00:12]

{'train_runtime': 14.63, 'train_loss': 0.0, 'num_tokens': 2446.0,
 'completions/mean_length': 128.0, 'completions/clipped_ratio': 1.0,
 'rewards/reward_fn/mean': 0.0, 'reward': 0.0, 'kl': 0.0, 'entropy': 0.022}

GRPO model saved to /tmp/grpo_test/final
```

### 3. 验证项

| 验证项 | 结果 | 说明 |
|--------|------|------|
| **vLLM generation** | **失败** | `torch 2.10.0 + vllm 0.17.1` 不兼容：`AssertionError: duplicate template name` (torch._inductor)。用 `--use_vllm False` 绕过，HF 原生 generation 正常 |
| **Reward 函数** | **通过（但值为 0）** | 修复 `parse_json_output` 后不再 crash。reward 全为 0 是因为 `max_completion_length=128` 太短，100% 生成被截断，无法产出完整 JSON |
| **OOM / Crash** | **无** | 2 步训练正常完成，模型保存成功（LoRA adapter 349MB） |

### 4. Reward 值
- `rewards/reward_fn/mean`: **0.0**
- `reward_std`: **0.0**
- `frac_reward_zero_std`: **1.0**（所有 prompt 的多次生成 reward 方差为 0，无学习信号）

原因：`max_completion_length=128` 导致所有生成被截断（`clipped_ratio=1.0`），JSON 不完整，三个 reward 组件全返回 0。正式训练用 `max_completion_length=2048` 应正常。

### 5. 过程中发现并修复的问题

| 问题 | 修复 |
|------|------|
| `--model_path` 参数不存在 | 改用 `--sft_checkpoint` |
| `--max_steps` 不在 GRPOArgs 中 | 已添加到 `config.py` + `train_grpo.py` |
| `gradient_accumulation_steps=8` 导致 sampler 需要 ≥16 样本 | mini-batch 测试用 `--gradient_accumulation_steps 1` |
| `parse_json_output` 不兼容 TRL 1.1.0 chat message 格式 | 已修复：支持 `list[dict]` 输入 |
| vLLM + torch 2.10.0 不兼容 | 暂用 `--use_vllm False`，正式训练需升级 vllm 或降级 torch |

### 6. 正式训练前需处理
1. **vLLM 兼容性**：升级 `vllm` 或降级 `torch`（否则只能用 HF 原生 generation，速度慢很多）
2. **`max_completion_length`**：正式训练设 2048
3. 代码改动（`config.py`, `train_grpo.py`, `rewards.py`）已直接在服务器上修改，需同步回 git

---
