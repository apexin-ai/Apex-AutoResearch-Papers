# ssh check westb models for math500

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westb_models_for_math500_20260521T123943_result.json`
- **Structured JSON:** [`639e4ea4ceb141bb7ee7.json`](../../sessions/63/639e4ea4ceb141bb7ee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westb-23072 上可用模型汇总（`/root/autodl-tmp/recovery_aware_struct_prune/` 下）：

### Base 模型
| 路径 | 大小 |
|------|------|
| `models/DeepSeek-R1-Distill-Qwen-1.5B/` | 3.4G |

### 7B 剪枝模型（20% / 25%）
| 路径 | 大小 |
|------|------|
| `pruned_standard_20/` | 12G |
| `pruned_standard_25/` | 11G |
| `pruned_cka_only_20/` | 12G |
| `pruned_rasp_20/` | 12G |
| `pruned_rasp_rlvr_20/` | 12G |
| `pruned_cka_only_20_qwen_math/` | 12G |
| `pruned_standard_20_qwen_math/` | 12G |

### 7B SFT 恢复模型
| 路径 | 大小 |
|------|------|
| `sft_cka_only_20/` (根目录) | 12G |
| `sft_standard_25/checkpoint-1870/` | 12G |
| `sft_rasp_rlvr_20/checkpoint-1870/` | 12G |
| `sft_qwen_math_cka_only_20/checkpoint-935/` | 12G |
| `sft_qwen_math_cka_only_20_final/` | 12G |
| `sft_standard_20_qwen_math/checkpoint-935/` | 12G |
| `sft_standard_20_qwen_math_final/` | 12G |

### 7B GRPO 模型
| 路径 | 大小 |
|------|------|
| `grpo_cka_only_20/checkpoint-100/` | 12G |
| `grpo_cka_only_20_seed123/` (根目录) | 12G |
| `grpo_standard_25_westb/checkpoint-100/` | 11G |
| `grpo_random_20/` | （无 model.safetensors）|

### 1.5B 系列
| 路径 | 大小 |
|------|------|
| `pruned_standard_20_1p5b/` | — |
| `pruned_cka_only_20_1p5b/` | — |
| `pruned_rasp_20_1p5b/` | — |
| `sft_cka_only_20_1p5b/` | — |
| `sft_standard_20_1p5b/` | — |
| `sft_rasp_20_1p5b/` | — |
| `grpo_cka_only_20_1p5b/checkpoint-100/` | — |
| `grpo_standard_20_1p5b/` | 2.8G |
| `grpo_rasp_20_1p5b/checkpoint-100/` | — |

共 **27 个含 model.safetensors 的模型路径**可用于 MATH-500 eval。

---
