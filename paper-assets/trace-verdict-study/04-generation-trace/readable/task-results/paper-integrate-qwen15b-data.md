# paper integrate qwen15b data

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_integrate-qwen15b-data_20260516T111258_result.json`
- **Structured JSON:** [`27496571eca265046ffe.json`](../../sessions/27/27496571eca265046ffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。更新了三个文件：

1. **`artifacts/_project/paper/main_results_tables.tex`** — Table 2 重构为 Cross-Model Generalization 表，Qwen-1.5B 作为独立模型行（exception_only=99.83%, VOTA=99.58%, no_trace=67.31%），底部增加跨尺度比较摘要
2. **`artifacts/paper_tables/main_results_tables.tex`** — 同步更新
3. **`docs/paper/experiments.tex`** — 内联表改为四列（Qwen-7B / Qwen-1.5B / DeepSeek-6.7B / Range），正文重写为强调 scale invariance 发现

关键叙事强化点：
- Exception only 在 Qwen-7B 和 1.5B 上精确一致（99.83%），跨 4.7× 参数差异完全 scale-invariant
- 新增 "Range" 列一目了然：exception 0.50pp vs VOTA 15.13pp vs no_trace 7.82pp
- no_trace 在最小模型上退化最严重（67.31%），反衬 exception signal 绕过了模型容量瓶颈

---
