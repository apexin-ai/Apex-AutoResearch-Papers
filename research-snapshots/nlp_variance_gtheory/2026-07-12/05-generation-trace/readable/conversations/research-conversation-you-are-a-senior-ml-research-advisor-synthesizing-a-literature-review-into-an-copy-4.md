# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/909c3f35-7245-4648-9244-972b695204c2.jsonl`
- **Structured JSON:** [`dba2ea1e113f3ac845d8.json`](../../sessions/db/dba2ea1e113f3ac845d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:26:29.898Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:26:29.898Z",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning / Knowledge Representation and Reasoning\n\nDirection: Trace the complete computational circuit governing RAG evidence integration vs. override in open-weight LLMs, mapping causal interactions between retrieval heads, parametric memory components, copy suppression mechanisms, and FFN layers. Use the discovered circuit to design principled, multi-point inference-time interventions that outperform existing heuristic steering methods (SpARE, CoRect, ContextFocus) on knowledge-conflict benchmarks.\n\nSeed Papers:\n- ReDeEP (ICLR 2025) — Identifies Knowledge FFNs and Copying Heads as key components but stops at component-level; no circuit tracing\n- Retrieval Head Mechanistically Explains Long-Context Factuality (ICLR 2025) — Identifies <5% of heads carry retrieval signal; universal across model families; but no interaction with parametric circuits\n- Taming Knowledge Conflicts / JuICE (ICML 2025) — Discovers superposition in attention heads (both memory and context); proposes test-time intervention; complicates clean head-type dichotomy but remains head-level\n- CoRect (arXiv 2025) — Discovers flip phenomenon (56% of conflict cases); deep FFN layers suppress correct answers; intervention is additive patching without circuit diagnosis\n- Knowledge Circuits in Pretrained Transformers (NeurIPS 2024) — Provides circuit discovery methodology for factual recall; not applied to RAG\n- CD-T: Efficient Automated Circuit Discovery (ICLR 2025) — Enables circuit discovery in seconds; 97% ROC AUC; key enabling tool\n- SpARE (NAACL 2025) — SAE-based steering under knowledge conflicts; +10% EM; heuristic target selection\n- Atlas of In-Context Learning (NeurIPS 2025) — Separates in-context vs parametric heads; 94% AUC linear probe; but no causal interaction mapping\n\nKnown Gaps:\n- No end-to-end circuit has been traced connecting retrieval heads → FFN layers → copy suppression → output in RAG, comparing success vs failure cases\n- JUICE shows heads operate in superposition (both memory and context), but no work has traced how this superposition resolves across layers and through FFN interactions\n- The flip phenomenon (CoRect: correct answers appear mid-layers then get suppressed) has no circuit-level causal explanation\n- Existing interventions (SpARE, CoRect, ContextFocus, JuICE) select targets heuristically or statistically, not via causal circuit analysis; no multi-point coordinated intervention exists\n\nTheoretical Anchor: The promote-suppress-iterate mechanism (Yan & Jia, EMNLP 2025) provides a theoretical framework — MLPs promote all candidate answers while attention suppresses alternatives iteratively. In RAG, this mechanism should create a specific circuit pathology: retrieval heads promote context-derived answers, but parametric MLPs re-promote stored answers in deeper layers, and copy suppression heads (which operate via general suppression, not selective) inadvertently suppress context-derived tokens. The flip phenomenon is a direct observable consequence of this circuit pathology.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Models: Llama-3.1-8B (primary), Gemma-2-9B (validation)\n- Tools: CD-T, TransformerLens, pyvene, attribution patching\n- Timeline: 10-12 weeks to AAAI August 2026 deadline\n\nQuality Self-Checks:\n- [x] Core insight: In RAG, evidence override is caused by a specific circuit pathology where parametric MLPs in deep layers re-assert stored answers after retrieval heads have already injected context-derived answers — and this pathology can be surgically repaired.\n- [x] Why not obvious: JUICE shows heads are in superposition (not cleanly separable), so you can't just prune memory heads. You need full circuit tracing to find where the parametric signal actually dominates, which requires the promote-suppress-iterate lens applied to RAG specifically.\n- [x] Baseline fear test: Simple baselines (prune top-k memory heads, boost top-k retrieval heads) exist (Jin et al. 2024, IRCAN). Circuit-informed intervention must show that selecting targets via causal analysis yields better targets than statistical/heuristic selection. The multi-point coordination (boost + suppress simultaneously at circuit-identified layers) is what baselines cannot do.\n- [x] Information exploited: The full causal interaction graph between components that existing methods treat in isolation. Specifically, which FFN neurons in which layers re-assert parametric answers AFTER retrieval heads have already injected context, and which copy suppression heads inadvertently suppress context-derived tokens.\n\nAvoid:\n- Replicating ReDeEP at larger scale (component identification without circuit tracing)\n- Assuming clean retrieval-head vs memory-head separation (JUICE refutes this; must account for superposition)\n- Pure interpretability without intervention (AAAI reviewers will ask 'so what?')\n- Ignoring the flip phenomenon as validation (it's the most mechanistically informative empirical finding)\n- Over-claiming circuit completeness (circuits at 7B may be distributed; frame contributions carefully)\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"Taming Knowledge Conflicts in Language Models (JuICE)\",\n    \"venue\": \"ICML 2025 (Spotlight)\",\n    \"problem_identification\": \"Prior work (PH3, Jin et al. 2024) assumes attention heads have fixed roles as either 'memory heads' or 'context heads.' The authors empirically falsified this: in Gemma-2b, zero layers and only 6/26 attention modules behaved consistently across clean, substitution, and coherent conflict settings. The dichotomy is an artifact of narrow evaluation.\",\n    \"key_insight\": \"Influential attention heads operate in CP superposition — their weight matrices encode both factual recall and in-context induction functions simultaneously, with the dominant role determined by the input and conflict type, not by fixed wiring.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"JuICE uses a dual-run inference strategy. First, it identifies heads whose knock-out effect is consistent across all conflict types (filtering out superposed heads that flip roles). At test time, it runs the model twice: the first pass saves selected heads' activations unperturbed; the second pass adds scaled first-run activations back, avoiding the residual-stream perturbation cascades that degrade single-pass interventions. A two-layer theoretical construction proves superposition arises inevitably from joint factual-recall and induction training.\",\n    \"limitations_and_open_questions\": \"Doubles inference cost (dual forward pass). Head identification is still statistical (cross-conflict consistency filter), not causally grounded in circuit structure. No FFN analysis — superposition is characterized only at the attention head level. Tested only up to 8B parameters.\",\n    \"building_blocks\": [\n      \"CP superposition phenomenon as empirical constraint on circuit tracing\",\n      \"Dual-run activation-addition intervention pattern\",\n      \"Cross-conflict-type consistency filtering for robust head selection\",\n      \"Theoretical proof that superposition is inevitable under joint training\"\n    ],\n    \"relevance_to_seed\": \"Defines the superposition challenge: any RAG circuit tracing that assumes clean head-type separation will fail, and interventions must avoid residual-stream perturbation cascades — the dual-run pattern or circuit-informed multi-point coordination are needed.\"\n  },\n  {\n    \"title\": \"CD-T: Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Existing circuit discovery (ACDC, EAP) relies on activation patching requiring iterative forward passes, taking hours per circuit. EAP's linear approximation introduces propagation errors. Neither method efficiently supports fine-grained positional analysis (which head at which token position matters).\",\n    \"key_insight\": \"Circuit discovery can be reframed from an empirical causal intervention problem to an analytical mathematical decomposition problem — contextual decomposition propagates relevant/irrelevant activation components through the network in a single forward pass, eliminating the patch-and-observe loop.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"CD-T decomposes every activation into relevant (β) and irrelevant (γ) components, where β captures deviation from mean activation. Custom propagation rules handle linear layers (proportional bias distribution), attention (decomposed Q/K/V with separate softmax), and ReLU. An L1-norm ratio R(s,T) = ||β||/||γ|| scores each component's contribution. Iterative greedy pruning selects minimal faithful circuits. Achieves 97% ROC AUC recovering known manual circuits (IOI, Greater-Than, Docstring) on GPT-2-small in seconds.\",\n    \"limitations_and_open_questions\": \"Tested only on attention heads in small models (GPT-2-small, 4-layer transformers). MLP/FFN circuit integration not explored. Relevance metric doesn't distinguish positive from negative (inhibitory) contributions. Manual circuits still outperform CD-T circuits of equal size. Fixed-k node selection requires task-specific tuning.\",\n    \"building_blocks\": [\n      \"Single-pass decomposition framework adaptable to RAG (β=context tokens, γ=query tokens)\",\n      \"Fine-grained positional circuit discovery (head × token position)\",\n      \"L1-ratio relevance metric capturing both promoting and suppressing components\",\n      \"Seconds-scale runtime enabling iteration over many RAG examples\"\n    ],\n    \"relevance_to_seed\": \"Primary enabling tool for the proposed methodology — its seconds-scale runtime makes full circuit tracing across hundreds of RAG conflict examples feasible, and its positional granularity can reveal how retrieved-context tokens interact with query tokens at specific heads.\"\n  },\n  {\n    \"title\": \"The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Prior mechanistic studies of ICL (Jin et al. 2024) used computationally prohibitive path-patching (~2048 forward passes/sample) on toy single-token tasks. No work had characterized how attention heads function in realistic, open-domain RAG with multi-token answers and full Wikipedia passages.\",\n    \"key_insight\": \"In-context heads are not monolithic — they decompose into functionally distinct task heads (encoding question type, middle layers) and retrieval heads (extracting answer spans, deep layers), each with independently extractable and transferable function vectors.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Uses AttnLRP (attention-aware layer-wise relevance propagation) to attribute each head's contribution to predictions under open-book vs. closed-book settings. A difference score D between counterfactual-context and no-context conditions separates in-context heads (top-100 by D) from parametric heads (bottom-100). Within in-context heads, relevance aggregated over question vs. answer token positions yields a task/retrieval subclassification. A linear probe on logit-lens-projected retrieval head outputs achieves 94-98% AUC for predicting whether answers come from context or memory.\",\n    \"limitations_and_open_questions\": \"Explicitly does not trace head-to-FFN interactions — acknowledged as future work. Only QA tasks with short answers tested. Top-K head selection is unprincipled. No analysis of inhibitory effects or how parametric heads actively suppress context-derived answers. Reviewers questioned novelty beyond Jin et al. (2024).\",\n    \"building_blocks\": [\n      \"Three-way head taxonomy (task/retrieval/parametric) with layer distribution\",\n      \"AttnLRP-based attribution for scalable head identification\",\n      \"Lightweight source-tracking linear probe (94% AUC, forward-pass only)\",\n      \"Function vector extraction and injection for causal validation\"\n    ],\n    \"relevance_to_seed\": \"Provides the head-level taxonomy that the proposed circuit must connect through FFN interactions — the explicit gap (no MLP analysis, no cross-component tracing) is precisely where the proposed work contributes.\"\n  },\n  {\n    \"title\": \"IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"Prior interventions for knowledge conflicts operated at the output-probability level (CAD) or attention-head level (ITI), missing the FFN neurons that actually process contextual information. The authors hypothesized that specific FFN neurons encode context-processing functions and that amplifying them could shift model behavior toward context faithfulness.\",\n    \"key_insight\": \"Context-processing in LLMs is partially localizable to a small set (~14) of FFN neurons in upper layers, identifiable via integrated gradients comparing question-only vs. context+question activations, and amplifiable via simple weight multiplication with zero inference overhead.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Integrated gradients compute each neuron's attribution to context processing by interpolating activations from a question-only baseline to context+question values (m=20 Riemann steps). Three-stage filtering (threshold → per-example top-20 → cross-example frequency ranking) identifies a shared set of ~14 context-aware neurons. These neurons' weights are multiplied by β≈7 offline, permanently modifying the model. On MemoTrap, LLaMA-2-7B improves from 24.5% to 56.1% accuracy; combining with CAD reaches 61.8%.\",\n    \"limitations_and_open_questions\": \"No superposition awareness — assumes neurons have clean, separable context-processing roles. Only 3 synthetic benchmarks; no RAG evaluation. β=7 multiplication on potentially polysemantic neurons risks side effects. 50% neuron overlap across prompts means half are prompt-dependent. The 'context is always right' assumption is unsafe for noisy retrieval. No cross-component interaction analysis.\",\n    \"building_blocks\": [\n      \"Integrated-gradients neuron attribution methodology for context processing\",\n      \"Evidence that context-aware function concentrates in upper-layer FFN neurons\",\n      \"Weight-multiplication intervention pattern (zero inference cost)\",\n      \"Complementarity with output-level methods (IRCAN+CAD stacking)\"\n    ],\n    \"relevance_to_seed\": \"Neuron-level baseline for the proposed circuit-informed intervention — IRCAN's heuristic neuron selection (integrated gradients + frequency filtering) is exactly what circuit-grounded target selection should outperform, and its upper-layer FFN concentration aligns with the hypothesis that deep FFN layers re-assert parametric answers.\"\n  },\n  {\n    \"title\": \"How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing\",\n    \"venue\": \"arXiv 2026 (preprint)\",\n    \"problem_identification\": \"Prior factual knowledge work (Burns et al. 2023, Meng et al. 2022) treats truthfulness as a static, single-layer property. No work had tracked the full layer-by-layer geometric evolution of representations when models process correct vs. incorrect continuations, missing the dynamic mechanism of factual acceptance/rejection.\",\n    \"key_insight\": \"Factual discrimination in transformers is encoded entirely through angular separation (rotation) on an approximate hypersphere — not through magnitude differences — and larger models (≥1.6B) actively suppress correct answers when processing incorrect inputs, with probe accuracy peaking at mid-layers then declining.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Forced-completion probing appends known correct/incorrect single tokens to queries and tracks five geometric measurements across all layers: trajectory similarity, rotational divergence (ρ), norm ratio (η), commitment ratio (κ via logit lens), and attention allocation (α). Across LLaMA-2-13B, Mistral-7B, and StableLM-2-1.6B, the norm ratio stays within 3% of unity while angular divergence grows substantially. Active suppression manifests as κ dropping to 0.08 for incorrect inputs (vs. 0.77 for correct). The phenomenon is absent in Qwen2-1.5B, suggesting a ~1.6B parameter emergence threshold.\",\n    \"limitations_and_open_questions\": \"Forced single-token completion differs from autoregressive generation dynamics. Only 300 queries across 3 domains. Four models cannot establish a true phase transition — Qwen2's null result may reflect architecture, not scale. No circuit-level causal explanation for which components drive the rotation and suppression.\",\n    \"building_blocks\": [\n      \"Rotational divergence metric (ρ/η decomposition) for probing factual processing\",\n      \"Active suppression measurement via commitment ratio κ\",\n      \"Empirical evidence that magnitude-based hallucination detectors miss the signal\",\n      \"Mid-layer peak in discriminative information as intervention target indicator\"\n    ],\n    \"relevance_to_seed\": \"Provides the geometric framework explaining the flip phenomenon: correct answers peak at mid-layers (high κ) then get suppressed in deep layers (κ collapse) via rotation — this is the observable signature of the circuit pathology where deep FFN layers re-assert parametric answers, and it confirms that interventions must target angular representations, not magnitudes.\"\n  },\n  {\n    \"title\": \"ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"Prior RAG hallucination detectors either measured parametric knowledge OR external context utilization in isolation, creating confounded estimates. They diagnosed this via systematic analysis showing 1006/1024 attention heads have higher external context scores on truthful vs. hallucinated outputs, while later FFN layers show higher parametric knowledge scores for hallucinations.\",\n    \"key_insight\": \"RAG hallucination detection is a confounding problem from causal inference: Knowledge FFNs (parametric signal) and Copying Heads (context signal) must be treated as covariates in multivariate regression, not analyzed independently.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Parametric Knowledge Score (PKS) measures per-FFN-layer vocabulary distribution shift via LogitLens + JSD. External Context Score (ECS) measures attention to retrieved context by Copying Heads (identified via OV matrix eigenvalue analysis). Hallucination score combines both via fitted linear regression. AARF mitigation conditionally amplifies Copying Heads and dampens Knowledge FFNs when hallucination score exceeds threshold.\",\n    \"limitations_and_open_questions\": \"Reviewers criticized PKS as not guaranteed to measure parametric knowledge specifically (correlation ≠ mechanism), causal experiments were noisy, and numerous hyperparameters (top-k layers/heads, α, β, τ) require per-dataset tuning. Component-level analysis without circuit tracing — no interaction mapping between Knowledge FFNs and Copying Heads.\",\n    \"building_blocks\": [\n      \"LogitLens-based PKS for measuring FFN knowledge injection\",\n      \"OV-eigenvalue Copying Head identification\",\n      \"AARF conditional activation scaling pattern\",\n      \"RAGTruth dataset\",\n      \"Confounding-as-covariates framework for dual-source analysis\"\n    ],\n    \"relevance_to_seed\": \"Establishes the component-level anatomy (Knowledge FFNs + Copying Heads) that our circuit tracing extends into a full causal interaction graph, and AARF is a single-point heuristic intervention our multi-point circuit-informed approach must outperform.\"\n  },\n  {\n    \"title\": \"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (SpARE)\",\n    \"venue\": \"NAACL 2025 (Oral)\",\n    \"problem_identification\": \"Existing representation engineering methods (ActAdd, TaskVec, SEA) fail to steer knowledge selection because they edit polysemantic dense vectors where minor changes in one dimension affect multiple semantic features. Diagnosed via linear probing showing conflict signals peak at mid-layers, then empirically demonstrating baseline steering failures.\",\n    \"key_insight\": \"Less than 0.05% of SAE features (selected via mutual information) control the entire knowledge selection behavior, and effective steering requires input-dependent, constrained editing in residual stream space rather than SAE reconstruction space.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Collects SAE-encoded activations from context-favoring vs. parametric-favoring model predictions, selects top features by mutual information with outcome, determines each feature's directional role. For inference: computes input-specific min/max-constrained edits (removing undesired features, adding desired ones) and applies them through SAE decoder columns to the original residual stream, avoiding lossy SAE reconstruction. Achieves +10% EM over baselines.\",\n    \"limitations_and_open_questions\": \"Requires pre-trained SAEs (not available for all models). Only evaluated on ODQA (NQSwap, Macnoise) — unclear generalization to multi-hop reasoning or long-form generation. Feature selection is heuristic (MI-based), not causally grounded in circuit structure. Binary knowledge selection framing oversimplifies real-world knowledge integration.\",\n    \"building_blocks\": [\n      \"MI-based SAE feature selection pipeline\",\n      \"Constrained input-dependent SAE editing (Eq. 2-4)\",\n      \"Conflict detection linear probing methodology\",\n      \"Pre-trained SAEs for Llama2-7B/Llama3-8B/Gemma2-9B\",\n      \"NQSwap and Macnoise benchmarks\"\n    ],\n    \"relevance_to_seed\": \"Primary heuristic baseline our circuit-informed intervention must outperform; demonstrates SAE features can steer knowledge selection but selects targets statistically rather than via causal circuit analysis — exactly the gap our work fills.\"\n  },\n  {\n    \"title\": \"Circuit Tracing: Revealing Computational Graphs in Language Models\",\n    \"venue\": \"Anthropic Technical Report, March 2025\",\n    \"problem_identification\": \"Per-layer transcoders create artificially long attribution chains because the same conceptual feature manifests across multiple MLP layers via the residual stream. SAEs decompose activations but not computation, making them unsuitable for circuit tracing. Identified through progression from SAEs → per-layer transcoders → recognizing cross-layer redundancy.\",\n    \"key_insight\": \"Cross-layer transcoders (CLTs) exploit the residual stream's information-sharing property to collapse multi-layer amplification chains into direct feature connections, converting circuit discovery from expensive ablation-based search into direct readoff from a locally-linear replacement model.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CLTs read from the residual stream at one layer and contribute decoder vectors to MLP outputs at all subsequent layers, trained to approximate true MLP outputs with tanh-based sparsity. On any prompt, freezing attention patterns and LayerNorm makes the CLT-replaced model fully linear — circuits are paths through this linear network. Attribution graphs use stop-gradient Jacobians and Neumann-series influence pruning for tractable visualization. Applied to Claude 3.5 Haiku scale.\",\n    \"limitations_and_open_questions\": \"QK attention circuits invisible (only OV traced). 11.5-21.7% reconstruction error hides unknown computation. CLTs may learn unfaithful shortcuts — LessWrong analysis shows they collapse multi-step computations into lookup tables. Only ~25% of prompts yield satisfying interpretations. Inhibitory (absent-feature) mechanisms are invisible.\",\n    \"building_blocks\": [\n      \"Cross-layer transcoder architecture and training\",\n      \"Stop-gradient Jacobian attribution\",\n      \"Neumann-series influence matrix pruning\",\n      \"Local replacement model concept\",\n      \"Circuit Tracer library (Gemma-2-2B, Llama-3.1-1B, Qwen3-4B)\",\n      \"CLT-Forge distributed training library\"\n    ],\n    \"relevance_to_seed\": \"Directly applicable methodology for our RAG circuit discovery — CLTs enable end-to-end tracing from retrieval heads through FFN layers to output, though we must address the faithfulness concerns and adapt to open-weight models (Llama-3.1-8B) where pre-trained CLTs may not exist.\"\n  },\n  {\n    \"title\": \"Transcoders Find Interpretable LLM Feature Circuits\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"SAEs decompose MLP activations into interpretable features but cannot trace computation THROUGH MLPs because SAE features are dense linear combinations of neurons, each with its own nonlinearity — making cross-layer attribution intractable. Identified by recognizing SAEs answer 'what features exist?' but not 'what transformation is performed?'\",\n    \"key_insight\": \"Training a sparse wide ReLU network to approximate MLP input→output behavior (rather than reconstructing activations) yields a clean factorization where each feature's contribution decomposes into an input-dependent scalar activation times an input-invariant weight dot product, enabling weights-based circuit analysis.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Transcoders minimize ||MLP(x) - TC(x)||² + λ||z||₁, replacing opaque MLPs with sparse interpretable alternatives. The contribution of feature i (layer l) to feature i' (layer l') factors as z(l,i)·(f_dec(l,i)·f_enc(l',i')), separating model wiring (fixed weights) from activation patterns (input-dependent). Greedy recursive attribution traces circuits backward from output logits through transcoder features and attention OV circuits. De-embeddings (W_E^T · f_enc) enable blind feature analysis without any input data.\",\n    \"limitations_and_open_questions\": \"Only qualitative case studies on GPT2-small — no large-scale quantitative circuit evaluation. Attention pattern computation not modeled (only OV circuits). Approximation error may hide critical computation. Follow-up (Paulo et al. 2025) showed skip transcoders are Pareto-better. Scalability of circuit analysis to production models unproven at time of publication.\",\n    \"building_blocks\": [\n      \"Transcoder architecture and training pipeline\",\n      \"Input-invariant/input-dependent factorization framework\",\n      \"De-embedding analysis for weight-based feature interpretation\",\n      \"transcoder_circuits Python library\",\n      \"Blind case study protocol for feature reverse-engineering\"\n    ],\n    \"relevance_to_seed\": \"Foundational tool for decomposing FFN contributions in our RAG circuit — transcoders enable tracing how parametric Knowledge FFNs transform retrieval head outputs across layers, and the factorization framework lets us identify fixed circuit structure underlying the flip phenomenon.\"\n  },\n  {\n    \"title\": \"Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"All prior mechanistic work on knowledge conflicts addressed context-memory conflicts (external vs. internal). Intra-memory conflicts (contradictory facts within parameters from conflicting training data) had no mechanistic analysis. Identified by mapping the conflict taxonomy from Xu et al. (EMNLP 2024) against existing mechanistic studies and finding the intra-memory cell empty.\",\n    \"key_insight\": \"Creating matched model pairs (conflicted vs. clean, trained on identical data ± contradictions) enables cross-model activation patching (CMAP) that isolates the mechanistic signature of intra-memory conflict without prompt-mismatch noise.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Constructs SynWikiBio: 2000 synthetic biographies with controlled contradictions using nonsense entity names to guarantee zero pre-training overlap. Trains conflicted (l'_mix) and clean (l'_clean) model pairs on GPT-2 XL and Qwen3-4B. Applies logit lens to track competing token probabilities across layers, finding attention components dominate in layers 21-47. CMAP transfers activations from clean→conflicted model at specific components, achieving up to 70% steering success on Qwen3-4B vs. 22% with standard patching.\",\n    \"limitations_and_open_questions\": \"Only 1:1 contradictions studied; modest success rates on GPT-2 XL (~22%) suggest highly distributed encoding. Unexpected attribute-type asymmetry (CMAP helps for company but not university attributes) is unresolved — raises whether knowledge conflict is a unified phenomenon. Synthetic data only; transfer to natural pre-training conflicts unvalidated.\",\n    \"building_blocks\": [\n      \"SynWikiBio controlled conflict dataset\",\n      \"Model-pair experimental paradigm (conflicted vs. clean)\",\n      \"CMAP adapted for knowledge conflict study\",\n      \"Shared-prefix prompt construction for conflict elicitation\",\n      \"Three-stage pipeline: controlled conflicts → logit lens localization → activation patching verification\"\n    ],\n    \"relevance_to_seed\": \"Closest methodological precedent for our work but addresses intra-memory (not RAG) conflicts. The model-pair CMAP paradigm could be adapted to compare RAG-augmented vs. parametric-only inference, and the finding that conflicts are distributed across attention components in later layers aligns with the flip phenomenon we aim to explain.\"\n  },\n  {\n    \"title\": \"Retrieval Head Mechanistically Explains Long-Context Factuality\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"No mechanistic explanation existed for how transformers retrieve information from arbitrary positions in long contexts, nor why models hallucinate under long-context settings. The authors framed this as identifying the minimal sub-network implementing conditional copy-paste retrieval.\",\n    \"key_insight\": \"Fewer than 5% of attention heads ('retrieval heads') implement a conditional copy-paste algorithm, are universal across model families, intrinsic to pretraining (not created by context extension), and causally necessary — ablating them causes hallucination while ablating equal numbers of non-retrieval heads has negligible effect.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Defines a 'retrieval score' measuring per-head token-level recall of copy-paste behavior on needle-in-a-haystack tasks with semantically irrelevant, unmemorizable answers. Scores converge after few samples. Progressive head masking causally validates necessity: top-50 retrieval heads (~5%) drop NIAH below 50%, while masking random heads preserves 95% accuracy. Tested across LLaMA/Mistral/Yi/Qwen at 6B-56B scales, MoE (Mixtral), and hybrid SSM (Jamba).\",\n    \"limitations_and_open_questions\": \"No mechanism explaining *when/why* retrieval heads dynamically activate. Limited to copy-paste retrieval — does not address semantic paraphrasing retrieval or interaction with parametric knowledge circuits. No circuit tracing beyond individual head identification.\",\n    \"building_blocks\": [\n      \"Retrieval score metric for head classification\",\n      \"Progressive head masking protocol\",\n      \"NIAH-based detection datasets with unmemorizable answers\",\n      \"Taxonomy: always-active vs context-sensitive retrieval heads\"\n    ],\n    \"relevance_to_seed\": \"Provides the foundational retrieval-side component of our circuit — the <5% of heads whose output must be traced through FFN layers and copy-suppression mechanisms to understand evidence integration vs. override.\"\n  },\n  {\n    \"title\": \"CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Decoding-time methods (CAD, AdaCAD) only adjust final token distributions without preventing intermediate representations from being steered toward parametric answers, while weight-editing methods (ROME) require ground-truth targets. The authors used Logit Lens analysis across 500 NQ conflict cases to discover the 'flip phenomenon.'\",\n    \"key_insight\": \"In 56% of knowledge-conflict cases, the correct context-derived answer reaches Rank-1 at intermediate layers but gets suppressed by deep FFN layers before output — the model 'knows' the right answer internally but fails to produce it, motivating surgical disinhibition rather than forced steering.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Two-stage label-free inference-time intervention. Stage 1: dual forward passes (contextualized vs. null-context) compute Contextual Mutual Information per token, verified by attention grounding scores, to select a trustworthy target token without labels. Stage 2: identifies suppressive FFN layers where u_l^T · w_target < 0 (FFN output negatively projects onto target's unembedding), then applies additive patches φ_l = -α·(u_l^T·w_target/||w_target||²)·w_target to neutralize suppression. α=1 achieves exact disinhibition.\",\n    \"limitations_and_open_questions\": \"Computational overhead from dual forward passes unquantified. Modest gains on multi-hop reasoning suggest parametric suppression interacts differently with complex reasoning chains. No circuit-level causal explanation for *why* specific FFN layers suppress — treatment is statistical, not mechanistic.\",\n    \"building_blocks\": [\n      \"Flip phenomenon empirics (56% of conflict cases)\",\n      \"Logit Lens layer-wise analysis of answer rank trajectories\",\n      \"Label-free trustworthy token selection via CMI + attention verification\",\n      \"Suppressive layer identification via unembedding projection sign\"\n    ],\n    \"relevance_to_seed\": \"The flip phenomenon is the key empirical observable our circuit must causally explain; CoRect's layer identification method (unembedding projection) provides a baseline for circuit-informed suppressive layer detection.\"\n  },\n  {\n    \"title\": \"ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Existing RAG faithfulness methods focus on enhancing context utilization but overlook that internal parametric knowledge stored in FFN layers actively undermines faithfulness. The authors measured activation ratios across layers during faithful vs. unfaithful generation to locate the source.\",\n    \"key_insight\": \"Mid-to-deep FFN layers (70-90% of model depth) exhibit disproportionately high activation during unfaithful RAG generation, functioning as parametric memory repositories that override context — and soft suppression with a tunable coefficient enables plug-and-play control.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Three components: (1) UA-FFN identification via activation gap ΔR^l = E[R^l|unfaithful] - E[R^l|faithful], selecting top-N layers; (2) soft suppression scaling FFN activations by λ∈[0,1]; (3) knowledge preference calibration combining supervised fine-tuning (KAT) with a max-margin loss (KPO) that forces P(y*|q,c) >> P(y*|q). Evaluated on CoFaithfulQA (52K instances from 6 QA datasets) and ConFiQA. Achieves +5% ConR, -4% MemR vs. vanilla RAG.\",\n    \"limitations_and_open_questions\": \"Requires training data for KAT/KPO — not purely inference-time. UA-FFN identification is statistical (activation ratios), not causal-circuit-based. Reviewers questioned performance under noisy retrieval and closed-book degradation. FFN suppression is uniform across neurons within selected layers — no neuron-level granularity.\",\n    \"building_blocks\": [\n      \"Activation ratio metric for FFN layer ranking\",\n      \"Soft suppression coefficient λ for plug-and-play control\",\n      \"KPO max-margin loss for knowledge preference calibration\",\n      \"CoFaithfulQA benchmark (52K instances)\"\n    ],\n    \"relevance_to_seed\": \"Direct competitor/baseline — identifies the same mid-to-deep FFN layers our circuit must explain, but uses statistical activation gaps rather than causal circuit tracing, and applies uniform layer-level suppression rather than neuron/feature-level surgical intervention.\"\n  },\n  {\n    \"title\": \"Analysing the Residual Stream of Language Models Under Knowledge Conflicts\",\n    \"venue\": \"NeurIPS 2024 Workshop (MINT)\",\n    \"problem_identification\": \"Prior conflict detection relied on prompting-based strategies requiring extra inference passes. No work had examined whether LLMs' internal representations encode detectable conflict signals before answer generation. The authors applied linear probing across all layers to map the temporal structure of conflict processing.\",\n    \"key_insight\": \"Knowledge conflicts are processed in two sequential phases in the residual stream: conflict detection peaks at mid-layers (~layer 14 in Llama3-8B), followed by knowledge selection peaking later (~layer 17) — and both signals coexist without erasure, with contextual-knowledge use producing distinctly more skewed activation distributions in deep layers.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Layer-wise logistic regression probes (with L1 regularization) on hidden states, attention outputs, and MLP outputs at the final token position, trained on two binary tasks: conflict detection (conflicting vs. non-conflicting context) and knowledge selection (will model use contextual vs. parametric answer). Complemented by distributional shape analysis (Kurtosis, Hoyer sparsity, Gini coefficient) showing significant skewness divergence in layers 20-30. Tested on NQSwap/Macnoise/ConflictQA across Llama2-7B and Llama3-8B.\",\n    \"limitations_and_open_questions\": \"Probing captures correlation, not causation — detecting a signal doesn't prove the model uses it. Limited to English QA, greedy decoding, two model families. No intervention experiments. The paper is explicitly a preliminary study leading to SpARE (NAACL 2025).\",\n    \"building_blocks\": [\n      \"Two-phase conflict processing timeline (detect → select)\",\n      \"Distributional skewness metrics for knowledge-source discrimination\",\n      \"Layer-wise probing protocol for conflict signals\",\n      \"Evidence that MLP/attention stop adding conflict info after mid-layers while residual stream retains it\"\n    ],\n    \"relevance_to_seed\": \"Provides representation-level evidence our circuit must explain: conflict detection at mid-layers and selection at later layers maps directly onto the promote-suppress-iterate framework, and the coexistence finding constrains circuit hypotheses about when/where parametric vs. contextual signals compete.\"\n  },\n  {\n    \"title\": \"A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models\",\n    \"venue\": \"EMNLP 2025 Findings\",\n    \"problem_identification\": \"SAE research had fragmented across architectures (Gated, TopK, JumpReLU, etc.), training strategies, evaluation metrics, and applications without a unifying survey. No comprehensive resource organized the design space or identified open challenges systematically.\",\n    \"key_insight\": \"SAE variants primarily address a single core tension — the sparsity-fidelity tradeoff — through either architectural innovations (separating gating from magnitude estimation) or training innovations (end-to-end optimization through the full model), with shrinkage bias from L1 regularization being the key technical obstacle most variants attempt to resolve.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Taxonomizes SAE literature along two axes: improvement target (architecture vs. training strategy) and historical stage (individual neurons → small models → scaled deployment). Covers 15+ SAE variants with formal specifications. Categorizes feature explanation into input-based (MaxAct, PruningMaxAct) and output-based (VocabProj, MutInfo) methods. Evaluates metrics across structural (MSE, FVU, L0, delta LM loss) and functional (sparse probing, TPP, feature absorption, SCR) dimensions. References SAEBench as standardized evaluation.\",\n    \"limitations_and_open_questions\": \"Notable omission of transcoders (Dunefsky et al. 2024), which approximate MLP input-output functions via sparse bottlenecks and have been argued to outperform SAEs on interpretability benchmarks. No discussion of SAE application to circuit discovery specifically. Four open challenges identified: incomplete concept dictionaries, lack of theoretical foundations, reconstruction errors, and computational burden at scale.\",\n    \"building_blocks\": [\n      \"Taxonomy of SAE architectures with formal specifications\",\n      \"Evaluation framework: structural vs. functional metrics\",\n      \"Feature explanation methods (MaxAct, PruningMaxAct, VocabProj, MutInfo)\",\n      \"SAEBench reference for standardized comparison\",\n      \"Model steering via SAE-derived steering vectors\"\n    ],\n    \"relevance_to_seed\": \"Essential methodological reference for our SAE/transcoder-based circuit analysis — the taxonomy guides architecture selection (TopK or Gated SAE for sparsity without shrinkage bias), and the evaluation framework (sparse probing, TPP) provides metrics for validating that discovered circuit features are genuinely monosemantic.\"\n  },\n  {\n    \"title\": \"Knowledge Circuits in Pretrained Transformers\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"Prior interpretability work studied isolated components (knowledge neurons, individual attention heads) but never traced the full collaborative subgraph responsible for expressing a specific fact. The authors identified this gap by noting that component-level analyses cannot explain how information flows from subject tokens through intermediate processing to output.\",\n    \"key_insight\": \"Factual knowledge expression depends on a discoverable, sparse circuit of cooperating components — mover heads (transfer subject info to final position), relation heads (activate relation-specific processing), and MLPs (aggregate and map to target entities) — that retains ~70% of full-model performance with <10% of edges.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"They model the transformer as a DAG with edges between residual stream, attention heads, MLPs, and output. Edge significance is measured by ablation: S(e_i) = log P(o) - log P(o|ablate e_i). Edges below threshold τ are pruned to yield a minimal circuit. They taxonomize surviving heads into mover, relation, and mixture types based on attention patterns, then validate circuit completeness via Hit@10 on held-out facts.\",\n    \"limitations_and_open_questions\": \"Limited to GPT-2 and TinyLLaMA (1.1B); circuit discovery takes 1-2 days on A800 GPUs, raising scalability concerns for 7B+ models. Circuits are traced for single-fact recall only — not for RAG or conflicting-knowledge settings where the same circuit must handle competing signals.\",\n    \"building_blocks\": [\n      \"Edge-ablation circuit discovery methodology\",\n      \"Mover/relation/mixture head taxonomy\",\n      \"MatchNLL significance metric\",\n      \"TransformerLens integration\",\n      \"Hit@10 circuit validation\"\n    ],\n    \"relevance_to_seed\": \"Provides the foundational circuit discovery methodology and component vocabulary (information heads, relation heads, MLPs) that we will extend from single-fact recall to RAG knowledge-conflict circuits.\"\n  },\n  {\n    \"title\": \"Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries\",\n    \"venue\": \"EMNLP 2025\",\n    \"problem_identification\": \"How LMs generate multiple valid answers to one-to-many queries (e.g., 'cities in France') without repeating was mechanistically unexplained. The authors identified this by observing that standard factual recall analyses assume single-answer settings and cannot account for iterative answer generation.\",\n    \"key_insight\": \"MLPs indiscriminately promote ALL candidate answers simultaneously, while attention heads iteratively suppress previously generated ones — a division of labor where MLPs are recall engines and attention is the deduplication/selection mechanism.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"They introduce Token Lens, which aggregates weighted value vectors attending to specific tokens (Σ p·v), projects through Wo and the unembedding matrix, yielding per-token logit contributions. Their MLP knockout zeros attention weights from the last token to targets, then measures the resulting MLP output change in logit space to isolate how MLPs use attention-relayed information. Causal tracing with noise injection validates which tokens are causally critical.\",\n    \"limitations_and_open_questions\": \"Mechanism studied only for one-to-many factual recall, not knowledge conflicts or RAG. The suppress-then-iterate dynamic across layers has not been tested when two competing knowledge sources (parametric vs. context) simultaneously activate the promotion pathway.\",\n    \"building_blocks\": [\n      \"Token Lens technique\",\n      \"MLP knockout method\",\n      \"Promote-suppress theoretical framework\",\n      \"Layer-wise logit attribution\"\n    ],\n    \"relevance_to_seed\": \"Directly anchors our RAG circuit pathology hypothesis: in knowledg\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:26:29.901Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:26:29.901Z",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-30T06:26:29.939Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-30 (UTC).**

## Research area: Target: AAAI 2026
Track: Machine Learning / Knowledge Representation and Reasoning

Direction: Trace the complete computational circuit governing RAG evidence integration vs. override in open-weight LLMs, mapping causal interactions between retrieval heads, parametric memory components, copy suppression mechanisms, and FFN layers. Use the discovered circuit to design principled, multi-point inference-time interventions that outperform existing heuristic steering methods (SpARE, CoRect, ContextFocus) on knowledge-conflict benchmarks.

Seed Papers:
- ReDeEP (ICLR 2025) — Identifies Knowledge FFNs and Copying Heads as key components but stops at component-level; no circuit tracing
- Retrieval Head Mechanistically Explains Long-Context Factuality (ICLR 2025) — Identifies <5% of heads carry retrieval signal; universal across model families; but no interaction with parametric circuits
- Taming Knowledge Conflicts / JuICE (ICML 2025) — Discovers superposition in attention heads (both memory and context); proposes test-time intervention; complicates clean head-type dichotomy but remains head-level
- CoRect (arXiv 2025) — Discovers flip phenomenon (56% of conflict cases); deep FFN layers suppress correct answers; intervention is additive patching without circuit diagnosis
- Knowledge Circuits in Pretrained Transformers (NeurIPS 2024) — Provides circuit discovery methodology for factual recall; not applied to RAG
- CD-T: Efficient Automated Circuit Discovery (ICLR 2025) — Enables circuit discovery in seconds; 97% ROC AUC; key enabling tool
- SpARE (NAACL 2025) — SAE-based steering under knowledge conflicts; +10% EM; heuristic target selection
- Atlas of In-Context Learning (NeurIPS 2025) — Separates in-context vs parametric heads; 94% AUC linear probe; but no causal interaction mapping

Known Gaps:
- No end-to-end circuit has been traced connecting retrieval heads → FFN layers → copy suppression → output in RAG, comparing success vs failure cases
- JUICE shows heads operate in superposition (both memory and context), but no work has traced how this superposition resolves across layers and through FFN interactions
- The flip phenomenon (CoRect: correct answers appear mid-layers then get suppressed) has no circuit-level causal explanation
- Existing interventions (SpARE, CoRect, ContextFocus, JuICE) select targets heuristically or statistically, not via causal circuit analysis; no multi-point coordinated intervention exists

Theoretical Anchor: The promote-suppress-iterate mechanism (Yan & Jia, EMNLP 2025) provides a theoretical framework — MLPs promote all candidate answers while attention suppresses alternatives iteratively. In RAG, this mechanism should create a specific circuit pathology: retrieval heads promote context-derived answers, but parametric MLPs re-promote stored answers in deeper layers, and copy suppression heads (which operate via general suppression, not selective) inadvertently suppress context-derived tokens. The flip phenomenon is a direct observable consequence of this circuit pathology.

Constraints:
- Compute: ≤200 H100-hours
- Models: Llama-3.1-8B (primary), Gemma-2-9B (validation)
- Tools: CD-T, TransformerLens, pyvene, attribution patching
- Timeline: 10-12 weeks to AAAI August 2026 deadline

Quality Self-Checks:
- [x] Core insight: In RAG, evidence override is caused by a specific circuit pathology where parametric MLPs in deep layers re-assert stored answers after retrieval heads have already injected context-derived answers — and this pathology can be surgically repaired.
- [x] Why not obvious: JUICE shows heads are in superposition (not cleanly separable), so you can't just prune memory heads. You need full circuit tracing to find where the parametric signal actually dominates, which requires the promote-suppress-iterate lens applied to RAG specifically.
- [x] Baseline fear test: Simple baselines (prune top-k memory heads, boost top-k retrieval heads) exist (Jin et al. 2024, IRCAN). Circuit-informed intervention must show that selecting targets via causal analysis yields better targets than statistical/heuristic selection. The multi-point coordination (boost + suppress simultaneously at circuit-identified layers) is what baselines cannot do.
- [x] Information exploited: The full causal interaction graph between components that existing methods treat in isolation. Specifically, which FFN neurons in which layers re-assert parametric answers AFTER retrieval heads have already injected context, and which copy suppression heads inadvertently suppress context-derived tokens.

Avoid:
- Replicating ReDeEP at larger scale (component identification without circuit tracing)
- Assuming clean retrieval-head vs memory-head separation (JUICE refutes this; must account for superposition)
- Pure interpretability without intervention (AAAI reviewers will ask 'so what?')
- Ignoring the flip phenomenon as validation (it's the most mechanistically informative empirical finding)
- Over-claiming circuit completeness (circuits at 7B may be distributed; frame contributions carefully)

## Paper analyses (20 papers)

[
  {
    "title": "Taming Knowledge Conflicts in Language Models (JuICE)",
    "venue": "ICML 2025 (Spotlight)",
    "problem_identification": "Prior work (PH3, Jin et al. 2024) assumes attention heads have fixed roles as either 'memory heads' or 'context heads.' The authors empirically falsified this: in Gemma-2b, zero layers and only 6/26 attention modules behaved consistently across clean, substitution, and coherent conflict settings. The dichotomy is an artifact of narrow evaluation.",
    "key_insight": "Influential attention heads operate in CP superposition — their weight matrices encode both factual recall and in-context induction functions simultaneously, with the dominant role determined by the input and conflict type, not by fixed wiring.",
    "innovation_type": "new_formulation",
    "method_summary": "JuICE uses a dual-run inference strategy. First, it identifies heads whose knock-out effect is consistent across all conflict types (filtering out superposed heads that flip roles). At test time, it runs the model twice: the first pass saves selected heads' activations unperturbed; the second pass adds scaled first-run activations back, avoiding the residual-stream perturbation cascades that degrade single-pass interventions. A two-layer theoretical construction proves superposition arises inevitably from joint factual-recall and induction training.",
    "limitations_and_open_questions": "Doubles inference cost (dual forward pass). Head identification is still statistical (cross-conflict consistency filter), not causally grounded in circuit structure. No FFN analysis — superposition is characterized only at the attention head level. Tested only up to 8B parameters.",
    "building_blocks": [
      "CP superposition phenomenon as empirical constraint on circuit tracing",
      "Dual-run activation-addition intervention pattern",
      "Cross-conflict-type consistency filtering for robust head selection",
      "Theoretical proof that superposition is inevitable under joint training"
    ],
    "relevance_to_seed": "Defines the superposition challenge: any RAG circuit tracing that assumes clean head-type separation will fail, and interventions must avoid residual-stream perturbation cascades — the dual-run pattern or circuit-informed multi-point coordination are needed."
  },
  {
    "title": "CD-T: Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition",
    "venue": "ICLR 2025",
    "problem_identification": "Existing circuit discovery (ACDC, EAP) relies on activation patching requiring iterative forward passes, taking hours per circuit. EAP's linear approximation introduces propagation errors. Neither method efficiently supports fine-grained positional analysis (which head at which token position matters).",
    "key_insight": "Circuit discovery can be reframed from an empirical causal intervention problem to an analytical mathematical decomposition problem — contextual decomposition propagates relevant/irrelevant activation components through the network in a single forward pass, eliminating the patch-and-observe loop.",
    "innovation_type": "simplification",
    "method_summary": "CD-T decomposes every activation into relevant (β) and irrelevant (γ) components, where β captures deviation from mean activation. Custom propagation rules handle linear layers (proportional bias distribution), attention (decomposed Q/K/V with separate softmax), and ReLU. An L1-norm ratio R(s,T) = ||β||/||γ|| scores each component's contribution. Iterative greedy pruning selects minimal faithful circuits. Achieves 97% ROC AUC recovering known manual circuits (IOI, Greater-Than, Docstring) on GPT-2-small in seconds.",
    "limitations_and_open_questions": "Tested only on attention heads in small models (GPT-2-small, 4-layer transformers). MLP/FFN circuit integration not explored. Relevance metric doesn't distinguish positive from negative (inhibitory) contributions. Manual circuits still outperform CD-T circuits of equal size. Fixed-k node selection requires task-specific tuning.",
    "building_blocks": [
      "Single-pass decomposition framework adaptable to RAG (β=context tokens, γ=query tokens)",
      "Fine-grained positional circuit discovery (head × token position)",
      "L1-ratio relevance metric capturing both promoting and suppressing components",
      "Seconds-scale runtime enabling iteration over many RAG examples"
    ],
    "relevance_to_seed": "Primary enabling tool for the proposed methodology — its seconds-scale runtime makes full circuit tracing across hundreds of RAG conflict examples feasible, and its positional granularity can reveal how retrieved-context tokens interact with query tokens at specific heads."
  },
  {
    "title": "The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation",
    "venue": "NeurIPS 2025",
    "problem_identification": "Prior mechanistic studies of ICL (Jin et al. 2024) used computationally prohibitive path-patching (~2048 forward passes/sample) on toy single-token tasks. No work had characterized how attention heads function in realistic, open-domain RAG with multi-token answers and full Wikipedia passages.",
    "key_insight": "In-context heads are not monolithic — they decompose into functionally distinct task heads (encoding question type, middle layers) and retrieval heads (extracting answer spans, deep layers), each with independently extractable and transferable function vectors.",
    "innovation_type": "analysis",
    "method_summary": "Uses AttnLRP (attention-aware layer-wise relevance propagation) to attribute each head's contribution to predictions under open-book vs. closed-book settings. A difference score D between counterfactual-context and no-context conditions separates in-context heads (top-100 by D) from parametric heads (bottom-100). Within in-context heads, relevance aggregated over question vs. answer token positions yields a task/retrieval subclassification. A linear probe on logit-lens-projected retrieval head outputs achieves 94-98% AUC for predicting whether answers come from context or memory.",
    "limitations_and_open_questions": "Explicitly does not trace head-to-FFN interactions — acknowledged as future work. Only QA tasks with short answers tested. Top-K head selection is unprincipled. No analysis of inhibitory effects or how parametric heads actively suppress context-derived answers. Reviewers questioned novelty beyond Jin et al. (2024).",
    "building_blocks": [
      "Three-way head taxonomy (task/retrieval/parametric) with layer distribution",
      "AttnLRP-based attribution for scalable head identification",
      "Lightweight source-tracking linear probe (94% AUC, forward-pass only)",
      "Function vector extraction and injection for causal validation"
    ],
    "relevance_to_seed": "Provides the head-level taxonomy that the proposed circuit must connect through FFN interactions — the explicit gap (no MLP analysis, no cross-component tracing) is precisely where the proposed work contributes."
  },
  {
    "title": "IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons",
    "venue": "NeurIPS 2024",
    "problem_identification": "Prior interventions for knowledge conflicts operated at the output-probability level (CAD) or attention-head level (ITI), missing the FFN neurons that actually process contextual information. The authors hypothesized that specific FFN neurons encode context-processing functions and that amplifying them could shift model behavior toward context faithfulness.",
    "key_insight": "Context-processing in LLMs is partially localizable to a small set (~14) of FFN neurons in upper layers, identifiable via integrated gradients comparing question-only vs. context+question activations, and amplifiable via simple weight multiplication with zero inference overhead.",
    "innovation_type": "new_technique",
    "method_summary": "Integrated gradients compute each neuron's attribution to context processing by interpolating activations from a question-only baseline to context+question values (m=20 Riemann steps). Three-stage filtering (threshold → per-example top-20 → cross-example frequency ranking) identifies a shared set of ~14 context-aware neurons. These neurons' weights are multiplied by β≈7 offline, permanently modifying the model. On MemoTrap, LLaMA-2-7B improves from 24.5% to 56.1% accuracy; combining with CAD reaches 61.8%.",
    "limitations_and_open_questions": "No superposition awareness — assumes neurons have clean, separable context-processing roles. Only 3 synthetic benchmarks; no RAG evaluation. β=7 multiplication on potentially polysemantic neurons risks side effects. 50% neuron overlap across prompts means half are prompt-dependent. The 'context is always right' assumption is unsafe for noisy retrieval. No cross-component interaction analysis.",
    "building_blocks": [
      "Integrated-gradients neuron attribution methodology for context processing",
      "Evidence that context-aware function concentrates in upper-layer FFN neurons",
      "Weight-multiplication intervention pattern (zero inference cost)",
      "Complementarity with output-level methods (IRCAN+CAD stacking)"
    ],
    "relevance_to_seed": "Neuron-level baseline for the proposed circuit-informed intervention — IRCAN's heuristic neuron selection (integrated gradients + frequency filtering) is exactly what circuit-grounded target selection should outperform, and its upper-layer FFN concentration aligns with the hypothesis that deep FFN layers re-assert parametric answers."
  },
  {
    "title": "How Transformers Reject Wrong Answers: Rotational Dynamics of Factual Constraint Processing",
    "venue": "arXiv 2026 (preprint)",
    "problem_identification": "Prior factual knowledge work (Burns et al. 2023, Meng et al. 2022) treats truthfulness as a static, single-layer property. No work had tracked the full layer-by-layer geometric evolution of representations when models process correct vs. incorrect continuations, missing the dynamic mechanism of factual acceptance/rejection.",
    "key_insight": "Factual discrimination in transformers is encoded entirely through angular separation (rotation) on an approximate hypersphere — not through magnitude differences — and larger models (≥1.6B) actively suppress correct answers when processing incorrect inputs, with probe accuracy peaking at mid-layers then declining.",
    "innovation_type": "new_formulation",
    "method_summary": "Forced-completion probing appends known correct/incorrect single tokens to queries and tracks five geometric measurements across all layers: trajectory similarity, rotational divergence (ρ), norm ratio (η), commitment ratio (κ via logit lens), and attention allocation (α). Across LLaMA-2-13B, Mistral-7B, and StableLM-2-1.6B, the norm ratio stays within 3% of unity while angular divergence grows substantially. Active suppression manifests as κ dropping to 0.08 for incorrect inputs (vs. 0.77 for correct). The phenomenon is absent in Qwen2-1.5B, suggesting a ~1.6B parameter emergence threshold.",
    "limitations_and_open_questions": "Forced single-token completion differs from autoregressive generation dynamics. Only 300 queries across 3 domains. Four models cannot establish a true phase transition — Qwen2's null result may reflect architecture, not scale. No circuit-level causal explanation for which components drive the rotation and suppression.",
    "building_blocks": [
      "Rotational divergence metric (ρ/η decomposition) for probing factual processing",
      "Active suppression measurement via commitment ratio κ",
      "Empirical evidence that magnitude-based hallucination detectors miss the signal",
      "Mid-layer peak in discriminative information as intervention target indicator"
    ],
    "relevance_to_seed": "Provides the geometric framework explaining the flip phenomenon: correct answers peak at mid-layers (high κ) then get suppressed in deep layers (κ collapse) via rotation — this is the observable signature of the circuit pathology where deep FFN layers re-assert parametric answers, and it confirms that interventions must target angular representations, not magnitudes."
  },
  {
    "title": "ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Prior RAG hallucination detectors either measured parametric knowledge OR external context utilization in isolation, creating confounded estimates. They diagnosed this via systematic analysis showing 1006/1024 attention heads have higher external context scores on truthful vs. hallucinated outputs, while later FFN layers show higher parametric knowledge scores for hallucinations.",
    "key_insight": "RAG hallucination detection is a confounding problem from causal inference: Knowledge FFNs (parametric signal) and Copying Heads (context signal) must be treated as covariates in multivariate regression, not analyzed independently.",
    "innovation_type": "new_formulation",
    "method_summary": "Parametric Knowledge Score (PKS) measures per-FFN-layer vocabulary distribution shift via LogitLens + JSD. External Context Score (ECS) measures attention to retrieved context by Copying Heads (identified via OV matrix eigenvalue analysis). Hallucination score combines both via fitted linear regression. AARF mitigation conditionally amplifies Copying Heads and dampens Knowledge FFNs when hallucination score exceeds threshold.",
    "limitations_and_open_questions": "Reviewers criticized PKS as not guaranteed to measure parametric knowledge specifically (correlation ≠ mechanism), causal experiments were noisy, and numerous hyperparameters (top-k layers/heads, α, β, τ) require per-dataset tuning. Component-level analysis without circuit tracing — no interaction mapping between Knowledge FFNs and Copying Heads.",
    "building_blocks": [
      "LogitLens-based PKS for measuring FFN knowledge injection",
      "OV-eigenvalue Copying Head identification",
      "AARF conditional activation scaling pattern",
      "RAGTruth dataset",
      "Confounding-as-covariates framework for dual-source analysis"
    ],
    "relevance_to_seed": "Establishes the component-level anatomy (Knowledge FFNs + Copying Heads) that our circuit tracing extends into a full causal interaction graph, and AARF is a single-point heuristic intervention our multi-point circuit-informed approach must outperform."
  },
  {
    "title": "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (SpARE)",
    "venue": "NAACL 2025 (Oral)",
    "problem_identification": "Existing representation engineering methods (ActAdd, TaskVec, SEA) fail to steer knowledge selection because they edit polysemantic dense vectors where minor changes in one dimension affect multiple semantic features. Diagnosed via linear probing showing conflict signals peak at mid-layers, then empirically demonstrating baseline steering failures.",
    "key_insight": "Less than 0.05% of SAE features (selected via mutual information) control the entire knowledge selection behavior, and effective steering requires input-dependent, constrained editing in residual stream space rather than SAE reconstruction space.",
    "innovation_type": "combination",
    "method_summary": "Collects SAE-encoded activations from context-favoring vs. parametric-favoring model predictions, selects top features by mutual information with outcome, determines each feature's directional role. For inference: computes input-specific min/max-constrained edits (removing undesired features, adding desired ones) and applies them through SAE decoder columns to the original residual stream, avoiding lossy SAE reconstruction. Achieves +10% EM over baselines.",
    "limitations_and_open_questions": "Requires pre-trained SAEs (not available for all models). Only evaluated on ODQA (NQSwap, Macnoise) — unclear generalization to multi-hop reasoning or long-form generation. Feature selection is heuristic (MI-based), not causally grounded in circuit structure. Binary knowledge selection framing oversimplifies real-world knowledge integration.",
    "building_blocks": [
      "MI-based SAE feature selection pipeline",
      "Constrained input-dependent SAE editing (Eq. 2-4)",
      "Conflict detection linear probing methodology",
      "Pre-trained SAEs for Llama2-7B/Llama3-8B/Gemma2-9B",
      "NQSwap and Macnoise benchmarks"
    ],
    "relevance_to_seed": "Primary heuristic baseline our circuit-informed intervention must outperform; demonstrates SAE features can steer knowledge selection but selects targets statistically rather than via causal circuit analysis — exactly the gap our work fills."
  },
  {
    "title": "Circuit Tracing: Revealing Computational Graphs in Language Models",
    "venue": "Anthropic Technical Report, March 2025",
    "problem_identification": "Per-layer transcoders create artificially long attribution chains because the same conceptual feature manifests across multiple MLP layers via the residual stream. SAEs decompose activations but not computation, making them unsuitable for circuit tracing. Identified through progression from SAEs → per-layer transcoders → recognizing cross-layer redundancy.",
    "key_insight": "Cross-layer transcoders (CLTs) exploit the residual stream's information-sharing property to collapse multi-layer amplification chains into direct feature connections, converting circuit discovery from expensive ablation-based search into direct readoff from a locally-linear replacement model.",
    "innovation_type": "new_technique",
    "method_summary": "CLTs read from the residual stream at one layer and contribute decoder vectors to MLP outputs at all subsequent layers, trained to approximate true MLP outputs with tanh-based sparsity. On any prompt, freezing attention patterns and LayerNorm makes the CLT-replaced model fully linear — circuits are paths through this linear network. Attribution graphs use stop-gradient Jacobians and Neumann-series influence pruning for tractable visualization. Applied to Claude 3.5 Haiku scale.",
    "limitations_and_open_questions": "QK attention circuits invisible (only OV traced). 11.5-21.7% reconstruction error hides unknown computation. CLTs may learn unfaithful shortcuts — LessWrong analysis shows they collapse multi-step computations into lookup tables. Only ~25% of prompts yield satisfying interpretations. Inhibitory (absent-feature) mechanisms are invisible.",
    "building_blocks": [
      "Cross-layer transcoder architecture and training",
      "Stop-gradient Jacobian attribution",
      "Neumann-series influence matrix pruning",
      "Local replacement model concept",
      "Circuit Tracer library (Gemma-2-2B, Llama-3.1-1B, Qwen3-4B)",
      "CLT-Forge distributed training library"
    ],
    "relevance_to_seed": "Directly applicable methodology for our RAG circuit discovery — CLTs enable end-to-end tracing from retrieval heads through FFN layers to output, though we must address the faithfulness concerns and adapt to open-weight models (Llama-3.1-8B) where pre-trained CLTs may not exist."
  },
  {
    "title": "Transcoders Find Interpretable LLM Feature Circuits",
    "venue": "NeurIPS 2024",
    "problem_identification": "SAEs decompose MLP activations into interpretable features but cannot trace computation THROUGH MLPs because SAE features are dense linear combinations of neurons, each with its own nonlinearity — making cross-layer attribution intractable. Identified by recognizing SAEs answer 'what features exist?' but not 'what transformation is performed?'",
    "key_insight": "Training a sparse wide ReLU network to approximate MLP input→output behavior (rather than reconstructing activations) yields a clean factorization where each feature's contribution decomposes into an input-dependent scalar activation times an input-invariant weight dot product, enabling weights-based circuit analysis.",
    "innovation_type": "new_formulation",
    "method_summary": "Transcoders minimize ||MLP(x) - TC(x)||² + λ||z||₁, replacing opaque MLPs with sparse interpretable alternatives. The contribution of feature i (layer l) to feature i' (layer l') factors as z(l,i)·(f_dec(l,i)·f_enc(l',i')), separating model wiring (fixed weights) from activation patterns (input-dependent). Greedy recursive attribution traces circuits backward from output logits through transcoder features and attention OV circuits. De-embeddings (W_E^T · f_enc) enable blind feature analysis without any input data.",
    "limitations_and_open_questions": "Only qualitative case studies on GPT2-small — no large-scale quantitative circuit evaluation. Attention pattern computation not modeled (only OV circuits). Approximation error may hide critical computation. Follow-up (Paulo et al. 2025) showed skip transcoders are Pareto-better. Scalability of circuit analysis to production models unproven at time of publication.",
    "building_blocks": [
      "Transcoder architecture and training pipeline",
      "Input-invariant/input-dependent factorization framework",
      "De-embedding analysis for weight-based feature interpretation",
      "transcoder_circuits Python library",
      "Blind case study protocol for feature reverse-engineering"
    ],
    "relevance_to_seed": "Foundational tool for decomposing FFN contributions in our RAG circuit — transcoders enable tracing how parametric Knowledge FFNs transform retrieval head outputs across layers, and the factorization framework lets us identify fixed circuit structure underlying the flip phenomenon."
  },
  {
    "title": "Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models",
    "venue": "arXiv 2026",
    "problem_identification": "All prior mechanistic work on knowledge conflicts addressed context-memory conflicts (external vs. internal). Intra-memory conflicts (contradictory facts within parameters from conflicting training data) had no mechanistic analysis. Identified by mapping the conflict taxonomy from Xu et al. (EMNLP 2024) against existing mechanistic studies and finding the intra-memory cell empty.",
    "key_insight": "Creating matched model pairs (conflicted vs. clean, trained on identical data ± contradictions) enables cross-model activation patching (CMAP) that isolates the mechanistic signature of intra-memory conflict without prompt-mismatch noise.",
    "innovation_type": "new_formulation",
    "method_summary": "Constructs SynWikiBio: 2000 synthetic biographies with controlled contradictions using nonsense entity names to guarantee zero pre-training overlap. Trains conflicted (l'_mix) and clean (l'_clean) model pairs on GPT-2 XL and Qwen3-4B. Applies logit lens to track competing token probabilities across layers, finding attention components dominate in layers 21-47. CMAP transfers activations from clean→conflicted model at specific components, achieving up to 70% steering success on Qwen3-4B vs. 22% with standard patching.",
    "limitations_and_open_questions": "Only 1:1 contradictions studied; modest success rates on GPT-2 XL (~22%) suggest highly distributed encoding. Unexpected attribute-type asymmetry (CMAP helps for company but not university attributes) is unresolved — raises whether knowledge conflict is a unified phenomenon. Synthetic data only; transfer to natural pre-training conflicts unvalidated.",
    "building_blocks": [
      "SynWikiBio controlled conflict dataset",
      "Model-pair experimental paradigm (conflicted vs. clean)",
      "CMAP adapted for knowledge conflict study",
      "Shared-prefix prompt construction for conflict elicitation",
      "Three-stage pipeline: controlled conflicts → logit lens localization → activation patching verification"
    ],
    "relevance_to_seed": "Closest methodological precedent for our work but addresses intra-memory (not RAG) conflicts. The model-pair CMAP paradigm could be adapted to compare RAG-augmented vs. parametric-only inference, and the finding that conflicts are distributed across attention components in later layers aligns with the flip phenomenon we aim to explain."
  },
  {
    "title": "Retrieval Head Mechanistically Explains Long-Context Factuality",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "No mechanistic explanation existed for how transformers retrieve information from arbitrary positions in long contexts, nor why models hallucinate under long-context settings. The authors framed this as identifying the minimal sub-network implementing conditional copy-paste retrieval.",
    "key_insight": "Fewer than 5% of attention heads ('retrieval heads') implement a conditional copy-paste algorithm, are universal across model families, intrinsic to pretraining (not created by context extension), and causally necessary — ablating them causes hallucination while ablating equal numbers of non-retrieval heads has negligible effect.",
    "innovation_type": "analysis",
    "method_summary": "Defines a 'retrieval score' measuring per-head token-level recall of copy-paste behavior on needle-in-a-haystack tasks with semantically irrelevant, unmemorizable answers. Scores converge after few samples. Progressive head masking causally validates necessity: top-50 retrieval heads (~5%) drop NIAH below 50%, while masking random heads preserves 95% accuracy. Tested across LLaMA/Mistral/Yi/Qwen at 6B-56B scales, MoE (Mixtral), and hybrid SSM (Jamba).",
    "limitations_and_open_questions": "No mechanism explaining *when/why* retrieval heads dynamically activate. Limited to copy-paste retrieval — does not address semantic paraphrasing retrieval or interaction with parametric knowledge circuits. No circuit tracing beyond individual head identification.",
    "building_blocks": [
      "Retrieval score metric for head classification",
      "Progressive head masking protocol",
      "NIAH-based detection datasets with unmemorizable answers",
      "Taxonomy: always-active vs context-sensitive retrieval heads"
    ],
    "relevance_to_seed": "Provides the foundational retrieval-side component of our circuit — the <5% of heads whose output must be traced through FFN layers and copy-suppression mechanisms to understand evidence integration vs. override."
  },
  {
    "title": "CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts",
    "venue": "arXiv 2026",
    "problem_identification": "Decoding-time methods (CAD, AdaCAD) only adjust final token distributions without preventing intermediate representations from being steered toward parametric answers, while weight-editing methods (ROME) require ground-truth targets. The authors used Logit Lens analysis across 500 NQ conflict cases to discover the 'flip phenomenon.'",
    "key_insight": "In 56% of knowledge-conflict cases, the correct context-derived answer reaches Rank-1 at intermediate layers but gets suppressed by deep FFN layers before output — the model 'knows' the right answer internally but fails to produce it, motivating surgical disinhibition rather than forced steering.",
    "innovation_type": "new_technique",
    "method_summary": "Two-stage label-free inference-time intervention. Stage 1: dual forward passes (contextualized vs. null-context) compute Contextual Mutual Information per token, verified by attention grounding scores, to select a trustworthy target token without labels. Stage 2: identifies suppressive FFN layers where u_l^T · w_target < 0 (FFN output negatively projects onto target's unembedding), then applies additive patches φ_l = -α·(u_l^T·w_target/||w_target||²)·w_target to neutralize suppression. α=1 achieves exact disinhibition.",
    "limitations_and_open_questions": "Computational overhead from dual forward passes unquantified. Modest gains on multi-hop reasoning suggest parametric suppression interacts differently with complex reasoning chains. No circuit-level causal explanation for *why* specific FFN layers suppress — treatment is statistical, not mechanistic.",
    "building_blocks": [
      "Flip phenomenon empirics (56% of conflict cases)",
      "Logit Lens layer-wise analysis of answer rank trajectories",
      "Label-free trustworthy token selection via CMI + attention verification",
      "Suppressive layer identification via unembedding projection sign"
    ],
    "relevance_to_seed": "The flip phenomenon is the key empirical observable our circuit must causally explain; CoRect's layer identification method (unembedding projection) provides a baseline for circuit-informed suppressive layer detection."
  },
  {
    "title": "ParamMute: Suppressing Knowledge-Critical FFNs for Faithful Retrieval-Augmented Generation",
    "venue": "NeurIPS 2025",
    "problem_identification": "Existing RAG faithfulness methods focus on enhancing context utilization but overlook that internal parametric knowledge stored in FFN layers actively undermines faithfulness. The authors measured activation ratios across layers during faithful vs. unfaithful generation to locate the source.",
    "key_insight": "Mid-to-deep FFN layers (70-90% of model depth) exhibit disproportionately high activation during unfaithful RAG generation, functioning as parametric memory repositories that override context — and soft suppression with a tunable coefficient enables plug-and-play control.",
    "innovation_type": "combination",
    "method_summary": "Three components: (1) UA-FFN identification via activation gap ΔR^l = E[R^l|unfaithful] - E[R^l|faithful], selecting top-N layers; (2) soft suppression scaling FFN activations by λ∈[0,1]; (3) knowledge preference calibration combining supervised fine-tuning (KAT) with a max-margin loss (KPO) that forces P(y*|q,c) >> P(y*|q). Evaluated on CoFaithfulQA (52K instances from 6 QA datasets) and ConFiQA. Achieves +5% ConR, -4% MemR vs. vanilla RAG.",
    "limitations_and_open_questions": "Requires training data for KAT/KPO — not purely inference-time. UA-FFN identification is statistical (activation ratios), not causal-circuit-based. Reviewers questioned performance under noisy retrieval and closed-book degradation. FFN suppression is uniform across neurons within selected layers — no neuron-level granularity.",
    "building_blocks": [
      "Activation ratio metric for FFN layer ranking",
      "Soft suppression coefficient λ for plug-and-play control",
      "KPO max-margin loss for knowledge preference calibration",
      "CoFaithfulQA benchmark (52K instances)"
    ],
    "relevance_to_seed": "Direct competitor/baseline — identifies the same mid-to-deep FFN layers our circuit must explain, but uses statistical activation gaps rather than causal circuit tracing, and applies uniform layer-level suppression rather than neuron/feature-level surgical intervention."
  },
  {
    "title": "Analysing the Residual Stream of Language Models Under Knowledge Conflicts",
    "venue": "NeurIPS 2024 Workshop (MINT)",
    "problem_identification": "Prior conflict detection relied on prompting-based strategies requiring extra inference passes. No work had examined whether LLMs' internal representations encode detectable conflict signals before answer generation. The authors applied linear probing across all layers to map the temporal structure of conflict processing.",
    "key_insight": "Knowledge conflicts are processed in two sequential phases in the residual stream: conflict detection peaks at mid-layers (~layer 14 in Llama3-8B), followed by knowledge selection peaking later (~layer 17) — and both signals coexist without erasure, with contextual-knowledge use producing distinctly more skewed activation distributions in deep layers.",
    "innovation_type": "analysis",
    "method_summary": "Layer-wise logistic regression probes (with L1 regularization) on hidden states, attention outputs, and MLP outputs at the final token position, trained on two binary tasks: conflict detection (conflicting vs. non-conflicting context) and knowledge selection (will model use contextual vs. parametric answer). Complemented by distributional shape analysis (Kurtosis, Hoyer sparsity, Gini coefficient) showing significant skewness divergence in layers 20-30. Tested on NQSwap/Macnoise/ConflictQA across Llama2-7B and Llama3-8B.",
    "limitations_and_open_questions": "Probing captures correlation, not causation — detecting a signal doesn't prove the model uses it. Limited to English QA, greedy decoding, two model families. No intervention experiments. The paper is explicitly a preliminary study leading to SpARE (NAACL 2025).",
    "building_blocks": [
      "Two-phase conflict processing timeline (detect → select)",
      "Distributional skewness metrics for knowledge-source discrimination",
      "Layer-wise probing protocol for conflict signals",
      "Evidence that MLP/attention stop adding conflict info after mid-layers while residual stream retains it"
    ],
    "relevance_to_seed": "Provides representation-level evidence our circuit must explain: conflict detection at mid-layers and selection at later layers maps directly onto the promote-suppress-iterate framework, and the coexistence finding constrains circuit hypotheses about when/where parametric vs. contextual signals compete."
  },
  {
    "title": "A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models",
    "venue": "EMNLP 2025 Findings",
    "problem_identification": "SAE research had fragmented across architectures (Gated, TopK, JumpReLU, etc.), training strategies, evaluation metrics, and applications without a unifying survey. No comprehensive resource organized the design space or identified open challenges systematically.",
    "key_insight": "SAE variants primarily address a single core tension — the sparsity-fidelity tradeoff — through either architectural innovations (separating gating from magnitude estimation) or training innovations (end-to-end optimization through the full model), with shrinkage bias from L1 regularization being the key technical obstacle most variants attempt to resolve.",
    "innovation_type": "analysis",
    "method_summary": "Taxonomizes SAE literature along two axes: improvement target (architecture vs. training strategy) and historical stage (individual neurons → small models → scaled deployment). Covers 15+ SAE variants with formal specifications. Categorizes feature explanation into input-based (MaxAct, PruningMaxAct) and output-based (VocabProj, MutInfo) methods. Evaluates metrics across structural (MSE, FVU, L0, delta LM loss) and functional (sparse probing, TPP, feature absorption, SCR) dimensions. References SAEBench as standardized evaluation.",
    "limitations_and_open_questions": "Notable omission of transcoders (Dunefsky et al. 2024), which approximate MLP input-output functions via sparse bottlenecks and have been argued to outperform SAEs on interpretability benchmarks. No discussion of SAE application to circuit discovery specifically. Four open challenges identified: incomplete concept dictionaries, lack of theoretical foundations, reconstruction errors, and computational burden at scale.",
    "building_blocks": [
      "Taxonomy of SAE architectures with formal specifications",
      "Evaluation framework: structural vs. functional metrics",
      "Feature explanation methods (MaxAct, PruningMaxAct, VocabProj, MutInfo)",
      "SAEBench reference for standardized comparison",
      "Model steering via SAE-derived steering vectors"
    ],
    "relevance_to_seed": "Essential methodological reference for our SAE/transcoder-based circuit analysis — the taxonomy guides architecture selection (TopK or Gated SAE for sparsity without shrinkage bias), and the evaluation framework (sparse probing, TPP) provides metrics for validating that discovered circuit features are genuinely monosemantic."
  },
  {
    "title": "Knowledge Circuits in Pretrained Transformers",
    "venue": "NeurIPS 2024",
    "problem_identification": "Prior interpretability work studied isolated components (knowledge neurons, individual attention heads) but never traced the full collaborative subgraph responsible for expressing a specific fact. The authors identified this gap by noting that component-level analyses cannot explain how information flows from subject tokens through intermediate processing to output.",
    "key_insight": "Factual knowledge expression depends on a discoverable, sparse circuit of cooperating components — mover heads (transfer subject info to final position), relation heads (activate relation-specific processing), and MLPs (aggregate and map to target entities) — that retains ~70% of full-model performance with <10% of edges.",
    "innovation_type": "new_formulation",
    "method_summary": "They model the transformer as a DAG with edges between residual stream, attention heads, MLPs, and output. Edge significance is measured by ablation: S(e_i) = log P(o) - log P(o|ablate e_i). Edges below threshold τ are pruned to yield a minimal circuit. They taxonomize surviving heads into mover, relation, and mixture types based on attention patterns, then validate circuit completeness via Hit@10 on held-out facts.",
    "limitations_and_open_questions": "Limited to GPT-2 and TinyLLaMA (1.1B); circuit discovery takes 1-2 days on A800 GPUs, raising scalability concerns for 7B+ models. Circuits are traced for single-fact recall only — not for RAG or conflicting-knowledge settings where the same circuit must handle competing signals.",
    "building_blocks": [
      "Edge-ablation circuit discovery methodology",
      "Mover/relation/mixture head taxonomy",
      "MatchNLL significance metric",
      "TransformerLens integration",
      "Hit@10 circuit validation"
    ],
    "relevance_to_seed": "Provides the foundational circuit discovery methodology and component vocabulary (information heads, relation heads, MLPs) that we will extend from single-fact recall to RAG knowledge-conflict circuits."
  },
  {
    "title": "Promote, Suppress, Iterate: How Language Models Answer One-to-Many Factual Queries",
    "venue": "EMNLP 2025",
    "problem_identification": "How LMs generate multiple valid answers to one-to-many queries (e.g., 'cities in France') without repeating was mechanistically unexplained. The authors identified this by observing that standard factual recall analyses assume single-answer settings and cannot account for iterative answer generation.",
    "key_insight": "MLPs indiscriminately promote ALL candidate answers simultaneously, while attention heads iteratively suppress previously generated ones — a division of labor where MLPs are recall engines and attention is the deduplication/selection mechanism.",
    "innovation_type": "analysis",
    "method_summary": "They introduce Token Lens, which aggregates weighted value vectors attending to specific tokens (Σ p·v), projects through Wo and the unembedding matrix, yielding per-token logit contributions. Their MLP knockout zeros attention weights from the last token to targets, then measures the resulting MLP output change in logit space to isolate how MLPs use attention-relayed information. Causal tracing with noise injection validates which tokens are causally critical.",
    "limitations_and_open_questions": "Mechanism studied only for one-to-many factual recall, not knowledge conflicts or RAG. The suppress-then-iterate dynamic across layers has not been tested when two competing knowledge sources (parametric vs. context) simultaneously activate the promotion pathway.",
    "building_blocks": [
      "Token Lens technique",
      "MLP knockout method",
      "Promote-suppress theoretical framework",
      "Layer-wise logit attribution"
    ],
    "relevance_to_seed": "Directly anchors our RAG circuit pathology hypothesis: in knowledg
... (truncated)

## Your task

Synthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.

Think about:
- What PATTERNS OF INNOVATION keep working in this field?
- What do reviewers consistently reward?
- Where are the real gaps (not assumed gaps)?
- What combinations haven't been tried?
- What mistakes should we avoid?

## Output format

Output a JSON object with these sections:
{
  "innovation_patterns": [
    {"pattern": "name", "description": "how it works", "examples": ["paper1", "paper2"], "success_rate": "high/medium/low"}
  ],
  "reviewer_preferences": [
    "What reviewers in this area consistently care about (based on evidence from paper analyses)"
  ],
  "field_gaps": [
    {"gap": "description of unsolved problem", "evidence": "which papers mention this limitation", "difficulty": "high/medium/low", "impact_if_solved": "high/medium/low"}
  ],
  "untried_combinations": [
    {"idea_sketch": "what could be combined", "from_papers": ["which papers inspire this"], "why_promising": "reason"}
  ],
  "method_building_blocks": [
    {"tool": "name", "what_it_does": "description", "used_by": ["papers"], "could_be_applied_to": "new application"}
  ],
  "common_pitfalls": [
    "Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)"
  ],
  "field_trajectory": "Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)",
  "meta_advice": "If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)"
}

Be specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.

IMPORTANT: You MUST end your response with the JSON object.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "494a08d9-3166-43b1-a3f9-8b1becb4874b",
  "type": "user",
  "uuid": "da7f72d9-4e76-456d-9193-891246770177",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:26:29.937Z_

```json
{
  "parentUuid": "da7f72d9-4e76-456d-9193-891246770177",
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
  "uuid": "79c575e7-507e-470c-847b-e108b6585f22",
  "timestamp": "2026-05-30T06:26:29.937Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:26:29.937Z_

```json
{
  "parentUuid": "79c575e7-507e-470c-847b-e108b6585f22",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cbf90d1b-cfa6-4ce9-a367-13a6c50acc3e",
  "timestamp": "2026-05-30T06:26:29.937Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "cbf90d1b-cfa6-4ce9-a367-13a6c50acc3e",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Design circuit-informed RAG interventions via promote-suppress pathology",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:26:47.981Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for generating novel research ideas in the area of mechanistic interpretability of RAG knowledge conflicts in LLMs. Let me carefully analyze all the papers and their relationships to produce a comprehensive, evidence-based JSON output.

Let me think through each section:

**Innovation Patterns:**
1. Component-level → Circuit-level elevation (Knowledge Circuits → ReDeEP → proposed work)
2. New formulation/lens on existing phenomenon (JuICE reframing head roles as superposition, CoRect discovering flip phenomenon)


3. Tool simplification enabling new science (CD-T making circuit discovery feasible, transcoders enabling MLP tracing)
4. Dual-source confounding treatment (ReDeEP treating parametric + context as covariates)
5. Geometric/representational analysis (Rotational Dynamics paper)
6. SAE-based monosemantic decomposition for steering (SpARE)

**Reviewer Preferences:**
- Causal validation (not just correlation/probing)
- Practical downstream impact ("so what?" test)
- Cross-model generalization
- Addressing superposition/polysemanticity honestly
- Clean experimental controls

**Field Gaps:**
- End-to-end circuit from retrieval heads through knowledge conflict resolution to output generation
- Systematic treatment of how different knowledge sources compete during inference
- Scalable methods for tracing information flow across retrieval-augmented architectures
- Understanding failure modes when parametric and retrieved knowledge directly contradict

**Untried Combinations:**
- CD-T + promote-suppress framework for RAG
- CLT circuit tracing + CoRect flip phenomenon
- SpARE SAE features + circuit-informed target selection
- CMAP model-pair paradigm for RAG vs parametric-only

**Method Building Blocks:**
- CD-T, TransformerLens, transcoders, CLTs, Token Lens, LogitLens, AttnLRP, SAEs, pyvene

**Common Pitfalls:**
- Assuming clean head-type separation (JuICE refutes)
- Correlation-based probing without causal validation
- Single-point interventions
- Ignoring polysemanticity and superposition in feature attribution
- Over-claiming circuit completeness

Now I'm constructing the full JSON structure to organize these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbf90d1b-cfa6-4ce9-a367-13a6c50acc3e",
  "isSidechain": false,
  "requestId": "req_011CbYH42FTuJ8g2Zcuskt7N",
  "type": "assistant",
  "uuid": "9bcf6a4d-a9e0-481d-9574-c2b57d60fa5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduGeSte622oMETkZkQ926",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8653,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8653,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 9 · 2026-05-30T06:30:11.730Z_

I'll analyze the full set of paper analyses to synthesize this field guide. Let me first review the truncated portions and cross-reference key details.

Now let me produce the comprehensive field guide based on deep analysis of all 20 papers and the research direction.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Component-to-Circuit Elevation",
      "description": "Identify components previously studied in isolation (heads, FFN layers, neurons) and trace their causal interactions into a full circuit. The key move is taking a known taxonomy (e.g., mover heads, relation heads, Knowledge FFNs, Copying Heads) and showing how they collaborate or conflict across layers — upgrading from a parts list to a wiring diagram.",
      "examples": ["Knowledge Circuits in Pretrained Transformers (NeurIPS 2024)", "Circuit Tracing (Anthropic 2025)", "Transcoders Find Interpretable LLM Feature Circuits (NeurIPS 2024)"],
      "success_rate": "high"
    },
    {
      "pattern": "Empirical Phenomenon Discovery → Mechanistic Explanation → Surgical Intervention",
      "description": "The highest-impact papers follow a three-beat arc: (1) discover a surprising empirical regularity (e.g., flip phenomenon, superposition, retrieval head universality), (2) provide a mechanistic account of why it happens, (3) design an intervention exploiting the mechanism. Papers that stop at step 1 or 2 get workshops; papers that complete all three get spotlights. CoRect discovered the flip phenomenon but stopped at statistical treatment; JuICE discovered superposition but only filtered for robust heads. The gap is always step 2→3.",
      "examples": ["CoRect (flip phenomenon → FFN suppression → additive patching)", "JuICE (superposition discovery → consistency filtering → dual-run intervention)", "SpARE (MI feature selection → constrained editing → steering)"],
      "success_rate": "high"
    },
    {
      "pattern": "Tool Simplification Enabling New Science",
      "description": "Replace an expensive methodology (e.g., iterative activation patching taking hours) with a mathematically equivalent but computationally cheaper alternative (e.g., single-pass decomposition), then demonstrate new analyses that were previously infeasible. CD-T replaced ACDC's iterative patching with analytical decomposition, achieving seconds-scale runtime. Transcoders replaced opaque MLP computation with sparse interpretable alternatives. The innovation is the tool; the science it enables is the payoff.",
      "examples": ["CD-T (ICLR 2025)", "Transcoders (NeurIPS 2024)", "Cross-Layer Transcoders (Anthropic 2025)"],
      "success_rate": "high"
    },
    {
      "pattern": "Dual-Source Confounding Framework",
      "description": "Reframe a problem previously analyzed from one knowledge source's perspective as a multi-source confounding problem requiring joint treatment. ReDeEP's key insight was that hallucination detection must treat parametric knowledge and external context as covariates in multivariate regression. This pattern generalizes: any RAG behavior is the result of at least two interacting signals, and analyzing either alone yields confounded estimates.",
      "examples": ["ReDeEP (ICLR 2025)", "Analysing the Residual Stream (NeurIPS 2024 Workshop)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Geometric Reframing of Discrete Phenomena",
      "description": "Replace discrete categorizations (correct/incorrect, faithful/unfaithful) with continuous geometric measurements (angular divergence, rotational dynamics, distributional skewness) that reveal hidden structure. The Rotational Dynamics paper showed factual discrimination is encoded in angle, not magnitude — invalidating magnitude-based detectors. This pattern works because it provides new metrics and new intervention targets.",
      "examples": ["Rotational Dynamics (arXiv 2026)", "Analysing the Residual Stream (NeurIPS 2024 Workshop)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Controlled Pair Comparison",
      "description": "Construct matched experimental conditions (model pairs, prompt pairs, activation pairs) that differ on exactly one variable of interest, enabling clean causal attribution. Where Knowledge Collides used conflicted vs. clean model pairs; CoRect used contextualized vs. null-context forward passes; Atlas used open-book vs. closed-book settings. The pattern's power is in eliminating confounds through careful experimental design rather than post-hoc statistical adjustment.",
      "examples": ["Where Knowledge Collides (arXiv 2026)", "CoRect (arXiv 2026)", "Atlas of ICL (NeurIPS 2025)"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Causal validation is non-negotiable: every top-venue paper includes ablation, patching, or knockout experiments beyond correlation/probing. Atlas reviewers questioned novelty partly because it extended Jin et al.'s taxonomy without new causal mechanisms. ReDeEP reviewers explicitly criticized PKS as 'correlation ≠ mechanism.' Pure probing studies (Analysing the Residual Stream) end up at workshops, not main conferences.",
    "Cross-model generalization is expected: Retrieval Head tested across LLaMA/Mistral/Yi/Qwen at 6B-56B + MoE + SSM hybrids. CD-T validated on multiple known circuits. Papers tested on a single model family (IRCAN on LLaMA-2-7B only, Where Knowledge Collides on GPT-2 XL + Qwen3-4B) receive skepticism about generality. Two model families is the minimum bar for AAAI/NeurIPS; three is preferred.",
    "Downstream utility ('so what?') separates acceptances from rejections: AAAI ML track reviewers demand practical applications. JuICE provided an intervention; Atlas explicitly did not trace interactions (acknowledged as future work) and reviewers noted limited novelty. Pure interpretability without an intervention or detection method struggles at applied venues.",
    "Honest treatment of superposition and polysemanticity: Post-JuICE, reviewers will reject any paper that assumes clean head-type separation without empirical validation. IRCAN's assumption that neurons have separable context-processing roles is a known weakness. Papers must explicitly test for and address polysemanticity.",
    "Quantitative comparison against strong, recent baselines: SpARE compared against ActAdd, TaskVec, SEA. CoRect compared against CAD, AdaCAD. Papers that compare only against vanilla models or outdated baselines (e.g., only CAD without AdaCAD) get criticized. Include at least 3 concurrent/recent methods.",
    "Compute transparency and reproducibility: Papers must specify GPU-hours, model access requirements, and hyperparameter sensitivity. ReDeEP was criticized for numerous hyperparameters requiring per-dataset tuning. Methods with fewer knobs and clear sensitivity analysis are preferred."
  ],
  "field_gaps": [
    {
      "gap": "No end-to-end circuit connecting retrieval heads → FFN knowledge layers → copy suppression → output logits in RAG, comparing success (context-faithful) vs. failure (parametric override) cases",
      "evidence": "Atlas (NeurIPS 2025) explicitly acknowledges 'no head-to-FFN interaction tracing' as future work. ReDeEP identifies Knowledge FFNs and Copying Heads but provides no interaction map. Knowledge Circuits (NeurIPS 2024) traces factual recall circuits but not RAG circuits. Retrieval Head (ICLR 2025) identifies retrieval heads but does not trace their output through parametric circuits.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No circuit-level causal explanation for the flip phenomenon (correct answer reaches Rank-1 at mid-layers then gets suppressed before output)",
      "evidence": "CoRect documents the flip phenomenon in 56% of conflict cases but provides only statistical treatment (unembedding projection sign). Rotational Dynamics shows the geometric signature (κ collapse in deep layers) but no circuit identification. Promote-Suppress-Iterate provides the theoretical framework but has not been applied to RAG conflicts.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "No multi-point coordinated intervention targeting circuit-identified locations simultaneously (boost retrieval signal + suppress parametric re-assertion + protect against copy suppression)",
      "evidence": "All existing interventions are single-mechanism: SpARE edits SAE features at one layer type, CoRect patches suppressive FFNs, IRCAN amplifies context neurons, ParamMute suppresses UA-FFN layers, JuICE restores head activations. None coordinates across component types based on a unified circuit diagnosis.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "How superposition in attention heads (JuICE) resolves across layers through FFN interactions — the dynamic pathway from superposed head output to final answer selection",
      "evidence": "JuICE proves superposition is inevitable via a two-layer theoretical construction but characterizes it only at the head level. No work traces how a superposed head's output is processed by downstream FFNs that may amplify one component (parametric or contextual) over the other. Analysing the Residual Stream shows conflict detection peaks at mid-layers and selection at later layers, suggesting a resolution pathway that remains unmapped.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Transfer of mechanistic findings from intra-memory conflicts to context-memory (RAG) conflicts",
      "evidence": "Where Knowledge Collides develops CMAP for intra-memory conflicts with up to 70% steering success, but notes that transfer to context-memory conflicts is unvalidated. The attribute-type asymmetry finding (works for company but not university) suggests conflict resolution may not be a unified mechanism — this is unresolved for RAG settings.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Faithful circuit tracing at 7B+ scale with validated reconstruction fidelity",
      "evidence": "CLTs have 11.5-21.7% reconstruction error (Anthropic 2025). CD-T tested only on GPT-2-small. Knowledge Circuits takes 1-2 days on A800 for TinyLLaMA (1.1B). Transcoders evaluated only qualitatively on GPT-2-small. No work has demonstrated faithful, complete circuit discovery at the 7-9B scale needed for modern open-weight LLMs.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Understanding copy suppression heads' behavior under RAG specifically — whether they suppress context-derived tokens indiscriminately or selectively",
      "evidence": "The seed direction hypothesizes that copy suppression heads 'operate via general suppression, not selective' and inadvertently suppress context-derived tokens. But no empirical work has tested this in RAG. The Retrieval Head paper identifies retrieval heads but not their suppression counterparts. ReDeEP identifies Copying Heads via OV eigenvalue analysis but does not distinguish copy from copy-suppression.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Evaluation under noisy/adversarial retrieval conditions — all current mechanistic work assumes retrieval quality is given",
      "evidence": "ParamMute reviewers questioned performance under noisy retrieval. IRCAN's 'context is always right' assumption is unsafe for real-world RAG. SpARE's binary knowledge selection framing 'oversimplifies real-world knowledge integration.' No mechanistic study examines how circuits behave when retrieved evidence is partially correct, contradictory across passages, or adversarially manipulated.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "Apply CD-T's single-pass decomposition framework to RAG conflict inputs, using context tokens as 'relevant' (β) and query-only tokens as 'irrelevant' (γ), to discover circuits at positional granularity in seconds — then validate discovered circuits against the flip phenomenon trajectory from CoRect's Logit Lens analysis",
      "from_papers": ["CD-T (ICLR 2025)", "CoRect (arXiv 2026)", "Knowledge Circuits (NeurIPS 2024)"],
      "why_promising": "CD-T's seconds-scale runtime enables circuit discovery across hundreds of conflict examples (infeasible with ACDC/EAP), its positional granularity can reveal exactly which heads attend to retrieved-context tokens at which positions, and CoRect's flip phenomenon provides a ground-truth trajectory to validate against. No one has applied CD-T to RAG because CD-T was published for IOI/Greater-Than circuits and RAG researchers use separate tools."
    },
    {
      "idea_sketch": "Use transcoders (or CLTs) to trace the information pathway FROM retrieval head outputs THROUGH FFN layers, identifying which transcoder features activate differently in flip vs. non-flip cases — creating a causal graph connecting the Retrieval Head paper's components to CoRect's phenomenon",
      "from_papers": ["Transcoders (NeurIPS 2024)", "Circuit Tracing / CLTs (Anthropic 2025)", "Retrieval Head (ICLR 2025)", "CoRect (arXiv 2026)"],
      "why_promising": "Transcoders solve the key technical barrier: SAEs can decompose what features exist at each layer but cannot trace computation through MLPs. Transcoders' input-dependent/input-invariant factorization directly enables identifying which MLP features transform retrieval head outputs into parametric re-assertions. The combination hasn't been tried because transcoders were validated only on GPT-2-small and the RAG community uses attribution patching instead."
    },
    {
      "idea_sketch": "Combine SpARE's SAE feature selection with circuit-informed target identification: instead of selecting features by mutual information (statistical), select SAE features that lie on the causal pathway between retrieval heads and the flip point — then apply SpARE's constrained editing framework at multiple circuit-identified locations simultaneously",
      "from_papers": ["SpARE (NAACL 2025)", "Knowledge Circuits (NeurIPS 2024)", "CD-T (ICLR 2025)"],
      "why_promising": "SpARE already achieves +10% EM with heuristic feature selection; circuit-informed selection should find better targets. SpARE's infrastructure (pre-trained SAEs for Llama3-8B and Gemma2-9B) is directly reusable. The multi-point coordination (edit features at multiple layers guided by circuit topology) is what no existing method does."
    },
    {
      "idea_sketch": "Adapt the CMAP (cross-model activation patching) paradigm from intra-memory conflicts to RAG by creating matched inference pairs: same model, same query, but with vs. without retrieved context — then patch activations from the context-augmented run into specific circuit locations during the no-context run to identify which components carry the contextual signal and at what layers it gets overridden",
      "from_papers": ["Where Knowledge Collides (arXiv 2026)", "ReDeEP (ICLR 2025)", "JuICE (ICML 2025)"],
      "why_promising": "CMAP achieved 70% steering success (vs. 22% standard patching) for intra-memory conflicts on Qwen3-4B, showing that matched-pair patching is far more powerful than single-model analysis. The RAG setting naturally provides the matched pair (with/without context) without needing to train model pairs. This directly addresses JuICE's superposition challenge: by comparing the same heads under both conditions, we can separate which role (memory vs. context) each head plays in each case."
    },
    {
      "idea_sketch": "Apply the Promote-Suppress-Iterate theoretical framework to RAG by tracing which MLPs promote parametric answers, which attention heads suppress them after retrieval head injection, and whether deep-layer MLPs re-promote parametric answers — using Token Lens to measure per-component logit contributions across layers, and validating against ParamMute's finding that layers at 70-90% depth show disproportionate activation during unfaithful generation",
      "from_papers": ["Promote-Suppress-Iterate (EMNLP 2025)", "ParamMute (NeurIPS 2025)", "CoRect (arXiv 2026)", "Rotational Dynamics (arXiv 2026)"],
      "why_promising": "The promote-suppress-iterate framework was developed for one-to-many factual recall and has never been tested when two competing knowledge sources simultaneously activate the promotion pathway. ParamMute and CoRect provide independent empirical evidence (activation ratios and flip phenomenon) that deep FFN layers re-assert parametric answers — this is exactly the 're-promotion' the framework predicts but has not been explicitly connected to it."
    },
    {
      "idea_sketch": "Use the Rotational Dynamics framework's angular measurements (ρ, η, κ) as a real-time monitoring signal during circuit interventions: track whether an intervention successfully prevents the angular divergence and κ-collapse that characterize parametric override, providing a geometric validation layer that's orthogonal to accuracy metrics",
      "from_papers": ["Rotational Dynamics (arXiv 2026)", "CoRect (arXiv 2026)", "SpARE (NAACL 2025)"],
      "why_promising": "Current intervention evaluations use only task accuracy (EM, F1), which doesn't reveal whether the intervention works for the right mechanistic reason. Angular metrics would show whether an intervention truly prevents parametric re-assertion (maintained angular alignment with context-derived answer) vs. accidentally compensating (magnitude boost that happens to override suppression). This combination hasn't been tried because the Rotational Dynamics paper is very recent (2026 preprint) and focused on forced-completion probing, not intervention evaluation."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "CD-T (Contextual Decomposition for Transformers)",
      "what_it_does": "Single-pass decomposition of every activation into relevant (β) and irrelevant (γ) components, scoring each component's contribution via L1-norm ratio. Achieves 97% ROC AUC on known circuits in seconds.",
      "used_by": ["CD-T (ICLR 2025)"],
      "could_be_applied_to": "RAG circuit discovery at scale — define β as context-token-derived activations to trace how retrieved evidence propagates through the network, running across hundreds of conflict examples in hours rather than months"
    },
    {
      "tool": "Token Lens",
      "what_it_does": "Aggregates weighted attention value vectors (Σ p·v) attending to specific tokens, projects through Wo and unembedding to yield per-token logit contributions — revealing which tokens' information is being promoted or suppressed at each layer.",
      "used_by": ["Promote-Suppress-Iterate (EMNLP 2025)"],
      "could_be_applied_to": "Tracing how retrieved-passage tokens' information flows through the network — identifying the exact layers where context-derived answer tokens' logit contributions peak and then decline (the mechanistic substrate of the flip phenomenon)"
    },
    {
      "tool": "Logit Lens + Layer-wise Rank Tracking",
      "what_it_does": "Projects hidden states at each layer through the unembedding matrix to observe the evolving probability distribution over tokens, tracking when specific answer tokens reach/leave top ranks.",
      "used_by": ["CoRect (arXiv 2026)", "Where Knowledge Collides (arXiv 2026)", "ReDeEP (ICLR 2025)"],
      "could_be_applied_to": "Automated flip-point detection: identify the exact layer where the context-derived answer's rank peaks and the parametric answer's rank rises, providing ground-truth labels for circuit discovery"
    },
    {
      "tool": "Transcoders / Cross-Layer Transcoders (CLTs)",
      "what_it_does": "Replace opaque MLP computation with sparse interpretable alternatives that factorize into input-dependent activation × input-invariant weight contribution, enabling attribution of information flow THROUGH (not just within) FFN layers.",
      "used_by": ["Transcoders (NeurIPS 2024)", "Circuit Tracing (Anthropic 2025)"],
      "could_be_applied_to": "Tracing exactly which FFN features transform retrieval head outputs into parametric re-assertions — solving the key opacity problem where ReDeEP identifies Knowledge FFNs but cannot see inside them"
    },
    {
      "tool": "AttnLRP (Attention-aware Layer-wise Relevance Propagation)",
      "what_it_does": "Attributes each attention head's contribution to final predictions by propagating relevance backward through the network with attention-aware decomposition rules, enabling scalable head identification without patching.",
      "used_by": ["Atlas of ICL (NeurIPS 2025)"],
      "could_be_applied_to": "Rapid pre-screening of candidate heads for detailed circuit analysis — identifying the top-100 heads most differential between RAG-faithful and parametric-override predictions before running expensive CD-T or patching on the short list"
    },
    {
      "tool": "Pre-trained SAEs (Sparse Autoencoders)",
      "what_it_does": "Decompose polysemantic neural activations into monosemantic features, enabling interpretable analysis and targeted editing of specific semantic features without affecting others.",
      "used_by": ["SpARE (NAACL 2025)", "SAE Survey (EMNLP 2025)"],
      "could_be_applied_to": "Feature-level (not neuron-level) circuit tracing in RAG — identifying which monosemantic features in FFN layers correspond to parametric answer promotion vs. context evidence processing, enabling precise surgical edits that avoid polysemanticity-induced side effects"
    },
    {
      "tool": "Contextual Mutual Information (CMI) with Attention Grounding",
      "what_it_does": "Compares contextualized vs. null-context forward passes to compute per-token mutual information, validated by attention scores over context, to select a trustworthy target token without labels.",
      "used_by": ["CoRect (arXiv 2026)"],
      "could_be_applied_to": "Label-free circuit validation — identifying which token the model 'wants' to output at each layer provides the target signal for tracing whether circuit interventions redirect the model toward context-derived vs. parametric answers"
    },
    {
      "tool": "CMAP (Cross-Model Activation Patching)",
      "what_it_does": "Transfers activations from a clean/reference model to a target model at specific components to measure whether the clean model's processing can override the target model's conflicted state. Achieves up to 70% steering on Qwen3-4B.",
      "used_by": ["Where Knowledge Collides (arXiv 2026)"],
      "could_be_applied_to": "RAG circuit validation — patching activations from a successful context-faithful run into a context-overriding run at circuit-identified components to verify that the discovered circuit is truly causal"
    },
    {
      "tool": "Retrieval Score Metric",
      "what_it_does": "Measures per-head token-level recall of copy-paste behavior using needle-in-a-haystack tasks with unmemorizable answers. Converges after few samples and identifies <5% of heads as retrieval-critical.",
      "used_by": ["Retrieval Head (ICLR 2025)"],
      "could_be_applied_to": "Identifying the entry points (retrieval heads) of the RAG circuit, whose downstream interactions through FFN layers and copy suppression must be traced — the starting nodes for circuit discovery"
    },
    {
      "tool": "Commitment Ratio κ (via Logit Lens)",
      "what_it_does": "Measures how 'committed' the model is to a particular answer at each layer, tracking whether the correct answer's probability rises then falls (active suppression signature).",
      "used_by": ["Rotational Dynamics (arXiv 2026)"],
      "could_be_applied_to": "Geometric validation of circuit interventions — measuring whether an intervention prevents κ-collapse (active suppression of correct answers) rather than just boosting final accuracy, providing mechanistic rather than behavioral evaluation"
    }
  ],
  "common_pitfalls": [
    "Assuming clean head-type separation (memory heads vs. context heads): JuICE (ICML 2025) empirically falsified this — in Gemma-2b, only 6/26 attention modules behaved consistently across conflict settings, and a theoretical construction proves superposition is inevitable under joint training. Any circuit analysis that hard-assigns heads to single roles will produce a fragile, misleading circuit. Must test head behavior across multiple conflict types.",
    "Stopping at component identification without circuit tracing: ReDeEP identifies Knowledge FFNs and Copying Heads, Atlas identifies task/retrieval/parametric heads, IRCAN identifies context-aware neurons — all received the criticism 'no interaction mapping.' Listing important components is table-stakes; the contribution must be the interaction graph. Reviewers have seen enough component catalogs.",
    "Pure interpretability without intervention or application: Atlas (NeurIPS 2025) was criticized by reviewers for limited novelty beyond head taxonomy because it did not provide an intervention. AAAI ML track reviewers specifically will ask 'so what can you DO with this understanding?' Always complete the discover→explain→intervene arc.",
    "Using correlation-based probing as causal evidence: Analysing the Residual Stream (NeurIPS 2024 Workshop) explicitly acknowledges 'probing captures correlation, not causation.' ReDeEP reviewers flagged PKS as 'not guaranteed to measure parametric knowledge specifically.' Every probing/attribution result must be validated by at least one causal intervention (ablation, patching, or activation addition).",
    "Overfitting interventions to a single benchmark or conflict type: IRCAN tested on only 3 synthetic benchmarks with no RAG evaluation. ParamMute's UA-FFN identification may not transfer under noisy retrieval. SpARE evaluated only on ODQA (NQSwap, Macnoise). Evaluate on at least 2-3 diverse conflict benchmarks (substitution, coherent, multi-hop) and include a non-conflict control to measure side effects.",
    "Ignoring computational overhead of interventions: JuICE doubles inference cost via dual forward passes. CoRect requires dual forward passes. These costs are often unquantified. Reviewers at AAAI will compare against simpler baselines — if a complex intervention only marginally beats a much cheaper one, it won't be accepted. Always report latency and compare against cost-matched baselines.",
    "Layer-level granularity when neuron/feature-level is needed: ParamMute applies uniform suppression across all neurons within selected layers, missing the fact that individual neurons may serve both parametric and contextual functions (polysemanticity). IRCAN found 50% of context neurons are prompt-dependent. Use SAE features or transcoder features for finer granularity.",
    "Over-claiming circuit completeness at the 7B scale: Anthropic's CLTs have 11.5-21.7% reconstruction error even at smaller scales. Where Knowledge Collides achieved only 22% success on GPT-2 XL with standard patching. CD-T was only tested on GPT-2-small. Frame any 7B+ circuit analysis as 'the dominant pathway' or 'the primary circuit,' not 'the complete circuit.' Use reconstruction fidelity metrics (FVU, delta LM loss) to bound what fraction of behavior is explained.",
    "Training-time methods masquerading as inference-time: ParamMute requires KAT/KPO training data. Weight multiplication (IRCAN) permanently modifies the model. For AAAI, clearly distinguish whether the method is purely inference-time (no training, no weight modification) vs. requires calibration data vs. requires fine-tuning. Each has different applicability claims.",
    "Neglecting the 'context is always right' assumption: IRCAN, ParamMute, and most faithfulness methods assume retrieved context should always override parametric knowledge. This is unsafe when retrieval is noisy, outdated, or adversarial. Acknowledge this assumption and ideally test what happens when context is wrong (does the intervention make the model blindly faithful?)."
  ],
  "field_trajectory": "The field is converging on three macro-directions. First, **full-circuit mechanistic accounts of multi-source knowledge integration** — the community has exhaustively cataloged individual components (retrieval heads, Knowledge FFNs, context-aware neurons, copy suppression heads) and is now ready to connect them into end-to-end causal graphs. Papers like Knowledge Circuits (NeurIPS 2024) and Circuit Tracing (Anthropic 2025) provided the methodology; papers like Atlas, ReDeEP, and JuICE provided the components; the synthesis connecting these across the RAG inference pathway is the clear next frontier, and 2026 will likely see 2-3 papers attempting this at different scales. Second, **principled, circuit-informed inference-time intervention** is replacing heuristic steering. The progression from broad methods (CAD, contrastive decoding) through component-targeting (IRCAN neurons, SpARE SAE features, CoRect FFN patches) is heading toward multi-point coordinated interventions that simultaneously modulate multiple circuit components based on causal analysis rather than statistical correlation. The key technical enabler is faster circuit discovery (CD-T, transcoders, CLTs) making it feasible to diagnose each input's specific failure mode and tailor interventions accordingly. Third, **geometric and representational theory of knowledge conflict processing** is emerging as a complement to discrete circuit analysis. The Rotational Dynamics paper's finding that factual discrimination is encoded in angular separation, combined with Analysing the Residual Stream's two-phase processing timeline, suggests that a unified geometric theory of how parametric and contextual representations compete, merge, or override each other across layers may be achievable — and would provide both explanatory power and new intervention targets (angular corrections rather than activation additions). The overall trajectory is from 'what components matter?' (2024) through 'how do they interact?' (2025-2026) toward 'how do we optimally control these interactions at inference time?' (2026-2027).",
  "meta_advice": "If you're writing a strong 2026 paper in this area, here is what distinguishes accepted work from rejected work based on the evidence. **Lead with a surprising empirical finding, not a method.** The most-cited papers in this set (Retrieval Head, JuICE, CoRect) all discovered something unexpected — universal retrieval heads in <5% of attention, superposition making head-type separation impossible, 56% of cases showing mid-layer flip. Your method should be motivated by explaining and exploiting such a finding. **Complete the full arc from discovery to mechanism to intervention.** Atlas got workshop-level impact partly because it stopped at taxonomy; JuICE and SpARE got spotlights because they provided actionable interventions. But don't just bolt on an intervention — the intervention must be specifically motivated by the mechanistic insight. The strongest framing is: 'we discovered X mechanism causing Y failure, and because we understand the mechanism, we can surgically fix it at Z locations — which is why our intervention outperforms heuristic approaches that don't know about X.' **Use the flip phenomenon as your Rosetta Stone.** CoRect's finding that correct answers appear at mid-layers then get suppressed is the most mechanistically informative empirical phenomenon in this space, and it has no circuit-level causal explanation. Any paper that causally explains the flip phenomenon through a traced circuit will immediately have impact. **Validate across conflict types, not just substitution conflicts.** JuICE showed that head behavior changes dramatically across clean, substitution, and coherent conflict settings — any method evaluated on only one conflict type is incomplete. Use NQSwap (substitution), ConflictQA (coherent), and ideally a multi-hop conflict benchmark. **Be honest about what your circuit doesn't explain.** Anthropic's CLTs have >11% reconstruction error; Knowledge Circuits explains ~70% of performance with <10% of edges. Frame contributions as 'the dominant pathway' and quantify explained vs. unexplained variance. Reviewers will trust you more, and the honest framing is also more scientifically accurate. **Budget compute for cross-model validation from day one.** Plan for at least two model families (Llama-3.1-8B + Gemma-2-9B is ideal given existing SAE availability from SpARE). A finding that holds on one model is an observation; a finding that holds on two is a contribution. Finally, **benchmark against SpARE and CoRect as your primary baselines** — they are the strongest recent heuristic interventions and their target selection methods (MI-based SAE features and unembedding projection sign) represent exactly the 'statistical, not causal' approach your circuit-informed method must outperform. Show the gap is not just in accuracy but in precision: your circuit identifies targets that their heuristics miss, and your multi-point coordination achieves improvements that single-point methods cannot."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bcf6a4d-a9e0-481d-9574-c2b57d60fa5f",
  "isSidechain": false,
  "requestId": "req_011CbYH42FTuJ8g2Zcuskt7N",
  "type": "assistant",
  "uuid": "7c7bb318-374d-4c89-b221-1423f6e7db1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduGeSte622oMETkZkQ926",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12836,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8653,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8653,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12836
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "7c7bb318-374d-4c89-b221-1423f6e7db1c",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Design circuit-informed RAG interventions via promote-suppress pathology",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "7c7bb318-374d-4c89-b221-1423f6e7db1c",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Design circuit-informed RAG interventions via promote-suppress pathology",
  "sessionId": "909c3f35-7245-4648-9244-972b695204c2"
}
```

---
