# ops gpu colocation check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_colocation_check_20260514T063356_result.json`
- **Structured JSON:** [`17d8dcfd2c54a5bfa0a6.json`](../../sessions/17/17d8dcfd2c54a5bfa0a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the analysis:

## GPU 共存可行性

**当前 VRAM 基线：**
| GPU | 实验 | VRAM 占用 | GPU Util | FPS |
|-----|------|-----------|----------|-----|
| cuda:0 | exp_008f (H=8, dim=0) | 2742 MiB (2.8%) | 1-29% | ~6.0 |
| cuda:1 | exp_008e_v3 (H=15, dt=1) | 4158 MiB (4.2%) | 0-12% | ~6.5 |

每张卡 97887 MiB (96 GB)。208 CPU cores (Xeon 8470Q × 2)。

**共存评估：**

| 组合 | VRAM 预估 | 占比 | 可行 | 说明 |
|------|-----------|------|------|------|
| H=8 × 2 | ~5.5 GB | 5.6% | **YES** | 远低于容量 |
| Baseline(H=15) + H=8 | ~6.9 GB | 7.0% | **YES** | 远低于容量 |
| Baseline × 2 | ~8.4 GB | 8.6% | **YES** | 远低于容量 |
| H=15 × 2 | ~8.3 GB | 8.5% | **YES** | 远低于容量 |

**Throughput 影响预估：5-15%**（非 30-50%）
- GPU util 峰值仅 29%，两进程共存后 ~40-50%，GPU kernel 调度竞争很小
- 208 CPU cores，每个实验仅用 4 envs（~5-10 cores），CPU 完全不是瓶颈
- 主要开销：CUDA context 切换 (~300MB 额外 VRAM) + 偶尔的 kernel 排队
- DreamerV3 proprio 训练主要是 CPU-bound（env stepping），不是 GPU-bound

**结论：4 并发实验（每 GPU 2 个）完全可行。**

---

## 当前实验 ETA

| 实验 | 进度 | 剩余 steps | FPS | 预计剩余 |
|------|------|-----------|-----|---------|
| exp_008f | 40K/105K | 65K | 6.0 | **~3.0h** |
| exp_008e_v3 | 52K/105K | 53K | 6.5 | **~2.3h** |

---

## Wave 调度方案

假设共存 fps 降 10%：baseline ~6.6 fps, H=8 ~5.4 fps, H=15 ~5.9 fps

### Wave 1（008f/008e_v3 完成后，~3h 后启动）— Baselines
无依赖，可立即并行。

| GPU | Slot A | Slot B |
|-----|--------|--------|
| cuda:0 | Walker baseline seed 2 (~4.4h) | Walker baseline seed 3 (~4.4h) |
| cuda:1 | Cheetah baseline seed 1 (~4.4h) | Cheetah baseline seed 2 (~4.4h) |

**Wave 1 时长：~4.4h**

### Wave 2（Wave 1 完成后）— 崩塌复现 + 剩余 baseline
plan_011/012 依赖 plan_010（baseline v/e 校准），此时已完成。

| GPU | Slot A | Slot B |
|-----|--------|--------|
| cuda:0 | Walker 008d seed 2 (~5.4h) | Walker 008d seed 3 (~5.4h) |
| cuda:1 | Cheetah baseline seed 3 (~4.4h) | Walker 008f seed 2 (~5.4h) |

**Wave 2 时长：~5.4h**

### Wave 3（Wave 2 完成后）— 因果控制 + Cheetah collapse
| GPU | Slot A | Slot B |
|-----|--------|--------|
| cuda:0 | Walker 008f seed 3 (~5.4h) | Cheetah trained dt_emb seed 1 (~5.4h) |
| cuda:1 | Cheetah trained dt_emb seed 2 (~5.4h) | Cheetah trained dt_emb seed 3 (~5.4h) |

**Wave 3 时长：~5.4h**

### Wave 4（Wave 3 完成后）— Cheetah 因果控制
| GPU | Slot A | Slot B |
|-----|--------|--------|
| cuda:0 | Cheetah dim=0 seed 1 (~5.4h) | Cheetah dim=0 seed 2 (~5.4h) |
| cuda:1 | Cheetah dim=0 seed 3 (~5.4h) | [P1] Walker 008a seed 2 (~5.0h) |

**Wave 4 时长：~5.4h**

---

## 总时间估算

| 阶段 | Wall time |
|------|-----------|
| 当前实验完成 | 3.0h |
| Wave 1 (baselines) | 4.4h |
| Wave 2 (collapse + remaining) | 5.4h |
| Wave 3 (causal + Cheetah) | 5.4h |
| Wave 4 (Cheetah causal + P1) | 5.4h |
| **P0 总计** | **~23.6h** |

P0 全部 15 个 run 约 **24h wall time**（约 1 天）。加 P1（5 个 run），再加 ~5.4h，总计 **~29h**。

对比无共存方案：15 runs × 5h / 2 GPUs = 37.5h。**共存节省 ~14h（37%）。**

**建议**：先在 Wave 1 用两个短实验（如 2 个 baseline）共存验证实际 fps 降幅，确认后再全面推行 4 并发。

---
