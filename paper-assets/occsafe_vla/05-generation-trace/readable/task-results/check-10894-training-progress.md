# check 10894 training progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_10894-training-progress_20260529T100711_result.json`
- **Structured JSON:** [`4427178116a6fa3f9ac9.json`](../../sessions/44/4427178116a6fa3f9ac9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894 — random_occ_v2_s0_r4 训练状态

| 项目 | 状态 |
|------|------|
| **进程** | PID 49565 存活，已运行 11h16m |
| **当前 step** | 39,620 / 50,005 (**79.2%**) |
| **训练速度** | ~1.01 s/step |
| **预计剩余** | ~2h55m（约完成时间：今天 ~14:10 UTC） |
| **最新 loss** | step=39600: occ_loss=0.0417, action_loss=0.0869, depth_loss=0.0 |
| **GPU** | 1× NVIDIA RTX PRO 6000 Blackwell, 利用率 99%, 显存 62.2/97.9 GiB (63%) |
| **磁盘** | /root/autodl-tmp 221G/250G used (89%, 剩余 30G) |

训练正常推进，预计再约 3 小时完成，在 DDL 前无压力。磁盘偏满但足够跑完。

---
