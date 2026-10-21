# Section 3: Method

## 3.1 Problem Setup

Consider a training corpus $\mathcal{D} = \{x_1, \ldots, x_N\}$ drawn from a mixture of human-authored and machine-generated text. An unknown fraction $\pi$ of the documents are synthetic, injected through one or more language model generators whose outputs have entered the data pipeline. We assume access to a pre-trained sample-level detector $f: \mathcal{X} \to [0,1]$ that produces calibrated scores $q(x_i) = \hat{P}(\text{synthetic} \mid x_i)$ for each document. Crucially, we do **not** assume knowledge of the true contamination ratio $\pi$, nor do we require ground-truth provenance labels at training time.

Our goal is to learn a language model on $\mathcal{D}$ that performs as well as possible on the underlying clean (human-authored) distribution, measured by perplexity on a held-out evaluation set containing no synthetic text. The key challenge is determining how aggressively to downweight documents that the detector flags as potentially synthetic, without discarding useful training signal.

## 3.2 Detect-and-Reweight Framework

We adopt the importance weighting scheme introduced by \citet{drayson2025}:
$$w_i = (1 - q(x_i))^b, \quad b \geq 0$$
where $q(x_i)$ is the detector's estimated synthetic probability for document $x_i$ and $b$ is a non-negative exponent controlling the penalty strength. This formulation defines a continuous spectrum from uniform weighting ($b = 0$, all samples treated equally) to hard filtering ($b \to \infty$, only samples with $q \approx 0$ retained).

Each sample's contribution to the training loss is scaled by its normalized weight $\bar{w}_i = w_i / (\frac{1}{N}\sum_j w_j)$, so the weighted cross-entropy objective becomes:
$$\mathcal{L}_{\text{weighted}} = \frac{1}{N} \sum_{i=1}^{N} \bar{w}_i \cdot \ell(x_i; \theta)$$
where $\ell(x_i; \theta)$ is the per-sample cross-entropy loss.

The central question is how to choose $b$. \citet{drayson2025} select $b$ from a discrete grid via validation-based empirical tuning, requiring a held-out set and per-model search. We propose an alternative: deriving $b$ adaptively from the batch statistics themselves, eliminating the need for external validation or prior knowledge of $\pi$.

## 3.3 Adaptive $b^*$ via Effective Authenticity Estimation

**Effective authenticity rate.** We define the effective authenticity rate under weighting parameter $b$ as:
$$\alpha_{\text{eff}}(b) = \frac{\sum_{i=1}^{N} (1 - q_i)^{b+1}}{\sum_{i=1}^{N} (1 - q_i)^{b}}$$

Intuitively, $\alpha_{\text{eff}}(b)$ measures the weighted average "cleanness" of the corpus under the weighting scheme parameterized by $b$. It has three key properties: (i) $\alpha_{\text{eff}}(0) = \frac{1}{N}\sum_i (1 - q_i) = 1 - \hat{\rho}$, the unweighted empirical authenticity rate; (ii) $\alpha_{\text{eff}}(b)$ is monotonically non-decreasing in $b$, since increasing $b$ concentrates weight on samples with higher $(1 - q_i)$; and (iii) $\alpha_{\text{eff}}(b) \to 1$ as $b \to \infty$, reflecting that extreme downweighting retains only the cleanest samples.

**Optimal exponent.** We seek the smallest $b$ that raises the effective authenticity above a target threshold $\tau$:
$$b^* = \inf\{b \geq 0 : \alpha_{\text{eff}}(b) \geq \tau\}$$
subject to a sample efficiency constraint described below. The threshold $\tau$ encodes the desired purity level (see Section 3.4 for selection guidelines). Taking the infimum ensures minimal intervention: we apply only as much downweighting as needed to meet the purity target, preserving training signal from borderline samples.

**Effective sample size constraint.** Aggressive downweighting reduces the effective number of training samples. We quantify this via the effective sample size:
$$\text{ESS}(b) = \frac{\left(\sum_{i=1}^{N} w_i\right)^2}{\sum_{i=1}^{N} w_i^2}$$
which equals $N$ when $b = 0$ (uniform weights) and decreases as $b$ increases. We impose a minimum $\text{ESS}(b^*) \geq n_{\min}$ to ensure stable gradient estimates. When the $\alpha_{\text{eff}}$ threshold and ESS constraint conflict---i.e., reaching $\tau$ would require $b$ so large that $\text{ESS}$ drops below $n_{\min}$---the algorithm returns the $b$ that maximizes $\alpha_{\text{eff}}$ among all ESS-feasible values:
$$b^* = \arg\max_{b \geq 0} \alpha_{\text{eff}}(b) \quad \text{s.t.} \quad \text{ESS}(b) \geq n_{\min}$$

**Algorithm.** We summarize the complete procedure in Algorithm 1.

> **Algorithm 1:** Adaptive $b^*$ Selection
>
> **Input:** Batch scores $\{q_1, \ldots, q_B\}$, threshold $\tau$, minimum ESS $n_{\min}$, upper bound $b_{\max}$
>
> 1. Compute $\alpha_{\text{eff}}(0)$. If $\alpha_{\text{eff}}(0) \geq \tau$, return $b^* = 0$ (batch is sufficiently clean).
> 2. **Grid search:** Evaluate $\alpha_{\text{eff}}(b)$ and $\text{ESS}(b)$ over a fine grid $b \in [0, b_{\max}]$. Track the smallest $b_\tau$ where $\alpha_{\text{eff}}(b_\tau) \geq \tau$, and the best ESS-feasible $b_f = \arg\max_b \alpha_{\text{eff}}(b)$ s.t. $\text{ESS}(b) \geq n_{\min}$. Terminate early if $\text{ESS}(b) < n_{\min}$.
> 3. **Bisection refinement:** If $b_\tau$ was found, refine via bisection (50 iterations) to locate $b^*$ precisely.
> 4. If $\text{ESS}(b^*) \geq n_{\min}$, return $b^*$. Otherwise, return $b_f$.
> 5. Compute weights $w_i = (1 - q_i)^{b^*}$, normalized to sum to $B$.
>
> **Output:** Normalized weights $\{\bar{w}_1, \ldots, \bar{w}_B\}$

**Numerical stability.** All power computations $(1 - q_i)^b$ are performed in log-space as $\exp(b \cdot \log(1 - q_i))$ with log-sum-exp shifting to prevent underflow, and intermediate quantities use double precision.

## 3.4 Practical Considerations

**Per-batch computation.** The exponent $b^*$ is computed independently for each mini-batch from the batch's detector score distribution. No cross-batch state or smoothing is maintained. This design is stateless and trivially parallelizable, though it means $b^*$ may fluctuate across batches depending on the local contamination level. In practice, $b^*$ values vary across batches depending on the local contamination level; concrete distributional statistics are reported in Section 5. [*Pending: $b^*$ distribution statistics from adaptive\_fix experiments*]

**Upper bound.** We impose a hard ceiling $b_{\max} = 20.0$ to prevent degenerate solutions where a single sample dominates the batch. In most batches the ESS constraint binds before $b_{\max}$, though in rare cases ($<0.3\%$) extreme batch compositions cause $b^*$ to reach the ceiling. For these batches, the algorithm returns the largest ESS-feasible $b$, degenerating to fixed aggressive downweighting rather than a principled $b^*$.

**Computational overhead.** The grid search (1,000 evaluations) followed by bisection (50 iterations) involves only scalar reductions over the batch scores. The wall-clock cost is negligible relative to the forward and backward passes of the language model---typically under 1 ms per batch on GPU.

**Threshold setting.** When $\pi$ is approximately known, we set $\tau = 1 - \pi/2$, the midpoint between $\alpha_{\text{eff}}(0) = 1 - \pi$ (no intervention) and $1.0$ (perfect decontamination), as a practical default that balances decontamination strength against information loss. When $\pi$ is unavailable---the common case in web-scale training---$\tau = 0.8$ serves as a robust default that performs well across $\pi \in [0.2, 0.6]$.
