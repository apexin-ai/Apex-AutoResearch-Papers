# check westb available models

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_available_models_20260518T094750_result.json`
- **Structured JSON:** [`49b0b28c6d56fa791962.json`](../../sessions/49/49b0b28c6d56fa791962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westb-23072 上的模型清单：

**Dense model**
- `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` ✅

**Pruned models (未训练)**
| 路径 | 说明 |
|------|------|
| `pruned_cka_only_20/` | CKA-only 剪枝 20% |
| `pruned_gradient_20/` | Gradient 剪枝 20% |
| `pruned_magnitude_20/` | Magnitude 剪枝 20% |
| `pruned_random_20/` | Random 剪枝 20% |
| `pruned_rasp_25/` | RASP 剪枝 25% |
| `pruned_rasp_30/` | RASP 剪枝 30% |
| `pruned_rasp_rlvr_20/` | RASP-RLVR 剪枝 20% |
| `pruned_standard_25/` | Standard 剪枝 25% |
| `pruned_standard_30/` | Standard 剪枝 30% |

**SFT checkpoints**
| 路径 | 说明 |
|------|------|
| `sft_cka_only_20/` | CKA-only 20% SFT |
| `sft_gradient_20/` | Gradient 20% SFT |
| `sft_random_20/` | Random 20% SFT |
| `sft_rasp_25/` | RASP 25% SFT |
| `sft_rasp_rlvr_20/` | RASP-RLVR 20% SFT |
| `sft_standard_25/` | Standard 25% SFT |

**GRPO checkpoints**
| 路径 | 说明 |
|------|------|
| `grpo_cka_only_20/` | CKA-only 20% GRPO |
| `grpo_random_20/` | Random 20% GRPO |
| `grpo_rasp_25/` | RASP 25% GRPO |

所有路径前缀均为 `/root/autodl-tmp/recovery_aware_struct_prune/`。

---

**你要找的 5 个模型全部不在 westb 上：**

| 需要的模型 | westb 状态 |
|-----------|-----------|
| `grpo_standard_20` / `grpo_standard_20_fair` | ❌ 没有（只有 25% 的 `grpo` 没有 standard 20%） |
| `grpo_rasp_20` / `grpo_stage2_rasp_20_v9` | ❌ 没有（只有 `grpo_rasp_25`） |
| `sft_standard_20` | ❌ 没有（只有 `sft_standard_25`） |
| `sft_rasp_20` | ❌ 没有（只有 `sft_rasp_25`） |
| `grpo_unpruned_v2` | ❌ 没有 |

westb 上有的是另一批实验（25%/30% sparsity 以及 cka_only/gradient/random/rasp_rlvr 等 ablation 变体），核心的 20% standard/rasp GRPO/SFT checkpoint 都只在 westd-11672 上。

---
