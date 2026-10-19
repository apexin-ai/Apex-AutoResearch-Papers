# research trace 283x claim

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_trace-283x-claim_20260520T183534_result.json`
- **Structured JSON:** [`a5fb5ff21858f6f7b2ec.json`](../../sessions/a5/a5fb5ff21858f6f7b2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found the exact source. Here's the full trace:

## 结论

### 2.83× 的精确计算

来源：`mvp_exposure_dag.py` 第 294-298 行

```python
severity = max(
    abs(plim[1] / beta[1]),  # |γ₁/β₁|
    abs(plim[2] / beta[2]),  # |γ₂/β₂|
)
```

DGP 设定 `beta = [0.0, 1.0, -0.5]`。对 worst-case C 矩阵（log 第 38-41 行）：

| 系数 | β (真值) | γ̂ (估计) | \|γ̂/β\| | 类型 |
|------|---------|----------|---------|------|
| β₁ | 1.0 | -0.838 | **0.838** | SIGN_REVERSAL |
| β₂ | -0.5 | -1.4138 | **2.83** | AMPLIFICATION |

**2.83× 来自 β₂ = -0.5 → γ̂₂ = -1.4138**，即 |-1.4138 / -0.5| = 2.8276 ≈ 2.83。这是第二个系数的 amplification，不是第一个系数的 sign reversal。

### 问题所在

D004 和 paper_framing.md 写的是：
> β=1.0 → estimate=-0.84 (sign reversal + **2.83x** amplification)

这把 β₁ 的 sign reversal（severity 0.84×）和 β₂ 的 amplification（severity 2.83×）混在一句话里，让读者以为 2.83× 描述的是 β₁=1.0 那个系数。Reviewer 指出 |-0.84/1.0| = 0.84 ≠ 2.83 完全正确。

### 修正建议

experiments.tex 当前写法（第 20 行）：
> The worst-case severity reaches 2.83× the true effect magnitude.

这句话**本身不算错**——severity 定义为 max_k |γ̂_k/β_k|，确实是 2.83×。但不能和 "β=1.0 → -0.84" 放在一起暗示因果关系。修正方案：

**方案 A**（拆开两个系数分别说）：
> The worst-case confusion matrix simultaneously produces sign reversal on β₁ (1.0 → −0.84) and 2.83× amplification on β₂ (−0.5 → −1.41).

**方案 B**（只保留可独立验证的数字）：
> The worst-case severity—defined as max_k |γ̂_k / β_k|—reaches 2.83×, driven by amplification of the smaller coefficient (β₂ = −0.5 → γ̂₂ = −1.41).

D004 和 paper_framing.md 也需要同步修正，避免 "β=1.0 → 2.83x" 这个误导性并列。

---
