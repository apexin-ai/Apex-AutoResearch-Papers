# code plan 009 bootstrap ty

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_009_bootstrap_ty_20260514T212820_result.json`
- **Structured JSON:** [`97aaa0b9c9d9b7208dd5.json`](../../sessions/97/97aaa0b9c9d9b7208dd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**N=1000 Monte Carlo 模拟完成。** 完整结果已保存至服务器 `results/bootstrap_ty_results.json`。

### Type I Error Rate (H0: 独立 AR(1))

| T | d_max=0 | d_max=1 | d_max=adaptive |
|---|---------|---------|----------------|
| 10 | **0.081** | 0.047 | 0.052 |
| 15 | **0.080** | 0.052 | 0.046 |
| 20 | 0.075 | 0.043 | 0.043 |
| 30 | **0.081** | 0.043 | 0.043 |

- d_max=0 时 Type I 偏高（~0.08），超过名义 0.05 但未超 0.10 红线
- d_max=1 和 adaptive 控制在 0.04-0.05，接近名义水平

### Statistical Power (H1: VAR(2), β=0.3)

| T | d_max=0 | d_max=1 | d_max=adaptive |
|---|---------|---------|----------------|
| 10 | 0.205 | 0.090 | **0.050** |
| 15 | 0.311 | 0.131 | 0.124 |
| 20 | 0.409 | 0.172 | 0.169 |
| 30 | **0.606** | 0.283 | 0.289 |

### 关键结论

1. **T=10 效力严重不足**：即使在最宽松的 d_max=0 下 power 仅 0.205；d_max=adaptive 时 power=0.05（等同于随机）。**审稿人的担忧完全成立。**

2. **T=20 仍然不够**：d_max=1 时 power=0.172，远低于 0.50 门槛。

3. **T=30 也不达标**：d_max=1 时 power=0.283，仍低于 0.50。唯有 d_max=0 时 power=0.606 达到 moderate 水平，但此时 Type I error 偏高（0.081）。

4. **d_max 敏感性显著**：所有 T 下 power range 都超过 0.15（T=30 时达 0.323），d_max 选择对结论影响巨大。

### 对论文的影响

- **T=10 下 TY Granger 检验不可靠**，既不能作为主要证据也不能作为 robustness check。必须在论文中透明报告这一局限。
- 即使扩展到 T=20，power 仍然极低。要达到 power≥0.50 可能需要 T≥40-50（或更强的因果效应）。
- **建议**：论文应 (a) 将 TY 作为辅助指标而非核心证据，(b) 补充 permutation-based 检验或 bootstrap 推断作为替代，(c) 在 limitation 中明确报告此 power analysis 结果。

---
