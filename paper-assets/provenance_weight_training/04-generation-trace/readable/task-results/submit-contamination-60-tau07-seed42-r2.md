# submit contamination 60 tau07 seed42 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_contamination_60_tau07_seed42_r2_20260516T020831_result.json`
- **Structured JSON:** [`198ea0b7ec052fef15c8.json`](../../sessions/19/198ea0b7ec052fef15c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动确认：

- **PID**: 282223（实际 python 进程），cuda:0 占用 **46514 MiB**
- **参数**: `alpha_eff=0.7`（即 tau=0.7 ✓），`n_min` 体现为 ESS 下界约 2.0-4.0 ✓
- **进度**: step 18/6103，速度 ~2.23s/it，预计 ~3h46m 完成
- **加权正常**: b 值在 0~0.9 范围波动，weighted_loss > unweighted_loss（高 contamination 样本被上权）

训练已稳定运行。

---
