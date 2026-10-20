# ops gpu2 cleanup kill duplicate d100

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2_cleanup_kill_duplicate_d100_20260514T155231_result.json`
- **Structured JSON:** [`d4c0950a92a9359c1a11.json`](../../sessions/d4/d4c0950a92a9359c1a11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已清理：**
- v3 进程树 1：PID 395337→395341→395342 — SIGTERM 终止
- v3 进程树 2（重复提交）：PID 395759→395763→395764 — SIGTERM 终止
- v3 tmux session `exp_001_eval_05B_d100_aligned_v3` — 已删除
- Zombie PID 318424 — 已 kill

**v4 状态正常：**
- PID 396024 运行中，GSM8K 进度 258/1319 (20%)
- 速度从 ~6.12s/it 提升到 ~5.65s/it（竞争消除后）
- GPU 2 显存 3695 MiB，利用率 36%（从 99% 降下来）

---
