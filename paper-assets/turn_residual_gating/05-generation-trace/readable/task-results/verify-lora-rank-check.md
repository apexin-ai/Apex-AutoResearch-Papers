# verify lora rank check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_lora_rank_check_20260520T062536_result.json`
- **Structured JSON:** [`fcc81c5c78d8f91461da.json`](../../sessions/fc/fcc81c5c78d8f91461da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果确认完毕。

## 汇总

**config.py**: `LORA_RANK = 16`

**argparse**: 无 `--lora-rank` 参数（共 20 个参数，无一与 LoRA rank 相关），因此所有实验都使用 config.py 的硬编码值。

**4 个实验 checkpoint 的 adapter_config.json 确认结果：**

| 实验 | checkpoint 路径 | LoRA rank (`r`) | `lora_alpha` | 来源 |
|------|----------------|-----------------|--------------|------|
| v7 TG | `runs/phase2_tg_s42_v7/lora/adapter_config.json` | **16** | 32 | PEFT 保存的配置 |
| UG | `runs/phase2_ug_s42/lora/adapter_config.json` | **16** | 32 | PEFT 保存的配置 |
| LoRA-only | `runs/phase2_lora_only_s42/lora/adapter_config.json` | **16** | 32 | PEFT 保存的配置 |
| v9 PCGrad | `checkpoints/tg_v9_pcgrad_s42/lora/adapter_config.json` | **16** | 32 | PEFT 保存的配置 |

**结论**：所有 4 个实验的 LoRA rank 均为 **16**，不是论文中写的 8。论文需要修正为 rank=16, alpha=32。其他共同配置：target_modules = `[q_proj, v_proj]`，dropout = 0.05。

---
