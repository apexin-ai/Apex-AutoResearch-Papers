# research crossover literature

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_crossover-literature_20260514T022820_result.json`
- **Structured JSON:** [`83fc9746d20590fc2bca.json`](../../sessions/83/83fc9746d20590fc2bca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研结果

### 核心回答：没有人报告过 importance vs random 的 phase-dependent crossover

搜索了 2024-2026 年的 KV cache eviction、attention pruning、compound sparsity 相关文献，**没有找到任何论文直接报告过**同一 eviction strategy 在不同 attention concentration phase 下相对优劣反转的现象。这是一个 novel finding。

### 8 篇直接相关论文

| # | 论文 | Venue | 与我们的关联 |
|---|------|-------|-------------|
| 1 | [DefensiveKV](https://openreview.net/forum?id=nJgS06sX3O) | ICLR'26 | Importance score 的 stability assumption 是脆弱的，mean aggregation 在极端情况下失效。**解释了 why**，但没与 phase/random 联系 |
| 2 | [NACL](https://aclanthology.org/2024.acl-long.428/) | ACL'24 | 混合 importance + random eviction 来弥补 attention bias。**隐含承认** importance 在某些情况不如 random，但未分析 phase 依赖 |
| 3 | [Ada-KV](https://arxiv.org/abs/2407.11550) | NeurIPS'25 | **最接近的工作**。发现 dispersed attention head 需要更大 budget，从 concentrated head 转移 budget。但只调 budget 不切换 strategy，且是 head-wise 不是 phase-wise |
| 4 | [Entropy Meets Importance](https://arxiv.org/abs/2510.13832) | 2025 | 高 entropy（分散 attention）head 对 pruning 更鲁棒，低 entropy head 被 prune 导致 sharp-drop。**提供了理论解释**：分散 attention 时 importance score 区分度下降 |
| 5 | [Surprising Effectiveness of Randomness](https://openreview.net/forum?id=YncWrbIxnN) | ICLR'25 | Random pruning 在 lower pruning ratio 出人意料有效。**部分印证**但是 weight pruning，非 token phase |
| 6 | [Attention Score is not All You Need](https://arxiv.org/abs/2406.12335) | EMNLP'24 | Attention score 作为 importance indicator 不充分，token importance 跨 window 会 shift |
| 7 | [ThinKV](https://openreview.net/forum?id=M3CeHnZKNC) | ICLR'26 | 不同 thought phase（reasoning/execution/transition）用不同压缩策略。**最接近 phase-dependent strategy** 但是语义 phase，且调力度不切换 strategy type |
| 8 | [Sparse Frontier](https://arxiv.org/abs/2504.17768) | 2025 | 无 universal optimal sparse attention strategy，retrieval vs reasoning 需要不同 mechanism |

### 最接近的发现

**Ada-KV** 认识到 dispersed attention 需要不同处理，但止步于 budget reallocation。我们的发现更进一步：在 low-sparsity phase，不仅需要更大 budget，还需要**完全不同的 strategy**（importance→random），且反转幅度巨大（111x）。

### Novelty Claim 建议

这个 crossover 现象可以 claim 为 novel contribution。建议 framing：

> We identify a previously unreported **phase-dependent strategy crossover**: importance-based KV eviction outperforms random in high-sparsity phases (concentrated attention) but catastrophically underperforms in low-sparsity phases (distributed attention), with up to 111× worse information impact. While prior work recognized importance scoring fragility (DefensiveKV, ICLR'26) and random diversity value (NACL, ACL'24), no existing work demonstrated that strategy ranking reverses across attention concentration phases within a single sequence.

完整调研已存入 `memory.md`。

---
