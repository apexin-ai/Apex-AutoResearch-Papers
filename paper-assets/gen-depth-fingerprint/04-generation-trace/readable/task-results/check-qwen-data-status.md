# check qwen data status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-data-status_20260514T222818_result.json`
- **Structured JSON:** [`4d937385ad32882e206d.json`](../../sessions/4d/4d937385ad32882e206d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 进程状态

| PID | 模型 | Shard | 状态 | 运行时间 |
|-----|------|-------|------|---------|
| 117855 | qwen3-0.6b | 0 | **Rl (运行中)** | 1h03m |
| 118126 | qwen3-0.6b | 1 | **Rl (运行中)** | 1h03m |
| 120617 | qwen3-1.7b | 0 | **Rl (运行中)** | 30m |
| 120694 | qwen3-1.7b | 1 | **Rl (运行中)** | 30m |

### GPU 使用率

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| 0 | 40% | 3977 MiB |
| 1 | 44% | 3977 MiB |
| 2 | 34% | 1825 MiB |
| 3 | 33% | 1825 MiB |

GPU 0-1 跑 Qwen3-1.7B（显存更大），GPU 2-3 跑 Qwen3-0.6B。全部活跃计算中。

### 数据进度

**已完成模型：**

| 模型 | 行数 | 已合并 | 状态 |
|------|------|--------|------|
| pythia-1b | 4555 | ✅ generations.jsonl | 完整（seed 0-999, depth 0-4, 804 seeds 达到 depth 4） |
| olmo-2-1b | 4713 | ✅ generations.jsonl | 完整 |

**进行中模型：**

| 模型 | Shard | 行数 | 最后 seed_id | 最后 depth | Seed 进度 | 预估完成度 |
|------|-------|------|-------------|-----------|----------|-----------|
| qwen3-0.6b | 0 | 1593 | 350 | 0 | 350/500 (70%) | ~70% |
| qwen3-0.6b | 1 | 1542 | 840 | 3 | 340/500 (68%) | ~68% |
| qwen3-1.7b | 0 | 1331 | 289 | 3 | 289/500 (58%) | ~58% |
| qwen3-1.7b | 1 | 1384 | 795 | 0 | 295/500 (59%) | ~59% |

**均未合并**（无 generations.jsonl，只有 shard 文件）。

### 预估剩余时间

- **Qwen3-0.6b**：3135 行 / 63 min ≈ 50 行/min，预计总量 ~4600 行，剩余 ~30 min
- **Qwen3-1.7b**：2715 行 / 30 min ≈ 90 行/min，预计总量 ~4600 行，剩余 ~20 min

### 结论

- 4 个进程全部存活运行中，tmux session 死亡后进程仍在以 orphan 方式继续执行，数据在正常写入
- **无需重跑**，等待 ~30 min 即可全部完成
- 完成后需要合并 shard 文件为 `generations.jsonl`

---
