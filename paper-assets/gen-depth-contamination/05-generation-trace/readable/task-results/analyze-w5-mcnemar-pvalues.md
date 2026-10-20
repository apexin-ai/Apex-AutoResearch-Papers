# analyze w5 mcnemar pvalues

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_w5-mcnemar-pvalues_20260518T151645_result.json`
- **Structured JSON:** [`556bd72799cfbad4302d.json`](../../sessions/55/556bd72799cfbad4302d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Claim "all McNemar p < 0.01" 不成立。**

36 组对比 (12 config x 3 baseline classifiers)，只有 4/36 达到 p < 0.01，31/36 完全不显著。

关键发现:

| 统计 | 值 |
|------|-----|
| 总比较数 | 36 |
| p < 0.01 | 4 (11%) |
| p < 0.05 | 5 (14%) |
| p >= 0.05 | 31 (86%) |
| Max p | 0.868 |

5 个显著结果中:
- **LLaMA-8B / C4**: 3 个 baseline 都显著**优于** OBD (LogReg p=6.2e-5, SVC p=1.1e-4, RF p=1.3e-3)
- **Qwen-1.5B / Wiki**: OBD 显著优于 LogReg (p=9.4e-4) 和 SVC (p=2.3e-4)，但 RF 无差异

**结论**: 绝大多数配置下 OBD-LightGBM 与 LogReg/SVM/RF 无显著差异，说明 depth 可分性来自 15D 特征表示而非分类器选择。论文中 "all McNemar p < 0.01" 的 claim 需要修正或删除。

产出文件:
- LaTeX 表: `artifacts/mcnemar_pvalues/mcnemar_detail.tex`
- Summary: `artifacts/mcnemar_pvalues/summary.md`
- 原始 JSON: 远程 `results/mcnemar_obd_vs_baselines/mcnemar_results.json`

---
