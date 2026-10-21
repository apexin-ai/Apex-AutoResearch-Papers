# analysis deepseek extra errors

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-extra-errors_20260516T120236_result.json`
- **Structured JSON:** [`15979b7a91aeccfa4f14.json`](../../sessions/15/15979b7a91aeccfa4f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/deepseek_exception_only_error_analysis.md`。

核心发现：

**DeepSeek 的 6 个额外错误全部来自同一个 problem（MBPP/113）的同一个 try/except 解法的 6 份重复。** 本质上是 1 个独特的错误模式：模型看到 `[ERROR] ValueError` 就判 fail，无法理解异常被 `except ValueError` 捕获后代码仍然正确。

关键数据：
- 测试集 1190 样本中，仅 8 个是"caught exception"（trace 有 `[ERROR]` 但 label=pass）
- DeepSeek 8/8 全错（100% fail rate），Qwen 仅 2/8 错（GeneratorExit 那 2 个）
- 训练集中此模式占比仅 0.3%（14/4720），极端不平衡导致 `[ERROR] → fail` 成为主导学习信号
- 跨 3 个 seed 完全一致：DeepSeek 在 MBPP/113 上 100% 失败，Qwen 100% 正确
- 训练超参完全相同，差异纯粹来自模型架构/预训练差异
- Tokenizer 差异（DeepSeek 多 ~24% tokens）不是原因——输入仅 128 tokens，远未截断

---
