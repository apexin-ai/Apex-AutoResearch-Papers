# check training status all

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_status_all_20260516T080728_result.json`
- **Structured JSON:** [`6e89707c58c025f95474.json`](../../sessions/6e/6e89707c58c025f95474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全局训练状态快照 — 2026-05-16 16:10 CST

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 81,077 / 97,887 MiB (83%) | 99% |
| 1 | 94,329 / 97,887 MiB (96%) | 100% |

### 进程状态

| 任务 | PID | 状态 | 当前进度 | 详情 |
|------|-----|------|---------|------|
| **Qwen 主链** | 337267 | **运行中** | [6/9] `dataflow_aware_s44`, step 800/~2816 (28%) | 5/9 completed. loss=0.0433, best R@1=0.5701, val_loss=0.4944 |
| **StarCoder 链** | 519791 (→129747) | **运行中** | `embedding_distance_s43`, step 800/~2810 (28%) | 4 subruns done (random×3 + emb_dist_s42). loss=0.3149, best R@1=0.4810, val_loss=0.5229 |
| **UniXcoder** | 161238/161239 | **刚完成/过渡中** | `embedding_distance_s42` early stopped @ step 1200 | random_s42 ✓ (有 final), emb_dist_s42 ✓ (best val_loss=0.4466 @ step 600, R@1=0.5440). 原 PID 149858 已退出 |
| **RepoBench eval** | 159860 (→158952) | **运行中** | 等待 `repobench_random_s42` eval 完成 | PID 158952 运行 ~16min, eval Qwen random_s42 checkpoint, GPU 1 占 24GB |
| **Watcher (Qwen)** | 966920 | **存活** | — | `watch_and_chain_qwen_s42.sh` |
| **Watcher (StarCoder)** | 20226 | **存活** | — | `watch_and_chain_starcoder_s42.sh` |

### Qwen 链完成记录

| # | Subrun | 开始时间 | 完成时间 | 耗时 |
|---|--------|---------|---------|------|
| 1 | random_s43 | May 14 19:24 | May 15 01:58 | ~6.5h |
| 2 | random_s44 | May 15 01:58 | May 15 08:32 | ~6.5h |
| 3 | embedding_distance_s43 | May 15 08:32 | May 15 14:50 | ~6.3h |
| 4 | embedding_distance_s44 | May 15 14:50 | May 15 23:53 | ~9h |
| 5 | dataflow_aware_s43 | May 15 23:53 | May 16 10:54 | ~11h |
| **6** | **dataflow_aware_s44** | **May 16 10:54** | **进行中** | ~5.3h in, step 800/2816 |

### UniXcoder 最终指标

| Subrun | Best val_loss | R@1 | R@5 | 结果 |
|--------|-------------|-----|-----|------|
| random_s42 | — | — | — | 完成 (有 final checkpoint) |
| embedding_distance_s42 | 0.4466 (step 600) | 0.5440 | 0.9758 | Early stopped @ step 1200 |

### 关键观察

1. **UniXcoder 原 PID 149858 已不存在**，PID 161238/161239 刚启动（16:07），但 train.log 已显示 early stopping。UniXcoder 链可能缺少后续 subrun 的自动调度脚本——需确认 dataflow_aware 等后续 strategy 是否会自动启动。
2. **Qwen** 还剩 3 个 subrun（7-9/9），当前 subrun 按趋势估计再需 ~14h，整体 ETA 约 **May 18 中午**。
3. **StarCoder** 还剩 4 个 subrun（embedding_distance_s44 + dataflow_aware×3），整体 ETA 约 **May 19**。
4. **RepoBench eval** 正在 eval 第一个 checkpoint（random_s42），队列后续会依次 eval 其他完成的 checkpoints。

---
