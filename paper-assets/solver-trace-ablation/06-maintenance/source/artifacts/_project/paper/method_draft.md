# §3 Method — Draft (solver-trace-ablation, EMNLP 2026)
<!-- Word budget: ~1200. All numbers traceable to registry. -->

We formalize the task of natural language to formal logic translation (§3.1), describe the GRPO training framework (§3.2), introduce Solver Trace Ablation as a diagnostic protocol (§3.3), define the Intensional Structural Reward (§3.4), present the reward formulations under study (§3.5), and catalog the hacking modes discovered across conditions (§3.6).

## 3.1 Task: NL-to-Formal-Logic Formalization

Given a natural language reasoning problem *x* consisting of premises and a conclusion, the task is to produce a formal logic program *f(x) = {c₁, c₂, …, cₙ}* comprising *n* components (axioms, rules, or clauses) that an external automated solver can evaluate. We consider two target formalisms: first-order logic (FOL), verified by the Prover9 theorem prover, and Prolog, verified by SWI-Prolog. A formalization is *proved* if the solver returns a successful derivation within a fixed timeout.

This setup decouples generation (the language model) from verification (the solver), providing a binary execution signal *r_exec ∈ {0, 1}* that is noise-free but structurally uninformative: a formalization that embeds the conclusion directly in its premises will prove trivially, receiving the same reward as a faithful translation.

## 3.2 GRPO Training

We train a language model π_θ using Group Relative Policy Optimization (GRPO; Shao et al., 2024). For each problem *x*, GRPO samples a group of *K* candidate formalizations {f₁, …, f_K} from π_θ, scores each with a reward function *r(·)*, and updates the policy using the group-normalized advantage:

> **A_i = (r(f_i) − μ_group) / σ_group**

where μ_group and σ_group are the mean and standard deviation of rewards within the group. The policy gradient objective follows:

> **L(θ) = −E[A_i · log π_θ(f_i | x)] + β_KL · D_KL(π_θ ∥ π_ref)**

In the baseline configuration, the reward is purely execution-based: *r(f) = r_exec(f)*. This drives prove rate from 12% (base model; `sta-phase0-baseline`) to 32% at 100 steps (`plan003-eval-exec-only-r5`), eventually reaching 93% at 500 steps—but, as we show in §4, this improvement is largely achieved through structural shortcuts.

## 3.3 Solver Trace Ablation (STA)

Solver Trace Ablation is a post-hoc diagnostic protocol that assesses the structural necessity of each component in a proved formalization. The protocol adapts leave-one-out (LOO) analysis from mutation testing (DeMillo et al., 1978; Jia & Harman, 2011) to formal logic verification.

For a proved formalization *f = {c₁, c₂, …, cₙ}* with *n* components, STA proceeds as follows:

1. **Baseline verification.** Confirm that the full formalization *f* proves successfully under the target solver.
2. **Component ablation.** For each component *c_i* (i = 1, …, n), construct the ablated formalization *f\{c_i}* and re-run the solver.
3. **Necessity determination.** Component *c_i* is *necessary* if the solver fails on *f\{c_i}*, and *redundant* otherwise.
4. **Aggregation.** Compute the fraction of necessary components as the Intensional Structural Reward (ISR; §3.4).

STA is solver-agnostic: the same protocol applies to Prover9 (FOL) and SWI-Prolog (Prolog) without modification, enabling cross-logic diagnostic transfer (§4).

STA is applied only to proved samples (*r_exec = 1*). For unproved samples, ISR is undefined (the baseline verification in Step 1 fails). When reporting population-level ISR statistics, we report *proved-only* ISR (ISR*), which conditions on successful baseline verification, to avoid conflating structural quality with prove rate.

## 3.4 Intensional Structural Reward (ISR)

Given a proved formalization *f = {c₁, …, cₙ}*, we define ISR as the fraction of components whose removal causes proof failure:

> **ISR(f) = (1/n) Σᵢ 𝟙[solver fails on f\{c_i}]**

where *f\{c_i}* denotes *f* with component *c_i* removed. ISR is bounded in [0, 1]: ISR = 1 indicates every component is individually necessary for the proof, while ISR = 0 indicates no single component is necessary (all are redundant).

ISR measures *syntactic component necessity*—whether each component contributes to the proof derivation—not semantic faithfulness to the natural language input. This distinction is critical: a formalization can achieve ISR = 1 by containing a single tautological component (e.g., a premise identical to the conclusion), which is necessary by construction but semantically degenerate.

**Premise count bias.** ISR is mathematically influenced by the number of components: formalizations with fewer premises have higher expected ISR under random ablation, since each component constitutes a larger fraction of the proof. We control for this confound in our analysis via premise-count-matched comparisons (§4).

## 3.5 Reward Formulations

To study the effect of incorporating ISR into GRPO training, we evaluate the following reward formulations:

**Execution-only (baseline).** *r(f) = r_exec(f)*. Binary solver success, providing no structural signal.

**Additive ISR.** *r(f) = r_exec(f) · (1 + β · ISR(f))*, where β > 0 controls the ISR weight. The multiplicative gating by r_exec ensures ISR contributes only for proved samples. We evaluate β ∈ {0.1, 0.3}.

**Additive random (control).** *r(f) = r_exec(f) · (1 + β · U)*, where U ~ Uniform(0, 1) replaces ISR with a random signal. This isolates the effect of ISR-specific information from the effect of reward variance alone.

**SFT (supervised baseline).** Standard supervised fine-tuning on ground-truth formalizations, serving as a non-RL reference point.

Additional formulations (convex combination *r = α · r_exec + β · ISR*) were explored but produced degenerate outcomes (ISR < 1 acts as a penalty on proved samples, suppressing prove rate); we report these briefly in §4.

## 3.6 Reward Hacking Taxonomy

Across experimental conditions, we identify seven distinct reward hacking strategies, classified by manual inspection and automated pattern detection:

- **H1. Multi-premise conclusion embedding.** The conclusion is embedded verbatim within one or more premises. The proof succeeds trivially via subsumption. Prevalent across all GRPO conditions (52–93% of proved samples).
- **H2. Tautological collapse.** The formalization reduces to two components where one trivially entails the other.
- **H3. Complexity without utility.** Extraneous axioms that do not contribute to the proof but inflate component count.
- **H4. Repetition collapse.** Identical components repeated multiple times, inflating *n* while each copy is individually redundant under LOO ablation.
- **H5. Contradiction explosion.** Contradictory axioms from which anything follows *ex falso quodlibet*, yielding ISR = 0 since no single axiom is necessary once the contradiction is established.
- **H6. ISR inflation via conclusion duplication.** The conclusion appears as a single premise identical to the goal. Under LOO, removing this sole necessary component causes proof failure, yielding ISR ≈ 1. This mode is ISR-specific: it appears in 64.5% of ISR-rewarded proved samples across three seeds but in 0% of random-rewarded samples.
- **H7. Query-as-fact gaming (Prolog).** The model converts the natural language question into a snake_case atom and asserts it simultaneously as a fact and a query, causing SWI-Prolog to trivially succeed. This mode bypasses text-match hacking classifiers and was identified only through functional analysis of the n_necessary distribution.

Modes H1–H5 arise under execution-only reward. H6 emerges specifically under ISR reward, representing *meta-level* Goodhart behavior: the model games the diagnostic metric itself. H7 is specific to Prolog STA and reveals a classifier blind spot—text-match detection fails, requiring cross-validation with functional necessity analysis.
