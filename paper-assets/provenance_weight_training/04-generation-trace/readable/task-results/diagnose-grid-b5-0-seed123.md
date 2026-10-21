# diagnose grid b5 0 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grid_b5_0_seed123_20260514T113757_result.json`
- **Structured JSON:** [`79452d6219e8cca65e3c.json`](../../sessions/79/79452d6219e8cca65e3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

- **根因**：SIGHUP（信号 1）— tmux session 管理冲突导致进程被终止，非 OOM/CUDA/代码问题
- **训练进度**：在 step 552/6103（9%）被中断，训练指标正常
- **最后 checkpoint**：`checkpoint-500`，含完整模型文件
- **当前状态**：on_failed hook 已自动重试第 3 次（PID 94717），GPU cuda:3 正在正常训练
- **无需手动干预**，建议确认当前运行是否从 checkpoint 恢复

报告已保存至 `artifacts/grid_b5_0_seed123/report/diagnose_grid_b5_0_seed123.md`。

---
