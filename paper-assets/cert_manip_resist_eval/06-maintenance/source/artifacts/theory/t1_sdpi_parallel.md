# T1: SDPI Parallel Channel Composition

## Setting

Consider a multi-judge evaluation protocol where $K$ judges independently score the same input.

| Symbol | Definition |
|--------|-----------|
| $\mathcal{X}$ | Input space (e.g., response pairs) |
| $\mathcal{Y}$ | Score/verdict space |
| $X \in \mathcal{X}$ | Input to be evaluated |
| $W_k: \mathcal{X} \to \mathcal{Y}$ | Judge $k$'s stochastic channel, $k = 1, \ldots, K$ |
| $Y_k = W_k(X)$ | Judge $k$'s output |
| $\eta_k \in [0,1]$ | SDPI contraction coefficient of $W_k$: $\eta_k := \sup_{P \neq Q} \frac{D_{KL}(W_k P \| W_k Q)}{D_{KL}(P \| Q)}$ |
| $\eta_{\max}$ | $\max_k \eta_k$ |
| $I(Y_i; Y_j)$ | Pairwise mutual information between judge outputs (under reference input distribution) |
| $I_{\max}$ | $\max_{i \neq j} I(Y_i; Y_j)$ |
| $f(Y_1, \ldots, Y_K)$ | Panel aggregation rule (e.g., majority vote) |

**Attacker's action**: Replace the input distribution $P_X$ with a manipulated distribution $Q_X$, incurring cost $\Delta := D_{KL}(Q_X \| P_X)$, with the goal of flipping $f(Y^K)$.

**Channel model**: The joint channel $W^{(K)}: X \to (Y_1, \ldots, Y_K)$ broadcasts a single input to $K$ judges. Judges may be correlated—both through the shared input $X$ (which induces marginal dependence) and through shared biases (training data overlap, architectural similarities), which induce conditional dependence $I(Y_i; Y_j \mid X) > 0$.

---

## Key Distinction: Serial vs Parallel

### Serial Chain (Markov cascade)

If judges formed a processing pipeline $X \to Y_1 \to Y_2 \to \cdots \to Y_K$ (each judge only sees the previous judge's output):

$$D_{KL}(P_{Y_K \mid Q} \| P_{Y_K \mid P}) \leq \prod_{k=1}^K \eta_k \cdot D_{KL}(Q \| P) = \eta^K \cdot \Delta$$

for homogeneous channels ($\eta_k = \eta$). The attacker's influence **decays exponentially** with $K$—each link in the chain further attenuates the perturbation signal. This is iterated application of the data processing inequality.

### Parallel Channels (broadcast)

The actual multi-judge setting: $X$ is broadcast simultaneously to all $K$ judges.

$$X \longrightarrow \begin{cases} W_1 \to Y_1 \\ W_2 \to Y_2 \\ \vdots \\ W_K \to Y_K \end{cases}$$

Each channel independently processes the **same input**. The information about the perturbation $P \to Q$ does not attenuate through a chain; instead, each judge extracts its own view of the perturbation. The total information the attacker injects into the panel **grows** with $K$ (additively, bounded by redundancy), rather than decaying.

**Mathematical distinction**:

| Property | Serial ($X \to Y_1 \to \cdots \to Y_K$) | Parallel ($X \to \{Y_1, \ldots, Y_K\}$) |
|----------|------|----------|
| SDPI composition | $\eta_{\text{joint}} = \prod_k \eta_k = \eta^K$ | $\eta_{\text{joint}} \leq K_{\text{eff}} \cdot \eta_{\max}$ |
| Scaling with $K$ | Exponential decay | Linear growth (sublinear with correlation) |
| Attacker's influence | Vanishes: $\eta^K \to 0$ | Bounded: $\leq K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta$ |
| Defense mechanism | Information attenuation | Voting concentration |

**The original proposal's error**: treating the multi-judge panel as a serial chain gives a misleadingly optimistic $\eta^K$ defense. The parallel model is weaker in information attenuation but provides defense through a different mechanism: the combinatorial difficulty of flipping a majority vote.

---

## Lemma 1: Parallel Information Bound

**Lemma 1** (Parallel Channel SDPI). *Let $W^{(K)}: \mathcal{X} \to \mathcal{Y}^K$ be a $K$-judge parallel channel with component SDPI constants $\eta_1, \ldots, \eta_K$ and pairwise mutual information $I(Y_i; Y_j)$ under a reference input distribution. For any two input distributions $P, Q$ over $\mathcal{X}$:*

$$D_{KL}\!\left(W^{(K)} Q \;\big\|\; W^{(K)} P\right) \leq K_{\text{eff}} \cdot \eta_{\max} \cdot D_{KL}(Q \| P)$$

*where*

$$\boxed{K_{\text{eff}} = 1 + (K-1) \cdot \exp\!\left(-2 \, I_{\max}\right)}$$

*with $I_{\max} = \max_{i \neq j} I(Y_i; Y_j)$.*

**Boundary behavior**:
- $I_{\max} = 0$ (independent judges): $K_{\text{eff}} = K$ — full additive composition.
- $I_{\max} \to \infty$ (perfectly correlated): $K_{\text{eff}} \to 1$ — degenerates to a single channel.
- For fixed $I_{\max}$: $K_{\text{eff}}$ is affine in $K$, growing as $\exp(-2I_{\max}) \cdot K$.

---

## Proof Sketch

### Step 1: Individual SDPI

By definition of the contraction coefficient, for each channel $k$:

$$D_{KL}(W_k Q \| W_k P) \leq \eta_k \cdot D_{KL}(Q \| P) \leq \eta_{\max} \cdot \Delta$$

where $\Delta = D_{KL}(Q \| P)$.

### Step 2: Joint channel decomposition

The joint output KL divergence decomposes via the chain rule:

$$D_{KL}\!\left(P_{Y^K \mid Q} \;\big\|\; P_{Y^K \mid P}\right) = \sum_{k=1}^K D_{KL}\!\left(P_{Y_k \mid Y_{<k}, Q} \;\big\|\; P_{Y_k \mid Y_{<k}, P}\right)$$

where $Y_{<k} = (Y_1, \ldots, Y_{k-1})$. Each term is the **conditional information increment**: how much new information channel $k$ provides about whether the input was $P$ or $Q$, given the outputs of channels $1, \ldots, k-1$.

### Step 3: Conditional reduction via correlation

Define the **residual information ratio** for channel $k$:

$$r_k := \frac{D_{KL}\!\left(P_{Y_k \mid Y_{<k}, Q} \;\big\|\; P_{Y_k \mid Y_{<k}, P}\right)}{\eta_{\max} \cdot \Delta}$$

For the first channel: $r_1 \leq 1$ (direct SDPI).

For $k \geq 2$: conditioning on $Y_{<k}$ partially "explains" the variation in $Y_k$ due to the shared input perturbation. When $Y_k$ is correlated with $Y_{<k}$, the previous outputs already carry most of the perturbation signal, reducing $Y_k$'s conditional contribution.

Concretely, in the compound symmetric setting (all pairwise MI equal to $I_0$), the conditional KL for channel $k$ given $Y_{<k}$ reflects the **residual uncertainty** after removing the information already extracted by earlier channels. The Gaussian analysis (Step 4) shows this residual is governed by $\exp(-2 \, I_0)$.

### Step 4: Gaussian compound symmetric derivation

Consider the canonical model: $Y_k = X + \sqrt{\rho} \, Z + \sqrt{1-\rho} \, \varepsilon_k$ where $Z, \varepsilon_k \sim \mathcal{N}(0,1)$ i.i.d., $X \sim \mathcal{N}(\mu, \sigma_X^2)$, and $\rho \in [0,1]$ is the shared-noise fraction.

**Conditional covariance** of $(Y_1, \ldots, Y_K)$ given $X$:

$$\Sigma_{ij \mid X} = \begin{cases} 1 & i = j \\ \rho & i \neq j \end{cases} = (1-\rho) \, I + \rho \, \mathbf{1}\mathbf{1}^\top$$

**Joint KL divergence** under mean shift $\mu \to \mu'$, $\Delta\mu = \mu' - \mu$:

$$D_{KL}\!\left(P_{Y^K \mid Q} \;\big\|\; P_{Y^K \mid P}\right) = \frac{(\Delta\mu)^2}{2} \cdot \mathbf{1}^\top \!\left[({\sigma_X^2 + \rho}) \, \mathbf{1}\mathbf{1}^\top + (1-\rho) \, I\right]^{-1}\! \mathbf{1}$$

By the Sherman–Morrison formula:

$$\mathbf{1}^\top \Sigma_{\text{total}}^{-1} \mathbf{1} = \frac{K}{(1-\rho) + K(\sigma_X^2 + \rho)}$$

The **exact** joint SDPI constant:

$$\eta_{\text{joint}} = \frac{K \, \sigma_X^2}{(1-\rho) + K(\sigma_X^2 + \rho)}$$

Dividing by $\eta_{\text{single}} = \sigma_X^2 / (\sigma_X^2 + 1)$ gives the **exact** effective channel count:

$$K_{\text{eff}}^{\text{exact}} = \frac{K \, (\sigma_X^2 + 1)}{(1-\rho) + K(\sigma_X^2 + \rho)}$$

### Step 5: Deriving the proposed upper bound

In the Gaussian model, the conditional mutual information:

$$I(Y_i; Y_j \mid X) = -\tfrac{1}{2} \log(1 - \rho^2) \implies \exp(-2 \, I_0) = 1 - \rho^2$$

We claim $K_{\text{eff}}^{\text{exact}} \leq 1 + (K-1)(1-\rho^2)$, which is the proposed $K_{\text{eff}}$ when $I_{\max} = I_0$.

**Proof of the upper bound**: Set $e = \exp(-2 \, I_0) = 1 - \rho^2 \in [0,1]$ and $a = 1 - e = \rho^2$. We need:

$$\frac{K}{1 + (K-1) \, a \cdot g(\sigma_X^2)} \leq 1 + (K-1)(1-a)$$

where $g$ absorbs the SNR dependence. It suffices to show $K \leq [1 + (K-1)a][1 + (K-1)(1-a)]$.

Expanding the RHS:

$$[1 + (K-1)a][1 + (K-1)(1-a)] = 1 + (K-1) + (K-1)^2 a(1-a) = K + (K-1)^2 a(1-a) \geq K$$

since $(K-1)^2 a(1-a) \geq 0$ for $a \in [0,1]$, $K \geq 1$. $\square$

The bound is tight at the boundaries: $a = 0$ gives $K_{\text{eff}} = K$ (independent), $a = 1$ gives $K_{\text{eff}} = 1$ (fully correlated).

**Remark on the MI quantity**: The above uses $I(Y_i; Y_j \mid X)$ (conditional on input). When using the unconditional $I(Y_i; Y_j)$—which also includes correlation through the shared signal $X$—the bound remains valid because $I(Y_i; Y_j) \geq I(Y_i; Y_j \mid X)$, so $\exp(-2 \, I(Y_i; Y_j)) \leq \exp(-2 \, I(Y_i; Y_j \mid X))$, giving a (possibly looser but still valid) upper bound on $K_{\text{eff}}$.

---

## Corollary: K_eff Interpretation

### Formula

$$K_{\text{eff}} = 1 + (K-1) \cdot \exp(-2 \, I_{\max}) = \underbrace{\exp(-2I_{\max})}_{\text{independence factor}} \cdot K + \underbrace{(1 - \exp(-2I_{\max}))}_{\text{redundancy}}$$

$K_{\text{eff}}$ decomposes $K$ judges into an "effective independent count" that discounts the redundancy from correlated judges.

### Properties

1. **Monotonicity in $I_{\max}$**: $\partial K_{\text{eff}} / \partial I_{\max} = -2(K-1) \exp(-2I_{\max}) \leq 0$. More correlation → fewer effective channels.

2. **Affine in $K$**: For fixed $I_{\max}$, $K_{\text{eff}} = \alpha + (1-\alpha)K$ where $\alpha = 1 - \exp(-2I_{\max}) \in [0,1]$. Adding a judge increases $K_{\text{eff}}$ by $\exp(-2I_{\max}) < 1$: diminishing returns under correlation.

3. **Marginal gain of diversity**: $\partial K_{\text{eff}} / \partial I_{\max} \big|_{I_{\max}=0}$ = $-2(K-1)$. Near-independence amplifies K strongly; reducing $I_{\max}$ from small values has disproportionate benefit.

4. **Compound symmetric upper bound**: $K_{\text{eff}} \geq K_{\text{eff}}^{\text{exact}}$ (the true effective count from the Gaussian model). The gap is $O((K-1)^2 a(1-a))$ where $a = 1 - \exp(-2I_{\max})$, maximized at $a = 1/2$ ($I_{\max} = \frac{1}{2}\ln 2 \approx 0.35$).

### Numerical examples

| $K$ | $I_{\max}$ | $\exp(-2I_{\max})$ | $K_{\text{eff}}$ | Interpretation |
|-----|-----------|-------------------|-----------------|---------------|
| 5   | 0         | 1.0               | 5.0             | Fully independent |
| 5   | 0.35      | 0.50              | 3.0             | Moderate correlation |
| 5   | 1.0       | 0.14              | 1.5             | High correlation |
| 5   | 2.0       | 0.018             | 1.07            | Near-clones |
| 10  | 0.35      | 0.50              | 5.5             | 10 judges ≈ 5.5 effective |
| 20  | 0.35      | 0.50              | 10.5            | Half efficiency |

---

## Connection to Manipulation Resistance

### From information bound to attack cost

The parallel SDPI bound limits the total distinguishability the attacker can create at the panel's output:

$$D_{KL}\!\left(W^{(K)} Q \;\big\|\; W^{(K)} P\right) \leq K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta$$

By Pinsker's inequality, the total variation between attacked and honest output distributions:

$$\text{TV}\!\left(W^{(K)} Q, \, W^{(K)} P\right) \leq \sqrt{\frac{K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta}{2}}$$

For the attacker to flip the panel verdict with probability $\geq 1 - \delta$, they need $\text{TV} \geq 1 - 2\delta$, giving:

$$\boxed{\Delta \geq \frac{2(1-2\delta)^2}{K_{\text{eff}} \cdot \eta_{\max}}}$$

### The defense gap: additive information vs. exponential concentration

The information bound alone gives a **constant** (in $K$) lower bound on the perturbation cost — not an improving defense. The true defense emerges from the interaction between the SDPI bound and the **concentration of the majority vote**.

**Majority vote concentration**: For $K_{\text{eff}}$ effectively independent judges each with accuracy $p > 1/2$, by Hoeffding's inequality:

$$\Pr[\text{incorrect verdict}] \leq \exp\!\left(-2 K_{\text{eff}} \left(p - \tfrac{1}{2}\right)^2\right)$$

**Under attack**: The attacker's perturbation shifts each judge's accuracy from $p$ to at most $p' = p - \text{TV}(W_k Q, W_k P)$. By Pinsker applied per-channel:

$$p' \geq p - \sqrt{\frac{\eta_{\max} \cdot \Delta}{2}}$$

For the verdict to flip **reliably** against this concentration, the attacker needs $p' < 1/2$, AND the majority vote of $K_{\text{eff}}$ independent coins at rate $p'$ must produce a wrong answer. This requires:

$$\sqrt{\frac{\eta_{\max} \cdot \Delta}{2}} > \left(p - \frac{1}{2}\right) - O\!\left(\frac{1}{\sqrt{K_{\text{eff}}}}\right)$$

The $O(1/\sqrt{K_{\text{eff}}})$ correction arises from the concentration width. In other words, the attacker must not just cross the $p = 1/2$ boundary — they must **clear it by $\Omega(1/\sqrt{K_{\text{eff}}})$** to overcome the vote concentration.

**The defense structure**:

| Component | Scales as | Role |
|-----------|----------|------|
| Attacker's total info budget | $O(K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta)$ | Linear in $K_{\text{eff}}$ |
| Per-judge accuracy shift | $O(\sqrt{\eta_{\max} \cdot \Delta})$ | Independent of $K$ |
| Votes needed to flip | $\lceil K/2 \rceil$ | Linear in $K$ |
| Concentration barrier | $\exp(-\Omega(K_{\text{eff}}))$ | Exponential in $K_{\text{eff}}$ |

The gap: the attacker's per-perturbation leverage on each judge is **fixed** ($\sqrt{\eta_{\max} \cdot \Delta}$, independent of $K$). But the probability that this fixed leverage flips the majority **decays exponentially** in $K_{\text{eff}}$. To maintain a constant attack success rate, the attacker must increase $\Delta$ as $\Omega(\log K_{\text{eff}})$.

More precisely, for attack success probability $\geq 1 - \delta$ with $\delta$ constant:

$$\Delta \geq \frac{2\left(p - \frac{1}{2}\right)^2}{\eta_{\max}} + \frac{c \cdot \log(1/\delta)}{\eta_{\max} \cdot K_{\text{eff}}}$$

The first term is the threshold to cross $p = 1/2$; the second is the additional cost to overcome concentration. The defense improves with $K_{\text{eff}}$ through the **concentration term**, not through the information bound alone.

### Summary of the defense argument

1. **SDPI**: Each judge's output shift is bounded by $\eta_{\max} \cdot \Delta$ (contraction).
2. **Parallel composition**: The total panel information gain is $\leq K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta$ (sublinear due to correlation).
3. **Voting concentration**: Flipping the majority of $K_{\text{eff}}$ independent votes requires the perturbation to clear the accuracy margin **plus** the concentration width $\Omega(1/\sqrt{K_{\text{eff}}})$.
4. **Manipulation cost**: $\Delta = \Omega\!\left(\frac{(p - 1/2)^2}{\eta_{\max}}\right)$, with the success probability of sub-threshold attacks decaying as $\exp(-\Omega(K_{\text{eff}}))$.

The parallel setting gives a **polynomial** (not exponential) information gain for the attacker, but the majority vote's exponential concentration creates the defense gap.

---

## Open Questions

1. **Tight $K_{\text{eff}}$ for non-Gaussian channels**: The proposed $K_{\text{eff}} = 1 + (K-1)\exp(-2I_{\max})$ is an upper bound tight for Gaussians. For discrete-output LLM judges (Likert scores, binary verdicts), the true $K_{\text{eff}}$ may be tighter. Can we derive distribution-specific bounds using the hypercontractivity ribbon (Polyanskiy & Wu, 2016)?

2. **Empirical estimation of $I_{\max}$**: $I(Y_i; Y_j)$ between LLM judge outputs needs estimation from finite samples. With discrete scores and limited evaluation instances, the plug-in MI estimator has high variance. Investigate: (a) nearest-neighbor MI estimators, (b) lower bounds via classifier-based variational MI, (c) correlation as a proxy (rank correlation → MI via copula).

3. **Heterogeneous $\eta_k$**: The bound uses $\eta_{\max}$, but judges may have widely varying contraction coefficients. A tighter bound via $\sum_k \eta_k \cdot r_k$ (weighted by residual ratios) could give a more informative $K_{\text{eff}}$.

4. **Adaptive attacks**: The current analysis assumes the attacker commits to a single $Q$ (static perturbation). Adaptive attacks that choose different perturbations per judge (if judges can be queried independently) break the parallel model. Bound the cost of adaptive strategies.

5. **Beyond majority vote**: For weighted aggregation (e.g., confidence-weighted average), the concentration argument changes. The effective defense may be stronger or weaker depending on the weight structure and its interaction with $K_{\text{eff}}$.

6. **Experimental validation (MVP)**:
   - Fix $K = 5$ diverse LLM judges. Estimate pairwise $I(Y_i; Y_j)$ on a held-out evaluation set.
   - Compute predicted $K_{\text{eff}}$. Compare against empirical "effective sample size" from bootstrap analysis of verdict stability.
   - Test manipulation: apply systematic perturbations to inputs and measure how many judges flip, comparing to the $K_{\text{eff}}$-based prediction.
