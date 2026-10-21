# Idea Brief: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural Self-Consistency with Learned Aggregation


- **Idea ID**: `idea_010`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-6
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 via ARR May 2026 (submission: May 25, 2026; commitment: Aug 2, 2026; notification: Aug 20, 2026; conference: Oct 24-29, Budapest), Backup: ARR August 2026 (submission: Aug 3, 2026) → EACL 2027 or NAACL 2027

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

Test-time compute scaling (TTS) dramatically improves LLM reasoning on scalar-answer tasks, but structured prediction outputs — entity sets, relation graphs, event frames, SQL parse trees, dialogue states — have no clear verification function. Adaptive TTS methods (DSC, Slim-SC, ReASC, CGES, Sonata) further optimize compute allocation — but exclusively for scalar answers where consistency is trivially measured by answer agreement. We ask: when and why does sampling multiple schema-constrained structured outputs and aggregating via structural consistency improve prediction quality, how should compute be adaptively allocated across instances of varying structural complexity, and when does TTS fundamentally fail for structured prediction? We demonstrate through information extraction as the primary testbed, while establishing a general-purpose framework applicable to any structured prediction task.

## Opportunity / Why Now

TTS is the dominant paradigm for boosting LLM reasoning (DeepSeek-R1, o1), and a rapidly growing literature on adaptive TTS — DSC (NAACL 2025 Findings), Slim-SC (EMNLP 2025), ReASC (ACL 2026), CGES (arXiv 2511.02603), Sonata (ICLR 2026), CoRefine (arXiv 2602.08948), 'Learning When to Sample' (arXiv 2603.08999) — demonstrates that confidence-gated early stopping and difficulty-adaptive allocation can reduce sampling budgets by 45-80% with negligible accuracy loss. Yet this entire literature operates on scalar answers where consistency reduces to answer agreement. Two critical findings frame the gap for structured prediction: (1) PMC12888769 shows weak consistency-accuracy correlation for IE using surface-level Fleiss' Kappa on zero-shot models (Spearman 0.20-0.28), but the authors note that fine-tuned models 'could exhibit different consistency-accuracy dynamics'; (2) arXiv 2509.06861 argues TTS cannot help knowledge-intensive tasks because sampling cannot inject new information. We hypothesize that both findings admit an important exception: for fine-tuned models on structured prediction tasks, a significant fraction of errors are uncertainty-based (boundary detection, type ambiguity, structural composition) rather than knowledge-gap errors — and structural consistency (not surface string matching) can identify correct outputs in this regime. Moreover, structural consistency scores provide a natural gating signal for adaptive compute allocation: high early agreement signals easy instances where further sampling is wasteful, while low agreement signals hard instances requiring the full sampling budget. This opportunity extends beyond IE: any LLM task producing structured outputs — SQL queries, code ASTs, clinical FHIR resources, dialogue states — faces the same gap between scalar-answer TTS methods and structured prediction reality. XGrammar (MLSys 2025) makes constrained sampling near-free (<40 microseconds/token via vLLM's default backend), and mature UIE models (ProUIE, GoLLIE) provide strong base samplers. Concurrent work on multi-model NER ensembles (EL4NER, ACL 2025 submission) aggregates across different models, and CSC-SQL applies self-consistency to text-to-SQL via merge revision — but no work provides a general framework for adaptive structural self-consistency from a single fine-tuned model, isolating TTS contribution from model diversity and directly testing whether self-consistency scaling works for structured prediction.

## Landscape (SOTA & Limitations)

Test-time scaling is extensively studied for math/code (Forest-of-Thought, ICML 2025; Parallel TTS, Oct 2025; 30B+ token study, Dec 2024) but targets scalar-answer tasks exclusively. Self-consistency voting (Wang et al., ICLR 2023) and its successors — Reasoning-Aware Self-Consistency (NAACL 2025), inverse-entropy weighted voting (arXiv Nov 2025), Radial Consensus Score (arXiv April 2026), confidence-informed SC (arXiv Feb 2025), Ranked Voting SC (ACL 2025 Findings) — all aggregate scalar, embedding-space, or ranked-list answers. Critically, a mature and rapidly growing adaptive TTS literature optimizes compute allocation along a clear lineage: DSC (NAACL 2025 Findings) uses difficulty-based batch-level sample pre-allocation, ranking problems by difficulty and partitioning into easy/hard groups to adaptively allocate inference budgets; Slim-SC (EMNLP 2025) dynamically prunes redundant reasoning chains step-by-step during generation based on inter-chain semantic similarity, achieving up to 45% latency reduction; ReASC (ACL 2026) reframes adaptive sampling from response counting to evidence sufficiency via two-stage reliability-aware accumulation achieving 70% cost reduction; CGES (arXiv 2511.02603) forms Bayesian posteriors over candidate answers for principled early stopping with 69.4% call reduction; Sonata (ICLR 2026) trains a lightweight adapter to predict self-consistency from hidden states for thinking budget allocation (20-60% reduction); CoRefine (arXiv 2602.08948) uses a 211k-parameter Conv1D controller for HALT/RETHINK/ALTERNATIVE decisions with 63% wall-clock speedup; 'Learning When to Sample' (arXiv 2603.08999) achieves 80% token reduction via confidence-aware gating. The 'Reasoning on a Budget' survey (arXiv 2507.02076) provides a comprehensive taxonomy of adaptive TTC methods. However, all these methods define consistency and confidence over scalar answers — none addresses structured outputs where consistency measurement itself is non-trivial. In adjacent structured prediction domains, Functional Majority Voting (arXiv 2604.15618) aggregates code generation samples via execution-based functional equivalence — but this relies on executability, inapplicable to IE or most structured prediction tasks. CSC-SQL applies self-consistency with merge revision to text-to-SQL, but uses a task-specific correction model rather than a general structural consistency framework. STED (arXiv 2512.23712, NeurIPS 2025 Workshop) introduces Semantic Tree Edit Distance for measuring consistency of structured JSON outputs using Hungarian algorithm-based order-invariant matching and multi-level similarity, but functions as an evaluation framework rather than an improvement method — it measures consistency without leveraging it for aggregation or adaptive compute allocation. No work defines a general structural self-consistency framework for structured prediction outputs or uses it for adaptive compute gating. In IE specifically, ProUIE (April 2026) achieves SOTA via GRPO with stepwise fine-grained rewards on Qwen3-4B (ACE05-NER: 86.15 F1, ACE05-Arg: 52.58 F1, SciERC: 46.76 F1, avg NER: 79.44, avg RE: 71.17), and MR-UIE (Sept 2025) applies multi-perspective reasoning with RL — but both are training-time methods that generate single-pass outputs at inference. Post-hoc correction approaches include VerifiNER (ACL 2024) using KB-grounded verification and EL4NER (arXiv 2505.23038) ensembling multiple small LLMs for NER — but these are KB-dependent or multi-model approaches, fundamentally different from single-model self-consistency with adaptive gating. SaM (ACL 2025) dynamically selects and merges domain-specific NER expert models, again a multi-model approach. PMC12888769 (2026) measured consistency-accuracy correlation using Fleiss' Kappa on zero-shot hard-prompted models, finding weak Spearman correlations (0.20-0.28) — but used surface string matching on un-fine-tuned models while we propose structural consistency on task-specific fine-tuned models, and they acknowledged this limitation. The 'Two Failures of Self-Consistency' (Chen et al., 2023) demonstrates poor compositional consistency — IE has compositional structure (entity to relation to event) that may exhibit similar failures, which we explicitly test. No concurrent work applies adaptive test-time sampling with structural aggregation from a single fine-tuned model to any structured prediction task — confirmed via arXiv and OpenReview searches through May 2026.

## Proposed Approach

We propose Adaptive Structural Self-Consistency Scaling (AS2CS) as both a method and an empirical framework for understanding when adaptive TTS helps structured prediction, demonstrated through information extraction as a comprehensive testbed. The research is structured in three phases: pilot validation (Phase 0), full experimental study (Phase 1), and adaptive gating evaluation (Phase 2).

**Phase 0: Pilot Validation and Headroom Analysis (~8h H100, Days 1-3)**
Before committing to the full study, we run a targeted pilot to validate two premises. First, using 200 instances each from ACE05 NER and ACE05 EAE (event argument extraction), we sample N=8 extractions at T=1.0 from fine-tuned Qwen3-8B and compute: (a) Fleiss' Kappa on surface string matches (replicating PMC12888769), (b) our soft Jaccard span-level structural consistency score, and (c) Spearman correlation of each metric with per-instance F1 against gold annotations. If structural consistency yields significantly stronger correlation than Fleiss' Kappa (target: Spearman >=0.40 vs. their 0.20-0.28), we proceed. Second, we compute oracle best-of-N F1 gaps per dataset and subtask at N=8 to establish headroom ceilings: if oracle best-of-8 exceeds single-pass by <1 F1 on a subtask, TTS gains are fundamentally ceiling-limited there. We use headroom gaps to prioritize analysis: high-headroom subtasks (likely EAE at ~52 F1, SciERC RE at ~47 F1) receive full experimental treatment, while low-headroom subtasks (likely ACE05 NER near ~87 F1) are analyzed primarily for negative/diagnostic insight. Phase 0 also generates training data for the learned aggregation scorer (Phase 2). If both metrics show weak correlation (<=0.30) even with structural consistency, we pivot to a negative/analytical result.

**Base Models**: Qwen3-8B fine-tuned on UIE instruction data (JSON output format, trained with LLaMA Factory following ProUIE's pipeline) as primary model, and GoLLIE-7B as a cross-architecture generalization check.

**Sampling**: For each input, we sample N in {4, 8, 16, 32} schema-constrained extractions via XGrammar-backed structured generation in vLLM with temperature T=1.0 (standard for self-consistency sampling, maximizing output diversity), enforcing valid JSON output at near-zero overhead.

**Phase 1: Structural Consistency Aggregation (Full Study)**
Three aggregation functions tailored to IE subtask structure: (1) span-level entity voting via soft Jaccard similarity over character offsets with type-aware grouping (threshold tau_span), (2) relation-level graph consensus via edge majority voting after entity coreference alignment using mention overlap (threshold tau_coref), (3) event-level frame aggregation via trigger-anchored slot matching with role-wise majority voting (threshold tau_trigger). A composite structural agreement score ranks candidates or constructs a merged consensus output.

**Aggregation Hyperparameter Sensitivity Analysis**: Each aggregation function depends on a threshold parameter. We report sensitivity sweeps: tau_span in {0.3, 0.5, 0.7, 0.8}, tau_coref in {0.3, 0.5, 0.7}, tau_trigger in {0.5, 0.7, 0.9}. We report F1 variance across threshold settings per dataset.

**Phase 2: Adaptive Gating and Learned Aggregation**

*Adaptive Structural Consistency Gating (ASCG)*: Rather than applying a fixed N=32 samples uniformly, we use structural consistency at early samples as a confidence signal for adaptive compute allocation. For each instance: (1) sample N_min=4 extractions and compute structural agreement score S_4, (2) if S_4 >= theta_gate (high early agreement), accept the N=4 aggregation result and stop — the instance is 'easy' and further sampling is wasteful, (3) if S_4 < theta_gate, continue sampling to N_mid=8 and recompute S_8, (4) if S_8 >= theta_gate, accept the N=8 result, (5) otherwise, sample to N_max=16 or 32. We sweep theta_gate in {0.6, 0.7, 0.8, 0.9} and report: average effective N per dataset (expected: 6-10x vs. fixed 32x), compute savings (target: 50-70% reduction with <0.5 F1 loss), and cost-accuracy Pareto frontiers comparing fixed-N vs. adaptive-N. This extends the adaptive TTS paradigm (DSC, Slim-SC, ReASC, CGES, Sonata) to structured prediction for the first time, where the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement.

*Learned Aggregation Scorer (LAS)*: Beyond hand-crafted threshold-based aggregation, we train a lightweight MLP (2 hidden layers, ~10K parameters) on Phase 0 pilot data to predict per-instance extraction quality from structural features. Input features (per-instance, computed from N samples): (i) span overlap distribution statistics (mean, variance, max of pairwise soft Jaccard across samples), (ii) type agreement entropy (entropy of predicted entity/relation type distributions across samples), (iii) consistency trajectory (agreement scores at N=4, 8, 16 — captures how consistency evolves with more samples), (iv) structural complexity features (number of predicted entities, relations, events per sample — captures extraction difficulty). The MLP outputs a scalar quality estimate used for: (a) sample selection (select the sample with highest predicted quality), (b) adaptive gating (use predicted quality as the confidence signal instead of raw structural agreement). We compare: hand-crafted aggregation vs. learned selection vs. learned gating, analyzing whether the learned scorer transfers across datasets (train on ACE05 pilot data, evaluate on SciERC/TACREV) and whether it improves over hand-crafted thresholds. The comparison between hand-crafted vs. learned aggregation is itself a finding — if learned aggregation helps significantly, it suggests structural consistency in IE is too complex for simple heuristics; if hand-crafted suffices, it validates the interpretability of our structural metrics.

**Broader Applicability of ASCG to Structured Prediction**: While we demonstrate AS2CS through IE, the ASCG framework is the first general-purpose adaptive TTS method for any structured prediction task with non-scalar outputs. The core abstraction — sample multiple structured outputs, measure structural consistency via domain-appropriate alignment, and use consistency as a gating signal for adaptive compute allocation — transfers directly to: (1) semantic parsing, where SQL query graphs can be compared via AST edit distance and table/column overlap, and structural consistency identifies cases where the model is uncertain about join structure or predicate composition (cf. CSC-SQL's merge revision approach, which uses a task-specific correction model rather than general structural gating); (2) code generation, where AST-structured outputs enable tree-edit-distance-based consistency measurement beyond Functional Majority Voting's execution-dependent approach — particularly valuable for non-executable partial code or code in languages without test harnesses; (3) clinical NER and structured extraction, where FHIR-formatted outputs have hierarchical schema constraints and consistency across samples can identify uncertain entity boundaries and type assignments in medical text; (4) dialogue state tracking, where slot-value structures can be compared via slot-wise agreement and structural consistency identifies ambiguous user intents. In each case, the structural consistency metric and gating threshold require domain-specific instantiation, but the adaptive allocation framework (sample N_min, compute structural agreement, gate on consistency) is task-agnostic. We leave empirical validation on these domains to future work, focusing on IE as the most challenging case due to its multi-level compositional structure (entity → relation → event).

**Ablation Framework**: Six baselines: (a) single-pass greedy (same model, no TTS), (b) random-of-N (lower bound), (c) naive majority voting (surface string matching, replicating PMC12888769), (d) oracle best-of-N (upper bound), (e) VerifiNER (KB-dependent paradigm comparison on NER subtasks), (f) fixed-N S2CS (uniform sampling without adaptive gating — to isolate ASCG contribution). The gap between oracle and single-pass bounds achievable gain; the gap between AS2CS and naive-majority isolates structural aggregation; the gap between fixed-N and adaptive-N isolates compute efficiency.

**Error Taxonomy Analysis** (key analytical contribution): We categorize model errors into: (i) uncertainty errors — correct extraction appears in at least one of N samples but not deterministically (TTS can help), (ii) knowledge-gap errors — correct extraction never appears in any sample (TTS cannot help), (iii) systematic errors — model consistently produces the same wrong output (TTS cannot help). We report the fraction of each error type per dataset and subtask, directly addressing the knowledge-intensive limitation critique.

**Headroom-Aware Analysis**: We correlate TTS gains with base single-pass performance level, testing the hypothesis that TTS is most effective for medium-difficulty subtasks (high enough base performance for meaningful samples, low enough ceiling for improvement room). This analysis helps practitioners predict where TTS is worth applying without running the full pipeline.

**Compositional Consistency Analysis**: Following the 'Two Failures' work, we measure consistency at atomic (entity) vs. compositional (relation, event frame) granularity.

**Evaluation**: 5 datasets — ACE05 (NER+RE+EE), Few-NERD (fine-grained NER, 66 entity types), SciERC (NER+RE), TACREV (sentence-level RE), WikiEvents (document-level EAE). We report F1 with bootstrap significance tests (p<0.05), scaling curves (F1 vs. N and vs. total compute), cost-accuracy Pareto frontiers for fixed-N vs. adaptive-N, error taxonomy distributions, and headroom gap correlations.

## Resource Estimate

- **auto_research**: {'breakdown': 'Phase 0 pilot + headroom analysis (400 instances ACE05 NER+EAE, N=8, correlation + oracle gap): ~8h. Fine-tuning Qwen3-8B on UIE data: ~20h. Phase 1 sampling Qwen3-8B (5 datasets x 32 samples x T=1.0): ~10h. Phase 1 sampling GoLLIE-7B (5 datasets x 32 samples x T=1.0): ~13h. Oracle/random/naive ablation computation: ~10h. Error taxonomy analysis: ~15h. Compositional consistency analysis: ~8h. Aggregation threshold sensitivity sweeps: ~7h. Phase 2 adaptive gating experiments (4 theta_gate values x 5 datasets x 2 models): ~12h. Learned aggregation scorer training and evaluation: ~5h. VerifiNER paradigm comparison: ~5h. Scaling curves, Pareto frontiers, headroom correlation analysis: ~7h. Total itemized: ~120h. Additional ablations and reruns: ~23h. Buffer: ~22h (not counted in itemized total; combined with ablation headroom yields ~45h or 27% of budget).', 'claude_api_cost': '$350-550', 'estimated_gpu_cost': '$413 (165h x $2.50/hr)', 'gpu_hours': '~165h H100 80GB (with 45h buffer)', 'gpu_utilization': '~26% wall-clock utilization across 2 GPUs over 13 days (~90% computational efficiency during active jobs due to automated pipeline scheduling)', 'risk_note': 'Phase 0 on Days 1-3 serves as go/no-go gate; if pilot fails, only 8h invested. Adaptive gating adds ~12h compute but dramatically improves practical value. Learned scorer training is lightweight (~5h) but transfer across datasets is an empirical question. Reducing to T=1.0 only (standard for self-consistency) creates a 27% compute buffer, sufficient for unexpected reruns or debugging.', 'speed_bottleneck': 'Qwen3-8B fits on single H100; 2 GPUs enable parallel sweeps', 'team': '0 after initial setup', 'timeline': '11-13 days with 2x H100 80GB GPUs (fits before May 25 ARR deadline)'}
- **human_in_loop**: {'claude_api_cost': '$150-250', 'estimated_gpu_cost': '$325', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~35-40% wall-clock utilization', 'risk_note': 'ACE05 requires LDC license (LDC2006T06)', 'team': '1 researcher, ~30min/day', 'timeline': '5-6 weeks'}
- **manual**: {'estimated_gpu_cost': '$325 (at ~$2.50/hr)', 'gpu_hours': '~130h H100 80GB', 'gpu_utilization': '~25-30% wall-clock utilization', 'team': '1-2 researchers', 'timeline': '8-10 weeks'}

## Key References

- Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., ICLR 2023)
- Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters (ICLR 2025)
- Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning (ICML 2025)
- Test-Time Scaling in Reasoning Models Is Not Effective for Knowledge-Intensive Tasks Yet (Zhao et al., arXiv 2509.06861, 2025)
- Consistency-Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction (PMC12888769, 2026)
- Two Failures of Self-Consistency in the Multi-Step Reasoning of LLMs (Chen et al., arXiv 2305.14279, 2023)
- XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)
- GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)
- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv 2604.10633, 2026)
- MR-UIE: Multi-Perspective Reasoning with Reinforcement Learning for Universal Information Extraction (arXiv 2509.09082, 2025)
- VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models (ACL 2024)
- EL4NER: Ensemble Learning for Named Entity Recognition via Multiple Small-Parameter Large Language Models (arXiv 2505.23038, 2025)
- Selecting and Merging: Towards Adaptable and Scalable Named Entity Recognition with Large Language Models (ACL 2025)
- Ranked Voting based Self-Consistency of Large Language Models (ACL 2025 Findings)
- Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)
- The Art of Scaling Test-Time Compute for Large Language Models (arXiv 2512.02008, 2024)
- The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute (arXiv 2511.02309, 2025)
- Beyond Majority Voting: Efficient Best-Of-N with Radial Consensus Score (arXiv 2026)
- Scalable Best-of-N Selection for Large Language Models via Self-Certainty (arXiv 2502.18581, 2025)
- Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning (Wang et al., NAACL 2025 Findings)
- Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency (Hong et al., EMNLP 2025)
- Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning (ReASC, ACL 2026)
- CGES: Confidence-Guided Early Stopping for Efficient and Accurate Self-Consistency (arXiv 2511.02603, 2025)
- Learning When to Sample: Confidence-Aware Self-Consistency for Efficient LLM Chain-of-Thought Reasoning (arXiv 2603.08999, 2026)
- Adaptive Thinking: Large Language Models Know When to Think in Latent Space (Sonata, ICLR 2026)
- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv 2602.08948, 2026)
- STED and Consistency Scoring: A Framework for Evaluating LLM Structured Output Reliability (arXiv 2512.23712, NeurIPS 2025 Workshop)
- Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs (arXiv 2507.02076, 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Three-phase design is clearly delineated with explicit go/no-go criteria. Ablation framework with 6 baselines is comprehensive. Error taxonomy, headroom-aware analysis, and compositional consistency analysis are well-motivated. Aggregation hyperparameter sensitivity sweeps address the fragility concern from Round 3.', 'score': 4}**/5
  - feasibility: **{'rationale': 'Pilot-gated design limits risk to 8h before go/no-go. T=1.0-only sampling creates a 27% compute buffer (165h vs 200h cap). XGrammar overhead verified as negligible. Qwen3-8B throughput on H100 (~500 tok/s) supports the sampling estimates. 13-day timeline with 2 GPUs is tight but achievable. No pre-trained UIE model exists, but LlamaFactory fine-tuning is well-tooled.', 'score': 4}**/5
  - impact: **{'rationale': 'The contribution portfolio — ASCG (first adaptive TTS for structured prediction), error taxonomy (uncertainty vs knowledge-gap), headroom analysis (when TTS is worth applying), and broader applicability framework (semantic parsing, code gen, clinical NER, DST) — provides reliable value regardless of whether absolute F1 gains are large. The analytical contribution alone answers questions the IE community needs addressed.', 'score': 4}**/5
  - novelty: **{'rationale': 'The gap is independently verified as genuine — no published work applies adaptive structural self-consistency to structured prediction. MIDGARD (ACL 2024) is the closest predecessor but targets commonsense reasoning graphs (not IE), uses MDL (not structural similarity voting), and lacks adaptive sampling. SCSG (March 2026) uses simple majority voting on ABSA tuples without adaptive gating. The ASCG + LAS combination is novel. Both MIDGARD and SCSG should be cited but do not invalidate the novelty claim.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 30.0%
**终审自评 (Y)**: 38.0%
**出口三重共识 (Z)**: 31.0%
**Z 区间**: [26.0%, 35.0%]
**真实提升 (Z-X)**: +1.0 pp
**幻觉幅度 (Y-Z)**: +7.0 pp
**出口一致性**: 中（std=3.2%，落在 3-7% 区间）
**出口三次评估**: [33.0, 28.0, 34.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [核心叙事 / 全文 framing] — **从"方法迁移"叙事重构为"诊断范式"叙事**：原始 proposal 以 "we present AS2CS, the first systematic study of adaptive TTS for structured prediction" 开篇，读起来像"把 adaptive TTS 搬到 IE 上"。修改为以 "When and why does TTS help structured prediction?" 为核心问题驱动，TTS Applicability Diagnostic Framework 作为 primary contribution，ASCG/LAS 降格为"构建诊断所需的技术工具"。这使标题的 "When Does..." 承诺在 contribution 列表中被兑现，叙事类型对齐近年高接受度的 empirical-science 范式（类似 "Are Emergent Abilities a Mirage?"）。 — 命中 Novelty + Significance

2. [Contribution 排序 / 贡献列表] — **重组四项贡献的排列优先级**：原始排序为 (1) ASCG, (2) LAS, (3) headroom-aware analysis。修改为 (1) TTS Applicability Diagnostic Framework（三轴诊断 + 3-step practitioner protocol）, (2) Error Taxonomy, (3) ASCG, (4) LAS。分析贡献优先于方法贡献，明确区分"分析贡献（primary）"和"技术贡献（enabling）"。 — 命中 Novelty（避免被定性为 engineering contribution）

3. [核心论点 / Introduction + Conclusion] — **确立 punch line: "TTS for structured prediction requires knowledge internalization first"**：原始 proposal 将 fine-tuning 作为实验前提但未赋予其解释性地位。修改为：fine-tuning 将错误分布从 knowledge-gap-dominated 转向 uncertainty-dominated，从而恢复 consistency-accuracy correlation——这是论文的 take-home message，用一句话概括全文核心 insight，提升审稿人记忆度。 — 命中 Analysis Depth + Insight Memorability

4. [TTS Applicability Diagnostic / 新增独立章节] — **将三个独立分析维度整合为统一诊断框架**：原始 proposal 中 error taxonomy、compositional complexity、model capability 散落在三个独立 RQ 中。修改为整合为 (uncertainty-error ratio × structural complexity × base model capability) 的联合诊断空间，呈现为 2D heatmap + conditioning variable 的 signature figure，并包装为 3-step lightweight protocol（50 dev instances 采样 → 估计复杂度 → 查 heatmap 得 recommended settings）。 — 命中 Significance + Practical Impact

5. [Novelty 定位 / Motivation 段落] — **重新 articulate 核心技术挑战**：原始表述 "the key challenge is that the consistency signal itself requires structural alignment rather than simple answer agreement"，将对齐本身当作挑战，但对齐是已有技术。修改为：核心挑战是 consistency-accuracy 假设（所有 adaptive TTS 方法的前提）在结构化 domain 中默认失效，需要在假设失效的条件下重建 adaptive TTS 的基础——novelty 在于"修复前提"而非"换对齐算法"。 — 命中 Novelty

6. [Error Taxonomy / Contribution (3) → 升格为 Contribution (2)] — **从 defensive argument 升格为 formal contribution + TTS feasibility diagnostic tool**：原始 proposal 中 error taxonomy 是"回应 arXiv 2509.06861 批评"的防御性论点。修改为：给出操作性定义（uncertainty error = target 出现在 ≥1 但 <N 个采样中; knowledge-gap error = 在 0 个采样中出现），提供 cross-benchmark 分布统计，展示 TTS gain 与 uncertainty-error 占比的相关性，测量 zero-shot → few-shot → fine-tuned 条件下的错误类型迁移曲线。增加 N ∈ {4,8,16,32} 的分类稳定性 sensitivity analysis。 — 命中 Novelty + Broader Impact

7. [RQ4 / 实验设计] — **将 Compositional Consistency Degradation 从实验清单末尾提升为显式 RQ**：原始 proposal 仅在最后一句提到 "compositional consistency degradation"。修改为 RQ4，设计 per-instance complexity-binned 实验（按 entity count、relation nesting depth、event argument count 分层），显式检验是 gradual degradation 还是 sharp phase transition。报告 alignment 计算开销与复杂度的交互。这是 structured prediction 独有的分析维度，scalar-answer TTS 文献中不存在。 — 命中 Analysis Depth + Novelty

8. [Pilot Validation / 新增章节] — **增加 pilot-gated 验证步骤 + 收紧阈值**：原始 proposal 说 "We address both through a pilot-gated, headroom-aware research design" 但未给出具体操作。修改为：在每个 benchmark 上对 fine-tuned 和 zero-shot 模型各采 N=8 输出，计算 structural consistency 与 instance-level F1 的 Spearman ρ。Primary proceed 阈值 ρ ≥ 0.4（非原始版本未指定的模糊表述）；0.3 ≤ ρ < 0.4 标记为 marginal regime；ρ < 0.3 across the board 则 pivot 为 negative finding 的分析贡献。Fine-tuned vs. zero-shot 的 paired comparison 本身是独立 empirical 贡献。 — 命中 Technical Soundness

9. [Baselines / 实验设计] — **从隐含的 2-level 对比扩展为显式 8-level baseline 矩阵**：原始 proposal 仅隐含 "adaptive vs. fixed sampling"。修改为 8 级阶梯：① single-decode greedy (cost floor), ② fixed-N naive majority vote, ③ fixed-N structural aggregation (ablation), ④ logprob-based confidence gating, ⑤ ASCG + raw consistency, ⑥ ASCG + LAS (proposed), ⑦ Best-of-N with LLM-as-judge reranking (selection vs. aggregation), ⑧ oracle Best-of-N (ceiling)。 — 命中 Technical Soundness + Rigor

10. [Temperature / 实验设计] — **增加 temperature ablation**：原始 proposal 直接采用 T=1.0 并声称 "standard for self-consistency"。修改为 T ∈ {0.5, 0.7, 1.0, 1.2} ablation study，分析 temperature 对 consistency-accuracy correlation、aggregation quality、gating accuracy 的影响，承认 T=1.0 是 reasoning task 标准但可能不适用于 fine-tuned IE 模型。 — 命中 Technical Soundness

11. [Constrained Decoding / 实验设计] — **增加 constrained decoding × TTS 交互效应分析**：原始 proposal 未讨论 XGrammar constrained decoding 对 consistency signal 的 confounding effect。修改为增加 constrained vs. unconstrained + post-hoc filter 的 ablation，检验 constrained decoding 是否人为膨胀 consistency。若检测到膨胀，提出 dev-set recalibration 策略。报告其对 ρ 的影响作为 minor analytical finding。 — 命中 Technical Soundness

12. [Model Scale / 实验设计] — **增加 model capability case study + few-shot 条件**：原始 proposal 仅用 Qwen3-8B 和 GoLLIE-7B。修改为增加 Qwen3-32B fine-tuned（ACE05 + SciERC）和 Qwen3-32B few-shot（无 fine-tune）。GoLLIE 独立为 cross-architecture 比较，不与 scale 混为一谈。RQ3 从 "scaling curve" 降级为 "case study on model capability"——诚实匹配只有两个 scale point 的现实。 — 命中 Soundness + Feasibility

13. [LAS / Contribution (4)] — **明确训练协议 + 三路 ablation + transfer + feature importance**：原始 proposal 对 LAS 训练数据来源未说明。修改为：(a) 明确用 official dev set 训练、test set 评估（杜绝泄露）；(b) 增加 annotation efficiency sensitivity (50/100/200/500 instances)；(c) ablation: LAS vs. feature-threshold vs. raw consistency score；(d) leave-one-dataset-out transfer 用 paired bootstrap 检验（非 arbitrary 85% threshold）；(e) SHAP/permutation importance 识别 universally transferable vs. task-specific features。 — 命中 Technical Soundness + Reproducibility

14. [泛化声明 / Scope 章节] — **收窄 generality claims 至 IE domain**：原始 proposal 声称 "the first general-purpose framework for adaptive TTS with structured outputs" 并列举 SQL/code/clinical/DST 四个额外 domain 作为 contribution。修改为将核心 claim 限定为 IE，SQL/code/clinical/DST 降为 future work 展望，消除 claim-experiment gap。 — 命中 Technical Soundness（消除 overclaiming 风险）

15. [Priority Claims / 全文] — **软化 "first" 声明**：原始 proposal 三次使用 "the first"。修改为 "to our knowledge, among the first to..."，叙事重心从 "we are first" 转向 "the problem is hard because [specific challenges], and we propose [specific solutions]"。 — 命中 Novelty（降低被 falsify 的风险）

16. [Related Work / 新增三个方向] — **从仅覆盖 adaptive self-consistency 扩展到六个方向**：原始 proposal 仅引用 DSC/Slim-SC/ReASC/CGES/Sonata/STED。修改为增加：(a) classical structured prediction ensemble methods, (b) LLM confidence estimation for structured outputs, (c) test-time augmentation for NLP, (d) TTS for non-scalar generative NLP + code generation structural consistency (CodeT, MBR-based selection), (e) LLM calibration for structured tasks。每个方向明确差异化定位。加深 STED 讨论：STED = evaluation, AS2CS = aggregation + adaptive gating + diagnostic framework。 — 命中 Related Work

17. [统计方案 / Evaluation Metrics] — **增加显著性检验和多 seed 报告**：原始 proposal 未指定统计检验。修改为 paired bootstrap test (n=10000) + 95% CI，3-5 random seeds 的 mean±std，significance threshold "≥ 2 F1 with p < 0.05"。 — 命中 Technical Soundness

18. [Significance 底线 / Motivation] — **显式声明何种增益算 meaningful**：原始 proposal 无此声明。修改为 "≥ 2 F1 points or ≥ 30% cost reduction at equivalent F1"，展示作者的 self-awareness。 — 命中 Soundness + 评审印象

19. [Paper Organization / 新增段落] — **增加 main vs. appendix 分配策略**：原始 proposal 无此规划，所有实验并列。修改为：正文聚焦 pilot validation 核心结果 + ASCG vs. baselines 主表 + diagnostic heatmap (signature figure) + error taxonomy 分布；所有 ablation 放 appendix；RQ3/RQ4 正文各 1-2 段。缓解 "tries to do too much" 的常见 reviewer 批评。 — 命中 Technical Soundness + Presentation

20. [Cost Framing / Introduction + Experiments] — **增加 concrete cost-efficiency metrics**：原始 proposal 用抽象的 "compute-efficient" 表述。修改为报告具体的 average samples saved、cost-accuracy Pareto 改进百分比，总 cost 定义包含 LLM sampling + alignment overhead + gating overhead（honest accounting），并报告 wall-clock time breakdown per complexity bin。 — 命中 Significance + Practical Impact

【主要风险】:

1. **Algorithmic novelty 的结构性 ceiling**：即使叙事重构为"诊断范式"，ASCG/LAS 的核心技术组件（已有对齐算法 + 标准 MLP + 常规 gating loop）仍然缺乏 algorithmic novelty。如果 1-2 位 reviewer 坚持要 novel algorithm 而非 novel analysis/diagnostic，论文可能被定性为 "systematic empirical study" 并被降分。这是结构性限制，无法通过 proposal 优化进一步缓解——只能靠实验结果的 surprising 程度（特别是 phase transition 发现或 dramatic fine-tuning effect）来补偿。

2. **Pilot validation 失败的 pivot 风险**：如果 fine-tuned 模型的 ρ < 0.4 across the board（即结构化 consistency 即使用 alignment-based metrics 也无法作为可靠 confidence proxy），论文必须 pivot 为 negative finding。虽然 dual-outcome 设计使这在学术上是可发表的，但 negative finding 论文的 EMNLP 主会接受概率显著低于 positive finding（估计降至 20-25%），且论文的 primary contribution（diagnostic framework）将失去其 prescriptive value（只剩 descriptive value）。

【实施评估】:

- **计算资源**: 需要至少 1 × A100-80GB（或等价）用于 Qwen3-8B/GoLLIE-7B 的 fine-tuning 和多次采样推理；Qwen3-32B fine-tuning + 推理需要 2-4 × A100-80GB 或 1 × H100。5 个 benchmark × 4 模型配置 × N=8-16 采样 × 多 seed = 大量推理，预估总 GPU 时长 200-400 A100-hours（含 fine-tuning ~50h + 推理 ~150-350h）。如用云平台（AWS/GCP），约 $600-$1200。LLM-as-judge baseline (baseline 7) 如果用 API model 会有额外 API 成本，约 $100-$300。
- **数据需求**: ACE05、Few-NERD、SciERC、TACREV、WikiEvents 五个 benchmark 均公开可得。ACE05 需要 LDC 许可证（大多数学术机构已有）。UIE 格式的 fine-tuning 数据需要从原始数据集转换，转换脚本已有公开实现。无需构建新数据集。
- **人工介入**: 不需要人工标注（所有 benchmark 自带 gold annotation）。Error taxonomy 分类完全自动化（基于 gold 对比的操作性定义）。需要研究者人工检查 ~50-100 个 error classification 实例做 sanity check（约 2-4 小时）。LAS feature importance 的 SHAP 分析结果需要研究者解读。整体人工介入量低。
- **训练需求**: 需要模型训练。(a) Qwen3-8B fine-tuning on UIE tasks（~10-15h on 1×A100）；(b) Qwen3-32B fine-tuning（~20-30h on 2-4×A100）；(c) GoLLIE-7B 可能需要适配训练或直接用预训练版本；(d) LAS MLP 训练极轻（CPU 级别，分钟级）。总训练时长约 30-50 GPU-hours。
- **新 Benchmark**: 不需要构建新 benchmark。所有评测在已有公开 benchmark 上进行。但需要构建 complexity-binned evaluation splits（按 entity count、relation depth 等分层），这是对现有数据的重新组织而非新建。
- **预估周期**: 从启动到可投稿约 **8-10 周**。细分：Week 1-2 数据准备 + fine-tuning；Week 2-3 Pilot validation（决定 proceed/pivot）；Week 3-6 主实验（ASCG vs. baselines × 5 benchmarks × 多配置）；Week 5-7 ablation studies + diagnostic heatmap 构建；Week 7-9 写作；Week 9-10 内部 rev


## MVP Validation Results

- **Date**: 2026-05-14
- **Hypothesis Supported**: Yes

### Key Metrics

NER full rho_sj=0.388 (SJ>FK +6.6pp, p=2e-20) | RE full rho_sj=0.234 (FAIL <0.30) | RE cond rho_sj=0.372 (SJ>FK +11.8pp) | RE pct_zero=42.4% | NER oracle headroom=+5.5pp | RE oracle headroom=+13.1pp | Gate 0: NER F1=66.2%, RE F1=42.1%

### Summary

MVP 验证 structural self-consistency 作为 IE test-time scaling 信号。5 轮 pilot 实验（ft_001/ft_002_v2 模型，T=1.0/0.7，N=8，SciERC 551 instances）+ 1 轮度量分解诊断。结果：NER 方向强正向（rho_sj=0.388, SJ>FK p=2e-20）；RE full-set FAIL（rho_sj=0.234<0.30），但 RE conditional set（排除 all-zero knowledge-gap 实例）显示强信号（rho_sj=0.372, SJ>FK 11.8pp）。E1 诊断排除了度量设计问题——RE weakness 是复合错误传播的固有属性。T=0.7 vs T=1.0 对比揭示采样温度对信号质量的影响。假设部分验证：entity-level IE 有效，relation-level 需 capability-aware 分析。

### Recommendation

GO — 进入 research 阶段，走 Narrative A（NER-primary + RE diagnostic）。NER 信号足够强且 SJ>FK 优势一致。RE conditional 分析 + E1 诊断 + 温度敏感性分析为论文增加诊断深度。下一步：E3 (NER N=16 验证 rho 是否过 0.40) + E4 (NER 多数据集泛化 CoNLL/OntoNotes) + RE 诊断整理。目标 ARR May 2026-05-25。
