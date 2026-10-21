# fix stuck preparing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_stuck-preparing-experiments_20260515T190835_result.json`
- **Structured JSON:** [`af3d429826594791e4a9.json`](../../sessions/af/af3d429826594791e4a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 实验 | 服务器 | PID | 状态变更 | Cron |
|------|--------|-----|----------|------|
| `eval-mag-perdof-norm0p3-object-r2` | bjb2-28827 | 127570 ✅存活 | PREPARING → QUEUED → **RUNNING** | `6dfe7623` 每20min |
| `eval-obs-only-object-norm02-seed43-r2` | bjb1-32546 | 148788 ✅存活 | PREPARING → QUEUED → **RUNNING** | `eba1ca2c` 每20min |

两个进程都在正常运行——模型和环境已加载完成，正在执行 evaluation rollouts（output_file 尚未生成，说明还在第一个 task）。Registry 已更新为 RUNNING，cron 每 20 分钟自动检查进程存活和进度。

---
