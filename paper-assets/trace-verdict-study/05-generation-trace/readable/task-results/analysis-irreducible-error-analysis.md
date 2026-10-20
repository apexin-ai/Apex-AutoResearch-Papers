# analysis irreducible error analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irreducible_error_analysis_20260515T194428_result.json`
- **Structured JSON:** [`94af1c75c717fa9367f4.json`](../../sessions/94/94af1c75c717fa9367f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**3 个 seed 错的是完全相同的 2 个样本**（id=901, id=905），均来自 HumanEval/95。

**根因**：Python `all()` 对 generator expression 短路时触发 `GeneratorExit`（`BaseException` 子类，非真正错误），但 tracer 将其标记为 `[ERROR]`。exception_only 条件下模型只看到 7 行 `[ERROR] GeneratorExit`，合理但错误地预测为 fail。

这是 exception_only 表征的**真正不可约误差**——整个测试集 1190 条中仅这 2 条含 `GeneratorExit`，模型无训练信号学习其良性本质。报告已写入 `artifacts/irreducible_error_analysis.md`。

报告末尾有一个待验证项：DeepSeek exception_only seed42 也是 99.83%，建议后续确认它是否也错在同样的 id=901/905 上。

---
