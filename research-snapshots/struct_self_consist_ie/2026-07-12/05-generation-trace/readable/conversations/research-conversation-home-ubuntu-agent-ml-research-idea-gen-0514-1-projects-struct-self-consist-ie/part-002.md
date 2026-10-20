# Research conversation: 执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260 — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-home-ubuntu-agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie.md) · [Structured JSON](../../../sessions/39/394b29a69d9515461348.json)

## Round 1

### Tool result

_source line 110 · 2026-05-31T14:25:21.630Z_

<details><summary>↩ Tool result · `toolu_01PGVS48hpc6UDY8sdffhiiu`</summary>

```text
1	# Idea Brief: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural Self-Consistency with Learned Aggregation
2	
3	
4	- **Idea ID**: `idea_010`
5	- **Created**: 2026-05-14
6	- **Approved**: 2026-05-14
7	- **Source**: foreign:be-idea-gen-0509-6
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 via ARR May 2026 (submission: May 25, 2026; commitment: Aug 2, 2026; notification: Aug 20, 2026; conference: Oct 24-29, Budapest), Backup: ARR August 2026 (submission: Aug 3, 2026) → EACL 2027 or NAACL 2027
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.
14	
15	Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.
16	
17	Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
21	2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
22	3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.
23	
24	Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.
25	
26	Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	Test-time compute scaling (TTS) dramatically improves LLM reasoning on scalar-answer tasks, but structured prediction outputs — entity sets, relation graphs, event frames, SQL parse trees, dialogue states — have no clear verification function. Adaptive TTS methods (DSC, Slim-SC, ReASC, CGES, Sonata) further optimize compute allocation — but exclusively for scalar answers where consistency is trivially measured by answer agreement. We ask: when and why does sampling multiple schema-constrained structured outputs and aggregating via structural consistency improve prediction quality, how should compute be adaptively allocated across instances of varying structural complexity, and when does TTS fundamentally fail for structured prediction? We demonstrate through information extraction as the primary testbed, while establishing a general-purpose framework applicable to any structured prediction task.
31	
32	## Opportunity / Why Now
33	
34	TTS is the dominant paradigm for boosting LLM reasoning (DeepSeek-R1, o1), and a rapidly growing literature on adaptive TTS — DSC (NAACL 2025 Findings), Slim-SC (EMNLP 2025), ReASC (ACL 2026), CGES (arXiv 2511.02603), Sonata (ICLR 2026), CoRefine (arXiv 2602.08948), 'Learning When to Sample' (arXiv 2603.08999) — demonstrates that confidence-gated early stopping and difficulty-adaptive allocation can reduce sampling budgets by 45-80% with negligible accuracy loss. Yet this entire literature operates on scalar answers where consistency reduces to answer agreement. Two critical findings frame the gap for structured prediction: (1) PMC12888769 shows weak consistency-accuracy correlation for IE using surface-level Fleiss' Kappa on zero-shot models (Spearman 0.20-0.28), but the authors note that fine-tuned models 'could exhibit different consistency-accuracy dynamics'; (2) arXiv 2509.06861 argues TTS cannot help knowledge-intensive tasks because sampling cannot inject new information. We hypothesize that both findings admit an important exception: for fine-tuned models on structured prediction tasks, a significant fraction of errors are uncertainty-based (boundary detection, type ambiguity, structural composition) rather than knowledge-gap errors — and structural consistency (not surface string matching) can identify correct outputs in this regime. Moreover, structural consistency scores provide a natural gating signal for adaptive compute allocation: high early agreement signals easy instances where further sampling is wasteful, while low agreement signals hard instances requiring the full sampling budget. This opportunity extends beyond IE: any LLM task producing structured outputs — SQL queries, code ASTs, clinical FHIR resources, dialogue states — faces the same gap between scalar-answer TTS methods and structured prediction reality. XGrammar (MLSys 2025) makes constrained sampling near-free (<40 microseconds/token via vLLM's default backend), and mature UIE models (ProUIE, GoLLIE) provide strong base samplers. Concurrent work on multi-model NER ensembles (EL4NER, ACL 2025 submission) aggregates across different models, and CSC-SQL applies self-consistency to text-to-SQL via merge revision — but no work provides a general framework for adaptive structural self-consistency from a single fine-tuned model, isolating TTS contribution from model diversity and directly testing whether self-consistency scaling works for structured prediction.
35	
36	## Landscape (SOTA & Limitations)
37	
38	Test-time scaling is extensively studied for math/code (Forest-of-Thought, ICML 2025; Parallel TTS, Oct 2025; 30B+ token study, Dec 2024) but targets scalar-answer tasks exclusively. Self-consistency voting (Wang et al., ICLR 2023) and its successors — Reasoning-Aware Self-Consistency (NAACL 2025), inverse-entropy weighted voting (arXiv Nov 2025), Radial Consensus Score (arXiv April 2026), confidence-informed SC (arXiv Feb 2025), Ranked Voting SC (ACL 2025 Findings) — all aggregate scalar, embedding-space, or ranked-list answers. Critically, a mature and rapidly growing adaptive TTS literature optimizes compute allocation along a clear lineage: DSC (NAACL 2025 Findings) uses difficulty-based batch-level sample pre-allocation, ranking problems by difficulty and partitioning into easy/hard groups to adaptively allocate inference budgets; Slim-SC (EMNLP 2025) dynamically prunes redundant reasoning chains step-by-step during generation based on inter-chain semantic similarity, achieving up to 45% latency reduction; ReASC (ACL 2026) reframes adaptive sampling from response counting to evidence sufficiency via two-stage reliability-aware accumulation achieving 70% cost reduction; CGES (arXiv 2511.02603) forms Bayesian posteriors over candidate answers for principled early stopping with 69.4% call reduction; Sonata (ICLR 2026) trains a lightweight adapter to predict self-consistency from hidden states for thinking budget allocation (20-60% reduction); CoRefine (arXiv 2602.08948) uses a 211k-parameter Conv1D controller for HALT/RETHINK/ALTERNATIVE decisions with 63% wall-clock speedup; 'Learning When to Sample' (arXiv 2603.08999) achieves 80% token reduction via confidence-aware gating. The 'Reasoning on a Budget' survey (arXiv 2507.02076) provides a comprehensive taxonomy of adaptive TTC methods. However, all these methods define consistency and confidence over scalar answers — none addresses structured outputs where consistency measurement itself is non-trivial. In adjacent structured prediction domains, Functional Majority Voting (arXiv 2604.15618) aggregates code generation samples via execution-based functional equivalence — but this relies on executability, inapplicable to IE or most structured prediction tasks. CSC-SQL applies self-consistency with merge revision to text-to-SQL, but uses a task-specific correction model rather than a general structural consistency framework. STED (arXiv 2512.23712, NeurIPS 2025 Workshop) introduces Semantic Tree Edit Distance for measuring consistency of structured JSON outputs using Hungarian algorithm-based order-invariant matching and multi-level similarity, but functions as an evaluation framework rather than an improvement method — it measures consistency without leveraging it for aggregation or adaptive compute allocation. No work defines a general structural self-consistency framework for structured prediction outputs or uses it for adaptive compute gating. In IE specifically, ProUIE (April 2026) achieves SOTA via GRPO with stepwise fine-grained rewards on Qwen3-4B (ACE05-NER: 86.15 F1, ACE05-Arg: 52.58 F1, SciERC: 46.76 F1, avg NER: 79.44, avg RE: 71.17), and MR-UIE (Sept 2025) applies multi-perspective reasoning with RL — but both are training-time methods that generate single-pass outputs at inference. Post-hoc correction approaches include VerifiNER (ACL 2024) using KB-grounded verification and EL4NER (arXiv 2505.23038) ensembling multiple small LLMs for NER — but these are KB-dependent or multi-model approaches, fundamentally different from single-model self-consistency with adaptive gating. SaM (ACL 2025) dynamically selects and merges domain-specific NER expert models, again a multi-model approach. PMC12888769 (2026) measured consistency-accuracy correlation using Fleiss' Kappa on zero-shot hard-prompted models, finding weak Spearman correlations (0.20-0.28) — but used surface string matching on un-fine-tuned models while we propose structural consistency on task-specific fine-tuned models, and they acknowledged this limitation. The 'Two Failures of Self-Consistency' (Chen et al., 2023) demonstrates poor compositional consistency — IE has compositional structure (entity to relation to event) that may exhibit similar failures, which we explicitly test. No concurrent work applies adaptive test-time sampling with structural aggregation from a single fine-tuned model to any structured prediction task — confirmed via arXiv and OpenReview searches through May 2026.
39	
40	## Proposed Approach
41	
42	We propose Adaptive Structural Self-Consistency Scaling (AS2CS) as both a method and an empirical framework for understanding when adaptive TTS helps structured prediction, demonstrated through information extraction as a comprehensive testbed. The research is structured in three phases: pilot validation (Phase 0), full experimental study (Phase 1), and adaptive gating evaluation (Phase 2).
43	
44	**Phase 0: Pilot Validation and Headroom Analysis (~8h H100, Days 1-3)**
45	Before committing to the full study, we run a targeted pilot to validate two premises. First, using 200 instances each from ACE05 NER and ACE05 EAE (event argument extraction), we sample N=8 extractions at T=1.0 from fine-tuned Qwen3-8B and compute: (a) Fleiss' Kappa on surface string matches (replicating PMC12888769), (b) our soft Jaccard span-level structural consistency score, and (c) Spearman correlation of each metric with per-instance F1 against gold annotations. If structural consistency yields significantly stronger correlation than Fleiss' Kappa (target: Spearman >=0.40 vs. their 0.20-0.28), we proceed. Second, we compute oracle best-of-N F1 gaps per dataset and subtask at N=8 to establish headroom ceilings: if oracle best-of-8 exceeds single-pass by <1 F1 on a subtask, TTS gains are fundamentally ceiling-limited there. We use headroom gaps to prioritize analysis: high-headroom subtasks (likely EAE at ~52 F1, SciERC RE at ~47 F1) receive full experimental treatment, while low-headroom subtasks (likely ACE05 NER near ~87 F1) are analyzed primarily for negative/diagnostic insight. Phase 0 also generates training data for the learned aggregation scorer (Phase 2). If both metrics show weak correlation (<=0.30) even with structural consistency, we pivot to a negative/analytical result.
46	
47	**Base Models**: Qwen3-8B fine-tuned on UIE instruction data (JSON output format, trained with LLaMA Factory following ProUIE's pipeline) as primary model, and GoLLIE-7B as a cross-architecture generalization check.
48	
49	**Sampling**: For each input, we sample N in {4, 8, 16, 32} schema-constrained extractions via XGrammar-backed structured generation in vLLM with temperature T=1.0 (standard for self-consistency sampling, maximizing output diversity), enforcing valid JSON output at near-zero overhead.
50	
51	**Phase 1: Structural Consistency Aggregation (Full Study)**
52	Three aggregation functions tailored to IE subtask structure: (1) span-level entity voting via soft Jaccard similarity over character offsets with type-aware grouping (threshold tau_span), (2) relation-level graph consensus via edge majority voting after entity coreference alignment using mention overlap (threshold tau_coref), (3) event-level frame aggregation via trigger-anchored slot matching with role-wise majority voting (threshold tau_trigger). A composite structural agreement score ranks candidates or constructs a merged consensus output.
53	
54	**Aggregation Hyperparameter Sensitivity Analysis**: Each aggregation function depends on a threshold parameter. We report sensitivity sweeps: tau_span in {0.3, 0.5, 0.7, 0.8}, tau_coref in {0.3, 0.5, 0.7}, tau_trigger in {0.5, 0.7, 0.9}. We report F1 variance across threshold settings per dataset.
55	
56	**Phase 2: Adaptive Gating and Learned Aggregation**
57	
58	*Adaptive Structural Consistency Gating (ASCG)*: Rather than applying a fixed N=32 samples uniformly, we use structural consistency at early samples as a confidence signal for adaptive compute allocation. For each instance: (1) sample N_min=4 extractions and compute structural agreement score S_4, (2) if S_4 >= theta_gate (high early agreement), accept the N=4 aggregation result and stop — the instance is 'easy' and further sampling is wasteful, (3) if S_4 < theta_gate, continue sampling to N_mid=8 and recompute S_8, (4) if S_8 >= theta_gate, accept the N=8 result, (5) otherwise, sample to N_max=16 or 32. We sweep theta_gate in {0.6, 0.7, 0.8, 0.9} and report: average effective N per dataset (expected: 6-10x vs. fixed 32x), compute savings (target: 50-70% reduction with <0.5 F1 loss), and cost-accuracy Pareto frontiers comparing fixed-N vs. adaptive-N. This extends the adaptive TTS paradigm (DSC, Slim-SC, ReASC, CGES, Sonata) to structured prediction for the first time, where the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement.
59	
60	*Learned Aggregation Scorer (LAS)*: Beyond hand-crafted threshold-based aggregation, we train a lightweight MLP (2 hidden layers, ~10K parameters) on Phase 0 pilot data to predict per-instance extraction quality from structural features. Input features (per-instance, computed from N samples): (i) span overlap distribution statistics (mean, variance, max of pairwise soft Jaccard across samples), (ii) type agreement entropy (entropy of predicted entity/relation type distributions across samples), (iii) consistency trajectory (agreement scores at N=4, 8, 16 — captures how consistency evolves with more samples), (iv) structural complexity features (number of predicted entities, relations, events per sample — captures extraction difficulty). The MLP outputs a scalar quality estimate used for: (a) sample selection (select the sample with highest predicted quality), (b) adaptive gating (use predicted quality as the confidence signal instead of raw structural agreement). We compare: hand-crafted aggregation vs. learned selection vs. learned gating, analyzing whether the learned scorer transfers across datasets (train on ACE05 pilot data, evaluate on SciERC/TACREV) and whether it improves over hand-crafted thresholds. The comparison between hand-crafted vs. learned aggregation is itself a finding — if learned aggregation helps significantly, it suggests structural consistency in IE is too complex for simple heuristics; if hand-crafted suffices, it validates the interpretability of our structural metrics.
61	
62	**Broader Applicability of ASCG to Structured Prediction**: While we demonstrate AS2CS through IE, the ASCG framework is the first general-purpose adaptive TTS method for any structured prediction task with non-scalar outputs. The core abstraction — sample multiple structured outputs, measure structural consistency via domain-appropriate alignment, and use consistency as a gating signal for adaptive compute allocation — transfers directly to: (1) semantic parsing, where SQL query graphs can be compared via AST edit distance and table/column overlap, and structural consistency identifies cases where the model is uncertain about join structure or predicate composition (cf. CSC-SQL's merge revision approach, which uses a task-specific correction model rather than general structural gating); (2) code generation, where AST-structured outputs enable tree-edit-distance-based consistency measurement beyond Functional Majority Voting's execution-dependent approach — particularly valuable for non-executable partial code or code in languages without test harnesses; (3) clinical NER and structured extraction, where FHIR-formatted outputs have hierarchical schema constraints and consistency across samples can identify uncertain entity boundaries and type assignments in medical text; (4) dialogue state tracking, where slot-value structures can be compared via slot-wise agreement and structural consistency identifies ambiguous user intents. In each case, the structural consistency metric and gating threshold require domain-specific instantiation, but the adaptive allocation framework (sample N_min, compute structural agreement, gate on consistency) is task-agnostic. We leave empirical validation on these domains to future work, focusing on IE as the most challenging case due to its multi-level compositional structure (entity → relation → event).
63	
64	**Ablation Framework**: Six baselines: (a) single-pass greedy (same model, no TTS), (b) random-of-N (lower bound), (c) naive majority voting (surface string matching, replicating PMC12888769), (d) oracle best-of-N (upper bound), (e) VerifiNER (KB-dependent paradigm comparison on NER subtasks), (f) fixed-N S2CS (uniform sampling without adaptive gating — to isolate ASCG contribution). The gap between oracle and single-pass bounds achievable gain; the gap between AS2CS and naive-majority isolates structural aggregation; the gap between fixed-N and adaptive-N isolates compute efficiency.
65	
66	**Error Taxonomy Analysis** (key analytical contribution): We categorize model errors into: (i) uncertainty errors — correct extraction appears in at least one of N samples but not deterministically (TTS can help), (ii) knowledge-gap errors — correct extraction never appears in any sample (TTS cannot help), (iii) systematic errors — model consistently produces the same wrong output (TTS cannot help). We report the fraction of each error type per dataset and subtask, directly addressing the knowledge-intensive limitation critique.
67	
68	**Headroom-Aware Analysis**: We correlate TTS gains with base single-pass performance level, testing the hypothesis that TTS is most effective for medium-difficulty subtasks (high enough base performance for meaningful samples, low enough ceiling for improvement room). This analysis helps practitioners predict where TTS is worth applying without running the full pipeline.
69	
70	**Compositional Consistency Analysis**: Following the 'Two Failures' work, we measure consistency at atomic (entity) vs. compositional (relation, event frame) granularity.
71	
72	**Evaluation**: 5 datasets — ACE05 (NER+RE+EE), Few-NERD (fine-grained NER, 66 entity types), SciERC (NER+RE), TACREV (sentence-level RE), WikiEvents (document-level EAE). We report F1 with bootstrap significance tests (p<0.05), scaling curves (F1 vs. N and vs. total compute), cost-accuracy Pareto frontiers for fixed-N vs. adaptive-N, error taxonomy distributions, and headroom gap correlations.
73	
74	## Resource Estimate
75	
76	- **auto_research**: {'breakdown': 'Phase 0 pilot + headroom analysis (400 instances ACE05 NER+EAE, N=8, correlation + oracle gap): ~8h. Fine-tuning Qwen3-8B on UIE data: ~20h. Phase 1 sampling Qwen3-8B (5 datasets x 32 samples x T=1.0): ~10h. Phase 1 sampling GoLLIE-7B (5 datasets x 32 samples x T=1.0): ~13h. Oracle/random/naive ablation computation: ~10h. Error taxonomy analysis: ~15h. Compositional consistency analysis: ~8h. Aggregation threshold sensitivity sweeps: ~7h. Phase 2 adaptive gating experiments (4 theta_gate values x 5 datasets x 2 models): ~12h. Learned aggregation scorer training and evaluation: ~5h. VerifiNER paradigm comparison: ~5h. Scaling curves, Pareto frontiers, headroom correlation analysis: ~7h. Total itemized: ~120h. Additional ablations and reruns: ~23h. Buffer: ~22h (not counted in itemized total; combined with ablation headroom yields ~45h or 27% of budget).', 'claude_api_cost': '$350-550', 'estimated_gpu_cost': '$413 (165h x $2.50/hr)', 'gpu_hours': '~165h H100 80GB (with 45h buffer)', 'gpu_utilization': '~26% wall-clock utilization across 2 GPUs over 13 days (~90% computational efficiency during active jobs due to automated pipeline scheduling)', 'risk_note': 'Phase 0 on Days 1-3 serves as go/no-go gate; if pilot fails, only 8h invested. Adaptive gating adds ~12h compute but dramatically improves practical value. Learned scorer training is lightweight (~5h) but transfer across datasets is an empirical question. Reducing to T=1.0 only (standard for self-consistency) creates a 27% compute buffer, sufficient for unexpected reruns or debugging.', 'speed_bottleneck': 'Qwen3-8B fits on single H100; 2 GPUs enable parallel sweeps', 'team': '0 after initial setup', 'timeline': '11-13 days with 2x H100 80GB GPUs (fits before May 25 ARR deadline)'}
77	- **human_in_loop**: {'claude_api_cost': '$150-250', 'estimated_gpu_cost': '$325', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~35-40% wall-clock utilization', 'risk_note': 'ACE05 requires LDC license (LDC2006T06)', 'team': '1 researcher, ~30min/day', 'timeline': '5-6 weeks'}
78	- **manual**: {'estimated_gpu_cost': '$325 (at ~$2.50/hr)', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~25-30% wall-clock utilization', 'team': '1-2 researchers', 'timeline': '8-10 weeks'}
79	
80	## Key References
81	
82	- Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., ICLR 2023)
83	- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)
84	- Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning (ICML 2025)
85	- Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet (Zhao et al., arXiv 2509.06861, 2025)
86	- Consistency-Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction (PMC12888769, 2026)
87	- Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs (Chen et al., arXiv 2305.14279, 2023)
88	- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)
89	- GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)
90	- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv 2604.10633, 2026)
91	- MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction (arXiv 2509.09082, 2025)
92	- VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models (ACL 2024)
93	- EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models (arXiv 2505.23038, 2025)
94	- Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models (ACL 2025)
95	- Ranked Voting based Self-Consistency of Large Language Models (ACL 2025 Findings)
96	- Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)
97	- The Art of Scaling Test-Time Compute for Large Language Models (arXiv 2512.02008, 2024)
98	- The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute (arXiv 2511.02309, 2025)
99	- Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score (arXiv 2026)
100	- Scalable Best-of-N Selection for Large Language Models via Self-Certainty (arXiv 2502.18581, 2025)
101	- Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning (Wang et al., NAACL 2025 Findings)
102	- Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency (Hong et al., EMNLP 2025)
103	- Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning (ReASC, ACL 2026)
104	- CGES: Confidence-Guided Early Stopping for Efficient and Accurate Self-Consistency (arXiv 2511.02603, 2025)
105	- Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning (arXiv 2603.08999, 2026)
106	- Adaptive Thinking: Large Language Models Know When to Think in Latent Space (Sonata, ICLR 2026)
107	- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv 2602.08948, 2026)
108	- STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability (arXiv 2512.23712, NeurIPS 2025 Workshop)
109	- Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs (arXiv 2507.02076, 2025)
110	
111	## Reviewer Evaluation
112	
113	**Scores**:
114	  - clarity: **{'rationale': 'Three-phase design is clearly delineated with explicit go/no-go criteria. Ablation framework with 6 baselines is comprehensive. Error taxonomy, headroom-aware analysis, and compositional consistency analysis are well-motivated. Aggregation hyperparameter sensitivity sweeps address the fragility concern from Round 3.', 'score': 4}**/5
115	  - feasibility: **{'rationale': 'Pilot-gated design limits risk to 8h before go/no-go. T=1.0-only sampling creates a 27% compute buffer (165h vs 200h cap). XGrammar overhead verified as negligible. Qwen3-8B throughput on H100 (~500 tok/s) supports the sampling estimates. 13-day timeline with 2 GPUs is tight but achievable. No pre-trained UIE model exists, but LlamaFactory fine-tuning is well-tooled.', 'score': 4}**/5
116	  - impact: **{'rationale': 'The contribution portfolio — ASCG (first adaptive TTS for structured prediction), error taxonomy (uncertainty vs knowledge-gap), headroom analysis (when TTS is worth applying), and broader applicability framework (semantic parsing, code gen, clinical NER, DST) — provides reliable value regardless of whether absolute F1 gains are large. The analytical contribution alone answers questions the IE community needs addressed.', 'score': 4}**/5
117	  - novelty: **{'rationale': 'The gap is independently verified as genuine — no published work applies adaptive structural self-consistency to structured prediction. MIDGARD (ACL 2024) is the closest predecessor but targets commonsense reasoning graphs (not IE), uses MDL (not structural similarity voting), and lacks adaptive sampling. SCSG (March 2026) uses simple majority voting on ABSA tuples without adaptive gating. The ASCG + LAS combination is novel. Both MIDGARD and SCSG should be cited but do not invalidate the novelty claim.', 'score': 4}**/5
118	
119	## Human Review Note
120	
121	## Agent 审核结果（完整三阶段 pipeline）
122	
123	**Verdict**: PASS
124	
125	**入口三重共识 (X)**: 30.0%
126	**终审自评 (Y)**: 38.0%
127	**出口三重共识 (Z)**: 31.0%
128	**Z 区间**: [26.0%, 35.0%]
129	**真实提升 (Z-X)**: +1.0 pp
130	**幻觉幅度 (Y-Z)**: +7.0 pp
131	**出口一致性**: 中（std=3.2%，落在 3-7% 区间）
132	**出口三次评估**: [33.0, 28.0, 34.0]
133	
134	### 优化方案 / 拒绝详情
135	【优化方案】
136	
137	1. [核心叙事 / 全文 framing] — **从"方法迁移"叙事重构为"诊断范式"叙事**：原始 proposal 以 "we present AS2CS, the first systematic study of adaptive TTS for structured prediction" 开篇，读起来像"把 adaptive TTS 搬到 IE 上"。修改为以 "When and why does TTS help structured prediction?" 为核心问题驱动，TTS Applicability Diagnostic Framework 作为 primary contribution，ASCG/LAS 降格为"构建诊断所需的技术工具"。这使标题的 "When Does..." 承诺在 contribution 列表中被兑现，叙事类型对齐近年高接受度的 empirical-science 范式（类似 "Are Emergent Abilities a Mirage?"）。 — 命中 Novelty + Significance
138	
139	2. [Contribution 排序 / 贡献列表] — **重组四项贡献的排列优先级**：原始排序为 (1) ASCG, (2) LAS, (3) headroom-aware analysis。修改为 (1) TTS Applicability Diagnostic Framework（三轴诊断 + 3-step practitioner protocol）, (2) Error Taxonomy, (3) ASCG, (4) LAS。分析贡献优先于方法贡献，明确区分"分析贡献（primary）"和"技术贡献（enabling）"。 — 命中 Novelty（避免被定性为 engineering contribution）
140	
141	3. [核心论点 / Introduction + Conclusion] — **确立 punch line: "TTS for structured prediction requires knowledge internalization first"**：原始 proposal 将 fine-tuning 作为实验前提但未赋予其解释性地位。修改为：fine-tuning 将错误分布从 knowledge-gap-dominated 转向 uncertainty-dominated，从而恢复 consistency-accuracy correlation——这是论文的 take-home message，用一句话概括全文核心 insight，提升审稿人记忆度。 — 命中 Analysis Depth + Insight Memorability
142	
143	4. [TTS Applicability Diagnostic / 新增独立章节] — **将三个独立分析维度整合为统一诊断框架**：原始 proposal 中 error taxonomy、compositional complexity、model capability 散落在三个独立 RQ 中。修改为整合为 (uncertainty-error ratio × structural complexity × base model capability) 的联合诊断空间，呈现为 2D heatmap + conditioning variable 的 signature figure，并包装为 3-step lightweight protocol（50 dev instances 采样 → 估计复杂度 → 查 heatmap 得 recommended settings）。 — 命中 Significance + Practical Impact
144	
145	5. [Novelty 定位 / Motivation 段落] — **重新 articulate 核心技术挑战**：原始表述 "the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement"，将对齐本身当作挑战，但对齐是已有技术。修改为：核心挑战是 consistency-accuracy 假设（所有 adaptive TTS 方法的前提）在结构化 domain 中默认失效，需要在假设失效的条件下重建 adaptive TTS 的基础——novelty 在于"修复前提"而非"换对齐算法"。 — 命中 Novelty
146	
147	6. [Error Taxonomy / Contribution (3) → 升格为 Contribution (2)] — **从 defensive argument 升格为 formal contribution + TTS feasibility diagnostic tool**：原始 proposal 中 error taxonomy 是"回应 arXiv 2509.06861 批评"的防御性论点。修改为：给出操作性定义（uncertainty error = target 出现在 ≥1 但 &lt;N 个采样中; knowledge-gap error = 在 0 个采样中出现），提供 cross-benchmark 分布统计，展示 TTS gain 与 uncertainty-error 占比的相关性，测量 zero-shot → few-shot → fine-tuned 条件下的错误类型迁移曲线。增加 N ∈ {4,8,16,32} 的分类稳定性 sensitivity analysis。 — 命中 Novelty + Broader Impact
148	
149	7. [RQ4 / 实验设计] — **将 Compositional Consistency Degradation 从实验清单末尾提升为显式 RQ**：原始 proposal 仅在最后一句提到 "compositional consistency degradation"。修改为 RQ4，设计 per-instance complexity-binned 实验（按 entity count、relation nesting depth、event argument count 分层），显式检验是 gradual degradation 还是 sharp phase transition。报告 alignment 计算开销与复杂度的交互。这是 structured prediction 独有的分析维度，scalar-answer TTS 文献中不存在。 — 命中 Analysis Depth + Novelty
150	
151	8. [Pilot Validation / 新增章节] — **增加 pilot-gated 验证步骤 + 收紧阈值**：原始 proposal 说 "We address both through a pilot-gated, headroom-aware research design" 但未给出具体操作。修改为：在每个 benchmark 上对 fine-tuned 和 zero-shot 模型各采 N=8 输出，计算 structural consistency 与 instance-level F1 的 Spearman ρ。Primary proceed 阈值 ρ ≥ 0.4（非原始版本未指定的模糊表述）；0.3 ≤ ρ < 0.4 标记为 marginal regime；ρ < 0.3 across the board 则 pivot 为 negative finding 的分析贡献。Fine-tuned vs. zero-shot 的 paired comparison 本身是独立 empirical 贡献。 — 命中 Technical Soundness
152	
153	9. [Baselines / 实验设计] — **从隐含的 2-level 对比扩展为显式 8-level baseline 矩阵**：原始 proposal 仅隐含 "adaptive vs. fixed sampling"。修改为 8 级阶梯：① single-decode greedy (cost floor), ② fixed-N naive majority vote, ③ fixed-N structural aggregation (ablation), ④ logprob-based confidence gating, ⑤ ASCG + raw consistency, ⑥ ASCG + LAS (proposed), ⑦ Best-of-N with LLM-as-judge reranking (selection vs. aggregation), ⑧ oracle Best-of-N (ceiling)。 — 命中 Technical Soundness + Rigor
154	
155	10. [Temperature / 实验设计] — **增加 temperature ablation**：原始 proposal 直接采用 T=1.0 并声称 "standard for self-consistency"。修改为 T ∈ {0.5, 0.7, 1.0, 1.2} ablation study，分析 temperature 对 consistency-accuracy correlation、aggregation quality、gating accuracy 的影响，承认 T=1.0 是 reasoning task 标准但可能不适用于 fine-tuned IE 模型。 — 命中 Technical Soundness
156	
157	11. [Constrained Decoding / 实验设计] — **增加 constrained decoding × TTS 交互效应分析**：原始 proposal 未讨论 XGrammar constrained decoding 对 consistency signal 的 confounding effect。修改为增加 constrained vs. unconstrained + post-hoc filter 的 ablation，检验 constrained decoding 是否人为膨胀 consistency。若检测到膨胀，提出 dev-set recalibration 策略。报告其对 ρ 的影响作为 minor analytical finding。 — 命中 Technical Soundness
158	
159	12. [Model Scale / 实验设计] — **增加 model capability case study + few-shot 条件**：原始 proposal 仅用 Qwen3-8B 和 GoLLIE-7B。修改为增加 Qwen3-32B fine-tuned（ACE05 + SciERC）和 Qwen3-32B few-shot（无 fine-tune）。GoLLIE 独立为 cross-architecture 比较，不与 scale 混为一谈。RQ3 从 "scaling curve" 降级为 "case study on model capability"——诚实匹配只有两个 scale point 的现实。 — 命中 Soundness + Feasibility
160	
161	13. [LAS / Contribution (4)] — **明确训练协议 + 三路 ablation + transfer + feature importance**：原始 proposal 对 LAS 训练数据来源未说明。修改为：(a) 明确用 official dev set 训练、test set 评估（杜绝泄露）；(b) 增加 annotation efficiency sensitivity (50/100/200/500 instances)；(c) ablation: LAS vs. feature-threshold vs. raw consistency score；(d) leave-one-dataset-out transfer 用 paired bootstrap 检验（非 arbitrary 85% threshold）；(e) SHAP/permutation importance 识别 universally transferable vs. task-specific features。 — 命中 Technical Soundness + Reproducibility
162	
163	14. [泛化声明 / Scope 章节] — **收窄 generality claims 至 IE domain**：原始 proposal 声称 "the first general-purpose framework for adaptive TTS with structured outputs" 并列举 SQL/code/clinical/DST 四个额外 domain 作为 contribution。修改为将核心 claim 限定为 IE，SQL/code/clinical/DST 降为 future work 展望，消除 claim-experiment gap。 — 命中 Technical Soundness（消除 overclaiming 风险）
164	
165	15. [Priority Claims / 全文] — **软化 "first" 声明**：原始 proposal 三次使用 "the first"。修改为 "to our knowledge, among the first to..."，叙事重心从 "we are first" 转向 "the problem is hard because [specific challenges], and we propose [specific solutions]"。 — 命中 Novelty（降低被 falsify 的风险）
166	
167	16. [Related Work / 新增三个方向] — **从仅覆盖 adaptive self-consistency 扩展到六个方向**：原始 proposal 仅引用 DSC/Slim-SC/ReASC/CGES/Sonata/STED。修改为增加：(a) classical structured prediction ensemble methods, (b) LLM confidence estimation for structured outputs, (c) test-time augmentation for NLP, (d) TTS for non-scalar generative NLP + code generation structural consistency (CodeT, MBR-based selection), (e) LLM calibration for structured tasks。每个方向明确差异化定位。加深 STED 讨论：STED = evaluation, AS2CS = aggregation + adaptive gating + diagnostic framework。 — 命中 Related Work
168	
169	17. [统计方案 / Evaluation Metrics] — **增加显著性检验和多 seed 报告**：原始 proposal 未指定统计检验。修改为 paired bootstrap test (n=10000) + 95% CI，3-5 random seeds 的 mean±std，significance threshold "≥ 2 F1 with p < 0.05"。 — 命中 Technical Soundness
170	
171	18. [Significance 底线 / Motivation] — **显式声明何种增益算 meaningful**：原始 proposal 无此声明。修改为 "≥ 2 F1 points or ≥ 30% cost reduction at equivalent F1"，展示作者的 self-awareness。 — 命中 Soundness + 评审印象
172	
173	19. [Paper Organization / 新增段落] — **增加 main vs. appendix 分配策略**：原始 proposal 无此规划，所有实验并列。修改为：正文聚焦 pilot validation 核心结果 + ASCG vs. baselines 主表 + diagnostic heatmap (signature figure) + error taxonomy 分布；所有 ablation 放 appendix；RQ3/RQ4 正文各 1-2 段。缓解 "tries to do too much" 的常见 reviewer 批评。 — 命中 Technical Soundness + Presentation
174	
175	20. [Cost Framing / Introduction + Experiments] — **增加 concrete cost-efficiency metrics**：原始 proposal 用抽象的 "compute-efficient" 表述。修改为报告具体的 average samples saved、cost-accuracy Pareto 改进百分比，总 cost 定义包含 LLM sampling + alignment overhead + gating overhead（honest accounting），并报告 wall-clock time breakdown per complexity bin。 — 命中 Significance + Practical Impact
176	
177	【主要风险】:
178	
179	1. **Algorithmic novelty 的结构性 ceiling**：即使叙事重构为"诊断范式"，ASCG/LAS 的核心技术组件（已有对齐算法 + 标准 MLP + 常规 gating loop）仍然缺乏 algorithmic novelty。如果 1-2 位 reviewer 坚持要 novel algorithm 而非 novel analysis/diagnostic，论文可能被定性为 "systematic empirical study" 并被降分。这是结构性限制，无法通过 proposal 优化进一步缓解——只能靠实验结果的 surprising 程度（特别是 phase transition 发现或 dramatic fine-tuning effect）来补偿。
180	
181	2. **Pilot validation 失败的 pivot 风险**：如果 fine-tuned 模型的 ρ < 0.4 across the board（即结构化 consistency 即使用 alignment-based metrics 也无法作为可靠 confidence proxy），论文必须 pivot 为 negative finding。虽然 dual-outcome 设计使这在学术上是可发表的，但 negative finding 论文的 EMNLP 主会接受概率显著低于 positive finding（估计降至 20-25%），且论文的 primary contribution（diagnostic framework）将失去其 prescriptive value（只剩 descriptive value）。
182	
183	【实施评估】:
184	
185	- **计算资源**: 需要至少 1 × A100-80GB（或等价）用于 Qwen3-8B/GoLLIE-7B 的 fine-tuning 和多次采样推理；Qwen3-32B fine-tuning + 推理需要 2-4 × A100-80GB 或 1 × H100。5 个 benchmark × 4 模型配置 × N=8-16 采样 × 多 seed = 大量推理，预估总 GPU 时长 200-400 A100-hours（含 fine-tuning ~50h + 推理 ~150-350h）。如用云平台（AWS/GCP），约 $600-$1200。LLM-as-judge baseline (baseline 7) 如果用 API model 会有额外 API 成本，约 $100-$300。
186	- **数据需求**: ACE05、Few-NERD、SciERC、TACREV、WikiEvents 五个 benchmark 均公开可得。ACE05 需要 LDC 许可证（大多数学术机构已有）。UIE 格式的 fine-tuning 数据需要从原始数据集转换，转换脚本已有公开实现。无需构建新数据集。
187	- **人工介入**: 不需要人工标注（所有 benchmark 自带 gold annotation）。Error taxonomy 分类完全自动化（基于 gold 对比的操作性定义）。需要研究者人工检查 ~50-100 个 error classification 实例做 sanity check（约 2-4 小时）。LAS feature importance 的 SHAP 分析结果需要研究者解读。整体人工介入量低。
188	- **训练需求**: 需要模型训练。(a) Qwen3-8B fine-tuning on UIE tasks（~10-15h on 1×A100）；(b) Qwen3-32B fine-tuning（~20-30h on 2-4×A100）；(c) GoLLIE-7B 可能需要适配训练或直接用预训练版本；(d) LAS MLP 训练极轻（CPU 级别，分钟级）。总训练时长约 30-50 GPU-hours。
189	- **新 Benchmark**: 不需要构建新 benchmark。所有评测在已有公开 benchmark 上进行。但需要构建 complexity-binned evaluation splits（按 entity count、relation depth 等分层），这是对现有数据的重新组织而非新建。
190	- **预估周期**: 从启动到可投稿约 **8-10 周**。细分：Week 1-2 数据准备 + fine-tuning；Week 2-3 Pilot validation（决定 proceed/pivot）；Week 3-6 主实验（ASCG vs. baselines × 5 benchmarks × 多配置）；Week 5-7 ablation studies + diagnostic heatmap 构建；Week 7-9 写作；Week 9-10 内部 rev
191	
192	
193	## MVP Validation Results
194	
195	- **Date**: 2026-05-14
196	- **Hypothesis Supported**: Yes
197	
198	### Key Metrics
199	
200	NER full rho_sj=0.388 (SJ>FK +6.6pp, p=2e-20) | RE full rho_sj=0.234 (FAIL <0.30) | RE cond rho_sj=0.372 (SJ>FK +11.8pp) | RE pct_zero=42.4% | NER oracle headroom=+5.5pp | RE oracle headroom=+13.1pp | Gate 0: NER F1=66.2%, RE F1=42.1%
201	
202	### Summary
203	
204	MVP 验证 structural self-consistency 作为 IE test-time scaling 信号。5 轮 pilot 实验（ft_001/ft_002_v2 模型，T=1.0/0.7，N=8，SciERC 551 instances）+ 1 轮度量分解诊断。结果：NER 方向强正向（rho_sj=0.388, SJ>FK p=2e-20）；RE full-set FAIL（rho_sj=0.234<0.30），但 RE conditional set（排除 all-zero knowledge-gap 实例）显示强信号（rho_sj=0.372, SJ>FK 11.8pp）。E1 诊断排除了度量设计问题——RE weakness 是复合错误传播的固有属性。T=0.7 vs T=1.0 对比揭示采样温度对信号质量的影响。假设部分验证：entity-level IE 有效，relation-level 需 capability-aware 分析。
205	
206	### Recommendation
207	
208	GO — 进入 research 阶段，走 Narrative A（NER-primary + RE diagnostic）。NER 信号足够强且 SJ>FK 优势一致。RE conditional 分析 + E1 诊断 + 温度敏感性分析为论文增加诊断深度。下一步：E3 (NER N=16 验证 rho 是否过 0.40) + E4 (NER 多数据集泛化 CoNLL/OntoNotes) + RE 诊断整理。目标 ARR May 2026-05-25。
209	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b1cfa29-911a-4cff-9887-76b1ce536132",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "403eecdd-6662-44ec-9b2c-2b06e14c68b5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural Self-Consistency with Learned Aggregation\n\n\n- **Idea ID**: `idea_010`\n- **Created**: 2026-05-14\n- **Approved**: 2026-05-14\n- **Source**: foreign:be-idea-gen-0509-6\n- **Level**: top-tier\n- **Target Venues**: EMNLP 2026 via ARR May 2026 (submission: May 25, 2026; commitment: Aug 2, 2026; notification: Aug 20, 2026; conference: Oct 24-29, Budapest), Backup: ARR August 2026 (submission: Aug 3, 2026) → EACL 2027 or NAACL 2027\n\n## Seed Topic\n\nTarget: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.\n\nDirection: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.\n\nContribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.\n2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.\n3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.\n\nLook for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.\n\nTag: direction=information_extraction, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].\n\n## Core Problem\n\nTest-time compute scaling (TTS) dramatically improves LLM reasoning on scalar-answer tasks, but structured prediction outputs — entity sets, relation graphs, event frames, SQL parse trees, dialogue states — have no clear verification function. Adaptive TTS methods (DSC, Slim-SC, ReASC, CGES, Sonata) further optimize compute allocation — but exclusively for scalar answers where consistency is trivially measured by answer agreement. We ask: when and why does sampling multiple schema-constrained structured outputs and aggregating via structural consistency improve prediction quality, how should compute be adaptively allocated across instances of varying structural complexity, and when does TTS fundamentally fail for structured prediction? We demonstrate through information extraction as the primary testbed, while establishing a general-purpose framework applicable to any structured prediction task.\n\n## Opportunity / Why Now\n\nTTS is the dominant paradigm for boosting LLM reasoning (DeepSeek-R1, o1), and a rapidly growing literature on adaptive TTS — DSC (NAACL 2025 Findings), Slim-SC (EMNLP 2025), ReASC (ACL 2026), CGES (arXiv 2511.02603), Sonata (ICLR 2026), CoRefine (arXiv 2602.08948), 'Learning When to Sample' (arXiv 2603.08999) — demonstrates that confidence-gated early stopping and difficulty-adaptive allocation can reduce sampling budgets by 45-80% with negligible accuracy loss. Yet this entire literature operates on scalar answers where consistency reduces to answer agreement. Two critical findings frame the gap for structured prediction: (1) PMC12888769 shows weak consistency-accuracy correlation for IE using surface-level Fleiss' Kappa on zero-shot models (Spearman 0.20-0.28), but the authors note that fine-tuned models 'could exhibit different consistency-accuracy dynamics'; (2) arXiv 2509.06861 argues TTS cannot help knowledge-intensive tasks because sampling cannot inject new information. We hypothesize that both findings admit an important exception: for fine-tuned models on structured prediction tasks, a significant fraction of errors are uncertainty-based (boundary detection, type ambiguity, structural composition) rather than knowledge-gap errors — and structural consistency (not surface string matching) can identify correct outputs in this regime. Moreover, structural consistency scores provide a natural gating signal for adaptive compute allocation: high early agreement signals easy instances where further sampling is wasteful, while low agreement signals hard instances requiring the full sampling budget. This opportunity extends beyond IE: any LLM task producing structured outputs — SQL queries, code ASTs, clinical FHIR resources, dialogue states — faces the same gap between scalar-answer TTS methods and structured prediction reality. XGrammar (MLSys 2025) makes constrained sampling near-free (<40 microseconds/token via vLLM's default backend), and mature UIE models (ProUIE, GoLLIE) provide strong base samplers. Concurrent work on multi-model NER ensembles (EL4NER, ACL 2025 submission) aggregates across different models, and CSC-SQL applies self-consistency to text-to-SQL via merge revision — but no work provides a general framework for adaptive structural self-consistency from a single fine-tuned model, isolating TTS contribution from model diversity and directly testing whether self-consistency scaling works for structured prediction.\n\n## Landscape (SOTA & Limitations)\n\nTest-time scaling is extensively studied for math/code (Forest-of-Thought, ICML 2025; Parallel TTS, Oct 2025; 30B+ token study, Dec 2024) but targets scalar-answer tasks exclusively. Self-consistency voting (Wang et al., ICLR 2023) and its successors — Reasoning-Aware Self-Consistency (NAACL 2025), inverse-entropy weighted voting (arXiv Nov 2025), Radial Consensus Score (arXiv April 2026), confidence-informed SC (arXiv Feb 2025), Ranked Voting SC (ACL 2025 Findings) — all aggregate scalar, embedding-space, or ranked-list answers. Critically, a mature and rapidly growing adaptive TTS literature optimizes compute allocation along a clear lineage: DSC (NAACL 2025 Findings) uses difficulty-based batch-level sample pre-allocation, ranking problems by difficulty and partitioning into easy/hard groups to adaptively allocate inference budgets; Slim-SC (EMNLP 2025) dynamically prunes redundant reasoning chains step-by-step during generation based on inter-chain semantic similarity, achieving up to 45% latency reduction; ReASC (ACL 2026) reframes adaptive sampling from response counting to evidence sufficiency via two-stage reliability-aware accumulation achieving 70% cost reduction; CGES (arXiv 2511.02603) forms Bayesian posteriors over candidate answers for principled early stopping with 69.4% call reduction; Sonata (ICLR 2026) trains a lightweight adapter to predict self-consistency from hidden states for thinking budget allocation (20-60% reduction); CoRefine (arXiv 2602.08948) uses a 211k-parameter Conv1D controller for HALT/RETHINK/ALTERNATIVE decisions with 63% wall-clock speedup; 'Learning When to Sample' (arXiv 2603.08999) achieves 80% token reduction via confidence-aware gating. The 'Reasoning on a Budget' survey (arXiv 2507.02076) provides a comprehensive taxonomy of adaptive TTC methods. However, all these methods define consistency and confidence over scalar answers — none addresses structured outputs where consistency measurement itself is non-trivial. In adjacent structured prediction domains, Functional Majority Voting (arXiv 2604.15618) aggregates code generation samples via execution-based functional equivalence — but this relies on executability, inapplicable to IE or most structured prediction tasks. CSC-SQL applies self-consistency with merge revision to text-to-SQL, but uses a task-specific correction model rather than a general structural consistency framework. STED (arXiv 2512.23712, NeurIPS 2025 Workshop) introduces Semantic Tree Edit Distance for measuring consistency of structured JSON outputs using Hungarian algorithm-based order-invariant matching and multi-level similarity, but functions as an evaluation framework rather than an improvement method — it measures consistency without leveraging it for aggregation or adaptive compute allocation. No work defines a general structural self-consistency framework for structured prediction outputs or uses it for adaptive compute gating. In IE specifically, ProUIE (April 2026) achieves SOTA via GRPO with stepwise fine-grained rewards on Qwen3-4B (ACE05-NER: 86.15 F1, ACE05-Arg: 52.58 F1, SciERC: 46.76 F1, avg NER: 79.44, avg RE: 71.17), and MR-UIE (Sept 2025) applies multi-perspective reasoning with RL — but both are training-time methods that generate single-pass outputs at inference. Post-hoc correction approaches include VerifiNER (ACL 2024) using KB-grounded verification and EL4NER (arXiv 2505.23038) ensembling multiple small LLMs for NER — but these are KB-dependent or multi-model approaches, fundamentally different from single-model self-consistency with adaptive gating. SaM (ACL 2025) dynamically selects and merges domain-specific NER expert models, again a multi-model approach. PMC12888769 (2026) measured consistency-accuracy correlation using Fleiss' Kappa on zero-shot hard-prompted models, finding weak Spearman correlations (0.20-0.28) — but used surface string matching on un-fine-tuned models while we propose structural consistency on task-specific fine-tuned models, and they acknowledged this limitation. The 'Two Failures of Self-Consistency' (Chen et al., 2023) demonstrates poor compositional consistency — IE has compositional structure (entity to relation to event) that may exhibit similar failures, which we explicitly test. No concurrent work applies adaptive test-time sampling with structural aggregation from a single fine-tuned model to any structured prediction task — confirmed via arXiv and OpenReview searches through May 2026.\n\n## Proposed Approach\n\nWe propose Adaptive Structural Self-Consistency Scaling (AS2CS) as both a method and an empirical framework for understanding when adaptive TTS helps structured prediction, demonstrated through information extraction as a comprehensive testbed. The research is structured in three phases: pilot validation (Phase 0), full experimental study (Phase 1), and adaptive gating evaluation (Phase 2).\n\n**Phase 0: Pilot Validation and Headroom Analysis (~8h H100, Days 1-3)**\nBefore committing to the full study, we run a targeted pilot to validate two premises. First, using 200 instances each from ACE05 NER and ACE05 EAE (event argument extraction), we sample N=8 extractions at T=1.0 from fine-tuned Qwen3-8B and compute: (a) Fleiss' Kappa on surface string matches (replicating PMC12888769), (b) our soft Jaccard span-level structural consistency score, and (c) Spearman correlation of each metric with per-instance F1 against gold annotations. If structural consistency yields significantly stronger correlation than Fleiss' Kappa (target: Spearman >=0.40 vs. their 0.20-0.28), we proceed. Second, we compute oracle best-of-N F1 gaps per dataset and subtask at N=8 to establish headroom ceilings: if oracle best-of-8 exceeds single-pass by <1 F1 on a subtask, TTS gains are fundamentally ceiling-limited there. We use headroom gaps to prioritize analysis: high-headroom subtasks (likely EAE at ~52 F1, SciERC RE at ~47 F1) receive full experimental treatment, while low-headroom subtasks (likely ACE05 NER near ~87 F1) are analyzed primarily for negative/diagnostic insight. Phase 0 also generates training data for the learned aggregation scorer (Phase 2). If both metrics show weak correlation (<=0.30) even with structural consistency, we pivot to a negative/analytical result.\n\n**Base Models**: Qwen3-8B fine-tuned on UIE instruction data (JSON output format, trained with LLaMA Factory following ProUIE's pipeline) as primary model, and GoLLIE-7B as a cross-architecture generalization check.\n\n**Sampling**: For each input, we sample N in {4, 8, 16, 32} schema-constrained extractions via XGrammar-backed structured generation in vLLM with temperature T=1.0 (standard for self-consistency sampling, maximizing output diversity), enforcing valid JSON output at near-zero overhead.\n\n**Phase 1: Structural Consistency Aggregation (Full Study)**\nThree aggregation functions tailored to IE subtask structure: (1) span-level entity voting via soft Jaccard similarity over character offsets with type-aware grouping (threshold tau_span), (2) relation-level graph consensus via edge majority voting after entity coreference alignment using mention overlap (threshold tau_coref), (3) event-level frame aggregation via trigger-anchored slot matching with role-wise majority voting (threshold tau_trigger). A composite structural agreement score ranks candidates or constructs a merged consensus output.\n\n**Aggregation Hyperparameter Sensitivity Analysis**: Each aggregation function depends on a threshold parameter. We report sensitivity sweeps: tau_span in {0.3, 0.5, 0.7, 0.8}, tau_coref in {0.3, 0.5, 0.7}, tau_trigger in {0.5, 0.7, 0.9}. We report F1 variance across threshold settings per dataset.\n\n**Phase 2: Adaptive Gating and Learned Aggregation**\n\n*Adaptive Structural Consistency Gating (ASCG)*: Rather than applying a fixed N=32 samples uniformly, we use structural consistency at early samples as a confidence signal for adaptive compute allocation. For each instance: (1) sample N_min=4 extractions and compute structural agreement score S_4, (2) if S_4 >= theta_gate (high early agreement), accept the N=4 aggregation result and stop — the instance is 'easy' and further sampling is wasteful, (3) if S_4 < theta_gate, continue sampling to N_mid=8 and recompute S_8, (4) if S_8 >= theta_gate, accept the N=8 result, (5) otherwise, sample to N_max=16 or 32. We sweep theta_gate in {0.6, 0.7, 0.8, 0.9} and report: average effective N per dataset (expected: 6-10x vs. fixed 32x), compute savings (target: 50-70% reduction with <0.5 F1 loss), and cost-accuracy Pareto frontiers comparing fixed-N vs. adaptive-N. This extends the adaptive TTS paradigm (DSC, Slim-SC, ReASC, CGES, Sonata) to structured prediction for the first time, where the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement.\n\n*Learned Aggregation Scorer (LAS)*: Beyond hand-crafted threshold-based aggregation, we train a lightweight MLP (2 hidden layers, ~10K parameters) on Phase 0 pilot data to predict per-instance extraction quality from structural features. Input features (per-instance, computed from N samples): (i) span overlap distribution statistics (mean, variance, max of pairwise soft Jaccard across samples), (ii) type agreement entropy (entropy of predicted entity/relation type distributions across samples), (iii) consistency trajectory (agreement scores at N=4, 8, 16 — captures how consistency evolves with more samples), (iv) structural complexity features (number of predicted entities, relations, events per sample — captures extraction difficulty). The MLP outputs a scalar quality estimate used for: (a) sample selection (select the sample with highest predicted quality), (b) adaptive gating (use predicted quality as the confidence signal instead of raw structural agreement). We compare: hand-crafted aggregation vs. learned selection vs. learned gating, analyzing whether the learned scorer transfers across datasets (train on ACE05 pilot data, evaluate on SciERC/TACREV) and whether it improves over hand-crafted thresholds. The comparison between hand-crafted vs. learned aggregation is itself a finding — if learned aggregation helps significantly, it suggests structural consistency in IE is too complex for simple heuristics; if hand-crafted suffices, it validates the interpretability of our structural metrics.\n\n**Broader Applicability of ASCG to Structured Prediction**: While we demonstrate AS2CS through IE, the ASCG framework is the first general-purpose adaptive TTS method for any structured prediction task with non-scalar outputs. The core abstraction — sample multiple structured outputs, measure structural consistency via domain-appropriate alignment, and use consistency as a gating signal for adaptive compute allocation — transfers directly to: (1) semantic parsing, where SQL query graphs can be compared via AST edit distance and table/column overlap, and structural consistency identifies cases where the model is uncertain about join structure or predicate composition (cf. CSC-SQL's merge revision approach, which uses a task-specific correction model rather than general structural gating); (2) code generation, where AST-structured outputs enable tree-edit-distance-based consistency measurement beyond Functional Majority Voting's execution-dependent approach — particularly valuable for non-executable partial code or code in languages without test harnesses; (3) clinical NER and structured extraction, where FHIR-formatted outputs have hierarchical schema constraints and consistency across samples can identify uncertain entity boundaries and type assignments in medical text; (4) dialogue state tracking, where slot-value structures can be compared via slot-wise agreement and structural consistency identifies ambiguous user intents. In each case, the structural consistency metric and gating threshold require domain-specific instantiation, but the adaptive allocation framework (sample N_min, compute structural agreement, gate on consistency) is task-agnostic. We leave empirical validation on these domains to future work, focusing on IE as the most challenging case due to its multi-level compositional structure (entity → relation → event).\n\n**Ablation Framework**: Six baselines: (a) single-pass greedy (same model, no TTS), (b) random-of-N (lower bound), (c) naive majority voting (surface string matching, replicating PMC12888769), (d) oracle best-of-N (upper bound), (e) VerifiNER (KB-dependent paradigm comparison on NER subtasks), (f) fixed-N S2CS (uniform sampling without adaptive gating — to isolate ASCG contribution). The gap between oracle and single-pass bounds achievable gain; the gap between AS2CS and naive-majority isolates structural aggregation; the gap between fixed-N and adaptive-N isolates compute efficiency.\n\n**Error Taxonomy Analysis** (key analytical contribution): We categorize model errors into: (i) uncertainty errors — correct extraction appears in at least one of N samples but not deterministically (TTS can help), (ii) knowledge-gap errors — correct extraction never appears in any sample (TTS cannot help), (iii) systematic errors — model consistently produces the same wrong output (TTS cannot help). We report the fraction of each error type per dataset and subtask, directly addressing the knowledge-intensive limitation critique.\n\n**Headroom-Aware Analysis**: We correlate TTS gains with base single-pass performance level, testing the hypothesis that TTS is most effective for medium-difficulty subtasks (high enough base performance for meaningful samples, low enough ceiling for improvement room). This analysis helps practitioners predict where TTS is worth applying without running the full pipeline.\n\n**Compositional Consistency Analysis**: Following the 'Two Failures' work, we measure consistency at atomic (entity) vs. compositional (relation, event frame) granularity.\n\n**Evaluation**: 5 datasets — ACE05 (NER+RE+EE), Few-NERD (fine-grained NER, 66 entity types), SciERC (NER+RE), TACREV (sentence-level RE), WikiEvents (document-level EAE). We report F1 with bootstrap significance tests (p<0.05), scaling curves (F1 vs. N and vs. total compute), cost-accuracy Pareto frontiers for fixed-N vs. adaptive-N, error taxonomy distributions, and headroom gap correlations.\n\n## Resource Estimate\n\n- **auto_research**: {'breakdown': 'Phase 0 pilot + headroom analysis (400 instances ACE05 NER+EAE, N=8, correlation + oracle gap): ~8h. Fine-tuning Qwen3-8B on UIE data: ~20h. Phase 1 sampling Qwen3-8B (5 datasets x 32 samples x T=1.0): ~10h. Phase 1 sampling GoLLIE-7B (5 datasets x 32 samples x T=1.0): ~13h. Oracle/random/naive ablation computation: ~10h. Error taxonomy analysis: ~15h. Compositional consistency analysis: ~8h. Aggregation threshold sensitivity sweeps: ~7h. Phase 2 adaptive gating experiments (4 theta_gate values x 5 datasets x 2 models): ~12h. Learned aggregation scorer training and evaluation: ~5h. VerifiNER paradigm comparison: ~5h. Scaling curves, Pareto frontiers, headroom correlation analysis: ~7h. Total itemized: ~120h. Additional ablations and reruns: ~23h. Buffer: ~22h (not counted in itemized total; combined with ablation headroom yields ~45h or 27% of budget).', 'claude_api_cost': '$350-550', 'estimated_gpu_cost': '$413 (165h x $2.50/hr)', 'gpu_hours': '~165h H100 80GB (with 45h buffer)', 'gpu_utilization': '~26% wall-clock utilization across 2 GPUs over 13 days (~90% computational efficiency during active jobs due to automated pipeline scheduling)', 'risk_note': 'Phase 0 on Days 1-3 serves as go/no-go gate; if pilot fails, only 8h invested. Adaptive gating adds ~12h compute but dramatically improves practical value. Learned scorer training is lightweight (~5h) but transfer across datasets is an empirical question. Reducing to T=1.0 only (standard for self-consistency) creates a 27% compute buffer, sufficient for unexpected reruns or debugging.', 'speed_bottleneck': 'Qwen3-8B fits on single H100; 2 GPUs enable parallel sweeps', 'team': '0 after initial setup', 'timeline': '11-13 days with 2x H100 80GB GPUs (fits before May 25 ARR deadline)'}\n- **human_in_loop**: {'claude_api_cost': '$150-250', 'estimated_gpu_cost': '$325', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~35-40% wall-clock utilization', 'risk_note': 'ACE05 requires LDC license (LDC2006T06)', 'team': '1 researcher, ~30min/day', 'timeline': '5-6 weeks'}\n- **manual**: {'estimated_gpu_cost': '$325 (at ~$2.50/hr)', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~25-30% wall-clock utilization', 'team': '1-2 researchers', 'timeline': '8-10 weeks'}\n\n## Key References\n\n- Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., ICLR 2023)\n- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)\n- Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning (ICML 2025)\n- Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet (Zhao et al., arXiv 2509.06861, 2025)\n- Consistency-Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction (PMC12888769, 2026)\n- Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs (Chen et al., arXiv 2305.14279, 2023)\n- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)\n- GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\n- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv 2604.10633, 2026)\n- MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction (arXiv 2509.09082, 2025)\n- VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models (ACL 2024)\n- EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models (arXiv 2505.23038, 2025)\n- Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models (ACL 2025)\n- Ranked Voting based Self-Consistency of Large Language Models (ACL 2025 Findings)\n- Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)\n- The Art of Scaling Test-Time Compute for Large Language Models (arXiv 2512.02008, 2024)\n- The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute (arXiv 2511.02309, 2025)\n- Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score (arXiv 2026)\n- Scalable Best-of-N Selection for Large Language Models via Self-Certainty (arXiv 2502.18581, 2025)\n- Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning (Wang et al., NAACL 2025 Findings)\n- Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency (Hong et al., EMNLP 2025)\n- Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning (ReASC, ACL 2026)\n- CGES: Confidence-Guided Early Stopping for Efficient and Accurate Self-Consistency (arXiv 2511.02603, 2025)\n- Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning (arXiv 2603.08999, 2026)\n- Adaptive Thinking: Large Language Models Know When to Think in Latent Space (Sonata, ICLR 2026)\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv 2602.08948, 2026)\n- STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability (arXiv 2512.23712, NeurIPS 2025 Workshop)\n- Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs (arXiv 2507.02076, 2025)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Three-phase design is clearly delineated with explicit go/no-go criteria. Ablation framework with 6 baselines is comprehensive. Error taxonomy, headroom-aware analysis, and compositional consistency analysis are well-motivated. Aggregation hyperparameter sensitivity sweeps address the fragility concern from Round 3.', 'score': 4}**/5\n  - feasibility: **{'rationale': 'Pilot-gated design limits risk to 8h before go/no-go. T=1.0-only sampling creates a 27% compute buffer (165h vs 200h cap). XGrammar overhead verified as negligible. Qwen3-8B throughput on H100 (~500 tok/s) supports the sampling estimates. 13-day timeline with 2 GPUs is tight but achievable. No pre-trained UIE model exists, but LlamaFactory fine-tuning is well-tooled.', 'score': 4}**/5\n  - impact: **{'rationale': 'The contribution portfolio — ASCG (first adaptive TTS for structured prediction), error taxonomy (uncertainty vs knowledge-gap), headroom analysis (when TTS is worth applying), and broader applicability framework (semantic parsing, code gen, clinical NER, DST) — provides reliable value regardless of whether absolute F1 gains are large. The analytical contribution alone answers questions the IE community needs addressed.', 'score': 4}**/5\n  - novelty: **{'rationale': 'The gap is independently verified as genuine — no published work applies adaptive structural self-consistency to structured prediction. MIDGARD (ACL 2024) is the closest predecessor but targets commonsense reasoning graphs (not IE), uses MDL (not structural similarity voting), and lacks adaptive sampling. SCSG (March 2026) uses simple majority voting on ABSA tuples without adaptive gating. The ASCG + LAS combination is novel. Both MIDGARD and SCSG should be cited but do not invalidate the novelty claim.', 'score': 4}**/5\n\n## Human Review Note\n\n## Agent 审核结果（完整三阶段 pipeline）\n\n**Verdict**: PASS\n\n**入口三重共识 (X)**: 30.0%\n**终审自评 (Y)**: 38.0%\n**出口三重共识 (Z)**: 31.0%\n**Z 区间**: [26.0%, 35.0%]\n**真实提升 (Z-X)**: +1.0 pp\n**幻觉幅度 (Y-Z)**: +7.0 pp\n**出口一致性**: 中（std=3.2%，落在 3-7% 区间）\n**出口三次评估**: [33.0, 28.0, 34.0]\n\n### 优化方案 / 拒绝详情\n【优化方案】\n\n1. [核心叙事 / 全文 framing] — **从\"方法迁移\"叙事重构为\"诊断范式\"叙事**：原始 proposal 以 \"we present AS2CS, the first systematic study of adaptive TTS for structured prediction\" 开篇，读起来像\"把 adaptive TTS 搬到 IE 上\"。修改为以 \"When and why does TTS help structured prediction?\" 为核心问题驱动，TTS Applicability Diagnostic Framework 作为 primary contribution，ASCG/LAS 降格为\"构建诊断所需的技术工具\"。这使标题的 \"When Does...\" 承诺在 contribution 列表中被兑现，叙事类型对齐近年高接受度的 empirical-science 范式（类似 \"Are Emergent Abilities a Mirage?\"）。 — 命中 Novelty + Significance\n\n2. [Contribution 排序 / 贡献列表] — **重组四项贡献的排列优先级**：原始排序为 (1) ASCG, (2) LAS, (3) headroom-aware analysis。修改为 (1) TTS Applicability Diagnostic Framework（三轴诊断 + 3-step practitioner protocol）, (2) Error Taxonomy, (3) ASCG, (4) LAS。分析贡献优先于方法贡献，明确区分\"分析贡献（primary）\"和\"技术贡献（enabling）\"。 — 命中 Novelty（避免被定性为 engineering contribution）\n\n3. [核心论点 / Introduction + Conclusion] — **确立 punch line: \"TTS for structured prediction requires knowledge internalization first\"**：原始 proposal 将 fine-tuning 作为实验前提但未赋予其解释性地位。修改为：fine-tuning 将错误分布从 knowledge-gap-dominated 转向 uncertainty-dominated，从而恢复 consistency-accuracy correlation——这是论文的 take-home message，用一句话概括全文核心 insight，提升审稿人记忆度。 — 命中 Analysis Depth + Insight Memorability\n\n4. [TTS Applicability Diagnostic / 新增独立章节] — **将三个独立分析维度整合为统一诊断框架**：原始 proposal 中 error taxonomy、compositional complexity、model capability 散落在三个独立 RQ 中。修改为整合为 (uncertainty-error ratio × structural complexity × base model capability) 的联合诊断空间，呈现为 2D heatmap + conditioning variable 的 signature figure，并包装为 3-step lightweight protocol（50 dev instances 采样 → 估计复杂度 → 查 heatmap 得 recommended settings）。 — 命中 Significance + Practical Impact\n\n5. [Novelty 定位 / Motivation 段落] — **重新 articulate 核心技术挑战**：原始表述 \"the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement\"，将对齐本身当作挑战，但对齐是已有技术。修改为：核心挑战是 consistency-accuracy 假设（所有 adaptive TTS 方法的前提）在结构化 domain 中默认失效，需要在假设失效的条件下重建 adaptive TTS 的基础——novelty 在于\"修复前提\"而非\"换对齐算法\"。 — 命中 Novelty\n\n6. [Error Taxonomy / Contribution (3) → 升格为 Contribution (2)] — **从 defensive argument 升格为 formal contribution + TTS feasibility diagnostic tool**：原始 proposal 中 error taxonomy 是\"回应 arXiv 2509.06861 批评\"的防御性论点。修改为：给出操作性定义（uncertainty error = target 出现在 ≥1 但 &lt;N 个采样中; knowledge-gap error = 在 0 个采样中出现），提供 cross-benchmark 分布统计，展示 TTS gain 与 uncertainty-error 占比的相关性，测量 zero-shot → few-shot → fine-tuned 条件下的错误类型迁移曲线。增加 N ∈ {4,8,16,32} 的分类稳定性 sensitivity analysis。 — 命中 Novelty + Broader Impact\n\n7. [RQ4 / 实验设计] — **将 Compositional Consistency Degradation 从实验清单末尾提升为显式 RQ**：原始 proposal 仅在最后一句提到 \"compositional consistency degradation\"。修改为 RQ4，设计 per-instance complexity-binned 实验（按 entity count、relation nesting depth、event argument count 分层），显式检验是 gradual degradation 还是 sharp phase transition。报告 alignment 计算开销与复杂度的交互。这是 structured prediction 独有的分析维度，scalar-answer TTS 文献中不存在。 — 命中 Analysis Depth + Novelty\n\n8. [Pilot Validation / 新增章节] — **增加 pilot-gated 验证步骤 + 收紧阈值**：原始 proposal 说 \"We address both through a pilot-gated, headroom-aware research design\" 但未给出具体操作。修改为：在每个 benchmark 上对 fine-tuned 和 zero-shot 模型各采 N=8 输出，计算 structural consistency 与 instance-level F1 的 Spearman ρ。Primary proceed 阈值 ρ ≥ 0.4（非原始版本未指定的模糊表述）；0.3 ≤ ρ < 0.4 标记为 marginal regime；ρ < 0.3 across the board 则 pivot 为 negative finding 的分析贡献。Fine-tuned vs. zero-shot 的 paired comparison 本身是独立 empirical 贡献。 — 命中 Technical Soundness\n\n9. [Baselines / 实验设计] — **从隐含的 2-level 对比扩展为显式 8-level baseline 矩阵**：原始 proposal 仅隐含 \"adaptive vs. fixed sampling\"。修改为 8 级阶梯：① single-decode greedy (cost floor), ② fixed-N naive majority vote, ③ fixed-N structural aggregation (ablation), ④ logprob-based confidence gating, ⑤ ASCG + raw consistency, ⑥ ASCG + LAS (proposed), ⑦ Best-of-N with LLM-as-judge reranking (selection vs. aggregation), ⑧ oracle Best-of-N (ceiling)。 — 命中 Technical Soundness + Rigor\n\n10. [Temperature / 实验设计] — **增加 temperature ablation**：原始 proposal 直接采用 T=1.0 并声称 \"standard for self-consistency\"。修改为 T ∈ {0.5, 0.7, 1.0, 1.2} ablation study，分析 temperature 对 consistency-accuracy correlation、aggregation quality、gating accuracy 的影响，承认 T=1.0 是 reasoning task 标准但可能不适用于 fine-tuned IE 模型。 — 命中 Technical Soundness\n\n11. [Constrained Decoding / 实验设计] — **增加 constrained decoding × TTS 交互效应分析**：原始 proposal 未讨论 XGrammar constrained decoding 对 consistency signal 的 confounding effect。修改为增加 constrained vs. unconstrained + post-hoc filter 的 ablation，检验 constrained decoding 是否人为膨胀 consistency。若检测到膨胀，提出 dev-set recalibration 策略。报告其对 ρ 的影响作为 minor analytical finding。 — 命中 Technical Soundness\n\n12. [Model Scale / 实验设计] — **增加 model capability case study + few-shot 条件**：原始 proposal 仅用 Qwen3-8B 和 GoLLIE-7B。修改为增加 Qwen3-32B fine-tuned（ACE05 + SciERC）和 Qwen3-32B few-shot（无 fine-tune）。GoLLIE 独立为 cross-architecture 比较，不与 scale 混为一谈。RQ3 从 \"scaling curve\" 降级为 \"case study on model capability\"——诚实匹配只有两个 scale point 的现实。 — 命中 Soundness + Feasibility\n\n13. [LAS / Contribution (4)] — **明确训练协议 + 三路 ablation + transfer + feature importance**：原始 proposal 对 LAS 训练数据来源未说明。修改为：(a) 明确用 official dev set 训练、test set 评估（杜绝泄露）；(b) 增加 annotation efficiency sensitivity (50/100/200/500 instances)；(c) ablation: LAS vs. feature-threshold vs. raw consistency score；(d) leave-one-dataset-out transfer 用 paired bootstrap 检验（非 arbitrary 85% threshold）；(e) SHAP/permutation importance 识别 universally transferable vs. task-specific features。 — 命中 Technical Soundness + Reproducibility\n\n14. [泛化声明 / Scope 章节] — **收窄 generality claims 至 IE domain**：原始 proposal 声称 \"the first general-purpose framework for adaptive TTS with structured outputs\" 并列举 SQL/code/clinical/DST 四个额外 domain 作为 contribution。修改为将核心 claim 限定为 IE，SQL/code/clinical/DST 降为 future work 展望，消除 claim-experiment gap。 — 命中 Technical Soundness（消除 overclaiming 风险）\n\n15. [Priority Claims / 全文] — **软化 \"first\" 声明**：原始 proposal 三次使用 \"the first\"。修改为 \"to our knowledge, among the first to...\"，叙事重心从 \"we are first\" 转向 \"the problem is hard because [specific challenges], and we propose [specific solutions]\"。 — 命中 Novelty（降低被 falsify 的风险）\n\n16. [Related Work / 新增三个方向] — **从仅覆盖 adaptive self-consistency 扩展到六个方向**：原始 proposal 仅引用 DSC/Slim-SC/ReASC/CGES/Sonata/STED。修改为增加：(a) classical structured prediction ensemble methods, (b) LLM confidence estimation for structured outputs, (c) test-time augmentation for NLP, (d) TTS for non-scalar generative NLP + code generation structural consistency (CodeT, MBR-based selection), (e) LLM calibration for structured tasks。每个方向明确差异化定位。加深 STED 讨论：STED = evaluation, AS2CS = aggregation + adaptive gating + diagnostic framework。 — 命中 Related Work\n\n17. [统计方案 / Evaluation Metrics] — **增加显著性检验和多 seed 报告**：原始 proposal 未指定统计检验。修改为 paired bootstrap test (n=10000) + 95% CI，3-5 random seeds 的 mean±std，significance threshold \"≥ 2 F1 with p < 0.05\"。 — 命中 Technical Soundness\n\n18. [Significance 底线 / Motivation] — **显式声明何种增益算 meaningful**：原始 proposal 无此声明。修改为 \"≥ 2 F1 points or ≥ 30% cost reduction at equivalent F1\"，展示作者的 self-awareness。 — 命中 Soundness + 评审印象\n\n19. [Paper Organization / 新增段落] — **增加 main vs. appendix 分配策略**：原始 proposal 无此规划，所有实验并列。修改为：正文聚焦 pilot validation 核心结果 + ASCG vs. baselines 主表 + diagnostic heatmap (signature figure) + error taxonomy 分布；所有 ablation 放 appendix；RQ3/RQ4 正文各 1-2 段。缓解 \"tries to do too much\" 的常见 reviewer 批评。 — 命中 Technical Soundness + Presentation\n\n20. [Cost Framing / Introduction + Experiments] — **增加 concrete cost-efficiency metrics**：原始 proposal 用抽象的 \"compute-efficient\" 表述。修改为报告具体的 average samples saved、cost-accuracy Pareto 改进百分比，总 cost 定义包含 LLM sampling + alignment overhead + gating overhead（honest accounting），并报告 wall-clock time breakdown per complexity bin。 — 命中 Significance + Practical Impact\n\n【主要风险】:\n\n1. **Algorithmic novelty 的结构性 ceiling**：即使叙事重构为\"诊断范式\"，ASCG/LAS 的核心技术组件（已有对齐算法 + 标准 MLP + 常规 gating loop）仍然缺乏 algorithmic novelty。如果 1-2 位 reviewer 坚持要 novel algorithm 而非 novel analysis/diagnostic，论文可能被定性为 \"systematic empirical study\" 并被降分。这是结构性限制，无法通过 proposal 优化进一步缓解——只能靠实验结果的 surprising 程度（特别是 phase transition 发现或 dramatic fine-tuning effect）来补偿。\n\n2. **Pilot validation 失败的 pivot 风险**：如果 fine-tuned 模型的 ρ < 0.4 across the board（即结构化 consistency 即使用 alignment-based metrics 也无法作为可靠 confidence proxy），论文必须 pivot 为 negative finding。虽然 dual-outcome 设计使这在学术上是可发表的，但 negative finding 论文的 EMNLP 主会接受概率显著低于 positive finding（估计降至 20-25%），且论文的 primary contribution（diagnostic framework）将失去其 prescriptive value（只剩 descriptive value）。\n\n【实施评估】:\n\n- **计算资源**: 需要至少 1 × A100-80GB（或等价）用于 Qwen3-8B/GoLLIE-7B 的 fine-tuning 和多次采样推理；Qwen3-32B fine-tuning + 推理需要 2-4 × A100-80GB 或 1 × H100。5 个 benchmark × 4 模型配置 × N=8-16 采样 × 多 seed = 大量推理，预估总 GPU 时长 200-400 A100-hours（含 fine-tuning ~50h + 推理 ~150-350h）。如用云平台（AWS/GCP），约 $600-$1200。LLM-as-judge baseline (baseline 7) 如果用 API model 会有额外 API 成本，约 $100-$300。\n- **数据需求**: ACE05、Few-NERD、SciERC、TACREV、WikiEvents 五个 benchmark 均公开可得。ACE05 需要 LDC 许可证（大多数学术机构已有）。UIE 格式的 fine-tuning 数据需要从原始数据集转换，转换脚本已有公开实现。无需构建新数据集。\n- **人工介入**: 不需要人工标注（所有 benchmark 自带 gold annotation）。Error taxonomy 分类完全自动化（基于 gold 对比的操作性定义）。需要研究者人工检查 ~50-100 个 error classification 实例做 sanity check（约 2-4 小时）。LAS feature importance 的 SHAP 分析结果需要研究者解读。整体人工介入量低。\n- **训练需求**: 需要模型训练。(a) Qwen3-8B fine-tuning on UIE tasks（~10-15h on 1×A100）；(b) Qwen3-32B fine-tuning（~20-30h on 2-4×A100）；(c) GoLLIE-7B 可能需要适配训练或直接用预训练版本；(d) LAS MLP 训练极轻（CPU 级别，分钟级）。总训练时长约 30-50 GPU-hours。\n- **新 Benchmark**: 不需要构建新 benchmark。所有评测在已有公开 benchmark 上进行。但需要构建 complexity-binned evaluation splits（按 entity count、relation depth 等分层），这是对现有数据的重新组织而非新建。\n- **预估周期**: 从启动到可投稿约 **8-10 周**。细分：Week 1-2 数据准备 + fine-tuning；Week 2-3 Pilot validation（决定 proceed/pivot）；Week 3-6 主实验（ASCG vs. baselines × 5 benchmarks × 多配置）；Week 5-7 ablation studies + diagnostic heatmap 构建；Week 7-9 写作；Week 9-10 内部 rev\n\n\n## MVP Validation Results\n\n- **Date**: 2026-05-14\n- **Hypothesis Supported**: Yes\n\n### Key Metrics\n\nNER full rho_sj=0.388 (SJ>FK +6.6pp, p=2e-20) | RE full rho_sj=0.234 (FAIL <0.30) | RE cond rho_sj=0.372 (SJ>FK +11.8pp) | RE pct_zero=42.4% | NER oracle headroom=+5.5pp | RE oracle headroom=+13.1pp | Gate 0: NER F1=66.2%, RE F1=42.1%\n\n### Summary\n\nMVP 验证 structural self-consistency 作为 IE test-time scaling 信号。5 轮 pilot 实验（ft_001/ft_002_v2 模型，T=1.0/0.7，N=8，SciERC 551 instances）+ 1 轮度量分解诊断。结果：NER 方向强正向（rho_sj=0.388, SJ>FK p=2e-20）；RE full-set FAIL（rho_sj=0.234<0.30），但 RE conditional set（排除 all-zero knowledge-gap 实例）显示强信号（rho_sj=0.372, SJ>FK 11.8pp）。E1 诊断排除了度量设计问题——RE weakness 是复合错误传播的固有属性。T=0.7 vs T=1.0 对比揭示采样温度对信号质量的影响。假设部分验证：entity-level IE 有效，relation-level 需 capability-aware 分析。\n\n### Recommendation\n\nGO — 进入 research 阶段，走 Narrative A（NER-primary + RE diagnostic）。NER 信号足够强且 SJ>FK 优势一致。RE conditional 分析 + E1 诊断 + 温度敏感性分析为论文增加诊断深度。下一步：E3 (NER N=16 验证 rho 是否过 0.40) + E4 (NER 多数据集泛化 CoNLL/OntoNotes) + RE 诊断整理。目标 ARR May 2026-05-25。\n",
      "numLines": 209,
      "startLine": 1,
      "totalLines": 209
    }
  },
  "sourceToolAssistantUUID": "9b1cfa29-911a-4cff-9887-76b1ce536132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 111_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "403eecdd-6662-44ec-9b2c-2b06e14c68b5",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863"
}
```

---


### Tool call

_source line 112 · 2026-05-31T14:25:32.686Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UmeEWW7muJ2ANSmanJqW3R`</summary>

```json
{
  "command": "# Try a few large session files for paper agent issues\nPA_DIR=$(find /home/ubuntu -maxdepth 4 -type d -name \"*paper-agent*\" 2>/dev/null | head -1)\nls $PA_DIR 2>/dev/null | head -3\necho \"---\"\ndu -sh $PA_DIR/*.jsonl 2>/dev/null | sort -hr | head -5\necho \"---\"\n# Look at the agent session\nls /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-008377ff/*.jsonl 2>/dev/null | head -3\necho \"---worker sessions count---\"\nfind /home/ubuntu -maxdepth 4 -type d -name \"*claude-sessions-*\" 2>/dev/null | grep -v claude-sessions-agent | grep -v claude-sessions-director | grep -v claude-sessions-reviewer | grep -v claude-sessions-paper-agent | sort -u | head -20",
  "description": "Paper agent sessions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403eecdd-6662-44ec-9b2c-2b06e14c68b5",
  "isSidechain": false,
  "requestId": "req_011CbaoNscq3CBJW3Q7oiDcV",
  "type": "assistant",
  "uuid": "7c28db77-21d7-488c-b32c-4d264a9ce3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TwVnBEDdrxWdJ5XfwSXgSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17954,
      "cache_read_input_tokens": 196589,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-31T14:25:32.835Z_

<details><summary>↩ Tool result · `toolu_01UmeEWW7muJ2ANSmanJqW3R`</summary>

```text
mcp-logs-agent-ml-research
---
---
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-008377ff/8639289c-6af0-4e1b-9d67-91a2aa067161.jsonl
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-008377ff/c86c3c87-0403-4ab0-ab23-ec9d1d67c052.jsonl
---worker sessions count---
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-briefer-31089a1d
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-content-aa42d635
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-review-visual-f9bb569d
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-visual-1a48d884
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-figure-optimize-04520750
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-18960d1d
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-1df9a4fe
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-ad2241b1
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-da66ea7e
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-director-46d7d321
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-1-71d0a8e7
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-2-8bebda96
/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-3-b1d4dfb6
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-briefer-31089a1d
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-review-visual-f9bb569d
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b
/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c28db77-21d7-488c-b32c-4d264a9ce3dd",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "e1298813-f02f-4c10-a507-f5ab91572e63",
  "toolUseResult": {
    "stdout": "mcp-logs-agent-ml-research\n---\n---\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-008377ff/8639289c-6af0-4e1b-9d67-91a2aa067161.jsonl\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-agent-008377ff/c86c3c87-0403-4ab0-ab23-ec9d1d67c052.jsonl\n---worker sessions count---\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-briefer-31089a1d\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-content-aa42d635\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-review-visual-f9bb569d\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-visual-1a48d884\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-figure-optimize-04520750\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-18960d1d\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-1df9a4fe\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-ad2241b1\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage--claude-sessions-no-project-da66ea7e\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-director-46d7d321\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-1-71d0a8e7\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-2-8bebda96\n/home/ubuntu/.cache/claude-cli-nodejs/-home-ubuntu--agent-ml-research-norm-free-capacity-triage-projects-norm-free-capacity-triage--claude-sessions-review-reviewer-3-b1d4dfb6\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-briefer-31089a1d\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-paper-audit-review-visual-f9bb569d\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b\n/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-1-68ddc296",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7c28db77-21d7-488c-b32c-4d264a9ce3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-31T14:25:37.879Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015GMrfNsvCYvNicgshqz8gC`</summary>

```json
{
  "command": "# Confirm scan_reports paths and any prior reports\nls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/\necho \"---\"\n# Read the most recent paper findings to confirm final score\ngrep -nE 'R4[0-9].*(3\\.0|3\\.5|borderline|Borderline|fresh|Fresh)' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml | head -20",
  "description": "Locate final review status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1298813-f02f-4c10-a507-f5ab91572e63",
  "isSidechain": false,
  "requestId": "req_011CbaoPhVuCdcQH99cK3tat",
  "type": "assistant",
  "uuid": "1c657bc5-6a1c-4aac-8852-b56cf07187f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014Fkdhk42JeeH1aYAXAw9xM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2388,
      "cache_read_input_tokens": 214543,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-31T14:25:37.932Z_

<details><summary>↩ Tool result · `toolu_015GMrfNsvCYvNicgshqz8gC`</summary>

```text
layer1_20260531T142125.json
---
4321:  rationale: 'R40 Fresh 审稿 3.0 (R1=3.5, R2=3.0)。3 个 SYSTEMIC_ISSUE: framing/novelty、统计脆弱、形式化薄弱。核心负面发现站住脚。Reviewer
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c657bc5-6a1c-4aac-8852-b56cf07187f7",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "62e0cf7f-175a-4fcc-97e8-d826e7457819",
  "toolUseResult": {
    "stdout": "layer1_20260531T142125.json\n---\n4321:  rationale: 'R40 Fresh 审稿 3.0 (R1=3.5, R2=3.0)。3 个 SYSTEMIC_ISSUE: framing/novelty、统计脆弱、形式化薄弱。核心负面发现站住脚。Reviewer",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1c657bc5-6a1c-4aac-8852-b56cf07187f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-31T14:25:41.891Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TgunKkezkck2kAL2c7P82A`</summary>

```json
{
  "command": "# Find sampling of high level decisions (D193 D200 D210 etc.) - skip to verify pretrained breakthrough decision\nsed -n '3000,3300p' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml | head -300",
  "description": "Mid-project decisions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e0cf7f-175a-4fcc-97e8-d826e7457819",
  "isSidechain": false,
  "requestId": "req_011CbaoQ5G6Wa8Kw5i4jiNxK",
  "type": "assistant",
  "uuid": "0c70e14e-2cd0-4965-ab22-62dcc1d2bcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01313ShcUCNBXrUiz39qbogN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 216931,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-31T14:25:41.936Z_

<details><summary>↩ Tool result · `toolu_01TgunKkezkck2kAL2c7P82A`</summary>

```text
    提升到 70-80%，论文从 Findings 级升级到 Main 级。三个实验全 CPU-based 复用已有数据，零 GPU 成本。我们已有 LLaMA
    8B FT 上 VC/SJ-weighted 初步数据（VC best），现在扩展到全部 config。
  related_experiments:
  - exp_id: exp_entity_construction
    role: baseline
    result: LP-weighted works in ~30% configs
  - exp_id: exp_qwen25_72b_fewshot
    role: motivation
    result: FS regime LP ρ=0.06 but VC ρ=0.26-0.43
  depends_on:
  - D165
- id: D168
  date: 2026-05-20 08:52 UTC
  summary: DGEC Layer 1 (Heterogeneous-T) 放弃。Mixed pool 不 robustly 优于 T=1.0 (1/3 seeds
    显著)。DGEC 缩减为 2 层：Signal-Adaptive Weighting + Entity Construction。T=0.7 alone 最优
    (+1.81pp) 挑战 gating rule，作为 appendix 发现保留。
  rationale: Exp C 结果：mixed T=0.7+T=1.0 vs T=1.0 alone Δ=+0.59pp (uniform) / +0.39pp
    (VC)，3 seeds 中仅 1/3 显著。且 mixed pool degen (17.0%) > T=1.0 degen (12.4%)，不降反升。T=0.7
    alone 反而 construction 最强 (+1.81pp, p=0.006) 尽管 degen=22.3% 超阈值，暗示样本质量 > 多样性。DGEC
    核心赌注转到 Exp A/B (VC/SJ weighting)。
  related_experiments:
  - exp_id: exp_dgec_heterogeneous_t
    role: primary
    result: negative — mixed pool not robustly better than T=1.0
  depends_on:
  - D167
- id: D169
  date: 2026-05-20 08:53 UTC
  summary: DGEC Layer 2 SJ-weighted construction 失败 (1/17 显著正, 7/17 显著负)。唯一正向 SciERC
    72B ZS +2.0pp。SJ 不适合作 construction 权重（共识相似度 ≠ 质量信号）。DGEC 核心赌注全在 VC-weighted (Exp
    A)。
  rationale: SJ 衡量 sample 与整体共识的相似度，是 popularity proxy 而非 quality proxy。高 degen 时
    SJ 给错误共识高权重，导致 construction 反而降低。VC 直接衡量 entity-level agreement，与 construction
    操作（entity majority vote）概念对齐，是更合理的权重。Exp B Worker 遗漏 8B Qwen3 FT configs，但 SJ
    整体 pattern 足以否定。
  related_experiments:
  - exp_id: exp_dgec_sj_construction
    role: primary
    result: negative — 1/17 positive, 7/17 negative, 9 n.s.
  depends_on:
  - D167
  - D168
- id: D170
  date: 2026-05-20 09:04 UTC
  summary: 'DGEC "统一方法" 目标不可达。VC-weighted construction 32% (6/19) 成功率，与 LP 25% (3/12)
    仅微弱改善，且 7/19 显著负向。三层干预全部失败或混合。Salvageable: WNUT VC +0.92pp (新发现)、SciERC ZS SJ
    +2.0pp (比 LP 更强)、signal-dataset 交互效应。8B Qwen3 FT configs 仍缺，补测 Worker 已派。'
  rationale: Exp A/B/C 全部结果：Layer 1 Heterogeneous-T 不 robust (1/3 seed sig)；Layer
    2a SJ 1/17 sig+, 7/17 sig-；Layer 2b VC 6/19 sig+, 7/19 sig-。Construction 成功率从
    ~25% 到 ~32%，远不及 70-80% 目标。但用户 18 方向已在并行推进，B1(SCD)、B2(Verifier)、A1(MBR) 等可能提供替代
    prescriptive contribution。
  related_experiments:
  - exp_id: exp_dgec_vc_construction
    role: primary
    result: mixed — 6/19 sig+, 7/19 sig-, net ≈0
  - exp_id: exp_dgec_sj_construction
    role: control
    result: negative
  - exp_id: exp_dgec_heterogeneous_t
    role: control
    result: negative
  depends_on:
  - D167
  - D168
  - D169
- id: D171
  date: 2026-05-20 09:09 UTC
  summary: DGEC 彻底关闭 (D170 确认)。8B Qwen3 FT 补测：VC 劣于 LP (FewNERD +0.40 vs +1.40, SciERC
    +0.57 vs +1.02)，SJ 全面失败。LP-weighted construction 仍是最佳。DGEC 数据作为 appendix signal
    comparison（增强论文诚实度和系统性）。论文叙事回退到 pre-D167 + C1 TTS 升级。
  rationale: VC 在 LP-positive configs 上效果更差且 cross-seed 方差更大 (range 1.21-2.05pp vs
    LP std ~0.25pp)。SJ 在 FewNERD 8B FT -1.48pp (显著负)。三层干预全面失败。但 DGEC 实验数据有 appendix
    价值：系统性 signal comparison (LP/VC/SJ × 19+ configs) 展示方法论严谨性。论文核心叙事回退到诊断框架 + LP
    entity construction as partial mitigation，叠加 C1 TTS 叙事升级。18 方向继续推进，B1(SCD)/B2(Verifier)
    可能提供新的 prescriptive contribution。
  related_experiments:
  - exp_id: exp_dgec_vc_construction
    role: primary
    result: VC worse than LP on LP-positive configs
  - exp_id: exp_dgec_sj_construction
    role: control
    result: SJ broadly negative including 8B FT
  depends_on:
  - D170
- id: D172
  date: 2026-05-20 09:27 UTC
  summary: DGEC 正式关闭：8B Qwen3 FT 补测确认 VC/SJ 均劣于 LP，统一方法不可行。6 空闲 GPU 立即分配给 B1(SCD)
    + B3(Prompted Diversity)
  rationale: VC 补测 28 configs 总体 32% sig+（远低于 70-80% 目标），SJ 26 configs 仅 1 sig+/15
    sig-。即使在 LP-success configs 上 VC 也不一致（seed-dependent），SJ 全面引入噪声。DGEC 作为统一方法路线彻底关闭。6
    张空闲 GPU（5090-b 4卡 + 5090-c:2,3）立即给 B1 SCD（最高优先级方法创新）和 B3 Prompted Diversity。
  related_experiments:
  - exp_id: exp_dgec_vc_construction
    role: evidence
    result: negative
  - exp_id: exp_dgec_sj_construction
    role: evidence
    result: negative
  - exp_id: exp_dgec_heterogeneous_t
    role: evidence
    result: negative
  depends_on:
  - D170
  - D171
- id: D173
  date: 2026-05-20 09:31 UTC
  summary: 新增 E1 Adaptive Signal Routing 方向：用 DGEC 19 configs × 3 signals 数据训练 signal
    router，替代全局固定 LP weighting
  rationale: DGEC 失败的真正含义是"不同 (model, dataset, regime) 下最优信号不同"。19 configs × 3 signals
    = 57 个数据点已证明 signal-dataset 交互效应。Router 预测最优 signal 替代 always-LP，如果 accuracy>60%
    且 ΔF1 显著>LP baseline，这就是论文 prescriptive core。CPU only 1-2h。同时 A1 MBR 形式化提供理论基础：entity
    construction = MBR, weighting = importance sampling, DGEC 失败 = bad importance
    weights → 需要 adaptive selection。
  related_experiments:
  - exp_id: exp_dgec_vc_construction
    role: data_source
    result: negative
  - exp_id: exp_dgec_sj_construction
    role: data_source
    result: negative
  depends_on:
  - D172
- id: D174
  date: 2026-05-20 09:39 UTC
  summary: 新增 E2 Mixture-of-Signals Ensemble + E3 Cross-Model Distillation + F1 Inference
    Scaling Law 三个方向；B1 SCD 升级为 Iterative SCD (Q6/Q7)
  rationale: B5 +0.42pp 证明跨模型多样性是真实机制。E2 ensemble 比 E1 routing 更稳健（不依赖 router accuracy）。E3
    把 B1+B5 结合：跨模型 construction → 蒸馏到单模型，inference cost 不变。F1 Scaling Law 把论文 reposition
    到 inference-time scaling 热点——测 F1 vs N power law，揭示 structured IE 的 SC scaling
    远弱于 reasoning，用 degeneracy 解释。B1 Iterative SCD 测多轮蒸馏收敛行为。
  related_experiments:
  - exp_id: exp_cross_model_consistency
    role: motivation
    result: success
  - exp_id: exp_adaptive_sampling_budget
    role: motivation
    result: success
  depends_on:
  - D173
- id: D175
  date: 2026-05-20 09:49 UTC
  summary: 论文写作工程锁定：Title T2, 8 页预算, 05-22 中午 go/no-go 决策点, Plan B (no SCD) 仍可拿 Main
  rationale: 'T2 "Beyond Single-Signal Self-Consistency: An Inference-Scaling Perspective
    on Structured IE" 选择理由：TTS 是当前最热 framing，"Beyond Single-Signal" 直接点出核心发现（DGEC
    negative → adaptive），且 F1 scaling law 即使 exponent 不够 sharp 也能支撑 "inference-scaling
    perspective" 叙事。如 F1 结果弱则 fallback T1。05-22 中午设 go/no-go：所有 CPU 实验 + B1 R1 应出完，Reviewer
    做 "is this Main-ready?" 评估。Plan B：即使 B1 SCD 失败，B5+B7+E1/E2+A1+A4+F1+DGEC§4 仍够
    Main 4.0。'
  related_experiments: []
  depends_on:
  - D174
- id: D176
  date: 2026-05-20 10:00 UTC
  summary: E1 Adaptive Signal Routing 完成：RF 56% acc, +0.39pp vs LP +0.15pp。定位为诊断性证据而非部署方案——feature
    importance (oracle_headroom > degeneracy > base_f1) 直接验证 regime-dependent thesis
  rationale: E1 在 16 configs 上训练 router 选择最佳 construction method。Router 本身 accuracy
    56%（16 样本 LOO 预期有限），但核心价值在两方面：(1) router beats always-LP 2.6×（+0.39 vs +0.15pp），证明没有
    universal best method；(2) RF feature importance 显示 oracle_headroom、degeneracy_rate、base_f1
    是最强预测器，这正好是我们诊断发现的三个 regime factor，为论文 §5 prescriptive guidance 提供定量支撑。论文中 frame
    为 "A simple meta-learner confirms regime-dependent optimal construction"，不 overclaim
    为 deployable system。
  related_experiments:
  - exp_id: e1_signal_routing
    role: primary
    result: 'mixed-positive: router works but accuracy limited by 16 datapoints'
  depends_on:
  - D172
  - D173
- id: D177
  date: 2026-05-20 10:04 UTC
  summary: 'Reviewer R1-R9 adversarial stress test: 7/9 充分防御, 无 critical。R5 加 Bonferroni
    summary 句, R9 DGEC negatives 入 appendix。E1 routing 确认 appendix-only 定位。'
  rationale: 'Reviewer 模拟 9 个审稿人攻击角度评估论文防御完备性。最关键发现：(1) R5 多重比较——主线 claim 全 survive
    Bonferroni, post-hoc ε 已透明披露, 只需加一句 summary sentence; (2) R9 negative reporting——DGEC
    三层实验全失败尚未写入论文, 需入 appendix 增强诚实度; (3) R4 reproducibility——建议 supplementary 附伪代码(可选);
    (4) E1 routing 单独审查——n=16 统计效力不足, oracle_headroom 非部署可用 feature, 确认 appendix-only
    定位(D176)。整体结论: 论文防御骨架 solid, 两个 minor 增强即可。'
  related_experiments:
  - exp_id: e1_signal_routing
    role: reviewed
    result: appendix-only per D176
  - exp_id: exp_dgec_vc_construction
    role: negative-to-report
    result: DGEC negatives need appendix entry
  - exp_id: exp_dgec_sj_construction
    role: negative-to-report
    result: DGEC negatives need appendix entry
  depends_on:
  - D176
  - D172
- id: D178
  date: 2026-05-20 10:05 UTC
  summary: Response letter 分版策略：v1 仅含已验证 evidence，B1/E2/R8/I 完成后逐步更新 v2→v3→final。不在未完成实验上做
    mitigation claim。
  rationale: Reviewer critical 指出 response letter 映射表有 5 项引用了 registry 中不存在的实验。虽然这些实验全在
    Agent 执行队列中（不是虚构），但 Reviewer 原则正确——不应承诺不可核实的结果。采用分版策略：v1 基于已验证 evidence（B5/B7/A1/A4/construction/Bonferroni/scaling），未完成实验标注
    "in progress" 不作为 claim。每个实验完成注册后更新。E1 routing 确认 appendix-only。
  related_experiments:
  - exp_id: e1_signal_routing
    role: confirmed appendix-only
    result: 56% acc, n=16 insufficient
  - exp_id: exp_cross_model_consistency
    role: verified positive
    result: +0.42pp
  - exp_id: exp_adaptive_sampling_budget
    role: verified positive
    result: 40-50% compute saving
  depends_on:
  - D176
  - D177
- id: D179
  date: 2026-05-20 10:08 UTC
  summary: Main text 8 页聚焦 5 核心贡献，其余 appendix 化。B1 SCD 进 main table 取决于 05-22 结果强度。
  rationale: Reviewer ROADMAP 审查指出 18+ 新方向 vs 8 页论文的膨胀风险。同意。Main text 锁定 5 个故事线：(1)
    Diagnostic gap, (2) Three failure mechanisms, (3) Entity construction + gating,
    (4) Scaling behavior, (5) Honest negatives。E1/E2/I/J/K/L/R8 全部 appendix。B1 SCD
    是唯一可能进 main table 的额外方法——如果 SCD distillation 显著提升 F1，写入 §7 main table "SCD" 列；否则也入
    appendix。这个判断在 05-22 go/no-go 时基于实际数据做。用户设计的 Table 1 五列结构（Greedy/SC-LP/Cross-Model/Adaptive/SCD）作为上限模板，实际列数根据结果确定。
  related_experiments: []
  depends_on:
  - D177
  - D178
- id: D180
  date: 2026-05-20 10:10 UTC
  summary: A1 MBR Proposition 1 proof 修正：F1 utility 改为 set-overlap (精确), 加 Dembczynski
    et al. footnote, "importance-weighted" 改为 "quality-weighted"
  rationale: Reviewer 逐句验证发现 critical 逻辑跳跃：F1 是 non-decomposable metric，proof 中 "decomposes
    into per-entity marginal decisions" 对 F1 不成立。p̂(e)>1/2 阈值对 set-overlap utility
    精确成立，对 F1 仅在 |E_∪|→∞ 极限下近似成立。采用 Method A（最小修改）：(1) utility 改为 set-overlap 使 proof
    精确；(2) footnote 说明 F1 下的近似及 empirical tightness，引用 Dembczynski et al. 2011；(3)
    "importance-weighted" 改为 "quality-weighted" 因为 LP/VC/SJ 不是 density ratio。这个修复实际加分——展示数学严谨性和对
    F-measure optimization 文献的了解。
  related_experiments:
  - exp_id: exp_014_entity_majority_voting
    role: empirical validation of p>1/2 threshold
    result: voting works empirically, confirming approximation is tight
  depends_on:
  - D176
- id: D181
  date: 2026-05-20 10:15 UTC
  summary: E1 routing demote + redesign：砍 oracle_headroom（部署不可用），用 deployment-available
    features 重跑；E2 Mixture 升级为主文 primary adaptive method 候选
  rationale: 用户 Round 7 指出 E1 的 oracle_headroom 是 fatal flaw（需要 ground truth，部署不可用）。三个并行
    action：(1) E1 redesign 只用 deployment-available features (model_size, regime, degeneracy_rate_estimated,
    lp/vc_variance)；(2) E2 Mixture-of-Signals 升级为 §5 primary adaptive method 候选——部署友好（权重固定，无
    routing decision）；(3) 等 14B/32B 增加 configs 到 25+ 作为 backup。§5 决策树：E2 work → primary;
    E1 deployable work → secondary; 都不 work → Cross-Model SC + SCD carry（Plan B）。
  related_experiments:
  - exp_id: e1_signal_routing
    role: demoted, redesign needed
    result: 56% acc but oracle_headroom fatal flaw
  - exp_id: E2_mixture_of_signals
    role: promoted to primary candidate
    result: pending
  depends_on:
  - D176
  - D179
- id: D182
  date: 2026-05-20 10:26 UTC
  summary: 'R5 Bonferroni-Holm: SciERC FT +1.02pp 降级为 exploratory，FewNERD claims 稳健。MBR
    utility 修正为 balanced set-overlap。'
  rationale: 'Holm-Bonferroni 校正(k=57, α=0.05)后仅 8/57 存活，6/8 来自 FewNERD。SciERC N=8
    所有方法 p_adj≥0.20 — response letter "SciERC FT +1.02pp, all p<0.01" 不可保持。FewNERD
    作为 primary evidence，SciERC FT 降为 directionally positive。同时修正 MBR Proposition 1
    utility: 纯 |ŷ∩y''| 的 MBR-optimal 是 include everything，改为 balanced set-overlap
    |ŷ∩y''|-|ŷ\y''| 使 1/2 threshold 精确成立。'
  related_experiments:
  - exp_id: R5_bonferroni_holm
    role: evidence
    result: 8/57 survive, SciERC FT fails
  - exp_id: exp_014_entity_majority_voting
    role: affected
    result: claim strength downgraded for SciERC
  depends_on:
  - D180
  - D178
- id: D183
  date: 2026-05-20 10:34 UTC
  summary: 'E2 Mixture-of-Signals: LP 主导所有 ensemble 权重，SciERC 不显著，construction weighting
    无效。E2 降为 appendix，处方贡献仍以 entity construction + gating 为核心。'
  rationale: E2 grid search ensemble 在 FewNERD 显著(+0.49~1.12pp)但 SciERC 不显著(p>0.29)。LP
    占权重 0.8 across configs，FK/SJ 权重=0。LR 弱于 grid search。Construction weighting 全部
    ≤ uniform。E2 不能作为通用处方方法。但 LP 主导性本身强化诊断论点：只有 LP 有 per-sample 预测力。D181 升级 E2 为 primary
    adaptive 的前提不成立，回退为 appendix 探索。
  related_experiments:
  - exp_id: E2_mixture_of_signals
    role: evidence
    result: FewNERD-specific, LP-dominant, SciERC n.s.
  - exp_id: exp_014_entity_majority_voting
    role: reinforced
    result: uniform MV optimal, weighting adds nothing
  depends_on:
  - D181
- id: D184
  date: 2026-05-20 10:38 UTC
  summary: 'Round 8: 目标升至 Main 4.3+。采纳 N(Inverse Scaling) + P(Impossibility)，调整 E1×1/E2×1，拒绝
    O(Cross-Task)。Paper Agent 开始重构。'
  rationale: 用户要求 agent-speed aggressive push。N 和 P 是 high-value low-cost 方向：N 复用现有数据
    CPU 1-2h，P 纯理论可能是 4.5 级别贡献。E2×3 variants 改为×1(per-regime weights)因为 LP dominance
    是 fundamental limitation。E1×3 改为×1(GB+interactions)因为特征空间薄。拒绝 O Cross-Task 因为
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c70e14e-2cd0-4965-ab22-62dcc1d2bcd5",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "fcbfb7ae-d6b8-4dac-91cf-a0c45b53a9a3",
  "toolUseResult": {
    "stdout": "    提升到 70-80%，论文从 Findings 级升级到 Main 级。三个实验全 CPU-based 复用已有数据，零 GPU 成本。我们已有 LLaMA\n    8B FT 上 VC/SJ-weighted 初步数据（VC best），现在扩展到全部 config。\n  related_experiments:\n  - exp_id: exp_entity_construction\n    role: baseline\n    result: LP-weighted works in ~30% configs\n  - exp_id: exp_qwen25_72b_fewshot\n    role: motivation\n    result: FS regime LP ρ=0.06 but VC ρ=0.26-0.43\n  depends_on:\n  - D165\n- id: D168\n  date: 2026-05-20 08:52 UTC\n  summary: DGEC Layer 1 (Heterogeneous-T) 放弃。Mixed pool 不 robustly 优于 T=1.0 (1/3 seeds\n    显著)。DGEC 缩减为 2 层：Signal-Adaptive Weighting + Entity Construction。T=0.7 alone 最优\n    (+1.81pp) 挑战 gating rule，作为 appendix 发现保留。\n  rationale: Exp C 结果：mixed T=0.7+T=1.0 vs T=1.0 alone Δ=+0.59pp (uniform) / +0.39pp\n    (VC)，3 seeds 中仅 1/3 显著。且 mixed pool degen (17.0%) > T=1.0 degen (12.4%)，不降反升。T=0.7\n    alone 反而 construction 最强 (+1.81pp, p=0.006) 尽管 degen=22.3% 超阈值，暗示样本质量 > 多样性。DGEC\n    核心赌注转到 Exp A/B (VC/SJ weighting)。\n  related_experiments:\n  - exp_id: exp_dgec_heterogeneous_t\n    role: primary\n    result: negative — mixed pool not robustly better than T=1.0\n  depends_on:\n  - D167\n- id: D169\n  date: 2026-05-20 08:53 UTC\n  summary: DGEC Layer 2 SJ-weighted construction 失败 (1/17 显著正, 7/17 显著负)。唯一正向 SciERC\n    72B ZS +2.0pp。SJ 不适合作 construction 权重（共识相似度 ≠ 质量信号）。DGEC 核心赌注全在 VC-weighted (Exp\n    A)。\n  rationale: SJ 衡量 sample 与整体共识的相似度，是 popularity proxy 而非 quality proxy。高 degen 时\n    SJ 给错误共识高权重，导致 construction 反而降低。VC 直接衡量 entity-level agreement，与 construction\n    操作（entity majority vote）概念对齐，是更合理的权重。Exp B Worker 遗漏 8B Qwen3 FT configs，但 SJ\n    整体 pattern 足以否定。\n  related_experiments:\n  - exp_id: exp_dgec_sj_construction\n    role: primary\n    result: negative — 1/17 positive, 7/17 negative, 9 n.s.\n  depends_on:\n  - D167\n  - D168\n- id: D170\n  date: 2026-05-20 09:04 UTC\n  summary: 'DGEC \"统一方法\" 目标不可达。VC-weighted construction 32% (6/19) 成功率，与 LP 25% (3/12)\n    仅微弱改善，且 7/19 显著负向。三层干预全部失败或混合。Salvageable: WNUT VC +0.92pp (新发现)、SciERC ZS SJ\n    +2.0pp (比 LP 更强)、signal-dataset 交互效应。8B Qwen3 FT configs 仍缺，补测 Worker 已派。'\n  rationale: Exp A/B/C 全部结果：Layer 1 Heterogeneous-T 不 robust (1/3 seed sig)；Layer\n    2a SJ 1/17 sig+, 7/17 sig-；Layer 2b VC 6/19 sig+, 7/19 sig-。Construction 成功率从\n    ~25% 到 ~32%，远不及 70-80% 目标。但用户 18 方向已在并行推进，B1(SCD)、B2(Verifier)、A1(MBR) 等可能提供替代\n    prescriptive contribution。\n  related_experiments:\n  - exp_id: exp_dgec_vc_construction\n    role: primary\n    result: mixed — 6/19 sig+, 7/19 sig-, net ≈0\n  - exp_id: exp_dgec_sj_construction\n    role: control\n    result: negative\n  - exp_id: exp_dgec_heterogeneous_t\n    role: control\n    result: negative\n  depends_on:\n  - D167\n  - D168\n  - D169\n- id: D171\n  date: 2026-05-20 09:09 UTC\n  summary: DGEC 彻底关闭 (D170 确认)。8B Qwen3 FT 补测：VC 劣于 LP (FewNERD +0.40 vs +1.40, SciERC\n    +0.57 vs +1.02)，SJ 全面失败。LP-weighted construction 仍是最佳。DGEC 数据作为 appendix signal\n    comparison（增强论文诚实度和系统性）。论文叙事回退到 pre-D167 + C1 TTS 升级。\n  rationale: VC 在 LP-positive configs 上效果更差且 cross-seed 方差更大 (range 1.21-2.05pp vs\n    LP std ~0.25pp)。SJ 在 FewNERD 8B FT -1.48pp (显著负)。三层干预全面失败。但 DGEC 实验数据有 appendix\n    价值：系统性 signal comparison (LP/VC/SJ × 19+ configs) 展示方法论严谨性。论文核心叙事回退到诊断框架 + LP\n    entity construction as partial mitigation，叠加 C1 TTS 叙事升级。18 方向继续推进，B1(SCD)/B2(Verifier)\n    可能提供新的 prescriptive contribution。\n  related_experiments:\n  - exp_id: exp_dgec_vc_construction\n    role: primary\n    result: VC worse than LP on LP-positive configs\n  - exp_id: exp_dgec_sj_construction\n    role: control\n    result: SJ broadly negative including 8B FT\n  depends_on:\n  - D170\n- id: D172\n  date: 2026-05-20 09:27 UTC\n  summary: DGEC 正式关闭：8B Qwen3 FT 补测确认 VC/SJ 均劣于 LP，统一方法不可行。6 空闲 GPU 立即分配给 B1(SCD)\n    + B3(Prompted Diversity)\n  rationale: VC 补测 28 configs 总体 32% sig+（远低于 70-80% 目标），SJ 26 configs 仅 1 sig+/15\n    sig-。即使在 LP-success configs 上 VC 也不一致（seed-dependent），SJ 全面引入噪声。DGEC 作为统一方法路线彻底关闭。6\n    张空闲 GPU（5090-b 4卡 + 5090-c:2,3）立即给 B1 SCD（最高优先级方法创新）和 B3 Prompted Diversity。\n  related_experiments:\n  - exp_id: exp_dgec_vc_construction\n    role: evidence\n    result: negative\n  - exp_id: exp_dgec_sj_construction\n    role: evidence\n    result: negative\n  - exp_id: exp_dgec_heterogeneous_t\n    role: evidence\n    result: negative\n  depends_on:\n  - D170\n  - D171\n- id: D173\n  date: 2026-05-20 09:31 UTC\n  summary: 新增 E1 Adaptive Signal Routing 方向：用 DGEC 19 configs × 3 signals 数据训练 signal\n    router，替代全局固定 LP weighting\n  rationale: DGEC 失败的真正含义是\"不同 (model, dataset, regime) 下最优信号不同\"。19 configs × 3 signals\n    = 57 个数据点已证明 signal-dataset 交互效应。Router 预测最优 signal 替代 always-LP，如果 accuracy>60%\n    且 ΔF1 显著>LP baseline，这就是论文 prescriptive core。CPU only 1-2h。同时 A1 MBR 形式化提供理论基础：entity\n    construction = MBR, weighting = importance sampling, DGEC 失败 = bad importance\n    weights → 需要 adaptive selection。\n  related_experiments:\n  - exp_id: exp_dgec_vc_construction\n    role: data_source\n    result: negative\n  - exp_id: exp_dgec_sj_construction\n    role: data_source\n    result: negative\n  depends_on:\n  - D172\n- id: D174\n  date: 2026-05-20 09:39 UTC\n  summary: 新增 E2 Mixture-of-Signals Ensemble + E3 Cross-Model Distillation + F1 Inference\n    Scaling Law 三个方向；B1 SCD 升级为 Iterative SCD (Q6/Q7)\n  rationale: B5 +0.42pp 证明跨模型多样性是真实机制。E2 ensemble 比 E1 routing 更稳健（不依赖 router accuracy）。E3\n    把 B1+B5 结合：跨模型 construction → 蒸馏到单模型，inference cost 不变。F1 Scaling Law 把论文 reposition\n    到 inference-time scaling 热点——测 F1 vs N power law，揭示 structured IE 的 SC scaling\n    远弱于 reasoning，用 degeneracy 解释。B1 Iterative SCD 测多轮蒸馏收敛行为。\n  related_experiments:\n  - exp_id: exp_cross_model_consistency\n    role: motivation\n    result: success\n  - exp_id: exp_adaptive_sampling_budget\n    role: motivation\n    result: success\n  depends_on:\n  - D173\n- id: D175\n  date: 2026-05-20 09:49 UTC\n  summary: 论文写作工程锁定：Title T2, 8 页预算, 05-22 中午 go/no-go 决策点, Plan B (no SCD) 仍可拿 Main\n  rationale: 'T2 \"Beyond Single-Signal Self-Consistency: An Inference-Scaling Perspective\n    on Structured IE\" 选择理由：TTS 是当前最热 framing，\"Beyond Single-Signal\" 直接点出核心发现（DGEC\n    negative → adaptive），且 F1 scaling law 即使 exponent 不够 sharp 也能支撑 \"inference-scaling\n    perspective\" 叙事。如 F1 结果弱则 fallback T1。05-22 中午设 go/no-go：所有 CPU 实验 + B1 R1 应出完，Reviewer\n    做 \"is this Main-ready?\" 评估。Plan B：即使 B1 SCD 失败，B5+B7+E1/E2+A1+A4+F1+DGEC§4 仍够\n    Main 4.0。'\n  related_experiments: []\n  depends_on:\n  - D174\n- id: D176\n  date: 2026-05-20 10:00 UTC\n  summary: E1 Adaptive Signal Routing 完成：RF 56% acc, +0.39pp vs LP +0.15pp。定位为诊断性证据而非部署方案——feature\n    importance (oracle_headroom > degeneracy > base_f1) 直接验证 regime-dependent thesis\n  rationale: E1 在 16 configs 上训练 router 选择最佳 construction method。Router 本身 accuracy\n    56%（16 样本 LOO 预期有限），但核心价值在两方面：(1) router beats always-LP 2.6×（+0.39 vs +0.15pp），证明没有\n    universal best method；(2) RF feature importance 显示 oracle_headroom、degeneracy_rate、base_f1\n    是最强预测器，这正好是我们诊断发现的三个 regime factor，为论文 §5 prescriptive guidance 提供定量支撑。论文中 frame\n    为 \"A simple meta-learner confirms regime-dependent optimal construction\"，不 overclaim\n    为 deployable system。\n  related_experiments:\n  - exp_id: e1_signal_routing\n    role: primary\n    result: 'mixed-positive: router works but accuracy limited by 16 datapoints'\n  depends_on:\n  - D172\n  - D173\n- id: D177\n  date: 2026-05-20 10:04 UTC\n  summary: 'Reviewer R1-R9 adversarial stress test: 7/9 充分防御, 无 critical。R5 加 Bonferroni\n    summary 句, R9 DGEC negatives 入 appendix。E1 routing 确认 appendix-only 定位。'\n  rationale: 'Reviewer 模拟 9 个审稿人攻击角度评估论文防御完备性。最关键发现：(1) R5 多重比较——主线 claim 全 survive\n    Bonferroni, post-hoc ε 已透明披露, 只需加一句 summary sentence; (2) R9 negative reporting——DGEC\n    三层实验全失败尚未写入论文, 需入 appendix 增强诚实度; (3) R4 reproducibility——建议 supplementary 附伪代码(可选);\n    (4) E1 routing 单独审查——n=16 统计效力不足, oracle_headroom 非部署可用 feature, 确认 appendix-only\n    定位(D176)。整体结论: 论文防御骨架 solid, 两个 minor 增强即可。'\n  related_experiments:\n  - exp_id: e1_signal_routing\n    role: reviewed\n    result: appendix-only per D176\n  - exp_id: exp_dgec_vc_construction\n    role: negative-to-report\n    result: DGEC negatives need appendix entry\n  - exp_id: exp_dgec_sj_construction\n    role: negative-to-report\n    result: DGEC negatives need appendix entry\n  depends_on:\n  - D176\n  - D172\n- id: D178\n  date: 2026-05-20 10:05 UTC\n  summary: Response letter 分版策略：v1 仅含已验证 evidence，B1/E2/R8/I 完成后逐步更新 v2→v3→final。不在未完成实验上做\n    mitigation claim。\n  rationale: Reviewer critical 指出 response letter 映射表有 5 项引用了 registry 中不存在的实验。虽然这些实验全在\n    Agent 执行队列中（不是虚构），但 Reviewer 原则正确——不应承诺不可核实的结果。采用分版策略：v1 基于已验证 evidence（B5/B7/A1/A4/construction/Bonferroni/scaling），未完成实验标注\n    \"in progress\" 不作为 claim。每个实验完成注册后更新。E1 routing 确认 appendix-only。\n  related_experiments:\n  - exp_id: e1_signal_routing\n    role: confirmed appendix-only\n    result: 56% acc, n=16 insufficient\n  - exp_id: exp_cross_model_consistency\n    role: verified positive\n    result: +0.42pp\n  - exp_id: exp_adaptive_sampling_budget\n    role: verified positive\n    result: 40-50% compute saving\n  depends_on:\n  - D176\n  - D177\n- id: D179\n  date: 2026-05-20 10:08 UTC\n  summary: Main text 8 页聚焦 5 核心贡献，其余 appendix 化。B1 SCD 进 main table 取决于 05-22 结果强度。\n  rationale: Reviewer ROADMAP 审查指出 18+ 新方向 vs 8 页论文的膨胀风险。同意。Main text 锁定 5 个故事线：(1)\n    Diagnostic gap, (2) Three failure mechanisms, (3) Entity construction + gating,\n    (4) Scaling behavior, (5) Honest negatives。E1/E2/I/J/K/L/R8 全部 appendix。B1 SCD\n    是唯一可能进 main table 的额外方法——如果 SCD distillation 显著提升 F1，写入 §7 main table \"SCD\" 列；否则也入\n    appendix。这个判断在 05-22 go/no-go 时基于实际数据做。用户设计的 Table 1 五列结构（Greedy/SC-LP/Cross-Model/Adaptive/SCD）作为上限模板，实际列数根据结果确定。\n  related_experiments: []\n  depends_on:\n  - D177\n  - D178\n- id: D180\n  date: 2026-05-20 10:10 UTC\n  summary: A1 MBR Proposition 1 proof 修正：F1 utility 改为 set-overlap (精确), 加 Dembczynski\n    et al. footnote, \"importance-weighted\" 改为 \"quality-weighted\"\n  rationale: Reviewer 逐句验证发现 critical 逻辑跳跃：F1 是 non-decomposable metric，proof 中 \"decomposes\n    into per-entity marginal decisions\" 对 F1 不成立。p̂(e)>1/2 阈值对 set-overlap utility\n    精确成立，对 F1 仅在 |E_∪|→∞ 极限下近似成立。采用 Method A（最小修改）：(1) utility 改为 set-overlap 使 proof\n    精确；(2) footnote 说明 F1 下的近似及 empirical tightness，引用 Dembczynski et al. 2011；(3)\n    \"importance-weighted\" 改为 \"quality-weighted\" 因为 LP/VC/SJ 不是 density ratio。这个修复实际加分——展示数学严谨性和对\n    F-measure optimization 文献的了解。\n  related_experiments:\n  - exp_id: exp_014_entity_majority_voting\n    role: empirical validation of p>1/2 threshold\n    result: voting works empirically, confirming approximation is tight\n  depends_on:\n  - D176\n- id: D181\n  date: 2026-05-20 10:15 UTC\n  summary: E1 routing demote + redesign：砍 oracle_headroom（部署不可用），用 deployment-available\n    features 重跑；E2 Mixture 升级为主文 primary adaptive method 候选\n  rationale: 用户 Round 7 指出 E1 的 oracle_headroom 是 fatal flaw（需要 ground truth，部署不可用）。三个并行\n    action：(1) E1 redesign 只用 deployment-available features (model_size, regime, degeneracy_rate_estimated,\n    lp/vc_variance)；(2) E2 Mixture-of-Signals 升级为 §5 primary adaptive method 候选——部署友好（权重固定，无\n    routing decision）；(3) 等 14B/32B 增加 configs 到 25+ 作为 backup。§5 决策树：E2 work → primary;\n    E1 deployable work → secondary; 都不 work → Cross-Model SC + SCD carry（Plan B）。\n  related_experiments:\n  - exp_id: e1_signal_routing\n    role: demoted, redesign needed\n    result: 56% acc but oracle_headroom fatal flaw\n  - exp_id: E2_mixture_of_signals\n    role: promoted to primary candidate\n    result: pending\n  depends_on:\n  - D176\n  - D179\n- id: D182\n  date: 2026-05-20 10:26 UTC\n  summary: 'R5 Bonferroni-Holm: SciERC FT +1.02pp 降级为 exploratory，FewNERD claims 稳健。MBR\n    utility 修正为 balanced set-overlap。'\n  rationale: 'Holm-Bonferroni 校正(k=57, α=0.05)后仅 8/57 存活，6/8 来自 FewNERD。SciERC N=8\n    所有方法 p_adj≥0.20 — response letter \"SciERC FT +1.02pp, all p<0.01\" 不可保持。FewNERD\n    作为 primary evidence，SciERC FT 降为 directionally positive。同时修正 MBR Proposition 1\n    utility: 纯 |ŷ∩y''| 的 MBR-optimal 是 include everything，改为 balanced set-overlap\n    |ŷ∩y''|-|ŷ\\y''| 使 1/2 threshold 精确成立。'\n  related_experiments:\n  - exp_id: R5_bonferroni_holm\n    role: evidence\n    result: 8/57 survive, SciERC FT fails\n  - exp_id: exp_014_entity_majority_voting\n    role: affected\n    result: claim strength downgraded for SciERC\n  depends_on:\n  - D180\n  - D178\n- id: D183\n  date: 2026-05-20 10:34 UTC\n  summary: 'E2 Mixture-of-Signals: LP 主导所有 ensemble 权重，SciERC 不显著，construction weighting\n    无效。E2 降为 appendix，处方贡献仍以 entity construction + gating 为核心。'\n  rationale: E2 grid search ensemble 在 FewNERD 显著(+0.49~1.12pp)但 SciERC 不显著(p>0.29)。LP\n    占权重 0.8 across configs，FK/SJ 权重=0。LR 弱于 grid search。Construction weighting 全部\n    ≤ uniform。E2 不能作为通用处方方法。但 LP 主导性本身强化诊断论点：只有 LP 有 per-sample 预测力。D181 升级 E2 为 primary\n    adaptive 的前提不成立，回退为 appendix 探索。\n  related_experiments:\n  - exp_id: E2_mixture_of_signals\n    role: evidence\n    result: FewNERD-specific, LP-dominant, SciERC n.s.\n  - exp_id: exp_014_entity_majority_voting\n    role: reinforced\n    result: uniform MV optimal, weighting adds nothing\n  depends_on:\n  - D181\n- id: D184\n  date: 2026-05-20 10:38 UTC\n  summary: 'Round 8: 目标升至 Main 4.3+。采纳 N(Inverse Scaling) + P(Impossibility)，调整 E1×1/E2×1，拒绝\n    O(Cross-Task)。Paper Agent 开始重构。'\n  rationale: 用户要求 agent-speed aggressive push。N 和 P 是 high-value low-cost 方向：N 复用现有数据\n    CPU 1-2h，P 纯理论可能是 4.5 级别贡献。E2×3 variants 改为×1(per-regime weights)因为 LP dominance\n    是 fundamental limitation。E1×3 改为×1(GB+interactions)因为特征空间薄。拒绝 O Cross-Task 因为",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0c70e14e-2cd0-4965-ab22-62dcc1d2bcd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 118_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "fcbfb7ae-d6b8-4dac-91cf-a0c45b53a9a3",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863"
}
```

---


### Assistant

_source line 119 · 2026-05-31T14:25:45.755Z_

I have enough. Let me also examine a worker mistake quickly and check what kinds of mistakes were highest cost.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcbfb7ae-d6b8-4dac-91cf-a0c45b53a9a3",
  "isSidechain": false,
  "requestId": "req_011CbaoQNPUmvKo6eF4ZCfrs",
  "type": "assistant",
  "uuid": "077f6012-dc22-4cf5-ad7a-3d9aabea2535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011RmBoFZSvbJfjgQjJHAnan",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8066,
      "cache_read_input_tokens": 217339,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool call

_source line 120 · 2026-05-31T14:25:49.452Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TZF1Lg9uDNWHyo788Gjx1M`</summary>

```json
{
  "command": "# Pull the last 30 decisions to confirm trajectory\nsed -n '4400,4415p' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\necho \"---\"\n# Final R41 score summary\ngrep -nE 'R41|R42|R43|R44|R45' /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml | head -20",
  "description": "Confirm tail decisions and final review rounds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "077f6012-dc22-4cf5-ad7a-3d9aabea2535",
  "isSidechain": false,
  "requestId": "req_011CbaoQNPUmvKo6eF4ZCfrs",
  "type": "assistant",
  "uuid": "c1d90a65-f2cb-44f9-91dc-3632d6c2bcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011RmBoFZSvbJfjgQjJHAnan",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8066,
      "cache_read_input_tokens": 217339,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-31T14:25:49.531Z_

<details><summary>↩ Tool result · `toolu_01TZF1Lg9uDNWHyo788Gjx1M`</summary>

```text
  summary: 确认 SciERC +0.32pp metric 自洽（entity-type-averaged macro-F1），R45 回退正确，论文冻结提交
  rationale: tab:entity_construction caption 标注 Δ macro F1，SciERC greedy=.667 精确匹配
    entity-type-averaged macro-F1。R45 的 +1.11pp 用错了 instance-averaged（greedy=.6467）。当前论文内部一致，DDL
    前不改。5-seed entity-type-averaged 重算留作 rebuttal 储备。
  related_experiments: []
  depends_on:
  - D246
- id: D248
  date: 2026-05-24 09:13 UTC
  summary: Reviewer critical 降级为 info：micro-F1 不是 construction 的论文 metric，论文内部自洽
  rationale: Reviewer 错误认为 micro-F1 是论文 construction 的 metric。实际 tab:entity_construction
    使用 entity-type-averaged macro-F1（caption 标注 Δ macro F1，greedy=.667 精确匹配）。Construction
    在该 metric 下为正。micro-F1 结果留作 rebuttal 准备。
  related_experiments: []
  depends_on:
  - D247
---
4356:  summary: 研究确认收敛，不追加主要实验；等 pretrained N16/N32 完成后提交 R41
4392:  summary: R45 回退完成，冻结论文内容，DDL 前不追查 SciERC +0.32pp metric 一致性
4400:  summary: 确认 SciERC +0.32pp metric 自洽（entity-type-averaged macro-F1），R45 回退正确，论文冻结提交
4402:    entity-type-averaged macro-F1。R45 的 +1.11pp 用错了 instance-averaged（greedy=.6467）。当前论文内部一致，DDL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1d90a65-f2cb-44f9-91dc-3632d6c2bcc5",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "450613b1-77f7-42fb-a57c-ff17ba138234",
  "toolUseResult": {
    "stdout": "  summary: 确认 SciERC +0.32pp metric 自洽（entity-type-averaged macro-F1），R45 回退正确，论文冻结提交\n  rationale: tab:entity_construction caption 标注 Δ macro F1，SciERC greedy=.667 精确匹配\n    entity-type-averaged macro-F1。R45 的 +1.11pp 用错了 instance-averaged（greedy=.6467）。当前论文内部一致，DDL\n    前不改。5-seed entity-type-averaged 重算留作 rebuttal 储备。\n  related_experiments: []\n  depends_on:\n  - D246\n- id: D248\n  date: 2026-05-24 09:13 UTC\n  summary: Reviewer critical 降级为 info：micro-F1 不是 construction 的论文 metric，论文内部自洽\n  rationale: Reviewer 错误认为 micro-F1 是论文 construction 的 metric。实际 tab:entity_construction\n    使用 entity-type-averaged macro-F1（caption 标注 Δ macro F1，greedy=.667 精确匹配）。Construction\n    在该 metric 下为正。micro-F1 结果留作 rebuttal 准备。\n  related_experiments: []\n  depends_on:\n  - D247\n---\n4356:  summary: 研究确认收敛，不追加主要实验；等 pretrained N16/N32 完成后提交 R41\n4392:  summary: R45 回退完成，冻结论文内容，DDL 前不追查 SciERC +0.32pp metric 一致性\n4400:  summary: 确认 SciERC +0.32pp metric 自洽（entity-type-averaged macro-F1），R45 回退正确，论文冻结提交\n4402:    entity-type-averaged macro-F1。R45 的 +1.11pp 用错了 instance-averaged（greedy=.6467）。当前论文内部一致，DDL",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c1d90a65-f2cb-44f9-91dc-3632d6c2bcc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 122 · 2026-05-31T14:25:52.040Z_

Now I have comprehensive evidence. Let me write the final report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "450613b1-77f7-42fb-a57c-ff17ba138234",
  "isSidechain": false,
  "requestId": "req_011CbaoQvyYjqnatgvjZa3bg",
  "type": "assistant",
  "uuid": "cf9cf75f-3b3e-4ad9-b2e8-de86b4282dbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mm4nVKN2HVXkHTVwzr7Y8L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 225405,
      "output_tokens": 17507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool call

_source line 123 · 2026-05-31T14:31:18.210Z_

<details open><summary>🔧 Tool call — Write · `toolu_01R5a7yRUzzh8VeBaPF7CR1b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
  "content": "# struct_self_consist_ie — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:54Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0514_1\n\n## 1. 项目概况\n\n- **目标 venue**: EMNLP 2026 Main（via ARR May），DDL 2026-05-25\n- **生命周期**: 2026-05-14 04:20 → 2026-05-25 ~19:00（约 11 天）\n- **最终标题**: *\"When Does Test-Time Scaling Help Structured Prediction?\"* → 改为 \"**When Self-Consistency Fails for NER**\"（D239/D240，从 \"Structured IE\" 收窄到 NER）\n- **实验规模**: 312 个 DONE 实验（成功 207 / 负向 55 / 杀掉 51 / 失败 15），17 个 PREPARING 未启动；平均 retry 仅 0.055，最大 1（registry 上看似干净，下文揭示这是**虚假干净**）\n- **角色 token 消耗**: agent 34.4M output、reviewer 38.0M output、paper_agent 28.3M output、director 25.1M output、worker 计 ~126K turns；累计 ~183M tokens\n- **session 数**: 2271，总 turns 383,079，errors 2,199\n- **论文产出**: main.tex 编译通过，46 页（≤8 页正文），62 references，匿名 repo 已 push\n- **最终 fresh 审稿评分**: R40 = 3.0（R1=3.5, R2=3.0），R41 提交后处于\"待审\"状态——**未达到 Main Conference 阈值（4.0）也未达到 Findings 阈值（3.5+）**，仅达到 Borderline Findings（2.5）到 Borderline Conference（3.5）区间，未达到用户在 D219 设定的 4.5 目标，也未达到 D225 校准的 3.5–4.0 目标\n- **决策密度**: 248 条 D 决策（前 8 天 195 条，DDL eve 5 条），平均 ~22.5 条/天，5-14 单日 61 条\n- **错题本**: 70 条 mistakes，46/70 high severity；以 code_bug (26) 和 agent_behavior (15) 为主\n\n## 2. 项目叙事重建\n\n### 阶段 A（5/14，第 1 天）：MVP 反复试错与第一次基础叙事建立（D001–D061）\n- 4:23 UTC 设定原始假设：fine-tuned 模型 + soft Jaccard（SJ）能让 IE 一致性-准确率相关性 ρ≥0.40，显著超过 PMC12888769 的 Fleiss' Kappa (FK) 基线\n- 当天连发 61 条 D 决策（项目历史最高）：换数据集（ACE05 LDC 受限 → SciERC RE，D003）、Gate 0 NER 通过/RE FAIL、加 temperature ablation、加 4 个 baseline (log-prob/EM/voting/SJ)、补 N=16\n- **第一次 pivot（D018, 12:27）**: exp_016 发现 best-of-N selection 在 NER 上**全部不如 greedy**——核心 sales pitch \"TTS improves IE\" 死掉。Director 当机立断把叙事从 \"TTS improvement\" 改为 \"correlation-selection gap analysis\"\n\n### 阶段 B（5/15–5/17）：Dream 反复打脸 + reframe 循环（D062–D108）\n- 共 10 次 Dream，前 4 次三档全 3/6（Weak Reject），原因稳定指向 novelty/positioning/related work\n- D011（5/14 10:52）已诊断：\"只对比 FK 一个弱 baseline\" 是 #1 问题，补 log-prob/voting/EM\n- 5/15 加入 free-form decoding ablation (exp-018)，叙事第二次升级到 \"constrained decoding bottleneck\"\n- 5/16 加入 Few-NERD 第三数据集 + 3rd seed + LoRA rank ablation，叙事第三次升级到 \"capability trap + two failure mechanisms\"\n- 5/14 周俊伟（外部用户）首次远程介入：\"重新 dream 一次，我看你之前 dream 的记录都没有达标啊\"——这是项目第一次人工干预，结果是 Director **再启动一次 dream（dream_20260514T203201），仍未达标**\n\n### 阶段 C（5/18，中期转折，第 5 天）：用户强 mandate + GPU 扩容 + 方法论狂飙（D125–D162）\n- 5/18 05:52 曹晓玉（PI）介入：\"纯诊断性质缺乏 positive contribution的问题有解决吗\"\n- 5/18 09:51 PI 进一步：\"你有四张卡，还有好多天才DDL，不要这么短视，实验都提前准备…大胆想\"\n- 5/18 15:18 PI 严厉训话：\"三张空卡为什么不提前准备…论文定位是 diagnostic也太弱了…我要中主会…赶紧干吧\"\n- 5/18 15:44 PI 加注 GPU：\"再给你八卡 RTX 5090\"，资源从 4 → 12 张 5090\n- **后果**：当天 26 条 mistakes（仅次于 5/20 的 21 + 5/19 的 11），是项目错误密度最高的阶段——Worker 大规模并行 + 跨服务器分流引入大量 wrong-model-data、wrong-server、stale-baseline、unicode bug 等\n- D130 全文 \"systemic reframe\"：8 项统计 softening + 4 项贡献重构\n\n### 阶段 D（5/19–5/20，方法论疯狂搜索期，第 6–7 天）：所有 entity-level method 全 negative（D163–D202）\n- 用户 5/20 18:12 给 \"无条件 4.5 mandate\"：D219 把目标从 3.5–4.0 直接抬到 4.5（Consider for Award，约 top 2.5%）\n- **2 天内试了 ≥ 8 个 method**：MRSC（multi-round SC, -2.94pp）、LSC（latent SC, -2.5pp）、ESJ（entity self-judgment, AUROC=0.51 ≈ chance）、E_θ verifier、B1 SCD（self-consistent decoding）、B2 entity verifier（+3.62pp 后发现 train-on-test 数据泄漏 M036）、B3 prompted diversity、DGEC heterogeneous-T/SJ/VC weighting\n- **全 negative**。Director 5/20 把 4 个 negative 重组为 \"unified narrative: lack entity-level self-judgment ability + MV is the only valid signal\"\n- 9/15 high-severity mistakes 在此期间发生（M030 wrong-model-data，M033 wrong baseline，M037/M038 VLLM server-without-client 3 次复发，M046 SCD +3.84pp 是 metric artifact）\n- **5/21 02:16 D211 Hidden-state probe 一度看似 救场**：AUROC 0.92 >> ESJ 0.51——但 12 小时内被 Reviewer 拆穿是 entity-level StratifiedKFold instance 泄漏（M051），GroupKFold 重做后 2/3 数据集 < MV（D215）\n\n### 阶段 E（5/21–5/22，framing 翻烧饼期，第 8–9 天）：D219–D243\n- N-scaling 数据 (N=8/16/32/64) 陆续齐全后，framing 在 48 小时内**翻烧饼三次**：\n  - **D235 (5/22 04:13)**: \"MV works too slowly; LP-best dominates at all budgets\"\n  - **D236 (5/22 05:42)**: \"MV gains are marginal and cost-prohibitive; LP-best dominates at every budget point\"\n  - **D237 (5/22 06:29，D236 作废)**: \"**dataset-dependent** optimal strategy + diagnostic framework as primary\"\n  - **D238 (5/22 09:23)**: 升级到 \"**boundary conditions for TTS in structured prediction**\" + 标题改为 \"When Does Test-Time Scaling Fail?\"\n  - **D239 (5/22 10:38)**: R35 fresh review 给 3.5，要求 \"标题收窄为 NER\"——D238 升级被推翻\n  - **D240 (5/22 11:19)**: R36 fresh 给 3.0（比 R35 还低），\"IE\" 仍被判 overclaim，最终回到 **\"When Self-Consistency Fails for NER\"**\n- 5/22 10:30 用户问：\"这个问题（scope overclaim）出现很多遍了，怎么回事，一直没解决吗\"——表达明显不满\n- 5/22 10:42 用户：\"仔细反思每一次审稿，有重大升级和导致一直卡住的时刻\"\n\n### 阶段 F（5/23–5/24，收口期，第 10–11 天）：D243–D248\n- D243（5/22 20:53）：\"研究确认收敛，不追加主要实验\"\n- D244（5/24 02:32）：\"DDL eve 不启动新实验，4×5090 保留给 rebuttal\"——24 小时前用户还在催\"该补补，质量优先\"，但收尾时 Director 选择保守\n- 5/23–5/24 出现 M068（Worker 将 global k=57 Holm p=0.055 全局替换为 seed-replication p=0.013，混淆统计框架，影响 12+ 处）+ M069（主表 SciERC EM AUROC 复制错误，9.1σ 偏差）+ M070（5-seed construction +1.11pp 是 metric 不一致产物）——**临提交前论文数字最为不稳**\n- 5/23 12:36 周俊伟：\"论文图太少…Figure 1 必须用 PaperBanana 重画，不要有廉价感\"——发起 4 轮 figure 反复\n- 5/24 09:13 D248 把 Reviewer critical 降级为 info：micro-F1 不是 construction 的 metric——一个临门一脚的争议未必正确解决，留作 rebuttal\n\n**关键转折点小结**：D018 (NER best-of-N 失败) → D130 (systemic reframe) → D219 (4.5 mandate) → D238 (TTS boundary 升级) → D240 (回退 NER) → D243 (收敛冻结)。**前 4 个转折都是 Director 自主，后 2 个完全由 fresh reviewer + 用户压力 forcing**。\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n\n| 维度 | 原始 IDEA_BRIEF (5/14) | 最终论文 (5/24) |\n|------|---------------------|----------------|\n| 核心方法 | Adaptive Structural Self-Consistency Scaling (AS2CS) + Learned Aggregation Scorer (LAS) | **方法部分被淡化为 ablation**；论文实际叙事是 \"诊断框架 + correlation-selection gap\" |\n| 假设 | structural consistency + adaptive gating → TTS for IE 可行 | TTS 在 NER 上几乎全负向，agreement 信号有相关性但无 selection 能力 |\n| 范围 | 5 datasets × 多个 IE 任务（NER/RE/EE）+ general framework for structured prediction | **3 NER 数据集**（SciERC/CoNLL/FewNERD），RE/SQL 降级为 exploratory |\n| Contribution 数 | 4 项（ASCG/LAS/error taxonomy/headroom analysis） | 3 项（QE Framework / Diagnostic Cascade / Entity-level construction），全部 reframe |\n| 标题命题 | \"When does TTS help structured prediction?\" | \"When does TTS fail for NER?\" — **命题翻转、范围收窄一个数量级** |\n\n**Reframe 次数**: paper_framing.md 显式经历 ≥5 次 framing 升级/降级（D018→D130→D219→D237→D238→D239→D240），最终回到 5/15 早期的 \"NER + correlation-selection gap\" 叙事，绕了一大圈。\n\n**判定**：最终 findings **没有回答最初的核心问题**（\"when does AS2CS help\"），而是给出了一个相反方向的、范围窄得多的 finding（\"on NER, TTS mostly doesn't help, but here's why\"）。从科研价值看，这种偏离**合理但代价巨大**——更合理的做法是早期（D018 时）就承认\"方法不 work, 转向诊断\"，而不是在 D170 (5/20 09:04) 才正式宣告 \"DGEC 三层干预全部失败\"，期间又试 ≥8 个 method 全 fail。\n\n### 3.2 实验设计的科研严谨性\n\n- **Falsifiability**: ✅ 5/14 MVP 就有 ρ≥0.40 PASS/<0.30 FAIL 阈值，多个 gate 设计了反向条件。\n- **Baseline 充分性**: ⚠️ 初始仅对比 FK 一个弱 baseline（Dream 1 三档全 3/6 的 #1 反馈），D012 后补足 log-prob/EM/voting，**事后补救**。\n- **统计方法**: ⚠️ Bootstrap CI 使用一致，但全文 57 个统计检验仅 8/57 survive Holm-Bonferroni (D182)。M068 显示 Worker 全文混淆两个统计框架。Reviewer 多次警告 p-hacking 风险（D241 N2: \"跑 2 additional seeds 而非切 BH FDR——avoid p-hacking\"）。\n- **实验规模**: 3 seeds（部分实验仅 1 seed），3 NER 数据集，2 模型规模（8B/14B/32B/72B 但后两者非 fine-tune，存在 confound D217）。\n- **数据完整性事故**: M036 train-on-test 数据泄漏 +3.62pp 写入论文后才被 Reviewer 发现；M051 hidden-state probe entity-level CV 泄漏导致 AUROC 从 0.92 跌到 0.65；M016 unified_metrics 迁移后 LP global ρ 从 0.42 降到 0.22（50% 降幅）。这三起任一件都可能引发审稿 desk reject 级别的质疑。\n\n### 3.3 Findings 的质量与 Novelty\n\n- **核心 finding（最终版）**: \"Self-consistency 在 NER 上失败的诊断框架：degeneracy + LP-F1 alignment + LP compression 三因子级联预测 dataset-dependent 最优策略\"\n- **Novelty**: ⚠️ Reviewer 反复指出与 Yao et al. 2026 (task-level correlation)、Yun et al. 2025 (reasoning SC)、Nédellec & Xia 2026 (surface matching) 的差异是 **incremental**——entity-level vs task-level、structural vs surface、mechanistic vs descriptive\n- **审稿历史**:\n  - R8 (Round 8): R1=3.5, R2=2.5 → 平均 3.0 (5/16)\n  - R24: 3.25 (5/19)\n  - R25: 3.5/3.5 (5/19)\n  - R27: 3.0 Findings (5/21)\n  - R35: 3.5 Borderline Conference (5/22)\n  - R36: 3.0 Findings (5/22, 较 R35 下降 0.5)\n  - R40: **R1=3.5, R2=3.0** = avg 3.25 (5/22)\n  - R41/R42/R43 (continue+verify+fresh): R43 = **3.0 Findings**（5/23 04:08 用户已表达不满）\n- **最终评分**: 论文在 fresh 审稿下持续在 **3.0–3.5 之间震荡 11 个 round**，未稳定突破 3.5。**未达到 Main Conference（4.0）门槛**，仅勉强达到 Findings（3.0）。\n- **包装 vs 内容**: 包装上**过度优化**——Figure 1 重画 4 轮、claim-evidence 反复对账、24 轮 paper-audit-review-visual session。但内容上**核心负面结果**是 robust 的。从最终 3.0 评分看，**论文质量与评分匹配**——problems are real, contributions are honest but marginal。\n\n### 3.4 研究效率\n\n- **直接贡献最终论文的实验**: 估算 ~70-80 个（NER 3 dataset × N-scaling × seed × ablation）\n- **探索性弯路**: 8 个 method 全 negative（MRSC/LSC/ESJ/E_θ/B1 SCD/B2 verifier/B3 prompted diversity/DGEC 三层），cross-task universality（A1 Spider SQL + A2 HumanEval）也未进正文\n- **Negative results 的价值**: 部分进入 §6/appendix（DGEC negatives、ESJ AUROC=0.51、hidden-state probe complexity-dependent），但**未成为论文核心 selling point**——这些 negative 的 reframing 工作量极大，与产出价值不匹配\n- **从 idea 到可投稿**: 11 天，**严格意义上的 4 天有效 ddl sprint 起码有 2 天浪费在 method 探索**（5/19–5/20）。如果项目 5/18 用户介入前就接受 \"diagnostic-only\" 定位，可能省下 2 天用于深化分析\n\n### 3.5 论文与实际科研的匹配度\n\n- **总体如实**：核心 negative finding (TTS 在 NER 上失败) 真实存在\n- **过度包装风险**:\n  - QE Framework \"AUROC up to 0.82, ρ up to 0.45\"——R45 cycle 发现 M069 主表 SciERC EM AUROC 是 9.1σ 异常（.749 vs 多 seed mean .631），论文 freeze 时**仍未确认是否修正**\n  - \"Entity-level construction +1.02-1.53pp where headroom allows\"——M036/M070 显示这些数字至少经历了 train-on-test leak 和 metric 不一致两次重大修订\n  - \"5 confidence signals across 4 families systematic comparison\"——R36 reviewer 仍认为 incremental over Yao et al.\n- **被省略的 negative**: 8 个失败 method 中只有 DGEC 和 ESJ 进了 appendix；MRSC/LSC/E_θ/B1 SCD/B2 verifier/B3 prompted diversity 完全未提\n- **Claim/evidence 匹配**: M067 是关键警示——\"LP-best +8pp on Few-NERD\" 写入论文但**无任何实验支撑**，纯属拼凑\n\n### 3.6 人工参与分析\n\n**触发条件**:\n1. 主动催促（用户每日 1-3 次主动飞书）\n2. ESCALATED_TO_HUMAN 事件（agent 9 次 + reviewer 16 次 = 25 次系统触发）\n3. 关键决策审批（GPU 扩容、submit-to-review、framing 改动）\n4. 系统告警（30 分钟无动作的 keepalive）\n\n**用户介入的关键时刻与影响**:\n\n| 日期/时间 | 用户 | 干预内容 | 项目走向影响 |\n|---------|------|--------|------------|\n| 5/14 20:31 | 周俊伟 | \"重新 dream 一次\" | 触发 dream_20260514T203201（第 3 次 dream）——结果仍 3/6 weak reject |\n| 5/18 05:52 | 曹晓玉 | \"纯诊断缺乏 positive contribution\" | **核心转折**——Director 进入 method 狂搜模式，引发 5/19–5/20 的 8 method × 全 negative 灾难 |\n| 5/18 15:18 | 曹晓玉 | \"你有 main 来帮你干活，他的 worker 并发没有上限\" | Director 放开 GPU 调度上限，5/18–5/20 错误密度爆炸（共 39 mistakes/3 days） |\n| 5/18 15:44 | 曹晓玉 | \"再给你八卡 RTX 5090\" | 资源 4→12 卡，但 cross-server 协调成本激增（M030/M031/M032/M042/M053/M058 系列 wrong-server/dup-launch） |\n| 5/20 18:12 | 曹晓玉 | \"我唯一的想法就是我们要拿到 4.5 分\" | D219 把 target 从 3.5–4.0 抬到 4.5；5/21 12:03 D225 又下调回 3.5–4.0——纯属应付式上调 |\n| 5/21 09:00–09:07 | 曹晓玉 | \"5090-b 关机\" + \"无卡开机了\" | 单边资源回撤，Director 须临时迁移实验 |\n| 5/22 10:30 | 曹晓玉 | \"这个问题（scope overclaim）出现很多遍了，怎么回事\" | 表达明显不满；D239–D240 框架收窄从此处倒推执行 |\n| 5/23 03:04 | 曹晓玉 | \"论文通读一遍了吗，写作质量很重要\" | 触发 24 轮 paper-audit-review-visual session |\n| 5/23 12:36 | 周俊伟 | \"论文图太少…Figure 1 用 PaperBanana 重画\" | 加入 paper-figure-optimize 角色（4 session），晚期增加图表 |\n| 5/23 17:07/17:13/17:20 | 张默涵 | 反复追问 reference verification | 揭示 M059（ma2024selfimproving 全部作者 AI 幻觉）+ M040/M041（3/96 bib 条目作者幻觉） |\n| 5/23 19:15 | 运维 | \"ARR 提交前数据自查\" | 触发全文数据真实性审计 |\n| 5/24 04:08 | 曹晓玉 | \"Must-Fix 问题你们自己仔细反思看看怎么改\" + \"autodl-5090-c 已关机\" | DDL 前 2 天单边减资源 |\n\n**决策质量**:\n- **PI（曹晓玉）的决策质量**: 资源给予慷慨 + 目标导向明确（中 Main），但**对 agent 团队的 capacity 估计过于乐观**。\"4.5 mandate\"（5/20）和\"实验都提前准备\"（5/18）是**直接的项目恶化驱动力**——它使 Director 从\"诊断收敛\"模式切换到 \"method 狂搜模式\"，引发后续 2 天 8 个 method 全 negative + 21 mistakes/day 的高错误率\n- **周俊伟的介入**: 偏向于具体技术批评（dream 不达标、figure 不够、reference 验证），**精准但晚**——很多问题在 reviewer 已有信号\n- **张默涵的介入**: 在 DDL 前 48 小时几次精准 catch 引用 bug——属于关键质量兜底\n\n**反事实推理**：\n- **如果没有 5/18 PI 的\"加强 positive contribution\"压力**：项目大概率在 5/18–5/19 就接受 \"diagnostic-only\" 定位，省下 8 个 method × negative 的 2 天，proceed 到 R20 左右；最终评分可能仍在 3.0–3.5，但 mistakes 数会少 ~30%\n- **如果 PI 5/20 没给\"4.5 mandate\"**：D219 不会出现，D225 也不需要回调；framing 不会经历 D237/D238 的过度扩展再收窄\n- **如果 D243 早 2 天出现**：5/22–5/23 的写作 polish 时间会从 ~48h 增加到 ~96h，paper 质量会更稳，但 R36 fresh 3.0 的核心问题不会改善——那是 **scope overclaim** 引发，主因是 D238 的过度扩展\n\n**人工干预时机**:\n- **太晚的**: 5/22 10:30 PI 才发火 \"scope 问题出现很多遍\"——其实 5/14 09:25 D008 就已经收窄过一次（\"Narrative B 排除\"），中间 7 天 framing 反复横跳没人 hard stop\n- **太早的**: 5/20 18:12 PI 在所有 method 还在跑、cross-task 数据未出时就给\"无条件 4.5 mandate\"——把 4.0 → 4.5 的 commitment 强加给一个还在 3.0 的项目\n- **恰当的**: 5/23 张默涵反复追 reference verification——这是 desk-reject 红线\n\n## 4. 角色行为深度分析\n\n### 4.1 Director (262 sessions, 25.7K min, 920 Bash, 970 reply_to_user)\n- **做得好**: D018 (5/14 12:27) 在 best-of-N 失败后 2 小时内完成第一次大 pivot；D243 (5/22 20:53) 在压力下做出\"收敛冻结\"判断\n- **做得不好**:\n  - **framing 翻烧饼**: 5/22 06:29–10:38 共 5 次 framing 修改（D236/237/238/239/240），平均每 1.5 小时一次。**这不是 fresh review 驱动的，主要由 Reviewer #117/118 内部审核驱动**——Director 对 Reviewer 单边判断的依赖度过高\n  - **被 PI 误导**: 5/18–5/20 在用户压力下扩展 method 探索，违反自己 D018 已确认的 \"diagnostic > prescriptive\" 判断\n  - **数据 provenance 失控**: M016/M018/M024/M025/M026/M027 系列显示 Director 对论文数字溯源**完全无 grip**——多次 Reviewer 兜底才发现 SciERC AUROC 5 个值中 4 个不可溯源（M006）\n- **DIRECTOR_DECISION 事件**: 仅 3 次显式 log，但实际 248 条 D 决策——**Director 决策\"显式化\"机制几乎失效**\n\n### 4.2 Main Agent (283 sessions, 37.6K min, 9 escalations)\n- **做得好**: 工具调用结构化（spawn_worker 2207 次，update_registry 2383 次）；message 量化报告\n- **做得不好**:\n  - **Worker spawn 后不验证**: M021/M037/M038/M042/M047/M049/M052 共 7 次 false-done 或 false-failed 判断，**Worker 报告状态可信度系统性 < 70%**\n  - **wrong-model-data 系列**: M030/M031/M032 三次在 7B/8B/LLaMA 数据上跑错——Agent 派发 Worker 时未严格 path validation\n  - **N=8 vs N=16 混源**: M007/M024/M027/M057 反复在不同 N 配置间张冠李戴\n  - **Statistical replacement bugs**: M068 Worker 全文替换 Holm p 值，混淆两个独立统计框架\n- **Agent ESCALATED_TO_HUMAN: 9 次**——Agent 实际 ack 自己 \"out of capability\" 的频率不高，更多是被 reviewer 兜底揭穿\n\n### 4.3 Reviewer (299 sessions, 29.2K min, 16 escalations, 464 errors)\n- **关键贡献**: 几乎所有 high-severity bug 都是 Reviewer catch 的——M002 (per-type degen 定义)、M006 (SCIERC_REF 不可溯源)、M016 (LP global ρ 50% 降幅)、M026 (cross_selection LLaMA vs Qwen 行错)、M036 (B2 verifier train-on-test leak)、M051 (probe entity-level CV leak)、M068 (Holm p 值混淆)、M069 (主表 AUROC 9.1σ 偏差)、M070 (construction metric inconsistency)\n- **角色定位**: 项目的**实际质量底线**——没有 Reviewer，论文几乎 100% 会因数据 bug 在 ARR 阶段 desk reject\n- **问题**:\n  - Reviewer **过度依赖文本对账**而非独立 SSH 验证——M050 (probe AUROC 0.920 vs 0.987 都是中间结果误用) 是 Reviewer 自己误信本地 artifact\n  - Reviewer 16 次 ESCALATED_TO_HUMAN——遇到模糊 framing 选择 escalate 而非裁定\n  - M011 显示 Reviewer 自己也会犯 CRITICAL 误判（macro vs micro F1 混淆）然后被 Director 错误信任\n\n### 4.4 Paper Agent (58 sessions, 22.5K min)\n- **做得好**: 高密度 Read (5607) + Edit (5359)，paper_compile_and_check 726 次——LaTeX 工程链稳定\n- **做得不好**:\n  - **AI hallucinated bib entries**: M040/M041/M059 共 4 个引用条目 author 全是 AI 幻觉——这是 desk reject 红线，靠 Pre-Review Gate Step 6 才被 catch\n  - **数值 patch 顺序错乱**: M024/M025/M026/M027 显示 Paper Agent 在表格修复时不查 cross-table consistency\n  - **D248 micro-F1 vs macro-F1 metric 错位**: 临门一脚发现 construction \"+1.11pp\" 是 metric 不一致——Paper Agent 12 处 patch 全部撤销\n\n### 4.5 Worker (1335 sessions, 7.7K min, 604 errors)\n- 每个 worker session 平均 5.8 minutes（短任务为主）\n- 误诊远程进程状态 **5 次**（M021/M037/M038/M047/M049）——这是结构性问题\n- VLLM \"server-without-client\" 缺陷复发 **3 次**（M037/M038 + 14B early inference）——同样 bug 反复出现\n- M030–M032 同模型 Worker wrong-data 错误 3 次同源\n- M042 Worker 连错服务器且**返回 status=done** 这种虚假信号——signal coverage 不完整\n\n## 5. 关键发现\n\n### F1 [HARNESS] 5/22 framing 翻烧饼是\"Reviewer 单边驱动 + Director 缺乏锚点\"的系统暴露 — **严重程度: 高**\n\n**证据**:\n- D235 (5/22 04:13, \"LP dominates at all budgets\") → D236 (5/22 05:42, 同样表述) → **D237 (5/22 06:29) 作废 D236**（Reviewer #118 catch CoNLL LP -2.34pp） → D238 (5/22 09:23 \"TTS boundary conditions\" 升级) → D239 (5/22 10:38 R35 fresh 强制收窄回 NER) → D240 (5/22 11:19 R36 fresh 3.0 进一步收窄)\n- 6.5 小时内 5 次 framing 修改，前 3 次内部 Reviewer 驱动，后 2 次 fresh review 强制矫正\n- mistakes M062/M063 直接归因：\"Framing 升级时未检查证据覆盖度\"\n\n**根因**: 系统设计层面，没有 \"framing 升级 → 必须经 paper-audit 与 evidence-coverage 自检 → 再用 fresh review 复核\" 的链路。**只要 Reviewer 单方面给出 \"Framing OK\" 就可以推进**，但 Reviewer 本身在内部审稿模式下更宽容（D241 中 user 明确\"R41 我希望 fresh 模式拿干净分数\"）。\n\n**改进建议**:\n- 增加 \"framing-pivot gate\"：任一 D 决策标记 `framing_change=true` 时，必须强制 dream + fresh review 两路并行，48 小时冷却期才能 commit\n- Director 在 framing 决策时必须显式列出 \"evidence coverage table\"——每个标题关键词对应的 dataset/model/seed 数量\n\n### F2 [HARNESS + MODEL] PI 资源/目标 mandate 与 agent 实际产能不匹配，催生 8 method × 全 negative 灾难 — **严重程度: 高**\n\n**证据**:\n- 5/18 05:52 PI：\"纯诊断缺乏 positive contribution\" → 5/18 全天 13 mistakes（项目第三高）\n- 5/18 15:18 PI：\"worker 并发没有上限\"+ 12 张 5090 → 5/19–5/20 共 32 mistakes\n- 5/20 18:12 PI：\"无条件 4.5 mandate\" → D219 上调目标→ D225 (5/21 12:03) 又下调 → 4.5 commitment 仅维持 18 小时\n- 8 个 method 全 negative（MRSC/LSC/ESJ/E_θ/B1 SCD/B2 verifier/B3 prompted diversity/DGEC）\n- D170 (5/20 09:04) 自我评估：\"Construction 成功率从 ~25% 到 ~32%，远不及 70-80% 目标\"——method 探索失败显式确认\n\n**根因**: 系统设计上，PI 给的 mandate 直接进入 Director 决策上下文，但**没有 capability-check 机制**——agent 团队没办法量化\"4.5 需要 X 个 novel insight，我们最多产出 Y 个\"，于是被迫接单。MODEL 层面，单个 agent 的 long-horizon planning 不足以在 PI 指令前主动反驳 \"这个目标不现实\"。\n\n**严重程度评估**: 这 2 天浪费了 ~24 GPU-day，引入 21 + 11 = 32 mistakes，并使最终 framing 走了 D219→D238→D240 的大弯路。如果 5/20 PI 沟通时 Director 能 push back \"4.5 需要的不是更多 method，而是 mechanistic theorem\"，至少能省一半成本。\n\n**改进建议**:\n- 引入 \"target-capability gap\" 工具——目标分数与当前评分差距 >0.5 时，强制 dream + Reviewer 联合评估 \"需要多少新 evidence\"\n- PI mandate 进入系统时必须经过 Reviewer 独立 feasibility check\n\n### F3 [HARNESS] Worker 远程状态诊断不可靠，5 次 false-failed 误判 — **严重程度: 高**\n\n**证据**:\n- M021 (5/19): Worker 超时 5h，registry 误标 FAILED 但远程 nohup 训练正常\n- M037 (5/20): 14B early inference Worker 1 + Worker 2 均报 done，输出目录空\n- M038 (5/20): VLLM server-without-client 缺陷 3 次复发——Worker 启 server 不启 client，GPU 空转\n- M047 (5/20): 14B inference 第 1 次误诊为 failed，输出实际完好\n- M049 (5/21): 14B inference 第 2 次误诊，PID 252310 仍在运行 98% GPU util\n- M052 (5/21): exp_fewnerd_t05_s456 cron 误判为 failed\n- M042 (5/20): Worker 连错服务器（autodl-5090 vs autodl-5090-c）还返回 status=done\n\n**根因**: Worker 诊断协议依赖（a）输出文件存在性（b）进程存活——但 vLLM model loading 期可达 15-20 min 无输出。系统没有强制 Worker 在诊断前同时检查 `ps -p PID` + `nvidia-smi` + `ls -la output_dir` 三步。\n\n**严重程度**: 累计浪费 ~12 GPU-hours + ~3 小时人工 escalation 时间。**更危险的是 M042 类——Worker 在错误服务器上\"成功\"完成空操作返回 done**，这种 signal-noise 信号几乎无法 detect。\n\n**改进建议**:\n- Worker `submit_training_job` 后 5 min 内强制 ssh_read_only 验证 GPU util > 0\n- Worker `status=done` 必须附带 (a) output file size > threshold (b) 关键 metric 值（如 greedy F1 在预期范围）\n- 增加 `cross_validate_worker_status` 工具，对所有 cron-flagged failed 做强制 Reviewer 复验\n\n### F4 [HARNESS] 数据 provenance 链断裂导致论文数字反复回炉 — **严重程度: 高**\n\n**证据**:\n- M006: SCIERC_REF 5 值中 4 值不可溯源（5/18）\n- M013: 6 个分析脚本各自实现 F1/退化定义，**同一数据产 3 个不同 Greedy F1** + 2 种 degeneracy 定义（5/18）\n- M014: degen_rate 字段实际是 sample_f1_pct_zero（CoNLL 差 82pp）（5/18）\n- M016: unified_metrics 迁移后 FewNERD LP global ρ 0.42 → 0.22（50% 降幅），论文 4 处错引（5/18）\n- M024/M025/M026/M027: 主表/Tab5 SciERC AUROC 顺序翻转、CoNLL degen N=16 误用、headroom 用 LLaMA 行（5/19）\n- M057: CoNLL v4 3-seed 混合 exp002 + MF4v2 两个 pipeline（5/21）\n- M069: 主表 SciERC EM AUROC .749 是 9.1σ copy-paste 错误（5/23）\n- M070: 5-seed construction +1.11pp 是 instance-averaged vs micro-F1 metric 不一致（5/24）\n\n**根因**:\n1. 论文表格数字**手动填写**而非脚本自动生成（M024 显式记录）\n2. 同一指标多脚本独立实现（M013 unified_metrics 出现前）\n3. 数据 patch 时**不查 cross-table consistency**（M025）\n4. registry 中实验状态与服务器实际不一致（M058 跨服务器去重失败）\n\n**严重程度**: 每一项都可能成为 ARR reviewer 投诉的 \"不可复现\" 红线。M016 的 50% ρ 降幅如果未及时 catch，整篇论文 QE 章节立刻崩塌。M069/M070 在 DDL 前 48 小时才被发现——**论文 freeze 时数字稳定性是历史最低点**。\n\n**改进建议**:\n- 引入 \"paper_consistency_audit\" 工具，每次 Paper Agent edit 后强制全文 grep 数值 + 与 registry/report.json 交叉验证\n- 论文数字必须有 `provenance.yaml` 条目：`{ value, exp_id, metric_key, computed_at }`\n- 主表禁止手动填写，强制由 `generate_main_table.py` 从 registry 生成\n\n### F5 [HARNESS] 文献/引用幻觉是 desk-reject 红线，靠人工兜底才 catch — **严重程度: 高**\n\n**证据**:\n- M040/M041: 3/96 bib entries 作者 AI 幻觉（chen2025twofailures / wen2025abstention / liu2025uqcc），URL 指向错误论文（5/20）\n- M059: ma2024selfimproving 全 5 个作者 AI 幻觉，正确第一作者为 Xie（5/21）\n- 张默涵 5/23 17:07 介入：反复追问 reference verification 才 catch M059\n\n**根因**: Paper Agent 生成 bib entries 时\"标题正确 + 作者幻觉\"是典型 LLM 失效模式。系统缺少强制 Semantic Scholar API 验证。\n\n**改进建议**:\n- \"reference-audit\" skill 必须在 Paper Agent **每次** 新增 bib 时自动触发，不依赖 pre-review gate\n\n### F6 [MODEL] 数学/统计概念在跨 worker 复制时系统性丢失 — **严重程度: 中**\n\n**证据**:\n- M068 (5/22): Worker 把 global k=57 Holm p=0.055 全文替换为 seed-replication k=5 p=0.013，混淆两个统计框架，影响 12+ 处\n- M009/M010 (5/18): span-based vs text-based matching 多次混淆\n- M013 (5/18): 6 个独立 F1/degeneracy 实现\n- D227 (5/21): \"代码库中 3 个 MV 实现使用不同 threshold + entity match\"\n\n**根因**: 这不完全是 harness 问题——长上下文中保持\"两个统计框架的语义区分\"对当前模型是困难的。Worker 接到 \"全文替换 X→Y\" 指令时倾向于做精确字符串替换而不验证语义。\n\n**改进建议**: 涉及统计/数学概念的全文修改禁止 Worker 独立执行，必须 Agent 亲自做。Director 指令应强制要求\"列出修改清单 + 每处的语义检查\"。\n\n### F7 [HARNESS] Dream 机制对 framing 健康度的检测能力不足 — **严重程度: 中**\n\n**证据**:\n- Dream 1（5/14 09:33）三档全 3/6，结构性问题 ID 完整（缺 baseline / novelty 薄 / formula 不一致）\n- Dream 2（5/14 10:53）三档全 3/6（持平）——Dream 系统未能给出 \"what changed since last dream\"\n- Dream 3（5/14 20:32）三档评分模式相似——dream 系统**对框架质量改进的 sensitivity 几乎为 0**\n- Dream 5（5/15）+ Dream 6（5/16）后系统连续输出 3.0/5 plateau，但实际 fresh review 给到 3.5（D224 R27）\n- Dream/fresh review 的相关性极弱\n\n**严重程度**: 项目 5/14–5/16 共做了 6 次 dream，没有一次提供了 fresh review 才发现的 \"scope overclaim\" 问题。Dream 失去了 early-warning 作用。\n\n**改进建议**: Dream 应**预先训练**到与 fresh review 评分对齐（calibration）；或减少 dream 频率，增加 fresh review 频率。\n\n### F8 [HARNESS] 跨服务器资源调度引入大量\"虚假状态\"事故 — **严重程度: 中**\n\n**证据**:\n- M020/M023/M035 (5/19): registry GPU 字段格式不规范 / 手动启动绕过 cron / 未注册 GPU 进程\n- M042 (5/20): Worker 连错服务器（autodl-5090 vs autodl-5090-c）+ 返回虚假 done\n- M053/M058 (5/21): 重复启动 / 跨服务器数据未在 registry 标注\n- M065/M066 (5/22): kill_job 未实际终止 vLLM 子进程 + 3 个 PREPARING 实验未启动空转 9h\n\n**根因**: 用户 5/18 一次性给 12 张卡（autodl-5090 + autodl-5090-b + autodl-5090-c）后，registry 缺少 \"server-aware\" 一致性检查。Agent 派发 Worker 时 server alias 容易混淆。\n\n**改进建议**: registry 必须强制 `server` + `gpu_ids` 双字段，submit_training_job 内置 hostname 验证。\n\n### F9 [MODEL] Long-horizon planning 失效，11 天内 5 次重大 framing reframe — **严重程度: 中**\n\n**证据**:\n- D018 (5/14): correlation-selection gap framing 建立\n- D130 (5/18): systemic reframe 8 项\n- D219 (5/20): 目标 3.5→4.5\n- D237 (5/22): dataset-dependent + diagnostic primary\n- D238 (5/22): TTS boundary for structured prediction\n- D239/240: 回退 NER\n\n**根因**: agent (Director) 在长上下文中难以维持 \"previously rejected hypothesis\" 的标记——D008 已排除 RE-primary，D018 已排除 best-of-N improvement，但 5/20 PI 一句\"加 positive contribution\"，Director 又开始 method 探索；5/22 fresh review 才 hard reset。**memory.md 134 行 + paper_framing.md 87 行不足以承载 11 天 248 D 决策的状态机**。\n\n**严重程度**: 每次 framing 重构需要 12-24 小时（paper edit + audit + dream），累计成本 ~3 个工作日。\n\n**改进建议**:\n- 引入 \"rejected_hypothesis.yaml\"——每次 framing 撤销时显式 log 被排除的方向 + 排除理由 + 重启 gate（什么新证据才能 unblock）\n- Director 系统 prompt 加 \"before pivoting, list past 3 framing decisions and verify new framing doesn't revisit a previously-rejected direction\"\n\n### F10 [HARNESS] 错题本 (mistakes.yaml) 未能真正阻止同类错误复发 — **严重程度: 中**\n\n**证据**:\n- VLLM server-without-client 在 M037/M038 后明确写入 prevention，但 M037 中的 \"13\" 同类问题再次出现\n- Worker false-failed 诊断 M021 (5/19) 后明确 prevention，但 M047 (5/20) / M049 (5/21) / M052 (5/21) 反复出现 4 次\n- wrong-model-data M030 (5/20 06:00) → M031 (5/20 07:00) → M032 (5/20 08:00) 同日 3 次\n- 跨表 metric 不一致 M013 (5/18) → M057 (5/21) → M070 (5/24) 横跨 6 天\n\n**根因**: mistakes.yaml prevention 字段写入后，**没有任何 enforcement 机制**让后续 Worker 在执行同类任务前先 grep mistakes.yaml。完全靠 Agent 自己的 context 记忆。\n\n**改进建议**:\n- 增加 `pre_spawn_worker` hook：根据 task 类型自动 attach 相关 prevention rule\n- mistakes.yaml 中 high-severity + repeated > 2 次的应该升级为 constraints.yaml 强约束\n\n### F11 [MODEL] Agent 自我纠错能力弱，全靠 Reviewer 兜底 — **严重程度: 中**\n\n**证据**:\n- 70 条 mistakes 中，**几乎全部是 Reviewer 或独立 Worker 发现**，Agent 自查发现率 < 10%\n- M050: Director 引用本地 artifact AUROC 0.920 直接报告给 PI 和 Paper Agent，未让 Reviewer 验证服务器端最终输出（5/21）\n- M067: 论文中 \"LP-best +8pp on Few-NERD\" 无任何数据支撑，被 Reviewer 排查后确认是 number-stitching 幻觉\n- M069: 主表 SciERC EM AUROC 9.1σ 偏差，Paper Agent 与 Reviewer 都未在初始 patch 时 catch\n\n**根因**: MODEL 层面，agent 在长上下文中对 \"我刚才写的数字是否正确\" 的元认知较弱。即使 mistakes.yaml 已记录类似错误，agent 复用旧数据时不主动验证。\n\n**改进建议**: 论文相关 patch 任务必须经过独立 Reviewer 在不同 session 复算——不能由 Paper Agent + 同一 Reviewer 闭环验证。\n\n### F12 [HARNESS] 用户对话与 agent 状态机不同步 — **严重程度: 低**\n\n**证据**:\n- 5/22 14:20 用户：\"我希望选择 fresh 拿到干净的得分，不会选择 Continue 模式\"——但 Director 5/22–5/23 多次 default 推荐 Continue 模式\n- 5/22 10:30 用户：\"这个问题（scope overclaim）出现很多遍了\"——表明用户感受到的重复 ≠ agent 内部认知的\"已修复\"\n- 5/23 03:13 用户：\"实验都结束了？\"——agent 实际还在跑 6 个实验\n\n**根因**: ralph_loop 把用户飞书消息注入 Director context，但没有\"用户偏好持久化\"机制。每次 BOOT 后用户偏好（如 \"always use fresh mode\"）丢失。\n\n**改进建议**: 用户消息中的偏好（识别 mode \"I prefer X\" / \"don't do Y\"）自动 promote 到 constraints.yaml 或 user_preferences.yaml，每次 BOOT 强制载入。\n\n### F13 [HARNESS] Paper Agent 多轮 figure 优化对最终评分贡献不显著 — **严重程度: 低**\n\n**证据**:\n- 5/23 12:36 周俊伟：\"Figure 1 必须用 PaperBanana 重画\" → 5/23 14:40/15:04/15:10/15:53/16:00 共 4 轮反复\n- paper-figure-optimize 角色 4 session，paper-audit-review-visual 24 session\n- 但 R36/R40 fresh review 仍 3.0，figure 在审稿意见中**不是核心扣分项**\n\n**严重程度**: 占用了 DDL 前 ~6 小时的 polish 时间，**机会成本可观**——这段时间本可以做 R36 reviewer concerns 的 mechanistic 深化。\n\n**改进建议**: figure polish 应在 framing 稳定后才启动；framing 反复期不投入 figure 工时。\n\n---\n\n**总结**: 这是一个**核心 negative finding 真实、但被 system + model + PI mandate 三方拉扯导致执行成本极高**的项目。最终 ~3.0 fresh score 与\"NER-only diagnostic\"的实际科研价值匹配，与用户期望的 4.5 不匹配。系统层面最重要的 3 个改进点：(1) framing-pivot gate (F1+F9) (2) Worker 状态诊断协议加固 (F3+F8) (3) 论文数据 provenance 自动化 (F4+F5)。模型层面，long-horizon planning 与跨工作流元认知是上限——目前 agent 团队的 capability ceiling 不足以在没有 hard system gate 时维持 11 天 240+ 决策的一致性。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9cf75f-3b3e-4ad9-b2e8-de86b4282dbc",
  "isSidechain": false,
  "requestId": "req_011CbaoQvyYjqnatgvjZa3bg",
  "type": "assistant",
  "uuid": "30a74bff-f5df-44d5-9c73-5ea38555502c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mm4nVKN2HVXkHTVwzr7Y8L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 225405,
      "output_tokens": 17507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 124 · 2026-05-31T14:31:18.242Z_

<details><summary>↩ Tool result · `toolu_01R5a7yRUzzh8VeBaPF7CR1b`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a74bff-f5df-44d5-9c73-5ea38555502c",
  "isSidechain": false,
  "promptId": "ddb9aabe-f13c-4e71-9e59-17fb1dca6232",
  "type": "user",
  "uuid": "08930b7d-ae6d-4782-81c0-dfc0451e729d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
    "content": "# struct_self_consist_ie — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:54Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0514_1\n\n## 1. 项目概况\n\n- **目标 venue**: EMNLP 2026 Main（via ARR May），DDL 2026-05-25\n- **生命周期**: 2026-05-14 04:20 → 2026-05-25 ~19:00（约 11 天）\n- **最终标题**: *\"When Does Test-Time Scaling Help Structured Prediction?\"* → 改为 \"**When Self-Consistency Fails for NER**\"（D239/D240，从 \"Structured IE\" 收窄到 NER）\n- **实验规模**: 312 个 DONE 实验（成功 207 / 负向 55 / 杀掉 51 / 失败 15），17 个 PREPARING 未启动；平均 retry 仅 0.055，最大 1（registry 上看似干净，下文揭示这是**虚假干净**）\n- **角色 token 消耗**: agent 34.4M output、reviewer 38.0M output、paper_agent 28.3M output、director 25.1M output、worker 计 ~126K turns；累计 ~183M tokens\n- **session 数**: 2271，总 turns 383,079，errors 2,199\n- **论文产出**: main.tex 编译通过，46 页（≤8 页正文），62 references，匿名 repo 已 push\n- **最终 fresh 审稿评分**: R40 = 3.0（R1=3.5, R2=3.0），R41 提交后处于\"待审\"状态——**未达到 Main Conference 阈值（4.0）也未达到 Findings 阈值（3.5+）**，仅达到 Borderline Findings（2.5）到 Borderline Conference（3.5）区间，未达到用户在 D219 设定的 4.5 目标，也未达到 D225 校准的 3.5–4.0 目标\n- **决策密度**: 248 条 D 决策（前 8 天 195 条，DDL eve 5 条），平均 ~22.5 条/天，5-14 单日 61 条\n- **错题本**: 70 条 mistakes，46/70 high severity；以 code_bug (26) 和 agent_behavior (15) 为主\n\n## 2. 项目叙事重建\n\n### 阶段 A（5/14，第 1 天）：MVP 反复试错与第一次基础叙事建立（D001–D061）\n- 4:23 UTC 设定原始假设：fine-tuned 模型 + soft Jaccard（SJ）能让 IE 一致性-准确率相关性 ρ≥0.40，显著超过 PMC12888769 的 Fleiss' Kappa (FK) 基线\n- 当天连发 61 条 D 决策（项目历史最高）：换数据集（ACE05 LDC 受限 → SciERC RE，D003）、Gate 0 NER 通过/RE FAIL、加 temperature ablation、加 4 个 baseline (log-prob/EM/voting/SJ)、补 N=16\n- **第一次 pivot（D018, 12:27）**: exp_016 发现 best-of-N selection 在 NER 上**全部不如 greedy**——核心 sales pitch \"TTS improves IE\" 死掉。Director 当机立断把叙事从 \"TTS improvement\" 改为 \"correlation-selection gap analysis\"\n\n### 阶段 B（5/15–5/17）：Dream 反复打脸 + reframe 循环（D062–D108）\n- 共 10 次 Dream，前 4 次三档全 3/6（Weak Reject），原因稳定指向 novelty/positioning/related work\n- D011（5/14 10:52）已诊断：\"只对比 FK 一个弱 baseline\" 是 #1 问题，补 log-prob/voting/EM\n- 5/15 加入 free-form decoding ablation (exp-018)，叙事第二次升级到 \"constrained decoding bottleneck\"\n- 5/16 加入 Few-NERD 第三数据集 + 3rd seed + LoRA rank ablation，叙事第三次升级到 \"capability trap + two failure mechanisms\"\n- 5/14 周俊伟（外部用户）首次远程介入：\"重新 dream 一次，我看你之前 dream 的记录都没有达标啊\"——这是项目第一次人工干预，结果是 Director **再启动一次 dream（dream_20260514T203201），仍未达标**\n\n### 阶段 C（5/18，中期转折，第 5 天）：用户强 mandate + GPU 扩容 + 方法论狂飙（D125–D162）\n- 5/18 05:52 曹晓玉（PI）介入：\"纯诊断性质缺乏 positive contribution的问题有解决吗\"\n- 5/18 09:51 PI 进一步：\"你有四张卡，还有好多天才DDL，不要这么短视，实验都提前准备…大胆想\"\n- 5/18 15:18 PI 严厉训话：\"三张空卡为什么不提前准备…论文定位是 diagnostic也太弱了…我要中主会…赶紧干吧\"\n- 5/18 15:44 PI 加注 GPU：\"再给你八卡 RTX 5090\"，资源从 4 → 12 张 5090\n- **后果**：当天 26 条 mistakes（仅次于 5/20 的 21 + 5/19 的 11），是项目错误密度最高的阶段——Worker 大规模并行 + 跨服务器分流引入大量 wrong-model-data、wrong-server、stale-baseline、unicode bug 等\n- D130 全文 \"systemic reframe\"：8 项统计 softening + 4 项贡献重构\n\n### 阶段 D（5/19–5/20，方法论疯狂搜索期，第 6–7 天）：所有 entity-level method 全 negative（D163–D202）\n- 用户 5/20 18:12 给 \"无条件 4.5 mandate\"：D219 把目标从 3.5–4.0 直接抬到 4.5（Consider for Award，约 top 2.5%）\n- **2 天内试了 ≥ 8 个 method**：MRSC（multi-round SC, -2.94pp）、LSC（latent SC, -2.5pp）、ESJ（entity self-judgment, AUROC=0.51 ≈ chance）、E_θ verifier、B1 SCD（self-consistent decoding）、B2 entity verifier（+3.62pp 后发现 train-on-test 数据泄漏 M036）、B3 prompted diversity、DGEC heterogeneous-T/SJ/VC weighting\n- **全 negative**。Director 5/20 把 4 个 negative 重组为 \"unified narrative: lack entity-level self-judgment ability + MV is the only valid signal\"\n- 9/15 high-severity mistakes 在此期间发生（M030 wrong-model-data，M033 wrong baseline，M037/M038 VLLM server-without-client 3 次复发，M046 SCD +3.84pp 是 metric artifact）\n- **5/21 02:16 D211 Hidden-state probe 一度看似 救场**：AUROC 0.92 >> ESJ 0.51——但 12 小时内被 Reviewer 拆穿是 entity-level StratifiedKFold instance 泄漏（M051），GroupKFold 重做后 2/3 数据集 < MV（D215）\n\n### 阶段 E（5/21–5/22，framing 翻烧饼期，第 8–9 天）：D219–D243\n- N-scaling 数据 (N=8/16/32/64) 陆续齐全后，framing 在 48 小时内**翻烧饼三次**：\n  - **D235 (5/22 04:13)**: \"MV works too slowly; LP-best dominates at all budgets\"\n  - **D236 (5/22 05:42)**: \"MV gains are marginal and cost-prohibitive; LP-best dominates at every budget point\"\n  - **D237 (5/22 06:29，D236 作废)**: \"**dataset-dependent** optimal strategy + diagnostic framework as primary\"\n  - **D238 (5/22 09:23)**: 升级到 \"**boundary conditions for TTS in structured prediction**\" + 标题改为 \"When Does Test-Time Scaling Fail?\"\n  - **D239 (5/22 10:38)**: R35 fresh review 给 3.5，要求 \"标题收窄为 NER\"——D238 升级被推翻\n  - **D240 (5/22 11:19)**: R36 fresh 给 3.0（比 R35 还低），\"IE\" 仍被判 overclaim，最终回到 **\"When Self-Consistency Fails for NER\"**\n- 5/22 10:30 用户问：\"这个问题（scope overclaim）出现很多遍了，怎么回事，一直没解决吗\"——表达明显不满\n- 5/22 10:42 用户：\"仔细反思每一次审稿，有重大升级和导致一直卡住的时刻\"\n\n### 阶段 F（5/23–5/24，收口期，第 10–11 天）：D243–D248\n- D243（5/22 20:53）：\"研究确认收敛，不追加主要实验\"\n- D244（5/24 02:32）：\"DDL eve 不启动新实验，4×5090 保留给 rebuttal\"——24 小时前用户还在催\"该补补，质量优先\"，但收尾时 Director 选择保守\n- 5/23–5/24 出现 M068（Worker 将 global k=57 Holm p=0.055 全局替换为 seed-replication p=0.013，混淆统计框架，影响 12+ 处）+ M069（主表 SciERC EM AUROC 复制错误，9.1σ 偏差）+ M070（5-seed construction +1.11pp 是 metric 不一致产物）——**临提交前论文数字最为不稳**\n- 5/23 12:36 周俊伟：\"论文图太少…Figure 1 必须用 PaperBanana 重画，不要有廉价感\"——发起 4 轮 figure 反复\n- 5/24 09:13 D248 把 Reviewer critical 降级为 info：micro-F1 不是 construction 的 metric——一个临门一脚的争议未必正确解决，留作 rebuttal\n\n**关键转折点小结**：D018 (NER best-of-N 失败) → D130 (systemic reframe) → D219 (4.5 mandate) → D238 (TTS boundary 升级) → D240 (回退 NER) → D243 (收敛冻结)。**前 4 个转折都是 Director 自主，后 2 个完全由 fresh reviewer + 用户压力 forcing**。\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n\n| 维度 | 原始 IDEA_BRIEF (5/14) | 最终论文 (5/24) |\n|------|---------------------|----------------|\n| 核心方法 | Adaptive Structural Self-Consistency Scaling (AS2CS) + Learned Aggregation Scorer (LAS) | **方法部分被淡化为 ablation**；论文实际叙事是 \"诊断框架 + correlation-selection gap\" |\n| 假设 | structural consistency + adaptive gating → TTS for IE 可行 | TTS 在 NER 上几乎全负向，agreement 信号有相关性但无 selection 能力 |\n| 范围 | 5 datasets × 多个 IE 任务（NER/RE/EE）+ general framework for structured prediction | **3 NER 数据集**（SciERC/CoNLL/FewNERD），RE/SQL 降级为 exploratory |\n| Contribution 数 | 4 项（ASCG/LAS/error taxonomy/headroom analysis） | 3 项（QE Framework / Diagnostic Cascade / Entity-level construction），全部 reframe |\n| 标题命题 | \"When does TTS help structured prediction?\" | \"When does TTS fail for NER?\" — **命题翻转、范围收窄一个数量级** |\n\n**Reframe 次数**: paper_framing.md 显式经历 ≥5 次 framing 升级/降级（D018→D130→D219→D237→D238→D239→D240），最终回到 5/15 早期的 \"NER + correlation-selection gap\" 叙事，绕了一大圈。\n\n**判定**：最终 findings **没有回答最初的核心问题**（\"when does AS2CS help\"），而是给出了一个相反方向的、范围窄得多的 finding（\"on NER, TTS mostly doesn't help, but here's why\"）。从科研价值看，这种偏离**合理但代价巨大**——更合理的做法是早期（D018 时）就承认\"方法不 work, 转向诊断\"，而不是在 D170 (5/20 09:04) 才正式宣告 \"DGEC 三层干预全部失败\"，期间又试 ≥8 个 method 全 fail。\n\n### 3.2 实验设计的科研严谨性\n\n- **Falsifiability**: ✅ 5/14 MVP 就有 ρ≥0.40 PASS/<0.30 FAIL 阈值，多个 gate 设计了反向条件。\n- **Baseline 充分性**: ⚠️ 初始仅对比 FK 一个弱 baseline（Dream 1 三档全 3/6 的 #1 反馈），D012 后补足 log-prob/EM/voting，**事后补救**。\n- **统计方法**: ⚠️ Bootstrap CI 使用一致，但全文 57 个统计检验仅 8/57 survive Holm-Bonferroni (D182)。M068 显示 Worker 全文混淆两个统计框架。Reviewer 多次警告 p-hacking 风险（D241 N2: \"跑 2 additional seeds 而非切 BH FDR——avoid p-hacking\"）。\n- **实验规模**: 3 seeds（部分实验仅 1 seed），3 NER 数据集，2 模型规模（8B/14B/32B/72B 但后两者非 fine-tune，存在 confound D217）。\n- **数据完整性事故**: M036 train-on-test 数据泄漏 +3.62pp 写入论文后才被 Reviewer 发现；M051 hidden-state probe entity-level CV 泄漏导致 AUROC 从 0.92 跌到 0.65；M016 unified_metrics 迁移后 LP global ρ 从 0.42 降到 0.22（50% 降幅）。这三起任一件都可能引发审稿 desk reject 级别的质疑。\n\n### 3.3 Findings 的质量与 Novelty\n\n- **核心 finding（最终版）**: \"Self-consistency 在 NER 上失败的诊断框架：degeneracy + LP-F1 alignment + LP compression 三因子级联预测 dataset-dependent 最优策略\"\n- **Novelty**: ⚠️ Reviewer 反复指出与 Yao et al. 2026 (task-level correlation)、Yun et al. 2025 (reasoning SC)、Nédellec & Xia 2026 (surface matching) 的差异是 **incremental**——entity-level vs task-level、structural vs surface、mechanistic vs descriptive\n- **审稿历史**:\n  - R8 (Round 8): R1=3.5, R2=2.5 → 平均 3.0 (5/16)\n  - R24: 3.25 (5/19)\n  - R25: 3.5/3.5 (5/19)\n  - R27: 3.0 Findings (5/21)\n  - R35: 3.5 Borderline Conference (5/22)\n  - R36: 3.0 Findings (5/22, 较 R35 下降 0.5)\n  - R40: **R1=3.5, R2=3.0** = avg 3.25 (5/22)\n  - R41/R42/R43 (continue+verify+fresh): R43 = **3.0 Findings**（5/23 04:08 用户已表达不满）\n- **最终评分**: 论文在 fresh 审稿下持续在 **3.0–3.5 之间震荡 11 个 round**，未稳定突破 3.5。**未达到 Main Conference（4.0）门槛**，仅勉强达到 Findings（3.0）。\n- **包装 vs 内容**: 包装上**过度优化**——Figure 1 重画 4 轮、claim-evidence 反复对账、24 轮 paper-audit-review-visual session。但内容上**核心负面结果**是 robust 的。从最终 3.0 评分看，**论文质量与评分匹配**——problems are real, contributions are honest but marginal。\n\n### 3.4 研究效率\n\n- **直接贡献最终论文的实验**: 估算 ~70-80 个（NER 3 dataset × N-scaling × seed × ablation）\n- **探索性弯路**: 8 个 method 全 negative（MRSC/LSC/ESJ/E_θ/B1 SCD/B2 verifier/B3 prompted diversity/DGEC 三层），cross-task universality（A1 Spider SQL + A2 HumanEval）也未进正文\n- **Negative results 的价值**: 部分进入 §6/appendix（DGEC negatives、ESJ AUROC=0.51、hidden-state probe complexity-dependent），但**未成为论文核心 selling point**——这些 negative 的 reframing 工作量极大，与产出价值不匹配\n- **从 idea 到可投稿**: 11 天，**严格意义上的 4 天有效 ddl sprint 起码有 2 天浪费在 method 探索**（5/19–5/20）。如果项目 5/18 用户介入前就接受 \"diagnostic-only\" 定位，可能省下 2 天用于深化分析\n\n### 3.5 论文与实际科研的匹配度\n\n- **总体如实**：核心 negative finding (TTS 在 NER 上失败) 真实存在\n- **过度包装风险**:\n  - QE Framework \"AUROC up to 0.82, ρ up to 0.45\"——R45 cycle 发现 M069 主表 SciERC EM AUROC 是 9.1σ 异常（.749 vs 多 seed mean .631），论文 freeze 时**仍未确认是否修正**\n  - \"Entity-level construction +1.02-1.53pp where headroom allows\"——M036/M070 显示这些数字至少经历了 train-on-test leak 和 metric 不一致两次重大修订\n  - \"5 confidence signals across 4 families systematic comparison\"——R36 reviewer 仍认为 incremental over Yao et al.\n- **被省略的 negative**: 8 个失败 method 中只有 DGEC 和 ESJ 进了 appendix；MRSC/LSC/E_θ/B1 SCD/B2 verifier/B3 prompted diversity 完全未提\n- **Claim/evidence 匹配**: M067 是关键警示——\"LP-best +8pp on Few-NERD\" 写入论文但**无任何实验支撑**，纯属拼凑\n\n### 3.6 人工参与分析\n\n**触发条件**:\n1. 主动催促（用户每日 1-3 次主动飞书）\n2. ESCALATED_TO_HUMAN 事件（agent 9 次 + reviewer 16 次 = 25 次系统触发）\n3. 关键决策审批（GPU 扩容、submit-to-review、framing 改动）\n4. 系统告警（30 分钟无动作的 keepalive）\n\n**用户介入的关键时刻与影响**:\n\n| 日期/时间 | 用户 | 干预内容 | 项目走向影响 |\n|---------|------|--------|------------|\n| 5/14 20:31 | 周俊伟 | \"重新 dream 一次\" | 触发 dream_20260514T203201（第 3 次 dream）——结果仍 3/6 weak reject |\n| 5/18 05:52 | 曹晓玉 | \"纯诊断缺乏 positive contribution\" | **核心转折**——Director 进入 method 狂搜模式，引发 5/19–5/20 的 8 method × 全 negative 灾难 |\n| 5/18 15:18 | 曹晓玉 | \"你有 main 来帮你干活，他的 worker 并发没有上限\" | Director 放开 GPU 调度上限，5/18–5/20 错误密度爆炸（共 39 mistakes/3 days） |\n| 5/18 15:44 | 曹晓玉 | \"再给你八卡 RTX 5090\" | 资源 4→12 卡，但 cross-server 协调成本激增（M030/M031/M032/M042/M053/M058 系列 wrong-server/dup-launch） |\n| 5/20 18:12 | 曹晓玉 | \"我唯一的想法就是我们要拿到 4.5 分\" | D219 把 target 从 3.5–4.0 抬到 4.5；5/21 12:03 D225 又下调回 3.5–4.0——纯属应付式上调 |\n| 5/21 09:00–09:07 | 曹晓玉 | \"5090-b 关机\" + \"无卡开机了\" | 单边资源回撤，Director 须临时迁移实验 |\n| 5/22 10:30 | 曹晓玉 | \"这个问题（scope overclaim）出现很多遍了，怎么回事\" | 表达明显不满；D239–D240 框架收窄从此处倒推执行 |\n| 5/23 03:04 | 曹晓玉 | \"论文通读一遍了吗，写作质量很重要\" | 触发 24 轮 paper-audit-review-visual session |\n| 5/23 12:36 | 周俊伟 | \"论文图太少…Figure 1 用 PaperBanana 重画\" | 加入 paper-figure-optimize 角色（4 session），晚期增加图表 |\n| 5/23 17:07/17:13/17:20 | 张默涵 | 反复追问 reference verification | 揭示 M059（ma2024selfimproving 全部作者 AI 幻觉）+ M040/M041（3/96 bib 条目作者幻觉） |\n| 5/23 19:15 | 运维 | \"ARR 提交前数据自查\" | 触发全文数据真实性审计 |\n| 5/24 04:08 | 曹晓玉 | \"Must-Fix 问题你们自己仔细反思看看怎么改\" + \"autodl-5090-c 已关机\" | DDL 前 2 天单边减资源 |\n\n**决策质量**:\n- **PI（曹晓玉）的决策质量**: 资源给予慷慨 + 目标导向明确（中 Main），但**对 agent 团队的 capacity 估计过于乐观**。\"4.5 mandate\"（5/20）和\"实验都提前准备\"（5/18）是**直接的项目恶化驱动力**——它使 Director 从\"诊断收敛\"模式切换到 \"method 狂搜模式\"，引发后续 2 天 8 个 method 全 negative + 21 mistakes/day 的高错误率\n- **周俊伟的介入**: 偏向于具体技术批评（dream 不达标、figure 不够、reference 验证），**精准但晚**——很多问题在 reviewer 已有信号\n- **张默涵的介入**: 在 DDL 前 48 小时几次精准 catch 引用 bug——属于关键质量兜底\n\n**反事实推理**：\n- **如果没有 5/18 PI 的\"加强 positive contribution\"压力**：项目大概率在 5/18–5/19 就接受 \"diagnostic-only\" 定位，省下 8 个 method × negative 的 2 天，proceed 到 R20 左右；最终评分可能仍在 3.0–3.5，但 mistakes 数会少 ~30%\n- **如果 PI 5/20 没给\"4.5 mandate\"**：D219 不会出现，D225 也不需要回调；framing 不会经历 D237/D238 的过度扩展再收窄\n- **如果 D243 早 2 天出现**：5/22–5/23 的写作 polish 时间会从 ~48h 增加到 ~96h，paper 质量会更稳，但 R36 fresh 3.0 的核心问题不会改善——那是 **scope overclaim** 引发，主因是 D238 的过度扩展\n\n**人工干预时机**:\n- **太晚的**: 5/22 10:30 PI 才发火 \"scope 问题出现很多遍\"——其实 5/14 09:25 D008 就已经收窄过一次（\"Narrative B 排除\"），中间 7 天 framing 反复横跳没人 hard stop\n- **太早的**: 5/20 18:12 PI 在所有 method 还在跑、cross-task 数据未出时就给\"无条件 4.5 mandate\"——把 4.0 → 4.5 的 commitment 强加给一个还在 3.0 的项目\n- **恰当的**: 5/23 张默涵反复追 reference verification——这是 desk-reject 红线\n\n## 4. 角色行为深度分析\n\n### 4.1 Director (262 sessions, 25.7K min, 920 Bash, 970 reply_to_user)\n- **做得好**: D018 (5/14 12:27) 在 best-of-N 失败后 2 小时内完成第一次大 pivot；D243 (5/22 20:53) 在压力下做出\"收敛冻结\"判断\n- **做得不好**:\n  - **framing 翻烧饼**: 5/22 06:29–10:38 共 5 次 framing 修改（D236/237/238/239/240），平均每 1.5 小时一次。**这不是 fresh review 驱动的，主要由 Reviewer #117/118 内部审核驱动**——Director 对 Reviewer 单边判断的依赖度过高\n  - **被 PI 误导**: 5/18–5/20 在用户压力下扩展 method 探索，违反自己 D018 已确认的 \"diagnostic > prescriptive\" 判断\n  - **数据 provenance 失控**: M016/M018/M024/M025/M026/M027 系列显示 Director 对论文数字溯源**完全无 grip**——多次 Reviewer 兜底才发现 SciERC AUROC 5 个值中 4 个不可溯源（M006）\n- **DIRECTOR_DECISION 事件**: 仅 3 次显式 log，但实际 248 条 D 决策——**Director 决策\"显式化\"机制几乎失效**\n\n### 4.2 Main Agent (283 sessions, 37.6K min, 9 escalations)\n- **做得好**: 工具调用结构化（spawn_worker 2207 次，update_registry 2383 次）；message 量化报告\n- **做得不好**:\n  - **Worker spawn 后不验证**: M021/M037/M038/M042/M047/M049/M052 共 7 次 false-done 或 false-failed 判断，**Worker 报告状态可信度系统性 < 70%**\n  - **wrong-model-data 系列**: M030/M031/M032 三次在 7B/8B/LLaMA 数据上跑错——Agent 派发 Worker 时未严格 path validation\n  - **N=8 vs N=16 混源**: M007/M024/M027/M057 反复在不同 N 配置间张冠李戴\n  - **Statistical replacement bugs**: M068 Worker 全文替换 Holm p 值，混淆两个独立统计框架\n- **Agent ESCALATED_TO_HUMAN: 9 次**——Agent 实际 ack 自己 \"out of capability\" 的频率不高，更多是被 reviewer 兜底揭穿\n\n### 4.3 Reviewer (299 sessions, 29.2K min, 16 escalations, 464 errors)\n- **关键贡献**: 几乎所有 high-severity bug 都是 Reviewer catch 的——M002 (per-type degen 定义)、M006 (SCIERC_REF 不可溯源)、M016 (LP global ρ 50% 降幅)、M026 (cross_selection LLaMA vs Qwen 行错)、M036 (B2 verifier train-on-test leak)、M051 (probe entity-level CV leak)、M068 (Holm p 值混淆)、M069 (主表 AUROC 9.1σ 偏差)、M070 (construction metric inconsistency)\n- **角色定位**: 项目的**实际质量底线**——没有 Reviewer，论文几乎 100% 会因数据 bug 在 ARR 阶段 desk reject\n- **问题**:\n  - Reviewer **过度依赖文本对账**而非独立 SSH 验证——M050 (probe AUROC 0.920 vs 0.987 都是中间结果误用) 是 Reviewer 自己误信本地 artifact\n  - Reviewer 16 次 ESCALATED_TO_HUMAN——遇到模糊 framing 选择 escalate 而非裁定\n  - M011 显示 Reviewer 自己也会犯 CRITICAL 误判（macro vs micro F1 混淆）然后被 Director 错误信任\n\n### 4.4 Paper Agent (58 sessions, 22.5K min)\n- **做得好**: 高密度 Read (5607) + Edit (5359)，paper_compile_and_check 726 次——LaTeX 工程链稳定\n- **做得不好**:\n  - **AI hallucinated bib entries**: M040/M041/M059 共 4 个引用条目 author 全是 AI 幻觉——这是 desk reject 红线，靠 Pre-Review Gate Step 6 才被 catch\n  - **数值 patch 顺序错乱**: M024/M025/M026/M027 显示 Paper Agent 在表格修复时不查 cross-table consistency\n  - **D248 micro-F1 vs macro-F1 metric 错位**: 临门一脚发现 construction \"+1.11pp\" 是 metric 不一致——Paper Agent 12 处 patch 全部撤销\n\n### 4.5 Worker (1335 sessions, 7.7K min, 604 errors)\n- 每个 worker session 平均 5.8 minutes（短任务为主）\n- 误诊远程进程状态 **5 次**（M021/M037/M038/M047/M049）——这是结构性问题\n- VLLM \"server-without-client\" 缺陷复发 **3 次**（M037/M038 + 14B early inference）——同样 bug 反复出现\n- M030–M032 同模型 Worker wrong-data 错误 3 次同源\n- M042 Worker 连错服务器且**返回 status=done** 这种虚假信号——signal coverage 不完整\n\n## 5. 关键发现\n\n### F1 [HARNESS] 5/22 framing 翻烧饼是\"Reviewer 单边驱动 + Director 缺乏锚点\"的系统暴露 — **严重程度: 高**\n\n**证据**:\n- D235 (5/22 04:13, \"LP dominates at all budgets\") → D236 (5/22 05:42, 同样表述) → **D237 (5/22 06:29) 作废 D236**（Reviewer #118 catch CoNLL LP -2.34pp） → D238 (5/22 09:23 \"TTS boundary conditions\" 升级) → D239 (5/22 10:38 R35 fresh 强制收窄回 NER) → D240 (5/22 11:19 R36 fresh 3.0 进一步收窄)\n- 6.5 小时内 5 次 framing 修改，前 3 次内部 Reviewer 驱动，后 2 次 fresh review 强制矫正\n- mistakes M062/M063 直接归因：\"Framing 升级时未检查证据覆盖度\"\n\n**根因**: 系统设计层面，没有 \"framing 升级 → 必须经 paper-audit 与 evidence-coverage 自检 → 再用 fresh review 复核\" 的链路。**只要 Reviewer 单方面给出 \"Framing OK\" 就可以推进**，但 Reviewer 本身在内部审稿模式下更宽容（D241 中 user 明确\"R41 我希望 fresh 模式拿干净分数\"）。\n\n**改进建议**:\n- 增加 \"framing-pivot gate\"：任一 D 决策标记 `framing_change=true` 时，必须强制 dream + fresh review 两路并行，48 小时冷却期才能 commit\n- Director 在 framing 决策时必须显式列出 \"evidence coverage table\"——每个标题关键词对应的 dataset/model/seed 数量\n\n### F2 [HARNESS + MODEL] PI 资源/目标 mandate 与 agent 实际产能不匹配，催生 8 method × 全 negative 灾难 — **严重程度: 高**\n\n**证据**:\n- 5/18 05:52 PI：\"纯诊断缺乏 positive contribution\" → 5/18 全天 13 mistakes（项目第三高）\n- 5/18 15:18 PI：\"worker 并发没有上限\"+ 12 张 5090 → 5/19–5/20 共 32 mistakes\n- 5/20 18:12 PI：\"无条件 4.5 mandate\" → D219 上调目标→ D225 (5/21 12:03) 又下调 → 4.5 commitment 仅维持 18 小时\n- 8 个 method 全 negative（MRSC/LSC/ESJ/E_θ/B1 SCD/B2 verifier/B3 prompted diversity/DGEC）\n- D170 (5/20 09:04) 自我评估：\"Construction 成功率从 ~25% 到 ~32%，远不及 70-80% 目标\"——method 探索失败显式确认\n\n**根因**: 系统设计上，PI 给的 mandate 直接进入 Director 决策上下文，但**没有 capability-check 机制**——agent 团队没办法量化\"4.5 需要 X 个 novel insight，我们最多产出 Y 个\"，于是被迫接单。MODEL 层面，单个 agent 的 long-horizon planning 不足以在 PI 指令前主动反驳 \"这个目标不现实\"。\n\n**严重程度评估**: 这 2 天浪费了 ~24 GPU-day，引入 21 + 11 = 32 mistakes，并使最终 framing 走了 D219→D238→D240 的大弯路。如果 5/20 PI 沟通时 Director 能 push back \"4.5 需要的不是更多 method，而是 mechanistic theorem\"，至少能省一半成本。\n\n**改进建议**:\n- 引入 \"target-capability gap\" 工具——目标分数与当前评分差距 >0.5 时，强制 dream + Reviewer 联合评估 \"需要多少新 evidence\"\n- PI mandate 进入系统时必须经过 Reviewer 独立 feasibility check\n\n### F3 [HARNESS] Worker 远程状态诊断不可靠，5 次 false-failed 误判 — **严重程度: 高**\n\n**证据**:\n- M021 (5/19): Worker 超时 5h，registry 误标 FAILED 但远程 nohup 训练正常\n- M037 (5/20): 14B early inference Worker 1 + Worker 2 均报 done，输出目录空\n- M038 (5/20): VLLM server-without-client 缺陷 3 次复发——Worker 启 server 不启 client，GPU 空转\n- M047 (5/20): 14B inference 第 1 次误诊为 failed，输出实际完好\n- M049 (5/21): 14B inference 第 2 次误诊，PID 252310 仍在运行 98% GPU util\n- M052 (5/21): exp_fewnerd_t05_s456 cron 误判为 failed\n- M042 (5/20): Worker 连错服务器（autodl-5090 vs autodl-5090-c）还返回 status=done\n\n**根因**: Worker 诊断协议依赖（a）输出文件存在性（b）进程存活——但 vLLM model loading 期可达 15-20 min 无输出。系统没有强制 Worker 在诊断前同时检查 `ps -p PID` + `nvidia-smi` + `ls -la output_dir` 三步。\n\n**严重程度**: 累计浪费 ~12 GPU-hours + ~3 小时人工 escalation 时间。**更危险的是 M042 类——Worker 在错误服务器上\"成功\"完成空操作返回 done**，这种 signal-noise 信号几乎无法 detect。\n\n**改进建议**:\n- Worker `submit_training_job` 后 5 min 内强制 ssh_read_only 验证 GPU util > 0\n- Worker `status=done` 必须附带 (a) output file size > threshold (b) 关键 metric 值（如 greedy F1 在预期范围）\n- 增加 `cross_validate_worker_status` 工具，对所有 cron-flagged failed 做强制 Reviewer 复验\n\n### F4 [HARNESS] 数据 provenance 链断裂导致论文数字反复回炉 — **严重程度: 高**\n\n**证据**:\n- M006: SCIERC_REF 5 值中 4 值不可溯源（5/18）\n- M013: 6 个分析脚本各自实现 F1/退化定义，**同一数据产 3 个不同 Greedy F1** + 2 种 degeneracy 定义（5/18）\n- M014: degen_rate 字段实际是 sample_f1_pct_zero（CoNLL 差 82pp）（5/18）\n- M016: unified_metrics 迁移后 FewNERD LP global ρ 0.42 → 0.22（50% 降幅），论文 4 处错引（5/18）\n- M024/M025/M026/M027: 主表/Tab5 SciERC AUROC 顺序翻转、CoNLL degen N=16 误用、headroom 用 LLaMA 行（5/19）\n- M057: CoNLL v4 3-seed 混合 exp002 + MF4v2 两个 pipeline（5/21）\n- M069: 主表 SciERC EM AUROC .749 是 9.1σ copy-paste 错误（5/23）\n- M070: 5-seed construction +1.11pp 是 instance-averaged vs micro-F1 metric 不一致（5/24）\n\n**根因**:\n1. 论文表格数字**手动填写**而非脚本自动生成（M024 显式记录）\n2. 同一指标多脚本独立实现（M013 unified_metrics 出现前）\n3. 数据 patch 时**不查 cross-table consistency**（M025）\n4. registry 中实验状态与服务器实际不一致（M058 跨服务器去重失败）\n\n**严重程度**: 每一项都可能成为 ARR reviewer 投诉的 \"不可复现\" 红线。M016 的 50% ρ 降幅如果未及时 catch，整篇论文 QE 章节立刻崩塌。M069/M070 在 DDL 前 48 小时才被发现——**论文 freeze 时数字稳定性是历史最低点**。\n\n**改进建议**:\n- 引入 \"paper_consistency_audit\" 工具，每次 Paper Agent edit 后强制全文 grep 数值 + 与 registry/report.json 交叉验证\n- 论文数字必须有 `provenance.yaml` 条目：`{ value, exp_id, metric_key, computed_at }`\n- 主表禁止手动填写，强制由 `generate_main_table.py` 从 registry 生成\n\n### F5 [HARNESS] 文献/引用幻觉是 desk-reject 红线，靠人工兜底才 catch — **严重程度: 高**\n\n**证据**:\n- M040/M041: 3/96 bib entries 作者 AI 幻觉（chen2025twofailures / wen2025abstention / liu2025uqcc），URL 指向错误论文（5/20）\n- M059: ma2024selfimproving 全 5 个作者 AI 幻觉，正确第一作者为 Xie（5/21）\n- 张默涵 5/23 17:07 介入：反复追问 reference verification 才 catch M059\n\n**根因**: Paper Agent 生成 bib entries 时\"标题正确 + 作者幻觉\"是典型 LLM 失效模式。系统缺少强制 Semantic Scholar API 验证。\n\n**改进建议**:\n- \"reference-audit\" skill 必须在 Paper Agent **每次** 新增 bib 时自动触发，不依赖 pre-review gate\n\n### F6 [MODEL] 数学/统计概念在跨 worker 复制时系统性丢失 — **严重程度: 中**\n\n**证据**:\n- M068 (5/22): Worker 把 global k=57 Holm p=0.055 全文替换为 seed-replication k=5 p=0.013，混淆两个统计框架，影响 12+ 处\n- M009/M010 (5/18): span-based vs text-based matching 多次混淆\n- M013 (5/18): 6 个独立 F1/degeneracy 实现\n- D227 (5/21): \"代码库中 3 个 MV 实现使用不同 threshold + entity match\"\n\n**根因**: 这不完全是 harness 问题——长上下文中保持\"两个统计框架的语义区分\"对当前模型是困难的。Worker 接到 \"全文替换 X→Y\" 指令时倾向于做精确字符串替换而不验证语义。\n\n**改进建议**: 涉及统计/数学概念的全文修改禁止 Worker 独立执行，必须 Agent 亲自做。Director 指令应强制要求\"列出修改清单 + 每处的语义检查\"。\n\n### F7 [HARNESS] Dream 机制对 framing 健康度的检测能力不足 — **严重程度: 中**\n\n**证据**:\n- Dream 1（5/14 09:33）三档全 3/6，结构性问题 ID 完整（缺 baseline / novelty 薄 / formula 不一致）\n- Dream 2（5/14 10:53）三档全 3/6（持平）——Dream 系统未能给出 \"what changed since last dream\"\n- Dream 3（5/14 20:32）三档评分模式相似——dream 系统**对框架质量改进的 sensitivity 几乎为 0**\n- Dream 5（5/15）+ Dream 6（5/16）后系统连续输出 3.0/5 plateau，但实际 fresh review 给到 3.5（D224 R27）\n- Dream/fresh review 的相关性极弱\n\n**严重程度**: 项目 5/14–5/16 共做了 6 次 dream，没有一次提供了 fresh review 才发现的 \"scope overclaim\" 问题。Dream 失去了 early-warning 作用。\n\n**改进建议**: Dream 应**预先训练**到与 fresh review 评分对齐（calibration）；或减少 dream 频率，增加 fresh review 频率。\n\n### F8 [HARNESS] 跨服务器资源调度引入大量\"虚假状态\"事故 — **严重程度: 中**\n\n**证据**:\n- M020/M023/M035 (5/19): registry GPU 字段格式不规范 / 手动启动绕过 cron / 未注册 GPU 进程\n- M042 (5/20): Worker 连错服务器（autodl-5090 vs autodl-5090-c）+ 返回虚假 done\n- M053/M058 (5/21): 重复启动 / 跨服务器数据未在 registry 标注\n- M065/M066 (5/22): kill_job 未实际终止 vLLM 子进程 + 3 个 PREPARING 实验未启动空转 9h\n\n**根因**: 用户 5/18 一次性给 12 张卡（autodl-5090 + autodl-5090-b + autodl-5090-c）后，registry 缺少 \"server-aware\" 一致性检查。Agent 派发 Worker 时 server alias 容易混淆。\n\n**改进建议**: registry 必须强制 `server` + `gpu_ids` 双字段，submit_training_job 内置 hostname 验证。\n\n### F9 [MODEL] Long-horizon planning 失效，11 天内 5 次重大 framing reframe — **严重程度: 中**\n\n**证据**:\n- D018 (5/14): correlation-selection gap framing 建立\n- D130 (5/18): systemic reframe 8 项\n- D219 (5/20): 目标 3.5→4.5\n- D237 (5/22): dataset-dependent + diagnostic primary\n- D238 (5/22): TTS boundary for structured prediction\n- D239/240: 回退 NER\n\n**根因**: agent (Director) 在长上下文中难以维持 \"previously rejected hypothesis\" 的标记——D008 已排除 RE-primary，D018 已排除 best-of-N improvement，但 5/20 PI 一句\"加 positive contribution\"，Director 又开始 method 探索；5/22 fresh review 才 hard reset。**memory.md 134 行 + paper_framing.md 87 行不足以承载 11 天 248 D 决策的状态机**。\n\n**严重程度**: 每次 framing 重构需要 12-24 小时（paper edit + audit + dream），累计成本 ~3 个工作日。\n\n**改进建议**:\n- 引入 \"rejected_hypothesis.yaml\"——每次 framing 撤销时显式 log 被排除的方向 + 排除理由 + 重启 gate（什么新证据才能 unblock）\n- Director 系统 prompt 加 \"before pivoting, list past 3 framing decisions and verify new framing doesn't revisit a previously-rejected direction\"\n\n### F10 [HARNESS] 错题本 (mistakes.yaml) 未能真正阻止同类错误复发 — **严重程度: 中**\n\n**证据**:\n- VLLM server-without-client 在 M037/M038 后明确写入 prevention，但 M037 中的 \"13\" 同类问题再次出现\n- Worker false-failed 诊断 M021 (5/19) 后明确 prevention，但 M047 (5/20) / M049 (5/21) / M052 (5/21) 反复出现 4 次\n- wrong-model-data M030 (5/20 06:00) → M031 (5/20 07:00) → M032 (5/20 08:00) 同日 3 次\n- 跨表 metric 不一致 M013 (5/18) → M057 (5/21) → M070 (5/24) 横跨 6 天\n\n**根因**: mistakes.yaml prevention 字段写入后，**没有任何 enforcement 机制**让后续 Worker 在执行同类任务前先 grep mistakes.yaml。完全靠 Agent 自己的 context 记忆。\n\n**改进建议**:\n- 增加 `pre_spawn_worker` hook：根据 task 类型自动 attach 相关 prevention rule\n- mistakes.yaml 中 high-severity + repeated > 2 次的应该升级为 constraints.yaml 强约束\n\n### F11 [MODEL] Agent 自我纠错能力弱，全靠 Reviewer 兜底 — **严重程度: 中**\n\n**证据**:\n- 70 条 mistakes 中，**几乎全部是 Reviewer 或独立 Worker 发现**，Agent 自查发现率 < 10%\n- M050: Director 引用本地 artifact AUROC 0.920 直接报告给 PI 和 Paper Agent，未让 Reviewer 验证服务器端最终输出（5/21）\n- M067: 论文中 \"LP-best +8pp on Few-NERD\" 无任何数据支撑，被 Reviewer 排查后确认是 number-stitching 幻觉\n- M069: 主表 SciERC EM AUROC 9.1σ 偏差，Paper Agent 与 Reviewer 都未在初始 patch 时 catch\n\n**根因**: MODEL 层面，agent 在长上下文中对 \"我刚才写的数字是否正确\" 的元认知较弱。即使 mistakes.yaml 已记录类似错误，agent 复用旧数据时不主动验证。\n\n**改进建议**: 论文相关 patch 任务必须经过独立 Reviewer 在不同 session 复算——不能由 Paper Agent + 同一 Reviewer 闭环验证。\n\n### F12 [HARNESS] 用户对话与 agent 状态机不同步 — **严重程度: 低**\n\n**证据**:\n- 5/22 14:20 用户：\"我希望选择 fresh 拿到干净的得分，不会选择 Continue 模式\"——但 Director 5/22–5/23 多次 default 推荐 Continue 模式\n- 5/22 10:30 用户：\"这个问题（scope overclaim）出现很多遍了\"——表明用户感受到的重复 ≠ agent 内部认知的\"已修复\"\n- 5/23 03:13 用户：\"实验都结束了？\"——agent 实际还在跑 6 个实验\n\n**根因**: ralph_loop 把用户飞书消息注入 Director context，但没有\"用户偏好持久化\"机制。每次 BOOT 后用户偏好（如 \"always use fresh mode\"）丢失。\n\n**改进建议**: 用户消息中的偏好（识别 mode \"I prefer X\" / \"don't do Y\"）自动 promote 到 constraints.yaml 或 user_preferences.yaml，每次 BOOT 强制载入。\n\n### F13 [HARNESS] Paper Agent 多轮 figure 优化对最终评分贡献不显著 — **严重程度: 低**\n\n**证据**:\n- 5/23 12:36 周俊伟：\"Figure 1 必须用 PaperBanana 重画\" → 5/23 14:40/15:04/15:10/15:53/16:00 共 4 轮反复\n- paper-figure-optimize 角色 4 session，paper-audit-review-visual 24 session\n- 但 R36/R40 fresh review 仍 3.0，figure 在审稿意见中**不是核心扣分项**\n\n**严重程度**: 占用了 DDL 前 ~6 小时的 polish 时间，**机会成本可观**——这段时间本可以做 R36 reviewer concerns 的 mechanistic 深化。\n\n**改进建议**: figure polish 应在 framing 稳定后才启动；framing 反复期不投入 figure 工时。\n\n---\n\n**总结**: 这是一个**核心 negative finding 真实、但被 system + model + PI mandate 三方拉扯导致执行成本极高**的项目。最终 ~3.0 fresh score 与\"NER-only diagnostic\"的实际科研价值匹配，与用户期望的 4.5 不匹配。系统层面最重要的 3 个改进点：(1) framing-pivot gate (F1+F9) (2) Worker 状态诊断协议加固 (F3+F8) (3) 论文数据 provenance 自动化 (F4+F5)。模型层面，long-horizon planning 与跨工作流元认知是上限——目前 agent 团队的 capability ceiling 不足以在没有 hard system gate 时维持 11 天 240+ 决策的一致性。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "30a74bff-f5df-44d5-9c73-5ea38555502c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 125_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "08930b7d-ae6d-4782-81c0-dfc0451e729d",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863"
}
```

---


### Assistant

_source line 126 · 2026-05-31T14:31:27.170Z_

报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md`。

**核心结论**：
- 项目 11 天产出 ~3.0 fresh score（Findings 区间），未达 PI 4.5 mandate，与 NER-only diagnostic 实际价值匹配
- 248 D 决策、70 mistakes（46 high-severity）、5 次重大 framing reframe
- **13 个 finding**，归因：HARNESS 8 / HARNESS+MODEL 1 / MODEL 3 / 其它 1
- 最严重的 5 个问题：(F1) framing 翻烧饼 + (F2) PI mandate-capability 不匹配 + (F3) Worker 远程状态诊断不可靠 + (F4) 数据 provenance 链断裂 + (F5) bib 引用 AI 幻觉
- 人工干预分析：5/18 PI "加 positive contribution" + 5/20 PI "4.5 mandate" 是项目最关键的 2 个负面外部冲击，催生 2 天 8 method × 全 negative + 21 mistakes/day 的灾难期

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08930b7d-ae6d-4782-81c0-dfc0451e729d",
  "isSidechain": false,
  "requestId": "req_011CbaoqAHANyh2mCPgUDbdp",
  "type": "assistant",
  "uuid": "1d13b2e4-f0fa-4da8-95e7-6342abe18339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JxZNnZnJo9K5Y1AbUvwHFv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17587,
      "cache_read_input_tokens": 226376,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17587,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Runtime record

_source line 127_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "1d13b2e4-f0fa-4da8-95e7-6342abe18339",
  "sessionId": "0ab421e3-b321-43b0-9376-3da2710e4863"
}
```

---
