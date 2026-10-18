# analysis feature importance stability

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_feature_importance_stability_20260514T223439_result.json`
- **Structured JSON:** [`32d6195c6b979969149b.json`](../../sessions/32/32d6195c6b979969149b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

### 核心结论

**Universal Core 4 特征**（所有 6 实验 top-5）：var_surprisal、p90_ppl、mean_surprisal、p75_ppl，累积占总 importance 的 44-68%。全部是 surprise/perplexity-based，lexical diversity 特征无一进入稳定 top-5。

**Spearman rank correlation**：
- 同模型跨策略：ρ = 0.859（Pythia t09 与 k50 完全一致 ρ=1.000）
- 同策略跨模型：ρ = 0.801
- 跨策略一致性 > 跨模型一致性

**主要异常**：mean_ppl 变异最大（CV=0.64），在 Pythia 稳定 rank 3 但在 GPT2XL_t09 collapse 到 rank 18，属共线性导致的 importance 重分配。

**产出**：
- 完整分析报告 → `artifacts/feature_importance_consistency_analysis.md`
- 关键 insight → `memory.md` 已更新
- 推荐论文 figure：feature importance heatmap（6 实验 × 19 特征），配合文中 Spearman ρ 量化论证

---
