# Idea Brief: StructTTS: Characterizing When Test-Time Compute Scaling Works for Structured Information Extraction


- **Idea ID**: `idea_005`
- **Created**: 2026-05-11
- **Approved**: 2026-05-11
- **Source**: foreign:be-idea-gen-0509-6
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission: May 25, 2026), AACL-IJCNLP 2026 (ARR submission: May 25, 2026; shared cycle with EMNLP, binding choice at submission), AAAI 2027 (abstract: ~Jul 25, paper: ~Aug 1, 2026)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.

Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.

Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.

Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.

Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Test-time compute scaling (TTS) has been systematically studied for reasoning (math, coding, QA) where it excels, shown ineffective for knowledge-intensive tasks (arXiv 2509.06861), and demonstrated to produce mixed or negative results for agentic structured actions due to vote-splitting (CATTS, arXiv 2602.12276) and the verification gap (General AgentBench, arXiv 2602.18998). Yet an entire class of tasks — structured prediction (IE, semantic parsing, table extraction) — remains empirically uncharted on the TTS applicability spectrum. This gap is not merely academic: the TTS survey (arXiv 2503.24235) and 'Inference-Time Scaling for Complex Tasks' (arXiv 2504.00294) systematically evaluate math, STEM, planning, NP-hard, navigation, and spatial reasoning, but none examines structured prediction tasks where outputs are schema-constrained objects rather than free-form text or step-by-step derivations. Meanwhile, existing IE refinement approaches explore only sequential depth: SCIR (AAAI 2026) trains dual-path correction models achieving 5.27% avg F1 improvement at ~2x inference cost, VerifiNER (ACL 2024) performs post-hoc NER-only verification using external knowledge bases. Neither explores the complementary parallel breadth strategy from TTS. The central open question is not 'can TTS improve IE F1?' but rather 'where does structured prediction sit on the TTS applicability spectrum, and what structural properties determine TTS effectiveness?' — a question with implications far beyond IE, extending to semantic parsing, code generation, and any task producing schema-constrained outputs.

## Opportunity / Why Now

Structured prediction occupies a theoretically distinctive position on the TTS applicability spectrum, but this position has never been empirically validated. Three structural properties create testable hypotheses about TTS effectiveness: (1) **The verification gap is closable**: The General AgentBench (arXiv 2602.18998) identifies the verification gap — inability to reliably select correct candidates from parallel samples — as a fundamental bottleneck for parallel TTS. For general agent tasks, no training-free verifier exists. IE is unique: schema-constrained outputs enable training-free structural verification (type validity, argument referencing, cross-candidate consistency via IoU matching), potentially closing this gap without learned reward models. This is the verification asymmetry condition under which TTS provides maximal benefit (arXiv 2512.02304). (2) **Vote-splitting is structurally resolvable**: The vote-splitting problem that degrades TTS for web agents (CATTS, arXiv 2602.12276) arises because semantically equivalent actions have different surface forms. For IE, IoU-based structural matching directly resolves this — soft-matching entity spans, relation tuples, and event templates handles surface variation that defeats string-equality voting. (3) **Flat output structure hypothesis**: Unlike chain-of-thought reasoning where sequential refinement dominates (The Sequential Edge, arXiv 2511.02309), IE outputs are complete structured objects with no intermediate reasoning chain. This may make parallel exploration more natural than sequential refinement — but equally, it may mean there is less to 'explore' (the output space is more constrained), potentially causing early saturation. This is an empirical question. However, constrained decoding may reduce candidate diversity ('The Hidden Cost of Structure,' RANLP 2025), potentially undermining the breadth strategy. By mapping these properties to empirical outcomes, we produce a TTS applicability taxonomy for structured prediction — a contribution valuable regardless of absolute F1 numbers and with implications for semantic parsing, code generation (cf. S*, EMNLP Findings 2025), text-to-SQL (cf. Agentar-Scale-SQL, arXiv 2509.24403), and table extraction.

## Landscape (SOTA & Limitations)

Test-time scaling (TTS) has been systematically studied across multiple task types with sharply varying results. For reasoning (math, coding, QA), TTS is well-established (ICLR 2025; Forest-of-Thought, ICML 2025; S* for code generation, EMNLP Findings 2025). For knowledge-intensive tasks, TTS fails (arXiv 2509.06861). For structured web actions, uniform scaling degrades performance due to vote-splitting (CATTS, arXiv 2602.12276). For general agents, both sequential and parallel scaling show limited effectiveness due to context ceiling and verification gap respectively (General AgentBench, arXiv 2602.18998). The Sequential Edge (arXiv 2511.02309) shows sequential self-consistency beats parallel in 95.6% of configurations for chain-of-thought reasoning — but evaluates only math/science tasks. Adaptive Parallel Reasoning (arXiv 2504.15466, BAIR 2026) demonstrates coordinated parallel inference can outperform sequential when properly coordinated. 'Inference-Time Scaling for Complex Tasks' (arXiv 2504.00294) evaluates 8 challenging task types but omits structured prediction entirely, noting that TTS advantages 'vary across tasks and diminish as problem complexity increases' — underscoring the need for task-type-specific characterization. The Parallel Test-Time Scaling with Multi-Sequence Verifiers paper (arXiv 2603.03417, Mar 2026) shows joint verification across candidates outperforms isolated scoring, achieving same accuracy at half the latency. For text-to-SQL, Agentar-Scale-SQL (arXiv 2509.24403) achieves #1 on BIRD leaderboard via hybrid TTS (parallel + sequential + RL-trained verification), demonstrating TTS can work for structured prediction when verification is available. For IE specifically: SCIR (AAAI 2026) applies iterative single-candidate refinement via fine-tuned dual-path correction models, achieving 5.27% average F1 improvement at ~13.33% inference overhead (~2x cost with 2 iterations) across 11 datasets (WikiEvents, RAMS, CrossNER, FewRel, Wiki-ZSL for English) — but requires task-specific training and does not evaluate on ACE05, SciERC, TACREV, or MAVEN. VerifiNER (ACL 2024) performs post-hoc NER-only verification using UMLS knowledge bases. Neither explores parallel multi-candidate generation with structural scoring. On the generation side, XGrammar (MLSys 2025) enables near-zero overhead constrained decoding with 95-99% conformance rates, but 'The Hidden Cost of Structure' (RANLP 2025) demonstrates constrained decoding can degrade task performance and reduce output diversity. DCCD (arXiv 2603.03305) mitigates this via draft-then-constrain generation. SemDiD (NeurIPS 2025) achieves diversity improvement through semantic-guided decoding, and the diversity-fidelity trade-off (arXiv 2502.11027) shows diverse prompts yield up to 10.8% relative gains. The Radial Consensus Score (arXiv 2604.12196, Apr 2026) advances best-of-N selection beyond majority voting but targets free-form text. GLiNER2 (arXiv 2507.18546) demonstrates schema-driven IE is a maturing paradigm but does not address inference-time scaling. The gap: no work characterizes TTS boundary conditions for structured prediction as a task class, no work empirically maps where IE sits on the TTS applicability spectrum, and no work compares parallel vs. sequential TTS with training-free verification for extraction.

## Proposed Approach

We propose StructTTS, a framework for characterizing the boundary conditions of test-time compute scaling for structured prediction, using information extraction (NER, RE, EE) as the empirical testbed. The central goal is not merely to improve IE F1, but to produce a TTS applicability taxonomy for structured prediction — determining when, why, and to what extent TTS helps for tasks producing schema-constrained outputs, and how IE compares to reasoning, knowledge, and agentic tasks on the TTS spectrum.

Given input text and a target IE schema, we use Qwen3-8B as the primary model (with Qwen3.6-27B for cross-model scaling on 2 key datasets) to generate N schema-valid candidate extractions via constrained decoding (XGrammar) with diversity-enhanced sampling, producing structured JSON of entities, relations, or events.

**Diversity-Enhanced Candidate Generation:**
To counter diversity loss under constrained decoding (RANLP 2025), we employ three complementary strategies: (a) temperature sampling with T ∈ {0.5, 0.7, 0.9, 1.1, 1.3}, (b) diverse prompt templates — paraphrased extraction instructions with varied schema element orderings, following the diversity-fidelity trade-off principle (arXiv 2502.11027), and (c) nucleus sampling with varied top-p ∈ {0.7, 0.85, 0.95}. We include an explicit diversity measurement experiment, computing pairwise entity-level Jaccard distance and structural edit distance across candidates at N ∈ {8, 16, 32}. If diversity remains insufficient under constrained decoding, we evaluate DCCD-style draft-then-constrain generation (arXiv 2603.03305) as an alternative.

**Structural Verification (2 components):**
(1) **Structural self-consistency aggregator (primary signal):** Extends majority voting to complex IE structures via partial-match alignment — directly closing the verification gap identified in General AgentBench (arXiv 2602.18998) and addressing the vote-splitting problem from CATTS (arXiv 2602.12276) by matching semantically equivalent but textually different extractions:
- *Entity matching:* Given entities e_i = (start_i, end_i, type_i) and e_j = (start_j, end_j, type_j), compute character-span IoU = |[start_i,end_i] ∩ [start_j,end_j]| / |[start_i,end_i] ∪ [start_j,end_j]|. Match if IoU ≥ τ_span (default 0.5) AND type_i == type_j. Match score = IoU.
- *Relation matching:* Given relations r_i = (head_i, tail_i, rel_type_i) and r_j, match if head entities soft-match AND tail entities soft-match AND rel_type_i == rel_type_j. Match score = mean(head_IoU, tail_IoU).
- *Event template matching:* Given events ev_i = (trigger_i, event_type_i, {role_k: arg_k}) and ev_j, match if triggers soft-match (IoU ≥ τ_span) AND event_type_i == event_type_j. For cross-sentence arguments (WikiEvents), argument matching uses document-level character offsets rather than sentence-relative positions. Match score = trigger_IoU × (number of roles with soft-matched arguments / total roles in union).
- *Agreement score:* For candidate C_i with extracted element set E_i, compute agreement(C_i) = (1/|E_i|) × Σ_{e ∈ E_i} [(1/(N-1)) × Σ_{j≠i} max_{e' ∈ E_j} match_score(e, e')]. This measures how well each element in C_i is corroborated by other candidates.

(2) **Lightweight schema sanity filter (secondary):** Detects residual semantic inconsistencies not caught by format-level constrained decoding: (i) relation arguments referencing entities not present in the same extraction, (ii) entity types incompatible with their relation/event roles as defined by the schema. We explicitly acknowledge this component is secondary: under constrained decoding with a competent 8B model, format violations are near-zero (0-0.97%), and these semantic checks are expected to fire infrequently. We measure and report the firing rate as an empirical datapoint. This filter becomes more valuable for non-constrained outputs (e.g., DCCD drafts) or weaker models, and its contribution is assessed via ablation rather than claimed as a major novelty.

**Selection Strategies:**
(a) Verifier-scored best-of-N: select the candidate with highest combined score (α × sanity_score + (1-α) × agreement), where α is tuned on dev sets.
(b) Structural weighted voting: merge candidates via partial-match aggregation — for each unique entity/relation/event cluster (formed by transitive closure of soft matches), retain the element with highest weighted support.
(c) Verifier-guided beam search: expand partial extractions (entity → relation → event) and prune branches with low scores at each stage.

**SCIR Head-to-Head Comparison (primary result, not afterthought):**
We elevate the compute-normalized comparison with SCIR to a primary result. Three scenarios:
(a) **If SCIR code (github.com/Sheehan-Fang/SCIR) becomes publicly accessible**: re-run SCIR on all 5 of our datasets using Qwen3-8B as the base model (~12h A100 for training + inference). Present side-by-side F1 and F1-improvement-per-FLOP at matched compute budgets: SCIR at 2x cost vs. StructTTS at N=2,4,8,16.
(b) **If SCIR code is unavailable** (the GitHub link returned 404 as of May 2026): implement a faithful training-free sequential refinement baseline — 2-pass iterative self-correction where each subsequent extraction receives the previous extraction as context, without SCIR's trained dual-path module. This isolates the sequential-depth strategy from SCIR's task-specific training. Compare against SCIR's published WikiEvents numbers as a reference point.
(c) **In either case**: present the core efficiency question as a primary finding — at what N does training-free parallel TTS match SCIR's trained sequential refinement? If StructTTS at N=4 (4x cost, no training) exceeds SCIR's 5.27% avg improvement (2x cost, requires training), the training-free advantage is compelling. If SCIR wins on efficiency, that is equally informative: trained sequential depth beats training-free parallel breadth for IE, consistent with The Sequential Edge, and a key datapoint for the taxonomy.

**Sequential TTS Baseline (addressing The Sequential Edge, arXiv 2511.02309):**
Generate K candidates sequentially where each subsequent extraction receives the previous extraction as context, using inverse-entropy voting for final selection. Compare: (i) parallel best-of-N with structural verification vs. (ii) sequential refinement with inverse-entropy voting vs. (iii) SCIR-style iterative correction (trained or approximated), at matched token budgets.

**Evaluation:** 5 core datasets across all major IE subtasks: ACE05 (NER+RE+EE, ~40 test docs), SciERC (scientific NER+RE, ~500 test abstracts), TACREV (RE, 2K-instance stratified subset from 15.5K test), MAVEN (event detection, ~710 test docs), and WikiEvents (event argument extraction, ~100 test docs). Post-review additions (if accepted): DocRED, Few-NERD (2K subset), RAMS.

**Baselines:** (i) single-pass without constrained decoding, (ii) single-pass with constrained decoding (XGrammar), (iii) SCIR iterative self-correction (re-run or faithful approximation), (iv) VerifiNER (NER benchmarks only), (v) naive self-consistency voting adapted for IE, (vi) best-of-N with random selection (compute control), (vii) DCCD draft-conditioned constrained decoding (single-pass), (viii) sequential refinement with inverse-entropy voting (The Sequential Edge baseline, at matched token budget).

**First-class contributions — taxonomy first, then scaling curves and efficiency:**
(1) **TTS applicability taxonomy for structured prediction (CENTRAL contribution):** Characterize IE subtasks along two axes — combinatorial ambiguity (number of valid extraction alternatives per instance, measured via oracle diversity at high N) and verification signal strength (how many schema constraints are checkable, plus self-consistency agreement variance). Map each subtask's position to its empirical TTS scaling behavior. This taxonomy answers: 'when does TTS help for structured prediction?' and provides a predictive framework applicable beyond IE to semantic parsing, text-to-SQL, code generation, and table extraction. The taxonomy is a standalone contribution valuable regardless of absolute F1 numbers — it provides the first empirical characterization of structured prediction on the TTS spectrum alongside reasoning (where TTS works), knowledge (where it fails), and agentic tasks (where it's mixed).
(2) F1-vs-N scaling curves (N=1 to 48) across all 5 datasets, identifying which IE subtasks exhibit sustained gains vs. early plateaus, and the sweet-spot N where marginal F1 gain per additional candidate becomes negligible.
(3) **SCIR compute-matched efficiency comparison (primary result):** F1-improvement-per-FLOP for StructTTS at N=2,4,8,16 vs. SCIR at 2x cost vs. sequential baseline vs. single-pass with larger model (Qwen3.6-27B). Explicitly identify whether training-free parallel breadth or trained sequential depth is more compute-efficient for IE.
(4) Parallel vs. sequential TTS comparison at matched token budgets, empirically testing whether The Sequential Edge's findings transfer to structured extraction.
(5) Diversity analysis: measure and report candidate diversity at N ∈ {8, 16, 32} under different sampling strategies, and analyze whether diversity correlates with scaling effectiveness.
(6) Cross-model scaling: test whether TTS with Qwen3-8B can match single-pass Qwen3.6-27B performance.
(7) **Compute-normalized Pareto analysis:** F1 improvement per H100-hour, comparing small-model × N candidates vs. single-pass large model vs. SCIR iterative correction.

**Contingency Plan (addressing timeline risk):**
Total timeline: 16 days (8-10 days experiments, ~6 days writing). Scope-reduction triggers with priority ordering:
- **Core (must complete, days 1-8):** Scaling curves on 5 datasets with Qwen3-8B, SCIR comparison (re-run or approximation), sequential baseline on 3 datasets (ACE05, SciERC, WikiEvents).
- **Day 10 trigger:** If core experiments incomplete, drop Qwen3.6-27B experiments entirely. Justify as 'cross-mode

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$250-400 (~2500-4000 turns for experiment design, code generation, SCIR adaptation, diversity analysis, scaling curve analysis, taxonomy construction, and paper drafting)', 'estimated_gpu_cost': '$495 (330h × ~$1.50/hr)', 'gpu_hours': '~330h A100 80GB (≈190h H100 equivalent; exhaustive search over N values 1-48, temperatures, diversity strategies, verifier weight combinations, across 5 datasets × 2 models with subsetted TACREV + sequential baseline + SCIR comparison)', 'gpu_utilization': 'High (>90% active); agent queues experiments back-to-back, automatically parses results and launches follow-up ablations. SCIR re-running and diversity analysis overlap with main experiments.', 'risk_note': 'Agent may over-explore diversity strategies on datasets where constrained decoding already provides sufficient variety; ~10-15% of GPU hours may go to unproductive exploration. SCIR code unavailability would require agent to implement sequential approximation from paper description, risking unfaithful reproduction.', 'speed_bottleneck': 'GPU count is primary bottleneck — Qwen3-8B experiments with N=48 across 5 datasets complete in ~4-5 days on 2 GPUs. SCIR training + inference adds ~0.5 days. Qwen3.6-27B on 2 datasets with N≤16 adds ~1.5 days.', 'team': '0 (initial setup, schema definitions, and constrained decoding configuration only)', 'timeline': '8-10 days with 4 GPUs; ~14 days with 2 GPUs (contingency triggers at days 10, 12, 14)'}
- **human_in_loop**: {'claude_api_cost': '$100-180 (~1000-1800 turns at ~$0.10/turn Opus)', 'estimated_gpu_cost': '$428 (285h × ~$1.50/hr)', 'gpu_hours': '~285h A100 80GB (≈164h H100 equivalent)', 'gpu_utilization': 'Moderate (50-60%); agent automates experiment scripting across 5 datasets, result parsing, diversity metric computation, SCIR re-running, and ablation scheduling. Human gates verifier design choices, validates partial-match alignment correctness, interprets scaling curves and taxonomy construction.', 'risk_note': 'SCIR code availability uncertain (GitHub link returned 404 as of May 2026); if unavailable, training-free sequential approximation adds ~5h but produces weaker comparison. Agent may generate subtly incorrect IoU-based matching logic for event arguments with cross-sentence spans (WikiEvents); human must validate matching functions before full experiment sweeps.', 'team': '1 researcher, ~35min/day reviewing agent-proposed matching algorithms, SCIR comparison analysis, and taxonomy characterization', 'timeline': '4-7 weeks (with contingency triggers at days 10, 12, 14)'}
- **manual**: {'estimated_gpu_cost': '$375 (250h × ~$1.50/hr avg on neocloud providers)', 'gpu_hours': '~250h A100 80GB (≈144h H100 equivalent)', 'gpu_utilization': 'Low effective utilization (~25%); GPU idle during verifier logic development, diversity metric implementation, scoring function iteration, and scaling curve analysis. Compute concentrated in batch inference bursts.', 'team': '1-2 researchers', 'timeline': '2.5-4 months'}

## Key References

- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)
- Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning (ICML 2025)
- The Art of Scaling Test-Time Compute for Large Language Models (arXiv 2512.02008, Dec 2025)
- Scaling Test-Time Compute Without Verification or RL is Suboptimal (arXiv 2502.12118, Feb 2025)
- When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers (arXiv 2512.02304, Dec 2025)
- Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet (arXiv 2509.06861, Sep 2025)
- The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute (arXiv 2511.02309, Nov 2025)
- Agentic Test-Time Scaling for WebAgents (CATTS) (arXiv 2602.12276, Feb 2026)
- Benchmark Test-Time Scaling of General LLM Agents (arXiv 2602.18998, Feb 2026)
- Inference-Time Scaling for Complex Tasks: Where We Stand and What Lies Ahead (arXiv 2504.00294, Apr 2025)
- Learning Adaptive Parallel Reasoning with Language Models (arXiv 2504.15466, Apr 2025; BAIR blog May 2026)
- Parallel Test-Time Scaling with Multi-Sequence Verifiers (arXiv 2603.03417, Mar 2026)
- S*: Test Time Scaling for Code Generation (EMNLP Findings 2025, arXiv 2502.14382)
- Agentar-Scale-SQL: Advancing Text-to-SQL through Orchestrated Test-Time Scaling (arXiv 2509.24403, 2025)
- A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well? (arXiv 2503.24235, Mar 2025)
- On the Effect of Sampling Diversity in Scaling LLM Inference (arXiv 2502.11027, Feb 2025)
- Semantic-guided Diverse Decoding for Large Language Models (SemDiD, NeurIPS 2025)
- Draft-Conditioned Constrained Decoding for Structured Generation in LLMs (DCCD, arXiv 2603.03305, Mar 2026)
- SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema (AAAI 2026)
- VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models (ACL 2024)
- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)
- The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance (RANLP 2025)
- Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score (arXiv 2604.12196, Apr 2026)
- GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface (arXiv 2507.18546, Jul 2025)
- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv 2026)
- MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction (arXiv 2025)
- Ranked Voting based Self-Consistency of Large Language Models (ACL Findings 2025)
- Grammar-constrained decoding for structured information extraction with fine-tuned generative models (Frontiers AI 2024)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptional specification — IoU matching algorithms are precisely defined for entities/relations/events, compute breakdown is tabular and verifiable, SCIR comparison has explicit scenario branches (code available vs. not), and contingency plan specifies exactly what gets cut and when.', 'score': 5}**/5
  - feasibility: **{'rationale': '~164h H100 is well within budget. Both models (Qwen3-8B, Qwen3.6-27B) are publicly available. All 5 datasets are standard. The 16-day timeline is tight but the explicit contingency triggers (days 10/12/14) with prioritized scope cuts make it manageable. SCIR uses the same Qwen3-8B model, enabling direct comparison if code becomes available.', 'score': 4}**/5
  - impact: **{'rationale': 'The taxonomy contribution generalizes beyond IE to semantic parsing, text-to-SQL, code generation, and table extraction. The empirical characterization provides actionable guidance for the community on when TTS is worth the compute for structured tasks. The SCIR efficiency comparison (training-free parallel vs. trained sequential) answers a practical question regardless of which wins.', 'score': 4}**/5
  - novelty: **{'rationale': 'The TTS applicability taxonomy for structured prediction fills a verified gap — no existing work characterizes where IE sits on the TTS spectrum. The combination of IoU-based structural self-consistency for cross-candidate verification with constrained decoding for IE is genuinely new, though individual components (best-of-N, IoU matching, constrained decoding) exist separately.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果

**中稿概率**: [34.0% - 44.0%] 中位 38.0%

### 实施评估
- **计算资源**: ≤164h H100（单卡），主要用于 Qwen3-8B（5 datasets, N=1-48）和 Qwen3.6-27B（2 datasets, N≤16）的推理。无训练开销。按当前云计算价格约 $500-$800。学术机构通常可获取。
- **数据需求**: ACE05（需 LDC license，大多数 NLP 实验室已有）、SciERC（公开）、TACREV（公开，用 2K subset）、MAVEN（公开）、WikiEvents（公开）。均为标准 IE benchmark，无数据获取障碍。
- **人工介入**: 无需人工标注或人工评审。实验全自动化。仅需研究者进行结果分析和论文撰写。
- **训练需求**: **无模型训练**。完全 training-free 方法（constrained decoding + sampling + aggregation）。仅需推理 API 或本地部署 Qwen3 系列模型。
- **新 Benchmark**: 不需要。使用现有 5 个标准 IE benchmark。taxonomy 本身是概念性贡献而非数据集。
- **预估周期**: 约 3-4 周。实验执行约 2 周（含 contingency buffer），分析+写作约 1-2 周。Proposal 已设置 day 10/12/14 的 scope reduction triggers，整体时间控制合理。

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题]** — 从 "characterizes the boundary conditions of TTS for structured prediction" 改为 **"Predictive Taxonomy of Test-Time Compute Scaling for Structured Prediction: Evidence from Information Extraction and Text-to-SQL"**。标题直接点明"predictive taxonomy"，并限定实证范围。 — 命中 Novelty（明确贡献类型）+ Significance（scope 诚实）

2. **[Introduction 第一段 / 核心定位]** — 增加 **"Whether vs. How" framing**：现有 TTS 文献（Snell et al., CaTS, Sequential Edge）解决"给定 TTS 有效，如何最优分配 compute"；本文解决上游决策——"对于一个结构化预测任务，TTS 是否值得投资"。一句话定位，让 reviewer 在 30 秒内抓住贡献的不可替代性。 — 命中 Novelty（与先行工作的区分度）

3. **[核心叙事结构 / 全局重构]** — 将 taxonomy 从"实验后的描述性总结"**反转为"先验预测框架 + IE 作为 falsification test"**。Introduction 先提出两轴和四象限预测矩阵，明确 NER/RE/EE 各自的象限位置，然后声明实验目的是验证/否证这些预测。这一重构不需要额外实验，纯粹是 framing 升级，但从根本上改变了 reviewer 对 novelty 的感知——从"做了实验总结规律"（empirical-only，novelty 低分）到"提出可检验框架 + 用实验验证"（hypothesis-driven，novelty 中高分）。 — 命中 Novelty（从描述性到预测性）+ Technical Soundness（hypothesis-driven 实验设计）

4. **[Method / 新增 Axis Operationalization Protocol 章节]** — 为两轴提供**具体的量化定义和计算公式**：
   - **CA_theo（理论上界）**：NER = log(∑C(n,k)×|T|^k)；RE = log(|E|²×|R|)；EE = log(|Tr|×|EvT|×∏(|E_r|+1))；Text-to-SQL = 采样近似
   - **CA_emp（经验值，核心跨任务指标）**：对模型采样 N 个输出，计 unique valid structures 的 log 数。跨任务单位统一（log count），反映模型实际不确定性而非理论空间
   - **VSS 经验测量**：N 个无约束样本中被结构验证拒绝的比例；分解为 VSS_hard（hard structural violation）和 VSS_soft（soft type violation）
   - CA_theo − CA_emp 的 gap 有独立诊断价值（模型自信度 vs. 理论复杂度）

   原始 proposal 仅有"combinatorial ambiguity"和"verification signal strength"两个概念标签，无法量化、不可复现。此变更将 taxonomy 从"定性分类"升级为"可操作的预测工具"，是整个优化中最关键的补强。 — 命中 Novelty（从定性到定量）+ Technical Soundness（可复现性）

5. **[Predictions / 全面重构预测体系]** — 原始 proposal 仅有隐含的跨任务排序预测。新版建立**四层预测体系**：
   - **Cross-task ordering（P1-P3，降级为 illustrative）**：EE>RE>NER 等，仅 3 个点、1/6 随机概率，明确标注统计效力有限
   - **Dataset-level predictions（主力之一）**：9 个 dataset-task 组合的 CA_emp 与 TTS gain 的 Spearman 相关
   - **Instance-level predictions（最高统计功效，主力）**：每个 dataset 内按 CA_emp 四分位分桶，验证单调递增；数百 data points per dataset
   - **Divergence predictions（taxonomy 最强 test）**：找到 CA/VSS 跨越 task-type 边界的 dataset，检验 taxonomy 是否优于"更难的任务获益更大"的朴素假设

   附加：Parallel vs. sequential 的象限级预测（P4-P6）；scaling curve functional form 作为探索性子分析。 — 命中 Technical Soundness（统计功效）+ Novelty（多层次验证框架在 NLP taxonomy 论文中罕见）

6. **[Analysis Plan / 新增 Competing Predictor Analysis]** — 加入 **baseline-F1 作为 competing predictor**，直接回应"taxonomy 不过是'难的任务 TTS 收益大'的重新包装"的质疑：
   - Predictor A: 1 − greedy F1（headroom）
   - Predictor B: CA_emp + VSS
   - Predictor C: full model
   - 报告 Spearman 相关和 incremental R²

   这是抵御"trivially true"攻击的最有力武器。如果 B 或 C 显著超过 A，taxonomy 的增量价值得到量化证明。 — 命中 Novelty（taxonomy 增量价值的统计论证）+ Technical Soundness（对 competing hypothesis 的正面回应）

7. **[Analysis Plan / 新增 Axis Independence Verification]** — 计算 CA_emp 与 VSS 的 instance-level Spearman 相关 + scatter plot。|r|<0.3 → 四象限结构有实证支撑；|r|>0.7 → taxonomy 实质一维，需讨论哪个轴主导。 — 命中 Technical Soundness（验证核心结构假设）

8. **[Analysis Plan / 新增 Cross-Model Stability (RQ1b)]** — 对 CA_emp 和 VSS 分别用 3 个模型计算，报告变异系数。验证 taxonomy 是"task-level"还是"task×model-level"。无论结果如何都有 takeaway。 — 命中 Technical Soundness（泛化性验证）

9. **[实验设计 / SCIR 对比降级]** — 原始 proposal 将 SCIR compute-matched comparison 列为 **"primary result"**，但 SCIR 代码 404 不可用。新版将其**降级为 "contextual reference point"**，明确声明：若代码可用则完全复现，否则引用 published numbers 并标注 cross-setup caveat 作为 limitation。消除了将 primary claim 建立在不可控外部依赖上的审稿风险。 — 命中 Technical Soundness（消除最大实验公平性隐患）

10. **[实验设计 / Parallel vs. Sequential 升为 Primary Experiment (RQ2)]** — 替代 SCIR 成为主控实验。两个条件完全由作者实现和控制，确保公平比较。新增明确的 operationalization：
    - Sequential pipeline：前一轮输出 + 原始输入 → 模型 refine → 重复 K 轮
    - Inverse-entropy voting：选 token-level generation entropy 最低的输出
    - Matched budget：parallel 与 sequential 总 token 数 ±10% 内
    - 与 taxonomy 整合：P4-P6 预测哪个象限偏好 parallel vs. sequential

    原始 proposal 的 sequential baseline 仅一句话带过。 — 命中 Technical Soundness（实验可复现性）+ Novelty（与 taxonomy 预测整合）

11. **[实验设计 / 新增 Constrained Decoding 分析（降为 Supplementary Analysis）]** — 原始 proposal 将 constrained decoding 视为纯工程手段。新版将其重新定位为 **taxonomy 自检**：constrained decoding 将 verification 从 post-hoc 前移到 in-process，可能耦合 CA 和 VSS，测试两轴独立性假设。但考虑 8 页正文限制，降级为 supplementary analysis（正文 1-2 段 + appendix），避免挤压 RQ1/RQ2 的展示空间。新增 unconstrained + post-hoc filtering 控制条件，解决因果混淆。 — 命中 Technical Soundness（控制条件完备）+ scope 管理

12. **[实验设计 / 新增 text-to-SQL OOD 验证]** — 增加 Spider 数据集（Qwen3-8B, N=1-16, ~12h H100）作为 **out-of-domain quantitative calibration**。叙事定位为 practitioner protocol 的 prospective calibration test：先用 protocol 预测，再对比实际结果。明确承认定性方向（TTS 对 text-to-SQL 有效）已有先行证据，本实验的价值在于定量预测精度。 — 命中 Significance（跨任务泛化的初步证据）+ Technical Soundness（OOD 验证）

13. **[Models / 新增 Llama-3.1-8B]** — 原始 proposal 仅用 Qwen3 家族。新增 Llama-3.1-8B（ACE05 + WikiEvents, N=1/4/8/16/32, ~18h H100）作为 cross-family robustness check 和 CA_emp/VSS cross-model stability 数据源。 — 命中 Technical Soundness（跨模型泛化）

14. **[Metrics / 标准化 TTS gain 定义]** — 原始 proposal 未明确 TTS gain 定义。新版统一为 **ΔF1(N=1 → N=32)**，消除 oracle-best N 的选择偏差。辅助指标：AUC under F1-vs-log(N) curve。明确 per-instance F1 定义（entity/relation/event-level micro-F1 per instance）。Sensitivity analysis 跨 N cutoff (8/16/32)。 — 命中 Technical Soundness（指标定义严谨性）

15. **[Statistical Rigor / 新增多项统计承诺]** — 原始 proposal 无统计讨论。新增：3 runs ± std、bootstrap CI for saturation points、instance-level Spearman rank correlation、incremental R² regression、sign tests for ordinal predictions。核心统计功效来自 instance-level analysis（数百 data points per dataset），而非 run-level aggregation。 — 命中 Technical Soundness（统计严谨性）

16. **[新增 Pre-registered Diagnostic Framework]** — 为每条核心预测预先指定失败模式和诊断实验。例如：P1 失败 → 消融 IoU vs. exact-match；instance-level 相关弱 → 比较 CA_emp vs. CA_theo；CA+VSS 不能 beat baseline-F1 → 结论"task difficulty subsumes taxonomy"（negative but informative）。这种"预注册"式设计在 NLP 会议中罕见，确保 confirming 和 disconfirming results 都产出有价值的发现。 — 命中 Novelty（方法论立场独特）+ Technical Soundness（dual-outcome 设计）

17. **[新增 Practitioner TTS Investment Decision Protocol]** — 将 taxonomy 打包为可直接使用的 5 步决策流程：定义 schema → 小规模无约束采样(~16 samples) → 估算 CA_emp 和 VSS → 查 taxonomy 象限 → 预测 gain range 并与 fine-tuning 成本比较。text-to-SQL 作为该 protocol 的 prospective calibration。 — 命中 Significance（实用价值）

18. **[Related Work / 扩充和精确化]** — 原始 proposal 声称 "empirically absent"，改为 **"lacks systematic cross-task characterization"**。新增三条线索的系统覆盖：(a) TTS scaling theory (Snell et al. 2024) — 明确互补关系；(b) LLM-based structured extraction (Code4Struct, GoLLIE, StructGPT) — baseline 选择依据；(c) verification/reward modeling — 将 structural verification 定位为 verification spectrum 的 training-free endpoint。主动承认 CA/VSS 的概念先驱（General AgentBench's verification gap ≈ informal VSS, etc.），贡献精确定位为"首次 operationalize + 跨任务系统验证"。 — 命中 Related Work（覆盖充分、定位清晰）

19. **[Contributions / 从 7 合并为 5]** — 原始 7 项含大量冗余（diversity analysis, cross-model analysis, Pareto analysis 各自独立列出）。新版 5 项各自实质性且不重叠：(1) predictive taxonomy + multi-resolution validation + competing predictor；(2) scaling characterization with instance-level analysis；(3) parallel vs. sequential controlled comparison；(4) practitioner decision protocol；(5) cross-model Pareto analysis + axis stability assessment。 — 命中 Novelty（contribution 表述不膨胀）

20. **[Scope / 泛化声明收窄]** — 原始 proposal 在 abstract/intro/contribution 中直接声称 taxonomy "extends to semantic parsing, text-to-SQL, code generation, table extraction"。新版将核心声明**限定为 flat structured extraction tasks**，跨任务迁移预测移入 Discussion 作为 informed speculation + 文献交叉验证，不在 contribution 中硬声明 beyond-IE 适用性。 — 命中 Technical Soundness（claims 与 evidence 匹配）

21. **[Compute / N 上限调整 + budget 重分配]** — N 从 48 降至 32（8B 模型在 N>32 很可能已过饱和点），释放约 30h 给 Llama cross-family check (~18h) 和 text-to-SQL (~12h)。总 budget ≤200h H100。移除 proposal 中的 contingency plan 细节（属项目管理，非学术内容）。 — 命中 Feasibility（资源分配合理化）

---

【主要风险】

1. **Taxonomy 增量价值可能不显著（最核心风险）**：如果 competing predictor analysis 中 CA_emp + VSS 无法在 incremental R² 上显著超过 baseline-F1 alone，taxonomy 退化为"难的任务 TTS 收益大"的形式化重新包装，核心 novelty 主张崩塌。Diagnostic framework 已设计好应对（承认 negative finding），但论文从 "taxonomy paper" 降级为 "empirical scaling study"，中稿难度上升。这是无法通过 proposal 层面优化消除的固有实验风险。

2. **CA-VSS 两轴高度相关导致四象限退化**：如果 instance-level Spearman |r| > 0.7，四象限中有两个事实上为空，taxonomy 实质为一维分类。论文仍可报告"单轴就够"作为 finding，但核心架构的优雅性受损。Reviewer 可能评价为 "over-engineered framework for a one-dimensional phenomenon"。

---

【实施评估】

- **计算资源**: ≤200h 单卡 H100。分配：Qwen3-8B IE 主实验 ~90h；Qwen3-8B Spider ~12h；Qwen3.6-27B (2 datasets) ~25h；Llama-3.1-8B (2 datasets) ~18h；baselines + supplementary analysis ~25h；buffer ~30h。按云计算单价约 $600-$1000。学术 GPU 集群或主流云平台均可执行。无需多卡并行。
- **数据需求**: ACE05（需 LDC license，大多数 NLP 实验室已有）、SciERC（公开）、TACREV（公开，2K subset）、MAVEN（公开）、WikiEvents（公开）、Spider（公开）。全部为标准 benchmark，无数据获取障碍。
- **人工介入**: **无需任何人工标注或人工评审**。实验全自动（constrained decoding + sampling + aggregation）。仅需研究者进行结果分析、统计检验和论文撰写。
- **训练需求**: **无模型训练**。完全 training-free 方法。仅需本地部署或 API 访问 Qwen3-8B、Qwen3.6-27B、Llama-3.1-8B 进行推理。模型权重均公开可得。
- **新 Benchmark**: **不需要构建新的 benchmark**。使用现有 6 个标准数据集。Taxonomy 和 practitioner protocol 是概念/方法论贡献，不涉及新数据集发布。
- **预估周期**: **4-5 周**。第 1 周：环境搭建 + XGrammar 集成 + pilot experiments；第 2-3 周：主实验执行（Qwen3-8B 全量 + Llama + text-to-SQL）；第 3-4 周：Qwen3.6-27B + supplementary analysis + 统计分析；第 4-5 周：论文撰写 + 图表制作。Proposal 中已预留 30h buffer 应对意外。

