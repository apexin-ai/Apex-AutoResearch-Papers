# analysis error analysis plan018

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_plan018_20260518T134244_result.json`
- **Structured JSON:** [`faab58d1d89c31cf3606.json`](../../sessions/fa/faab58d1d89c31cf3606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Error analysis 完成。报告已保存到 `artifacts/error_analysis_report.md` 并注册。

核心发现：

**exception_only (99.83%, 2 errors)**：仅有的 2 个错误都是 HumanEval/95 的 FN，根因是 `GeneratorExit`（`all()` 短路时 generator 正常清理触发的异常，非真实 bug）。

**vota (99.41%, 7 errors)**：全部 FN，6 个来自 MBPP/113（`try/except ValueError` 正常捕获异常，但 trace 中仍显示 `[ERROR] ValueError`），1 个来自 MBPP/794。额外 noise 来自 assert/call/return 事件。

**full_trace (81.76%, 217 errors)**：**100% 的错误都发生在 trace 被截断的样本上**。2048 token 限制导致截断后只剩 module imports 和内存地址，所有 error/assert 标记被丢失。这不是任务难度问题，是信息过载问题。

**no_trace (75.13%, 296 errors)**：FN 主导（206 vs 90），模型在缺乏 trace 时采取保守策略偏向预测 fail。140 个错误可被任意 trace 条件修复。

**跨条件**：exception_only 和其他条件的错误集**零重叠**。61 个样本在 no_trace 下正确但在 full_trace 下错误，说明截断的 trace 比没有 trace 更糟。

---
