# analysis rho03 uniform seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho03_uniform_seed456_20260523T031226_result.json`
- **Structured JSON:** [`469e53c8cbcb2beee3de.json`](../../sessions/46/469e53c8cbcb2beee3de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练未完成 — step 1500/6103 时磁盘满崩溃。**

详情：
- `/root/autodl-tmp` 250GB 100% 占满
- 崩溃错误：`safetensors_rust.SafetensorError: No space left on device (os error 28)`
- checkpoint-1000 有效（3.4GB），可用于恢复训练
- checkpoint-500（3.4GB）和 checkpoint-1500（44KB 损坏）可删

**可清理空间（~92GB）：** 9 个已完成实验（有 `final/`）的中间 checkpoint 可安全删除：
- `rho03_uniform_seed42`, `rho03_uniform_seed123`, `rho03_adaptive_seed42`, `rho03_adaptive_seed123`
- `bs8_nmin4_uniform_seed42`, `bs8_nmin4_adaptive_seed42`
- `detect_remove_q05_v2_seed123_r2`, `uniform_epoch_matched_seed456`, `dr_epoch_matched_seed456`

每个实验 3 个 checkpoint × 3.4GB ≈ 10.2GB。

**建议方案：**
1. 删除上述已完成实验的中间 checkpoint（~92GB）
2. 删除本实验的 checkpoint-500 和损坏的 checkpoint-1500
3. 从 checkpoint-1000 恢复训练到 6103 步
4. 训练完成后再跑 eval

是否继续？还是你想先确认哪些可以删？

---
