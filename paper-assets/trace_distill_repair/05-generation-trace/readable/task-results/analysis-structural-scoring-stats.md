# analysis structural scoring stats

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_structural_scoring_stats_20260514T202717_result.json`
- **Structured JSON:** [`6a300b15c583271b733b.json`](../../sessions/6a/6a300b15c583271b733b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/phase2_structural_scoring_report.md`。

核心数据：

- **451 segments across 36 instances**, keep 23 (5.1%), 22 个 instance 全部 drop
- **按 segment type**: exception_chain keep rate 最高 (13.9%) > call_subtree (9.5%) > loop_iteration (2.0%) > basic_block (1.2%)
- **Keep 的 23 segments**: call_subtree 占 56.5%，token 中位数 319，confidence 均值仅 0.61
- **Line scoring 对比**: line segments 总计 ~61K (vs structural 451)，大 trace 上 ratio 达 600x+，line scoring LLM 调用量将是 structural 的 ~136 倍
- **>2K token 子集**: 32/36 instances

---
