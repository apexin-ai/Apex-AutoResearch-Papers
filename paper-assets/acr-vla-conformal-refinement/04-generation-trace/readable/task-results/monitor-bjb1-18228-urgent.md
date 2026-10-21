# monitor bjb1 18228 urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-18228-urgent_20260515T045319_result.json`
- **Structured JSON:** [`ed48cf15d1ad49329948.json`](../../sessions/ed/ed48cf15d1ad49329948.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Spatial Eval 状态汇总（bjb1-18228, 2026-05-15 12:53 服务器时间）

### 实验状态

| # | 实验 | 模式 | 状态 | 完成进度 | 当前 SR | 日志最后更新 |
|---|------|------|------|---------|---------|-------------|
| 1 | **v4-default-r2** | acr_vla (default) | **失败** | 0/10 | N/A | 05-14 22:17 |
| 2 | **v4-small (perdof)** | acr_vla | **运行中** | 7/10 tasks | 42.9% (30/70) | 12:26 (~28min前) |
| 3 | **v4-obs-only-r2** | crm_obs_only | **运行中** | 7/10 tasks | 40.0% (24/60) | 12:49 (~5min前) |
| 4 | **v4-scalar** | crm_scalar | **运行中** | 4/10 tasks | 56.7% (17/30) | 12:48 (~6min前) |

### 详细结果

**1. v4-default-r2 — 启动即失败**
- 错误：`python: command not found`（exit code 127）
- 原因：脚本用了 `python` 而非 `python3`

**2. v4-small (perdof ACR-VLA)** — 7/10 tasks 完成
| Task | SR |
|------|----|
| between plate & ramekin | 60% (6/10) |
| next to ramekin | 100% (10/10) |
| table center | 10% (1/10) |
| on cookie box | 40% (4/10) |
| top drawer | 0% (0/10) |
| on ramekin | 0% (0/10) |
| next to cookie box | 90% (9/10) |

**3. v4-obs-only-r2** — 7/10 tasks 完成（task 7 进行中，midpoint 5/5）
| Task | SR |
|------|----|
| between plate & ramekin | 90% (9/10) |
| next to ramekin | 100% (10/10) |
| table center | 0% (0/10) |
| on cookie box | 40% (4/10) |
| top drawer | 10% (1/10) |
| on ramekin | 0% (0/10) |
| next to cookie box | 进行中 (5/5 at midpoint) |

**4. v4-scalar** — 4/10 tasks 完成（task 4 进行中）
| Task | SR |
|------|----|
| between plate & ramekin | 60% (6/10) |
| next to ramekin | 100% (10/10) |
| table center | 10% (1/10) |
| on cookie box | 进行中 (1/5 at midpoint) |

### GPU 状态
- 4x RTX 4090，4 个 python 进程占用 GPU（PIDs: 231426, 253085, 270097, 288939）
- GPU 利用率 18-22%，符合 eval 推理模式
- 无 JSON 输出文件（实验未完成）

### 判断
**实验未卡死。** 3 个实验活跃运行中，日志在过去 30 分钟内均有更新。只有 v4-default-r2 因 `python` 命令找不到而启动失败（需修复后重启）。预计 obs-only 和 perdof 约 1-2 小时内完成（剩余 3 个 tasks），scalar 约 2-3 小时（剩余 6 个 tasks）。

---
