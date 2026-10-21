# analysis prediction overlap 1 5b vs 7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction_overlap_1_5b_vs_7b_20260516T142527_result.json`
- **Structured JSON:** [`5a5c1e5e496bbee58cf7.json`](../../sessions/5a/5a5c1e5e496bbee58cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**IDs 901 和 905（HumanEval/95）是 universal irreducible errors**，所有模型（Qwen-7B/1.5B、DeepSeek-7B）在所有稳定 seed 上均错误预测为 "fail"。

根因：Python `all()` 短路时触发 `GeneratorExit`，tracer 标记为 `[ERROR]`，但这不是真实错误——是 Python generator protocol 的正常行为。模型无法区分这种 benign internal exception 和真实的运行时错误。

额外发现：
- DeepSeek 还在 MBPP/113（try/except ValueError）上稳定出错（6 samples），但 Qwen 不受影响
- 整个测试集仅 8/1190 samples 有"误导性 trace"（`[ERROR]` + label=pass），所有模型错误都集中在这 8 个样本上
- 潜在修复：从 trace 中过滤 `GeneratorExit`/`StopIteration` 等 Python 内部协议异常

---
