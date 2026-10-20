# Mechanistic Explanation: Phase-Dependent Interaction in Compound Sparsity

## 1. Entropy–Discrimination Collapse Under Head Pruning

The core mechanism driving importance eviction's disproportionate degradation in compound settings is an **entropy–discrimination feedback loop**. When attention heads are pruned, the surviving heads must absorb the representational burden of the removed heads, causing their attention distributions to become more diffuse (higher entropy). UNComp (Xiong et al., EMNLP 2025) formally demonstrates that matrix entropy quantifies the effective information capacity of attention patterns, and higher entropy corresponds to lower discriminability among token importance scores. AhaKV (2025) independently shows that when attention entropy is high, the scale of softmax must be adaptively tuned to recover meaningful importance rankings — without such correction, standard attention-score-based importance metrics degenerate.

This degeneration is phase-dependent. During low-sparsity reasoning phases — where the model explores multiple reasoning paths and attention is naturally more uniform [MEASURED: our II data shows low-phase has highest compound penalty] — head pruning pushes already-diffuse attention distributions past a critical entropy threshold where importance scores lose their ranking fidelity. The result is that importance-based eviction selects tokens based on near-random score differences, but with **systematic positional and structural biases** inherited from the softmax geometry (e.g., attention sinks, causal position bias). This "biased pseudo-random" selection is strictly worse than true random eviction, which at least treats all tokens equiprobably [HYPOTHESIS, supported by DefensiveKV (ICLR 2026) showing mean aggregation is "inherently fragile" and vulnerable in extreme cases, and by the Greedy Bias paper (2026) showing single-metric importance has systematic blind spots for structurally relevant tokens].

During high-sparsity phases — where the model converges on an answer and attention concentrates on a small set of critical tokens — importance scores retain high discrimination even after head pruning, because the surviving heads still produce sharply peaked attention patterns [HYPOTHESIS, consistent with Thinking Tokens MI paper (NeurIPS 2025) showing MI peaks are sparse (<5% of steps) and correspond to convergent reasoning moments]. Hence, importance eviction functions correctly in these phases, and the compound penalty is small.

**Evidence level summary:** The entropy–discrimination link is [LITERATURE: UNComp, AhaKV, DefensiveKV]. The phase-dependent attention uniformity is [MEASURED: our II gradient data]. The "biased pseudo-random worse than true random" claim is [HYPOTHESIS: logically follows from DefensiveKV fragility + Greedy Bias findings, but not directly measured in compound setting].

## 2. Gradient Amplification Through Cascading Overload

The phase gradient (low/high II ratio) increases monotonically with sparsity level — 12.8× at s=0.15 vs. 52.9× at s=0.25 [MEASURED] — because **higher sparsity amplifies the entropy–discrimination collapse nonlinearly**. At s=0.25, more heads are pruned than at s=0.15, meaning each surviving head must absorb a larger share of the removed heads' functions. This additional load pushes the attention entropy in low-sparsity phases even further past the discrimination threshold, while high-sparsity phases — where attention was already concentrated — are more resilient to head removal (the "important" heads tend to survive importance-based pruning).

This asymmetric resilience creates a widening gap: as overall sparsity increases, the high-phase II grows roughly linearly (0.205 → 0.584, ~2.8×), but the low-phase II grows super-linearly (2.627 → 30.903, ~11.8×) [MEASURED]. The mechanism is analogous to the phase transition phenomenon documented by Ma et al. (npj Artificial Intelligence 2026): each compression dimension has an independent phase transition point (PTP), and operating near the PTP produces sharply nonlinear degradation. In the low-sparsity reasoning phase, the compound of head pruning + KV eviction pushes the system closer to (or past) its effective PTP, while in the high-sparsity phase the system remains in the safe zone. Higher overall sparsity s moves the low-phase operating point further into the critical region, explaining the gradient's super-linear growth.

Additionally, token importance recurrence (LazyEviction, 2025) exacerbates this: tokens that are temporarily unimportant during exploration phases may become critical later. Importance eviction in compound settings — where discrimination is already degraded — is especially prone to irreversibly evicting such recurring tokens, creating compounding errors as generation proceeds [LITERATURE: LazyEviction, RetentiveKV's "deferred importance" phenomenon].

**Evidence level summary:** Gradient magnitude and monotonicity are [MEASURED]. The cascading overload mechanism is [HYPOTHESIS, supported by phase transition theory from Ma et al.]. Token importance recurrence as an amplifier is [LITERATURE: LazyEviction, RetentiveKV].

## 3. Super-Additivity From Circular Dependency

Compound sparsity is super-additive (II > 0 at all phases) [MEASURED] because head pruning and KV cache eviction create a **circular dependency** that neither compression alone introduces. Head pruning alters the attention patterns that importance-based eviction relies on for its scoring signal; simultaneously, KV cache eviction removes tokens that the remaining heads need for context. SLiM (Mozaffari et al., ICML 2025) formally proves that compound compression error is non-additive — the cross-term between pruning error and quantization/eviction error cannot be eliminated by independent optimization. The Compression Ordering study (2025) further shows this interaction is directional: the error from applying compression A first, then B, differs from B-then-A, because early-stage compression creates "information shadows" that distort subsequent importance estimation.

In our setting, the circular dependency manifests as: (1) pruned heads cannot compensate for evicted tokens by redistributing attention, because they no longer exist; (2) evicted tokens cannot provide contextual grounding for the remaining heads' computations. This bidirectional loss has no counterpart when either compression is applied alone. The super-additive penalty is positive at all phases because even in high-sparsity phases (where importance eviction is well-calibrated), the absence of pruned heads means the model has strictly fewer degrees of freedom to route around evicted tokens [HYPOTHESIS, consistent with SLiM's non-additive error theory and SparK's (AAAI 2026) empirical finding of 65% compound degradation with ThinK+SnapKV].

**Evidence level summary:** Super-additivity at all phases is [MEASURED]. Non-additive error theory is [LITERATURE: SLiM, Compression Ordering]. The circular dependency mechanism is [HYPOTHESIS, consistent with SparK empirical results].

## 4. Random Baseline: The Absence of Systematic Bias

If random eviction also produces super-additive compound effects but with a smaller phase gradient, this would confirm that the **large gradient is specific to importance-based methods' discrimination failure**, not an inherent property of compound sparsity geometry. Random eviction, by definition, has no systematic bias — it does not preferentially evict tokens near any decision boundary, nor does it inherit softmax-geometric artifacts. The Surprising Effectiveness of Randomness (ICLR 2025) demonstrates that random pruning is competitive with importance-based methods at low compression ratios precisely because it avoids the systematic errors that importance metrics introduce.

In compound settings, random eviction's "honest ignorance" means its error is uniformly distributed across phases, producing a flatter gradient. The super-additivity would still exist (the circular dependency from §3 applies regardless of eviction strategy), but without the entropy–discrimination collapse amplifying the low-phase penalty. A smaller random gradient would thus constitute evidence that: (a) the phase-dependent II pattern is driven by importance metric failure rather than architectural fragility; (b) phase-gated strategy switching (importance in high-sparsity phases, random or hybrid in low-sparsity phases) could substantially reduce the compound penalty [HYPOTHESIS, pending random baseline r2 results for s=0.15 and s=0.25].

NACL (ACL 2024) provides indirect support: its hybrid importance+random eviction strategy implicitly acknowledges that pure importance eviction is suboptimal in certain regimes, though it applies the mixture uniformly rather than phase-conditionally. Ada-KV (NeurIPS 2025) shows that dispersed-attention heads require larger budgets, suggesting that the problematic regime (high entropy, low discrimination) is already recognized as needing special treatment — our contribution is identifying that this regime is **phase-localized** in reasoning models and that **compound compression makes it dramatically worse**.

**Evidence level summary:** Random gradient prediction is [HYPOTHESIS, pending data]. Random effectiveness at low ratios is [LITERATURE: Surprising Effectiveness of Randomness]. Phase-localization of the problematic regime is [MEASURED + HYPOTHESIS].

---

## Key References

| Paper | Venue | Role in Narrative |
|-------|-------|-------------------|
| UNComp (Xiong et al.) | EMNLP 2025 | Matrix entropy → sparsity discrimination theory |
| DefensiveKV (FFY et al.) | ICLR 2026 | Importance stability assumption is fragile |
| Greedy Bias (2026) | arXiv | Single-metric importance has systematic blind spots |
| Thinking Tokens MI (2025) | NeurIPS 2025 | MI peaks sparse (<5%), phase-localized in reasoning |
| SLiM (Mozaffari et al.) | ICML 2025 | Compound compression error formally non-additive |
| Phase Transitions (Ma et al.) | npj AI 2026 | Independent PTPs per compression dimension |
| Compression Ordering (2025) | arXiv | Interaction direction depends on ordering |
| LazyEviction (2025) | arXiv | Token importance recurrence phenomenon |
| RetentiveKV (2026) | arXiv | Deferred importance — early-low, late-critical tokens |
| SparK | AAAI 2026 | 65% compound degradation empirical evidence |
| Surprising Effectiveness of Randomness | ICLR 2025 | Random competitive at low ratios, avoids systematic bias |
| NACL | ACL 2024 | Hybrid importance+random, implicit acknowledgment |
| Ada-KV | NeurIPS 2025 | Dispersed heads need larger budgets |
| AhaKV (2025) | arXiv | Softmax scale must adapt to entropy for discrimination |
| RaaS | ACL 2025 | Token importance non-monotonic across decoding phases |
