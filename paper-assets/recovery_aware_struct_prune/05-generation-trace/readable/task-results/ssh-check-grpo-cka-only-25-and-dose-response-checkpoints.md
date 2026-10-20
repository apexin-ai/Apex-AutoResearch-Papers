# ssh check grpo cka only 25 and dose response checkpoints

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_grpo_cka_only_25_and_dose_response_checkpoints_20260523T194549_result.json`
- **Structured JSON:** [`bd5906daa286d14c685c.json`](../../sessions/bd/bd5906daa286d14c685c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Checkpoint 存在性汇总

### westd-32935（数据盘 650G，已用 577G / 89%）

| Checkpoint | 路径 | 大小 | 存在 |
|---|---|---|---|
| **grpo_cka_only_25** | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25/model.safetensors` | **11G** | **✅** |
| sft_rasp_alpha0p5_20 | `.../sft_rasp_alpha0p5_20/model.safetensors` | 12G | ✅ |
| sft_rasp_alpha2p0_20 | `.../sft_rasp_alpha2p0_20/model.safetensors` | 12G | ✅ |
| sft_alpha4_20 | `.../sft_alpha4_20/model.safetensors` | 12G | ✅ |
| grpo_rasp_alpha0p5_20 | — | — | ❌ 不存在 |
| grpo_rasp_alpha2p0_20 | `.../grpo_rasp_alpha2p0_20/model.safetensors` | 12G | ✅ |
| grpo_alpha4_20 | `.../grpo_alpha4_20/model.safetensors` | 12G | ✅ |

### westb-23072

| Checkpoint | 路径 | 大小 | 存在 |
|---|---|---|---|
| **grpo_cka_only_25** | — | — | **❌ 不存在** |
| sft_rasp_alpha3p0_20 | `.../sft_rasp_alpha3p0_20/checkpoint-935/model.safetensors` | 12G | ✅ |
| grpo_rasp_alpha0p5_20 | `.../grpo_rasp_alpha0p5_20/model.safetensors` | 12G | ✅ |

### 关键发现

- **grpo_cka_only_25**：仅在 **westd-32935** 上存在（11G，May 21），westb-23072 上没有。Director 决策 25% MATH-500 用 westd 上这份即可。
- **grpo_rasp_alpha0p5_20**：仅在 **westb-23072** 上存在（12G，May 23 刚生成），westd 上没有。

---
