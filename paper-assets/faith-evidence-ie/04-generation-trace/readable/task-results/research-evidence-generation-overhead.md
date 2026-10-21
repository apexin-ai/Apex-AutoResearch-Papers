# research evidence generation overhead

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_evidence-generation-overhead_20260515T201203_result.json`
- **Structured JSON:** [`96f9234b225cf205c23e.json`](../../sessions/96/96f9234b225cf205c23e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/literature_survey_evidence_overhead.md`。

核心发现：

**四个方向共 15 篇论文，关键结论：**

1. **MTL 开销**：负迁移（gradient conflict）在 joint IE 中普遍存在；Saini et al. (2023) 直接证明 joint model 在 document-level 反而不如 pipeline。
2. **Rationale 生成代价**：Mind Your Step (ICML 2025) 显示 CoT 最高导致 36.3% 性能下降；Token-Budget-Aware (ACL 2025) 证明推理 token 与答案 token 存在直接竞争。
3. **Decoupling**：generative IE survey 一致指出输出 token 限制是核心瓶颈，输出格式设计直接影响抽取质量。
4. **DocRE evidence 处理**：DREEAM/Eider/SIRE 全部回避了将 evidence 作为生成目标——它们用 attention 引导或轻量级独立模块，从未在同一序列中联合生成。

**关键缺口**：没有先前工作量化过在单一自回归输出中联合生成 evidence + relation 的代价。我们的 no-evidence ablation (+20.6% rel_f1) 是这方面的首个实证，为 decoupled 架构提供了强有力的动机。

---
