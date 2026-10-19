# paper research verify citations v2 related work

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_research_verify_citations_v2_related_work_20260516T124847_result.json`
- **Structured JSON:** [`5199626294fca2623f04.json`](../../sessions/51/5199626294fca2623f04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果写入 `artifacts/paper_drafts/v2/citation_verification.md`。

核心发现：

| 引用 | 存在 | 语境匹配 | 需要操作 |
|------|------|----------|----------|
| dodge2020finetuning | YES | PARTIAL | 重新措辞：论文讲的是 seed 导致的性能方差和训练 divergence，不是 val loss 与 task metric 的 misalignment |
| thakur2021beir | YES | **NO** | BEIR 本身不讨论 checkpoint sensitivity。该claim 应引用 **MultiContrievers (Clavié et al., BlackboxNLP 2024)**，该文直接证明 BEIR ranking 对 checkpoint 高度敏感 |
| muennighoff2023mteb | YES | YES | 无需修改 |
| craswell2020overview | YES | PARTIAL | 建议改引 Craswell et al. SIGIR 2021 ("Reusable Test Collections in the Large Data Regime")，该文显式分析 pooling depth 对评估的影响 |

---
