# check qwen process status final

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-process-status-final_20260514T223844_result.json`
- **Structured JSON:** [`6ee7f2a1c0f57899d14c.json`](../../sessions/6e/6ee7f2a1c0f57899d14c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程状态：4 个全部运行中

| PID | 模型 | Shard | 状态 | 运行时间 | GPU | GPU利用率 | 显存 |
|-----|------|-------|------|---------|-----|----------|------|
| 117855 | Qwen3-0.6B | 0 | Running (Rl) | 1h13m | cuda:2 | 34% | 1825 MiB |
| 118126 | Qwen3-0.6B | 1 | Running (Rl) | 1h13m | cuda:3 | 33% | 1825 MiB |
| 120617 | Qwen3-1.7B | 0 | Running (Rl) | 40m | cuda:0 | 39% | 3977 MiB |
| 120694 | Qwen3-1.7B | 1 | Running (Rl) | 40m | cuda:1 | 44% | 3977 MiB |

### 数据文件进度

总 seeds: 1000（shard0: 0-499, shard1: 500-999），max_depth=4

| 模型 | Shard | 行数 | 当前 seed_id | 进度 |
|------|-------|------|-------------|------|
| qwen3-0.6b | 0 | 1847 | ~409 | **~82%** |
| qwen3-0.6b | 1 | 1787 | ~899 | **~80%** |
| qwen3-1.7b | 0 | 1553 | ~341 | **~68%** |
| qwen3-1.7b | 1 | 1625 | ~854 | **~71%** |

### 合并状态

两个模型均 **NOT_MERGED**（`generations.jsonl` 不存在）。

### 结论

- 4 个进程全部正常运行中，GPU 活跃
- **Qwen3-0.6B**: ~80-82% 完成，已运行 73 min，预计再 ~16 min 完成
- **Qwen3-1.7B**: ~68-71% 完成，已运行 41 min，预计再 ~18 min 完成
- 均未完成，需要继续等待，不要合并

---
