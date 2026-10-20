# ops westd model inventory

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_model_inventory_20260518T145038_result.json`
- **Structured JSON:** [`c455bc39ba906fda2eef.json`](../../sessions/c4/c455bc39ba906fda2eef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整模型（有 model weights + config + tokenizer）

**GRPO 模型：**
| 目录 | 大小 | Checkpoints |
|---|---|---|
| `grpo_stage2_rasp_20_fair` | 46G | final + ckpt-80, 90, 100 |
| `grpo_stage2_standard_20_fair` | 61G | final + ckpt-80, 90, 100 |
| `grpo_standard_20_extended_300` | 91G | final + ckpt-280, 290, 300 |
| `grpo_cka_only_20` | 23G | final + ckpt-100 |
| `grpo_rasp_25` | 22G | final + ckpt-100 |
| `grpo_standard_25` | 22G | final + ckpt-100 |
| `grpo_unpruned_v2` | 29G | final + ckpt-100 |

**SFT 模型：**
| 目录 | 大小 |
|---|---|
| `sft_cka_only_20` | 12G |
| `sft_rasp_20_westd` | 12G |
| `sft_qwen_math_rasp_20` | 12G |
| `sft_qwen_math_standard_20` | 12G |
| `sft_rasp_25` | 11G |
| `sft_qwen_math_rasp_25` | 11G |
| `sft_qwen_math_standard_25` | 11G |
| `sft_rasp_rlvr_20_qwen_math` | 12G |

**Pruned 模型（含 pruning_metadata.pt）：**
| 目录 | 大小 |
|---|---|
| `pruned_rasp_20` | 12G |
| `pruned_standard_20` | 12G |
| `pruned_qwen_math_rasp_20` | 12G |
| `pruned_qwen_math_standard_20` | 12G |
| `pruned_rasp_25` | 11G |
| `pruned_standard_25` | 11G |
| `pruned_rasp_25_qwen_math` | 11G |
| `pruned_standard_25_qwen_math` | 11G |
| `pruned_rasp_rlvr_20_qwen_math` | 12G |

## 不完整/空目录

| 目录 | 问题 |
|---|---|
| `sft_standard_20_westd` (12K) | 只有 config.json, generation_config.json, chat_template.jinja，**缺 model.safetensors** |
| `sft_standard_25` (0) | 空目录 |
| `sft_unpruned_baseline` (0) | 空目录 |
| `pruned_rasp_rlvr_20` (0) | 空目录 |
| `grpo_rasp_25_transfer_log` (0) | 空目录（日志目录） |

## /root/autodl-tmp/ 顶层

| 目录 | 大小 |
|---|---|
| `recovery_aware_struct_prune/` | 482G |
| `models/` | 0 (空) |
| `models_ms/` | 0 (空) |

## 磁盘

```
总量: 619G | 已用: 482G | 可用: 138G | 使用率: 78%
```

---
