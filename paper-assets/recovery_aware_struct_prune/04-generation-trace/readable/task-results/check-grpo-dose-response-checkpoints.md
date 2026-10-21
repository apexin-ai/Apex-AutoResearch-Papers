# check grpo dose response checkpoints

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grpo_dose_response_checkpoints_20260523T215104_result.json`
- **Structured JSON:** [`96d387d55193eee155f0.json`](../../sessions/96/96d387d55193eee155f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果如下：

## GRPO Dose-Response Checkpoints 状态

### 20% Sparsity — Alpha 变体

| 模型 | 状态 | 位置 |
|------|------|------|
| grpo_alpha0p5_20 | ❌ 不存在 | westd-32935 无此目录。注意：**westb-23072 有 `grpo_rasp_alpha0p5_20/`**（12.3GB model.safetensors）✅ |
| grpo_alpha2p0_20 | ❌ 不存在 | westd-32935 无此目录。但有 **`grpo_rasp_alpha2p0_20/`**（12.3GB model.safetensors）✅ |
| grpo_alpha4_20 | ✅ 完整 | westd-32935: `grpo_alpha4_20/`（12.3GB model.safetensors） |
| grpo_alpha4_20/checkpoint-100 | ❌ 不存在 | 无子目录 checkpoint |
| grpo_rasp_alpha3p0_20_v2 | ❌ 不完整 | westd-32935: 仅有 README.md + completions/，**无 model.safetensors** |

### 20% Sparsity — 其他 GRPO

| 模型 | 状态 | 位置 |
|------|------|------|
| grpo_random_20 | ❌ 不完整 | westd-32935: 仅有 README + config，**无 model.safetensors** |
| grpo_random_20_retrain | ✅ 完整 | westb-23072: 12.2GB model.safetensors |
| grpo_stage2_rasp_20_fair | ✅ 完整 | westd-32935: 12.3GB model.safetensors |
| grpo_stage2_standard_20_fair | ✅ 完整 | westd-32935: 12.3GB model.safetensors |

### 25% Sparsity

| 模型 | 状态 | 位置 |
|------|------|------|
| grpo_cka_only_25 | ✅ 完整 | westd-32935: 11.6GB model.safetensors |
| grpo_standard_25 | ✅ 完整 | westd-32935: 11.6GB model.safetensors |

### SFT (验证)

| 模型 | 状态 | 位置 |
|------|------|------|
| sft_rasp_alpha0p5_20 | ✅ 完整 | westd-32935: 12.3GB model.safetensors |
| sft_rasp_alpha2p0_20 | ✅ 完整 | westd-32935: 12.3GB model.safetensors |
| sft_alpha4_20 | ✅ 完整 | westd-32935: 12.3GB model.safetensors |
| sft_cka_only_25 | ✅ 完整 | westd-32935: 11.6GB model.safetensors |

### 关键发现

1. **命名差异**：alpha0p5 和 alpha2p0 的 GRPO 版本实际命名为 `grpo_rasp_alpha*`（带 `rasp_` 前缀），不是 `grpo_alpha*`。alpha0p5 在 westb-23072 上，alpha2p0 在 westd-32935 上。
2. **grpo_rasp_alpha3p0_20_v2**：目录存在但模型文件缺失，需重训或重新导出。
3. **grpo_random_20**：westd-32935 上目录不完整（无模型权重），但 westb-23072 上有完整的 `grpo_random_20_retrain`。
4. westb-23072 上无 `grpo_standard_25` 和 `grpo_cka_only_25`（这两个都在 westd-32935 上完整存在）。

---
