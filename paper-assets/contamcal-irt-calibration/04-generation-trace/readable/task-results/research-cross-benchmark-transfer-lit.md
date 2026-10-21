# research cross benchmark transfer lit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cross-benchmark-transfer-lit_20260519T223355_result.json`
- **Structured JSON:** [`ca53f72e49676d39b611.json`](../../sessions/ca/ca53f72e49676d39b611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成，已注册为 artifact `lit_cross_benchmark_transfer`。

核心发现：

**现有文献尚未充分记录 MMLU→GSM8K 这种跨 benchmark、跨格式、跨能力域的 contamination transfer。** Spiesberger et al. (2026, ICML sub) 仅证实 within-benchmark shallow generalization；Yao et al. (2026) 发现 SFT contamination effect 仅限被污染任务本身。我们的 +11.07pp 超越了这两个结论。

建议 framing 方向：**"SFT as capability elicitor"**——MMLU contamination SFT 教的不是 MMLU 答案（content effect），而是通过多学科 QA 训练让模型学会结构化推理模式，释放了预训练中已有但未被 elicit 的数学能力。支撑：(1) MC→generation 格式完全不同，排除 format memorization；(2) Ren et al. (2026) 证明强基座模型能从 SFT 提取可迁移程序化模式；(3) LIMA 的 Superficial Alignment Hypothesis 表明 SFT 核心作用是 capability elicitation。

---
