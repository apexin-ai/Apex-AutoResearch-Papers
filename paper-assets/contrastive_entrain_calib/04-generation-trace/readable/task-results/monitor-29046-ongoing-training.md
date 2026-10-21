# monitor 29046 ongoing training

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_29046-ongoing-training_20260523T142521_result.json`
- **Structured JSON:** [`6bb587a5e92ab1f44fa8.json`](../../sessions/6b/6bb587a5e92ab1f44fa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### exp-004-heldout (GPU 0)
| 项目 | 值 |
|------|-----|
| 进度 | **3290 / 8000 steps** (41.1%) |
| GPU | RTX PRO 6000 Black, 22.9GB / 97.9GB, **3% util**（刚跑完一个 step，间歇期） |
| 最新 checkpoint | `checkpoint-3000` |
| step 速度 | ~93s/step |
| 已耗时 | ~30,396s (8.4h)，从 13:58 开始 |
| 剩余 steps | 4710 |
| **ETA** | ~4710 × 93s ≈ **121.6h (约 5.1 天)** → 预计 **5/29 凌晨** |
| loss | sft≈0, l2≈0.0013, total≈0.0001 |

### exp-003-len512-r3only (GPU 1)
| 项目 | 值 |
|------|-----|
| 进度 | **916 / 8000 steps** (11.5%) |
| GPU | RTX PRO 6000 Black, 41.3GB / 97.9GB, **97% util** |
| 最新 checkpoint | `checkpoint-500` |
| step 速度 | ~47s/step |
| 已耗时 | ~12h，从 10:17 开始 |
| 剩余 steps | 7084 |
| **ETA** | ~7084 × 47s ≈ **92.5h (约 3.9 天)** → 预计 **5/27 晚间** |
| reward | ~0.54, kl≈0.012, epoch≈20 |

### 磁盘
| 挂载点 | 总量 | 已用 | 剩余 | 使用率 |
|--------|------|------|------|--------|
| `/root` | 30G | 25G | 5.5G | **82%** |
| `/root/autodl-tmp` | 250G | 76G | 175G | 31% |

**注意**: 根分区 82% 偏高，随着 checkpoint 增加需关注。两个实验的 checkpoint 都存在 autodl-tmp 上（31%），暂无压力。

---
