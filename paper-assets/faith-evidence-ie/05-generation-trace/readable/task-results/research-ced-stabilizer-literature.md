# research ced stabilizer literature

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ced-stabilizer-literature_20260514T183814_result.json`
- **Structured JSON:** [`b2d92a77072d920b73c7.json`](../../sessions/b2/b2d92a77072d920b73c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**`literature_map.yaml`** — 17 篇论文，按 5 个 category 组织，每篇含 key_finding 和 relevance_to_ced_stabilizer。

**`artifacts/ced_stabilizer_literature_survey.md`** — 调研摘要，核心结论：

**最相关的已有工作**：
- **GDPO** (ICML 2026)：理论上解释了多 reward 归一化导致 advantage collapse——与我们的 CED vs. extraction-only 对比完美吻合
- **Dr. GRPO** (COLM 2025)：分析了 reward_std→0 时的 difficulty bias，直接解释我们观察到的 frac_zero_std 现象
- **DRA-GRPO**：从优化层面注入 diversity 信号，CED 从 reward design 层面天然具备
- **DAPO** (NeurIPS 2025)：Clip-Higher 解决 entropy collapse，但属于 algorithm trick 而非 reward design

**我们的新颖性**：
1. 首次证明 reward 结构（非 algorithm trick）决定 GRPO 训练稳定性
2. Contrastive evidence discrimination 作为 RL stabilizer 在 IE 领域全新
3. 三种 reward type 的 controlled ablation 提供了罕见的干净因果证据

**建议的三个 positioning 角度**：
1. Multi-dimensional reward as implicit diversity regularizer（引 GDPO 理论）
2. Reward variance maintenance for gradient health（引 Dr. GRPO + arXiv 2601.23135 理论）
3. Task-specific contrastive signal as a "free stabilizer"（最有叙事张力——CED 本为 faithfulness 设计，意外稳定了训练）

---
