# ops scp models for e3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp_models_for_e3_20260518T153905_result.json`
- **Structured JSON:** [`58b0efb919138662cb5a.json`](../../sessions/58/58b0efb919138662cb5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足。** westb `/root/autodl-tmp` 只剩 7.7GB，需要 ~24GB。

当前 westb 上的大目录一览（`/root/autodl-tmp/recovery_aware_struct_prune/`）：

| 目录 | 大小 | 备注 |
|------|------|------|
| grpo_cka_only_20 | 27G | 最大，可能含多个 checkpoint |
| grpo_rasp_25 | 11G | |
| grpo_standard_20_1p5b | 9.6G | |
| pruned_gradient_20 | 12G | |
| pruned_magnitude_20 | 12G | |
| pruned_rasp_25 | 11G | |
| pruned_rasp_rlvr_20 | 12G | |
| pruned_standard_25 | 11G | |
| sft_* (多个) | 11-12G each | |
| pruned_cka_only_20 | 12G | **E3 需要** |
| pruned_random_20 | 12G | **E3 需要** |

E3 CKA Heatmap 只需要 5 个模型（pruned_standard_20, pruned_rasp_20, pruned_cka_only_20, pruned_random_20, DeepSeek-R1-Distill-Qwen-7B）。

需要你决定删哪些来腾出 24GB 空间。候选：
- `grpo_cka_only_20` (27G) — 如果 westd 上有备份，删它一个就够
- `pruned_gradient_20` + `pruned_magnitude_20` (24G) — 如果 E3 不需要
- 25% 系列（pruned_rasp_25, pruned_standard_25, sft_rasp_25 等）
- 1.5B 系列模型

要删哪些？或者还有其他方案？

---
