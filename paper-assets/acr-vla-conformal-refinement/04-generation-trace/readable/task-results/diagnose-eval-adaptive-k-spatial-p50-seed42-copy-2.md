# diagnose eval adaptive k spatial p50 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-adaptive-k-spatial-p50-seed42_20260520T073204_result.json`
- **Structured JSON:** [`8dd28b6fdbc058cb45e6.json`](../../sessions/8d/8dd28b6fdbc058cb45e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败根因：Cron 误判（false positive）。** 原 PID 675831 被 deploy worker kill 后重启为 PID 681823，cron 未追踪到新 PID，5 次检测均无 sentinel/W&B 信号 → 自动标记 failed。

**实际状态：进程正常运行中。**
- PID 681823 状态 `Rl+`，已运行 17h36m
- 已完成 3/10 tasks（SR: 70% / 100% / 0%），第 4 个 task 进行中
- GPU 使用 5972/24564 MiB，无错误
- 输出 JSON 尚未生成（全部 task 完成后才写入）

**结论：无需重新提交。** 等进程自然完成后，手动修正 conclusion 为 success 并补录 metrics。

---
