# analysis 300 item subset distribution

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_300-item-subset-distribution_20260523T081151_result.json`
- **Structured JSON:** [`0e3d6cea7a59e79a431f.json`](../../sessions/0e/0e3d6cea7a59e79a431f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**300-item 随机子集在所有维度上都是无偏的：**

| 维度 | 检验 | 统计量 | p 值 | 效应量 |
|------|------|--------|------|--------|
| Difficulty | KS test | D=0.030 | 0.946 | Cohen's d=−0.020 |
| Domain | Chi-square | χ²=1.99 | 0.574 | Cramér's V=0.047 |
| RRF exposure | KS test | D=0.042 | 0.664 | — |
| Subject coverage | — | 52/57 | 91.2% | — |

关键发现：
- 子集是 `np.random.choice(14042, 300, seed=42)` 随机抽样，不是按 RRF 分数排序的 top-300
- 所有 p 值远大于 0.05，所有效应量 < 0.05（negligible）
- 对比实验：如果改用 RRF top-300，domain 分布会显著偏斜（χ²=31.6, p<0.001），Social Sciences 从 21.9% 涨到 34.7%

产出已注册：
- 报告：`artifacts/subset_distribution_analysis.md`
- 图表：`cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_analysis.{png,pdf}`
- JSON 原始数据：`cqa1:/root/contamcal-irt-calibration/analysis/subset_distribution_results.json`

---
