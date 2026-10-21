# code e1b prune 1p5b v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1b_prune_1p5b_v2_20260518T110237_result.json`
- **Structured JSON:** [`724c0db36c699782755a.json`](../../sessions/72/724c0db36c699782755a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进度可见了：~56 秒/题，9/200 完成。按此速率：
- 单个 eval ≈ 3 小时
- 3 个 eval ≈ 9 小时

这比预期慢很多。DeepSeek-R1 是 thinking model，每题生成很长的推理链（max 4096 tokens）。

Pipeline 在后台稳定运行，当前状态：
- **Step 1a**: Importance scores ✅ (完成)
- **Step 1b**: CKA overlap ✅ (完成) 
- **Step 2a**: Standard pruning ✅ → 1.78B → 1.46B (17.60%)
- **Step 2b**: CKA-only pruning ✅ → 1.78B → 1.45B (18.38%)
- **Step 2c**: RASP pruning ✅ → 1.78B → 1.45B (18.18%)
- **Step 3**: GSM8K eval - standard 模型 9/200 进行中，约 3h 剩余

所有 3 个 pruned model 已保存：
- `/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b`
- `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b`
- `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b`

### Pruning 细节

| 方法 | 原始参数 | 剪后参数 | 实际 sparsity | Attn groups pruned | MLP groups pruned |
|------|----------|----------|---------------|--------------------|--------------------|
| Standard | 1,777M | 1,464M | 17.60% | 0/56 | 91/336 |
| CKA-only | 1,777M | 1,451M | 18.38% | 0/56 | 95/336 |
| RASP | 1,777M | 1,454M | 18.18% | 0/56 | 94/336 |

三种方法都只剪 MLP groups，未触及 attention（1.5B 只有 2 个 KV heads/层，剪一个 GQA group 代价太大）。

Standard 集中剪后半层（layers 15-26，每层 7/12 groups），RASP 和 CKA-only 分布更均匀。

Pipeline 将继续后台运行。Eval 结果预计 ~9 小时后全部完成。需要中断或调整（如减少 max_new_tokens 加速）？

---
