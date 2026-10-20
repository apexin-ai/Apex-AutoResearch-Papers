# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # When Do Mechanistic Interventions

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf.jsonl`
- **Structured JSON:** [`8ea2971f22952daf86f5.json`](../../sessions/8e/8ea2971f22952daf86f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:27:32.816Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:27:32.816Z",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models\n\n## Description\nWhen do mechanistic interventions actually improve model behavior? We propose and test a Domain Amenability Hypothesis: mechanistic interventions succeed when applied to domains with well-defined output semantics, constrained output structure, verifiable ground truth, and independently testable specificity. Process Reward Models — producing binary step-level correctness judgments in verifiable mathematical reasoning, yet conflating fluency with correctness (43% of reward gains from stylistic exploitation) — represent an ideal testbed. We study two architecturally diverse 7B discriminative PRMs (Qwen2.5-Math and Math-Shepherd-Mistral) plus a 1.5B variant for deeper circuit analysis. We train SAEs from scratch on PRM activations — explicitly contrasting with SteerRM's pretrained base-model SAE approach — using a pilot-then-target layer selection strategy that reduces training cost by ~45% while enabling analysis across all informative layers. We apply multi-method causal circuit tracing (RelP and activation patching on 7B models, plus attribution graphs via CLTs on the 1.5B model) to produce a cross-validated circuit taxonomy. We then compare three core intervention granularities — feature-level (with output-score filtering per Arad et al.), neuron-level (CIRM-style), and circuit-level — plus two extension granularities, with streamlined self-repair quantification combining attribution-based survey and focused path patching. All interventions are assessed against both Orgad et al.'s (ICML 2026) evaluation criteria and Lee et al.'s (2026) scientific rigor criteria, producing a granularity-by-criterion matrix. By contrasting PRM results against Basu et al.'s clinical LM failures, this work provides the first structured empirical evidence for when mechanistic interventions succeed.\n\n## Core Problem\nThe mechanistic interpretability community faces a critical unresolved question: under what conditions do mechanistic interventions actually improve model behavior? 'Interpretability without Actionability' (Basu et al., March 2026) found that four mechanistic intervention methods — including SAE steering and activation patching — produced zero or negligible corrections on clinical triage LMs, revealing a persistent knowledge-action gap. Yet concurrent work shows successes: SteerRM achieves +7.3 points on RM-Bench via SAE feature suppression, and CIRM matches 70B RM performance by editing <2% of neurons. The field urgently needs a systematic empirical framework to determine WHEN mechanistic interventions succeed vs. fail, testing multiple intervention granularities within a single controlled domain. We propose a Domain Amenability Hypothesis: mechanistic interventions are more likely to succeed in domains with (a) well-defined output semantics, (b) constrained output structure, (c) verifiable ground truth, and (d) independently testable specificity. Process Reward Models — with their binary step-level reward structure, scalar output, constrained mathematical domain, and orthogonally measurable fluency vs. reasoning dimensions — represent an ideal testbed for this hypothesis, while simultaneously addressing the practical problem that PRMs conflate fluency with reasoning correctness (43% of reward gains from stylistic exploitation; Tiwari et al., 2026). This domain-conditions framing is our own contribution; we adopt Orgad et al.'s (ICML 2026) evaluation criteria (comparative utility, mechanistic faithfulness, generalization, specificity) and Lee et al.'s (2026) scientific rigor criteria (falsifiability, reproducibility, predictivity) as complementary assessment frameworks for our interventions, and situate our multi-granularity approach within the 'Locate, Steer, Improve' pipeline taxonomy (Zhang et al., 2026).\n\n## Opportunity\nThe interpretability-actionability debate (Basu et al. vs. SteerRM/CIRM successes) lacks a controlled empirical framework that simultaneously tests WHEN interventions succeed (domain conditions) and HOW intervention granularity affects success. Meanwhile, PRM debiasing spans multiple intervention granularities never compared within a unified framework: SteerRM (2026) performs correlational feature-level suppression using pretrained base-model SAEs; CIRM (Shinoda et al., ACL 2026) performs neuron-level causal mediation; 'One Bias After Another' (2026) uses linear probes for mechanistic reward shaping; CRA (2025) trains SAEs from scratch on PRM activations for backdoor correction. A key methodological gap exists in the SAE-based approach: SteerRM used pretrained LlamaScope SAEs trained on base-model activations, restricting effective analysis to layers 0-9 where reconstruction quality is adequate; CRA trained SAEs directly on PRM activations, enabling analysis across all layers. No work has systematically evaluated which approach is more effective for PRM debiasing. Furthermore, Wang et al. (2026) demonstrate automated evolutionary bias discovery in RMs, providing a principled upstream methodology for identifying which biases to target with mechanistic interventions — yet no work has connected automated bias discovery to mechanistic circuit tracing and intervention. No work has: (a) systematically compared feature-level, neuron-level, and circuit-level interventions within one experimental framework on PRMs, (b) performed multi-method causal circuit tracing on PRM internals with both RelP and attribution graphs, (c) explicitly tested a domain amenability hypothesis by contrasting a domain that satisfies all four conditions (PRMs) against documented failures in domains that lack them (clinical LMs), or (d) applied output-score-based feature filtering (Arad et al., EMNLP 2025) to improve SAE steering on reward models. The 'Locate, Steer, Improve' survey (Zhang et al., 2026) explicitly identifies the gap between localization and practical steering as the central unsolved problem in actionable MI; our multi-granularity comparison directly addresses this gap within a controlled domain.\n\n## Related Work / Landscape\nTHE ACTIONABILITY DEBATE: 'Interpretability without Actionability' (Basu et al., arXiv:2603.18353, March 2026) tested four mechanistic intervention methods on clinical triage LMs and found a persistent knowledge-action gap: SAE steering produced zero corrections, activation patching showed null net gain at standard strength. Orgad et al. (arXiv:2605.11161, ICML 2026) propose evaluating interpretability work along two dimensions — concreteness (how precisely an action is articulated) and validation (empirical support for the action's utility) — and identify evaluation criteria for output-modifying actions: comparative utility against standard baselines, mechanistic faithfulness, generalization across architectures, and specificity of targeted effects. Importantly, these dimensions characterize the interpretability research output itself, not domain properties; we adopt their evaluation criteria as our assessment framework while contributing our own Domain Amenability Hypothesis about which domain properties favor mechanistic intervention success. Lee et al. (arXiv:2605.05508, May 2026) argue interpretability can serve as rigorous evaluation when it satisfies three scientific criteria: falsifiability, reproducibility, and predictivity. They identify three failure modes for causal interpretability methods — non-specificity (interventions affect multiple behaviors), inconsistency (unreliable behavioral shifts across inputs), and underdetermination (multiple features appear to influence identical behaviors) — providing a complementary diagnostic framework to Orgad et al.'s criteria.\n\nACTIONABLE MI SURVEY: 'Locate, Steer, and Improve' (Zhang et al., arXiv:2601.14004, Jan 2026) provides the most comprehensive taxonomy of actionable MI, categorizing localization methods (magnitude analysis, causal attribution, gradient detection, probing, vocabulary projection, circuit discovery) and intervention methods (amplitude manipulation, targeted optimization, vector arithmetic) across multiple granularities (neuron, feature, head, circuit, layer, parameter). Key findings: causal methods outperform magnitude-based identification; SAE features enable monosemantic intervention but are expensive; polysemy limits neuron-level approaches; success requires sparse and decomposable mechanisms. Our work directly instantiates their 'locate-steer-improve' pipeline across multiple granularities in a controlled domain.\n\nPRM BIAS: Tiwari et al. (arXiv:2603.06621) established that PRMs function as fluency detectors with 43% of reward gains from stylistic exploitation, introducing PRM-BiasBench. 'Consistency Not Causality' (arXiv:2502.14619) shows RMs are insensitive to problem removal but sensitive to formatting. Wang et al. (arXiv:2602.15222, Feb 2026) present an automated evolutionary pipeline for discovering RM biases — using LLM-based iterative proposal and refinement of candidate biases, validated through counterfactual pairs. They found 10 statistically significant biases in Skywork-V2-8B including preferences for redundant spacing and hallucinated content, and note their discovered biases 'present concrete targets for mechanistic interpretability research.' Their methodology complements our contrastive pair construction by providing a principled upstream bias discovery phase.\n\nINTERVENTION GRANULARITIES AND SAE METHODOLOGY: (1) Feature-level: SteerRM (arXiv:2603.12795, March 2026) uses pretrained LlamaScope SAEs (32× expansion, trained on Llama-3.1-8B-Base activations) applied to RM hidden states, with contrastive feature identification via a strength-stability criterion. Critically, they restricted analysis to layers 0-9 because reconstruction quality degrades sharply beyond this range — with MSE increasing by orders of magnitude — reflecting distributional mismatch between base-model SAE training data and RM-specific activations. This is not an inherent SAE limitation but a pretrained-vs-fine-tuned domain gap. Their approach is training-free but limited to architectures with available pretrained SAEs (Llama, Gemma). In contrast, CRA (arXiv:2508.04216) trains SAEs from scratch on PRM activations (8× expansion, 8× V100 GPUs) across all layers of Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B, achieving usable reconstruction at all layers since SAEs are matched to the actual PRM activation distribution. Our approach follows CRA's from-scratch methodology, which is more principled for PRMs but costlier than pretrained SAEs. Arad et al. (arXiv:2505.20063, EMNLP 2025) demonstrate that feature selection quality critically determines steering effectiveness: distinguishing 'output features' (which causally affect model outputs) from 'input features' (which merely activate on relevant inputs) yields 2-3× improvement, suggesting SteerRM's activation-difference features may be suboptimal without output-score validation. (2) Neuron-level: CIRM (Shinoda et al., arXiv:2604.27495, ACL 2026) uses Spearman correlation for bias-specific neuron identification with Pearl's causal mediation analysis — edits <2% of neurons in 2 general RMs to match 70B performance, finds bias signals primarily in early layers. Selection is correlation-based on polysemantic neurons without SAE decomposition. (3) Probe-level: 'One Bias After Another' (arXiv:2603.03291, Feb 2026) uses linear activation probes for mechanistic reward shaping across five RMs. (4) Training-time approaches: Factored CRL (arXiv:2601.21350, ICML 2026) separates causal/non-causal reward factors via adversarial gradient reversal; Robust Reward Modeling (Lu et al., arXiv:2604.13833, April 2026) performs causal decomposition via decoder-based intent reconstruction — these complement our inference-time mechanistic approach.\n\nSPARSE REWARD CIRCUITRY: Xu et al. (arXiv:2602.00986, Feb 2026) identify a sparse reward subsystem in LLMs containing 'value neurons' (predicting state value) and 'dopamine neurons' (encoding step-level TD errors), with zeroing top 1% of value neurons causing catastrophic -54.9% accuracy degradation vs. -0.6% for random neurons. Their L1-norm probe pruning provides an efficient neuron identification methodology to compare against CIRM's Spearman correlation.\n\nSAE-ON-RM WORK: CRA (arXiv:2508.04216) trains SAEs on PRM activations for backdoor correction. SARM (arXiv:2508.08746, AAAI 2026 Oral) integrates SAEs for interpretable reward decomposition. Activation monitoring (arXiv:2603.04069) uses SAEs on residual streams for hacking detection. SAFER (arXiv:2507.00665) applies SAEs to probe safety-relevant features in RMs.\n\nCIRCUIT ANALYSIS TOOLS: Attribution graphs (Lindsey et al., Anthropic 2025) combine cross-layer transcoders with backward Jacobian tracing. RelP (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight) provides faithful gradient-based circuit discovery requiring only 2 forward passes + 1 backward pass — achieving Pearson r=0.956 vs. r=0.006 for attribution patching on GPT-2 Large MLPs, validated on models up to Qwen2-7B. CLT-Forge (arXiv:2603.21014) provides open-source CLT infrastructure up to ~1B scale.\n\nSELF-REPAIR: McGrath et al. (ICML 2024) showed self-repair varies significantly across prompts and involves LayerNorm scaling (~30% of measured self-repair), with sparse neuron sets in final MLP layers performing anti-erasure. They recommend path patching over full-component ablation and LayerNorm freezing during ablations.\n\nGENERATIVE PRM LANDSCAPE: ThinkPRM (arXiv:2504.16828, TMLR 2026) and GenPRM (arXiv:2504.00891, AAAI 2026) demonstrate generative PRMs outperform discriminative PRMs on accuracy with far less training data. However, discriminative PRMs remain widely deployed due to lower inference cost and deployment simplicity. Understanding failure modes of discriminative systems has independent value.\n\n## Approach\nWe conduct the first systematic empirical test of when mechanistic interventions succeed, using Process Reward Models as a controlled domain that we argue satisfies all four conditions of our Domain Amenability Hypothesis: (a) well-defined output semantics (binary step-level correctness judgments), (b) constrained output structure (scalar reward scores), (c) verifiable ground truth (mathematically checkable reasoning), and (d) independently testable specificity (fluency bias measurable separately from reasoning accuracy on orthogonal benchmarks). We contrast this with the clinical triage domain where Basu et al. found failure — which lacks verifiable ground truth, has unconstrained output structure, and has no orthogonal specificity test. We study two architecturally diverse 7B discriminative PRMs — Qwen2.5-Math-PRM-7B (Qwen2.5-Math base) and Math-Shepherd-Mistral-7B-PRM (Mistral-7B base) — plus Skywork-o1-Open-PRM-Qwen-2.5-1.5B for deeper mechanistic analysis, systematically comparing three core intervention granularities (feature-level, neuron-level, circuit-level) across all models and two extension granularities (layer-level, hybrid) on the single most informative PRM.\n\n**Phase 1: Pilot-Guided SAE Training with Output-Score Filtering.**\n\n*SAE methodology: from-scratch on PRM activations.* A critical methodological choice distinguishes our approach from SteerRM. SteerRM used pretrained LlamaScope SAEs (trained on Llama-3.1-8B-Base activations) applied to RM hidden states, restricting effective analysis to layers 0-9 where reconstruction quality remains adequate — beyond which MSE increases by orders of magnitude due to distributional mismatch between base-model and reward-model activations. We instead follow CRA's precedent of training SAEs from scratch on PRM-specific activations, using 8× expansion factor via SAELens. This is more principled: PRM activation distributions differ substantially from base LMs, particularly in later layers where reward-specific representations are learned. CRA validated this approach on Math-Shepherd-PRM-7B and Qwen2.5-Math-PRM-7B using 8× V100 GPUs. The trade-off is compute cost versus analysis coverage: pretrained SAEs are free but architecture-restricted and layer-limited; from-scratch SAEs cost ~2-4 A100-days per PRM but enable analysis across all layers.\n\n*Pilot-then-target layer selection.* To avoid training SAEs wastefully on all ~28-32 layers of 7B PRMs, we adopt a pilot-then-target strategy: (a) Train SAEs on all 28 layers of the 1.5B PRM (cheap: ~15 H100-hours total at 8× expansion). (b) Analyze which layer ranges concentrate fluency-encoding vs. reasoning-encoding features by computing per-layer output-score distributions (Arad et al.'s filtering). (c) Identify a key layer range (we hypothesize layers 0-16 based on CIRM's early-layer bias finding and the reward-head gradient flow pattern). (d) Train SAEs only on the identified layer range for 2×7B PRMs, plus every 4th layer outside this range as a coverage check. This reduces per-PRM SAE training from ~30 SAEs to ~16, cutting SAE training compute by ~45%.\n\n*Feature identification with output-score filtering.* Use contrastive input pairs (fluent-but-wrong vs. disfluent-but-correct reasoning steps, sourced from PRM-BiasBench and augmented with Wang et al.'s automated evolutionary bias discovery pipeline to identify novel bias targets) to identify candidate fluency-associated and reasoning-associated features via activation difference analysis. Critically, apply Arad et al.'s output-score filtering: for each candidate feature, compute its output score (causal effect on model output via single forward pass with high steering factor on a neutral prompt). Retain only features with high output scores (≥0.1 threshold), filtering out features that merely detect fluency cues but don't causally influence reward scores.\n\n**Phase 2: Multi-Method Causal Circuit Tracing.**\n\nTier A (both 7B PRMs — budget: 60 H100-hours): (a) Relevance Patching (RelP) for efficient, faithful gradient-based circuit discovery across all components simultaneously — requiring only 2 forward + 1 backward pass per sample, validated on Qwen2-7B with Pearson r=0.956 faithfulness (~15h across 2 PRMs on 1000+ contrastive samples). (b) Activation patching at every attention head and MLP layer with contrastive pairs to measure causal effect on step-level reward scores, providing cross-validation of RelP findings (~45h across 2 PRMs).\n\nTier B (1.5B PRM — budget: 35 H100-hours): Attribution graphs using cross-layer transcoders via CLT-Forge on Skywork-o1-Open-PRM-Qwen-2.5-1.5B, at the demonstrated-feasible scale for CLT training. This produces complete feature-level circuit maps for representative examples.\n\n**Concrete CLT fallback:** If CLT training on the 1.5B PRM exceeds 45 H100-hours or reconstruction loss exceeds 2× the per-layer SAE baseline, we fall back to Tier A methods only (RelP + activation patching on both 7B PRMs), which constitute two independent causal methods sufficient for cross-validation.\n\nComponents are classified as fluency-encoding, reasoning-encoding, or mixed only when at least two methods converge.\n\n**Phase 2b: Streamlined Self-Repair Quantification.** We quantify self-repair following McGrath et al. (ICML 2024) in two stages:\n\n(a) *Attribution-based survey* (cheap: ~5 H100-hours). Use RelP-derived attribution scores to approximate self-repair ratios SR(C) = (|DE(C)| - |TE(C)|) / |DE(C)| for all identified fluency-encoding components across N≥500 test examples, where DE(C) = direct effect and TE(C) = total effect. This provides distributional estimates (median, IQR, 5th/95th percentiles) of self-repair across all components.\n\n(b) *Focused path patching* (targeted: ~15 H100-hours). For the top-10 components with highest estimated SR from stage (a), perform exhaustive path patching with LayerNorm freezing on N≥200 examples per component. Decompose self-repair into downstream attention compensation (ΣΔ DE_h), downstream MLP compensation (ΣΔ DE_m), and LayerNorm scaling (ΔDE_LN). Compare single-site vs. multi-site ablation to test H4.\n\n**Phase 3: Multi-Granularity Intervention Comparison.** Three CORE granularities and two EXTENSION granularities:\n\n**Core granularities (all 3 PRMs × 3 core benchmarks):**\n(i) Feature-level: SAE feature suppression on output-score-filtered bias features (our improved SteerRM-style approach with from-scratch SAEs + Arad et al. filtering);\n(ii) Neuron-level: CIRM-style correlation-based neuron identification with causal mediation (median replacement), adapted to PRMs — comparing Spearman correlation selection against Xu et al.'s L1-norm probe pruning as alternative identification methods;\n(iii) Circuit-level: targeted ablation/dampening of causally-validated fluency circuits while preserving reasoning circuits, using path patching for precise intervention.\n\n**Extension granularities (single most informative PRM × 3 core benchmarks):**\n(iv) Layer-level: blanket dampening of layers classified as predominantly fluency-encoding — the coarsest intervention, serving as a lower bound;\n(v) Hybrid: circuit-informed feature suppression restricting feature-level interventions to causally-validated output-score-filtered features within identified fluency circuits — the finest-grained intervention, serving as an upper bound.\n\nWe benchmark core interventions on three core benchmarks: ProcessBench (core error detection), PRM-BiasBench (bias-specific evaluation), and RM-Bench Hard split (style-invariant adversarial evaluation). PRMBench and Socratic-PRMBench serve as extension benchmarks evaluated on the single most informative PRM across all five granularities, providing fine-grained diagnostic depth without expanding the core matrix.\n\n**Phase 4: Actionability Assessment.** We evaluate each intervention against two complementary frameworks:\n\n*Orgad et al.'s criteria* — (1) Comparative utility: does each intervention outperform simple baselines (fine-tuning on debiased data, prompt-based re-ranking, random component ablation)? (2) Mechanistic faithfulness: do interventions on identified components produce predicted changes? (3) Generalization: do findings hold across our two architecturally diverse 7B PRMs? (4) Specificity: do interventions affect only targeted bias, or cause broad side effects?\n\n*Lee et al.'s scientific rigor criteria* — (1) Falsifiability: are our mechanistic claims testable and potentially disprovable? (2) Reproducibility: are intervention effects consistent across similar inputs? (3) Predictivity: can our circuit taxonomy predict intervention outcomes on held-out examples? We explicitly test Lee et al.'s three failure modes — non-specificity, inconsistency, and underdetermination — as diagnostic checks on our findings.\n\nThis produces a granularity-by-criterion matrix that, combined with our Domain Amenability Hypothesis and the contrast with Basu et al.'s clinical LM failures, provides the first structured empirical evidence for WHEN mechanistic interventions succeed.\n\n**Domain Amenability Hypothesis — Testing and Contrast.** We argue PRMs satisfy all four domain amenability conditions, in stark contrast to clinical triage LMs: (1) Well-defined output semantics: PRM rewards are binary step-level judgments vs. open-ended clinical assessments; (2) Constrained output structure: scalar reward score vs. unconstrained text; (3) Verifiable ground truth: mathematically checkable reasoning vs. subjective triage correctness; (4) Testable specificity: fluency bias reduction measurable independently from reasoning accuracy on orthogonal benchmarks vs. entangled clinical dimensions. If our interventions succeed (>3% improvement on at least one benchmark), this provides positive evidence for the hypothesis; if they fail despite the favorable domain conditions, this significantly strengthens the case that mechanistic intervention is fundamentally limited.\n\n**Revised Hypotheses.** H1 (Domain Amenability): PRM mechanistic interventions will show statistically significant improvements (>3% on at least one benchmark), providing positive evidence for our Domain Amenability Hypothesis — in contrast to Basu et al.'s clinical LM null result. H2 (Circuit Structure): Multi-method causal tracing will identify separable fluency-reasoning circuit structure in PRMs, with convergence across at least two analysis methods, corroborating CIRM's early-layer bias encoding and Xu et al.'s sparse reward subsystem findings. H3 (Granularity-Dependent Effectiveness): Among the three core intervention granularities, effectiveness will vary by evaluation context — circuit-informed approaches will outperform on adversarially-constructed bias probes (PRM-BiasBench), while feature-level may suffice for naturally-distributed errors (ProcessBench). H4 (Self-Repair): Self-repair (estimated via attribution-based SR ratio) will partially attenuate single-site interventions (median SR > 0.3), but multi-site simultaneous intervention will yield TE_multi > Σ TE_single, demonstrating that coordinated ablation disrupts self-repair pathways.\n\n## Inspiration\nPrimary question: The actionability debate (Basu et al. vs. SteerRM/CIRM successes) — PRMs as the ideal controlled testbed via our Domain Amenability Hypothesis; Evaluation frameworks: Orgad et al.'s criteria (comparative utility, mechanistic faithfulness, generalization, specificity) + Lee et al.'s scientific rigor criteria (falsifiability, reproducibility, predictivity); Taxonomic framework: 'Locate, Steer, Improve' survey's locate-steer-improve pipeline; SAE methodology: CRA's from-scratch PRM SAE training (contrasted with SteerRM's pretrained LlamaScope approach) + Arad et al.'s output-score filtering; Circuit tracing: RelP for efficient faithful circuit discovery + CLT-Forge for attribution graphs; Neuron identification: CIRM's causal mediation + Xu et al.'s L1-norm probe pruning; Bias discovery: Wang et al.'s automated evolutionary bias discovery for contrastive pair construction; Self-repair methodology: McGrath et al.'s path patching and LayerNorm freezing\n\n## Key References\n- Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations (Basu et al., arXiv:2603.18353, 2026)\n- Position: Interpretability Can Be Actionable (Orgad et al., arXiv:2605.11161, ICML 2026)\n- Rigorous Interpretation Is a Form of Evaluation (Lee et al., arXiv:2605.05508, May 2026)\n- Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models (Zhang et al., arXiv:2601.14004, 2026)\n- SAEs Are Good for Steering — If You Select the Right Features (Arad et al., arXiv:2505.20063, EMNLP 2025)\n- Automatically Finding Reward Model Biases (Wang et al., arXiv:2602.15222, Feb 2026)\n- Sparse Reward Subsystem in Large Language Models (Xu et al., arXiv:2602.00986, 2026)\n- Robust Reward Modeling for Large Language Models via Causal Decomposition (Lu et al., arXiv:2604.13833, 2026)\n- Explorations of Self-Repair in Language Models (McGrath et al., ICML 2024)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (Tiwari et al., arXiv:2603.06621, 2026)\n- Debiasing Reward Models via Causally Motivated Inference-Time Intervention (Shinoda et al., arXiv:2604.27495, ACL 2026)\n- SteerRM: Debiasing Reward Models via Sparse Autoencoders (arXiv:2603.12795, 2026)\n- One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models (arXiv:2603.03291, 2026)\n- Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction (arXiv:2508.04216, 2025)\n- Interpretable Reward Model via Sparse Autoencoder (arXiv:2508.08746, AAAI 2026 Oral)\n- Monitoring Emergent Reward Hacking During Generation via Internal Activations (arXiv:2603.04069, 2026)\n- Reward Models Identify Consistency, Not Causality (arXiv:2502.14619, 2025)\n- CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models (arXiv:2507.15698, 2025)\n- RM-Bench: Benchmarking Reward Models of Language Models with Subtlety and Style (ICLR 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF (arXiv:2601.21350, ICML 2026)\n- SAFER: Probing Safety in Reward Models with Sparse Autoencoder (arXiv:2507.00665, 2025)\n- Circuit Tracing: Revealing Computational Graphs in Language Models (Lindsey et al., Anthropic, 2025)\n- RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching (arXiv:2508.21258, NeurIPS 2025 MechInterp Workshop Spotlight)\n- CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs (arXiv:2603.21014, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns (arXiv:2505.23474, 2025)\n- Process Reward Models That Think (ThinkPRM, arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Towards Best Practices of Activation Patching in Language Models: Metrics and Methods (Goldowsky-Dill et al., arXiv:2309.16042, 2023)\n- Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups (arXiv:2410.21508, 2024)\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '280 H100-hours (Phase 1 — pilot SAE on 1.5B: 15h, targeted SAE training on 2×7B: 50h, output-score filtering: 5h; Phase 2 — Tier A RelP + activation patching on 2×7B: 60h, Tier B CLT on 1.5B: 35h; Phase 2b — attribution-based self-repair survey: 5h, focused path patching: 15h; Phase 3 — core interventions 3×3×3: 35h, extension interventions 2×1×3 + 5×1×2: 15h; baselines + CIRM adaptation: 30h; buffer: 15h)', 'timeline': '12 weeks (Phase 1: dataset construction + Wang et al. bias discovery + pilot SAE + targeted SAE training 3w; Phase 2: circuit tracing Tier A + Tier B in parallel 3w; Phase 2b + Phase 3: self-repair + interventions 3w; Phase 4: actionability analysis + extension benchmarks + writing 3w — with 1w overlap from parallelization)', 'estimated_gpu_cost': '$560 (at $2.00/H100-hr on-demand)'}\n- **human_in_loop**: {'gpu_hours': '250 H100-hours (automated experiment scripting reduces overhead; Claude generates CIRM adaptation + output-score filtering pipeline)', 'timeline': '10 weeks (Claude generates contrastive datasets integrating Wang et al. pipeline, automates multi-method tracing, adapts CIRM to PRM setting, implements self-repair protocol, drafts analysis)', 'claude_api_cost': '$380 (dataset generation ~$80, experiment code + CIRM adaptation + output-score pipeline ~$110, analysis + self-repair ~$70, actionability framework ~$60, paper drafting ~$60)', 'estimated_gpu_cost': '$500'}\n- **auto_research**: {'gpu_hours': '330 H100-hours (additional exploratory runs, automated hyperparameter sweeps for SAE training and output-score thresholds, broader self-repair analysis)', 'timeline': '8 weeks (aggressive parallelization across 3 PRMs; automated multi-method tracing; continuous experiment design loop)', 'claude_api_cost': '$800 (continuous experiment design, automated cross-validation, CIRM reproduction + adaptation, iterative paper refinement)', 'estimated_gpu_cost': '$660', 'speed_bottleneck': 'Sequential dependency: pilot SAE training (1.5B) must complete before targeted layer selection for 7B SAE training. However: Tier A (7B) and Tier B (1.5B) circuit tracing run in parallel once SAEs are ready, and the 3-core-granularity comparison parallelizes across PRMs.'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:27:32.819Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:27:32.819Z",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

## Round 1

48 recorded events

### User

_source line 3 · 2026-05-19T21:27:32.832Z_

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
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "8e48d7e0-e09a-438d-aa7d-5c38db9d2980",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:27:32.831Z_

```json
{
  "parentUuid": "8e48d7e0-e09a-438d-aa7d-5c38db9d2980",
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
  "uuid": "d893609f-029b-4b32-8b6a-7f1f576edf17",
  "timestamp": "2026-05-19T21:27:32.831Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:27:32.831Z_

```json
{
  "parentUuid": "d893609f-029b-4b32-8b6a-7f1f576edf17",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9ba52694-4041-4870-9042-57e5b2ab9588",
  "timestamp": "2026-05-19T21:27:32.831Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
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
  "leafUuid": "9ba52694-4041-4870-9042-57e5b2ab9588",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:27:49.225Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Let me first carefully read through the proposal, then conduct web searches to understand the current landscape before providing my assessment.

Wait - this is for CoRL 2026 (Conference on Robot Learning), but the proposal is about mechanistic interpretability of Process Reward Models (PRMs) in mathematical reasoning. This seems like a mismatch - CoRL is about robot learning, not NLP/interpretability. Let me re-read...

Actually, the user said "CoRL 2026 主会" - Conference on Robot Learning. 

There's a fundamental mismatch here: the proposal focuses entirely on mechanistic interpretability, sparse autoencoders, and process reward models for mathematical reasoning—all squarely in the NLP/ML interpretability domain—but CoRL is a robotics conference. This is a major red flag that either the venue is wrong or there's been some confusion about the submission target.

Let me set aside the venue concern for now and focus on evaluating the idea quality as instructed, though I should flag this discrepancy. Before diving into the evaluation, I need to search for the foundational papers and prior work—particularly the "Interpretability without Actionability" paper that motivates this proposal, and the existing work on process reward models and interpretability methods that this builds on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ba52694-4041-4870-9042-57e5b2ab9588",
  "isSidechain": false,
  "requestId": "req_011CbCdsA4pioNL44eMp6TRH",
  "type": "assistant",
  "uuid": "1f04c37f-833d-4004-b994-fb7888b9f9d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6uKRR88yZPPvm63DsoxiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 701,
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
          "output_tokens": 701,
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

_source line 9 · 2026-05-19T21:27:49.714Z_

I need to conduct thorough literature searches before evaluating this proposal. Let me first load the WebSearch tool, then run multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f04c37f-833d-4004-b994-fb7888b9f9d2",
  "isSidechain": false,
  "requestId": "req_011CbCdsA4pioNL44eMp6TRH",
  "type": "assistant",
  "uuid": "fc0a1f5a-d63c-4df8-aa23-2af7aad8f70c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6uKRR88yZPPvm63DsoxiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 701,
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
          "output_tokens": 701,
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

_source line 10 · 2026-05-19T21:27:49.719Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019CYTqo64FPGWpFEF3Gq34F`</summary>

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
  "parentUuid": "fc0a1f5a-d63c-4df8-aa23-2af7aad8f70c",
  "isSidechain": false,
  "requestId": "req_011CbCdsA4pioNL44eMp6TRH",
  "type": "assistant",
  "uuid": "b62c1978-7614-4e21-9dc2-76426964e923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X6uKRR88yZPPvm63DsoxiJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 13985,
      "output_tokens": 701,
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
          "output_tokens": 701,
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

_source line 11 · 2026-05-19T21:27:49.725Z_

<details><summary>↩ Tool result · `toolu_019CYTqo64FPGWpFEF3Gq34F`</summary>

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
  "parentUuid": "b62c1978-7614-4e21-9dc2-76426964e923",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "741bb596-52ba-414b-80a7-55d50564b4d5",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "b62c1978-7614-4e21-9dc2-76426964e923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:27:52.838Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me run multiple targeted searches to understand the landscape. I'll search for the key papers and concepts mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741bb596-52ba-414b-80a7-55d50564b4d5",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "13353b8e-7066-49fa-9a72-0cbb7b8bec29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 13 · 2026-05-19T21:27:52.840Z_

Now let me run multiple targeted searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13353b8e-7066-49fa-9a72-0cbb7b8bec29",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "4c76bfd1-ca3d-4ec1-a650-c2bf34fc8855",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 14 · 2026-05-19T21:27:53.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011JSum6KxgF8imjkZyV6pVg`</summary>

```json
{
  "query": "Basu et al. \"Interpretability without Actionability\" mechanistic interventions clinical LM 2026 arXiv:2603.18353"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c76bfd1-ca3d-4ec1-a650-c2bf34fc8855",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "5beb8fc6-7120-418b-b0a4-858d9c93ce2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 15 · 2026-05-19T21:27:54.280Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QmQJVXucN9na991tkF7uZS`</summary>

```json
{
  "query": "SteerRM debiasing reward models sparse autoencoders SAE 2026 arXiv:2603.12795"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5beb8fc6-7120-418b-b0a4-858d9c93ce2d",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "a588018c-e15d-40f6-93a7-ce732dd22da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 16 · 2026-05-19T21:27:55.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DAH5HVMfSJjyjvypq3ivQg`</summary>

```json
{
  "query": "CIRM Shinoda causal inference reward model debiasing neuron-level ACL 2026 arXiv:2604.27495"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a588018c-e15d-40f6-93a7-ce732dd22da4",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "de90f077-a697-46d2-842a-89f96953849c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 17 · 2026-05-19T21:27:55.705Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FxpTYVpdvx1EH4coFgufkb`</summary>

```json
{
  "query": "mechanistic interpretability reward models process reward models PRM 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de90f077-a697-46d2-842a-89f96953849c",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "7e8c8f73-da9f-4e82-8f2f-0b35e0e5e8c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 18 · 2026-05-19T21:27:56.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KiWcoQ1Jh5QkrEeBxrYzLu`</summary>

```json
{
  "query": "Orgad et al. \"Interpretability Can Be Actionable\" ICML 2026 arXiv:2605.11161"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8c8f73-da9f-4e82-8f2f-0b35e0e5e8c2",
  "isSidechain": false,
  "requestId": "req_011CbCdtQqrFrkndS9aFvxGT",
  "type": "assistant",
  "uuid": "ffc62e63-b5c8-4e21-903f-d7c4c997102f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPYeFT5ViChmSG8ah1GR7x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 23707,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 23707,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1227
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

_source line 19 · 2026-05-19T21:28:00.164Z_

<details><summary>↩ Tool result · `toolu_01DAH5HVMfSJjyjvypq3ivQg`</summary>

```text
Web search results for query: "CIRM Shinoda causal inference reward model debiasing neuron-level ACL 2026 arXiv:2604.27495"

Links: [{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/pdf/2601.21350"},{"title":"How causal inference tools can support debiasing of machine learning models for meaningful brain-based predictions","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314055.full.pdf"},{"title":"Neural spiking for causal inference","url":"https://www.biorxiv.org/content/10.1101/253351.full.pdf"},{"title":"Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment","url":"https://arxiv.org/pdf/2501.09620"},{"title":"CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models","url":"https://arxiv.org/pdf/2507.15698"}]

I found the paper! Here's what I found:

The paper presents CIRM (Causally Motivated Inference-time Reward Model debiasing), which works by: (a) computing activations of neurons in reward models and identifying bias-specific neurons on a validation set, and (b) at inference time, replacing the activations of identified bias-specific neurons with their medians to debias rewards across five types of biases.

The research addresses the problem that reward models suffer from biases, with the most famous being length bias where reward models tend to assign higher scores to longer responses regardless of actual helpfulness.

The paper is available on arXiv (2604.27495) and appears to be forthcoming at ACL 2026. The work takes a neuron-level causal inference approach to debiasing reward models through inference-time intervention.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de90f077-a697-46d2-842a-89f96953849c",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "eca3c466-abd5-4062-b26e-92690acbd95c",
  "toolUseResult": {
    "query": "CIRM Shinoda causal inference reward model debiasing neuron-level ACL 2026 arXiv:2604.27495",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L9BxH23jMLrVJ2DVwx3S1G",
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
            "title": "How causal inference tools can support debiasing of machine learning models for meaningful brain-based predictions",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.20.24314055.full.pdf"
          },
          {
            "title": "Neural spiking for causal inference",
            "url": "https://www.biorxiv.org/content/10.1101/253351.full.pdf"
          },
          {
            "title": "Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment",
            "url": "https://arxiv.org/pdf/2501.09620"
          },
          {
            "title": "CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models",
            "url": "https://arxiv.org/pdf/2507.15698"
          }
        ]
      },
      "I found the paper! Here's what I found:\n\nThe paper presents CIRM (Causally Motivated Inference-time Reward Model debiasing), which works by: (a) computing activations of neurons in reward models and identifying bias-specific neurons on a validation set, and (b) at inference time, replacing the activations of identified bias-specific neurons with their medians to debias rewards across five types of biases.\n\nThe research addresses the problem that reward models suffer from biases, with the most famous being length bias where reward models tend to assign higher scores to longer responses regardless of actual helpfulness.\n\nThe paper is available on arXiv (2604.27495) and appears to be forthcoming at ACL 2026. The work takes a neuron-level causal inference approach to debiasing reward models through inference-time intervention."
    ],
    "durationSeconds": 4.957362775999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "de90f077-a697-46d2-842a-89f96953849c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T21:28:02.085Z_

<details><summary>↩ Tool result · `toolu_01FxpTYVpdvx1EH4coFgufkb`</summary>

```text
Web search results for query: "mechanistic interpretability reward models process reward models PRM 2026 survey"

Links: [{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"Process Reward Model with Q-value Rankings | OpenReview","url":"https://openreview.net/forum?id=wQEdh2cgEk"},{"title":"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026","url":"https://dl.acm.org/doi/10.1145/3774904.3792551"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Interpretable Reward Modeling with Active Concept Bottlenecks","url":"https://arxiv.org/pdf/2507.04695"}]

Based on the search results, I found relevant information about process reward models and recent developments in this area:

## Process Reward Models Survey

A recent survey comparing different forms of reward acquisition—including rule-based rewards, outcome reward models (ORMs), and process reward models (PRMs)—uses a six-aspect evaluation scheme covering resource efficiency, granularity, anti-hacking robustness, generalization, interpretability, and functionality.

### Key Characteristics of PRMs

PRMs are more costly than ORMs because ORMs only label the final outcome, whereas PRMs require correctness labels for every intermediate step. However, PRMs offer increased interpretability, improved credit assignment, and more precise alignment with domain-specific objectives compared to outcome reward models.

### Recent Developments (2025-2026)

The search results reveal several advances in mechanistic interpretability and PRM approaches:

- PathFinder-PRM leverages explicit error categorization (e.g., math vs. consistency) before reward computation, yielding enhanced interpretability and sample efficiency.

- AgentPRM is a re-defined PRM for agent tasks that captures both the interdependence between sequential decisions and their contribution to the final goal.

- An approach based on the Concept Bottleneck Model paradigm actively queries human feedback for annotations of interpretable latent dimensions to uncover underlying concepts influencing decisions, enhancing transparency of reward models while ensuring alignment with human values.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e8c8f73-da9f-4e82-8f2f-0b35e0e5e8c2",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "7e8739b3-6936-4ffd-aa08-91e57e8967d9",
  "toolUseResult": {
    "query": "mechanistic interpretability reward models process reward models PRM 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_013b7adanraoDRiSGiy7o4kz",
        "content": [
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process",
            "url": "https://arxiv.org/pdf/2510.08049"
          },
          {
            "title": "Process Reward Model with Q-value Rankings | OpenReview",
            "url": "https://openreview.net/forum?id=wQEdh2cgEk"
          },
          {
            "title": "AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress | Proceedings of the ACM Web Conference 2026",
            "url": "https://dl.acm.org/doi/10.1145/3774904.3792551"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "Interpretable Reward Modeling with Active Concept Bottlenecks",
            "url": "https://arxiv.org/pdf/2507.04695"
          }
        ]
      },
      "Based on the search results, I found relevant information about process reward models and recent developments in this area:\n\n## Process Reward Models Survey\n\nA recent survey comparing different forms of reward acquisition—including rule-based rewards, outcome reward models (ORMs), and process reward models (PRMs)—uses a six-aspect evaluation scheme covering resource efficiency, granularity, anti-hacking robustness, generalization, interpretability, and functionality.\n\n### Key Characteristics of PRMs\n\nPRMs are more costly than ORMs because ORMs only label the final outcome, whereas PRMs require correctness labels for every intermediate step. However, PRMs offer increased interpretability, improved credit assignment, and more precise alignment with domain-specific objectives compared to outcome reward models.\n\n### Recent Developments (2025-2026)\n\nThe search results reveal several advances in mechanistic interpretability and PRM approaches:\n\n- PathFinder-PRM leverages explicit error categorization (e.g., math vs. consistency) before reward computation, yielding enhanced interpretability and sample efficiency.\n\n- AgentPRM is a re-defined PRM for agent tasks that captures both the interdependence between sequential decisions and their contribution to the final goal.\n\n- An approach based on the Concept Bottleneck Model paradigm actively queries human feedback for annotations of interpretable latent dimensions to uncover underlying concepts influencing decisions, enhancing transparency of reward models while ensuring alignment with human values."
    ],
    "durationSeconds": 6.3767832219999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7e8c8f73-da9f-4e82-8f2f-0b35e0e5e8c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T21:28:02.711Z_

<details><summary>↩ Tool result · `toolu_01QmQJVXucN9na991tkF7uZS`</summary>

```text
Web search results for query: "SteerRM debiasing reward models sparse autoencoders SAE 2026 arXiv:2603.12795"

Links: [{"title":"[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/abs/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/html/2603.12795"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/pdf/2603.12795"},{"title":"Interpretable Reward Model via Sparse Autoencoder","url":"https://arxiv.org/html/2508.08746v4"},{"title":"Interpretable Reward Model via Sparse Autoencoder","url":"https://arxiv.org/pdf/2508.08746"}]

Based on the search results, here's what I found about the paper:

SteerRM is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. Reward models are critical components of alignment pipelines, yet they exhibit biases toward superficial stylistic cues, preferring better-presented responses over semantically superior ones.

SteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time. Across six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance.

The paper was submitted on March 13, 2026 and was authored by Mengyuan Sun, Zhuohao Yu, Weizheng Gu, Shikun Zhang, and Wei Ye from Peking University's National Engineering Research Center for Software Engineering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a588018c-e15d-40f6-93a7-ce732dd22da4",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "3dad4068-aa14-4c3e-9a67-a6d46a5710b2",
  "toolUseResult": {
    "query": "SteerRM debiasing reward models sparse autoencoders SAE 2026 arXiv:2603.12795",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N37msLomdSJ65aEQmLKDTy",
        "content": [
          {
            "title": "[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2603.12795"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2603.12795"
          },
          {
            "title": "SteerRM: Debiasing Reward Models via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2603.12795"
          },
          {
            "title": "Interpretable Reward Model via Sparse Autoencoder",
            "url": "https://arxiv.org/html/2508.08746v4"
          },
          {
            "title": "Interpretable Reward Model via Sparse Autoencoder",
            "url": "https://arxiv.org/pdf/2508.08746"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\nSteerRM is the first training-free method for debiasing reward models using Sparse Autoencoder (SAE)-based interventions. Reward models are critical components of alignment pipelines, yet they exhibit biases toward superficial stylistic cues, preferring better-presented responses over semantically superior ones.\n\nSteerRM isolates stylistic effects using contrastive paired responses, identifies bias-related SAE features with a strength-stability criterion, and suppresses them at inference time. Across six reward models on RM-Bench, SteerRM improves Hard-split accuracy by 7.3 points on average while preserving overall performance.\n\nThe paper was submitted on March 13, 2026 and was authored by Mengyuan Sun, Zhuohao Yu, Weizheng Gu, Shikun Zhang, and Wei Ye from Peking University's National Engineering Research Center for Software Engineering."
    ],
    "durationSeconds": 8.428394817000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a588018c-e15d-40f6-93a7-ce732dd22da4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
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
  "leafUuid": "3dad4068-aa14-4c3e-9a67-a6d46a5710b2",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Tool result

_source line 24 · 2026-05-19T21:28:05.077Z_

<details><summary>↩ Tool result · `toolu_011JSum6KxgF8imjkZyV6pVg`</summary>

```text
Web search results for query: "Basu et al. "Interpretability without Actionability" mechanistic interventions clinical LM 2026 arXiv:2603.18353"

Links: [{"title":"[2603.18353] Interpretability without actionability","url":"https://arxiv.org/abs/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.18353"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science","url":"https://gist.science/paper/2603.18353"},{"title":"Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF","url":"https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations"

**Authors:** Sanjay Basu and 7 other authors (Sadiq Y. Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, and Rajaie Batniji)

**arXiv ID:** 2603.18353

**Submission Date:** March 18, 2026

**Research Focus:** The paper investigates whether mechanistic interpretability methods can bridge the gap between language models' encoded task-relevant knowledge in internal representations and their output performance.

**Methodology:** The study compared four mechanistic interpretability methods -- concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct) -- for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).

**Key Finding:** Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. Concept bottleneck steering corrected 20% of missed hazards but disrupted 53% of correct detections, indistinguishable from random perturbation.

The paper is available on arXiv at https://arxiv.org/abs/2603.18353


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5beb8fc6-7120-418b-b0a4-858d9c93ce2d",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "bce34b63-8b6c-4446-a162-77a00aa1babc",
  "toolUseResult": {
    "query": "Basu et al. \"Interpretability without Actionability\" mechanistic interventions clinical LM 2026 arXiv:2603.18353",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q6SpDoabd95K7yon74dBMi",
        "content": [
          {
            "title": "[2603.18353] Interpretability without actionability",
            "url": "https://arxiv.org/abs/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
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
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models by Sanjay Basu, Sadiq Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, Rajaie Batniji :: SSRN",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6437137"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.18353"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations | Gist.Science",
            "url": "https://gist.science/paper/2603.18353"
          },
          {
            "title": "Interpretability without Actionability: Mechanistic Intervention Methods Fail to Correct Clinical Triage Errors in Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/403186214_Interpretability_without_Actionability_Mechanistic_Intervention_Methods_Fail_to_Correct_Clinical_Triage_Errors_in_Language_Models"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** \"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations\"\n\n**Authors:** Sanjay Basu and 7 other authors (Sadiq Y. Patel, Parth Sheth, Bhairavi Muralidharan, Namrata Elamaran, Aakriti Kinra, John Morgan, and Rajaie Batniji)\n\n**arXiv ID:** 2603.18353\n\n**Submission Date:** March 18, 2026\n\n**Research Focus:** The paper investigates whether mechanistic interpretability methods can bridge the gap between language models' encoded task-relevant knowledge in internal representations and their output performance.\n\n**Methodology:** The study compared four mechanistic interpretability methods -- concept bottleneck steering (Steerling-8B), sparse autoencoder feature steering, logit lens with activation patching, and linear probing with truthfulness separator vector steering (Qwen 2.5 7B Instruct) -- for correcting false-negative triage errors using 400 physician-adjudicated clinical vignettes (144 hazards, 256 benign).\n\n**Key Finding:** Linear probes discriminated hazardous from benign cases with 98.2% AUROC, yet the model's output sensitivity was only 45.1%, a 53-percentage-point knowledge-action gap. Concept bottleneck steering corrected 20% of missed hazards but disrupted 53% of correct detections, indistinguishable from random perturbation.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2603.18353"
    ],
    "durationSeconds": 11.387372928000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5beb8fc6-7120-418b-b0a4-858d9c93ce2d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T21:28:05.413Z_

<details><summary>↩ Tool result · `toolu_01KiWcoQ1Jh5QkrEeBxrYzLu`</summary>

```text
Web search results for query: "Orgad et al. "Interpretability Can Be Actionable" ICML 2026 arXiv:2605.11161"

Links: [{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161"},{"title":"[2605.11161] Interpretability Can Be Actionable","url":"https://arxiv.org/abs/2605.11161"},{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"ICML Poster Position: Interpretability Can Be Actionable","url":"https://icml.cc/virtual/2026/poster/67043"},{"title":"Actionable Interpretability Must Be Defined in Terms of Symmetries","url":"https://arxiv.org/pdf/2601.12913"},{"title":"ICML 2025 Saturday 07/19","url":"https://icml.cc/virtual/2025/day/7/19"}]

I found the paper! Here's what I found about "Interpretability Can Be Actionable" by Orgad et al.:

**Paper Details:**
- Authors: Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, Mor Geva
- arXiv:2605.11161v1 [cs.LG] 11 May 2026

**Main Argument:**
The paper argues that the central missing ingredient is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.

**Key Concepts:**
The authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.

The paper is a position paper that addresses mounting concern that much of this work has not translated into practical impact, raising questions about its relevance and utility.

You can access the full paper at https://arxiv.org/abs/2605.11161 or view it on the ICML 2026 virtual conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffc62e63-b5c8-4e21-903f-d7c4c997102f",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "1a2d54f3-03e8-40ef-9bb6-20304ca401ce",
  "toolUseResult": {
    "query": "Orgad et al. \"Interpretability Can Be Actionable\" ICML 2026 arXiv:2605.11161",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P6pizjUtno4ePy449dmzBj",
        "content": [
          {
            "title": "Interpretability Can Be Actionable",
            "url": "https://arxiv.org/html/2605.11161"
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
            "title": "ICML Poster Position: Interpretability Can Be Actionable",
            "url": "https://icml.cc/virtual/2026/poster/67043"
          },
          {
            "title": "Actionable Interpretability Must Be Defined in Terms of Symmetries",
            "url": "https://arxiv.org/pdf/2601.12913"
          },
          {
            "title": "ICML 2025 Saturday 07/19",
            "url": "https://icml.cc/virtual/2025/day/7/19"
          }
        ]
      },
      "I found the paper! Here's what I found about \"Interpretability Can Be Actionable\" by Orgad et al.:\n\n**Paper Details:**\n- Authors: Hadas Orgad, Fazl Barez, Tal Haklay, Isabelle Lee, Marius Mosbach, Anja Reusch, Naomi Saphra, Byron Wallace, Sarah Wiegreffe, Eric Wong, Ian Tenney, Mor Geva\n- arXiv:2605.11161v1 [cs.LG] 11 May 2026\n\n**Main Argument:**\nThe paper argues that the central missing ingredient is not new methods, but evaluation criteria: interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself.\n\n**Key Concepts:**\nThe authors define actionable interpretability along two dimensions—concreteness and validation—and analyze the barriers currently preventing real-world impact.\n\nThe paper is a position paper that addresses mounting concern that much of this work has not translated into practical impact, raising questions about its relevance and utility.\n\nYou can access the full paper at https://arxiv.org/abs/2605.11161 or view it on the ICML 2026 virtual conference website."
    ],
    "durationSeconds": 9.375166245,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ffc62e63-b5c8-4e21-903f-d7c4c997102f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T21:28:09.856Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've confirmed several key papers exist. Now let me search for more specific aspects:
1. "Domain Amenability Hypothesis" - has anyone proposed something similar?
2. Multi-granularity comparison of mechanistic interventions
3. CRA (Causal Reward Adjustment) SAE on PRM
4. Lee et al. 2026 scientific rigor criteria
5. What CoRL 2026 actually accepts - is this venue appropriate?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a2d54f3-03e8-40ef-9bb6-20304ca401ce",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "18457bcb-0359-4f14-9d0b-6b1293e8eec5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 27 · 2026-05-19T21:28:10.344Z_

Good, key papers are confirmed. Let me do additional targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18457bcb-0359-4f14-9d0b-6b1293e8eec5",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "50002179-66e8-4572-8dd6-99a60782f61c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 28 · 2026-05-19T21:28:11.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A1zN5zb46WXKQtpEY2q662`</summary>

```json
{
  "query": "\"domain amenability\" mechanistic interpretability when do interventions succeed conditions 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50002179-66e8-4572-8dd6-99a60782f61c",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "3867490e-faba-44de-8be3-96a4187d4064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 29 · 2026-05-19T21:28:11.779Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012zohcpjQYztCaxDoK7RBVi`</summary>

```json
{
  "query": "multi-granularity comparison mechanistic interventions feature neuron circuit level systematic empirical 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3867490e-faba-44de-8be3-96a4187d4064",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "684fd337-9490-4331-86dd-2f1d4c2bf8bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 30 · 2026-05-19T21:28:12.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019S4wf5x3F2BHKCDTsJ3fWq`</summary>

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
  "parentUuid": "684fd337-9490-4331-86dd-2f1d4c2bf8bb",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "dab6371e-b0b8-4e3e-82b6-79599297f6e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 31 · 2026-05-19T21:28:13.534Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RhNG7odaVbsPNcdbB45Yfo`</summary>

```json
{
  "query": "Lee et al. \"Rigorous Interpretation Is a Form of Evaluation\" 2026 arXiv:2605.05508 falsifiability reproducibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dab6371e-b0b8-4e3e-82b6-79599297f6e4",
  "isSidechain": false,
  "requestId": "req_011CbCduZJNjatxgQeZB5Gp4",
  "type": "assistant",
  "uuid": "6c9ccb6b-d651-42bb-a40d-c1403466906e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PodTaDrPpQDf7bZGA5h9TF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3692,
      "cache_read_input_tokens": 24934,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 24934,
          "cache_creation_input_tokens": 3692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3692
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

_source line 32 · 2026-05-19T21:28:18.538Z_

<details><summary>↩ Tool result · `toolu_012zohcpjQYztCaxDoK7RBVi`</summary>

```text
Web search results for query: "multi-granularity comparison mechanistic interventions feature neuron circuit level systematic empirical 2026"

Links: [{"title":"Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3787104"},{"title":"Mechanistic Interpretability of GPT-2","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-study-of-gpt-2"},{"title":"Mechanistic Interpretability of GPT-like Models on Summarization Tasks","url":"https://arxiv.org/html/2505.17073v1"},{"title":"NeuroBreak: LLM Jailbreak Analysis","url":"https://www.emergentmind.com/topics/neurobreak"},{"title":"Can Information Flows Suggest Targets for Interventions in Neural   Circuits?","url":"https://arxiv.org/pdf/2111.05299"},{"title":"29th Annual Computational Neuroscience Meeting: CNS*2020 - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7751124/"},{"title":"Biomimetic model of corticostriatal micro-assemblies discovers a neural code | Nature Communications","url":"https://www.nature.com/articles/s41467-025-67076-x"}]

Based on the search results, I found several relevant sources on mechanistic interpretability research:

The most directly relevant result is a recent ACM survey that organizes mechanistic interpretability techniques along three dimensions—granularity (neurons, circuits, whole algorithms), analytical paradigm (manual tracing, causal intervention, representation analysis), and degree of automation. The survey integrates empirical insights from landmark case studies, including induction heads, the indirect-object circuit, grokking-related phase transitions, and sparse-feature discovery.

Additionally, there are recent papers from 2025-2026 examining mechanistic interventions at multiple levels:

- Research on GPT-2 requires causal experimentation—ablation, path patching, activation substitution—along with careful interpretation of effect sizes and systematic evaluation of redundancy and backup mechanisms.

- One framework provides a foundation for comparing different adaptation techniques and model architectures, enabling systematic investigation of how different approaches affect model internals.

- NeuroBreak combines multi-granular representation probing, semantic/functional neuron attribution, and real-time intervention to form a robust foundation for LLM defense strategies.

These results reflect active research into multi-level mechanistic interpretability with systematic empirical validation across neuron and circuit levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "684fd337-9490-4331-86dd-2f1d4c2bf8bb",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "bf8f4aa1-459a-44a3-89a7-211a51400336",
  "toolUseResult": {
    "query": "multi-granularity comparison mechanistic interventions feature neuron circuit level systematic empirical 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013FNemYeeA8db9qDCkRLqA2",
        "content": [
          {
            "title": "Bridging the Black Box: A Survey on Mechanistic Interpretability in AI | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3787104"
          },
          {
            "title": "Mechanistic Interpretability of GPT-2",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-study-of-gpt-2"
          },
          {
            "title": "Mechanistic Interpretability of GPT-like Models on Summarization Tasks",
            "url": "https://arxiv.org/html/2505.17073v1"
          },
          {
            "title": "NeuroBreak: LLM Jailbreak Analysis",
            "url": "https://www.emergentmind.com/topics/neurobreak"
          },
          {
            "title": "Can Information Flows Suggest Targets for Interventions in Neural   Circuits?",
            "url": "https://arxiv.org/pdf/2111.05299"
          },
          {
            "title": "29th Annual Computational Neuroscience Meeting: CNS*2020 - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7751124/"
          },
          {
            "title": "Biomimetic model of corticostriatal micro-assemblies discovers a neural code | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-025-67076-x"
          }
        ]
      },
      "Based on the search results, I found several relevant sources on mechanistic interpretability research:\n\nThe most directly relevant result is a recent ACM survey that organizes mechanistic interpretability techniques along three dimensions—granularity (neurons, circuits, whole algorithms), analytical paradigm (manual tracing, causal intervention, representation analysis), and degree of automation. The survey integrates empirical insights from landmark case studies, including induction heads, the indirect-object circuit, grokking-related phase transitions, and sparse-feature discovery.\n\nAdditionally, there are recent papers from 2025-2026 examining mechanistic interventions at multiple levels:\n\n- Research on GPT-2 requires causal experimentation—ablation, path patching, activation substitution—along with careful interpretation of effect sizes and systematic evaluation of redundancy and backup mechanisms.\n\n- One framework provides a foundation for comparing different adaptation techniques and model architectures, enabling systematic investigation of how different approaches affect model internals.\n\n- NeuroBreak combines multi-granular representation probing, semantic/functional neuron attribution, and real-time intervention to form a robust foundation for LLM defense strategies.\n\nThese results reflect active research into multi-level mechanistic interpretability with systematic empirical validation across neuron and circuit levels."
    ],
    "durationSeconds": 6.755309479000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "684fd337-9490-4331-86dd-2f1d4c2bf8bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T21:28:18.733Z_

<details><summary>↩ Tool result · `toolu_019S4wf5x3F2BHKCDTsJ3fWq`</summary>

```text
Web search results for query: "CoRL 2026 Conference on Robot Learning topics scope call for papers"

Links: [{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models","url":"https://arxiv.org/pdf/2512.11908"},{"title":"Iterative transfer learning for automatic collective motion tuning on multiple robot platforms","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10060795/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"}]

Based on the search results, here's information about the CoRL 2026 Conference on Robot Learning call for papers:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Call for Papers

CoRL 2026 invites submissions of high-quality research papers that offer novel contributions to robot learning.

## Key Scope Requirements

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

## Important Deadlines

Key submission dates are: Abstract Submission May 25, Full Paper Submission May 28. CoRL 2026 will be held in Austin, Texas, US.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dab6371e-b0b8-4e3e-82b6-79599297f6e4",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "cd6e8b80-1b33-4807-ab59-f7cffbe6421e",
  "toolUseResult": {
    "query": "CoRL 2026 Conference on Robot Learning topics scope call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L1Wv8bgSd3hr3sAbY9CjDd",
        "content": [
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
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
            "title": "Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models",
            "url": "https://arxiv.org/pdf/2512.11908"
          },
          {
            "title": "Iterative transfer learning for automatic collective motion tuning on multiple robot platforms",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10060795/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          }
        ]
      },
      "Based on the search results, here's information about the CoRL 2026 Conference on Robot Learning call for papers:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Call for Papers\n\nCoRL 2026 invites submissions of high-quality research papers that offer novel contributions to robot learning.\n\n## Key Scope Requirements\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nAll submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.\n\n## Important Deadlines\n\nKey submission dates are: Abstract Submission May 25, Full Paper Submission May 28. CoRL 2026 will be held in Austin, Texas, US."
    ],
    "durationSeconds": 6.0060643190000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dab6371e-b0b8-4e3e-82b6-79599297f6e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T21:28:18.812Z_

<details><summary>↩ Tool result · `toolu_01RhNG7odaVbsPNcdbB45Yfo`</summary>

```text
Web search results for query: "Lee et al. "Rigorous Interpretation Is a Form of Evaluation" 2026 arXiv:2605.05508 falsifiability reproducibility"

Links: [{"title":"Rigorous Interpretation Is a Form of Evaluation","url":"https://arxiv.org/html/2605.05508v1"},{"title":"Towards A Rigorous Science of Interpretable Machine Learning","url":"https://arxiv.org/pdf/1702.08608"},{"title":"Large Language Model-Assisted Point-in-Time Interpretation of Advanced Hemodynamics in Liver Transplant Recipients: A Pilot Evaluation of Content Quality and Safety","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12841667/"},{"title":"Evaluating the Accuracy and Explanatory Quality of Large Language Models ChatGPT, Claude, DeepSeek, Gemini, Grok, and Le Chat in Statistical Test Selection for Hypothesis Testing Decisions","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12627256/"},{"title":"How Trustworthy Are LLM-as-Judge Ratings for Interpretive Responses? Implications for Qualitative Research Workflows","url":"https://arxiv.org/pdf/2604.00008"}]

I found the paper! Here's what the search revealed:

The paper "Rigorous Interpretation Is a Form of Evaluation" by Isabelle Lee, Emmy Liu, Cathy Jiao, and others was published on arXiv (2605.05508v1) on May 6, 2026.

The paper argues that understanding why a model produces a behavior can be as important as measuring what it produces, and that interpretability can serve as a richer and more principled form of model evaluation beyond surface-level performance metrics.

The authors explore three ways interpretability can function evaluatively: (1) fixing problems by identifying the root causes of unwanted behavior, (2) detecting subtly faulty mechanisms that invalidate model outputs, and (3) predicting potential issues before they arise.

The paper appears to directly address the relationship between rigorous interpretation and evaluation in machine learning models, which connects to questions about falsifiability and reproducibility in model assessment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c9ccb6b-d651-42bb-a40d-c1403466906e",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "7e8f0e91-b4f1-40e7-b64f-805d2f87bec9",
  "toolUseResult": {
    "query": "Lee et al. \"Rigorous Interpretation Is a Form of Evaluation\" 2026 arXiv:2605.05508 falsifiability reproducibility",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BMFEDe7CZMXfwCzftga7JJ",
        "content": [
          {
            "title": "Rigorous Interpretation Is a Form of Evaluation",
            "url": "https://arxiv.org/html/2605.05508v1"
          },
          {
            "title": "Towards A Rigorous Science of Interpretable Machine Learning",
            "url": "https://arxiv.org/pdf/1702.08608"
          },
          {
            "title": "Large Language Model-Assisted Point-in-Time Interpretation of Advanced Hemodynamics in Liver Transplant Recipients: A Pilot Evaluation of Content Quality and Safety",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12841667/"
          },
          {
            "title": "Evaluating the Accuracy and Explanatory Quality of Large Language Models ChatGPT, Claude, DeepSeek, Gemini, Grok, and Le Chat in Statistical Test Selection for Hypothesis Testing Decisions",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12627256/"
          },
          {
            "title": "How Trustworthy Are LLM-as-Judge Ratings for Interpretive Responses? Implications for Qualitative Research Workflows",
            "url": "https://arxiv.org/pdf/2604.00008"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nThe paper \"Rigorous Interpretation Is a Form of Evaluation\" by Isabelle Lee, Emmy Liu, Cathy Jiao, and others was published on arXiv (2605.05508v1) on May 6, 2026.\n\nThe paper argues that understanding why a model produces a behavior can be as important as measuring what it produces, and that interpretability can serve as a richer and more principled form of model evaluation beyond surface-level performance metrics.\n\nThe authors explore three ways interpretability can function evaluatively: (1) fixing problems by identifying the root causes of unwanted behavior, (2) detecting subtly faulty mechanisms that invalidate model outputs, and (3) predicting potential issues before they arise.\n\nThe paper appears to directly address the relationship between rigorous interpretation and evaluation in machine learning models, which connects to questions about falsifiability and reproducibility in model assessment."
    ],
    "durationSeconds": 5.276156148000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c9ccb6b-d651-42bb-a40d-c1403466906e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "7e8f0e91-b4f1-40e7-b64f-805d2f87bec9",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Tool result

_source line 37 · 2026-05-19T21:28:30.464Z_

<details><summary>↩ Tool result · `toolu_01A1zN5zb46WXKQtpEY2q662`</summary>

```text
Web search results for query: ""domain amenability" mechanistic interpretability when do interventions succeed conditions 2025 2026"

Links: [{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"Call for Papers | Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/cfp/"},{"title":"Mechanistic Interpretability Framework","url":"https://www.emergentmind.com/topics/mechanistic-interpretability-framework"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Survey on the Role of Mechanistic Interpretability in Generative AI","url":"https://www.mdpi.com/2504-2289/9/8/193"},{"title":"Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Mechanistic Interpretability Workshop at ICML 2026","url":"https://mechinterpworkshop.com/"},{"title":"Mechanistic interpretability: 10 Breakthrough Technologies 2026 | MIT Technology Review","url":"https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/"}]

I found several relevant results about mechanistic interpretability from 2025-2026, but I didn't find specific information about "domain amenability" in relation to when interventions succeed. Let me search more specifically for that term:

Links: [{"title":"Improving predictions of compound amenability for liquid chromatography–mass spectrometry to enhance non-targeted analysis | Analytical and Bioanalytical Chemistry | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00216-024-05229-5"},{"title":"(Un)reasonable Allure of Ante-hoc Interpretability for High-stakes   Domains: Transparency Is Necessary but Insufficient for Comprehensibility","url":"https://arxiv.org/pdf/2306.02312"},{"title":"Domain Level Interpretability: Interpreting Black-box Model with Domain-specific Embedding | Proceedings of the 17th ACM International Conference on Web Search and Data Mining","url":"https://doi.org/10.1145/3616855.3635688"},{"title":"Model interpretability enhances domain generalization in the case of textual complexity modeling - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11873011/"},{"title":"Model interpretability enhances domain generalization in the case of textual complexity modeling - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40041855/"},{"title":"Model interpretability enhances domain generalization in the case of textual complexity modeling","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11873011/"},{"title":"Interpretability Analysis of Domain Adapted Dense Retrievers Göksenin Yüksel","url":"https://arxiv.org/pdf/2501.14459"}]

The search results for "domain amenability" are returning results about chemical domains and general domain adaptation, not about mechanistic interpretability and interventions. Let me search for more specific terms related to interventions and conditions for success in mechanistic interpretability:

Links: [{"title":"Interpretability Can Be Actionable Hadas Orgad 1","url":"https://arxiv.org/pdf/2605.11161"},{"title":"Interpretability Can Be Actionable","url":"https://arxiv.org/html/2605.11161"},{"title":"The Hitchhiker's Guide to Actionable Interpretability","url":"https://actionable-interpretability-guide.github.io/"},{"title":"Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://arxiv.org/html/2603.18353v1"},{"title":"[2605.11161] Interpretability Can Be Actionable","url":"https://arxiv.org/abs/2605.11161"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/pdf/2601.14004"},{"title":"(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations","url":"https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"},{"title":"Interpretability without actionability: mechanistic methods ...","url":"https://arxiv.org/pdf/2603.18353"}]

Based on my web search results, I found highly relevant recent work on mechanistic interpretability and interventions from 2025-2026. However, I did not find specific work using the exact term "domain amenability" in relation to mechanistic interpretability interventions.

The most relevant recent work I found addresses related themes:

## Key Recent Research on Interpretability and Interventions (2025-2026):

**Actionable Interpretability Framework:** Interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. A recent position paper by Orgad et al. (2026) proposes this as a central evaluation criterion for interpretability work.

**When Interventions Succeed:** Importantly, recent research reveals significant challenges. Language models encode near-perfect task knowledge in linearly separable internal representations, yet current mechanistic interpretability methods at best correct a minority of errors, with the knowledge-action gap persisting across all four intervention paradigms tested, suggesting fundamental limitations of inference-time representation-level steering.

**Types of Targeted Interventions:** Interpretability can identify components responsible for specific behaviors, enabling targeted interventions through model editing that modifies weights to insert, remove, or correct behaviors without full retraining, and runtime interventions that steer activations along interpretable directions at inference time.

**Practical Survey:** A practical survey presents a framework structured around "Locate, Steer, and Improve," formally categorizing Localizing and Steering methods based on specific Interpretable Objects to establish a rigorous intervention protocol, enabling tangible improvements in Alignment, Capability, and Efficiency.

The specific term "domain amenability" does not appear in recent mechanistic interpretability literature, so it's possible this is from a more specialized paper or uses different terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3867490e-faba-44de-8be3-96a4187d4064",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "739293b1-5e3c-45c7-aac7-e3b90576f5e6",
  "toolUseResult": {
    "query": "\"domain amenability\" mechanistic interpretability when do interventions succeed conditions 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JPNFf9F62Qwkwp2YtfzZ2m",
        "content": [
          {
            "title": "Interpretability Can Be Actionable Hadas Orgad 1",
            "url": "https://arxiv.org/pdf/2605.11161"
          },
          {
            "title": "Call for Papers | Mechanistic Interpretability Workshop at ICML 2026",
            "url": "https://mechinterpworkshop.com/cfp/"
          },
          {
            "title": "Mechanistic Interpretability Framework",
            "url": "https://www.emergentmind.com/topics/mechanistic-interpretability-framework"
          },
          {
            "title": "Automated Interpretability-Driven Model Auditing and Control: A Research Agenda",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"
          },
          {
            "title": "Survey on the Role of Mechanistic Interpretability in Generative AI",
            "url": "https://www.mdpi.com/2504-2289/9/8/193"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MECHANISTIC INTERPRETABILITY",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "Mechanistic Interpretability Workshop at ICML 2026",
            "url": "https://mechinterpworkshop.com/"
          },
          {
            "title": "Mechanistic interpretability: 10 Breakthrough Technologies 2026 | MIT Technology Review",
            "url": "https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/"
          }
        ]
      },
      "I found several relevant results about mechanistic interpretability from 2025-2026, but I didn't find specific information about \"domain amenability\" in relation to when interventions succeed. Let me search more specifically for that term:",
      {
        "tool_use_id": "srvtoolu_018j19b62DV1fLck2oTYhfzu",
        "content": [
          {
            "title": "Improving predictions of compound amenability for liquid chromatography–mass spectrometry to enhance non-targeted analysis | Analytical and Bioanalytical Chemistry | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00216-024-05229-5"
          },
          {
            "title": "(Un)reasonable Allure of Ante-hoc Interpretability for High-stakes   Domains: Transparency Is Necessary but Insufficient for Comprehensibility",
            "url": "https://arxiv.org/pdf/2306.02312"
          },
          {
            "title": "Domain Level Interpretability: Interpreting Black-box Model with Domain-specific Embedding | Proceedings of the 17th ACM International Conference on Web Search and Data Mining",
            "url": "https://doi.org/10.1145/3616855.3635688"
          },
          {
            "title": "Model interpretability enhances domain generalization in the case of textual complexity modeling - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11873011/"
          },
          {
            "title": "Model interpretability enhances domain generalization in the case of textual complexity modeling - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/40041855/"
          },
          {
            "title": "Model interpretability enhances domain generalization in the case of textual complexity modeling",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11873011/"
          },
          {
            "title": "Interpretability Analysis of Domain Adapted Dense Retrievers Göksenin Yüksel",
            "url": "https://arxiv.org/pdf/2501.14459"
          }
        ]
      },
      "The search results for \"domain amenability\" are returning results about chemical domains and general domain adaptation, not about mechanistic interpretability and interventions. Let me search for more specific terms related to interventions and conditions for success in mechanistic interpretability:",
      {
        "tool_use_id": "srvtoolu_019JH34YA14dDwDheXpvetkq",
        "content": [
          {
            "title": "Interpretability Can Be Actionable Hadas Orgad 1",
            "url": "https://arxiv.org/pdf/2605.11161"
          },
          {
            "title": "Interpretability Can Be Actionable",
            "url": "https://arxiv.org/html/2605.11161"
          },
          {
            "title": "The Hitchhiker's Guide to Actionable Interpretability",
            "url": "https://actionable-interpretability-guide.github.io/"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://arxiv.org/html/2603.18353v1"
          },
          {
            "title": "[2605.11161] Interpretability Can Be Actionable",
            "url": "https://arxiv.org/abs/2605.11161"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://arxiv.org/pdf/2601.14004"
          },
          {
            "title": "(PDF) Interpretability without actionability: mechanistic methods cannot correct language model errors despite near-perfect internal representations",
            "url": "https://www.researchgate.net/publication/402859588_Interpretability_without_actionability_mechanistic_methods_cannot_correct_language_model_errors_despite_near-perfect_internal_representations"
          },
          {
            "title": "Interpretability without actionability: mechanistic methods ...",
            "url": "https://arxiv.org/pdf/2603.18353"
          }
        ]
      },
      "Based on my web search results, I found highly relevant recent work on mechanistic interpretability and interventions from 2025-2026. However, I did not find specific work using the exact term \"domain amenability\" in relation to mechanistic interpretability interventions.\n\nThe most relevant recent work I found addresses related themes:\n\n## Key Recent Research on Interpretability and Interventions (2025-2026):\n\n**Actionable Interpretability Framework:** Interpretability should be evaluated by actionability—the extent to which insights enable concrete decisions and interventions beyond interpretability research itself. A recent position paper by Orgad et al. (2026) proposes this as a central evaluation criterion for interpretability work.\n\n**When Interventions Succeed:** Importantly, recent research reveals significant challenges. Language models encode near-perfect task knowledge in linearly separable internal representations, yet current mechanistic interpretability methods at best correct a minority of errors, with the knowledge-action gap persisting across all four intervention paradigms tested, suggesting fundamental limitations of inference-time representation-level steering.\n\n**Types of Targeted Interventions:** Interpretability can identify components responsible for specific behaviors, enabling targeted interventions through model editing that modifies weights to insert, remove, or correct behaviors without full retraining, and runtime interventions that steer activations along interpretable directions at inference time.\n\n**Practical Survey:** A practical survey presents a framework structured around \"Locate, Steer, and Improve,\" formally categorizing Localizing and Steering methods based on specific Interpretable Objects to establish a rigorous intervention protocol, enabling tangible improvements in Alignment, Capability, and Efficiency.\n\nThe specific term \"domain amenability\" does not appear in recent mechanistic interpretability literature, so it's possible this is from a more specialized paper or uses different terminology."
    ],
    "durationSeconds": 19.156660548,
    "searchCount": 3
  },
  "sourceToolAssistantUUID": "3867490e-faba-44de-8be3-96a4187d4064",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-19T21:28:30.471Z_

```json
{
  "parentUuid": "739293b1-5e3c-45c7-aac7-e3b90576f5e6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fd273fef-584f-495e-aa04-a55cbc6e4c15",
  "timestamp": "2026-05-19T21:28:30.471Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 39 · 2026-05-19T21:28:36.567Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important - the CoRL 2026 search confirms that CoRL is specifically about **robot learning** and requires submissions to "focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." This proposal is about mechanistic interpretability of Process Reward Models for mathematical reasoning - it has nothing to do with robotics.

This is a fundamental venue mismatch that I need to flag. Let me also note that the "Domain Amenability Hypothesis" appears to be novel - I didn't find prior work using this exact framing.

Let me do one more search to check if there's any existing work that systematically compares multiple granularities of mechanistic interventions within a single domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd273fef-584f-495e-aa04-a55cbc6e4c15",
  "isSidechain": false,
  "requestId": "req_011CbCdwQQtZMLNZoXgaN2HB",
  "type": "assistant",
  "uuid": "db252554-8b4d-4b02-8a22-59f83d913e2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116u9vpMinPVcPGj9qnbSsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1906,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 28626,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1906,
          "output_tokens": 345,
          "cache_read_input_tokens": 28626,
          "cache_creation_input_tokens": 2146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2146
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

_source line 40 · 2026-05-19T21:28:41.356Z_

Critical finding: CoRL is a robotics conference. Let me do one final search to complete my landscape understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db252554-8b4d-4b02-8a22-59f83d913e2e",
  "isSidechain": false,
  "requestId": "req_011CbCdwQQtZMLNZoXgaN2HB",
  "type": "assistant",
  "uuid": "a6afc9aa-af7f-48d6-a7af-77b6aa09b5ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116u9vpMinPVcPGj9qnbSsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1906,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 28626,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1906,
          "output_tokens": 345,
          "cache_read_input_tokens": 28626,
          "cache_creation_input_tokens": 2146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2146
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

_source line 41 · 2026-05-19T21:28:41.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKGfP8GBfv51GECtY7F187`</summary>

```json
{
  "query": "CRA causal reward adjustment SAE PRM backdoor correction arXiv:2508.04216 sparse autoencoder process reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6afc9aa-af7f-48d6-a7af-77b6aa09b5ec",
  "isSidechain": false,
  "requestId": "req_011CbCdwQQtZMLNZoXgaN2HB",
  "type": "assistant",
  "uuid": "a4da2726-754e-4b96-9c00-b3984c0c9042",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116u9vpMinPVcPGj9qnbSsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1906,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 28626,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1906,
          "output_tokens": 345,
          "cache_read_input_tokens": 28626,
          "cache_creation_input_tokens": 2146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2146
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

_source line 42 · 2026-05-19T21:28:41.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xAAsCsSfm6NW5Gf1e1Nvs`</summary>

```json
{
  "query": "\"Locate Steer Improve\" actionable mechanistic interpretability survey Zhang 2026 arXiv:2601.14004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4da2726-754e-4b96-9c00-b3984c0c9042",
  "isSidechain": false,
  "requestId": "req_011CbCdwQQtZMLNZoXgaN2HB",
  "type": "assistant",
  "uuid": "fdd6fa8a-d0c3-40cc-ae19-c1403e6a1178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116u9vpMinPVcPGj9qnbSsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1906,
      "cache_creation_input_tokens": 2146,
      "cache_read_input_tokens": 28626,
      "output_tokens": 345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2146,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1906,
          "output_tokens": 345,
          "cache_read_input_tokens": 28626,
          "cache_creation_input_tokens": 2146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2146
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

_source line 43 · 2026-05-19T21:28:47.594Z_

<details><summary>↩ Tool result · `toolu_01HKGfP8GBfv51GECtY7F187`</summary>

```text
Web search results for query: "CRA causal reward adjustment SAE PRM backdoor correction arXiv:2508.04216 sparse autoencoder process reward"

Links: [{"title":"[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/abs/2508.04216"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in ...","url":"https://arxiv.org/pdf/2508.04216"},{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"},{"title":"Causal Policy Learning in Reinforcement Learning: Backdoor-Adjusted Soft Actor-Critic","url":"https://arxiv.org/pdf/2506.05445"},{"title":"Causal Bandit Over Unknown Graphs: Upper Confidence Bounds With Backdoor Adjustment","url":"https://arxiv.org/pdf/2502.02020"}]

Based on the search results, here's what I found about the research paper arXiv:2508.04216:

## Overview

The paper is titled "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction".

## Problem Addressed

External reasoning systems combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving. However, these systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers.

## The CRA Method

Causal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.

## Key Results

Experiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.

The approach uses causal inference principles to address the problem, with the sparse autoencoder (SAE) component being crucial for identifying interpretable semantic features in the PRM's internal representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4da2726-754e-4b96-9c00-b3984c0c9042",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "b49e7183-e7aa-4763-bb55-3d1c2c36b5af",
  "toolUseResult": {
    "query": "CRA causal reward adjustment SAE PRM backdoor correction arXiv:2508.04216 sparse autoencoder process reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BMMgsWqmbCMwSqtjs4Zs4V",
        "content": [
          {
            "title": "[2508.04216] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/abs/2508.04216"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/html/2508.04216v1"
          },
          {
            "title": "[PDF] Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Causal-Reward-Adjustment:-Mitigating-Reward-Hacking-Song-Song/d98cf088a2ca29326352d4499c11d32b25e75bfa"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in ...",
            "url": "https://arxiv.org/pdf/2508.04216"
          },
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          },
          {
            "title": "Causal Policy Learning in Reinforcement Learning: Backdoor-Adjusted Soft Actor-Critic",
            "url": "https://arxiv.org/pdf/2506.05445"
          },
          {
            "title": "Causal Bandit Over Unknown Graphs: Upper Confidence Bounds With Backdoor Adjustment",
            "url": "https://arxiv.org/pdf/2502.02020"
          }
        ]
      },
      "Based on the search results, here's what I found about the research paper arXiv:2508.04216:\n\n## Overview\n\nThe paper is titled \"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction\".\n\n## Problem Addressed\n\nExternal reasoning systems combine language models with process reward models (PRMs) to select high-quality reasoning paths for complex tasks such as mathematical problem solving. However, these systems are prone to reward hacking, where high-scoring but logically incorrect paths are assigned high scores by the PRMs, leading to incorrect answers.\n\n## The CRA Method\n\nCausal Reward Adjustment (CRA) is a method that mitigates reward hacking by estimating the true reward of a reasoning path. CRA trains sparse autoencoders on the PRM's internal activations to recover interpretable features, then corrects confounding by using backdoor adjustment.\n\n## Key Results\n\nExperiments on math solving datasets demonstrate that CRA mitigates reward hacking and improves final accuracy, without modifying the policy model or retraining PRM.\n\nThe approach uses causal inference principles to address the problem, with the sparse autoencoder (SAE) component being crucial for identifying interpretable semantic features in the PRM's internal representations."
    ],
    "durationSeconds": 5.991182514,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4da2726-754e-4b96-9c00-b3984c0c9042",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T21:28:47.704Z_

<details><summary>↩ Tool result · `toolu_011xAAsCsSfm6NW5Gf1e1Nvs`</summary>

```text
Web search results for query: ""Locate Steer Improve" actionable mechanistic interpretability survey Zhang 2026 arXiv:2601.14004"

Links: [{"title":"[2601.14004] Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/abs/2601.14004"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/399956588_Locate_Steer_and_Improve_A_Practical_Survey_of_Actionable_Mechanistic_Interpretability_in_Large_Language_Models"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260114004Z/abstract"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic","url":"https://arxiv.org/pdf/2601.14004"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://arxiv.org/html/2601.14004v4"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://bibbase.org/network/publication/lindsey-vanderweij-nanda-others-locatesteerandimproveapracticalsurveyofactionablemechanisticinterpretabilityinlargelanguagemodels-2026"},{"title":"GitHub - rattlesnakey/Awesome-Actionable-MI-Survey: The Github repo for our survey paper: \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\" · GitHub","url":"https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey"},{"title":"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large L - YouTube","url":"https://www.youtube.com/watch?v=GpAK_SwfVOY"},{"title":"Paper page - Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models","url":"https://huggingface.co/papers/2601.14004"}]

## Search Results

I found the paper you were looking for. Here are the key details:

**Paper Title:** "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models"

**ArXiv ID:** arXiv:2601.14004

**Lead Author:** Hengyuan Zhang

**Submission Date:** January 20, 2026 (with the latest version v4 on April 14, 2026)

**Main Contribution:** The paper presents a practical survey structured around the pipeline: "Locate, Steer, and Improve." It formally categorizes Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol, demonstrating how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as an actionable methodology for model optimization.

**Additional Resources:** The curated paper list is available at https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey

The paper is available in multiple formats on arXiv, including PDF and HTML versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdd6fa8a-d0c3-40cc-ae19-c1403e6a1178",
  "isSidechain": false,
  "promptId": "a7ab1539-857f-4f11-a86d-10b2113c408a",
  "type": "user",
  "uuid": "aa5de220-24b3-4056-8618-acf33e95d5d3",
  "toolUseResult": {
    "query": "\"Locate Steer Improve\" actionable mechanistic interpretability survey Zhang 2026 arXiv:2601.14004",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BwiRXzoWYMgW92oiSVSmUs",
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
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260114004Z/abstract"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic",
            "url": "https://arxiv.org/pdf/2601.14004"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://arxiv.org/html/2601.14004v4"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://bibbase.org/network/publication/lindsey-vanderweij-nanda-others-locatesteerandimproveapracticalsurveyofactionablemechanisticinterpretabilityinlargelanguagemodels-2026"
          },
          {
            "title": "GitHub - rattlesnakey/Awesome-Actionable-MI-Survey: The Github repo for our survey paper: \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\" · GitHub",
            "url": "https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey"
          },
          {
            "title": "Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large L - YouTube",
            "url": "https://www.youtube.com/watch?v=GpAK_SwfVOY"
          },
          {
            "title": "Paper page - Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models",
            "url": "https://huggingface.co/papers/2601.14004"
          }
        ]
      },
      "## Search Results\n\nI found the paper you were looking for. Here are the key details:\n\n**Paper Title:** \"Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models\"\n\n**ArXiv ID:** arXiv:2601.14004\n\n**Lead Author:** Hengyuan Zhang\n\n**Submission Date:** January 20, 2026 (with the latest version v4 on April 14, 2026)\n\n**Main Contribution:** The paper presents a practical survey structured around the pipeline: \"Locate, Steer, and Improve.\" It formally categorizes Localizing (diagnosis) and Steering (intervention) methods based on specific Interpretable Objects to establish a rigorous intervention protocol, demonstrating how this framework enables tangible improvements in Alignment, Capability, and Efficiency, effectively operationalizing MI as an actionable methodology for model optimization.\n\n**Additional Resources:** The curated paper list is available at https://github.com/rattlesnakey/Awesome-Actionable-MI-Survey\n\nThe paper is available in multiple formats on arXiv, including PDF and HTML versions."
    ],
    "durationSeconds": 6.032858796,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fdd6fa8a-d0c3-40cc-ae19-c1403e6a1178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "aa5de220-24b3-4056-8618-acf33e95d5d3",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Assistant

_source line 47 · 2026-05-19T21:29:39.753Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to provide a thorough evaluation. Let me synthesize my findings.

## Key Observations

### 1. CRITICAL VENUE MISMATCH
CoRL (Conference on Robot Learning) requires submissions to "focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics." This proposal is entirely about mechanistic interpretability of Process Reward Models for mathematical reasoning. There is ZERO robotics content. This is a fundamental mismatch that makes acceptance probability essentially 0% at CoRL, regardless of the idea's quality.

I should flag this prominently but also evaluate the idea quality on its own merits for potential submission to an appropriate venue (like NeurIPS, ICML, ACL, EMNLP, etc.).


### 2. Idea Quality Assessment

The core contribution is the "Domain Amenability Hypothesis" - proposing that mechanistic interventions work when domains have well-defined output semantics, constrained structure, verifiable ground truth, and testable specificity. The plan is to test this on Process Reward Models for math (which should satisfy these conditions) and contrast with clinical language models where prior work found interventions failed. The hypothesis itself is a novel framing, though the underlying intuition feels somewhat intuitive.

The multi-granularity comparison across feature, neuron, and circuit levels within a single domain is genuinely novel - I haven't seen prior work doing this exact systematic comparison. But the individual techniques are mostly existing methods: SAE training, feature suppression, neuron-level intervention, and circuit tracing. So this is really a large-scale empirical study combining known methods in a structured way.

The Domain Amenability Hypothesis has a post-hoc quality to it though - I'm essentially picking domains where interventions succeed and fail, then listing properties that differ between them. Any pair of success/failure cases will naturally have distinguishing properties, so the real question is whether this rises above obvious pattern-matching.

Without a third domain that satisfies some conditions but not others, the hypothesis feels unfalsifiable from just two data points. The confounds are also substantial: different models, different methods, different scales between the PRM and clinical LM comparisons make it hard to isolate whether success comes from the four domain properties or something else entirely. The four conditions themselves seem somewhat arbitrary too - why these specific properties rather than information density or training data quality?

The multi-granularity comparison has practical value and the actionability question is timely, but the theoretical framing is weak. An ideal reviewer would likely note that the Domain Amenability Hypothesis is interesting but can't really be tested with only two domains, and that PRMs succeeding with mechanistic interventions isn't particularly surprising given their scalar outputs and verifiable ground truth. The real contribution here is more engineering-focused - running existing methods on PRMs and comparing results - rather than a fundamental scientific insight.

The novelty is moderate since the systematic comparison is genuinely new but the individual components are existing work, and the significance is also moderate because while the question matters, the answer is somewhat predictable. The related work section is thorough though. For CoRL specifically, this has zero chance since there's no robotics content at all, but at a venue like NeurIPS or ICML it might have around 20-30% acceptance probability based on idea quality alone. Given that the user specifically asked about CoRL 2026, I need to be direct about the mismatch. I need to focus on evaluating the idea quality itself, though the venue mismatch is too significant to ignore. For the acceptance probability, if this goes to CoRL it's essentially a desk reject at 0-5%, but submitted to an appropriate NLP venue like NeurIPS, ICML, or EMNLP, the systematic empirical study could realistically achieve 20-30% acceptance—the Domain Amenability Hypothesis provides novel framing, though it's weakly testable, and while the multi-granularity comparison is useful, the work is ultimately incremental despite thorough related work coverage.

Since the user specifically asked about CoRL 2026, I should flag this venue mismatch prominently but also evaluate the idea on its actual merits for the machine interpretation and NLP field where it belongs.

Looking at the substantive evaluation: the Domain Amenability Hypothesis is an interesting framing, though the evidence is limited with just two comparisons. The systematic multi-granularity comparison does fill a real gap in the literature, but the individual methods are all established techniques. The significance is moderate—while the actionability debate is timely, the likely conclusion that interventions work better on constrained tasks isn't particularly surprising. The related work section is quite strong with comprehensive coverage and clear positioning.

For acceptance prospects, I'd estimate around 20-30% at an appropriate MI/NLP venue, held back by the post-hoc nature of the core hypothesis and the risk that the findings feel intuitive. At CoRL specifically, it's essentially a desk reject at roughly 5% given the complete absence of robotics content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa5de220-24b3-4056-8618-acf33e95d5d3",
  "isSidechain": false,
  "requestId": "req_011CbCdxg6jupSinH2jBQgxL",
  "type": "assistant",
  "uuid": "748d3f57-342e-43be-a0b5-ddf78660830c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lpdu1itGaWvru3G8kxrTf9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 30772,
      "output_tokens": 6187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6187,
          "cache_read_input_tokens": 30772,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 48 · 2026-05-19T21:31:03.742Z_

Now I have sufficient information to provide a thorough, evidence-based evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【⚠️ 致命问题：投稿会议与论文主题严重不匹配】

CoRL (Conference on Robot Learning) 的 Call for Papers 明确要求 "submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics"。本 proposal 的内容——对 Process Reward Models 的机制可解释性分析和多粒度干预比较——完全属于 NLP/ML interpretability 领域，与机器人学习没有任何关联。

如果确实投 CoRL 2026，大概率在 desk review 阶段被拒。建议改投 NeurIPS 2026、ICML 2026 (interpretability track)、ACL/EMNLP 2026 等更匹配的会议。

以下评估假设该 proposal 投向一个**主题匹配的顶会** (NeurIPS/ICML/EMNLP)，纯粹评估 idea 质量。

---

【领域调研】:

- [Basu et al., arXiv:2603.18353] (2026): 核心动机论文。在临床分诊 LM 上测试四种机制干预方法（包括 SAE steering 和 activation patching），发现即使线性探针 AUROC 达 98.2%，干预效果几乎为零，揭示 "knowledge-action gap"。本 proposal 的 Domain Amenability Hypothesis 以此为反面对照。

- [SteerRM, arXiv:2603.12795] (2026): 使用预训练 LlamaScope SAE 对 RM 进行 feature-level debiasing，RM-Bench Hard split +7.3 pts。关键局限：仅在 layers 0-9 有效（分布 mismatch）。本 proposal 的 feature-level 干预直接建立在此之上（改用 from-scratch SAE）。

- [CIRM/Shinoda et al., arXiv:2604.27495] (ACL 2026): Neuron-level 因果中介分析，编辑 <2% 神经元可匹配 70B RM 性能。本 proposal 的 neuron-level 干预直接复现并比较此方法。

- [Orgad et al., arXiv:2605.11161] (ICML 2026): Position paper，提出用 actionability 评估 interpretability，定义 concreteness 和 validation 两个维度。本 proposal 采用其评估框架但未贡献新框架。

- [Lee et al., arXiv:2605.05508] (2026): 主张严格的解释可作为评估形式，提出 falsifiability/reproducibility/predictivity 三个标准。本 proposal 采用此框架作为互补评估。

- [Zhang et al., "Locate, Steer, Improve", arXiv:2601.14004] (2026): 最全面的 actionable MI survey，分类定位和干预方法。本 proposal 明确将自己定位为此 survey 框架的实例化。

- [CRA, arXiv:2508.04216] (2025): 在 PRM 激活上从零训练 SAE 进行 backdoor correction。本 proposal 的 SAE 训练方法直接继承自此工作。

- [Arad et al., arXiv:2505.20063] (EMNLP 2025): 证明 output-score filtering 能将 SAE steering 效果提升 2-3×。本 proposal 的 feature filtering 方法直接来自此工作。

- 调研总结：这个领域正处于"机制可解释性能否真正指导干预"的激烈争论期（Basu 否定 vs. SteerRM/CIRM 肯定），2026 年 Q1-Q2 涌现了大量工作。但各工作各自为战，确实缺少一个统一框架内的多粒度系统比较。本 proposal 试图填补这个空白，但其理论贡献（Domain Amenability Hypothesis）基于 N=2 的领域对比，论证力度偏弱。

---

【Trivial Alternative 检验】:

存在显著的 trivial alternative 威胁：

1. **简单的方法对比也能回答核心问题**：如果目标只是"PRM debiasing 哪种粒度最好"，可以直接跑 SteerRM (feature) + CIRM (neuron) + circuit ablation 在同一组 benchmark 上比较，无需 Domain Amenability Hypothesis 的理论包装。这个 "engineering comparison" 本身有实用价值，但 novelty 有限。

2. **Domain Amenability Hypothesis 是事后叙事**：从两个领域（PRM 成功 vs. 临床 LM 失败）归纳出 4 个区分条件，任何两个不同领域都能找到一组区分属性。没有第三个（或更多）验证域来测试 hypothesis 的预测力，这本质上是一个 N=2 的 post-hoc 归纳，而非可证伪的理论。真正有说服力的做法需要：找到一个满足部分条件但不满足全部条件的中间域（如 code generation RMs），测试预测。

3. **增量价值定位**：proposal 的真正增量不在"理论"而在"系统比较"——将多种已有方法在统一框架内公平比较。这有 benchmark/evaluation paper 的价值，但 idea 层面的 novelty 上限较低。

---

【前提假设检验】:

核心 claim 的逻辑链有以下未经验证的假设：

1. **"PRM 满足 4 个条件 → 干预必然成功" 是未验证跳跃**：4 个条件（well-defined output semantics, constrained output structure, verifiable ground truth, testable specificity）是否是充分条件？是否是必要条件？是否遗漏了关键变量（如模型规模、训练方式、任务复杂度、reward 空间维度）？这些都没有理论推导支撑，纯粹是从一个成功案例和一个失败案例的对比中归纳的。

2. **与 Basu et al. 的对比存在严重混淆因素**：两个实验使用不同的模型架构、不同的模型规模、不同的训练数据、不同的任务、不同的评估标准。即使 PRM 干预成功而临床 LM 干预失败，也无法归因于 4 个 domain 属性——可能是模型差异、任务难度差异、数据分布差异等任何因素导致。这是一个典型的 confounded comparison。

3. **"43% of reward gains from stylistic exploitation" 的引用假设 PRMs 的 bias 足够大且可分离**：如果实际上 fluency 和 reasoning 在 PRM 内部高度纠缠（而非可分离的 circuit），所有基于"先定位再干预"的方法都会失败——这恰恰可能验证 Basu et al. 的观点而非 proposal 的假设。

4. **"至少两种方法收敛即可确认 circuit"的标准较低**：RelP 和 activation patching 在方法论上高度相关（都是梯度/因果干预类），它们的收敛不如两种理论上独立的方法（如因果方法 + 信息理论方法）那样有说服力。

---

【3 维度打分】:

1. **Novelty: 弱-中** — 
   - "Domain Amenability Hypothesis" 作为命名和框架是新的，但其本质——"干预在更简单、更结构化的任务上更容易成功"——接近于 common sense。搜索结果中未发现完全相同的命名框架，但 Orgad et al. (ICML 2026) 的 concreteness/validation 维度和 Zhang et al. 的 survey 已经隐含了类似思路（在更结构化的任务上更容易 validate intervention）。
   - 多粒度系统比较确实是一个真实的 gap（没有找到在 PRM 上同时比较 feature/neuron/circuit 三个粒度的先行工作），但这更像 evaluation/benchmark paper 的贡献而非 idea-level breakthrough。
   - 具体方法几乎全部来自现有工作：from-scratch SAE 来自 CRA，output-score filtering 来自 Arad et al.，neuron-level 来自 CIRM，circuit tracing 来自 RelP/CLT。proposal 的角色更像"集成者"而非"创新者"。

2. **Significance: 中** — 
   - 研究问题（何时机制干预有效）是 2026 年 MI 领域的核心争论，时机很好。Basu et al. vs. SteerRM/CIRM 的对立确实需要系统性的实证研究来调和。
   - 但核心发现如果是 positive（"PRM 干预成功，因为 PRM 满足我们提出的 4 个条件"），审稿人很可能说 **"I would have guessed this"**——PRM 有 scalar output、binary classification、verifiable ground truth，干预成功并不令人意外。如果 negative（干预也失败），则 strengthen Basu et al. 的观点，有一定反直觉价值但仍停留在"在另一个领域重复了失败"。
   - 实用价值层面，多粒度比较对从业者有参考意义，但影响力局限于 PRM debiasing 这个较窄的子领域。

3. **Related Work: 强** — 
   - 对领域的覆盖非常全面：涵盖了 actionability 争论的两方（Basu vs. Orgad）、评估框架（Orgad criteria + Lee criteria）、PRM bias 文献（Tiwari, Wang）、各种干预粒度（SteerRM, CIRM, CRA, probe-level）、circuit 分析工具（RelP, CLT）、self-repair 文献（McGrath）、generative PRM 对比（ThinkPRM, GenPRM）。
   - 差异化定位清晰：明确指出了与 SteerRM（pretrained SAE 局限）、CIRM（单一粒度）、CRA（单一应用场景）的差异。
   - 引用的关键论文经搜索验证均真实存在且描述基本准确（Basu et al.、SteerRM、CIRM、Orgad et al.、Lee et al.、Zhang et al. survey 均已确认）。
   - 唯一的弱点：对 "为什么这 4 个条件而非其他条件" 缺乏来自 related work 的理论支撑。

---

【概率估计】: 

- **投 CoRL 2026**: 0-5%（主题完全不匹配，大概率 desk reject）
- **投主题匹配的 ML 顶会 (NeurIPS/ICML/EMNLP)**: [18% - 28%] 中位 22%

---

【估计理由】: 

对于主题匹配的 ML 顶会（以下分析忽略 CoRL 的不匹配问题）：

该 proposal 的方向正确——actionability 争论是 2026 MI 领域的核心问题，时机好。Related work 覆盖出色，定位清晰。但 **idea 的内核本质上是一个系统性实验比较**（将多种现有方法在 PRM 上统一跑一遍），而非概念或方法上的创新。

概率上界主要受 **Novelty** 限制：
- Domain Amenability Hypothesis 是 N=2 的 post-hoc 归纳，与 Basu et al. 的对比存在严重混淆因素，无法支撑因果性 claim
- 如果核心发现是 positive（PRM 干预有效），审稿人大概率反应是 "I would have guessed this"——这直接限制了 impact 的天花板
- 没有方法论创新——所有具体方法都来自 2024-2026 的现有工作

概率下界由 Related Work 的扎实程度和研究问题的时效性托底——即使 idea 不够 surprising，作为一个高质量的 empirical study 仍有 ~18% 的进入概率。

---

【主要风险】:

1. **"I would have guessed this" 风险**：核心发现（PRM 这种简单任务上干预更成功）几乎是 trivially predictable。审稿人可能认为 Domain Amenability Hypothesis 没有真正的理论贡献，只是对显而易见的事实进行了命名。

2. **因果推断无效风险**：与 Basu et al. 临床 LM 的对比包含太多 confounding factors（模型不同、规模不同、任务不同、训练数据不同），即使结果支持 hypothesis 也无法排除其他解释，审稿人会直接攻击这个 causal claim 的有效性。
```

Sources:
- [Basu et al. - Interpretability without Actionability](https://arxiv.org/abs/2603.18353)
- [SteerRM: Debiasing Reward Models via Sparse Autoencoders](https://arxiv.org/abs/2603.12795)
- [CIRM - Debiasing Reward Models via Causally Motivated Inference-Time Intervention](https://arxiv.org/html/2604.27495)
- [Orgad et al. - Interpretability Can Be Actionable (ICML 2026)](https://arxiv.org/abs/2605.11161)
- [Lee et al. - Rigorous Interpretation Is a Form of Evaluation](https://arxiv.org/html/2605.05508v1)
- [Locate, Steer, and Improve Survey](https://arxiv.org/abs/2601.14004)
- [CRA: Causal Reward Adjustment](https://arxiv.org/abs/2508.04216)
- [Arad et al. - SAEs Are Good for Steering](https://arxiv.org/abs/2505.20063)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "748d3f57-342e-43be-a0b5-ddf78660830c",
  "isSidechain": false,
  "requestId": "req_011CbCdxg6jupSinH2jBQgxL",
  "type": "assistant",
  "uuid": "b4237112-234d-4f2f-aa7a-5a6548799bae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lpdu1itGaWvru3G8kxrTf9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3971,
      "cache_read_input_tokens": 30772,
      "output_tokens": 6187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6187,
          "cache_read_input_tokens": 30772,
          "cache_creation_input_tokens": 3971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3971
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

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # When Do Mechanistic Interventions Succeed? A Multi-Granularity Empirical Test on Process Reward Models  ## Descr…",
  "leafUuid": "b4237112-234d-4f2f-aa7a-5a6548799bae",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Test mechanistic interventions on process reward models",
  "sessionId": "a2f7dbb6-03fd-47b6-8d7b-35fa56aa6aaf"
}
```

---
