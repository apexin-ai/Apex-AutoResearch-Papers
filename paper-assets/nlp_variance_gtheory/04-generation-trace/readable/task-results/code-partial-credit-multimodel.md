# code partial credit multimodel

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_partial_credit_multimodel_20260523T090334_result.json`
- **Structured JSON:** [`e399d4d04b23cb454859.json`](../../sessions/e3/e399d4d04b23cb454859.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## 数据检查
8 模型 GSM8K 数据全部可用（每模型 57,600 条，共 460,800 条），`generated_text` 包含完整 CoT 推理步骤。

## Partial-Credit 评分
- 评分方法：从 CoT 文本提取算术表达式（`<&lt;a+b=c>>` 和 `a + b = c` 格式），逐步验证计算正确性
- 正确答案 → 1.0；错误答案 → 正确算术步骤占比；无可提取步骤 → 0.0
- 错误答案中：48.1% 所有算术步骤都正确（问题设置错），39.1% 部分正确，12.7% 全错

## Henderson I G-study：Binary vs Partial-Credit

| 指标 | Binary | Partial-Credit | Δ |
|------|--------|----------------|---|
| Grand Mean | 0.582 | 0.899 | +0.317 |
| G_item | **0.863** | **0.768** | **-0.095** |
| σ²_item % | 16.9% | 10.3% | -6.6% |
| σ²_residual % | 39.9% | 64.9% | +25.0% |
| σ²_model % | 10.7% | 4.0% | -6.8% |

## Per-Model G_item（5-facet）

| Model | Acc | G_binary | G_partial | ΔG |
|-------|-----|----------|-----------|-----|
| OLMo-2-7B | .701 | .919 | .894 | -.025 |
| Gemma-2-9B | .805 | .903 | .750 | -.152 |
| Llama-3.1-8B | .490 | .759 | .450 | **-.309** |
| Qwen3-8B | .622 | .760 | .707 | -.054 |

Partial credit 一致降低 G_item，因为大量"算术正确但设置错误"的响应获得高分，增大了 response-level 残差方差。

## 产出
- 服务器：`/root/nlp_variance_gtheory/results/partial_credit_multimodel/` （scored jsonl + gstudy json）
- 本地：已注册 artifact `art_20260523_f3d17f`
- 脚本：`/root/nlp_variance_gtheory/partial_credit_multimodel.py`

---
