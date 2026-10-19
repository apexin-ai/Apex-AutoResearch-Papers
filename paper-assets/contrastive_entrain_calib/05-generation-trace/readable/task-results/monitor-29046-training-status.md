# monitor 29046 training status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_29046-training-status_20260523T124737_result.json`
- **Structured JSON:** [`80bf4f50dbb8485a512d.json`](../../sessions/80/80bf4f50dbb8485a512d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 监控报告

### exp-004-heldout (GPU0)
| 指标 | 值 |
|------|-----|
| 当前 step | **2660 / 8000** (33.3%) |
| 最新 checkpoint | checkpoint-2500 |
| 速度 | ~93s / 10 steps → **9.3s/step** |
| 已用时间 | ~6.8h (24527s) |
| 剩余 steps | 5340 |
| **ETA 完成** | **~13.8h → 约 5/24 10:30** |
| 状态 | 正常，sft loss=0, l2 loss ~0.0015-0.0017 |

### exp-003-len512-v3 (GPU1)
| 指标 | 值 |
|------|-----|
| 当前 step | **790 / 8000** (9.9%) |
| 最新 checkpoint | checkpoint-500 |
| 速度 | **~46.5s/step** (略快于之前的 49.8s) |
| 已用时间 | ~10.5h |
| 剩余 steps | 7210 |
| **ETA 完成** | **~93h → 约 5/27 18:00** |
| 状态 | 正常运行，PID 553700，R3-only 模式（d_syc not loaded） |

### GPU & 磁盘
| 资源 | 状态 |
|------|------|
| GPU0 | 45°C, 178W/600W, 23GB/98GB VRAM, 33% util |
| GPU1 | 65°C, 400W/600W, 41GB/98GB VRAM, 95% util |
| 根分区 | 25G/30G used (**82%**, 偏高) |
| 数据盘 | 75G/250G used (30%, 充裕) |

**注意**: 根分区 82% 使用率偏高，建议关注是否有不必要的文件可以清理。exp-003 预计还需约 4 天才能完成。

---
