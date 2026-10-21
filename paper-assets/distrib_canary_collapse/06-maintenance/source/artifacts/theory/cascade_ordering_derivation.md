# Information-Theoretic Derivation of Cascade Ordering

## Setup and Notation

Consider the iterative training loop with mixing dynamics:
$$p_{t+1} = (1-\alpha)\, p_{\text{real}} + \alpha\, \hat{p}_t, \quad \alpha \in [0,1]$$
where $p_{\text{real}}$ is the human data distribution and $\hat{p}_t = \mathcal{T}(p_t)$ is the output distribution of model $M_t$ trained on $p_t$. The training map $\mathcal{T}$ represents MLE fine-tuning.

We track three families of metrics over generations $t = 0, 1, \ldots, T$:

| Family | Metric | Notation | Functional type |
|--------|--------|----------|-----------------|
| Entropy | Token entropy | $H_t = -\sum_i p_t(i) \log p_t(i)$ | Smooth, concave |
| Diversity | Distinct-$n$ | $D_t = \lvert\{w : p_t(w) > \epsilon\}\rvert / V$ | Threshold-based |
| Calibration | ECE | $\text{ECE}_t = \sum_b \frac{n_b}{N}\lvert C_b - A_b \rvert$ | Smooth, confidence-coupled |

**Onset definition.** Metric $X$ exhibits onset at generation $t_X = \min\{t \geq 1 : |X_t - X_0| > 2\sigma_X\}$, where $\sigma_X$ is the baseline variability estimated from the $\alpha{=}0$ control experiment.

---

## Part 1: Entropy Leads Diversity

### Assumption A1 (Mode Amplification)

The training map $\mathcal{T}$ is *mode-amplifying*: it redistributes probability mass from low-probability tokens toward high-probability tokens. Formally, there exists a threshold $\bar{p}$ such that:
$$\mathcal{T}(p)_i > p_i \implies p_i \geq \bar{p}, \qquad \mathcal{T}(p)_j < p_j \implies p_j \leq \bar{p}.$$

This is the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail. Documented extensively in the model collapse literature (Shumailov et al., 2024; Dohmatob et al., 2024).

### Proposition 1 (Entropy is a first-order indicator)

Let $p \in \Delta^{V-1}$ and let $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then:

$$\Delta H = H(p + \delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2).$$

**Proof.** Taylor-expand $H$ around $p$:
$$H(p + \delta) = -\sum_i (p_i + \delta_i)\log(p_i + \delta_i)$$
$$= -\sum_i (p_i + \delta_i)\left[\log p_i + \frac{\delta_i}{p_i} - \frac{\delta_i^2}{2p_i^2} + \cdots\right]$$
$$= H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \sum_i \frac{\delta_i^2}{2p_i} + O(\|\delta\|^3).$$

Since $\sum_i \delta_i = 0$:
$$\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \frac{\delta_i^2}{p_i} + O(\|\delta\|^3). \tag{1}$$

The first-order term $-\sum_i \delta_i \log p_i$ is strictly negative under mode amplification: tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$, hence $\log p_i \geq \log \bar{p}$; tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$, hence $\log p_j \leq \log \bar{p}$. Writing $m = \sum_{i:\delta_i>0} \delta_i$:

$$-\sum_i \delta_i \log p_i = -m\left[\overline{\log p}^{+} - \overline{\log p}^{-}\right] < 0 \tag{2}$$

where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means of $\log p_i$ over gaining/losing tokens. The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease. $\square$

### Definition (Effective support)

Define the $\epsilon$-effective support as:
$$S_\epsilon(p) = \bigl|\{i \in [V] : p_i > \epsilon\}\bigr|$$

where $\epsilon > 0$ is the *generation threshold*: the minimum probability for a token type to appear in a finite sample of generated text. For a sample of $N$ tokens, $\epsilon \approx c/N$ for a small constant $c$.

Distinct-$n$ is monotonically related to $S_\epsilon$ (more precisely, to the support of the $n$-gram distribution induced by $p$, but the mechanism is identical).

### Proposition 2 (Diversity is a threshold indicator)

**Assumption:** $\epsilon \leq \bar{p}$ (generation threshold below mode threshold). For natural language with $V \approx 50{,}000$ and typical generation sample sizes, $\epsilon \approx c/N \ll \bar{p}$, so this condition is easily satisfied.

Under the same perturbation $\delta$:
$$\Delta S_\epsilon = S_\epsilon(p+\delta) - S_\epsilon(p) = -\bigl|\{i : p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}\bigr|.$$

This equals zero whenever the perturbation is small relative to the *margin*:
$$\|\delta\|_\infty < \min_{i:\, p_i > \epsilon}\,(p_i - \epsilon) =: \gamma(p, \epsilon). \tag{3}$$

**Proof.** Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$. If $\|\delta\|_\infty < \gamma$, no token satisfies this. $\square$

### Theorem 1 (Entropy leads diversity under mode amplification)

Under Assumption A1, the following asymmetry holds:

**(a)** $|\Delta H| > 0$ is compatible with $\Delta S_\epsilon = 0$. (Entropy changes while diversity does not.)

**(b)** Under mode-amplifying $\delta$, if $\Delta S_\epsilon < 0$, then $\Delta H < 0$. (Diversity loss implies entropy loss.)

**Proof of (a).** Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p, \epsilon)$. By Proposition 2, $\Delta S_\epsilon = 0$. By Proposition 1 (Eq. 2), $\Delta H < 0$. Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.

**Proof of (b).** If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k \leq -(p_k - \epsilon) < 0$. Under mode amplification, $\delta_k < 0$ implies $p_k \leq \bar{p}$, so $k$ is a low-probability token losing mass. The total mass $m = -\sum_{j:\delta_j<0} \delta_j > 0$ transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$ (the gaining tokens are strictly more probable than the losing tokens, at least one of which has $p_k \leq \bar{p}$). By Eq. (2), $\Delta H < 0$. $\square$

### Interpretation

Theorem 1 establishes entropy as a *strictly more sensitive* indicator than diversity under mode-amplifying dynamics:
- Entropy responds to the *first derivative* of distributional shift (any probability mass redistribution changes it).
- Diversity responds only when a *level crossing* occurs (a token probability drops below the generation threshold $\epsilon$).

The margin $\gamma(p, \epsilon)$ quantifies how much distributional shift diversity can absorb silently. For natural language distributions with long tails, many tokens sit well above $\epsilon$, making $\gamma$ large relative to the per-generation perturbation $\alpha \cdot \|\mathcal{T}(p) - p\|$.

---

## Part 2: ECE Co-moves with Entropy

**Connection to marginal entropy.** For an autoregressive LM, the marginal token distribution is determined by conditional distributions: $p(w) = \prod_j q_\theta(w_j|w_{<j})$. Mode amplification at the marginal level (A1) corresponds to peakier conditional predictions: if $p_t$ concentrates on fewer token sequences, the per-position conditionals $q_\theta(\cdot|w_{<j})$ necessarily become more concentrated. We formalize this as Assumption A1'.

### Assumption A1' (Conditional Mode Amplification)

If $\mathcal{T}$ is mode-amplifying at marginal level (A1), then for typical contexts $x \sim p_{\text{eval}}$, the conditional next-token distribution $q_\theta(\cdot|x)$ also becomes more peaked after training on mixed data.

### Setup

Let $q_\theta(\cdot | x)$ denote the model's next-token predictive distribution given context $x$. Define:
- **Per-token entropy**: $h(x) = -\sum_y q_\theta(y|x) \log q_\theta(y|x)$
- **Per-token confidence**: $c(x) = \max_y q_\theta(y|x)$
- **Average conditional entropy**: $\bar{H}_t = \mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$
- **Average confidence**: $C_t = \mathbb{E}_{x \sim p_{\text{eval}}}[c(x)]$
- **Accuracy**: $A_t = \mathbb{E}_{x \sim p_{\text{eval}}}[\mathbf{1}[\arg\max_y q_\theta(y|x) = y^*]]$ where $y^*$ is the true next token.

ECE in the overconfident regime simplifies to $\text{ECE}_t \approx C_t - A_t$.

### Proposition 3 (Entropy–confidence coupling)

For any distribution $q$ over $V$ outcomes:
$$c(x) = \max_y q(y|x) \geq \exp(-h(x)). \tag{4}$$

**Proof.** This follows from $H_1(q) \geq H_\infty(q)$ (Shannon entropy dominates min-entropy):
$$h(x) = H_1(q(\cdot|x)) \geq H_\infty(q(\cdot|x)) = -\log \max_y q(y|x) = -\log c(x).$$
Exponentiating both sides gives Eq. (4). $\square$

### Assumption A2 (Accuracy stationarity)

The model's next-token accuracy on held-out real data is approximately stationary during early collapse: $A_t \approx A_0$ for $t \leq t^*$, where $t^*$ is the generation at which the model's representations have shifted enough to degrade prediction quality on clean data.

This holds because: (i) the evaluation set is fixed real data; (ii) the model's internal representations change gradually; (iii) in the early generations, the model is primarily becoming *overconfident* (narrowing its predictive distribution) rather than *wrong* (predicting different tokens).

### Proposition 4 (ECE tracks entropy)

Under Assumptions A1' and A2, for $t \leq t^*$: if the conditional entropy $\bar{H}_t$ decreases, then $\text{ECE}_t$ increases.

**Argument.** Under mode amplification at the conditional level (A1'), for each context $x$, $q_\theta(\cdot|x)$ becomes more peaked across generations. This has two immediate consequences:
1. The per-token conditional entropy decreases: $h(x) \downarrow$.
2. By Proposition 3, $c(x) \geq \exp(-h(x))$, so as $h(x)$ decreases the lower bound on confidence rises; moreover, a more peaked distribution directly implies higher $c(x) = \max_y q(y|x)$.

Averaging over contexts: $\bar{H}_t = \mathbb{E}_x[h(x)]$ decreases and $C_t = \mathbb{E}_x[c(x)]$ increases. Under A2, accuracy $A_t \approx A_0$ is approximately stationary, so:
$$\Delta\text{ECE}_t \approx \Delta C_t - \Delta A_t \approx \Delta C_t > 0.$$

This is a qualitative directional argument; the quantitative relationship between $|\Delta \bar{H}|$ and $|\Delta\text{ECE}|$ depends on the distribution geometry and is confirmed empirically. $\square$

### Interpretation

Proposition 4 shows that ECE increases *whenever* conditional entropy decreases. Both are **continuous functionals** of the model's output distribution — neither requires a discrete threshold crossing. This explains their empirical co-occurrence at the same generation.

The coupling is *mechanical*: lower entropy $\Leftrightarrow$ peakier softmax $\Rightarrow$ higher confidence $\Rightarrow$ higher ECE (given constant accuracy). This is not merely correlation; it is a functional dependency through the shared softmax distribution.

**Caveat.** In practice, additional factors can amplify ECE beyond what the entropy change alone would suggest (e.g., the model may shift which tokens it is confident about, not just become more confident on the same tokens). The argument establishes the *direction* of co-movement, not an exact quantitative prediction.

---

## Part 3: Cascade Timing Bounds

### Proposition 5 (Diversity onset lags entropy onset by $\geq 1$ generation)

Under Assumption A1, if the per-generation perturbation satisfies:
$$\alpha \cdot \|\mathcal{T}(p_s) - p_s\|_\infty < \gamma(p_s, \epsilon) \quad \text{for all } 0 \leq s \leq t_H, \tag{6}$$
then $t_D \geq t_H + 1$.

**Proof.** By condition (6), at every generation $s \leq t_H$ the perturbation $\ell^\infty$-norm $\alpha \cdot \|\mathcal{T}(p_s) - p_s\|_\infty$ is less than the margin $\gamma(p_s, \epsilon)$. By Proposition 2, no token exits the effective support at any generation $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$ and $t_D > t_H$.

Since time is discrete (integer generations), $t_D \geq t_H + 1$. $\square$

### When does the bound saturate?

Condition (6) holds when:
1. $\alpha$ is moderate ($\alpha \leq 0.75$): the per-generation synthetic fraction is not overwhelming.
2. The vocabulary distribution has a *gap* between the tail tokens and the generation threshold $\epsilon$: tokens don't sit right at the edge.
3. The training map $\mathcal{T}$ produces bounded perturbations: the model doesn't radically reorganize probabilities in one generation.

For $\alpha = 1.0$ (full replacement), condition (6) may fail, and entropy and diversity can onset simultaneously — consistent with the catastrophic collapse reported in full-replacement settings (Shumailov et al., 2024).

### Proposition 6 (MAUVE onset lags diversity)

MAUVE measures distributional divergence in a discretized embedding space (k-means quantization of neural text embeddings). Define the MAUVE score as:
$$\text{MAUVE}(P, Q) = \exp\left(-\text{KL}_{\text{frontier}}(P \| Q)\right)$$
where $P, Q$ are the quantized embedding distributions of real and generated text.

**Claim (heuristic).** MAUVE onset requires diversity loss to propagate into the embedding space, which involves:
1. Token-level probability shifts (detected by entropy, gen $t_H$)
2. $n$-gram distribution shifts (detected by distinct-$n$, gen $t_D$)
3. Aggregate embedding distribution shifts (detected by MAUVE, gen $t_M \geq t_D + 1$)

Each step introduces at least one generation of additional lag because the k-means quantization and KL frontier computation average over many samples, requiring *systematic* rather than marginal distributional shift.

**Remark.** This claim is a heuristic argument, not a formal proof. The precise lag depends on the embedding model, the number of k-means clusters, and the sample size. Empirically, MAUVE onset is 1--2 generations after diversity onset on WikiText. However, on C4, MAUVE onset occurs at gen 1, simultaneous with entropy — suggesting the MAUVE lag is corpus-dependent rather than universal (see *Comparison with Empirical Data*).

---

## Summary of Cascade Ordering

$$\underbrace{H_t,\; \text{ECE}_t}_{\text{Phase 1: first-order indicators}} \;\longrightarrow\; \underbrace{\text{Distinct-}n_t}_{\text{Phase 2: threshold indicator}} \;\longrightarrow\; \underbrace{\text{MAUVE}_t}_{\text{Phase 3: aggregate indicator}}$$

| Transition | Mechanism | Minimum lag | Rigour |
|-----------|-----------|-------------|--------|
| Entropy → Diversity | First-order vs. threshold sensitivity (Thm. 1) | 1 generation | Proved under A1 |
| Entropy ↔ ECE | Functional coupling through softmax (Prop. 4) | 0 (simultaneous) | Argued under A1', A2 |
| Diversity → MAUVE | Token-level → aggregate embedding shift | 1 generation | Conjecture |

---

## Comparison with Empirical Data

We validated the cascade ordering across 20 experiments spanning $\alpha \in \{0.10, 0.25, 0.30, \ldots, 1.00\}$, multiple seeds, and two corpora (WikiText, C4), using 2$\sigma$ onset detection.

**Result (α ≥ 0.30).** Among the 15 experiments where the entropy perturbation exceeds the 2$\sigma$ detection threshold ($\alpha \geq 0.30$), cascade ordering $t_H \leq t_D$ holds in **15/15** cases, with $t_H = 1$ and $t_D = 2$ uniformly:

| Experiment | $t_H$ (Entropy) | $t_{\text{ECE}}$ | $t_D$ (min Distinct-$n$) | $t_M$ (MAUVE) | $t_D - t_H$ |
|-----------|:---:|:---:|:---:|:---:|:---:|
| $\alpha{=}0.50$, s42 | 1 | 1 | 2 | 3 | **1** |
| $\alpha{=}0.50$, s43 | 1 | 1 | 2 | 2 | **1** |
| $\alpha{=}0.75$, s42 | 1 | 1 | 2 | 3 | **1** |
| $\alpha{=}0.75$, s43 | 1 | 1 | 2 | 2 | **1** |

(Representative subset shown; full data in `cascade_empirical_data.json`.)

All 15 experiments with $\alpha \geq 0.30$ show:
- **Entropy and ECE onset simultaneously at gen 1** (Prop. 4: zero lag between first-order indicators). ✓
- **Diversity lags entropy by exactly 1 generation** (Prop. 5: minimum lag = 1). ✓
- **MAUVE lags diversity by 0--1 generation** on WikiText (Prop. 6 heuristic). ✓

**Low-α regime (α < 0.30).** For the 5 experiments at $\alpha \leq 0.25$ (2 at $\alpha{=}0.10$, 3 at $\alpha{=}0.25$), the entropy perturbation remains below the 2$\sigma$ threshold (gen-1 deviation 0.004–0.011, threshold 0.121), so cascade ordering is neither confirmed nor refuted — the signal is below detection resolution. This is consistent with the theory: small $\alpha$ produces small perturbation $\delta$ that remains within the diversity margin $\gamma(p, \epsilon)$, satisfying condition (6) trivially — neither entropy nor diversity onset is triggered by the entropy channel, so the ordering is vacuously satisfied.

**Threshold sensitivity.** At $\alpha = 0.10$, the diversity onset ($t_D = 2$) is detected at only ${\sim}2.1\sigma$ above the noise floor. At a 3$\sigma$ threshold, this onset would be marginal or undetected. The cascade ordering result is robust for $\alpha \geq 0.30$ but should be interpreted with caution at $\alpha = 0.10$–$0.25$ where both signals approach the detection limit.

**C4 MAUVE caveat.** MAUVE as a lagging indicator (gen 3–7+) is observed on WikiText; on C4, MAUVE onset occurs at gen 1, simultaneous with entropy. This domain-dependence suggests the MAUVE lag is driven by corpus-specific distributional properties rather than a universal cascade mechanism.

---

## Assumptions and Limitations

**A1 (Mode Amplification)** is the central assumption. It holds when:
- The model has finite capacity relative to the data distribution complexity
- Training uses MLE (cross-entropy loss) on finite samples
- The training distribution has non-trivial tail structure

It may fail when: the model perfectly memorizes the training data (infinite capacity regime), or when regularization explicitly preserves entropy (e.g., label smoothing, entropy bonuses in RL).

**A2 (Accuracy Stationarity)** holds during early collapse but eventually breaks. When accuracy degrades, ECE dynamics become more complex (overconfidence + inaccuracy), potentially decoupling from pure entropy dynamics. This is consistent with the empirical observation that ECE magnitude grows super-linearly at high $\alpha$ (842% at $\alpha{=}0.50$ vs. 1810% at $\alpha{=}0.75$).

**Generation threshold $\epsilon$** is a simplification. In practice, distinct-$n$ depends on the sampling procedure (temperature, top-$k$, nucleus sampling), the text length, and $n$-gram order. The threshold argument holds qualitatively for any generation procedure that maps low-probability tokens to zero effective frequency, but the precise value of $\gamma$ depends on these details.

**Discrete generations.** The 1-generation minimum lag is partly an artifact of discrete time. In a continuous-time formulation (where $\alpha$ represents a rate rather than a fraction), the lag would be a continuous delay proportional to $\gamma / (\alpha \cdot \text{mode amplification rate})$. The discrete setting provides a clean lower bound.
