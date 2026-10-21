# analysis phase diagram t25 a060 s42 fp32 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t25_a060_s42_fp32_v3_20260522T064047_result.json`
- **Structured JSON:** [`eaecef25f48c11f3708c.json`](../../sessions/ea/eaecef25f48c11f3708c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## T=25 α=0.60 结果：**Scenario A 确认**

| 指标 | 结果 |
|------|------|
| **PermG (FDR forward)** | **5/8** |
| Robust pairs (≥3/5 methods) | 6/8 |
| Diff XCorr (FDR) | 8/8 |
| Threshold Onset | 6/8 |
| TY Granger | 4/8 |
| Reverse PermG | 0/8（方向性确认） |
| Final perplexity | 61.95 |
| Final batch loss | 0.2753 |

**关键发现**：α=0.60 的 sync-dip（T=10/15/20 均为 PermG=0/8）在 T=25 消解为 5/8。对比 v2（13 代 → 0/8）和 v3（26 代 → 5/8），sync-dip 是**统计功效不足的伪象**，而非结构性特征。α_c 3-point fit 成立。

产出文件：
- `artifacts/D102_t25_a060_v3_analysis.md` — 完整分析报告
- `artifacts/D102_t25_a060_s42_fp32_v3.json` — 5method JSON

---
