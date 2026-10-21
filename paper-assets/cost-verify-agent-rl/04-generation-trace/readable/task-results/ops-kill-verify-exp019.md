# ops kill verify exp019

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-verify-exp019_20260514T165115_result.json`
- **Structured JSON:** [`953decf6998b3de8eb5f.json`](../../sessions/95/953decf6998b3de8eb5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| 项目 | 状态 |
|------|------|
| PID 366066 | 已 kill，确认死亡 |
| 残留进程 | 无（sft_train/exp019/run_exp019 均无） |
| Checkpoint | 空目录，已重命名为 `exp019_expert_sft_v2_INVALID` |

### GPU 状态

| GPU | 型号 | VRAM 使用 | 利用率 | 温度 |
|-----|------|-----------|--------|------|
| 0 | RTX PRO 6000 (96GB) | **0MiB / 97887MiB** | 0% | 40°C |
| 1 | RTX PRO 6000 (96GB) | **0MiB / 97887MiB** | 0% | 28°C |

### 磁盘

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 86G | 165G | 35% |

两块 GPU 完全空闲，磁盘充裕，可立即启动新实验。

---
