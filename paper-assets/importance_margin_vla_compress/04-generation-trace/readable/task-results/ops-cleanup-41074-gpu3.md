# ops cleanup 41074 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_41074_gpu3_20260519T214915_result.json`
- **Structured JSON:** [`e45843ef894f03c47f86.json`](../../sessions/e4/e45843ef894f03c47f86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part 1: westd-41074 清理

**GPU 3 已清理干净** — PID 49844 已 kill，显存 0MiB。

| GPU | 状态 | 进程 | 显存 |
|-----|------|------|------|
| 0 | 正常运行 | PID 26118 (C4-ext VTC-only) | 30,108 MiB |
| 1 | 正常运行 | PID 47691 (C5 RoboFlamingo) | 48,080 MiB |
| 2 | 空闲 | — | 0 MiB |
| 3 | **已清理** | — | 0 MiB |

---

### Part 2: cqa1-33015 训练进度

**已完成的训练（4个）：**

| 实验 | 完成时间 | Final Loss | Eval Loss |
|------|----------|-----------|-----------|
| m32_seed44 | 05/19 16:14 | 0.0415 | 0.0635 |
| m64_seed44 | 05/19 16:15 | 0.0310 | 0.0699 |
| m96_seed44 | 05/19 16:01 | 0.0467 | 0.0526 |
| m32_official | 05/19 17:20 | 0.0491 | 0.0603 |

**正在运行的训练（3个）：**

| 实验 | GPU | Step | Loss | SPS | 剩余 | ETA |
|------|-----|------|------|-----|------|-----|
| m128_seed43 | 1 | 91,650/100K | 0.107 | 3.9 | ~8,350 | **~06:26** |
| m16_seed43 | 2 | 91,700/100K | 0.085 | 4.0 | ~8,300 | **~06:25** |
| m16_seed44_v3 | 0 | 70,000/100K | 0.066 | 4.1 | ~30,000 | **~07:52** |

**Eval 已完成（GPU 3）：**

| 实验 | Suite | Overall SR | 95% CI |
|------|-------|-----------|--------|
| eval_m32_seed44 | libero_object | **59.6%** (298/500) | [55.2%, 63.8%] |

进程 PID 685415 仍在 GPU 3（3.5GB），但 eval 日志显示已于 19:01 完成输出结果。可能是进程未退出，需要注意。

**关键标注：** m128_seed43 和 m16_seed43 均已超 91K/100K（>91%），预计约 35 分钟后完成。m16_seed44_v3 进度 70%，预计约 2 小时后完成。

---
