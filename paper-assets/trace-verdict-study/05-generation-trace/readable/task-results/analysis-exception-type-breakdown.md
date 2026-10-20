# analysis exception type breakdown

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exception_type_breakdown_20260517T004655_result.json`
- **Structured JSON:** [`effefc2a47d70355b040.json`](../../sessions/ef/effefc2a47d70355b040.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `/root/trace-verdict-study/docs/paper/exception_type_breakdown.md`。

核心发现：
- **Exception-only 模型在 1190 个样本中仅有 2 个错误**（99.83% accuracy），且 3 个 seed 结果完全一致
- **唯一失败模式**：HumanEval/95 的 2 个 `pass_with_GeneratorExit` 样本（benign exception 被误判为 fail）
- 所有真实 exception types（AssertionError 188, TypeError 53, NameError 21, AttributeError 5, StopIteration 2）和 no_trace_fail（70）均 100% 正确
- HumanEval vs MBPP 差异完全由 GeneratorExit 造成

---
