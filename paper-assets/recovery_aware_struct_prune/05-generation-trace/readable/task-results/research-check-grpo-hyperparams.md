# research check grpo hyperparams

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_grpo_hyperparams_20260523T184142_result.json`
- **Structured JSON:** [`ade20c820ba75428c90d.json`](../../sessions/ad/ade20c820ba75428c90d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRPO max_completion_length 审计

脚本默认值: `train_grpo_v5.py --max_completion_length default = 512` (第191行)

Table 1 使用的成功实验（killed 的原始版本已排除）：

| 实验 | exp_id | 命令中显式设置? | 实际值 | 备注 |
|------|--------|---------------|--------|------|
| CKA-only GRPO 20% | grpo_cka_only_20 | **Yes** (1024) | **1024** | |
| Standard GRPO 20% | grpo_standard_20_fair | **Yes** (1024) | **1024** | |
| RASP α=1.0 GRPO 20% | grpo_rasp_20_fair | **No** | **512** | 使用脚本默认值 |
| Random GRPO 20% | grpo_random_20 | **No** | **512** | 使用脚本默认值 |

**不一致?: Yes**

**具体差异:** CKA-only 和 Standard 显式设了 `--max_completion_length 1024`，而 RASP 和 Random 未设置该参数，使用脚本默认值 512。Reviewer 怀疑方向正确但猜反了对象——不是 Random 用默认值 512 vs Standard 用 1024，而是 **RASP 和 Random 都用了 512，CKA-only 和 Standard 用了 1024**。

此外，这两组实验的其他超参也不一致：CKA-only 和 Standard 显式设了 `--temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit`，而 RASP 和 Random 全部使用脚本默认值。论文声称 "identical GRPO hyperparameters" 不成立。

---
