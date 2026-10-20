# research proofwriter survey

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_proofwriter_survey_20260514T143225_result.json`
- **Structured JSON:** [`26fa32c4c88a98aec504.json`](../../sessions/26/26fa32c4c88a98aec504.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `docs/proofwriter_survey.md`。核心结论：

**ProofWriter OWA D5 是最佳第二数据集**，直接用 HuggingFace `smoorsmith/proofwriter` 的 600 test 样本。

关键判断：
- **格式完全兼容**：同样是 premises → conclusion → T/F/U，pipeline 适配量约 1 天
- **与 FOLIO 互补性强**：合成模板 vs 专家标注，简单语言 vs 复杂自然语言
- **Logic-LLM 先例**：该论文正是用 FOLIO + ProofWriter OWA-D5 做评测，审稿人容易接受
- **不对称性预测**：ProofWriter 模板化语言会同时降低 FOL 和 Code 的翻译难度，disagree rate 预期下降，9:1 不对称性可能缩小——这恰好能说明不对称性与数据集语言复杂度相关而非方法固有偏差
- **额外分析轴**：推理深度 D0-D5 可分析"推理复杂度 vs 表征分歧"的关系
- **风险**：数据太简单导致 disagree 样本不足，可通过选择 D5 + RelNeg 配置缓解

---
