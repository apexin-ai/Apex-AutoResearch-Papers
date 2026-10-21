# diagnose exp029 seed6 ood eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_seed6_ood_eval_v2_20260521T141056_result.json`
- **Structured JSON:** [`b2d4404457136fc7b3ef.json`](../../sessions/b2/b2d4404457136fc7b3ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/exp029_seed6_ood_eval_v2/diagnosis.md` 并注册。

**核心发现：实验没有真正失败。** 134 个 OOD 任务的评估已完整跑完，结果是 **29.1% pass@1**。

被 cron 误判为失败的原因：评估完成后，wandb 0.26.0 在 Ray worker 进程退出时的 atexit teardown 触发了 `BrokenPipeError`，导致进程非零退出码。cron 看到进程死亡 + 无 sentinel 文件 → 自动标记为失败。

Checkpoint 和 symlink 状态正常，v1 的 `Unsupported model` 问题已修复。不需要 v3 重跑。

---
