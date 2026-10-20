---
dream_id: dream_20260515T004704
tier: best
overall_score: 4 (Weak Accept)
timestamp: 2026-05-15T01:58:59.433373+00:00
---


# Reviewer 2 (R2): Novelty, Positioning, Related Work, and Clarity

**Paper:** "Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"

**Focus:** Novelty, positioning, related work, and writing quality

---

## Summary

This paper presents a factorial diagnostic analysis of why variable-rate imagination (dt>1) fails in DreamerV3. Through controlled ablations across four DMC environments, it identifies a causal chain: trained duration embeddings enable the critic to exploit imprecise multi-step RSSM predictions, producing systematic value overestimation (measured via a "normalized value-eval ratio" or nve) that stochastically leads to catastrophic collapse. The paper proposes restricting imagination to dt=1 while retaining multi-dt training data as a zero-cost mitigation recovering ~95% baseline performance. The diagnostic marker (nve > 1.5x) achieves 18/18 classification accuracy across three primary environments.

---

## Strengths

- **Genuinely informative C6 finding.** The most novel insight is that trained dt-embedding + dt=1 imagination succeeds (94.8% baseline) while trained dt-embedding + dt>1 imagination collapses. This pinpoints the failure to imagination-time exploitation rather than the embedding's existence or training data composition. The implication -- that representing temporal abstractions is not the same as safely planning with them -- is a conceptually sharp distinction that goes beyond standard model exploitation narratives.

- **Precise "necessary but not sufficient" framing of stochastic collapse.** Rather than hiding the stochasticity (4/9 collapse rate), the paper makes it a first-class finding. The distinction between sustained vs. transient nve>1.5x as the second gate for collapse is scientifically honest and more defensible than a deterministic claim. This framing connects naturally to the primacy bias and early-training stochasticity literature.

- **Factorial design provides clean causal isolation.** The 008d vs 008f vs 008a vs 008e_v3 comparison matrix systematically isolates factors. The three-way comparison (trained embedding + dt>1 imagination = collapse; no embedding + dt>1 = degraded but stable; trained embedding + dt=1 imagination = 95% baseline) is more methodologically rigorous than typical ablation studies in MBRL papers.

- **Cross-environment replication is convincing.** 18/18 classification accuracy across Walker, Cheetah, and Cartpole, with environment-dependent collapse severity correlated to RSSM prediction error, supports an architecture-level rather than task-specific phenomenon. The inclusion of Hopper Hop (5/6) as a harder supplementary case is appropriate and honest.

- **Actionable practical recommendation.** The C6 mitigation requires zero architecture change and zero computational overhead. This is genuinely useful for practitioners working with variable-dt training data in DreamerV3 or similar systems.

---

## Weaknesses

### Major

1. **Incremental novelty over known MBRL failure modes.** Value overestimation from model exploitation is thoroughly established (Thrun & Schwartz 1993; Janner et al. 2019 MBPO; Pan et al. 2020). The general principle -- that a learned conditioning signal can exploit model imprecision -- is a predictable instantiation of this known failure class. The paper's contribution is identifying the *specific pathway* (dt-embedding mechanism) and providing a *diagnostic marker* (nve), but the conceptual surprise is limited. The paper should explicitly frame itself as "identifying a specific new instance of a known failure class" rather than implying a fundamentally new phenomenon. Currently the framing oscillates between these two positions.

2. **Critically thin related work section.** The paper cites only ~16 references. For a diagnostic analysis paper whose value depends on precise positioning against prior knowledge, this is a serious gap. Critical missing discussions:

   - **TAWM (Nhu et al., ICML 2025):** This is the single most important missing reference. TAWM explicitly conditions a world model on dt and shows it *succeeds* in TD-MPC2. The contrast -- dt-conditioning works in MPC but fails in imagination-based actor-critic -- is the strongest argument for the paper's novelty. Without citing TAWM, the paper cannot make its most compelling case for why the finding is surprising.
   
   - **THICK (Gumbsch et al., ICLR 2024) and Hieros (Mattes et al., ICML 2024):** Hierarchical temporal abstraction in Dreamer-family models that avoids flat dt-embedding. These demonstrate the field's convergent solution (hierarchy) to the problem this paper diagnoses. Not citing them leaves a gap in the "what should practitioners do instead" discussion.
   
   - **LS-Imagine (Li et al., ICLR 2025 Oral):** Extends Dreamer imagination horizon via goal-conditioned jumps. Concurrent work on the same core problem (short-sighted Dreamer imagination) using a different mechanism (goal conditioning vs. dt-embedding). Must be cited for completeness.
   
   - **Time-discretization invariance (Tallec et al. 2019; Park et al. 2021):** Theoretical foundations for why variable dt is fundamentally difficult in RL. These would strengthen the theoretical grounding of the paper's findings.
   
   - **DreamSmooth (Lee et al., ICLR 2024) / HarmonyDream (Ma et al., ICML 2024):** Reward prediction as an MBRL bottleneck. Directly relevant to the 75x reward MAE explosion in the dt_embed_dim=0 ablation.
   
   - **MTS3 (Shaj et al., NeurIPS 2023):** Multi-time-scale state space model for variable-rate prediction. Relevant foundational architecture for multi-rate dynamics.
   
   - **Frauenknecht et al. (ICLR 2025):** On rollout quality in MBRL -- directly supports the finding that imagination at dt>1 produces corrupted data.
   
   - **DreamerV4 (Hafner & Yan 2025):** Replaces RSSM with transformer. The paper should discuss whether the identified failure mode is RSSM-specific or would persist in transformer world models.

3. **"Delusional critic" terminology is misleading.** Lu et al. (2018) define delusional bias precisely: it arises when function approximation + policy-class constraints create Bellman backups that no realizable policy can achieve. The mechanism here is fundamentally different -- it is model imprecision amplified by learned temporal conditioning, producing overestimated values for trajectories the agent *can* execute but the model *cannot accurately predict*. This is closer to "model exploitation" (Janner et al. 2019) than "delusional bias" (Lu et al. 2018). Using "delusional critic" risks: (a) confusing readers familiar with the Lu et al. definition, (b) implying a theoretical connection that does not hold, and (c) inviting reviewer pushback on terminological imprecision. **Recommendation:** Use "conditioning-induced value overestimation" or "model-exploitation via temporal conditioning" as the primary term. Cite Lu et al. as an analogy but clearly differentiate.

4. **Post-hoc nve threshold without sensitivity analysis.** The nve > 1.5x at 35K+ threshold was calibrated and evaluated on the same data. No held-out validation, no cross-validation, and no sensitivity analysis is provided. The Hopper miss (peak 1.42x, just below 1.5x) already demonstrates threshold fragility. With only 3 seeds per condition, a single additional miss would drop accuracy from 100% to 94%. The paper should report accuracy across a range of thresholds (1.3x, 1.5x, 1.7x) and discuss the AUROC or similar threshold-free metric.

### Minor-to-Moderate

5. **Single-environment C6 validation.** The C6 mitigation is the paper's most actionable contribution, yet it is validated with 3 seeds in Walker Walk only. The paper frames it as architecture-level guidance. Without at least one additional environment, the practical recommendation is undersupported. The Limitations section acknowledges this but it remains a significant gap.

6. **Confounded causal control.** The dt_embed_dim=0 ablation simultaneously removes the hypothesized mechanism AND degrades reward prediction by 75x. The paper acknowledges this (Section 4.5, RSSM fidelity table) but still claims a "closed causal chain." The C6 finding (trained dt_emb + dt=1 = success) partially compensates, but the chain from "dt_embedding causes overestimation" relies on a confounded control. "Strongly supported causal chain" would be more accurate than "closed."

7. **Zero figures in a dynamics-diagnostic paper.** The paper is entirely tables and text. Learning curves, nve trajectories over training, embedding divergence plots, and the classification scatter would dramatically improve both readability and persuasiveness. The temporal dynamics patterns central to the narrative (V-recovery zigzag, sustained vs. transient overestimation, entropy reversal) cannot be conveyed through tables. This is a significant presentation weakness for a venue like CoRL.

---

## Questions for Authors

1. **TAWM contrast:** TAWM (Nhu et al. 2025) shows dt-conditioning succeeds in TD-MPC2. Can you articulate precisely why imagination-based actor-critic training is uniquely vulnerable? Is it the lack of online MPC correction that grounds value estimates in reality, the single critic (vs. ensemble), or a structural difference in how dt-conditioning interacts with the training objective?

2. **Threshold selection:** What is the nve classification accuracy at thresholds of 1.3x and 1.7x? Was 1.5x selected via any principled criterion (e.g., maximizing separation), or was it chosen post-hoc? Would a threshold-free metric (AUROC on nve as a continuous predictor of trained vs. untrained dt_emb) be more appropriate?

3. **Delusional vs. exploitative:** The paper uses "delusional critic" but the mechanism seems closer to model exploitation (Janner et al. 2019). In Lu et al.'s framework, delusion arises from policy-class constraints making certain backups unrealizable. Here the backups are realizable but based on inaccurate model predictions. Can you justify why "delusional" is more appropriate than "exploitative" or "overoptimistic"?

4. **Transformer world models:** DreamerV4 replaces RSSM with a transformer. Would the identified failure mode persist? The RSSM's autoregressive compounding is central to your causal chain -- if a transformer world model has lower dt>1 prediction error, does the mechanism disappear? This would clarify whether the finding is RSSM-specific or generalizes.

5. **Partial ablation:** Have you considered detaching dt_embedding gradients from the critic only (while allowing the world model to train with it)? This would isolate critic exploitation from reward prediction degradation without the 75x MAE confound.

6. **C6 cross-environment:** Is there any C6 data for Cheetah or Cartpole? Even preliminary (1 seed) would substantially strengthen the practical recommendation.

7. **Connection to model predictive control literature:** The paper focuses on imagination-based training, but the broader MBRL community includes MPC approaches (TD-MPC2, PETS) where multi-step prediction errors are handled differently. How does your finding inform the choice between imagination-based and MPC-based planning in world-model RL?

---

## Minor Issues

- **Title breadth:** "Why Temporal Abstraction Fails" implies generality beyond what the study supports (DreamerV3 only, DMC only, dt in {1,2}). Consider "Why Variable-Rate Imagination Fails in DreamerV3" or "Diagnosing Value Overestimation from Duration Embedding in DreamerV3."

- **Abstract precision:** "four DMC environments" includes Hopper Hop where accuracy is 83%, not 100%. The abstract should note that the 100% accuracy claim applies to three primary environments.

- **Table density:** 14 tables in the main text is excessive. Several could be merged or moved to an appendix (e.g., Tables 8, 11, 14).

- **Notation:** dt_emb uses both `dt\_\text{emb}` and "duration embedding" and "dt-embedding" inconsistently. Standardize.

- **Missing error bars/CIs:** Several tables report point estimates without confidence intervals (e.g., Cheetah and Cartpole in Table 1 show individual seeds but Hopper shows only IQM -- inconsistent presentation).

- **Section 4.10 (actor entropy):** Described in text only with no table or figure. The entropy reversal pattern is a key piece of evidence for the mechanism and deserves visualization.

- **The paper would benefit from a causal diagram figure** showing the hypothesized chain: trained dt_emb -> RSSM fidelity gap exploitation -> reward bias -> value overestimation -> actor gradient corruption -> collapse. Currently this is described verbally in the Discussion but a visual would make the argument much more accessible.

- **Reference formatting:** Some references lack venue information or use inconsistent formats (e.g., "arXiv preprint" vs. conference name).

---

## Significance Assessment

The paper addresses a real question (why does temporal abstraction fail in world-model RL?) and provides a genuine answer with practical value. The C6 recommendation is immediately useful. However, the significance is bounded by three factors:

1. **Limited surprise:** Most MBRL researchers would predict that learned conditioning on an imprecise model dimension leads to exploitation. The specific mechanism is new; the general principle is not.

2. **Narrow scope:** DreamerV3 + DMC + dt in {1,2}. The paper is careful about scoping claims, which is appropriate, but it limits impact.

3. **Defensive rather than constructive:** The paper tells practitioners what *not* to do (don't use dt>1 imagination with trained dt_emb) and what to do instead (use dt=1). This is valuable but the community would benefit more from understanding *how to make dt>1 imagination work* -- the uncertainty-gated pilot hints at this but is underdeveloped.

Would this change practitioner behavior? For the small community working on temporal abstraction in Dreamer-family models, yes. For the broader MBRL community, the diagnostic methodology (nve as overestimation marker) and the general lesson (learned conditioning amplifies model exploitation) may have moderate impact.

---

## Preliminary Score and Confidence

**Score: 4 (Weak Accept)**

The factorial design is rigorous, the C6 finding is genuinely informative, the stochastic collapse framing is scientifically honest, and the cross-environment replication is convincing. These are above-average strengths for a diagnostic paper.

However, the thin related work (especially missing TAWM, THICK, LS-Imagine), the misleading "delusional critic" terminology, the absence of figures, the post-hoc threshold without sensitivity analysis, and the single-environment C6 validation prevent a confident accept. The novelty is incremental over known MBRL failure modes, though the specific mechanism and diagnostic marker add value.

With expanded related work (especially the TAWM contrast, which would actually *strengthen* the novelty argument), 2-3 key figures, threshold sensitivity analysis, and at least one additional C6 environment, this would be a solid accept.

**Confidence: 4/5**

I am confident in the assessment of novelty (incremental but real), related work gaps (clear omissions), and terminology concerns. I am slightly less certain about the significance assessment -- the value of diagnostic papers is inherently harder to evaluate than method papers, and the nve marker + C6 recommendation may prove more useful to the community than I currently estimate.

---

## Revision Priority (ordered)

1. **Expand related work:** Add TAWM (critical -- strengthens your novelty), THICK, Hieros, LS-Imagine, DreamSmooth, MTS3, Tallec 2019, Frauenknecht 2025. This is the single highest-impact revision because TAWM transforms the novelty narrative from "we found a specific instance of known failure" to "dt-conditioning succeeds in MPC but fails in imagination -- here's why."

2. **Add 2-3 figures:** nve trajectories over training (showing sustained vs. transient), learning curves overlay, classification scatter. Essential for a dynamics-diagnostic paper.

3. **Fix terminology:** Replace "delusional critic" with "conditioning-induced value overestimation" or similar. Cite Lu et al. as analogy but explicitly differentiate.

4. **Threshold sensitivity:** Report accuracy at 1.3x, 1.5x, 1.7x. Consider AUROC.

5. **Cross-environment C6:** Run at least Cheetah C6 (2 seeds minimum).

6. **Soften causal chain language:** "Strongly supported" rather than "closed" given the dt_embed_dim=0 confound.
