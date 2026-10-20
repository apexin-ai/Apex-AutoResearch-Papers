# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # When Do Mechanistic Interventions

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/cefece39-4a22-4b55-849d-406fa8e8331e.jsonl`
- **Structured JSON:** [`f0953f2e2a672f24568b.json`](../../sessions/f0/f0953f2e2a672f24568b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T19:13:22.906Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T19:13:22.906Z",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Related Work / Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Inspiration\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}\n- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}\n- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T19:13:22.909Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T19:13:22.909Z",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-19T19:13:22.920Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models

## Description
When do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.

## Core Problem
The mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).

## Opportunity
The interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.

## Related Work / Landscape
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

## Inspiration
Primary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing

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

## Resource Estimate
- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}
- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}
- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "55702ce9-e773-43c3-bb68-c96e9790cbcb",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T19:13:22.919Z_

```json
{
  "parentUuid": "55702ce9-e773-43c3-bb68-c96e9790cbcb",
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
  "uuid": "5541f0cb-11fa-4790-a400-e4f34cd14bd9",
  "timestamp": "2026-05-19T19:13:22.919Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T19:13:22.919Z_

```json
{
  "parentUuid": "5541f0cb-11fa-4790-a400-e4f34cd14bd9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e63ffa78-f60c-400c-8803-8dd87fa2f4e2",
  "timestamp": "2026-05-19T19:13:22.919Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "e63ffa78-f60c-400c-8803-8dd87fa2f4e2",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Assistant

_source line 8 · 2026-05-19T19:13:33.982Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Let me first note something important: this proposal is about mechanistic interpretability of Process Reward Models (PRMs) - this is an NLP/ML interpretability topic, NOT a robotics topic. CoRL is specifically about robot learning. This is a fundamental mismatch that I need to address.

Wait, let me re-read the instructions. The user says "评估其投稿 CoRL 2026 主会的中稿潜力". So the target venue is CoRL 2026. 

There's a clear tension here: the proposal focuses on mechanistic interpretability of language model reward models, which is fundamentally an NLP/ML interpretability problem, while CoRL 2026 is a robotics-focused venue. The evaluation rubric also references "NLP/CL 领域" which suggests the assessment criteria are designed for NLP/ML work, not robotics. I'll proceed with the evaluation while flagging this significant venue mismatch as a critical issue.

Now I need to search for relevant work in mechanistic interpretability and reward model research to properly contextualize this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e63ffa78-f60c-400c-8803-8dd87fa2f4e2",
  "isSidechain": false,
  "requestId": "req_011CbCTdmFrT9N54TdtgFFji",
  "type": "assistant",
  "uuid": "a66ec21c-ca14-4b92-9e5b-84acbfd7457c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTG6xLScjUaUS3yTNQvn7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 475,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 9722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9722
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

_source line 9 · 2026-05-19T19:13:34.147Z_

我需要先进行领域调研，然后再进行评估。让我搜索相关领域的最新研究。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a66ec21c-ca14-4b92-9e5b-84acbfd7457c",
  "isSidechain": false,
  "requestId": "req_011CbCTdmFrT9N54TdtgFFji",
  "type": "assistant",
  "uuid": "df09e0ba-4f44-41fa-889c-c2f6ca8540b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTG6xLScjUaUS3yTNQvn7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 475,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 9722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9722
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

_source line 10 · 2026-05-19T19:13:34.607Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PvzmWkta4mg3hyErJ1EcqT`</summary>

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
  "parentUuid": "df09e0ba-4f44-41fa-889c-c2f6ca8540b7",
  "isSidechain": false,
  "requestId": "req_011CbCTdmFrT9N54TdtgFFji",
  "type": "assistant",
  "uuid": "c645e61d-dc19-4aff-b82e-9dfec8853afc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WTG6xLScjUaUS3yTNQvn7D",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 475,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9722,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 475,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 9722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9722
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

_source line 11 · 2026-05-19T19:13:34.614Z_

<details><summary>↩ Tool result · `toolu_01PvzmWkta4mg3hyErJ1EcqT`</summary>

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
  "parentUuid": "c645e61d-dc19-4aff-b82e-9dfec8853afc",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "b9c12c2f-9384-4ce9-bc41-59da69fadaa6",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c645e61d-dc19-4aff-b82e-9dfec8853afc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T19:13:49.056Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the required 3-5 web searches to understand the field landscape before making any judgments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9c12c2f-9384-4ce9-bc41-59da69fadaa6",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "29e8bd47-01d6-42aa-a118-8e15459ab666",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 13 · 2026-05-19T19:13:50.048Z_

Now let me conduct the required searches. I'll run multiple searches in parallel to cover the key aspects of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e8bd47-01d6-42aa-a118-8e15459ab666",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "3de0a178-d070-4bbc-bd7b-68bff8c0ad32",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 14 · 2026-05-19T19:13:50.578Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Br5pwEQBDYZ3d4wfnuhVxh`</summary>

```json
{
  "query": "mechanistic interpretability actionability reward models SAE steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3de0a178-d070-4bbc-bd7b-68bff8c0ad32",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "4b2adf43-d3b5-48f9-8311-704daf0c10b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 15 · 2026-05-19T19:13:51.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRFmGbU2YKdAUKTHRaqwbU`</summary>

```json
{
  "query": "Basu et al \"Interpretability without Actionability\" arXiv 2603.18353 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b2adf43-d3b5-48f9-8311-704daf0c10b7",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "f80e07fd-9a5f-4d7f-9f17-da95f18508df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 16 · 2026-05-19T19:13:52.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019YdshwkT19tZKgk5p41AGs`</summary>

```json
{
  "query": "SteerRM debiasing reward models sparse autoencoders arXiv 2603.12795"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f80e07fd-9a5f-4d7f-9f17-da95f18508df",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "f11f1754-8949-4955-b5d0-e996b03aede7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 17 · 2026-05-19T19:13:53.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FTRknrdnaPwUqCEBQcZtKD`</summary>

```json
{
  "query": "CIRM Shinoda causal inference reward model debiasing ACL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f11f1754-8949-4955-b5d0-e996b03aede7",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "295951be-4a2a-4435-acd4-ab7029de80d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 18 · 2026-05-19T19:13:53.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0174Cvhc2zzhDTxoKMFKQ7SP`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "295951be-4a2a-4435-acd4-ab7029de80d1",
  "isSidechain": false,
  "requestId": "req_011CbCTedfUYVZj1nfbrdCt7",
  "type": "assistant",
  "uuid": "1da7ba30-7b18-46c0-9cef-f0195119e7fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L9cBwSq1Wj1xDtsjrVDfqS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 23707,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1001,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1001
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

_source line 19 · 2026-05-19T19:13:57.191Z_

<details><summary>↩ Tool result · `toolu_01RRFmGbU2YKdAUKTHRaqwbU`</summary>

```text
Web search results for query: "Basu et al "Interpretability without Actionability" arXiv 2603.18353 2026"

Links: [{"title":"[2603.18353] Interpretability without actionability","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"}]

I found the paper you're looking for. The paper "Interpretability without actionability" is authored by Sanjay Basu and colleagues from UC San Francisco, Waymark, University of Pennsylvania, Virginia Commonwealth University, and Stanford University, published on arXiv on March 18, 2026.

The paper examines whether mechanistic interpretability methods can bridge the "knowledge-action gap" — where language models encode task-relevant knowledge in internal representations that far exceeds their output performance.

The researchers compared four mechanistic interpretability methods (concept bottleneck steering, sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering) for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes.

Key findings include:
- Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, representing a 53-percentage-point knowledge-action gap
- Concept bottleneck steering corrected 20% of missed hazards but disrupted 53% of correct detections, indistinguishable from random perturbation
- The knowledge-action gap persists across all four intervention paradigms tested, suggesting fundamental limitations, with implications for AI safety frameworks that assume interpretability enables effective error correction


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f80e07fd-9a5f-4d7f-9f17-da95f18508df",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "d4dcd63b-ae75-409e-b3e6-4d859643defb",
  "toolUseResult": {
    "query": "Basu et al \"Interpretability without Actionability\" arXiv 2603.18353 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012gEVmqwVLov59QtoRgxwMR",
        "content": [
          {
            "title": "[2603.18353] Interpretability without actionability",
            "url": "https://arxiv.org/abs/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/html/2603.18353v1"
          },
          {
            "title": "(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.18353"
          }
        ]
      },
      "I found the paper you're looking for. The paper \"Interpretability without actionability\" is authored by Sanjay Basu and colleagues from UC San Francisco, Waymark, University of Pennsylvania, Virginia Commonwealth University, and Stanford University, published on arXiv on March 18, 2026.\n\nThe paper examines whether mechanistic interpretability methods can bridge the \"knowledge-action gap\" — where language models encode task-relevant knowledge in internal representations that far exceeds their output performance.\n\nThe researchers compared four mechanistic interpretability methods (concept bottleneck steering, sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering) for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes.\n\nKey findings include:\n- Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, representing a 53-percentage-point knowledge-action gap\n- Concept bottleneck steering corrected 20% of missed hazards but disrupted 53% of correct detections, indistinguishable from random perturbation\n- The knowledge-action gap persists across all four intervention paradigms tested, suggesting fundamental limitations, with implications for AI safety frameworks that assume interpretability enables effective error correction"
    ],
    "durationSeconds": 5.553156331999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f80e07fd-9a5f-4d7f-9f17-da95f18508df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T19:14:02.016Z_

<details><summary>↩ Tool result · `toolu_019YdshwkT19tZKgk5p41AGs`</summary>

```text
Web search results for query: "SteerRM debiasing reward models sparse autoencoders arXiv 2603.12795"

Links: [{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"},{"title":"[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/abs/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/html/2603.12795"},{"title":"[2508.08746] Interpretable Reward Model via Sparse Autoencoder","url":"https://arxiv.org/abs/2508.08746"},{"title":"SparseRM: A Lightweight Preference Modeling with Sparse Autoencoder","url":"https://arxiv.org/pdf/2511.07896"}]

I found the paper you're looking for! Here's what the search returned:

**SteerRM: Debiasing Reward Models via Sparse Autoencoders** is a paper by Mengyuan Sun, Zhuohao Yu, Weizheng Gu, Shikun Zhang, and Wei Ye from Peking University's National Engineering Research Center for Software Engineering. The paper addresses how reward models exhibit biases toward superficial stylistic cues, preferring better-presented responses over semantically superior ones.

The paper proposes SteerRM, the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. SteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.

Across six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance. The researchers also found that format-related features are concentrated in shallow layers and transfer across models, revealing shared architecture-level bias encoding patterns.

The paper was submitted to arXiv on March 13, 2026 (arXiv:2603.12795).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f11f1754-8949-4955-b5d0-e996b03aede7",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "eb477fba-5690-4bbf-91e1-2b78e2736019",
  "toolUseResult": {
    "query": "SteerRM debiasing reward models sparse autoencoders arXiv 2603.12795",
    "results": [
      {
        "tool_use_id": "srvtoolu_016LRRRiUaebbA9w1ExUpPXw",
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
            "title": "[2508.08746] Interpretable Reward Model via Sparse Autoencoder",
            "url": "https://arxiv.org/abs/2508.08746"
          },
          {
            "title": "SparseRM: A Lightweight Preference Modeling with Sparse Autoencoder",
            "url": "https://arxiv.org/pdf/2511.07896"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search returned:\n\n**SteerRM: Debiasing Reward Models via Sparse Autoencoders** is a paper by Mengyuan Sun, Zhuohao Yu, Weizheng Gu, Shikun Zhang, and Wei Ye from Peking University's National Engineering Research Center for Software Engineering. The paper addresses how reward models exhibit biases toward superficial stylistic cues, preferring better-presented responses over semantically superior ones.\n\nThe paper proposes SteerRM, the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. SteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.\n\nAcross six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance. The researchers also found that format-related features are concentrated in shallow layers and transfer across models, revealing shared architecture-level bias encoding patterns.\n\nThe paper was submitted to arXiv on March 13, 2026 (arXiv:2603.12795)."
    ],
    "durationSeconds": 9.424869239000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f11f1754-8949-4955-b5d0-e996b03aede7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T19:14:02.916Z_

<details><summary>↩ Tool result · `toolu_01FTRknrdnaPwUqCEBQcZtKD`</summary>

```text
Web search results for query: "CIRM Shinoda causal inference reward model debiasing ACL 2026"

Links: [{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"Counterfactual Debiasing for Fact Verification Anonymous ACL submission","url":"https://openreview.net/pdf?id=BddNTCq65yq"},{"title":"How causal inference tools can support debiasing of machine learning models for meaningful brain-based predictions","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314055.full.pdf"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"}]

Based on the search results, I found several papers related to causal inference, reward models, and debiasing, but no results specifically matching the exact query about "CIRM Shinoda" at ACL 2026.

The search returned papers on related topics including:

1. **"Factored Causal Representation Learning for Robust Reward Modeling in RLHF"** - discussing how reward models can assign higher scores to preference-irrelevant patterns and methods to mitigate spurious factors.

2. **"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment"** - which develops a causal reward model (CRM) that is robust to spurious correlations and captures the true causal relationship of responses on human preferences.

3. **"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models"** - addressing length bias in reward models using causal reasoning.

4. **"SteerRM: Debiasing Reward Models via Sparse Autoencoders"** - proposing methods to mitigate reward model biases.

However, the specific paper you're looking for with "CIRM" and author "Shinoda" from ACL 2026 does not appear in these search results. The search may have returned related work in the field of causal inference and reward model debiasing, but not the specific paper. You might want to check the ACL 2026 conference proceedings directly or search with different keywords.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "295951be-4a2a-4435-acd4-ab7029de80d1",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "064f4e63-dfaa-4faa-bac5-b09832f86ba1",
  "toolUseResult": {
    "query": "CIRM Shinoda causal inference reward model debiasing ACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X9YLWgq9ajdzPgpcC1Fqjp",
        "content": [
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/pdf/2507.15698"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "Counterfactual Debiasing for Fact Verification Anonymous ACL submission",
            "url": "https://openreview.net/pdf?id=BddNTCq65yq"
          },
          {
            "title": "How causal inference tools can support debiasing of machine learning models for meaningful brain-based predictions",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.20.24314055.full.pdf"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          }
        ]
      },
      "Based on the search results, I found several papers related to causal inference, reward models, and debiasing, but no results specifically matching the exact query about \"CIRM Shinoda\" at ACL 2026.\n\nThe search returned papers on related topics including:\n\n1. **\"Factored Causal Representation Learning for Robust Reward Modeling in RLHF\"** - discussing how reward models can assign higher scores to preference-irrelevant patterns and methods to mitigate spurious factors.\n\n2. **\"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment\"** - which develops a causal reward model (CRM) that is robust to spurious correlations and captures the true causal relationship of responses on human preferences.\n\n3. **\"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models\"** - addressing length bias in reward models using causal reasoning.\n\n4. **\"SteerRM: Debiasing Reward Models via Sparse Autoencoders\"** - proposing methods to mitigate reward model biases.\n\nHowever, the specific paper you're looking for with \"CIRM\" and author \"Shinoda\" from ACL 2026 does not appear in these search results. The search may have returned related work in the field of causal inference and reward model debiasing, but not the specific paper. You might want to check the ACL 2026 conference proceedings directly or search with different keywords."
    ],
    "durationSeconds": 9.381302758000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "295951be-4a2a-4435-acd4-ab7029de80d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "064f4e63-dfaa-4faa-bac5-b09832f86ba1",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Tool result

_source line 24 · 2026-05-19T19:14:03.821Z_

<details><summary>↩ Tool result · `toolu_0174Cvhc2zzhDTxoKMFKQ7SP`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope robot learning"

Links: [{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"CoRL 2026 - Workshops","url":"https://www.corl.org/program/workshops"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"}]

Based on the search results, here's what I found about CoRL 2026's conference topics and scope:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas, and is dedicated to the intersection of robotics, machine learning, and control.

## Core Topics and Scope

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

More specifically, the conference welcomes papers in areas such as:
- Learning representations for robotic perception and control, learning robot foundation models, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.
- Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and video models and latent world models for robot learning.

## Conference Emphasis

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. The conference has a strong emphasis on real-world robotic experiments and demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1da7ba30-7b18-46c0-9cef-f0195119e7fb",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "8dad0e8b-4761-4c4b-abf6-db32048ec9db",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope robot learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LEC8jroqsTZAV4FGPibG9U",
        "content": [
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "CoRL 2026 - Workshops",
            "url": "https://www.corl.org/program/workshops"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026's conference topics and scope:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 is scheduled for November 10–12, 2026, in Austin, Texas, and is dedicated to the intersection of robotics, machine learning, and control.\n\n## Core Topics and Scope\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\nMore specifically, the conference welcomes papers in areas such as:\n- Learning representations for robotic perception and control, learning robot foundation models, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.\n- Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and video models and latent world models for robot learning.\n\n## Conference Emphasis\n\nAuthors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. The conference has a strong emphasis on real-world robotic experiments and demonstrations."
    ],
    "durationSeconds": 10.005085777,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1da7ba30-7b18-46c0-9cef-f0195119e7fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T19:14:14.083Z_

<details><summary>↩ Tool result · `toolu_01Br5pwEQBDYZ3d4wfnuhVxh`</summary>

```text
Web search results for query: "mechanistic interpretability actionability reward models SAE steering 2026"

Links: [{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=YvsUD8C9QS"},{"title":"Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features","url":"https://arxiv.org/pdf/2602.10437"},{"title":"Interpretability without actionability: mechanistic methods cannot...","url":"https://arxiv.org/abs/2603.18353"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.03659"},{"title":"When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability","url":"https://arxiv.org/pdf/2601.03047"}]

Based on the search results, here's what I found on mechanistic interpretability, actionability, reward models, SAE steering in 2026:

## Key Findings

**The Interpretability-Actionability Gap**

The distinction between representational interpretability and operational actionability should be explicit in regulatory standards. A significant March 2026 paper challenges the assumption that interpretability automatically enables correction: current mechanistic interpretability methods cannot reliably translate internal knowledge into corrected outputs, with implications for AI safety frameworks that assume interpretability enables effective error correction.

In a clinical safety task, linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. SAE feature steering produced zero effect despite 3,695 significant features.

**SAE Steering Applications**

Recent work has applied SAE-based steering to language models. A policy network observes residual stream activations and selects an SAE feature to amplify at each generation step. Training this policy with task-specific rewards produces intervention logs: the converged policy identifies features that, when amplified, change model outputs at each token position.

**Emerging Research Directions**

Training-time interventions that modify model weights—including reinforcement learning from human feedback targeting safety-critical categories, direct preference optimisation on hazard detection, or representation-level fine-tuning guided by probe-identified directions—may succeed where inference-time steering fails.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b2adf43-d3b5-48f9-8311-704daf0c10b7",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "5320efc3-66ed-469a-b81a-da6785f864b6",
  "toolUseResult": {
    "query": "mechanistic interpretability actionability reward models SAE steering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y7qwy19DAqKSWBqi1FBL2K",
        "content": [
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/html/2603.18353v1"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=YvsUD8C9QS"
          },
          {
            "title": "Control Reinforcement Learning: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features",
            "url": "https://arxiv.org/pdf/2602.10437"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot...",
            "url": "https://arxiv.org/abs/2603.18353"
          },
          {
            "title": "(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"
          },
          {
            "title": "Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2510.03659"
          },
          {
            "title": "When the Coffee Feature Activates on Coffins: An Analysis of Feature Extraction and Steering for Mechanistic Interpretability",
            "url": "https://arxiv.org/pdf/2601.03047"
          }
        ]
      },
      "Based on the search results, here's what I found on mechanistic interpretability, actionability, reward models, SAE steering in 2026:\n\n## Key Findings\n\n**The Interpretability-Actionability Gap**\n\nThe distinction between representational interpretability and operational actionability should be explicit in regulatory standards. A significant March 2026 paper challenges the assumption that interpretability automatically enables correction: current mechanistic interpretability methods cannot reliably translate internal knowledge into corrected outputs, with implications for AI safety frameworks that assume interpretability enables effective error correction.\n\nIn a clinical safety task, linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. SAE feature steering produced zero effect despite 3,695 significant features.\n\n**SAE Steering Applications**\n\nRecent work has applied SAE-based steering to language models. A policy network observes residual stream activations and selects an SAE feature to amplify at each generation step. Training this policy with task-specific rewards produces intervention logs: the converged policy identifies features that, when amplified, change model outputs at each token position.\n\n**Emerging Research Directions**\n\nTraining-time interventions that modify model weights—including reinforcement learning from human feedback targeting safety-critical categories, direct preference optimisation on hazard detection, or representation-level fine-tuning guided by probe-identified directions—may succeed where inference-time steering fails."
    ],
    "durationSeconds": 23.500233118999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4b2adf43-d3b5-48f9-8311-704daf0c10b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T19:14:17.125Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for a few more specific things - the CIRM paper, Orgad et al., and the domain amenability angle.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5320efc3-66ed-469a-b81a-da6785f864b6",
  "isSidechain": false,
  "requestId": "req_011CbCThXxWgRkeUqQhXnqp9",
  "type": "assistant",
  "uuid": "c11c7b0e-89a1-4e74-b070-17a06f336fd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDPauFk2aqXMe9yF2vJqoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2553,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24708,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2553,
          "output_tokens": 265,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-19T19:14:17.655Z_

Let me do a few more targeted searches to verify key references and understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c11c7b0e-89a1-4e74-b070-17a06f336fd2",
  "isSidechain": false,
  "requestId": "req_011CbCThXxWgRkeUqQhXnqp9",
  "type": "assistant",
  "uuid": "00894db3-acbb-4399-94fa-d531ae6d38a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDPauFk2aqXMe9yF2vJqoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2553,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24708,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2553,
          "output_tokens": 265,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T19:14:19.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mo688AVRedRyeXf1Rdz4GP`</summary>

```json
{
  "query": "Shinoda \"Debiasing Reward Models via Causally Motivated Inference-Time Intervention\" arXiv 2604.27495"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00894db3-acbb-4399-94fa-d531ae6d38a9",
  "isSidechain": false,
  "requestId": "req_011CbCThXxWgRkeUqQhXnqp9",
  "type": "assistant",
  "uuid": "02ff754a-abb5-48e8-bd1f-e8eaff21f266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDPauFk2aqXMe9yF2vJqoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2553,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24708,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2553,
          "output_tokens": 265,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T19:14:20.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TEBL8gjZPt1aaJoaMFaL5w`</summary>

```json
{
  "query": "Orgad et al \"Interpretability Can Be Actionable\" ICML 2026 arXiv 2605.11161"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ff754a-abb5-48e8-bd1f-e8eaff21f266",
  "isSidechain": false,
  "requestId": "req_011CbCThXxWgRkeUqQhXnqp9",
  "type": "assistant",
  "uuid": "5d3a460a-17cc-4323-915d-25a7b0421542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDPauFk2aqXMe9yF2vJqoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2553,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24708,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2553,
          "output_tokens": 265,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T19:14:20.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DoRd9BfDk6zEAkoPnCtAjJ`</summary>

```json
{
  "query": "process reward model mechanistic interpretability circuit analysis SAE 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d3a460a-17cc-4323-915d-25a7b0421542",
  "isSidechain": false,
  "requestId": "req_011CbCThXxWgRkeUqQhXnqp9",
  "type": "assistant",
  "uuid": "f138e663-00f2-4cf1-9fe9-f52c57d0a610",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDPauFk2aqXMe9yF2vJqoU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2553,
      "cache_creation_input_tokens": 1175,
      "cache_read_input_tokens": 24708,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1175,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2553,
          "output_tokens": 265,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 1175,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1175
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T19:14:27.884Z_

<details><summary>↩ Tool result · `toolu_01Mo688AVRedRyeXf1Rdz4GP`</summary>

```text
Web search results for query: "Shinoda "Debiasing Reward Models via Causally Motivated Inference-Time Intervention" arXiv 2604.27495"

Links: [{"title":"[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/abs/2604.27495"},{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/pdf/2510.23751"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/pdf/2506.19248"},{"title":"Fixing the Broken Compass: Diagnosing and Improving Inference-Time Reward Modeling","url":"https://arxiv.org/pdf/2503.05188"}]

I found the paper you're looking for. Here are the key details:

**Title:** Debiasing Reward Models via Causally Motivated Inference-Time Intervention

**Authors:** Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida from Human Informatics Labs., NTT, Inc.

**Main Contribution:** The paper proposes causally motivated intervention for mitigating multiple types of biases in reward models (RMs) at inference time, first identifying neurons whose activations are strongly correlated with predefined bias attributes, and applying neuron-level intervention that suppresses these signals.

**Key Finding:** The method shows reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs.

The paper is available on arXiv at https://arxiv.org/abs/2604.27495 (published April 30, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02ff754a-abb5-48e8-bd1f-e8eaff21f266",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "77d1f6c2-02db-4fd6-9f6b-cf3b32a5976e",
  "toolUseResult": {
    "query": "Shinoda \"Debiasing Reward Models via Causally Motivated Inference-Time Intervention\" arXiv 2604.27495",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AbuRjSLkwaE82bgErX7VNN",
        "content": [
          {
            "title": "[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2604.27495"
          },
          {
            "title": "Debiasing Reward Models via Causally Motivated Inference-Time Intervention",
            "url": "https://arxiv.org/html/2604.27495"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Debiasing Reward Models by Representation Learning with Guarantees",
            "url": "https://arxiv.org/pdf/2510.23751"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/pdf/2506.19248"
          },
          {
            "title": "Fixing the Broken Compass: Diagnosing and Improving Inference-Time Reward Modeling",
            "url": "https://arxiv.org/pdf/2503.05188"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Title:** Debiasing Reward Models via Causally Motivated Inference-Time Intervention\n\n**Authors:** Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida from Human Informatics Labs., NTT, Inc.\n\n**Main Contribution:** The paper proposes causally motivated intervention for mitigating multiple types of biases in reward models (RMs) at inference time, first identifying neurons whose activations are strongly correlated with predefined bias attributes, and applying neuron-level intervention that suppresses these signals.\n\n**Key Finding:** The method shows reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2604.27495 (published April 30, 2026)."
    ],
    "durationSeconds": 8.628422322999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02ff754a-abb5-48e8-bd1f-e8eaff21f266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T19:14:35.571Z_

<details><summary>↩ Tool result · `toolu_01DoRd9BfDk6zEAkoPnCtAjJ`</summary>

```text
Web search results for query: "process reward model mechanistic interpretability circuit analysis SAE 2025 2026"

Links: [{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/pdf/2509.24713"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/pdf/2304.14997"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Circuit Insights: Towards Interpretability Beyond Activations","url":"https://arxiv.org/pdf/2510.14936"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/pdf/2602.11180"}]

I found several relevant research papers and articles on mechanistic interpretability, circuit analysis, and SAEs. Here's a summary of the key findings:

## Recent Research (2025-2026)

A mechanistic interpretability framework identifies specialized neural circuits responsible for rare-event processing in reward models, with Circuit-Aware Reward Training (CART) using circuit analysis to guide data augmentation, regularization, and ensemble strategies.

The Mechanistic Interpretability Benchmark (MIB) establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models, published in April 2025. Supervised DAS significantly outperforms unsupervised SAE features in causal variable localization tasks.

## SAE Methods and Circuit Analysis

Later studies extend interpretability pipelines to SAE features, which are generally more interpretable and often monosemantic. Additionally, transcoders decompose attributions into input-dependent and input-invariant components, with variants such as skip-transcoders and cross-layer transcoders demonstrating that transcoders match or exceed the interpretability gained through SAEs.

## Broader Trends

MIT Technology Review recognized mechanistic interpretability as a 2026 Breakthrough Technology, while the January 2025 "Open Problems" paper identified that practical SAE methods still underperform simple baselines on safety-relevant tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f138e663-00f2-4cf1-9fe9-f52c57d0a610",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "a1ebf0fe-5fc5-423a-b014-7bb93681ae45",
  "toolUseResult": {
    "query": "process reward model mechanistic interpretability circuit analysis SAE 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017hPyLnMbDyh8xgV7ZuH9Jb",
        "content": [
          {
            "title": "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF",
            "url": "https://arxiv.org/pdf/2509.24713"
          },
          {
            "title": "Towards Automated Circuit Discovery for Mechanistic Interpretability",
            "url": "https://arxiv.org/pdf/2304.14997"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Mechanistic Interpretability Framework",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-framework"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read",
            "url": "https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"
          },
          {
            "title": "Circuit Insights: Towards Interpretability Beyond Activations",
            "url": "https://arxiv.org/pdf/2510.14936"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions",
            "url": "https://arxiv.org/pdf/2602.11180"
          }
        ]
      },
      "I found several relevant research papers and articles on mechanistic interpretability, circuit analysis, and SAEs. Here's a summary of the key findings:\n\n## Recent Research (2025-2026)\n\nA mechanistic interpretability framework identifies specialized neural circuits responsible for rare-event processing in reward models, with Circuit-Aware Reward Training (CART) using circuit analysis to guide data augmentation, regularization, and ensemble strategies.\n\nThe Mechanistic Interpretability Benchmark (MIB) establishes two evaluation tracks—circuit localization and causal variable localization—across diverse tasks and models, published in April 2025. Supervised DAS significantly outperforms unsupervised SAE features in causal variable localization tasks.\n\n## SAE Methods and Circuit Analysis\n\nLater studies extend interpretability pipelines to SAE features, which are generally more interpretable and often monosemantic. Additionally, transcoders decompose attributions into input-dependent and input-invariant components, with variants such as skip-transcoders and cross-layer transcoders demonstrating that transcoders match or exceed the interpretability gained through SAEs.\n\n## Broader Trends\n\nMIT Technology Review recognized mechanistic interpretability as a 2026 Breakthrough Technology, while the January 2025 \"Open Problems\" paper identified that practical SAE methods still underperform simple baselines on safety-relevant tasks."
    ],
    "durationSeconds": 15.08092637100001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f138e663-00f2-4cf1-9fe9-f52c57d0a610",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T19:14:41.136Z_

<details><summary>↩ Tool result · `toolu_01TEBL8gjZPt1aaJoaMFaL5w`</summary>

```text
Web search results for query: "Orgad et al "Interpretability Can Be Actionable" ICML 2026 arXiv 2605.11161"

Links: [{"title":"[2605.11161] Interpretability Can Be Actionable","url":"https://arxiv.org/abs/2605.11161"},{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161"},{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"ICML Poster Position: Interpretability Can Be Actionable","url":"https://icml.cc/virtual/2026/poster/67043"},{"title":"Hadas Orgad @ ICML on X: \"So – why actionable interpretability? Most interpretability work stops at \"here’s what the model is doing.\" But what do we do with that knowledge? Can we change how models are trained, deployed, or aligned based on these insights? That’s the core question we’re tackling.\" / X","url":"https://x.com/OrgadHadas/status/1910426456653783216"},{"title":"Actionable Interpretability Must Be Defined in Terms of Symmetries","url":"https://arxiv.org/pdf/2601.12913"}]

I found the paper! Here's what the search revealed:

The paper "Interpretability Can Be Actionable" was submitted on May 11, 2026, with authors including Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, and Mor Geva.

The paper argues that the central missing ingredient is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.

The authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.

The paper is available at arXiv:2605.11161 and has been accepted as a position paper at ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d3a460a-17cc-4323-915d-25a7b0421542",
  "isSidechain": false,
  "promptId": "d78fa034-b2e5-40db-be70-8e24da9c9783",
  "type": "user",
  "uuid": "8beea3a4-c6bf-439c-925f-4f3481d6cdc9",
  "toolUseResult": {
    "query": "Orgad et al \"Interpretability Can Be Actionable\" ICML 2026 arXiv 2605.11161",
    "results": [
      {
        "tool_use_id": "srvtoolu_013fiqHtzESyMVjXeUWmgSm8",
        "content": [
          {
            "title": "[2605.11161] Interpretability Can Be Actionable",
            "url": "https://arxiv.org/abs/2605.11161"
          },
          {
            "title": "Interpretability Can Be Actionable",
            "url": "https://arxiv.org/html/2605.11161"
          },
          {
            "title": "Interpretability Can Be Actionable Hadas Orgad 1",
            "url": "https://arxiv.org/pdf/2605.11161"
          },
          {
            "title": "ICML Poster Position: Interpretability Can Be Actionable",
            "url": "https://icml.cc/virtual/2026/poster/67043"
          },
          {
            "title": "Hadas Orgad @ ICML on X: \"So – why actionable interpretability? Most interpretability work stops at \"here’s what the model is doing.\" But what do we do with that knowledge? Can we change how models are trained, deployed, or aligned based on these insights? That’s the core question we’re tackling.\" / X",
            "url": "https://x.com/OrgadHadas/status/1910426456653783216"
          },
          {
            "title": "Actionable Interpretability Must Be Defined in Terms of Symmetries",
            "url": "https://arxiv.org/pdf/2601.12913"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nThe paper \"Interpretability Can Be Actionable\" was submitted on May 11, 2026, with authors including Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, and Mor Geva.\n\nThe paper argues that the central missing ingredient is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.\n\nThe authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.\n\nThe paper is available at arXiv:2605.11161 and has been accepted as a position paper at ICML 2026."
    ],
    "durationSeconds": 20.929993612999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5d3a460a-17cc-4323-915d-25a7b0421542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-19T19:14:41.140Z_

```json
{
  "parentUuid": "8beea3a4-c6bf-439c-925f-4f3481d6cdc9",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "82013e61-95df-4b16-9092-21d3150be071",
  "timestamp": "2026-05-19T19:14:41.140Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "82013e61-95df-4b16-9092-21d3150be071",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Assistant

_source line 37 · 2026-05-19T19:15:28.838Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me also check the CoRL scope more carefully, since this is a critical issue.

Key observations:

1. **VENUE MISMATCH**: This is the most critical issue. CoRL (Conference on Robot Learning) is specifically about robotics + machine learning. The proposal is about mechanistic interpretability of Process Reward Models for mathematical reasoning — this has ZERO connection to robotics. The CoRL 2026 call for papers explicitly states topics like "imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight." This proposal would be a desk reject at CoRL.


2. **EVALUATION FRAMEWORK MISMATCH**: The system prompt asks me to evaluate this for CoRL 2026, but the rubric itself references "NLP/CL 领域的影响力" (impact in NLP/computational linguistics), which suggests there's a fundamental disconnect between the venue being evaluated and the evaluation criteria being applied. This appears to be a case where the wrong rubric was paired with the wrong venue.

3. **CRITICAL ISSUE TO FLAG**: If the user actually submits this NLP/interpretability work to CoRL (a robotics conference), it would face desk rejection regardless of quality. I need to prominently highlight this venue mismatch while still evaluating the work on its actual merits using the NLP-focused rubric provided.

Now looking at the substantive contribution: the core idea is framing when mechanistic interventions succeed as a "Domain Amenability Hypothesis"—essentially that interventions work better on tasks with well-defined outputs and verifiable ground truth. This observation feels fairly intuitive. The more concrete contribution is systematically comparing intervention granularities across a single framework, which is more of a benchmarking study than a novel conceptual advance.

The novelty concern deepens when I consider what's already been done—SteerRM, CIRM, and CRA have all tackled similar problems with SAE-based steering, neuron-level causal interventions, and SAE training on PRM activations respectively. This proposal essentially combines existing methods and adds a framing about why PRMs are good testbeds. The Domain Amenability Hypothesis itself is somewhat tautological: of course mechanistic interventions work better when you can actually measure whether they're working and the problem space is constrained. A simpler alternative might be that fine-tuning on debiased data or prompt engineering could achieve comparable or better results for PRM debiasing without the mechanistic overhead.

Looking at the core assumptions, the four conditions proposed (well-defined semantics, constrained structure, verifiable ground truth, testable specificity) are asserted rather than theoretically derived. With only two data points—PRMs succeeding and clinical LMs failing—I can't actually isolate which conditions matter, since these domains differ across every dimension: task, model, architecture, training data, everything. Any of those differences could explain the divergence. The significance question remains real though: understanding when mechanistic interventions succeed is genuinely important for the field, but the proposed answer doesn't quite deliver the rigor needed to answer it convincingly.

The related work is impressively thorough, showing deep familiarity with the literature, though that comprehensiveness doesn't address the fundamental weakness that the core contribution boils down to a systematic comparison plus a loosely-formulated hypothesis. There's also a critical venue issue here—this is fundamentally about NLP and ML interpretability with zero robotics content, which would likely result in a desk rejection at CoRL. The appropriate venues would be ICML, NeurIPS, ICLR, ACL, or EMNLP instead. Given that I'm evaluating specifically for CoRL 2026, the venue mismatch alone probably means the acceptance probability should be essentially 0-5% regardless of the idea's quality.

That said, let me also assess the idea on its own merits for an appropriate NLP/ML venue, since that's useful context. The Domain Amenability Hypothesis feels somewhat intuitive but under-specified, and the multi-granularity comparison, while systematic, isn't methodologically novel—most of the individual pieces already exist. The question itself is important, but the evidence provided is thin with only two domains compared. For a proper venue, I'd estimate this sits around 20-30% acceptance probability.

For CoRL specifically, it's essentially a non-starter at 0-5%—the venue mismatch is just too fundamental.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82013e61-95df-4b16-9092-21d3150be071",
  "isSidechain": false,
  "requestId": "req_011CbCTjXbF5G3DVCvwBjqcy",
  "type": "assistant",
  "uuid": "d5829ae8-d44f-4bca-b18c-5da5f71b570f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JE9K6d6MXRWw5SZUgPvdw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 720,
      "cache_creation_input_tokens": 5228,
      "cache_read_input_tokens": 24708,
      "output_tokens": 5927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 720,
          "output_tokens": 5927,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 5228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5228
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-19T19:17:06.572Z_

Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

==========================================================================
⚠️ 关键前置问题：严重的投稿目标会议错位
==========================================================================

在进入 idea 质量评估之前，必须指出一个致命问题：
本 proposal 关于 NLP/ML 领域的 Process Reward Model 机制可解释性，
而 CoRL (Conference on Robot Learning) 的核心主题是机器人学习：
仿真到真实迁移、机器人操纵/运动/导航/驾驶、机器人感知、
机器人强化学习等。CoRL 2026 (Austin, TX, Nov 10-12) 的 Call for Papers
明确要求 "real-robot experiments or convincing evidence that simulation
experiments are transferable to real robots"。

本 proposal 与机器人学习领域零交集——无机器人实验、无机器人任务、
无 embodied 组件。如果直接投稿 CoRL 2026 主会，大概率被 desk reject。

适合的目标会议：ICML / NeurIPS / ICLR (ML track) 或 ACL / EMNLP (NLP track)。

以下评估假设投稿目标为一个合适的 ML/NLP 顶会（如 NeurIPS 2026），
以便下游 agent 能在正确语境下优化 proposal。

==========================================================================

【领域调研】:

- [Basu et al., arXiv:2603.18353] (March 2026): "Interpretability without 
  Actionability" — 在临床分诊 LM 上测试四种机制可解释性干预方法
  （含 SAE steering、activation patching），发现均无法有效纠正输出错误。
  线性探针达 98.2% AUROC 但模型输出灵敏度仅 45.1%，存在 53pp 的
  knowledge-action gap。已验证存在，是本 proposal 的核心对比点。

- [SteerRM, arXiv:2603.12795] (March 2026): 北大团队提出首个
  training-free SAE-based RM 去偏方法。使用预训练 LlamaScope SAE，
  在 RM-Bench Hard split 上平均提升 7.3 points。发现 format-related
  features 集中在浅层且跨模型迁移。已经实现了 feature-level 干预。

- [CIRM / Shinoda et al., arXiv:2604.27495] (April 2026, ACL 2026): 
  NTT 团队提出 neuron-level 因果中介分析去偏，编辑 <2% neurons 
  即可匹配 70B RM 性能。已经实现了 neuron-level 干预。

- [Orgad et al., arXiv:2605.11161] (ICML 2026 Position Paper): 
  提出可解释性应以 actionability 为评估标准，定义 concreteness 
  和 validation 两个维度。本 proposal 采用其评估框架但并非核心创新。

- [Lee et al., arXiv:2605.05508] (May 2026): 
  提出可解释性作为严格评估的三个科学标准（可证伪性、可复现性、
  预测性），提供互补诊断框架。

- [Zhang et al., arXiv:2601.14004] (Jan 2026): "Locate, Steer, Improve" 
  综述，提供 actionable MI 的最全面分类法。本 proposal 实例化其 pipeline。

- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从头训练 SAE 用于
  后门纠正，本 proposal 的 SAE 方法论直接沿用此工作。

- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 区分 output features
  和 input features 可带来 2-3× 改进。本 proposal 采用其过滤方法。

- 调研总结: 这个领域在 2026 年初极为活跃。PRM 去偏已有 feature-level
  (SteerRM)、neuron-level (CIRM)、probe-level (One Bias After Another) 
  等多种粒度的独立工作。"可解释性是否 actionable"的辩论也有了正反两方
  的 position papers。本 proposal 试图在已有拼图上做"统一比较框架+
  domain amenability 假说"，但核心方法论组件均来自已有工作。


【Trivial Alternative 检验】:

存在明显的 trivial alternative 威胁，分两个层面：

(1) 对于 "Domain Amenability Hypothesis"：这个假说本质上在说"当任务
    有明确输出语义、受限输出结构、可验证 ground truth、可独立测试
    specificity 时，机制干预更容易成功"。这近乎同义反复——"当你能
    清晰定义成功、精确测量效果、独立检验副作用时，干预更可能被判定
    为成功"。一个更 trivial 的表述是："机制干预在更简单、更可度量的
    任务上效果更好"。审稿人很可能认为这不是一个需要实验验证的
    hypothesis，而是一个 obvious observation。

(2) 对于 PRM 去偏本身：fine-tuning on debiased data（proposal 自己
    列为 baseline）可能以更低成本达到类似或更好效果。Factored CRL
    (ICML 2026) 已经在训练时解决了这个问题。本 proposal 的增量价值
    在于"理解 why/when 干预 work"，但如果假说本身是 trivial 的，
    这个增量价值就大打折扣。


【前提假设检验】:

核心 claim 的逻辑链有以下未经验证的环节：

(1) N=2 归纳问题：整个 Domain Amenability Hypothesis 的"验证"建立在
    两个数据点上——PRM（满足四条件，干预成功）vs. 临床 LM（不满足
    四条件，干预失败）。但这两个域之间的差异远不止这四个条件（模型
    架构、训练数据、任务类型、模型规模、领域知识等全部不同）。无法
    排除混淆因素，无法证明是这四个条件而非其他因素导致了成功/失败
    的差异。这不是"验证假说"，而是"post-hoc rationalization"。

(2) 四个条件的选择缺乏理论基础：为什么是这四个条件而非其他？为什么
    不是"输出维度低"、"任务复杂度低"、"偏差是线性可分的"等？
    这四个条件看起来是从 PRM 的特征反推出来的（PRM 有什么特点 →
    这些特点就是成功的条件），存在严重的 overfitting to the 
    observation 风险。

(3) "43% of reward gains from stylistic exploitation" 这个数字来自
    Tiwari et al.，但这是在特定 PRM 和特定攻击设置下的结果，
    能否推广到本 proposal 使用的 Qwen2.5-Math-PRM 和 
    Math-Shepherd-Mistral-7B-PRM 是未经验证的。

(4) 对 Basu et al. 失败的归因：Basu et al. 的失败可能有多种原因
    （SAE 质量差、steering 方向选择不当、临床任务本身更难等），
    proposal 将其归因于"domain 不满足四条件"是一个未经验证的
    归因。Basu et al. 自己的分析也指向了更具体的技术原因。


【3 维度打分】:

1. Novelty: 弱 — 
   核心贡献有两个层面：(a) Domain Amenability Hypothesis 和 
   (b) multi-granularity comparison。
   
   对于 (a)：这个假说本身接近同义反复（见 Trivial Alternative 检验），
   且仅基于 N=2 的 post-hoc 对比，缺乏理论推导。这不构成 strong 
   novelty。
   
   对于 (b)：这是一个 systematic empirical comparison，但比较的
   对象——feature-level (SteerRM, 2603.12795)、neuron-level 
   (CIRM, 2604.27495)、circuit-level (activation patching) ——
   均为已有方法的直接应用或微调。唯一的方法论增量是将 Arad et al.
   的 output-score filtering 与 CRA 的 from-scratch SAE 结合，
   但这是 straightforward engineering integration。
   
   与最相关工作的 delta：SteerRM 已做 feature-level；CIRM 已做
   neuron-level；CRA 已做 PRM-specific SAE training。本 proposal
   的核心 novelty 是"把它们放在一起比较"+ 一个薄弱的 framing 假说。
   这更接近 survey + benchmark 而非 research contribution。

2. Significance: 中 — 
   "when do mechanistic interventions succeed" 是 MI 社区当前的
   核心问题之一，Basu et al. 和 Orgad et al. 分别从负面和正面
   推动了这个讨论。这个问题的重要性毋庸置疑。
   
   但本 proposal 对这个问题的回答质量堪忧：N=2 的 domain 对比
   不可能给出有说服力的答案。即使 PRM 干预成功，审稿人仍然无法
   判断是因为 Domain Amenability Hypothesis 的四个条件还是其他
   原因。结论的可推广性极低。
   
   PRM 去偏的实际应用价值存在，但 discriminative PRM 正在被
   generative PRM (ThinkPRM, GenPRM) 替代，这削弱了 practical 
   significance。
   
   对领域的影响：如果结果 positive，贡献的是"又一个 MI 干预成功
   的 case study"，但 SteerRM 和 CIRM 已经提供了类似证据。
   如果结果 negative，那更有意思（但 proposal 的设计倾向于 
   positive result）。

3. Related Work: 强 — 
   Related work 覆盖极为全面，涵盖了 actionability debate 双方
   (Basu et al., Orgad et al.)、所有主要 intervention 粒度
   (SteerRM, CIRM, CRA, One Bias After Another)、评估框架
   (Lee et al.)、分类法 (Zhang et al.)、电路分析工具 
   (RelP, CLT-Forge)、self-repair (McGrath et al.) 等。
   差异化定位也算清晰——"统一比较框架"的定位在文献中确实空白。
   引用的论文经核实均真实存在且描述准确。


【概率估计】: [15% - 25%] 中位 20%

【估计理由】: 
投稿 CoRL 的话概率接近 0%（完全 off-topic，会被 desk reject）。

即使投稿合适的 ML/NLP 顶会（NeurIPS/ICML/ACL），idea 质量也
处于 15-25% 区间：

- Novelty 是核心瓶颈。Domain Amenability Hypothesis 近乎同义反复
  且 N=2 归纳不具说服力；multi-granularity comparison 是 
  straightforward 的已有方法组合。审稿人大概率会评价为 "well-executed
  but incremental"。

- Significance 被两个因素削弱：(a) discriminative PRM 正被 generative 
  PRM 替代，降低了实际应用价值；(b) 对核心问题 "when do MI interventions 
  succeed" 的回答因 N=2 设计而不具说服力。

- Related work 的强项不足以弥补 novelty 的弱项——在顶会审稿中，
  idea 新颖性通常是决定性因素。

- 形式完善度很高（详细的实验 plan、完整的 resource estimate、
  双 outcome 设计），但这是执行层面的优势，不改变 idea 内核。

上界 25% 受限于 Novelty 维度——即使实验完美执行，核心 claim 
的 intellectual contribution 仍然薄弱。

【主要风险】: 
1. Domain Amenability Hypothesis 被审稿人判定为 tautological/obvious，
   且 N=2 对比被认为不构成 hypothesis testing（这是最可能的拒稿理由）
2. "统一比较已有方法"的定位被归类为 benchmark/survey paper 而非
   research paper，不符合顶会主会对 novelty 的要求
```

**补充说明给下游 agent：**

如果要进入迭代优化，我建议重点关注两个方向：
1. **必须解决 venue 问题**——如果坚持投 CoRL，需要彻底重新设计 proposal 使其与机器人学习相关（例如：将机制可解释性应用于 robot reward models / robot policy learning），否则投稿无意义。
2. **如果转投 NLP/ML 顶会**，核心问题是 Domain Amenability Hypothesis 太弱——需要要么 (a) 增加更多对比域使假说检验更有说服力，要么 (b) 放弃假说包装、转而强化 multi-granularity comparison 的方法论贡献和实用价值。

Sources:
- [Interpretability without Actionability (Basu et al.)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM: Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/abs/2604.27495)
- [Position: Interpretability Can Be Actionable (Orgad et al.)](https://arxiv.org/abs/2605.11161)
- [Rigorous Interpretation Is a Form of Evaluation (Lee et al.)](https://arxiv.org/abs/2605.05508)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 About](https://www.corl.org/about-corl)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5829ae8-d44f-4bca-b18c-5da5f71b570f",
  "isSidechain": false,
  "requestId": "req_011CbCTjXbF5G3DVCvwBjqcy",
  "type": "assistant",
  "uuid": "9851dbee-4671-46bc-97da-bc4a6c321b93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019JE9K6d6MXRWw5SZUgPvdw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 720,
      "cache_creation_input_tokens": 5228,
      "cache_read_input_tokens": 24708,
      "output_tokens": 5927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 720,
          "output_tokens": 5927,
          "cache_read_input_tokens": 24708,
          "cache_creation_input_tokens": 5228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5228
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "9851dbee-4671-46bc-97da-bc4a6c321b93",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "cefece39-4a22-4b55-849d-406fa8e8331e"
}
```

---
