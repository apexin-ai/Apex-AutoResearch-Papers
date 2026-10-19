# code plan006 humaid run

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-humaid-run_20260520T230721_result.json`
- **Structured JSON:** [`5c60f391ab8a72e0de5d.json`](../../sessions/5c/5c60f391ab8a72e0de5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已获取。下面是汇总分析。

---

## plan_006 humaid 实证结果汇总

### 1. 运行状态
- **成功**，2.9 分钟完成
- 9 个矩阵加载（3 模型 × 3 prompt），其中 **qwen3/few-shot-5 全零**（coverage=0, n_valid=0，标注完全失败），实际有效 **8/9 组合**

### 2. 混淆矩阵摘要

| 模型 | prompt | mean_diag | min_diag | worst confusion |
|------|--------|-----------|----------|-----------------|
| llama4 | zero-shot | 0.671 | 0.426 | C[6,0]=0.370 |
| llama4 | few-shot-3 | 0.676 | 0.407 | C[6,0]=0.407 |
| llama4 | few-shot-5 | 0.688 | 0.415 | C[6,0]=0.396 |
| qwen3 | zero-shot | 0.715 | 0.340 | C[6,5]=0.252 |
| qwen3 | few-shot-3 | 0.706 | 0.393 | C[6,5]=0.298 |
| qwen3 | few-shot-5 | **0.000** | 0.000 | **全零（失败）** |
| deepseek | zero-shot | 0.724 | 0.294 | C[8,7]=0.228 |
| deepseek | few-shot-3 | 0.725 | 0.385 | C[6,0]=0.250 |
| deepseek | few-shot-5 | 0.724 | 0.374 | C[8,7]=0.268 |

- deepseek 最好（diag 0.724），llama4 最差（diag 0.671）
- 最常见混淆：class 6 ("other_relevant_information") 是所有模型的主要混淆目标

### 3. F1 vs |downstream bias|

- **Macro F1 范围：0.614–0.690**，全部低于 0.93
- **Baumann check: 0%**（没有 F1>0.93 的情况，因为 humaid K=10 是高难度任务）
- 最大 bias 按 topology：
  - **IV: 12.4%–42.1%**（最脆弱）
  - **exposure: 9.0%–17.4%**
  - **mediation/frontdoor: 10.7%–14.8%**
  - **confounding: 4.9%–6.2%**
  - **mbias: 5.1%–6.5%**
  - **collider: 4.1%–5.6%**（最稳健）
- **0 sign flips**

### 4. ASV 值

| ASV type | non-None | range |
|----------|----------|-------|
| magnitude | 32/63 | 0.307–1.114 |
| significance | 2/63 | 1.681–1.704 |
| sign_flip | 0/63 | — |

- magnitude ASV 只有 4 个 topology 触发：mediation (0.62–0.90), exposure (0.65–1.11), IV (0.31–0.83), frontdoor (0.62–0.91)
- confounding/collider/mbias 的 bias 始终不超过 10% threshold → 无 magnitude ASV

### 5. Type I/II error

| topology | T1 range (before) | T1 after ASV filter | Power (before) |
|----------|-------------------|---------------------|----------------|
| confounding | **1.000** | 1.000 (safe) | 1.000 |
| mbias | 0.611–0.746 | same (safe) | 1.000 |
| mediation | 0.429–0.716 | 0 (unsafe) | 1.000 |
| collider | 0.111–0.217 | same (safe) | 1.000 |
| exposure | 0.040–0.061 | 0 (unsafe) | 1.000 |
| frontdoor | 0.041–0.059 | 0 (unsafe) | 1.000 |
| IV | 0.035–0.050 | 0 (unsafe) | 0.754–0.785 |

- **ASV-unsafe: 31/63 (49.2%)**
- confounding 的 Type I error = 100%（完全膨胀，符合预期）
- ASV 过滤过于保守：unsafe 的 topology 直接把 power 降到 0

### 6. Inter-model error correlation (humaid, 排除 qwen3/few-shot-5)

| prompt | pair | agreement | kappa | error_corr |
|--------|------|-----------|-------|------------|
| zero-shot | llama4-qwen3 | 0.485 | 0.417 | 0.121 |
| zero-shot | llama4-deepseek | 0.485 | 0.419 | 0.074 |
| zero-shot | qwen3-deepseek | 0.559 | 0.491 | 0.085 |
| few-shot-3 | llama4-qwen3 | 0.490 | 0.420 | 0.157 |
| few-shot-3 | llama4-deepseek | 0.465 | 0.392 | 0.056 |
| few-shot-3 | qwen3-deepseek | 0.507 | 0.433 | 0.051 |

- **Agreement 0.465–0.559**, **Kappa 0.392–0.491**（fair to moderate）
- **Error correlation 0.051–0.157**（低），模型犯错较独立

### 7. 异常/与预期不符

1. **qwen3/few-shot-5 全零** — 该组合标注完全失败，需排除
2. **confounding T1=100%** — 高但符合理论预期（K=10 放大了混杂效应）
3. **ASV 过滤过于保守** — unsafe 时 power 直接归零，实际应该有梯度式衰减
4. **0 sign flips** — K=10 时对角占优仍然足够保持符号正确
5. **IV bias 达 42%** — 这是 Wald estimator 对测量误差的已知脆弱性

### 8. 输出文件

| 文件 | 大小 |
|------|------|
| `artifacts/plan006/asv_empirical_results.json` | 119K |
| `artifacts/plan006/f1_vs_bias.png` | 171K |
| `artifacts/plan006/asv_heatmap.png` | 72K |
| `artifacts/plan006/plan006_humaid_run.log` | 2.9K |

---
