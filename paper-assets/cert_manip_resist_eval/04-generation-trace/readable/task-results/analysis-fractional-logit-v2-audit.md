# analysis fractional logit v2 audit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fractional-logit-v2-audit_20260524T190248_result.json`
- **Structured JSON:** [`9e36f5fb802f81b13a59.json`](../../sessions/9e/9e36f5fb802f81b13a59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果输出如下。

## Fractional Logit V2 审计结果

| K | Paper Claims | Registry V1 | **Actual V2 (Fractional Logit)** |
|---|-------------|-------------|----------------------------------|
| K=3 | 9/12 | 4/12 | **9/12** |
| K=5 | 11/12 | 9/12 | **9/12** |
| K=7 | 12/12 | 10/12 | **9/12** |

### 关键发现

1. **K=3: 论文声明 9/12 → 审计确认 9/12**。完全匹配。Registry V1 的 4/12 是错误的。

2. **K=5: 论文声明 11/12 → 审计得到 9/12**。论文夸大了 2 个 conditions。未通过的 3 个是 position_bias (两个 benchmark 都不显著) 和 arc×sycophancy (p=0.265)。

3. **K=7: 论文声明 12/12 → 审计得到 9/12**。论文夸大了 3 个 conditions。同样的 pattern：position_bias 两个 benchmark + arc×sycophancy 未通过 FDR。

4. **Position bias 在所有 K 值下都不显著**，且 K_eff 系数接近 0 或为负。这是系统性弱点。

5. **Adaptive R²: 未找到任何 adaptive R² / random forest R² 数据**。论文声称 0.275，registry 记录 0.256，但服务器上完全没有这个分析的结果文件。

6. **SE inflation**: clustered SE 相对基础 SE 的膨胀率普遍很低（多数 <1x），说明 max-p clustering 策略在 fractional logit 下并未显著放大标准误。

结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/fractional_logit_v2.json`。

---
