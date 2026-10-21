# A/B/C Scenario Patches for λ=0.1 Results

> **使用方法**：确定场景后，按该场景的替换表逐个替换 placeholder。
> **数字占位符**：`{MEAN}`, `{S0}`, `{S1}`, `{S2}`, `{DELTA}` 替换为真实数字。
> `{MEAN}` = 3-seed 均值，`{DELTA}` = `{MEAN}` − 54.5
> **Contingency 原文为 2 seeds，已更新为 3 seeds。**

---

## Scenario B (CAR mean ≤ 57%): Full Redundancy

> SDF 在整个测试范围内冗余。论文变为 purely negative finding。Level B 为唯一 binding constraint。

### 位置 1: claim3.tex §6.3 paragraph (L29-30)

**删除**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
\placeholder{Pending: $\lambda = 0.1$ results (expected 2026-05-27).}
```

**替换为**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
Increasing $\lambda$ by 20$\times$ to 0.1 yields CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%, {S2}\%), within the null distribution (mean 54.5\%, $\sigma = 2.15$). SDF supervision is redundant with the demonstration signal across the full tested range $\lambda \in [0.005, 0.1]$ (Figure~\ref{fig:lambda_car}). This result disambiguates the two-level failure analysis (Section~\ref{sec:conclusion}): because even a 20$\times$ increase in SDF loss weight fails to produce additional avoidance, the binding constraint is not training signal magnitude (Level~A) but the structural mismatch between end-effector monitoring and full-body collision surfaces (Level~B). Stronger geometric supervision cannot compensate for supervising the wrong collision surface.
```

### 位置 2: claim3.tex figure caption (L35)

**删除**: `\placeholder{Pending: $\lambda = 0.1$.}`

**替换为**:
```latex
$\lambda = 0.1$ ({MEAN}\%) remains within the null band, confirming redundancy across a 20$\times$ loss weight range.
```

### 位置 3: discussion.tex Two-level failure paragraph (L9)

**删除**:
```latex
\placeholder{Pending: $\lambda = 0.1$ results will determine whether higher-dose SDF overcomes Level~A masking or remains redundant.}
```

**替换为**:
```latex
At $\lambda = 0.1$ (20$\times$ higher dose), CAR remains within the null range ({MEAN}\%), confirming that Level~A signal masking is not the binding constraint. The failure is architectural: EE-only supervision cannot prevent arm-body collisions regardless of loss weight.
```

### 位置 4: discussion.tex Limitations paragraph (L12)

**删除**:
```latex
\placeholder{Pending: if $\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect warrants dedicated analysis.}
```

**替换为**: （删除整个 placeholder，不替换。全域冗余下无需额外 limitation。）

### 位置 5: abstract.tex（两处修改）

**5a — λ range 扩展**

old_string:
```
$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$), rendering geometric supervision redundant at tested loss weights
```

new_string:
```
$\lambda \in \{0.005, 0.01, 0.1\}$ ($p > 0.1$), rendering geometric supervision redundant across a 20$\times$ loss weight range
```

**5b — 末句强化**

old_string:
```
EE-only geometric supervision is counterproductive at both levels: at tested loss weights, training signals are redundant with the demonstration distribution, and end-effector monitoring produces more collisions by redistributing them to unmonitored arm links.
```

new_string:
```
EE-only geometric supervision is counterproductive at both levels: across a 20$\times$ loss weight range ($\lambda \in [0.005, 0.1]$), training signals are redundant with the demonstration distribution, and end-effector monitoring produces more collisions by redistributing them to unmonitored arm links.
```

### 位置 6: introduction.tex (L20)

old_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01\}$ produces no additional benefit ($p > 0.1$). Geometric supervision is redundant with the avoidance signal already present in the demonstration distribution
```

new_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01, 0.1\}$ produces no additional benefit ($p > 0.1$). Geometric supervision is redundant with the avoidance signal already present in the demonstration distribution across a 20$\times$ loss weight range
```

---

## Scenario C (CAR mean 57-60%): Gray Zone

> 边缘区结果。表述谨慎，不做强 claim。Level A 是否有 breakpoint 留为 open question。

### 位置 1: claim3.tex §6.3 paragraph (L29-30)

**删除**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
\placeholder{Pending: $\lambda = 0.1$ results (expected 2026-05-27).}
```

**替换为**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
At $\lambda = 0.1$, CAR\,=\,{MEAN}\% (seeds: {S0}\%, {S1}\%, {S2}\%), a {DELTA}\,pp separation from the null distribution mean of 54.5\% ($\sigma = 2.15$; Figure~\ref{fig:lambda_car}). This increase is suggestive but falls in a range where seed-to-seed variation and a genuine treatment effect are difficult to distinguish with three seeds. If the separation is robust, it would indicate a dose-response threshold between $\lambda = 0.01$ and $\lambda = 0.1$, suggesting that Level~A signal masking (Section~\ref{sec:conclusion}) can be partially overcome at higher loss weights while the Level~B structural limitation of EE-only monitoring remains.
```

### 位置 2: claim3.tex figure caption (L35)

**删除**: `\placeholder{Pending: $\lambda = 0.1$.}`

**替换为**:
```latex
$\lambda = 0.1$ ({MEAN}\%) shows a suggestive but inconclusive separation from the null band.
```

### 位置 3: discussion.tex Two-level failure paragraph (L9)

**删除**:
```latex
\placeholder{Pending: $\lambda = 0.1$ results will determine whether higher-dose SDF overcomes Level~A masking or remains redundant.}
```

**替换为**:
```latex
At $\lambda = 0.1$, CAR shows a suggestive increase to {MEAN}\% (3 seeds), but the separation from the null distribution ({DELTA}\,pp) is insufficient for definitive assessment of whether Level~A masking has a breakpoint at this dose.
```

### 位置 4: discussion.tex Limitations paragraph (L12)

**删除**:
```latex
\placeholder{Pending: if $\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect warrants dedicated analysis.}
```

**替换为**:
```latex
The $\lambda = 0.1$ result ({MEAN}\%, 3 seeds) is suggestive but statistically ambiguous; additional seeds or a wider $\lambda$ sweep would clarify whether a dose-response threshold exists.
```

### 位置 5: abstract.tex（两处修改）

**5a — 追加 λ=0.1 结果**

old_string:
```
$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$), rendering geometric supervision redundant at tested loss weights
```

new_string:
```
$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$); at $\lambda = 0.1$, CAR increases to {MEAN}\% but the separation from the null distribution is inconclusive. Geometric supervision is redundant or marginal at tested loss weights
```

**5b — 末句调整**

old_string:
```
EE-only geometric supervision is counterproductive at both levels: at tested loss weights, training signals are redundant with the demonstration distribution, and end-effector monitoring produces more collisions by redistributing them to unmonitored arm links.
```

new_string:
```
EE-only geometric supervision is counterproductive: at $\lambda \leq 0.01$, training signals are redundant with the demonstration distribution; $\lambda = 0.1$ shows marginal improvement but remains inconclusive; and end-effector monitoring produces more collisions by redistributing them to unmonitored arm links.
```

### 位置 6: introduction.tex (L20)

old_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01\}$ produces no additional benefit ($p > 0.1$). Geometric supervision is redundant with the avoidance signal already present in the demonstration distribution
```

new_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01\}$ produces no additional benefit ($p > 0.1$); $\lambda = 0.1$ yields a suggestive increase to {MEAN}\% but remains inconclusive (3 seeds). At low loss weights, geometric supervision is redundant with the avoidance signal already present in the demonstration distribution
```

---

## Scenario A (CAR mean ≥ 60%): Dose-Response

> SDF 在高 λ 有效。需平衡 dose-response 发现与 Level B 结构缺陷。Claim 3 从 "fully redundant" 收窄为 "redundant at low weights, effective at high weights but still structurally limited"。

### 位置 1: claim3.tex §6.3 paragraph (L29-30)

**删除**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
\placeholder{Pending: $\lambda = 0.1$ results (expected 2026-05-27).}
```

**替换为**:
```latex
\paragraph{Dose-response at higher loss weights.}\label{sec:lambda_high}
Increasing $\lambda$ to 0.1 raises CAR to {MEAN}\% (seeds: {S0}\%, {S1}\%, {S2}\%), a {DELTA}\,pp increase beyond the null distribution mean of 54.5\% (Figure~\ref{fig:lambda_car}). This provides evidence for a dose-response relationship: SDF supervision becomes effective only when $\lambda$ exceeds a threshold between 0.01 and 0.1, below which the geometric gradient is masked by the action loss. In the two-level failure framework (Section~\ref{sec:conclusion}), this result indicates that Level~A signal masking has a breakpoint, while Level~B structural misalignment persists: oracle experiments with perfect SDF still reduce CAR below unrefined baselines regardless of signal strength, confirming that EE-only monitoring remains the binding constraint for full-body safety.
```

### 位置 2: claim3.tex figure caption (L35)

**删除**: `\placeholder{Pending: $\lambda = 0.1$.}`

**替换为**:
```latex
$\lambda = 0.1$ ({MEAN}\%) rises above the null band, indicating a dose-response threshold between $\lambda = 0.01$ and 0.1.
```

### 位置 3: discussion.tex Two-level failure paragraph (L9)

**删除**:
```latex
\placeholder{Pending: $\lambda = 0.1$ results will determine whether higher-dose SDF overcomes Level~A masking or remains redundant.}
```

**替换为**:
```latex
At $\lambda = 0.1$, CAR increases to {MEAN}\% (3 seeds), indicating that Level~A signal masking has a breakpoint between $\lambda = 0.01$ and 0.1. Level~B misalignment remains: oracle CAR stays below baselines regardless of signal strength.
```

### 位置 4: discussion.tex Limitations paragraph (L12)

**删除**:
```latex
\placeholder{Pending: if $\lambda = 0.1$ produces genuine additional avoidance, the collision transfer effect warrants dedicated analysis.}
```

**替换为**:
```latex
The dose-response effect at $\lambda = 0.1$ ({MEAN}\% CAR, {DELTA}\,pp above null) warrants dedicated analysis of whether the additional avoidance redistributes collisions to unmonitored links, as observed in oracle experiments.
```

### 位置 5: abstract.tex（两处修改）

**5a — 追加 dose-response 结果**

old_string:
```
$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$), rendering geometric supervision redundant at tested loss weights
```

new_string:
```
$\lambda \in \{0.005, 0.01\}$ ($p > 0.1$); at $\lambda = 0.1$, CAR rises to {MEAN}\%, indicating a dose-response threshold above which geometric supervision contributes beyond the demonstration distribution
```

**5b — 末句重构（平衡 dose-response 与 Level B）**

old_string:
```
EE-only geometric supervision is counterproductive at both levels: at tested loss weights, training signals are redundant with the demonstration distribution, and end-effector monitoring produces more collisions by redistributing them to unmonitored arm links.
```

new_string:
```
EE-only geometric supervision is structurally limited: at low loss weights, training signals are masked by the demonstration distribution; at $\lambda = 0.1$, CAR improves but end-effector monitoring still redistributes collisions to unmonitored arm links, as confirmed by oracle experiments.
```

### 位置 6: introduction.tex (L20)

old_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01\}$ produces no additional benefit ($p > 0.1$). Geometric supervision is redundant with the avoidance signal already present in the demonstration distribution
```

new_string:
```
adding SDF supervision at $\lambda \in \{0.005, 0.01\}$ produces no additional benefit ($p > 0.1$), but at $\lambda = 0.1$, CAR rises to {MEAN}\%, revealing a dose-response threshold. Below this threshold, geometric supervision is masked by the avoidance signal already present in the demonstration distribution
```
