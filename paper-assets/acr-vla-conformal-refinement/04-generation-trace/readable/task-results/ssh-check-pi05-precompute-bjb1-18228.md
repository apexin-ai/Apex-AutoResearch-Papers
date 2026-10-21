# ssh check pi05 precompute bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-pi05-precompute-bjb1-18228_20260524T004901_result.json`
- **Structured JSON:** [`1fc37c633ecd0281a9c8.json`](../../sessions/1f/1fc37c633ecd0281a9c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 Precompute 状态报告

### 当前活跃缓存：`/root/autodl-tmp/crm_cache_pi05/`

**配置**：10 shards, input_mode=full, 4 GPU 运行 shards 1-4, benchmarks=['object', 'spatial']

| Benchmark | 状态 | 详情 |
|-----------|------|------|
| **spatial** | **已完成** | 60,250 samples，merged files 就绪 (obs_features/k_samples/expert_actions.pt) |
| **object** | **进行中** | shards 0,5-9 已完成，shards 1-4 运行中；已有 merged (69,303/72,507 = 95.6%) |
| **long** | **未完成** | 仅 s0 的 36 个 partial (0.2GB)，当前无进程处理 |
| **goal** | **未开始** | 目录不存在 |

### Object 各 shard 进度

| Shard | 进度 | 速度 | 剩余时间 |
|-------|------|------|----------|
| 1 | 5300/7251 (73%) | 1.84s/sample | ~60 min |
| 2 | 4700/7251 (65%) | 2.07s/sample | ~88 min |
| 3 | 5100/7251 (70%) | 1.88s/sample | ~67 min |
| 4 | 5000/7251 (69%) | 1.93s/sample | ~72 min |

**Object ETA**：最慢 shard (2) 约 88 分钟 → 预计 ~14:30 UTC 完成

### 关键问题

**long 和 goal 的 precompute 尚未配置在当前运行中。** 当前 4 个 shard 仅处理 `['object', 'spatial']`。object 完成后这 4 个进程会结束（spatial 已完成无需重跑）。

需要额外启动 long 和 goal 的 precompute 才能开始完整的 CRM 训练。

### 另有旧缓存 `crm_cache_pi05_2048/`
4 个 benchmark 各有 s0 单 shard 的 partial 文件（long 53K, goal 51.5K, spatial 51.5K, object 54.5K），似乎是更早的单 GPU 预计算，已被弃用。

---
