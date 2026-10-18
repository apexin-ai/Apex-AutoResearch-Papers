# analysis bayesian equivalence bf01

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bayesian_equivalence_bf01_20260522T015858_result.json`
- **Structured JSON:** [`a6e18cb02be77ea10c6e.json`](../../sessions/a6/a6e18cb02be77ea10c6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| | BF₀₁ | 解读 |
|---|---|---|
| σ=1pp | 1.19 | anecdotal |
| σ=2pp | 1.40 | anecdotal |
| **σ=3pp** | **1.62** | **anecdotal** |
| σ=5pp | 2.08 | anecdotal |

- **Observed interaction**: −0.48 pp（magnitude 符合预期 ~0.47 pp）
- **SE**: 4.27 pp（每 cell 仅 12–13 个 batch，精度不足）
- **t(46) = −0.112**

BF₀₁ 全部 < 3，无法达到 "moderate evidence for null" 的门槛。根本原因是 2×2 median-split 后每个 cell 只有 12–13 个 batch，SE 相对于 effect size 太大（4.27 vs 0.48），数据信息量不足以让 Bayes factor 区分 H₀ 和 H₁。

BF₀₁ < 3，LaTeX 未生成。这个结果与 TOST p=0.209 一致——两种方法都指向同一个结论：**当前样本量下无法给出 interaction 是否为零的确定性结论**，但方向上数据略偏向 null（BF₀₁ > 1）。

脚本和 JSON 已保存到 artifacts 目录。

---
