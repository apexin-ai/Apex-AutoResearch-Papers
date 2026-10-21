# analysis process kappa crossmodel table

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_process-kappa-crossmodel-table_20260520T115157_result.json`
- **Structured JSON:** [`fe47488e5ce19e987a98.json`](../../sessions/fe/fe47488e5ce19e987a98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Process-κ 跨模型汇总表（FOLIO-204, K=12, TF-IDF cosine）

| Model | N | Mean Cosine (±std) | Answer κ | Pearson r | p-value | Convergent Pairs % |
|-------|---|-------------------|----------|-----------|---------|-------------------|
| **Mistral-7B** | 204 | 0.690 (±0.099) | 0.460 | −0.064 | 0.362 | 9.5% |
| **LLaMA-3.1-8B** | 204 | 0.759 (±0.074) | 0.447 | −0.001 | 0.985 | 2.7% |
| **Qwen2.5-7B** | 204 | 0.790 (±0.073) | 0.658 | +0.226 | 0.001** | 2.5% |
| **Qwen2.5-14B** | 204 | 0.766 (±0.081) | 0.744 | +0.244 | <0.001*** | 3.2% |

关键发现：

1. **低 κ 模型（Mistral, LLaMA）**：过程相似度与答案一致性无显著相关（r≈0, p>0.3）。文本表面相似但答案不一致——"殊途殊归"。
2. **高 κ 模型（Qwen 系列）**：出现显著正相关（r≈0.23, p<0.001）。答案越一致的题，推理文本也越相似——过程与结论趋于对齐。
3. **Convergent pairs**（同答案但 cosine<0.5）：Mistral 高达 9.5%，其余模型 2.5–3.2%。Mistral 更频繁地"不同推理路径偶然得到相同答案"。

结果已保存至 `artifacts/process_kappa_cross_model.json`。

---
