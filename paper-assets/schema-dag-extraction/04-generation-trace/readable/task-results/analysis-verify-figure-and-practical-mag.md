# analysis verify figure and practical mag

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_figure_and_practical_mag_20260516T035935_result.json`
- **Structured JSON:** [`4872aef1834abf61cbe9.json`](../../sessions/48/4872aef1834abf61cbe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/d037_data_consistency_check.json`。

**汇总：**

| 检查项 | 结果 |
|--------|------|
| **Figure 1a** | **MISMATCH** — 绘图脚本硬编码 pooled recall（count_22=0.527, count_44=0.551），论文正文引用 macro-avg recall（0.522, 0.549）。两组数值均来自同一 round2 JSON，分别是 `pooled_recall` 和 `mean_recall` 字段 |
| **Cluster Bootstrap CI** | FewNERD [0.069, 0.219]，MAVEN [0.081, 0.185]，均显著排除零 |
| **Practical Magnitude** | 论文 IQR=0.054/gap=2.2pp 与 `w2_practical_effect_results.json`（100 random 16-type subsets）的 0.0539/2.16pp 一致（四舍五入）。Director 提到的 IQR=0.066/gap=2.63pp 来自 `round2_statistical_analyses.json` 的 `80pool_16sub` 条目，对应原始 n=25 batches 分析（BCS 分布不同，但回归斜率相同 -0.401） |

---
