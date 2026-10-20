# research 009b literature linkage

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_009b-literature-linkage_20260514T190050_result.json`
- **Structured JSON:** [`f4557dd9b82f8a8feb65.json`](../../sessions/f4/f4557dd9b82f8a8feb65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。搜索了6组关键词、检索了~20篇论文的详细信息，产出要点：

**核心发现**：
- **没有论文报告过完全一样的现象**（world-model imagination 中 learned temporal embedding 导致的 seed-dependent delusional critic collapse），novelty claim 成立
- **最接近的工作**是 Hussing et al. (2024, RLC)：在高 UTD ratio 下观察到 seed-dependent value divergence，部分 seed 自发恢复，归因于 optimizer momentum
- Lu et al. (2018, NeurIPS Oral) 的 delusional bias 理论可直接解释我们的 collapse 机制：dt_embedding 请求长 imagination step → RSSM 无法准确预测 → critic 从不可实现的轨迹 back up value
- Gumbsch et al. (2024, ICLR Spotlight) 的 THICK Dreamer 是最近的架构类比，但用 discrete context boundary 回避了 delusional critic

产出文件：`artifacts/009b_literature_search.md`，包含完整论文列表和可直接追加到 `literature_map.yaml` 的 YAML block（16 条新条目）。

---
