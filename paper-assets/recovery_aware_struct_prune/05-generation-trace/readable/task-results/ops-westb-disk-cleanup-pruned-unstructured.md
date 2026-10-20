# ops westb disk cleanup pruned unstructured

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_pruned_unstructured_20260519T105308_result.json`
- **Structured JSON:** [`c43a2d2e3f989aac9130.json`](../../sessions/c4/c43a2d2e3f989aac9130.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- 已删除 `pruned_unstructured_20/`，释放 15GB
- 当前可用：**38GB** / 250GB（85% 使用率），seed123 checkpoint (~12GB) 空间充足
- 无 `.tmp` / `.bak` / `optimizer.pt` 临时文件

**其他大型目录（均 ~12GB，未删除）：**

| 目录 | 大小 |
|---|---|
| sft_rasp_rlvr_20/ | 12G |
| sft_random_20/ | 12G |
| sft_gradient_20/ | 12G |
| sft_cka_only_20/ | 12G |
| pruned_standard_20/ | 12G |
| pruned_rasp_rlvr_20/ | 12G |
| pruned_rasp_20/ | 12G |
| pruned_random_20/ | 12G |
| pruned_cka_only_20/ | 12G |
| grpo_cka_only_20/ | 12G |

这些目录每个 12GB，如后续需要更多空间可考虑清理已完成评估的 checkpoint。

---
