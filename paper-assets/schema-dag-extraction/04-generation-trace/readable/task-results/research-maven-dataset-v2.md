# research maven dataset v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_maven-dataset-v2_20260515T031646_result.json`
- **Structured JSON:** [`b956f3aa389b1940c660.json`](../../sessions/b9/b956f3aa389b1940c660.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已存在且内容完整，已注册为 artifact (`art_20260515_d9b24e`)。

核心结论：

| 维度 | Few-NERD | MAVEN |
|------|----------|-------|
| Task | NER (66 types) | Event Detection (168 types) |
| Domain | Wikipedia | Wikipedia |
| Size | ~188K sentences | 4,480 docs / 118,732 mentions |
| Public | Yes (HF) | Yes (GitHub, MIT, 免费) |
| Test labels | 公开 | 不公开 (用 dev set: 710 docs / 18,904 mentions) |

**BCS/SDGD 适用性**：168 types 基于 FrameNet 层级组织，sibling types 语义高度相近（原论文 Table 7 已量化 sibling 混淆率 14.6-19.8%）。SDGD graph coloring 空间远大于 Few-NERD，效果应更显著。NER + ED 跨任务验证可证明 confusability-aware schema decomposition 是 task-agnostic 策略。

---
