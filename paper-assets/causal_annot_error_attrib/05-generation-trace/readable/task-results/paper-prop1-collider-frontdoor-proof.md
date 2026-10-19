# paper prop1 collider frontdoor proof

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prop1-collider-frontdoor-proof_20260520T223911_result.json`
- **Structured JSON:** [`e3e8f9b56918001a481d.json`](../../sessions/e3/e3e8f9b56918001a481d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File structure is clean: Notation → FWL → Confounding → Mediation → **Collider** → **Front-door** → Exposure → Summary.

## 汇报

### Collider (完整代数证明)

**证明状态：完整**

关键论证步骤：
1. 从 FWL 直接推导（Lemma 不适用，因 ε_Y 与 A 非独立）
2. 利用 T ⊥ ε_Y（无条件）+ 全协方差公式得到 B(C) = −Cov(E[g(A)|A*], E[h(A)|A*]) / E[Var(T|A*)]
3. **端点分析**：B(I) = B_Berkson（满 Berkson bias），B(uniform) = 0（无偏）——与 confounding 方向完全相反
4. **比例情形 (Prop col_prop)**：当 h = λg 时，证明 |B(C)| ≤ |B(I)|，利用 x/(a−x) 单调递增
5. **一般情形 (Prop col_gen)**：Cauchy-Schwarz 界 B̄_col = √(V_g·V_h) / E[Var(T|A)]，若 |τ| > B̄_col 则 sign preservation 对所有 C 成立
6. **数值验证**：|τ|=1.0 >> B̄_col=0.147，100k random C 中 sign_flip=0%

### Front-door (半形式化证明 + 数值验证)

**证明状态：半形式化（与 mediation 同级）**

关键论证步骤：
1. FWL 分解将 numerator 分为 indirect-effect leakage + confounding residual 两项
2. **核心发现：confounding 项与 C 无关**。利用 Gaussian 回归残差 ξ = U − [α_U/Var(T)]T ⊥ (T, A, A*)，证明 Cov(T,U|A*=j) = [α_U/Var(T)]·Var(T|A*=j)，从而 confounding 项在除以 D(C) 后简化为常数 λα_U/Var(T)
3. 剩余 B_med(C) 与 mediation 拓扑结构完全相同，从 0（C=I）插值到 Cov(T,f(A))/Var(T)（C=uniform）
4. Sign preservation 条件：sign(λα_U) = sign(λα_U + Cov(T,f(A)))
5. **数值验证**：两端点 0.500 和 0.797 均为正，100k random C 中 sign_flip=0%

### Boundary cases 验证
- **C=I**：Collider 给出 τ+B_Berkson=0.886>0 ✓；Front-door 给出 0.500>0 ✓
- **C=uniform**：Collider 给出 τ=1.0>0 ✓；Front-door 给出 0.797>0 ✓

---
