# analysis cross family error overlap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_family_error_overlap_20260516T182909_result.json`
- **Structured JSON:** [`094ac9e4badc8f338118.json`](../../sessions/09/094ac9e4badc8f338118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。以下是核心结论：

---

## 结果

**确认 universal irreducible ceiling：所有 4 个模型在 exception_only 条件下共享完全相同的 2 个错误样本（index 901, 905）。**

| 模型 | 错误数 | 错误索引 |
|------|--------|----------|
| Qwen-7B (3 seeds) | 2 | [901, 905] |
| Qwen-1.5B | 2 | [901, 905] |
| CodeLlama-13B | 2 | [901, 905] |
| DeepSeek-6.7B | 8 | [540-543, 548-549, 901, 905] |

**两个 universal error 样本均来自 HumanEval/95 (check_dict_case)**，标签为 pass，但 trace 中有 7 条 `[ERROR] GeneratorExit` —— 这是 `all()` 短路 generator 时的正常 Python 行为，不是真正的错误。在 exception_only 视图下，模型只看到密集的 [ERROR] 行，无法区分这是无害的 runtime artifact。

DeepSeek 额外错的 6 个样本来自 MBPP/113 (check_integer)，trace 显示被 try/except 捕获的 ValueError —— 同样是"看起来像错误但实际通过"的情况，但其他 3 个模型能正确判断。

**根因**：exception_only 表示的语义歧义（GeneratorExit + caught exceptions 显示为 [ERROR]）造成了表示层面的硬上限，与模型容量无关。

报告路径：`artifacts/cross_model_exception_only_overlap.md`

---
