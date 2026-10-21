# code w10 beam ablation k2 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w10_beam_ablation_k2_collect_20260517T092650_result.json`
- **Structured JSON:** [`c7543989b40564fb03fa.json`](../../sessions/c7/c7543989b40564fb03fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需删除。

---

## w10_beam_ablation_k2 实验结果

| 指标 | beam k=2 | greedy | beam k=4 |
|------|----------|--------|----------|
| DR violation rate | **0.35%** | 0.93% | 0% |
| CF violations | 71 | 9.90% | 0.53% |
| Entity F1 | **31.54** | 30.98 | 32.00 |
| Relation F1 | **8.75** | 8.36 | 8.56 |

### 完整 violation metrics
- JSON failures: 0/551 (0.0%)
- Entity type violations: 0/2473 (0.0%)
- Relation vocab violations: 0/1724 (0.0%)
- Domain/Range violations: 6/1724 (0.4%)
- Cross-field consistency violations: 71
- Go/No-go DR rate: 0.0035

### 对比分析

**vs greedy**: beam k=2 在所有指标上均有提升。DR 从 0.93% 降到 0.35%，E_F1 +0.56，R_F1 +0.39。

**vs beam k=4**: k=2 的 DR 略高（0.35% vs 0%），E_F1 略低（31.54 vs 32.00），R_F1 略高（8.75 vs 8.56）。k=4 在约束满足上更好（DR=0），但 k=2 的关系抽取 F1 稍强。

**结论**: beam search 相对 greedy 有明确增益。k=2 和 k=4 差异较小，k=4 在约束满足上更优（DR=0），k=2 在 R_F1 上微优。整体趋势：beam width 越大约束违反越少，F1 差异不大。

---
