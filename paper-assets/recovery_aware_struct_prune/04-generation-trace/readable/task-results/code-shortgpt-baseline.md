# code shortgpt baseline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_shortgpt_baseline_20260519T132458_result.json`
- **Structured JSON:** [`59ea53b61d481488b8b0.json`](../../sessions/59/59ea53b61d481488b8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

**`src/prune_shortgpt.py`** 已部署到 westd-29022 并通过端到端验证。

### 脚本功能
实现 ShortGPT (Men et al., 2024) depth pruning：用 forward hook 捕获每层 input/output hidden states，计算 Block Influence = 1 - cos_sim，删除 BI 最低的层（保留首尾层）。

### 参数
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--model_path` | (必填) | 预训练模型路径 |
| `--pruning_ratio` | 0.2 | 层删除比例 |
| `--calibration_size` | 512 | 校准样本数 |
| `--output_path` | (必填) | 输出路径 |
| `--seed` | 42 | |
| `--dtype` | bfloat16 | |

### Dry-run 结果（calibration_size=8）
- 28 → 23 层，删除 [15, 16, 17, 24, 25]
- 7.62B → 6.45B 参数（15.3% sparsity）
- Forward pass 验证通过
- 保存的模型可正常重新加载（config.layer_types 同步更新）

### SFT/GRPO 兼容性
输出是标准 Qwen2ForCausalLM（只是 `num_hidden_layers=23`），可直接传入现有 `train_sft_warmup.py` 和 `train_grpo_v5.py`，无需任何修改。

---
