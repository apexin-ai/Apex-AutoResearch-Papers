# monitor eval progress

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval_progress_20260515T230117_result.json`
- **Structured JSON:** [`7570bf2716f683781010.json`](../../sessions/75/7570bf2716f683781010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总所有数据，计算完成时间估算。

## 评测进度报告

### 1. 进度概览

| | **baseline_plus** (GPU 0) | **baseline_std** (GPU 1) |
|---|---|---|
| 输出路径 | `baseline_plus_v2/` (注意是 v2 非 v3) | `baseline_std_v3/` |
| libero_spatial | **完成** | **完成** |
| libero_object | **接近完成** (10/10 tasks 已有 videos，eval_info 未写入) | **进行中** (8/10 tasks 已有 videos) |
| libero_goal | 未开始 | 未开始 |
| libero_10 | 未开始 | 未开始 |

**注意**：脚本中第 4 个 suite 是 `libero_10`，不是 `libero_long`。

### 2. 速率估算

- spatial 完整 suite (500 episodes): baseline_plus ~102 min, baseline_std ~111 min
- 每个 episode 约 **12-13s**

### 3. 剩余时间估算

| | baseline_plus (GPU 0) | baseline_std (GPU 1) |
|---|---|---|
| object 剩余 | ~2 min | ~20 min |
| libero_goal | ~102 min | ~111 min |
| libero_10 | ~102 min | ~111 min |
| **总计** | **~3.5 小时** | **~4 小时** |

预计完成时间：baseline_plus 约 **今天 10:30 UTC**，baseline_std 约 **11:00 UTC**。

### 4. GPU 使用情况

| GPU | 型号 | VRAM 使用 | VRAM 总量 | GPU Util |
|---|---|---|---|---|
| 0 | RTX PRO 6000 Blackwell | **2154 MiB** | 97887 MiB (96 GB) | 0% |
| 1 | RTX PRO 6000 Blackwell | **2633 MiB** | 97887 MiB (96 GB) | 0% |

### 5. 能否在同一 GPU 上跑 dry-run？

**可以。** 当前 VRAM 使用仅 2-3 GB / 96 GB（~2.5%），剩余 ~94 GB 空闲。即使推理时 VRAM 会有峰值，也远不到占满的程度。在任一 GPU 上并行跑 dry-run 完全可行——只需设置 `CUDA_VISIBLE_DEVICES` 指向同一张卡即可。

不过 GPU util 采样时为 0%（可能处于 episode 间隙），实际推理时会有负载。建议 dry-run 先限制 batch_size=1 并监控 VRAM 峰值。

---
