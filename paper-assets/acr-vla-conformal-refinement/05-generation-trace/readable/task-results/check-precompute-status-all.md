# check precompute status all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_precompute-status-all_20260521T145216_result.json`
- **Structured JSON:** [`6dc257058691de5113f9.json`](../../sessions/6d/6dc257058691de5113f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the complete status:

## Precompute Shard 状态汇总

### Object Shards (10 shards, ~7251 samples each)

| Shard | 服务器 | GPU | 状态 | 进度 | 速度 | 预计剩余 | Cache .pt |
|-------|--------|-----|------|------|------|----------|-----------|
| **s0** | bjb2-40593 | GPU 0 (99%) | **RUNNING** (原始进程) | 2700/7251 | 3.38s/sample | ~4.3h | 30 files (混合100/500粒度) |
| **s1** | bjb1-32546 | GPU 0-4之一 | **RUNNING** (r2) | 1000/7251 | 2.15s/sample | ~3.7h | 2 files (500粒度) |
| **s2** | bjb1-32546 | GPU 0-4之一 | **RUNNING** (r2) | 1100/7251 | 1.91s/sample | ~3.3h | 2 files (500粒度) |
| **s3** | bjb1-32546 | GPU 0-4之一 | **RUNNING** (r2) | 1100/7251 | 1.93s/sample | ~3.3h | 2 files (500粒度) |
| **s4** | bjb1-32546 | GPU 0-4之一 | **RUNNING** (r2) | 1000/7251 | 2.05s/sample | ~3.6h | 2 files (500粒度) |
| **s5** | bjb1-32546 | GPU 0-4之一 | **RUNNING** (r2) | 1500/7251 | 2.02s/sample | ~3.2h | 混合(fix+r2) |
| **s6** | bjb1-32546 | GPU 5 (0%) | **DEAD** | 1500/7251 | — | — | 15 files (100粒度, 覆盖0-1500) |
| **s7** | bjb1-18228 | GPU 0-3之一 | **RUNNING** (r2) | 1100/7250 | 1.92s/sample | ~3.3h | 2 files (500粒度) |
| **s8** | bjb1-18228 | GPU 0-3之一 | **RUNNING** (r2) | 1100/7250 | 1.94s/sample | ~3.3h | 2 files (500粒度) |
| **s9** | bjb1-18228 | GPU 0-3之一 | **RUNNING** (r2) | 1100/7250 | 1.95s/sample | ~3.3h | 2 files (500粒度) |

### Spatial Shards (7 shards, ~8607 samples each)

| Shard | 服务器 | GPU | 状态 | 进度 | 速度 | 预计剩余 | Cache .pt |
|-------|--------|-----|------|------|------|----------|-----------|
| **s0** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1900/8608 | 2.27s/sample | ~4.2h | 3 files (500粒度) |
| **s1** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1900/8607 | 2.26s/sample | ~4.2h | 3 files |
| **s2** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1900/8607 | 2.22s/sample | ~4.1h | 3 files |
| **s3** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1800/8607 | 2.27s/sample | ~4.3h | 3 files |
| **s4** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1900/8607 | 2.21s/sample | ~4.1h | 3 files |
| **s5** | bjb2-28827 | GPU 0-5之一 | **RUNNING** | 1800/8607 | 2.31s/sample | ~4.4h | 3 files |
| **s6** | bjb1-18228 | GPU 0-3之一 | **RUNNING** | 2200/8607 | 1.90s/sample | ~3.4h | 4 files (500粒度) |

### 问题

1. **Object shard 6 已死** — bjb1-32546 GPU 5 空闲(0% util, 1 MiB)，进程停在 1500/7251。已有 1500 samples 缓存可复用。
2. **Object shard 0 r2 尝试 OOM 崩溃** — bjb2-40593 有 2 个 GPU 进程各占 9.6 GB，r2 启动时 OOM。但**原始进程仍在运行**（shard0.log 活跃更新到 2700/7251），只是速度较慢(3.38s vs ~2s)。
3. **bjb1-32546 GPU 5 闲置** — 可以用来重启 Object shard 6（从 1500 处 resume）。

### Cache 总计

| 服务器 | .pt 文件数 |
|--------|-----------|
| bjb1-32546 | 88 |
| bjb1-18228 | 139 (含旧 s1-s4 数据) |
| bjb2-28827 | 18 |
| bjb2-40593 | 30 |

---
