# analysis silhouette final fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_silhouette_final_fix_20260521T031755_result.json`
- **Structured JSON:** [`2a583767e22afdaabcf2.json`](../../sessions/2a/2a583767e22afdaabcf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：**

- **0.632 不可复现。** 仅存在于初始 commit (ac60b7e)，穷举所有 baseline/d公式/数据模式/缩放方式均无法得到此值，大概率来自早期已不存在的数据快照。
- **推荐值：0.660**（k=2 KMeans，features_8gen.csv，gen-1 vs gen-2+ Cohen's d + |Spearman ρ|，StandardScaler）
- 最接近 0.632 的是 Test 1（3-class pooled d 硬编码值）= 0.6239，但这不是从数据直接计算的标准方法
- 该分区在所有 35 种 3-vs-4 二分中排名 #1，是最优划分

需要替换的位置：results.tex (×2), appendix_ddr_validation.tex (×2), appendix_instruct.tex (×1), plot_instruct_ddr_comparison.py (×1)

结果已保存到 `artifacts/_project/analysis/silhouette_final_determination.txt`。

---
