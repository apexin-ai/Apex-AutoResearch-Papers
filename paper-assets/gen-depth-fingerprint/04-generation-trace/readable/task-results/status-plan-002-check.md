# status plan 002 check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_plan-002-check_20260514T205506_result.json`
- **Structured JSON:** [`3363054d252071bf72c8.json`](../../sessions/33/3363054d252071bf72c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan-002 状态汇总

### 1. 进程状态

| 任务 | PID | 状态 | 运行时间 | GPU |
|------|-----|------|----------|-----|
| pythia1b-s0 | 108021 | **已完成** (EXIT_CODE=0) | — | — |
| pythia1b-s1 | 108098 | **已完成** (EXIT_CODE=0) | — | — |
| olmo2-s0 | 108242 | **运行中** | 46 min | cuda:2 (3614 MiB) |
| olmo2-s1 | 108452 | **运行中** | 46 min | cuda:3 (3614 MiB) |
| qwen3-1_7b-s0 | 111533 | **运行中** | 3 min | cuda:0 (3968 MiB) |
| qwen3-1_7b-s1 | 111646 | **运行中** | 3 min | cuda:1 (3968 MiB) |
| qwen17b-s0 | 112179 | **运行中** | 2 min 42s | cuda:0 (3968 MiB) |
| qwen17b-s1 | 112264 | **运行中** | 2 min 40s | cuda:1 (3968 MiB) |

### 2. Pythia-1B 输出完整性

| 文件 | 行数 | 跳过 | 耗时 |
|------|------|------|------|
| `data/pythia-1b/generations_shard0.jsonl` | 2286 | 91 | 2296.7s |
| `data/pythia-1b/generations_shard1.jsonl` | 2269 | 100 | 2247.6s |
| **合计** | **4555** | **191** | — |

与预期（~5000 = 1000 seeds × 5 depths）相比缺少 ~445 条，其中 191 条是因 empty output 被跳过，另外约 254 条差异可能来自 seed 文件实际不足 1000（olmo 日志显示只加载了 995 seeds）。**pythia1b 任务已正常完成。**

### 3. OLMo-2 进度

| 文件 | 当前行数 | 预期 |
|------|----------|------|
| `data/olmo-2-1b/generations_shard0.jsonl` | 1693 | ~2485 |
| `data/olmo-2-1b/generations_shard1.jsonl` | 1589 | ~2485 |

olmo 速度约 8.5s/seed，已跑 46 分钟，进度约 68%/64%。按此速度还需约 20-25 分钟完成。

### 4. Qwen 重复提交冲突 — 严重问题

**qwen3-1_7b 和 qwen17b 是完全重复的任务**，两组进程使用：
- 相同的 `--model-name qwen3-1.7b`
- 相同的 `--model-path Qwen3-1___7B-Base`
- 相同的 `--shard-id 0/1`
- 写入相同的输出文件 `data/qwen3-1.7b/generations_shard{0,1}.jsonl`

两组进程**共享 GPU 0 和 GPU 1**（每个 GPU 上有两个进程，各占 3968 MiB，合计 ~7950 MiB）。当前输出文件仅 63/60 行，两组进程同时写同一文件，**存在数据交错/损坏风险**。

建议：kill 掉 qwen17b 的两个进程（PID 112179, 112264），清空输出文件后让 qwen3-1_7b 独占 GPU 0/1 重跑。

### 5. GPU 占用

| GPU | 显存占用 | 利用率 | 进程 |
|-----|----------|--------|------|
| 0 | 7950 MiB | 86% | qwen3-1_7b-s0 + qwen17b-s0（冲突） |
| 1 | 7950 MiB | 86% | qwen3-1_7b-s1 + qwen17b-s1（冲突） |
| 2 | 3623 MiB | 50% | olmo2-s0 |
| 3 | 3623 MiB | 43% | olmo2-s1 |

### 6. Qwen3-0.6B 模型

**已下载**：`/root/autodl-tmp/models/Qwen/Qwen3-0.6B-Base` 和 `Qwen3-0___6B-Base` 均存在。Qwen3-1.7B-Base 也已就位。

---
