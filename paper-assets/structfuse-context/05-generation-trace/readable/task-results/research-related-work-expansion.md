# research related work expansion

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-expansion_20260514T211428_result.json`
- **Structured JSON:** [`f004d48fccfda3512c8b.json`](../../sessions/f0/f004d48fccfda3512c8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出**:
- `literature_map.yaml` — 从 ~22 entries (6 需验证) 扩展到 **37 verified entries**，7 个 categories
- `artifacts/literature/related_work_expansion_report.md` — 完整报告

**关键发现**:

1. **CoCoHaNeRe 找到了**: "Effective Hard Negative Mining for Contrastive Learning-Based Code Search", ACM TOSEM 2025。**但有重要 nuance**: 它的论点是非可微 embedding negatives "slow and ineffective"，并非直接说 embedding negatives 有害。Claim 1 的 "correcting misconception" framing 需要调整——更准确的表述是 "challenging the premise that complex gradient-based mechanisms are necessary"。

2. **新增 15 篇**: SweRank, SWE-Fixer, CoCoHaNeRe, CL-DRD, ContraCode, CodeRetriever, ARISE, DeepSeek-Coder, RepoFusion, LocAgent, CodexGraph, RANGER, FAISS, Tree-sitter, + 1 篇从旧 category 移入新 category

3. **修正 2 处错误**: SWE-smith venue (→NeurIPS 2025 Spotlight), contrastive learning paper 标题和 venue 都是错的

4. **GRACE 没找到**对应的 code-specific 论文，已 drop

5. **Recency**: 70% citations from 2022+, 27% from 2025

---
