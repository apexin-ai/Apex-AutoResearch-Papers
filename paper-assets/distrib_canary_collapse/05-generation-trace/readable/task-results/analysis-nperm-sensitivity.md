# analysis nperm sensitivity

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nperm_sensitivity_20260517T020808_result.json`
- **Structured JSON:** [`adb36494e5e5b7614364.json`](../../sessions/ad/adb36494e5e5b7614364.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**n_perm 稳定性分析结论：p 值高度稳定，n_perm=5000 足够。**

| 指标 | 值 |
|------|-----|
| Max \|p(5k) - p(10k)\| | 0.0098 |
| Mean \|Δ\| | 0.0016 |
| 显著性翻转 | **0** |

所有 forward 方向 p 值变化 < 0.002，reverse 方向最大变化 0.0098（出现在非显著的 ece→distinct_1 reverse, seed 44, p≈0.26→0.27）。没有任何 pair 在 5k 显著但 10k 不显著（或反之）。

产出文件：
- `results/rebuttal/nperm_10k/a075_s{42,43,44}_perm10k.json`
- `results/rebuttal/nperm_stability.json`
- `results/rebuttal/nperm_stability_summary.txt`

---
