# Identifiability Analysis of the Gated Multi-Facet Rasch Model

<!-- 
Purpose: Formal identifiability analysis of G-MFRM parameters (θ, b, d, c, τ) under fixed e_i.
Relation to paper: Core theoretical contribution addressing the non-triviality of the gating extension.
Complements: error_propagation_theory.md (exp-012) which analyzes sensitivity to e_i noise.
-->

## 1. Preliminaries

### 1.1 Model Specification

The **Gated Multi-Facet Rasch Model (G-MFRM)** extends the standard MFRM by incorporating a contamination interaction term:

$$
\text{logit}\, P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, c_n, e_i, \tau_k) = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i
$$

where:
- $Y_{nij} \in \{0, 1, \ldots, K\}$: ordinal rating assigned by judge $j$ to model $n$ on item $i$
- $\theta_n$: ability of model $n$ ($n = 1, \ldots, N$)
- $b_i$: difficulty of item $i$ ($i = 1, \ldots, I$)
- $d_j$: severity of judge $j$ ($j = 1, \ldots, J$)
- $\tau_k$: threshold parameter for category $k$ ($k = 1, \ldots, K$), with $\tau_1 = 0$ by convention
- $c_n \geq 0$: contamination susceptibility of model $n$
- $e_i \in \mathbb{R}$: exposure level of item $i$ (fixed/known)

The standard MFRM is recovered when $c_n = 0$ for all $n$, or equivalently when $e_i = 0$ for all $i$.

### 1.2 Definitions of Identifiability

**Definition 1 (Structural Identifiability).** A parameter $\xi$ in a model $\mathcal{M}$ is *structurally identifiable* if for all $\xi, \xi'$ in the parameter space $\Xi$:
$$
P(\mathbf{Y} \mid \xi) = P(\mathbf{Y} \mid \xi') \quad \Longrightarrow \quad \xi = \xi'
$$

**Definition 2 (Local Identifiability).** A parameter $\xi_0$ is *locally identifiable* if there exists a neighborhood $U$ of $\xi_0$ such that for all $\xi \in U \setminus \{\xi_0\}$:
$$
P(\mathbf{Y} \mid \xi) \neq P(\mathbf{Y} \mid \xi_0)
$$

**Definition 3 (Generic Identifiability).** The model is *generically identifiable* if the set of non-identified parameter values has Lebesgue measure zero in $\Xi$.

**Theorem (Rothenberg, 1971).** Under standard regularity conditions, local identifiability at $\xi_0$ is equivalent to the Fisher information matrix $\mathcal{I}(\xi_0)$ being nonsingular (full rank) at $\xi_0$.

### 1.3 Standard MFRM Identifiability (Known Results)

For the standard MFRM without the gating term:
$$
\text{logit}\, P(Y_{nij} \geq k) = \theta_n - b_i - d_j - \tau_k
$$

the model has a **location indeterminacy**: for any constant $\alpha$,
$$
(\theta_n + \alpha,\; b_i + \alpha,\; d_j,\; \tau_k) \quad \text{and} \quad (\theta_n,\; b_i,\; d_j - \alpha,\; \tau_k)
$$
produce identical likelihoods.

The standard identifying constraints are:
- $\sum_n \theta_n = 0$, or fix one $\theta_{n_0} = 0$, or $\sum_i b_i = 0$
- $\sum_j d_j = 0$ (or fix one $d_{j_0} = 0$)
- $\tau_1 = 0$

**Connectedness requirement (Linacre, 1994):** In an incomplete (non-crossed) design, the MFRM is identifiable if and only if the design is *connected*—i.e., the bipartite graph linking facets through shared observations forms a single connected component. In a fully crossed design (every judge rates every model on every item), connectedness is trivially satisfied.

## 2. Identifiability of G-MFRM with Fixed $e_i$

### 2.1 Indeterminacies in G-MFRM

**Proposition 1 (Location Indeterminacy Persists).** The G-MFRM inherits the location indeterminacy of the standard MFRM in the $(\theta, b)$ and $d$ subspaces.

*Proof.* Consider the transformation $T_\alpha: (\theta_n, b_i, d_j, c_n) \mapsto (\theta_n + \alpha, b_i + \alpha, d_j, c_n)$. The linear predictor becomes:
$$
(\theta_n + \alpha) - (b_i + \alpha) - d_j - \tau_k + c_n \cdot e_i = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i
$$
which is unchanged. Similarly for shifts in $d_j$. □

**Proposition 2 (No New Scale Indeterminacy from Gating Term).** When $e_i$ is fixed and known, the gating term $c_n \cdot e_i$ does *not* introduce additional location or scale indeterminacies beyond those of the standard MFRM.

*Proof.* Suppose there exist $\delta \neq 0$ and a transformation such that $c_n' = c_n + \delta$ preserves all probabilities. Then we require:
$$
c_n \cdot e_i = (c_n + \delta) \cdot e_i \quad \forall\, i \text{ with } e_i \neq 0
$$
This gives $\delta \cdot e_i = 0$ for all $i$ with $e_i \neq 0$, hence $\delta = 0$, a contradiction.

For a scale transformation $c_n' = \lambda c_n$ with $\lambda \neq 1$: we require $c_n \cdot e_i = \lambda c_n \cdot e_i$ for all $(n, i)$, which fails whenever $c_n \neq 0$ and $e_i \neq 0$. □

**Remark.** This is a key structural insight: because $e_i$ is externally fixed (not estimated), the product $c_n \cdot e_i$ does not suffer from the bilinear indeterminacy $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would arise if both $c_n$ and $e_i$ were free parameters. The decision to fix $e_i$ from external contamination detection tools is not merely practical but is *necessary for identifiability*.

### 2.2 Necessary Conditions

**Proposition 3 (Exposure Variation is Necessary for $c_n$ Identifiability).** If $e_i = e$ for all $i$ (constant exposure), then $c_n$ is not separately identifiable from $\theta_n$.

*Proof.* When $e_i = e$ is constant, the linear predictor becomes:
$$
\theta_n - b_i - d_j - \tau_k + c_n \cdot e = (\theta_n + c_n e) - b_i - d_j - \tau_k
$$
Define $\theta_n^* = \theta_n + c_n e$. The model reduces to a standard MFRM with ability $\theta_n^*$, and no data can distinguish $(\theta_n, c_n)$ from $(\theta_n + c_n e - c_n' e,\; c_n')$ for arbitrary $c_n'$. □

**Corollary 1.** $\text{Var}(e_i) > 0$ is a *necessary condition* for the identifiability of $c_n$.

**Proposition 4 (Minimum Judge Requirement).** In the G-MFRM with fully crossed design, $J \geq 2$ is necessary for identifying the judge severity parameters $d_j$ separately from $\theta_n$.

*Proof.* With $J = 1$, there is a single $d_1$ which is confounded with the location of $\theta_n$ (shifting all $\theta_n$ up by $\alpha$ and $d_1$ down by $\alpha$ is observationally equivalent). With $J \geq 2$ and the constraint $\sum_j d_j = 0$, the $d_j$ differences are identified from the differential rating patterns across judges. □

**Remark.** Unlike the standard MFRM where $J \geq 2$ suffices for full identifiability (given connectedness), the G-MFRM does *not* require additional judges beyond $J = 2$ for identifiability of $c_n$. The contamination parameters are identified through the item facet (variation in $e_i$), not the judge facet.

**Proposition 5 (Minimum Item Requirements).** For $c_n$ to be identifiable for a given model $n$, model $n$ must be evaluated on at least two items $i, i'$ with $e_i \neq e_{i'}$.

*Proof.* The contribution of model $n$ to the likelihood involves terms of the form $\theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$. To separate $\theta_n$ from $c_n$, we need observations at different values of $e_i$. With only one distinct value of $e_i$, the argument from Proposition 3 applies locally to model $n$. With two distinct values $e_i \neq e_{i'}$, the system:
$$
\theta_n + c_n e_i = \eta_i, \quad \theta_n + c_n e_{i'} = \eta_{i'}
$$
has a unique solution $(\theta_n, c_n)$ given $(\eta_i, \eta_{i'})$ and $e_i \neq e_{i'}$. □

### 2.3 Sufficient Conditions

**Theorem 1 (Sufficient Conditions for G-MFRM Identifiability).** Consider the G-MFRM with parameter vector $\xi = (\theta_1, \ldots, \theta_N, b_1, \ldots, b_I, d_1, \ldots, d_J, c_1, \ldots, c_N, \tau_2, \ldots, \tau_K)$ and fixed exposure values $e_1, \ldots, e_I$. The model is locally identifiable (up to the standard location constraints) under the following sufficient conditions:

1. **Design:** Fully crossed—every judge $j$ rates every model $n$ on every item $i$.
2. **Judges:** $J \geq 2$.
3. **Items:** $I \geq 2$ with at least two distinct exposure values, i.e., $|\{e_i : i = 1, \ldots, I\}| \geq 2$.
4. **Exposure variation:** $\text{Var}(e_i) > 0$ (implied by condition 3).
5. **Normalization:** $\sum_n \theta_n = 0$, $\sum_j d_j = 0$, and $\tau_1 = 0$.

Under these conditions, the Fisher information matrix $\mathcal{I}(\xi)$ is nonsingular for generic parameter values.

*Proof sketch.* We verify the rank of $\mathcal{I}(\xi)$ by examining the score equations. The total number of free parameters after normalization is:
$$
p = (N - 1) + I + (J - 1) + N + (K - 1) = 2N + I + J + K - 3
$$

The score vector $\nabla_\xi \ell(\xi)$ has components:

**For $\theta_n$:** $\frac{\partial \ell}{\partial \theta_n} = \sum_{i,j,k} \left[ \mathbb{1}(Y_{nij} \geq k) - P(Y_{nij} \geq k \mid \xi) \right]$

**For $b_i$:** $\frac{\partial \ell}{\partial b_i} = -\sum_{n,j,k} \left[ \mathbb{1}(Y_{nij} \geq k) - P(Y_{nij} \geq k \mid \xi) \right]$

**For $d_j$:** $\frac{\partial \ell}{\partial d_j} = -\sum_{n,i,k} \left[ \mathbb{1}(Y_{nij} \geq k) - P(Y_{nij} \geq k \mid \xi) \right]$

**For $c_n$:** $\frac{\partial \ell}{\partial c_n} = \sum_{i,j,k} e_i \left[ \mathbb{1}(Y_{nij} \geq k) - P(Y_{nij} \geq k \mid \xi) \right]$

The Fisher information matrix entry for the $(\theta_n, c_n)$ block of a single model $n$ is:
$$
\mathcal{I}_{(\theta_n, c_n)} = \sum_{i,j,k} \begin{pmatrix} 1 \\ e_i \end{pmatrix} \begin{pmatrix} 1 & e_i \end{pmatrix} \cdot \text{Var}[\mathbb{1}(Y_{nij} \geq k)]
$$
$$
= \sum_{i,j,k} P_{nijk}(1 - P_{nijk}) \begin{pmatrix} 1 & e_i \\ e_i & e_i^2 \end{pmatrix}
$$

where $P_{nijk} = P(Y_{nij} \geq k \mid \xi)$.

The determinant of this $2 \times 2$ block is:
$$
\det \mathcal{I}_{(\theta_n, c_n)} = \left(\sum_{i,j,k} w_{nijk}\right)\left(\sum_{i,j,k} w_{nijk} e_i^2\right) - \left(\sum_{i,j,k} w_{nijk} e_i\right)^2
$$

where $w_{nijk} = P_{nijk}(1 - P_{nijk}) > 0$ for $P_{nijk} \in (0,1)$.

By the Cauchy-Schwarz inequality, this determinant is strictly positive if and only if the $e_i$ values are not all identical (weighted by $w_{nijk}$). Under condition 3, $|\{e_i\}| \geq 2$, so $\text{Var}_{w}(e_i) > 0$ and the block is positive definite.

The remaining blocks ($b_i$, $d_j$, $\tau_k$) inherit identifiability from the standard MFRM theory under connectedness (which is guaranteed by the fully crossed design). The cross-information between $(b_i)$ and $(c_n)$ does not introduce rank deficiencies because $b_i$ enters additively while $c_n$ enters multiplicatively with $e_i$.

A formal proof of generic full rank proceeds by showing the information matrix is nonsingular at a specific parameter value (e.g., $\theta_n = b_i = d_j = 0$, $c_n = 1$, $\tau_k = k-1$), which by continuity implies nonsingularity in a neighborhood, and by the analytic dependence of $\mathcal{I}(\xi)$ on $\xi$, the singular set has measure zero (generic identifiability). □

### 2.4 The Role of Incomplete Designs

**Proposition 6 (Incomplete Designs).** In an incomplete design where not all $(n, i, j)$ combinations are observed, identifiability of $c_n$ additionally requires:

(a) For each model $n$, the set of items evaluated must contain at least two items with distinct $e_i$ values.

(b) The design must be connected in the sense of Linacre (1994) for the standard MFRM parameters.

(c) Each model $n$ must be rated by at least one judge on items spanning distinct exposure levels.

*Proof sketch.* Condition (a) follows from the argument of Proposition 5. Conditions (b) and (c) ensure that the MFRM substructure remains identified and that exposure variation is exploited in the observations for each model. □

## 3. Role of Exposure Variation

### 3.1 Quantifying Information About $c_n$

The Fisher information for $c_n$ (conditional on other parameters) is:
$$
\mathcal{I}(c_n) = \sum_{i \in \mathcal{O}_n} \sum_{j \in \mathcal{J}_n} \sum_{k=1}^K e_i^2 \cdot P_{nijk}(1 - P_{nijk})
$$

where $\mathcal{O}_n$ is the set of items observed for model $n$ and $\mathcal{J}_n$ the set of judges.

**Key observations:**
- Items with $e_i = 0$ (unexposed items) contribute zero information about $c_n$.
- Items with large $|e_i|$ contribute quadratically more information.
- The information is maximized when observations span a wide range of $e_i$ values.

### 3.2 Separation of $\theta_n$ and $c_n$

The joint information for $(\theta_n, c_n)$ has off-diagonal element $\sum_{i,j,k} w_{nijk} e_i$. The *conditional* information for $c_n$ given $\theta_n$ is:

$$
\mathcal{I}(c_n \mid \theta_n) = \sum_{i,j,k} w_{nijk} e_i^2 - \frac{\left(\sum_{i,j,k} w_{nijk} e_i\right)^2}{\sum_{i,j,k} w_{nijk}}
$$

$$
= \left(\sum_{i,j,k} w_{nijk}\right) \cdot \text{Var}_w(e_i)
$$

where $\text{Var}_w(e_i)$ is the weighted variance of exposure values with weights $w_{nijk}$.

**Proposition 7 (Precision of $c_n$ Estimation).** The asymptotic variance of $\hat{c}_n$ satisfies:
$$
\text{Var}(\hat{c}_n) \geq \frac{1}{\mathcal{I}(c_n \mid \theta_n)} = \frac{1}{\left(\sum_{i,j,k} w_{nijk}\right) \cdot \text{Var}_w(e_i)}
$$

This bound reveals that:
1. **More items** (larger $I$) reduce variance linearly.
2. **More judges** (larger $J$) reduce variance linearly.
3. **Greater exposure variance** reduces variance—this is the key design lever specific to G-MFRM.

### 3.3 Degenerate Cases

**Case 1: $e_i = 0$ for all $i$.** The model reduces to standard MFRM; $c_n$ vanishes from the likelihood. Parameters $c_n$ are completely unidentified.

**Case 2: $e_i = e > 0$ constant.** As shown in Proposition 3, $c_n$ is confounded with $\theta_n$. The model is equivalent to MFRM with effective ability $\theta_n^* = \theta_n + c_n e$.

**Case 3: $e_i \in \{0, e\}$ binary.** The model is identifiable: items with $e_i = 0$ anchor $\theta_n$ (no contamination effect), while items with $e_i = e$ provide leverage for estimating $c_n$. This is the *minimal* exposure design for identifiability.

**Case 4: $e_i$ continuous with high variance.** Optimal for estimation precision. The design acts like a regression with $e_i$ as the "predictor" for the contamination effect.

### 3.4 Connection to Regression Interpretation

The G-MFRM linear predictor for model $n$ can be rewritten (absorbing $b_i + d_j + \tau_k$ into an "adjusted threshold"):
$$
\eta_{nijk} = \underbrace{\theta_n}_{\text{intercept}} + \underbrace{c_n}_{\text{slope}} \cdot e_i - b_i - d_j - \tau_k
$$

For fixed $(j, k)$, the model is a logistic regression in $e_i$ with model-specific intercept $\theta_n$ and slope $c_n$. The identifiability of slope and intercept in logistic regression requires variation in the predictor ($e_i$)—a classical result.

## 4. Comparison with Standard MFRM

### 4.1 Parameter Space Geometry

| Property | Standard MFRM | G-MFRM (fixed $e_i$) |
|----------|--------------|----------------------|
| Free parameters | $N + I + J + K - 3$ | $2N + I + J + K - 3$ |
| Indeterminacies | Location (1 d.f.) | Location (1 d.f., same) |
| Identification constraints needed | 2 (location + $\tau_1$) | 2 (same as MFRM) |
| Design requirement | Connectedness | Connectedness + $\text{Var}(e_i) > 0$ |
| Minimum judges | $J \geq 2$ | $J \geq 2$ |
| Minimum items | $I \geq 2$ | $I \geq 2$ with distinct $e_i$ |

### 4.2 What Changes When $c_n \cdot e_i$ is Added

The gating term adds $N$ parameters ($c_1, \ldots, c_N$) while requiring no additional normalization constraints. This is because:

1. **No bilinear ambiguity:** Since $e_i$ is fixed, there is no $c_n \leftrightarrow e_i$ trade-off.
2. **No additive confounding with $\theta_n$:** The exposure variation $\text{Var}(e_i) > 0$ breaks the degeneracy (Proposition 3).
3. **No confounding with $b_i$:** The terms $-b_i$ and $c_n \cdot e_i$ are structurally different—$b_i$ is item-specific (no $n$ subscript), while $c_n \cdot e_i$ is model-specific in its coefficient.

**Key insight:** The gating extension is *not* a trivial addition. It changes the structure of the sufficient statistics—specifically, the sufficient statistic for $c_n$ is $\sum_{i,j,k} e_i \cdot \mathbb{1}(Y_{nij} \geq k)$, which is a *weighted* sum of responses (weighted by exposure), distinct from the unweighted sum that is sufficient for $\theta_n$. The existence of distinct sufficient statistics is what enables simultaneous identification.

### 4.3 Comparison of Information Structures

In the standard MFRM, the information about $\theta_n$ depends on the number of items and judges:
$$
\mathcal{I}^{\text{MFRM}}(\theta_n) = \sum_{i,j,k} P_{nijk}(1 - P_{nijk})
$$

In the G-MFRM, the information about $\theta_n$ is *reduced* due to the need to simultaneously estimate $c_n$. The effective information is:
$$
\mathcal{I}^{\text{G-MFRM}}(\theta_n \mid c_n) = \mathcal{I}^{\text{MFRM}}(\theta_n) \cdot \left(1 - \rho_w^2(1, e_i)\right)
$$

where $\rho_w^2(1, e_i)$ is the squared weighted correlation between the constant vector $\mathbf{1}$ and the exposure vector $\mathbf{e}$ (with weights $w_{nijk}$). When the mean of $e_i$ is far from zero, this correlation is high, and there is greater information loss. **Design implication:** Centering $e_i$ around zero (e.g., $\bar{e} = 0$) minimizes the information loss for $\theta_n$.

## 5. Connection to IRT/Psychometric Literature

### 5.1 Rasch Model Identifiability Framework

San Martín (2016) provided a comprehensive treatment of identifiability in IRT models, distinguishing between fixed-effects and random-effects specifications. For the fixed-effects Rasch model:
- Under **fixed effects**: identifiability requires fixing one ability parameter (or imposing $\sum \theta_n = 0$) and one difficulty parameter (or $\sum b_i = 0$).
- Under **random effects** ($\theta_n \sim F$): the marginal likelihood identifies $b_i$ up to location without fixing parameters, because the mixing distribution $F$ absorbs the indeterminacy.

San Martín and De Boeck (2015) showed that the interpretation of the difficulty parameter $b_i$ differs fundamentally between these two specifications, highlighting that identifiability is not merely a technical constraint but affects substantive interpretation.

The G-MFRM inherits the fixed-effects identifiability structure for $(\theta, b, d)$ while adding parameters $c_n$ that are identified through the covariate $e_i$—a structure more akin to explanatory IRT models (De Boeck & Wilson, 2004) where person covariates enter the model.

### 5.2 Identifiability with Guessing/Slipping Parameters

San Martín, Rolin, and Castro (2013) analyzed identifiability of the 1PL-G model (Rasch with guessing):
$$
P(Y_{ni} = 1) = c + (1-c) \cdot \text{logit}^{-1}(\theta_n - b_i)
$$

They showed that the guessing parameter $c$ requires at least 3 items for identifiability and that one item must have its guessing parameter fixed. The G-MFRM gating term $c_n \cdot e_i$ is structurally different from a guessing parameter—it is an additive interaction rather than a lower asymptote—but the parallel is instructive: additional parameters require additional structural constraints for identification.

### 5.3 Cognitive Diagnostic Model Identifiability

Xu and Zhang (2016) established necessary and sufficient conditions for identifiability of diagnostic classification models (DINA model) based on the structure of the Q-matrix. Their key result: the Q-matrix must be *complete* (containing two identity sub-matrices) for all attribute profiles to be distinguishable.

The analogy to G-MFRM: the exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ plays a role analogous to the Q-matrix—it defines the "loading structure" of the contamination facet. Just as Q-matrix completeness is necessary for identifiability in CDMs, exposure variation is necessary for identifiability in G-MFRM.

### 5.4 Differential Item Functioning

The G-MFRM gating term has a structural connection to uniform DIF. In DIF analysis, an item functions differently across groups:
$$
\text{logit}\, P(Y_{ni} = 1 \mid g_n) = \theta_n - b_i + \gamma_i \cdot g_n
$$
where $g_n$ is a group indicator. The G-MFRM replaces the binary group indicator with continuous susceptibility $c_n$ and replaces the item-specific DIF parameter $\gamma_i$ with the known exposure $e_i$:
$$
\text{G-MFRM}: \quad \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i
$$
$$
\text{DIF}: \quad \theta_n - b_i + \gamma_i \cdot g_n
$$

Key structural differences:
- DIF: $\gamma_i$ is item-specific and estimated; $g_n$ is known (group membership).
- G-MFRM: $c_n$ is model-specific and estimated; $e_i$ is known (exposure level).
- The "transposition" of known/unknown between items and persons gives G-MFRM different identifiability properties.

### 5.5 Many-Facet Rasch Extensions

Uto and Ueno (2020) proposed a generalized many-facet Rasch model incorporating multiple rater characteristics (severity, consistency, range restriction) with Bayesian estimation via Hamiltonian Monte Carlo. Their model demonstrates that additional facets can be identified given sufficient crossing of the design, supporting the feasibility of estimating additional parameters (like $c_n$) in multi-facet contexts.

## 6. Practical Implications

### 6.1 Minimum Experimental Design Requirements

Based on the theoretical analysis, the following are *minimum* requirements for a valid G-MFRM study:

**Hard requirements (violation → non-identifiability):**
- At least $J = 2$ judges
- At least $I = 2$ items with distinct exposure levels
- $\text{Var}(e_i) > 0$
- Fully crossed design (or connected incomplete design satisfying Proposition 6)

**Recommended requirements (for practical identifiability and precision):**
- $J \geq 3$ judges (robustness to judge dropout)
- $I \geq 20$ items spanning a range of $e_i$ values
- Include items with $e_i = 0$ (anchors for $\theta_n$) and items with high $e_i$ (leverage for $c_n$)
- Binary or near-binary $e_i$ distribution may suffice but continuous $e_i$ is more efficient

### 6.2 Design Optimization Guidelines

**Guideline 1: Include "clean" items.** Items with $e_i = 0$ (no contamination) serve as anchors for estimating $\theta_n$ without confounding. At least $30\%$ of items should have $e_i \approx 0$.

**Guideline 2: Maximize exposure range.** The precision of $\hat{c}_n$ scales with $\text{Var}(e_i)$. Including items with very high exposure provides the most leverage.

**Guideline 3: Center exposure values.** If possible, use a design where $\bar{e}_i \approx 0$ (mean-centered exposure). This minimizes the correlation between the sufficient statistics for $\theta_n$ and $c_n$, improving joint estimation efficiency.

**Guideline 4: Sufficient judges per item.** Each item should be rated by at least 2 judges. More judges reduce the variance of all parameters but are especially important for $d_j$ estimation.

### 6.3 Practical vs. Structural Identifiability

Even when structural identifiability holds, *practical identifiability* may fail if:
- $\text{Var}(e_i)$ is very small (weak identification)
- $c_n$ values are close to zero for most models (near-boundary estimation)
- The sample of responses per cell $(n, i, j)$ is small (single observation in fully crossed design)

**Recommendation:** Verify practical identifiability via:
1. Posterior diagnostic: $\hat{R}$ convergence and ESS in Bayesian estimation
2. Profile likelihood: check for flat ridges
3. Simulation: confirm parameter recovery under the planned design (as done in mvp_003 and exp-012)

### 6.4 Connection to Our Experimental Validation

The experimental results from mvp_003 (N=50, I=100, J=8, fully crossed) confirm practical identifiability:
- Joint estimation achieved $\hat{R} = 1.03$ and ESS = 224, indicating MCMC convergence
- Rank correlation $\tau = 0.92$ between true and estimated parameters
- The design satisfies all sufficient conditions of Theorem 1 with substantial margin

## 7. Summary of Main Results

| # | Statement | Type | Key Condition |
|---|-----------|------|---------------|
| P1 | Location indeterminacy persists | Negative | Standard constraints needed |
| P2 | No new indeterminacy from gating | Positive | $e_i$ fixed |
| P3 | Constant $e_i$ → $c_n$ unidentified | Necessary | $\text{Var}(e_i) > 0$ |
| P4 | $J \geq 2$ for $d_j$ identification | Necessary | Same as MFRM |
| P5 | Two distinct $e_i$ per model | Necessary | Item coverage |
| P6 | Incomplete design conditions | Necessary | Connectedness + coverage |
| P7 | Precision bound for $\hat{c}_n$ | Informational | $\propto 1/\text{Var}_w(e_i)$ |
| T1 | Sufficient conditions for full identifiability | Sufficient | Crossed + $J≥2$ + $\text{Var}(e_i)>0$ |

---

## References

- Linacre, J. M. (1994). *Many-Facet Rasch Measurement*. MESA Press.

- Rothenberg, T. J. (1971). Identification in parametric models. *Econometrica*, 39(3), 577–591.

- San Martín, E. (2016). Identification of item response theory models. In W. J. van der Linden (Ed.), *Handbook of Item Response Theory, Volume 2: Statistical Tools* (pp. 127–150). CRC Press.

- San Martín, E., & De Boeck, P. (2015). What do you mean by a difficult item? On the interpretation of the difficulty parameter in a Rasch model. In R. E. Millsap et al. (Eds.), *Quantitative Psychology Research*, Springer Proceedings in Mathematics & Statistics, Vol. 89, Chapter 1. Springer.

- San Martín, E., Rolin, J.-M., & Castro, L. M. (2013). Identification of the 1PL model with guessing parameter: Parametric and semi-parametric results. *Psychometrika*, 78(2), 341–379.

- Fariña, P., González, J., & San Martín, E. (2019). The use of an identifiability-based strategy for the interpretation of parameters in the 1PL-G and Rasch models. *Psychometrika*, 84(2), 511–528.

- Xu, G., & Zhang, S. (2016). Identifiability of diagnostic classification models. *Psychometrika*, 81(3), 625–649.

- Uto, M., & Ueno, M. (2020). A generalized many-facet Rasch model and its Bayesian estimation using Hamiltonian Monte Carlo. *Behaviormetrika*, 47(2), 469–496.

- De Boeck, P., & Wilson, M. (2004). *Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach*. Springer.
