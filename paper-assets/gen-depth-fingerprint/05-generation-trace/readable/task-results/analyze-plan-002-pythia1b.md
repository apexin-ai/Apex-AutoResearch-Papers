# analyze plan 002 pythia1b

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_plan-002-pythia1b_20260514T205112_result.json`
- **Structured JSON:** [`022cb0f505fbaa683d9e.json`](../../sessions/02/022cb0f505fbaa683d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan-002 Pythia-1B 生成结果汇总

### 总览

| | Shard 0 | Shard 1 | 合计 |
|---|---|---|---|
| Seeds | 497 (id 0-496) | 498 (id 497-994) | 995 |
| 写入记录数 | 2,286 | 2,269 | **4,555** |
| 理想记录数 (seeds×5) | 2,485 | 2,490 | 4,975 |
| 丢失记录 | 199 | 221 | 420 |
| WARNING 事件数 | 91 | 100 | 191 |
| 耗时 | 2,296.7s (38.3min) | 2,247.6s (37.5min) | ~75.8min |
| 吞吐 | 0.21 seeds/s | 0.22 seeds/s | — |
| EXIT_CODE | 0 | 0 | — |

> 注意：`wiki_seed_1000.jsonl` 实际只有 995 条 seed，非 1000 条。

### Depth 分布

| Depth | Shard 0 | Shard 1 | 合计 | 缺失率 |
|---|---|---|---|---|
| 0 | 497 | 498 | 995 | 0% |
| 1 | 497 | 496 | 993 | 0.2% |
| 2 | 457 | 455 | 912 | 8.3% |
| 3 | 429 | 422 | 851 | 14.5% |
| 4 | 406 | 398 | 804 | 19.2% |

跳过原因几乎全部是 `empty output`（少数 `empty input`），即链式续写中某一步生成了空文本导致链断裂。depth 越深缺失越多，符合预期——链式退化的累积效应。

### 输出文件

| 文件 | 大小 | 行数 |
|---|---|---|
| `data/pythia-1b/generations_shard0.jsonl` | 2.4M | 2,286 |
| `data/pythia-1b/generations_shard1.jsonl` | 2.4M | 2,269 |

### 数据格式

每条记录包含字段：`id`, `depth`, `text`, `seed_id`, `token_count`, `model`。`token_count` 均为 256，`model` 为 `pythia-1b`。格式正确。

高 depth 文本出现明显退化（重复循环），这是预期行为——正是 gen-depth fingerprint 实验要捕捉的信号。

### 结论

**生成成功完成。** 两个 shard 均正常退出，4,555 条记录已写入，完成率 91.6%（4,555/4,975）。缺失的 8.4% 来自链式续写中的空输出断链，集中在 depth 2-4，属于 Pythia-1B 模型在特定 seed 上的正常退化现象，不影响实验分析。

---
