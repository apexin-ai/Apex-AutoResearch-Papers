# diag contamination 60 random seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_contamination_60_random_seed42_20260518T083805_result.json`
- **Structured JSON:** [`3d84437093f2d0ba4cba.json`](../../sessions/3d/3d84437093f2d0ba4cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：**这是 cron 误报，训练实际已成功完成。**

- **根因**：训练是 resume 启动的，日志写入了 output_dir 下的 `train_resume.log`，而非 cron 监控的 `~/runs/.../contamination_60_random_seed42.log` 路径。且未启用 W&B，所以 cron 判定无 metrics 标记为 failed。
- **训练进度**：6103/6103 steps (100%)，final model 已保存，无任何 error/OOM/traceback。
- **GPU 状态**：cuda:3 空闲（0MiB, 0%），进程已正常退出。
- **无需重跑**，模型完整可用。

报告已写入 `artifacts/diag_contamination_60_random_seed42.md`。

---
