# analysis fewnerd 3seed unified

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_3seed_unified_20260524T112009_result.json`
- **Structured JSON:** [`171a02081a012393876b.json`](../../sessions/17/171a02081a012393876b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
FewNERD 3-seed (s42, s456, s123) N=8 T=1.0 Qwen3-8B FT
Metric: entity-type-averaged macro-F1

| Seed   | Greedy | MV    | MV Δ(pp) | LP    | LP Δ(pp) | Oracle | Degen% |
|--------|--------|-------|----------|-------|----------|--------|--------|
| 42     | 75.07  | 70.44 | -4.63    | 75.30 | +0.23    | 85.52  | 9.1    |
| 456    | 75.12  | 71.93 | -3.20    | 75.11 | -0.01    | 86.30  | 8.1    |
| 123    | 75.06  | 71.44 | -3.62    | 75.22 | +0.15    | 86.81  | 9.2    |
| Mean±σ | 75.08±0.03 | 71.27±0.62 | -3.82±0.60 | 75.21±0.08 | +0.12±0.10 | 86.21±0.53 | 8.80±0.48 |
```

要点：
- **MV strict 在 macro-F1 下大幅损伤** (-3.82 pp)，所有 8 个 entity type 均为负 delta，"other" 和 "event" 最严重（-7.69, -5.17 pp）
- **LP 基本持平** (+0.12 pp)，方差极小（±0.10）
- **Oracle headroom** 约 +11.13 pp，说明 sample diversity 足够
- 数据来源：`fewnerd_mf4v2_seed42_v3`、`fewnerd_mf4v2_seed456`、`fewnerd_mf4v2_seed123_v4`（任务指定的 seed42/seed456 原路径为空目录）

已写入 `artifacts/fewnerd_3seed_unified_stats.txt` 并注册。

---
