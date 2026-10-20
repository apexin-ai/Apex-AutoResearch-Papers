# Idea Brief: Contrastive Graph Learning for Compositional Tool-Chain Jailbreak Detection in LLM Agents


- **Idea ID**: `idea_005`
- **Created**: 2026-05-17
- **Approved**: 2026-05-17
- **Source**: foreign:be-idea-gen-0515-5
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026 — submit under 'LLM Agents' area)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (9 days from today 2026-05-16). Track: LLM Security.

Direction: LLM safety robustness — defense methods against jailbreaking, adversarial prompt attacks, and safety alignment degradation. In-scope: robust safety training that resists adaptive attacks, automated red-teaming frameworks for systematic vulnerability discovery, safety-aware decoding or filtering at inference time, detecting and mitigating safety degradation when models are fine-tuned or distilled, multi-turn attack defense, tool-use and agentic safety. NOT limited to text — agentic tool-call safety and multi-modal attack surfaces welcome.

Contribution type: METHOD ONLY. Must propose a concrete defense algorithm, detection pipeline, or training recipe — not just a new attack or red-teaming dataset. Attack + defense paired contributions OK if defense is the primary contribution.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Safety research is mostly inference-heavy — budget for evaluation across multiple attack suites, not large-scale pretraining.
2. Time: ≤11 days. Build on existing open safety benchmarks and models (Llama-3-Guard, ShieldGemma, Qwen3, DeepSeek-R1 distills). Use established attack libraries (HarmBench, JailbreakBench, StrongREJECT) for evaluation.
3. Eval: Attack Success Rate (ASR) reduction on HarmBench, JailbreakBench, AdvBench; safety score on WildGuard/Aegis; utility preservation on MT-Bench/MMLU (defense must not kill helpfulness).

This is a NEW dedicated track at EMNLP 2026 — high visibility, growing fast, few established defense methods. 2026 research shows reasoning models can jailbreak other models at 97% success; defense lags far behind attack. Look for: inference-time safety filters that adapt to attack patterns, representation-level safety mechanisms (circuit-based), robust alignment under fine-tuning distribution shift, defense against multi-turn and agentic attacks. Avoid: yet another jailbreak attack without defense contribution, prompt-template-only defenses, safety classifiers without adversarial robustness guarantees.

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (765s) — 发现 5 个研究方向
   - Structure-Guided Draft Training for Reasoning Speculative Decoding
   - Retroactive KV Cascade Compression for Iterative Multi-Round RAG
   - Retrospective Boundary KV Distillation After Thinking Phase Completion
   - Difficulty-Bucketed Batch Routing for Throughput-Optimal Reasoning Serving
   - PRM-Score-Gated KV Compression for Efficient Inference-Time Tree Search
3. **Method Synthesis** (239s) — 完成: "Structure-Guided Draft Training for Reasoning Speculative Decoding" [solid] → EMNLP 2026 (ARR submission deadline May 25, 2026 — confirmed open), ICLR 2027 (deadline expected ~October 2026, not yet announced — traditional fall submission window)
3. **Method Synthesis** (347s) — 完成: "Retroactive KV Cascade Compression for Iterative Multi-Round RAG" [top-tier] → EMNLP 2026 (ARR deadline May 25, 2026 — 16 days remaining as of 2026-05-09; requires near-complete draft), ACL 2027 (ARR cycle ~Sep-Oct 2026), NAACL 2027 (ARR cycle ~Oct 2026), MLSys 2027 (deadline TBA, historically ~Oct-Nov of prior year)
3. **Method Synthesis** (252s) — 完成: "Retrospective Boundary KV Distillation After Thinking Phase Completion" [top-tier] → EMNLP 2026 (ARR submission deadline May 25, 2026), AIMLSystems 2026 (full paper deadline June 15, 2026)
3. **Method Synthesis** (338s) — 完成: "Difficulty-Bucketed Batch Routing for Throughput-Optimal Reasoning Serving" [solid] → EMNLP 2026 (Industry or Main Track — ARR deadline May 25, 2026; strong precedent: DAST appeared in EMNLP 2025 Industry Track), ICLR 2027 (deadline expected September–October 2026; research-track framing on throughput-optimal reasoning serving)
3. **Method Synthesis** (283s) — 完成: "PRM-Score-Gated KV Compression for Efficient Inference-Time Tree Search" [solid] → EMNLP 2026 (ARR deadline May 25, 2026 — confirmed open), AAAI 2027 (deadline TBD, historically announced August–September; conference February 2027), ICLR 2027 (deadline TBD, historically announced September–October; no official CFP yet as of May 2026)

## Core Problem

LLM agents can be jailbroken through sequences of individually-benign tool calls that compose into harmful operations — STAC (arXiv 2509.25624) achieves >90% ASR on GPT-4.1 via this — yet existing defenses either operate at the wrong granularity (step-level guardrails like ToolSafe miss cross-step compositional intent; prompt-level detectors like RLM-JB analyze input text, not execution traces), rely on manually-authored rules that cannot generalize to novel compositions (AgentArmor's type system at ICLR 2026, Agent-Sentry's structural classifier with allowlists, ARGUS's provenance-based verification, SMT solvers), target the wrong graph type (G-Guard/GuardNet reason over text entity graphs; BlindGuard/XG-Guard/G-Safeguard model MAS inter-agent communication graphs, not intra-agent tool-call dependencies), or operate at the wrong stage (MindGuard's DDGs detect tool-poisoning pre-execution via attention flows but cannot detect compositional harm that emerges only from post-execution data-flow composition of benign calls). No learned defense reasons over tool-call dependency graphs to detect distributed malicious intent emerging from benign compositions.

## Opportunity / Why Now

STAC (arXiv 2509.25624, Sep 2025; benchmark open-sourced at amazon-science/MultiTurnAgentAttack) provides ready-made evaluation for compositional tool-chain attacks (483 cases, 1352 interactions, 10 failure modes) with an automated generation pipeline that can be repurposed to create additional synthetic attack traces for both pre-training and fine-tuning augmentation. Its best prompt-based defense reduces ASR by only 28.8%. The trace-based defense space has matured rapidly — AgentArmor (ICLR 2026) constructs PDGs with rule-based type systems, Agent-Sentry (Mar 2026) layers structural classifiers with provenance-aware allowlists, ARGUS (May 2026) uses provenance graphs for decision auditing, MindGuard (Jan 2026) uses attention-flow DDGs for pre-execution tool-poisoning detection — but all are rule-based or attention-based and cannot generalize to unseen compositional patterns that emerge post-execution. Meanwhile, graph-based anomaly detection for MAS has advanced (G-Safeguard at ACL 2025, BlindGuard at ACL 2026 with corruption-guided contrastive learning), but none target single-agent tool-call composition. TraceSafe (Apr 2026) explicitly identifies 'structural bottleneck' as the key challenge for trajectory guardrails, motivating graph-structural approaches. Supervised contrastive learning (Khosla et al., NeurIPS 2020) demonstrates superior data efficiency over cross-entropy in reduced-data regimes, and label contrastive coding for graph classification (LCGNN, arXiv 2101.05486) verifies this advantage extends to graph-level tasks — making supervised contrastive pre-training viable even with moderate corpus sizes. EMNLP 2026 (ARR submission deadline: May 25, 2026) is an appropriate venue under the 'LLM Agents' area.

## Landscape (SOTA & Limitations)

STAC (arXiv 2509.25624, Sep 2025; withdrawn from ICLR 2026 but benchmark remains open-source) demonstrates that chaining benign tool calls achieves >90% ASR even on GPT-4.1; its best prompt-based defense reduces ASR by only 28.8%. ToolSafe (arXiv 2601.10156, Jan 2026) trains an RL-based step-level guardrail with interpretable feedback (TS-Guard) but reasons per-step rather than over full graph structure. RLM-JB (arXiv 2602.16520, Feb 2026) uses recursive language models for jailbreak detection but operates on INPUT TEXT, not tool-call execution traces. AgentArmor (ICLR 2026, arXiv 2508.01249) constructs program dependency graphs (PDGs) and applies a type-system-based inspector, reducing ASR to 3% on AgentDojo — but targets indirect prompt injection with a rule-based type system that cannot generalize to novel compositions. Agent-Sentry (arXiv 2603.22868, Mar 2026) uses structural classifier + allowlist + LLM judge — fundamentally rule-based, targeting prompt injection. ARGUS (arXiv 2605.03378, May 2026) constructs influence provenance graphs with rule-based verification for context-aware prompt injection. MindGuard (arXiv 2508.20412, Jan 2026) constructs Decision Dependence Graphs (DDGs) from LLM attention flows for tool-poisoning defense — achieving 94-99% detection precision — but operates pre-execution on attention patterns, uses empirical thresholds rather than learned representations, and targets tool metadata poisoning where the threat is in the tool description, not compositional harm emerging from execution-level data-flow between benign calls. G-Guard (arXiv 2507.07146) uses GCN on text entity graphs. GuardNet (arXiv 2509.23037) achieves 99.8% F1 via hierarchical GNN over token graphs. In the MAS defense space, G-Safeguard (ACL 2025) applies supervised GNN on multi-agent communication topology; BlindGuard (ACL 2026, arXiv 2508.08127) uses unsupervised corruption-guided contrastive learning on hierarchical agent graphs — its corruption-guided detection paradigm directly inspires our approach but operates on inter-agent communication, not tool-call dependencies. XG-Guard (arXiv 2512.18733) uses bi-level GNN for explainable MAS anomaly detection. IPIGuard (EMNLP 2025) constructs tool dependency graphs but targets indirect prompt injection via pre-planned execution. TraceSafe (arXiv 2604.07223, Apr 2026) benchmarks mid-trajectory guardrails and finds structural data competence matters more than semantic safety alignment. The key gap: all existing trace/provenance-based defenses (AgentArmor, Agent-Sentry, ARGUS, MindGuard) are RULE-BASED or THRESHOLD-BASED and cannot generalize to unseen compositional patterns; no LEARNED model reasons over tool-call data-flow dependency graphs to detect compositional jailbreaks where each individual tool invocation is benign.

## Proposed Approach

We propose CompGraph, a supervised contrastive graph learning framework that detects compositional jailbreaks in tool-augmented LLM agents by reasoning over tool-call dependency graphs. The approach has four components:

(1) GRAPH CONSTRUCTION: From agent execution traces (STAC format), we construct directed acyclic graphs where nodes represent individual tool invocations and edges capture three types of dependencies: data-flow (output-to-input value propagation), temporal ordering, and argument overlap (shared entities/values across calls). Each node is encoded via frozen Qwen3-Embedding-8B (MTEB #1 multilingual embedding model, 4096-dim) applied to a concatenation of tool name, serialized arguments, and return value summary. We use a general-purpose embedding model rather than a safety classifier — since STAC attacks use individually benign tool calls, a safety-tuned encoder would produce near-identical 'safe' embeddings for all nodes, destroying discriminative signal.

(2) CORRUPTION-GUIDED CONTRASTIVE PRE-TRAINING: We construct a pre-training corpus of ~5000 benign tool-call graphs (randomly composed from STAC's tool inventory) plus ~2000 synthetic attack graphs (generated via STAC's automated generation pipeline). A 3-layer MPNN encoder with graph-level mean-pooling readout is trained via supervised contrastive loss (SupCon; Khosla et al., NeurIPS 2020): positive pairs are augmented views of same-class graphs (node feature masking, edge dropping, subgraph sampling); negative pairs are cross-class graphs. Crucially, we apply three formally-defined corruption operators to benign graphs as hard negatives:

   (a) DATA-FLOW REROUTING: For a benign edge (tool_i → tool_j), redirect the data-flow to a sensitive tool_k where tool_k ∈ {send_email, http_post, write_external_file, api_call_external}. This simulates STAC's 'data exfiltration' and 'unauthorized communication' failure modes by creating chains where benign data-gathering feeds into exfiltration endpoints.

   (b) CHAIN EXTENSION: Append a terminal exfiltration node to an existing benign subgraph's leaf node, connecting via a data-flow edge that propagates the leaf's output. The appended node is sampled from a sensitive-tool vocabulary. This simulates STAC's 'information leakage' and 'privacy violation' failure modes.

   (c) ARGUMENT INJECTION: Identify sensitive argument values (API keys, file paths containing 'credentials'/'password'/'secret', PII fields) in one subgraph and copy them into an unrelated tool call's arguments in a different subgraph, creating a cross-subgraph data-flow edge. This simulates STAC's 'credential misuse' and 'unauthorized access' failure modes.

   Each corruption operator maps to 2-3 of STAC's 10 failure modes, and we validate that corrupted graphs are structurally similar to real attack graphs by measuring graph edit distance between corruptions and held-out STAC attacks (requiring mean GED within 1σ of intra-attack-class GED). This ensures corruptions produce realistic hard negatives rather than unrealistic graph structures.

   We justify this supervised contrastive approach on data-efficiency grounds: unlike self-supervised GCL — which requires >4,000 graphs to outperform untrained baselines by a modest ~2% ROC-AUC (arXiv 2509.01541) — supervised contrastive learning with explicit class labels provides direct optimization signal, demonstrating superior data efficiency over cross-entropy in reduced-data regimes (Khosla et al., NeurIPS 2020). LCGNN (arXiv 2101.05486) confirms this advantage extends to graph-level classification, achieving faster convergence and lower loss with the same training data. Our pre-training corpus of ~7000 graphs with explicit class labels operates in a fundamentally different efficiency regime than self-supervised GCL.

(3) FEW-SHOT-AWARE FINE-TUNING: With only 483 labeled STAC samples (averaging ~48 per failure mode, likely imbalanced), standard supervised fine-tuning risks overfitting. We adopt a three-pronged strategy:

   (a) LINEAR PROBE (primary): Freeze the pre-trained MPNN encoder entirely and train only a lightweight classification head (2-layer MLP) on STAC's labeled data. This reduces trainable parameters by >95% and prevents catastrophic forgetting of pre-trained representations.

   (b) PROTOTYPE-BASED CLASSIFICATION (alternative): Compute mean graph embedding per class (benign vs. each failure mode) from support examples, classify test graphs via nearest-prototype in embedding space. This requires zero gradient updates at inference and naturally handles class imbalance.

   (c) AUGMENTED FINE-TUNING (scaling): Use STAC's automated pipeline to generate ~500 additional labeled attack traces (validated through in-environment execution), expanding the fine-tuning set to ~1000 labeled samples. We report results both with and without augmentation to isolate the contribution of additional data.

   We compare all three strategies and report which achieves best ASR reduction vs. FPR tradeoff.

(4) SUPERVISED CLASSIFICATION: The fine-tuned system outputs binary safe/unsafe prediction plus auxiliary 10-way failure-mode classification (when using the MLP head). We use stratified splitting by failure mode for evaluation.

Evaluation: (a) In-distribution: held-out STAC splits (stratified by failure mode), reporting ASR reduction and detection F1. (b) Cross-failure-mode generalization: hold out 2-3 of STAC's 10 failure modes during training and evaluate on held-out modes — testing whether learned graph representations capture transferable compositional structure. (c) False positive rate on benign traces from STAC's baseline runs. (d) Baselines: (i) STAC's reasoning-driven defense prompt (best existing, 28.8% ASR reduction), (ii) ToolSafe's step-level TS-Guard, (iii) Weisfeiler-Leman subtree kernel + SVM on tool-call graphs, (iv) hand-crafted graph features (depth, branching factor, data-flow chain length, argument overlap density, tool fanout, sensitive-tool reachability, cross-subgraph data-flow count) + random forest, (v) MPNN from scratch (no pre-training) with linear probe, (vi) self-supervised GraphCL pre-training + linear probe ablation (to directly compare supervised vs. self-supervised contrastive), (vii) SupCon without corruption augmentations ablation (to isolate corruption contribution). We target competitive ASR reduction with <5% FPR on benign traces.

The key contribution is methodological: we formalize tool-call dependency graph construction from execution traces, define semantically-grounded corruption operators that generate realistic hard negatives mapped to known failure modes, and demonstrate that supervised contrastive graph learning with few-shot-aware fine-tuning captures compositional attack patterns invisible to step-level, prompt-level, rule-based, or attention-based defenses.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$250-400 (800+ orchestration turns + $120 synthetic trace generation)', 'estimated_gpu_cost': '$420-630 (210h × $2.00-3.00/hr H100)', 'gpu_hours': '~210h H100 (embedding extraction ~15h, synthetic attack generation ~20h, corruption validation ~10h, contrastive pre-training with augmentation search ~50h, fine-tuning strategy comparison ~40h, non-neural baselines ~10h, ablations ~45h, evaluation ~20h)', 'gpu_utilization': '~80%; continuous scheduling with parallelized ablation arms, capped at ≤210h', 'risk_note': 'Without human judgment on corruption operator semantics, auto-mode should run GED validation as automated quality gate: reject corrupted graphs with GED > 2σ from mean intra-attack-class GED.', 'speed_bottleneck': 'GPU count for parallel ablation arms (2-4 H100s optimal); secondary bottleneck is Qwen3-Embedding-8B throughput for encoding ~70K tool-call descriptions', 'team': '0 (initial setup: STAC dataset download, environment config, STAC pipeline setup for synthetic generation)', 'timeline': '5-7 days with 2-4 H100 GPUs available concurrently'}
- **human_in_loop**: {'claude_api_cost': '$150-250 (300 orchestration turns × $0.10 + $100 for synthetic trace generation)', 'estimated_gpu_cost': '$380-570 (190h × $2.00-3.00/hr H100)', 'gpu_hours': '~190h H100 (embedding extraction ~15h, synthetic attack generation via STAC pipeline ~20h, corruption operator validation ~10h, contrastive pre-training ~40h, fine-tuning strategies ~35h, non-neural baselines ~10h, ablations ~40h, evaluation ~20h)', 'gpu_utilization': '~55-65%; agent queues sequential experiments, human reviews corruption quality and validates GED constraints', 'risk_note': "Primary risks: (1) STAC's pipeline may produce repetitive attack patterns — mitigated by measuring pairwise GED diversity before training; (2) corruption operators may produce unrealistic graphs — mitigated by GED validation against real attacks; (3) 483 labeled samples may be insufficient even with linear probing — mitigated by prototype-based fallback and pipeline augmentation.", 'team': '1 researcher, ~1-2hr/day for corruption operator validation, GED quality checks, and writing', 'timeline': '7-9 days (targeting EMNLP 2026 ARR May 25 deadline)'}
- **manual**: {'estimated_gpu_cost': '$320-480 (160h × $2.00-3.00/hr H100)', 'gpu_hours': '~160h H100 (embedding extraction ~15h, synthetic attack generation via STAC pipeline ~15h, corruption-guided contrastive pre-training ~40h, fine-tuning strategies (linear probe + prototype + augmented) ~35h, ablations ~35h, evaluation ~20h)', 'gpu_utilization': '~25-35% effective; GPU idles during debugging, analysis, and writing', 'team': '2 researchers (1 ML/graph learning, 1 LLM security/agent systems)', 'timeline': '2-3 months'}

## Key References

- STAC: When Innocent Tools Form Dangerous Chains to Jailbreak LLM Agents (arXiv 2509.25624, Sep 2025; withdrawn from ICLR 2026; benchmark open-sourced at amazon-science/MultiTurnAgentAttack)
- ToolSafe: Enhancing Tool Invocation Safety of LLM-based Agents via Proactive Step-level Guardrail and Feedback (arXiv 2601.10156, Jan 2026)
- RLM-JB: Recursive Language Models for Jailbreak Detection — A Procedural Defense for Tool-Augmented Agents (arXiv 2602.16520, Feb 2026)
- AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection (ICLR 2026, arXiv 2508.01249)
- Agent-Sentry: Bounding LLM Agents via Execution Provenance (arXiv 2603.22868, Mar 2026)
- ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection (arXiv 2605.03378, May 2026)
- MindGuard: Intrinsic Decision Inspection for Securing LLM Agents Against Metadata Poisoning (arXiv 2508.20412, Jan 2026)
- G-Guard: Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak (arXiv 2507.07146, 2025)
- GuardNet: Graph-Attention Filtering for Jailbreak Defense in Large Language Models (arXiv 2509.23037, Sep 2025)
- BlindGuard: Safeguarding LLM-based Multi-Agent Systems under Unknown Attacks (ACL 2026, arXiv 2508.08127)
- XG-Guard: Explainable and Fine-Grained Safeguarding of LLM Multi-Agent Systems via Bi-Level Graph Anomaly Detection (arXiv 2512.18733, Dec 2025)
- G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems (ACL 2025)
- IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents (EMNLP 2025)
- TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories (arXiv 2604.07223, Apr 2026)
- Supervised Contrastive Learning (Khosla et al., NeurIPS 2020)
- Label Contrastive Coding based Graph Neural Network for Graph Classification [LCGNN] (arXiv 2101.05486, DASFAA 2021)
- Graph Contrastive Learning vs. Untrained Baselines: The Role of Dataset Size (arXiv 2509.01541, Sep 2025)
- Graph Contrastive Learning with Augmentations [GraphCL] (NeurIPS 2020)
- Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models (2025)
- SentinelAgent: Graph-based Anomaly Detection in Multi-Agent Systems (arXiv 2505.24201, May 2025)
- ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)
- GAMMAF: A Common Framework for Graph-Based Anomaly Monitoring Benchmarking in LLM Multi-Agent Systems (arXiv 2604.24477, Apr 2026)
- DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs (arXiv 2602.16935, Feb 2026)
- Solver-Aided Verification of Policy Compliance in Tool-Augmented LLM Agents (arXiv 2603.20449, Mar 2026)
- AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents (ICLR 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally well-structured proposal with razor-sharp differentiation from 15+ related works across multiple threat models and granularities. Corruption operators are formally defined with explicit mapping to STAC failure modes. Evaluation plan includes 7 baselines and 2 ablations with clear hypotheses. The complexity (4 components, 3 corruption operators, 3 fine-tuning strategies) is warranted by the problem.', 'score': 4}**/5
  - feasibility: **{'rationale': "Manual mode at 160h and HIL at 190h are within the 200h H100 budget. All required resources are verified available: STAC benchmark open-sourced on GitHub, Qwen3-Embedding-8B on HuggingFace, STAC's automated generation pipeline for synthetic data. The three-pronged fine-tuning strategy (linear probe, prototype, augmented) intelligently addresses the 483-sample data scarcity. Timeline of 7-9 days is tight but feasible given the well-scoped plan and existing tooling.", 'score': 4}**/5
  - impact: **{'rationale': "Addresses a verified and urgent gap: STAC achieves >90% ASR on GPT-4.1 with best prompt defense reducing ASR by only 28.8%. EMNLP 2026's new LLM Security track (verified via official CFP) provides high visibility for defense contributions. If the approach works, it establishes a new paradigm (learned graph-structural defense) for an under-defended attack surface that TraceSafe identifies as suffering from a 'structural bottleneck' — directly motivating graph-structural approaches.", 'score': 4}**/5
  - novelty: **{'rationale': 'Verified gap is real: no existing work uses a learned GNN on tool-call dependency graphs for compositional jailbreaks. AgentArmor (rule-based type system), Agent-Sentry (XGBoost on hand-crafted features), ARGUS (rule-based verification), MindGuard (threshold-based attention-flow), and MAS defenses (BlindGuard/G-Safeguard operate on inter-agent graphs) all target different threat models or use non-learned/non-graph-structural methods. Domain-specific corruption operators mapped to STAC failure modes add genuine methodological novelty. However, the core technical machinery (MPNN + SupCon + corruption augmentation) is a recombination of established components.', 'score': 4}**/5

## Human Review Note

【优化方案】

1. **[标题]** — 从系统命名式标题改为传达理论贡献的标题："Learning Compact Benign Manifolds on Tool-Call Dependency Graphs for Cross-Compositional Attack Detection" — 命中 Novelty（审稿人第一印象从"又一个系统"变为"有理论深度的方法论工作"）

2. **[Introduction §1 / 核心研究问题]** — 将原始的 existence claim（"first learned defense on tool-call dependency graphs"）彻底重塑为 capability claim："Can learned graph representations generalize to structurally novel compositional attacks whose failure modes were never seen during training?" 以 cross-failure-mode generalization 作为核心研究问题而非附属评估项 — 命中 Novelty + Significance（从"我是第一个做 X 的"升级为"我解决了一个有 intellectual substance 的开放问题"）

3. **[Introduction §2 / Taxonomy 作为 co-primary contribution]** — 新增独立段落，将"rule-based vs. learned defenses 的适用边界"提升为与 CompGraph 系统并列的核心贡献。阐明：rule-based 方法在 single-step policy violations 和 type-checkable invariants 上足够，learned methods 仅在 multi-hop indirect flows、compositional novelty、temporal constraints 时有增量价值。使论文即使被更好系统替代，taxonomy 仍具引用价值 — 命中 Significance（提供 meta-level insight，使 borderline 论文有独立 conceptual contribution 作为安全网）

4. **[Introduction §3 / LLM-as-judge trivial alternative 预判]** — 新增段落主动论证 CompGraph 相对于"直接用强 LLM 判断 trace"的不可替代性：(a) latency（per-step MPNN ~5-20ms vs. LLM API ~500-2000ms），(b) determinism（MPNN 输出确定性 vs. LLM 多次运行方差），(c) cost（单次 forward pass vs. 每步 API 调用）。在 intro 层面 neutralize 这一最强 trivial alternative — 命中 Significance + Novelty（防止审稿人第一反应是"why not just use GPT-4?"）

5. **[Related Work / §2.1 IDS 经典范式 lineage]** — 新增对 intrusion detection 经典文献的定位：Forrest et al. 1996（system call sequences）、LSTM-based IDS、Deep SVDD（2018）。明确声明：novelty 不在于"learn normal, detect deviation"这一已有 30 年历史的原则，而在于将其应用于 compositional tool-call graphs 并通过 security-grounded corruption operators 实现 cross-failure-mode generalization — 命中 Related Work 全面性 + Novelty defensibility（安全背景审稿人不会认为作者有盲区）

6. **[Related Work / §2.2 BlindGuard 技术差异化]** — 新增专节论证三大技术挑战：(a) 低拓扑区分度——tool-call graphs 中 benign/malicious 拓扑近乎同构，区分在语义而非结构，BlindGuard 的 random node/edge corruption 无法模拟真实攻击；(b) 高节点同质性——所有节点都是 tool invocation（vs. MAS 中异构 agent 角色），需要更丰富的边语义和子图模式；(c) 语义 augmentation 必要性——随机扰动不够，必须用 domain-grounded corruption operators 模拟攻击原语。由此从"换了个 domain"升级为"解决了新的技术问题" — 命中 Novelty（直接防御"This is BlindGuard applied to a different graph type"的判定）

7. **[Related Work / §2.3 GAD 文献差异化]** — 新增对 graph-level contrastive anomaly detection 文献（SIGNET, ICLR 2024; BOURNE, NeurIPS 2024）的讨论。核心差异：(a) GAD 假设 anomaly 在 topology 上可区分，tool-call graph 的 anomaly 是 semantic 的；(b) GAD 用 task-agnostic random augmentation，CompGraph 用 domain-specific security-grounded corruption — 命中 Related Work（防止审稿人认为作者不知道 GAD 文献）+ Novelty（主动建立区分）

8. **[新增 Section 3: 理论框架 — Benign Manifold + Attack Primitive Compositionality]** — 这是最核心的理论新增，包含四层论证：
   - §3.1 Benign Manifold Hypothesis：SupCon 学习 benign execution 的紧致低维流形
   - §3.2 Corruption Operators 作为 Attack Primitives：三个 operators 不是模拟完整攻击，而是模拟攻击原语（数据流重定向 / 链路延伸 / 参数注入）；任何 compositional attack 需通过这些原语的有限组合（≤3）偏离 benign manifold
   - §3.3 组合泛化机制：corruption-guided boundary sharpening 在原语方向上的灵敏度可线性组合地泛化到未见攻击组合——类比词表征泛化到未见句子的逻辑
   - §3.4 Scope Bounding：显式限定 claim 适用前提——generalization 成立条件为攻击偏离方向落在 primitives span 的子空间内；对正交方向的攻击退化为 pure anomaly detection 效果
   
   附 empirical validation：对 STAC 10 个 failure mode 做 primitive decomposition，验证各 mode 可被 ≤3 个 primitive 组合解释
   — 命中 Novelty（从 engineering contribution 升级为有可验证理论的 method paper；区分于 Deep SVDD 等泛泛的 anomaly detection）

9. **[Section 3 / Taint Analysis 回应论证]** — 新增论证 GNN 的 representational advantage 超越经典 taint analysis：(a) Multi-hop indirect data flow（无单一 source-to-sink 边）；(b) Context-dependent benignity（同结构不同 context 的区分——限定适用范围为 graph structure 可推断 context 的场景，不 overclaim trigger provenance）；(c) Temporal ordering constraints（taint analysis 是 order-agnostic 的 reachability analysis）；(d) Compositional novelty（无需 per-pattern rules）。预测 CompGraph 最大优势在 multi-hop + temporal + compositionally novel 攻击上 — 命中 Novelty（neutralize "overcomplicated taint analysis" 判定）

10. **[Section 4: Method / §4.5 Runtime Monitoring 定位]** — 将原始模糊的"post-execution detection"明确改为 per-step runtime monitor：每个 tool call 完成后增量更新 graph + MPNN forward pass → 超阈值即中止执行。这使 ASR reduction 指标有明确语义（prevention 而非 forensics） — 命中 Technical Soundness（消除"到底是 runtime defense 还是 forensic tool"的 paradigm confusion）

11. **[Section 4: Method / Benign Graph 生成策略]** — 将原始的"randomly composed from tool inventory"改为：优先使用 STAC benign task 的真实 agent traces（~3000），辅以约束随机生成（type-compatible data-flow + 频率分布匹配真实 traces）。报告 MMD 量化预训练 benign graphs 与真实 benign traces 之间的分布偏移 — 命中 Technical Soundness（防止 spurious "non-random = attack" signal）

12. **[Section 5: Baselines / 从原有数量扩展至 11 个]** — 新增 6 个关键 baselines：
    - AgentArmor（ICLR 2026; PDG + type system）：直接对比 rule-based 最强系统
    - Agent-Sentry（Mar 2026; provenance graph → XGBoost）：对比 existing learned defense
    - Taint Analysis（classical taint tracking）：neutralize trivial alternative
    - BlindGuard-adapted（random corruption on same MPNN）：隔离 semantic vs. random augmentation 的贡献
    - Sequence Transformer（same embeddings + SupCon, temporal order, Transformer encoder）：隔离 graph structure vs. sequence 的贡献
    - LLM-as-judge（GPT-4o few-shot + calibrated confidence）：neutralize 最强 trivial alternative + 提供 latency/cost 锚点
    
    所有 neural baselines 声明参数量匹配（±10%），appendix 报告 exact parameter count — 命中 Technical Soundness（每个核心 claim 都有直接实验支撑，无遗漏对比）

13. **[Section 5: Evaluation Protocol / ASR Reduction]** — 将含糊的 ASR reduction 定义改为 prefix-based simulation 统一协议：对每条攻击 trace 从 step 1 逐步回放，记录首次触发 alert 的 step index；所有 baselines 使用同一协议。额外报告 detection latency distribution（首次触发位于 trace 进度百分比） — 命中 Technical Soundness（跨 baseline 可比性建立；detection latency 展示实际安全价值）

14. **[Section 5: Cross-failure-mode Evaluation 强化]** — (a) 报告全部 C(10,3)=120 hold-out configurations 的完整结果分布（violin plot），消除 cherry-picking 嫌疑；(b) 明确报告每个 configuration 下 test set exact size + statistical power 讨论；(c) 5-fold stratified CV + mean±std for in-distribution — 命中 Technical Soundness（小样本场景下的统计说服力最大化）

15. **[Section 5: Corruption-Unseen Evaluation 设计]** — 新增核心子实验：pre-train with all 3 operators → 测试 STAC 中"non-analogous" failure modes。操作化定义 structural analogy（≤2 次 operator 应用可复现 = analogous）；3-4 名标注者 likert scale（0-3）+ Fleiss' κ；多阈值 robustness check。验证 encoder 是否超越 corruption operators 显式编码的模式 — 命中 Novelty（generalization hypothesis 的 empirical test，不再是 claim without evidence）

16. **[Section 5: Ablation 全面扩展]** — 新增 5 个 ablation 维度：
    - Corruption operator leave-one-out（3 组）：每个 operator 的独立贡献
    - Edge type ablation（3 组）：data-flow only → +temporal → all three
    - Node embedding ablation（3 组）：Qwen3-8B / MiniLM-L6 / one-hot+BoW + latency-accuracy Pareto frontier
    - BlindGuard augmentation vs. semantic corruption A/B test
    - Graph size sensitivity（performance vs. trace length）
    — 命中 Technical Soundness（审稿人对 "which component matters" 的必问问题预先回答）

17. **[Section 5: 指标体系扩展]** — 从原始的 ASR reduction + F1 + FPR 扩展为：AUROC/AUPRC（threshold-independent primary metrics）+ FPR@90/95% recall + Recall@1/5% FPR + per-failure-mode F1 breakdown（10-mode table）+ ROC/PR curves 图 + cost comparison with LLM-as-judge — 命中 Technical Soundness（全面且实用的评估角度）

18. **[Section 5: Inference Latency 报告]** — 新增 per-step latency 分解为三部分（embedding / graph update / MPNN forward pass），按图规模 5/10/20 nodes 分别报告，with/without GPU。结合 node embedding ablation 构建 latency-accuracy Pareto frontier — 命中 Technical Soundness（"practical monitor" claim 需要 evidence）

19. **[Section 5: Out-of-Benchmark Validation]** — 新增小规模外部验证：从 AgentBench/ToolBench 手动构造 20-30 条 compositional attack traces，报告 CompGraph 的定性表现，证明模型不 overfit 到 STAC-specific patterns。配合 STAC failure mode taxonomy（单跳/多跳、direct/indirect、有/无时序约束）论证覆盖性 — 命中 Technical Soundness（缓解单一 benchmark 的 external validity 质疑）

20. **[Limitations Section]** — 新增显式讨论：(a) Generalization 的适用边界（primitives span 之外的攻击方向可能失效）；(b) STAC 483 traces / 10 modes 的规模限制；(c) 统计效力在小 test set 场景下的局限；(d) Context-dependent claim 受限于不编码 trigger provenance — 命中 reviewer 信任度（主动暴露 limitation 远优于被动被发现）

21. **[Timeline]** — 从原始的 "May 25 deadline"（9天）调整为 10 周计划（目标 ARR July 2026），给予充足实验和写作时间 — 命中 Feasibility（确保所有实验承诺可执行）

【主要风险】:

1. **BlindGuard overlap 风险**：BlindGuard（ACL 2026）使用近乎相同的 paradigm（corruption-guided contrastive graph learning）仅在不同 graph type 上。尽管已论证三大技术挑战和 primitive compositionality 理论差异，但如果分到熟悉 BlindGuard 的审稿人，仍可能主观判定"parallel application of the same idea"。Rebuttal 需强调：(a) random corruption 在 tool-call graphs 上失效的实验证据（Baseline #9 的结果）；(b) primitive compositionality 理论是 BlindGuard 没有的独立贡献。

2. **数据规模 / 单一 Benchmark 风险**：STAC 仅 483 traces / 10 failure modes，在 EMNLP 主会可能被认为 "toy scale"。Cross-failure-mode holdout 后 test set 可能仅 50-100 条。即使有 120 configurations violin plot + out-of-benchmark validation + statistical rigor，审稿人仍可能要求更大规模实验。这是当前无法根本解决的结构性弱点——agent security benchmark 生态尚不成熟。

【实施评估】:

- **计算资源**: 1-2 块 A100 GPU 即可满足全部需求。Qwen3-Embedding-8B 推理（~5000 graphs × ~10 nodes/graph × ~100ms/inference ≈ 1.4 GPU-hours）；MPNN pre-training + fine-tuning 单次 <1 小时；全部 ablation（8 组 × 5-fold CV × 120 cross-mode configs × 小模型）总计约 80-120 GPU-hours。LLM-as-judge baseline 约 $30-50 GPT-4o API 费用。总体计算需求适中，普通实验室 GPU 集群即可覆盖。

- **数据需求**: (a) STAC Benchmark（483 labeled traces）— 需确认公开可用性（大概率公开，2025 发布）；(b) STAC benign task traces — 运行 benchmark 中 benign tasks 生成；(c) AgentBench / ToolBench 数据用于外部验证（公开可得）；(d) AgentArmor / Agent-Sentry 若有开源数据可复用。无需构建大规模新数据集。

- **人工介入**: (a) 3-4 名标注者对 10 个 failure mode 进行 primitive analogy 标注（每人约 2-3 小时，含讨论校准）；(b) 手动构造 20-30 条 out-of-benchmark attack traces（约 2-3 人天）；(c) AgentArmor/Agent-Sentry 若无公开代码，可能需联系原作者（沟通成本）。总体人工需求低，无需众包标注。

- **训练需求**: MPNN encoder 规模小（~3 层 / 256-dim / 1-5M 参数），单次训练 <1 小时（A100）。Sequence Transformer baseline 类似规模。**不需要训练大型语言模型**——Qwen3-Embedding-8B 仅用于推理（frozen），不做 fine-tuning。整体训练需求远低于典型 NLP 投稿。

- **新 Benchmark**: 不需要构建独立的新 benchmark。需要的产出物：(a) Corruption-generated synthetic graphs（pipeline 自动生成，非独立发布物）；(b) 20-30 条 out-of-benchmark attack traces（小规模 validation，非正式 benchmark）；(c) STAC failure mode primitive decomposition 标注（1
