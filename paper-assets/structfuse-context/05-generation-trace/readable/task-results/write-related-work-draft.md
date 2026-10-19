# write related work draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_related-work-draft_20260514T220708_result.json`
- **Structured JSON:** [`8f94e595cdfe5229bcfb.json`](../../sessions/8f/8f94e595cdfe5229bcfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_drafts/related_work_v1.md` 并注册。

**结构总结：**

- **§2.1 Code Retrieval Methods** (3段)：BM25→dense (SweRank, SWE-Fixer) → graph-guided inference (LocAgent, RANGER, CodexGraph, RepoGraph, GraphCoder, ARISE)。结尾点出 gap：所有 graph 方法仅在 inference-time 用结构信号，encoder 训练完全不含结构信息。

- **§2.2 Contrastive Learning for Code** (3段)：ContraCode, CodeRetriever, Ding et al. 的对比学习方法 → code2vec, GraphCodeBERT 的结构表示（区分 GraphCodeBERT 的 function-level pre-training vs 我们的 repo-level fine-tuning） → 点出 negative sampling 策略缺乏系统研究的 gap。

- **§2.3 Hard Negative Mining** (3段)：SimCLR, DPR, ANCE, CL-DRD 的通用方法 → CoCoHaNeRe 的 gradient-based 方法（表述为"gradient-based 优于 non-differentiable embedding negatives"，未说 embedding negatives 有害） → bridge 到我们的 contribution：simple static embedding mining suffices + representation geometry 决定策略有效性。

**引用统计：** 19 个 `\cite{}`，全部来自 literature_map.yaml，无编造引用。

---
