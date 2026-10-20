# analysis bf16 fp16 sensitivity

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_fp16_sensitivity_20260521T074400_result.json`
- **Structured JSON:** [`2fd8f60b995bf981e9d9.json`](../../sessions/2f/2fd8f60b995bf981e9d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果非常清晰，完全符合预期：

## 结果

### Precision 相关方差分量对比

| Component | 3-Precision (%) | BF16+FP16 (%) | Delta |
|---|---|---|---|
| **precision** | 0.4033 | **0.0006** | -0.4027 |
| **precision×item** | 1.3036 | **0.0412** | -1.2623 |
| **model×precision** | 0.1995 | **0.0009** | -0.1986 |

### 关键发现

1. **precision 主效应**：排除 FP32 后从 0.40% 降至 **0.0006%**（几乎为零）。BF16 和 FP16 的平均准确率差异仅 0.23pp（69.32% vs 69.09%），三个模型上方向不一致（Llama/Mistral FP16 略高，Qwen BF16 略高）。

2. **precision×item 交互**：从 1.30% 降至 **0.04%**（降幅 97%）。FP32 几乎是 precision×item 交互的唯一来源。

3. **其他分量稳定**：item_id（46.4→52.9%）、model×item（18.2→22.5%）占比上升是因为 precision 相关分量释放的空间被重新分配，绝对结构未变。

4. **数据覆盖**：525,400 条记录，3 个模型（Llama-3.1-8B、Mistral-7B、Qwen3-8B），BF16 273K + FP16 252K。

### 回应 Reviewer

FP32 与 BF16/FP16 有 ~6pp accuracy gap（62.9% vs 69.1%），是 precision facet 方差的主要来源。排除 FP32 后，precision 及其交互项均降至 ≈0%，证实 BF16≈FP16 在评估方差上无实质差异。Reviewer 关于 FP32 confound 的担忧是合理的——precision facet 的方差确实由 FP32 驱动，而非数值精度的渐进差异。

结果已保存至 `results/analysis/bf16_fp16_only_gstudy.json`。

---
