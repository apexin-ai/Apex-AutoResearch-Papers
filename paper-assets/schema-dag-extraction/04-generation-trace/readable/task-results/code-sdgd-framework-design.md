# code sdgd framework design

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sdgd-framework-design_20260515T025924_result.json`
- **Structured JSON:** [`e02d4de52e4de4593944.json`](../../sessions/e0/e02d4de52e4de4593944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入并注册。核心内容：

**算法 5 步**：pairwise cosine similarity → τ-thresholded confusability graph → greedy graph coloring → per-batch vLLM extraction → union merge

**关键决策**：
- SDGD-zero（embedding similarity）和 SDGD-cal（empirical confusion matrix）两个变体
- τ 首选 Contribution A 的 empirical θ*，fallback adaptive mean+std ≈ 0.85
- Greedy coloring（largest_first），66 nodes 微秒级，接近最优
- NER 阶段 simple union merge（batch 间 type 不重叠，graph coloring 保证）

**5 个模块**：`similarity.py` / `graph.py` / `decompose.py` / `merge.py` / `evaluate.py`，通过 `SDGDDecomposer` 类封装，对接现有 `build_prompt` + `build_json_schema` + `text_match_eval`。vLLM engine 只初始化一次，batch 间复用。

等 exp003a 确认数据干净后开始实际编码。

---
