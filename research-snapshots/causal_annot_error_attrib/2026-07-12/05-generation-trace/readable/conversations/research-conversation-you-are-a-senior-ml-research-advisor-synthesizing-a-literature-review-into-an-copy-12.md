# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/13bd2976-51f0-4e17-a33b-807055254d4e.jsonl`
- **Structured JSON:** [`6479c823d3df05a53e41.json`](../../sessions/64/6479c823d3df05a53e41.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:48:03.971Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:48:03.971Z",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning / Knowledge Representation and Reasoning\n\nDirection: Trace the complete computational circuit governing RAG evidence integration vs. override in open-weight LLMs, mapping causal interactions between retrieval heads, parametric memory components, copy suppression mechanisms, and FFN layers. Use the discovered circuit to design principled, multi-point inference-time interventions that outperform existing heuristic steering methods (SpARE, CoRect, ContextFocus) on knowledge-conflict benchmarks.\n\nSeed Papers:\n- ReDeEP (ICLR 2025) — Identifies Knowledge FFNs and Copying Heads as key components but stops at component-level; no circuit tracing\n- Retrieval Head Mechanistically Explains Long-Context Factuality (ICLR 2025) — Identifies <5% of heads carry retrieval signal; universal across model families; but no interaction with parametric circuits\n- Taming Knowledge Conflicts / JuICE (ICML 2025) — Discovers superposition in attention heads (both memory and context); proposes test-time intervention; complicates clean head-type dichotomy but remains head-level\n- CoRect (arXiv 2025) — Discovers flip phenomenon (56% of conflict cases); deep FFN layers suppress correct answers; intervention is additive patching without circuit diagnosis\n- Knowledge Circuits in Pretrained Transformers (NeurIPS 2024) — Provides circuit discovery methodology for factual recall; not applied to RAG\n- CD-T: Efficient Automated Circuit Discovery (ICLR 2025) — Enables circuit discovery in seconds; 97% ROC AUC; key enabling tool\n- SpARE (NAACL 2025) — SAE-based steering under knowledge conflicts; +10% EM; heuristic target selection\n- Atlas of In-Context Learning (NeurIPS 2025) — Separates in-context vs parametric heads; 94% AUC linear probe; but no causal interaction mapping\n\nKnown Gaps:\n- No end-to-end circuit has been traced connecting retrieval heads → FFN layers → copy suppression → output in RAG, comparing success vs failure cases\n- JUICE shows heads operate in superposition (both memory and context), but no work has traced how this superposition resolves across layers and through FFN interactions\n- The flip phenomenon (CoRect: correct answers appear mid-layers then get suppressed) has no circuit-level causal explanation\n- Existing interventions (SpARE, CoRect, ContextFocus, JuICE) select targets heuristically or statistically, not via causal circuit analysis; no multi-point coordinated intervention exists\n\nTheoretical Anchor: The promote-suppress-iterate mechanism (Yan & Jia, EMNLP 2025) provides a theoretical framework — MLPs promote all candidate answers while attention suppresses alternatives iteratively. In RAG, this mechanism should create a specific circuit pathology: retrieval heads promote context-derived answers, but parametric MLPs re-promote stored answers in deeper layers, and copy suppression heads (which operate via general suppression, not selective) inadvertently suppress context-derived tokens. The flip phenomenon is a direct observable consequence of this circuit pathology.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Models: Llama-3.1-8B (primary), Gemma-2-9B (validation)\n- Tools: CD-T, TransformerLens, pyvene, attribution patching\n- Timeline: 10-12 weeks to AAAI August 2026 deadline\n\nQuality Self-Checks:\n- [x] Core insight: In RAG, evidence override is caused by a specific circuit pathology where parametric MLPs in deep layers re-assert stored answers after retrieval heads have already injected context-derived answers — and this pathology can be surgically repaired.\n- [x] Why not obvious: JUICE shows heads are in superposition (not cleanly separable), so you can't just prune memory heads. You need full circuit tracing to find where the parametric signal actually dominates, which requires the promote-suppress-iterate lens applied to RAG specifically.\n- [x] Baseline fear test: Simple baselines (prune top-k memory heads, boost top-k retrieval heads) exist (Jin et al. 2024, IRCAN). Circuit-informed intervention must show that selecting targets via causal analysis yields better targets than statistical/heuristic selection. The multi-point coordination (boost + suppress simultaneously at circuit-identified layers) is what baselines cannot do.\n- [x] Information exploited: The full causal interaction graph between components that existing methods treat in isolation. Specifically, which FFN neurons in which layers re-assert parametric answers AFTER retrieval heads have already injected context, and which copy suppression heads inadvertently suppress context-derived tokens.\n\nAvoid:\n- Replicating ReDeEP at larger scale (component identification without circuit tracing)\n- Assuming clean retrieval-head vs memory-head separation (JUICE refutes this; must account for superposition)\n- Pure interpretability without intervention (AAAI reviewers will ask 'so what?')\n- Ignoring the flip phenomenon as validation (it's the most mechanistically informative empirical finding)\n- Over-claiming circuit completeness (circuits at 7B may be distributed; frame contributions carefully)\n\n## Paper analyses (23 papers)\n\n[\n  {\n    \"title\": \"Knowledge Circuits in Pretrained Transformers\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"Prior work treated knowledge-storing components (MLPs, attention heads) as isolated units ('Restorative Theory'). No work had traced how these components collaborate as circuits for factual recall, despite circuit analysis succeeding on algorithmic tasks.\",\n    \"key_insight\": \"Factual recall operates through structured subgraphs with three functionally specialized head types — mover heads (extract subject attributes), relation heads (extract relation attributes), and mixture heads (combine information) — whose interactions explain hallucinations, knowledge editing failures, and ICL.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Applies ACDC and EAP-IG circuit discovery to factual recall on GPT-2 and TinyLLaMA. Edges are scored via zero ablation with MatchNLL loss and pruned in reverse topological order (5-8x faster than forward). Resulting circuits use <10% of edges but retain ~70% Hit@10 performance. Component roles are analyzed via unembedding projection and attention pattern visualization.\",\n    \"limitations_and_open_questions\": \"Reviewers noted the methodology is 'a direct application of standard causal mediation analysis' with no concrete downstream application. Limited to GPT-2/TinyLLaMA scale; threshold-sensitive; traversal order affects discovered circuits. Head-type definitions (mover/relation/mixture) lack rigorous statistical justification.\",\n    \"building_blocks\": [\n      \"EAP-IG for efficient edge attribution\",\n      \"Reverse topological pruning order\",\n      \"Mover/relation/mixture head taxonomy\",\n      \"Unembedding projection for component analysis\"\n    ],\n    \"relevance_to_seed\": \"Provides the foundational circuit discovery methodology we must adapt for RAG — but their circuits cover only parametric factual recall, not the retrieval-context integration pathway where parametric and contextual signals compete.\"\n  },\n  {\n    \"title\": \"Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Circuit discovery faced a scalability-interpretability tradeoff: coarse-grained circuits (head/MLP nodes) are polysemantic and hard to interpret, while fine-grained approaches require pre-existing mechanistic hypotheses. Neither paradigm could scalably discover unexpected mechanisms.\",\n    \"key_insight\": \"SAE features resolve polysemanticity by providing monosemantic circuit nodes — enabling circuits that are simultaneously interpretable (each node represents one concept) and discoverable (via standard causal methods on the SAE-decomposed computation graph).\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Decomposes every activation via trained SAEs into sparse monosemantic features, making each feature (plus error terms) a node in the computation graph. Uses attribution patching with integrated gradients (N=10 interpolation points) to discover causal edges. The SHIFT method enables debiasing by human-inspecting circuit features and zero-ablating spurious ones — improving worst-group accuracy from 24% to 89% without disambiguating data. An unsupervised pipeline clusters model behaviors via gradient-space clustering and extracts circuits for thousands of behaviors automatically.\",\n    \"limitations_and_open_questions\": \"Depends entirely on SAE quality; error terms remain uninterpretable. SHIFT requires human annotation (scalability bottleneck). Supervised evaluation limited to simple grammatical tasks. How well do SAE-based circuits capture the superposition phenomena identified by JuICE?\",\n    \"building_blocks\": [\n      \"SAE features as circuit nodes\",\n      \"SHIFT editing via feature ablation\",\n      \"Gradient-based behavior clustering\",\n      \"Integrated gradients for attribution patching\"\n    ],\n    \"relevance_to_seed\": \"Offers a strictly more interpretable circuit formulation than head-level analysis — critical for disentangling the superposition JuICE identified where heads carry both memory and context signals. SAE feature-level circuits could separate these into distinct monosemantic pathways.\"\n  },\n  {\n    \"title\": \"CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Using Logit Lens on 500 NQ conflict cases, discovered the 'flip phenomenon': in 56% of failures (282/500), the correct context-derived answer appears in intermediate layers but gets suppressed by deeper FFN layers before output — split into 'middle flip' (154 cases) and 'last-layer flip' (128 cases).\",\n    \"key_insight\": \"Knowledge conflicts are predominantly a suppression problem, not a comprehension problem — the model internally 'knows' the correct answer from context in over half of failure cases, but parametric FFN memories actively overwrite it.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Two-stage training-free inference-time method. Stage 1: contrastive forward passes (context vs. null) compute contextual mutual information scores to identify trustworthy target tokens without ground-truth labels, filtered by attention-based faithfulness verification. Stage 2: identifies suppressive FFN layers (those with negative projection onto target's unembedding vector) and applies additive rectification patches that geometrically guarantee positive logit shifts — a 'disinhibition' paradigm that removes blockages rather than forceful steering.\",\n    \"limitations_and_open_questions\": \"44% of failures don't exhibit the flip phenomenon — what other mechanisms cause them? No comparison with SpARE or ContextFocus. Last-layer flip vs. middle flip may involve different mechanisms but are treated uniformly. No circuit-level causal explanation for WHY specific FFN layers suppress — exactly the gap our project targets.\",\n    \"building_blocks\": [\n      \"Flip phenomenon quantification methodology\",\n      \"Contrastive null-pass token selection\",\n      \"Geometric suppressive layer identification via unembedding projection\",\n      \"Disinhibition-based rectification\"\n    ],\n    \"relevance_to_seed\": \"The flip phenomenon is the most mechanistically informative empirical finding for our project — it's the observable consequence of the promote-suppress-iterate pathology we hypothesize. CoRect's intervention is effective but heuristic; our circuit analysis should explain which specific neurons/features cause suppression and enable more targeted multi-point intervention.\"\n  },\n  {\n    \"title\": \"On Mechanistic Circuits for Extractive Question-Answering\",\n    \"venue\": \"COLM 2025\",\n    \"problem_identification\": \"Mechanistic circuit analysis had been confined to toy/synthetic tasks. No one had extracted circuits for context-augmented extractive QA — the real-world setting where models must decide between context extraction and parametric recall.\",\n    \"key_insight\": \"Context-faithfulness and memory-faithfulness activate qualitatively different neural pathways with minimal overlap — context circuits are compact (4-5 attention layers, minimal MLP) while memory circuits are large and distributed (>15 layers, >30 heads, heavy MLP involvement).\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Constructs probe datasets D_copy (token-swapped contexts forcing context extraction) and D_memory (corrupted contexts forcing parametric recall). Applies hierarchical causal mediation analysis with greedy component selection until δ=0.95 threshold. Discovers that a single attention head reliably attends to answer spans, yielding ATTNATTRIB — zero-cost attribution during generation. Steering combines attention upweighting (β=10 at context-circuit heads) and MLP mean-ablation (at memory-circuit MLPs), redirecting 92% of memory-based answers to context.\",\n    \"limitations_and_open_questions\": \"Restricted to single-hop extractive QA; probe datasets use artificial token-swap perturbations. Circuit interactions when both pathways activate simultaneously are uncharacterized. Reviewers noted path-patching may capture correlations, not strict causation. No analysis of multi-hop reasoning or RAG-scale retrieval.\",\n    \"building_blocks\": [\n      \"D_copy/D_memory probe dataset design\",\n      \"ATTNATTRIB zero-cost attribution\",\n      \"Combined attention upweighting + MLP ablation steering\",\n      \"Hierarchical circuit extraction methodology\"\n    ],\n    \"relevance_to_seed\": \"Most directly relevant prior work — demonstrates circuit-based steering for context vs. memory in QA. However, their clean separation (compact context circuit vs. distributed memory circuit) may not hold under JuICE's superposition finding. Our project must handle the messier case where the same heads carry both signals, requiring SAE-level decomposition rather than head-level circuits.\"\n  },\n  {\n    \"title\": \"Knowledge Conflicts for LLMs: A Survey\",\n    \"venue\": \"EMNLP 2024\",\n    \"problem_identification\": \"No unified framework existed for understanding the landscape of knowledge conflicts in LLMs. Research was fragmented across context-memory, inter-context, and intra-memory conflicts with no systematic organization of causes, behaviors, and solutions.\",\n    \"key_insight\": \"Knowledge prioritization depends on semantic coherence, logical structure, and persuasiveness of competing sources — not simply on source type (context vs. memory) — and a 40% gap exists between knowledge probe accuracy and generation accuracy, showing models store correct knowledge they cannot reliably express.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Systematically catalogs three conflict types (context-memory, inter-context, intra-memory) with their causes, model behaviors, and resolution strategies. Organizes solutions into pre-hoc (fine-tuning, pre-training, discriminators) and post-hoc (decoding, prompting, ensemble) families. Identifies seven open problems including mechanistic explainability, conflict interplay, and multimodality.\",\n    \"limitations_and_open_questions\": \"All cataloged resolution strategies are behavioral interventions — no mechanistic/circuit-level approaches. The survey explicitly flags 'microscopic examinations of attention heads and neuron activations' as the key open problem. Literature is dominated by artificial conflict scenarios (entity substitution), limiting ecological validity.\",\n    \"building_blocks\": [\n      \"CM/IC/IM conflict taxonomy\",\n      \"Pre-hoc vs. post-hoc solution framework\",\n      \"Catalog of conflict benchmarks (NQ-Swap, ConflictQA, etc.)\",\n      \"Seven open research directions\"\n    ],\n    \"relevance_to_seed\": \"Defines our problem space and explicitly identifies mechanistic understanding as the key open problem (Open Problem #5). The survey's behavioral-level characterizations are precisely what our circuit analysis aims to explain mechanistically — transforming 'what happens' into 'why it happens' at the component level.\"\n  },\n  {\n    \"title\": \"Do All Autoregressive Transformers Remember Facts the Same Way? A Cross-Architecture Analysis of Recall Mechanisms\",\n    \"venue\": \"EMNLP 2025\",\n    \"problem_identification\": \"The widely-assumed universality of MLP-based factual recall (from Meng et al.'s work on GPT) was never validated across architectures. Knowledge editing methods (ROME, MEMIT) and interpretability tools assumed MLP dominance as a universal property of transformers.\",\n    \"key_insight\": \"Factual recall localization is architecture-specific, not universal: GPT/LLaMA use early MLP layers while Qwen/DeepSeek concentrate recall in early attention layers — and no single architectural factor (hidden size, head count, GQA vs. MHA, vocabulary) explains the divergence.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Compares 17 models across 4 families (GPT, LLaMA, Qwen, DeepSeek) using three complementary techniques: restoration effects (causal tracing with Gaussian noise), severing effects (blocking module outputs), and knockout (blocking 5 consecutive layers). Resolves discrepancies between restoration and severing via Gini coefficient analysis of AIE concentration. Introduces semantic similarity evaluation (Sentence-BERT, τ=0.7) to handle lexically different but semantically correct predictions.\",\n    \"limitations_and_open_questions\": \"Identifies WHERE facts are stored but not HOW recall works mechanistically. Cannot explain WHY architectures differ — all individual factors were ruled out, suggesting complex interactions with training dynamics. Limited to CounterFact dataset (100 sentences/model). Does this architecture-specificity extend to RAG integration circuits?\",\n    \"building_blocks\": [\n      \"Gini coefficient for AIE concentration analysis\",\n      \"Semantic similarity evaluation for factual recall\",\n      \"Cross-architecture comparison methodology\",\n      \"Architecture-specificity of recall mechanisms\"\n    ],\n    \"relevance_to_seed\": \"Critical validation constraint: our circuit discoveries on Llama-3.1-8B (MLP-dominated recall) may not transfer to Gemma-2-9B validation. We must verify that the RAG integration circuit — not just the parametric recall circuit — shows consistent structure across architectures, or explicitly characterize the differences.\"\n  },\n  {\n    \"title\": \"Retrieval Head Mechanistically Explains Long-Context Factuality\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"No mechanistic explanation existed for how LLMs retrieve facts from arbitrary positions in long contexts. Identified via observation that models pass NIAH tests but no one traced which components are responsible.\",\n    \"key_insight\": \"Fewer than 5% of attention heads ('retrieval heads') perform nearly all factual retrieval via a copy-paste algorithm; they are intrinsic to short-context pretraining and persist unchanged through context extension.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Defined a retrieval score as token-level recall of copy-paste behavior during autoregressive decoding, thresholded across ~600 NIAH instances per model. Validated causally: masking retrieval heads drops accuracy to 63.6% vs 94.7% for random-head masking. Extended induction-head analysis from Olsson et al. to long-context retrieval across 4 model families and 6 scales.\",\n    \"limitations_and_open_questions\": \"Detection relies on synthetic copy-paste tasks that may not capture paraphrastic retrieval; no analysis of downstream circuit pathways beyond retrieval heads (no FFN interaction, no copy suppression tracing). Only decoder-only full-attention architectures tested.\",\n    \"building_blocks\": [\n      \"Retrieval score metric\",\n      \"NIAH-based head classification protocol\",\n      \"Causal head ablation methodology\",\n      \"Per-model retrieval head indices\",\n      \"Retrieval head detection algorithm\"\n    ],\n    \"relevance_to_seed\": \"Provides the entry point of the RAG circuit — the sparse retrieval heads that inject context signal — but stops at component identification without tracing how this signal propagates through FFNs and copy suppression to the output.\"\n  },\n  {\n    \"title\": \"Scaling and Evaluating Sparse Autoencoders\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"ReLU-based SAEs suffer from activation shrinkage (L1 penalty biases activations toward zero) and massive dead latents (up to 90% inactive), with no rigorous scaling laws or evaluation suite. Identified by measuring systematic underestimation in ReLU activations with frozen masks.\",\n    \"key_insight\": \"Sparsity control and reconstruction quality are separable: using TopK activation (keep k largest, zero rest) enforces sparsity architecturally rather than via loss penalty, eliminating shrinkage entirely.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Replaced min(reconstruction + λ·L1) with min(reconstruction) subject to exactly-k-sparse activations via TopK. Introduced AuxK auxiliary loss using top-k_aux dead latents to model residual error, reducing dead latents to 7% at 16M scale. Established clean power-law scaling L(n,k) with tokens-to-convergence scaling as n^0.6.\",\n    \"limitations_and_open_questions\": \"Evaluation metrics are proxies (no ground-truth features exist); TopK forces uniform sparsity per input (real feature counts may vary); no causal/circuit-level validation of learned features; computational cost at 16M scale is substantial.\",\n    \"building_blocks\": [\n      \"TopK SAE architecture\",\n      \"AuxK dead-latent revival loss\",\n      \"Scaling laws L(n,k)\",\n      \"Evaluation suite: downstream loss, probe loss (61 tasks), N2G explainability, ablation sparsity\"\n    ],\n    \"relevance_to_seed\": \"Provides the SAE methodology backbone for SpARE-style interventions — TopK SAEs yield cleaner, sparser features for identifying retrieval-faithfulness latents in residual streams at circuit-critical layers.\"\n  },\n  {\n    \"title\": \"ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"Prior RAG hallucination detectors treated external context usage and parametric knowledge as independent signals. Using OV matrix eigenvalue analysis and FFN vocabulary-space projection, authors showed these pathways confound each other — analyzing one without controlling the other yields inaccurate detection.\",\n    \"key_insight\": \"RAG hallucinations arise from an imbalance between Knowledge FFNs (later-layer FFNs injecting parametric knowledge) and Copying Heads (positive OV-eigenvalue heads copying from context) — the interaction, not either component alone, drives hallucination.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defined External Context Score (cosine similarity of attended-token hidden states to generated token via Copying Heads) and Parametric Knowledge Score (JSD between vocab distributions before/after FFN layers). Cast detection as multivariate regression treating each as confounder. AARF intervention amplifies copying head attention (α>1) and dampens FFN contributions (β<1) when hallucination score exceeds threshold τ.\",\n    \"limitations_and_open_questions\": \"ECS/PKS are intuitive proxies without provable faithfulness; heavy hyperparameter burden (α, β, τ, top-K, chunk size) varies per model/dataset with no automated selection. Reviewer criticism: missing strong baselines (AlignScore at 84-86% F1) and noisy causal results.\",\n    \"building_blocks\": [\n      \"ECS/PKS scoring framework\",\n      \"OV-eigenvalue copying head identification\",\n      \"JSD-based FFN knowledge attribution\",\n      \"AARF intervention mechanism\",\n      \"RAGTruth and Dolly-AC benchmarks\"\n    ],\n    \"relevance_to_seed\": \"Identifies the two key RAG component types (Knowledge FFNs, Copying Heads) and quantifies their aggregate interaction, but does not trace the circuit connecting them — exactly the gap our proposed work fills.\"\n  },\n  {\n    \"title\": \"Position-aware Automatic Circuit Discovery\",\n    \"venue\": \"ACL 2025\",\n    \"problem_identification\": \"Existing circuit discovery methods (EAP, ACDC) aggregate edge importance across all token positions, causing score cancellation (opposite-sign contributions net to zero) and overestimation (many small cross-position effects outrank important single-position edges). Demonstrated empirically on GPT-2-small.\",\n    \"key_insight\": \"Attention edges are inherently cross-positional (query at position t, key/value at position t'); collapsing positions before scoring destroys this structure and hides functionally critical edges.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Extended Edge Attribution Patching to position-specific gradient computation by recasting the computation graph from (component, layer) to (component, layer, position) nodes, tripling attention edge granularity. Introduced 'dataset schemas' — abstract semantic span labels (Subject, Verb, IO) that align variable-length examples into a common positional frame. Automated schema generation via LLM-generated saliency-guided annotation.\",\n    \"limitations_and_open_questions\": \"Schemas require fixed span ordering across examples with no general design principles; tested on only 2 models and 3 tasks; no comparison to ACDC; schema transferability across models is poor.\",\n    \"building_blocks\": [\n      \"PEAP method and code (github.com/technion-cs-nlp/PEAP)\",\n      \"Dataset schema formalism\",\n      \"LLM+saliency automated schema pipeline\",\n      \"Position-aware edge attribution patching\"\n    ],\n    \"relevance_to_seed\": \"Directly applicable to RAG circuit discovery where context tokens and query tokens play structurally different roles — PEAP's schema formalism can define 'Query', 'Passage', 'Answer' spans to discover position-sensitive retrieval circuits.\"\n  },\n  {\n    \"title\": \"Open Problems in Mechanistic Interpretability\",\n    \"venue\": \"TMLR 2025\",\n    \"problem_identification\": \"The MI field lacked a unified research agenda. 29 researchers across 18 organizations synthesized scattered knowledge via collaborative expert elicitation, identifying that current work overwhelmingly focuses on activations (what neurons represent) while neglecting mechanisms (how weights compute representations).\",\n    \"key_insight\": \"Mechanistic interpretability decomposes into a pipeline — decomposition → description → validation — and each stage has distinct failure modes (polysemanticity, interpretability illusions, lack of causal grounding) that current methods systematically conflate.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Taxonomized open problems across three axes: methods/foundations (8 SDL limitations, circuit completeness, feature universality), applications (monitoring unsafe cognition, predicting novel-situation behavior), and socio-technical challenges (automation, adversarial robustness of explanations). Critically evaluated SAEs, probing, circuit discovery, and attribution methods, proposing intrinsic interpretability as underexplored.\",\n    \"limitations_and_open_questions\": \"SDL features are distribution-dependent and may not map to human concepts; validation methods are gameable; no formal theoretical foundation connects interpretability to generalization; circuit completeness may be intractable for distributed representations.\",\n    \"building_blocks\": [\n      \"Decompose-describe-validate pipeline framework\",\n      \"Taxonomy of SAE limitations\",\n      \"Criteria for circuit completeness\",\n      \"Feature universality evaluation criteria\"\n    ],\n    \"relevance_to_seed\": \"Frames the circuit completeness challenge our work faces — distributed representations across heads/layers make complete circuit identification hard — and warns that SDL latents are dataset-dependent, relevant for SAE-based feature extraction in RAG circuits.\"\n  },\n  {\n    \"title\": \"IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"LLMs' parametric knowledge conflicts with contextual knowledge at inference time, causing hallucinations. Prior work used prompt engineering or decoding strategies but never directly intervened at the neuron level to prioritize context processing.\",\n    \"key_insight\": \"Specific FFN neurons are disproportionately responsible for context processing vs. parametric recall; these can be identified via integrated gradients measuring each neuron's marginal contribution to context processing, then amplified via simple weight scaling without retraining.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Defined attribution score Attr(n) = (v_{c,q} - v_q) · ∫gradient measuring each neuron's marginal context contribution. Selected top neurons by co-occurrence frequency across examples as a shared reusable set. Applied multiplicative weight scaling (W' = β·W) at inference, combinable with Context-Aware Decoding for further gains. Achieved 129-136% accuracy improvement on MemoTrap.\",\n    \"limitations_and_open_questions\": \"Only evaluated on 3 synthetic benchmarks; untested on long-context/RAG settings; no mechanism to distinguish reliable vs. unreliable context; context-aware neurons assumed transferable across instances. Reviewer criticism: no comparison with probing/SAE-based steering; safety concern that forcing context fidelity could amplify jailbreaks.\",\n    \"building_blocks\": [\n      \"Integrated-gradient neuron attribution pipeline\",\n      \"Intersection-based neuron selection heuristic\",\n      \"Multiplicative reweighting intervention template\",\n      \"MemoTrap/COSE_KRE/ECARE_KRE benchmarks\"\n    ],\n    \"relevance_to_seed\": \"The primary baseline for statistical neuron selection in knowledge conflicts — IRCAN's gradient-attribution + frequency heuristic approach is the natural comparison point for circuit-based targeting that claims more principled and precise intervention.\"\n  },\n  {\n    \"title\": \"Taming Knowledge Conflicts in Language Models (JuICE)\",\n    \"venue\": \"ICML 2025 (Spotlight)\",\n    \"problem_identification\": \"Prior work assumed attention heads are either 'memory heads' or 'context heads' with fixed roles. The authors showed empirically that top-ranked memory heads flip behavior across conflict types (e.g., Head (9,3) in Gemma shifts from +0.13 to -0.17 context probability), and combining individually effective heads causes counteracting degradation (top-10 heads perform worse than top-3).\",\n    \"key_insight\": \"Influential attention heads operate in superposition—simultaneously carrying both parametric and contextual signals—making single-pass interventions unreliable because modified activations cascade through the residual stream and alter downstream head roles.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"JuICE identifies reliable heads by filtering for consistency across multiple conflict types (substitution, coherent counterfactual), retaining only heads with non-negative scores under all conditions. At inference, a dual-run approach caches unperturbed first-run head activations, then injects them as steering signals during a second forward pass, avoiding the cascade effects that degrade single-pass interventions. Theoretical analysis on a two-layer transformer proves superposition emerges naturally from gradient descent and that dual-run succeeds where single-pass deletion fails.\",\n    \"limitations_and_open_questions\": \"Doubles inference cost via two forward passes; only handles binary parametric-vs-contextual conflicts, not partial relevance. Does not trace the full circuit—operates at the head level without analyzing FFN interactions or information flow pathways.\",\n    \"building_blocks\": [\n      \"ParaConflict benchmark (6 datasets, 3 conflict types)\",\n      \"Dual-run activation caching intervention\",\n      \"Cross-conflict-type consistency filtering for head selection\",\n      \"Theoretical framework proving superposition emergence\"\n    ],\n    \"relevance_to_seed\": \"Directly validates that clean head-type separation is impossible (superposition), motivating full circuit tracing; the dual-run technique could serve as one intervention point in a multi-point circuit-informed strategy.\"\n  },\n  {\n    \"title\": \"Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (SpARE)\",\n    \"venue\": \"NAACL 2025 (Oral)\",\n    \"problem_identification\": \"Existing representation engineering methods (ActAdd, TaskVec) use polysemantic dense activation vectors for steering, leading to imprecise interventions. The authors identified that SAE features provide monosemantic decomposition suitable for targeted knowledge selection control, and that knowledge conflict signals are detectable at mid-layers.\",\n    \"key_insight\": \"Pre-trained SAE features can isolate monosemantic dimensions controlling knowledge source selection, enabling bidirectional steering (add parametric features while removing contextual features, or vice versa) with input-dependent clamping constraints to prevent destructive edits.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"SpARE collects hidden states from conflict instances grouped by behavioral outcome (contextual vs parametric answer), encodes them through pre-trained SAEs, ranks features by mutual information I(Z_i; Y) with answer type, and selects top-k features with directional association via mean comparison. Steering applies simultaneous removal and addition of opposing feature sets with input-dependent clamping (min/max constraints) to the hidden states at mid-layers, decoded back via SAE decoder. Achieves +10% over ActAdd and +15% over contrastive decoding on NQSwap.\",\n    \"limitations_and_open_questions\": \"Feature selection is purely correlational (mutual information), not causally verified via circuit analysis. Requires pre-trained SAEs (not available for all models). Only tested on binary QA conflicts at 7-9B scale. How do selected SAE features map to specific circuit components?\",\n    \"building_blocks\": [\n      \"SAE-based monosemantic feature identification for knowledge conflicts\",\n      \"Bidirectional activation editing with input-dependent clamping\",\n      \"Mutual information ranking for feature selection\",\n      \"Mid-layer intervention targeting\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline—demonstrates SAE features can steer knowledge selection but selects targets heuristically. Circuit-informed intervention should identify the same (or better) targets via causal analysis, and coordinate multi-point interventions that SpARE's single-layer approach cannot.\"\n  },\n  {\n    \"title\": \"The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Despite growing use of retrieval-augmented generation, the internal mechanisms by which LLMs integrate retrieved context vs parametric knowledge remained opaque. No systematic taxonomy existed mapping which attention heads serve retrieval vs parametric roles, nor how to trace knowledge source attribution at inference time.\",\n    \"key_insight\": \"A contrastive attribution design (open-book with counterfactual contexts vs closed-book) using AttnLRP cleanly separates in-context heads (deeper layers, retrieve from context) from parametric heads (early layers, store relational knowledge), with further decomposition into task heads (middle layers, encode question semantics) and retrieval heads.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Uses AttnLRP (attention-aware LRP) to compute per-head relevance scores, then applies a contrastive difference score between open-book (counterfactual context) and closed-book settings to classify heads as in-context or parametric. Within in-context heads, token-level relevance aggregation separates task heads from retrieval heads. Function vectors extracted from each head type demonstrate causal roles: task head FVs achieve 94.75% zero-shot question induction, retrieval head attention amplification yields 93.45% recall. A linear probe over retrieval head logit-lens outputs achieves ≥94% AUC for knowledge source detection.\",\n    \"limitations_and_open_questions\": \"Explicitly acknowledges no analysis of MLP interactions—'how they interact with MLP modules remains an open question.' Head taxonomy is static; does not account for superposition (cf. JuICE). No causal interaction mapping between head types across layers.\",\n    \"building_blocks\": [\n      \"AttnLRP-based head attribution methodology\",\n      \"In-context vs parametric head taxonomy with layer distribution\",\n      \"Function vector extraction and steering\",\n      \"94% AUC linear probe for knowledge source tracing\",\n      \"Contrastive open-book/closed-book experimental design\"\n    ],\n    \"relevance_to_seed\": \"Provides the head-level atlas that circuit tracing should connect into end-to-end pathways; the retrieval head identification and linear probe are directly usable as starting nodes for circuit discovery. The acknowledged gap (no MLP interaction analysis) is exactly what our project addresses.\"\n  },\n  {\n    \"title\": \"Summing Up the Facts: Additive Mechanisms Behind Factual Recall in LLMs\",\n    \"venue\": \"NeurIPS 2024 (Workshop → expanded)\",\n    \"problem_identification\": \"Prior work (ROME, causal tracing) identified individual components involved in factual recall but treated them in isolation. The authors discovered that no single mechanism suffices—factual recall emerges from constructive interference of multiple independent, qualitatively different mechanisms summing in the residual stream.\",\n    \"key_insight\": \"Factual recall operates via an 'additive motif': four distinct mechanism types (subject heads ~18%, relation heads ~24%, mixed heads ~27%, MLPs ~30%) each contribute insufficient individual signal, but constructively interfere on the correct answer because it is the only token boosted by all four simultaneously.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Extends Direct Logit Attribution (DLA) to decompose attention head outputs by source token position, enabling separation of mixed heads into subject-attending and relation-attending components. Uses edge patching to confirm independence of mechanisms. Counterfactual sets (S-set: vary relation keeping subject; R-set: vary subject keeping relation) characterize each mechanism's contribution profile. Primary analysis on Pythia-2.8B with generalization to GPT-2 XL and GPT-J.\",\n    \"limitations_and_open_questions\": \"Studied only simple factual recall templates on Pythia-2.8B; generalization to complex queries and larger models is unverified. The DLA source-token decomposition relies on LayerNorm linearity approximation. How does this additive motif behave under knowledge conflicts when multiple candidate answers receive partial boosts?\",\n    \"building_blocks\": [\n      \"DLA-by-source-token decomposition method\",\n      \"Additive motif framework for factual recall\",\n      \"Subject/relation/mixed head taxonomy\",\n      \"Counterfactual set methodology (S-set, R-set)\"\n    ],\n    \"relevance_to_seed\": \"Establishes that parametric knowledge assembly is distributed and additive—critical for understanding why single-point interventions fail. In RAG conflicts, the additive motif predicts that MLPs and relation heads will continue boosting parametric answers even after retrieval heads inject context, explaining the flip phenomenon.\"\n  },\n  {\n    \"title\": \"How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training\",\n    \"venue\": \"ACL 2025 Findings\",\n    \"problem_identification\": \"Knowledge circuits had only been analyzed at single snapshots; no work traced how these circuits evolve during learning. The authors identified that understanding circuit dynamics during continual pre-training could reveal how new knowledge structurally integrates into existing representations.\",\n    \"key_insight\": \"Knowledge circuit evolution follows a deep-to-shallow formation pattern with a distinct phase shift: an initial 'formation' phase crystallizes circuit topology (decreasing entropy, increasing structural consistency), followed by an 'optimization' phase that refines computations within the stabilized structure, yielding 54% better performance.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Uses EAP-IG (Edge Attribution Patching with Integrated Gradients) to discover knowledge circuits at multiple training checkpoints across GPT-2 Small/Medium, TinyLlama, and Phi-1.5. Tracks circuit evolution via entropy (edge importance concentration), Jaccard similarity (topology stability), and edge activation ratios per layer. Constructs synthetic biographical data to control knowledge novelty, classifying knowledge as relevant (extending existing entities) vs completely new (fictional entities), finding relevant knowledge is consistently acquired more efficiently.\",\n    \"limitations_and_open_questions\": \"Limited to ≤1.3B models due to EAP-IG scalability constraints with GQA. Only standard next-token prediction training; no analysis of instruction tuning or RLHF. Does the deep-to-shallow pattern hold for knowledge acquired via in-context retrieval rather than weight updates?\",\n    \"building_blocks\": [\n      \"EAP-IG circuit discovery at multiple checkpoints\",\n      \"Circuit entropy and Jaccard similarity as evolution metrics\",\n      \"Relevant vs completely-new knowledge classification\",\n      \"Deep-to-shallow circuit formation pattern\"\n    ],\n    \"relevance_to_seed\": \"The deep-to-shallow pattern suggests parametric knowledge circuits are anchored in deep layers—consistent with CoRect's finding that deep FFN layers suppress correct answers. Understanding where parametric circuits crystallize informs where circuit-informed interventions should target suppression of parametric re-assertion.\"\n  },\n  {\n    \"title\": \"Copy Suppression: Comprehensively Understanding an Attention Head\",\n    \"venue\": \"BlackboxNLP 2024 / Patterns (Cell Press) 2025\",\n    \"problem_identification\": \"Multiple prior studies on narrow tasks found 'negative heads' that systematically favored wrong answers, but no unified explanation existed. The authors traced this to a single general-purpose mechanism—copy suppression—operating across the full training distribution in GPT-2 Small's L10H7.\",\n    \"key_insight\": \"Copy suppression is a three-step mechanism: (1) earlier components predict a copied token, (2) the QK circuit detects prediction-context matches (95.72% diagonal dominance), (3) the OV circuit writes negative logits for matched tokens (84.70% self-suppression). This single mechanism explains 76.9% of L10H7's total impact via a copy-suppression-preserving ablation (CSPA).\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Develops CSPA—an ablation retaining only copy suppression functionality (OV projection onto negative unembedding components, QK restriction to top-5% logit-lens predictions)—recovering 76.9% of the head's KL divergence impact. Weight-based analysis of W_U·W_QK and W_U·W_OV matrices confirms the mechanism operates via prediction-matching and self-suppression. Demonstrates the head also performs semantic copy suppression (suppressing morphological variants) and explains 39% of self-repair behavior when upstream components are ablated.\",\n    \"limitations_and_open_questions\": \"Analyzed only GPT-2 Small; generalization to larger models proved inconsistent. The query-side computation for self-repair remains unexplained. How does copy suppression interact with retrieval heads in RAG—does it inadvertently suppress context-derived tokens that were 'copied' from retrieved passages?\",\n    \"building_blocks\": [\n      \"Copy-suppression-preserving ablation (CSPA) methodology\",\n      \"Three-step copy suppression mechanism characterization\",\n      \"QK/OV weight matrix analysis for mechanism verification\",\n      \"Self-repair via passive deactivation of suppression\"\n    ],\n    \"relevance_to_seed\": \"Directly relevant to the hypothesized circuit pathology: copy suppression heads operate via general suppression (not selective), so context-derived tokens injected by retrieval heads may be inadvertently suppressed if they match earlier predictions. This is a candidate mechanism for the flip phenomenon where correct answers appear then get suppressed in deeper layers.\"\n  },\n  {\n    \"title\": \"Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Existing circuit discovery methods (ACDC, EAP) are either prohibitively slow (hours per circuit) or rely on linear approximations that overestimate edge importance and require non-zero gradients, limiting applicable metrics. No method efficiently produced circuits at attention-head-at-specific-position granularity.\",\n    \"key_ins\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:48:03.974Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:48:03.974Z",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-30T06:48:03.987Z_

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

## Paper analyses (23 papers)

[
  {
    "title": "Knowledge Circuits in Pretrained Transformers",
    "venue": "NeurIPS 2024",
    "problem_identification": "Prior work treated knowledge-storing components (MLPs, attention heads) as isolated units ('Restorative Theory'). No work had traced how these components collaborate as circuits for factual recall, despite circuit analysis succeeding on algorithmic tasks.",
    "key_insight": "Factual recall operates through structured subgraphs with three functionally specialized head types — mover heads (extract subject attributes), relation heads (extract relation attributes), and mixture heads (combine information) — whose interactions explain hallucinations, knowledge editing failures, and ICL.",
    "innovation_type": "cross_domain",
    "method_summary": "Applies ACDC and EAP-IG circuit discovery to factual recall on GPT-2 and TinyLLaMA. Edges are scored via zero ablation with MatchNLL loss and pruned in reverse topological order (5-8x faster than forward). Resulting circuits use <10% of edges but retain ~70% Hit@10 performance. Component roles are analyzed via unembedding projection and attention pattern visualization.",
    "limitations_and_open_questions": "Reviewers noted the methodology is 'a direct application of standard causal mediation analysis' with no concrete downstream application. Limited to GPT-2/TinyLLaMA scale; threshold-sensitive; traversal order affects discovered circuits. Head-type definitions (mover/relation/mixture) lack rigorous statistical justification.",
    "building_blocks": [
      "EAP-IG for efficient edge attribution",
      "Reverse topological pruning order",
      "Mover/relation/mixture head taxonomy",
      "Unembedding projection for component analysis"
    ],
    "relevance_to_seed": "Provides the foundational circuit discovery methodology we must adapt for RAG — but their circuits cover only parametric factual recall, not the retrieval-context integration pathway where parametric and contextual signals compete."
  },
  {
    "title": "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Circuit discovery faced a scalability-interpretability tradeoff: coarse-grained circuits (head/MLP nodes) are polysemantic and hard to interpret, while fine-grained approaches require pre-existing mechanistic hypotheses. Neither paradigm could scalably discover unexpected mechanisms.",
    "key_insight": "SAE features resolve polysemanticity by providing monosemantic circuit nodes — enabling circuits that are simultaneously interpretable (each node represents one concept) and discoverable (via standard causal methods on the SAE-decomposed computation graph).",
    "innovation_type": "new_formulation",
    "method_summary": "Decomposes every activation via trained SAEs into sparse monosemantic features, making each feature (plus error terms) a node in the computation graph. Uses attribution patching with integrated gradients (N=10 interpolation points) to discover causal edges. The SHIFT method enables debiasing by human-inspecting circuit features and zero-ablating spurious ones — improving worst-group accuracy from 24% to 89% without disambiguating data. An unsupervised pipeline clusters model behaviors via gradient-space clustering and extracts circuits for thousands of behaviors automatically.",
    "limitations_and_open_questions": "Depends entirely on SAE quality; error terms remain uninterpretable. SHIFT requires human annotation (scalability bottleneck). Supervised evaluation limited to simple grammatical tasks. How well do SAE-based circuits capture the superposition phenomena identified by JuICE?",
    "building_blocks": [
      "SAE features as circuit nodes",
      "SHIFT editing via feature ablation",
      "Gradient-based behavior clustering",
      "Integrated gradients for attribution patching"
    ],
    "relevance_to_seed": "Offers a strictly more interpretable circuit formulation than head-level analysis — critical for disentangling the superposition JuICE identified where heads carry both memory and context signals. SAE feature-level circuits could separate these into distinct monosemantic pathways."
  },
  {
    "title": "CoRect: Context-Aware Logit Contrast for Hidden State Rectification to Resolve Knowledge Conflicts",
    "venue": "arXiv 2026",
    "problem_identification": "Using Logit Lens on 500 NQ conflict cases, discovered the 'flip phenomenon': in 56% of failures (282/500), the correct context-derived answer appears in intermediate layers but gets suppressed by deeper FFN layers before output — split into 'middle flip' (154 cases) and 'last-layer flip' (128 cases).",
    "key_insight": "Knowledge conflicts are predominantly a suppression problem, not a comprehension problem — the model internally 'knows' the correct answer from context in over half of failure cases, but parametric FFN memories actively overwrite it.",
    "innovation_type": "new_technique",
    "method_summary": "Two-stage training-free inference-time method. Stage 1: contrastive forward passes (context vs. null) compute contextual mutual information scores to identify trustworthy target tokens without ground-truth labels, filtered by attention-based faithfulness verification. Stage 2: identifies suppressive FFN layers (those with negative projection onto target's unembedding vector) and applies additive rectification patches that geometrically guarantee positive logit shifts — a 'disinhibition' paradigm that removes blockages rather than forceful steering.",
    "limitations_and_open_questions": "44% of failures don't exhibit the flip phenomenon — what other mechanisms cause them? No comparison with SpARE or ContextFocus. Last-layer flip vs. middle flip may involve different mechanisms but are treated uniformly. No circuit-level causal explanation for WHY specific FFN layers suppress — exactly the gap our project targets.",
    "building_blocks": [
      "Flip phenomenon quantification methodology",
      "Contrastive null-pass token selection",
      "Geometric suppressive layer identification via unembedding projection",
      "Disinhibition-based rectification"
    ],
    "relevance_to_seed": "The flip phenomenon is the most mechanistically informative empirical finding for our project — it's the observable consequence of the promote-suppress-iterate pathology we hypothesize. CoRect's intervention is effective but heuristic; our circuit analysis should explain which specific neurons/features cause suppression and enable more targeted multi-point intervention."
  },
  {
    "title": "On Mechanistic Circuits for Extractive Question-Answering",
    "venue": "COLM 2025",
    "problem_identification": "Mechanistic circuit analysis had been confined to toy/synthetic tasks. No one had extracted circuits for context-augmented extractive QA — the real-world setting where models must decide between context extraction and parametric recall.",
    "key_insight": "Context-faithfulness and memory-faithfulness activate qualitatively different neural pathways with minimal overlap — context circuits are compact (4-5 attention layers, minimal MLP) while memory circuits are large and distributed (>15 layers, >30 heads, heavy MLP involvement).",
    "innovation_type": "cross_domain",
    "method_summary": "Constructs probe datasets D_copy (token-swapped contexts forcing context extraction) and D_memory (corrupted contexts forcing parametric recall). Applies hierarchical causal mediation analysis with greedy component selection until δ=0.95 threshold. Discovers that a single attention head reliably attends to answer spans, yielding ATTNATTRIB — zero-cost attribution during generation. Steering combines attention upweighting (β=10 at context-circuit heads) and MLP mean-ablation (at memory-circuit MLPs), redirecting 92% of memory-based answers to context.",
    "limitations_and_open_questions": "Restricted to single-hop extractive QA; probe datasets use artificial token-swap perturbations. Circuit interactions when both pathways activate simultaneously are uncharacterized. Reviewers noted path-patching may capture correlations, not strict causation. No analysis of multi-hop reasoning or RAG-scale retrieval.",
    "building_blocks": [
      "D_copy/D_memory probe dataset design",
      "ATTNATTRIB zero-cost attribution",
      "Combined attention upweighting + MLP ablation steering",
      "Hierarchical circuit extraction methodology"
    ],
    "relevance_to_seed": "Most directly relevant prior work — demonstrates circuit-based steering for context vs. memory in QA. However, their clean separation (compact context circuit vs. distributed memory circuit) may not hold under JuICE's superposition finding. Our project must handle the messier case where the same heads carry both signals, requiring SAE-level decomposition rather than head-level circuits."
  },
  {
    "title": "Knowledge Conflicts for LLMs: A Survey",
    "venue": "EMNLP 2024",
    "problem_identification": "No unified framework existed for understanding the landscape of knowledge conflicts in LLMs. Research was fragmented across context-memory, inter-context, and intra-memory conflicts with no systematic organization of causes, behaviors, and solutions.",
    "key_insight": "Knowledge prioritization depends on semantic coherence, logical structure, and persuasiveness of competing sources — not simply on source type (context vs. memory) — and a 40% gap exists between knowledge probe accuracy and generation accuracy, showing models store correct knowledge they cannot reliably express.",
    "innovation_type": "analysis",
    "method_summary": "Systematically catalogs three conflict types (context-memory, inter-context, intra-memory) with their causes, model behaviors, and resolution strategies. Organizes solutions into pre-hoc (fine-tuning, pre-training, discriminators) and post-hoc (decoding, prompting, ensemble) families. Identifies seven open problems including mechanistic explainability, conflict interplay, and multimodality.",
    "limitations_and_open_questions": "All cataloged resolution strategies are behavioral interventions — no mechanistic/circuit-level approaches. The survey explicitly flags 'microscopic examinations of attention heads and neuron activations' as the key open problem. Literature is dominated by artificial conflict scenarios (entity substitution), limiting ecological validity.",
    "building_blocks": [
      "CM/IC/IM conflict taxonomy",
      "Pre-hoc vs. post-hoc solution framework",
      "Catalog of conflict benchmarks (NQ-Swap, ConflictQA, etc.)",
      "Seven open research directions"
    ],
    "relevance_to_seed": "Defines our problem space and explicitly identifies mechanistic understanding as the key open problem (Open Problem #5). The survey's behavioral-level characterizations are precisely what our circuit analysis aims to explain mechanistically — transforming 'what happens' into 'why it happens' at the component level."
  },
  {
    "title": "Do All Autoregressive Transformers Remember Facts the Same Way? A Cross-Architecture Analysis of Recall Mechanisms",
    "venue": "EMNLP 2025",
    "problem_identification": "The widely-assumed universality of MLP-based factual recall (from Meng et al.'s work on GPT) was never validated across architectures. Knowledge editing methods (ROME, MEMIT) and interpretability tools assumed MLP dominance as a universal property of transformers.",
    "key_insight": "Factual recall localization is architecture-specific, not universal: GPT/LLaMA use early MLP layers while Qwen/DeepSeek concentrate recall in early attention layers — and no single architectural factor (hidden size, head count, GQA vs. MHA, vocabulary) explains the divergence.",
    "innovation_type": "analysis",
    "method_summary": "Compares 17 models across 4 families (GPT, LLaMA, Qwen, DeepSeek) using three complementary techniques: restoration effects (causal tracing with Gaussian noise), severing effects (blocking module outputs), and knockout (blocking 5 consecutive layers). Resolves discrepancies between restoration and severing via Gini coefficient analysis of AIE concentration. Introduces semantic similarity evaluation (Sentence-BERT, τ=0.7) to handle lexically different but semantically correct predictions.",
    "limitations_and_open_questions": "Identifies WHERE facts are stored but not HOW recall works mechanistically. Cannot explain WHY architectures differ — all individual factors were ruled out, suggesting complex interactions with training dynamics. Limited to CounterFact dataset (100 sentences/model). Does this architecture-specificity extend to RAG integration circuits?",
    "building_blocks": [
      "Gini coefficient for AIE concentration analysis",
      "Semantic similarity evaluation for factual recall",
      "Cross-architecture comparison methodology",
      "Architecture-specificity of recall mechanisms"
    ],
    "relevance_to_seed": "Critical validation constraint: our circuit discoveries on Llama-3.1-8B (MLP-dominated recall) may not transfer to Gemma-2-9B validation. We must verify that the RAG integration circuit — not just the parametric recall circuit — shows consistent structure across architectures, or explicitly characterize the differences."
  },
  {
    "title": "Retrieval Head Mechanistically Explains Long-Context Factuality",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "No mechanistic explanation existed for how LLMs retrieve facts from arbitrary positions in long contexts. Identified via observation that models pass NIAH tests but no one traced which components are responsible.",
    "key_insight": "Fewer than 5% of attention heads ('retrieval heads') perform nearly all factual retrieval via a copy-paste algorithm; they are intrinsic to short-context pretraining and persist unchanged through context extension.",
    "innovation_type": "analysis",
    "method_summary": "Defined a retrieval score as token-level recall of copy-paste behavior during autoregressive decoding, thresholded across ~600 NIAH instances per model. Validated causally: masking retrieval heads drops accuracy to 63.6% vs 94.7% for random-head masking. Extended induction-head analysis from Olsson et al. to long-context retrieval across 4 model families and 6 scales.",
    "limitations_and_open_questions": "Detection relies on synthetic copy-paste tasks that may not capture paraphrastic retrieval; no analysis of downstream circuit pathways beyond retrieval heads (no FFN interaction, no copy suppression tracing). Only decoder-only full-attention architectures tested.",
    "building_blocks": [
      "Retrieval score metric",
      "NIAH-based head classification protocol",
      "Causal head ablation methodology",
      "Per-model retrieval head indices",
      "Retrieval head detection algorithm"
    ],
    "relevance_to_seed": "Provides the entry point of the RAG circuit — the sparse retrieval heads that inject context signal — but stops at component identification without tracing how this signal propagates through FFNs and copy suppression to the output."
  },
  {
    "title": "Scaling and Evaluating Sparse Autoencoders",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "ReLU-based SAEs suffer from activation shrinkage (L1 penalty biases activations toward zero) and massive dead latents (up to 90% inactive), with no rigorous scaling laws or evaluation suite. Identified by measuring systematic underestimation in ReLU activations with frozen masks.",
    "key_insight": "Sparsity control and reconstruction quality are separable: using TopK activation (keep k largest, zero rest) enforces sparsity architecturally rather than via loss penalty, eliminating shrinkage entirely.",
    "innovation_type": "combination",
    "method_summary": "Replaced min(reconstruction + λ·L1) with min(reconstruction) subject to exactly-k-sparse activations via TopK. Introduced AuxK auxiliary loss using top-k_aux dead latents to model residual error, reducing dead latents to 7% at 16M scale. Established clean power-law scaling L(n,k) with tokens-to-convergence scaling as n^0.6.",
    "limitations_and_open_questions": "Evaluation metrics are proxies (no ground-truth features exist); TopK forces uniform sparsity per input (real feature counts may vary); no causal/circuit-level validation of learned features; computational cost at 16M scale is substantial.",
    "building_blocks": [
      "TopK SAE architecture",
      "AuxK dead-latent revival loss",
      "Scaling laws L(n,k)",
      "Evaluation suite: downstream loss, probe loss (61 tasks), N2G explainability, ablation sparsity"
    ],
    "relevance_to_seed": "Provides the SAE methodology backbone for SpARE-style interventions — TopK SAEs yield cleaner, sparser features for identifying retrieval-faithfulness latents in residual streams at circuit-critical layers."
  },
  {
    "title": "ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Prior RAG hallucination detectors treated external context usage and parametric knowledge as independent signals. Using OV matrix eigenvalue analysis and FFN vocabulary-space projection, authors showed these pathways confound each other — analyzing one without controlling the other yields inaccurate detection.",
    "key_insight": "RAG hallucinations arise from an imbalance between Knowledge FFNs (later-layer FFNs injecting parametric knowledge) and Copying Heads (positive OV-eigenvalue heads copying from context) — the interaction, not either component alone, drives hallucination.",
    "innovation_type": "new_formulation",
    "method_summary": "Defined External Context Score (cosine similarity of attended-token hidden states to generated token via Copying Heads) and Parametric Knowledge Score (JSD between vocab distributions before/after FFN layers). Cast detection as multivariate regression treating each as confounder. AARF intervention amplifies copying head attention (α>1) and dampens FFN contributions (β<1) when hallucination score exceeds threshold τ.",
    "limitations_and_open_questions": "ECS/PKS are intuitive proxies without provable faithfulness; heavy hyperparameter burden (α, β, τ, top-K, chunk size) varies per model/dataset with no automated selection. Reviewer criticism: missing strong baselines (AlignScore at 84-86% F1) and noisy causal results.",
    "building_blocks": [
      "ECS/PKS scoring framework",
      "OV-eigenvalue copying head identification",
      "JSD-based FFN knowledge attribution",
      "AARF intervention mechanism",
      "RAGTruth and Dolly-AC benchmarks"
    ],
    "relevance_to_seed": "Identifies the two key RAG component types (Knowledge FFNs, Copying Heads) and quantifies their aggregate interaction, but does not trace the circuit connecting them — exactly the gap our proposed work fills."
  },
  {
    "title": "Position-aware Automatic Circuit Discovery",
    "venue": "ACL 2025",
    "problem_identification": "Existing circuit discovery methods (EAP, ACDC) aggregate edge importance across all token positions, causing score cancellation (opposite-sign contributions net to zero) and overestimation (many small cross-position effects outrank important single-position edges). Demonstrated empirically on GPT-2-small.",
    "key_insight": "Attention edges are inherently cross-positional (query at position t, key/value at position t'); collapsing positions before scoring destroys this structure and hides functionally critical edges.",
    "innovation_type": "new_technique",
    "method_summary": "Extended Edge Attribution Patching to position-specific gradient computation by recasting the computation graph from (component, layer) to (component, layer, position) nodes, tripling attention edge granularity. Introduced 'dataset schemas' — abstract semantic span labels (Subject, Verb, IO) that align variable-length examples into a common positional frame. Automated schema generation via LLM-generated saliency-guided annotation.",
    "limitations_and_open_questions": "Schemas require fixed span ordering across examples with no general design principles; tested on only 2 models and 3 tasks; no comparison to ACDC; schema transferability across models is poor.",
    "building_blocks": [
      "PEAP method and code (github.com/technion-cs-nlp/PEAP)",
      "Dataset schema formalism",
      "LLM+saliency automated schema pipeline",
      "Position-aware edge attribution patching"
    ],
    "relevance_to_seed": "Directly applicable to RAG circuit discovery where context tokens and query tokens play structurally different roles — PEAP's schema formalism can define 'Query', 'Passage', 'Answer' spans to discover position-sensitive retrieval circuits."
  },
  {
    "title": "Open Problems in Mechanistic Interpretability",
    "venue": "TMLR 2025",
    "problem_identification": "The MI field lacked a unified research agenda. 29 researchers across 18 organizations synthesized scattered knowledge via collaborative expert elicitation, identifying that current work overwhelmingly focuses on activations (what neurons represent) while neglecting mechanisms (how weights compute representations).",
    "key_insight": "Mechanistic interpretability decomposes into a pipeline — decomposition → description → validation — and each stage has distinct failure modes (polysemanticity, interpretability illusions, lack of causal grounding) that current methods systematically conflate.",
    "innovation_type": "analysis",
    "method_summary": "Taxonomized open problems across three axes: methods/foundations (8 SDL limitations, circuit completeness, feature universality), applications (monitoring unsafe cognition, predicting novel-situation behavior), and socio-technical challenges (automation, adversarial robustness of explanations). Critically evaluated SAEs, probing, circuit discovery, and attribution methods, proposing intrinsic interpretability as underexplored.",
    "limitations_and_open_questions": "SDL features are distribution-dependent and may not map to human concepts; validation methods are gameable; no formal theoretical foundation connects interpretability to generalization; circuit completeness may be intractable for distributed representations.",
    "building_blocks": [
      "Decompose-describe-validate pipeline framework",
      "Taxonomy of SAE limitations",
      "Criteria for circuit completeness",
      "Feature universality evaluation criteria"
    ],
    "relevance_to_seed": "Frames the circuit completeness challenge our work faces — distributed representations across heads/layers make complete circuit identification hard — and warns that SDL latents are dataset-dependent, relevant for SAE-based feature extraction in RAG circuits."
  },
  {
    "title": "IRCAN: Mitigating Knowledge Conflicts in LLM Generation via Identifying and Reweighting Context-Aware Neurons",
    "venue": "NeurIPS 2024",
    "problem_identification": "LLMs' parametric knowledge conflicts with contextual knowledge at inference time, causing hallucinations. Prior work used prompt engineering or decoding strategies but never directly intervened at the neuron level to prioritize context processing.",
    "key_insight": "Specific FFN neurons are disproportionately responsible for context processing vs. parametric recall; these can be identified via integrated gradients measuring each neuron's marginal contribution to context processing, then amplified via simple weight scaling without retraining.",
    "innovation_type": "new_technique",
    "method_summary": "Defined attribution score Attr(n) = (v_{c,q} - v_q) · ∫gradient measuring each neuron's marginal context contribution. Selected top neurons by co-occurrence frequency across examples as a shared reusable set. Applied multiplicative weight scaling (W' = β·W) at inference, combinable with Context-Aware Decoding for further gains. Achieved 129-136% accuracy improvement on MemoTrap.",
    "limitations_and_open_questions": "Only evaluated on 3 synthetic benchmarks; untested on long-context/RAG settings; no mechanism to distinguish reliable vs. unreliable context; context-aware neurons assumed transferable across instances. Reviewer criticism: no comparison with probing/SAE-based steering; safety concern that forcing context fidelity could amplify jailbreaks.",
    "building_blocks": [
      "Integrated-gradient neuron attribution pipeline",
      "Intersection-based neuron selection heuristic",
      "Multiplicative reweighting intervention template",
      "MemoTrap/COSE_KRE/ECARE_KRE benchmarks"
    ],
    "relevance_to_seed": "The primary baseline for statistical neuron selection in knowledge conflicts — IRCAN's gradient-attribution + frequency heuristic approach is the natural comparison point for circuit-based targeting that claims more principled and precise intervention."
  },
  {
    "title": "Taming Knowledge Conflicts in Language Models (JuICE)",
    "venue": "ICML 2025 (Spotlight)",
    "problem_identification": "Prior work assumed attention heads are either 'memory heads' or 'context heads' with fixed roles. The authors showed empirically that top-ranked memory heads flip behavior across conflict types (e.g., Head (9,3) in Gemma shifts from +0.13 to -0.17 context probability), and combining individually effective heads causes counteracting degradation (top-10 heads perform worse than top-3).",
    "key_insight": "Influential attention heads operate in superposition—simultaneously carrying both parametric and contextual signals—making single-pass interventions unreliable because modified activations cascade through the residual stream and alter downstream head roles.",
    "innovation_type": "new_formulation",
    "method_summary": "JuICE identifies reliable heads by filtering for consistency across multiple conflict types (substitution, coherent counterfactual), retaining only heads with non-negative scores under all conditions. At inference, a dual-run approach caches unperturbed first-run head activations, then injects them as steering signals during a second forward pass, avoiding the cascade effects that degrade single-pass interventions. Theoretical analysis on a two-layer transformer proves superposition emerges naturally from gradient descent and that dual-run succeeds where single-pass deletion fails.",
    "limitations_and_open_questions": "Doubles inference cost via two forward passes; only handles binary parametric-vs-contextual conflicts, not partial relevance. Does not trace the full circuit—operates at the head level without analyzing FFN interactions or information flow pathways.",
    "building_blocks": [
      "ParaConflict benchmark (6 datasets, 3 conflict types)",
      "Dual-run activation caching intervention",
      "Cross-conflict-type consistency filtering for head selection",
      "Theoretical framework proving superposition emergence"
    ],
    "relevance_to_seed": "Directly validates that clean head-type separation is impossible (superposition), motivating full circuit tracing; the dual-run technique could serve as one intervention point in a multi-point circuit-informed strategy."
  },
  {
    "title": "Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering (SpARE)",
    "venue": "NAACL 2025 (Oral)",
    "problem_identification": "Existing representation engineering methods (ActAdd, TaskVec) use polysemantic dense activation vectors for steering, leading to imprecise interventions. The authors identified that SAE features provide monosemantic decomposition suitable for targeted knowledge selection control, and that knowledge conflict signals are detectable at mid-layers.",
    "key_insight": "Pre-trained SAE features can isolate monosemantic dimensions controlling knowledge source selection, enabling bidirectional steering (add parametric features while removing contextual features, or vice versa) with input-dependent clamping constraints to prevent destructive edits.",
    "innovation_type": "combination",
    "method_summary": "SpARE collects hidden states from conflict instances grouped by behavioral outcome (contextual vs parametric answer), encodes them through pre-trained SAEs, ranks features by mutual information I(Z_i; Y) with answer type, and selects top-k features with directional association via mean comparison. Steering applies simultaneous removal and addition of opposing feature sets with input-dependent clamping (min/max constraints) to the hidden states at mid-layers, decoded back via SAE decoder. Achieves +10% over ActAdd and +15% over contrastive decoding on NQSwap.",
    "limitations_and_open_questions": "Feature selection is purely correlational (mutual information), not causally verified via circuit analysis. Requires pre-trained SAEs (not available for all models). Only tested on binary QA conflicts at 7-9B scale. How do selected SAE features map to specific circuit components?",
    "building_blocks": [
      "SAE-based monosemantic feature identification for knowledge conflicts",
      "Bidirectional activation editing with input-dependent clamping",
      "Mutual information ranking for feature selection",
      "Mid-layer intervention targeting"
    ],
    "relevance_to_seed": "Primary baseline—demonstrates SAE features can steer knowledge selection but selects targets heuristically. Circuit-informed intervention should identify the same (or better) targets via causal analysis, and coordinate multi-point interventions that SpARE's single-layer approach cannot."
  },
  {
    "title": "The Atlas of In-Context Learning: How Attention Heads Shape In-Context Retrieval Augmentation",
    "venue": "NeurIPS 2025",
    "problem_identification": "Despite growing use of retrieval-augmented generation, the internal mechanisms by which LLMs integrate retrieved context vs parametric knowledge remained opaque. No systematic taxonomy existed mapping which attention heads serve retrieval vs parametric roles, nor how to trace knowledge source attribution at inference time.",
    "key_insight": "A contrastive attribution design (open-book with counterfactual contexts vs closed-book) using AttnLRP cleanly separates in-context heads (deeper layers, retrieve from context) from parametric heads (early layers, store relational knowledge), with further decomposition into task heads (middle layers, encode question semantics) and retrieval heads.",
    "innovation_type": "analysis",
    "method_summary": "Uses AttnLRP (attention-aware LRP) to compute per-head relevance scores, then applies a contrastive difference score between open-book (counterfactual context) and closed-book settings to classify heads as in-context or parametric. Within in-context heads, token-level relevance aggregation separates task heads from retrieval heads. Function vectors extracted from each head type demonstrate causal roles: task head FVs achieve 94.75% zero-shot question induction, retrieval head attention amplification yields 93.45% recall. A linear probe over retrieval head logit-lens outputs achieves ≥94% AUC for knowledge source detection.",
    "limitations_and_open_questions": "Explicitly acknowledges no analysis of MLP interactions—'how they interact with MLP modules remains an open question.' Head taxonomy is static; does not account for superposition (cf. JuICE). No causal interaction mapping between head types across layers.",
    "building_blocks": [
      "AttnLRP-based head attribution methodology",
      "In-context vs parametric head taxonomy with layer distribution",
      "Function vector extraction and steering",
      "94% AUC linear probe for knowledge source tracing",
      "Contrastive open-book/closed-book experimental design"
    ],
    "relevance_to_seed": "Provides the head-level atlas that circuit tracing should connect into end-to-end pathways; the retrieval head identification and linear probe are directly usable as starting nodes for circuit discovery. The acknowledged gap (no MLP interaction analysis) is exactly what our project addresses."
  },
  {
    "title": "Summing Up the Facts: Additive Mechanisms Behind Factual Recall in LLMs",
    "venue": "NeurIPS 2024 (Workshop → expanded)",
    "problem_identification": "Prior work (ROME, causal tracing) identified individual components involved in factual recall but treated them in isolation. The authors discovered that no single mechanism suffices—factual recall emerges from constructive interference of multiple independent, qualitatively different mechanisms summing in the residual stream.",
    "key_insight": "Factual recall operates via an 'additive motif': four distinct mechanism types (subject heads ~18%, relation heads ~24%, mixed heads ~27%, MLPs ~30%) each contribute insufficient individual signal, but constructively interfere on the correct answer because it is the only token boosted by all four simultaneously.",
    "innovation_type": "analysis",
    "method_summary": "Extends Direct Logit Attribution (DLA) to decompose attention head outputs by source token position, enabling separation of mixed heads into subject-attending and relation-attending components. Uses edge patching to confirm independence of mechanisms. Counterfactual sets (S-set: vary relation keeping subject; R-set: vary subject keeping relation) characterize each mechanism's contribution profile. Primary analysis on Pythia-2.8B with generalization to GPT-2 XL and GPT-J.",
    "limitations_and_open_questions": "Studied only simple factual recall templates on Pythia-2.8B; generalization to complex queries and larger models is unverified. The DLA source-token decomposition relies on LayerNorm linearity approximation. How does this additive motif behave under knowledge conflicts when multiple candidate answers receive partial boosts?",
    "building_blocks": [
      "DLA-by-source-token decomposition method",
      "Additive motif framework for factual recall",
      "Subject/relation/mixed head taxonomy",
      "Counterfactual set methodology (S-set, R-set)"
    ],
    "relevance_to_seed": "Establishes that parametric knowledge assembly is distributed and additive—critical for understanding why single-point interventions fail. In RAG conflicts, the additive motif predicts that MLPs and relation heads will continue boosting parametric answers even after retrieval heads inject context, explaining the flip phenomenon."
  },
  {
    "title": "How Do LLMs Acquire New Knowledge? A Knowledge Circuits Perspective on Continual Pre-Training",
    "venue": "ACL 2025 Findings",
    "problem_identification": "Knowledge circuits had only been analyzed at single snapshots; no work traced how these circuits evolve during learning. The authors identified that understanding circuit dynamics during continual pre-training could reveal how new knowledge structurally integrates into existing representations.",
    "key_insight": "Knowledge circuit evolution follows a deep-to-shallow formation pattern with a distinct phase shift: an initial 'formation' phase crystallizes circuit topology (decreasing entropy, increasing structural consistency), followed by an 'optimization' phase that refines computations within the stabilized structure, yielding 54% better performance.",
    "innovation_type": "analysis",
    "method_summary": "Uses EAP-IG (Edge Attribution Patching with Integrated Gradients) to discover knowledge circuits at multiple training checkpoints across GPT-2 Small/Medium, TinyLlama, and Phi-1.5. Tracks circuit evolution via entropy (edge importance concentration), Jaccard similarity (topology stability), and edge activation ratios per layer. Constructs synthetic biographical data to control knowledge novelty, classifying knowledge as relevant (extending existing entities) vs completely new (fictional entities), finding relevant knowledge is consistently acquired more efficiently.",
    "limitations_and_open_questions": "Limited to ≤1.3B models due to EAP-IG scalability constraints with GQA. Only standard next-token prediction training; no analysis of instruction tuning or RLHF. Does the deep-to-shallow pattern hold for knowledge acquired via in-context retrieval rather than weight updates?",
    "building_blocks": [
      "EAP-IG circuit discovery at multiple checkpoints",
      "Circuit entropy and Jaccard similarity as evolution metrics",
      "Relevant vs completely-new knowledge classification",
      "Deep-to-shallow circuit formation pattern"
    ],
    "relevance_to_seed": "The deep-to-shallow pattern suggests parametric knowledge circuits are anchored in deep layers—consistent with CoRect's finding that deep FFN layers suppress correct answers. Understanding where parametric circuits crystallize informs where circuit-informed interventions should target suppression of parametric re-assertion."
  },
  {
    "title": "Copy Suppression: Comprehensively Understanding an Attention Head",
    "venue": "BlackboxNLP 2024 / Patterns (Cell Press) 2025",
    "problem_identification": "Multiple prior studies on narrow tasks found 'negative heads' that systematically favored wrong answers, but no unified explanation existed. The authors traced this to a single general-purpose mechanism—copy suppression—operating across the full training distribution in GPT-2 Small's L10H7.",
    "key_insight": "Copy suppression is a three-step mechanism: (1) earlier components predict a copied token, (2) the QK circuit detects prediction-context matches (95.72% diagonal dominance), (3) the OV circuit writes negative logits for matched tokens (84.70% self-suppression). This single mechanism explains 76.9% of L10H7's total impact via a copy-suppression-preserving ablation (CSPA).",
    "innovation_type": "analysis",
    "method_summary": "Develops CSPA—an ablation retaining only copy suppression functionality (OV projection onto negative unembedding components, QK restriction to top-5% logit-lens predictions)—recovering 76.9% of the head's KL divergence impact. Weight-based analysis of W_U·W_QK and W_U·W_OV matrices confirms the mechanism operates via prediction-matching and self-suppression. Demonstrates the head also performs semantic copy suppression (suppressing morphological variants) and explains 39% of self-repair behavior when upstream components are ablated.",
    "limitations_and_open_questions": "Analyzed only GPT-2 Small; generalization to larger models proved inconsistent. The query-side computation for self-repair remains unexplained. How does copy suppression interact with retrieval heads in RAG—does it inadvertently suppress context-derived tokens that were 'copied' from retrieved passages?",
    "building_blocks": [
      "Copy-suppression-preserving ablation (CSPA) methodology",
      "Three-step copy suppression mechanism characterization",
      "QK/OV weight matrix analysis for mechanism verification",
      "Self-repair via passive deactivation of suppression"
    ],
    "relevance_to_seed": "Directly relevant to the hypothesized circuit pathology: copy suppression heads operate via general suppression (not selective), so context-derived tokens injected by retrieval heads may be inadvertently suppressed if they match earlier predictions. This is a candidate mechanism for the flip phenomenon where correct answers appear then get suppressed in deeper layers."
  },
  {
    "title": "Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition (CD-T)",
    "venue": "ICLR 2025",
    "problem_identification": "Existing circuit discovery methods (ACDC, EAP) are either prohibitively slow (hours per circuit) or rely on linear approximations that overestimate edge importance and require non-zero gradients, limiting applicable metrics. No method efficiently produced circuits at attention-head-at-specific-position granularity.",
    "key_ins
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
  "promptId": "0c4d8276-2217-46bf-9145-709739add176",
  "type": "user",
  "uuid": "7b251330-9612-4d3c-9d9d-53724b7e1257",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:48:03.985Z_

```json
{
  "parentUuid": "7b251330-9612-4d3c-9d9d-53724b7e1257",
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
  "uuid": "b8d72ac5-a806-4f63-910c-8468e4fb6da9",
  "timestamp": "2026-05-30T06:48:03.985Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:48:03.985Z_

```json
{
  "parentUuid": "b8d72ac5-a806-4f63-910c-8468e4fb6da9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "35c998a0-c4b9-41c6-be97-fc471a446237",
  "timestamp": "2026-05-30T06:48:03.985Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
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
  "leafUuid": "35c998a0-c4b9-41c6-be97-fc471a446237",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Design causal RAG integration circuit for knowledge conflict resolution",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:48:24.509Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 23 paper analyses into a strategic "Field Guide" for generating novel research ideas in the area of mechanistic interpretability for RAG knowledge conflicts. Let me carefully analyze all the papers and produce a comprehensive, evidence-based JSON output.

Let me organize my thinking:

**Innovation Patterns:**
1. Cross-domain application of existing methods to new settings (Knowledge Circuits applied circuit discovery from algorithmic tasks to factual recall; COLM 2025 paper applied circuit analysis to extractive QA)
2. Resolving assumed dichotomies (JuICE showed heads aren't cleanly memory vs context; additive motif showed no single mechanism suffices)


3. The identify-then-intervene workflow appears across multiple papers—ReDeEP, IRCAN, and SpARE all follow this pattern of pinpointing components before testing their causal role
4. Contrastive setups drive discovery, whether comparing open-book versus closed-book scenarios in Atlas or context versus null conditions in CoRect
5. Reframing problems through new lenses—like using SAE nodes as the unit of analysis in Sparse Feature Circuits or JuICE's superposition framing—opens up mechanistic insights

**Reviewer Preferences:**
- Causal validation, not just correlational analysis
- Downstream applications ("so what?" test)
- Cross-model/architecture validation
- Strong baselines
- Quantitative metrics for mechanistic claims

**Field Gaps:**
- End-to-end circuit from retrieval heads through FFNs to output

I'm seeing several untested combinations that could work: combining CD-T with PEAP to discover position-aware circuits in RAG, using SAE features as circuit nodes while analyzing copy suppression, layering the additive motif framework onto RAG conflict analysis, and using JuICE's dual-run approach with circuit-informed target selection. The core building blocks are there—CD-T for fast discovery, PEAP for position-aware edges, SAE features as nodes, CSPA for suppression analysis, AttnLRP for attribution, and contrastive null-pass designs. Now I'm structuring the full JSON response with careful, evidence-based claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35c998a0-c4b9-41c6-be97-fc471a446237",
  "isSidechain": false,
  "requestId": "req_011CbYJhRZ5KzwAcaTzXDm6h",
  "type": "assistant",
  "uuid": "ea04281f-851e-48ef-b53e-f7eabf37bc84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vKxPoK1jdusUtRM77NuLV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12650,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7929,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12650
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

_source line 9 · 2026-05-30T06:51:18.676Z_

I'll carefully analyze all 23 papers to synthesize a comprehensive field guide. Let me first read through any truncated paper analyses to ensure completeness.

Given the depth of the paper analyses provided, let me synthesize this into the strategic field guide.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Cross-domain method transfer to understudied settings",
      "description": "Taking a well-validated methodology from one domain (e.g., circuit discovery on algorithmic tasks) and rigorously applying it to a harder, more practically relevant domain (e.g., factual recall, RAG). The innovation is not the method itself but the adaptation decisions, new findings in the target domain, and the demonstration that prior assumptions break down.",
      "examples": [
        "Knowledge Circuits (NeurIPS 2024) — applied ACDC/EAP-IG from algorithmic tasks to factual recall, discovering mover/relation/mixture head taxonomy",
        "On Mechanistic Circuits for Extractive QA (COLM 2025) — transferred circuit analysis to context-augmented QA, discovering context circuits are compact while memory circuits are distributed",
        "How Do LLMs Acquire New Knowledge (ACL 2025) — applied EAP-IG circuit discovery across training checkpoints, discovering deep-to-shallow formation pattern"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Dissolving false dichotomies with finer-grained analysis",
      "description": "Challenging a widely-held binary assumption (memory vs context heads, MLP vs attention storage, component isolation vs interaction) by introducing a more nuanced analysis framework that reveals the binary was an artifact of coarse measurement. These papers tend to get spotlight/oral status because they force the field to update its mental models.",
      "examples": [
        "JuICE (ICML 2025 Spotlight) — dissolved memory-head vs context-head dichotomy by showing superposition in attention heads",
        "Summing Up the Facts (NeurIPS 2024) — dissolved the 'one mechanism suffices' assumption, showing factual recall requires additive interference of 4+ independent mechanisms",
        "Sparse Feature Circuits (ICLR 2025 Oral) — dissolved the scalability-interpretability tradeoff by using SAE features as monosemantic circuit nodes",
        "Do All Transformers Remember Facts the Same Way (EMNLP 2025) — dissolved the assumed universality of MLP-based recall across architectures"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Identify-then-intervene pipeline with mechanistic grounding",
      "description": "A two-phase structure: Phase 1 discovers specific components/features/circuits using interpretability tools, Phase 2 designs an inference-time intervention targeting those components. Papers that stop at Phase 1 ('pure interpretability') face 'so what?' criticism; papers that skip Phase 1 and intervene heuristically face 'why those targets?' criticism. The strongest papers do both and show Phase 1 enables better Phase 2.",
      "examples": [
        "ReDeEP (ICLR 2025 Spotlight) — identified Knowledge FFNs + Copying Heads, then designed AARF intervention",
        "IRCAN (NeurIPS 2024) — identified context-aware neurons via integrated gradients, then applied multiplicative reweighting",
        "SpARE (NAACL 2025 Oral) — identified knowledge-selection SAE features via MI ranking, then applied bidirectional clamped steering",
        "CoRect (arXiv 2026) — identified suppressive FFN layers via unembedding projection, then applied additive rectification patches"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Contrastive experimental design for causal attribution",
      "description": "Constructing matched pairs of inputs that differ in exactly one dimension (context present vs absent, factual vs counterfactual context, conflict vs no-conflict) to isolate specific mechanisms. This design enables clean causal claims and is the methodological backbone of nearly every accepted paper in this space.",
      "examples": [
        "Atlas (NeurIPS 2025) — open-book with counterfactual context vs closed-book contrastive design",
        "CoRect (arXiv 2026) — context vs null contrastive forward passes for token selection",
        "COLM 2025 QA Circuits — D_copy (token-swapped forcing context) vs D_memory (corrupted forcing parametric) probe datasets",
        "Retrieval Head (ICLR 2025 Oral) — NIAH-based copy-paste detection with head ablation"
      ],
      "success_rate": "high"
    },
    {
      "pattern": "Scaling interpretability tools to practical granularity",
      "description": "Developing faster or more granular versions of existing interpretability methods that unlock analysis at previously intractable scales or resolutions. The innovation is engineering + insight about what information is lost at coarser granularity.",
      "examples": [
        "CD-T (ICLR 2025) — reduced circuit discovery from hours to seconds with 97% ROC AUC",
        "PEAP (ACL 2025) — extended EAP from position-agnostic to position-aware granularity, revealing hidden edges",
        "TopK SAEs (ICLR 2025 Oral) — architectural sparsity control enabling 16M-feature SAEs with clean scaling laws"
      ],
      "success_rate": "medium"
    },
    {
      "pattern": "Empirical phenomenon discovery as theoretical anchor",
      "description": "Discovering a surprising, quantifiable empirical phenomenon that serves as both a validation target and a motivation for mechanistic investigation. The phenomenon must be surprising enough to demand explanation and specific enough to constrain theories.",
      "examples": [
        "CoRect's flip phenomenon — 56% of conflict failures show correct answer appearing then being suppressed",
        "JuICE's head superposition — individual heads flip behavior across conflict types",
        "Copy Suppression (BlackboxNLP 2024) — single head explains 76.9% of total impact via three-step suppression mechanism"
      ],
      "success_rate": "high"
    }
  ],

  "reviewer_preferences": [
    "Causal validation is non-negotiable: Every accepted paper includes ablation, patching, or intervention experiments that go beyond correlational/attributional analysis. Knowledge Circuits (NeurIPS 2024) was criticized precisely for being 'a direct application of standard causal mediation analysis' without downstream application — the method was fine, but the 'so what?' was missing.",
    "Cross-model generalization is expected at top venues: Retrieval Head tested across 4 model families and 6 scales; Do All Transformers Remember Facts compared 17 models across 4 families. Papers limited to a single model (Copy Suppression on GPT-2 Small only) face generalization concerns. For AAAI, Llama + Gemma validation is the minimum viable coverage.",
    "Strong baselines matter more than absolute numbers: ReDeEP was criticized for missing AlignScore (84-86% F1) as a baseline; IRCAN was criticized for no comparison with probing/SAE-based steering. Reviewers actively check whether the strongest available baseline is included.",
    "Quantifiable mechanistic claims are rewarded over qualitative narratives: Copy Suppression's 76.9% CSPA recovery, Retrieval Head's <5% of heads carrying retrieval signal, CoRect's 56% flip phenomenon rate — specific numbers that can be independently verified.",
    "Interventions must show practical benefit beyond interpretability: Pure interpretability papers (Atlas acknowledges 'no MLP interaction analysis') are accepted as analytical contributions but receive lower enthusiasm than papers pairing understanding with demonstrable improvement (SpARE's +10% EM, IRCAN's +129% accuracy).",
    "Theoretical grounding elevates empirical work: JuICE's formal proof that superposition emerges from gradient descent on a two-layer transformer contributed to its Spotlight status. Papers that offer even lightweight theoretical justification for why their method works outperform pure empirical papers.",
    "Ecological validity of evaluation matters: The Knowledge Conflicts survey notes that literature is 'dominated by artificial conflict scenarios (entity substitution).' Reviewers increasingly question whether NQ-Swap/CounterFact results transfer to real-world RAG settings."
  ],

  "field_gaps": [
    {
      "gap": "No end-to-end causal circuit traced from retrieval heads through FFN layers and copy suppression to output in RAG, comparing success vs failure cases",
      "evidence": "Retrieval Head (ICLR 2025) stops at retrieval head identification without downstream tracing; Atlas (NeurIPS 2025) explicitly states 'how they interact with MLP modules remains an open question'; ReDeEP identifies Knowledge FFNs and Copying Heads but does not trace the circuit connecting them; COLM 2025 finds context vs memory circuits but does not trace their interaction when both activate simultaneously",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No circuit-level causal explanation for the flip phenomenon (correct answers appearing mid-layer then being suppressed)",
      "evidence": "CoRect (arXiv 2026) documents the flip in 56% of conflict failures and intervenes with geometric rectification, but explicitly has 'no circuit-level causal explanation for WHY specific FFN layers suppress.' The promote-suppress-iterate framework (Yan & Jia, EMNLP 2025) provides a theoretical prediction but no empirical circuit validation in RAG.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "How superposition in attention heads (JuICE) resolves across layers through FFN interactions — the dynamic mechanism, not just the static observation",
      "evidence": "JuICE (ICML 2025) proves superposition exists and shows it causes cascade effects, but remains at the head level without analyzing FFN interactions or information flow pathways. COLM 2025 finds circuit interactions 'when both pathways activate simultaneously are uncharacterized.'",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No multi-point coordinated intervention exists — all current methods intervene at a single level (heads OR FFNs OR SAE features) without coordinating across circuit stages",
      "evidence": "SpARE intervenes at mid-layer SAE features only; CoRect patches FFN layers only; JuICE caches and reinjects head activations only; IRCAN reweights FFN neurons only; ReDeEP's AARF adjusts copying heads and FFNs independently. COLM 2025 combines attention upweighting + MLP ablation but selects targets via hierarchical mediation, not full circuit analysis.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Copy suppression's role in RAG is entirely uncharacterized — whether it inadvertently suppresses context-derived tokens that were 'copied' from retrieved passages",
      "evidence": "Copy Suppression (BlackboxNLP 2024) characterizes the three-step mechanism (predict → match → suppress) in GPT-2 Small but explicitly asks 'How does copy suppression interact with retrieval heads in RAG?' No subsequent work has answered this.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Architecture-specificity of RAG integration circuits is unknown — parametric recall is architecture-specific (Do All Transformers), but nobody has checked whether context integration circuits vary similarly",
      "evidence": "Do All Transformers (EMNLP 2025) shows GPT/LLaMA use early MLP layers while Qwen/DeepSeek use early attention for factual recall, but notes 'Does this architecture-specificity extend to RAG integration circuits?' as an open question.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "SAE-based circuit discovery has not been applied to RAG knowledge conflicts — only to toy grammatical tasks and generic behavior clustering",
      "evidence": "Sparse Feature Circuits (ICLR 2025 Oral) provides the methodology (SAE features as monosemantic circuit nodes + IG attribution), but tested only on simple grammatical tasks. SpARE uses SAE features for steering but without circuit discovery. Open Problems in MI (TMLR 2025) warns that 'SDL latents are dataset-dependent.'",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "The 44% of knowledge conflict failures that do NOT exhibit the flip phenomenon have no mechanistic explanation",
      "evidence": "CoRect documents that 44% of failures don't show the flip pattern but provides no analysis of what alternative failure modes exist. These could involve different circuit pathologies requiring different interventions.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "CD-T + PEAP for position-aware RAG circuit discovery at scale: Use CD-T's efficiency (seconds per circuit) with PEAP's position-aware schema formalism defining 'Query', 'Retrieved Passage', 'Answer Span' positions to discover the full RAG integration circuit with cross-position edge attribution",
      "from_papers": ["CD-T (ICLR 2025)", "PEAP (ACL 2025)", "Knowledge Circuits (NeurIPS 2024)"],
      "why_promising": "CD-T solves the speed bottleneck; PEAP solves the position-collapse problem that would otherwise hide how retrieval heads at passage positions connect to FFN layers processing query tokens. Neither paper has been applied to RAG, and their combination is non-obvious because CD-T uses contextual decomposition while PEAP uses gradient-based attribution — integration requires reconciling the scoring mechanisms."
    },
    {
      "idea_sketch": "SAE feature-level circuit tracing through the copy suppression pathway: Use Sparse Feature Circuits methodology to decompose copy suppression heads (identified via CSPA) into monosemantic features, then trace which features suppress context-derived tokens vs parametric predictions",
      "from_papers": ["Sparse Feature Circuits (ICLR 2025 Oral)", "Copy Suppression (BlackboxNLP 2024)", "TopK SAEs (ICLR 2025 Oral)"],
      "why_promising": "Copy suppression operates via general suppression (not selective), meaning it probably affects both parametric and context-derived tokens. SAE decomposition could reveal whether specific monosemantic features within copy suppression heads differentially target context vs parametric tokens — resolving whether copy suppression is a uniform mechanism or has hidden selectivity. This would directly explain one pathway for the flip phenomenon."
    },
    {
      "idea_sketch": "Additive motif analysis under knowledge conflicts: Apply the Summing Up the Facts framework (DLA-by-source-token decomposition) to RAG conflict cases, decomposing the residual stream into contributions from retrieval heads, subject heads, relation heads, mixed heads, and MLPs to characterize how the constructive interference pattern changes (or breaks) when parametric and contextual answers compete",
      "from_papers": ["Summing Up the Facts (NeurIPS 2024)", "CoRect (arXiv 2026)", "ReDeEP (ICLR 2025)"],
      "why_promising": "The additive motif predicts that in knowledge conflicts, both parametric and context-derived answers receive partial boosts from overlapping mechanism sets, and the winner depends on which accumulates more total signal. This framework could quantitatively predict the flip phenomenon: the context answer leads at mid-layers (retrieval head contribution dominant) but the parametric answer overtakes in deep layers (MLP contributions accumulate). No one has applied this specific analytical lens to RAG."
    },
    {
      "idea_sketch": "Circuit-informed JuICE: Replace JuICE's statistical head selection with circuit-traced targets, then extend the dual-run technique to coordinate interventions at multiple circuit stages (retrieval heads, mid-layer FFNs, copy suppression heads) simultaneously",
      "from_papers": ["JuICE (ICML 2025)", "Knowledge Circuits (NeurIPS 2024)", "COLM 2025 QA Circuits"],
      "why_promising": "JuICE's key limitation is that it operates at head level without analyzing FFN interactions, and its consistency-based filtering is a heuristic proxy for causal importance. Circuit-traced targets would be causally grounded. The dual-run technique handles the superposition problem that defeats single-pass interventions, but currently only targets heads — extending it to FFN neurons at circuit-identified layers addresses the multi-point gap."
    },
    {
      "idea_sketch": "Contrastive circuit comparison between flip and non-flip failure cases: Discover separate circuits for the 56% flip cases and 44% non-flip cases identified by CoRect, then classify failure types at inference to apply targeted interventions per type",
      "from_papers": ["CoRect (arXiv 2026)", "CD-T (ICLR 2025)", "On Mechanistic Circuits for Extractive QA (COLM 2025)"],
      "why_promising": "CoRect treats middle-flip and last-layer-flip uniformly despite acknowledging they may involve different mechanisms. Circuit-contrastive analysis across failure types would reveal whether different pathologies require different intervention strategies — analogous to how medical diagnosis improves treatment by distinguishing disease subtypes."
    },
    {
      "idea_sketch": "Deep-to-shallow circuit formation analysis applied to in-context knowledge integration: Track how RAG integration circuits form across context length (analogous to training checkpoints) to understand whether the model builds retrieval circuits incrementally or all-at-once",
      "from_papers": ["How Do LLMs Acquire New Knowledge (ACL 2025)", "Atlas (NeurIPS 2025)", "Retrieval Head (ICLR 2025)"],
      "why_promising": "The deep-to-shallow formation pattern suggests parametric knowledge anchors in deep layers, predicting that deep FFN suppression of context answers (CoRect's flip) reflects the model's default parametric circuit being phylogenetically older and more entrenched than the retrieval circuit. This developmental perspective could explain why interventions at different layers have different effectiveness."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "CD-T (Contextual Decomposition for Transformers)",
      "what_it_does": "Discovers circuits in seconds (vs hours for ACDC) with 97% ROC AUC by computing exact contributions of component subsets via contextual decomposition, supporting any differentiable or non-differentiable metric",
      "used_by": ["CD-T (ICLR 2025)"],
      "could_be_applied_to": "Primary circuit discovery engine for tracing the full RAG integration circuit at head-level granularity; its speed enables iterative hypothesis testing across hundreds of conflict examples to characterize circuit variability"
    },
    {
      "tool": "PEAP (Position-aware Edge Attribution Patching)",
      "what_it_does": "Extends edge attribution to position-specific granularity using 'dataset schemas' that align variable-length inputs into common semantic frames, tripling attention edge resolution and revealing edges hidden by position-agnostic methods",
      "used_by": ["PEAP (ACL 2025)"],
      "could_be_applied_to": "RAG circuit discovery where 'Query', 'Passage', 'Answer' spans play structurally different roles — critical for distinguishing retrieval head edges (passage→output) from parametric edges (query→MLP→output)"
    },
    {
      "tool": "SAE features as circuit nodes (Sparse Feature Circuits methodology)",
      "what_it_does": "Decomposes activations through trained SAEs into monosemantic features, then uses attribution patching with integrated gradients to discover causal edges between features, resolving polysemanticity at the node level",
      "used_by": ["Sparse Feature Circuits (ICLR 2025 Oral)", "SpARE (NAACL 2025)"],
      "could_be_applied_to": "Disentangling JuICE's superposition — SAE features could separate the memory and context signals that coexist in superposed attention heads into distinct monosemantic pathways, enabling clean intervention without cascade effects"
    },
    {
      "tool": "Copy-Suppression-Preserving Ablation (CSPA)",
      "what_it_does": "Retains only copy suppression functionality of an attention head (OV projection onto negative unembedding components, QK restriction to top-5% logit-lens predictions), enabling precise measurement of how much a head's impact comes from copy suppression vs other functions",
      "used_by": ["Copy Suppression (BlackboxNLP 2024)"],
      "could_be_applied_to": "Quantifying how much of the flip phenomenon is attributable to copy suppression vs parametric FFN re-assertion — by applying CSPA to candidate suppressive heads in RAG conflict cases and measuring whether the flip persists"
    },
    {
      "tool": "Contrastive null-pass methodology",
      "what_it_does": "Runs two forward passes (with context vs without/null context) and computes differences in internal representations to identify which components are specifically engaged by contextual information, with geometric faithfulness verification",
      "used_by": ["CoRect (arXiv 2026)", "Atlas (NeurIPS 2025)"],
      "could_be_applied_to": "Labeling circuit edges as context-dependent vs context-independent during circuit discovery, enabling automatic classification of edges into retrieval pathway vs parametric pathway without manual annotation"
    },
    {
      "tool": "DLA-by-source-token decomposition",
      "what_it_does": "Extends Direct Logit Attribution to decompose attention head outputs by which source token position they attend to, separating contributions from subject tokens, relation tokens, and context tokens within the same head",
      "used_by": ["Summing Up the Facts (NeurIPS 2024)"],
      "could_be_applied_to": "Layer-by-layer tracking of whether the leading answer token shifts from context-derived to parametric across the residual stream — providing the quantitative trajectory that the flip phenomenon describes qualitatively"
    },
    {
      "tool": "AttnLRP (Attention-aware Layer-wise Relevance Propagation)",
      "what_it_does": "Computes per-head relevance scores that respect attention structure, enabling head-level attribution of output tokens to specific input tokens through specific heads, with contrastive scoring between experimental conditions",
      "used_by": ["Atlas (NeurIPS 2025)"],
      "could_be_applied_to": "Initial head classification (in-context vs parametric vs task) to define starting nodes for circuit discovery, avoiding the cold-start problem of not knowing which heads to trace from"
    },
    {
      "tool": "JuICE's dual-run activation caching",
      "what_it_does": "Caches unperturbed activations from a first forward pass, then injects them as steering signals during a second pass, avoiding cascade effects that degrade single-pass interventions due to head superposition",
      "used_by": ["JuICE (ICML 2025)"],
      "could_be_applied_to": "Multi-point circuit-informed intervention — extend beyond head-level caching to cache activations at circuit-identified FFN neurons and copy suppression heads, coordinating intervention across all circuit stages"
    }
  ],

  "common_pitfalls": [
    "Stopping at component identification without tracing interactions: Knowledge Circuits (NeurIPS 2024) was criticized by reviewers as 'a direct application of standard causal mediation analysis' with no downstream application. ReDeEP identifies Knowledge FFNs and Copying Heads but doesn't trace how they interact. The field has matured past 'we found important components' — circuit-level interaction mapping and intervention are now the expected contribution level.",
    "Assuming clean separability of head roles when JuICE proves superposition exists: COLM 2025's finding that context circuits are compact and memory circuits are distributed may be an artifact of their token-swap probe design that artificially eliminates the superposition JuICE identified. Any method that classifies heads as binary (retrieval vs memory) risks building on a false premise.",
    "Using artificial conflict benchmarks (NQ-Swap, entity substitution) as sole evaluation: The Knowledge Conflicts Survey (EMNLP 2024) warns that ecological validity is limited. Reviewers increasingly question transfer to real-world RAG settings. Include at least one realistic conflict benchmark (e.g., temporally outdated knowledge, genuine retrieval errors).",
    "Single-model results without architecture validation: Do All Transformers (EMNLP 2025) showed factual recall localization is architecture-specific — MLP-dominant in LLaMA vs attention-dominant in Qwen. Circuit claims on Llama-3.1-8B alone will face immediate 'does this generalize?' questions. Gemma-2-9B validation is essential.",
    "Over-parameterized interventions that look like curve-fitting: ReDeEP was criticized for 'heavy hyperparameter burden (α, β, τ, top-K, chunk size) varying per model/dataset with no automated selection.' Circuit-informed interventions should have fewer, more principled hyperparameters — ideally with targets determined by the circuit analysis rather than grid search.",
    "Ignoring the 44% of failures outside the flip phenomenon: CoRect documents that 44% of conflict failures don't exhibit the flip. A circuit-based method that only explains/fixes flip cases will leave nearly half the problem unsolved. Must characterize and address multiple failure modes.",
    "Confusing correlation with causation in attribution methods: COLM 2025 reviewers noted 'path-patching may capture correlations, not strict causation.' IRCAN's integrated-gradient attribution and SpARE's mutual-information ranking are correlational. Circuit analysis must use interventional validation (ablation, patching) to establish genuine causal edges.",
    "Treating circuit completeness as achievable: Open Problems in MI (TMLR 2025) warns that circuit completeness may be intractable for distributed representations. Frame contributions as 'sufficient circuits' (enough to explain and intervene on specific phenomena) rather than claiming exhaustive circuit discovery.",
    "Neglecting computational cost analysis: JuICE doubles inference cost via dual forward passes. SpARE requires pre-trained SAEs. Any intervention must report latency overhead — AAAI reviewers care about practical deployability, especially for inference-time methods."
  ],

  "field_trajectory": "The field is converging toward three macro-directions. First, the granularity of mechanistic analysis is descending from component-level (individual heads or MLPs, 2023-2024) through circuit-level (connected subgraphs, 2024-2025) toward feature-level circuits using SAE decomposition (2025-2026) — this is the Sparse Feature Circuits trajectory, and it is accelerating as TopK SAEs make high-quality features available at scale. Second, the field is shifting from pure interpretability toward 'interpretability-grounded intervention,' where mechanistic understanding directly produces better steering, editing, or control methods — this reflects both reviewer demand ('so what?') and practical RAG deployment needs. Papers that combine circuit discovery with demonstrable intervention improvements (COLM 2025's 92% memory→context redirect, SpARE's +10% EM) are consistently the most impactful. Third, there is growing recognition that LLM internals are messier than early work assumed: heads operate in superposition (JuICE), recall mechanisms are architecture-specific (Do All Transformers), factual recall requires additive interference of 4+ mechanisms (Summing Up the Facts), and copy suppression is a general-purpose mechanism with unintended side effects. The next generation of work must embrace this complexity rather than simplify it away. The intersection of these three trends — feature-level circuit discovery that accounts for superposition and delivers practical interventions — defines the frontier for 2026. The specific application of this intersection to RAG knowledge conflicts is the highest-impact target, given that RAG is the dominant LLM deployment paradigm and knowledge conflicts are its primary failure mode, yet no mechanistic circuit analysis has been performed on the full RAG integration pathway.",

  "meta_advice": "If I were advising a PhD student targeting AAAI 2026 in this area, I would give five concrete directives. First, your paper must tell a story that connects discovery to application — the interpretability community has enough 'we found interesting components' papers (Knowledge Circuits got this criticism), and the NLP community has enough 'we improved a metric by heuristic X' papers (IRCAN, CoRect). The winning formula is: mechanistic discovery that enables a principled intervention that outperforms heuristic baselines because the circuit analysis reveals targets that statistical selection misses. Second, use the flip phenomenon (CoRect) as your mechanistic anchor — it's the most empirically informative finding, it has no circuit-level explanation, and it provides a natural validation target where circuit-informed predictions can be checked against observed layer-by-layer behavior. Third, handle superposition seriously: JuICE proved that heads carry mixed signals, so head-level circuit analysis will produce misleading results. You need either SAE feature-level decomposition (Sparse Feature Circuits + TopK SAEs) or JuICE's dual-run technique to work around this — ideally both, with SAE features providing the interpretable nodes and dual-run handling intervention cascades. Fourth, validate on Gemma-2-9B (not just Llama-3.1-8B), because Do All Transformers showed architecture-specificity in parametric recall, and reviewers will demand cross-architecture evidence. If the circuit differs between architectures, that's actually a finding — characterize the difference rather than hiding it. Fifth, position your multi-point intervention against the strongest available baselines (SpARE, CoRect, JuICE, and COLM 2025's ATTNATTRIB + MLP ablation) on the same benchmarks (NQSwap, ConflictQA, ParaConflict), and ablate your intervention to show that circuit-informed target selection outperforms each paper's own target selection heuristic while using the same intervention mechanics. The most convincing experiment is not 'our method beats all baselines' but 'using circuit-derived targets in their own intervention framework improves their results' — this isolates the value of circuit analysis from the value of any particular intervention technique."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea04281f-851e-48ef-b53e-f7eabf37bc84",
  "isSidechain": false,
  "requestId": "req_011CbYJhRZ5KzwAcaTzXDm6h",
  "type": "assistant",
  "uuid": "cc6f2777-3a19-4c86-836b-1e71ad815242",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011vKxPoK1jdusUtRM77NuLV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12650,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7929,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7929,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12650
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
  "leafUuid": "cc6f2777-3a19-4c86-836b-1e71ad815242",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Design causal RAG integration circuit for knowledge conflict resolution",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "cc6f2777-3a19-4c86-836b-1e71ad815242",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Design causal RAG integration circuit for knowledge conflict resolution",
  "sessionId": "13bd2976-51f0-4e17-a33b-807055254d4e"
}
```

---
