# analysis error analysis plan018

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_plan018_20260520T102400_result.json`
- **Structured JSON:** [`ba8d4644e588f98e7f44.json`](../../sessions/ba/ba8d4644e588f98e7f44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/error_analysis_report.md` 并注册为 artifact (`art_20260520_0e880c`)。

核心发现总结：

1. **Tier 1 错误全是 FP（pass→fail 误报）**，根因是两类 trace 伪影：
   - **GeneratorExit**：Python `all()` 短路触发的内部异常被 tracer 标记为 `[ERROR]`，HumanEval/95 因此在所有 4 个模型×3 个 seed 上一致出错
   - **Caught exception**：`try/except` 中被捕获的异常也标记为 `[ERROR]`，DeepSeek 最敏感（MBPP/113 全部 10 个通过解被误判）

2. **Tier 2 (loop_only) 与 Tier 1 错误几乎不重叠**（Qwen-7B 交集=0），loop trace 对 75% 的错误样本缺乏诊断信息（no_error 类型）

3. **FP/FN 比例随 trace 质量变化**：T1 ~100% FP → T2 ~60/40 → BL ~55/45

4. **Tier 1 错误跨 seed 完全确定**（3 个 seed 完全一致），是格式盲区而非模型泛化失败

---
