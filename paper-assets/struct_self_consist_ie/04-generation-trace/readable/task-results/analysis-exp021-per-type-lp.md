# analysis exp021 per type lp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp021_per_type_lp_20260516T225811_result.json`
- **Structured JSON:** [`be0e9f3b97cc1dca5ffd.json`](../../sessions/be/be0e9f3b97cc1dca5ffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## Per-Entity-Type LP Selection 分析结果

| Type | N | Degen% | Greedy F1 | LP Sel F1 | Δ(pp) | LP ρ | Headroom |
|------|---:|-------:|----------:|----------:|------:|-----:|---------:|
| Event | 1306 | 6.0% | 0.6551 | 0.6616 | +0.65 | 0.457 | 16.14pp |
| Other | 3433 | 6.6% | 0.6374 | 0.6847 | **+4.73** | 0.491 | 19.40pp |
| Organization | 6647 | 6.7% | 0.7203 | 0.7324 | +1.21 | 0.509 | 13.32pp |
| Building | 1587 | 7.2% | 0.7024 | 0.7047 | +0.23 | 0.478 | 14.90pp |
| Product | 2276 | 8.2% | 0.6564 | 0.6765 | +2.01 | 0.483 | 15.77pp |
| Location | 8023 | 11.4% | 0.7926 | 0.7979 | +0.53 | 0.520 | 10.27pp |
| Person | 8016 | 13.4% | 0.8220 | 0.8345 | +1.25 | 0.544 | 9.22pp |
| Art | 1277 | 19.8% | 0.7557 | 0.7540 | -0.17 | 0.451 | 9.21pp |

## 因果链验证

- **Spearman(degeneracy, lp_delta) = -0.381** (p=0.352)：方向为负，但 8 个 data points 统计功效不足
- **Spearman(degeneracy, headroom) = -0.881** (p=0.004)：强显著负相关，degeneracy 高的 type headroom 小
- **Spearman(headroom, lp_delta) = +0.571** (p=0.139)：headroom 大 → LP delta 大，方向正确

解读：因果链 `low degeneracy → high headroom → LP effective` 在 type 粒度方向一致。Art type (degen 20%) 是唯一 LP 为负的 type；Other type (degen 最低 6.6%，headroom 最大 19.4pp) LP delta 最大 (+4.73pp)。

产出文件：
- 服务器：`output/exp_021_inference/per_type_lp_analysis.csv` + `per_type_lp_table.tex`
- 本地：`artifacts/per_type_lp_analysis.csv` + `artifacts/per_type_lp_table.tex`

---
