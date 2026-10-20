# ops collect cka heatmap results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_cka_heatmap_results_20260518T163015_result.json`
- **Structured JSON:** [`57a1d9ce3b27c9bfcffe.json`](../../sessions/57/57a1d9ce3b27c9bfcffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 CKA heatmap 计算已完成。汇总如下：

## E3 CKA Heatmap 结果

| Method | Diagonal CKA Mean | Min | Max |
|--------|-------------------|------|------|
| **CKA-only** (Dense vs CKA-only pruned) | **0.6202** | 0.3794 | 0.9921 |
| **Standard** (Dense vs Standard pruned) | **0.9039** | 0.8412 | 0.9926 |
| **Random** (Dense vs Random pruned) | **0.9233** | 0.7668 | 0.9960 |
| **RASP** (Dense vs RASP pruned) | **0.8822** | 0.7574 | 0.9934 |

产出文件：
- `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_heatmap_cka_only.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_heatmap_standard.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_heatmap_random.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/cka_heatmap_rasp.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/e3_cka_heatmap.pdf` (39KB, 4-method 合并 heatmap)

关键发现：CKA-only 的 diagonal CKA 极低（mean=0.62），说明纯 CKA 剪枝后模型内部表征与 Dense 偏离严重。Standard 和 Random 保留表征最好（0.90, 0.92），RASP 居中（0.88）。

---
