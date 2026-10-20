# analysis g model calculation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_g_model_calculation_20260523T030205_result.json`
- **Structured JSON:** [`f420c794d81b8073a165.json`](../../sessions/f4/f420c794d81b8073a165.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果摘要：

| Benchmark | G_model | G_item | σ²_rel_M 主导来源 |
|-----------|---------|--------|-------------------|
| MMLU | 0.8626 | 0.8962 | model×prompt (59%) |
| ARC | **0.6708** | 0.8917 | model×prompt (88%) |
| HellaSwag | **0.9576** | 0.8716 | model×item (76%) |
| GSM8K | 0.8745 | 0.8629 | model×prompt (92%) |
| MATH | **0.9569** | 0.8880 | model×prompt (72%) |

核心发现：

1. **G_item 稳定（0.86–0.90），G_model 差异极大（0.67–0.96）**——item 难度测量一致可靠，但模型排序可靠性因 benchmark 而异。

2. **ARC 的 G_model 仅 0.67**——model×prompt 交互占相对误差的 88%，prompt 选择严重改变模型排名。GSM8K 类似（92%）但因 σ²(model) 更大而 G_model 仍有 0.87。

3. **HellaSwag/MATH G_model > 0.95**——这两个 benchmark 在区分模型方面非常可靠，误差主要来自 model×item（模型对不同题目的反应差异），而非 prompt 选择。

JSON 已保存并注册（`art_20260523_fd4e91`）。

---
