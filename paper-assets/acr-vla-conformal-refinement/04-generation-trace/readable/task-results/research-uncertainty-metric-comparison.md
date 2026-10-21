# research uncertainty metric comparison

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_uncertainty-metric-comparison_20260521T001327_result.json`
- **Structured JSON:** [`14f98a7abed959d75038.json`](../../sessions/14/14f98a7abed959d75038.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集齐全。以下是对比分析：

---

## Uncertainty 计算公式对比

**常量**: `CORRECTION_DIM=6`, `FULL_ACTION_DIM=7`, `H_EFF=5`

| 维度 | `select_action_adaptive_k` | `select_action_conformal_crm` |
|------|--------------------------|----------------------------|
| **K 值** | K=2 探测，触发后扩展到 K=10 | 固定 K=2 |
| **输入维度** | **7D** (`FULL_ACTION_DIM`, 含 gripper) | **6D** (`CORRECTION_DIM`, 仅 pose) |
| **展开方式** | per-step L2 norm, 再跨时间步求**均值** | 先 flatten 到 30D, 再算**单次 L2 norm** |
| **数学公式** | `u = (1/T) Σ_t ‖a1_t − a2_t‖₂`, `a_t ∈ ℝ⁷` | `u = ‖a1 − a2‖₂`, `a ∈ ℝ³⁰` (即 `√(Σ_t ‖a1_t − a2_t‖₂²)`, `a_t ∈ ℝ⁶`) |
| **归一化** | 除以 T（时间步均值） | 无归一化 |
| **输出** | 标量 (mean L2) | 标量 (L2 norm) |
| **阈值默认值** | `0.1` | `0.074855` (标注为 P50) |
| **阈值来源** | 手动设定 | 从校准集 L2 分布的 P50 分位数得到 |
| **触发后动作** | 扩展到 K=10, argmin(squared L2 to mean) 选 6D pose, CRM obs_only 修正 | K=2 不变, 选距 centroid 更近的 sample, CRM obs_only 修正 |

## 本质区别

两个 metric 是**不同的聚合方式**:

- **Adaptive K**: 均值聚合 — `mean_t(‖Δa_t‖)`, 是 per-step norm 的**算术平均**
- **Conformal CRM**: 范数聚合 — `‖Δa‖ = √(Σ_t ‖Δa_t‖²)`, 是 concatenated vector 的 **L2 范数**（等价于 per-step norm 的 **RMS × √T**）

由 QM-AM 不等式:

```
u_conformal = √T × RMS(‖Δa_t‖) ≥ √T × mean(‖Δa_t‖) = √T × u_adaptive
```

即 **u_conformal ≥ √5 × u_adaptive ≈ 2.24 × u_adaptive**（等分布情况下取等号）。

额外差异: adaptive_k 在 **7D** 上计算(含 gripper), conformal_crm 在 **6D** 上计算(仅 pose)。gripper diff 通常很小，影响有限。

## P50=0.074855 在 Adaptive K 空间的等价分位

假设 uncertainty 在时间步上均匀分布（取等号的情况）：

```
u_adaptive_equiv = u_conformal / √T = 0.074855 / √5 ≈ 0.0335
```

实际中因各时间步不等（Jensen gap），真实等价值在 **0.0335 ~ 0.074855/5 = 0.015** 之间。

Adaptive K 的默认阈值 0.1 对应 conformal 空间约 `0.1 × √5 ≈ 0.224`，远高于 P50=0.074855——这意味着 adaptive_k 用 0.1 阈值时，触发率远低于 conformal_crm 用 P50 阈值。

## 统一建议

**应选 conformal_crm 的公式**（flatten 后 L2 norm, 仅 6D pose），理由：

1. **物理一致性** — 只在 pose 维度计算，排除 gripper 的干扰（gripper 是离散值 ±1，其 L2 diff 语义不同于连续 pose）
2. **对大偏差更敏感** — L2 norm 对单步大偏差的响应比均值更强（一个时间步出大错就应触发修正）
3. **有校准分位数** — P50=0.074855 已从校准集得到，可直接用 conformal 理论设阈值；adaptive_k 的 0.1 是无校准的手动猜测
4. **简洁** — 无需额外归一化，与 conformal prediction 的 nonconformity score 自然对齐

---
