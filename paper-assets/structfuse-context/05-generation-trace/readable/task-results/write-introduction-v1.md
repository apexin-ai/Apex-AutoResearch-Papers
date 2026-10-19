# write introduction v1

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_introduction-v1_20260515T083143_result.json`
- **Structured JSON:** [`bad78736bd52dd9f17b8.json`](../../sessions/ba/bad78736bd52dd9f17b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用（未在 MCP 工具列表中）。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md`

**与旧版的关键变更**：
- 移除 "challenges the prevailing assumption"、"we demonstrate" 等断言式表述（D049 合规）
- Claim 1 改为 "establishes a strong zero-cost baseline"，不再对标 CoCoHaNeRe
- Claim 2 用 exploratory observation + preliminary mechanistic analysis 措辞
- 同时报告 pilot（+1.6–2.0pp）和 M2 seed 43（+0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint）两组数据
- 5 段结构：重要性→NLP hard negative mining + CoCoHaNeRe gap→结构信号 insight→主要发现→contributions
- ~800 words，全部 `\cite{}` key 与 references.bib 对齐

---
