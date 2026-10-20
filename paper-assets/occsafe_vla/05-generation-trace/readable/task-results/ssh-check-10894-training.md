# ssh check 10894 training

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-10894-training_20260527T010732_result.json`
- **Structured JSON:** [`52e038f1d64979582110.json`](../../sessions/52/52e038f1d64979582110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 GPU 训练状态

| GPU | PID | 状态 | exp_id | step/total | occ_loss | action_loss | 速度 | ETA (UTC) |
|-----|------|------|--------|------------|----------|-------------|------|-----------|
| cuda:0 | 481426 | **ALIVE** | full_occ_ln_v2_s1c | 2000/50005 | 0.0252 | 0.1787 | 1.08 it/s | ~May 27 21:20 |
| cuda:1 | 481643 | **ALIVE** | full_occ_ln_v2_s2 | ~1949/50005 | 0.0129 | 0.2207 | 1.08 it/s | ~May 27 21:20 |
| cuda:2 | 481988 | **ALIVE** | detach_ln_v2_s0c | ~1951/50005 | 0.0161 | 0.2422 | 1.08 it/s | ~May 27 21:20 |
| cuda:3 | 482336 | **DEAD** | detach_ln_v2_s1c | 818/50005 | — | — | — | — |

3 个活跃进程均运行约 31 分钟，loss 下降正常。剩余 ~48000 步 × ~0.93 s/step ≈ 12.3 小时，预计 May 27 ~21:20 UTC 完成，距 DDL (May 28 12:00 UTC) 有充足余量。

### cuda:3 诊断

**PID 482336 被 SIGTERM 杀死**，时间 08:50:59 UTC，仅跑到 step 818。日志最后一行：
```
Signal 15 (SIGTERM) received by PID 482336
```
这是外部 kill，非 OOM/crash。

**GPU 状态异常：** 0 MiB 内存 + 100% 利用率 + 36°C（其他 GPU 68-70°C）+ 100W 功耗。这是典型的 **stuck utilization counter** —— 进程被 SIGTERM 后 CUDA context 未正常释放，GPU 硬件计数器卡死。GPU 实际空闲无负载。

**可用于新任务**，但需要先执行 `nvidia-smi -r -i 3`（单卡 reset）清除卡死计数器。如果单卡 reset 失败，需要服务器 reboot。

---
