# diagnose eval baseline fullft spatial v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_baseline_fullft_spatial_v11_20260522T192511_result.json`
- **Structured JSON:** [`b2e684208d4d6b7dc932.json`](../../sessions/b2/b2e684208d4d6b7dc932.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验未失败，是 cron 误报。** 实验于 2026-05-23 03:14:59 正常完成，4 tasks × 200 episodes 全部跑完，结果文件已保存。Cron 因进程正常退出后不再存活、且无 sentinel/W&B 信号，误判为 failed。

结果：Avg TSR = 0.4%, Avg CAR = 0.0%（baseline 在 Level II safety 下几乎完全失败）。无需重跑。

报告已写入 `artifacts/worker_output_diagnose_eval_baseline_fullft_spatial_v11.md`。

---
