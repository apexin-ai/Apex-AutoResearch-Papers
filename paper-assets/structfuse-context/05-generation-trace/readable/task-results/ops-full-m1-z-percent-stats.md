# ops full m1 z percent stats

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-m1-z-percent-stats_20260513T112118_result.json`
- **Structured JSON:** [`ea2e8fd900bb3da62495.json`](../../sessions/ea/ea2e8fd900bb3da62495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全量 Z% 统计结果

| 指标 | 值 |
|------|-----|
| Total instances | 44,173 |
| 有结构数据 | 15,153 (34.3%) |
| Z+（connected-not-gold > 0） | 11,825 |
| **条件 Z%**（Z+ / 有结构数据） | **78.0%** |
| 全量 Z%（Z+ / 全部） | 26.8% |

**与 pilot 对比**: Pilot 72.5% → 全量条件 Z% 78.0%（+5.5pp），趋势一致。

**关键问题**: 65.7% 的 instance 没有结构数据（call_graph/dataflow_paths 为空）。论文 Claim 1 的条件 Z%=78.0% 成立，但需明确讨论 coverage 限制——CodeQL/Beniget 仅对 34.3% 的 instance 产生了结构连接。

**Per-repo 分布**: 123 repos，19 repos Z%=0%（小型/单文件），Top repos 可达 93-95%（oauthlib, chardet, sqlparse）。Mean per-repo Z%=27.4%，Median=8.4%（被无结构数据 instance 拉低）。

已追加到 memory.md。

---
