# maintenance disk cleanup 20260522

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_maintenance_disk_cleanup_20260522_20260522T082743_result.json`
- **Structured JSON:** [`0c567f181329b744a83b.json`](../../sessions/0c/0c567f181329b744a83b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。磁盘从 59GB → 102GB 可用（释放 ~43GB）。

**已删除的中间 checkpoint**：
- `bs16_uniform_seed456`: 12G → 1.2G
- `bs16_adaptive_tau07_seed456`: 12G → 1.2G
- `contamination_60_adaptive_seed123_tau08`: 12G → 1.2G（有 final/）
- `ngram_adaptive_seed123`: 4.6G → 1.2G（有 final/）
- `dr_epoch_matched_seed123_r2`: 12G → 1.2G（有 final/）

**跳过未删除**：
- `detect_remove_q05_v2_seed123_r2`, `random_reweight_v2_seed456`（RUNNING）
- `gpt2_adaptive_seed456`, `detect_remove_q05_seed42`, `rho06_tau07_seed123`（无 final/，状态不确定）

任务中提到的 failed 实验（`detect_remove_q05_v2_seed123`, `dr_epoch_matched_seed123`）目录已不存在，无需处理。

---
