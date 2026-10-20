# analysis prediction overlap 1 5b vs 7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction_overlap_1_5b_vs_7b_20260516T134707_result.json`
- **Structured JSON:** [`312ca5b5286d7e99dad9.json`](../../sessions/31/312ca5b5286d7e99dad9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `/root/trace-verdict-study/artifacts/prediction_overlap_analysis.md`。

核心发现：

**Qwen-7B vs Qwen-1.5B: Jaccard = 1.0（完全相同）。** 两个模型在所有 seed 下都只错 ID 901 和 905，完全一致。

**根因是数据层面的 artifact，不是模型能力问题：**
- **ID 901, 905 (HumanEval/95):** 代码用 `all(... for k in keys)` 生成器表达式，`all()` 短路时触发 `GeneratorExit`，tracer 把它标记为 `[ERROR]`。这是正常 Python 行为，不是 bug。7 行 `[ERROR]` 让所有模型（3 个架构、6 个稳定 seed）都判为 fail。
- **ID 540-549 (MBPP/113, DeepSeek 独有):** `try/except ValueError` 捕获的异常被标记为 `[ERROR]`。Qwen 两个尺寸都能推理出 except 已处理，DeepSeek 不行。

**结论：irreducible error floor 假说成立。** 99.83% 是 exception_only 条件的理论天花板，2/1190 的错误源于 tracer 把良性异常（GeneratorExit）标为 `[ERROR]`。Scale 无关、seed 无关、架构无关。修复路径：tracer 过滤 GeneratorExit，或区分 `[CAUGHT]` vs `[UNCAUGHT]`。

---
