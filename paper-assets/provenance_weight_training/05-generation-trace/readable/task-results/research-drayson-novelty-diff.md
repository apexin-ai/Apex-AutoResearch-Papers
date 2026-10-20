# research drayson novelty diff

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_drayson-novelty-diff_20260514T150031_result.json`
- **Structured JSON:** [`7d3f216f63e96cac059d.json`](../../sessions/7d/7d3f216f63e96cac059d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

**Drayson et al. 的 b 选择方式**：验证集 empirical 选取（WikiText-2 validation 上跑 1 generation 后选最佳），per-model 固定（GPT-2/SmolLM 135M/360M 用 b=10，SmolLM 1.7B 用 b=1），无系统性 ablation。本质是 manual tuning，比 grid search 更粗糙。

**我们的差异化空间确认存在**：
1. **Adaptive b*** 无人做过——所有现有 contamination-aware weighting 方法要么固定 b，要么不用 detection score
2. **Unknown proportion setting** 是与 Drayson 最大的问题设置差异（他们控制混合比例，我们估计）
3. **Lightweight detector sufficiency** 也是有效差异点（他们用 ModernBERT AUC=0.986，我们用 TF-IDF AUC=0.939）

**建议 narrative**：主打 Angle A（heuristic→principled）+ B（unknown proportion），用 Angle C（soft-to-hard continuum）作为 Method 框架呈现。

---
