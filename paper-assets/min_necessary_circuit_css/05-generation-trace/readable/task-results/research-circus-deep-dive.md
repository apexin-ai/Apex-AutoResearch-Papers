# research circus deep dive

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_circus_deep_dive_20260512T221843_result.json`
- **Structured JSON:** [`5b214e2dec362adc9e24.json`](../../sessions/5b/5b214e2dec362adc9e24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Q5 结论（最关键）：CIRCUS **没有**做跨方法比较

CIRCUS 只使用一种底层方法（CLT attribution graphs），变化的是剪枝阈值配置，不涉及 EAP/ACDC/EP 等不同 circuit discovery 算法。这确认了 CSS 的核心差异点。

## CSS vs CIRCUS 精确差异

| 维度 | CIRCUS | CSS (ours) |
|------|--------|-----------|
| 变化什么 | 单方法内剪枝阈值 | 不同算法族 (gradient/mask/causal) |
| 方法数 | 1 种 (CLT attribution) | K=3+ 种根本不同算法 |
| 稳定性来源 | Intra-method 阈值鲁棒性 | Cross-method 算法间一致性 |
| 聚合方式 | 连续 s(e)∈[0,1] + strict τ=1 | 二值投票 ≥ threshold |
| 计算开销 | 极低 (5.5%) | 需运行 K 种完整 pipeline |
| 跨方法分析 | 不做 | Pairwise Jaccard / agreement matrix |

**核心论点**：CIRCUS 回答"这条边对阈值选择鲁棒吗？"，CSS 回答"这条边是算法无关的吗？"。不同算法有不同 inductive bias（梯度 vs 因果干预 vs 可微剪枝），跨方法共识的信息正交性远高于阈值变化。

## 其他要点

- **模型/任务**：Gemma-2-2B + Llama-3.2-1B，仅 short factoid completions（capitals, arithmetic, trivia），50/20 prompts
- **Consensus 公式**：s(e) = (1/B)Σ𝟙[e∈E(b)]，B=9 主实验，strict consensus τ=1
- **Faithfulness**：IR + KL divergence + activation patching (p=0.0004)，consensus ~40× smaller than union 但保持解释力
- **GitHub 仓库**：未公开

已追加到 `artifacts/related_work_notes.md` Section 1b。

Sources:
- [CIRCUS paper (arXiv)](https://arxiv.org/abs/2603.00523)
- [CIRCUS HTML full text](https://arxiv.org/html/2603.00523)
- [Swapnil Parekh's page](https://swapnilparekh.github.io/)

---
