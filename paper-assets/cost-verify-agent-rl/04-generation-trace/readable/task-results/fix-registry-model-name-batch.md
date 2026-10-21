# fix registry model name batch

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_registry_model_name_batch_20260521T160121_result.json`
- **Structured JSON:** [`ca06efe7bd9228691113.json`](../../sessions/ca/ca06efe7bd9228691113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 9 个实验更新成功。汇总如下：

| 实验 ID | 更新前 model_name | 更新后 model_name |
|---------|------------------|------------------|
| `exp029_seed4_v2` | Qwen2.5-1.5B-Instruct | Qwen3-1.5B (qwen3_exp021_ragen_sft_v4) |
| `exp029_seed5_v2` | Qwen2.5-1.5B-Instruct | Qwen3-1.5B (qwen3_exp021_ragen_sft_v4) |
| `exp029_seed6_v3` | Qwen2.5-1.5B-Instruct | Qwen3-1.5B (qwen3_exp021_ragen_sft_v4) |
| `exp029_seed7` | Qwen2.5-1.5B-Instruct (qwen3_exp021_ragen_sft_v4) | Qwen3-1.5B (qwen3_exp021_ragen_sft_v4) |
| `exp029_seed8` | Qwen2.5-1.5B-Instruct (qwen3_exp021_ragen_sft_v4) | Qwen3-1.5B (qwen3_exp021_ragen_sft_v4) |
| `exp029_seed6_ood_eval_v2` | Qwen2.5-1.5B-Instruct (episode GRPO seed=789, step 15) | Qwen3-1.5B (episode GRPO seed=789, step 15) |
| `exp029_seed5_ood_eval` | Qwen2.5-1.5B-Instruct (episode GRPO seed=456, step 10, partial training) | Qwen3-1.5B (episode GRPO seed=456, step 10, partial training) |
| `sft_baseline_ood_eval_v2` | *(空)* | Qwen3-1.5B SFT (qwen3_exp021_ragen_sft_v4) |
| **`exp029_seed6_ood_eval`** *(额外发现)* | Qwen2.5-1.5B-Instruct (episode GRPO seed=789, step 15) | Qwen3-1.5B (episode GRPO seed=789, step 15) |

额外检查：`exp029_seed6_ood_eval`（v2 的前身，已 failed）也标了 Qwen2.5，已一并修正。除此之外没有其他遗漏的 exp029 相关实验。

---
