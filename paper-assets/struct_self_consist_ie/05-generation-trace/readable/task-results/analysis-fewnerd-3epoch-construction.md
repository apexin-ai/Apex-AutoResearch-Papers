# analysis fewnerd 3epoch construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd-3epoch-construction_20260524T071447_result.json`
- **Structured JSON:** [`3b8d5b1680a694a17379.json`](../../sessions/3b/3b8d5b1680a694a17379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Dataset | Seeds | MV Δ | LP Δ | Pooled p |
|---------|-------|------|------|----------|
| FewNERD (3-epoch) | 42, 456 | -0.03pp (n.s.) | **+0.74pp** | <0.001 |

关键发现：
- LP construction 方向与论文一致（+0.74pp vs 论文报的 +1.40pp），pooled p<0.001
- 种子间方差大：seed42 LP Δ=-0.04pp，seed456 LP Δ=+1.52pp
- MV construction 在 FewNERD 上无效（-0.03pp, p=0.64），LP 加权是关键

报告已写入 `artifacts/rebuttal_construction_fewnerd_3epoch.md`。

---
