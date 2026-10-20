# Research conversation: When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models ## Description Wh

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-3/3f5fd744-9b44-4834-9e52-865d235777f7.jsonl`
- **Structured JSON:** [`639b0037e34dde356503.json`](../../sessions/63/639b0037e34dde356503.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:40:47.122Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:40:47.122Z",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "content": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}, 'human_in_loop': {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}, 'auto_research': {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}}\n\n## Inspired By\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Target Venues\n- ICLR 2027 (full paper deadline: ~September 2026 AoE — primary target, 12-week comfortable timeline; the domain amenability hypothesis and actionability framing position this as a timely contribution to a live debate)\n- ICML 2027 (full paper deadline: ~January 2027 AoE — safe fallback with time for extended experiments and thorough analysis)\n- AAAI 2027 (full paper deadline: July 28, 2026 AoE — aggressive 10-week target, feasible with human-in-loop or auto-research timeline)\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:40:47.129Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:40:47.129Z",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

## Round 1

60 recorded events

### User

_source line 3 · 2026-05-20T05:40:47.157Z_

# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models

## Description
When do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.

## Core Problem
The mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).

## Opportunity
The interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.

## Landscape
THE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.

ACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.

PRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.

INTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.

SPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.

SAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.

CIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.

SELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.

GENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.

## Approach
We conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.

**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**

*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.

*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.

*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.

**Phase 2: Multi-Method Causal Circuit Tracing.**

Tier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).

Tier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.

**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.

Components are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.

**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:

(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.

(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.

**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:

**Core granularities (all 3 PRMs × 3 core benchmarks):**
(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);
(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;
(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.

**Extension granularities (single most informative PRM × 3 core benchmarks):**
(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;
(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.

We benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.

**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:

*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?

*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.

This produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.

**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.

**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.

## Resource Estimate
{'manual': {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}, 'human_in_loop': {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}, 'auto_research': {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}}

## Inspired By
Primary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing

## Target Venues
- ICLR 2027 (full paper deadline: ~September 2026 AoE — primary target, 12-week comfortable timeline; the domain amenability hypothesis and actionability framing position this as a timely contribution to a live debate)
- ICML 2027 (full paper deadline: ~January 2027 AoE — safe fallback with time for extended experiments and thorough analysis)
- AAAI 2027 (full paper deadline: July 28, 2026 AoE — aggressive 10-week target, feasible with human-in-loop or auto-research timeline)

## Key References
- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)
- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)
- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)
- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)
- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)
- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)
- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)
- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)
- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)
- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)
- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)
- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)
- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)
- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)
- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)
- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)
- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)
- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)
- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)
- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)
- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)
- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)
- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)
- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)
- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)
- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)
- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "6128e8e8-5413-4d15-aafa-fcdbda3858f6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:40:47.155Z_

```json
{
  "parentUuid": "6128e8e8-5413-4d15-aafa-fcdbda3858f6",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "e26f91f3-4057-44bb-8982-c1c68d8bfef4",
  "timestamp": "2026-05-20T05:40:47.155Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:40:47.155Z_

```json
{
  "parentUuid": "e26f91f3-4057-44bb-8982-c1c68d8bfef4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8fd37c67-891d-4f25-91d4-5a5e495b1770",
  "timestamp": "2026-05-20T05:40:47.155Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "8fd37c67-891d-4f25-91d4-5a5e495b1770",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:40:55.308Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this field before making any recommendations.

Let me start by reading the proposal carefully, then conduct targeted web searches.

The proposal is about testing when mechanistic interventions succeed on Process Reward Models (PRMs), comparing feature-level, neuron-level, and circuit-level interventions. Key aspects to evaluate:

1. Baselines - are they sufficient?
2. Experimental design - any gaps?


3. Evaluation metrics - comprehensive enough?
4. Ablation design - can it isolate component contributions?
5. Compute-normalized comparisons - fair?
6. Feasibility - resources, data, timeline

Now I need to search for the key papers mentioned and understand current experimental standards in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fd37c67-891d-4f25-91d4-5a5e495b1770",
  "isSidechain": false,
  "requestId": "req_011CbDHUgnZU5AeenWzzfrQj",
  "type": "assistant",
  "uuid": "a7fe2370-aa80-45e6-9d5d-8e6f84d63b2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWohCkkcriaqLUyiLZrwo7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 14448,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 318,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T05:40:55.312Z_

I need to conduct thorough background research before making any experimental design recommendations. Let me first search for the key papers and current experimental standards in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7fe2370-aa80-45e6-9d5d-8e6f84d63b2b",
  "isSidechain": false,
  "requestId": "req_011CbDHUgnZU5AeenWzzfrQj",
  "type": "assistant",
  "uuid": "7f54d739-3365-4adc-a14b-fce24fd4b769",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWohCkkcriaqLUyiLZrwo7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 14448,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 318,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T05:40:55.433Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KxcKiJd7yxsexWnpK8opws`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f54d739-3365-4adc-a14b-fce24fd4b769",
  "isSidechain": false,
  "requestId": "req_011CbDHUgnZU5AeenWzzfrQj",
  "type": "assistant",
  "uuid": "966e6f4d-c517-4870-a135-3fde9273d653",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWohCkkcriaqLUyiLZrwo7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9798,
      "cache_read_input_tokens": 14448,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 318,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 9798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9798
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T05:40:55.439Z_

<details><summary>↩ Tool result · `toolu_01KxcKiJd7yxsexWnpK8opws`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "966e6f4d-c517-4870-a135-3fde9273d653",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "d0285457-e135-489d-9130-e1628a96abcb",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "966e6f4d-c517-4870-a135-3fde9273d653",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:40:59.171Z_

Now let me conduct my pre-assessment research. I'll run multiple searches in parallel to understand the current experimental standards.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0285457-e135-489d-9130-e1628a96abcb",
  "isSidechain": false,
  "requestId": "req_011CbDHVJ6q5MvNkd75CZXD6",
  "type": "assistant",
  "uuid": "e08e3f6d-9427-4d1e-90f9-e6315e0e4cdd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WwHyunoe8s5MiLeqxAwTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 24246,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 24246,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:40:59.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014NyHAkVej8xwcDTQXBAt7B`</summary>

```json
{
  "query": "SteerRM SAE debiasing reward models experimental setup baselines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e08e3f6d-9427-4d1e-90f9-e6315e0e4cdd",
  "isSidechain": false,
  "requestId": "req_011CbDHVJ6q5MvNkd75CZXD6",
  "type": "assistant",
  "uuid": "3d067581-453c-4b01-a9a1-f21b88384d35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WwHyunoe8s5MiLeqxAwTK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 24246,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 24246,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T05:41:07.667Z_

<details><summary>↩ Tool result · `toolu_014NyHAkVej8xwcDTQXBAt7B`</summary>

```text
Web search results for query: "SteerRM SAE debiasing reward models experimental setup baselines 2026"

Links: [{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"},{"title":"[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/abs/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/html/2603.12795"},{"title":"Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance","url":"https://arxiv.org/pdf/2512.23461"},{"title":"ENHANCING LLM STEERING THROUGH SPARSE AUTOENCODER-BASED VECTOR REFINEMENT","url":"https://www.arxiv.org/pdf/2509.23799"}]

Based on the search results, here's information about SteerRM's experimental setup and baselines:

## Experimental Setup

SteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.

The evaluation focused on six reward models on RM-Bench, where SteerRM improved Hard-split accuracy by 7.3 points on average while preserving overall performance. 

Results on a Gemma-based reward model and a controlled non-format bias further suggest generalization across RM architectures and bias types.

## Key Findings

Format-related features are concentrated in shallow layers and transfer across models, revealing shared architecture-level bias encoding patterns.

In a controlled politeness-bias setting, SteerRM recovered accuracy from 61.0% to 66.0%, suggesting that the same contrastive SAE intervention can mitigate controlled stylistic biases beyond Markdown formatting.

## Method Overview

SteerRM is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. Existing debiasing methods typically require retraining or architectural modifications, while direct activation suppression degrades performance due to representation entanglement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d067581-453c-4b01-a9a1-f21b88384d35",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "ae29eb8a-1b27-4de3-b6c5-6baaa69271ad",
  "toolUseResult": {
    "query": "SteerRM SAE debiasing reward models experimental setup baselines 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01THVuv3xgT1J4G7aVze9uGF",
        "content": [
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          },
          {
            "title": "[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2603.12795"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2603.12795"
          },
          {
            "title": "Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance",
            "url": "https://arxiv.org/pdf/2512.23461"
          },
          {
            "title": "ENHANCING LLM STEERING THROUGH SPARSE AUTOENCODER-BASED VECTOR REFINEMENT",
            "url": "https://www.arxiv.org/pdf/2509.23799"
          }
        ]
      },
      "Based on the search results, here's information about SteerRM's experimental setup and baselines:\n\n## Experimental Setup\n\nSteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.\n\nThe evaluation focused on six reward models on RM-Bench, where SteerRM improved Hard-split accuracy by 7.3 points on average while preserving overall performance. \n\nResults on a Gemma-based reward model and a controlled non-format bias further suggest generalization across RM architectures and bias types.\n\n## Key Findings\n\nFormat-related features are concentrated in shallow layers and transfer across models, revealing shared architecture-level bias encoding patterns.\n\nIn a controlled politeness-bias setting, SteerRM recovered accuracy from 61.0% to 66.0%, suggesting that the same contrastive SAE intervention can mitigate controlled stylistic biases beyond Markdown formatting.\n\n## Method Overview\n\nSteerRM is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. Existing debiasing methods typically require retraining or architectural modifications, while direct activation suppression degrades performance due to representation entanglement."
    ],
    "durationSeconds": 7.996998861,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3d067581-453c-4b01-a9a1-f21b88384d35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:41:10.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014adZZt1aY6BJ84EQLghHiH`</summary>

```json
{
  "query": "CIRM causal inference reward model debiasing Shinoda ACL 2026 experimental design baselines evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae29eb8a-1b27-4de3-b6c5-6baaa69271ad",
  "isSidechain": false,
  "requestId": "req_011CbDHWCAfevVk7MDKUBn14",
  "type": "assistant",
  "uuid": "e134e788-d347-4ac9-a941-c252b8189601",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WyXARSst19d1H1gmMC7pcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 25091,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 654,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25091,
          "cache_creation_input_tokens": 654,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 654
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:41:20.041Z_

<details><summary>↩ Tool result · `toolu_014adZZt1aY6BJ84EQLghHiH`</summary>

```text
Web search results for query: "CIRM causal inference reward model debiasing Shinoda ACL 2026 experimental design baselines evaluation"

Links: [{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"}]

Based on the search results, I found relevant information about CIRM (Causal Inference Reward Model). Here's what I discovered:

## CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention

CIRM is a method that computes activations of neurons in reward models and identifies bias-specific neurons, then at inference time replaces the activations of these identified neurons with their medians to debias rewards.

### Approach and Design

The method identifies the top and bottom k neurons as bias-specific neurons through correlation analysis and repeats this process for five types of biases. The approach computes the medians of the activations for each neuron.

### Problem Context

Reward models have been reported to suffer from biases, with length bias being one of the most famous cases where reward models tend to assign higher scores to longer responses regardless of their actual helpfulness.

The search results indicate this is a recent work (from approximately 3 weeks ago based on the arxiv listing), though I didn't find explicit confirmation of the ACL 2026 venue or all the experimental details about baselines and evaluation metrics you mentioned. The paper appears to address multiple bias types in reward models using a causal inference approach applied at inference time without requiring retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e134e788-d347-4ac9-a941-c252b8189601",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "45ec88c0-ab89-438f-9a21-2aa597f56c2e",
  "toolUseResult": {
    "query": "CIRM causal inference reward model debiasing Shinoda ACL 2026 experimental design baselines evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ux4udY924wxf94ERfr2Zy4",
        "content": [
          {
            "title": "Debiasing Reward Models via Causally Motivated Inference-Time Intervention",
            "url": "https://arxiv.org/html/2604.27495"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/pdf/2507.15698"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          }
        ]
      },
      "Based on the search results, I found relevant information about CIRM (Causal Inference Reward Model). Here's what I discovered:\n\n## CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention\n\nCIRM is a method that computes activations of neurons in reward models and identifies bias-specific neurons, then at inference time replaces the activations of these identified neurons with their medians to debias rewards.\n\n### Approach and Design\n\nThe method identifies the top and bottom k neurons as bias-specific neurons through correlation analysis and repeats this process for five types of biases. The approach computes the medians of the activations for each neuron.\n\n### Problem Context\n\nReward models have been reported to suffer from biases, with length bias being one of the most famous cases where reward models tend to assign higher scores to longer responses regardless of their actual helpfulness.\n\nThe search results indicate this is a recent work (from approximately 3 weeks ago based on the arxiv listing), though I didn't find explicit confirmation of the ACL 2026 venue or all the experimental details about baselines and evaluation metrics you mentioned. The paper appears to address multiple bias types in reward models using a causal inference approach applied at inference time without requiring retraining."
    ],
    "durationSeconds": 9.692225707000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e134e788-d347-4ac9-a941-c252b8189601",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:41:23.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XmfwtuKLSE7vCADLoHZPbc`</summary>

```json
{
  "query": "Basu et al \"Interpretability without Actionability\" mechanistic interventions clinical LM experimental setup 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45ec88c0-ab89-438f-9a21-2aa597f56c2e",
  "isSidechain": false,
  "requestId": "req_011CbDHX72PCMRudgpjZZRA5",
  "type": "assistant",
  "uuid": "db944617-450d-44f4-bde0-7ee4f1a03f37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gp9UR4KpLAzzMWuTkQBmh2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 25745,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25745,
          "cache_creation_input_tokens": 632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 632
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:41:30.488Z_

<details><summary>↩ Tool result · `toolu_01XmfwtuKLSE7vCADLoHZPbc`</summary>

```text
Web search results for query: "Basu et al "Interpretability without Actionability" mechanistic interventions clinical LM experimental setup 2026"

Links: [{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science","url":"https://gist.science/paper/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot...","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"},{"title":"Sanjay BASU | Research profile","url":"https://www.researchgate.net/profile/Sanjay-Basu"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF","url":"https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"}]

I found the paper! Here's information about the Basu et al. study on "Interpretability without actionability":

## Paper Overview

The paper is titled "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations" by Sanjay Basu and 7 other authors.

## Experimental Setup

The study compared four mechanistic interpretability methods -- concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct) -- for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).

## Key Findings

Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. Concept bottleneck steering corrected 17 of 85 missed hazards (20%) but simultaneously caused 25 of 47 correctly detected hazards to be missed (53%), indistinguishable from randomly modifying concept activations (p=0.84).

## Main Conclusion

The paper concludes that while mechanistic interpretability is a powerful tool for understanding models, it currently fails as a reliable mechanism for correcting errors in safety-critical applications. The study demonstrates a fundamental limitation: high-fidelity internal representations do not translate to actionable corrections via current inference-time steering methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db944617-450d-44f4-bde0-7ee4f1a03f37",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "f5e69290-59b0-46a6-a497-6545078b2fff",
  "toolUseResult": {
    "query": "Basu et al \"Interpretability without Actionability\" mechanistic interventions clinical LM experimental setup 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KJizkg9YRJzP6wNgCuApyT",
        "content": [
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science",
            "url": "https://gist.science/paper/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot...",
            "url": "https://arxiv.org/abs/2603.18353"
          },
          {
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/html/2603.18353v1"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.18353"
          },
          {
            "title": "Sanjay BASU | Research profile",
            "url": "https://www.researchgate.net/profile/Sanjay-Basu"
          },
          {
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"
          }
        ]
      },
      "I found the paper! Here's information about the Basu et al. study on \"Interpretability without actionability\":\n\n## Paper Overview\n\nThe paper is titled \"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations\" by Sanjay Basu and 7 other authors.\n\n## Experimental Setup\n\nThe study compared four mechanistic interpretability methods -- concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct) -- for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).\n\n## Key Findings\n\nLinear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. Concept bottleneck steering corrected 17 of 85 missed hazards (20%) but simultaneously caused 25 of 47 correctly detected hazards to be missed (53%), indistinguishable from randomly modifying concept activations (p=0.84).\n\n## Main Conclusion\n\nThe paper concludes that while mechanistic interpretability is a powerful tool for understanding models, it currently fails as a reliable mechanism for correcting errors in safety-critical applications. The study demonstrates a fundamental limitation: high-fidelity internal representations do not translate to actionable corrections via current inference-time steering methods."
    ],
    "durationSeconds": 7.054438371000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "db944617-450d-44f4-bde0-7ee4f1a03f37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T05:41:34.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JGeCPayrEnj2txzS3B9Mi8`</summary>

```json
{
  "query": "Arad et al \"SAEs Are Good for Steering If You Select Right Features\" EMNLP 2025 output-score filtering experimental methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e69290-59b0-46a6-a497-6545078b2fff",
  "isSidechain": false,
  "requestId": "req_011CbDHXsmgk8zKGknygaJrS",
  "type": "assistant",
  "uuid": "a76a773c-4198-4024-b726-e93b76516675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CkFitCverdEAqA4xCAZZc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 26377,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 978,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 26377,
          "cache_creation_input_tokens": 978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 978
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:41:49.592Z_

<details><summary>↩ Tool result · `toolu_01JGeCPayrEnj2txzS3B9Mi8`</summary>

```text
Web search results for query: "Arad et al "SAEs Are Good for Steering If You Select Right Features" EMNLP 2025 output-score filtering experimental methodology"

Links: [{"title":"SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.519/"},{"title":"Dana Arad 🛫 EMNLP25 on X: \"Tried steering with SAEs and found that not all features behave as expected? Check out our new preprint - \"SAEs Are Good for Steering - If You Select the Right Features\" 🧵 https://t.co/M7YysXwatx\" / X","url":"https://x.com/dana_arad4/status/1927370565964235027"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250520063A/abstract"},{"title":"[2505.20063] SAEs Are Good for Steering -- If You Select the Right Features","url":"https://arxiv.org/abs/2505.20063"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features","url":"https://arxiv.org/pdf/2505.20063"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://arxiv.org/html/2505.20063v1"},{"title":"dblp: SAEs Are Good for Steering - If You Select the Right Features.","url":"https://dblp.org/rec/journals/corr/abs-2505-20063.html"}]

Based on the search results, I found relevant information about the Arad et al. paper on SAEs for steering. Here's what I found regarding the output-score filtering experimental methodology:

## Paper Overview

The paper "SAEs Are Good for Steering – If You Select the Right Features" by Dana Arad, Aaron Mueller, and Yonatan Belinkov was published at EMNLP 2025 (pages 10241–10259).

## Methodological Approach

The authors distinguish between two types of features: input features that mainly capture patterns in the model's input, and output features that have a human-understandable effect on the model's output. They propose input and output scores to characterize and locate these types of features, and show that high values for both scores rarely co-occur in the same features.

## Output-Score Filtering Results

After filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.

The 2-3x improvements from filtering out features with low output scores makes SAE steering competitive with supervised methods.

## Evaluation Framework

The authors demonstrate the effectiveness of these insights on the recent AxBench, a benchmark for evaluating steering methods.

The full paper is available on both the ACL Anthology and arXiv (2505.20063) if you need more detailed information about the specific experimental methodology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a76a773c-4198-4024-b726-e93b76516675",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "5a16e80e-b9a0-4d17-b41a-82695d10734b",
  "toolUseResult": {
    "query": "Arad et al \"SAEs Are Good for Steering If You Select Right Features\" EMNLP 2025 output-score filtering experimental methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WApRdUvLjgsd2Cq9jd1Epc",
        "content": [
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.519/"
          },
          {
            "title": "Dana Arad 🛫 EMNLP25 on X: \"Tried steering with SAEs and found that not all features behave as expected? Check out our new preprint - \"SAEs Are Good for Steering - If You Select the Right Features\" 🧵 https://t.co/M7YysXwatx\" / X",
            "url": "https://x.com/dana_arad4/status/1927370565964235027"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250520063A/abstract"
          },
          {
            "title": "[2505.20063] SAEs Are Good for Steering -- If You Select the Right Features",
            "url": "https://arxiv.org/abs/2505.20063"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features",
            "url": "https://arxiv.org/pdf/2505.20063"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://arxiv.org/html/2505.20063v1"
          },
          {
            "title": "dblp: SAEs Are Good for Steering - If You Select the Right Features.",
            "url": "https://dblp.org/rec/journals/corr/abs-2505-20063.html"
          }
        ]
      },
      "Based on the search results, I found relevant information about the Arad et al. paper on SAEs for steering. Here's what I found regarding the output-score filtering experimental methodology:\n\n## Paper Overview\n\nThe paper \"SAEs Are Good for Steering – If You Select the Right Features\" by Dana Arad, Aaron Mueller, and Yonatan Belinkov was published at EMNLP 2025 (pages 10241–10259).\n\n## Methodological Approach\n\nThe authors distinguish between two types of features: input features that mainly capture patterns in the model's input, and output features that have a human-understandable effect on the model's output. They propose input and output scores to characterize and locate these types of features, and show that high values for both scores rarely co-occur in the same features.\n\n## Output-Score Filtering Results\n\nAfter filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.\n\nThe 2-3x improvements from filtering out features with low output scores makes SAE steering competitive with supervised methods.\n\n## Evaluation Framework\n\nThe authors demonstrate the effectiveness of these insights on the recent AxBench, a benchmark for evaluating steering methods.\n\nThe full paper is available on both the ACL Anthology and arXiv (2505.20063) if you need more detailed information about the specific experimental methodology."
    ],
    "durationSeconds": 15.095336136999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a76a773c-4198-4024-b726-e93b76516675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "5a16e80e-b9a0-4d17-b41a-82695d10734b",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Tool call

_source line 23 · 2026-05-20T05:41:53.163Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01REMHSzLcZav1dRjHkt2zQt`</summary>

```json
{
  "query": "ProcessBench PRM-BiasBench RM-Bench evaluation metrics process reward models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a16e80e-b9a0-4d17-b41a-82695d10734b",
  "isSidechain": false,
  "requestId": "req_011CbDHZHR1n5kJ15okfTPZU",
  "type": "assistant",
  "uuid": "be7ed5ea-a6d4-4819-bdd8-ba89ced9a958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Amv6svbPSdDjkorgaXB7G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 27355,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 27355,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T05:41:59.955Z_

<details><summary>↩ Tool result · `toolu_01REMHSzLcZav1dRjHkt2zQt`</summary>

```text
Web search results for query: "ProcessBench PRM-BiasBench RM-Bench evaluation metrics process reward models 2025 2026"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"ProcessBench: Identifying Process Errors in Mathematical Reasoning","url":"https://arxiv.org/pdf/2412.06559"},{"title":"Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://huggingface.co/papers/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"RM-Bench: Benchmarking Reward Models of Language Models with Subtlety   and Style","url":"https://arxiv.org/pdf/2410.16184"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/pdf/2501.07301"}]

Based on the search results, here's what I found about these process reward model evaluation benchmarks:

## ProcessBench

ProcessBench is used to evaluate process reward models (PRMs) and critic models, where general language models are prompted to critique each solution step by step. ProcessBench emphasizes step-by-step error detection in mathematical derivations, thereby increasing the granularity of the evaluation.

## PRMBench

PRMBench, based on PRM800K, employs GPT-4o for data optimization and constructs a fine-grained evaluation dataset comprising 6,216 instances. PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

## RM-Bench

RM-Bench is a novel benchmark designed to evaluate reward models based on their sensitivity to subtle content differences and resistance to style biases. RM-Bench strongly correlates with policy model performance and nearly 40 reward models were evaluated on it.

## PRM-BiasBench

PRM-BiasBench is a benchmark extending ProcessBench with controlled perturbations across 8 transformation types, along with an open-source diagnostic toolkit to enable systematic PRM robustness evaluation.

These benchmarks represent recent advances (2024-2025) in systematically evaluating process reward models across different dimensions of performance and robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be7ed5ea-a6d4-4819-bdd8-ba89ced9a958",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "db5d6f24-8b27-4943-b8ca-5f3357636cc6",
  "toolUseResult": {
    "query": "ProcessBench PRM-BiasBench RM-Bench evaluation metrics process reward models 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HCZgwhNL8ytAV5tUV4rra8",
        "content": [
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2412.06559"
          },
          {
            "title": "Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://huggingface.co/papers/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "RM-Bench: Benchmarking Reward Models of Language Models with Subtlety   and Style",
            "url": "https://arxiv.org/pdf/2410.16184"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "The Lessons of Developing Process Reward Models in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2501.07301"
          }
        ]
      },
      "Based on the search results, here's what I found about these process reward model evaluation benchmarks:\n\n## ProcessBench\n\nProcessBench is used to evaluate process reward models (PRMs) and critic models, where general language models are prompted to critique each solution step by step. ProcessBench emphasizes step-by-step error detection in mathematical derivations, thereby increasing the granularity of the evaluation.\n\n## PRMBench\n\nPRMBench, based on PRM800K, employs GPT-4o for data optimization and constructs a fine-grained evaluation dataset comprising 6,216 instances. PRMBench comprises 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.\n\n## RM-Bench\n\nRM-Bench is a novel benchmark designed to evaluate reward models based on their sensitivity to subtle content differences and resistance to style biases. RM-Bench strongly correlates with policy model performance and nearly 40 reward models were evaluated on it.\n\n## PRM-BiasBench\n\nPRM-BiasBench is a benchmark extending ProcessBench with controlled perturbations across 8 transformation types, along with an open-source diagnostic toolkit to enable systematic PRM robustness evaluation.\n\nThese benchmarks represent recent advances (2024-2025) in systematically evaluating process reward models across different dimensions of performance and robustness."
    ],
    "durationSeconds": 6.787701293999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "be7ed5ea-a6d4-4819-bdd8-ba89ced9a958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:42:02.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Aa4YXc5kjW6c2NXYpvz7RV`</summary>

```json
{
  "query": "Orgad et al \"Position Interpretability Can Be Actionable\" ICML 2026 evaluation criteria concreteness validation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db5d6f24-8b27-4943-b8ca-5f3357636cc6",
  "isSidechain": false,
  "requestId": "req_011CbDHa3hnoph5cRouBTjF1",
  "type": "assistant",
  "uuid": "12aec064-7c4d-468a-bac7-bea71735dee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUrWKtQeo37PX5Rtm5xpDL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 28321,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 28321,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 795
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T05:42:09.555Z_

<details><summary>↩ Tool result · `toolu_01Aa4YXc5kjW6c2NXYpvz7RV`</summary>

```text
Web search results for query: "Orgad et al "Position Interpretability Can Be Actionable" ICML 2026 evaluation criteria concreteness validation"

Links: [{"title":"The Hitchhiker's Guide to Actionable Interpretability","url":"https://actionable-interpretability-guide.github.io/"},{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161"},{"title":"ICML Poster Position: Interpretability Can Be Actionable","url":"https://icml.cc/virtual/2026/poster/67043"},{"title":"[2605.11161] Interpretability Can Be Actionable","url":"https://arxiv.org/abs/2605.11161"},{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"General Information | Workshop on Actionable Interpretability@COLM 2026","url":"https://actionable-interpretability.github.io/"},{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"}]

Based on the search results, I found relevant information about the Orgad et al. paper on actionable interpretability:

## Paper Overview

The position paper argues that the central missing ingredient for interpretability research is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.

## Evaluation Criteria: Concreteness and Validation

The authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.

Regarding the specific evaluation levels, high concreteness and high validation refers to precise specifications with demonstrated utility, informed by interpretability insights drawn either from the work itself or prior work.

## ICML 2026 Presentation

The paper identifies five domains where interpretability offers unique leverage and presents a framework for actionable interpretability with evaluation criteria aligned with practical outcomes. This work was presented as a position paper at ICML 2026.

The full paper is available on arXiv (2605.11161) and includes an actionability checklist for interpretability research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12aec064-7c4d-468a-bac7-bea71735dee7",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "98ad8ab5-b935-447a-a085-8c4988f47c9d",
  "toolUseResult": {
    "query": "Orgad et al \"Position Interpretability Can Be Actionable\" ICML 2026 evaluation criteria concreteness validation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GwWCLhHqxnJEgZJDfHjbhd",
        "content": [
          {
            "title": "The Hitchhiker's Guide to Actionable Interpretability",
            "url": "https://actionable-interpretability-guide.github.io/"
          },
          {
            "title": "Interpretability Can Be Actionable",
            "url": "https://arxiv.org/html/2605.11161"
          },
          {
            "title": "ICML Poster Position: Interpretability Can Be Actionable",
            "url": "https://icml.cc/virtual/2026/poster/67043"
          },
          {
            "title": "[2605.11161] Interpretability Can Be Actionable",
            "url": "https://arxiv.org/abs/2605.11161"
          },
          {
            "title": "Interpretability Can Be Actionable Hadas Orgad 1",
            "url": "https://arxiv.org/pdf/2605.11161"
          },
          {
            "title": "General Information | Workshop on Actionable Interpretability@COLM 2026",
            "url": "https://actionable-interpretability.github.io/"
          },
          {
            "title": "ICML 2026 Call for Papers",
            "url": "https://icml.cc/Conferences/2026/CallForPapers"
          }
        ]
      },
      "Based on the search results, I found relevant information about the Orgad et al. paper on actionable interpretability:\n\n## Paper Overview\n\nThe position paper argues that the central missing ingredient for interpretability research is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.\n\n## Evaluation Criteria: Concreteness and Validation\n\nThe authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.\n\nRegarding the specific evaluation levels, high concreteness and high validation refers to precise specifications with demonstrated utility, informed by interpretability insights drawn either from the work itself or prior work.\n\n## ICML 2026 Presentation\n\nThe paper identifies five domains where interpretability offers unique leverage and presents a framework for actionable interpretability with evaluation criteria aligned with practical outcomes. This work was presented as a position paper at ICML 2026.\n\nThe full paper is available on arXiv (2605.11161) and includes an actionability checklist for interpretability research."
    ],
    "durationSeconds": 6.815350837000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "12aec064-7c4d-468a-bac7-bea71735dee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:42:12.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018LCdFvbBBU8LPJEeEKi1Me`</summary>

```json
{
  "query": "RelP relevance patching circuit discovery language models NeurIPS 2025 mechanistic interpretability workshop experimental validation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ad8ab5-b935-447a-a085-8c4988f47c9d",
  "isSidechain": false,
  "requestId": "req_011CbDHakj7KjtfgJAPEc8KU",
  "type": "assistant",
  "uuid": "42ad5aa1-5e67-496d-9494-972219625553",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yc793AKd15SwFSYtsxEQgf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 29116,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29116,
          "cache_creation_input_tokens": 647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 647
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T05:42:22.094Z_

<details><summary>↩ Tool result · `toolu_018LCdFvbBBU8LPJEeEKi1Me`</summary>

```text
Web search results for query: "RelP relevance patching circuit discovery language models NeurIPS 2025 mechanistic interpretability workshop experimental validation"

Links: [{"title":"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching","url":"https://arxiv.org/html/2508.21258v2"},{"title":"GitHub - FarnoushRJ/RelP: [NeurIPS 2025 MechInterp Workshop - Spotlight] Official implementation of the paper \"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching\" · GitHub","url":"https://github.com/FarnoushRJ/RelP"},{"title":"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching | OpenReview","url":"https://openreview.net/forum?id=5PKPy82sWN"},{"title":"[2508.21258] RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching","url":"https://arxiv.org/abs/2508.21258"},{"title":"RelP: Faithful and Efficient Circuit Discovery via Relevance Patching | Request PDF","url":"https://www.researchgate.net/publication/395125313_RelP_Faithful_and_Efficient_Circuit_Discovery_via_Relevance_Patching"},{"title":"NeurIPS RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching","url":"https://neurips.cc/virtual/2025/loc/mexico-city/133241"},{"title":"RelP: Faithful and Efficient Circuit Discovery via Relevance Patching","url":"https://arxiv.org/html/2508.21258v1"}]

Based on the search results, here's what I found about RelP:

## RelP: Relevance Patching for Circuit Discovery

RelP was presented at the Mechanistic Interpretability Workshop at NeurIPS 2025, and it was accepted as a Spotlight presentation.

### Key Innovation

RelP replaces the local gradients in attribution patching with propagation coefficients derived from Layer-wise Relevance Propagation (LRP). LRP propagates the network's output backward through the layers, redistributing relevance to lower-level components according to local propagation rules that ensure properties such as relevance conservation or improved signal-to-noise ratio.

### Motivation

Activation patching is a standard method in mechanistic interpretability for localizing the components of a model responsible for specific behaviors, but it is computationally expensive to apply at scale. Attribution patching offers a faster, gradient-based approximation, yet suffers from noise and reduced reliability in deep, highly non-linear networks.

### Efficiency and Faithfulness

Like attribution patching, RelP requires only two forward passes and one backward pass, maintaining computational efficiency while improving faithfulness.

### Experimental Validation

RelP was validated across a range of models and tasks, showing that it more accurately approximates activation patching than standard attribution patching, particularly when analyzing residual stream and MLP outputs in the Indirect Object Identification (IOI) task. For instance, for MLP outputs in GPT-2 Large, attribution patching achieves a Pearson correlation of 0.006, whereas RelP reaches 0.956.

The official code implementation is available on GitHub, and the work includes comparisons with other methods like Integrated Gradients for circuit discovery.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42ad5aa1-5e67-496d-9494-972219625553",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "0988bc87-ce86-4884-8196-e20c766f5ca0",
  "toolUseResult": {
    "query": "RelP relevance patching circuit discovery language models NeurIPS 2025 mechanistic interpretability workshop experimental validation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BwobQ3wFznKQPckq3ASB8D",
        "content": [
          {
            "title": "RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching",
            "url": "https://arxiv.org/html/2508.21258v2"
          },
          {
            "title": "GitHub - FarnoushRJ/RelP: [NeurIPS 2025 MechInterp Workshop - Spotlight] Official implementation of the paper \"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching\" · GitHub",
            "url": "https://github.com/FarnoushRJ/RelP"
          },
          {
            "title": "RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching | OpenReview",
            "url": "https://openreview.net/forum?id=5PKPy82sWN"
          },
          {
            "title": "[2508.21258] RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching",
            "url": "https://arxiv.org/abs/2508.21258"
          },
          {
            "title": "RelP: Faithful and Efficient Circuit Discovery via Relevance Patching | Request PDF",
            "url": "https://www.researchgate.net/publication/395125313_RelP_Faithful_and_Efficient_Circuit_Discovery_via_Relevance_Patching"
          },
          {
            "title": "NeurIPS RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching",
            "url": "https://neurips.cc/virtual/2025/loc/mexico-city/133241"
          },
          {
            "title": "RelP: Faithful and Efficient Circuit Discovery via Relevance Patching",
            "url": "https://arxiv.org/html/2508.21258v1"
          }
        ]
      },
      "Based on the search results, here's what I found about RelP:\n\n## RelP: Relevance Patching for Circuit Discovery\n\nRelP was presented at the Mechanistic Interpretability Workshop at NeurIPS 2025, and it was accepted as a Spotlight presentation.\n\n### Key Innovation\n\nRelP replaces the local gradients in attribution patching with propagation coefficients derived from Layer-wise Relevance Propagation (LRP). LRP propagates the network's output backward through the layers, redistributing relevance to lower-level components according to local propagation rules that ensure properties such as relevance conservation or improved signal-to-noise ratio.\n\n### Motivation\n\nActivation patching is a standard method in mechanistic interpretability for localizing the components of a model responsible for specific behaviors, but it is computationally expensive to apply at scale. Attribution patching offers a faster, gradient-based approximation, yet suffers from noise and reduced reliability in deep, highly non-linear networks.\n\n### Efficiency and Faithfulness\n\nLike attribution patching, RelP requires only two forward passes and one backward pass, maintaining computational efficiency while improving faithfulness.\n\n### Experimental Validation\n\nRelP was validated across a range of models and tasks, showing that it more accurately approximates activation patching than standard attribution patching, particularly when analyzing residual stream and MLP outputs in the Indirect Object Identification (IOI) task. For instance, for MLP outputs in GPT-2 Large, attribution patching achieves a Pearson correlation of 0.006, whereas RelP reaches 0.956.\n\nThe official code implementation is available on GitHub, and the work includes comparisons with other methods like Integrated Gradients for circuit discovery."
    ],
    "durationSeconds": 9.477817530999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "42ad5aa1-5e67-496d-9494-972219625553",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T05:42:22.104Z_

```json
{
  "parentUuid": "0988bc87-ce86-4884-8196-e20c766f5ca0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e994f2a0-59dc-45b5-9c52-d3babb328319",
  "timestamp": "2026-05-20T05:42:22.104Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T05:42:25.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V5UcvxNtV9imto7ccByHSM`</summary>

```json
{
  "query": "CLT-Forge cross-layer transcoders attribution graphs 1B scale mechanistic interpretability 2026 limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e994f2a0-59dc-45b5-9c52-d3babb328319",
  "isSidechain": false,
  "requestId": "req_011CbDHbgQS679x8nHNGwV34",
  "type": "assistant",
  "uuid": "198ed761-fa8c-4917-974d-c1af9b19a9f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rrp5NnDwsyMbzbaiz4nbAA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 29763,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 29763,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T05:42:34.609Z_

<details><summary>↩ Tool result · `toolu_01V5UcvxNtV9imto7ccByHSM`</summary>

```text
Web search results for query: "CLT-Forge cross-layer transcoders attribution graphs 1B scale mechanistic interpretability 2026 limitations"

Links: [{"title":"CLT-Forge: Scalable Cross-Layer Transcoder Library","url":"https://www.emergentmind.com/papers/2603.21014"},{"title":"(PDF) CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://www.researchgate.net/publication/403072082_CLT-Forge_A_Scalable_Library_for_Cross-Layer_Transcoders_and_Attribution_Graphs"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/html/2603.21014v1"},{"title":"CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/pdf/2603.21014"},{"title":"Cross-Layer Transcoders (CLTs)","url":"https://www.emergentmind.com/topics/cross-layer-transcoders-clts"},{"title":"[2603.21014] CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs","url":"https://arxiv.org/abs/2603.21014"},{"title":"Transcoders find interpretable LLM feature circuits","url":"https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"},{"title":"GitHub - LLM-Interp/CLT-Forge: A Mechanistic Interpretability Toolkit for Cross-Layer Transcoder Training and Attribution-Graph Visualization · GitHub","url":"https://github.com/LLM-Interp/CLT-Forge"}]

Based on the search results, here's what I found about CLT-Forge, cross-layer transcoders, attribution graphs, and the 1B scale work in mechanistic interpretability:

## Overview

CLT-Forge is the first unified open-source framework for scalable training and interpretability of Cross-Layer Transcoders. The library integrates efficient feature-sharded training, compressed activation caching, automated interpretability, attribution graph computation, and an extensible visualization interface into a single workflow.

## 1B Scale Training

With feature sharding across 8 large GPUs, the framework trained CLTs with about 1.5 million features on a 1B-parameter model. Compressed activation caching cut storage from ~20 TB to ~4 TB with only a small accuracy trade-off (a few percent).

## Key Components

The framework integrates scalable distributed training with model sharding and compressed activation caching, a unified automated interpretability pipeline for feature analysis and explanation, attribution graph computation using Circuit-Tracer, and a flexible visualization interface.

## Limitations

A major limitation identified in the research is that attribution graphs are often large and redundant, limiting their interpretability in practice, with the size of attribution graphs potentially growing to hundreds of nodes, making them difficult to analyze in practice. Cross-Layer Transcoders address this by sharing features across layers while preserving layer-specific decoding, yielding more compact representations, but remain difficult to train and analyze at scale.

The work was published on March 22, 2026, and the code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "198ed761-fa8c-4917-974d-c1af9b19a9f2",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "6f64b5fc-42a5-49c5-ba2b-4905f48ce4d0",
  "toolUseResult": {
    "query": "CLT-Forge cross-layer transcoders attribution graphs 1B scale mechanistic interpretability 2026 limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Hs2UKq8D7xP6vq3P2mvjd",
        "content": [
          {
            "title": "CLT-Forge: Scalable Cross-Layer Transcoder Library",
            "url": "https://www.emergentmind.com/papers/2603.21014"
          },
          {
            "title": "(PDF) CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs",
            "url": "https://www.researchgate.net/publication/403072082_CLT-Forge_A_Scalable_Library_for_Cross-Layer_Transcoders_and_Attribution_Graphs"
          },
          {
            "title": "CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs",
            "url": "https://arxiv.org/html/2603.21014v1"
          },
          {
            "title": "CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs",
            "url": "https://arxiv.org/pdf/2603.21014"
          },
          {
            "title": "Cross-Layer Transcoders (CLTs)",
            "url": "https://www.emergentmind.com/topics/cross-layer-transcoders-clts"
          },
          {
            "title": "[2603.21014] CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs",
            "url": "https://arxiv.org/abs/2603.21014"
          },
          {
            "title": "Transcoders find interpretable LLM feature circuits",
            "url": "https://www.researchgate.net/publication/397201244_Transcoders_find_interpretable_LLM_feature_circuits"
          },
          {
            "title": "GitHub - LLM-Interp/CLT-Forge: A Mechanistic Interpretability Toolkit for Cross-Layer Transcoder Training and Attribution-Graph Visualization · GitHub",
            "url": "https://github.com/LLM-Interp/CLT-Forge"
          }
        ]
      },
      "Based on the search results, here's what I found about CLT-Forge, cross-layer transcoders, attribution graphs, and the 1B scale work in mechanistic interpretability:\n\n## Overview\n\nCLT-Forge is the first unified open-source framework for scalable training and interpretability of Cross-Layer Transcoders. The library integrates efficient feature-sharded training, compressed activation caching, automated interpretability, attribution graph computation, and an extensible visualization interface into a single workflow.\n\n## 1B Scale Training\n\nWith feature sharding across 8 large GPUs, the framework trained CLTs with about 1.5 million features on a 1B-parameter model. Compressed activation caching cut storage from ~20 TB to ~4 TB with only a small accuracy trade-off (a few percent).\n\n## Key Components\n\nThe framework integrates scalable distributed training with model sharding and compressed activation caching, a unified automated interpretability pipeline for feature analysis and explanation, attribution graph computation using Circuit-Tracer, and a flexible visualization interface.\n\n## Limitations\n\nA major limitation identified in the research is that attribution graphs are often large and redundant, limiting their interpretability in practice, with the size of attribution graphs potentially growing to hundreds of nodes, making them difficult to analyze in practice. Cross-Layer Transcoders address this by sharing features across layers while preserving layer-specific decoding, yielding more compact representations, but remain difficult to train and analyze at scale.\n\nThe work was published on March 22, 2026, and the code is available on GitHub."
    ],
    "durationSeconds": 9.051450345999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "198ed761-fa8c-4917-974d-c1af9b19a9f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T05:42:37.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016qYgm7S6fGdpuicf5XuHdh`</summary>

```json
{
  "query": "CRA \"Causal Reward Adjustment\" SAE training PRM activations backdoor correction experimental design compute cost"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f64b5fc-42a5-49c5-ba2b-4905f48ce4d0",
  "isSidechain": false,
  "requestId": "req_011CbDHcbrs38hMk8MBru8pc",
  "type": "assistant",
  "uuid": "1ab9f503-2d62-420a-bf3c-44c889b8114d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hcf4LykWZGiQ2HSW77iRRZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 917,
      "cache_read_input_tokens": 30769,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 917,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30769,
          "cache_creation_input_tokens": 917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 917
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "1ab9f503-2d62-420a-bf3c-44c889b8114d",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Tool result

_source line 35 · 2026-05-20T05:42:45.107Z_

<details><summary>↩ Tool result · `toolu_016qYgm7S6fGdpuicf5XuHdh`</summary>

```text
Web search results for query: "CRA "Causal Reward Adjustment" SAE training PRM activations backdoor correction experimental design compute cost"

Links: [{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"},{"title":"Preprint. CONCEPT-SAE: ACTIVE CAUSAL PROBING OF VISUAL MODEL BEHAVIOR","url":"https://arxiv.org/pdf/2509.22015"},{"title":"Efficient Process Reward Model Training via Active Learning","url":"https://arxiv.org/html/2504.10559v1"},{"title":"Robust Reward Modeling for Large Language Models via Causal Decomposition","url":"https://arxiv.org/html/2604.13833"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/html/2507.15698"}]

Based on the search results, I found comprehensive information about CRA (Causal Reward Adjustment) and its experimental approach:

## Overview

CRA is a method that mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.

## Three-Step Approach

CRA consists of three steps: (1) extracting interpretable features from the reward model, (2) identifying confounding features associated with reward hacking, and (3) implementing backdoor adjustment using the identified features to mitigate the reward hacking problem.

## SAE Training on PRM Activations

In the first step, the method trains a sparse autoencoder (SAE) on the hidden representations of PRM. The SAE learns to encode each internal representation into a sparse latent vector, where each dimension corresponds to a distinct semantic feature.

## Identifying Reward Hacking Features

In the second step, the method detects which latent feature is the reward hacking feature by computing the activation distribution of each feature over two groups of reasoning steps—those labeled as reward hacking and those considered normal.

## Experimental Results

On MATH, the average accuracy increases from 57.3% to 60.2%, with an average gain of 2.9 percentage points, and on GSM8K, the accuracy improves from 77.9% to 79.5%, with an average gain of 1.6 percentage points.

## Training Details

SAEs are trained using the Adam optimizer (lr=0.001, cosine annealing) for 50 epochs with a batch size of 2,048 and a sparsity coefficient.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ab9f503-2d62-420a-bf3c-44c889b8114d",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "6e6081d3-3e36-4075-824f-df953bce2645",
  "toolUseResult": {
    "query": "CRA \"Causal Reward Adjustment\" SAE training PRM activations backdoor correction experimental design compute cost",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KEThY3vURfDfhsCKWGimMf",
        "content": [
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"
          },
          {
            "title": "Preprint. CONCEPT-SAE: ACTIVE CAUSAL PROBING OF VISUAL MODEL BEHAVIOR",
            "url": "https://arxiv.org/pdf/2509.22015"
          },
          {
            "title": "Efficient Process Reward Model Training via Active Learning",
            "url": "https://arxiv.org/html/2504.10559v1"
          },
          {
            "title": "Robust Reward Modeling for Large Language Models via Causal Decomposition",
            "url": "https://arxiv.org/html/2604.13833"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/html/2507.15698"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about CRA (Causal Reward Adjustment) and its experimental approach:\n\n## Overview\n\nCRA is a method that mitigates reward hacking by estimating the true reward of a reasoning path, training sparse autoencoders on the PRM's internal activations to recover interpretable features, then correcting confounding by using backdoor adjustment.\n\n## Three-Step Approach\n\nCRA consists of three steps: (1) extracting interpretable features from the reward model, (2) identifying confounding features associated with reward hacking, and (3) implementing backdoor adjustment using the identified features to mitigate the reward hacking problem.\n\n## SAE Training on PRM Activations\n\nIn the first step, the method trains a sparse autoencoder (SAE) on the hidden representations of PRM. The SAE learns to encode each internal representation into a sparse latent vector, where each dimension corresponds to a distinct semantic feature.\n\n## Identifying Reward Hacking Features\n\nIn the second step, the method detects which latent feature is the reward hacking feature by computing the activation distribution of each feature over two groups of reasoning steps—those labeled as reward hacking and those considered normal.\n\n## Experimental Results\n\nOn MATH, the average accuracy increases from 57.3% to 60.2%, with an average gain of 2.9 percentage points, and on GSM8K, the accuracy improves from 77.9% to 79.5%, with an average gain of 1.6 percentage points.\n\n## Training Details\n\nSAEs are trained using the Adam optimizer (lr=0.001, cosine annealing) for 50 epochs with a batch size of 2,048 and a sparsity coefficient."
    ],
    "durationSeconds": 7.787678196999987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1ab9f503-2d62-420a-bf3c-44c889b8114d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T05:42:47.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cturwyiy7rmgEuxGkQtRot`</summary>

```json
{
  "query": "process reward model debiasing fine-tuning baseline comparison 2025 2026 state of art"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e6081d3-3e36-4075-824f-df953bce2645",
  "isSidechain": false,
  "requestId": "req_011CbDHdNkbhVXaAVCdAkawb",
  "type": "assistant",
  "uuid": "1fd87d6e-bd3e-40b7-bac7-8fc333d6f310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017peZqTxh89hPuTma2EKkDM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 31686,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 31686,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T05:42:55.390Z_

<details><summary>↩ Tool result · `toolu_01Cturwyiy7rmgEuxGkQtRot`</summary>

```text
Web search results for query: "process reward model debiasing fine-tuning baseline comparison 2025 2026 state of art"

Links: [{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"[2605.02348v1] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/abs/2605.02348v1"},{"title":"[2605.02348] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/abs/2605.02348"},{"title":"Reward-Model Fine-Tuning","url":"https://www.emergentmind.com/topics/reward-model-based-fine-tuning"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"},{"title":"The Bidirectional Process Reward Model","url":"https://arxiv.org/pdf/2508.01682"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"}]

Based on the search results, here are the latest findings on process reward models, debiasing, fine-tuning, and baseline comparisons from 2025-2026:

## Recent Advances in Process Reward Models (2025-2026)

**State-of-the-Art Baselines:**
Fine-tuned LLM-based PRMs significantly outperform baseline PRMs based on original LLMs and are competitive with or better than state-of-the-art PRMs. Recent competitive models include RLHFlow-Llama3.1-8B, Qwen2.5-Math-7B-PRM800K, and Qwen2.5-7B-Skywork-PRM.

**Debiasing Approaches:**
Sequential debiasing proves most effective, raising mean bias scores by up to +0.40 over baseline while preserving fluency. One approach debias models at decoding time, using a Process Reward Model as a judge to score candidates for both fairness and fluency.

**Fine-Tuning Methods:**
PURE introduces a min-form credit assignment method for process supervised reinforcement learning, and supplementing PRM-based fine-tuning with just 10% verifiable rewards produces best results, achieving 82.5% accuracy on AMC23.

**Known Challenges:**
PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization, which is critical to addressing PRM reliability.

**Emerging Architectures:**
BiPRM consistently outperforms unidirectional baselines, achieving improvements of up to 31.9% in stepwise reward estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fd87d6e-bd3e-40b7-bac7-8fc333d6f310",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "be088382-916c-45f6-b631-e05537b62c4d",
  "toolUseResult": {
    "query": "process reward model debiasing fine-tuning baseline comparison 2025 2026 state of art",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Up6FFuSh1nUATnzmxbucna",
        "content": [
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "[2605.02348v1] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation",
            "url": "https://arxiv.org/abs/2605.02348v1"
          },
          {
            "title": "[2605.02348] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation",
            "url": "https://arxiv.org/abs/2605.02348"
          },
          {
            "title": "Reward-Model Fine-Tuning",
            "url": "https://www.emergentmind.com/topics/reward-model-based-fine-tuning"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/pdf/2507.15698"
          },
          {
            "title": "The Bidirectional Process Reward Model",
            "url": "https://arxiv.org/pdf/2508.01682"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          }
        ]
      },
      "Based on the search results, here are the latest findings on process reward models, debiasing, fine-tuning, and baseline comparisons from 2025-2026:\n\n## Recent Advances in Process Reward Models (2025-2026)\n\n**State-of-the-Art Baselines:**\nFine-tuned LLM-based PRMs significantly outperform baseline PRMs based on original LLMs and are competitive with or better than state-of-the-art PRMs. Recent competitive models include RLHFlow-Llama3.1-8B, Qwen2.5-Math-7B-PRM800K, and Qwen2.5-7B-Skywork-PRM.\n\n**Debiasing Approaches:**\nSequential debiasing proves most effective, raising mean bias scores by up to +0.40 over baseline while preserving fluency. One approach debias models at decoding time, using a Process Reward Model as a judge to score candidates for both fairness and fluency.\n\n**Fine-Tuning Methods:**\nPURE introduces a min-form credit assignment method for process supervised reinforcement learning, and supplementing PRM-based fine-tuning with just 10% verifiable rewards produces best results, achieving 82.5% accuracy on AMC23.\n\n**Known Challenges:**\nPRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization, which is critical to addressing PRM reliability.\n\n**Emerging Architectures:**\nBiPRM consistently outperforms unidirectional baselines, achieving improvements of up to 31.9% in stepwise reward estimation."
    ],
    "durationSeconds": 7.750428862999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1fd87d6e-bd3e-40b7-bac7-8fc333d6f310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T05:42:58.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014SatcUpSbvzHGkUvGUWdgf`</summary>

```json
{
  "query": "Wang et al \"Automatically Finding Reward Model Biases\" evolutionary bias discovery 2026 experimental methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be088382-916c-45f6-b631-e05537b62c4d",
  "isSidechain": false,
  "requestId": "req_011CbDHe8gJ8FKzzb5M4dECK",
  "type": "assistant",
  "uuid": "a7f9ded6-2935-4575-b8d5-6771009934d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhXzXY56DLtn2dUjxij9jj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 32630,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 32630,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T05:43:05.134Z_

<details><summary>↩ Tool result · `toolu_014SatcUpSbvzHGkUvGUWdgf`</summary>

```text
Web search results for query: "Wang et al "Automatically Finding Reward Model Biases" evolutionary bias discovery 2026 experimental methodology"

Links: [{"title":"[2602.15222] Automatically Finding Reward Model Biases","url":"https://arxiv.org/abs/2602.15222"},{"title":"Reward Model Biases in LLMs","url":"https://www.emergentmind.com/topics/reward-model-biases-in-llms"},{"title":"Automatically Finding Reward Model Biases","url":"https://www.arxiv.org/pdf/2602.15222"},{"title":"Automatically Finding Reward Model Biases","url":"https://arxiv.org/html/2602.15222"},{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/pdf/2603.03291"},{"title":"Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance","url":"https://arxiv.org/pdf/2512.23461"}]

Based on the search results, I found the paper you're looking for. Here's information about Wang et al.'s "Automatically Finding Reward Model Biases":

## Overview

The paper introduces and studies the research problem of automatically finding reward model biases in natural language.

## Methodology

The approach uses an LLM to iteratively propose and refine candidate biases. The paper offers a black-box pipeline that iteratively proposes and tests candidate biases following an evolutionary algorithm.

## Key Experimental Findings

The method recovered known biases and surfaced novel ones, including findings that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. 

The research shows evidence that evolutionary iteration outperforms flat best-of-N search, and validates the recall of the pipeline using synthetically injected biases.

## Publication Details

The paper was published on February 16, 2026, and is available on arXiv as paper 2602.15222. The corresponding author is Atticus Wang from MIT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7f9ded6-2935-4575-b8d5-6771009934d0",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "cca5f8d5-7e5b-405c-9355-6c273c68cb95",
  "toolUseResult": {
    "query": "Wang et al \"Automatically Finding Reward Model Biases\" evolutionary bias discovery 2026 experimental methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T2oUxtXuZv73F1aDtTNdGJ",
        "content": [
          {
            "title": "[2602.15222] Automatically Finding Reward Model Biases",
            "url": "https://arxiv.org/abs/2602.15222"
          },
          {
            "title": "Reward Model Biases in LLMs",
            "url": "https://www.emergentmind.com/topics/reward-model-biases-in-llms"
          },
          {
            "title": "Automatically Finding Reward Model Biases",
            "url": "https://www.arxiv.org/pdf/2602.15222"
          },
          {
            "title": "Automatically Finding Reward Model Biases",
            "url": "https://arxiv.org/html/2602.15222"
          },
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/pdf/2603.03291"
          },
          {
            "title": "Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance",
            "url": "https://arxiv.org/pdf/2512.23461"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about Wang et al.'s \"Automatically Finding Reward Model Biases\":\n\n## Overview\n\nThe paper introduces and studies the research problem of automatically finding reward model biases in natural language.\n\n## Methodology\n\nThe approach uses an LLM to iteratively propose and refine candidate biases. The paper offers a black-box pipeline that iteratively proposes and tests candidate biases following an evolutionary algorithm.\n\n## Key Experimental Findings\n\nThe method recovered known biases and surfaced novel ones, including findings that Skywork-V2-8B, a leading open-weight reward model, often mistakenly favors responses with redundant spacing and responses with hallucinated content. \n\nThe research shows evidence that evolutionary iteration outperforms flat best-of-N search, and validates the recall of the pipeline using synthetically injected biases.\n\n## Publication Details\n\nThe paper was published on February 16, 2026, and is available on arXiv as paper 2602.15222. The corresponding author is Atticus Wang from MIT."
    ],
    "durationSeconds": 7.130362848999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a7f9ded6-2935-4575-b8d5-6771009934d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T05:43:07.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RLzWWQMSimkS5HTfkjGn5x`</summary>

```json
{
  "query": "Xu et al \"Sparse Reward Subsystem\" value neurons dopamine neurons LLM experimental setup 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cca5f8d5-7e5b-405c-9355-6c273c68cb95",
  "isSidechain": false,
  "requestId": "req_011CbDHerN42BaxA4QosmpZY",
  "type": "assistant",
  "uuid": "62c9a5f0-aab7-4353-9005-5d762c476483",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ed4NHLxd7BQtBhh7vbyoYT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 615,
      "cache_read_input_tokens": 33518,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 615,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 33518,
          "cache_creation_input_tokens": 615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 615
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T05:43:15.564Z_

<details><summary>↩ Tool result · `toolu_01RLzWWQMSimkS5HTfkjGn5x`</summary>

```text
Web search results for query: "Xu et al "Sparse Reward Subsystem" value neurons dopamine neurons LLM experimental setup 2026"

Links: [{"title":"Sparse Reward Subsystem in Large Language Models","url":"https://arxiv.org/html/2602.00986"},{"title":"[2602.00986] Sparse Reward Subsystem in Large Language Models","url":"https://arxiv.org/abs/2602.00986"},{"title":"Sparse Reward Subsystem in Large Language Models","url":"https://www.arxiv.org/pdf/2602.00986"},{"title":"Dopamine neurons learn relative chosen value from probabilistic rewards","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5116238/"},{"title":"Reward-Bases: Dopaminergic Mechanisms for Adaptive Acquisition of Multiple Reward Types","url":"https://www.biorxiv.org/content/10.1101/2023.05.09.540067.full.pdf"}]

Based on the search results, I found the paper you're looking for. Here's what the research reveals:

## Overview

Xu et al. identify a sparse reward subsystem within the hidden states of Large Language Models (LLMs), drawing an analogy to the biological reward subsystem in the human brain.

## Key Findings

**Value Neurons:**
A sparse set of neurons within LLM hidden states performs functions analogous to biological value and dopamine neurons. The subsystem contains value neurons that represent the model's internal expectation of state value, and through intervention experiments, they establish the importance of these neurons for reasoning.

**Dopamine Neurons:**
Dopamine neurons within the reward subsystem encode reward prediction errors (RPE), exhibiting high activation when the reward is higher than expected and low activation when the reward is lower than expected.

## Experimental Robustness

The value neurons are robust across diverse datasets, model scales, and architectures; furthermore, they exhibit significant transferability across different datasets and models fine-tuned from the same base model.

The paper was published on February 1, 2026, on arXiv (paper ID 2602.00986).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62c9a5f0-aab7-4353-9005-5d762c476483",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "4aa0f574-bede-4d70-b120-0de636835eb8",
  "toolUseResult": {
    "query": "Xu et al \"Sparse Reward Subsystem\" value neurons dopamine neurons LLM experimental setup 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012epwcFx6QAgYiWRgkG222V",
        "content": [
          {
            "title": "Sparse Reward Subsystem in Large Language Models",
            "url": "https://arxiv.org/html/2602.00986"
          },
          {
            "title": "[2602.00986] Sparse Reward Subsystem in Large Language Models",
            "url": "https://arxiv.org/abs/2602.00986"
          },
          {
            "title": "Sparse Reward Subsystem in Large Language Models",
            "url": "https://www.arxiv.org/pdf/2602.00986"
          },
          {
            "title": "Dopamine neurons learn relative chosen value from probabilistic rewards",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5116238/"
          },
          {
            "title": "Reward-Bases: Dopaminergic Mechanisms for Adaptive Acquisition of Multiple Reward Types",
            "url": "https://www.biorxiv.org/content/10.1101/2023.05.09.540067.full.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research reveals:\n\n## Overview\n\nXu et al. identify a sparse reward subsystem within the hidden states of Large Language Models (LLMs), drawing an analogy to the biological reward subsystem in the human brain.\n\n## Key Findings\n\n**Value Neurons:**\nA sparse set of neurons within LLM hidden states performs functions analogous to biological value and dopamine neurons. The subsystem contains value neurons that represent the model's internal expectation of state value, and through intervention experiments, they establish the importance of these neurons for reasoning.\n\n**Dopamine Neurons:**\nDopamine neurons within the reward subsystem encode reward prediction errors (RPE), exhibiting high activation when the reward is higher than expected and low activation when the reward is lower than expected.\n\n## Experimental Robustness\n\nThe value neurons are robust across diverse datasets, model scales, and architectures; furthermore, they exhibit significant transferability across different datasets and models fine-tuned from the same base model.\n\nThe paper was published on February 1, 2026, on arXiv (paper ID 2602.00986)."
    ],
    "durationSeconds": 7.643282034000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "62c9a5f0-aab7-4353-9005-5d762c476483",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T05:43:19.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N2HgCcb7EYeo8swepY8Goj`</summary>

```json
{
  "query": "Lee et al \"Rigorous Interpretation Is a Form of Evaluation\" 2026 falsifiability reproducibility predictivity causal interpretability failure modes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aa0f574-bede-4d70-b120-0de636835eb8",
  "isSidechain": false,
  "requestId": "req_011CbDHfd5s3T5zsMnUgLhoH",
  "type": "assistant",
  "uuid": "c15792f8-e2b9-44dd-8b54-637a14ab1bb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bQieqMgwTXAykcaSfPFpj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 34133,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 34133,
          "cache_creation_input_tokens": 617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 617
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T05:43:27.443Z_

<details><summary>↩ Tool result · `toolu_01N2HgCcb7EYeo8swepY8Goj`</summary>

```text
Web search results for query: "Lee et al "Rigorous Interpretation Is a Form of Evaluation" 2026 falsifiability reproducibility predictivity causal interpretability failure modes"

Links: [{"title":"Rigorous Interpretation Is a Form of Evaluation","url":"https://arxiv.org/html/2605.05508v1"},{"title":"2026 Marks Shift From AI Hype to Rigorous Evaluation - NYC Today","url":"https://nationaltoday.com/us/ny/new-york/news/2026/04/10/2026-is-the-year-of-ai-evaluation-not-ai-hype/"},{"title":"A Roadmap for a Rigorous Science of Interpretability","url":"https://www.researchgate.net/publication/314115920_A_Roadmap_for_a_Rigorous_Science_of_Interpretability"},{"title":"A Survey on Interpretation Methods and Tools for ...","url":"https://arxiv.org/pdf/2506.05451"},{"title":"TOK May 2026 Title 6: “To what extent is interpretation a ...","url":"https://www.revisiondojo.com/blog/tok-may-2026-title-6-to-what-extent-is-interpretation-a-reliable-tool-in-the-production-of-knowledge"},{"title":"Towards A Rigorous Science of Interpretable Machine Learning","url":"https://arxiv.org/pdf/1702.08608"}]

Based on the search results, I found the paper "Rigorous Interpretation Is a Form of Evaluation" on arXiv. Here's what the paper discusses regarding your query terms:

**Falsifiability**: The paper emphasizes that interpretability claims must be falsifiable—that is, they can in principle be counterfactually disprovable—for the claims to be testable and reliably correctable. The authors critique a tendency in parts of the interpretability literature to prioritize intuition-building over the formulation of falsifiable hypotheses.

**Predictivity**: The paper explores how interpretability can function evaluatively by predicting potential issues before they arise by fully understanding the model's behavior, and generates interpretability claims that are predictive by applying the framework of scientific prediction as testing of understanding.

**Causal Interpretability & Failure Modes**: The paper examines three ways interpretability can function evaluatively: (1) fixing problems by identifying the root causes of unwanted behavior, (2) detecting subtly faulty mechanisms that invalidate model outputs, and (3) predicting potential issues before they arise.

**Key Framework**: The authors reframe interpretability not merely as an exploratory add-on, but as a scientifically grounded and reliable explanation of behavior that constitutes an evaluation in its own right.

The paper appears to be a recent 2025-2026 publication available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c15792f8-e2b9-44dd-8b54-637a14ab1bb5",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "4f6d2239-5761-4361-aa4a-8b9c99c279ed",
  "toolUseResult": {
    "query": "Lee et al \"Rigorous Interpretation Is a Form of Evaluation\" 2026 falsifiability reproducibility predictivity causal interpretability failure modes",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EtZ9iW5sPiyADmJ5B5FaTL",
        "content": [
          {
            "title": "Rigorous Interpretation Is a Form of Evaluation",
            "url": "https://arxiv.org/html/2605.05508v1"
          },
          {
            "title": "2026 Marks Shift From AI Hype to Rigorous Evaluation - NYC Today",
            "url": "https://nationaltoday.com/us/ny/new-york/news/2026/04/10/2026-is-the-year-of-ai-evaluation-not-ai-hype/"
          },
          {
            "title": "A Roadmap for a Rigorous Science of Interpretability",
            "url": "https://www.researchgate.net/publication/314115920_A_Roadmap_for_a_Rigorous_Science_of_Interpretability"
          },
          {
            "title": "A Survey on Interpretation Methods and Tools for ...",
            "url": "https://arxiv.org/pdf/2506.05451"
          },
          {
            "title": "TOK May 2026 Title 6: “To what extent is interpretation a ...",
            "url": "https://www.revisiondojo.com/blog/tok-may-2026-title-6-to-what-extent-is-interpretation-a-reliable-tool-in-the-production-of-knowledge"
          },
          {
            "title": "Towards A Rigorous Science of Interpretable Machine Learning",
            "url": "https://arxiv.org/pdf/1702.08608"
          }
        ]
      },
      "Based on the search results, I found the paper \"Rigorous Interpretation Is a Form of Evaluation\" on arXiv. Here's what the paper discusses regarding your query terms:\n\n**Falsifiability**: The paper emphasizes that interpretability claims must be falsifiable—that is, they can in principle be counterfactually disprovable—for the claims to be testable and reliably correctable. The authors critique a tendency in parts of the interpretability literature to prioritize intuition-building over the formulation of falsifiable hypotheses.\n\n**Predictivity**: The paper explores how interpretability can function evaluatively by predicting potential issues before they arise by fully understanding the model's behavior, and generates interpretability claims that are predictive by applying the framework of scientific prediction as testing of understanding.\n\n**Causal Interpretability & Failure Modes**: The paper examines three ways interpretability can function evaluatively: (1) fixing problems by identifying the root causes of unwanted behavior, (2) detecting subtly faulty mechanisms that invalidate model outputs, and (3) predicting potential issues before they arise.\n\n**Key Framework**: The authors reframe interpretability not merely as an exploratory add-on, but as a scientifically grounded and reliable explanation of behavior that constitutes an evaluation in its own right.\n\nThe paper appears to be a recent 2025-2026 publication available on arXiv."
    ],
    "durationSeconds": 8.061619715999987,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c15792f8-e2b9-44dd-8b54-637a14ab1bb5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "4f6d2239-5761-4361-aa4a-8b9c99c279ed",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Assistant

_source line 46 · 2026-05-20T05:43:30.675Z_

Now let me do a couple more targeted searches on specific experimental concerns I'm identifying.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f6d2239-5761-4361-aa4a-8b9c99c279ed",
  "isSidechain": false,
  "requestId": "req_011CbDHgVitJ1i2DUm1DgzS3",
  "type": "assistant",
  "uuid": "ddcaac59-4c1b-442b-b0e2-c08d1e32cc7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFTgwDYjBdeoM6oTEw8ZS7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 34750,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 34750,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 776
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T05:43:31.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cv9K3X4tgm1GZXpzZq5twV`</summary>

```json
{
  "query": "Skywork-o1-Open-PRM-Qwen-2.5-1.5B model availability huggingface process reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddcaac59-4c1b-442b-b0e2-c08d1e32cc7f",
  "isSidechain": false,
  "requestId": "req_011CbDHgVitJ1i2DUm1DgzS3",
  "type": "assistant",
  "uuid": "1a14c81e-ff82-451c-936c-c37413d492f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFTgwDYjBdeoM6oTEw8ZS7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 34750,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 34750,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 776
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T05:43:39.394Z_

<details><summary>↩ Tool result · `toolu_01Cv9K3X4tgm1GZXpzZq5twV`</summary>

```text
Web search results for query: "Skywork-o1-Open-PRM-Qwen-2.5-1.5B model availability huggingface process reward model"

Links: [{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B"},{"title":"Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B"},{"title":"README.md · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 59ff2e35345e1a81dd3599a37db7ab2619e24c38","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blob/59ff2e35345e1a81dd3599a37db7ab2619e24c38/README.md"},{"title":"[model] add prm: Skywork-o1-Open-PRM-Qwen2.5-1.5B · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at d9308d8","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/commit/d9308d8260dab7b75db49f5a84b9824a4784f166"},{"title":"modeling_qwen2_rm.py · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 025915e3cab8c4f66837aeb531bfcf0bc19b9f4b","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blob/025915e3cab8c4f66837aeb531bfcf0bc19b9f4b/modeling_qwen2_rm.py"},{"title":"Skywork-o1-Open-PRM-Qwen-2.5-1.5B","url":"https://www.promptlayer.com/models/skywork-o1-open-prm-qwen-25-15b"},{"title":"README.md · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 8aa4397985719f15bb036460782792bfd764232b","url":"https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blame/8aa4397985719f15bb036460782792bfd764232b/README.md"},{"title":"Skywork o1 open model collections","url":"https://huggingface.co/collections/Skywork/skywork-o1-open-67453df58e12f6c3934738d0"},{"title":"jnorthrup/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face","url":"https://huggingface.co/jnorthrup/Skywork-o1-Open-PRM-Qwen-2.5-7B"},{"title":"README.md · Skywork/Skywork-o1-Open-Llama-3.1-8B at main","url":"https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B/blob/main/README.md"}]

Based on the search results, here's information about the Skywork-o1-Open-PRM-Qwen-2.5-1.5B model:

## Model Availability and Overview

The Skywork o1 Open-PRM-Qwen-2.5-1.5B is a specialized model designed to enhance reasoning capability through incremental process rewards, ideal for complex problem solving at a smaller scale. The model is available on Hugging Face at the official Skywork repository.

## Process Reward Model (PRM) Function

This is a Process Reward Model (PRM) developed by Skywork, designed to enhance reasoning capabilities through incremental process rewards as part of the Skywork o1 Open model series, specifically optimized for mathematical and coding tasks evaluation.

Built on the Qwen2.5-Math-1.5B-Instruct architecture, this model implements a novel approach to evaluating reasoning processes step-by-step rather than just final outputs.

## Training and Performance

The Skywork-o1-Open-PRM series are trained on Qwen2.5-Math-1.5B-Instruct and Qwen2.5-Math-7B-Instruct. The selected datasets include GSM8K, MATH, GaoKao, CN-Middle School 24, OlympiadBench, AMC-23, and AIME-24.

Notably, the Skywork o1 Open-PRM-Qwen-2.5-1.5B achieves the performance of 8B models, competing with advanced models like RLHFlow's Llama3.1-8B-PRM-Deepseek-Data and OpenR's Math-psa-7B.

## Licensing and Usage

The community usage of Skywork models require Skywork Community License and the Skywork models support commercial use.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a14c81e-ff82-451c-936c-c37413d492f8",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "26530f53-d4a7-4998-ba7c-aa1b70d949ea",
  "toolUseResult": {
    "query": "Skywork-o1-Open-PRM-Qwen-2.5-1.5B model availability huggingface process reward model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XHBnA5PoDsm3qLr5dT2g5B",
        "content": [
          {
            "title": "Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B · Hugging Face",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B"
          },
          {
            "title": "Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-7B"
          },
          {
            "title": "README.md · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 59ff2e35345e1a81dd3599a37db7ab2619e24c38",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blob/59ff2e35345e1a81dd3599a37db7ab2619e24c38/README.md"
          },
          {
            "title": "[model] add prm: Skywork-o1-Open-PRM-Qwen2.5-1.5B · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at d9308d8",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/commit/d9308d8260dab7b75db49f5a84b9824a4784f166"
          },
          {
            "title": "modeling_qwen2_rm.py · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 025915e3cab8c4f66837aeb531bfcf0bc19b9f4b",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blob/025915e3cab8c4f66837aeb531bfcf0bc19b9f4b/modeling_qwen2_rm.py"
          },
          {
            "title": "Skywork-o1-Open-PRM-Qwen-2.5-1.5B",
            "url": "https://www.promptlayer.com/models/skywork-o1-open-prm-qwen-25-15b"
          },
          {
            "title": "README.md · Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B at 8aa4397985719f15bb036460782792bfd764232b",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B/blame/8aa4397985719f15bb036460782792bfd764232b/README.md"
          },
          {
            "title": "Skywork o1 open model collections",
            "url": "https://huggingface.co/collections/Skywork/skywork-o1-open-67453df58e12f6c3934738d0"
          },
          {
            "title": "jnorthrup/Skywork-o1-Open-PRM-Qwen-2.5-7B · Hugging Face",
            "url": "https://huggingface.co/jnorthrup/Skywork-o1-Open-PRM-Qwen-2.5-7B"
          },
          {
            "title": "README.md · Skywork/Skywork-o1-Open-Llama-3.1-8B at main",
            "url": "https://huggingface.co/Skywork/Skywork-o1-Open-Llama-3.1-8B/blob/main/README.md"
          }
        ]
      },
      "Based on the search results, here's information about the Skywork-o1-Open-PRM-Qwen-2.5-1.5B model:\n\n## Model Availability and Overview\n\nThe Skywork o1 Open-PRM-Qwen-2.5-1.5B is a specialized model designed to enhance reasoning capability through incremental process rewards, ideal for complex problem solving at a smaller scale. The model is available on Hugging Face at the official Skywork repository.\n\n## Process Reward Model (PRM) Function\n\nThis is a Process Reward Model (PRM) developed by Skywork, designed to enhance reasoning capabilities through incremental process rewards as part of the Skywork o1 Open model series, specifically optimized for mathematical and coding tasks evaluation.\n\nBuilt on the Qwen2.5-Math-1.5B-Instruct architecture, this model implements a novel approach to evaluating reasoning processes step-by-step rather than just final outputs.\n\n## Training and Performance\n\nThe Skywork-o1-Open-PRM series are trained on Qwen2.5-Math-1.5B-Instruct and Qwen2.5-Math-7B-Instruct. The selected datasets include GSM8K, MATH, GaoKao, CN-Middle School 24, OlympiadBench, AMC-23, and AIME-24.\n\nNotably, the Skywork o1 Open-PRM-Qwen-2.5-1.5B achieves the performance of 8B models, competing with advanced models like RLHFlow's Llama3.1-8B-PRM-Deepseek-Data and OpenR's Math-psa-7B.\n\n## Licensing and Usage\n\nThe community usage of Skywork models require Skywork Community License and the Skywork models support commercial use."
    ],
    "durationSeconds": 7.765041169000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1a14c81e-ff82-451c-936c-c37413d492f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T05:43:42.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U85ow7WFdydgQNXwq6je1U`</summary>

```json
{
  "query": "SAELens training sparse autoencoders 7B model compute cost GPU hours 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26530f53-d4a7-4998-ba7c-aa1b70d949ea",
  "isSidechain": false,
  "requestId": "req_011CbDHhNqfyzPTWbH2MZpBj",
  "type": "assistant",
  "uuid": "8fc5406a-702f-4f87-8bac-7a2ba544d4c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Rm6bzqa5UGjUQJDXw5Qwf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 35526,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 35526,
          "cache_creation_input_tokens": 1565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1565
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T05:43:49.912Z_

<details><summary>↩ Tool result · `toolu_01U85ow7WFdydgQNXwq6je1U`</summary>

```text
Web search results for query: "SAELens training sparse autoencoders 7B model compute cost GPU hours 2025 2026"

Links: [{"title":"Training Superior Sparse Autoencoders for Instruct Models","url":"https://arxiv.org/html/2506.07691v1"},{"title":"SAELens/tutorials/training_a_sparse_autoencoder.ipynb at main · decoderesearch/SAELens","url":"https://github.com/jbloomAus/SAELens/blob/main/tutorials/training_a_sparse_autoencoder.ipynb"},{"title":"GitHub - hijohnnylin/SAELens: Training Sparse Autoencoders on Language Models","url":"https://github.com/hijohnnylin/SAELens"},{"title":"Training a Sparse Autoencoder in < 30 minutes on 16GB of ...","url":"https://www.lesswrong.com/posts/AtJdPZkMdsakLc6mB/training-a-sparse-autoencoder-in-less-than-30-minutes-on"},{"title":"SAELens/docs/training_saes.md at main · decoderesearch/SAELens","url":"https://github.com/decoderesearch/SAELens/blob/main/docs/training_saes.md"},{"title":"Reverse Engineering LLMs Using the New SAELens Library — ML Hive","url":"https://mlhive.com/2026/04/reverse-engineering-llms-saelens-mechanistic-interpretability"},{"title":"GitHub - decoderesearch/SAELens: Training Sparse Autoencoders on Language Models · GitHub","url":"https://github.com/decoderesearch/SAELens"},{"title":"GitHub - EleutherAI/sparsify: Sparsify transformers with SAEs and transcoders · GitHub","url":"https://github.com/EleutherAI/sparsify"},{"title":"Training SAEs - SAE Lens","url":"https://decoderesearch.github.io/SAELens/latest/training_saes/"},{"title":"Improving Dictionary Learning with Gated Sparse Autoencoders","url":"https://arxiv.org/pdf/2404.16014"}]

Based on the search results, here's what I found regarding SAELens training of sparse autoencoders for 7B models and compute costs:

## General Training Timeline

You can typically train a decent SAE for a real LLM on a single A100 GPU in a matter of hours. For context, typically this process takes in the realm of 3-4 hours and far more GPU power when using standard approaches.

## Hardware Setup

SAEs are trained on 8*NVIDIA A100 GPUs using sae_lens with custom implementation. For the 7B model class specifically, the expansion factor of SAE is fixed at 8X.

## Compute Optimization

Recent research has shown ways to significantly improve training efficiency. A ~10x speed increase to around 550MB/s can be achieved using Switch Sparse Autoencoders, which employ a mixture-of-experts approach.

The search results don't contain specific cost breakdowns in terms of dollar amounts or detailed GPU-hour calculations for 7B models, but they indicate that training is relatively affordable compared to other deep learning tasks, especially when using pre-cached activations or optimized training approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fc5406a-702f-4f87-8bac-7a2ba544d4c3",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "e77a5163-4b24-45ef-8b69-0590a51a563a",
  "toolUseResult": {
    "query": "SAELens training sparse autoencoders 7B model compute cost GPU hours 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S58M1AS4FfpoSzxJ4eHzQA",
        "content": [
          {
            "title": "Training Superior Sparse Autoencoders for Instruct Models",
            "url": "https://arxiv.org/html/2506.07691v1"
          },
          {
            "title": "SAELens/tutorials/training_a_sparse_autoencoder.ipynb at main · decoderesearch/SAELens",
            "url": "https://github.com/jbloomAus/SAELens/blob/main/tutorials/training_a_sparse_autoencoder.ipynb"
          },
          {
            "title": "GitHub - hijohnnylin/SAELens: Training Sparse Autoencoders on Language Models",
            "url": "https://github.com/hijohnnylin/SAELens"
          },
          {
            "title": "Training a Sparse Autoencoder in < 30 minutes on 16GB of ...",
            "url": "https://www.lesswrong.com/posts/AtJdPZkMdsakLc6mB/training-a-sparse-autoencoder-in-less-than-30-minutes-on"
          },
          {
            "title": "SAELens/docs/training_saes.md at main · decoderesearch/SAELens",
            "url": "https://github.com/decoderesearch/SAELens/blob/main/docs/training_saes.md"
          },
          {
            "title": "Reverse Engineering LLMs Using the New SAELens Library — ML Hive",
            "url": "https://mlhive.com/2026/04/reverse-engineering-llms-saelens-mechanistic-interpretability"
          },
          {
            "title": "GitHub - decoderesearch/SAELens: Training Sparse Autoencoders on Language Models · GitHub",
            "url": "https://github.com/decoderesearch/SAELens"
          },
          {
            "title": "GitHub - EleutherAI/sparsify: Sparsify transformers with SAEs and transcoders · GitHub",
            "url": "https://github.com/EleutherAI/sparsify"
          },
          {
            "title": "Training SAEs - SAE Lens",
            "url": "https://decoderesearch.github.io/SAELens/latest/training_saes/"
          },
          {
            "title": "Improving Dictionary Learning with Gated Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2404.16014"
          }
        ]
      },
      "Based on the search results, here's what I found regarding SAELens training of sparse autoencoders for 7B models and compute costs:\n\n## General Training Timeline\n\nYou can typically train a decent SAE for a real LLM on a single A100 GPU in a matter of hours. For context, typically this process takes in the realm of 3-4 hours and far more GPU power when using standard approaches.\n\n## Hardware Setup\n\nSAEs are trained on 8*NVIDIA A100 GPUs using sae_lens with custom implementation. For the 7B model class specifically, the expansion factor of SAE is fixed at 8X.\n\n## Compute Optimization\n\nRecent research has shown ways to significantly improve training efficiency. A ~10x speed increase to around 550MB/s can be achieved using Switch Sparse Autoencoders, which employ a mixture-of-experts approach.\n\nThe search results don't contain specific cost breakdowns in terms of dollar amounts or detailed GPU-hour calculations for 7B models, but they indicate that training is relatively affordable compared to other deep learning tasks, especially when using pre-cached activations or optimized training approaches."
    ],
    "durationSeconds": 7.332350357999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8fc5406a-702f-4f87-8bac-7a2ba544d4c3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T05:43:52.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqE31NRkTqRHVu7isHm8TM`</summary>

```json
{
  "query": "fine-tuning debiased data reward model baseline PRM comparison mechanistic intervention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e77a5163-4b24-45ef-8b69-0590a51a563a",
  "isSidechain": false,
  "requestId": "req_011CbDHi9oNoNnxpRdRh64QH",
  "type": "assistant",
  "uuid": "64deb43a-2f2b-49e3-a2c4-d8701624212e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHh5TasPiN2rCfNUeCjXwo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 37091,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 37091,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 916
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T05:44:01.377Z_

<details><summary>↩ Tool result · `toolu_01XqE31NRkTqRHVu7isHm8TM`</summary>

```text
Web search results for query: "fine-tuning debiased data reward model baseline PRM comparison mechanistic intervention 2025 2026"

Links: [{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/pdf/2603.03291"},{"title":"Language Models Get a Gender Makeover: Mitigating Gender Bias with   Few-Shot Data Interventions","url":"https://arxiv.org/pdf/2306.04597"},{"title":"Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance","url":"https://arxiv.org/pdf/2512.23461"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"The Fine-Tuning Landscape in 2025: A Comprehensive Analysis | by Pradeep Das | Medium","url":"https://medium.com/@pradeepdas/the-fine-tuning-landscape-in-2025-a-comprehensive-analysis-d650d24bed97"},{"title":"Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/pdf/2510.23751"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"}]

I found several relevant research papers on this topic. Here's what the search revealed:

## Key Recent Research (2025-2026)

**Mechanistic Interventions for Reward Model Debiasing:**

A March 2026 paper identifies two previously uncharacterized reward model biases and intervenes directly on RM representations, enabling targeted removal of specific spurious features without retraining, while explicitly distinguishing low-complexity correlational biases from entangled, context-dependent artifacts. The approach uses null-space projection based on the Linear Representation Hypothesis to mitigate length-, uncertainty-, and position-related biases.

**Process Reward Models (PRM) Development:**

Research comparing different PRM training approaches found that when evaluating models trained on the PRM800K dataset with hard labels against those trained on other data, none of the PRMs achieved superior scores compared to majority voting baselines in Best-of-8 evaluation.

**SAE-Based Debiasing Methods:**

Sparse Autoencoders (SAEs) provide a method for decomposing representations into sparse, interpretable features that enable targeted interventions without retraining, with SteerRM being a training-free method for mitigating format bias in reward models using SAE-based interventions.

**Fine-Tuning with Debiased Data:**

Curating fine-tuning datasets that counteract undesired biases can shift model outputs to be more fair, with research suggesting that even updating a small percentage of model weights with carefully chosen data can mitigate biases.

These papers collectively address reward model debiasing through various approaches including representation learning, sparse autoencoders, and data intervention strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64deb43a-2f2b-49e3-a2c4-d8701624212e",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "1398aa2e-7823-4d04-8d50-6cfa18cc79c7",
  "toolUseResult": {
    "query": "fine-tuning debiased data reward model baseline PRM comparison mechanistic intervention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X5Hh62TibxB8QGKuoT5Rv7",
        "content": [
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/pdf/2603.03291"
          },
          {
            "title": "Language Models Get a Gender Makeover: Mitigating Gender Bias with   Few-Shot Data Interventions",
            "url": "https://arxiv.org/pdf/2306.04597"
          },
          {
            "title": "Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance",
            "url": "https://arxiv.org/pdf/2512.23461"
          },
          {
            "title": "The Lessons of Developing Process Reward Models in ...",
            "url": "https://arxiv.org/pdf/2501.07301"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://arxiv.org/html/2503.21295v1"
          },
          {
            "title": "The Fine-Tuning Landscape in 2025: A Comprehensive Analysis | by Pradeep Das | Medium",
            "url": "https://medium.com/@pradeepdas/the-fine-tuning-landscape-in-2025-a-comprehensive-analysis-d650d24bed97"
          },
          {
            "title": "Debiasing Reward Models by Representation Learning with Guarantees",
            "url": "https://arxiv.org/pdf/2510.23751"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here's what the search revealed:\n\n## Key Recent Research (2025-2026)\n\n**Mechanistic Interventions for Reward Model Debiasing:**\n\nA March 2026 paper identifies two previously uncharacterized reward model biases and intervenes directly on RM representations, enabling targeted removal of specific spurious features without retraining, while explicitly distinguishing low-complexity correlational biases from entangled, context-dependent artifacts. The approach uses null-space projection based on the Linear Representation Hypothesis to mitigate length-, uncertainty-, and position-related biases.\n\n**Process Reward Models (PRM) Development:**\n\nResearch comparing different PRM training approaches found that when evaluating models trained on the PRM800K dataset with hard labels against those trained on other data, none of the PRMs achieved superior scores compared to majority voting baselines in Best-of-8 evaluation.\n\n**SAE-Based Debiasing Methods:**\n\nSparse Autoencoders (SAEs) provide a method for decomposing representations into sparse, interpretable features that enable targeted interventions without retraining, with SteerRM being a training-free method for mitigating format bias in reward models using SAE-based interventions.\n\n**Fine-Tuning with Debiased Data:**\n\nCurating fine-tuning datasets that counteract undesired biases can shift model outputs to be more fair, with research suggesting that even updating a small percentage of model weights with carefully chosen data can mitigate biases.\n\nThese papers collectively address reward model debiasing through various approaches including representation learning, sparse autoencoders, and data intervention strategies."
    ],
    "durationSeconds": 8.644801630000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "64deb43a-2f2b-49e3-a2c4-d8701624212e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-20T05:44:01.384Z_

```json
{
  "parentUuid": "1398aa2e-7823-4d04-8d50-6cfa18cc79c7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6983e175-686d-4dac-bd6d-3adfd7d1fdbb",
  "timestamp": "2026-05-20T05:44:01.384Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 54 · 2026-05-20T05:44:04.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015D72m29bJXMBfHx7kLNN9B`</summary>

```json
{
  "query": "\"One Bias After Another\" mechanistic reward shaping linear probes experimental setup baselines 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6983e175-686d-4dac-bd6d-3adfd7d1fdbb",
  "isSidechain": false,
  "requestId": "req_011CbDHizrPYL9TPwc5U2nT5",
  "type": "assistant",
  "uuid": "e8a05437-12b1-4f35-87c5-63029a15bfb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WqNgWBzFfwThMbBn9yahf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 38007,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 38007,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T05:44:14.419Z_

<details><summary>↩ Tool result · `toolu_015D72m29bJXMBfHx7kLNN9B`</summary>

```text
Web search results for query: ""One Bias After Another" mechanistic reward shaping linear probes experimental setup baselines 2026"

Links: [{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/html/2603.03291"},{"title":"One Bias After Another: Mechanistic Reward Shaping and ...","url":"https://arxiv.org/pdf/2603.03291"},{"title":"[2603.03291] One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/abs/2603.03291"},{"title":"Attention Probes | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/attention-probes/"},{"title":"Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs","url":"https://arxiv.org/html/2508.09019v1"}]

I found the research paper! Here's what I found about "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models":

## Overview
The paper studies Reward Models (RMs) that are crucial for online alignment of language models with human preferences, but are vulnerable to reward hacking, and finds that issues persist with respect to length, sycophancy, and overconfidence. The work also discovers new issues related to bias toward model-specific styles and answer-order.

## Methodology
The paper introduces a mechanistic reward shaping approach using linear activation probes to mitigate low-complexity biases. The approach categorizes RM biases by complexity, distinguishing between low-complexity biases amenable to linear probe intervention (length, uncertainty, position) and high-complexity biases resistant to simple debiasing (sycophancy, model-style sensitivity).

## Experimental Setup & Results
The paper provides extensive empirical analysis across four diverse benchmarks (PlausibleQA, BIG-bench, GSM8K-MC, MMLU), demonstrating both the effectiveness of the intervention for tractable biases and the limitations of linear interventions for complex artifacts. The proposed intervention does not significantly degrade accuracy on RewardBench-2, and probes constructed from synthetic datasets generalize out-of-distribution.

The paper was published on arXiv on February 6, 2026 (arxiv paper 2603.03291).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8a05437-12b1-4f35-87c5-63029a15bfb8",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "9b91a7c5-f827-4e48-931b-c9d6c8fcc7d2",
  "toolUseResult": {
    "query": "\"One Bias After Another\" mechanistic reward shaping linear probes experimental setup baselines 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LYuYbrmLjGFdvt1WT32Lw9",
        "content": [
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/html/2603.03291"
          },
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and ...",
            "url": "https://arxiv.org/pdf/2603.03291"
          },
          {
            "title": "[2603.03291] One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/abs/2603.03291"
          },
          {
            "title": "Attention Probes | Learn Mechanistic Interpretability",
            "url": "https://learnmechinterp.com/topics/attention-probes/"
          },
          {
            "title": "Activation Steering for Bias Mitigation: An Interpretable Approach to Safer LLMs",
            "url": "https://arxiv.org/html/2508.09019v1"
          }
        ]
      },
      "I found the research paper! Here's what I found about \"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models\":\n\n## Overview\nThe paper studies Reward Models (RMs) that are crucial for online alignment of language models with human preferences, but are vulnerable to reward hacking, and finds that issues persist with respect to length, sycophancy, and overconfidence. The work also discovers new issues related to bias toward model-specific styles and answer-order.\n\n## Methodology\nThe paper introduces a mechanistic reward shaping approach using linear activation probes to mitigate low-complexity biases. The approach categorizes RM biases by complexity, distinguishing between low-complexity biases amenable to linear probe intervention (length, uncertainty, position) and high-complexity biases resistant to simple debiasing (sycophancy, model-style sensitivity).\n\n## Experimental Setup & Results\nThe paper provides extensive empirical analysis across four diverse benchmarks (PlausibleQA, BIG-bench, GSM8K-MC, MMLU), demonstrating both the effectiveness of the intervention for tractable biases and the limitations of linear interventions for complex artifacts. The proposed intervention does not significantly degrade accuracy on RewardBench-2, and probes constructed from synthetic datasets generalize out-of-distribution.\n\nThe paper was published on arXiv on February 6, 2026 (arxiv paper 2603.03291)."
    ],
    "durationSeconds": 9.923839382999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8a05437-12b1-4f35-87c5-63029a15bfb8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "9b91a7c5-f827-4e48-931b-c9d6c8fcc7d2",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Tool call

_source line 58 · 2026-05-20T05:44:17.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDE5ZiD4TqNV42eWmc3QGj`</summary>

```json
{
  "query": "McGrath self-repair language models ICML 2024 path patching LayerNorm freezing experimental protocol"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b91a7c5-f827-4e48-931b-c9d6c8fcc7d2",
  "isSidechain": false,
  "requestId": "req_011CbDHjxajq764g1BhnreaL",
  "type": "assistant",
  "uuid": "57d9111f-ea82-4f41-ab3b-4a0a857f80f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP7y549hML8XHFpdW1EHSX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 39013,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 39013,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T05:44:26.770Z_

<details><summary>↩ Tool result · `toolu_01UDE5ZiD4TqNV42eWmc3QGj`</summary>

```text
Web search results for query: "McGrath self-repair language models ICML 2024 path patching LayerNorm freezing experimental protocol"

Links: [{"title":"[PDF] The Hydra Effect: Emergent Self-repair in Language Model Computations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Hydra-Effect:-Emergent-Self-repair-in-Language-McGrath-Rahtz/c8fd279848e9c50eec85b852f22f7fffb08f97fc"},{"title":"Published at ICLR 2024 Workshop on Secure and Trustworthy Large Language Models","url":"https://openreview.net/pdf/4a87d0b904b612776d98f77c897386875e7e1fc0.pdf"},{"title":"Explorations of Self-Repair in Language Models","url":"https://arxiv.org/html/2402.15390v1"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf"},{"title":"Explorations of Self-Repair in Language Models","url":"https://arxiv.org/pdf/2402.15390"},{"title":"GitHub - starship006/backup_research: Interpretability Research into the Self-Repair phenomena in Transformer Models; Accepted to ICML 2024; Accepted to SeT LLM @ ICLR 2024 Workshop | Oral · GitHub","url":"https://github.com/starship006/backup_research"},{"title":"TOWARDS BEST PRACTICES OF ACTIVATION PATCH-","url":"https://arxiv.org/pdf/2309.16042"},{"title":"The Hydra Effect: Emergent Self-repair in Language Model Computations","url":"https://arxiv.org/pdf/2307.15771"}]

I found relevant research on self-repair in language models. Here are the key findings from the search results:

## Overview

The research demonstrates two motifs: a form of adaptive computation where ablations of one attention layer of a language model cause another layer to compensate (termed the Hydra effect), and a counterbalancing function of late MLP layers that act to downregulate the maximum-likelihood token.

## Path Patching & Activation Patching

Research examines the role of metrics and methods in activation patching in language models, finding that variations in these techniques could lead to different interpretability results, with recommendations including the use of STR as the corruption method.

## LayerNorm Freezing Role

Up to 30% of the self-repairing of direct effects can be attributed to just the effect of ablations on the LayerNorm normalization factor. LayerNorm normalization factor changes fuel self-repair.

## Experimental Protocol

Research investigates self-repair across the whole pretraining distribution, focuses on individual attention heads (a smaller change, and thus more surprising to see repaired), and investigates the mechanisms behind self-repair on the whole distribution.

Self-repair measurements are made on attention heads when resample ablated on the top 2% of tokens according to direct effect, plotting both individual heads and trend lines averaged across heads in each layer.

The research papers appear to be primarily from ICML 2024, including McGrath et al.'s work on the Hydra effect and related explorations of self-repair mechanisms in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57d9111f-ea82-4f41-ab3b-4a0a857f80f8",
  "isSidechain": false,
  "promptId": "99d3c5e2-0497-49e0-b0a9-9173628678cd",
  "type": "user",
  "uuid": "4800fa97-4ec5-4bc5-8a8a-1e8ed0162706",
  "toolUseResult": {
    "query": "McGrath self-repair language models ICML 2024 path patching LayerNorm freezing experimental protocol",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RLLKrrHWxpQmiPHkzrmymt",
        "content": [
          {
            "title": "[PDF] The Hydra Effect: Emergent Self-repair in Language Model Computations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/The-Hydra-Effect:-Emergent-Self-repair-in-Language-McGrath-Rahtz/c8fd279848e9c50eec85b852f22f7fffb08f97fc"
          },
          {
            "title": "Published at ICLR 2024 Workshop on Secure and Trustworthy Large Language Models",
            "url": "https://openreview.net/pdf/4a87d0b904b612776d98f77c897386875e7e1fc0.pdf"
          },
          {
            "title": "Explorations of Self-Repair in Language Models",
            "url": "https://arxiv.org/html/2402.15390v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/06a52a54c8ee03cd86771136bc91eb1f-Paper-Conference.pdf"
          },
          {
            "title": "Explorations of Self-Repair in Language Models",
            "url": "https://arxiv.org/pdf/2402.15390"
          },
          {
            "title": "GitHub - starship006/backup_research: Interpretability Research into the Self-Repair phenomena in Transformer Models; Accepted to ICML 2024; Accepted to SeT LLM @ ICLR 2024 Workshop | Oral · GitHub",
            "url": "https://github.com/starship006/backup_research"
          },
          {
            "title": "TOWARDS BEST PRACTICES OF ACTIVATION PATCH-",
            "url": "https://arxiv.org/pdf/2309.16042"
          },
          {
            "title": "The Hydra Effect: Emergent Self-repair in Language Model Computations",
            "url": "https://arxiv.org/pdf/2307.15771"
          }
        ]
      },
      "I found relevant research on self-repair in language models. Here are the key findings from the search results:\n\n## Overview\n\nThe research demonstrates two motifs: a form of adaptive computation where ablations of one attention layer of a language model cause another layer to compensate (termed the Hydra effect), and a counterbalancing function of late MLP layers that act to downregulate the maximum-likelihood token.\n\n## Path Patching & Activation Patching\n\nResearch examines the role of metrics and methods in activation patching in language models, finding that variations in these techniques could lead to different interpretability results, with recommendations including the use of STR as the corruption method.\n\n## LayerNorm Freezing Role\n\nUp to 30% of the self-repairing of direct effects can be attributed to just the effect of ablations on the LayerNorm normalization factor. LayerNorm normalization factor changes fuel self-repair.\n\n## Experimental Protocol\n\nResearch investigates self-repair across the whole pretraining distribution, focuses on individual attention heads (a smaller change, and thus more surprising to see repaired), and investigates the mechanisms behind self-repair on the whole distribution.\n\nSelf-repair measurements are made on attention heads when resample ablated on the top 2% of tokens according to direct effect, plotting both individual heads and trend lines averaged across heads in each layer.\n\nThe research papers appear to be primarily from ICML 2024, including McGrath et al.'s work on the Hydra effect and related explorations of self-repair mechanisms in language models."
    ],
    "durationSeconds": 9.284525871999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "57d9111f-ea82-4f41-ab3b-4a0a857f80f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-20T05:47:18.034Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】

- **SteerRM** (arXiv:2603.12795, 2026): 在 RM-Bench Hard split 上用 6 个 RM 评测，baseline 包括原始 RM 和 ablation（去掉 stability criterion / strength criterion），用 pretrained LlamaScope SAE（32× expansion），只在 layer 0-9 有效。核心指标为 RM-Bench accuracy per split (Easy/Normal/Hard)。未对比 fine-tuning baseline。
- **CIRM** (Shinoda et al., arXiv:2604.27495, ACL 2026): 用 Spearman 相关 + Pearl 因果中介分析，在 2 个 general RM 上评测，baseline 包括原始 RM 和 70B RM 参考线。主要评测 RM-Bench 和 RewardBench，关注 <2% 神经元编辑匹配 70B 效果。
- **"One Bias After Another"** (arXiv:2603.03291, 2026): 用 linear probe 做 mechanistic reward shaping，横跨 5 个 RM，评测在 PlausibleQA、BIG-bench、GSM8K-MC、MMLU 四个 benchmark 上，同时在 RewardBench-2 上检查 accuracy 是否退化。区分了 low-complexity bias（可 intervene）和 high-complexity bias（不可 intervene）。
- **CRA** (arXiv:2508.04216, 2025): 在 Math-Shepherd-PRM-7B 和 Qwen2.5-Math-PRM-7B 上从头训 SAE（8× expansion, 8× V100），用 MATH 和 GSM8K 做下游评测（+2.9% / +1.6%），对比了原始 PRM 和 random feature ablation。
- **Arad et al.** (EMNLP 2025): 提出 output-score vs input-score 区分，在 AxBench 上评测，output-score filtering 带来 2-3× 提升。
- **Basu et al.** (arXiv:2603.18353, 2026): 4 种 mechanistic intervention 在 400 个临床 vignette 上测试，baseline 包括 random activation modification（p=0.84 无显著差异）。核心发现是 53pp knowledge-action gap。
- **Xu et al.** (arXiv:2602.00986, 2026): 在 LLM 隐状态中发现 sparse reward subsystem，zeroing top 1% value neurons 导致 -54.9% accuracy 退化。
- **McGrath et al.** (ICML 2024): self-repair 研究中 LayerNorm 贡献约 30%，推荐 path patching + LayerNorm freezing，在 GPT-2 Small/Medium 上验证。

**调研总结**: 该领域当前的实验设计标准要求：(1) 至少 2-3 个 RM/PRM 做跨架构验证；(2) 必须包含 non-mechanistic baseline（如 fine-tuning on debiased data）作为 comparative utility 的参照；(3) 需要同时报告 bias reduction 和 overall accuracy preservation（避免 Basu et al. 式的"修一个坏另一个"问题）；(4) ablation 需要隔离各组件贡献；(5) 审稿人普遍关注 compute-normalized fairness 和 statistical significance。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 在 Phase 4 Comparative Utility 中提到"fine-tuning on debiased data"作为 simple baseline，但未给出具体实现方案。这是 Orgad et al. 评估框架的核心要求之一，也是审稿人最可能提问的对照实验。具体问题：(a) debiased data 从哪来？用 PRM-BiasBench 的 clean split？还是用 Wang et al. pipeline 发现的 bias 做 counterfactual augmentation 后重新 fine-tune？(b) fine-tuning 的 compute budget 是多少？如果 mechanistic intervention 用了 280 H100-hours 但 fine-tuning baseline 只用了 10 hours，比较不公平；反之如果 fine-tuning 用了等量 compute，可能直接超过所有 mechanistic methods，使整篇论文的 practical motivation 受质疑。(c) "prompt-based re-ranking" baseline 同样缺少具体方案——是用 LLM 对 PRM 输出做 re-rank？还是 prompt engineering 让 PRM 忽略格式？这些 baseline 的模糊性会被审稿人视为实验设计不严谨。
- 严重度: 可补救
- 补救方案: 明确定义两个 non-mechanistic baselines：(1) **Fine-tuning baseline**: 在 PRM-BiasBench 的 counterfactual pairs 上对原始 PRM 做 LoRA fine-tuning（rank=16, ~2-4 GPU-hours per PRM），训练目标是在 contrastive pairs 上拉开 correct-step 和 incorrect-step 的 reward gap。这是最公平的对照——同样利用了 bias 知识，但通过参数更新而非 inference-time intervention。(2) **Prompt-based baseline**: 对于 discriminative PRM 不适用 prompt-based re-ranking（因为它们没有 generative decoder），应替换为 **output calibration baseline**（如 Platt scaling 或 temperature scaling on a held-out debiased validation set），这是最低成本的 non-mechanistic debiasing 方法。(3) 加入 **random component ablation** baseline（proposal 已提及但需明确 N=1000+ random seeds 以提供 robust null distribution）。每个 baseline 需报告与 mechanistic methods 等价的所有 benchmark 指标。
- 调研依据: "One Bias After Another" 在 RewardBench-2 上检查 accuracy preservation 作为 baseline 对照；CIRM 用 70B RM 作为 upper-bound reference；Orgad et al. 的 comparative utility criterion 明确要求对比 standard baselines。

【缺陷 2】
- 类别: 评估方案缺陷
- 问题: Proposal 的核心 benchmark 覆盖存在一个关键遗漏：**缺少对整体 PRM 能力的 preservation 评测**。所有三个 core benchmarks（ProcessBench、PRM-BiasBench、RM-Bench Hard）都主要评测 bias reduction 或 adversarial robustness，但没有一个 benchmark 专门评测 intervention 后 PRM 在 standard（非 adversarial）数学推理评测上的 accuracy 是否退化。Basu et al. 的核心教训恰恰是 intervention 在修复 bias 的同时可能破坏正常功能（concept bottleneck steering 修复了 20% 错误但同时引入 53% 新错误）。如果 proposal 的 intervention 在 PRM-BiasBench 上表现出色但在 standard ProcessBench / MATH-500 best-of-N 上 accuracy 下降 5%，审稿人会认为这是致命缺陷。
- 严重度: 可补救
- 补救方案: 加入一个 **preservation benchmark**：在 standard（未经 adversarial 处理的）数学推理数据上评测 PRM 的 best-of-N 精度——具体可用 MATH-500 + GSM8K test set，让 PRM 在原始 policy model 的 N=8 或 N=16 个 candidate solutions 中做 selection，比较 intervention 前后的 pass@1 和 majority-voting-equivalent accuracy。这直接回应 Orgad et al. 的 "specificity" criterion（intervention 是否只影响目标 bias）。在 core evaluation matrix 中加入一列 "Preservation (MATH-500 BoN)" 和 "Preservation (GSM8K BoN)"，与 bias reduction 指标并列报告。每个 intervention granularity 都必须同时报告 bias reduction 和 preservation，构成一个 trade-off Pareto front。
- 调研依据: Basu et al. 的 concept bottleneck steering 20% correction / 53% new errors 教训；"One Bias After Another" 在 RewardBench-2 上做了 accuracy preservation check；CIRM 也报告了 intervention 后 RM-Bench overall accuracy 而非仅 Hard split。

【缺陷 3】
- 类别: 实验设计不足
- 问题: Proposal 的 **Domain Amenability Hypothesis 验证方案过于薄弱**。当前的"验证"仅是：如果 PRM intervention 成功（>3%）就算 positive evidence，如果失败就算 negative evidence，然后与 Basu et al. 的 clinical LM 失败做 post-hoc 对比。这不是一个 controlled test——它是两个完全不同的实验（不同的模型、不同的 task、不同的团队、不同的 intervention 实现）的 narrative juxtaposition。审稿人会指出：PRM 成功可能是因为实验设计更好、compute 更多、或方法选择更恰当，而非因为 domain amenability。Basu et al. 用的是 Steerling-8B 和 Qwen 2.5 7B Instruct 做 clinical triage，而本 proposal 用的是 PRM-specific 7B models 做 math reasoning——差异变量太多，无法归因于 domain conditions。
- 严重度: 可补救
- 补救方案: 不建议改变 hypothesis 本身（那是 framing 层面的事），但实验设计上可以加强 domain amenability 的证据：(1) **Internal ablation of domain conditions**: 在 PRM 上构造一个 "degraded domain condition" 设置——例如将 binary step-level reward 替换为 soft/continuous reward（打破 condition (a)），或在非数学推理 domain（如 code review 或 essay quality）上评测同一套 intervention pipeline（打破 condition (c) verifiable ground truth）。如果 intervention 在 degraded conditions 下效果显著下降，这比 cross-study comparison 有力得多。(2) 如果 (1) 的 compute 成本过高，至少应在 **non-math domain** 做一个 pilot：用同一个 base model（如 Qwen2.5-7B）的 general RM（非 PRM）在 RewardBench 上做同样的 feature-level intervention，看是否效果减弱。这只需 ~10 additional H100-hours。(3) 如果连 (2) 也不可行，则需要在 writing 中明确承认这是 observational comparison 而非 controlled experiment，降低 claim 强度。
- 调研依据: 基于领域实验规范判断——Orgad et al. 的 validation dimension 要求 "empirical support"，而 cross-study narrative comparison 通常被审稿人视为 weak evidence。

【缺陷 4】
- 类别: ablation 不完整
- 问题: Proposal 对 **SAE 方法论选择（from-scratch vs. pretrained）的实验对比不够充分**。Proposal 多次强调 from-scratch SAE training 优于 SteerRM 的 pretrained LlamaScope 方法，并将此作为 key methodological contribution，但实验设计中没有 head-to-head 对比。如果不做直接对比，审稿人会问："你说 from-scratch 更好，证据在哪？" 目前的证据仅是 qualitative argument（distributional mismatch），缺少 quantitative ablation。
- 严重度: 可补救
- 补救方案: 在 Phase 1 中加入一个 **SAE methodology ablation**：对至少一个 Llama-based 或 Qwen-based PRM（如果有 pretrained LlamaScope/GemmaScope SAE 可用），同时运行 (a) from-scratch SAE 和 (b) pretrained base-model SAE（如果架构匹配），在相同 contrastive pairs 上做 feature identification + output-score filtering + downstream intervention，比较：(i) 各层 reconstruction quality (MSE, L0, explained variance)；(ii) 识别出的 fluency-associated features 数量和 overlap；(iii) 最终 intervention 效果差异。注意：如果两个 PRM 都没有对应的 pretrained SAE（Qwen2.5-Math 没有 LlamaScope，Math-Shepherd-Mistral 是 Mistral base），那这个对比确实不可行——此时需在 paper 中明确说明为何无法做 head-to-head comparison（没有可用的 pretrained SAE for these architectures），并将 argument 限定为 "from-scratch SAEs enable full-layer analysis whereas pretrained SAEs are architecture-restricted and layer-limited"。估计额外 compute ~5-10 H100-hours。
- 调研依据: SteerRM 报告了 pretrained LlamaScope SAE 在 layer 10+ 的 MSE 急剧恶化；CRA 在同样的两个 PRM 上从头训练了 SAE 并获得了全层可用的 reconstruction。两者的 experimental gap 恰好是 proposal 可以填补的。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: 三种 core intervention granularities 的 **compute 成本差异巨大但未做 compute-normalized comparison**。Feature-level intervention（SAE training + filtering + steering）需要大量前期 compute（SAE training ~50h + filtering ~5h），而 neuron-level intervention（CIRM-style correlation + median replacement）几乎不需要 SAE training（仅需 Spearman 相关计算），circuit-level intervention 需要更多 compute（circuit tracing ~60h + path patching ~15h）。如果 circuit-level intervention 只比 neuron-level 好 2%，但花了 10 倍 compute，审稿人会质疑 practical value。Proposal 目前没有讨论这个 trade-off。
- 严重度: 可补救
- 补救方案: 在 results reporting 中加入一个 **cost-effectiveness analysis table**，报告每种 intervention 的：(a) 前期 compute cost（SAE/circuit analysis/neuron identification 的 GPU-hours）；(b) 推理时额外 latency（feature steering 需要 SAE encoder forward pass，neuron median replacement 几乎无 overhead，circuit ablation 取决于实现）；(c) Δ performance / GPU-hour 和 Δ performance / inference-latency 的 ratio。这不需要额外实验，只需要在 existing 实验中记录和报告 compute。此外，建议加入一个 **wall-clock time table** 展示各方法从 "拿到 PRM" 到 "可以做 inference-time debiasing" 的端到端时间。
- 调研依据: 基于领域实验规范判断——Zhang et al. (2026) 的 survey 明确指出 SAE features "enable monosemantic intervention but are expensive"，审稿人会期望看到 cost-benefit analysis。

【缺陷 6】
- 类别: 可行性问题
- 问题: **CLT 训练在 1.5B PRM 上的可行性存在不确定性**。CLT-Forge 论文报告了在 1B 模型上训练 ~1.5M features 的经验，但 (a) 是在通用 LLM 上而非 PRM 上；(b) 压缩 activation caching 从 ~20TB 减到 ~4TB 仍需要大量存储；(c) attribution graph 的 "large and redundant" 问题可能使得在 PRM 上的 circuit map 可解释性受限。Proposal 虽然设置了 fallback（"If CLT training exceeds 45 H100-hours or reconstruction loss exceeds 2×..."），但 35 H100-hours 的 budget 可能不足——CLT-Forge 在 1B 模型上的训练需要 8× large GPU + 4TB 存储，这超出了简单的 GPU-hours 估算。
- 严重度: 可补救
- 补救方案: (a) 明确 storage requirement：Skywork-o1-Open-PRM-Qwen-2.5-1.5B 的 activation caching 需要多少存储？按 1.5B model, ~28 layers, 每 token 每层 1536 dims × 4 bytes，在 reasonable training corpus 上可能需要 0.5-2 TB（远小于 CLT-Forge 的 1B general LLM 案例，因为 PRM 的 training data 规模小得多）。(b) 预先在 proposal 中 specify CLT 的 hyperparameter choices（feature count target, sparsity coefficient），而非等到执行时再决定。(c) Fallback plan 已经很好，但建议将 fallback trigger 从 "45 H100-hours" 调整为 "35 H100-hours with a 10h buffer for debugging"——当前 budget 就是 35h 但 trigger 在 45h，逻辑矛盾。(d) 即使 CLT 训练成功，attribution graph 的可解释性问题需要预设 simplification strategy（如 top-K node pruning, community detection on graph structure）。
- 调研依据: CLT-Forge 论文报告 "attribution graphs are often large and redundant, limiting their interpretability"；storage 从 20TB → 4TB 仍然可观。

【缺陷 7】
- 类别: 评估方案缺陷
- 问题: **Statistical significance 和 variance reporting 的方案不明确**。Proposal 定义了 H1 的 success threshold 为 ">3% improvement on at least one benchmark"，但未说明 (a) 这个 3% 是否是统计显著的（需要多少 test examples、什么显著性检验）；(b) 不同 contrastive pair sets / random seeds 下的 variance 如何处理；(c) 多个 benchmark × 多个 intervention × 多个 PRM 构成的多重比较问题（multiple comparison correction）。Lee et al. 的 "reproducibility" criterion 和 "inconsistency" failure mode 直接指向这个问题。如果审稿人要求 bootstrap confidence intervals 或 Bonferroni correction，现有实验设计可能无法支持。
- 严重度: 可补救
- 补救方案: (a) 预定义 statistical protocol：对每个 (intervention, benchmark, PRM) 组合，用 bootstrap resampling (N=1000) 计算 95% confidence interval；(b) 对 core 3×3×3 matrix（3 granularities × 3 benchmarks × 3 PRMs = 27 comparisons），使用 Benjamini-Hochberg FDR correction；(c) 将 H1 的 success criterion 修改为 ">3% improvement with p<0.05 after FDR correction on at least one benchmark"；(d) 对 extension granularities（样本量可能较小），报告 effect size（Cohen's d）而非仅 p-value。这不增加 compute 成本，仅需在 evaluation pipeline 中加入统计检验。
- 调研依据: Lee et al. (2026) 的 reproducibility 和 inconsistency failure mode 直接要求 robust statistical reporting；CIRM 和 SteerRM 的论文中报告了 per-benchmark accuracy 但未做 formal significance test，这是一个可以超越的 methodological standard。

【缺陷 8】
- 类别: 实验设计不足
- 问题: **Neuron-level intervention 的 adaptation from general RM to PRM 缺少具体方案**。CIRM 是在 general RM（非 process-level）上做的，用 Spearman 相关来 identify bias-specific neurons。但 PRM 的结构不同：它对每个 reasoning step 产生 reward（而非对整个 response），neuron 的 bias encoding pattern 可能与 general RM 不同。Proposal 提到 "CIRM-style correlation-based neuron identification with causal mediation, adapted to PRMs" 和 "comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning"，但没有说明 adaptation 的具体细节——correlation 是在 step-level reward 还是 solution-level aggregated reward 上计算？contrastive pairs 是 step-level 还是 solution-level？mediation 的 mediator 定义是什么？
- 严重度: 可补救
- 补救方案: 明确 CIRM→PRM adaptation 的技术细节：(a) Neuron identification 在 **step-level** 上进行——对每个 (step, bias_label) pair 提取 hidden states，计算每个 neuron activation 与 step-level reward 的 Spearman 相关，用 PRM-BiasBench 的 step-level annotations 提供 bias labels；(b) Causal mediation 定义：intervene on neuron activation at the final token of each step（PRM 在此位置产生 step reward），mediator = neuron activation, treatment = fluent-but-wrong vs. disfluent-but-correct step, outcome = step-level reward score；(c) 与 Xu et al. 的 L1-norm probe pruning 对比时，需在相同 contrastive pairs 上运行两种 identification methods，比较 identified neuron overlap 和 downstream intervention 效果。
- 调研依据: CIRM 在 general RM 上用 solution-level reward 做 Spearman 相关；PRM 的 step-level 结构要求不同的 adaptation，这是一个 non-trivial implementation detail。

【缺陷 9】
- 类别: 可行性问题
- 问题: **Wang et al. 的 automated evolutionary bias discovery pipeline 的整合方案不够具体，且可能引入时间风险**。Proposal 提到用 Wang et al. 的 pipeline 来 "augment" contrastive pairs beyond PRM-BiasBench，但 (a) Wang et al. 的 pipeline 是在 general RM（Skywork-V2-8B）上验证的，未在 PRM 上验证过；(b) pipeline 需要 iterative LLM-based proposal + validation，这本身需要 API cost 和时间；(c) 发现的 biases 是否都适合做 mechanistic intervention 的 target 不确定——Wang et al. 发现的 "redundant spacing" 和 "hallucinated content" biases 可能在数学 PRM 上不存在或表现不同。如果 pipeline 在 PRM 上未能发现有意义的 novel biases，这部分工作变成 dead weight。
- 严重度: 可补救
- 补救方案: (a) 将 Wang et al. pipeline 定位为 **optional upstream enhancement** 而非 core dependency——即使 pipeline 未发现 novel biases，PRM-BiasBench 的 8 种 transformation types 已经足够支撑 contrastive pair construction；(b) 在 Phase 1 的 3 周 timeline 中，将 bias discovery 限定在第 1 周完成（~$30-50 API cost），如果 1 周内未发现 statistically significant novel biases，直接使用 PRM-BiasBench + Tiwari et al. 的 known biases 继续实验；(c) 如果发现 novel biases，作为 bonus contribution 报告，而非 core claim 的依赖。
- 调研依据: Wang et al. 的论文在 Skywork-V2-8B (general RM) 上发现了 10 个 biases，但 math PRM 的 bias landscape 可能不同。

Sources:
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)
- [Interpretability without Actionability](https://arxiv.org/abs/2603.18353)
- [SAEs Are Good for Steering – If You Select the Right Features (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)
- [Position: Interpretability Can Be Actionable (ICML 2026)](https://arxiv.org/abs/2605.11161)
- [Rigorous Interpretation Is a Form of Evaluation](https://arxiv.org/abs/2605.05508)
- [One Bias After Another: Mechanistic Reward Shaping](https://arxiv.org/abs/2603.03291)
- [CRA: Causal Reward Adjustment](https://arxiv.org/abs/2508.04216)
- [CLT-Forge: Scalable Cross-Layer Transcoder Library](https://arxiv.org/abs/2603.21014)
- [Automatically Finding Reward Model Biases](https://arxiv.org/abs/2602.15222)
- [Sparse Reward Subsystem in Large Language Models](https://arxiv.org/abs/2602.00986)
- [RelP: Faithful and Efficient Circuit Discovery](https://arxiv.org/abs/2508.21258)
- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://arxiv.org/abs/2412.06559)
- [PRMBench: Fine-grained Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [RM-Bench: Benchmarking Reward Models](https://arxiv.org/abs/2410.16184)
- [Skywork-o1-Open-PRM-Qwen-2.5-1.5B on HuggingFace](https://huggingface.co/Skywork/Skywork-o1-Open-PRM-Qwen-2.5-1.5B)
- [Explorations of Self-Repair in Language Models (ICML 2024)](https://arxiv.org/abs/2402.15390)
- [SAELens: Training Sparse Autoencoders on Language Models](https://github.com/decoderesearch/SAELens)
- [CoLD: Counterfactually-Guided Length Debiasing for PRMs](https://arxiv.org/abs/2507.15698)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4800fa97-4ec5-4bc5-8a8a-1e8ed0162706",
  "isSidechain": false,
  "requestId": "req_011CbDHksNEufQxM3A2Q56VB",
  "type": "assistant",
  "uuid": "088b1075-d48a-4ce3-a721-1a7c53a27f9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L89qChzkvzUJE4abchoRmc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 39700,
      "output_tokens": 7433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7433,
          "cache_read_input_tokens": 39700,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 932
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Description When do mechanistic interventions actually improve model behavior? We propose a…",
  "leafUuid": "088b1075-d48a-4ce3-a721-1a7c53a27f9e",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "3f5fd744-9b44-4834-9e52-865d235777f7"
}
```

---
