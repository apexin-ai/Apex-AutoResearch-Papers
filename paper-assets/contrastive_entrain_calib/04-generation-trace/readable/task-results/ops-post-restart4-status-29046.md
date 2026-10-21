# ops post restart4 status 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart4-status-29046_20260519T135149_result.json`
- **Structured JSON:** [`f140ab798eb2c774a9db.json`](../../sessions/f1/f140ab798eb2c774a9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都在正常运行，服务重启后未中断。

## exp-003 (GPU 1) — R3-only GRPO

| 项目 | 值 |
|------|-----|
| 当前 step | **2655 / 8000** (33.2%) |
| 速度 | ~26.3s/step |
| GPU 显存 | 38,161 / 97,887 MiB |
| GPU 利用率 | 95% |
| reward/r3_mean | ~0.54–0.69 (近10步) |
| 预计剩余 | **~39h** (约 5/21 下午完成) |

## exp002v2-recalib (GPU 0) — Cosine + recalib

| 项目 | 值 |
|------|-----|
| 当前 step | **1757 / 8000** (22.0%) |
| 速度 | ~15.3s/step |
| GPU 显存 | 66,907 / 97,887 MiB |
| GPU 利用率 | 95% |
| reward/combined_mean | ~0.64 (r1≈-0.05, r2≈-0.11, r3≈0.87) |
| 预计剩余 | **~27h** (约 5/21 凌晨完成) |

两个任务均稳定推进，日志持续更新中。

---
