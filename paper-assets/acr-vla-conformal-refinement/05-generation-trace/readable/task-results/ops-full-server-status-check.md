# ops full server status check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-server-status-check_20260521T160318_result.json`
- **Structured JSON:** [`cb7e334467c53a540b86.json`](../../sessions/cb/cb7e334467c53a540b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告：

---

## 📊 4 台服务器状态总览

### 1. bjb1-32546 — Object Precompute Shards 1-9

**GPU 状态** (6x RTX 4090):

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 19.3/24G | 99% | 🔄 shard 5 + shard 1 (共享) |
| 1 | 9.6/24G | 45% | 🔄 shard 2 |
| 2 | 19.3/24G | 99% | 🔄 shard 7 + shard 3 (共享) |
| 3 | 19.3/24G | 98% | 🔄 shard 8 + shard 4 (共享) |
| 4 | 9.6/24G | 24% | 🔄 shard 9 |
| 5 | 9.6/24G | 25% | 🔄 shard 6 |

**Precompute 进度** (object, 每 shard 总计 7251 samples):

| Shard | 进度 | 速度 | 预计剩余 |
|-------|------|------|----------|
| s1 | ~2900/7251 (40%) | 2.15s/sample | ~2.6h |
| s2 | ~3100/7251 (43%) | ~2.15s/sample | ~2.5h |
| s3 | ~3100/7251 (43%) | ~2.15s/sample | ~2.5h |
| s4 | ~3100/7251 (43%) | ~2.15s/sample | ~2.5h |
| s5 | 3700/7251 (51%) | 1.93s/sample | ~1.9h |
| s6 | 3600/7251 (50%) | 1.89s/sample | ~1.9h |
| s7 | ~3700/7251 (51%) | ~1.93s/sample | ~1.9h |
| s8 | ~3700/7251 (51%) | ~1.93s/sample | ~1.9h |
| s9 | ~3600/7251 (50%) | ~1.93s/sample | ~1.9h |

9 个 shard 全部 🔄 运行中。GPU 0/2/3 各跑 2 个 shard（时分复用），GPU 1/4/5 各跑 1 个。

---

### 2. bjb2-40593 — Object+Spatial Shard 0

**GPU 状态** (1x RTX 4090 D):

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 9.6/24G | 14% | 🔄 shard 0 (object+spatial) |

**Precompute 进度**:
- 🔄 **Object shard 0**: 4000/7251 (55%), 3.34s/sample, **~3.0h 剩余**
- ⏳ **Spatial shard 0**: 尚未开始（object 完成后才会跑 spatial）

⚠️ 这台机器用 `--precompute_batch_size 1`，速度比 bjb1 慢（3.34s vs 1.93s/sample）。Object 完成后还需额外跑 spatial（~8608 samples），预计 object+spatial **总共还要 ~11h**。

---

### 3. bjb2-28827 — Spatial Precompute Shards 0-5

**GPU 状态** (6x RTX 4090):

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 9.6/24G | 21% | 🔄 spatial shard 0 |
| 1 | 9.6/24G | 21% | 🔄 spatial shard 1 |
| 2 | 9.6/24G | 20% | 🔄 spatial shard 2 |
| 3 | 9.6/24G | 21% | 🔄 spatial shard 3 |
| 4 | 9.6/24G | 20% | 🔄 spatial shard 4 |
| 5 | 9.6/24G | 20% | 🔄 spatial shard 5 |

**Precompute 进度** (spatial, 每 shard 总计 8607-8608 samples):

| Shard | 进度 | 速度 | 预计剩余 |
|-------|------|------|----------|
| s0 | 3700/8608 (43%) | 2.27s/sample | ~3.1h |
| s1 | ~3500/8608 (41%) | ~2.3s/sample | ~3.3h |
| s2 | ~3500/8608 (41%) | ~2.3s/sample | ~3.3h |
| s3 | ~3500/8608 (41%) | ~2.3s/sample | ~3.3h |
| s4 | ~3500/8607 (41%) | ~2.3s/sample | ~3.3h |
| s5 | 3600/8607 (42%) | 2.31s/sample | ~3.2h |

6 个 shard 全部 🔄 运行中，每 GPU 1 个 shard。

---

### 4. bjb1-18228 — Spatial Shard 6

**GPU 状态** (4x RTX 4090):

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 0/24G | 0% | ❌ 空闲 |
| 1 | 0/24G | 0% | ❌ 空闲 |
| 2 | 0/24G | 0% | ❌ 空闲 |
| 3 | 9.6/24G | 46% | 🔄 spatial shard 6 |

**Precompute 进度**:
- 🔄 **Spatial shard 6**: 4400/8607 (51%), 1.89s/sample, **~2.2h 剩余**

⚠️ **3 块 GPU 完全空闲**（cuda:0-2），可用于其他任务。

---

## 总体估算

| 任务 | 服务器 | 完成时间 (约) |
|------|--------|---------------|
| Object s1-s9 | bjb1-32546 | ~02:40 (最慢 shard 1) |
| Object s0 | bjb2-40593 | ~03:10 |
| Spatial s0-s5 | bjb2-28827 | ~03:30 |
| Spatial s6 | bjb1-18228 | ~02:20 |
| ⚠️ Spatial s0 (on bjb2-40593) | bjb2-40593 | ~11:00+ (在 object 完成后) |

**关键发现**:
1. 所有 precompute 任务都在正常运行，无死进程
2. bjb2-40593 的 shard 0 是瓶颈 — 要串行跑 object+spatial 且速度最慢（batch_size=1），但 bjb2-28827 已经在跑 spatial shard 0，所以 bjb2-40593 的 spatial 部分可能是冗余的
3. bjb1-18228 有 3 块空闲 GPU
4. 之前提到的 14 个 RUNNING eval 实验 — 4 台服务器上均未发现 evaluate 相关进程，确认已死

---
