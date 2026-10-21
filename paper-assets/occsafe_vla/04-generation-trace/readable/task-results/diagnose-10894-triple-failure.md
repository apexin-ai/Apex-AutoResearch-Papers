# diagnose 10894 triple failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_triple_failure_20260526T180601_result.json`
- **Structured JSON:** [`4b056c5ea49cc3eb3ad0.json`](../../sessions/4b/4b056c5ea49cc3eb3ad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/diag_10894_triple_failure.md`。

**根因：磁盘满 (ENOSPC)**。三个实验几乎同时到达 step 20000 触发 checkpoint 保存（每个 ~15GB），数据盘 250GB 已有 154GB 旧 checkpoints，并发写入 ~45GB 导致磁盘满。三个实验各自在 `save_training_checkpoint()` 的不同子步骤崩溃。reverse_cutoff_s2_v2 因 checkpoint 保存时间错开而未受影响。

**不能直接重试**。当前剩余 75GB 仍不够三个实验后续所有 checkpoint。需要先：
1. 删除三个残缺的 20000_chkpt（~5-10GB）
2. 清理不再需要的旧 checkpoints（目标释放 ≥60GB）——需要你确认 `full_occ_ln_s0`、`cutoff_15k_s1` 等旧实验的 checkpoint 是否可删
3. 然后从 10000_chkpt resume 重启

---
