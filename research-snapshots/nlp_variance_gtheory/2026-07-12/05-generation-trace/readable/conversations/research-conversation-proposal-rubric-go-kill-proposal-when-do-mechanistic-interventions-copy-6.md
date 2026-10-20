# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # When Do Mechanistic Interventions

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/d7a8159a-c9dc-4356-acf4-68101de0b562.jsonl`
- **Structured JSON:** [`4d858d84948d247ca9b4.json`](../../sessions/4d/4d858d84948d247ca9b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:27:32.896Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:27:32.896Z",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Related Work / Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Inspiration\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}\n- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}\n- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:27:32.898Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:27:32.898Z",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-19T21:27:32.909Z_

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
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "07cb3c45-9699-498c-8a67-e14297bd5a0e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:27:32.907Z_

```json
{
  "parentUuid": "07cb3c45-9699-498c-8a67-e14297bd5a0e",
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
  "uuid": "ebe52387-7abc-4a9b-b6af-ab4438ebcae0",
  "timestamp": "2026-05-19T21:27:32.907Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:27:32.908Z_

```json
{
  "parentUuid": "ebe52387-7abc-4a9b-b6af-ab4438ebcae0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "614ad48f-6bcc-419e-94f3-eb03f1782f9a",
  "timestamp": "2026-05-19T21:27:32.908Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
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
  "leafUuid": "614ad48f-6bcc-419e-94f3-eb03f1782f9a",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM mechanistic intervention proposal",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:27:56.164Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Let me first carefully read the proposal, then conduct web searches to understand the field landscape before making my assessment.

Wait - this is for CoRL 2026 (Conference on Robot Learning)? But the proposal is about mechanistic interpretability of Process Reward Models (PRMs) in mathematical reasoning. This seems like it would be more appropriate for a venue like NeurIPS, ICML, ICLR, ACL, or EMNLP rather than CoRL. Let me re-read the user's instructions...


The user is asking me to evaluate the proposal's acceptance potential at CoRL 2026 main conference, but there's a fundamental mismatch here - CoRL focuses on robot learning and robotics, while this proposal is entirely about mechanistic interpretability of process reward models for mathematical reasoning, which has no connection to robotics whatsoever.

Looking at the system prompt more carefully, I notice it mentions NLP/CL (Natural Language Processing/Computational Linguistics) under the Significance section, which contradicts the CoRL venue specification. It seems like either the system prompt template was designed for NLP/CL venues and the user mistakenly specified CoRL, or there's been some confusion about the target conference. Either way, this venue mismatch is a critical issue I need to address. I'm noticing the venue mismatch—this looks like an NLP/mechanistic interpretability proposal for CoRL, which is a robotics conference—but I'll proceed with evaluating the idea quality and flag the discrepancy. Before assessing, I need to search for context on the actionability debate in mechanistic interpretability, recent work on process reward model debiasing methods like SteerRM and CIRM, and when SAE-based interventions actually succeed in practice.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "614ad48f-6bcc-419e-94f3-eb03f1782f9a",
  "isSidechain": false,
  "requestId": "req_011CbCdsANgV5F6povsnEJS6",
  "type": "assistant",
  "uuid": "cbf4f3ff-cb66-458d-b839-c79720f521aa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qNv87UAzDYth2DG6rsPks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 1001,
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
          "output_tokens": 1001,
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

_source line 9 · 2026-05-19T21:27:56.168Z_

我需要先进行领域调研，然后再进行评估。让我先搜索相关领域的最新进展。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbf4f3ff-cb66-458d-b839-c79720f521aa",
  "isSidechain": false,
  "requestId": "req_011CbCdsANgV5F6povsnEJS6",
  "type": "assistant",
  "uuid": "3ce5c759-64a1-4dc3-a80d-fb0ef950e793",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qNv87UAzDYth2DG6rsPks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 1001,
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
          "output_tokens": 1001,
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

_source line 10 · 2026-05-19T21:27:56.240Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RcR9UMovViMU7fzGkZY1Sk`</summary>

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
  "parentUuid": "3ce5c759-64a1-4dc3-a80d-fb0ef950e793",
  "isSidechain": false,
  "requestId": "req_011CbCdsANgV5F6povsnEJS6",
  "type": "assistant",
  "uuid": "f63623bc-c40a-424a-a877-3d3edd93f3d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qNv87UAzDYth2DG6rsPks",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 1001,
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
          "output_tokens": 1001,
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

_source line 11 · 2026-05-19T21:27:56.246Z_

<details><summary>↩ Tool result · `toolu_01RcR9UMovViMU7fzGkZY1Sk`</summary>

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
  "parentUuid": "f63623bc-c40a-424a-a877-3d3edd93f3d5",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "275ef03f-2413-4d0f-8ee4-7b3c17cca2f6",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "f63623bc-c40a-424a-a877-3d3edd93f3d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:27:59.748Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required web searches to understand the field landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "275ef03f-2413-4d0f-8ee4-7b3c17cca2f6",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "1473655e-cc1a-4d9e-a972-1614867c40e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 13 · 2026-05-19T21:28:00.334Z_

现在让我进行系统性的领域调研。我会并行发起多个搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1473655e-cc1a-4d9e-a972-1614867c40e3",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "35a6355d-20ad-4dc5-b4db-3975c486e2f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 14 · 2026-05-19T21:28:00.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VYdksPeaZhNkjrTWvSmbUz`</summary>

```json
{
  "query": "Basu et al. \"Interpretability without Actionability\" mechanistic interventions clinical LM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a6355d-20ad-4dc5-b4db-3975c486e2f6",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "2c86c71c-6718-48b7-8ca1-3c05209753d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 15 · 2026-05-19T21:28:01.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013KkjwSQHbHkdKt3ZrA727R`</summary>

```json
{
  "query": "SteerRM SAE debiasing reward models 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c86c71c-6718-48b7-8ca1-3c05209753d2",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "54d9e685-86ee-4ad6-8c30-0ed6cdecb520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 16 · 2026-05-19T21:28:02.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gv8YV2t48Rw8bjkpD85QNE`</summary>

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
  "parentUuid": "54d9e685-86ee-4ad6-8c30-0ed6cdecb520",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "dc408b57-5fed-46c9-99fb-739ba60c1acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 17 · 2026-05-19T21:28:02.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AHq9deXDLtzwa7pTxqTnNz`</summary>

```json
{
  "query": "Orgad et al. \"Interpretability Can Be Actionable\" ICML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc408b57-5fed-46c9-99fb-739ba60c1acc",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "fc2978a5-a9a2-494f-89f9-021159a8bc22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 18 · 2026-05-19T21:28:02.910Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MZG3KhzKoHtBQMWXdDFHiq`</summary>

```json
{
  "query": "process reward model bias fluency exploitation mechanistic interpretability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2978a5-a9a2-494f-89f9-021159a8bc22",
  "isSidechain": false,
  "requestId": "req_011CbCdtt9B8RfUYk7bkdeh7",
  "type": "assistant",
  "uuid": "bd119c29-1d71-4b33-a54d-3f014f377c7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHyy38vZcLojvBx77xLYYc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1528,
      "cache_read_input_tokens": 23707,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 345,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1528
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

_source line 19 · 2026-05-19T21:28:07.577Z_

<details><summary>↩ Tool result · `toolu_013KkjwSQHbHkdKt3ZrA727R`</summary>

```text
Web search results for query: "SteerRM SAE debiasing reward models 2026 arXiv"

Links: [{"title":"[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/abs/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/html/2603.12795"},{"title":"[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/abs/2604.27495"},{"title":"[2510.23751] Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/abs/2510.23751"}]

Based on the search results, I found the paper you're looking for:

**SteerRM** is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. 

SteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.

**Key Results:**
Across six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance. Results on a Gemma-based reward model and a controlled non-format bias further suggest generalization across RM architectures and bias types.

**Practical Impact:**
SAE-based interventions can mitigate reward-model biases without retraining, providing a practical and interpretable solution for alignment pipelines.

The paper was published on arXiv on March 13, 2026 (arXiv ID: 2603.12795) by researchers from Peking University's National Engineering Research Center for Software Engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54d9e685-86ee-4ad6-8c30-0ed6cdecb520",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "e8776d6d-c5c2-4ca0-9ffe-990bae38ca4a",
  "toolUseResult": {
    "query": "SteerRM SAE debiasing reward models 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Es4sxTiUYeNv3qwQysAs6v",
        "content": [
          {
            "title": "[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2603.12795"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2603.12795"
          },
          {
            "title": "[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2604.27495"
          },
          {
            "title": "[2510.23751] Debiasing Reward Models by Representation Learning with Guarantees",
            "url": "https://arxiv.org/abs/2510.23751"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**SteerRM** is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. \n\nSteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time.\n\n**Key Results:**\nAcross six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance. Results on a Gemma-based reward model and a controlled non-format bias further suggest generalization across RM architectures and bias types.\n\n**Practical Impact:**\nSAE-based interventions can mitigate reward-model biases without retraining, providing a practical and interpretable solution for alignment pipelines.\n\nThe paper was published on arXiv on March 13, 2026 (arXiv ID: 2603.12795) by researchers from Peking University's National Engineering Research Center for Software Engineering."
    ],
    "durationSeconds": 6.2294304430000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54d9e685-86ee-4ad6-8c30-0ed6cdecb520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T21:28:08.516Z_

<details><summary>↩ Tool result · `toolu_01Gv8YV2t48Rw8bjkpD85QNE`</summary>

```text
Web search results for query: "CIRM Shinoda causal inference reward model debiasing ACL 2026"

Links: [{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"Counterfactual Debiasing for Fact Verification Anonymous ACL submission","url":"https://openreview.net/pdf?id=BddNTCq65yq"},{"title":"How causal inference tools can support debiasing of machine learning models for meaningful brain-based predictions","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314055.full.pdf"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"}]

Based on the search results, I found relevant research on causal inference approaches for reward model debiasing, though I didn't find a specific paper exactly matching all those terms together for ACL 2026.

The search results reveal several key papers in this research area:

One approach develops a causal reward model (CRM) that is robust to spurious correlations by leveraging causal inference techniques and the concept of counterfactual invariance, ensuring that reward model predictions remain consistent under interventions on irrelevant aspects of the input.

The problem this addresses is that reward models may assign higher scores to preference-irrelevant patterns like response length or sycophantic phrasing, leading to reward hacking where LLMs exploit these shortcuts during RLHF while drifting from the intended objective.

Various biases have been identified in reward models including length bias, sycophancy bias, concept bias, and discrimination bias, rooted in spurious correlations rather than true causal relationships.

If you're looking for a specific paper by Shinoda with those exact terms, it may be a very recent submission or preprint that hasn't been widely indexed yet, or the specific combination of keywords may need adjustment. Would you like me to search with different keywords or more specific information?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc408b57-5fed-46c9-99fb-739ba60c1acc",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "a71e2c82-10b0-42f0-b13f-3234ff1778bd",
  "toolUseResult": {
    "query": "CIRM Shinoda causal inference reward model debiasing ACL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N66upZrLuGc2VnndZ8FW4g",
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
      "Based on the search results, I found relevant research on causal inference approaches for reward model debiasing, though I didn't find a specific paper exactly matching all those terms together for ACL 2026.\n\nThe search results reveal several key papers in this research area:\n\nOne approach develops a causal reward model (CRM) that is robust to spurious correlations by leveraging causal inference techniques and the concept of counterfactual invariance, ensuring that reward model predictions remain consistent under interventions on irrelevant aspects of the input.\n\nThe problem this addresses is that reward models may assign higher scores to preference-irrelevant patterns like response length or sycophantic phrasing, leading to reward hacking where LLMs exploit these shortcuts during RLHF while drifting from the intended objective.\n\nVarious biases have been identified in reward models including length bias, sycophancy bias, concept bias, and discrimination bias, rooted in spurious correlations rather than true causal relationships.\n\nIf you're looking for a specific paper by Shinoda with those exact terms, it may be a very recent submission or preprint that hasn't been widely indexed yet, or the specific combination of keywords may need adjustment. Would you like me to search with different keywords or more specific information?"
    ],
    "durationSeconds": 6.211768721999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dc408b57-5fed-46c9-99fb-739ba60c1acc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T21:28:10.757Z_

<details><summary>↩ Tool result · `toolu_01MZG3KhzKoHtBQMWXdDFHiq`</summary>

```text
Web search results for query: "process reward model bias fluency exploitation mechanistic interpretability 2025 2026"

Links: [{"title":"Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/pdf/2603.03291"},{"title":"Reward Model Interpretability via Optimal and Pessimal Tokens","url":"https://arxiv.org/pdf/2506.07326"},{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/pdf/2509.24713"},{"title":"AI Safety, Alignment, and Interpretability in 2026 | Zylos Research","url":"https://zylos.ai/research/2026-02-09-ai-safety-alignment-interpretability"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"}]

Based on the search results, I found several highly relevant papers and articles addressing your query:

## Key Findings

**Process Reward Model Vulnerabilities:**
Research demonstrates that process reward models (PRMs) are vulnerable to reward hacking through adversarial optimization, with gradient-based attacks inflating rewards on invalid trajectories. When policies are trained on math problems, they achieve near-perfect PRM rewards while maintaining low ground-truth accuracy, with 43% of reward gains coming from stylistic shortcuts. This reveals that current PRMs function as fluency detectors rather than reasoning verifiers.

**Bias and Mechanistic Solutions:**
Recent mechanistic reward shaping approaches reduce targeted biases without degrading reward quality while using minimal labeled data. By isolating and removing linear directions in representation space that correspond to spurious shortcuts, researchers can mitigate length-, uncertainty-, and position-related biases.

**Circuit-Level Analysis:**
A mechanistic interpretability framework has been proposed that identifies specialized neural circuits responsible for rare-event processing in reward models, drawing on the hypothesis that reward models develop functionally distinct circuits for longtail scenarios.

**Mechanistic Interpretability Progress:**
New research is driving automated tools like Anthropic's circuit tracer and DeepMind's Gemma Scope 2, along with collaborative efforts across disciplines. MIT Technology Review recognized mechanistic interpretability as a 2026 Breakthrough Technology.

These results highlight the intersection of reward modeling robustness, bias mitigation, exploitation vulnerabilities, and mechanistic interpretability as active areas of research in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd119c29-1d71-4b33-a54d-3f014f377c7f",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "4e044d73-9823-4773-9cd7-e1f3eac4187b",
  "toolUseResult": {
    "query": "process reward model bias fluency exploitation mechanistic interpretability 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UuoWbESiu5KY3Qstf9oFyy",
        "content": [
          {
            "title": "Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read",
            "url": "https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/pdf/2603.03291"
          },
          {
            "title": "Reward Model Interpretability via Optimal and Pessimal Tokens",
            "url": "https://arxiv.org/pdf/2506.07326"
          },
          {
            "title": "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF",
            "url": "https://arxiv.org/pdf/2509.24713"
          },
          {
            "title": "AI Safety, Alignment, and Interpretability in 2026 | Zylos Research",
            "url": "https://zylos.ai/research/2026-02-09-ai-safety-alignment-interpretability"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and articles addressing your query:\n\n## Key Findings\n\n**Process Reward Model Vulnerabilities:**\nResearch demonstrates that process reward models (PRMs) are vulnerable to reward hacking through adversarial optimization, with gradient-based attacks inflating rewards on invalid trajectories. When policies are trained on math problems, they achieve near-perfect PRM rewards while maintaining low ground-truth accuracy, with 43% of reward gains coming from stylistic shortcuts. This reveals that current PRMs function as fluency detectors rather than reasoning verifiers.\n\n**Bias and Mechanistic Solutions:**\nRecent mechanistic reward shaping approaches reduce targeted biases without degrading reward quality while using minimal labeled data. By isolating and removing linear directions in representation space that correspond to spurious shortcuts, researchers can mitigate length-, uncertainty-, and position-related biases.\n\n**Circuit-Level Analysis:**\nA mechanistic interpretability framework has been proposed that identifies specialized neural circuits responsible for rare-event processing in reward models, drawing on the hypothesis that reward models develop functionally distinct circuits for longtail scenarios.\n\n**Mechanistic Interpretability Progress:**\nNew research is driving automated tools like Anthropic's circuit tracer and DeepMind's Gemma Scope 2, along with collaborative efforts across disciplines. MIT Technology Review recognized mechanistic interpretability as a 2026 Breakthrough Technology.\n\nThese results highlight the intersection of reward modeling robustness, bias mitigation, exploitation vulnerabilities, and mechanistic interpretability as active areas of research in 2025-2026."
    ],
    "durationSeconds": 7.843561108999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bd119c29-1d71-4b33-a54d-3f014f377c7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
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
  "leafUuid": "4e044d73-9823-4773-9cd7-e1f3eac4187b",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM mechanistic intervention proposal",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Tool result

_source line 24 · 2026-05-19T21:28:10.874Z_

<details><summary>↩ Tool result · `toolu_01VYdksPeaZhNkjrTWvSmbUz`</summary>

```text
Web search results for query: "Basu et al. "Interpretability without Actionability" mechanistic interventions clinical LM 2026"

Links: [{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"Interpretability without actionability: mechanistic methods cannot...","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science","url":"https://gist.science/paper/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF","url":"https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"}]

I found the paper you're looking for. Basu et al.'s paper "Interpretability without actionability" examines whether mechanistic interpretability methods can bridge the gap between the task-relevant knowledge language models encode in internal representations and their actual output performance.

**Key findings:**

The study compared four mechanistic interpretability methods—concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct)—for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).

Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. TSV steering at high strength corrected 24% of missed hazards while disrupting 6% of correct detections, but left 76% of errors uncorrected.

**Main conclusion:**

Current mechanistic interpretability methods cannot reliably translate internal knowledge into corrected outputs, with implications for AI safety frameworks that assume interpretability enables effective error correction.

The paper was published on arxiv on March 18, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c86c71c-6718-48b7-8ca1-3c05209753d2",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "faebbdff-259e-4b5c-b7f9-51dcba380b89",
  "toolUseResult": {
    "query": "Basu et al. \"Interpretability without Actionability\" mechanistic interventions clinical LM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011YLjNd6bkpBP2YcCbTVJJ8",
        "content": [
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/html/2603.18353v1"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot...",
            "url": "https://arxiv.org/abs/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
          },
          {
            "title": "(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science",
            "url": "https://gist.science/paper/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.18353"
          },
          {
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"
          },
          {
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"
          }
        ]
      },
      "I found the paper you're looking for. Basu et al.'s paper \"Interpretability without actionability\" examines whether mechanistic interpretability methods can bridge the gap between the task-relevant knowledge language models encode in internal representations and their actual output performance.\n\n**Key findings:**\n\nThe study compared four mechanistic interpretability methods—concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct)—for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).\n\nLinear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. TSV steering at high strength corrected 24% of missed hazards while disrupting 6% of correct detections, but left 76% of errors uncorrected.\n\n**Main conclusion:**\n\nCurrent mechanistic interpretability methods cannot reliably translate internal knowledge into corrected outputs, with implications for AI safety frameworks that assume interpretability enables effective error correction.\n\nThe paper was published on arxiv on March 18, 2026."
    ],
    "durationSeconds": 10.015904335,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2c86c71c-6718-48b7-8ca1-3c05209753d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T21:28:11.333Z_

<details><summary>↩ Tool result · `toolu_01AHq9deXDLtzwa7pTxqTnNz`</summary>

```text
Web search results for query: "Orgad et al. "Interpretability Can Be Actionable" ICML 2026"

Links: [{"title":"The Hitchhiker's Guide to Actionable Interpretability","url":"https://actionable-interpretability-guide.github.io/"},{"title":"[2605.11161] Interpretability Can Be Actionable","url":"https://arxiv.org/abs/2605.11161"},{"title":"ICML Poster Position: Interpretability Can Be Actionable","url":"https://icml.cc/virtual/2026/poster/67043"},{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161"},{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"Actionable Interpretability Must Be Defined in Terms of Symmetries","url":"https://arxiv.org/pdf/2601.12913"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/pdf/2603.18353"}]

I found the paper! Here are the search results for "Interpretability Can Be Actionable" by Orgad et al.:

The paper "Interpretability Can Be Actionable" was authored by Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron C. Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, and Mor Geva, published in 2026.

**Key Arguments:**

The paper argues that interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. The authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.

The paper expresses concern that despite rapid growth in interpretability research, much of this work has not translated into practical impact.

**Framework and Solutions:**

To address these barriers, the authors identify five domains where interpretability offers unique leverage and present a framework for actionable interpretability with evaluation criteria aligned with practical outcomes.

The paper is available on arXiv (2605.11161) and was presented as a position paper at ICML 2026. A companion blog guide titled "The Hitchhiker's Guide to Actionable Interpretability" was also published.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2978a5-a9a2-494f-89f9-021159a8bc22",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "cbecf4f5-3b7f-4255-926c-3626e14fa80a",
  "toolUseResult": {
    "query": "Orgad et al. \"Interpretability Can Be Actionable\" ICML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Skfgo5fbCxMeCDJTBS2b9b",
        "content": [
          {
            "title": "The Hitchhiker's Guide to Actionable Interpretability",
            "url": "https://actionable-interpretability-guide.github.io/"
          },
          {
            "title": "[2605.11161] Interpretability Can Be Actionable",
            "url": "https://arxiv.org/abs/2605.11161"
          },
          {
            "title": "ICML Poster Position: Interpretability Can Be Actionable",
            "url": "https://icml.cc/virtual/2026/poster/67043"
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
            "title": "Actionable Interpretability Must Be Defined in Terms of Symmetries",
            "url": "https://arxiv.org/pdf/2601.12913"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/pdf/2603.18353"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Interpretability Can Be Actionable\" by Orgad et al.:\n\nThe paper \"Interpretability Can Be Actionable\" was authored by Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron C. Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, and Mor Geva, published in 2026.\n\n**Key Arguments:**\n\nThe paper argues that interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. The authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.\n\nThe paper expresses concern that despite rapid growth in interpretability research, much of this work has not translated into practical impact.\n\n**Framework and Solutions:**\n\nTo address these barriers, the authors identify five domains where interpretability offers unique leverage and present a framework for actionable interpretability with evaluation criteria aligned with practical outcomes.\n\nThe paper is available on arXiv (2605.11161) and was presented as a position paper at ICML 2026. A companion blog guide titled \"The Hitchhiker's Guide to Actionable Interpretability\" was also published."
    ],
    "durationSeconds": 8.551248261000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc2978a5-a9a2-494f-89f9-021159a8bc22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T21:28:13.503Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've got some initial results. Let me search for more specific things to round out my understanding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbecf4f5-3b7f-4255-926c-3626e14fa80a",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "2b550b98-0310-4aa9-9cdb-8477c4cdf168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 27 · 2026-05-19T21:28:13.980Z_

让我继续深入搜索几个关键方面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b550b98-0310-4aa9-9cdb-8477c4cdf168",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "4f888320-88db-4687-af1b-fd1bb07ea6e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 28 · 2026-05-19T21:28:14.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHGMm3188zhv9hUY9Q3ppx`</summary>

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
  "parentUuid": "4f888320-88db-4687-af1b-fd1bb07ea6e5",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "664c772d-2585-4661-ae5f-bea2be7fc548",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 29 · 2026-05-19T21:28:15.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERgTpkFpxYXdSr6dks7ybq`</summary>

```json
{
  "query": "\"domain amenability\" mechanistic interpretability when interventions succeed conditions 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "664c772d-2585-4661-ae5f-bea2be7fc548",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "401e2246-86df-48c1-ab5e-9af40fd31428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 30 · 2026-05-19T21:28:16.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0121YJkvYfkpDCynXcGjURy5`</summary>

```json
{
  "query": "Lee et al. \"Rigorous Interpretation Is a Form of Evaluation\" interpretability falsifiability 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401e2246-86df-48c1-ab5e-9af40fd31428",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "dda8a181-9da6-4351-9593-4a036a7dfd97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 31 · 2026-05-19T21:28:17.076Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EY22L3oFhgJKTZBtPWeqzA`</summary>

```json
{
  "query": "multi-granularity mechanistic intervention comparison feature neuron circuit level systematic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dda8a181-9da6-4351-9593-4a036a7dfd97",
  "isSidechain": false,
  "requestId": "req_011CbCduzdsTPwvX2RvBcsfx",
  "type": "assistant",
  "uuid": "931b3b05-01f4-489f-bc31-03452a3bfa73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ebVGKMuaSkyh6bEeyyu7j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 799,
      "cache_creation_input_tokens": 3052,
      "cache_read_input_tokens": 25235,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 799,
          "output_tokens": 303,
          "cache_read_input_tokens": 25235,
          "cache_creation_input_tokens": 3052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3052
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

_source line 32 · 2026-05-19T21:28:21.041Z_

<details><summary>↩ Tool result · `toolu_01XHGMm3188zhv9hUY9Q3ppx`</summary>

```text
Web search results for query: "Shinoda "Debiasing Reward Models via Causally Motivated Inference-Time Intervention" arXiv 2604.27495"

Links: [{"title":"[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/abs/2604.27495"},{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/pdf/2510.23751"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/pdf/2506.19248"},{"title":"Fixing the Broken Compass: Diagnosing and Improving Inference-Time Reward Modeling","url":"https://arxiv.org/pdf/2503.05188"}]

I found the paper! Here are the key details about the research:

**Paper Title:** Debiasing Reward Models via Causally Motivated Inference-Time Intervention

**Authors:** Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida from Human Informatics Labs., NTT, Inc.

**arXiv ID:** 2604.27495

**Key Contributions:**

Reward models play a central role in aligning large language models with human preferences, but RMs are often sensitive to spurious features such as response length. The paper proposes causally motivated intervention for mitigating multiple types of biases in RMs at inference time.

**Method:** The method first identifies neurons whose activations are strongly correlated with predefined bias attributes, and applies neuron-level intervention that suppresses these signals.

**Results:** The method observes reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs.

The paper was published on April 30, 2026, and is available on arXiv at https://arxiv.org/abs/2604.27495.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "664c772d-2585-4661-ae5f-bea2be7fc548",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "15711b56-ff14-403e-b4b4-984b4576fc9f",
  "toolUseResult": {
    "query": "Shinoda \"Debiasing Reward Models via Causally Motivated Inference-Time Intervention\" arXiv 2604.27495",
    "results": [
      {
        "tool_use_id": "srvtoolu_018sM1VcwW76ndVxFiNi2BNR",
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
      "I found the paper! Here are the key details about the research:\n\n**Paper Title:** Debiasing Reward Models via Causally Motivated Inference-Time Intervention\n\n**Authors:** Kazutoshi Shinoda, Kosuke Nishida, Kyosuke Nishida from Human Informatics Labs., NTT, Inc.\n\n**arXiv ID:** 2604.27495\n\n**Key Contributions:**\n\nReward models play a central role in aligning large language models with human preferences, but RMs are often sensitive to spurious features such as response length. The paper proposes causally motivated intervention for mitigating multiple types of biases in RMs at inference time.\n\n**Method:** The method first identifies neurons whose activations are strongly correlated with predefined bias attributes, and applies neuron-level intervention that suppresses these signals.\n\n**Results:** The method observes reductions in sensitivity to spurious features across diverse bias types, without inducing performance trade-offs.\n\nThe paper was published on April 30, 2026, and is available on arXiv at https://arxiv.org/abs/2604.27495."
    ],
    "durationSeconds": 6.119978389999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "664c772d-2585-4661-ae5f-bea2be7fc548",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T21:28:22.188Z_

<details><summary>↩ Tool result · `toolu_01ERgTpkFpxYXdSr6dks7ybq`</summary>

```text
Web search results for query: ""domain amenability" mechanistic interpretability when interventions succeed conditions 2026"

Links: [{"title":"Mechanistic Interpretability Explained (2026)","url":"https://www.taskade.com/blog/what-is-mechanistic-interpretability"},{"title":"AI Safety, Alignment, and Interpretability in 2026 | Zylos Research","url":"https://zylos.ai/research/2026-02-09-ai-safety-alignment-interpretability"},{"title":"Mechanistic Interpretability Named MIT's 2026 Breakthrough for Understanding AI Internal States | The Consciousness AI - Artificial Consciousness Research","url":"https://theconsciousness.ai/posts/mechanistic-interpretability-breakthrough-2026/"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Mechanistic interpretability: 10 Breakthrough Technologies 2026 | MIT Technology Review","url":"https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Interpreting Transformers Through Attention Head Intervention","url":"https://arxiv.org/pdf/2601.04398"}]

Based on the search results, I found relevant information about mechanistic interpretability and interventions in 2026, though the results don't specifically contain a technical concept explicitly called "domain amenability." However, I can share what the research shows about conditions for successful interventions:

## Mechanistic Interpretability and Intervention Success (2026)

OpenAI used in-house mechanistic interpretability tools to compare models with and without problematic training data, successfully identifying the source of malicious behaviors. This demonstrates practical intervention success.

Researchers identified the Indirect Object Identification (IOI) circuit in GPT-2 Small using causal interventions, isolating attention heads that vote for possible antecedents and MLPs that resolve the vote.

Regarding intervention design conditions, steering directions demand categorical exclusivity for clean intervention, with high separation indicating switch-like features firing predominantly for one code type, enabling targeted corrections without affecting the opposite category.

More broadly, mechanistic understanding now enables targeted control of model behaviour, successfully suppressing toxic outputs and manipulating semantic content through selective attention head intervention, validating the practical utility of interpretability research for AI safety.

The search results suggest that successful interventions depend on factors like clear feature separation, categorical exclusivity, and the ability to isolate specific circuit components—though the specific term "domain amenability" doesn't appear in these sources. Would you like me to search for more specific information about that particular concept?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "401e2246-86df-48c1-ab5e-9af40fd31428",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "1605832e-7188-49c4-a87a-215b1ccd5ed7",
  "toolUseResult": {
    "query": "\"domain amenability\" mechanistic interpretability when interventions succeed conditions 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DJnCfzsXGKpKcR8fCuSixC",
        "content": [
          {
            "title": "Mechanistic Interpretability Explained (2026)",
            "url": "https://www.taskade.com/blog/what-is-mechanistic-interpretability"
          },
          {
            "title": "AI Safety, Alignment, and Interpretability in 2026 | Zylos Research",
            "url": "https://zylos.ai/research/2026-02-09-ai-safety-alignment-interpretability"
          },
          {
            "title": "Mechanistic Interpretability Named MIT's 2026 Breakthrough for Understanding AI Internal States | The Consciousness AI - Artificial Consciousness Research",
            "url": "https://theconsciousness.ai/posts/mechanistic-interpretability-breakthrough-2026/"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "Mechanistic interpretability: 10 Breakthrough Technologies 2026 | MIT Technology Review",
            "url": "https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/"
          },
          {
            "title": "Mechanistic Interpretability Framework",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-framework"
          },
          {
            "title": "Interpreting Transformers Through Attention Head Intervention",
            "url": "https://arxiv.org/pdf/2601.04398"
          }
        ]
      },
      "Based on the search results, I found relevant information about mechanistic interpretability and interventions in 2026, though the results don't specifically contain a technical concept explicitly called \"domain amenability.\" However, I can share what the research shows about conditions for successful interventions:\n\n## Mechanistic Interpretability and Intervention Success (2026)\n\nOpenAI used in-house mechanistic interpretability tools to compare models with and without problematic training data, successfully identifying the source of malicious behaviors. This demonstrates practical intervention success.\n\nResearchers identified the Indirect Object Identification (IOI) circuit in GPT-2 Small using causal interventions, isolating attention heads that vote for possible antecedents and MLPs that resolve the vote.\n\nRegarding intervention design conditions, steering directions demand categorical exclusivity for clean intervention, with high separation indicating switch-like features firing predominantly for one code type, enabling targeted corrections without affecting the opposite category.\n\nMore broadly, mechanistic understanding now enables targeted control of model behaviour, successfully suppressing toxic outputs and manipulating semantic content through selective attention head intervention, validating the practical utility of interpretability research for AI safety.\n\nThe search results suggest that successful interventions depend on factors like clear feature separation, categorical exclusivity, and the ability to isolate specific circuit components—though the specific term \"domain amenability\" doesn't appear in these sources. Would you like me to search for more specific information about that particular concept?"
    ],
    "durationSeconds": 6.799652774999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "401e2246-86df-48c1-ab5e-9af40fd31428",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "1605832e-7188-49c4-a87a-215b1ccd5ed7",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM mechanistic intervention proposal",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Tool result

_source line 36 · 2026-05-19T21:28:23.953Z_

<details><summary>↩ Tool result · `toolu_0121YJkvYfkpDCynXcGjURy5`</summary>

```text
Web search results for query: "Lee et al. "Rigorous Interpretation Is a Form of Evaluation" interpretability falsifiability 2026"

Links: [{"title":"Rigorous Interpretation Is a Form of Evaluation","url":"https://arxiv.org/html/2605.05508v1"},{"title":"Towards falsifiable interpretability research","url":"https://arxiv.org/pdf/2010.12016"},{"title":"Towards A Rigorous Science of Interpretable Machine Learning","url":"https://arxiv.org/pdf/1702.08608"},{"title":"Are Interpretations Fairly Evaluated? A Definition Driven Pipeline for   Post-Hoc Interpretability","url":"https://arxiv.org/pdf/2009.07494"},{"title":"Towards Faithfully Interpretable NLP Systems: How should we define and   evaluate faithfulness?","url":"https://arxiv.org/pdf/2004.03685"}]

I found the paper you're looking for! Here's what I found:

When held to rigorous standards, interpretability can be evaluation. To fulfill its evaluative potential, interpretability methods must generate claims that are falsifiable, reproducible, and predictive—that is, interpretability must meet scientific standards.

The paper is authored by Isabelle Lee, Emmy Liu, Cathy Jiao, Brihi Joshi, Dani Yogatama, Fazl Barez, and Michael Saxon. The paper appears to be from 2026 based on the arxiv reference (2605.05508).

The paper reframes interpretability not merely as an exploratory add-on, but as a scientifically grounded and reliable explanation of behavior: an evaluation in its own right.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda8a181-9da6-4351-9593-4a036a7dfd97",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "48650819-1a8b-4abb-aa0f-ad2a63fd1b13",
  "toolUseResult": {
    "query": "Lee et al. \"Rigorous Interpretation Is a Form of Evaluation\" interpretability falsifiability 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QBduL2KKWErdAyKPjmdYyo",
        "content": [
          {
            "title": "Rigorous Interpretation Is a Form of Evaluation",
            "url": "https://arxiv.org/html/2605.05508v1"
          },
          {
            "title": "Towards falsifiable interpretability research",
            "url": "https://arxiv.org/pdf/2010.12016"
          },
          {
            "title": "Towards A Rigorous Science of Interpretable Machine Learning",
            "url": "https://arxiv.org/pdf/1702.08608"
          },
          {
            "title": "Are Interpretations Fairly Evaluated? A Definition Driven Pipeline for   Post-Hoc Interpretability",
            "url": "https://arxiv.org/pdf/2009.07494"
          },
          {
            "title": "Towards Faithfully Interpretable NLP Systems: How should we define and   evaluate faithfulness?",
            "url": "https://arxiv.org/pdf/2004.03685"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nWhen held to rigorous standards, interpretability can be evaluation. To fulfill its evaluative potential, interpretability methods must generate claims that are falsifiable, reproducible, and predictive—that is, interpretability must meet scientific standards.\n\nThe paper is authored by Isabelle Lee, Emmy Liu, Cathy Jiao, Brihi Joshi, Dani Yogatama, Fazl Barez, and Michael Saxon. The paper appears to be from 2026 based on the arxiv reference (2605.05508).\n\nThe paper reframes interpretability not merely as an exploratory add-on, but as a scientifically grounded and reliable explanation of behavior: an evaluation in its own right."
    ],
    "durationSeconds": 7.624635367999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dda8a181-9da6-4351-9593-4a036a7dfd97",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T21:28:25.114Z_

<details><summary>↩ Tool result · `toolu_01EY22L3oFhgJKTZBtPWeqzA`</summary>

```text
Web search results for query: "multi-granularity mechanistic intervention comparison feature neuron circuit level systematic 2025 2026"

Links: [{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read","url":"https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"},{"title":"Understanding Mechanistic Interpretability in AI Models | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Can Information Flows Suggest Targets for Interventions in Neural   Circuits?","url":"https://arxiv.org/pdf/2111.05299"},{"title":"Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3787104"},{"title":"Inferring and validating mechanistic models of neural microcircuits based on spike-train data","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821748/"}]

I've completed the web search for your query on multi-granularity mechanistic intervention comparison at feature, neuron, and circuit levels from 2025-2026. Here are the key findings:

## Recent Mechanistic Interpretability Work (2025-2026)

**Multi-Granularity Approaches:**
The appropriate level of granularity may correlate with the amount of mechanistic detail required for effective diagnosis and intervention. This highlights the importance of working across different analytical levels.

**Circuit-Level Research:**
Anthropic's 2025 circuit tracing work on Claude 3.5 Haiku demonstrated that mechanisms behind multi-step reasoning, hallucination, and jailbreak resistance can be surfaced and studied. TransformerLens has evolved as a fundamental instrument in the field of mechanistic interpretability by offering tools for in-depth circuit tracing and intervention.

**Feature and Neuron-Level Analysis:**
Sparse autoencoders and spatial statistical measures are being employed to unmix polysemantic neuron activations, illuminating monosemantic, geographically structured features in LLMs.

**Validation and Systematic Comparison:**
The 2025 "Open Problems" paper acknowledged that "conflating hypotheses with conclusions has been commonplace in mechanistic interpretability research" and validation is an important area for the field to improve.

The search results show that 2025-2026 research is increasingly focused on systematic approaches across multiple granularities, though significant validation challenges remain.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "931b3b05-01f4-489f-bc31-03452a3bfa73",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "284f7e33-4e99-4279-b0c9-6a7440d2191f",
  "toolUseResult": {
    "query": "multi-granularity mechanistic intervention comparison feature neuron circuit level systematic 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KdjfWxRr9mrPVuAuJXrnvA",
        "content": [
          {
            "title": "Mechanistic Interpretability Framework",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-framework"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models 8/16/2025 • 40 min read",
            "url": "https://intuitionlabs.ai/pdfs/understanding-mechanistic-interpretability-in-ai-models.pdf"
          },
          {
            "title": "Understanding Mechanistic Interpretability in AI Models | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mechanistic-interpretability-ai-llms"
          },
          {
            "title": "Automated Interpretability-Driven Model Auditing and Control: A Research Agenda",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"
          },
          {
            "title": "Can Information Flows Suggest Targets for Interventions in Neural   Circuits?",
            "url": "https://arxiv.org/pdf/2111.05299"
          },
          {
            "title": "Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3787104"
          },
          {
            "title": "Inferring and validating mechanistic models of neural microcircuits based on spike-train data",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6821748/"
          }
        ]
      },
      "I've completed the web search for your query on multi-granularity mechanistic intervention comparison at feature, neuron, and circuit levels from 2025-2026. Here are the key findings:\n\n## Recent Mechanistic Interpretability Work (2025-2026)\n\n**Multi-Granularity Approaches:**\nThe appropriate level of granularity may correlate with the amount of mechanistic detail required for effective diagnosis and intervention. This highlights the importance of working across different analytical levels.\n\n**Circuit-Level Research:**\nAnthropic's 2025 circuit tracing work on Claude 3.5 Haiku demonstrated that mechanisms behind multi-step reasoning, hallucination, and jailbreak resistance can be surfaced and studied. TransformerLens has evolved as a fundamental instrument in the field of mechanistic interpretability by offering tools for in-depth circuit tracing and intervention.\n\n**Feature and Neuron-Level Analysis:**\nSparse autoencoders and spatial statistical measures are being employed to unmix polysemantic neuron activations, illuminating monosemantic, geographically structured features in LLMs.\n\n**Validation and Systematic Comparison:**\nThe 2025 \"Open Problems\" paper acknowledged that \"conflating hypotheses with conclusions has been commonplace in mechanistic interpretability research\" and validation is an important area for the field to improve.\n\nThe search results show that 2025-2026 research is increasingly focused on systematic approaches across multiple granularities, though significant validation challenges remain."
    ],
    "durationSeconds": 8.034168092,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "931b3b05-01f4-489f-bc31-03452a3bfa73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-19T21:28:25.118Z_

```json
{
  "parentUuid": "284f7e33-4e99-4279-b0c9-6a7440d2191f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8fee4580-909b-4b6d-a074-b87f77e8a77c",
  "timestamp": "2026-05-19T21:28:25.118Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-19T21:28:29.043Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to round out my understanding, particularly about:
1. Whether anyone has already proposed a "domain amenability" or similar framework for when mechanistic interventions work
2. The CoRL venue scope - to verify if this is appropriate for CoRL
3. The "Locate, Steer, Improve" survey
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fee4580-909b-4b6d-a074-b87f77e8a77c",
  "isSidechain": false,
  "requestId": "req_011CbCdw1YijtwTGYdL2Aj32",
  "type": "assistant",
  "uuid": "565b7b1f-0218-4d20-9349-7b30adafb775",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WvnN6Pyv5sqvrDQsAXCZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 28287,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 28287,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 40 · 2026-05-19T21:28:29.544Z_

让我再做几个针对性的搜索来完善调研。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "565b7b1f-0218-4d20-9349-7b30adafb775",
  "isSidechain": false,
  "requestId": "req_011CbCdw1YijtwTGYdL2Aj32",
  "type": "assistant",
  "uuid": "2733ac91-6d23-464b-a08b-237ac1e50736",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WvnN6Pyv5sqvrDQsAXCZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 28287,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 28287,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 41 · 2026-05-19T21:28:30.027Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182EfyRqRkJKVBPrjWtXXxX`</summary>

```json
{
  "query": "CoRL 2026 Conference on Robot Learning topics scope call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2733ac91-6d23-464b-a08b-237ac1e50736",
  "isSidechain": false,
  "requestId": "req_011CbCdw1YijtwTGYdL2Aj32",
  "type": "assistant",
  "uuid": "7f3d57e0-46a6-477b-91b1-1f2af7a73349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WvnN6Pyv5sqvrDQsAXCZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 28287,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 28287,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 42 · 2026-05-19T21:28:30.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxD415dwjNbKZfN9samou8`</summary>

```json
{
  "query": "\"Locate Steer Improve\" actionable mechanistic interpretability survey Zhang 2026 arXiv 2601.14004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f3d57e0-46a6-477b-91b1-1f2af7a73349",
  "isSidechain": false,
  "requestId": "req_011CbCdw1YijtwTGYdL2Aj32",
  "type": "assistant",
  "uuid": "e7b5ee4d-e1fb-47f5-a3da-b7651310c074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WvnN6Pyv5sqvrDQsAXCZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 28287,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 28287,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 43 · 2026-05-19T21:28:32.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KXTxvPzSyHH9YPRcTdQw2g`</summary>

```json
{
  "query": "Arad et al. \"SAEs Are Good for Steering If You Select the Right Features\" EMNLP 2025 output features"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7b5ee4d-e1fb-47f5-a3da-b7651310c074",
  "isSidechain": false,
  "requestId": "req_011CbCdw1YijtwTGYdL2Aj32",
  "type": "assistant",
  "uuid": "948a4f62-0e09-41c6-8d75-0d5a862fd982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WvnN6Pyv5sqvrDQsAXCZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3750,
      "cache_read_input_tokens": 28287,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 306,
          "cache_read_input_tokens": 28287,
          "cache_creation_input_tokens": 3750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3750
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

_source line 44 · 2026-05-19T21:28:36.681Z_

<details><summary>↩ Tool result · `toolu_0182EfyRqRkJKVBPrjWtXXxX`</summary>

```text
Web search results for query: "CoRL 2026 Conference on Robot Learning topics scope call for papers"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"Synthesising robot behaviour through reinforcement learning for homeostasis","url":"https://www.biorxiv.org/content/10.1101/2024.06.03.597087.full.pdf"},{"title":"Automated Hybrid Reward Scheduling via Large Language Models for Robotic   Skill Learning","url":"https://arxiv.org/pdf/2505.02483"}]

Based on the search results, here's what I found about CoRL 2026's topics, scope, and call for papers:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Topics and Scope

CoRL welcomes papers in areas such as: Learning representations for robotic perception and control, Learning robot foundation models or general-purpose knowledge systems for robotics, Imitation learning for robotics, Reinforcement learning for control of physical robots, Learning approaches to robot safety and alignment, Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, Robot systems, hardware, and sensors for learning and data-driven approaches, Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and Video models and latent world models for robot learning.

## Key Requirements and Guidelines

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.

## Important Dates

Key dates for submissions include May 25 for abstract submission, May 28 for full paper submission, and November 9-12 for the conference in Austin, TX.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f3d57e0-46a6-477b-91b1-1f2af7a73349",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "208eb38a-762c-4b14-9223-9f02fafda4f8",
  "toolUseResult": {
    "query": "CoRL 2026 Conference on Robot Learning topics scope call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_0139YxonjZGKU8gQWjchfy6L",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "Synthesising robot behaviour through reinforcement learning for homeostasis",
            "url": "https://www.biorxiv.org/content/10.1101/2024.06.03.597087.full.pdf"
          },
          {
            "title": "Automated Hybrid Reward Scheduling via Large Language Models for Robotic   Skill Learning",
            "url": "https://arxiv.org/pdf/2505.02483"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026's topics, scope, and call for papers:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Topics and Scope\n\nCoRL welcomes papers in areas such as: Learning representations for robotic perception and control, Learning robot foundation models or general-purpose knowledge systems for robotics, Imitation learning for robotics, Reinforcement learning for control of physical robots, Learning approaches to robot safety and alignment, Applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics, Robot systems, hardware, and sensors for learning and data-driven approaches, Theoretical foundations of robot learning, including generalization theory and uncertainty quantification, and Video models and latent world models for robot learning.\n\n## Key Requirements and Guidelines\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. Submissions without a robotics focus will be returned without review.\n\n## Important Dates\n\nKey dates for submissions include May 25 for abstract submission, May 28 for full paper submission, and November 9-12 for the conference in Austin, TX."
    ],
    "durationSeconds": 6.650016152999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f3d57e0-46a6-477b-91b1-1f2af7a73349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-19T21:28:37.801Z_

<details><summary>↩ Tool result · `toolu_01KXTxvPzSyHH9YPRcTdQw2g`</summary>

```text
Web search results for query: "Arad et al. "SAEs Are Good for Steering If You Select the Right Features" EMNLP 2025 output features"

Links: [{"title":"SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.519/"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features","url":"https://arxiv.org/pdf/2505.20063"},{"title":"[2505.20063] SAEs Are Good for Steering -- If You Select the Right Features","url":"https://arxiv.org/abs/2505.20063"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"},{"title":"SAEs Are Good for Steering – If You Select the Right Features","url":"https://arxiv.org/html/2505.20063v2"},{"title":"SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"}]

I found the paper! Here's what the research covers:

This EMNLP 2025 paper by Dana Arad, Aaron Mueller, and Yonatan Belinkov is titled "SAEs Are Good for Steering – If You Select the Right Features."

**Key findings regarding output features:**

The authors draw a distinction between two types of features: input features, which mainly capture patterns in the model's input, and output features, those that have a human-understandable effect on the model's output. They propose input and output scores to characterize and locate these types of features, and show that high values for both scores rarely co-occur in the same features.

The output score measures the alignment between the effects of SAE features on the model's output distribution and the expected set of tokens—in their case, their top logit lens tokens.

**Practical impact:**

After filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.

The paper is available on the ACL Anthology and arXiv (arxiv.org/pdf/2505.20063).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "948a4f62-0e09-41c6-8d75-0d5a862fd982",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "9fcfaec2-286b-4891-8076-1210ef521dc2",
  "toolUseResult": {
    "query": "Arad et al. \"SAEs Are Good for Steering If You Select the Right Features\" EMNLP 2025 output features",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KAxZ2SBR8ny4HMgHXvfE4u",
        "content": [
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.519/"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features",
            "url": "https://arxiv.org/pdf/2505.20063"
          },
          {
            "title": "[2505.20063] SAEs Are Good for Steering -- If You Select the Right Features",
            "url": "https://arxiv.org/abs/2505.20063"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://www.researchgate.net/publication/397422533_SAEs_Are_Good_for_Steering_-_If_You_Select_the_Right_Features"
          },
          {
            "title": "SAEs Are Good for Steering – If You Select the Right Features",
            "url": "https://arxiv.org/html/2505.20063v2"
          },
          {
            "title": "SAEs Are Good for Steering -- If You Select the Right Features | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/saes-are-good-steering-if-you-select"
          }
        ]
      },
      "I found the paper! Here's what the research covers:\n\nThis EMNLP 2025 paper by Dana Arad, Aaron Mueller, and Yonatan Belinkov is titled \"SAEs Are Good for Steering – If You Select the Right Features.\"\n\n**Key findings regarding output features:**\n\nThe authors draw a distinction between two types of features: input features, which mainly capture patterns in the model's input, and output features, those that have a human-understandable effect on the model's output. They propose input and output scores to characterize and locate these types of features, and show that high values for both scores rarely co-occur in the same features.\n\nThe output score measures the alignment between the effects of SAE features on the model's output distribution and the expected set of tokens—in their case, their top logit lens tokens.\n\n**Practical impact:**\n\nAfter filtering out features with low output scores, steering with SAEs results in a 2–3x improvement, matching the performance of existing supervised methods.\n\nThe paper is available on the ACL Anthology and arXiv (arxiv.org/pdf/2505.20063)."
    ],
    "durationSeconds": 5.654568276999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "948a4f62-0e09-41c6-8d75-0d5a862fd982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T21:28:40.913Z_

<details><summary>↩ Tool result · `toolu_01UxD415dwjNbKZfN9samou8`</summary>

```text
Web search results for query: ""Locate Steer Improve" actionable mechanistic interpretability survey Zhang 2026 arXiv 2601.14004"

Links: [{"title":"[2601.14004] Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/abs/2601.14004"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/399956588_Locate_Steer_and_Improve_A_Practical_Survey_of_Actionable_Mechanistic_Interpretability_in_Large_Language_Models"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic","url":"https://arxiv.org/pdf/2601.14004"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260114004Z/abstract"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large L - YouTube","url":"https://www.youtube.com/watch?v=GpAK_SwfVOY"},{"title":"GitHub - rattlesnakey/Awesome-Actionable-MI-Survey: The Github repo for our survey paper: \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\" · GitHub","url":"https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://bibbase.org/network/publication/lindsey-vanderweij-nanda-others-locatesteerandimproveapracticalsurveyofactionablemechanisticinterpretabilityinlargelanguagemodels-2026"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/html/2601.14004v1"},{"title":"Paper page - Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://huggingface.co/papers/2601.14004"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202601.1663"}]

I found the paper you're looking for! Here are the search results:

**Paper Details:**

The paper presents a practical survey structured around the pipeline: "Locate, Steer, and Improve." 

**Title:** Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models

**Authors and Publication:** The paper was submitted on January 20, 2026, with the latest version (v4) revised on April 14, 2026, with authors including Hengyuan Zhang and 28 other co-authors

**arXiv Details:** arXiv:2601.14004, DOI: 10.48550/arXiv.2601.14004

**Content Focus:** The paper formally categorizes Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol, and demonstrates how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as an actionable methodology for model optimization.

**Resources:** The curated paper list of this work is available at https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7b5ee4d-e1fb-47f5-a3da-b7651310c074",
  "isSidechain": false,
  "promptId": "f07def41-fe12-4b73-ae3d-cb6d3cb0dac3",
  "type": "user",
  "uuid": "6e5b90be-fda3-4a37-87ec-63ca7dee792e",
  "toolUseResult": {
    "query": "\"Locate Steer Improve\" actionable mechanistic interpretability survey Zhang 2026 arXiv 2601.14004",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Ym3NbnQecfnxEkzeCNnFJ",
        "content": [
          {
            "title": "[2601.14004] Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://arxiv.org/abs/2601.14004"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/399956588_Locate_Steer_and_Improve_A_Practical_Survey_of_Actionable_Mechanistic_Interpretability_in_Large_Language_Models"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic",
            "url": "https://arxiv.org/pdf/2601.14004"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260114004Z/abstract"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large L - YouTube",
            "url": "https://www.youtube.com/watch?v=GpAK_SwfVOY"
          },
          {
            "title": "GitHub - rattlesnakey/Awesome-Actionable-MI-Survey: The Github repo for our survey paper: \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\" · GitHub",
            "url": "https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://bibbase.org/network/publication/lindsey-vanderweij-nanda-others-locatesteerandimproveapracticalsurveyofactionablemechanisticinterpretabilityinlargelanguagemodels-2026"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://arxiv.org/html/2601.14004v1"
          },
          {
            "title": "Paper page - Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://huggingface.co/papers/2601.14004"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202601.1663"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\n**Paper Details:**\n\nThe paper presents a practical survey structured around the pipeline: \"Locate, Steer, and Improve.\" \n\n**Title:** Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\n\n**Authors and Publication:** The paper was submitted on January 20, 2026, with the latest version (v4) revised on April 14, 2026, with authors including Hengyuan Zhang and 28 other co-authors\n\n**arXiv Details:** arXiv:2601.14004, DOI: 10.48550/arXiv.2601.14004\n\n**Content Focus:** The paper formally categorizes Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol, and demonstrates how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as an actionable methodology for model optimization.\n\n**Resources:** The curated paper list of this work is available at https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey"
    ],
    "durationSeconds": 9.929518441,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7b5ee4d-e1fb-47f5-a3da-b7651310c074",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "6e5b90be-fda3-4a37-87ec-63ca7dee792e",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM mechanistic intervention proposal",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Assistant

_source line 49 · 2026-05-19T21:29:26.194Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important. I found that CoRL 2026 (Conference on Robot Learning) explicitly states: "Submissions without a robotics focus will be returned without review." This proposal is about mechanistic interpretability of Process Reward Models for mathematical reasoning — it has absolutely nothing to do with robotics. This is a fatal venue mismatch.

Let me now synthesize all my findings and produce the evaluation.

Key observations from my research:

1. **Venue Mismatch (CRITICAL)**: CoRL 2026 is the Conference on Robot Learning. The call for papers explicitly says "Submissions should focus on a core robotics problem" and "Submissions without a robotics focus will be returned without review." This proposal has zero robotics content — it's about mechanistic interpretability of process reward models for mathematical reasoning. This would be desk-rejected immediately.


2. **References appear legitimate**: The cited papers from Basu, SteerRM, CIRM/Shinoda, Orgad, Lee, Zhang, and Arad all check out and are described accurately.
3. **The "Domain Amenability Hypothesis" seems genuinely novel**: I couldn't find this concept in existing mechanistic interpretability literature, suggesting it's an original contribution.
4. **Multi-granularity comparison is also novel**: No prior work systematically compares feature-level, neuron-level, and circuit-level interventions in a controlled setting—existing papers tackle these separately.

Now I'm questioning whether the Domain Amenability Hypothesis is actually meaningful or just a trivial observation that interventions work better on simpler, more constrained problems. The core claim feels dangerously close to stating the obvious.

The thesis has two components: first, a systematic multi-granularity comparison of mechanistic interventions on PRMs, which is primarily an empirical contribution about experimental design rather than a conceptual advance; second, the Domain Amenability Hypothesis itself, which is the conceptual piece but is only tested in one domain.

The hypothesis testing is particularly weak—comparing PRMs (where interventions succeed) against clinical language models from prior work (which they didn't even evaluate themselves) gives just two data points, which isn't convincing evidence. And if mechanistic interventions do work on PRMs, that's not surprising given that PRMs are exactly the kind of constrained, well-defined domain the hypothesis predicts should be amenable to such interventions. The multi-granularity comparison is methodologically sound but not unexpected, though the framing around actionability in mechanistic interpretability is genuinely timely. Basu et al. vs. SteerRM/CIRM is a real tension in the field.
- The experimental design is extremely thorough and well-thought-out.
- The integration of multiple evaluation frameworks (Orgad et al. + Lee et al.) is good practice.
- Training SAEs from scratch on PRM activations (vs. pretrained) is a sound methodological improvement.
- The pilot-then-target layer selection is a practical contribution.
- The "dual outcome" design where failure is also informative is well-constructed.

**Concerns:**
1. **Thin conceptual core**: The "Domain Amenability Hypothesis" is the main conceptual contribution, but it amounts to "interventions work better on constrained, verifiable tasks." This feels like it could be derived from first principles without running experiments.
2. **Weak hypothesis validation**: Testing against just PRMs as the positive case and Basu et al.'s clinical LMs as the negative case leaves the hypothesis underdeveloped—a reviewer would likely want evidence across five to ten domains spanning the full spectrum.
3. **Primarily a benchmark/comparison paper**: The core of the work is running existing methods (SteerRM, CIRM, circuit-level ablation) in a unified evaluation framework. This is useful but not conceptually deep.
4. **Self-fulfilling design**: They chose PRMs specifically because they satisfy the domain amenability conditions, so finding that interventions succeed there doesn't strongly validate the hypothesis—they selected for success.

**Venue Consideration:**
This is completely wrong for CoRL. It should go to NeurIPS, ICML, ICLR, ACL, or EMNLP. At CoRL it would be desk-rejected. I need to flag this as a critical issue, but I should still evaluate the idea quality for an appropriate ML interpretability venue like NeurIPS or ICML. Re-reading the instructions, the user is specifically asking about CoRL 2026, so I should note this mismatch prominently. For an appropriate venue, I'd estimate the novelty as weak-to-moderate—the hypothesis is somewhat intuitive, and while the multi-granularity comparison is methodologically novel, it's conceptually incremental. The significance is moderate; the actionability debate matters, but this feels more like a data point than a framework shift.

The related work coverage is extremely thorough, which is a strong point. At CoRL specifically, acceptance probability is essentially zero due to the venue mismatch. For the right venue, I'd estimate 20-30%—the direction is sound, the experimental design is solid, and the related work is comprehensive, but the conceptual foundation is thin and the results would likely be unsurprising.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e5b90be-fda3-4a37-87ec-63ca7dee792e",
  "isSidechain": false,
  "requestId": "req_011CbCdxB6yJSnCFHj8bzL2J",
  "type": "assistant",
  "uuid": "6629e8a3-e8d4-4299-a3f3-20b74fd97919",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgMt6tMhgLYBm3HNq8FBuV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 628,
      "cache_creation_input_tokens": 2088,
      "cache_read_input_tokens": 32037,
      "output_tokens": 6719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 628,
          "output_tokens": 6719,
          "cache_read_input_tokens": 32037,
          "cache_creation_input_tokens": 2088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2088
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

_source line 50 · 2026-05-19T21:31:10.794Z_

现在我已经有足够的调研信息来进行评估了。让我整理全部发现并输出评估报告。

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：投稿venue严重不匹配】

CoRL 2026（Conference on Robot Learning）的 Call for Papers 明确声明：
"Submissions should focus on a core robotics problem and demonstrate the relevance 
of proposed models, algorithms, datasets, and benchmarks to robotics."
"Submissions without a robotics focus will be returned without review."

本 proposal 研究的是 Process Reward Models 的机械可解释性干预，属于 NLP/ML 
interpretability 领域，与 robotics 完全无关。投稿 CoRL 将被 desk reject，
概率接近 100%。

建议目标 venue：NeurIPS 2026、ICML 2027、ICLR 2027、ACL 2026/2027、EMNLP 2026。

以下评估假设投稿至适配 venue（如 NeurIPS/ICML 级别的 ML interpretability track），
对 idea 质量进行客观评分。

───────────────────────────────────────────────

【领域调研】:

1. [Interpretability without Actionability (Basu et al., arXiv:2603.18353, Mar 2026)]:
   本 proposal 的核心出发点。该论文在 400 例临床分诊 vignettes 上测试了 4 种 
   mechanistic intervention（含 SAE steering、activation patching），发现即使 
   linear probes 达 98.2% AUROC，实际输出修正率极低（TSV steering 仅修正 24% 
   miss，SAE steering 修正接近 0）。揭示了 knowledge-action gap。论文真实存在，
   proposal 描述准确。

2. [SteerRM (arXiv:2603.12795, Mar 2026)]:
   使用预训练 LlamaScope SAEs 在 RM 上进行 training-free debiasing，RM-Bench 
   Hard split 平均提升 +7.3 points。局限于 Llama/Gemma 架构且仅有效覆盖 
   layers 0-9。Proposal 描述准确，且正确指出了 pretrained-vs-from-scratch SAE 
   的 methodological gap。

3. [CIRM / Shinoda et al. (arXiv:2604.27495, Apr 2026)]:
   neuron-level causal mediation intervention，用 Spearman 相关识别 bias 
   neurons，编辑 <2% neurons 即可在 general RMs 上匹配 70B 性能。Proposal 
   描述准确。

4. [Orgad et al. "Interpretability Can Be Actionable" (arXiv:2605.11161, ICML 2026 Position)]:
   提出 actionable interpretability 的 concreteness × validation 二维框架和
   评估标准（comparative utility, mechanistic faithfulness, generalization, 
   specificity）。注意：这是 Position Paper，不包含实证实验。Proposal 正确区分
   了 Orgad 的评估维度与自身的 Domain Amenability Hypothesis。

5. [Lee et al. "Rigorous Interpretation Is a Form of Evaluation" (arXiv:2605.05508, May 2026)]:
   提出 falsifiability/reproducibility/predictivity 三标准。Proposal 描述准确。

6. [Zhang et al. "Locate, Steer, Improve" Survey (arXiv:2601.14004, Jan 2026)]:
   最全面的 actionable MI 分类学，涵盖 localization 和 intervention 方法跨多个
   粒度（neuron, feature, head, circuit, layer, parameter）。关键发现：causal 
   methods 优于 magnitude-based；SAE features 支持单语义干预但昂贵；success 
   requires sparse/decomposable mechanisms。该 survey 识别了 localization → 
   practical steering 的 gap 但未做实证比较。

7. [Arad et al. "SAEs Are Good for Steering" (EMNLP 2025)]:
   区分 input features（仅在输入上激活）和 output features（因果影响输出），
   output-score filtering 带来 2-3× steering 改进。真实存在且描述准确。

8. [Tiwari et al. "Reward Under Attack" (arXiv:2603.06621)]:
   确立 PRMs 43% reward gains from stylistic exploitation。真实存在。

9. ["One Bias After Another" (arXiv:2603.03291)]:
   linear probes for mechanistic reward shaping across five RMs。真实存在。

- 调研总结：PRM debiasing 是 2026 年热点领域，已有 feature-level (SteerRM)、
  neuron-level (CIRM)、probe-level (One Bias After Another) 等多个独立工作，
  但确实没有工作在统一框架内跨粒度比较。"Domain Amenability" 作为显式概念未见
  先例，但其核心思想（constrained/verifiable domain → easier intervention）
  接近 common sense。本 proposal 试图填补 unified comparison 的 gap，
  但其概念贡献主要是实验组织框架而非新理论。

───────────────────────────────────────────────

【Trivial Alternative 检验】:

存在显著的 trivial alternative 威胁，分两个层面：

(1) 对 "Domain Amenability Hypothesis" 的 trivial alternative：
该假说的四个条件（well-defined output semantics, constrained output structure, 
verifiable ground truth, testable specificity）本质上等价于"任务越简单/越可形式
化/越可验证，干预越容易成功"。这接近一个 tautology：如果你能精确度量成功，你就更
可能证明自己成功了。审稿人很可能会认为这不需要跑实验就能 derive from first 
principles。更关键的是，proposal 的验证仅覆盖 N=2 domain（PRM 作为 positive 
case，Basu et al. 的 clinical LMs 作为 negative case，且后者不是作者自己跑
的），这远不足以 validate 一个 general hypothesis。

(2) 对 PRM debiasing 的 trivial alternative：
SteerRM 已经 +7.3 点，CIRM 已经 match 70B。在此基础上做 unified comparison 
的增量价值是什么？一个 trivial baseline 是：直接在 debiased data 上 fine-tune 
PRM（proposal 自己也提到这是 comparative utility baseline）。如果 fine-tuning 
on debiased data 达到类似效果，那整个 mechanistic intervention pipeline 的
实用价值被削弱。

增量价值：(a) 如果能证明不同粒度在不同评估维度上有可预测的优劣模式（H3），
这有一定方法论指导价值；(b) 如果 self-repair quantification 揭示了为什么某些
干预失败的 mechanistic 原因，这有科学价值。但这两个都是"如果"——属于实验层面
的不确定性，不改变 idea 内核的评估。

───────────────────────────────────────────────

【前提假设检验】:

核心逻辑链条中有以下未经验证的关键假设：

(1) **"PRMs satisfy all four domain amenability conditions" 是不是 post-hoc 
cherry-picking？**
作者选择 PRM 的理由本身就是它满足所有四个条件，然后预测干预会成功。这形成了
selection bias：如果你从一堆 domain 中挑出"看起来应该成功的"来跑实验，成功了
并不 surprising。失败了也只说明你的条件不够好。这个 hypothesis 在当前实验
设计下 unfalsifiable in a meaningful sense。

(2) **Basu et al. 的失败真的是因为 domain 不满足条件吗？**
Proposal 假设 clinical triage domain 的失败源于缺乏 verifiable ground truth、
unconstrained output、no orthogonal specificity test。但 Basu et al. 的失败
也可能源于：(a) model 规模不够大、(b) SAE 质量不够好、(c) intervention strength 
不对、(d) 评估 metric 选择不当。将失败归因于 "domain conditions" 是 proposal 
的假设，不是已证事实。这意味着即使 PRM 实验成功，也不能排除 confounders。

(3) **"Multi-method convergence = ground truth circuit"？**
Proposal 假设当两种 circuit tracing 方法（RelP + activation patching）收敛，
结果就可信。但两种方法可能共享系统性偏差（例如都对 attention heads 敏感而
对 MLP substructure 不敏感）。这在 MI 社区是公认的 open problem。

(4) **从 1.5B → 7B 的 circuit transferability：**
Proposal 在 1.5B 上做深度 circuit analysis（CLT attribution graphs），然后
将 findings 外推到 7B。但不同规模模型的 circuit structure 可能有质的不同
（superposition 程度不同），这个外推的 validity 未被讨论。

───────────────────────────────────────────────

【3 维度打分】:

1. Novelty: 弱-中 (介于弱和中之间)

理由：
- "Domain Amenability Hypothesis" 作为显式概念在我的搜索中未找到先例，有形式上
  的新颖性。但其实质内容（constrained + verifiable → easier intervention）
  接近 folk wisdom，概念增量有限。
- Multi-granularity unified comparison：Zhang et al. (2601.14004) 的 survey 
  已在分类学层面做了 feature/neuron/circuit 粒度的理论对比，本 proposal 补充
  的是实证比较。但"在同一 domain 上跑多个现有方法做 comparison"属于实验设计
  novelty，不属于 idea novelty。
- 方法论层面有少量 novelty：from-scratch SAE + Arad et al. output-score 
  filtering 应用于 PRM（改进 SteerRM）、pilot-then-target layer selection 
  （工程贡献）、将 Wang et al. 的 automated bias discovery 接入 contrastive 
  pair construction。但这些都是 incremental improvements on existing methods，
  不构成 new paradigm。
- 对比最直接的竞争工作：SteerRM 做了 feature-level，CIRM 做了 neuron-level，
  CRA 做了 from-scratch SAE training on PRMs。本 proposal 的核心是把这些都跑
  一遍然后比较。这更像 benchmark paper 而非 method paper。

2. Significance: 中

理由：
- 正面：Basu et al. vs. SteerRM/CIRM 的 actionability debate 是 2026 年 
  MI 社区的核心争论，非常 timely。Orgad et al. (ICML 2026) 和 Lee et al. 
  (2026) 分别从理论层面框架化了这个问题，但缺乏系统实证。本 proposal 如果
  执行良好，能提供有价值的实证 data point。
- 正面："什么时候 mechanistic interventions work" 这个问题本身很重要，
  对 MI 领域的研究方向选择有指导意义。
- 负面：但 proposal 的 evidence structure（N=2 domains, 其中 negative case 
  不是自己跑的）限制了 hypothesis 的 generalizability。一篇只在 PRM 上成功了
  的论文，能在多大程度上回答 "when do interventions succeed" 这个 general 
  question？审稿人可能认为这只是 "yet another PRM debiasing paper with 
  extra steps"。
- 结论：如果 reviewer 认可 framing，significance 是 strong；如果 reviewer 
  认为 framing 是 over-claim 而实质是 PRM debiasing comparison，
  significance 会降至 weak-moderate。这个分歧本身就限制了中稿概率。

3. Related Work: 强

理由：
- Related work 覆盖极为全面：核心竞争工作（SteerRM, CIRM, CRA, "One Bias After 
  Another"）、评估框架（Orgad et al., Lee et al.）、分类学（Zhang et al. 
  survey）、上游工具（Arad et al., Wang et al., RelP, CLT-Forge）、自修复 
  (McGrath et al.)、PRM bias 基准（Tiwari et al., PRM-BiasBench）全部覆盖。
- 所有我能验证的引用都真实存在且描述准确。
- 差异化定位清晰：明确了与 SteerRM（pretrained vs. from-scratch SAE）、
  CIRM（neuron vs. multi-granularity）、CRA（单一 SAE 分析 vs. 
  multi-method + intervention）的区别。
- 这是 proposal 最强的维度。

───────────────────────────────────────────────

【概率估计】: 18% - 28%，中位 22%

（注：此概率假设投稿至适配 venue 如 NeurIPS/ICML。投稿 CoRL 的接收概率 ≈ 0%。）

【估计理由】:

三维度综合：Related Work 强但这只是基本功不扣分；Significance 中（framing 
有争议性）；Novelty 弱-中（这是主要限制因素）。

核心瓶颈在于：这是一篇 "well-organized systematic empirical comparison" 而非 
"new idea" paper。Proposal 的精心程度极高（evaluation framework 引用得当、
实验设计周全、dual-outcome design、self-repair quantification），但这些都是
形式层面的完善。透过形式看本质：

**"如果核心发现是 positive（PRM 上 mechanistic interventions 成功了），
审稿人会说 surprising，还是 'I would have guessed this'？"**

答案偏向后者。SteerRM 和 CIRM 已经在 RMs 上成功了。在一个更 constrained 的 
PRM 设置上用更多方法再次成功，是 expected 的结果。Multi-granularity comparison 
的具体数字（谁高几个点）有参考价值，但不构成 surprising finding。

这将概率锚定在 25-35% 区间的下端。进一步考虑：
- Domain Amenability Hypothesis 的 N=2 测试 + 接近 tautology 的特性会被
  严格审稿人重点攻击，可能导致 reject
- "Primarily a comparison paper" 的定位在 top venue 偏弱
- 但 related work 和实验设计的完善度提供了 floor

综合估计中位 22%。

【主要风险】:

1. **"Domain Amenability Hypothesis" 被认为 near-tautological + under-tested 
   (N=2)**：审稿人很可能指出"说 constrained/verifiable domain 更容易 intervene 
   几乎是 self-evident"，且仅用一个 positive case（PRM）+ 一个非自己跑的 
   negative case（clinical LM）来 validate，evidence 严重不足。这是 idea 
   层面的核心风险，无法通过补实验完全解决（除非大幅增加 test domains，成本极高）。

2. **核心贡献被定位为 "systematic comparison" 而非 "new insight"**：审稿人可能
   认为"在同一 domain 上跑 SteerRM + CIRM + circuit ablation 然后比较"是
   有用的工程贡献但 novelty 不够 top venue。这类 "benchmark / comparison" 
   paper 在 NeurIPS/ICML 的接受门槛较高，除非 comparison 揭示了 surprising 
   patterns。
```

Sources:
- [Basu et al. - Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via SAEs (arXiv:2603.12795)](https://arxiv.org/abs/2603.12795)
- [CIRM - Shinoda et al. (arXiv:2604.27495)](https://arxiv.org/abs/2604.27495)
- [Orgad et al. - Interpretability Can Be Actionable (arXiv:2605.11161)](https://arxiv.org/abs/2605.11161)
- [Lee et al. - Rigorous Interpretation Is a Form of Evaluation (arXiv:2605.05508)](https://arxiv.org/abs/2605.05508)
- [Zhang et al. - Locate, Steer, Improve Survey (arXiv:2601.14004)](https://arxiv.org/abs/2601.14004)
- [Arad et al. - SAEs Are Good for Steering (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.519/)
- [Tiwari et al. - Reward Under Attack (arXiv:2603.06621)](https://arxiv.org/pdf/2603.06621)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6629e8a3-e8d4-4299-a3f3-20b74fd97919",
  "isSidechain": false,
  "requestId": "req_011CbCdxB6yJSnCFHj8bzL2J",
  "type": "assistant",
  "uuid": "2d7c54e7-2ee0-4e37-ab4b-d4937853dc86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UgMt6tMhgLYBm3HNq8FBuV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 628,
      "cache_creation_input_tokens": 2088,
      "cache_read_input_tokens": 32037,
      "output_tokens": 6719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 628,
          "output_tokens": 6719,
          "cache_read_input_tokens": 32037,
          "cache_creation_input_tokens": 2088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2088
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "2d7c54e7-2ee0-4e37-ab4b-d4937853dc86",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate PRM mechanistic intervention proposal",
  "sessionId": "d7a8159a-c9dc-4356-acf4-68101de0b562"
}
```

---
