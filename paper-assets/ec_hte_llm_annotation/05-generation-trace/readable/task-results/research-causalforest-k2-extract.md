# research causalforest k2 extract

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_causalforest-k2-extract_20260522T033916_result.json`
- **Structured JSON:** [`88e09eef60508be9cf5e.json`](../../sessions/88/88e09eef60508be9cf5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已保存至 `artifacts/causalforest_k2_results.md` 并注册 (`art_20260522_4b8f51`)。

**关键结论**：

1. **n_expert=500 时 EC-HTE 全面最优**：两个 regime 下 bias 降至 0.008（vs Naive 降幅 93%+），RMSE 和 Coverage 均最佳。

2. **Global correction 伤害低噪声子群**：Extreme regime 下，Global 将 S₀（π=0.05）的 bias 从 0.047 恶化到 0.125（2.6×），因为 pooled 混淆矩阵对干净子群过度校正。EC-HTE 避免了这个问题。

3. **EC-HTE 唯一弱点**：Moderate regime + n_expert=100 时，Global 的 RMSE 略优（0.095 vs 0.124），因为 π 值接近（0.10 vs 0.15）使全局估计几乎正确，而 per-subgroup 估计方差更大。n_expert=500 时 EC-HTE 恢复领先。

4. **exp-001 无 CausalForest 数据**，仅有混淆矩阵估计方法（naive/global_corrected/hb_dirichlet/mle_laplace）。

文件包含 Markdown 表格和可直接使用的 LaTeX snippet。

---
