# analysis finalize 3B d005 s123 sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_finalize-3B-d005-s123-sft_20260515T150831_result.json`
- **Structured JSON:** [`fa576da7858cd0df593e.json`](../../sessions/fa/fa576da7858cd0df593e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务已经完成：

**Step 1 & 2 — SFT 分析 + Registry 更新**: `exp_001_sft_3B_d005_s123` 已经是 **DONE/success** 状态（updated 15:08:45Z），指标已录入：
- final_loss: 1.1349
- final_token_accuracy: 0.7069
- total_steps: 3177
- wall_clock_seconds: 11333.2, gpu_hours: 3.15
- checkpoint_path: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123`

与日志一致（train_loss=1.1349, mean_token_accuracy=0.7069, 3177 steps, runtime=10982s）。

**Step 3 — Eval 提交**: `exp_001_eval_3B_d005_s123_aligned` 已经在 cuda:2 上 **RUNNING**（PID 580698，started 23:06:21，命令完全匹配要求的 eval 参数）。这是 SFT 完成后由 on_complete hook 自动提交的。

Registry 中旧的 `exp_001_eval_3B_d005_s123`（PREPARING）是之前的占位条目，实际 eval 在 `_aligned` 后缀的条目下运行。无需再次提交——按 C001 约束，GPU 2 已有同类进程。

---
