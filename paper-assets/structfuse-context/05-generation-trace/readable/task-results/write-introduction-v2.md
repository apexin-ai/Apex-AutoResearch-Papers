# write introduction v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_introduction-v2_20260515T015804_result.json`
- **Structured JSON:** [`e2f5ec9428f6ba9367de.json`](../../sessions/e2/e2f5ec9428f6ba9367de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_drafts/introduction_v2.md`。

v1 → v2 主要变化：
- **结构重组**：从 3 段 + 贡献列表改为标准 5 段（Problem → Gap → Approach → Findings → Contributions），每段 4-6 句
- **Claim 2 严格降级**：标注 `\textbf{exploratory observation}` + "pending multi-seed confirmation"，符合 D035
- **引用扩充**：新增 SimCLR、ContraCode、CodeRetriever、GraphCodeBERT、FAISS、RepoBench 等引用，key 均从 literature_map.yaml 取
- **数字占位**：所有依赖 M2 最终结果的数字用 `[TBD]` 标记（R@1 增量、seed 数、repo 数、connected rate）
- **叙事更清晰**：Para 2 明确点出 "embedding-close 但 structurally connected 的文件不应做 negatives" 这个 gap；Para 3 加入实验控制说明（identical pipeline, multiple seeds, two encoders）

M2 完成后（~May 17）填入最终数字即可定稿。

---
