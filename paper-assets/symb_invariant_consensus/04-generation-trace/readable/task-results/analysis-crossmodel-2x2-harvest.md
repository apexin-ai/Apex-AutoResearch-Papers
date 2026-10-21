# analysis crossmodel 2x2 harvest

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crossmodel-2x2-harvest_20260521T213632_result.json`
- **Structured JSON:** [`8af82ba0bde6f3b9a64a.json`](../../sessions/8a/8af82ba0bde6f3b9a64a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 2×2 矩阵已保存到 `results/exp_d126_crossmodel_sica/crossmodel_2x2_metrics.json`。

**2×2 矩阵结果：**

|  | **Mistral ext** | **Qwen3 ext** |
|---|---|---|
| **Mistral gen** (SC=40.2%) | SICA 34.31%, Δ-5.88pp, BR 3.44, BR∞ 32.1%, κ 0.619 | SICA 79.90%, Δ+39.71pp, BR 2.85, BR∞ 17.1%, κ 0.619 |
| **Qwen3 gen** (SC=86.8%) | SICA 37.75%, Δ-49.02pp, BR 2.16, BR∞ 45.7%, κ 0.836 | SICA 79.90%, Δ-6.86pp, BR 1.16, BR∞ 63.4%, κ 0.836 |

关键发现：
- **Extractor 能力主导 SICA 准确率**：Qwen3 作为 extractor 无论 generator 是谁都达到 ~79.9%，Mistral 作为 extractor 都在 34-38%
- Mistral→Qwen3 方向出现罕见的 **+39.71pp** 提升（弱 generator + 强 extractor 组合）
- Qwen3→Mistral 方向 **-49.02pp** 大幅下降（强 generator 被弱 extractor 拖垮）
- Process-κ 只取决于 generator（Qwen3 0.836 >> Mistral 0.619）

---
