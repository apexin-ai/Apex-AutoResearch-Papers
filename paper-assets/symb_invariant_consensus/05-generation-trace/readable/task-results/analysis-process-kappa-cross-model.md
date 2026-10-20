# analysis process kappa cross model

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_process-kappa-cross-model_20260520T223556_result.json`
- **Structured JSON:** [`066e518dd75e75be5d4a.json`](../../sessions/06/066e518dd75e75be5d4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。以下是完整分析：

## 结果（Common subset, N=166）

| Model | ProcessSim (mean±std) | Answer κ | Gap |
|-------|----------------------|----------|-----|
| Mistral-7B | 0.529±0.117 | 0.312 | **+0.218** |
| Qwen2.5-14B | 0.596±0.097 | 0.722 | **-0.126** |
| Qwen3-14B (nothink) | 0.608±0.095 | 0.763 | **-0.155** |
| Qwen3-14B (think) | 0.801±0.081 | 0.912 | **-0.111** |

## 关键发现

**"ProcessSim >> κ" 现象不跨模型泛化。** 只在 Mistral-7B 上成立（Gap=+0.22），三个更强的模型上 Gap 全部反转为负值：κ 显著高于 ProcessSim。

解读：
- **Mistral-7B**：推理过程高度相似但答案不一致——符合 confirmation bias 叙事（模型用相似模板推理但结论摇摆）
- **Qwen 系列**：答案一致性远超过程相似度——说明更强的模型能通过多样化推理路径收敛到一致答案，与 confirmation bias 假设相反

**注意**：论文中报告的 Mistral-7B 数值（ProcessSim=0.69, κ=0.41）与此处（0.53, 0.32）有差异，可能因温度设置或 TF-IDF 参数不同。但 Gap 方向一致（ProcessSim > κ）。

这个结果**不支持** "confirmation bias 是 same-model aggregation 通病"的 claim——它是弱模型特有现象。

---
