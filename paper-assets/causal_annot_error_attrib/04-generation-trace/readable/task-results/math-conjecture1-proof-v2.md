# math conjecture1 proof v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_math_conjecture1_proof_v2_20260524T032119_result.json`
- **Structured JSON:** [`14cdd28af2667da9aec6.json`](../../sessions/14/14cdd28af2667da9aec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 交付物总结

### Phase 1: 数值验证 — PASSED

**`artifacts/conjecture1_formula_verify.py`** — 三路交叉验证:
- **方法 B↔C**（原始公式 vs Director公式）：最大相对误差 **3.78e-09** → 代数恒等式确认
- **Key identity** $e_j = \frac{1}{q_j}\sum_{k\neq j}(C_0)_{jk}p_k(g_j - g_k)$：误差 < 2.2e-15
- **矩阵形式** $V_B'(1) = g^T M g$：误差 < 3.3e-08
- **DD condition** 充分性：110/110 cases V'(1)≤0 → 100% sufficient
- **DS symmetric + uniform p**：10000/10000 all V'(1)≤0

### Phase 2: 证明结果

**`artifacts/conjecture1_diagonal_dominant_proof.tex`**（6 pages, compiled PDF）:

| 条件 | 结果 | 方法 |
|------|------|------|
| K=2, α_j≥1/2 | V'(1)≤0 精确 | 已有 |
| K=3 symmetric | V'(1)≤0 精确 | 已有 |
| **DS + α_j≥1/2 + uniform p** | **V'(1)≤0 精确** | **特征值分析（新Thm 1）** |
| **α_j ≥ q_j/(p_j+q_j)** | **V'(1)≤0 精确** | **逐分量CS（新Thm 2）** |
| **α_j ≥ c > 1/K** | **V'(1) ≤ (1-c)²R_g²** | **定量界（新Thm 3）** |
| α_j≥1/2, 任意 p | ε < 0.001 (数值) | 10⁵ configs |
| 一般 column-stochastic | ε < 0.017 (数值) | 545,945 curves |

### 关键发现

1. **未能证明完全一般情况**。α_j ≥ 1/2 对一般 column-stochastic + 非均匀 p **不足以保证** V'(1)≤0（0.69% 反例），但反例全部来自极端类别不平衡（p_max/p_min > 300），且最大 step deviation < 0.001。

2. **瓶颈在于 spillover 比率 q_j/p_j**。逐分量 Cauchy-Schwarz 证明需要 α_j ≥ q_j/(p_j+q_j)，这是关于 C₀ 和 p 的联合条件。当某类别 p_j 极小时条件失败。

3. **一般情况证明可能需要利用 column-stochastic 矩阵的全局结构**（如 Birkhoff 分解、M 矩阵谱性质），而非逐行分析。

---
