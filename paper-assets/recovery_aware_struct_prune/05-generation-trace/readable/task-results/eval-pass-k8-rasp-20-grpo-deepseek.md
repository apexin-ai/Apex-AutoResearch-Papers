# eval pass k8 rasp 20 grpo deepseek

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_pass_k8_rasp_20_grpo_deepseek_20260516T230148_result.json`
- **Structured JSON:** [`c1251a263d08a0c6683f.json`](../../sessions/c1/c1251a263d08a0c6683f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Checkpoint 在 westb-23072 上（`grpo_stage2_rasp_20_v9`），不在 westd-11672。

**Checkpoint 不存在于 westd-11672。**

DeepSeek RASP 20% post-GRPO checkpoint 位于 **westb-23072**：
- `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/`（~12GB, model.safetensors）

westd-11672 上可用的 GRPO checkpoint：
| 路径 | 说明 |
|------|------|
| `grpo_rasp_qwen_math` | RASP Qwen Math |
| `grpo_rasp_25_qwen_math` | RASP 25% Qwen Math |
| `grpo_rasp_25` | RASP 25% |
| `grpo_rasp_rlvr_20_qwen_math` | RASP RLVR 20% Qwen Math |
| `grpo_standard_v8_step50` | Standard v8 step50 |
| `grpo_standard_qwen_math` | Standard Qwen Math |
| `grpo_standard_25_qwen_math` | Standard 25% Qwen Math |
| `grpo_standard_25` | Standard 25% |
| `grpo_unpruned_v2` | Unpruned v2 |

**选项：**
1. 从 westb 传输 `grpo_stage2_rasp_20_v9` 到 westd（~12GB，需要时间）
2. 直接在 westb-23072 cuda:0 上跑评估（checkpoint 已在本地）

如何处理？

---
