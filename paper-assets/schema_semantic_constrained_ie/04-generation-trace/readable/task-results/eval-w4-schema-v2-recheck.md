# eval w4 schema v2 recheck

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_w4_schema_v2_recheck_20260515T091628_result.json`
- **Structured JSON:** [`40d5f27194da5531fdbc.json`](../../sessions/40/40d5f27194da5531fdbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。v2 checker 版本为 `fixed_20260514_v2 (strip + alias + unique_et)`，核心变化是 ET 计算方式（strip 空格 + alias 归一化 + unique entity 去重）。

```
Schema-informed DocRED v2 checker results:
- ET: 0.19% (v1: 0.61%)  ← 降了 3x，v2 alias归一化消除了误报
- RV: 18.41% (v1: 18.41%)  ← 不变
- DR: 12.84% (v1: 12.84%)  ← 不变
- CF: 0.15% (v1: 0.15%)  ← 不变
- docs_checked: 943, parse_failures: 55
- total_triples: 16782, total_entities: 19524
- total_violation_rate: 14.63% (v1: 14.85%)
```

**唯一变化在 ET**：v1 报了 119 个 ET violations (0.61%)，v2 降到 38 个 (0.19%)。原因是 v2 checker 做了 entity type alias 归一化（PERSON→PER, ORGANIZATION→ORG 等），81 个原本判为违规的实际上是合法别名。

RV、DR、CF 三个指标完全不变——这符合预期，v2 只改了 ET 检测逻辑。

F1 指标不在 violation checker 输出中（需要单独的 F1 evaluation 脚本）。

---
