# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/1ffe918b-ce36-4b62-a5ce-cb5a2b75c457.jsonl`
- **Structured JSON:** [`985fe0eddacf596b907f.json`](../../sessions/98/985fe0eddacf596b907f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:37:06.719Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:37:06.719Z",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weighting Induces Sequential Skill Curriculum for Joint NER+RE+EE\",\n  \"core_problem\": \"GRPO-based information extraction (IE) rewards universally treat (span, type) pairs as atomic structural units: a prediction with the correct span but wrong type label receives the same near-zero reward as a completely missed mention. This atomicity assumption has a precise gradient-theoretic consequence. In early GRPO training when both span detection and type classification are unreliable, atomic rewards produce high-variance gradients: the expected non-zero signal requires simultaneously correct span AND correct type, a low-probability joint event whose probability product makes the reward sparse and noisy. Span-decoupled rewards break this bottleneck — span-boundary F1 is continuous, lower-variance, and receives non-zero gradient even when type is wrong, stabilizing the GRPO objective in early training and allowing span detection to converge first. As span accuracy increases, the type-conditioned component's gradient variance drops (conditioned on correct spans, type prediction becomes a simpler classification problem), creating a span→type→argument sequential convergence structure — an implicit curriculum emerging from reward decomposition rather than explicit scheduling.\\n\\nProUIE (arXiv:2604.10633, April 2026) provides the clearest empirical evidence for the cost of atomic rewards. Its Stepwise Fine-grained Reward (SFR) for event extraction computes argument-level F1 (F_full) by first matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap. When trigger type or span is wrong, fewer argument pairs match, reducing F_full — and the piecewise penalty (Eq. 9) simultaneously shifts gradient emphasis toward trigger correction rather than argument assignment. The result, as we infer from SFR's structure (ProUIE does not explicitly diagnose the mechanism), is that argument role learning receives weakened gradient signal whenever trigger detection fails. ProUIE reports ACE2005 Trigger F1=70.65% and Argument F1=52.58% versus InstructUIE (Flan-T5-XXL, 11B) at 77.13%/72.94% — a 20-point argument F1 deficit. ProUIE's authors attribute this to 'unified generation setting and reward configuration' and call for 'more appropriate reward design,' but do not identify which structural feature of SFR causes the gap.\\n\\nThe core missing ingredient is a principled span-boundary reward that is decoupled from type label, accompanied by a formal justification showing why this decomposition creates stable sequential skill acquisition during GRPO training. No published GRPO-IE work provides either: ProUIE's SFR, R1-RE, R2GRPO, and EXTRACT-0 all use atomic (span, type) rewards; and no GRPO-IE paper has analyzed reward decomposition through the lens of gradient variance or curriculum induction.\",\n  \"opportunity\": \"ProUIE's acknowledged performance gap ('more appropriate reward design') and its documented 20-point argument F1 deficit on ACE2005 create a precisely bounded opportunity with three distinct axes — two empirical and one theoretical — none of which existing work covers.\\n\\n**Axis 1 (Theoretical — primary novelty)**: No published work has formally analyzed how decomposing IE rewards by skill type (span detection vs. type classification vs. relational assignment) induces sequential skill convergence in GRPO training. The closest parallel is RuCL (arXiv:2602.21628), which uses tiered rubric rewards in GRPO for multimodal reasoning and provides a gradient variance decomposition in Appendix B showing that reliable foundational reward components reduce early-training gradient variance. For IE, the analogous argument requires showing that span-boundary F1 has systematically lower reward variance than joint (span, type) F1 in early training — because span IoU is a continuous signal while joint correctness is a low-probability conjunction — and that this variance gap induces a span→type→argument convergence ordering. Making this argument formally for IE, supported by per-component learning curves, is a genuine theoretical contribution gap. The recent 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) formally proves a relay regime for task-level difficulty ordering but does not analyze reward-component-level difficulty ordering within a single task type — the proposed analysis applies the relay regime concept at a different level of abstraction. The Reward Decomposition Theorem of arXiv:2604.19857 bounds the sub-optimality gap between decomposed and joint GRPO optimization but does not identify which structural properties of the reward signal (continuous span-IoU vs. joint conjunction) determine whether decomposition is beneficial — our variance analysis fills that gap.\\n\\n**Axis 2 (Algorithmic — secondary novelty)**: Existing GRPO-IE work uses fixed reward weights. The multi-objective RL literature (arXiv:2509.11452) has proven that fixed-weight scalarization is provably suboptimal for non-convex Pareto fronts, and APEX (arXiv:2601.06574) has identified 'variance hijacking' — high-variance reward components dominating gradients — as the mechanism behind fixed-weight failures. GDPO (arXiv:2601.05242, ICML 2026) addresses the related problem of advantage collapse via per-reward normalization but uses fixed aggregation weights. SPARD (arXiv:2604.07837, April 2026) introduces PAWA for reward-component-level adaptive weighting at the LLM alignment level, but applies to open-ended generation with LLM-judge rewards and provides no IE-specific structural decomposition or gradient-variance theoretical basis. MAESTRO (arXiv:2601.07208) formulates reward scalarization as a meta-learning bandit problem, also for open-domain generation. Contribution 2's novelty is therefore NOT a novel adaptive weighting algorithm per se, but the application and instantiation of convergence-gap weighting to the specific span/type/argument IE hierarchy, with the formula design directly derived from the gradient-variance analysis of Contribution 1. The gap-based formula max(ε, θ−F1_i)/σ_i is philosophically opposite to SPARD's momentum-based scheme (which up-weights components making reliable progress, risking perpetuating the dominance of whichever component improves first) and is chosen because the gradient-variance analysis identifies the gap to convergence — not the rate of progress — as the theoretically relevant quantity for curriculum enforcement. All GRPO-IE papers (ProUIE, R1-RE, R2GRPO, EXTRACT-0) use fixed weights; none applies adaptive weighting to the span/type/argument hierarchy with a structural motivation.\\n\\n**Axis 3 (Empirical — benchmark coverage)**: ProUIE evaluates EE on only ACE2005, CASIE, and PHEE; no RLVR-IE paper has assessed OOD event argument generalization on RAMS (139 event types, 65 argument roles, document-level), WikiEvents (50 event types, document-level), or MAVEN (168 event types, general-domain trigger detection). The proposed span-decoupled curriculum reward addresses ProUIE's diagnosed failure mode and directly fills all three gaps.\",\n  \"landscape\": \"**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. When trigger detection fails, F_full shrinks (fewer argument pairs match) and the gradient emphasis shifts to trigger correction rather than argument assignment — producing, as we infer from the structural piecewise design, weakened argument-learning signal during trigger training. ProUIE does not explicitly state this mechanism; the authors attribute weak EE to 'unified generation setting and reward configuration' and call for 'stronger event-specific modeling and more appropriate reward design' in limitations. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Our work differentiates from ProUIE on three axes: (1) span-boundary F1 computed independently of type label with formal gradient-variance justification; (2) dynamic weight adaptation replacing fixed weights; (3) per-component learning curve analysis.\\n\\n**SPARD** (arXiv:2604.07837, April 2026) proposes a self-paced curriculum for RL alignment via two components: **PAWA (Progress-Aware Weight Adaptation)**, which adjusts reward-component weights dynamically at training time, and **RADR (Reward-Attributed Data Rebalancing)**, which rebalances training data categories based on reward-attributed utility. PAWA operates at the reward-component level: the weight update is w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i) / Σ_j(w_t^{r,j}·exp(η·Q_t^j)), where Q_t^i = (μ_t^i − β·σ_t^i) − (μ_{t-1}^i − β·σ_{t-1}^i) is a Reliable Performance Gain based on the Lower Confidence Bound (LCB) principle — the exponential up-weighting fires when the LCB estimate of mean reward improvement is positive, i.e., when a component is making reliable *progress*. RADR rebalances data categories (Code, Knowledge QA, Text Transformation, Creative Writing). SPARD applies to open-ended LLM alignment with LLM-judge rewards across text generation domains; it does not address structured prediction or IE. Three differentiations from the proposed scheme: (a) **Formula philosophy**: SPARD's PAWA up-weights components making reliable *progress* (momentum), whereas our scheme w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) up-weights components that are *lagging* below the convergence target — enforcing curriculum by redistributing weight toward gaps rather than reinforcing momentum. In later training when span detection improves, SPARD might continue up-weighting span (it keeps showing LCB progress), while ours explicitly shifts weight to type and argument. (b) **IE structural decomposition**: SPARD applies to heterogeneous open-domain capabilities; the proposed scheme is designed specifically around the span/type/argument IE hierarchy and the structural insight that span-IoU is a continuous signal while type-correctness is a conjunction, which is absent from SPARD. (c) **Gradient-variance theoretical basis**: SPARD provides no formal analysis of why reward components have different variance profiles or why a particular weight ordering should emerge during training — the paper acknowledges that nonlinear objective interdependencies are not theoretically analyzed. The proposed Contribution 1 provides this analysis specifically for IE: span-IoU continuity vs. joint span+type conjunction explains the early-training variance differential that directly motivates the gap-based (not momentum-based) weighting formula. Note: SPARD's RADR data rebalancing is orthogonal to our approach (we do not modify data selection), but PAWA is genuine reward-component-level weighting — the differentiation rests on formula philosophy, IE-specific decomposition, and theoretical grounding, not on data-vs-reward-component scope.\\n\\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with a two-tier decomposed reward (foundational rubrics + advanced rubrics) for multimodal reasoning, with a curriculum coefficient progressively shifting weight from easy to hard rubrics. Appendix B provides gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. RuCL achieves +7.83% average improvement across seven benchmarks. It is the methodological parallel most relevant to our curriculum-induction claim — but for multimodal reasoning, not IE, and without the span-boundary decoupling insight or IE-specific convergence analysis.\\n\\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses a different failure mode of multi-reward GRPO: advantage collapse. In standard GRPO, rewards are summed before group-wise normalization (r_sum = r₁+...+rₙ; A = (r_sum − mean)/std), causing distinct reward combinations — e.g., (span=0, type=1), (span=0, type=2), and (span=1, type=2) — to map to identical normalized advantage values, destroying the relative signal between reward types. GDPO decouples normalization: each reward's advantage is normalized independently (A_i = (r_i − mean_i)/std_i) before summation and batch-wise renormalization. This preserves the relative differences between reward combinations at the normalization level. The proposed adaptive weight scheme is orthogonal: it operates after per-reward advantages are computed, adjusting the relative aggregation weights w_i(t) based on convergence progress rather than modifying the normalization step. The two mechanisms can be combined directly — GDPO normalization applied to each span/type/argument advantage, followed by convergence-progress adaptive aggregation weights — and this combination is a natural future direction. GDPO was tested on tool calling (Berkeley BFCL-v3: +4.73% live accuracy over GRPO), math, and coding, using DeepSeek-R1-1.5B and Qwen3-4B; it has not been applied to IE.\\n\\n**MAESTRO** (arXiv:2601.07208, January 2026) formulates reward scalarization as a contextual bandit problem, training a lightweight Conductor network that uses the policy's terminal hidden states to dynamically adapt reward weights, optimized via a bi-level scheme with group-relative advantages as meta-reward signal. Applied to open-domain generation across seven benchmarks, MAESTRO outperforms static multi-objective baselines. Compared to the proposed adaptive weight scheme, MAESTRO's bi-level optimization with a separate Conductor network introduces significant additional complexity; the proposed scheme uses a simple convergence-progress formula (max(ε, θ−F1_i)/σ_i) interpretable directly from the gradient-variance analysis, with no additional network parameters and no additional computational overhead over standard GRPO. Neither MAESTRO nor SPARD has been applied to IE or provides structural analysis of span/type/argument reward decomposition.\\n\\n**VCRL** (arXiv:2509.19803, September 2025) uses the variance of rollout group rewards as a real-time indicator of between-sample difficulty in RLVR for math reasoning: low variance indicates a sample is too easy or too hard, high variance indicates optimally difficult samples. VCRL drives curriculum via variance-based dynamic sampling to control training batch quality, achieving +4.67 points average on Qwen3-8B-Base over GSPO on five math benchmarks. The variance signal in VCRL is between-sample (which training examples to select based on predicted difficulty); the proposed work's variance analysis is within-sample (which reward components have lower variance within a single IE prediction, determining which skill should converge first). These are different uses of reward variance at different levels of abstraction and serve complementary purposes.\\n\\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally analyzes RLVR training dynamics on L-step compositional reasoning tasks, proving that mixed-difficulty training enters a relay regime when the difficulty ratio R = O(1) (smooth spectrum): persistent gradient signals on easier horizons make slightly harder horizons tractable, producing an implicit curriculum without explicit scheduling (Theorem 5.2 bounds inter-horizon plateau at Õ(L_max/η) vs. exponentially longer in the grokking regime). Crucially, the relay regime is analyzed at the task level — different training instances of different horizon lengths L₁ < L₂ < L_max — and the framework does not address reward decomposition. The proposed Contribution 1 applies the relay regime concept at a different level of analysis: within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, and the continuous span-IoU signal provides the 'smooth gradient handoff' that prevents prolonged plateaus during type and argument learning. This reward-component-level relay is a conceptual extension of the task-level relay regime, not a direct instantiation, and constitutes the novel contribution of Contribution 1 beyond the original framework.\\n\\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards in LVLMs, establishing convergence to a first-order stationary point at rate O(1/√T). Their result characterizes when sequential or parallel per-component optimization loses performance relative to joint training. The proposed Contribution 1 is complementary: rather than bounding the worst-case sub-optimality cost of decomposition in general, it identifies the specific structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that determines whether the decomposed reward yields lower early-training gradient variance. Together, the two analyses bracket the expected behavior: arXiv:2604.19857 establishes that decomposed GRPO is guaranteed to converge (sub-optimality is bounded), and the proposed variance analysis identifies why for IE rewards specifically the early-training variance reduction from span continuity is expected to dominate the sub-optimality cost.\\n\\n**Dynamic reward weighting** (arXiv:2509.11452, 2025) proves that fixed-weight scalarization fails on non-convex multi-objective RL Pareto fronts and proposes hypervolume-guided adaptive weight adjustment compatible with GRPO. **APEX** (arXiv:2601.06574, 2026) identifies 'variance hijacking' in multi-objective RL and proposes per-objective priority based on Learning Potential × Conflict Penalty × Progress Need. Neither paper applies adaptive weighting to IE or analyzes the span-type variance differential.\\n\\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation but do not analyze training dynamics or reward signal ordering in RL.\\n\\n**REAR** (EMNLP 2025 Findings) applies DeepSeek-R1-style RL to joint EAE+RE via supervised warm-up + joint RL, single joint reward; excludes NER and trigger detection. **R1-RE** (arXiv:2507.04642, July 2025) is RLVR for RE only, single reward, strong OOD robustness. **R2GRPO** (arXiv:2505.22068, May 2025) applies GRPO to scientific NER+RE with a composite reward, no EE and no substructure decomposition. **EXTRACT-0** (arXiv:2509.22906, September 2025) uses 7B LoRA+GRPO with semantic similarity reward for document extraction. **KnowCoder** (ACL 2024) achieves state-of-the-art IE via code-style schema SFT. **GoLLIE** (ICLR 2024) improves zero-shot IE via annotation guideline following.\\n\\nNo published GRPO-IE paper provides span-boundary reward independent of type label, formal gradient-variance curriculum justification for IE reward decomposition, or adaptive weighting applied to the span/type/argument IE skill hierarchy, as of May 2026.\",\n  \"approach\": \"We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) and a span-boundary-decoupled reward with adaptive component weighting. The paper has three contributions: a theoretical contribution (gradient variance analysis), an algorithmic contribution (adaptive weights replacing fixed weights, applied to the IE skill hierarchy), and an empirical contribution (per-component learning curves as diagnostic evidence for curriculum induction).\\n\\n**Contribution 1 — Gradient Variance Analysis (theoretical)**:\\nWe formalize the curriculum-induction property of span-decoupled rewards. In early GRPO training, let p_s = P(span correct) and p_t = P(type correct | span) be the model's per-token span detection rate and type accuracy given correct span. For standard atomic rewards (joint span+type), the non-zero reward probability is p_s · p_t — low in early training because it requires a conjunction. For span-decoupled rewards, the span component alone has non-zero probability p_s > p_s · p_t. The gradient variance of the span-decoupled reward is:\\n\\nVar(∇R_decomposed) = α₁²·Var(∇F1_span) + α₂²·Var(∇F1_type|span) + α₃²·Var(∇F1_arg) + cross terms\\n\\nWe show that when p_s < 0.5 (early training), Var(∇R_decomposed) < Var(∇R_atomic) because α₁·∇F1_span provides a stable non-zero signal that reduces total gradient variance, following the same framework as RuCL's Appendix B but derived for continuous span-IoU rewards rather than binary rubrics. As span detection improves (p_s → 0.7+), the type-conditioned component's gradient variance decreases (conditioning on correct spans reduces label ambiguity), and argument F1 receives cleaner signal. This creates a span→type→argument sequential convergence ordering that is a direct consequence of reward decomposition — not an explicitly scheduled curriculum.\\n\\nWe position this analysis in relation to two concurrent theoretical frameworks. First, 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) proves a relay regime for task-level difficulty ordering: when the training set contains tasks of smoothly graduated horizons L₁ < L₂ < L_max, gradient dominance is handed off from easy to hard tasks, producing implicit curriculum emergence. Our analysis applies the relay concept at a different level — within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, with span-IoU continuity providing the smooth gradient handoff. This is a reward-component-level relay, not a task-level relay, and the paper explicitly distinguishes these two levels. Second, arXiv:2604.19857 proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed and joint GRPO optimization at O(1/√T). Our variance analysis complements this bound: arXiv:2604.19857 characterizes the worst-case cost of decomposition (sub-optimality); our analysis identifies the structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that makes the early-training variance reduction benefit dominate this cost in practice. The testable prediction is per-component learning curves that show span F1 converging before type-conditioned F1, which converges before argument F1.\\n\\n**Contribution 2 — Adaptive Component Weights for IE Skill Hierarchy (algorithmic)**:\\nContribution 2's novelty is the APPLICATION and instantiation of convergence-gap weighting to the specific span/type/argument IE skill hierarchy, with the formula design directly derived from the gradient-variance analysis of Contribution 1 — not a novel adaptive weighting technique per se. SPARD (arXiv:2604.07837) has already demonstrated reward-component-level adaptive weighting for LLM alignment via PAWA, MAESTRO (arXiv:2601.07208) via meta-learning, and arXiv:2509.11452 + APEX are the motivating references for why fixed weights are suboptimal. The contribution here is the IE-specific instantiation: the choice of gap-based weighting (ours) over momentum-based weighting (SPARD's PAWA) is theoretically motivated by Contribution 1's analysis. SPARD's PAWA up-weights components making reliable progress (positive LCB improvement ΔQ_t > 0), which risks perpetuating dominance of whichever component improves first. Our scheme up-weights components that are lagging below the convergence target, which directly enforces the span→type→argument ordering identified by the gradient-variance analysis — once span F1 approaches θ, weight redistributes to type, and once type approaches θ, weight redistributes to argument. The variance normalization term (dividing by σ_i(t)) further ensures that components with reliable (low-variance) gradients receive appropriate weight even when converging, preventing gradient noise from high-variance components hijacking the curriculum. No published GRPO-IE paper applies any form of adaptive weighting to the span/type/argument hierarchy; this instantiation is a genuine contribution at the IE domain level.\\n\\nReplacing fixed weights (0.4/0.3/0.3) with a dynamic scheme motivated by arXiv:2509.11452's finding that fixed scalarization is suboptimal and APEX's identification of variance hijacking. At each evaluation checkpoint t, let F1_i(t) be the current F1 for component i ∈ {span, type, arg} and σ_i(t) be its rolling standard deviation over the last 50 steps. The adaptive weight:\\n\\nw_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)\\nnormalized so Σᵢ wᵢ(t) = 1, with ε=0.05 preventing zero weights, θ=0.7 as the convergence target.\\n\\nThis rule assigns higher weight to components that are lagging convergence (below θ=0.7) and lower variance (reliable gradient signal), preventing variance hijacking from the highest-variance component. Early in training, span typically has lower variance and below-target F1, so it receives high weight; once span F1 exceeds 0.7, weight shifts to type; once type converges, weight shifts to argument.\\n\\n**Relationship to GDPO**: GDPO (arXiv:2601.05242, ICML 2026) addresses a complementary but distinct normalization-level failure: advantage collapse, where summing rewards before group-wise normalization maps distinct reward combinations (e.g., span=0,type=1 vs. span=1,type=0) to identical normalized advantage values. GDPO's fix — normalizing each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation — operates at the normalization step. The proposed adaptive weights operate after per-reward advantages are computed, adjusting relative aggregation weights based on convergence progress. The two mechanisms are orthogonal and can be combined: applying GDPO normalization to each span/type/argument advantage before applying the convergence-progress adaptive weights would simultaneously prevent advantage collapse and enforce the curriculum. This combination is identified as a concrete future direction.\\n\\n**Secondary convergence criterion (θ sensitivity)**: The convergence target θ=0.7 assumes argument F1 will approach 70%+ during training (InstructUIE achieves 72.94% at 11B; the proposed system targets >60% at 8B, making this uncertain). If argument F1 plateaus below θ, the argument component would persistently receive high weight, risking the variance hijacking the scheme is designed to prevent. To address this: (a) a plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, regardless of whether F1_i has reached θ — converged-by-plateau components have their weight set to ε; (b) sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} is conducted via checkpoint evaluation on the saved main-run checkpoints, requiring no additional full training runs. If plateau detection triggers for argument before θ, weight redistribution favors whichever remaining component has the largest convergence gap and lowest variance.\\n\\n**Reward formula with adaptive weights**:\\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification)\\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration\\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong\\n\\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps.\\n\\n**Contribution 3 — Learning Curve Diagnostics (empirical)**:\\nPer-component F1 is logged every 50 GRPO steps throughout training, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves. The predicted pattern (span converges first, then type, then argument) is treated as an empirically testable consequence of the gradient variance analysis. Deviation from this pattern would falsify the curriculum-induction hypothesis and require reanalysis. This is a diagnostic contribution: even if final numbers are modest, the learning curves themselves constitute evidence about GRPO training dynamics for IE that no prior work has published.\\n\\n**Cascade failure reframing (addressing reviewer concern)**:\\nWe do not attribute to ProUIE the claim that wrong trigger type produces near-zero argument reward — ProUIE makes no such explicit statement. Our paper presents this as an inference: ProUIE's SFR structure (Eq. 9-10) implies that trigger group mismatch reduces F_full by limiting argument pair matching coverage, and the piecewise penalty shifts gradient emphasis toward trigger correction rather than argument assignment. The specific mechanism is our analysis, not ProUIE's diagnosis. ProUIE's authors observe the symptom (weak EE, especially argument F1) and call for 'more appropriate reward design'; our paper provides the mechanism and the fix.\\n\\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER).\\n\\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\\n\\n**Output format**: Code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures actual token length distribution before full training; all compute commitments gated on this measurement. Expected 300-600 tokens per example.\\n\\n**Baselines and comparison structure**:\\n(a) SFT baselines: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\\n(b) Single-reward GRPO: joint extraction F1 as the only reward, same Qwen3-8B — isolates reward decomposition effect\\n(c) Fixed-weight decomposed GRPO (α₁=0.4, α₂=0.3, α₃=0.3 throughout): ablation isolating adaptive weight contribution from span decoupling contribution\\n(d) α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5): derived from checkpoint evaluation, not a full new run — directly tests whether span-boundary decoupling is the essential design choice\\n(e) ProUIE published ACE2005 numbers (Qwen3-4B, scale difference noted explicitly)\\n(f) OOD: RAMS, WikiEvents, MAVEN (zero-shot cross-distribution generalization, sentence→document shift explicitly noted as confound; analysis identifies which document-level aspects hurt: coreference resolution for cross-sentence arguments, multi-sentence span detection)\\n\\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS (300-600 tokens) and WikiEvents (400-800 tokens) fit in full-document inference. OOD results are framed as 'zero-shot cross-distribution generalization from sentence-level training to document-level inference.' Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements. This converts the confound from a limitation to an analytical contribution.\\n\\n**Key testable hypotheses**:\\nH1 (curriculum): Per-component learning curves show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics.\\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute — isolates span-boundary decoupling contribution.\\nH3 (adaptive vs. fixed): Adaptive weight scheme produces higher Argument F1 than fixed-weight decomposed GRPO — isolates adaptive weighting contribution.\\nH4 (ProUIE gap): Decomposed GRPO closes a material fraction of the 20-point argument F1 gap vs. InstructUIE (target: Argument F1 >60% at 8B scale).\",\n  \"resource_estimate\": {\n    \"compute_note\": \"Single-run-primary design gated on 50-example dry run. Output token length: 300-600 tokens per example for joint NER+RE+EE with CoT (corrected from earlier 100-300 estimate). Dry run measures actual distribution before full training. Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.\",\n    \"manual\": {\n      \"gpu_hours\": \"~130-160 H100-hours total: dry run (~2 H100-hours) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours at ≤400 token output measured by dry run) + fixed-weight ablation from checkpoint evaluation (~20-25 H100-hours, not a full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours, draws on saved checkpoints). Total ≤165 H100-hours — within 200 H100-hour ceiling.\",\n      \"gpu_utilization\": \"Low (20-35%) — GPUs idle during gradient variance analysis derivation, learning curve interpretation, reward verifier implementation, and writing.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$325-660 (at $2.50-4/hr H100 cloud on-demand)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (same single-run-primary design; agent queues dry run first, then main GRPO run; α₁=0, fixed-weight, and θ sensitivity ablations derived from checkpoint eval, not new runs)\",\n      \"gpu_utilization\": \"Moderate (55-70%) — agent runs main experiment queue; human approves after dry run token measurement and after main GRPO run before committing ablation evals.\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-350 (experiment orchestration, learning curve analysis, reward weight logging, ProUIE comparison analysis, gradient variance derivation review, GDPO integration evaluation, ~1500-3000 turns at $0.08-0.12/turn)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"risk_note\": \"Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130-165 H100-hours total (dry run auto-queued first; main run launched if token length ≤700; checkpoint evals for ablations auto-queued after main run completes)\",\n      \"gpu_utilization\": \"Near-zero idle (~80-90%) — agent queues dry run, measures token lengths, adjusts epoch count if >700 tokens, launches main run, auto-logs per-component F1 learning curves every 50 steps, runs plateau detector and θ sensitivity from saved checkpoints.\",\n      \"timeline\": \"5-8 days with 4× H100 cluster\",\n      \"team\": \"0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger, schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)\",\n      \"claude_api_cost\": \"$175-400 (orchestration, learning curve analysis, gradient variance analysis review, ProUIE comparison, hypothesis evaluation, GDPO complementarity analysis, ~2000-4500 turns)\",\n      \"estimated_gpu_cost\": \"~$325-660\",\n      \"speed_bottleneck\": \"Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging adds minimal overhead. Learning curve generation and θ sensitivity eval are automated and gated on the main run completing.\",\n      \"risk_note\": \"Dry run mandatory first: agent auto-measures token lengths on 50 ACE2005 examples. If >700 tokens, reduces epoch count 30% before full training. Plateau detector monitors all three components (F1_i improvement <1% over 200 steps triggers weight floor activation at ε=0.1). If adaptive weight update produces weight collapse (one component reaches w>0.8 for >100 consecutive steps), agent logs alert and applies weight floor ε=0.1 on all components. Component F1 divergence (any component leads joint F1 by >20 points for 3 consecutive checkpoints) triggers auto-checkpoint and pause. θ sensitivity (θ ∈ {0.6, 0.7, 0.8}) auto-evaluated from saved checkpoints after main run.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date; commitment deadline August 2, 2026; acceptance notification August 20, 2026. Feasibility note: even for auto-research mode (5-8 day GPU timeline), producing a submission-quality paper by May 25 requires the full 16 days with zero margin — dry-run gate Days 1-2, main training Days 3-7, analysis Days 8-10, writing and revision Days 11-15, leaving no buffer for setbacks. SPARD, VCRL, and MAESTRO citations and the Contribution 2 reframing are required before submission and must be incorporated during writing days. The three contributions — reward decomposition extending ProUIE, adaptive weighting application to IE skill hierarchy extending SPARD/APEX/arXiv:2509.11452, and gradient variance theory as IE-domain analysis — are individually incremental extensions of prior work; the learning curve diagnostic is novel for IE but supports the method rather than constituting the core method. The Findings track is the realistic target given this contribution scope. Main track targeting requires stronger standalone theoretical novelty or substantially larger empirical improvement over the Findings threshold.)\",\n    \"ACL 2027 (ARR February 2027 cycle — comfortable fallback for all modes, and primary target for manual mode with 3-4 month timeline. The extended timeline allows: (a) stronger empirical coverage (additional datasets, further ablation), (b) optional GDPO+adaptive-weight combination experiment as a concrete future-direction follow-up, (c) tighter theoretical integration with arXiv:2602.14872's relay regime framework. Note: the August 2026 ARR cycle commits to EACL 2027, not EMNLP 2026 — this is verified from aclrollingreview.org/dates.)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose piecewise conditioning as the mechanism; does not cover RAMS/WikiEvents/MAVEN\",\n    \"SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility (arXiv:2604.07837, April 2026) — introduces PAWA (Progress-Aware Weight Adaptation) for reward-component-level dynamic weighting and RADR (Reward-Attributed Data Rebalancing) for data-category rebalancing; PAWA formula: w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i)/Σ_j(...), Q_t^i = LCB(t)−LCB(t−1) = (μ_t^i−β·σ_t^i)−(μ_{t-1}^i−β·σ_{t-1}^i), up-weighting components making reliable PROGRESS (momentum-based); RADR rebalances four text-generation data categories; applied to open-ended LLM alignment, not IE; no gradient-variance analysis; no span/type/argument decomposition; direct competitor for Contribution 2 — differentiated by formula philosophy (momentum vs. convergence-gap), IE-specific decomposition, and theoretical grounding\",\n    \"VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models (arXiv:2509.19803, September 2025) — uses variance of rollout group rewards as between-sample difficulty indicator for curriculum data selection in math RLVR (low variance = too easy/hard; high variance = optimal); Variance-based Dynamic Sampling selects moderately difficult samples; +4.67 points average on Qwen3-8B-Base over GSPO on five math benchmarks; distinction from proposed work: VCRL uses between-sample variance for difficulty-based data selection; proposed work uses within-sample reward-component variance for skill ordering within IE task structure\",\n    \"RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), curriculum coefficient shifting weight over training, Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition, but for multimodal reasoning not IE\",\n    \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — normalizes each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation to prevent advantage collapse where distinct reward combinations map to identical normalized values; GRPO sums rewards before normalization, losing relative signal; GDPO applied to tool calling (+4.73% BFCL live accuracy), math (+6.3% AIME for DeepSeek-R1-1.5B), coding; NOT applied to IE; orthogonal to proposed adaptive weights (normalization-level fix vs. weighting-level curriculum); combination of GDPO normalization + proposed adaptive weights is a concrete future direction\",\n    \"MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (arXiv:2601.07208, January 2026) — formulates reward scalarization as contextual bandit problem; Conductor network learns dynamic weights from policy hidden states and group-relative advantages via bi-level optimization; applied to open-domain generation across seven benchmarks; more complex than proposed scheme (additional network, bi-level optimization); no IE application; no span/type/argument decomposition\",\n    \"On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for mixed-difficulty RLVR on L-step compositional tasks: when difficulty ratio R = O(1), gradient signals on easier horizons make harder horizons tractable (Theorem 5.2: inter-horizon plateau exponentially shorter than grokking regime); implicit curriculum emerges at task level; does NOT analyze reward decomposition; proposed Contribution 1 extends relay concept from task-level to reward-component-level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness\",\n    \"Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — proves Reward Decomposition Theorem bounding sub-optimality gap between decomposed per-component and joint GRPO optimization; convergence to first-order stationary point at O(1/√T); applied to LVLMs with multiple reward signals (visual reasoning, instruction following, factual accuracy); proposed Contribution 1 complements this by identifying the structural IE-specific property (continuous span-IoU vs. joint span+type conjunction) that makes early-training variance reduction benefit dominate the sub-optimality cost characterized in this theorem\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; proposes hypervolume-guided and gradient-based adaptive weight optimization compatible with GRPO; motivation for adaptive component weights\",\n    \"APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking (high-variance reward components dominating gradients) in multi-objective RL; per-objective priority based on Learning Potential × Conflict Penalty × Progress Need; 10.9× hypervolume vs. static weighting; motivation for variance-aware weight adaptation\",\n    \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary EE baseline that ProUIE fails to beat and the performance target for this work\",\n    \"Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that span boundary detection is prerequisite for entity typing: removing boundary regression causes 36.73% F1 drop for long entities on ACE04; motivation for span-first curriculum\",\n    \"T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence for span-before-type ordering\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)\",\n    \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings) — joint EAE+RE via supervised warm-up + joint RL, single joint reward, excludes NER\",\n    \"R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025) — RE only, single reward\",\n    \"Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025) — scientific NER+RE, single composite reward, no EE\",\n    \"EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)\",\n    \"MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)\",\n    \"RAMS: Multi-Sentence Argument Linking (ACL 2020)\",\n    \"WikiEvents: Document-level Event Argument Extraction (NAACL 2021)\"\n  ],\n  \"description\": \"Joint NER+RE+EE GRPO training fails on event extraction because all existing reward designs treat (span, type) pairs as atomic — providing near-zero gradient when span localization is correct but type classification fails. CurriculumRLVR-IE addresses this with three contributions: (1) a formal gradient variance analysis showing that span-boundary rewards, being continuous span-IoU signals rather than low-probability span-AND-type conjunctions, have systematically lower variance in early training, inducing a span→type→argument sequential convergence (curriculum) as a consequence of reward decomposition rather than explicit scheduling — positioned as a reward-component-level instantiation of the relay regime framework from arXiv:2602.14872 and complementing the Reward Decomposition Theorem of arXiv:2604.19857; (2) an adaptive component weight scheme applied to the IE skill hierarchy — framed as application/instantiation rather than a novel adaptive weighting technique, since SPARD (arXiv:2604.07837, PAWA) already provides reward-component-level adaptive weighting for LLM alignment and MAESTRO (arXiv:2601.07208) provides meta-learning-based scalarization — distinguished from SPARD's momentum-based exponential scheme (which up-weights components making reliable LCB progress) by its convergence-gap formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), where gap-based lagging up-weighting is directly motivated by and consistent with the gradient-variance analysis of Contribution 1, and by its IE-specific span/type/argument structural decomposition absent from all existing adaptive weighting papers; the scheme includes a plateau detector (F1_i improvement <1% over 200 steps triggers convergence regardless of θ) and a θ ∈ {0.6, 0.7, 0.8} sensitivity analysis from saved checkpoints; explicitly distinguished from GDPO (arXiv:2601.05242, ICML 2026), which prevents advantage collapse at the normalization level and is orthogonal/combinable with adaptive aggregation weights; (3) per-component F1 learning curves logged every 50 GRPO steps as a falsifiable empirical test of the curriculum-induction hypothesis; VCRL (arXiv:2509.19803) uses between-sample reward variance for difficulty-based data selection in math — distinct from within-sample reward-component variance for skill ordering in IE. The primary foil is ProUIE (arXiv:2604.10633, Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%), whose SFR piecewise structure (as we infer from Eq. 9-10) weakens argument gradient when trigger matching fails. The backbone is Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run + one main GRPO run + checkpoint-derived ablations, total ~130-165 H100-hours within 200 H100-hour ceiling. Target: EMNLP 2026 Findings via May 25 ARR submission (human-in-loop and auto modes, zero timeline margin — 16 days total with no setbacks); ACL 2027 Main via February 2027 ARR (manual mode and fallback).\",\n  \"project_name\": \"joint_ie_decomposed_rlvr\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"UNCITED ACL 2026 CONCURRENT WORK — CSPO (arXiv:2604.10918, April 2026, accepted ACL 2026) proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation, explicitly framing the problem as 'reward ambiguity' in structured generation and assigning component-specific rewards backpropagated only through relevant tokens. The surface framing is identical to CurriculumRLVR-IE's 'reward atomicity' problem. A reviewer who knows CSPO will immediately flag its absence. The Generator must add CSPO to related work with 1 paragraph distinguishing: (a) span-boundary F1 independent of type label vs. CSPO's structure/style/content decomposition for LaTeX tokens, (b) gradient variance curriculum analysis and adaptive weighting are completely absent from CSPO, (c) CSPO has no sequential skill ordering — it assigns static component-specific rewards without dynamic adaptation.\", \"COMPOUND NOVELTY ATTRITION — By Round 6, the Generator has needed to reframe Contribution 1 as an extension of RuCL/relay regime, reframe Contribution 2 as an 'application/instantiation' after SPARD, and now must add CSPO as yet another partially overlapping prior work for structured-generation reward decomposition. Each addition is individually manageable, but the cumulative effect is that any single contribution, when correctly positioned, reads as incremental. An EMNLP reviewer reading the related work section with SPARD, GDPO, CSPO, RuCL, arXiv:2602.14872, and arXiv:2604.19857 all cited as partial precedents may characterize the paper as 'applying existing techniques to IE' rather than a methodological contribution. The paper needs a single sharpest claim — the gradient variance curriculum analysis for span-IoU continuity vs. type-conjunction probability is the strongest differentiator; the abstract and intro should lead with this, not bury it under the other contributions.\", \"EMPIRICAL RESULT RISK NOT ADEQUATELY SCOPED — The claim 'closes a material fraction of the 20-point ProUIE argument F1 gap' (H4, target >60%) is vague. If Qwen3-8B with the proposed reward reaches 58-62% Argument F1 vs. ProUIE's 52.58% (Qwen3-4B), a reviewer will ask: is the improvement from reward design or from the 4B→8B scale increase? The paper has no same-scale (8B) ProUIE comparison. The Generator should flag this confound more explicitly in the experimental design and add the fixed-weight Qwen3-8B ablation (baseline (c)) as the primary comparison for reward design effect, not the scale-mismatched ProUIE 4B numbers.\", \"EMNLP FINDINGS TIMELINE ZERO-MARGIN — With May 25 ARR deadline confirmed (15 days from today), even auto-research mode (5-8 GPU days) leaves 7-10 days for writing and CSPO/other citation additions. The Generator should explicitly acknowledge in the feasibility note that any single GPU or training failure eliminates the EMNLP 2026 window entirely, making ACL 2027 via February 2027 ARR the de-facto primary target for any non-auto mode.\"]\nFeedback: Round 6 has correctly addressed all Round 5 issues: SPARD is accurately described and differentiated by formula philosophy (momentum vs. convergence-gap), VCRL is cited with the correct between-sample vs. within-sample variance distinction, Contribution 2 is properly reframed as application/instantiation, and EMNLP Findings is the acknowledged realistic target. The technical nucleus remains sound. The single new action required: (1) Add CSPO (arXiv:2604.10918, ACL 2026) to related work — 1 paragraph: CSPO decomposes structured generation rewards by functional component (structure/style/content) for table-to-LaTeX and argues for component-specific backpropagation to resolve 'reward ambiguity'; distinguish by (a) span-boundary F1 independent of type label is a more precise decoupling than CSPO's LaTeX-component boundaries, (b) curriculum theory and adaptive weighting are entirely absent from CSPO, (c) CSPO targets document rendering fidelity not IE structured prediction. Beyond CSPO, two sharpening suggestions that would elevate novelty score above 3/5 without new experiments: (a) Restructure the abstract/intro to lead with the gradient variance curriculum claim as the paper's primary theoretical contribution, citing it as a reward-component-level relay regime (extending arXiv:2602.14872) specifically for IE — this is the strongest differentiator from all prior work; (b) Add an explicit acknowledgment in Section 5 that the scale difference (8B proposed vs. 4B ProUIE) is a confound in the primary ProUIE comparison and that the fixed-weight Qwen3-8B ablation (not ProUIE 4B) is the clean baseline for reward design effect. These changes require only writing revisions — no new experiments.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:37:06.724Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:37:06.724Z",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-10T08:37:06.766Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weighting Induces Sequential Skill Curriculum for Joint NER+RE+EE",
  "core_problem": "GRPO-based information extraction (IE) rewards universally treat (span, type) pairs as atomic structural units: a prediction with the correct span but wrong type label receives the same near-zero reward as a completely missed mention. This atomicity assumption has a precise gradient-theoretic consequence. In early GRPO training when both span detection and type classification are unreliable, atomic rewards produce high-variance gradients: the expected non-zero signal requires simultaneously correct span AND correct type, a low-probability joint event whose probability product makes the reward sparse and noisy. Span-decoupled rewards break this bottleneck — span-boundary F1 is continuous, lower-variance, and receives non-zero gradient even when type is wrong, stabilizing the GRPO objective in early training and allowing span detection to converge first. As span accuracy increases, the type-conditioned component's gradient variance drops (conditioned on correct spans, type prediction becomes a simpler classification problem), creating a span→type→argument sequential convergence structure — an implicit curriculum emerging from reward decomposition rather than explicit scheduling.\n\nProUIE (arXiv:2604.10633, April 2026) provides the clearest empirical evidence for the cost of atomic rewards. Its Stepwise Fine-grained Reward (SFR) for event extraction computes argument-level F1 (F_full) by first matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap. When trigger type or span is wrong, fewer argument pairs match, reducing F_full — and the piecewise penalty (Eq. 9) simultaneously shifts gradient emphasis toward trigger correction rather than argument assignment. The result, as we infer from SFR's structure (ProUIE does not explicitly diagnose the mechanism), is that argument role learning receives weakened gradient signal whenever trigger detection fails. ProUIE reports ACE2005 Trigger F1=70.65% and Argument F1=52.58% versus InstructUIE (Flan-T5-XXL, 11B) at 77.13%/72.94% — a 20-point argument F1 deficit. ProUIE's authors attribute this to 'unified generation setting and reward configuration' and call for 'more appropriate reward design,' but do not identify which structural feature of SFR causes the gap.\n\nThe core missing ingredient is a principled span-boundary reward that is decoupled from type label, accompanied by a formal justification showing why this decomposition creates stable sequential skill acquisition during GRPO training. No published GRPO-IE work provides either: ProUIE's SFR, R1-RE, R2GRPO, and EXTRACT-0 all use atomic (span, type) rewards; and no GRPO-IE paper has analyzed reward decomposition through the lens of gradient variance or curriculum induction.",
  "opportunity": "ProUIE's acknowledged performance gap ('more appropriate reward design') and its documented 20-point argument F1 deficit on ACE2005 create a precisely bounded opportunity with three distinct axes — two empirical and one theoretical — none of which existing work covers.\n\n**Axis 1 (Theoretical — primary novelty)**: No published work has formally analyzed how decomposing IE rewards by skill type (span detection vs. type classification vs. relational assignment) induces sequential skill convergence in GRPO training. The closest parallel is RuCL (arXiv:2602.21628), which uses tiered rubric rewards in GRPO for multimodal reasoning and provides a gradient variance decomposition in Appendix B showing that reliable foundational reward components reduce early-training gradient variance. For IE, the analogous argument requires showing that span-boundary F1 has systematically lower reward variance than joint (span, type) F1 in early training — because span IoU is a continuous signal while joint correctness is a low-probability conjunction — and that this variance gap induces a span→type→argument convergence ordering. Making this argument formally for IE, supported by per-component learning curves, is a genuine theoretical contribution gap. The recent 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) formally proves a relay regime for task-level difficulty ordering but does not analyze reward-component-level difficulty ordering within a single task type — the proposed analysis applies the relay regime concept at a different level of abstraction. The Reward Decomposition Theorem of arXiv:2604.19857 bounds the sub-optimality gap between decomposed and joint GRPO optimization but does not identify which structural properties of the reward signal (continuous span-IoU vs. joint conjunction) determine whether decomposition is beneficial — our variance analysis fills that gap.\n\n**Axis 2 (Algorithmic — secondary novelty)**: Existing GRPO-IE work uses fixed reward weights. The multi-objective RL literature (arXiv:2509.11452) has proven that fixed-weight scalarization is provably suboptimal for non-convex Pareto fronts, and APEX (arXiv:2601.06574) has identified 'variance hijacking' — high-variance reward components dominating gradients — as the mechanism behind fixed-weight failures. GDPO (arXiv:2601.05242, ICML 2026) addresses the related problem of advantage collapse via per-reward normalization but uses fixed aggregation weights. SPARD (arXiv:2604.07837, April 2026) introduces PAWA for reward-component-level adaptive weighting at the LLM alignment level, but applies to open-ended generation with LLM-judge rewards and provides no IE-specific structural decomposition or gradient-variance theoretical basis. MAESTRO (arXiv:2601.07208) formulates reward scalarization as a meta-learning bandit problem, also for open-domain generation. Contribution 2's novelty is therefore NOT a novel adaptive weighting algorithm per se, but the application and instantiation of convergence-gap weighting to the specific span/type/argument IE hierarchy, with the formula design directly derived from the gradient-variance analysis of Contribution 1. The gap-based formula max(ε, θ−F1_i)/σ_i is philosophically opposite to SPARD's momentum-based scheme (which up-weights components making reliable progress, risking perpetuating the dominance of whichever component improves first) and is chosen because the gradient-variance analysis identifies the gap to convergence — not the rate of progress — as the theoretically relevant quantity for curriculum enforcement. All GRPO-IE papers (ProUIE, R1-RE, R2GRPO, EXTRACT-0) use fixed weights; none applies adaptive weighting to the span/type/argument hierarchy with a structural motivation.\n\n**Axis 3 (Empirical — benchmark coverage)**: ProUIE evaluates EE on only ACE2005, CASIE, and PHEE; no RLVR-IE paper has assessed OOD event argument generalization on RAMS (139 event types, 65 argument roles, document-level), WikiEvents (50 event types, document-level), or MAVEN (168 event types, general-domain trigger detection). The proposed span-decoupled curriculum reward addresses ProUIE's diagnosed failure mode and directly fills all three gaps.",
  "landscape": "**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. When trigger detection fails, F_full shrinks (fewer argument pairs match) and the gradient emphasis shifts to trigger correction rather than argument assignment — producing, as we infer from the structural piecewise design, weakened argument-learning signal during trigger training. ProUIE does not explicitly state this mechanism; the authors attribute weak EE to 'unified generation setting and reward configuration' and call for 'stronger event-specific modeling and more appropriate reward design' in limitations. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Our work differentiates from ProUIE on three axes: (1) span-boundary F1 computed independently of type label with formal gradient-variance justification; (2) dynamic weight adaptation replacing fixed weights; (3) per-component learning curve analysis.\n\n**SPARD** (arXiv:2604.07837, April 2026) proposes a self-paced curriculum for RL alignment via two components: **PAWA (Progress-Aware Weight Adaptation)**, which adjusts reward-component weights dynamically at training time, and **RADR (Reward-Attributed Data Rebalancing)**, which rebalances training data categories based on reward-attributed utility. PAWA operates at the reward-component level: the weight update is w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i) / Σ_j(w_t^{r,j}·exp(η·Q_t^j)), where Q_t^i = (μ_t^i − β·σ_t^i) − (μ_{t-1}^i − β·σ_{t-1}^i) is a Reliable Performance Gain based on the Lower Confidence Bound (LCB) principle — the exponential up-weighting fires when the LCB estimate of mean reward improvement is positive, i.e., when a component is making reliable *progress*. RADR rebalances data categories (Code, Knowledge QA, Text Transformation, Creative Writing). SPARD applies to open-ended LLM alignment with LLM-judge rewards across text generation domains; it does not address structured prediction or IE. Three differentiations from the proposed scheme: (a) **Formula philosophy**: SPARD's PAWA up-weights components making reliable *progress* (momentum), whereas our scheme w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) up-weights components that are *lagging* below the convergence target — enforcing curriculum by redistributing weight toward gaps rather than reinforcing momentum. In later training when span detection improves, SPARD might continue up-weighting span (it keeps showing LCB progress), while ours explicitly shifts weight to type and argument. (b) **IE structural decomposition**: SPARD applies to heterogeneous open-domain capabilities; the proposed scheme is designed specifically around the span/type/argument IE hierarchy and the structural insight that span-IoU is a continuous signal while type-correctness is a conjunction, which is absent from SPARD. (c) **Gradient-variance theoretical basis**: SPARD provides no formal analysis of why reward components have different variance profiles or why a particular weight ordering should emerge during training — the paper acknowledges that nonlinear objective interdependencies are not theoretically analyzed. The proposed Contribution 1 provides this analysis specifically for IE: span-IoU continuity vs. joint span+type conjunction explains the early-training variance differential that directly motivates the gap-based (not momentum-based) weighting formula. Note: SPARD's RADR data rebalancing is orthogonal to our approach (we do not modify data selection), but PAWA is genuine reward-component-level weighting — the differentiation rests on formula philosophy, IE-specific decomposition, and theoretical grounding, not on data-vs-reward-component scope.\n\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with a two-tier decomposed reward (foundational rubrics + advanced rubrics) for multimodal reasoning, with a curriculum coefficient progressively shifting weight from easy to hard rubrics. Appendix B provides gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. RuCL achieves +7.83% average improvement across seven benchmarks. It is the methodological parallel most relevant to our curriculum-induction claim — but for multimodal reasoning, not IE, and without the span-boundary decoupling insight or IE-specific convergence analysis.\n\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses a different failure mode of multi-reward GRPO: advantage collapse. In standard GRPO, rewards are summed before group-wise normalization (r_sum = r₁+...+rₙ; A = (r_sum − mean)/std), causing distinct reward combinations — e.g., (span=0, type=1), (span=0, type=2), and (span=1, type=2) — to map to identical normalized advantage values, destroying the relative signal between reward types. GDPO decouples normalization: each reward's advantage is normalized independently (A_i = (r_i − mean_i)/std_i) before summation and batch-wise renormalization. This preserves the relative differences between reward combinations at the normalization level. The proposed adaptive weight scheme is orthogonal: it operates after per-reward advantages are computed, adjusting the relative aggregation weights w_i(t) based on convergence progress rather than modifying the normalization step. The two mechanisms can be combined directly — GDPO normalization applied to each span/type/argument advantage, followed by convergence-progress adaptive aggregation weights — and this combination is a natural future direction. GDPO was tested on tool calling (Berkeley BFCL-v3: +4.73% live accuracy over GRPO), math, and coding, using DeepSeek-R1-1.5B and Qwen3-4B; it has not been applied to IE.\n\n**MAESTRO** (arXiv:2601.07208, January 2026) formulates reward scalarization as a contextual bandit problem, training a lightweight Conductor network that uses the policy's terminal hidden states to dynamically adapt reward weights, optimized via a bi-level scheme with group-relative advantages as meta-reward signal. Applied to open-domain generation across seven benchmarks, MAESTRO outperforms static multi-objective baselines. Compared to the proposed adaptive weight scheme, MAESTRO's bi-level optimization with a separate Conductor network introduces significant additional complexity; the proposed scheme uses a simple convergence-progress formula (max(ε, θ−F1_i)/σ_i) interpretable directly from the gradient-variance analysis, with no additional network parameters and no additional computational overhead over standard GRPO. Neither MAESTRO nor SPARD has been applied to IE or provides structural analysis of span/type/argument reward decomposition.\n\n**VCRL** (arXiv:2509.19803, September 2025) uses the variance of rollout group rewards as a real-time indicator of between-sample difficulty in RLVR for math reasoning: low variance indicates a sample is too easy or too hard, high variance indicates optimally difficult samples. VCRL drives curriculum via variance-based dynamic sampling to control training batch quality, achieving +4.67 points average on Qwen3-8B-Base over GSPO on five math benchmarks. The variance signal in VCRL is between-sample (which training examples to select based on predicted difficulty); the proposed work's variance analysis is within-sample (which reward components have lower variance within a single IE prediction, determining which skill should converge first). These are different uses of reward variance at different levels of abstraction and serve complementary purposes.\n\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally analyzes RLVR training dynamics on L-step compositional reasoning tasks, proving that mixed-difficulty training enters a relay regime when the difficulty ratio R = O(1) (smooth spectrum): persistent gradient signals on easier horizons make slightly harder horizons tractable, producing an implicit curriculum without explicit scheduling (Theorem 5.2 bounds inter-horizon plateau at Õ(L_max/η) vs. exponentially longer in the grokking regime). Crucially, the relay regime is analyzed at the task level — different training instances of different horizon lengths L₁ < L₂ < L_max — and the framework does not address reward decomposition. The proposed Contribution 1 applies the relay regime concept at a different level of analysis: within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, and the continuous span-IoU signal provides the 'smooth gradient handoff' that prevents prolonged plateaus during type and argument learning. This reward-component-level relay is a conceptual extension of the task-level relay regime, not a direct instantiation, and constitutes the novel contribution of Contribution 1 beyond the original framework.\n\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857, April 2026) proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed per-component optimization and joint optimization for GRPO with composite rewards in LVLMs, establishing convergence to a first-order stationary point at rate O(1/√T). Their result characterizes when sequential or parallel per-component optimization loses performance relative to joint training. The proposed Contribution 1 is complementary: rather than bounding the worst-case sub-optimality cost of decomposition in general, it identifies the specific structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that determines whether the decomposed reward yields lower early-training gradient variance. Together, the two analyses bracket the expected behavior: arXiv:2604.19857 establishes that decomposed GRPO is guaranteed to converge (sub-optimality is bounded), and the proposed variance analysis identifies why for IE rewards specifically the early-training variance reduction from span continuity is expected to dominate the sub-optimality cost.\n\n**Dynamic reward weighting** (arXiv:2509.11452, 2025) proves that fixed-weight scalarization fails on non-convex multi-objective RL Pareto fronts and proposes hypervolume-guided adaptive weight adjustment compatible with GRPO. **APEX** (arXiv:2601.06574, 2026) identifies 'variance hijacking' in multi-objective RL and proposes per-objective priority based on Learning Potential × Conflict Penalty × Progress Need. Neither paper applies adaptive weighting to IE or analyzes the span-type variance differential.\n\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation but do not analyze training dynamics or reward signal ordering in RL.\n\n**REAR** (EMNLP 2025 Findings) applies DeepSeek-R1-style RL to joint EAE+RE via supervised warm-up + joint RL, single joint reward; excludes NER and trigger detection. **R1-RE** (arXiv:2507.04642, July 2025) is RLVR for RE only, single reward, strong OOD robustness. **R2GRPO** (arXiv:2505.22068, May 2025) applies GRPO to scientific NER+RE with a composite reward, no EE and no substructure decomposition. **EXTRACT-0** (arXiv:2509.22906, September 2025) uses 7B LoRA+GRPO with semantic similarity reward for document extraction. **KnowCoder** (ACL 2024) achieves state-of-the-art IE via code-style schema SFT. **GoLLIE** (ICLR 2024) improves zero-shot IE via annotation guideline following.\n\nNo published GRPO-IE paper provides span-boundary reward independent of type label, formal gradient-variance curriculum justification for IE reward decomposition, or adaptive weighting applied to the span/type/argument IE skill hierarchy, as of May 2026.",
  "approach": "We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) and a span-boundary-decoupled reward with adaptive component weighting. The paper has three contributions: a theoretical contribution (gradient variance analysis), an algorithmic contribution (adaptive weights replacing fixed weights, applied to the IE skill hierarchy), and an empirical contribution (per-component learning curves as diagnostic evidence for curriculum induction).\n\n**Contribution 1 — Gradient Variance Analysis (theoretical)**:\nWe formalize the curriculum-induction property of span-decoupled rewards. In early GRPO training, let p_s = P(span correct) and p_t = P(type correct | span) be the model's per-token span detection rate and type accuracy given correct span. For standard atomic rewards (joint span+type), the non-zero reward probability is p_s · p_t — low in early training because it requires a conjunction. For span-decoupled rewards, the span component alone has non-zero probability p_s > p_s · p_t. The gradient variance of the span-decoupled reward is:\n\nVar(∇R_decomposed) = α₁²·Var(∇F1_span) + α₂²·Var(∇F1_type|span) + α₃²·Var(∇F1_arg) + cross terms\n\nWe show that when p_s < 0.5 (early training), Var(∇R_decomposed) < Var(∇R_atomic) because α₁·∇F1_span provides a stable non-zero signal that reduces total gradient variance, following the same framework as RuCL's Appendix B but derived for continuous span-IoU rewards rather than binary rubrics. As span detection improves (p_s → 0.7+), the type-conditioned component's gradient variance decreases (conditioning on correct spans reduces label ambiguity), and argument F1 receives cleaner signal. This creates a span→type→argument sequential convergence ordering that is a direct consequence of reward decomposition — not an explicitly scheduled curriculum.\n\nWe position this analysis in relation to two concurrent theoretical frameworks. First, 'On the Learning Dynamics of RLVR at the Edge of Competence' (arXiv:2602.14872) proves a relay regime for task-level difficulty ordering: when the training set contains tasks of smoothly graduated horizons L₁ < L₂ < L_max, gradient dominance is handed off from easy to hard tasks, producing implicit curriculum emergence. Our analysis applies the relay concept at a different level — within a single IE task type, the reward components (span-IoU, type-conditioned F1, argument F1) form a difficulty ordering analogous to easy-to-hard horizons, with span-IoU continuity providing the smooth gradient handoff. This is a reward-component-level relay, not a task-level relay, and the paper explicitly distinguishes these two levels. Second, arXiv:2604.19857 proves a Reward Decomposition Theorem bounding the sub-optimality gap between decomposed and joint GRPO optimization at O(1/√T). Our variance analysis complements this bound: arXiv:2604.19857 characterizes the worst-case cost of decomposition (sub-optimality); our analysis identifies the structural property of IE rewards — span-IoU continuity vs. joint span+type conjunction — that makes the early-training variance reduction benefit dominate this cost in practice. The testable prediction is per-component learning curves that show span F1 converging before type-conditioned F1, which converges before argument F1.\n\n**Contribution 2 — Adaptive Component Weights for IE Skill Hierarchy (algorithmic)**:\nContribution 2's novelty is the APPLICATION and instantiation of convergence-gap weighting to the specific span/type/argument IE skill hierarchy, with the formula design directly derived from the gradient-variance analysis of Contribution 1 — not a novel adaptive weighting technique per se. SPARD (arXiv:2604.07837) has already demonstrated reward-component-level adaptive weighting for LLM alignment via PAWA, MAESTRO (arXiv:2601.07208) via meta-learning, and arXiv:2509.11452 + APEX are the motivating references for why fixed weights are suboptimal. The contribution here is the IE-specific instantiation: the choice of gap-based weighting (ours) over momentum-based weighting (SPARD's PAWA) is theoretically motivated by Contribution 1's analysis. SPARD's PAWA up-weights components making reliable progress (positive LCB improvement ΔQ_t > 0), which risks perpetuating dominance of whichever component improves first. Our scheme up-weights components that are lagging below the convergence target, which directly enforces the span→type→argument ordering identified by the gradient-variance analysis — once span F1 approaches θ, weight redistributes to type, and once type approaches θ, weight redistributes to argument. The variance normalization term (dividing by σ_i(t)) further ensures that components with reliable (low-variance) gradients receive appropriate weight even when converging, preventing gradient noise from high-variance components hijacking the curriculum. No published GRPO-IE paper applies any form of adaptive weighting to the span/type/argument hierarchy; this instantiation is a genuine contribution at the IE domain level.\n\nReplacing fixed weights (0.4/0.3/0.3) with a dynamic scheme motivated by arXiv:2509.11452's finding that fixed scalarization is suboptimal and APEX's identification of variance hijacking. At each evaluation checkpoint t, let F1_i(t) be the current F1 for component i ∈ {span, type, arg} and σ_i(t) be its rolling standard deviation over the last 50 steps. The adaptive weight:\n\nw_i(t) = max(ε, θ − F1_i(t)) / σ_i(t)\nnormalized so Σᵢ wᵢ(t) = 1, with ε=0.05 preventing zero weights, θ=0.7 as the convergence target.\n\nThis rule assigns higher weight to components that are lagging convergence (below θ=0.7) and lower variance (reliable gradient signal), preventing variance hijacking from the highest-variance component. Early in training, span typically has lower variance and below-target F1, so it receives high weight; once span F1 exceeds 0.7, weight shifts to type; once type converges, weight shifts to argument.\n\n**Relationship to GDPO**: GDPO (arXiv:2601.05242, ICML 2026) addresses a complementary but distinct normalization-level failure: advantage collapse, where summing rewards before group-wise normalization maps distinct reward combinations (e.g., span=0,type=1 vs. span=1,type=0) to identical normalized advantage values. GDPO's fix — normalizing each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation — operates at the normalization step. The proposed adaptive weights operate after per-reward advantages are computed, adjusting relative aggregation weights based on convergence progress. The two mechanisms are orthogonal and can be combined: applying GDPO normalization to each span/type/argument advantage before applying the convergence-progress adaptive weights would simultaneously prevent advantage collapse and enforce the curriculum. This combination is identified as a concrete future direction.\n\n**Secondary convergence criterion (θ sensitivity)**: The convergence target θ=0.7 assumes argument F1 will approach 70%+ during training (InstructUIE achieves 72.94% at 11B; the proposed system targets >60% at 8B, making this uncertain). If argument F1 plateaus below θ, the argument component would persistently receive high weight, risking the variance hijacking the scheme is designed to prevent. To address this: (a) a plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, regardless of whether F1_i has reached θ — converged-by-plateau components have their weight set to ε; (b) sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} is conducted via checkpoint evaluation on the saved main-run checkpoints, requiring no additional full training runs. If plateau detection triggers for argument before θ, weight redistribution favors whichever remaining component has the largest convergence gap and lowest variance.\n\n**Reward formula with adaptive weights**:\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification)\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong\n\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps.\n\n**Contribution 3 — Learning Curve Diagnostics (empirical)**:\nPer-component F1 is logged every 50 GRPO steps throughout training, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves. The predicted pattern (span converges first, then type, then argument) is treated as an empirically testable consequence of the gradient variance analysis. Deviation from this pattern would falsify the curriculum-induction hypothesis and require reanalysis. This is a diagnostic contribution: even if final numbers are modest, the learning curves themselves constitute evidence about GRPO training dynamics for IE that no prior work has published.\n\n**Cascade failure reframing (addressing reviewer concern)**:\nWe do not attribute to ProUIE the claim that wrong trigger type produces near-zero argument reward — ProUIE makes no such explicit statement. Our paper presents this as an inference: ProUIE's SFR structure (Eq. 9-10) implies that trigger group mismatch reduces F_full by limiting argument pair matching coverage, and the piecewise penalty shifts gradient emphasis toward trigger correction rather than argument assignment. The specific mechanism is our analysis, not ProUIE's diagnosis. ProUIE's authors observe the symptom (weak EE, especially argument F1) and call for 'more appropriate reward design'; our paper provides the mechanism and the fix.\n\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER).\n\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\n\n**Output format**: Code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures actual token length distribution before full training; all compute commitments gated on this measurement. Expected 300-600 tokens per example.\n\n**Baselines and comparison structure**:\n(a) SFT baselines: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\n(b) Single-reward GRPO: joint extraction F1 as the only reward, same Qwen3-8B — isolates reward decomposition effect\n(c) Fixed-weight decomposed GRPO (α₁=0.4, α₂=0.3, α₃=0.3 throughout): ablation isolating adaptive weight contribution from span decoupling contribution\n(d) α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5): derived from checkpoint evaluation, not a full new run — directly tests whether span-boundary decoupling is the essential design choice\n(e) ProUIE published ACE2005 numbers (Qwen3-4B, scale difference noted explicitly)\n(f) OOD: RAMS, WikiEvents, MAVEN (zero-shot cross-distribution generalization, sentence→document shift explicitly noted as confound; analysis identifies which document-level aspects hurt: coreference resolution for cross-sentence arguments, multi-sentence span detection)\n\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS (300-600 tokens) and WikiEvents (400-800 tokens) fit in full-document inference. OOD results are framed as 'zero-shot cross-distribution generalization from sentence-level training to document-level inference.' Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements. This converts the confound from a limitation to an analytical contribution.\n\n**Key testable hypotheses**:\nH1 (curriculum): Per-component learning curves show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics.\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute — isolates span-boundary decoupling contribution.\nH3 (adaptive vs. fixed): Adaptive weight scheme produces higher Argument F1 than fixed-weight decomposed GRPO — isolates adaptive weighting contribution.\nH4 (ProUIE gap): Decomposed GRPO closes a material fraction of the 20-point argument F1 gap vs. InstructUIE (target: Argument F1 >60% at 8B scale).",
  "resource_estimate": {
    "compute_note": "Single-run-primary design gated on 50-example dry run. Output token length: 300-600 tokens per example for joint NER+RE+EE with CoT (corrected from earlier 100-300 estimate). Dry run measures actual distribution before full training. Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.",
    "manual": {
      "gpu_hours": "~130-160 H100-hours total: dry run (~2 H100-hours) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours at ≤400 token output measured by dry run) + fixed-weight ablation from checkpoint evaluation (~20-25 H100-hours, not a full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours, draws on saved checkpoints). Total ≤165 H100-hours — within 200 H100-hour ceiling.",
      "gpu_utilization": "Low (20-35%) — GPUs idle during gradient variance analysis derivation, learning curve interpretation, reward verifier implementation, and writing.",
      "timeline": "3-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$325-660 (at $2.50-4/hr H100 cloud on-demand)"
    },
    "human_in_loop": {
      "gpu_hours": "~130-165 H100-hours total (same single-run-primary design; agent queues dry run first, then main GRPO run; α₁=0, fixed-weight, and θ sensitivity ablations derived from checkpoint eval, not new runs)",
      "gpu_utilization": "Moderate (55-70%) — agent runs main experiment queue; human approves after dry run token measurement and after main GRPO run before committing ablation evals.",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-350 (experiment orchestration, learning curve analysis, reward weight logging, ProUIE comparison analysis, gradient variance derivation review, GDPO integration evaluation, ~1500-3000 turns at $0.08-0.12/turn)",
      "estimated_gpu_cost": "~$325-660",
      "risk_note": "Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes."
    },
    "auto_research": {
      "gpu_hours": "~130-165 H100-hours total (dry run auto-queued first; main run launched if token length ≤700; checkpoint evals for ablations auto-queued after main run completes)",
      "gpu_utilization": "Near-zero idle (~80-90%) — agent queues dry run, measures token lengths, adjusts epoch count if >700 tokens, launches main run, auto-logs per-component F1 learning curves every 50 steps, runs plateau detector and θ sensitivity from saved checkpoints.",
      "timeline": "5-8 days with 4× H100 cluster",
      "team": "0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger, schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)",
      "claude_api_cost": "$175-400 (orchestration, learning curve analysis, gradient variance analysis review, ProUIE comparison, hypothesis evaluation, GDPO complementarity analysis, ~2000-4500 turns)",
      "estimated_gpu_cost": "~$325-660",
      "speed_bottleneck": "Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging adds minimal overhead. Learning curve generation and θ sensitivity eval are automated and gated on the main run completing.",
      "risk_note": "Dry run mandatory first: agent auto-measures token lengths on 50 ACE2005 examples. If >700 tokens, reduces epoch count 30% before full training. Plateau detector monitors all three components (F1_i improvement <1% over 200 steps triggers weight floor activation at ε=0.1). If adaptive weight update produces weight collapse (one component reaches w>0.8 for >100 consecutive steps), agent logs alert and applies weight floor ε=0.1 on all components. Component F1 divergence (any component leads joint F1 by >20 points for 3 consecutive checkpoints) triggers auto-checkpoint and pause. θ sensitivity (θ ∈ {0.6, 0.7, 0.8}) auto-evaluated from saved checkpoints after main run."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date; commitment deadline August 2, 2026; acceptance notification August 20, 2026. Feasibility note: even for auto-research mode (5-8 day GPU timeline), producing a submission-quality paper by May 25 requires the full 16 days with zero margin — dry-run gate Days 1-2, main training Days 3-7, analysis Days 8-10, writing and revision Days 11-15, leaving no buffer for setbacks. SPARD, VCRL, and MAESTRO citations and the Contribution 2 reframing are required before submission and must be incorporated during writing days. The three contributions — reward decomposition extending ProUIE, adaptive weighting application to IE skill hierarchy extending SPARD/APEX/arXiv:2509.11452, and gradient variance theory as IE-domain analysis — are individually incremental extensions of prior work; the learning curve diagnostic is novel for IE but supports the method rather than constituting the core method. The Findings track is the realistic target given this contribution scope. Main track targeting requires stronger standalone theoretical novelty or substantially larger empirical improvement over the Findings threshold.)",
    "ACL 2027 (ARR February 2027 cycle — comfortable fallback for all modes, and primary target for manual mode with 3-4 month timeline. The extended timeline allows: (a) stronger empirical coverage (additional datasets, further ablation), (b) optional GDPO+adaptive-weight combination experiment as a concrete future-direction follow-up, (c) tighter theoretical integration with arXiv:2602.14872's relay regime framework. Note: the August 2026 ARR cycle commits to EACL 2027, not EMNLP 2026 — this is verified from aclrollingreview.org/dates.)"
  ],
  "level": "top-tier",
  "key_references": [
    "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose piecewise conditioning as the mechanism; does not cover RAMS/WikiEvents/MAVEN",
    "SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility (arXiv:2604.07837, April 2026) — introduces PAWA (Progress-Aware Weight Adaptation) for reward-component-level dynamic weighting and RADR (Reward-Attributed Data Rebalancing) for data-category rebalancing; PAWA formula: w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i)/Σ_j(...), Q_t^i = LCB(t)−LCB(t−1) = (μ_t^i−β·σ_t^i)−(μ_{t-1}^i−β·σ_{t-1}^i), up-weighting components making reliable PROGRESS (momentum-based); RADR rebalances four text-generation data categories; applied to open-ended LLM alignment, not IE; no gradient-variance analysis; no span/type/argument decomposition; direct competitor for Contribution 2 — differentiated by formula philosophy (momentum vs. convergence-gap), IE-specific decomposition, and theoretical grounding",
    "VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models (arXiv:2509.19803, September 2025) — uses variance of rollout group rewards as between-sample difficulty indicator for curriculum data selection in math RLVR (low variance = too easy/hard; high variance = optimal); Variance-based Dynamic Sampling selects moderately difficult samples; +4.67 points average on Qwen3-8B-Base over GSPO on five math benchmarks; distinction from proposed work: VCRL uses between-sample variance for difficulty-based data selection; proposed work uses within-sample reward-component variance for skill ordering within IE task structure",
    "RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), curriculum coefficient shifting weight over training, Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition, but for multimodal reasoning not IE",
    "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — normalizes each reward's advantage independently (A_i = (r_i − mean_i)/std_i) before aggregation to prevent advantage collapse where distinct reward combinations map to identical normalized values; GRPO sums rewards before normalization, losing relative signal; GDPO applied to tool calling (+4.73% BFCL live accuracy), math (+6.3% AIME for DeepSeek-R1-1.5B), coding; NOT applied to IE; orthogonal to proposed adaptive weights (normalization-level fix vs. weighting-level curriculum); combination of GDPO normalization + proposed adaptive weights is a concrete future direction",
    "MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (arXiv:2601.07208, January 2026) — formulates reward scalarization as contextual bandit problem; Conductor network learns dynamic weights from policy hidden states and group-relative advantages via bi-level optimization; applied to open-domain generation across seven benchmarks; more complex than proposed scheme (additional network, bi-level optimization); no IE application; no span/type/argument decomposition",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for mixed-difficulty RLVR on L-step compositional tasks: when difficulty ratio R = O(1), gradient signals on easier horizons make harder horizons tractable (Theorem 5.2: inter-horizon plateau exponentially shorter than grokking regime); implicit curriculum emerges at task level; does NOT analyze reward decomposition; proposed Contribution 1 extends relay concept from task-level to reward-component-level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness",
    "Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — proves Reward Decomposition Theorem bounding sub-optimality gap between decomposed per-component and joint GRPO optimization; convergence to first-order stationary point at O(1/√T); applied to LVLMs with multiple reward signals (visual reasoning, instruction following, factual accuracy); proposed Contribution 1 complements this by identifying the structural IE-specific property (continuous span-IoU vs. joint span+type conjunction) that makes early-training variance reduction benefit dominate the sub-optimality cost characterized in this theorem",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; proposes hypervolume-guided and gradient-based adaptive weight optimization compatible with GRPO; motivation for adaptive component weights",
    "APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking (high-variance reward components dominating gradients) in multi-objective RL; per-objective priority based on Learning Potential × Conflict Penalty × Progress Need; 10.9× hypervolume vs. static weighting; motivation for variance-aware weight adaptation",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary EE baseline that ProUIE fails to beat and the performance target for this work",
    "Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that span boundary detection is prerequisite for entity typing: removing boundary regression causes 36.73% F1 drop for long entities on ACE04; motivation for span-first curriculum",
    "T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence for span-before-type ordering",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)",
    "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings) — joint EAE+RE via supervised warm-up + joint RL, single joint reward, excludes NER",
    "R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025) — RE only, single reward",
    "Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025) — scientific NER+RE, single composite reward, no EE",
    "EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "RAMS: Multi-Sentence Argument Linking (ACL 2020)",
    "WikiEvents: Document-level Event Argument Extraction (NAACL 2021)"
  ],
  "description": "Joint NER+RE+EE GRPO training fails on event extraction because all existing reward designs treat (span, type) pairs as atomic — providing near-zero gradient when span localization is correct but type classification fails. CurriculumRLVR-IE addresses this with three contributions: (1) a formal gradient variance analysis showing that span-boundary rewards, being continuous span-IoU signals rather than low-probability span-AND-type conjunctions, have systematically lower variance in early training, inducing a span→type→argument sequential convergence (curriculum) as a consequence of reward decomposition rather than explicit scheduling — positioned as a reward-component-level instantiation of the relay regime framework from arXiv:2602.14872 and complementing the Reward Decomposition Theorem of arXiv:2604.19857; (2) an adaptive component weight scheme applied to the IE skill hierarchy — framed as application/instantiation rather than a novel adaptive weighting technique, since SPARD (arXiv:2604.07837, PAWA) already provides reward-component-level adaptive weighting for LLM alignment and MAESTRO (arXiv:2601.07208) provides meta-learning-based scalarization — distinguished from SPARD's momentum-based exponential scheme (which up-weights components making reliable LCB progress) by its convergence-gap formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), where gap-based lagging up-weighting is directly motivated by and consistent with the gradient-variance analysis of Contribution 1, and by its IE-specific span/type/argument structural decomposition absent from all existing adaptive weighting papers; the scheme includes a plateau detector (F1_i improvement <1% over 200 steps triggers convergence regardless of θ) and a θ ∈ {0.6, 0.7, 0.8} sensitivity analysis from saved checkpoints; explicitly distinguished from GDPO (arXiv:2601.05242, ICML 2026), which prevents advantage collapse at the normalization level and is orthogonal/combinable with adaptive aggregation weights; (3) per-component F1 learning curves logged every 50 GRPO steps as a falsifiable empirical test of the curriculum-induction hypothesis; VCRL (arXiv:2509.19803) uses between-sample reward variance for difficulty-based data selection in math — distinct from within-sample reward-component variance for skill ordering in IE. The primary foil is ProUIE (arXiv:2604.10633, Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%), whose SFR piecewise structure (as we infer from Eq. 9-10) weakens argument gradient when trigger matching fails. The backbone is Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run + one main GRPO run + checkpoint-derived ablations, total ~130-165 H100-hours within 200 H100-hour ceiling. Target: EMNLP 2026 Findings via May 25 ARR submission (human-in-loop and auto modes, zero timeline margin — 16 days total with no setbacks); ACL 2027 Main via February 2027 ARR (manual mode and fallback).",
  "project_name": "joint_ie_decomposed_rlvr",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["UNCITED ACL 2026 CONCURRENT WORK — CSPO (arXiv:2604.10918, April 2026, accepted ACL 2026) proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation, explicitly framing the problem as 'reward ambiguity' in structured generation and assigning component-specific rewards backpropagated only through relevant tokens. The surface framing is identical to CurriculumRLVR-IE's 'reward atomicity' problem. A reviewer who knows CSPO will immediately flag its absence. The Generator must add CSPO to related work with 1 paragraph distinguishing: (a) span-boundary F1 independent of type label vs. CSPO's structure/style/content decomposition for LaTeX tokens, (b) gradient variance curriculum analysis and adaptive weighting are completely absent from CSPO, (c) CSPO has no sequential skill ordering — it assigns static component-specific rewards without dynamic adaptation.", "COMPOUND NOVELTY ATTRITION — By Round 6, the Generator has needed to reframe Contribution 1 as an extension of RuCL/relay regime, reframe Contribution 2 as an 'application/instantiation' after SPARD, and now must add CSPO as yet another partially overlapping prior work for structured-generation reward decomposition. Each addition is individually manageable, but the cumulative effect is that any single contribution, when correctly positioned, reads as incremental. An EMNLP reviewer reading the related work section with SPARD, GDPO, CSPO, RuCL, arXiv:2602.14872, and arXiv:2604.19857 all cited as partial precedents may characterize the paper as 'applying existing techniques to IE' rather than a methodological contribution. The paper needs a single sharpest claim — the gradient variance curriculum analysis for span-IoU continuity vs. type-conjunction probability is the strongest differentiator; the abstract and intro should lead with this, not bury it under the other contributions.", "EMPIRICAL RESULT RISK NOT ADEQUATELY SCOPED — The claim 'closes a material fraction of the 20-point ProUIE argument F1 gap' (H4, target >60%) is vague. If Qwen3-8B with the proposed reward reaches 58-62% Argument F1 vs. ProUIE's 52.58% (Qwen3-4B), a reviewer will ask: is the improvement from reward design or from the 4B→8B scale increase? The paper has no same-scale (8B) ProUIE comparison. The Generator should flag this confound more explicitly in the experimental design and add the fixed-weight Qwen3-8B ablation (baseline (c)) as the primary comparison for reward design effect, not the scale-mismatched ProUIE 4B numbers.", "EMNLP FINDINGS TIMELINE ZERO-MARGIN — With May 25 ARR deadline confirmed (15 days from today), even auto-research mode (5-8 GPU days) leaves 7-10 days for writing and CSPO/other citation additions. The Generator should explicitly acknowledge in the feasibility note that any single GPU or training failure eliminates the EMNLP 2026 window entirely, making ACL 2027 via February 2027 ARR the de-facto primary target for any non-auto mode."]
Feedback: Round 6 has correctly addressed all Round 5 issues: SPARD is accurately described and differentiated by formula philosophy (momentum vs. convergence-gap), VCRL is cited with the correct between-sample vs. within-sample variance distinction, Contribution 2 is properly reframed as application/instantiation, and EMNLP Findings is the acknowledged realistic target. The technical nucleus remains sound. The single new action required: (1) Add CSPO (arXiv:2604.10918, ACL 2026) to related work — 1 paragraph: CSPO decomposes structured generation rewards by functional component (structure/style/content) for table-to-LaTeX and argues for component-specific backpropagation to resolve 'reward ambiguity'; distinguish by (a) span-boundary F1 independent of type label is a more precise decoupling than CSPO's LaTeX-component boundaries, (b) curriculum theory and adaptive weighting are entirely absent from CSPO, (c) CSPO targets document rendering fidelity not IE structured prediction. Beyond CSPO, two sharpening suggestions that would elevate novelty score above 3/5 without new experiments: (a) Restructure the abstract/intro to lead with the gradient variance curriculum claim as the paper's primary theoretical contribution, citing it as a reward-component-level relay regime (extending arXiv:2602.14872) specifically for IE — this is the strongest differentiator from all prior work; (b) Add an explicit acknowledgment in Section 5 that the scale difference (8B proposed vs. 4B ProUIE) is a confound in the primary ProUIE comparison and that the fixed-weight Qwen3-8B ablation (not ProUIE 4B) is the clean baseline for reward design effect. These changes require only writing revisions — no new experiments.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "0a28ff51-06d0-459f-aac9-fbe277c655f7",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:37:06.761Z_

```json
{
  "parentUuid": "0a28ff51-06d0-459f-aac9-fbe277c655f7",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "1aea9b81-632f-4474-9d8f-e46bff43bfa3",
  "timestamp": "2026-05-10T08:37:06.761Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:37:06.761Z_

```json
{
  "parentUuid": "1aea9b81-632f-4474-9d8f-e46bff43bfa3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a446cf6d-10c7-4fe4-b6a7-bdb1ce32b7b8",
  "timestamp": "2026-05-10T08:37:06.761Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weightin…",
  "leafUuid": "a446cf6d-10c7-4fe4-b6a7-bdb1ce32b7b8",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled curriculum rewards for IE task decomposition",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:38:15.652Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on a course of action.

**Current State Assessment:**
- 6 rounds of revision with no meaningful score improvement (stuck at ~3.5/5)
- The core idea keeps accumulating prior work that needs to be differentiated
- Three specific issues in Round 6:
  1. CSPO (arXiv:2604.10918, ACL 2026) is uncited - very similar surface framing
  2. Compound novelty attrition - each contribution reads as incremental
  3. Empirical result risk - scale confound (8B vs 4B) not adequately addressed
  4. 

There's a hard deadline for EMNLP with zero margin. The real issue is that each contribution is getting progressively weaker under scrutiny. The gradient variance analysis is already framed as extending RuCL's existing framework and the relay regime from prior work, and now CSPO introduces yet another precedent for reward decomposition in structured generation—so the theoretical novelty keeps shrinking toward just applying known techniques to information extraction. The adaptive weights contribution was already downgraded to an application after SPARD emerged. Even the learning curves analysis is starting to feel like it's just documenting what happens when you run the method at different scales.

The reviewer's feedback stings because it's accurate: the paper reads like applying existing techniques to IE rather than introducing something methodologically new. But there's actually a defensible core insight buried in here—the observation that span-boundary rewards are fundamentally continuous (span IoU ranges across [0,1]) while type-correctness is binary, and this structural difference in the reward signal has real consequences for how RL training unfolds. That's a genuine insight worth defending, but it's getting lost under the weight of too many contributions and too much "applying frameworks" language.

I should consider a major revision that strips this down to a single sharp claim: the span continuity hypothesis, where the continuous versus discrete nature of reward components actually determines the convergence ordering in GRPO-based IE. That would be a much cleaner, more defensible contribution than trying to defend three increasingly marginal claims.

Alternatively, I could pivot entirely toward a genuinely novel problem that doesn't have all these partial precedents already in the literature—something like counterfactual credit assignment for joint extraction tasks, where the challenge is figuring out which tokens actually caused a failure when the model gets some parts right and others wrong.

Or there's the span-level policy gradient angle: standard token-level approaches treat all tokens in a span equally, but boundary tokens and type tokens should probably get different gradient weights since they serve different functions. That feels like it could be a real contribution if I can formalize it properly. I'm realizing that token-role-aware scaling is essentially the same as token-level reward decomposition—which CSPO already implements by routing gradients only through relevant tokens. So this approach isn't actually novel. Let me step back and think about what the real gap is here.

CSPO handles table-to-LaTeX with component-specific rewards and token-level routing, while our IE work adds span-boundary rewards with continuous IoU signals, sequential skill convergence theory, dynamic weighting schemes, and curriculum learning—none of which CSPO has. So CSPO doesn't invalidate the paper, but it does force a clearer positioning. The honest question is whether the gradient variance curriculum analysis for IE tasks is genuinely novel enough for a top venue.

The real insight is that the theoretical contribution around gradient variance and curriculum learning should be the paper's spine, not one of three equal claims. I should restructure this as a theory paper with empirical validation: lead with the core gradient variance curriculum claim for IE, position CSPO as prior work that does routing without sequential skill ordering or adaptive weighting, use a fixed-weight Qwen baseline as the main ablation instead of ProUIE, and target ACL 2027 as the realistic timeline.

But before committing to that major revision, I need to actually understand what CSPO does and whether there's a stronger pivot opportunity here. I'm noticing an alternative angle: instead of framing this around curriculum learning, what if the core contribution is about selective token masking in policy gradients for IE? The key observation is that not all tokens in an IE generation are equally important for the reward signal—structural tokens like JSON brackets don't carry IE information, while span content and type labels do. So the insight would be that policy gradients should focus gradient updates on tokens that are causally responsible for the reward, rather than wasting capacity on structural elements.

But then I realize CSPO already does this—it routes backpropagation through relevant tokens. So I need to actually read the CSPO paper to see exactly what ground it covers.

Stepping back, the core problem is genuinely real: atomic rewards in GRPO-IE fail when you get the span right but the type wrong. The decomposition solution makes sense, and the theory about different gradient variance profiles for different components is interesting. But I'm looking at this accumulated pile of prior work—RuCL, SPARD, GDPO, CSPO—and I need to figure out what's actually novel here versus what's already been explored.

The key question is whether there's enough unique combination that a top reviewer would see real contribution. I think it hinges on execution and honest framing: I shouldn't oversell novelty, but instead focus on the one thing nothing else has done—the formal analysis of why span-boundary reward continuity specifically (not just decomposing into easier subproblems) drives sequential convergence in IE GRPO training. CSPO does reward decomposition and token routing for LaTeX, but it doesn't analyze span-IoU continuity, doesn't formalize the gradient variance argument for why continuity matters, and doesn't establish the sequential convergence ordering that curriculum theory would predict.

So the genuine gap is the theory explaining why continuity matters, the IE-specific reward decomposition, and the adaptive weighting scheme. I'm going to do a major revision that leads with the theoretical claim as the primary contribution, properly differentiates from CSPO, fixes the scale confound, and tightens the abstract and introduction. Before I start rewriting, I need to actually fetch CSPO and search for any other recent IE plus reinforcement learning work I might have missed, plus check the current ACE2 setup.

I'm spinning up searches to fetch CSPO directly, look for related IE and RLVR papers, and verify the baseline accuracy against current SOTA.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a446cf6d-10c7-4fe4-b6a7-bdb1ce32b7b8",
  "isSidechain": false,
  "requestId": "req_011CataqPv3MCwTEf3LPgGjH",
  "type": "assistant",
  "uuid": "71b86d65-b35a-480a-ad85-642677a512a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GraeZ7Qwxu8HPEtCXJiEiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20947,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3299,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20947
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T08:38:16.314Z_

Looking at 6 rounds of revision with stalled scores, I need to honestly assess whether to minor-fix, major-revise, or pivot. Before deciding, I'll do deep research on CSPO and the broader landscape to understand how much novelty space remains.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71b86d65-b35a-480a-ad85-642677a512a8",
  "isSidechain": false,
  "requestId": "req_011CataqPv3MCwTEf3LPgGjH",
  "type": "assistant",
  "uuid": "c689cfd0-0572-4d0e-baae-a6654694995c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GraeZ7Qwxu8HPEtCXJiEiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20947,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3299,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20947
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T08:38:22.610Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019LG4vzMEkQ7ue5z2TcQRhf`</summary>

```json
{
  "description": "Research CSPO and recent IE/RLVR concurrent work",
  "subagent_type": "Explore",
  "prompt": "I need you to fetch and read several arXiv papers. Use WebFetch on each URL and return the abstract + methods sections (or as much as you can get).\n\n1. CSPO (arXiv:2604.10918): Fetch https://arxiv.org/abs/2604.10918 — read the abstract and method sections carefully. I need to know: (a) exactly how they decompose rewards, (b) whether they do token-level gradient routing or sequence-level reward decomposition, (c) what tasks they target, (d) whether they have any curriculum/sequential skill ordering analysis, (e) whether they have adaptive weighting.\n\n2. Also fetch https://arxiv.org/abs/2604.10633 (ProUIE) abstract to confirm the EE numbers.\n\n3. Search for any papers from 2025-2026 on \"information extraction GRPO reward decomposition\" or \"NER event extraction reinforcement learning reward\" that might be concurrent work not yet cited.\n\nReturn full details from each paper fetch."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c689cfd0-0572-4d0e-baae-a6654694995c",
  "isSidechain": false,
  "requestId": "req_011CataqPv3MCwTEf3LPgGjH",
  "type": "assistant",
  "uuid": "c45453ec-88b3-45c0-b4bd-a16106354b0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GraeZ7Qwxu8HPEtCXJiEiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20947,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3299,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20947
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T08:38:27.421Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M2SoCMn1KJCYhdkFQe5VHp`</summary>

```json
{
  "description": "Search for IE RLVR recent work and ACE2005 SOTA",
  "subagent_type": "Explore",
  "prompt": "I need you to do several web searches to understand the current state of reinforcement learning for information extraction (IE). \n\n1. Search for \"span boundary reward GRPO information extraction 2025 2026\" to find any papers doing span-decoupled rewards for IE.\n\n2. Search for \"event extraction argument F1 ACE2005 2025 2026 state of the art\" to find current SOTA numbers.\n\n3. Search for \"CSPO component specific policy optimization structured generation\" to find out more about this paper and its reception.\n\n4. Search for \"gradient variance reward decomposition curriculum GRPO NLP 2026\" to find if anyone has done the specific theoretical analysis proposed.\n\n5. Search for \"token level reward gradient routing named entity recognition event extraction\" to find any token-level gradient approaches for IE.\n\nReturn full search results with titles, authors, key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45453ec-88b3-45c0-b4bd-a16106354b0a",
  "isSidechain": false,
  "requestId": "req_011CataqPv3MCwTEf3LPgGjH",
  "type": "assistant",
  "uuid": "ab08b036-616e-439e-b76f-5d2b0c102542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GraeZ7Qwxu8HPEtCXJiEiZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20947,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3299,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20947
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:38:59.664Z_

<details><summary>↩ Tool result · `toolu_01M2SoCMn1KJCYhdkFQe5VHp`</summary>

```text
## Summary of Web Search Results

I've completed all five searches. Here are the full findings:

---

### 1. Span Boundary Reward + GRPO for Information Extraction (2025-2026)

**Key Papers Found:**

- **GRPO-VPS (Verifiable Process Supervision)** - Published at ICLR 2026
  - Segments model responses into discrete reasoning spans and extracts conditional probability of correct answers at segment boundaries
  - Uses probability differences between adjacent segments as supervision signals
  - Results: +2.6 points Pass@1 on Qwen2.5-Math-1.5B, +1.1 on 7B model
  - Source: https://arxiv.org/pdf/2604.20659

- **EGCA (Execution-Grounded Credit Assignment)** - ICLR 2026 Workshop on Scaling Post-Training
  - Identifies causal spans via reference-trace comparison
  - Concentrates GRPO advantage only on relevant spans
  - Localizes earliest execution divergence for near-correct candidates
  - Source: https://arxiv.org/html/2603.16158v1

- **XRPO (Explore-Exploit GRPO)** - arXiv 2510.06672
  - Balances exploration and exploitation in reward signals
  - Promotes informative rollout exploration while sharpening exploitation
  - Source: https://arxiv.org/html/2510.06672v2

- **Step-GRPO** - arXiv 2604.16890
  - Internalizes dynamic early exit for efficient reasoning
  - Uses semantic steps rather than token-level boundaries
  - Source: https://arxiv.org/html/2604.16890v1

---

### 2. Event Extraction SOTA on ACE2005 (2025-2026)

**Current State of the Art:**

- **PLMEE**: F1 of 80.7 on trigger classification (TC) - represents strong pre-trained LM baseline
- **NLI+**: Currently reported as SOTA for argument extraction on ACE2005
- **Recent improvements (2024-2025)**:
  - Joint event extraction with dynamic attention matching and graph attention networks outperforms existing SOTA (Feb 2025)
  - ECPEAE exceeded TabEAE with 0.26% improvement on ACE2005 (Dec 2024)
  - KPEE (keyword proposal-based framework) - two-stage approach using single-choice prompting (2025)

**Sources:**
- Papers with Code leaderboard: https://paperswithcode.com/sota/event-argument-extraction-on-ace2005
- Closed-Domain Event Extraction Literature Review (Jan 2025): https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf
- Joint event extraction paper (Nature, Feb 2025): https://www.nature.com/articles/s41598-025-91501-2
- Event Extraction Survey: https://arxiv.org/html/2512.19537v1

---

### 3. CSPO (Component-Specific Policy Optimization)

**Paper:** "CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation"
Source: https://arxiv.org/html/2604.10918

**Key Findings:**

- Addresses reward ambiguity in RL by decomposing structured generation into components (structure, style, content, etc.)
- Uses LaTeX parser to identify functional components in generated code
- Assigns component-specific rewards and backpropagates signals only through relevant tokens
- Enables targeted component-wise optimization instead of single aggregated reward
- Specifically designed for table-to-LaTeX generation where fidelity matters across multiple dimensions

**Reception:** Appears to be a well-received approach in structured generation; paper available at top venues.

---

### 4. Gradient Variance + Reward Decomposition + Curriculum Learning with GRPO (2026)

**Key Papers:**

- **VCRL (Variance-based Curriculum Reinforcement Learning)** - arXiv 2509.19803
  - Uses curriculum learning to match sample difficulty with model capability
  - Achieves SOTA performance outperforming GRPO baselines
  - Addresses limitation that GRPO doesn't consider sample difficulty
  - Source: https://arxiv.org/html/2509.19803

- **BNPO (Beta Normalization Policy Optimization)** - arXiv 2506.02864
  - Provides theoretical analysis of variance-reducing properties
  - Introduces advantage decomposition mechanism for complex reward systems
  - Source: https://arxiv.org/pdf/2506.02864

- **Why GRPO Needs Normalization** - arXiv 2601.23135
  - Analyzes GRPO from local-curvature perspective
  - Shows gradient decomposition as advantage-weighted token-level importance ratios
  - Demonstrates variance reduction through group normalization
  - Source: https://arxiv.org/abs/2601.23135

- **Stratified GRPO** - arXiv 2510.06214
  - Uses stratum-specific baselines to reduce variance in heterogeneous reward settings
  - Shows strict variance reduction when reward means are heterogeneous
  - Source: https://arxiv.org/html/2510.06214

**Theoretical Findings:** The specific analysis of gradient variance reduction, reward decomposition via curriculum learning, and component-specific optimization is actively being researched in early 2026, with VCRL and Stratified GRPO representing the most relevant work.

---

### 5. Token-Level Reward + Gradient Routing for NER/Event Extraction

**Key Research:**

- **GIRL (Gradient Imitation Reinforcement Learning)** - arXiv 2211.06014
  - Designs rewards to quantify how well pseudo-labeled data imitates gradient descent directions
  - Applied to NER, relation extraction, and event extraction in low-resource settings
  - Bootstraps optimization through trial-and-error learning
  - Source: https://arxiv.org/abs/2211.06014

- **Weak Reward Model for Causal Event Extraction** - arXiv 2406.18245
  - Transforms generative models into robust causal event extraction systems
  - Uses weak reward signals for token-level guidance
  - Source: https://arxiv.org/html/2406.18245

**Important Findings:**
- Token-level evaluation in IE is challenging because event spans may include intermittent text with blurred word boundaries
- Current work on token-level gradient routing for IE is limited; most approaches use span-level or argument-level decomposition
- GIRL's gradient imitation approach is the closest match to token-level gradient routing for IE tasks

---

## Overall Assessment

The field shows active development in:
1. **Span-decoupled rewards**: GRPO-VPS and EGCA demonstrate effective span-level credit assignment
2. **SOTA on ACE2005**: Incremental improvements with graph-based methods and prompt-learning approaches
3. **CSPO adoption**: Structured component-specific optimization gaining traction beyond LaTeX
4. **Theoretical foundations**: VCRL, BNPO, and Stratified GRPO provide the theoretical underpinnings for variance reduction and curriculum learning
5. **Token-level approaches**: Limited to GIRL-like gradient imitation; full token-level gradient routing for IE remains an open research direction

Sources:
- [GRPO-VPS](https://arxiv.org/pdf/2604.20659)
- [EGCA for Code Generation](https://arxiv.org/html/2603.16158v1)
- [XRPO](https://arxiv.org/html/2510.06672v2)
- [Step-GRPO](https://arxiv.org/html/2604.16890v1)
- [Papers with Code ACE2005 SOTA](https://paperswithcode.com/sota/event-argument-extraction-on-ace2005)
- [Closed-Domain Event Extraction Review](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)
- [Joint Event Extraction with GAT](https://www.nature.com/articles/s41598-025-91501-2)
- [Event Extraction Survey](https://arxiv.org/html/2512.19537v1)
- [CSPO Paper](https://arxiv.org/html/2604.10918)
- [VCRL](https://arxiv.org/html/2509.19803)
- [BNPO](https://arxiv.org/pdf/2506.02864)
- [Why GRPO Needs Normalization](https://arxiv.org/abs/2601.23135)
- [Stratified GRPO](https://arxiv.org/html/2510.06214)
- [GIRL](https://arxiv.org/abs/2211.06014)
- [Weak Reward Model for Event Extraction](https://arxiv.org/html/2406.18245)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab08b036-616e-439e-b76f-5d2b0c102542",
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "6be2fd2b-169b-4092-93cd-691590d1d2fa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to do several web searches to understand the current state of reinforcement learning for information extraction (IE). \n\n1. Search for \"span boundary reward GRPO information extraction 2025 2026\" to find any papers doing span-decoupled rewards for IE.\n\n2. Search for \"event extraction argument F1 ACE2005 2025 2026 state of the art\" to find current SOTA numbers.\n\n3. Search for \"CSPO component specific policy optimization structured generation\" to find out more about this paper and its reception.\n\n4. Search for \"gradient variance reward decomposition curriculum GRPO NLP 2026\" to find if anyone has done the specific theoretical analysis proposed.\n\n5. Search for \"token level reward gradient routing named entity recognition event extraction\" to find any token-level gradient approaches for IE.\n\nReturn full search results with titles, authors, key findings.",
    "agentId": "adce3f713f4dc38a4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Web Search Results\n\nI've completed all five searches. Here are the full findings:\n\n---\n\n### 1. Span Boundary Reward + GRPO for Information Extraction (2025-2026)\n\n**Key Papers Found:**\n\n- **GRPO-VPS (Verifiable Process Supervision)** - Published at ICLR 2026\n  - Segments model responses into discrete reasoning spans and extracts conditional probability of correct answers at segment boundaries\n  - Uses probability differences between adjacent segments as supervision signals\n  - Results: +2.6 points Pass@1 on Qwen2.5-Math-1.5B, +1.1 on 7B model\n  - Source: https://arxiv.org/pdf/2604.20659\n\n- **EGCA (Execution-Grounded Credit Assignment)** - ICLR 2026 Workshop on Scaling Post-Training\n  - Identifies causal spans via reference-trace comparison\n  - Concentrates GRPO advantage only on relevant spans\n  - Localizes earliest execution divergence for near-correct candidates\n  - Source: https://arxiv.org/html/2603.16158v1\n\n- **XRPO (Explore-Exploit GRPO)** - arXiv 2510.06672\n  - Balances exploration and exploitation in reward signals\n  - Promotes informative rollout exploration while sharpening exploitation\n  - Source: https://arxiv.org/html/2510.06672v2\n\n- **Step-GRPO** - arXiv 2604.16890\n  - Internalizes dynamic early exit for efficient reasoning\n  - Uses semantic steps rather than token-level boundaries\n  - Source: https://arxiv.org/html/2604.16890v1\n\n---\n\n### 2. Event Extraction SOTA on ACE2005 (2025-2026)\n\n**Current State of the Art:**\n\n- **PLMEE**: F1 of 80.7 on trigger classification (TC) - represents strong pre-trained LM baseline\n- **NLI+**: Currently reported as SOTA for argument extraction on ACE2005\n- **Recent improvements (2024-2025)**:\n  - Joint event extraction with dynamic attention matching and graph attention networks outperforms existing SOTA (Feb 2025)\n  - ECPEAE exceeded TabEAE with 0.26% improvement on ACE2005 (Dec 2024)\n  - KPEE (keyword proposal-based framework) - two-stage approach using single-choice prompting (2025)\n\n**Sources:**\n- Papers with Code leaderboard: https://paperswithcode.com/sota/event-argument-extraction-on-ace2005\n- Closed-Domain Event Extraction Literature Review (Jan 2025): https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf\n- Joint event extraction paper (Nature, Feb 2025): https://www.nature.com/articles/s41598-025-91501-2\n- Event Extraction Survey: https://arxiv.org/html/2512.19537v1\n\n---\n\n### 3. CSPO (Component-Specific Policy Optimization)\n\n**Paper:** \"CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation\"\nSource: https://arxiv.org/html/2604.10918\n\n**Key Findings:**\n\n- Addresses reward ambiguity in RL by decomposing structured generation into components (structure, style, content, etc.)\n- Uses LaTeX parser to identify functional components in generated code\n- Assigns component-specific rewards and backpropagates signals only through relevant tokens\n- Enables targeted component-wise optimization instead of single aggregated reward\n- Specifically designed for table-to-LaTeX generation where fidelity matters across multiple dimensions\n\n**Reception:** Appears to be a well-received approach in structured generation; paper available at top venues.\n\n---\n\n### 4. Gradient Variance + Reward Decomposition + Curriculum Learning with GRPO (2026)\n\n**Key Papers:**\n\n- **VCRL (Variance-based Curriculum Reinforcement Learning)** - arXiv 2509.19803\n  - Uses curriculum learning to match sample difficulty with model capability\n  - Achieves SOTA performance outperforming GRPO baselines\n  - Addresses limitation that GRPO doesn't consider sample difficulty\n  - Source: https://arxiv.org/html/2509.19803\n\n- **BNPO (Beta Normalization Policy Optimization)** - arXiv 2506.02864\n  - Provides theoretical analysis of variance-reducing properties\n  - Introduces advantage decomposition mechanism for complex reward systems\n  - Source: https://arxiv.org/pdf/2506.02864\n\n- **Why GRPO Needs Normalization** - arXiv 2601.23135\n  - Analyzes GRPO from local-curvature perspective\n  - Shows gradient decomposition as advantage-weighted token-level importance ratios\n  - Demonstrates variance reduction through group normalization\n  - Source: https://arxiv.org/abs/2601.23135\n\n- **Stratified GRPO** - arXiv 2510.06214\n  - Uses stratum-specific baselines to reduce variance in heterogeneous reward settings\n  - Shows strict variance reduction when reward means are heterogeneous\n  - Source: https://arxiv.org/html/2510.06214\n\n**Theoretical Findings:** The specific analysis of gradient variance reduction, reward decomposition via curriculum learning, and component-specific optimization is actively being researched in early 2026, with VCRL and Stratified GRPO representing the most relevant work.\n\n---\n\n### 5. Token-Level Reward + Gradient Routing for NER/Event Extraction\n\n**Key Research:**\n\n- **GIRL (Gradient Imitation Reinforcement Learning)** - arXiv 2211.06014\n  - Designs rewards to quantify how well pseudo-labeled data imitates gradient descent directions\n  - Applied to NER, relation extraction, and event extraction in low-resource settings\n  - Bootstraps optimization through trial-and-error learning\n  - Source: https://arxiv.org/abs/2211.06014\n\n- **Weak Reward Model for Causal Event Extraction** - arXiv 2406.18245\n  - Transforms generative models into robust causal event extraction systems\n  - Uses weak reward signals for token-level guidance\n  - Source: https://arxiv.org/html/2406.18245\n\n**Important Findings:**\n- Token-level evaluation in IE is challenging because event spans may include intermittent text with blurred word boundaries\n- Current work on token-level gradient routing for IE is limited; most approaches use span-level or argument-level decomposition\n- GIRL's gradient imitation approach is the closest match to token-level gradient routing for IE tasks\n\n---\n\n## Overall Assessment\n\nThe field shows active development in:\n1. **Span-decoupled rewards**: GRPO-VPS and EGCA demonstrate effective span-level credit assignment\n2. **SOTA on ACE2005**: Incremental improvements with graph-based methods and prompt-learning approaches\n3. **CSPO adoption**: Structured component-specific optimization gaining traction beyond LaTeX\n4. **Theoretical foundations**: VCRL, BNPO, and Stratified GRPO provide the theoretical underpinnings for variance reduction and curriculum learning\n5. **Token-level approaches**: Limited to GIRL-like gradient imitation; full token-level gradient routing for IE remains an open research direction\n\nSources:\n- [GRPO-VPS](https://arxiv.org/pdf/2604.20659)\n- [EGCA for Code Generation](https://arxiv.org/html/2603.16158v1)\n- [XRPO](https://arxiv.org/html/2510.06672v2)\n- [Step-GRPO](https://arxiv.org/html/2604.16890v1)\n- [Papers with Code ACE2005 SOTA](https://paperswithcode.com/sota/event-argument-extraction-on-ace2005)\n- [Closed-Domain Event Extraction Review](https://www.turing.ac.uk/sites/default/files/2025-07/arc_event_extraction_lit_review.pdf)\n- [Joint Event Extraction with GAT](https://www.nature.com/articles/s41598-025-91501-2)\n- [Event Extraction Survey](https://arxiv.org/html/2512.19537v1)\n- [CSPO Paper](https://arxiv.org/html/2604.10918)\n- [VCRL](https://arxiv.org/html/2509.19803)\n- [BNPO](https://arxiv.org/pdf/2506.02864)\n- [Why GRPO Needs Normalization](https://arxiv.org/abs/2601.23135)\n- [Stratified GRPO](https://arxiv.org/html/2510.06214)\n- [GIRL](https://arxiv.org/abs/2211.06014)\n- [Weak Reward Model for Event Extraction](https://arxiv.org/html/2406.18245)"
      }
    ],
    "totalDurationMs": 32240,
    "totalTokens": 24460,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 3518,
      "cache_creation_input_tokens": 1963,
      "cache_read_input_tokens": 16779,
      "output_tokens": 2200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1963
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3518,
          "output_tokens": 2200,
          "cache_read_input_tokens": 16779,
          "cache_creation_input_tokens": 1963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1963,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "ab08b036-616e-439e-b76f-5d2b0c102542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weightin…",
  "leafUuid": "6be2fd2b-169b-4092-93cd-691590d1d2fa",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled curriculum rewards for IE task decomposition",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Tool result

_source line 15 · 2026-05-10T08:39:08.292Z_

<details><summary>↩ Tool result · `toolu_019LG4vzMEkQ7ue5z2TcQRhf`</summary>

```text
Excellent! Now let me compile your comprehensive report with all the details you requested:

---

## DETAILED PAPER ANALYSIS

### 1. **CSPO (arXiv:2604.10918): Component-Specific Policy Optimization for Table-to-LaTeX**

**Abstract & Core Focus:**
CSPO addresses reward ambiguity in structured generation (table-to-LaTeX) by decomposing the problem across component types rather than treating it as a single monolithic reward.

**Reward Decomposition Method:**
- Decomposes rewards into **three component-specific signals**: structure, style, and content
- Uses **token-level gradient routing** (not sequence-level)—"backpropagates each signal only through the tokens relevant to its component"
- Introduces hierarchical evaluation metrics to assess each component independently

**Tasks Targeted:**
- Specialized in **structured table-to-LaTeX generation from images** (multimodal structured generation)

**Curriculum/Sequential Skill Ordering:**
- **NOT mentioned** in the abstract—no explicit curriculum learning or sequential skill analysis

**Adaptive Weighting:**
- **NOT mentioned** in the abstract—the method assigns component-specific rewards but abstract does not describe adaptive weighting mechanisms

**Key Innovation:**
Component-specific reward assignment with token-level credit assignment, avoiding the "reward ambiguity" problem where a single aggregated signal cannot distinguish which component caused success/failure.

---

### 2. **ProUIE (arXiv:2604.10633): Progressive Universal Information Extraction**

**Abstract & Performance:**
ProUIE is a **three-stage progressive approach** for LLM-based information extraction (NER, RE, EE) combining macro, meso, and micro-level learning.

**EE Performance Numbers:**
- Evaluated on **36 public datasets**
- Demonstrates **consistent improvements** in unified extraction without external data
- Outperforms instruction-tuned baselines on **NER & RE** while using a smaller backbone
- Shows **clear gains in production-oriented information extraction**

**Method Details:**
- **Macro-level**: Learning NER, RE, EE together
- **Meso-level**: Streamlining output formats
- **Micro-level**: GRPO with **stepwise fine-grained rewards (SFR)** applied over structural units

**Key Distinction from CSPO:**
ProUIE uses GRPO with stepwise fine-grained rewards rather than component-specific decomposition, and targets information extraction tasks rather than structured generation.

---

### 3. **Concurrent Work: Information-Theoretic Reward Decomposition (arXiv:2504.06020)**

**Reward Decomposition Method:**
- Decomposes rewards into two components: **prompt-free** (response-only) and **prompt-related** (prompt-response interaction)
- Uses **information-theoretic perspective** to extract components without requiring extra models
- More generalizable approach than standard RLHF reward models

**Adaptive Weighting:**
- YES—proposes "adaptive prioritization" that weights samples based on their prompt-free reward values
- Effectively creates importance-weighted curriculum based on decomposed signal

**Tasks:**
- General RLHF alignment (not task-specific)

**Key Insight:**
Addresses poor generalization by isolating prompt-independent evaluation signals—directly relevant to understanding why decomposition helps RLHF.

---

### 4. **Concurrent Work: Causal Decomposition for Robust Reward Modeling (arXiv:2604.13833)**

**Causal Decomposition Strategy:**
- Learns a **decoder that reconstructs latent intent embeddings** from candidate responses
- Uses **reconstruction error as regularization signal** to suppress spurious correlations
- Grounds preferences in prompt intent rather than response artifacts (length, tone)

**Results:**
- RewardBench accuracy: 0.832 → 0.868
- Improved robustness to length manipulation
- Evaluated on math, helpfulness, and safety tasks

**Distinction:**
This is a **causal approach** to reward modeling (preventing spurious correlations) rather than explicitly decomposing reward signals—complementary to CSPO's component decomposition.

---

## SEARCH FINDINGS: Concurrent Work (2025-2026)

The search identified **no papers specifically combining information extraction + GRPO reward decomposition** in the April 2026 arXiv window, making ProUIE and CSPO appear to be addressing relatively unique problem spaces:

1. **GDPO (arXiv:2601.05242)**: Addresses GRPO multi-reward collapse but targets reasoning/coding, not IE
2. **General RL trends**: Curriculum-RLAIF (2025) emerging for reward model training
3. **NER research**: GPRL model using Entity Order RL—suggests sequential ordering benefits NER, but not combined with GRPO reward decomposition

**Notable absence**: No papers found explicitly combining GRPO with structured information extraction reward decomposition—suggesting ProUIE and CSPO occupy novel territory.

---

## SUMMARY TABLE

| Paper | Decomposition Type | Level | Tasks | Curriculum? | Adaptive Weighting? |
|-------|-------------------|-------|-------|------------|-------------------|
| CSPO (2604.10918) | Component-specific (struct/style/content) | Token-level routing | Table-to-LaTeX | ❌ | ❌ |
| ProUIE (2604.10633) | Stepwise fine-grained rewards (SFR) | Structural units | NER/RE/EE | ✓ (3-stage) | ✓ (implicit) |
| Info-Theoretic (2504.06020) | Prompt-free vs. prompt-related | Sample-level | General RLHF | ❌ | ✓ (explicit) |
| Causal (2604.13833) | Intent reconstruction | Sample-level | Alignment | ❌ | ❌ |

---

Sources:
- [CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation](https://arxiv.org/abs/2604.10918)
- [ProUIE: Progressive Universal Information Extraction](https://arxiv.org/abs/2604.10633)
- [Information-Theoretic Reward Decomposition for Generalizable RLHF](https://arxiv.org/abs/2504.06020)
- [Robust Reward Modeling for Large Language Models via Causal Decomposition](https://arxiv.org/abs/2604.13833)
- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://huggingface.co/papers/2601.05242)
- [GRPO Overview and Analysis](https://cameronrwolfe.substack.com/p/grpo)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c45453ec-88b3-45c0-b4bd-a16106354b0a",
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "251619ac-e3cd-4cf8-aa0b-950f8363fc8d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to fetch and read several arXiv papers. Use WebFetch on each URL and return the abstract + methods sections (or as much as you can get).\n\n1. CSPO (arXiv:2604.10918): Fetch https://arxiv.org/abs/2604.10918 — read the abstract and method sections carefully. I need to know: (a) exactly how they decompose rewards, (b) whether they do token-level gradient routing or sequence-level reward decomposition, (c) what tasks they target, (d) whether they have any curriculum/sequential skill ordering analysis, (e) whether they have adaptive weighting.\n\n2. Also fetch https://arxiv.org/abs/2604.10633 (ProUIE) abstract to confirm the EE numbers.\n\n3. Search for any papers from 2025-2026 on \"information extraction GRPO reward decomposition\" or \"NER event extraction reinforcement learning reward\" that might be concurrent work not yet cited.\n\nReturn full details from each paper fetch.",
    "agentId": "aba7949b212f8f748",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me compile your comprehensive report with all the details you requested:\n\n---\n\n## DETAILED PAPER ANALYSIS\n\n### 1. **CSPO (arXiv:2604.10918): Component-Specific Policy Optimization for Table-to-LaTeX**\n\n**Abstract & Core Focus:**\nCSPO addresses reward ambiguity in structured generation (table-to-LaTeX) by decomposing the problem across component types rather than treating it as a single monolithic reward.\n\n**Reward Decomposition Method:**\n- Decomposes rewards into **three component-specific signals**: structure, style, and content\n- Uses **token-level gradient routing** (not sequence-level)—\"backpropagates each signal only through the tokens relevant to its component\"\n- Introduces hierarchical evaluation metrics to assess each component independently\n\n**Tasks Targeted:**\n- Specialized in **structured table-to-LaTeX generation from images** (multimodal structured generation)\n\n**Curriculum/Sequential Skill Ordering:**\n- **NOT mentioned** in the abstract—no explicit curriculum learning or sequential skill analysis\n\n**Adaptive Weighting:**\n- **NOT mentioned** in the abstract—the method assigns component-specific rewards but abstract does not describe adaptive weighting mechanisms\n\n**Key Innovation:**\nComponent-specific reward assignment with token-level credit assignment, avoiding the \"reward ambiguity\" problem where a single aggregated signal cannot distinguish which component caused success/failure.\n\n---\n\n### 2. **ProUIE (arXiv:2604.10633): Progressive Universal Information Extraction**\n\n**Abstract & Performance:**\nProUIE is a **three-stage progressive approach** for LLM-based information extraction (NER, RE, EE) combining macro, meso, and micro-level learning.\n\n**EE Performance Numbers:**\n- Evaluated on **36 public datasets**\n- Demonstrates **consistent improvements** in unified extraction without external data\n- Outperforms instruction-tuned baselines on **NER & RE** while using a smaller backbone\n- Shows **clear gains in production-oriented information extraction**\n\n**Method Details:**\n- **Macro-level**: Learning NER, RE, EE together\n- **Meso-level**: Streamlining output formats\n- **Micro-level**: GRPO with **stepwise fine-grained rewards (SFR)** applied over structural units\n\n**Key Distinction from CSPO:**\nProUIE uses GRPO with stepwise fine-grained rewards rather than component-specific decomposition, and targets information extraction tasks rather than structured generation.\n\n---\n\n### 3. **Concurrent Work: Information-Theoretic Reward Decomposition (arXiv:2504.06020)**\n\n**Reward Decomposition Method:**\n- Decomposes rewards into two components: **prompt-free** (response-only) and **prompt-related** (prompt-response interaction)\n- Uses **information-theoretic perspective** to extract components without requiring extra models\n- More generalizable approach than standard RLHF reward models\n\n**Adaptive Weighting:**\n- YES—proposes \"adaptive prioritization\" that weights samples based on their prompt-free reward values\n- Effectively creates importance-weighted curriculum based on decomposed signal\n\n**Tasks:**\n- General RLHF alignment (not task-specific)\n\n**Key Insight:**\nAddresses poor generalization by isolating prompt-independent evaluation signals—directly relevant to understanding why decomposition helps RLHF.\n\n---\n\n### 4. **Concurrent Work: Causal Decomposition for Robust Reward Modeling (arXiv:2604.13833)**\n\n**Causal Decomposition Strategy:**\n- Learns a **decoder that reconstructs latent intent embeddings** from candidate responses\n- Uses **reconstruction error as regularization signal** to suppress spurious correlations\n- Grounds preferences in prompt intent rather than response artifacts (length, tone)\n\n**Results:**\n- RewardBench accuracy: 0.832 → 0.868\n- Improved robustness to length manipulation\n- Evaluated on math, helpfulness, and safety tasks\n\n**Distinction:**\nThis is a **causal approach** to reward modeling (preventing spurious correlations) rather than explicitly decomposing reward signals—complementary to CSPO's component decomposition.\n\n---\n\n## SEARCH FINDINGS: Concurrent Work (2025-2026)\n\nThe search identified **no papers specifically combining information extraction + GRPO reward decomposition** in the April 2026 arXiv window, making ProUIE and CSPO appear to be addressing relatively unique problem spaces:\n\n1. **GDPO (arXiv:2601.05242)**: Addresses GRPO multi-reward collapse but targets reasoning/coding, not IE\n2. **General RL trends**: Curriculum-RLAIF (2025) emerging for reward model training\n3. **NER research**: GPRL model using Entity Order RL—suggests sequential ordering benefits NER, but not combined with GRPO reward decomposition\n\n**Notable absence**: No papers found explicitly combining GRPO with structured information extraction reward decomposition—suggesting ProUIE and CSPO occupy novel territory.\n\n---\n\n## SUMMARY TABLE\n\n| Paper | Decomposition Type | Level | Tasks | Curriculum? | Adaptive Weighting? |\n|-------|-------------------|-------|-------|------------|-------------------|\n| CSPO (2604.10918) | Component-specific (struct/style/content) | Token-level routing | Table-to-LaTeX | ❌ | ❌ |\n| ProUIE (2604.10633) | Stepwise fine-grained rewards (SFR) | Structural units | NER/RE/EE | ✓ (3-stage) | ✓ (implicit) |\n| Info-Theoretic (2504.06020) | Prompt-free vs. prompt-related | Sample-level | General RLHF | ❌ | ✓ (explicit) |\n| Causal (2604.13833) | Intent reconstruction | Sample-level | Alignment | ❌ | ❌ |\n\n---\n\nSources:\n- [CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation](https://arxiv.org/abs/2604.10918)\n- [ProUIE: Progressive Universal Information Extraction](https://arxiv.org/abs/2604.10633)\n- [Information-Theoretic Reward Decomposition for Generalizable RLHF](https://arxiv.org/abs/2504.06020)\n- [Robust Reward Modeling for Large Language Models via Causal Decomposition](https://arxiv.org/abs/2604.13833)\n- [GDPO: Group reward-Decoupled Normalization Policy Optimization](https://huggingface.co/papers/2601.05242)\n- [GRPO Overview and Analysis](https://cameronrwolfe.substack.com/p/grpo)"
      }
    ],
    "totalDurationMs": 45675,
    "totalTokens": 24200,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1987,
      "cache_read_input_tokens": 20590,
      "output_tokens": 1616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1987
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1616,
          "cache_read_input_tokens": 20590,
          "cache_creation_input_tokens": 1987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1987,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "c45453ec-88b3-45c0-b4bd-a16106354b0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T08:40:57.236Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me synthesize what I've found:

**CSPO Analysis:**
- CSPO does: table-to-LaTeX with structure/style/content decomposition at token-level routing
- CSPO does NOT do: sequential skill ordering, curriculum theory, adaptive weighting, IE-specific analysis

**Key new papers found:**
- EGCA (arXiv:2603.16158): Execution-Grounded Credit Assignment — identifies causal spans via reference-trace comparison, concentrates GRPO advantage on relevant spans, for code generation


- GRPO-VPS (arXiv:2604.20659): segments reasoning spans and uses probability differences between adjacent segments

The landscape is getting crowded—CSPO, EGCA, and GRPO-VPS all tackle span-level or component-level credit assignment in different ways. The gradient variance analysis still feels like the genuinely novel angle here, but I need to think carefully about whether the reward decomposition space is becoming too saturated.

None of these papers actually formalize the gradient variance comparison between span-IoU continuity and type-conjunction, and the IE application to joint NER+RE+EE extraction is still untouched. So maybe the move isn't to pivot entirely, but to do a major revision that centers everything around the Span-Continuity Gradient Variance Theorem as the single primary contribution, with the rest flowing as applications and corollaries. That would sharpen the claim significantly and make the theoretical novelty much harder to dismiss.

Actually, there's an even cleaner angle: reframing this as the Signal Topology Theorem for IE Policy Gradient, which formally explains how the continuous versus binary topology of reward components determines gradient variance ordering and naturally induces curriculum learning in GRPO-IE. This directly positions against CSPO—they do token routing but never explain *why* different components train differently. And I'd fix the scale confound by comparing against the same base model rather than mixing architectures.

But wait, maybe the real core insight is even simpler: topology-aware policy gradient for structured prediction, where the key observation is that continuous reward components like span-IoU have fundamentally different topological properties than binary ones like type-conjunction, and this topology directly controls gradient behavior and training dynamics. "decompose by component" — no theory of why this works
- EGCA uses reference traces (requires ground truth execution) — specific to code
- GRPO-VPS uses probability differences — specific to reasoning

So I'm looking for a genuinely novel angle that's testable on existing benchmarks without extra compute, and clearly distinct from prior work. My major revision would reframe this as a single theoretical contribution focused on how reward continuity drives convergence in GRPO for information extraction, rather than splitting it into three separate claims.

The core insight is that the topological structure of a reward component—whether it's continuous, binary, or compositional—directly determines its gradient variance early in training, how quickly it converges relative to other components, and whether you even need explicit curriculum scheduling. This is more precise than existing decomposition work, more theoretically grounded than variance-based approaches, and extends beyond what's been shown at the task level to the reward-component level.

The algorithm itself falls naturally out of this theory: weight each component by how far it still is from convergence, then normalize by its variance since noisy components can look like they need attention when they're just suffering from gradient noise. What sets this apart is that prior work like CSPO routes gradients without explaining *why* components train differently or in what order, ProUIE uses stepwise rewards without analyzing the continuity mechanism, and SPARD relies on momentum-based progress weighting—whereas our approach is grounded in the convergence-gap theory.

The core insight is clean enough to state in one sentence: the topology of the reward signal—whether components are continuous or binary—determines how gradients behave and creates an implicit curriculum where span-IoU converges first, type-conjunction second, and argument F1 third, all without explicit scheduling. That's the novel contribution, and it should anchor the abstract.

Now I need to revise the paper structure around this insight, starting with the title to emphasize reward topology as the organizing principle.

Updating the JSON to reflect this: the title shifts to highlight topology, the core problem becomes the topology claim itself, and the contributions restructure hierarchically with the Signal Topology Theorem as the main result and the IE instantiation as a corollary. I'm also adding CSPO to related work, fixing the scale confound by anchoring to Qwen3-8B, and acknowledging ACL 2027 as the target timeline.

For the title, I'm weighing options that lead with the theoretical contribution while staying memorable and distinct from CSPO's framing. Something like "Span-First by Design" captures the empirical phenomenon while "Signal Topology Theory" grounds it theoretically—I'm settling on a version that emphasizes how topology drives the implicit curriculum.

The key is being explicit about the domain, method, and insight: information extraction, GRPO, and the connection between reward continuity and sequential skill convergence. I'm leaning toward "CurriculumRLVR-IE: Reward Signal Topology Drives Sequential Skill Convergence in GRPO Information Extraction" or a tighter variant that leads with the gradient variance ordering theorem as the core theoretical contribution.

Now I need to restructure the entire paper around this insight. Instead of framing it as "atomic vs. span-decoupled rewards," the real story is answering why certain reward decompositions induce curriculum effects at all—and the answer is signal topology. That's the genuine novelty: a formal topological argument for why span-boundary rewards work for curriculum induction, not just empirical validation that they do. The adaptive weighting scheme and IE experiments follow naturally from this theorem, but the theorem itself is the centerpiece.

For CSPO, I see the connection now: their component-specific routing for LaTeX works empirically, but they never explain *why* it works or analyze convergence dynamics across components. The Signal Topology Theorem provides exactly that theoretical foundation—it explains why component-specific routing helps and predicts which decompositions should induce curriculum effects. IE is fundamentally different from their parallel rendering dimensions because span detection and type classification are semantically ordered skills, not independent rendering concerns. So our work isn't just another application of component routing; it's the theoretical explanation for why approaches like CSPO succeed in the first place.

For the scale confound, I need to be explicit: the fixed-weight Qwen3-8B ablation is my primary baseline since it shares the same backbone as the proposed system, so any improvement there is purely from reward design. ProUIE uses a smaller 4B model, so I can't cleanly separate reward design from scale effects. I'll decompose it as: the improvement from proposed over fixed-weight shows reward design gains, and the gap between fixed-weight and ProUIE captures the residual scale advantage.

On timeline, ACL 2027 with a February 2027 ARR deadline is the realistic target for non-auto modes. EMNLP 2026 is technically feasible with a May 25 ARR (15 days away), but only if I'm running in auto mode with no constraints.

Now I'm restructuring the entire paper around Signal Topology as the primary theoretical contribution. The key insight is that no one has formally characterized why reward signal topology—whether continuous, binary, or compositional—determines convergence ordering in GRPO for structured prediction. That's the fundamental gap I'm addressing. I'm reframing the core problem around this theoretical question, then making the application to reward design the instantiation of that theorem. This reduces the contribution to essentially one major insight with its practical application, and I need to integrate CSPO properly into the framework while fixing the scale confound I just outlined.

The mathematics itself isn't exotic—continuous rewards like Span-IoU have well-behaved second moments while binary rewards like Type-conjunction behave like Bernoulli distributions with higher variance, and conditional rewards compound these effects. But the contribution is showing this analysis explains why curriculum learning emerges in IE, and "signal topology" is the conceptual label for this mathematical property.

Now I'm drafting the revision. I'll keep the JSON structure but refocus each section to emphasize that the real novelty is applying gradient variance analysis to IE reward components—showing the continuous/binary distinction is what drives curriculum emergence. This hasn't been formalized in prior work.

For the title, I want something that leads with the theoretical mechanism: "CurriculumRLVR-IE: How Reward Signal Topology Induces Implicit Sequential Skill Curriculum in GRPO Information Extraction"

Now I'm rewriting the core sections to make the theorem the centerpiece and show how adaptive weighting and learning curves follow directly from it. to lead with theory):
The fundamental question in GRPO-based information extraction (IE) is not merely "how should rewards be decomposed?" but "why does reward decomposition produce curriculum effects — and for which structural properties of the reward signal?" No published work has answered this question formally. The existing IE reward literature (ProUIE, R1-RE, R2GRPO, EXTRACT-0) treats reward design as empirical engineering; no paper analyzes the mathematical properties of reward components that determine convergence ordering.

The central claim of this paper is a **Signal Topology Theorem** for GRPO-IE: the *topological property* of a reward component — specifically whether it is **continuous** (takes values in [0,1], like span-IoU), **binary** (takes values in {0,1}, like span+type conjunction), or **compositional** (conditioned on multiple binary components, like argument F1) — determines its gradient variance in early training, which in turn determines the natural ordering of convergence without needing explicit curriculum scheduling. The mathematical intuition is that continuous rewards like span-IoU have bounded variance similar to a Beta distribution, while binary rewards like span+type conjunction exhibit higher variance due to their Bernoulli-like structure with lower success probabilities in early training, creating a systematic variance hierarchy that drives which components learn first.

This is not a coincidence of hyperparameters or a quirk of GRPO optimization — it is a **structural property** of the reward topology itself. The consequence is an implicit curriculum: span detection converges first due to lower-variance gradient signal, then type prediction stabilizes as span accuracy improves (reducing the variance of the type-conditioned Bernoulli), and finally argument F1 receives clean signal only after both upstream components have stabilized. This span→type→argument sequential convergence emerges as a theorem consequence, not an empirically discovered phenomenon.

The practical implication is that existing GRPO-IE methods like ProUIE lose this variance advantage by treating span+type conjunction as an atomic reward unit, collapsing the continuous span-IoU signal into a binary conjunction and forfeiting the natural curriculum structure that the topology theorem predicts.

Now I'm seeing the empirical gap: ProUIE achieves only 52.58% argument F1 on ACE2005 versus InstructUIE's 72.94%, a 20-point deficit that the authors attribute to reward design without identifying the underlying mechanism. The Signal Topology Theorem explains exactly why — atomic rewards eliminate the variance ordering that produces implicit curriculum. CSPO shows empirically that component-specific routing helps for table-to-LaTeX generation, but lacks the theoretical framework to explain why different components converge at different rates or what structural property of the reward determines the ordering.

The contribution is one core theoretical result (the Signal Topology Theorem with formal gradient variance derivation) plus two direct applications: decoupled span-boundary rewards for IE as a theorem instantiation, and convergence-gap adaptive weighting as a theorem-motivated algorithm, validated empirically through per-component analysis.

I'm settling on the Signal Topology Theorem as the paper's signature — this is what sets it apart. The three contributions get reframed hierarchically: theorem first, then application, then validation. CSPO gets proper treatment in the landscape section, the scale confound is addressed directly, and the title emphasizes the theoretical contribution. This is a major restructuring because the paper shifts from three equal contributions to one theorem with two applications, and the framing moves from "reward decomposition for IE" to "signal topology theory for GRPO-IE curriculum."

Now I'm writing out the complete JSON with these changes locked in.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "251619ac-e3cd-4cf8-aa0b-950f8363fc8d",
  "isSidechain": false,
  "requestId": "req_011CatazMLGAqucuKdmTcfiG",
  "type": "assistant",
  "uuid": "694d062d-8afc-46af-9118-f9e788c27bd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JnL4xaRbUmcXcKPzbUoHS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2226,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 32578,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2226,
          "output_tokens": 5055,
          "cache_read_input_tokens": 32578,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T08:41:02.634Z_

Now I have a clear picture. Let me assess honestly before writing the revision:

**Diagnosis after research:**
- CSPO does token-level gradient routing for LaTeX, but zero theory of WHY components have different convergence dynamics
- EGCA (arXiv:2603.16158) does causal span credit assignment for code — another partial precedent for the "route gradients by component" idea
- The field is accumulating component-specific reward papers empirically, but NO paper provides a formal characterization of WHAT property of the reward signal (continuous vs. binary vs. compositional topology) determines gradient variance ordering and implicit curriculum emergence
- This is the genuine gap — not "span-decoupled rewards help" (CSPO shows this), but "WHY do continuous reward components produce lower-variance gradients and converge first, and how does this generate curriculum?"

**Decision: Major Revision** — restructure the entire paper around ONE primary theoretical contribution (Signal Topology Theorem) with the algorithmic and empirical contributions as direct corollaries, rather than three equal contributions that each read as incremental. Add CSPO, fix the scale confound, clarify timeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "694d062d-8afc-46af-9118-f9e788c27bd0",
  "isSidechain": false,
  "requestId": "req_011CatazMLGAqucuKdmTcfiG",
  "type": "assistant",
  "uuid": "46d9c40d-d235-49b9-8cbe-3d8a2e989fd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JnL4xaRbUmcXcKPzbUoHS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2226,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 32578,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2226,
          "output_tokens": 5055,
          "cache_read_input_tokens": 32578,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T08:41:03.092Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B9iDsCiC2NzXY7PeqqezR4`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46d9c40d-d235-49b9-8cbe-3d8a2e989fd8",
  "isSidechain": false,
  "requestId": "req_011CatazMLGAqucuKdmTcfiG",
  "type": "assistant",
  "uuid": "794711e4-077f-4354-99f4-338b3badf4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JnL4xaRbUmcXcKPzbUoHS4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2226,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 32578,
      "output_tokens": 5055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2226,
          "output_tokens": 5055,
          "cache_read_input_tokens": 32578,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T08:41:03.099Z_

<details><summary>↩ Tool result · `toolu_01B9iDsCiC2NzXY7PeqqezR4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "794711e4-077f-4354-99f4-338b3badf4ae",
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "1c01cffe-d352-4beb-957d-a470a84f88ff",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "794711e4-077f-4354-99f4-338b3badf4ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weightin…",
  "leafUuid": "1c01cffe-d352-4beb-957d-a470a84f88ff",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled curriculum rewards for IE task decomposition",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Assistant

_source line 22 · 2026-05-10T08:41:05.879Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me fetch the CSPO paper to get the actual details before writing the revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c01cffe-d352-4beb-957d-a470a84f88ff",
  "isSidechain": false,
  "requestId": "req_011Catb8pSQ3PDu286H4WWYy",
  "type": "assistant",
  "uuid": "08153a9d-c80a-442d-98d4-fc4731b67def",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019NZmC48VdttZRzGm6893uh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7787,
      "cache_read_input_tokens": 37517,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 37517,
          "cache_creation_input_tokens": 7787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7787
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T08:41:09.333Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CTZ4PfjuQKkgMQeJYByx9C`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10918",
  "prompt": "Extract: (1) the exact method for component-specific reward decomposition and token-level gradient routing, (2) what components they decompose into for LaTeX, (3) whether they have any sequential skill ordering or curriculum theory, (4) whether they have adaptive weighting, (5) the key results/numbers, (6) how they frame \"reward ambiguity\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08153a9d-c80a-442d-98d4-fc4731b67def",
  "isSidechain": false,
  "requestId": "req_011Catb8pSQ3PDu286H4WWYy",
  "type": "assistant",
  "uuid": "174a0bbf-2ab1-4092-9871-7b3733e83a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019NZmC48VdttZRzGm6893uh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7787,
      "cache_read_input_tokens": 37517,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 37517,
          "cache_creation_input_tokens": 7787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7787
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T08:41:10.552Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CqBwH59pgsxLiG6JyspKaH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.16158",
  "prompt": "Extract: (1) what EGCA (Execution-Grounded Credit Assignment) does exactly, (2) how it routes gradients to relevant spans, (3) what task it targets, (4) whether it applies to information extraction or only code/math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "174a0bbf-2ab1-4092-9871-7b3733e83a9b",
  "isSidechain": false,
  "requestId": "req_011Catb8pSQ3PDu286H4WWYy",
  "type": "assistant",
  "uuid": "c8bba6a5-8e85-41e7-96d2-d5e6fe7b435a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019NZmC48VdttZRzGm6893uh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7787,
      "cache_read_input_tokens": 37517,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7787,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 319,
          "cache_read_input_tokens": 37517,
          "cache_creation_input_tokens": 7787,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7787
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T08:41:13.007Z_

<details><summary>↩ Tool result · `toolu_01CTZ4PfjuQKkgMQeJYByx9C`</summary>

```text
# CSPO Paper Analysis

Based on the available arXiv abstract, I can only provide limited information, as the full technical details are not included in the webpage content provided.

**What is available:**

1. **Components decomposed**: The abstract specifies three LaTeX table components: "structure, style, and content"

2. **Core mechanism**: CSPO "assigns component-specific rewards and backpropagates each signal only through the tokens relevant to its component"

3. **Problem framing**: The authors describe "reward ambiguity that conflates multiple behavioral aspects" as the key limitation of standard single-reward RL approaches

**What cannot be determined from this excerpt:**

- Exact mathematical formulation of the reward decomposition
- Specific token-level gradient routing algorithm details
- Sequential skill ordering or curriculum learning approaches
- Adaptive weighting schemes
- Numerical results (the abstract mentions "extensive experiments" but provides no metrics)

**Recommendation**: To access the complete technical methodology, you would need to view the full PDF or HTML version of the paper, which are linked on the arXiv page but not included in this content excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "174a0bbf-2ab1-4092-9871-7b3733e83a9b",
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "0237d605-dec2-4fd7-9cef-8830f2f679f4",
  "toolUseResult": {
    "bytes": 46029,
    "code": 200,
    "codeText": "OK",
    "result": "# CSPO Paper Analysis\n\nBased on the available arXiv abstract, I can only provide limited information, as the full technical details are not included in the webpage content provided.\n\n**What is available:**\n\n1. **Components decomposed**: The abstract specifies three LaTeX table components: \"structure, style, and content\"\n\n2. **Core mechanism**: CSPO \"assigns component-specific rewards and backpropagates each signal only through the tokens relevant to its component\"\n\n3. **Problem framing**: The authors describe \"reward ambiguity that conflates multiple behavioral aspects\" as the key limitation of standard single-reward RL approaches\n\n**What cannot be determined from this excerpt:**\n\n- Exact mathematical formulation of the reward decomposition\n- Specific token-level gradient routing algorithm details\n- Sequential skill ordering or curriculum learning approaches\n- Adaptive weighting schemes\n- Numerical results (the abstract mentions \"extensive experiments\" but provides no metrics)\n\n**Recommendation**: To access the complete technical methodology, you would need to view the full PDF or HTML version of the paper, which are linked on the arXiv page but not included in this content excerpt.",
    "durationMs": 3670,
    "url": "https://arxiv.org/abs/2604.10918"
  },
  "sourceToolAssistantUUID": "174a0bbf-2ab1-4092-9871-7b3733e83a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T08:41:14.465Z_

<details><summary>↩ Tool result · `toolu_01CqBwH59pgsxLiG6JyspKaH`</summary>

```text
# EGCA: Execution-Grounded Credit Assignment Analysis

## (1) What EGCA Does

EGCA localizes reinforcement learning updates by identifying where programs fail semantically. It "executes the candidate and a canonical reference solution under identical instrumentation, identifies the earliest semantic divergence" and focuses learning signals on that specific location rather than spreading them uniformly across the entire program.

## (2) Gradient Routing Mechanism

The method "assigns advantage only to the corresponding token span while masking downstream tokens." This concentrates gradient updates to the precise tokens responsible for the semantic error, preventing irrelevant downstream code from receiving credit signals.

## (3) Target Task

EGCA specifically targets code generation, demonstrated through improvements on HumanEval (82.1% pass@1) and MBPP (68.9%) benchmarks.

## (4) Applicability

Based on the provided content, EGCA applies **exclusively to code generation**, not information extraction or other NLP tasks. The method relies on executable code with test cases and reference solutions, making it domain-specific to programming tasks rather than broadly applicable to general text or extraction problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8bba6a5-8e85-41e7-96d2-d5e6fe7b435a",
  "isSidechain": false,
  "promptId": "f575e849-19f4-474f-84c4-aeec1bbe6586",
  "type": "user",
  "uuid": "1570bd64-f1d4-404a-9059-cb2f4922328e",
  "toolUseResult": {
    "bytes": 45077,
    "code": 200,
    "codeText": "OK",
    "result": "# EGCA: Execution-Grounded Credit Assignment Analysis\n\n## (1) What EGCA Does\n\nEGCA localizes reinforcement learning updates by identifying where programs fail semantically. It \"executes the candidate and a canonical reference solution under identical instrumentation, identifies the earliest semantic divergence\" and focuses learning signals on that specific location rather than spreading them uniformly across the entire program.\n\n## (2) Gradient Routing Mechanism\n\nThe method \"assigns advantage only to the corresponding token span while masking downstream tokens.\" This concentrates gradient updates to the precise tokens responsible for the semantic error, preventing irrelevant downstream code from receiving credit signals.\n\n## (3) Target Task\n\nEGCA specifically targets code generation, demonstrated through improvements on HumanEval (82.1% pass@1) and MBPP (68.9%) benchmarks.\n\n## (4) Applicability\n\nBased on the provided content, EGCA applies **exclusively to code generation**, not information extraction or other NLP tasks. The method relies on executable code with test cases and reference solutions, making it domain-specific to programming tasks rather than broadly applicable to general text or extraction problems.",
    "durationMs": 3912,
    "url": "https://arxiv.org/abs/2603.16158"
  },
  "sourceToolAssistantUUID": "c8bba6a5-8e85-41e7-96d2-d5e6fe7b435a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T08:41:32.563Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have the full picture:

**CSPO:**
- Structure/style/content decomposition for table-to-LaTeX
- Token-level gradient routing by component
- "Reward ambiguity" framing
- NO curriculum theory
- NO adaptive weighting
- NO sequential skill ordering

**EGCA:**
- Code generation only (execution-grounded, needs test cases/reference solutions)
- NOT applicable to IE

Now I have everything I need to write the major revision. Let me proceed.

**The Core Decision**: Major revision — restructure the paper around the Signal Topology Theorem as the primary contribution.


---

So the real novelty here is that CSPO shows empirical evidence that component-level routing works, but it never explains the underlying mechanism. EGCA is irrelevant since it's purely for code. The gradient variance analysis connecting span-IoU continuity to type-conjunction convergence ordering is genuinely new—no one's formally shown that the topology of the reward signal itself determines how quickly different components learn. This Signal Topology Theorem is sharper than CSPO because it explains *why* routing helps, more precise than RuCL's two-tier rubric approach, and it fills a gap that existing work hasn't addressed.

Now I'm restructuring the paper around this one core theoretical claim with two algorithmic applications. The title needs to emphasize the theoretical contribution, the problem statement should lead with the topology theory gap rather than just "what to do," and I'm reorganizing the approach to present Theorem 1 first before showing how it applies. I'm also adding CSPO to the landscape with a clear differentiation, updating the venue timeline to target ACL 2027 as the primary venue for non-automated work, and revising the key references accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1570bd64-f1d4-404a-9059-cb2f4922328e",
  "isSidechain": false,
  "requestId": "req_011Catb9eoVeNMD4jx8G6jba",
  "type": "assistant",
  "uuid": "4d987b9e-65a8-48c0-bea7-2fd616b6021f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WKdeGXsadXJ8Ves96gXT7s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 45304,
      "output_tokens": 12360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12360,
          "cache_read_input_tokens": 45304,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T08:46:10.003Z_

Good. Now I have what I need. CSPO does token routing without any theory of WHY, and EGCA is code-only. The Signal Topology Theorem remains the genuine gap. Let me write the major revision now.

```json
{
  "title": "CurriculumRLVR-IE: Reward Signal Topology Theory for Implicit Sequential Skill Curriculum in GRPO Information Extraction",
  "change_type": "major",
  "core_problem": "The fundamental question in GRPO-based information extraction (IE) is not merely 'how should rewards be decomposed?' but 'why does reward decomposition produce curriculum effects — and for which structural properties of the reward signal?' No published work has answered this question formally. The IE reward literature (ProUIE, R1-RE, R2GRPO, EXTRACT-0) treats reward design as empirical engineering; no paper analyzes the mathematical properties of reward components that determine convergence ordering in policy gradient training.\n\nThe central claim of this paper is a **Signal Topology Theorem** for GRPO-IE: the topological property of a reward component — specifically whether it is **continuous** (takes values in [0,1], like span-IoU), **binary** (takes values in {0,1}, like span+type conjunction), or **compositional** (conditioned on multiple binary components, like argument F1) — determines its gradient variance in early GRPO training, and therefore determines convergence ordering without explicit curriculum scheduling. This is a structural claim, not an empirical one.\n\nFormally: for a GRPO policy with per-rollout reward R = Σᵢ αᵢ Rᵢ, the gradient variance contribution of component i scales as αᵢ² · Var(Rᵢ). For span-IoU (continuous, Beta-distributed), Var(R_span) is bounded by the variance of a symmetric Beta. For span+type conjunction (binary, Bernoulli with p = p_s · p_t), Var(R_type) = p_s·p_t·(1−p_s·p_t), which exceeds Var(R_span) in early training when p_s, p_t < 0.5 because the conjunction probability product p_s·p_t < p_s drives the Bernoulli toward its maximum variance regime. The variance inequality Var(R_span) < Var(R_type) < Var(R_arg) is a structural consequence of reward topology — it holds regardless of hyperparameter choices, as long as p_s < 0.5 in early training.\n\nThe consequence is an implicit curriculum that is a **theorem prediction**, not an empirically discovered phenomenon: (1) the span component provides lower-variance gradient signal in early training, causing span detection to converge first; (2) as p_s increases (span accuracy improves), p_t | (span correct) rises (type classification is a simpler Bernoulli conditioned on correct localization), reducing Var(R_type) and enabling type convergence; (3) argument F1 receives cleaner signal only after both span and type have stabilized, because its compound conditional variance is dominated by the upstream binary variance terms. The span→type→argument sequential convergence is predicted by the theorem before any experiment runs.\n\nWhy the theorem matters for IE: Current GRPO-IE methods (ProUIE, arXiv:2604.10633) use atomic (span, type) rewards, treating span+type conjunction as the fundamental unit. This eliminates span-IoU's continuous signal, forcing the model to learn from a Bernoulli with p = p_s·p_t — the lowest-probability joint event, maximizing gradient variance. ProUIE reports ACE2005 Argument F1=52.58% vs. InstructUIE's 72.94% (a 20-point gap) and calls for 'more appropriate reward design,' but does not identify why its SFR structure creates the gap. The Signal Topology Theorem provides this identification: atomic rewards destroy the variance ordering that produces implicit curriculum, causing type and argument learning to plateau while span detection catches up through noisy, high-variance gradient updates.\n\nCSPO (arXiv:2604.10918, ACL 2026) shows empirically that component-specific token-level gradient routing helps for table-to-LaTeX generation (structure/style/content decomposition), using the framing of 'reward ambiguity.' CSPO provides no theoretical explanation of WHY different components have different convergence dynamics, what structural property of the reward determines the ordering, or whether static component routing is sufficient or whether adaptive weighting is needed. The Signal Topology Theorem provides the theoretical foundation for CSPO's empirical observation — and, crucially, predicts when static routing is insufficient (when the variance ordering creates a hierarchy that fixed weights cannot enforce) and motivates the convergence-gap adaptive weighting as a theorem-derived algorithm rather than an empirical heuristic.",
  "opportunity": "The Signal Topology Theorem creates three opportunity axes, now hierarchically ordered: one theoretical (the theorem itself), one algorithmic (its direct application), and one empirical (its falsifiable prediction). This hierarchy replaces the prior three-equal-contributions framing that accumulated too many partial precedents.\n\n**Axis 1 (Theoretical — primary novelty and paper identity)**: The Signal Topology Theorem for GRPO-IE. No published work has formally characterized the relationship between reward component topology (continuous/binary/compositional) and gradient variance ordering in GRPO for structured prediction. The closest work:\n- RuCL (arXiv:2602.21628): Shows two-tier rubric curriculum via reward decomposition (Appendix B gradient variance analysis) for multimodal reasoning, but analyzes easy/hard rubric difficulty ordering, NOT the continuous/binary topological distinction as the mechanism. RuCL's variance reduction comes from reliable vs. unreliable rubrics — our theorem shows the deeper structural reason: reliable signals are reliable because they are continuous, not because they are 'easy.'\n- arXiv:2602.14872 (relay regime): Proves implicit curriculum at task-level difficulty ordering. Our theorem extends the relay concept from task level to reward-component level: within a single IE task, span-IoU continuity provides the 'smooth gradient handoff' that prevents plateau, analogous to how smooth difficulty spectrum prevents grokking at task level.\n- arXiv:2604.19857 (Reward Decomposition Theorem): Bounds sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary but different question: they ask 'how much do we lose by decomposing?' and bound the cost; we ask 'why does the span component help MORE than theory predicts?' and answer: because continuous topology reduces early-training variance, making the benefit dominate the bounded cost.\n- CSPO (arXiv:2604.10918): Empirically routes gradients through component-specific tokens for LaTeX generation. Provides no theoretical characterization of why components differ in convergence dynamics or what makes component routing beneficial. Our theorem provides this foundation.\n- VCRL (arXiv:2509.19803): Uses between-sample reward variance for difficulty-based data selection. Orthogonal: between-sample vs. within-sample, data selection vs. reward topology.\n\nThe theorem fills a gap that is visible across all these papers: they demonstrate that reward decomposition helps (CSPO, RuCL), or analyze how decomposed objectives converge (arXiv:2604.19857), or show that mixed-difficulty produces relay (arXiv:2602.14872) — but none explains the signal-structural mechanism that makes span detection specifically the curriculum foundation for IE.\n\n**Axis 2 (Algorithmic — theorem application)**: The convergence-gap adaptive weight scheme as a theorem corollary, not an independent contribution. The theorem predicts that variance inequality produces convergence ordering; the adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) is the algorithmic enforcement of this ordering — it redistributes weight toward components whose measured gradient variance (σ_i) remains high relative to their convergence gap. This is NOT a novel adaptive weighting technique (SPARD/PAWA, MAESTRO, arXiv:2509.11452 precede it); it is an instantiation of the theorem-derived curriculum principle for the IE skill hierarchy. The formula's philosophy (convergence-gap weighting, not momentum weighting) follows directly from the theorem: the theorem identifies the gap to convergence — not the rate of progress — as the theoretically relevant quantity.\n\n**Axis 3 (Empirical — theorem falsifiability)**: Per-component F1 learning curves logged every 50 GRPO steps serve as the empirical test of the theorem's sequential convergence prediction. The theorem predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering that no prior IE work has published. Deviation would falsify the topology hypothesis and require reanalysis. The empirical contribution is therefore not just 'we trained a model' but 'we provide the first learning curve evidence for or against reward-topology-induced curriculum in GRPO-IE.'",
  "landscape": "**CSPO** (arXiv:2604.10918, ACL 2026) is the most important addition to related work. CSPO proposes 'Component-Specific Policy Optimization' for table-to-LaTeX generation: it decomposes the structured generation reward into structure, style, and content components, and routes backpropagation signals only through tokens relevant to each component. The paper frames the problem as 'reward ambiguity that conflates multiple behavioral aspects.' CSPO is the closest concurrent work in the space of component-specific reward decomposition with token-level gradient routing, and its ACL acceptance confirms the research direction is timely. Three differentiations from CurriculumRLVR-IE: (a) CSPO applies component routing to LaTeX rendering fidelity (structure/style/content are parallel rendering dimensions in a formal language, not sequentially ordered IE skills); IE has a fundamentally different decomposition structure where span detection is a prerequisite for type classification and argument assignment — CSPO's parallel component routing has no notion of which component must converge before others; (b) CSPO provides no theoretical characterization of WHY component routing helps, why components might have different convergence dynamics, or what property of the reward signal determines convergence ordering — the paper's motivation is 'reward ambiguity' (an empirical observation) rather than a formal analysis; the Signal Topology Theorem provides this explanation for IE rewards specifically; (c) CSPO uses static component-specific rewards without adaptive weighting — the theorem-derived convergence-gap formula is absent. CSPO's empirical result (component routing helps for structured generation) and our theoretical result (continuous reward topology reduces gradient variance and induces sequential convergence) are complementary: CSPO shows the phenomenon exists; our theorem explains why.\n\n**ProUIE** (arXiv:2604.10633, April 2026) is the primary foil and most closely related concurrent GRPO-IE work. It applies GRPO with a Stepwise Fine-grained Reward (SFR) decomposed by structural unit across joint NER+RE+EE using Qwen3-4B (36 public datasets, three-stage training). For EE, SFR's Equation 10 is: R_sfr-ee = w_E·cov(E_g,E_p) + w_T·cov(T_g,T_p) + w_F·F̃_full − pen_ee, where F_full is computed by matching gold trigger groups to predicted trigger groups via maximum role-argument pair overlap, and the piecewise penalty (Eq. 9) prioritizes trigger errors over argument errors. When trigger detection fails, F_full shrinks (fewer argument pairs match) and gradient emphasis shifts toward trigger correction rather than argument assignment — producing, as we infer from the structural piecewise design, weakened argument-learning signal during trigger training. ProUIE does not explicitly state this mechanism; the authors attribute weak EE to 'unified generation setting and reward configuration' and call for 'stronger event-specific modeling and more appropriate reward design' in limitations. ProUIE's EE numbers: ACE2005 Trigger F1=70.65%, Argument F1=52.58% vs. InstructUIE 77.13%/72.94%. ProUIE evaluates EE on only ACE2005, CASIE, PHEE — RAMS, WikiEvents, MAVEN are uncovered. Critically, ProUIE's SFR uses atomic (span, type) as the atomic unit, conflating the continuous span-IoU signal with the binary type-classification signal — precisely the topology conflation that the Signal Topology Theorem identifies as the mechanism behind poor argument F1. CurriculumRLVR-IE differentiates from ProUIE on: (1) span-boundary F1 computed independently of type label, grounded in the theorem's gradient variance analysis; (2) convergence-gap adaptive weighting replacing fixed weights; (3) per-component learning curves as falsifiable theorem evidence.\n\n**SPARD** (arXiv:2604.07837, April 2026) proposes PAWA (Progress-Aware Weight Adaptation) for reward-component-level dynamic weighting in LLM alignment and RADR for data rebalancing. PAWA's exponential update w_{t+1}^{r,i} = w_t^{r,i}·exp(η·Q_t^i) fires when the LCB of mean reward improvement is positive (component making reliable progress). Three differentiations: (a) SPARD's PAWA is momentum-based (up-weights progress), risking perpetuating the dominance of whichever component improves first; the convergence-gap formula up-weights lagging components, which is theorem-motivated (the theorem identifies gap to convergence, not rate of progress, as the relevant quantity); (b) SPARD applies to open-ended LLM alignment without IE-specific structural decomposition or gradient-variance analysis; (c) SPARD provides no theoretical basis for why components have different variance profiles. The proposed adaptive scheme is an instantiation of the theorem's prediction, not a novel algorithm per se.\n\n**RuCL** (arXiv:2602.21628, 2026) uses GRPO with two-tier decomposed reward (foundational + advanced rubrics) for multimodal reasoning, with Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance. The Signal Topology Theorem deepens RuCL's analysis: RuCL shows reliable signals reduce variance (empirically); our theorem proves WHY span-IoU is specifically reliable (continuous topology → bounded Beta variance) while type-conjunction is specifically unreliable (binary topology → Bernoulli near maximum variance regime in early training). The theorem provides the mechanism that RuCL's analysis observes but does not derive.\n\n**GDPO** (arXiv:2601.05242, ICML 2026) addresses advantage collapse — where summing rewards before group-wise normalization maps distinct reward combinations to identical normalized advantage values, destroying relative signal. GDPO normalizes each reward's advantage independently before aggregation. This is orthogonal to the proposed work: GDPO operates at the normalization step; the theorem-derived adaptive weights operate at the aggregation step. The two mechanisms can be combined: GDPO normalization applied to each span/type/argument advantage, then convergence-gap adaptive aggregation weights. This combination is a concrete future direction.\n\n**MAESTRO** (arXiv:2601.07208) and **arXiv:2509.11452** motivate the general class of adaptive reward weighting approaches. Neither applies to IE or provides the IE-specific signal topology analysis. APEX (arXiv:2601.06574) identifies 'variance hijacking' in multi-objective RL — conceptually aligned with what the Signal Topology Theorem formalizes for IE: the binary type-conjunction component has higher variance and would hijack gradients without topology-aware decomposition.\n\n**On the Learning Dynamics of RLVR at the Edge of Competence** (arXiv:2602.14872, 2026) formally proves a relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2). The Signal Topology Theorem extends the relay concept from task level to reward-component level: within a single IE task type, the span/type/argument reward components form a difficulty ordering analogous to easy-to-hard task horizons, with span-IoU continuity providing the smooth gradient handoff. This is an extension in abstraction level, not a direct instantiation, and the paper explicitly distinguishes these two levels.\n\n**Rethinking Reinforcement Fine-Tuning in LVLM** (arXiv:2604.19857) proves a Reward Decomposition Theorem bounding the sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T). Complementary: they characterize the worst-case cost of decomposition; the Signal Topology Theorem identifies the structural IE-specific property (span-IoU continuity) that makes early-training variance reduction benefit dominate this bounded cost in practice.\n\n**VCRL** (arXiv:2509.19803) uses between-sample reward variance for difficulty-based data selection in math RLVR — explicitly distinct from the proposed within-sample reward-component variance analysis for skill ordering within IE task structure.\n\n**EGCA** (arXiv:2603.16158, ICLR 2026 Workshop) concentrates GRPO advantage signals on causal token spans for code generation, identifying earliest execution divergence from reference solutions. Distinct: EGCA requires executable code with test cases and reference execution traces; it is fundamentally inapplicable to IE. EGCA's credit assignment is causal (which tokens caused execution divergence); the Signal Topology Theorem's gradient variance analysis is structural (which reward components have lower variance by topology). Both address 'how should gradient credit be assigned,' but at different levels and with different mechanisms.\n\n**Locate and Label** (arXiv:2105.06804) provides architectural evidence that boundary detection is a prerequisite for entity typing — removing boundary regression causes 36.73% F1 drop for long entities on ACE04. T2-NER (TACL 2023) confirms span-then-type two-stage decomposition improves NER by +0.56% F1. These papers establish architectural motivation for the span-first ordering but do not analyze training dynamics or reward signal topology in RL.\n\n**REAR** (EMNLP 2025 Findings), **R1-RE** (arXiv:2507.04642), **R2GRPO** (arXiv:2505.22068), **EXTRACT-0** (arXiv:2509.22906): All GRPO-IE papers using atomic or fixed-weight composite rewards without signal topology analysis.",
  "approach": "We train Qwen3-8B-Instruct via GRPO with LoRA (rank 16, α=32, ~0.5% parameters) on a span-boundary-decoupled reward with theorem-derived adaptive component weighting. The paper has one primary theoretical contribution and two direct applications of that contribution.\n\n**Theorem 1 — Signal Topology Theorem (primary contribution)**:\n\nFor a GRPO policy π_θ trained with reward R = Σᵢ αᵢ Rᵢ where components {Rᵢ} have different topological properties, we prove:\n\n(a) *Variance ordering*: Var(R_span) < Var(R_type) < Var(R_arg) in early training when span detection probability p_s < 0.5. Specifically:\n- R_span (span-IoU): continuous on [0,1], Beta-distributed; Var(R_span) = μ_s(1−μ_s)/(1+φ) for shape parameter φ>0 (the Beta is never at maximum variance for bounded p_s, p_t)\n- R_type (span+type conjunction): binary, Bernoulli(p_s·p_t); Var(R_type) = p_s·p_t·(1−p_s·p_t), maximized near p=0.5, which occurs in mid-training when p_s<0.7 and p_t<0.7 — specifically exceeds Var(R_span) throughout early and mid-training\n- R_arg (argument F1): conditional on both span and type correctness; compound Bernoulli variance dominates until both upstream components are high-accuracy\n\n(b) *Sequential convergence ordering*: Lower variance in R_span produces a more stable GRPO gradient for span detection early in training (following the same framework as RuCL Appendix B but formally derived for continuous vs. binary topology rather than easy/hard rubric distinction). As p_s increases toward 0.7+, the type-conditioned component's effective Bernoulli probability p_t|span increases (simpler classification when span is correct), reducing Var(R_type) and enabling type convergence. Argument F1 receives stable signal only after both upstream variances decrease. The convergence ordering span → type → argument is a structural consequence of reward topology, not a manually scheduled curriculum.\n\n(c) *Falsifiable prediction*: Per-component F1 learning curves must show span F1 converging before type-conditioned F1, which converges before argument F1. Deviation falsifies the topology hypothesis.\n\nPositioning relative to concurrent theory: This theorem is positioned as a reward-component-level extension of the task-level relay regime (arXiv:2602.14872), which proves sequential gradient handoff across task difficulty levels but does not analyze reward component topology within a single task type. The theorem is also positioned as identifying the structural property (continuous vs. binary reward topology) that determines whether early-training variance reduction benefit dominates the sub-optimality cost characterized by arXiv:2604.19857's Reward Decomposition Theorem. CSPO (arXiv:2604.10918) demonstrates empirically that component routing helps for structured LaTeX generation without providing the theoretical characterization that our theorem supplies.\n\n**Application 1 — Theorem-Derived Reward Decomposition (algorithmic)**:\n\nTheorem 1 directly implies that IE rewards should separate span-IoU (continuous signal) from type-conjunction (binary signal) to exploit the variance ordering. This motivates the span-boundary-decoupled reward:\n- R_span: token-level F1 between predicted and gold entity/event mention spans, computed independently of type label (span IoU with gold, regardless of type classification) — the continuous component\n- R_type: type-level F1 conditioned on predicted-vs-gold span IoU≥0.5; power stretching γ=1.5 following ProUIE calibration — the binary component, but now isolated from span so its variance does not corrupt the span component's stable signal\n- R_arg: triple-level F1 for (head, relation, tail) or (trigger, role, argument-span) tuples; 0.15 additive partial credit for triples where both anchor spans are IoU≥0.5 matched but relation/role label is wrong — the compositional component\n\nThe convergence-gap adaptive weights follow from the theorem: w_i(t) = max(ε, θ−F1_i(t))/σ_i(t), normalized so Σᵢ wᵢ(t)=1, with ε=0.05, θ=0.7. This formula up-weights components that are (a) lagging below the convergence target (gap-based, not momentum-based) and (b) have stable gradients (low σ_i) — exactly the theorem's prediction for which component is ready to receive increased learning pressure. In early training, span has lower σ_span and below-target F1, receiving high weight; once span F1 exceeds θ, weight redistributes to type; once type converges, to argument. The philosophy contrast with SPARD's PAWA (which up-weights components making reliable progress, i.e., momentum) follows directly from the theorem: the theorem identifies gap-to-convergence, not rate-of-progress, as the relevant quantity for curriculum enforcement.\n\nTotal: R = w_span(t)·R_span + w_type(t)·R_type + w_arg(t)·R_arg, each clipped to [0,1]; weights initialized at (0.4/0.3/0.3) and updated every 50 GRPO steps. Plateau detector treats any component as 'converged' for weighting purposes if its F1_i improves <1% absolute over 200 consecutive steps, setting weight to ε regardless of whether F1_i has reached θ. Sensitivity analysis across θ ∈ {0.6, 0.7, 0.8} from saved checkpoints.\n\n**Application 2 — Per-Component Learning Curve Diagnostics (empirical)**:\n\nPer-component F1 is logged every 50 GRPO steps, producing span F1(t), type-conditioned F1(t), and argument F1(t) learning curves. The theorem predicts span F1 converges before type-conditioned F1, which converges before argument F1 — a falsifiable ordering. This is the primary empirical contribution: not just 'our method achieves better numbers' but 'the learning curves confirm/falsify the Signal Topology Theorem's convergence prediction.' The learning curves are also the first published per-component training dynamics for GRPO-IE, providing diagnostic value independent of the theorem.\n\n**Backbone and training**: Qwen3-8B-Instruct with LoRA (rank 16, same family as ProUIE's Qwen3-4B, next scale tier). Training on ACE2005 (joint NER+RE+EE, 33 event types, ~25K examples) + CoNLL-2003 (NER). Output format: code-style JSON with brief chain-of-thought trace (KnowCoder/GoLLIE schema conventions). Mandatory 50-example dry run measures actual token length distribution before full training; all compute commitments gated on this measurement.\n\n**Baselines and scale confound (explicit)**:\nThe scale difference between the proposed system (Qwen3-8B) and ProUIE (Qwen3-4B) is a confound in any direct ProUIE comparison: any performance advantage could reflect reward design OR the 4B→8B scale increase, and these cannot be disentangled from the ProUIE-4B comparison alone. The paper addresses this explicitly:\n- **Primary baseline for reward design effect**: Fixed-weight decomposed GRPO with Qwen3-8B (α₁=0.4, α₂=0.3, α₃=0.3, same backbone, same training data) — isolates adaptive weighting contribution from scale\n- **Primary baseline for decomposition effect**: Single-reward GRPO with Qwen3-8B (joint extraction F1 as the only reward) — isolates reward decomposition effect from scale\n- **Scale-controlled decomposition ablation**: α₁=0 ablation (span component removed, α₂=0.5, α₃=0.5) from checkpoint evaluation, same 8B backbone — directly tests whether span-boundary decoupling is the essential design choice\n- **Cross-system reference (not primary for reward design effect)**: ProUIE published ACE2005 numbers (Qwen3-4B) — presented as a cross-system reference with explicit note that scale difference is a confound; any residual advantage beyond what the fixed-weight Qwen3-8B achieves is attributable to adaptive weighting, not scale\n- **SFT upper bounds**: KnowCoder (7B) and InstructUIE published numbers (Trigger=77.13%, Argument=72.94% on ACE2005)\n\nThe paper's H4 hypothesis is rephrased as: 'Decomposed adaptive GRPO with Qwen3-8B achieves higher ACE2005 Argument F1 than fixed-weight decomposed GRPO with Qwen3-8B (H4a) and higher than single-reward GRPO with Qwen3-8B (H4b); whether this matches or exceeds ProUIE-4B is a cross-system data point, not the primary reward-design comparison.'\n\n**Anti-gaming safeguards**: Span-count guard penalizes predicted span count >2× gold (reward reduced by 0.3). Automated divergence monitoring flags runs where any component F1 leads joint F1 by >20 points for >3 consecutive checkpoints. Both verified on 50-example dry run before full training.\n\n**Document-level inference (RAMS, WikiEvents)**: Qwen3-8K supports 128K context; RAMS and WikiEvents fit in full-document inference. OOD results framed as zero-shot cross-distribution generalization from sentence-level training to document-level inference. Post-hoc error analysis categorizes failures by: (i) cross-sentence coreference chains, (ii) multi-sentence arguments, (iii) unseen argument roles, (iv) document-level context requirements.\n\n**Key testable hypotheses**:\nH1 (topology theorem): Per-component learning curves show span F1 converging before type-conditioned F1, which converges before argument F1 — falsifiable from logged training dynamics, predicted by Theorem 1.\nH2 (span decoupling): Decomposed reward with α₁>0 produces higher ACE2005 Argument F1 than α₁=0 ablation at matched compute (same backbone) — isolates span-boundary decoupling contribution.\nH3 (adaptive vs. fixed): Adaptive weight scheme produces higher Argument F1 than fixed-weight decomposed GRPO (same backbone) — isolates adaptive weighting contribution, the primary same-scale baseline.\nH4 (OOD generalization): Theorem-predicted convergence ordering generalizes to OOD benchmarks (RAMS, WikiEvents, MAVEN) — tests whether topology-induced curriculum creates more robust span detectors than single-reward GRPO.",
  "resource_estimate": {
    "compute_note": "Single-run-primary design gated on 50-example dry run. Output token length: 300-600 tokens per example for joint NER+RE+EE with CoT. Dry run measures actual distribution before full training. Adaptive weight update adds negligible overhead (one F1 computation per 50 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) derived from saved checkpoints, not new runs. All budgets target ≤200 H100-hours total.",
    "manual": {
      "gpu_hours": "~130-160 H100-hours total: dry run (~2 H100-hours) + main GRPO run with decomposed adaptive reward (~90-110 H100-hours) + fixed-weight Qwen3-8B ablation as primary same-scale comparison (~20-25 H100-hours, checkpoint evaluation not full new run) + SFT baseline eval (~15-20 H100-hours) + θ sensitivity checkpoint eval (~3-5 H100-hours). Total ≤165 H100-hours — within 200 H100-hour ceiling.",
      "gpu_utilization": "Low (20-35%) — GPUs idle during theorem derivation, learning curve interpretation, reward verifier implementation, CSPO differentiation writing, and paper writing.",
      "timeline": "3-4 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$325-660 (at $2.50-4/hr H100 cloud on-demand)"
    },
    "human_in_loop": {
      "gpu_hours": "~130-165 H100-hours total (same single-run-primary design; agent queues dry run first, then main GRPO run; fixed-weight and other ablations from checkpoint eval)",
      "gpu_utilization": "Moderate (55-70%) — agent runs main experiment queue; human approves after dry run token measurement and after main GRPO run before committing ablation evals.",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-350 (experiment orchestration, learning curve analysis, theorem validation, CSPO differentiation analysis, ~1500-3000 turns at $0.08-0.12/turn)",
      "estimated_gpu_cost": "~$325-660",
      "risk_note": "Primary risk: if dry run measures actual output >700 tokens, reduce epoch count by 30% before full training (human approval gate). Secondary risk: adaptive weight scheme may cause reward gaming if span component up-weights too aggressively — span-count guard (>2× gold → 0.3 penalty) verified on dry run. If argument F1 plateaus below θ for 200+ steps, plateau detector activates — monitor for weight collapse (any component w>0.8 for >100 steps). θ sensitivity analysis (θ ∈ {0.6, 0.7, 0.8}) run from saved checkpoints after main training completes."
    },
    "auto_research": {
      "gpu_hours": "~130-165 H100-hours total (dry run auto-queued first; main run launched if token length ≤700; checkpoint evals for ablations auto-queued after main run completes)",
      "gpu_utilization": "Near-zero idle (~80-90%) — agent queues dry run, measures token lengths, adjusts epoch count if >700 tokens, launches main run, auto-logs per-component F1 learning curves every 50 steps, runs plateau detector and θ sensitivity from saved checkpoints.",
      "timeline": "5-8 days with 4× H100 cluster",
      "team": "0 (setup: ~3-4h for LoRA config, adaptive weight verifier implementation, reward component F1 logger, schema prompt templates, plateau detector, θ sensitivity checkpoint eval script)",
      "claude_api_cost": "$175-400 (~2000-4500 turns)",
      "estimated_gpu_cost": "~$325-660",
      "speed_bottleneck": "Single-run-primary design; ablations from checkpoint evals, not new full runs. Per-component F1 logging adds minimal overhead.",
      "risk_note": "Dry run mandatory first. Plateau detector monitors all three components. Component F1 divergence triggers auto-checkpoint and pause. θ sensitivity auto-evaluated from saved checkpoints after main run."
    }
  },
  "target_venues": [
    "ACL 2027 Main (ARR February 2027 cycle) — primary target for all modes. The Signal Topology Theorem, properly developed with full gradient variance derivation in the appendix, with empirical learning-curve validation, is a main-track contribution if the theoretical novelty claim holds up to review. The extended timeline allows (a) stronger empirical coverage, (b) optional GDPO+adaptive-weight combination experiment as future direction, (c) tighter theoretical integration with arXiv:2602.14872's relay regime and arXiv:2604.19857's decomposition theorem.",
    "EMNLP 2026 Findings (ARR May 2026 cycle; submission deadline May 25, 2026 — 15 days from current date). Feasibility only in auto-research mode (5-8 GPU days), leaving 7-10 days for writing with CSPO and all other citations integrated. Even in auto mode, any single GPU failure or training divergence eliminates this window entirely — there is zero buffer. For manual mode (3-4 months) and human-in-loop mode (4-6 weeks), ACL 2027 is the de-facto primary target. EMNLP 2026 is a stretch goal in auto mode only, and the CSPO, EGCA, and timeline additions required by Round 6 must all be incorporated during the writing days."
  ],
  "level": "top-tier",
  "key_references": [
    "CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation (arXiv:2604.10918, ACL 2026) — component-specific reward decomposition with token-level gradient routing for table-to-LaTeX; decomposes into structure/style/content components; frames the problem as 'reward ambiguity'; provides empirical motivation for component routing without theoretical characterization of WHY different components have different convergence dynamics or what structural property of the reward determines ordering; no curriculum theory, no adaptive weighting, no sequential skill ordering prediction; parallel rendering dimensions (structure/style/content) vs. sequentially ordered IE skills (span → type → argument); the Signal Topology Theorem provides the theoretical foundation for CSPO's empirical observation",
    "ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv:2604.10633, April 2026) — joint NER+RE+EE GRPO with SFR (Eq. 10: R = w_E·cov(E) + w_T·cov(T) + w_F·F̃_full − pen_ee; Eq. 9: piecewise penalty prioritizing trigger before argument errors); EE underperforms on ACE2005 (Trigger=70.65%, Argument=52.58%); calls for 'more appropriate reward design'; does not diagnose atomic span+type conjunction as the mechanism causing poor argument gradient; does not cover RAMS/WikiEvents/MAVEN; uses Qwen3-4B (scale difference from proposed Qwen3-8B is an acknowledged confound in any direct comparison)",
    "SPARD: Self-Paced Curriculum for RL Alignment via Integrating Reward Dynamics and Data Utility (arXiv:2604.07837, April 2026) — PAWA (momentum-based exponential up-weighting when LCB of reward improvement is positive) and RADR (data category rebalancing); applied to open-ended LLM alignment; no gradient-variance analysis; no span/type/argument decomposition; PAWA momentum philosophy vs. theorem-derived convergence-gap philosophy: the Signal Topology Theorem identifies gap-to-convergence as the relevant quantity, directly motivating the gap-based formula over SPARD's momentum formula",
    "VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models (arXiv:2509.19803, September 2025) — between-sample variance for difficulty-based data selection in math RLVR; +4.67 points average on Qwen3-8B-Base; explicit distinction: VCRL uses between-sample variance for data selection; Signal Topology Theorem uses within-sample reward-component topology for skill ordering",
    "RuCL: Stratified Rubric-Based Curriculum Learning for MLLM Reasoning (arXiv:2602.21628, 2026) — GRPO with two-tier decomposed reward (foundational + advanced rubrics), Appendix B gradient variance decomposition showing reliable foundational signals reduce early-training gradient variance; +7.83% average across 7 benchmarks; closest methodological parallel for curriculum-via-reward-decomposition — the Signal Topology Theorem deepens RuCL's analysis by proving WHY span-IoU is reliably low-variance (continuous topology) while type-conjunction is reliably high-variance (Bernoulli at low-probability regime), deriving the mechanism that RuCL observes but does not formalize",
    "EGCA: Execution-Grounded Credit Assignment (arXiv:2603.16158, ICLR 2026 Workshop) — concentrates GRPO advantage on causal token spans via reference-execution comparison for code generation; requires executable code with test cases and reference execution traces; inapplicable to IE; credit assignment is causal (execution divergence) vs. structural (reward topology); cited to position the space of span-level credit assignment approaches and distinguish from IE-specific topology analysis",
    "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization (arXiv:2601.05242, ICML 2026, NVIDIA) — prevents advantage collapse by normalizing each reward's advantage independently; orthogonal to theorem-derived adaptive weights (normalization-level vs. aggregation-level); combination of GDPO normalization + convergence-gap adaptive weights is a concrete future direction",
    "MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (arXiv:2601.07208, January 2026) — contextual bandit formulation for dynamic reward weights; bi-level optimization with Conductor network; more complex than theorem-derived simple formula; no IE application",
    "On the Learning Dynamics of RLVR at the Edge of Competence (arXiv:2602.14872, 2026) — formally proves relay regime for task-level difficulty ordering in L-step compositional reasoning (Theorem 5.2); Signal Topology Theorem extends relay concept from task level to reward-component level within a single IE task type, with span-IoU continuity providing the smooth gradient handoff analogous to task-level difficulty smoothness",
    "Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization (arXiv:2604.19857, April 2026) — Reward Decomposition Theorem bounding sub-optimality of decomposed vs. joint GRPO optimization at O(1/√T); Signal Topology Theorem complements by identifying the structural IE-specific property (continuous span-IoU topology) that makes early-training variance reduction benefit dominate this bounded cost",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (arXiv:2509.11452, 2025) — proves fixed-weight scalarization provably suboptimal for non-convex multi-objective RL Pareto fronts; motivation for adaptive component weights",
    "APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574, 2026) — identifies variance hijacking; conceptually aligned with theorem's prediction that binary type-conjunction component has higher variance and would dominate gradients without topology-aware decomposition",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv:2304.08085) — Flan-T5-XXL (11B), Trigger F1=77.13%, Argument F1=72.94% on ACE2005 — primary SFT upper bound",
    "Locate and Label: A Two-stage Identifier for Nested Named Entity Recognition (arXiv:2105.06804) — architectural evidence that boundary detection is a prerequisite for entity typing: 36.73% F1 drop for long entities on ACE04 when boundary regression is removed; architectural motivation for the span-first convergence ordering that the theorem derives from gradient variance",
    "T2-NER: Unified Named Entity Recognition as Two-stage Span-based Entity Typing (TACL 2023) — span-then-type two-stage decomposition improves NER by +0.56% F1; additional architectural evidence",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (arXiv 2025)",
    "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support (EMNLP 2025 Findings)",
    "R1-RE: Cross-Domain Relation Extraction with RLVR (arXiv:2507.04642, July 2025)",
    "Beyond Path Selection: Better LLMs for Scientific Information Extraction with MimicSFT and R2GRPO (arXiv:2505.22068, May 2025)",
    "EXTRACT-0: A Specialized Language Model for Document Information Extraction (arXiv:2509.22906, September 2025)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "RAMS: Multi-Sentence Argument Linking (ACL 2020)",
    "WikiEvents: Document-level Event Argument Extraction (NAACL 2021)"
  ],
  "description": "Joint NER+RE+EE GRPO training fails on event extraction because existing reward designs treat (span, type) pairs as atomic units, conflating a continuous signal (span-IoU) with a binary signal (type-conjunction) and eliminating the gradient variance ordering that would otherwise produce implicit curriculum. CurriculumRLVR-IE's primary contribution is the **Signal Topology Theorem**: a formal proof that in GRPO for IE, the topological property of each reward component — continuous (span-IoU, Beta-distributed), binary (type-conjunction, Bernoulli at low-probability regime in early training), or compositional (argument F1, compound Bernoulli variance) — determines its gradient variance in early training, which in turn determines convergence ordering (span → type → argument) without explicit scheduling. This extends the relay regime of arXiv:2602.14872 from task-level difficulty ordering to reward-component-level topology ordering within a single IE task type, and complements arXiv:2604.19857's Reward Decomposition Theorem by identifying the specific structural property (span-IoU continuity) that makes variance reduction benefit dominate the bounded sub-optimality cost. Two direct applications follow from the theorem: (1) the span-boundary-decoupled reward design (span-IoU isolated from type-conjunction, each assigned to its correct topological class) as the theorem's algorithmic instantiation; (2) the convergence-gap adaptive weight formula w_i(t) = max(ε, θ−F1_i(t))/σ_i(t) as the theorem-derived curriculum enforcement mechanism — gap-based rather than momentum-based (contrasting with SPARD's PAWA) because the theorem identifies gap-to-convergence, not rate-of-progress, as the relevant quantity. CSPO (arXiv:2604.10918, ACL 2026) demonstrates empirically that component-specific token routing helps for table-to-LaTeX generation ('reward ambiguity' framing) without theoretical characterization of WHY components have different convergence dynamics; EGCA (arXiv:2603.16158) does causal span credit assignment for code generation (requires reference execution, inapplicable to IE); neither provides the topology-based gradient variance derivation or the sequential convergence prediction. GDPO (arXiv:2601.05242, ICML 2026) prevents advantage collapse at the normalization level — orthogonal and combinable with the proposed adaptive aggregation weights. Primary empirical contribution: per-component F1 learning curves logged every 50 GRPO steps as falsifiable evidence for or against the theorem's convergence ordering prediction — the first published training dynamics for GRPO-IE. Primary foil: ProUIE (Qwen3-4B, ACE2005 Trigger=70.65%, Argument=52.58%); scale confound (8B vs. 4B) explicitly acknowledged, with fixed-weight Qwen3-8B ablation as the primary same-scale baseline for reward design effect. Backbone: Qwen3-8B-Instruct with LoRA (rank 16). Compute: 50-example dry run + one main GRPO run + checkpoint-derived ablations, ~130-165 H100-hours within 200 H100-hour ceiling. Primary target: ACL 2027 Main via February 2027 ARR (all modes); EMNLP 2026 Findings via May 25 ARR is auto-mode-only stretch goal with zero timeline margin.",
  "project_name": "joint_ie_decomposed_rlvr",
  "source": "web_research"
}
```

**Summary of major revision decisions:**

The paper was stuck at 3.5/5 because three equal contributions each read as incremental extensions of existing work. The revision makes one structural change that addresses all four reviewer issues simultaneously:

1. **CSPO (Issue 1)**: Added to landscape with proper 1-paragraph differentiation. CSPO provides empirical motivation (component routing helps) without the theoretical mechanism — the Signal Topology Theorem is framed as providing the theoretical foundation for CSPO's observation.

2. **Compound novelty attrition (Issue 2)**: Resolved by restructuring from "three equal contributions" to "one theorem + two applications." The abstract now leads with the Signal Topology Theorem as the paper's identity. The theorem is genuinely novel: no prior paper (not CSPO, not RuCL, not arXiv:2602.14872) formally characterizes *why* continuous vs. binary reward topology determines gradient variance ordering and implicit curriculum emergence in GRPO-IE.

3. **Scale confound (Issue 3)**: Explicitly fixed — fixed-weight Qwen3-8B is now the *primary* baseline for reward design effect; ProUIE-4B is repositioned as a cross-system reference with explicit scale confound caveat. H4 is rephrased accordingly.

4. **Timeline (Issue 4)**: ACL 2027 via Feb 2027 ARR is explicitly the primary target for manual and human-in-loop modes. EMNLP 2026 is auto-mode-only with explicit acknowledgment of zero margin.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d987b9e-65a8-48c0-bea7-2fd616b6021f",
  "isSidechain": false,
  "requestId": "req_011Catb9eoVeNMD4jx8G6jba",
  "type": "assistant",
  "uuid": "5d10f237-263d-455a-9505-b9fc4d994fa8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WKdeGXsadXJ8Ves96gXT7s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 45304,
      "output_tokens": 12360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12360,
          "cache_read_input_tokens": 45304,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weightin…",
  "leafUuid": "5d10f237-263d-455a-9505-b9fc4d994fa8",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled curriculum rewards for IE task decomposition",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CurriculumRLVR-IE: Span-Boundary-Decoupled GRPO with Adaptive Weightin…",
  "leafUuid": "5d10f237-263d-455a-9505-b9fc4d994fa8",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Span-decoupled curriculum rewards for IE task decomposition",
  "sessionId": "1ffe918b-ce36-4b62-a5ce-cb5a2b75c457"
}
```

---
