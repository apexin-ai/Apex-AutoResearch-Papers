# analysis prediction overlap cross family

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction-overlap-cross-family_20260516T200241_result.json`
- **Structured JSON:** [`1d5dd456f0466330f921.json`](../../sessions/1d/1d5dd456f0466330f921.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**D049 部分成立。** 3/4 模型（Qwen-7B、Qwen-1.5B���CodeLlama-13B）错误集完全相同（Jaccard=1.0），都只错样本 901 和 905。DeepSeek 额外错 6 个 MBPP/113 样本。

**错误根因：**
- **通用错误（901, 905）**：`all()` 短路触发 `GeneratorExit`，trace 中出现 7 行 `[ERROR]` 标记，但代码实际 pass。所有模型被误导。
- **DeepSeek 独有错误（540–543, 548–549）**：try/except 捕获的 `ValueError` 在 trace 中显示为 `[ERROR]`，DeepSeek 未能学会区分 caught vs uncaught exception，其余 3 个模型可以。

**论文建议**：将 claim 改为 "3/4 model families hit identical ceiling with Jaccard=1.0 error overlap; root cause is benign exception markers in trace format"，比泛泛的 "universal ceiling" 更有说服力。

---
