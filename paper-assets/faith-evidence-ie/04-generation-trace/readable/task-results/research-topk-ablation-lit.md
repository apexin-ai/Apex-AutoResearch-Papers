# research topk ablation lit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_topk_ablation_lit_20260516T002831_result.json`
- **Structured JSON:** [`42f96acf501f8df661b9.json`](../../sessions/42/42f96acf501f8df661b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已写入 `artifacts/topk_ablation_lit_review.md`。

核心发现：

1. **literature_map.yaml 已有充分覆盖**——Category 13（BoN/Reranking）的 4 篇论文 + Category 14（RSFT Methodology）的 AdaSTaR/RIFT 直接解释了 top_k=3 的 negative result。

2. **文献共识**：RAFT 框架始终只取 top-1（不是 top-k），我们的 ablation 从反面验证了这个设计。BoN 文献（Huang et al. ICML 2025）证明 proxy reward 不完美时，扩大选择集导致 reward hacking——CED score 与 RE correctness 的 misalignment 在 top_k=3 时被放大。

3. **不需要新增论文到 literature_map.yaml**，已有收录足够支撑。写论文时可引用 Huang et al. (2025) 和 RAFT 的 top-1 设计作为文献锚点。

---
