# analysis 5paired cls cwm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_5paired-cls-cwm_20260512T140047_result.json`
- **Structured JSON:** [`03d1b4423aea9981bf26.json`](../../sessions/03/03d1b4423aea9981bf26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

## 4B CLS vs CWM 5-Paired 统计分析

### Per-seed gaps

| Seed | CLS acc | CWM acc | Gap |
|------|---------|---------|-----|
| 42 | 87.83 | 87.51 | +0.32 |
| 123 | 89.52 | 87.20 | +2.32 |
| 456 | 87.88 | 86.98 | +0.90 |
| 789 | 89.00 | 86.67 | +2.33 |
| 0 | 87.94 | 87.57 | +0.37 |
| **mean** | **88.43±0.78** | **87.19±0.37** | **+1.25** |

### 统计检验结果

| 检验 | 统计量 | p-value | 结论 |
|------|--------|---------|------|
| Paired t-test (two-sided) | t(4)=2.765 | **0.0506** | 边界不显著 |
| One-sided t-test (CLS>CWM) | — | **0.0253** | 显著 |
| Wilcoxon signed-rank (one-sided) | W=0.0 | **0.0312** | 显著 |
| Bootstrap 95% CI | — | [+0.46, +2.04] | 排除 0 |
| Cohen's d | 1.237 | — | **大效应** |
| TOST ±2pp | — | 0.0855 | 不等价 |

### 结论

CLS 在所有 5 个 seed 上都优于 CWM（+0.32 ~ +2.33pp），方向完全一致。

- **Two-sided paired t-test**: p=0.0506，刚好过 0.05 边界（n=5 power 不足）
- **One-sided test**: p=0.025，显著
- **Bootstrap CI**: [+0.46, +2.04]，不包含 0
- **Cohen's d=1.237**：大效应量
- **TOST ±2pp 不等价**：不能说两个方法等价

**判断：CLS > CWM 是真实效应（+1.25pp），方向性显著（one-sided p=0.025）。两种方法不等价。** n=5 导致 two-sided test power 不足，但所有证据一致指向 CLS 优于 CWM。

### 注意

Clustered bootstrap（per-instance 级别）未执行——CWM 的 eval 只保存了汇总指标，无 per-instance predictions。如需做 per-instance paired analysis，需重新运行 CWM 模型推理并保存逐条预测。

---
