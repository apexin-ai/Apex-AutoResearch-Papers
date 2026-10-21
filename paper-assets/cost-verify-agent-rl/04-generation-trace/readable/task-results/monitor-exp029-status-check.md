# monitor exp029 status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029_status_check_20260516T234923_result.json`
- **Structured JSON:** [`b479eab72e726bc041c9.json`](../../sessions/b4/b479eab72e726bc041c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 状态报告

| 项目 | 状态 |
|------|------|
| **进程** | **ALIVE** — PID 902342, 运行 3h37m22s, RSS 3.6MB (主控进程) |
| **GPU 0** | RTX PRO 6000, 63°C, 375W, 46GB/98GB, **100% util** |
| **GPU 1** | RTX PRO 6000, 63°C, 388W, 45GB/98GB, **100% util** |
| **训练进度** | **Step 7/100 (7%)**, 已耗时 ~3h26m, 预估剩余 ~47h38m (~1843s/step) |
| **最近 checkpoint** | `global_step_5` 已保存 (06:43 UTC) |

### 最新 val 指标 (step 5 eval)

| 指标 | 值 |
|------|-----|
| val-env/AlfworldSG/non-zero/pass@1 | **1.0** |
| val-core/unknown/reward/mean@32 | **1.25** |
| val-core/unknown/reward/best@32/mean | **9.84** |
| val-aux/unknown/reward/best@16/mean | 8.79 |
| val-aux/unknown/reward/best@8/mean | 6.44 |
| val-aux/unknown/reward/worst@32/mean | 0.0 |
| val-env/response_length | 7088 |

**结论**: 训练正常运行中，双卡满载。当前在 step 7，刚完成 step 5 的 validation + checkpoint 保存。pass@1=1.0 和 reward/best@32=9.84 看起来不错，但 reward/mean@32=1.25 说明整体 consistency 还较低。按当前速度全部 100 steps 约需 ~51h 总计。

---
