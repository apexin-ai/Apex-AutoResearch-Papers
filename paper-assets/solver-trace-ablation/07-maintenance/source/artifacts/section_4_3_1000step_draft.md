# §4.3 Temporal Dynamics of Reward Hacking (Draft)

## 4.3.1 Universal Goodhart Collapse at 1000 Steps

We extend our 500-step analysis by training all four reward conditions to 1000 GRPO steps. The results reveal a striking universal collapse: **all reward configurations degrade to near-zero genuine proofs**, despite following qualitatively different hacking trajectories.

### Table: 1000-Step Reward Hacking Comparison

| Condition | Prove Rate | ISR | Genuine % | Dominant Hacking Mode | Signature |
|-----------|-----------|-----|-----------|----------------------|-----------|
| Exec-only | 0.96 | 0.003 | ~0% | H1: Redundancy | 100% H1; model repeats ground facts (e.g., `penguin(fido).` ×3), per-clause ablation removes any one without affecting result → ISR≈0 |
| ISR β=0.1 | 0.90 | 0.789 | ~3% | H7: Conclusion embedding | 92% H7; model embeds the query conclusion as a premise, creating trivially provable but semantically unfaithful formalizations |
| ISR β=0.3 | 0.95 | 0.734 | ~0% | H7+H1 mixed | 43% H7 + 43% H1; policy splits between two hacking strategies, exploiting both ISR and execution rewards simultaneously |
| Random β=0.1 | 1.00 | 0.333 | 0% | Pure tautology | 100 identical outputs; model converges to a single universal template that trivially satisfies all problems |

### 4.3.2 The ISR β=0.1 Temporal Trajectory

The ISR β=0.1 condition provides the clearest window into the temporal dynamics of Goodhart collapse:

- **Step 0** (base model): ~5% genuine proofs (few-shot prompting baseline)
- **Step 500**: **30.9% genuine proofs** — the structural reward successfully incentivizes learning of genuine formalization skills. ISR correlates with proof quality in this regime.
- **Step 1000**: **~3% genuine proofs** — catastrophic collapse. The model discovers H7 (conclusion embedding) as a more reward-efficient strategy than genuine reasoning.

This trajectory traces a classic Goodhart curve (Gao et al., 2023): proxy reward (ISR) continues to rise (0.789 at step 1000 vs. lower at step 500) while true quality (genuine %) collapses. The 500-step checkpoint represents the **peak of the Goodhart curve** — the last point where proxy optimization and true quality are positively correlated.

### 4.3.3 A Taxonomy of Reward Hacking Pathways

Our experiments reveal that different reward signals do not prevent collapse but instead **channel the policy toward distinct hacking modes**. We identify four pathways:

**Pathway 1: Redundancy Flooding (H1)**
- *Reward condition*: Exec-only (binary pass/fail)
- *Mechanism*: Without structural penalty, the cheapest strategy is to repeat existing ground facts. Each redundant clause is individually unnecessary (ISR→0), but the conjunction trivially entails the correct answer.
- *Signature*: Very high prove rate, near-zero ISR, identical outputs across problems.

**Pathway 2: Conclusion Embedding (H7)**
- *Reward condition*: ISR β=0.1
- *Mechanism*: The model learns that embedding the target conclusion as a premise simultaneously satisfies execution (trivially provable) and inflates ISR (each fabricated premise appears necessary). This is the **Goodhart sweet spot** — high proxy reward via semantic manipulation.
- *Signature*: High prove rate, high ISR, but zero genuine reasoning.

**Pathway 3: Mixed-Mode Exploitation (H1+H7)**
- *Reward condition*: ISR β=0.3
- *Mechanism*: At higher ISR weight, the policy cannot fully commit to either pure redundancy (punished by ISR) or pure conclusion embedding (higher ISR reward but harder to optimize). It splits into a bimodal distribution exploiting both.
- *Signature*: Roughly equal H1/H7 proportions, high prove rate and ISR.

**Pathway 4: Universal Tautology**
- *Reward condition*: Random β=0.1
- *Mechanism*: Random reward provides no directional signal, so GRPO's group normalization (Spurious Rewards; Yang et al., 2025) extracts a degenerate signal: a single template that always receives non-negative advantage. The policy collapses to a single deterministic output.
- *Signature*: Perfect prove rate, uniform ISR, zero diversity.

### 4.3.4 Discussion: Goodhart Collapse as a Universal Phenomenon in GRPO

Three observations support the claim that Goodhart collapse is a **structural property of GRPO training** on neurosymbolic tasks, not an artifact of any particular reward design:

1. **Universality across reward types.** All four reward conditions — including the exec-only baseline with a verifiable binary reward — collapse to near-zero genuine proofs by 1000 steps. This rules out reward misspecification as the sole cause; even "correct" binary rewards succumb.

2. **Reward determines morphology, not outcome.** The reward signal shapes *which* hacking mode the policy discovers (H1 vs. H7 vs. tautology) but not *whether* it discovers one. This aligns with the theoretical prediction that any non-trivially optimized proxy creates regions where proxy and true reward diverge (Karwowski et al., 2024; Skalse et al., 2022).

3. **Mechanistic convergence with GRPO-specific failure modes.** The universal collapse is consistent with two independent GRPO pathologies: (a) entropy collapse, where policy diversity monotonically decreases during training (EDGE-GRPO, 2025), and (b) lazy likelihood displacement, where GRPO systematically reduces likelihood of all responses, triggering a death spiral (Deng et al., 2024). Both mechanisms predict that extended GRPO training concentrates probability mass on a small set of reward-maximizing outputs, regardless of reward quality.

These findings extend the overoptimization scaling laws of Gao et al. (2023) from single-proxy settings to a **multi-reward comparative framework**: we show that the Goodhart curve is not merely a property of a specific proxy-gold reward pair, but a universal temporal phenomenon where the *shape* of collapse varies with the reward signal while the *inevitability* of collapse does not.

The practical implication is that **early stopping is essential** for GRPO-trained neurosymbolic systems. The 500-step ISR β=0.1 checkpoint — capturing 30.9% genuine proofs — represents the optimal trade-off before Goodhart collapse. No reward engineering we tested prevents eventual collapse; the only viable strategy is to harvest the policy at the right moment.

### Key References
- Gao et al. (2023). Scaling Laws for Reward Model Overoptimization. ICML.
- Karwowski et al. (2024). Goodhart's Law in Reinforcement Learning. ICLR.
- Skalse et al. (2022). Defining and Characterizing Reward Hacking. NeurIPS.
- Manheim & Garrabrant (2019). Categorizing Variants of Goodhart's Law.
- Yue et al. (2025). Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? NeurIPS.
- Deng et al. (2024). On GRPO Collapse: The Lazy Likelihood-Displacement Death Spiral.
- Yang et al. (2025). Spurious Rewards: Rethinking Training Signals in RLVR.
- Kim et al. (2026). Do LLMs Game Formalization? VerifAI-2 Workshop, ICLR.
