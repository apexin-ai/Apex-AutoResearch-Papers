# diagnose eval qwen7b s42 cqa1 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_qwen7b_s42_cqa1_v2_20260519T213133_result.json`
- **Structured JSON:** [`c379a1c29a80dfe91cc7.json`](../../sessions/c3/c379a1c29a80dfe91cc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

**误报。实验已正常完成。** 5 个 dosage 全部评估成功，`.done` sentinel 和完整结果文件均存在（完成时间 05:07 CST）。

cron 误判原因：进程正常退出被视为"死亡"，且脚本不写 W&B metrics 导致 cron 二次判定失败。

注意事项：
- `/root/autodl-tmp` 磁盘 98% (仅剩 4.7G)，后续任务需清理空间
- GPU 0 当前在跑 GSM8K eval (PID 285390)，是后续新任务

---
