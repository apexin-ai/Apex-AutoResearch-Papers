# ops emergency status check 45947

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_status_check_45947_20260523T132947_result.json`
- **Structured JSON:** [`67fa4201310c50534525.json`](../../sessions/67/67fa4201310c50534525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-45947 状态

### 训练进程
| 实验 | PID | 存活 | 最新 ckpt | 估算当前 step | 进度 |
|------|-----|------|----------|-------------|------|
| s0_l005 | 589765 | Yes (GPU 0, 27GB) | 12000 (19:00) | ~14000 | ~47% (30k) |
| s0_l01 | 589840 | Yes (GPU 1, 27GB) | 12000 (19:01) | ~14000 | ~47% (30k) |

wandb 文件 (2ohlqvb3, umjcftxp) 最后写入 21:31-21:32，确认活跃。训练从 08:15 开始，save_interval=2000，10k→12k 约 2.5h，推算当前约 14000 步。

注：a3_obj.log / a3_spa.log 是旧的 A3 训练（已崩溃，AttributeError: 'GemmaModel' object has no attribute 'model'），与当前 A1 训练无关。

### Mid-Eval 状态
- serve_policy 存活: Yes (PID 626298 port 8000, PID 626351 port 8001, 各占 GPU 8.5GB)
- eval 进程存活: Yes（日志持续写入到 21:30）
- JSON 结果文件: **不存在**（目录为空）

**eval_l005** — 当前 Task 1, ep 38/50:
| Task | 名称 | TSR | CAR | 状态 |
|------|------|-----|-----|------|
| 0 | pick up orange juice → basket | 18.0% | 62.0% | 完成 |
| 1 | pick up chocolate pudding → basket | -- | -- | ep 38/50 进行中 |
| 2 | -- | -- | -- | 未开始 |
| 3 | -- | -- | -- | 未开始 |

**eval_l01** — 当前 Task 1, ep 36/50:
| Task | 名称 | TSR | CAR | 状态 |
|------|------|-----|-----|------|
| 0 | pick up orange juice → basket | 26.0% | 56.0% | 完成 |
| 1 | pick up chocolate pudding → basket | -- | -- | ep 36/50 进行中 |
| 2 | -- | -- | -- | 未开始 |
| 3 | -- | -- | -- | 未开始 |

预计 eval 完成还需 ~4-5 小时（4 task × 50 ep，剩余约 2.5 task × ~1.5h/task）。

### GPU
| GPU | 型号 | 温度 | 功耗 | 显存 | 利用率 |
|-----|------|------|------|------|--------|
| 0 | RTX PRO 6000 | 71°C | 443W/600W | 35610/97887 MiB (36%) | 100% |
| 1 | RTX PRO 6000 | 68°C | 420W/600W | 35610/97887 MiB (36%) | 75% |

每张 GPU 上同时跑 training (27GB) + serve_policy (8.5GB)。

### 磁盘
| 挂载点 | 总容量 | 已用 | 可用 | 使用率 |
|--------|-------|------|------|--------|
| / | 30G | 19G | 12G | 61% |
| /root/autodl-tmp | 250G | 176G | 75G | 71% |

---
