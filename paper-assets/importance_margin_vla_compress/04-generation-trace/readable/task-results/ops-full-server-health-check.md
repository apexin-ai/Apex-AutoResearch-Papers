# ops full server health check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_server_health_check_20260519T202607_result.json`
- **Structured JSON:** [`1b0a937937949d549469.json`](../../sessions/1b/1b0a937937949d549469.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41074

| GPU | PID | VRAM | Util | 实验 | Step | Loss | SPS |
|-----|-----|------|------|------|------|------|-----|
| 0 | 26118 | 30117/97887 MiB | 96% | VTC-only (m128) | 未知* | — | — |
| 1 | 43111 | 48089/97887 MiB | 97% | C5 RoboFlamingo (libero_object) | — | — | — |
| 2 | — | 0 MiB | 0% | 空闲 | | | |
| 3 | — | 0 MiB | 0% | 空闲 | | | |

\* PID 26118 在跑 `train_openvla_smart_compress.py m128`，GPU 96% 说明训练中，但日志停在 02:28 "Computing action statistics..."——没加 `-u` flag 导致 stdout 缓冲，看不到 step 进度。

另：SC+LoRA 已被 kill（SIGTERM），停在 step 1183，log: `train_openvla_sc_m128_lora_seed42.log`。

空闲 GPU: [2, 3]

## westd-27271

| GPU | PID | VRAM | Util | 实验 | Step | Loss | SPS |
|-----|-----|------|------|------|------|------|-----|
| 0 | 841334 | 32285/97887 MiB | **0%** | VTC+LoRA (m128, lora r=16) | **无** | — | — |
| 1 | — | 3 MiB | 0% | 空闲 | | | |

空闲 GPU: [1]

## cqa1-33015

| GPU | PID | VRAM | Util | 实验 | Step | Loss | SPS | ETA |
|-----|-----|------|------|------|------|------|-----|-----|
| 0 | 678106 | 2815/24564 MiB | 31% | m128_seed43 | 77500/100k | 0.069 | 4.0 | ~06:20 |
| 1 | 649697 | 2855/24564 MiB | 45% | m16_seed43 | 77200/100k | 0.094 | 4.0 | ~06:21 |
| 2 | 649845 | 2815/24564 MiB | 14% | m16_seed44_v3 | 53700/100k | 0.043 | 4.1 | ~07:54 |
| 3 | 685415 | 3478/24564 MiB | ~0% | eval m32_seed44 | ep 367/500 | — | — | ~05:01 |

空闲 GPU: 无

## 异常

1. **westd-27271 GPU 0 — PID 841334 (VTC+LoRA) 疑似卡死**：进程存活、占 32GB VRAM，但 GPU 利用率 0%。wandb 在 02:38 初始化后 2h+ 无任何训练步日志写入。需要排查（可能卡在数据加载/action stats 计算）。

2. **westd-41074 GPU 0 — VTC-only 日志不可读**：训练大概率在跑（96% GPU），但 `python` 未加 `-u` flag，stdout 缓冲导致日志文件停在初始化阶段，无法读取当前 step/loss。

---
