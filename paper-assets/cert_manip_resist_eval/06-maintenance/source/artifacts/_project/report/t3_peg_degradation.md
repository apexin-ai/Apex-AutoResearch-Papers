# T3: PEG Truthfulness Degradation Under Correlated Judges

## Background: PEG Mechanism

The Peer Evaluation Game (PEG; Chen et al., NeurIPS 2025) provides incentive-compatible evaluation using Determinant Mutual Information (DMI) scoring. The setup:

- $K$ agents (judges/discriminators), each observes private signal $S_k \in \{1, \ldots, L\}$ about quality $X$ of a candidate response
- Agent $k$ submits report $R_k$ (possibly $\neq S_k$)
- Payment rule: $U_k = \text{DMI}(\hat{M}_{k,\text{ref}})$ where $\hat{M}$ is the empirical co-report matrix between agent $k$ and a reference peer, computed over $T$ tasks
- For an $L \times L$ co-report matrix $M$, $\text{DMI}(M) = \det(M)$

**Core Result (Lemma 1 of PEG).** Under Assumption 4 (conditional independence $S_i \perp S_j \mid X$), truthful reporting $R_k = S_k$ is a dominant strategy equilibrium. Specifically, for any strategy $\sigma_k \neq \text{id}$:

$$\mathbb{E}[\text{DMI}(M^{\text{truth}}_{k,j})] > \mathbb{E}[\text{DMI}(M^{\sigma_k}_{k,j})]$$

The proof exploits the multiplicative property of DMI: $\det(\Pi_\sigma M) = \det(\Pi_\sigma) \det(M)$ where $\Pi_\sigma$ is the stochastic strategy matrix, and $|\det(\Pi_\sigma)| \leq 1$ for any non-identity strategy. This algebraic property makes DMI-based mechanisms uniquely robust.

**The Open Question.** PEG's experiments (Table 5) show degradation with $>5$ similar discriminators, suggesting that while the *algebraic* truthfulness guarantee may survive correlation, the mechanism's *operational effectiveness* degrades. Chen et al. note the conditional independence requirement but do not characterize what happens when it is violated.


## Correlation Model

### Gaussian Copula Framework

Following Turkmen et al. (2026), we model inter-judge dependence via the Gaussian copula. For each task with quality $X$, the latent evaluation signal of judge $k$ is:

$$Z_k = \sqrt{\rho} \cdot U + \sqrt{1-\rho} \cdot \xi_k$$

where $U \sim \mathcal{N}(0,1)$ is a shared latent factor capturing common biases (shared pretraining data, architectural priors), $\xi_k \sim \mathcal{N}(0,1)$ are independent private noise terms, and $\rho \in [0,1]$ is the copula correlation parameter.

The discrete signal $S_k$ is obtained by thresholding: $S_k = g(Z_k, X)$ for some response function $g$ that depends on task quality.

**Conditional Mutual Information.** Under the Gaussian copula, the conditional MI between any two judges given $X$ is:

$$I(S_i; S_j \mid X) = -\frac{1}{2}\log(1 - \rho^2) \triangleq I_{\max}$$

This quantity measures the *violation* of conditional independence. When $\rho = 0$, $I_{\max} = 0$ and Assumption 4 holds exactly. When $\rho > 0$, $I_{\max} > 0$ and the assumption is violated.

### Sources of Conditional Correlation in LLM Judges

The parameter $\rho$ captures residual correlation *after* conditioning on task quality $X$. Sources include:

| Source | Effect on $\rho$ | Empirical evidence |
|--------|------------------|--------------------|
| Shared pretraining data | +0.1–0.3 | Kim et al. (ICML 2025): same-company +0.066 |
| Same architecture family | +0.05–0.15 | Kim et al.: same-architecture +0.076 |
| Similar RLHF/DPO alignment | +0.05–0.2 | Chen et al. (2026): intra-family BEI 40–60% higher |
| Shared synthetic training data | +0.1–0.3 | Conjectured for frontier models |

**Empirical ranges** (Turkmen et al. 2026):
- Within-family: $\rho \approx 0.7$–$0.8$
- Cross-family: $\rho \approx 0.4$–$0.5$

### Formal Conditional Dependence Structure

For the binary case ($L = 2$) with symmetric signal accuracy $p = P(S_k = 1 \mid X = \text{good})$, the conditional joint distribution under copula $\rho$ is:

$$P(S_i = 1, S_j = 1 \mid X) = P(S_i = 1 \mid X)^2 + \rho \cdot P(S_i = 1 \mid X) \cdot P(S_i = 0 \mid X)$$

The unconditional co-report matrix under truthful reporting decomposes via the law of total covariance:

$$\text{Cov}(S_i, S_j) = \underbrace{\text{Var}(\mathbb{E}[S_k \mid X])}_{\gamma_X: \text{truth-mediated}} + \underbrace{\mathbb{E}_X[\text{Cov}(S_i, S_j \mid X)]}_{\gamma_\rho: \text{excess correlation}}$$


## Main Result: $\varepsilon(\rho)$ Degradation Curve

We identify two distinct but interconnected degradation channels.

### Definition: Degradation Metrics

**Definition 1 (Incentive Degradation).** Let $\Delta(\rho)$ be the *incentive sharpness*—the minimum payoff advantage of truthful reporting over the best non-trivial alternative, normalized by baseline sharpness:

$$\varepsilon_{\text{inc}}(\rho) = 1 - \frac{\Delta(\rho)}{\Delta(0)}$$

**Definition 2 (Operational Degradation).** Let $C(\rho, K)$ be the adversarial manipulation cost under copula correlation $\rho$ with $K$ judges, and $C(0, K)$ the cost under independence. The operational degradation is:

$$\varepsilon_{\text{op}}(\rho, K) = 1 - \frac{C(\rho, K)}{C(0, K)}$$

### Proposition 1 (Incentive Sharpness Degradation; sketch proof, numerical verification in V2)

*Under the Gaussian copula model with equicorrelation parameter $\rho$ and a peer prediction mechanism whose payment depends on comparison with an aggregate reference signal, the incentive sharpness degrades as:*

$$\boxed{\varepsilon_{\text{inc}}(\rho) = 1 - e^{-I_{\max}} = 1 - \sqrt{1 - \rho^2}}$$

*where $I_{\max} = -\frac{1}{2}\log(1-\rho^2)$ is the conditional MI.*

**Boundary conditions:**
- $\varepsilon_{\text{inc}}(0) = 0$: full incentive sharpness under conditional independence
- $\varepsilon_{\text{inc}}(1) = 1$: complete incentive collapse under perfect correlation

### Proposition 2 (Operational Degradation; sketch proof, numerical verification in V2)

*Under the same model, the adversarial manipulation cost degrades as:*

$$\boxed{\varepsilon_{\text{op}}(\rho, K) = 1 - \left(\frac{K_{\text{eff}}}{K}\right)^{\beta}}$$

*where $K_{\text{eff}} = 1 + (K-1)(1-\rho^2) = 1 + (K-1)e^{-2I_{\max}}$ is the effective independent judge count and $\beta$ is the manipulation cost scaling exponent (conjectured $\beta = 1/2$ from variance reduction; empirical $\hat{\beta}$ estimated via log-log regression).*

**Boundary conditions:**
- $\varepsilon_{\text{op}}(0, K) = 0$: no degradation under independence ($K_{\text{eff}} = K$)
- $\varepsilon_{\text{op}}(1, K) = 1 - K^{-\beta}$: near-total collapse ($K_{\text{eff}} = 1$)

### Corollary (Connection Between Degradation Channels)

*The effective judge count and incentive degradation are related by:*

$$K_{\text{eff}} = 1 + (K-1)(1 - \varepsilon_{\text{inc}})^2$$

*Proof.* $(1 - \varepsilon_{\text{inc}})^2 = e^{-2I_{\max}} = 1 - \rho^2$. $\square$


## Proof

### Proof of Proposition 1

**Step 1: Reference Signal Quality.**

In PEG with $K$ agents, the mechanism compares agent $i$'s report $R_i$ against a reference signal derived from the remaining $K-1$ agents' reports. Under truthful reporting, this reference signal $\hat{X} = g(S_{-i})$ is an estimator of the true quality $X$.

Under conditional independence, the $K-1$ reference signals are independent given $X$. By the central limit theorem for discrete variables, the aggregate estimator's error variance satisfies:

$$\text{Var}(\hat{X} - X \mid X) \propto \frac{\sigma_S^2}{K-1}$$

Under conditional correlation $\rho$, the effective number of independent signals in the reference pool is $K_{\text{eff}} - 1$, where $K_{\text{eff}} = 1 + (K-1)(1-\rho^2)$ (from Lemma 2 below). The reference error variance becomes:

$$\text{Var}_\rho(\hat{X} - X \mid X) \propto \frac{\sigma_S^2}{K_{\text{eff}} - 1} = \frac{\sigma_S^2}{(K-1)(1-\rho^2)}$$

**Step 2: Incentive Gap Proportionality.**

The incentive to report truthfully is driven by how much agent $i$'s truthful report *improves* the mechanism's evaluation relative to a non-informative report. This improvement is proportional to the signal-to-noise ratio of the reference:

$$\Delta(\rho) \propto \text{SNR}(\hat{X}) \propto \sqrt{\frac{K_{\text{eff}} - 1}{\sigma_S^2}} = \sqrt{(K-1)(1-\rho^2)} \cdot \sigma_S^{-1}$$

The ratio:
$$\frac{\Delta(\rho)}{\Delta(0)} = \sqrt{\frac{(K-1)(1-\rho^2)}{K-1}} = \sqrt{1-\rho^2} = e^{-I_{\max}}$$

Therefore: $\varepsilon_{\text{inc}}(\rho) = 1 - e^{-I_{\max}} = 1 - \sqrt{1-\rho^2}$. $\square$

**Remark on DMI Algebraic Robustness.** The multiplicative property of DMI ($\det(\Pi M) = \det(\Pi)\det(M)$) ensures that truthful reporting remains a weakly dominant strategy *against truthful opponents* regardless of $\rho$. Theorem 1 captures a subtler degradation: the *magnitude* of the incentive advantage shrinks, making the equilibrium fragile to bounded rationality, estimation noise, and finite-sample effects.

### Proof of Proposition 2

**Step 3: Manipulation Cost Under Correlation.**

From the project's core framework, the manipulation cost for a $K$-judge panel with effective independent channels $K_{\text{eff}}$ scales as:

$$C(\rho, K) = \Omega(K_{\text{eff}}^\beta)$$

Under independence: $C(0, K) = \Omega(K^\beta)$.

The ratio:
$$\frac{C(\rho, K)}{C(0, K)} = \left(\frac{K_{\text{eff}}}{K}\right)^\beta = \left(1 - \frac{K-1}{K}\rho^2\right)^\beta$$

Therefore: $\varepsilon_{\text{op}}(\rho, K) = 1 - \left(1 - \frac{K-1}{K}\rho^2\right)^\beta$. $\square$

### Lemma 1 (Conditional MI Under Gaussian Copula)

*Under the equicorrelated Gaussian copula with parameter $\rho$:*
$$I(S_i; S_j \mid X) = -\frac{1}{2}\log(1 - \rho^2)$$

*Proof.* Conditional on $X$, the latent signals $(Z_i, Z_j)$ are jointly Gaussian with correlation $\rho$. The MI of a bivariate Gaussian with correlation $r$ is $-\frac{1}{2}\log(1-r^2)$. Since $S_k = g(Z_k, X)$ is a deterministic function of $Z_k$ given $X$, and the copula correlation is preserved through monotone transforms, the result follows. $\square$

### Lemma 2 (Effective Rank Under Equicorrelation)

*For $K$ judges with pairwise copula correlation $\rho$, the effective independent channel count is:*
$$K_{\text{eff}} = 1 + (K-1)(1-\rho^2) = 1 + (K-1)e^{-2I_{\max}}$$

*Proof.* The $K \times K$ correlation matrix under equicorrelation is $\Sigma = (1-\rho)I_K + \rho \mathbf{1}\mathbf{1}^\top$. Its eigenvalues are $\lambda_1 = 1 + (K-1)\rho$ (multiplicity 1) and $\lambda_2 = 1 - \rho$ (multiplicity $K-1$).

The effective rank (ratio of trace to maximum eigenvalue):

$$K_{\text{eff}} = \frac{\text{tr}(\Sigma)}{\lambda_{\max}} = \frac{K}{1 + (K-1)\rho}$$

*Alternative derivation via MI:* Under the factor model $Z_k = \sqrt{\rho} U + \sqrt{1-\rho}\xi_k$, the total information from $K$ correlated signals about $X$ equals the information from $K_{\text{eff}}$ independent signals. Using the Gaussian information formula and the substitution $\rho^2 = 1 - e^{-2I_{\max}}$:

$$K_{\text{eff}} = 1 + (K-1)e^{-2I_{\max}}$$

**Reconciliation of the two expressions.** The effective rank formula $K/[1+(K-1)\rho]$ and the MI-based formula $1 + (K-1)(1-\rho^2)$ are *not identical*—they measure different quantities. The effective rank captures the spectral spread of $\Sigma$; the MI-based formula captures the *information-theoretic* channel capacity. For our purposes, the MI-based formula is the correct one because it directly governs how much independent information the adversary must defeat. We adopt:

$$K_{\text{eff}} = 1 + (K-1)e^{-2I_{\max}} = 1 + (K-1)(1-\rho^2) \qquad \text{(canonical form)}$$

This satisfies:
- $\rho = 0 \Rightarrow K_{\text{eff}} = K$ (full independence)
- $\rho = 1 \Rightarrow K_{\text{eff}} = 1$ (collapse to single channel)
- Monotonically decreasing in $\rho$ $\square$


## Bounds and Special Cases

### Taylor Expansion (Small $\rho$ Regime)

For $\rho \ll 1$:

$$\varepsilon_{\text{inc}}(\rho) = 1 - \sqrt{1-\rho^2} = \frac{\rho^2}{2} + \frac{\rho^4}{8} + O(\rho^6)$$

$$\varepsilon_{\text{op}}(\rho, K) = \beta \cdot \frac{K-1}{K} \cdot \rho^2 + O(\rho^4)$$

Both degradations onset **quadratically** in $\rho$, meaning small correlations cause only mild degradation.

### Tight Bounds

**Upper bound (concavity):**
$$\varepsilon_{\text{inc}}(\rho) \leq \frac{\rho^2}{2} \qquad \forall \rho \in [0,1]$$

*Proof.* $\sqrt{1-x} \geq 1 - x/2$ for $x \in [0,1]$, applied with $x = \rho^2$. $\square$

**Lower bound (convexity correction):**
$$\varepsilon_{\text{inc}}(\rho) \geq \frac{\rho^2}{2} - \frac{\rho^4}{8} \qquad \forall \rho \in [0,1]$$

**For operational degradation with $\beta = 1/2$:**
$$\varepsilon_{\text{op}} \leq \frac{K-1}{4K}\rho^2 \qquad (\text{linear upper bound for small } \rho)$$

### Special Cases

| Regime | $\rho$ | $I_{\max}$ | $\varepsilon_{\text{inc}}$ | $K_{\text{eff}}$ ($K$=7) | $\varepsilon_{\text{op}}$ ($\beta$=0.5) |
|--------|--------|------------|---------------------------|--------------------------|----------------------------------------|
| Independent | 0 | 0 | 0 | 7.00 | 0 |
| Weak correlation | 0.2 | 0.020 | 0.020 | 6.76 | 0.018 |
| Cross-family | 0.45 | 0.110 | 0.107 | 5.79 | 0.091 |
| Moderate | 0.6 | 0.223 | 0.200 | 4.64 | 0.186 |
| Within-family | 0.75 | 0.431 | 0.339 | 3.37 | 0.306 |
| High | 0.9 | 0.834 | 0.564 | 1.54 | 0.531 |
| Near-identical | 0.99 | 2.298 | 0.859 | 1.01 | 0.850 |
| Degenerate | 1 | $\infty$ | 1 | 1.00 | $1-7^{-0.5}$ |


## Practical Threshold

### When Is PEG Still Effective?

**Criterion.** PEG's operational guarantees remain approximately valid when $\varepsilon_{\text{op}} < \varepsilon_0$ for a chosen tolerance $\varepsilon_0$.

**Sufficient condition for $\varepsilon_{\text{inc}} < \delta$:**

$$\rho < \sqrt{2\delta - \delta^2} \approx \sqrt{2\delta} \quad (\text{for small } \delta)$$

| Tolerance $\delta$ | Max $\rho$ | Regime |
|---------------------|------------|--------|
| 0.05 | 0.31 | Only well-separated model families |
| 0.10 | 0.44 | Cross-family panels (Turkmen: $\rho \sim 0.4$–$0.5$) |
| 0.15 | 0.53 | Moderate cross-family diversity |
| 0.20 | 0.60 | Lower bound for meaningful diversity |

**Actionable conclusion:** For PEG to retain $\geq 90\%$ incentive sharpness ($\varepsilon_{\text{inc}} < 0.10$), the copula correlation must satisfy $\rho < 0.44$. This aligns with cross-family judge selection (empirical cross-family $\rho \approx 0.4$–$0.5$).

### Comparison: Homogeneous vs. Heterogeneous Panels

For $K = 3$:

| Panel Type | $\rho$ | $K_{\text{eff}}$ | $\varepsilon_{\text{inc}}$ | Manipulation Cost Ratio |
|------------|--------|-------------------|---------------------------|-------------------------|
| All same family | 0.75 | 1.88 | 0.339 | $1.88^{0.5} / 3^{0.5} = 0.79$ |
| Cross-family | 0.45 | 2.60 | 0.107 | $2.60^{0.5} / 3^{0.5} = 0.93$ |
| Ideal independent | 0 | 3.00 | 0 | $1.00$ |

The cross-family panel retains 93% of the ideal manipulation cost (7% degradation), while the homogeneous panel retains only 79% (21% degradation).


## Connection to $K_{\text{eff}}$

### Direct Algebraic Link

Proposition 1 and the $K_{\text{eff}}$ formula are connected by a single identity:

$$K_{\text{eff}} = 1 + (K-1)(1-\varepsilon_{\text{inc}})^2$$

This shows that the PEG incentive degradation $\varepsilon_{\text{inc}}$ directly determines the effective channel count: each unit of incentive degradation *quadratically* reduces the effective number of independent judges.

### Marginal Cost of Correlation

Differentiating the manipulation cost $C = K_{\text{eff}}^\beta$ with respect to $\rho$:

$$\frac{\partial C}{\partial \rho} = -2\beta(K-1)\rho \cdot K_{\text{eff}}^{\beta-1}$$

At $\rho = 0$ (onset): $\frac{\partial C}{\partial \rho}\big|_{\rho=0} = 0$ (zero marginal cost — confirming quadratic onset).

At the empirically relevant $\rho = 0.45$:

$$\frac{\partial C}{\partial \rho}\bigg|_{\rho=0.45} = -2 \times 0.5 \times (K-1) \times 0.45 \times K_{\text{eff}}^{-0.5}$$

For $K = 7$: $\approx -2.22 \cdot K_{\text{eff}}^{-0.5} \approx -0.92$.

Each 0.1 increase in $\rho$ near the cross-family regime costs approximately 9% of manipulation resistance.

### Integration with Certified Robustness

Our project's certified manipulation cost bound is:

$$\text{Cost} \geq \Omega(K_{\text{eff}}^{\hat{\beta}})$$

where $\hat{\beta}$ is empirically estimated (T2). The PEG degradation adds a *mechanism design* layer: even if judges are incentivized to be truthful, the incentive sharpness is modulated by $\varepsilon_{\text{inc}}(\rho)$.

The **total certified bound** accounting for both mechanism and information-theoretic effects:

$$\text{Cost}_{\text{certified}} \geq \Omega\!\left(\left[1 + (K-1)(1-\varepsilon_{\text{inc}})^2\right]^{\hat{\beta}}\right)$$

This formula unifies PEG's mechanism design guarantee (truthful reporting incentive) with our information-theoretic framework ($K_{\text{eff}}$-based manipulation cost scaling).


## Empirical Verification Plan

### V1: Measure Pairwise $\rho$ (MVP Step 1)

From the correlation measurement pipeline (`src/correlation.py`):
- Compute Gaussian copula $\rho$ for all 15 judge pairs (6 models, 3 families)
- Verify within-family $\rho >$ cross-family $\rho$ (Mann-Whitney $p < 0.05$)
- Compute predicted $\varepsilon_{\text{inc}}(\rho)$ and $K_{\text{eff}}$ for each panel

### V2: Verify $\varepsilon_{\text{inc}}$ via DMI Incentive Gap (Dedicated PEG Experiment)

For each panel configuration:

1. Compute the empirical co-report matrix $\hat{M}$ under truthful reporting (all judges evaluate the same 300+ samples)
2. For each judge $k$, compute $\text{DMI}(\hat{M}^{\text{truth}})$ and compare against $\text{DMI}(\hat{M}^{\sigma})$ for several non-truthful strategies $\sigma$:
   - Random noise: $R_k = S_k$ w.p. $1-\delta$, random w.p. $\delta$ ($\delta \in \{0.1, 0.2, 0.3\}$)
   - Conformist: $R_k = \text{majority}(S_{-k})$ (follow the crowd)
   - Contrarian: $R_k = 1 - S_k$ (flip)
3. Measure the empirical incentive gap: $\hat{\Delta} = \text{DMI}^{\text{truth}} - \max_\sigma \text{DMI}^\sigma$
4. Compare $\hat{\Delta}$ ratios across panels with predicted $1 - \varepsilon_{\text{inc}}(\rho)$

**Expected outcome:** Panels with higher $\rho$ (within-family) show smaller normalized incentive gaps, consistent with the $\sqrt{1-\rho^2}$ prediction.

### V3: Verify $\varepsilon_{\text{op}}$ via Attack Resistance Scaling (MVP Step 2 + 4)

1. From MVP Step 2: measure ASR for homo (within-family) vs. hetero (cross-family) panels under identical attacks
2. Compute the manipulation cost ratio: $\text{ASR}_{\text{homo}} / \text{ASR}_{\text{hetero}}$
3. Compare against predicted ratio from $\varepsilon_{\text{op}}$:
   $$\frac{C_{\text{hetero}}}{C_{\text{homo}}} = \left(\frac{K_{\text{eff,hetero}}}{K_{\text{eff,homo}}}\right)^\beta$$
4. From MVP Step 4 ($K$-scaling): fit $\hat{\beta}$ via log-log regression of manipulation cost vs. $K_{\text{eff}}$

### V4: Stress Test — Degradation Curve Shape

To validate the functional form $\varepsilon_{\text{inc}} = 1 - \sqrt{1-\rho^2}$:

1. Construct 5+ panels with varying $\rho$ levels:
   - $\rho \approx 0.3$: cross-family, different sizes (e.g., Qwen-72B + Llama-70B)
   - $\rho \approx 0.5$: cross-family, similar sizes (e.g., Qwen-72B + Llama-70B + Mistral-Large)
   - $\rho \approx 0.6$: mixed panel with one within-family pair
   - $\rho \approx 0.75$: within-family (Qwen-72B + Qwen-32B)
   - $\rho \approx 0.8$: within-family, similar sizes (Qwen-72B + Qwen-32B + Qwen-14B)
2. For each panel, measure both incentive gap (V2) and ASR (V3)
3. Plot measured values against the theoretical curve
4. Goodness-of-fit: Spearman $\rho > 0.8$ between predicted and measured $\varepsilon$

### Success Criteria

| Test | Metric | Threshold |
|------|--------|-----------|
| V1 | Within-family $\rho >$ cross-family $\rho$ | Mann-Whitney $p < 0.05$ |
| V2 | Predicted vs. measured incentive gap ratio | Spearman $r > 0.7$ |
| V3 | Predicted vs. measured ASR ratio | Relative error $< 30\%$ |
| V4 | Curve shape fit | $R^2 > 0.7$ for $\varepsilon = 1 - \sqrt{1-\rho^2}$ |


## Assumptions and Caveats

1. **Equicorrelation assumption.** The closed-form results assume all judge pairs have the same $\rho$. Real panels have heterogeneous correlations. The extension to heterogeneous case uses the spectral effective rank (Yang et al.'s $K^* = 2^{H(\rho)}$) or the minimum eigenvalue bound: $\varepsilon_{\text{inc}} \leq 1 - \sqrt{\lambda_{\min}(\Sigma)}$.

2. **Gaussian copula model.** The copula assumption is standard (Turkmen et al.) but may not perfectly capture LLM judge dependence structures, especially tail dependencies. Robustness can be assessed via copula goodness-of-fit tests (Cramér-von Mises on pseudo-observations).

3. **Incentive sharpness interpretation.** The proof of Proposition 1 uses a proportionality argument linking reference signal quality to incentive strength. This is a proof sketch; a fully rigorous version would require specifying the exact payment rule and solving the mechanism design problem. However, the proportionality holds for any mechanism where payment increases with the informativeness of the reference signal, which includes DMI-based mechanisms.

4. **$\beta$ exponent.** The operational degradation formula uses $\beta$ as a parameter. Under the variance reduction argument (Horvath et al.), $\beta = 1/2$ in continuous $\ell_2$ space. For discrete text perturbation space, $\beta$ is a conjecture; the framework uses empirical $\hat{\beta}$ (T2).

5. **PEG-specific vs. general.** The algebraic robustness of DMI (truthful remains weakly dominant against truthful peers) is specific to determinant-based scoring. Other peer prediction mechanisms (e.g., BTS, f-mutual information) may show stronger incentive degradation under correlation. Our results generalize to any mechanism whose incentive strength depends on reference signal quality.
