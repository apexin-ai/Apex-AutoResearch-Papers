# Analysis: Connecting Depth Signal to Distributional Collapse

This section provides an analytical framework that connects our empirical findings to the theory of recursive distributional collapse. We formalize recursive generation as an iterated distributional mapping, derive conditions under which adjacent depths become statistically indistinguishable, and explain why depth signal existence depends on the model's capacity to memorize its training data.

## Notation and Setup

Let $P_0$ denote the original (human-authored) text distribution. At each generation step $n$, a language model $M_n$ is trained on samples from $P_n$, producing a new distribution $P_{n+1}$ through autoregressive sampling. We write this recursive process as a distributional mapping $\mathcal{T}$:

$$P_{n+1} = \mathcal{T}(P_n) = \text{Sample}(M_n), \quad M_n = \text{Train}(P_n).$$

The mapping $\mathcal{T}$ depends on three components: the model architecture, the training procedure, and the decoding strategy (nucleus sampling, temperature scaling, or top-$k$ truncation). We treat $\mathcal{T}$ as a deterministic operator on distributions in the limit of infinite samples, following the idealized framework of Shumailov et al. (2024) and Alemohammad et al. (2024).

For a text $x$ and a reference language model $M_{\text{ref}}$, let $s(x) = -\log p_{M_{\text{ref}}}(x_t \mid x_{<t})$ denote the token-level surprisal sequence. Our 19-dimensional feature vector $\phi(x)$ consists of statistics computed from $s(x)$, including perplexity percentiles (p10, p50, p90), surprisal moments (mean, variance, skewness), $n$-gram entropies, and repetition ratios. The population-level feature distribution at depth $n$ is $\Phi_n = \phi_\#(P_n)$, the pushforward of $P_n$ through the feature map.


## 5.1 Why Perplexity Tail Statistics Track Generation Depth

Our experiments consistently identify $\texttt{p90\_ppl}$ (90th-percentile perplexity) and $\texttt{var\_surprisal}$ (surprisal variance) as the top-ranked features for depth discrimination across all nine model-strategy combinations. This finding has a natural explanation in terms of distributional tail collapse.

**Tail trimming under recursive generation.** Shumailov et al. (2024) establish that recursive training causes "tails of the original content distribution to disappear." The mechanism is straightforward: a language model trained on finite samples from $P_n$ underestimates low-probability events, because rare tokens in $P_n$ appear infrequently (or not at all) in the training corpus. The resulting model $M_n$ assigns near-zero probability mass to these rare events, so $P_{n+1}$ has thinner tails than $P_n$. Dohmatob et al. (2024) formalize this for Zipf-distributed token frequencies with exponent $\beta$: under temperature $\tau$, the effective tail exponent becomes $\beta/\tau$, while under top-$p$ or top-$k$ truncation, the tail is cut entirely beyond a threshold $k \asymp T_0^{1/\beta}$ determined by the training sample size $T_0$.

This tail trimming directly explains the dominance of $\texttt{p90\_ppl}$. The 90th-percentile perplexity measures the reference model's surprisal at the high end of the token difficulty distribution. Tokens that $P_0$ generates with moderate but non-negligible probability (the "outer shell" of the distribution's support) become progressively rarer under $P_1, P_2, \ldots$ as each recursive step trims the tails further. Consequently, text sampled from $P_n$ contains fewer high-surprisal tokens, and $\texttt{p90\_ppl}$ decreases monotonically with depth. By contrast, central-tendency statistics like $\texttt{mean\_ppl}$ are less sensitive because the bulk of the distribution changes slowly: the first few moments of $P_n$ are dominated by high-probability tokens that survive across generations.

**Surprisal variance as a concentration measure.** The monotonic decrease of $\texttt{var\_surprisal}$ with depth reflects a complementary phenomenon: distributional concentration. As recursive training removes tail tokens, the remaining token distribution becomes more peaked. A model trained on $P_n$ produces text where token-level surprisals are more uniform (concentrated around the mean), because the model has higher confidence on a narrower vocabulary. Formally, if $P_n$ is supported on a set $S_n$ with $S_0 \supset S_1 \supset S_2 \supset \cdots$, then the entropy $H(P_n)$ decreases monotonically, and the variance of the surprisal distribution $\text{Var}_{x \sim P_n}[s(x)]$ decreases as the support shrinks and probability mass concentrates.

This analysis explains why $\texttt{p90\_ppl}$ and $\texttt{var\_surprisal}$ form a complementary pair: the former captures tail erosion (what disappears), while the latter captures distributional concentration (what remains). Together, they provide a two-dimensional summary of the collapse trajectory that is more informative than any single statistic. Our empirical monotonicity correlations ($\rho = -0.82$ to $-0.89$ between these features and depth) quantify the strength of this monotone relationship across all tested configurations.

**Connection to the Depth Degradation Atlas.** The non-uniform spacing we observe in the Atlas (depth $0 \to 1$ gap far exceeding depth $2 \to 3$ gap) also follows from the tail-trimming framework. The initial step $P_0 \to P_1$ produces the largest distributional shift because $P_0$ has the richest tail structure, and the first round of finite-sample training removes the most probability mass from rare events. Subsequent steps operate on already-trimmed distributions, so each incremental shift is smaller. This produces a concave decay in inter-depth feature distances, consistent with our pairwise AUC trajectory: $\text{AUC}(d_1, d_2) = 0.953$, $\text{AUC}(d_2, d_3) = 0.862$, $\text{AUC}(d_3, d_4) = 0.766$.


## 5.2 Effective Discriminable Depth: An Upper Bound

We now formalize the notion of Effective Discriminable Depth (EDD) and derive conditions under which it is finite.

**Definition.** The EDD with respect to a feature map $\phi$ and a discrimination threshold $\alpha$ is

$$\text{EDD}(\phi, \alpha) = \max \{ n \geq 1 : \text{AUC}(\Phi_{n-1}, \Phi_n) \geq \alpha \},$$

where $\text{AUC}(\Phi_{n-1}, \Phi_n)$ is the area under the ROC curve for distinguishing samples from the feature distributions at depths $n-1$ and $n$.

**Fixed-point attractor.** Recursive generation converges to a fixed distribution under mild conditions. Alemohammad et al. (2024) show that autophagous generative loops converge to a fixed point $P^*$ where $\mathcal{T}(P^*) = P^*$, characterized by either precision loss (mode drift) or recall loss (mode collapse) depending on sampling bias. Marchi et al. (2024) prove this more formally using stochastic approximation: for any non-identity temperature, the generative distribution converges to a degenerate attractor, either a point mass (for $\tau < 1$) or a uniform distribution over a subset (for $\tau > 1$). The existence of such a fixed point $P^*$ implies $\lim_{n \to \infty} D_{\text{KL}}(P_n \| P_{n+1}) = 0$, which in turn implies $\lim_{n \to \infty} \text{AUC}(\Phi_n, \Phi_{n+1}) = 0.5$ (chance level).

**Contraction argument.** To bound EDD, we model the inter-depth KL divergence as a contracting sequence. Let $\delta_n = D_{\text{KL}}(P_n \| P_{n+1})$. If the mapping $\mathcal{T}$ is $\gamma$-contractive in KL divergence for some $\gamma \in (0, 1)$, meaning

$$\delta_{n+1} \leq \gamma \cdot \delta_n,$$

then by induction $\delta_n \leq \gamma^n \cdot \delta_0$, where $\delta_0 = D_{\text{KL}}(P_0 \| P_1)$ is the initial divergence between the human distribution and first-generation output.

The AUC between adjacent feature distributions is bounded by a function of their KL divergence. By the data processing inequality, $D_{\text{KL}}(\Phi_n \| \Phi_{n+1}) \leq D_{\text{KL}}(P_n \| P_{n+1}) = \delta_n$, and as KL divergence decreases, TV decreases (Pinsker: $\text{TV} \leq \sqrt{\text{KL}/2}$), which in turn implies AUC approaches 0.5 (since $\text{AUC} \leq 0.5 + \text{TV}$). When $\text{TV}$ becomes small enough, the AUC approaches 0.5.

Specifically, the AUC drops below threshold $\alpha$ when the total variation (or, equivalently, when no univariate projection of the feature distributions achieves sufficient separation). Setting $\text{AUC}(\Phi_n, \Phi_{n+1}) \geq \alpha$ requires $\delta_n$ to exceed some minimum $\delta_{\min}(\alpha, \phi)$ that depends on the threshold and the feature map's resolving power. This yields:

$$\text{EDD}(\phi, \alpha) \leq \left\lfloor \frac{\log(\delta_0 / \delta_{\min})}{\log(1/\gamma)} \right\rfloor.$$

This bound decomposes EDD into three interpretable factors:

1. **Initial divergence $\delta_0$**: How much the first generation differs from the original. Larger $\delta_0$ (e.g., from aggressive memorization of training data) provides a larger "budget" of distinguishability. Our training loss data confirms large initial shifts: Pythia nucleus loss drops from 2.27 (depth 0) to 1.37 (depth 1), indicating substantial distributional change.

2. **Contraction rate**: How quickly successive depths converge. Faster contraction yields lower EDD. The concave AUC decay profile we observe ($0.953 \to 0.862 \to 0.766 \to 0.683$) shows non-uniform contraction in AUC-excess (AUC $- 0.5$), with the contraction ratio decreasing from 0.80 to 0.69 across successive pairs (accelerating convergence).

3. **Feature resolution $\delta_{\min}$**: The minimum divergence that the feature map $\phi$ can resolve. Richer feature spaces (more dimensions, better-chosen statistics) achieve smaller $\delta_{\min}$, potentially extending EDD. This explains why our 19-dimensional feature vector yields EDD $= 4$ while a single feature (e.g., mean perplexity alone) would yield EDD $= 2$ or $3$.

**Empirical calibration.** With the observed AUC decay and $\alpha = 0.75$, our data gives EDD $= 4$ across all three model families. The binary AUC at the boundary, $\text{AUC}(d_3, d_4) \in [0.750, 0.784]$, clusters tightly around the threshold, while $\text{AUC}(d_4, d_5) \in [0.681, 0.684]$ falls uniformly below it. The consistency of EDD $= 4$ across three architectures (Pythia-1.4B, GPT-2 XL, OLMo-1B) suggests that the contraction rate $\gamma$ and initial divergence $\delta_0$ are determined primarily by the shared recursive training protocol rather than by architecture-specific factors.

**Caveat on rigor.** The $\gamma$-contraction assumption is a simplification. In practice, the mapping $\mathcal{T}$ may not satisfy uniform contraction across the entire distributional space, and the relationship between KL divergence and AUC in high-dimensional feature spaces involves constants that depend on the specific distributions. The bound above should be read as an order-of-magnitude argument explaining why EDD is $O(\log(\delta_0/\delta_{\min}))$ rather than as a tight numerical prediction. A fully rigorous treatment would require characterizing the Jacobian of $\mathcal{T}$ at the fixed point $P^*$, which we leave to future theoretical work.


## 5.3 Memorization as a Prerequisite for Depth Signal

Our experiments reveal a striking dependency: depth signal exists only when the model memorizes its training data to a sufficient degree. Under temperature $\tau = 1.1$, the four-depth classification accuracy drops to near chance, while $\tau = 0.5$ and $\tau = 0.9$ produce strong signal (70-85% accuracy). The training loss trajectory explains this pattern.

**The memorization mechanism.** At each recursive step, the depth signal is generated by the distributional shift $P_n \to P_{n+1}$. This shift occurs because the trained model $M_n$ differs from the data distribution $P_n$ in systematic ways: specifically, $M_n$ assigns higher probability to patterns it has memorized and lower probability to rare events it has underfit. The magnitude of this shift determines the strength of the depth signal at step $n$.

Training loss quantifies the degree of memorization. When $M_n$ achieves low training loss on samples from $P_n$, it has learned (and partially memorized) the distribution, so $P_{n+1} = \text{Sample}(M_n)$ differs substantially from $P_n$. Conversely, when training loss remains high, $M_n$ has failed to capture the fine-grained structure of $P_n$, so $P_{n+1} \approx P_n$ and little depth signal is produced.

**Temperature controls memorization through gradient magnitude.** Temperature $\tau$ scales the logits $z_i$ before softmax: $p_i \propto \exp(z_i / \tau)$. The text sampled at temperature $\tau$ from $P_n$ determines the training distribution for $M_n$. At high temperature ($\tau > 1$), the sampling distribution is flattened toward uniform, producing training text with high entropy and low redundancy. The model trained on such data cannot reduce its cross-entropy loss substantially, because the target distribution itself has high entropy. Our data confirms this: at $\tau = 1.1$, training loss decreases only from 2.27 to 1.91 (depth 0 to depth 1) and then to 1.85 (depth 2), a near-plateau. At $\tau = 0.5$, training loss drops from 2.27 to 0.42 to 0.16, indicating progressively stronger memorization at each depth.

Formally, the KL divergence between the sampling distribution and the trained model satisfies:

$$D_{\text{KL}}(P_n^{(\tau)} \| P_{n+1}^{(\tau)}) \propto L_{\text{train}}^{(n,0)} - L_{\text{train}}^{(n, T_{\text{steps}})},$$

where $L_{\text{train}}^{(n,0)}$ is the initial training loss at depth $n$ and $L_{\text{train}}^{(n, T_{\text{steps}})}$ is the loss after training. The depth signal at step $n$ is proportional to this gap. When $\tau$ is large, $L_{\text{train}}^{(n,0)}$ is already close to the entropy floor of the high-temperature distribution, leaving little room for the gap to grow.

**Connection to Dohmatob et al.'s tail narrowing.** The tail-narrowing framework provides a complementary perspective. Under temperature $\tau$, the effective Zipf exponent changes from $\beta$ to $\beta/\tau$ (Dohmatob et al., 2024). For $\tau > 1$, this produces a heavier tail (smaller exponent), which might appear to increase diversity. But the interaction with recursive training reverses this intuition: the heavier tail means that rare events in $P_n^{(\tau)}$ are less rare (closer to uniform), so the model trained on $P_n^{(\tau)}$ has less "room" to trim tails. The distributional shift per step is smaller, and depth signal is weaker.

Marchi et al. (2024) formalize the limiting behavior: for $\tau > 1$, the generative distribution contracts toward a uniform distribution over the supported tokens, while for $\tau < 1$, it collapses toward a small set of modes. Both trajectories eventually reach a fixed point, but the path for $\tau > 1$ involves smaller per-step changes (the distribution is already close to uniform), producing weaker depth signal. The path for $\tau < 1$ involves large per-step changes (aggressive mode collapse), producing strong but quickly saturating depth signal. Temperature $\tau \approx 0.9$ occupies an intermediate regime where each recursive step produces a substantial distributional shift without immediate mode collapse, yielding the strongest and most sustained depth signal across our experimental range.

**Implications for depth estimation in practice.** This analysis suggests that depth estimation will be most reliable when the generative model was trained with sufficient capacity and compute to memorize its training data, and when the decoding temperature is below 1.0. These conditions are increasingly common in practice: frontier language models are trained to near-zero training loss, and sampling temperatures in the range $[0.6, 1.0]$ are standard for open-ended generation. The memorization prerequisite therefore does not substantially limit the practical applicability of depth estimation, though it does imply that text generated with very high temperatures or from severely undertrained models may be depth-indistinguishable from its parent generation.


## Summary of Analytical Claims

The framework above yields three testable predictions, all confirmed by our experiments:

1. **Feature ranking prediction**: Tail-sensitive statistics ($\texttt{p90\_ppl}$, $\texttt{var\_surprisal}$) should outperform central-tendency statistics for depth discrimination. Confirmed: these features rank in the top 4 across all 9 settings.

2. **EDD finiteness and scaling**: EDD should scale logarithmically with the ratio of initial divergence to feature resolution, yielding a small constant for practical configurations. Confirmed: EDD $= 4$ across three model families, with tight clustering of boundary AUC values.

3. **Temperature-depth signal interaction**: Depth signal strength should correlate with the training loss gap across depths, which in turn depends on temperature. Confirmed: $\tau = 0.5$ yields loss gap $> 2.0$ and strong signal, $\tau = 1.1$ yields loss gap $< 0.4$ and no signal.


---

**References cited in this section:**

- Shumailov et al. (2024). "AI models collapse when trained on recursively generated data." *Nature*, 631, 755-759.
- Dohmatob et al. (2024). "A Tale of Tails: Model Collapse as a Change of Scaling Laws." *ICML 2024*.
- Alemohammad et al. (2024). "Self-Consuming Generative Models Go MAD." *ICLR 2024*.
- Marchi et al. (2024). "Heat Death of Generative Models in Closed-Loop Learning." *ICASSP 2025*.
- Shi et al. (2025). "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective." *NeurIPS 2025 Spotlight*.
