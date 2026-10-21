# research wang 7b models

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wang_7b_models_20260519T125547_result.json`
- **Structured JSON:** [`4993b2d8b0e85dcec845.json`](../../sessions/49/4993b2d8b0e85dcec845.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：Wang et al. 没有 7B 模型。**

- 他们仅训练了 340M（36个）和 1.3B（36个）两个规模，共 72 个模型
- 论文 Limitations 明确写道分析仅限 1.3B 以下，10B+ 规模是 open question
- HuggingFace collection 已全量检查，无任何 7B 模型
- 服务器 `/root/autodl-tmp/models_7b/` 下仅有 Qwen2.5-7B-Instruct 基座模型

报告已写入并注册为 artifact (`art_20260519_6bdbaf`)。

---
