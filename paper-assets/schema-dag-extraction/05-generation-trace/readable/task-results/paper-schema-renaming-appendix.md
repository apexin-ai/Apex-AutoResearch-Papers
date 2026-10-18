# paper schema renaming appendix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_schema_renaming_appendix_20260518T213448_result.json`
- **Structured JSON:** [`adbf032a7edf2ffcfe00.json`](../../sessions/ad/adbf032a7edf2ffcfe00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both edits applied correctly.

**产出汇报：**

1. **Appendix `\ref{app:renaming}`** (L681-701): 实验设计描述 + 2×3 结果表 + 解释段落，约 0.4 页
2. **Limitations 第 4 点** (L46): 更新为引用 Appendix，含具体数据 (3--9 pp)

**实验细节发现：**
- **Rename 策略**：对 14 对高 SCS 关系对（mean SCS=0.87），将其中一个 label 替换为语义不同的 paraphrase，用 all-MiniLM-L6-v2 embedding 选择使 cosine similarity 最小的替代名（mean new SCS=0.67，$\Delta$=-0.20）
- **具体例子**：`participant of` → `event involvement`, `follows` → `prior entry`, `mother` → `female progenitor`, `part of` → `integral segment of`
- **Batches**：复用 BCS-controlled 实验的 50 个 batch（25 low + 25 high），FewRel count=8，每 batch 96 samples
- **低 BCS batch 含 0-2 个被 rename 的 type；高 BCS batch 含 2-4 个**（高 BCS batch 天然包含更多 confusable pairs，因此 rename 更多）
- **Solo sanity check**：12 个被 rename 的 label 中 11 个单独可识别（仅 `mother` → `maternal parent` 失败），排除了"模型完全不认识新 label"的解释

---
