# ops w6 mistral docred constrained exit check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_w6_mistral_docred_constrained_exit_check_20260516T090813_result.json`
- **Structured JSON:** [`a2b46589f63f573cc468.json`](../../sessions/a2/a2b46589f63f573cc468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新完成。

---

## Metrics 完整表格

| Metric | Constrained | Unconstrained | Delta |
|--------|------------|---------------|-------|
| **ET_pct** | 0.00% | 7.58% | **-7.58pp** |
| **RV_pct** | 0.00% | 42.35% | **-42.35pp** |
| **DR_pct** | 33.20% | 57.42% | **-24.22pp** |
| **CF_pct** | 0.19% | 24.78% | **-24.59pp** |
| **E_F1** | 50.59% | 48.51% | **+2.08pp** |
| **E_P** | 65.02% | — | — |
| **E_R** | 41.40% | — | — |
| **R_F1** | 5.52% | 3.50% | **+2.02pp** |
| **R_P** | 5.67% | — | — |
| **R_R** | 5.37% | — | — |
| parse_fail_rate | 0.80% | — | — |
| total_samples | 998 | — | — |
| total_pred_entities | 12,535 | — | — |
| total_pred_relations | 11,554 | — | — |

## 结论

Grammar+Semantic 双层约束 (full_s1) 在 Mistral-7B + DocRED 上：
- **完全消除** ET 和 RV violations（0%）
- **DR 降幅 24.22pp**（57.42%→33.20%），残余 33% 为 semantic constraint 覆盖范围外的 domain-range 组合
- F1 无损反而微升（E_F1 +2.08pp, R_F1 +2.02pp），约束解码未牺牲质量

---
