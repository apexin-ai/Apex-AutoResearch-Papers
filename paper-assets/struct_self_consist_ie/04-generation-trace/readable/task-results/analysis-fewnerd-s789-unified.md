# analysis fewnerd s789 unified

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewnerd_s789_unified_20260518T230903_result.json`
- **Structured JSON:** [`d8c8536006fdcad4929c.json`](../../sessions/d8/d8c8536006fdcad4929c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 产出汇总

### 合并数据
- **路径**: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl`
- 3 分片 (12549 + 12549 + 12550) = **37648 行** ✓

### Seed789 分析结果 (`analysis.json`)

| 指标 | 值 |
|------|------|
| Greedy F1 | 0.7478 |
| Oracle F1 | 0.8714 |
| Headroom | 12.37pp |
| Degeneracy | 11.77% |
| LP Selection F1 | 0.7614 (+1.36pp) |
| DGS F1 | 0.7621 (+1.43pp vs greedy, +0.07pp vs LP) |
| LP Bootstrap 95% CI | [+1.19, +1.54]pp |

### 4-Seed 汇总 (42/123/456/789)

| 指标 | Mean | 95% CI |
|------|------|--------|
| Greedy F1 | 0.7481 | [0.7475, 0.7487] |
| Oracle F1 | 0.8739 | [0.8695, 0.8783] |
| LP Δ (pp) | **+1.38** | **[+1.32, +1.44]** |
| Degeneracy | 12.69% | [11.24%, 14.14%] |
| LP ρ_global | 0.217 | [0.173, 0.260] |

LP selection gain 在 4 seeds 上高度稳定（std=0.037pp），95% CI 完全在正区间，确认 FewNERD 上 LP selection 的统计显著性。

### Registry
- `exp_fewnerd_s789_n8` → DONE (success)
- Artifacts 已注册

---
