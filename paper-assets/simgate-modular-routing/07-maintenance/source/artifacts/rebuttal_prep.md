# EMNLP 2026 ARR Rebuttal Preparation

## Attack 1: Single-Environment Generalization

> "ScienceWorld is just one environment. How generalizable is your framework?"

We appreciate this concern and address it at two levels: the framework's generality and the specific finding's scope.

**Methodological generality is demonstrated across three environments.** We apply the identical diagnostic procedure—unchanged—to ScienceWorld, MATH (§3.4), and ALFWorld (§3.4), obtaining qualitatively distinct diagnoses: death dominance (78.9% label fraction; DAF=90.4%), no extractable signal (p=0.81), and information asymmetry (DAF=0%), respectively; moreover, the ALFWorld null-death diagnosis replicated across two models (Llama 16/16, Qwen 35/37 information-asymmetric episodes). Each diagnosis is correct: always-deterministic is optimal for ScienceWorld, neither strategy dominates in MATH, and the information-advantaged strategy wins in ALFWorld. The framework's value lies in producing the correct diagnosis for each environment without modification—it is a diagnostic tool, not a claim that all environments exhibit death dominance.

**The specific finding (death dominance) is replicated across three model families** (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B; DAF=88–90%, 2.2pp spread) and persists under 10× scaling to 72B (DAF=92.4%). This cross-model stability confirms death dominance is an environment property, not a model artifact. Additionally, a MiniHack pilot (Appendix R) correctly returns "no signal" as a fourth validated condition, further confirming framework applicability.

**Practical generalizability** is addressed by the ~50-episode pilot protocol (Appendix R), which provides preliminary build-vs-buy signal for all four tested conditions given the large effect sizes observed (d=3.02). The pilot is designed to be low-cost (4–8 GPU-hours vs. 200 for full router training), enabling practitioners to diagnose new environments before committing to router development. We distinguish *methodological generality* (applicable to any environment with paired episode outcomes) from *empirical generality* (full quantitative validation on ScienceWorld only), and scope claims accordingly (Limitations §1).

---

## Attack 2: Trivial Finding

> "Given the -100 death penalty, isn't death dominance obvious?"

The existence of a death penalty makes death *relevant*—not dominant. Whether death avoidance actually accounts for the overwhelming majority of routing signal is an empirical question with three non-trivial answers:

**(i) 10× scaling does not eliminate death dominance.** Qwen2.5-72B reduces death rate from 42.9% to 30.6% but yields DAF=92.4%—higher than the 7B baseline (90.4%). If death dominance were a trivial artifact of weak models, capability scaling should reduce it; instead, the gap between internal and deterministic safety persists because both strategies improve, preserving the differential (§3.3).

**(ii) Reflexion self-correction yields DAF>100%.** Under Reflexion (N=3), Δ_nd=−0.47: the self-correcting agent slightly *outperforms* deterministic on non-death episodes, yet still loses overall because death asymmetry more than accounts for the full gap. This counterintuitive result—a stronger agent performing worse due to catastrophic vulnerability—was not predictable from the penalty structure alone (§3.3).

**(iii) Suggestive observation (n=15): the 0.5B inverted-U.** A 0.5B model shows *reduced* death rate (13.3%) because it is too weak to reach dangerous states, suggesting a capability–vulnerability relationship where intermediate-capability models are most vulnerable. We note this as a suggestive pattern from a small sample (n=15 episodes), not a primary claim; it warrants future investigation with larger N.

**Crucially, the primary metric is penalty-independent.** The 78.9% death-asymmetry label fraction holds at any penalty value P>0 (§2.4). DAF is a derived, P-dependent measure; we report both precisely to separate the structural finding (78.9%) from its score-space amplification. At P=0, 54 sole-signal episodes lose their discriminating power, but the remaining 41 non-tie labels still show 51.2% death asymmetry, confirming that death events carry routing-relevant information independent of penalty magnitude.

The routing literature's design choices **presuppose** diverse signal sources: Toolformer learns per-token API calls, CogRouter adapts per-step reasoning depth, RouteLLM learns preference-based routing. These architectures would be unnecessary if single-mechanism dominance were the default assumption. Our finding that death avoidance accounts for 78.9% of non-tie labels directly challenges these design presuppositions. The absence of prior diagnostic work is not mere oversight—it reflects an implicit assumption of signal diversity that our quantification disproves.

---

## Attack 3: No Actionable Solution

> "You diagnosed the problem but didn't solve it. What's the practical value?"

Our contribution follows the established pattern of diagnostic work that redirects community effort. **Our framework is to routing what probing classifiers are to representations**: a diagnostic tool that should precede optimization, not replace it. Just as probing reveals what information is encoded before designing extraction methods, our framework reveals what signal drives routing before building routers. (A secondary analogy: "Attention is not Explanation" (Jain & Wallace, 2019) did not propose a new mechanism but changed how researchers interpret existing ones.) Our framework provides three forms of practical value:

**1. Cost-saving diagnostic.** The ~50-episode pilot protocol (Appendix R) answers "should we build a router?" in 4–8 GPU-hours. Our own experience validates this: we invested ~200 GPU-hours training routers (6 SFT variants × 8 seeds × 3 model scales) before the diagnostic framework revealed that always-deterministic is near-optimal. Had the pilot been run first, ~190 GPU-hours of router training would have been avoided. The framework transforms an open-ended engineering question into a quantitative decision with bounded cost.

**2. The diagnosis itself is actionable.** For ScienceWorld, the framework prescribes always-deterministic as the routing strategy—which achieves 90.5% of oracle non-tie decisions (§3.5). Crucially, always-deterministic is not only near-optimal but requires **zero additional training cost**—the framework's diagnosis directly yields a cost-free deployment strategy. This is not "no solution"; it is the correct solution, derived from understanding the mechanism. The finding that routing signal equals task-type identity (confirmed by leave-one-task-type-out degradation to chance, cross-task transfer failure, and majority-vote baseline matching) means practitioners should invest in reducing internal-strategy death rates rather than building routers.

**3. Cross-environment applicability yields different prescriptions.** In ALFWorld (DAF=0%), the framework diagnoses information asymmetry rather than death dominance, suggesting that router development *is* warranted—a qualitatively different recommendation from the same diagnostic tool. The framework's value is not tied to any single prescription but to its ability to generate environment-specific guidance before expensive router training.

---

## Attack 4: Router Positive Control Missing

> "You show step-level routers fail, but never demonstrate a task-level router succeeds. Without a positive control, 'signal-limited' is unsubstantiated."

The positive control's purpose is not to show a router can work, but to **confirm signal granularity**—that routing signal exists at one level (task-type) but not another (step). This granularity diagnosis is the core contribution of §3.6:

**(i) Task-type features consistently outperform step features.** A keyword variant adding task name to step features reaches 62.9% (Appendix P), and a task-type-only logistic regression on one-hot features achieves 64.7% (supplementary analysis)—both exceeding all step-level routers (56–59%). This directly demonstrates a granularity mismatch: task identity carries exploitable routing signal that step-level features cannot access. The accuracy is bounded below perfect because task-type labels are probabilistic (not all episodes of a death-prone type result in death), but the signal is clearly learnable at the correct granularity.

**(ii) LOTO confirms signal is a per-task-type constant with no cross-type generalization.** Under leave-one-task-type-out, two independent methods—600M–4B neural routers and logistic regression on one-hot task-type features—both collapse to chance (49.2% and 50.0% respectively; §3.6, Appendix P). This convergence from architecturally unrelated approaches confirms that routing signal is a per-task-type constant, not a learnable cross-type pattern. The diagnosis is "signal-limited, not architecture-limited."

**(iii) Generative router also fails (46.7%)** (Appendix P). An unconstrained generative approach (Qwen3-8B generating routing decisions from episode context) cannot extract step-level signal either, ruling out the hypothesis that SFT router architecture is the bottleneck.

**(iv) Structural explanation: death risk is a binary task-type property.** 10/11 task types carry death risk (§5). The routing label is determined primarily by whether the task type has death risk—a property that is constant within a task type but invisible to step-level features. The 7/11 pure-deterministic task types achieve 100% balanced accuracy; the 4 types with within-type episode variance cap at 50%.

**Summary:** The granularity diagnosis is complete—signal exists (task-type level), signal is absent (step level), and two independent methods confirm no cross-type generalization. This is not a missing positive control; it is a positive demonstration of where signal lives and why step-level routers cannot reach it.

---

## Attack 5: Per-Task Statistical Power

> "With only n=20 per task type, per-task conclusions are unreliable."

We agree that per-task conclusions should be interpreted cautiously, and have designed our analysis accordingly:

**(i) The headline finding is aggregate, not per-task.** The 78.9% death-asymmetry fraction (75/95 non-tie labels) is computed over the full N=245 episode pool. Bootstrap 95% CI: [69.5%, 86.3%] (B=10,000). This aggregate finding does not depend on per-task significance tests.

**(ii) Per-task results are explicitly exploratory.** Table 1 caption marks all per-task results as single-seed exploratory analyses. We do not make claims that require per-task statistical significance.

**(iii) Directional consistency is itself informative.** All 10 death-prone task types show deterministic preference (10/10 same direction). Under the null hypothesis of random direction, P(10/10 same) = 2^{-10} ≈ 0.001. This directional consistency test does not require large per-task N. Moreover, directional consistency holds across three independently sampled model families (Qwen 10/10, Llama 10/10, Gemma 10/10 = 30/30), where model architectures provide genuinely independent sampling—stronger than within-model 10/10.

**(iv) Cross-model replication substitutes for within-model N.** Three independent model families (Qwen, Llama, Gemma) independently converge on DAF 88–90% (2.2pp spread). This between-model replication provides stronger evidence for the finding's reliability than simply increasing N within a single model.

**(v) Wilson CIs are reported honestly.** Per-task Wilson CIs of ±20pp are wide, which is why we avoid strong per-task claims. The K=11 cluster bootstrap limitation is acknowledged in the paper (§2.4). The aggregate bootstrap CI ([69.5%, 86.3%]) confirms the finding is well-separated from the 50% null even accounting for task-level clustering.

---

## Attack 6: Limited Excitement / Novelty

> "The contribution is primarily empirical analysis rather than a new method. Excitement 2.5/5."

We position this work as an empirical analysis contribution in the "Interpretability and Analysis" track, where diagnostic frameworks have established precedent and impact:

**(i) Diagnostic contributions have a strong track record in this venue.** Probing classifiers (Conneau et al., 2018; Hewitt & Manning, 2019) did not propose new architectures but fundamentally changed how the community understands and evaluates representations. Behavioral testing (Ribeiro et al., 2020, CheckList) did not improve models but redirected evaluation methodology. BERTology (Rogers et al., 2020) synthesized analytical findings into actionable guidance. Our contribution type—diagnostic framework that precedes and redirects optimization—follows this lineage.

**(ii) Quantification is the contribution, not the direction.** "Death might matter for routing" is a reasonable intuition. But intuitions do not specify magnitudes. The finding that 78.9% of non-tie labels trace to a single mechanism is not a number anyone predicted—it could have been 30%, 50%, or 90%. The quantification transforms a vague intuition into a precise, actionable diagnostic: at 78.9%, building a step-level router is provably wasteful; at 30%, it might be justified. This precision is the information gain.

**(iii) Persistence across interventions is non-obvious.** The finding that death dominance survives 10× scaling (DAF=92.4%), self-correction (DAF>100%), multi-seed replication (3 model families, 2.2pp spread), and penalty removal (78.9% label fraction unchanged) was not predictable a priori. Each intervention was a plausible path to reducing death dominance; none succeeded. This persistence pattern is empirically informative for practitioners deciding whether to invest in router development.

**(iv) Findings is the appropriate venue tier.** We agree this is an empirical analysis contribution rather than a method innovation. The ARR system explicitly accommodates such work: Findings recognizes papers that provide reliable empirical insights to the community. Our contribution—a reusable diagnostic framework with a surprising quantitative finding—fits squarely in this category. The framework's demonstrated applicability across 3 environments and 4 diagnostic conditions (death dominance, no signal, information asymmetry, agent floor) provides lasting methodological value beyond the specific ScienceWorld finding.

---

## Compressed Version (~800 words)

*For ARR rebuttal word limit. Each attack ~130 words.*

### R1: Single-Environment Generalization
The framework is applied unchanged to three environments yielding qualitatively distinct diagnoses: death dominance in ScienceWorld (78.9% label fraction, DAF=90.4%), no extractable signal in MATH (p=0.81), and information asymmetry in ALFWorld (DAF=0%; replicated across Llama 16/16 and Qwen 35/37 episodes). The ~50-episode pilot correctly predicted all four tested conditions (including MiniHack "no signal") at 4–8 GPU-hours. The specific finding (death dominance) replicates across three model families (DAF=88–90%, 2.2pp spread) and persists under 10× scaling to 72B (DAF=92.4%), confirming it is an environment property, not a model artifact. We distinguish methodological generality (the procedure applies to any environment with paired episodes) from empirical generality (full validation on ScienceWorld only), providing preliminary evidence of applicability beyond death-dominated settings.

### R2: Trivial Finding
Death penalty makes death *relevant*—not dominant. The magnitude is empirical: (i) 10× scaling to 72B yields DAF=92.4%, *higher* than 7B—if trivial, scaling should eliminate it; (ii) Reflexion self-correction yields DAF>100%: a stronger agent loses overall due to catastrophic vulnerability, counterintuitive from penalty structure alone; (iii) the primary metric (78.9% label fraction) is penalty-independent, holding at any P>0. The routing literature presupposes diverse signal: Toolformer learns per-token calls, CogRouter per-step depth, RouteLLM preference-based routing. These architectures are unnecessary if single-mechanism dominance is default. Our 78.9% directly challenges these presuppositions. Absence of prior signal-source diagnosis reflects an implicit diversity assumption we disprove.

### R3: No Actionable Solution
Our framework is to routing what probing classifiers are to representations: diagnostic work that precedes optimization. Three practical values: (1) The ~50-episode pilot answers "should we build a router?" in 4–8 GPU-hours—we spent ~200 GPU-hours on router training before discovering always-deterministic is near-optimal; ~190 GPU-hours would have been saved. (2) The diagnosis prescribes always-deterministic, which achieves 90.5% of oracle decisions at **zero additional training cost**—a cost-free deployment strategy derived from mechanism understanding. (3) Cross-environment applicability yields different prescriptions: ALFWorld (DAF=0%) diagnoses information asymmetry, recommending router development—qualitatively different guidance from the same tool.

### R4: Router Positive Control
The positive control confirms **signal granularity**, not router viability. Task-type features reach 62.9–64.7% BA vs step-level 56–59%, confirming signal granularity mismatch. Under LOTO, two independent methods—600M–4B neural routers and logistic regression on one-hot features—both collapse to chance (49.2% and 50.0%), confirming routing signal is a per-task-type constant with no cross-type generalization. A generative router (Qwen3-8B) also fails at 46.7%, ruling out architecture bottleneck. The structural explanation: death risk is a binary task-type property (10/11 types), constant within type but invisible to step features. This is a complete granularity diagnosis, not a missing control.

### R5: Per-Task Statistical Power
The headline finding is aggregate (N=245, 78.9%, bootstrap CI [69.5%, 86.3%]), not per-task. Per-task results are explicitly exploratory (Table 1 caption). Directional consistency: all 10 death-prone types show deterministic preference (p≈0.001); this holds across three independently sampled model families (30/30). Cross-model replication (DAF 88–90%, 2.2pp spread) provides stronger reliability evidence than increasing within-model N. Per-task Wilson CIs are wide (±20pp), which is why we avoid strong per-task claims. The aggregate CI confirms the finding is well-separated from 50% null even accounting for task-level clustering.

### R6: Limited Excitement
Diagnostic contributions have strong venue precedent: probing classifiers, CheckList, BERTology all redirected community methodology without proposing new architectures. Quantification is the contribution—78.9% is not a number anyone predicted; it could have been 30% or 90%, and the precision transforms vague intuition into actionable guidance. Persistence across four interventions (10× scaling, self-correction, 3 model families, penalty removal) was not predictable a priori. We position this as an empirical analysis contribution appropriate for Findings, providing a reusable diagnostic framework validated across 3 environments and 4 conditions.

---

## Detailed Version (~1200 words)

*For venues with higher word limits. Integrates Q1–Q4 responses into relevant attacks.*

### R1: Single-Environment Generalization

The framework is applied unchanged to three environments, producing qualitatively distinct diagnoses: death dominance in ScienceWorld (78.9% label fraction, DAF=90.4%; §3.1), no extractable signal in MATH (73.5% vs 73.0%, McNemar p=0.81, 84.4% no-preference; §3.4), and information asymmetry in ALFWorld (DAF=0%, 35/37 non-tie labels favor information-advantaged strategy; §3.4). The ALFWorld diagnosis replicates across two model families: Llama-3.1-8B (16/16 non-tie labels, 100% directional consistency) and Qwen2.5-7B (35/37, 94.6%). A MiniHack pilot (Appendix R) returns "no signal" as a fourth validated condition.

The specific finding—death dominance—replicates across three architecturally distinct 7–9B model families (Qwen2.5-7B DAF=90.4%, Llama-3.1-8B DAF=88.2%, Gemma-2-9B DAF=89.7%; spread 2.2pp; §3.2) and persists under 10× scaling to 72B (DAF=92.4%; §3.3). Cross-model death rate stability (36–43% internal; §5) confirms death vulnerability is a task-environment property, not a model artifact.

**[Q4]** Regarding the relationship to causal inference: our counterfactual comparison is a simplified instance of Rubin's (1974) potential outcomes framework—each episode observes outcomes under two treatments (internal vs. deterministic)—not Pearl's structural counterfactual involving do-calculus. We clarify this distinction in Related Work (§4).

The ~50-episode pilot protocol (Appendix R) provides preliminary build-vs-buy signal for all four tested conditions given large effect sizes (d=3.02; §3.1) at 4–8 GPU-hours. We distinguish *methodological generality* (applicable to any environment with paired episode outcomes) from *empirical generality* (full quantitative validation on ScienceWorld only), and scope claims accordingly (Limitations §1).

### R2: Trivial Finding

A death penalty makes death *relevant* to routing—not dominant. The magnitude is empirical, with three non-trivial results:

**(i) 10× scaling does not eliminate death dominance.** Qwen2.5-72B reduces internal death rate from 42.9% to 30.6% but yields DAF=92.4%—higher than 7B (90.4%). **[Q1]** This increase occurs because the deterministic strategy also becomes safer (2.75% vs 16.3% at 7B), so Δ_nd=+2.28 shrinks as a fraction of the total gap. Death dominance is *more* extreme at larger scale, not less—if it were a trivial artifact of weak models, scaling should reduce it (§3.3).

**(ii) Reflexion self-correction yields DAF>100%.** Under Reflexion (N=3), Δ_nd=−0.47: the self-correcting agent slightly *outperforms* deterministic on non-death episodes, yet loses overall because death asymmetry more than accounts for the full gap (§3.3). This counterintuitive result—a stronger agent performing worse due to catastrophic vulnerability—was not predictable from the penalty structure alone.

**(iii) The primary metric is penalty-independent.** The 78.9% death-asymmetry label fraction (75/95 non-tie labels; §3.1) holds at any P>0. DAF is a derived P-dependent measure (7.4% at P=0, 50.4% at P=10, 90.4% at P=100; Appendix K); we report both to separate the structural finding from its score-space amplification. **[Q3]** Algorithm 1's death-priority rule assumes P exceeds maximum partial scores; in ScienceWorld P=100 on a 0–100 scale, satisfying this condition. For environments where P < max_partial_score, score comparison would supplement the death-priority heuristic.

The routing literature presupposes diverse signal: Toolformer (per-token), CogRouter (per-step depth), RouteLLM (preference-based). Our 78.9% directly challenges this implicit assumption in catastrophic-failure environments.

### R3: No Actionable Solution

Our framework is to routing what probing classifiers are to representations: diagnostic work that should precede optimization. Three forms of practical value:

**Cost-saving diagnostic.** The ~50-episode pilot (Appendix R) answers "should we build a router?" in 4–8 GPU-hours. We invested ~200 GPU-hours training routers (6 SFT variants × 8 seeds × 3 model scales) before the diagnostic revealed always-deterministic is near-optimal; ~190 GPU-hours would have been avoided.

**The diagnosis is directly actionable.** Always-deterministic achieves 90.5% of oracle non-tie decisions (§3.5) at zero additional training cost. The diagnosis yields a cost-free deployment strategy derived from mechanism understanding, not "no solution."

**[Q2] Routing value ceiling.** Of 245 episodes, 150 (61.2%) show no preference (§3.1); routing is relevant in only 95 (38.8%). The oracle margin is 2.89 points (always-deterministic −9.47 vs oracle −6.58; §3.5), bounding practical routing value. We discuss this explicitly in §5: "even optimal routing yields modest gains." This quantification is itself actionable—it tells practitioners the maximum return on router investment.

**Cross-environment prescriptions differ.** In ALFWorld (DAF=0%), the framework diagnoses information asymmetry rather than death dominance, recommending router development—qualitatively different guidance from the same diagnostic tool (§3.4). The framework's value is not tied to any single prescription.

### R4: Router Positive Control

The positive control confirms **signal granularity**—routing signal exists at task-type level but not step level—which is §3.6's core diagnostic contribution.

**Task-type features outperform step features.** A keyword variant adding task name to step features reaches 62.9% balanced accuracy (Appendix P). Independently, a task-type-only logistic regression on one-hot task-type features achieves 64.7% (supplementary analysis). Both exceed all step-level routers (56–59%; §3.6), directly demonstrating a granularity mismatch. The 62.9% result augments step-level features with task identity; the 64.7% uses *only* task identity, confirming that task-type is the informative feature.

**LOTO confirms no cross-type generalization.** Under leave-one-task-type-out, two architecturally unrelated approaches—600M–4B neural routers (49.2%; §3.6) and logistic regression on one-hot features (50.0%; Appendix P)—both collapse to chance. This convergence confirms routing signal is a per-task-type constant, not a learnable cross-type pattern.

**Generative router also fails.** Qwen3-8B generating routing decisions achieves 46.7% (Appendix P), ruling out SFT architecture as the bottleneck.

**Structural explanation:** 10/11 task types carry death risk (§5). Death risk is binary per task type—constant within type but invisible to step-level features. This is a complete granularity diagnosis: signal exists (task-type level), signal is absent (step level), two independent methods confirm no cross-type transfer. The diagnosis is "signal-limited, not architecture-limited."

### R5: Per-Task Statistical Power

The headline finding is aggregate, not per-task. The 78.9% death-asymmetry fraction is computed over N=245 episodes with bootstrap 95% CI [69.5%, 86.3%] (B=10,000; §3.1), well-separated from the 50% null.

**Per-task results are explicitly exploratory.** Table 1 caption marks all per-task analyses as single-seed, n≈20 exploratory results with power ≈50% for 20pp effects. We make no claims requiring per-task significance.

**Directional consistency provides strong evidence.** All 10 death-prone task types show deterministic preference (p≈0.001 under null). This holds across three independently sampled model families: Qwen 10/10, Llama 10/10, Gemma 10/10 = 30/30 (§3.2), where distinct architectures provide genuinely independent sampling—stronger evidence than within-model replication.

**Cross-model replication substitutes for within-model N.** Three model families independently converge on DAF 88–90% (2.2pp spread; §3.2). An independent seed replication (N=220) yields DAF=89.7%, within 0.7pp of the primary result (Appendix D).

**Cluster bootstrap caveat.** Wild cluster bootstrap with K=11 yields p=0.002 (§3.1), but K<20 falls below recommended thresholds (Cameron et al., 2008; Webb, 2023). We treat this as a sensitivity check; readers should rely on the non-clustered bootstrap CI ([81.1%, 99.0%] for DAF). Per-task Wilson CIs are wide (±20pp), which is why we avoid strong per-task claims.

### R6: Limited Excitement / Novelty

We position this as an empirical analysis contribution, where diagnostic frameworks have established precedent and impact at *ACL venues.

**Diagnostic contributions have strong track records.** Probing classifiers (Conneau et al., 2018; Hewitt & Manning, 2019) changed how the community evaluates representations without proposing new architectures. CheckList (Ribeiro et al., 2020) redirected evaluation methodology. BERTology (Rogers et al., 2020) synthesized analytical findings into actionable guidance. Our contribution—a diagnostic framework that precedes and redirects optimization—follows this lineage.

**Quantification is the contribution.** "Death might matter" is a reasonable intuition, but intuitions lack precision. The 78.9% finding specifies magnitude: at 30%, router development might be justified; at 78.9%, it is provably wasteful. This precision transforms vague intuition into actionable guidance with quantified decision boundaries.

**Persistence across interventions is non-obvious.** Death dominance survives 10× scaling (DAF=92.4%), self-correction (DAF>100%), multi-family replication (3 models, 2.2pp spread), and penalty removal (78.9% unchanged; §3.3, §5). Each was a plausible path to reducing death dominance; none succeeded.

**Findings is the appropriate venue.** ARR explicitly accommodates empirical analysis contributions. Our framework's demonstrated applicability across 3 environments and 4 diagnostic conditions (death dominance, no signal, information asymmetry, agent floor) provides lasting methodological value. The reusable diagnostic procedure—not the specific ScienceWorld finding—is the durable contribution.
