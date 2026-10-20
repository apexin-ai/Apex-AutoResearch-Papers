# check 15pct sft seeds and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_15pct_sft_seeds_and_eval_20260521T173620_result.json`
- **Structured JSON:** [`e3250a7c0da6aea1f81b.json`](../../sessions/e3/e3250a7c0da6aea1f81b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**15% SFT 多种子 checkpoint 不存在。**

westd-29022 上检查结果：

| 路径 | 存在 |
|------|------|
| `sft_cka_only_15` | 有（单种子） |
| `sft_standard_15` | 有（单种子） |
| `sft_cka_only_15_seed123/456` | 无 |
| `sft_standard_15_seed123/456` | 无 |
| `pruned_cka_only_15` | 有（单种子） |
| `pruned_standard_15` | 有（单种子） |
| `/root/runs/` 下 sft*15* | 无 |

前置的 pruned 模型也只有单种子，所以即使要补 SFT 多种子，需要先跑 pruning（不同 seed）→ SFT → eval 全链路。当前无法直接跑 GSM8K eval。

westd-29022 cuda:0 空闲待分配。

---
