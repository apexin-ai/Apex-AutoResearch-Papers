# analysis plan 005 cont

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-005-cont_20260515T054130_result.json`
- **Structured JSON:** [`801001e940f1fb8cb84d.json`](../../sessions/80/801001e940f1fb8cb84d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## plan-005-cont 总结

**Pythia-2.8B continuation prompt type 数据生成 — 成功完成**

| 指标 | 值 |
|------|-----|
| Total records | 4,620 |
| Unique seeds | 995 (全部覆盖) |
| Skipped | 168 (empty output/input) |
| Depth 分布 | d0=995, d1=992, d2=932, d3=874, d4=827 |
| 文件大小 | 4.93 MB |
| 运行时间 | 7,760s (~2h 9min) |
| 输出文件 | `data/pythia-2.8b-continuation/generations_shard0.jsonl` |

Depth 分布符合预期：深度越大，empty output 越多（d0 全保留 → d4 保留 83%）。

**兄弟任务进度：**
- **plan-005-elab** (elaboration): 889/995 seeds (~89%)，已写 4,404 records，仍在运行
- **plan-005-rewrite** (inspired_rewriting): 931/995 seeds (~94%)，已写 4,494 records，仍在运行

两个兄弟任务预计 10-20 分钟内完成。

---
