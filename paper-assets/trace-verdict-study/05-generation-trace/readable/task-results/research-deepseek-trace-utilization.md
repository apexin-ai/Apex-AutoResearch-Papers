# research deepseek trace utilization

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_deepseek-trace-utilization_20260515T131403_result.json`
- **Structured JSON:** [`e1be58b424aa29101fa8.json`](../../sessions/e1/e1be58b424aa29101fa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 memory.md。核心结论：

**CRUXEval 直接解释了 VOTA 差距。** Qwen2.5-Coder 技术报告 Table 11 显示：
- CRUXEval-I: Qwen 56.5% vs DeepSeek 39.0% (**+17.5pp**)
- CRUXEval-O: Qwen 56.0% vs DeepSeek 41.0% (**+15.0pp**)

这与 VOTA accuracy 差距（99.2% vs 84.45% = **14.75pp**）惊人吻合。

三个假说（均有文献支撑）：
1. **Execution reasoning readiness**：Qwen 预训练已建立更强的执行追踪能力，VOTA SFT 放大此优势（Hui et al. 2024 Table 11 + CRUXEval）
2. **Data scale × structured exposure**：5.5T vs 2T tokens + 3-stage 训练 + structural tokens → Qwen 对 VOTA 格式有更低 perplexity（Gao et al. 2025: "perplexity predicts SFT effectiveness"）
3. **Base model inductive bias ceiling**：train loss 相当但泛化差距 14.75pp → representation quality 问题而非 capacity 问题（Gao et al. 2025: "inductive bias outweighs SFT corpus"）

另外 Wang et al. (EMNLP 2025) 在 DeepSeek-Coder 上测了 5 种 trace 格式，最佳提升仅 +1.3pp（CodeExecutor on MBPP），且"不同模型对相同 trace 格式反应不一致"——与我们观察一致。

---
