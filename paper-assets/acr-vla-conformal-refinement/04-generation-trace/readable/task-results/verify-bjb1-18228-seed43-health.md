# verify bjb1 18228 seed43 health

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_bjb1-18228-seed43-health_20260515T190130_result.json`
- **Structured JSON:** [`1b705d80ad38d7b3d6e2.json`](../../sessions/1b/1b705d80ad38d7b3d6e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 实验状态汇总

当前服务器时间：~03:02 2026-05-16 (+0800)

| 实验 | 状态 | Tasks 完成 | 最后日志时间 | GPU | 备注 |
|---|---|---|---|---|---|
| eval-argmin-object-seed43 | **ALIVE** | 5/10 | 02:31 | GPU3 (3287MB) | PID 356701 运行中，31 min 无新日志（正常，rollout 耗时） |
| eval-obs-only-object-seed43 | **ALIVE** | 5/10 | 02:26 | GPU2 (3323MB) | PID 356495 运行中，36 min 无新日志 |
| eval-perdof-object-seed43 | **ALIVE** | 4/10 | 02:51 | GPU1 (3785MB) | PID 365930 运行中，11 min 无新日志 |
| eval-obs-only-spatial-seed43 | **DEAD** | 2/10 | 18:20 (昨天) | 无 | 进程已消失，无 EXIT_CODE 记录，~9 小时无活动 |

**关键发现：**

1. 前一个 Worker 的担忧大部分不成立——argmin-object-seed43 和 obs-only-object-seed43 都活着并在正常推进，有 GPU 进程在跑。
2. **obs-only-spatial-seed43 确认已死**，日志停在 2/10 tasks，进程不存在，无退出码。如 registry 仍标记 RUNNING 则需修正。需要重启。
3. GPU 0 被另一个实验占用：`eval-acr-object-v4-default-r2`（perdof seed42 default norm，PID 390936，02:11 启动），不是 seed43 实验。

---
