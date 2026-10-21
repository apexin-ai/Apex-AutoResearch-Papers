# analysis scierc 5seed construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-5seed-construction_20260523T191438_result.json`
- **Structured JSON:** [`c432bb3cd38d0f16b97d.json`](../../sessions/c4/c432bb3cd38d0f16b97d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

| Seed | Δ (pp) | p-value |
|------|--------|---------|
| 42   | −0.58  | 0.82    |
| 123  | +0.96  | 0.09    |
| 456  | +1.91  | 0.003*  |
| 2024 | +1.48  | 0.023*  |
| 3141 | +1.78  | 0.008*  |

**Mean Δ = +1.11pp, 4/5 positive, pooled p = 0.0003。**

与论文报告的 "+0.32pp n.s." 不一致——当前结果更强。差异可能是因为论文引用了旧实验 `exp_001_seed42_v2`（恰好对应 seed 42 的负方向结果）。如果确认使用 `scierc_mf4v2` 数据，可以将 entity construction claim 从 n.s. 升级为 significant（p<0.001），但需注明 seed 42 为唯一负方向。

---
