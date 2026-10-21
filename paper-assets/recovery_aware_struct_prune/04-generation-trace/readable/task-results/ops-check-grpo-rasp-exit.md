# ops check grpo rasp exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-grpo-rasp-exit_20260514T213532_result.json`
- **Structured JSON:** [`1ca0cfa606d6f14f4fe5.json`](../../sessions/1c/1ca0cfa606d6f14f4fe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 `DONE / negative`，cron 不存在（可能已被清除）。

**结论：grpo_rasp_20_fast 是负面结果。** 核心问题是 pruned model 生成的 completions 全部退化——hit max_length 1024，输出重复无意义字符（`. . . .`），几乎无正确答案。GRPO 需要组内 reward 方差来计算 advantage，但当 97.5-100% 的 completions reward 都是 0 时，advantage=0，loss=0，grad_norm=0，模型完全没有更新。

尽管 RASP pruned model post-prune 有 29% GSM8K accuracy（greedy decode），GRPO 的 sampling 配置下模型无法产生任何有效 completion 来启动学习。

---
