# monitor spatial final check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_spatial-final-check_20260515T044550_result.json`
- **Structured JSON:** [`f2062fca3a98251d9635.json`](../../sessions/f2/f2062fca3a98251d9635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**全部 4 个实验卡死，无任何新进度。** 进程存活、占用 GPU 显存，但日志 8+ 小时零输出。每个实验都卡在完成一个 task 后、初始化下一个 task 环境时 hang 住（可能是 MuJoCo/EGL 环境创建死锁）。

| 实验 | Tasks | 成功率 | 卡在 |
|------|-------|--------|------|
| argmin-only-spatial | 9/10 | 36.7% | task 10 |
| acr-spatial-v4-small (perdof) | 7/10 | 42.9% | task 8 |
| acr-spatial-v4-obs-only-r2 | 6/10 | 40.0% | task 7 |
| acr-spatial-v4-scalar | 3/10 | 56.7% | task 4 |

需要 kill 全部进程并重启。建议重启时加 task offset 参数（如果 evaluate.py 支持），跳过已完成的 tasks 只跑剩余部分，避免重复计算。

---
