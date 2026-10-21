# analysis plan 002 olmo2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-002-olmo2_20260514T211856_result.json`
- **Structured JSON:** [`02dce83605f3ab98c3c0.json`](../../sessions/02/02dce83605f3ab98c3c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已更新为 DONE/success。汇总：

### OLMo-2-1B 数据生成结果

| | Shard 0 | Shard 1 | **合计** |
|---|---|---|---|
| Records | 2,379 | 2,334 | **4,713** |
| Seeds | 497 | 498 | 995 |
| Skipped | 47 | 70 | 117 |
| Wall time | 3,885s (~65min) | 4,081s (~68min) | — |
| File size | 2.68 MB | 2.57 MB | 5.25 MB |

**Depth 分布：**

| Depth | S0 (OLMo-2) | S1 (OLMo-2) | S0 (Pythia ref) | S1 (Pythia ref) |
|---|---|---|---|---|
| gen0 | 497 | 498 | 497 | 498 |
| gen1 | 494 | 494 | 497 | 496 |
| gen2 | 477 | 470 | 457 | 455 |
| gen3 | 461 | 444 | 429 | 422 |
| gen4 | 450 | 428 | 406 | 398 |

OLMo-2 在深层 generation 的保留率明显高于 Pythia-1B（gen4: 450/428 vs 406/398），说明 OLMo-2 生成空输出的概率更低。数据质量正常，无 error/traceback。Registry 已更新完毕。

---
