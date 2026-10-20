# paper add 3 citations round2 v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_add_3_citations_round2_v2_20260521T001358_result.json`
- **Structured JSON:** [`90911c18325c0f6269c0.json`](../../sessions/90/90911c18325c0f6269c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改汇总：

| 文件 | 位置 | 改动 |
|------|------|------|
| `references.bib` | L57 (原 orphan 注释处) | 添加 `diveye` 条目 (Basani & Chen, ICLR 2026) |
| `references.bib` | Model Collapse 区段 | 添加 `schaeffer_collapse_position` (Schaeffer et al., ICML 2025) 和 `drayson_detection_prevents_collapse` (Drayson et al., EMNLP 2025) |
| `related_work.tex` | L7 baselines 列表 | 在 zero-shot scoring 和 learned classifiers 之间插入 `surprisal diversity \cite{diveye}` |
| `related_work.tex` | L16 collapse 段落 | 在 training-loop 和 inference chains 之间插入一句引用 Schaeffer（八种 collapse 定义） |
| `discussion.tex` | L13 之后 | 新增一句：detection 可过滤合成数据防止 model collapse，引用 Drayson |

---
