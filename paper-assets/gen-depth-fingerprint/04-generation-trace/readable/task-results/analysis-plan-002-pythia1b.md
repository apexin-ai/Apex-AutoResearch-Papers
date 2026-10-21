# analysis plan 002 pythia1b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-002-pythia1b_20260514T205159_result.json`
- **Structured JSON:** [`b6b737d8318ee42010d7.json`](../../sessions/b6/b6b737d8318ee42010d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息齐全。汇总如下：

---

## Plan-002 Pythia-1B 生成结果分析

### Shard 状态

| | shard-0 | shard-1 |
|---|---|---|
| **状态** | 成功 (EXIT_CODE=0) | 成功 (EXIT_CODE=0) |
| **文件路径** | `data/pythia-1b/generations_shard0.jsonl` | `data/pythia-1b/generations_shard1.jsonl` |
| **文件大小** | 2.50 MB | 2.44 MB |
| **记录数** | 2286 | 2269 |
| **seed 数** | 497 | 498 |
| **seed_id 范围** | 0–496 | 497–999 (首条 seed_id=497) |
| **跳过数** | 91 | 100 |
| **耗时** | 2296.7s (~38min) | 2247.6s (~37min) |
| **error/traceback** | 0 | 0 |
| **空文本记录** | 0 | 0 |

### 各 depth 记录数分布

| depth | shard-0 | shard-1 | 合计 |
|-------|---------|---------|------|
| 0 | 497 | 498 | 995 |
| 1 | 497 | 496 | 993 |
| 2 | 457 | 455 | 912 |
| 3 | 429 | 422 | 851 |
| 4 | 406 | 398 | 804 |
| **总计** | **2286** | **2269** | **4555** |

### 数据质量

- **无 error/exception/traceback**，两个 shard 均干净完成
- **无空文本记录**（空输出已在生成阶段被 skip，未写入文件）
- **depth 衰减模式符合预期**：depth 越深，被跳过的比例越高（empty output），depth-0 几乎无损（995/995），depth-4 丢失约 19%（804/995）。这是 Pythia-1B 模型能力有限导致的——深层 continuation 容易产生空输出
- **数据格式正确**：每条记录包含 `id`, `depth`, `text`, `seed_id`, `token_count`, `model` 字段，token_count=256

### Shard 合并

两个 shard seed_id 无重叠（shard-0: 0–496, shard-1: 497–999），可以直接 `cat` 合并。id 字段需注意：shard-1 的 id 从 2485 开始，与 shard-0（0–2285）不重叠，合并后 id 全局唯一。

是否需要执行合并操作？

---
