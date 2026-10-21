# analysis prediction overlap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction_overlap_20260516T191106_result.json`
- **Structured JSON:** [`2f7a48a40a1c4a2d86a8.json`](../../sessions/2f/2f7a48a40a1c4a2d86a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**核心结论**：5 个模型（Qwen-7B×3 seeds、Qwen-1.5B、CodeLlama-13B）在 exception_only 条件下犯完全相同的 2 个错误，100% 重叠，0 个独有错误。

两个错误均为 HumanEval/95 的 `GeneratorExit` 伪异常——`all()` 短路时 Python 正常的生成器回收机制在 exception_only trace 中表现为 `[ERROR]`，误导所有模型预测 "fail"（实际 label 为 "pass"）。

这强力支持 "universal irreducible ceiling" 结论：0.17% 的错误率是数据质量天花板，而非模型能力限制。跨架构、跨规模、跨种子完全一致。

---
