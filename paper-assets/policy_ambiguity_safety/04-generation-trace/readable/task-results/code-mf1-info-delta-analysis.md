# code mf1 info delta analysis

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf1_info_delta_analysis_20260520T171152_result.json`
- **Structured JSON:** [`7bbb7012dfc5cd43fb12.json`](../../sessions/7b/7bbb7012dfc5cd43fb12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，输出在 `full_study/analysis/info_delta_analysis.json`。关键发现：

**Per-type info delta**：authorization_scope (36.1±8.6) 和 incompleteness (34.6±8.4) 最大，coreferential (7.8±4.7) 最小，符合预期。

**Logistic regression — info delta 是显著混淆变量**：
- Model 1 (layer only): layer coef=0.54, p=0.001
- Model 2 (layer+info_delta): layer coef=0.20, **p=0.31 (不再显著)**；info_delta coef=0.029, p=0.0003
- Layer 系数下降 63.5%（远超 20% 阈值），说明 info delta 是 layer effect 的主要混淆源

**Sensitivity (排除 incompleteness)**：
- Spec (auth_scope + cond_prec): 45.0% vs Ling: 34.3%, Δpp=10.67
- χ²=5.76, **p=0.016**, Cramér's V=0.107, OR=1.56 [1.08, 2.26]
- 排除 incompleteness 后 layer effect 仍显著，但效应量从 V=0.132 降至 0.107

结论：info delta 确实部分混淆了 layer effect（logistic regression 中 layer 系数不再显著），但 sensitivity test 表明即使排除 info delta 最大的 incompleteness 类型，specification layer 的违规率仍显著高于 linguistic layer。论文中需要报告两个结果并讨论这一限制。

---
