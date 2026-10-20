# ops check all training status

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_training_status_20260516T024256_result.json`
- **Structured JSON:** [`230ff7fbd368141ab705.json`](../../sessions/23/230ff7fbd368141ab705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个 PID 存活，4 张 GPU 满载。汇总如下：

| 实验 | GPU | PID | 存活? | 进度 | 预估剩余 | 异常 |
|------|-----|-----|-------|------|----------|------|
| **contamination_60_tau07_seed42** | 0 (80%) | 282218/282223 | ✅ | 923/6103 (15%) | ~3h10m | 无。进程正常运行，PREPARING 状态不准确 |
| **grid_b0_3_seed42** | 1 (99%) | 274304 | ✅ | 2341/6103 (38%) | ~2h13m | 无 |
| **contamination_60_ess_only_seed42** | 2 (99%) | 265012 | ✅ | 5375/6103 (88%) | ~26min | 无，最快完成 |
| **detect_remove_baseline_seed42** | 3 (99%) | 276739 | ✅ | 1746/6103 (29%) | ~2h34m | 无 |

关键信息：
- 4 张 NVIDIA RTX PRO 6000 (98GB)，每张占用 ~46.5GB，GPU 利用率 80-99%
- 所有实验速度约 2.1-2.2 s/it
- **contamination_60_tau07_seed42** 已正常训练中（step 923），PID 282218 是 bash wrapper，282223 是实际 python 进程，状态正常
- **contamination_60_ess_only_seed42** 预计最先完成（~26 分钟后）

---
