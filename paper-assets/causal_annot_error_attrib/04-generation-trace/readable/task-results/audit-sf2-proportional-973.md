# audit sf2 proportional 973

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_sf2_proportional_973_20260523T175725_result.json`
- **Structured JSON:** [`63ab87a92a9a6279462d.json`](../../sessions/63/63ab87a92a9a6279462d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture is clear. Here's the report:

---

## 汇报

### 精确来源

- **文件**: `artifacts/exp_proportional_real_matrices_results.json`
- **JSON path**: `non_proportional.sign_preservation_rate` = `0.9730434782608696` → 97.3%
- **生成脚本**: `artifacts/exp_proportional_real_matrices.py`

### 含义

97.3% 是 **sign preservation rate**（`sign(tau_direct) == sign(tau_total)`），**不是** proportional effects 条件满足率。

实验设置：
- **混凝土矩阵**: 23 个真实 LLM confusion matrices（empirical）
- **DGP 参数**: `f ~ N(0,1)` independent of `g` — **synthetic，非 empirical**
- **组**: `non_proportional`（故意违反 proportional effects 的最差情况组）
- n = 1150（23 matrices × 50 seeds）

### 措辞问题

method.tex L97 当前写法：

> "97.3% of empirical LLM configurations **satisfy the condition**"

这里 "the condition" 上文指的是 proportional effects ($f = \lambda g$)，但 97.3% 衡量的是 **sign preservation**，不是 proportional effects 是否成立。实际上这行数据来自故意违反 proportional effects 的 non-proportional 组。

appendix_proofs.tex L1267 的写法更准确：

> "Even under non-proportional effects ($f$ independent of $g$), **sign preservation** remains at 97.3%"

### 建议修正

method.tex L97 应改为类似：

> "topic classification is more tenuous, but even under non-proportional effects, sign preservation holds for 97.3% of empirical LLM configurations (Table~\ref{tab:proportional_empirical}), and Proposition~\ref{prop:conf_gen} provides a fallback bound"

这样准确反映：(1) 97.3% 是 sign preservation 而非条件满足率；(2) 这是 worst-case（non-proportional）下的结果。

---
