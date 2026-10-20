# analysis scierc construction aligned

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc-construction-aligned_20260523T193856_result.json`
- **Structured JSON:** [`083aa0e4118c48cdda66.json`](../../sessions/08/083aa0e4118c48cdda66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `artifacts/scierc_5seed_construction_aligned_report.md` 并注册。

**结果摘要：**

| Seed | Greedy F1 | Construction F1 | Δ (pp) | p-value | Sign |
|------|-----------|-----------------|--------|---------|------|
| 42 | 65.02 | 64.44 | −0.58 | 0.8242 | − |
| 123 | 64.71 | 65.67 | +0.96 | 0.0853 | + |
| 456 | 64.56 | 66.47 | +1.91 | 0.0031* | + |
| 2024 | 64.78 | 66.25 | +1.48 | 0.0233* | + |
| 3141 | 64.27 | 66.05 | +1.78 | 0.0075* | + |

- **Mean Δ:** +1.11pp ± 1.01, **4/5 positive**
- **Pooled p:** 0.0003 (significant)
- **对齐影响：** Gold-filter 使 seed 2024 的 Δ 从 +0.87→+1.48pp，seed 3141 从 +0.62→+1.78pp（22 个 gold-empty instances 被移除后增益更明显）
- **论文建议：** "non-significant +0.32pp" 应改为 "+1.11pp (p < 0.001)"

---
