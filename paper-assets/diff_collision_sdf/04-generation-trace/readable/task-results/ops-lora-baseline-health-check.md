# ops lora baseline health check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_baseline_health_check_20260525T143156_result.json`
- **Structured JSON:** [`6c451fa5fc3721bb1214.json`](../../sessions/6c/6c451fa5fc3721bb1214.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 指标 | s0 (cuda:0) | s1 (cuda:1) |
|------|-------------|-------------|
| PID | 2275 (存活, 运行 9h52m) | 2353 (存活, 运行 9h52m) |
| 当前 step | 23655 / 30000 (79%) | 23664 / 30000 (79%) |
| 当前 loss | ~0.0149 | ~0.0108 |
| 速度 | 4.62 s/it | 4.61 s/it |
| 预估剩余 | ~8h09m → 完成约 05:00 UTC (5/26) | ~8h07m → 完成约 05:00 UTC (5/26) |
| best/ 存在？ | 是 (loss=0.01124 @ step 20000) | 是 (loss=0.01130 @ step 14000) |
| Checkpoints | 20000, 22000 | 20000, 22000 |
| GPU 显存 | 27089 MiB, 100% 利用率 | 27089 MiB, 100% 利用率 |

训练健康，两个 seed 进度同步。ETA 比之前预估晚约 6.5h（原估 22:30 UTC 5/25 → 实际约 05:00 UTC 5/26），因为是从 step ~16000 resume 后实际已跑到 23655，tqdm 剩余预估基于当前速度是 ~8h。Loss 在 0.008-0.02 范围正常波动，无异常。

---
