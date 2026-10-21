# diagnose seed66 failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed66-failure_20260521T014117_result.json`
- **Structured JSON:** [`ddb6dac1868bb2ccc821.json`](../../sessions/dd/ddb6dac1868bb2ccc821.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：

## seed66 失败诊断 (2026-05-21)

**根因：Cron false positive。** 3 个 seed66 进程实际仍在 bjb1-18228 上正常运行。

| 实验 | PID | GPU | 状态 |
|------|-----|-----|------|
| norm003-seed66 | 642428 | GPU0, 5.7GB, 35% | 运行中 |
| norm005-seed66 | 642506 | GPU2, 5.7GB, 38% | 运行中 |
| norm01-seed66 | 642775 | GPU3, 5.7GB, 34% | 运行中 |

- 日志在两次读取间从 rollout 5/20 → 10/20，确认进程在推进
- 无 OOM/CUDA error/traceback/segfault
- `sentinels/` 目录完全为空——从未写过 sentinel file
- seed66 用 `python3` 启动（无 `-u` 无 nohup），日志因 stdout 缓冲更新慢，但进程正常
- **无需重跑。** 预计再需 1-2 小时完成，之后手动修正 conclusion=success 并补录 metrics。

---
