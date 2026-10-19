# ssh read calibration results urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_read-calibration-results-urgent_20260520T045324_result.json`
- **Structured JSON:** [`525f528df4475654010f.json`](../../sessions/52/525f528df4475654010f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**`crm_magnitude_calibration.json` 尚未生成——脚本仍在运行。**

日志确认目标文件为 `logs/crm_magnitude_calibration.json`，但 JSON 在所有 episode 完成后才写入。

### 当前进度

| 项目 | 值 |
|------|-----|
| 总 episodes | 10 tasks × 10 eps = **100** |
| 已完成 | ~82 episodes（97 行日志 - 15 行 header） |
| 当前位置 | `pick_up_the_chocolate_pudding` ep 4/10 |
| 已用时间 | 6651s (~111 min) |
| 预估剩余 | ~18 episodes × ~80s ≈ **24 分钟** |
| 进度 | **~82%**，非之前预估的 95% |

### 已有的相关 calibration 数据

`k2_l2_calibration.json` 包含 3 个 Spearman 相关性（基于 5 eps/task 的先前 run）：

| 对 | ρ | p-value |
|----|---|---------|
| ρ(FMVD, K10_var) | **0.0825** | 2.33e-23 |
| ρ(K2_L2, K10_var) | **0.9979** | 0.0 |
| ρ(K2_L2, FMVD) | **0.0925** | 6.03e-29 |

其中 K2_L2 vs K10_var ≈ 0.998 符合预期 sanity check。

**但关键的 K1_correction_mag 相关性需要等当前脚本跑完。** 预计约 24 分钟后产出 JSON。

---
