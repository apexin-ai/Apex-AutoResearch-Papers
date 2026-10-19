# writing discussion draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_discussion_draft_20260514T101811_result.json`
- **Structured JSON:** [`e9186067b404be6bb841.json`](../../sessions/e9/e9186067b404be6bb841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion 草稿已写入 `/root/structfuse-context/artifacts/paper_drafts/discussion_draft.md`。

核心论点：

1. **Training-time vs Inference-time**：StructFuse 将结构计算一次性摊销到训练阶段（~110h, 0 timeout），推理零开销；CodexGraph/LocAgent/RANGER 每次查询需图遍历+LLM调用。两种范式互补——StructFuse encoder 可作 first-stage retriever 缩小搜索空间。直接数值对比因任务接口和评测基准不同而不恰当。

2. **Inter- vs Intra-procedural**：GraphCoder/ARISE 仅 intra-procedural data-flow，CodexGraph/LocAgent 无 data-flow。StructFuse 的 2-hop bounded inter-procedural 在覆盖率（Z=40.8%，XL repos 96%）和可扩展性（0% timeout）间取得平衡。

3. **Limitations**（4点）：2-hop 截断深调用链；CodeQL 语言限制；36% structural data rate（re-extraction 可改善）；n=3 seeds 统计功效不足，待 M2 full 补齐。所有定量 claim 已标注来源，强度词与 evidence 匹配（未用 "significantly"/"consistently"）。

---
