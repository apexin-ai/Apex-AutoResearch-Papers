# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/6226869d-1846-41e6-8065-9900be365161.jsonl`
- **Structured JSON:** [`6a41fbbb715bc974d86e.json`](../../sessions/6a/6a41fbbb715bc974d86e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:26:51.804Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:26:51.804Z",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision\",\n  \"core_problem\": \"Synthetic-data-based zero-shot event argument extraction (EAE) faces a structural data quality problem that existing approaches address only partially. LtGaE (AAAI 2026) uses soft RL penalties for argument completeness — a quality score penalty that fires when the proportion of empty arguments per sample deviates from a target range [τ−ε, τ+ε], but does not enforce per-role entity-type compatibility or hard cardinality bounds during decoding. Gatto et al. (ACL 2025 Long) uses free-form LLM generation with no formal constraints. FineCSDA (NLPCC 2024) targets the long-tail distribution of argument roles via sample-level augmentation of rare event types (SDAM) and context-level injection of rare role fillers (CDAM), but neither module enforces formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design rather than a structural guarantee. None of these approaches can guarantee proportional representation of rare argument roles across a finite generated corpus: even if individual constraint violation rates are low (plausible for strong instruction-following models), unconstrained generation will cluster on high-frequency role patterns due to LLM prior biases, systematically under-representing rare roles. This is a distributional coverage failure, not merely a constraint violation problem. The primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether structural regularization gains are mechanistically explained by rare-role coverage improvements. Answering these questions empirically — with a clean three-condition ablation, volume-controlled design, and stratified evaluation — is a concretely useful contribution for EMNLP Findings, even if overall F1 deltas are modest.\",\n  \"opportunity\": \"The supervised-to-zero-shot gap remains 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; TSCA IET Software 2026 adds ~+3.0/+1.0 F1 in fully supervised settings; best zero-shot cross-dataset: LtGaE 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). Training data quality for the generator model is a concrete bottleneck: LtGaE's soft RL penalties improve over prior unconstrained generation but cannot guarantee per-role proportional coverage; FineCSDA's targeted augmentation improves rare-role counts but lacks formal structural guarantees. SynthIE (EMNLP 2023) demonstrated that task-reversal generation can produce highly effective synthetic IE training data, but uses no grammar-constrained decoding and does not address event argument extraction. The key open question is whether hard constraints provide a measurable advantage over oracle-quality soft filtering under a volume-controlled design. This question has a clean experimental operationalization: (A) unconstrained generation, (B) unconstrained generation with post-hoc violation filtering (oracle soft constraint approximation, volume-matched to A and C), and (C) grammar-constrained generation via XGrammar — same model, same schema information, same final training volume. If C outperforms B on rare roles despite similar overall violation rates, the result directly demonstrates that the coverage guarantee (not just constraint compliance) drives the downstream gain. This is a falsifiable, mechanistically interpretable empirical finding — the type EMNLP Findings values.\",\n  \"landscape\": \"GuideX (ACL Findings 2025) sets SOTA on 7 zero-shot NER benchmarks with Llama-3.1 fine-tuned on generated data, but explicitly does not address event argument extraction.\\n\\nFineCSDA ('FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation', NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) directly identifies the long-tail distribution of argument roles as a bottleneck and proposes two augmentation modules: SDAM generates new document-level samples for rare event types, and CDAM injects rare argument roles and corresponding context into common event type documents. Unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design for rare types and roles, and provides no distributional coverage guarantee by construction.\\n\\nGatto et al. ('Document-Level Event-Argument Data Augmentation for Challenging Role Types', ACL 2025 Long, arXiv:2403.03304) is a direct predecessor: LLM-powered augmentation (Mad Lib Aug and Struct2Text) for extractive EAE, +13 F1 on zero-shot role types using BERT-QA, no schema constraints, few-shot cross-domain setting (5 documents per event type available), zero-shot roles within seen event types — not fully zero-shot event type generalization.\\n\\nBiTer (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) achieves +4.6%/+7.5%/+0.4% zero-shot Arg-C F1 on RAMS/WikiEvents/ACE2005 using within-dataset event-type-held-out splits. Protocol is NOT directly comparable to LtGaE's cross-dataset three-way protocol; reported separately with explicit footnote.\\n\\nLtGaE (AAAI 2026, arXiv:2603.02909) uses multi-agent Propose-Evaluate-Revise with RL reward that includes a soft penalty p_i activated when the proportion of empty arguments ρ_i deviates from a target range [τ−ε, τ+ε] — a global aggregate quality-score adjustment per sample, not a per-role coverage guarantee or hard decoding constraint. Achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki. Does not compare against BiTer.\\n\\nASEE (EMNLP Findings 2025, arXiv:2505.08690) addresses inference-time schema selection via RAG; no hard constraints; does not report RAMS/WikiEvents numbers.\\n\\nSALE (MDPI Electronics, March 2026) uses code-based LLM fine-tuning with RL alignment for cross-task zero-shot transfer; no formal schema constraints during data generation.\\n\\nExtracting Events Like Code (AAAI 2026, arXiv:2511.13118) uses Python class definitions for inference-time schema validation, not training-data generation.\\n\\nSynthIE (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) generates synthetic IE training data via task-reversal (structure→text generation), achieving large F1 gains on smaller models; uses no grammar-constrained decoding, no formal cardinality bounds, and targets IE triplets rather than compositional event argument extraction. Establishes the task-reversal generation paradigm that CompSchema-IE extends with hard compositional constraints.\\n\\nSupervised SOTA: DEGAP (COLING 2025, arXiv:2405.13325) — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1. TSCA (IET Software 2026) adds ~+3.0/+1.0 F1 in fully supervised settings.\\n\\nThe specific open question not addressed by any prior work — including FineCSDA, LtGaE, or Gatto et al.: does hard grammar constraint enforcement (cardinality + entity-type, XGrammar) outperform oracle post-hoc filtering of unconstrained generation under a volume-controlled design, and does any advantage concentrate in rare-role and high-cardinality-tightness strata where the coverage guarantee is theoretically most binding?\",\n  \"approach\": \"CompSchema-IE is framed explicitly as an empirical study targeting EMNLP 2026 Findings. The primary contribution is a clean, volume-controlled three-condition ablation that isolates the value of hard constraint enforcement over soft filtering, combined with a stratified analysis that localizes any gains mechanistically.\\n\\n**Primary Theoretical Argument (Coverage Guarantee, Violation-Rate-Independent)**:\\nEven with 0% individual constraint violations, unconstrained generation over a finite corpus cannot guarantee proportional representation of rare argument roles. An LLM generating N event instances for type T will sample role fillings according to its prior, which concentrates on high-frequency patterns. Roles instantiated rarely in natural text (e.g., 'Beneficiary' in Attack events, 'Origin' in Transport events) will be systematically under-represented regardless of violation rate. SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance within its cardinality bounds. Post-hoc filtering cannot recover this — it can only remove bad instances, not manufacture coverage for rare roles. FineCSDA (NLPCC 2024) partially addresses this via targeted prompting for rare types and roles (SDAM/CDAM), but without formal structural guarantees; CompSchema-IE's SCG provides the coverage guarantee by construction.\\n\\n**Step 0 — Motivating Pilot Study (Day 4, 4 GPU-hours)**:\\nSample 600 event instances from Qwen3-32B without constraints (standard structured prompting with RAMS/WikiEvents schema descriptions). The expanded sample (~4–5 instances per event type for RAMS's 139 types) enables reliable per-role violation statistics. Measure: entity-type mismatch rate, cardinality violation rate, role hallucination rate, and argument role coverage (proportion of schema roles appearing ≥1 time). Report all four metrics unconditionally. The primary paper argument holds regardless of outcome: low violation rates motivate the coverage guarantee framing; high rates additionally motivate constraint enforcement. Both are reported; neither determines the primary framing.\\n\\n**Step 1 — Schema Constraint Grammar (Days 1-3, human engineering)**:\\nDerive typed constraint specifications from RAMS (cardinality directly from public ontology TSV; entity-type compatibility from dataset annotations) and WikiEvents (entity-type compatibility from annotations). Encode as XGrammar-compatible context-free grammars. RAMS TSV availability substantially reduces construction effort. Scoped to 2 ontologies.\\n\\n**Step 2 — Three-Condition Data Generation with Volume Control (Days 5-7, ~62.5 GPU-hours)**:\\nAll conditions use Qwen3-32B on 2×A100 80GB via vLLM. To eliminate the volume confound — where Condition B (post-hoc filtered) would otherwise train on fewer instances than C — the following volume normalization protocol is applied:\\n\\n- **Pool Generation**: Generate 1.5× the target volume N as unconstrained instances (same chat prompting with schema descriptions). Report achieved token throughput and generation settings.\\n- **Condition A (Unconstrained)**: Randomly subsample N instances from the 1.5N pool.\\n- **Condition B (Post-hoc Filtered — Oracle Soft Baseline)**: Apply the automated verifier to the full 1.5N pool; retain instances passing all entity-type, cardinality, and role-hallucination checks, targeting N post-filter instances. Report the achieved discard rate (e.g., 'we generated 1.5N instances and discarded X%, retaining N for training') as a transparency metric. If the filter discards more than 33% (leaving fewer than N clean instances), increase the pool to 2× and regenerate the additional batch. This baseline approximates oracle-quality soft constraint enforcement without reimplementing LtGaE's RL loop; crucially, it CANNOT recover proportional coverage for roles absent from filtered instances.\\n- **Condition C (SCG-Constrained)**: Grammar-constrained vLLM decoding via XGrammar to exactly N instances, enforcing all role-entity-type assignments and cardinality constraints during the forward pass (<40μs/token overhead, per XGrammar MLSys 2025).\\n\\nAll three conditions train on exactly N instances, making the C-vs-B comparison methodologically airtight.\\n\\n**Step 3 — Constraint Verification (concurrent with Step 2)**:\\nThe automated verifier checks all generated instances and reports: filter rate for the A/B pool (transparency metric), corpus-level role coverage for each condition, near-zero filter rate for Condition C (SCG compliance guarantee).\\n\\n**Step 4 — Fine-tuning and Evaluation (Days 8-11, ~57 GPU-hours)**:\\nLoRA fine-tune Qwen3-8B on each of the three volume-matched corpora (3 conditions × ~15 GPU-hours = 45 GPU-hours). Evaluate zero-shot on WikiEvents and RAMS using LtGaE three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Comparison table: LtGaE, ASEE, supervised SOTA (DEGAP), Condition A, Condition B, Condition C. BiTer reported separately under native within-dataset protocol with explicit non-comparability footnote.\\n\\n**Step 5 — Stratified Evaluation (Day 12, ~12 GPU-hours for inference)**:\\nThe primary analysis section — demonstrates mechanistic explanation of C vs. A/B gaps:\\n(a) Role Rarity Strata: Rank argument roles by frequency in source schema annotations; partition into quartiles. Report C vs. A and C vs. B F1 for each quartile. Hypothesis: C-B gap concentrates in bottom quartile (rarest roles) because post-hoc filtering cannot create coverage for roles that unconstrained generation never instantiated.\\n(b) Cardinality Tightness Strata: Partition by RAMS-ontology cardinality — max=1 (singleton roles) vs. max>1. Report C vs. A and C vs. B F1 for each partition. Hypothesis: C outperforms B on max=1 roles because Condition B can only remove duplicates but may still have duplicate instances within filtered corpus; SCG hard-enforces the singleton constraint.\\nIf overall C-B delta is modest (e.g., <1 F1), the stratified analysis provides a theoretically grounded finding even for the Findings track: hard constraints help specifically where theory predicts, at a granularity that soft filtering cannot replicate.\\n\\n**Null Result Pre-Specification**:\\nWe pre-specify the null result interpretation in the paper: if C does not outperform B even in the rare-role quartile or singleton-cardinality partition, we report this as a clearly framed negative finding — for strong instruction-following models like Qwen3-32B, oracle post-hoc filtering achieves equivalent rare-role coverage to formal grammar constraints. This is a practically useful negative result: it suggests that engineering investment in SCG construction may not be warranted at this model scale, and that FineCSDA-style targeted prompting or post-hoc filtering is sufficient. EMNLP Findings publishes clearly framed negative results; this pre-specification distinguishes a null result from a failed experiment.\\n\\n**Paper writing**: Concurrent from Day 1 (intro, related work, method drafted during experiment runs); intensive final writing Days 13-16.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~125.5h A100 80GB total: pilot study generation 600 instances (4 GPU-hours); 1.5× unconstrained pool generation for Conditions A+B (~37.5 GPU-hours); SCG-constrained generation for Condition C (~25 GPU-hours); LoRA fine-tuning Qwen3-8B across 3 volume-matched conditions × 15 GPU-hours = 45 GPU-hours; stratified evaluation inference ~12 GPU-hours; evaluation and reporting ~2 GPU-hours\",\n      \"gpu_utilization\": \"Moderate (~50%): compressed timeline reduces idle gaps; human engineering on SCG module (Days 1-3) and paper writing (concurrent) introduce some idle GPU time, mitigated by parallelizing fine-tuning runs. Volume control adds ~12.5 GPU-hours of generation vs. original design.\",\n      \"timeline\": \"16 active days targeting May 25, 2026 ARR deadline (commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest). Day-by-day: Days 1-3 SCG construction + pilot study setup; Day 4 pilot study run (600 instances) + metric analysis; Days 5-7 data generation (1.5× A/B pool + C, staggered on 2×A100, pool generation starts Day 5, C generation starts Day 6 while A/B fine-tune begins); Days 8-10 LoRA fine-tuning (all 3 conditions, staggered); Day 11 LtGaE three-way evaluation; Day 12 stratified evaluation analysis; Days 13-16 intensive paper writing (concurrent with experiments from Day 1). No extended ablations, no ACE05 comparison, no BiTer replication.\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$187 (125.5h × $1.49/hr A100, RunPod/JarvisLabs)\",\n      \"h100_equiv\": \"~90h H100-equivalent (well within ≤200h H100 hard constraint)\",\n      \"risk_note\": \"Key risks and mitigations: (1) Overall C-B F1 delta may be small (<1 F1): mitigated by stratified evaluation and pre-specified null result interpretation — paper's primary claim is that hard constraints help in rare-role and singleton-cardinality strata; if this too is null, reported as a clear negative finding with specific positioning. (2) Filter rate exceeds 33% (B cannot reach N from 1.5N pool): mitigated by increasing pool to 2× for that condition and reporting achieved discard rate as transparency metric. (3) Pilot study shows <1% violations: expected and mitigated by coverage guarantee argument (violation-rate-independent). (4) 16-day timeline is tight: SCG construction is the bottleneck; RAMS TSV machine-readable cardinality substantially reduces this. Paper writing concurrent from Day 1 is required. (5) BiTer protocol mismatch: explicitly handled with separate table and footnote. (6) FineCSDA comparison: differentiated from CompSchema-IE by formal grammar-constrained decoding vs. targeted prompting, volume-controlled experimental design, and distributional coverage guarantee by construction.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR May 25, 2026 submission deadline; commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest, Hungary)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)\",\n    \"FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) — identifies long-tail argument role distribution as bottleneck; SDAM generates samples for rare event types, CDAM injects rare role fillers into common event type documents; no formal cardinality bounds or entity-type constraints; coverage relies on targeted prompting\",\n    \"Document-Level Event-Argument Data Augmentation for Challenging Role Types (Gatto, Sharif, Seegmiller, Preum; ACL 2025 Long, arXiv:2403.03304) — direct LLM-augmentation predecessor; no constrained decoding, no cardinality/entity-type constraints, few-shot cross-domain with zero-shot roles\",\n    \"SynthIE: Leveraging the Asymmetry of Knowledge Graph Structure for Synthetic IE Data Generation (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) — task-reversal generation paradigm; no grammar-constrained decoding, no formal cardinality bounds, targets IE triplets not event argument extraction\",\n    \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)\",\n    \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)\",\n    \"BiTer: Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) — within-dataset event-type-held-out evaluation protocol; not directly comparable to LtGaE three-way cross-dataset protocol\",\n    \"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation (ASEE, EMNLP Findings 2025, arXiv:2505.08690)\",\n    \"Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction (LtGaE, AAAI 2026, arXiv:2603.02909) — soft RL penalty p_i fires when per-sample empty-argument proportion ρ_i deviates from [τ−ε, τ+ε] (global aggregate quality score, not per-role coverage guarantee); 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki\",\n    \"Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (AAAI 2026, arXiv:2511.13118)\",\n    \"Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models (SALE, MDPI Electronics, March 2026)\",\n    \"DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying (COLING 2025, arXiv:2405.13325) — supervised SOTA: RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1\",\n    \"Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction (DEEIA, ACL 2024 Findings, arXiv:2405.01884) — RAMS 53.4 Arg-C F1, WikiEvents 67.0 Arg-C F1\",\n    \"Two-Stream Modeling for Document-Level Event Argument Extraction Using Contextual Clue and AMR Structures (TSCA, IET Software 2026) — supervised SOTA extension: +3.02/+1.01 F1 on RAMS/WikiEvents over prior SOTA\",\n    \"DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning (arXiv:2506.05128)\",\n    \"MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)\",\n    \"Document-Level Event Argument Extraction by Conditional Generation (NAACL 2021)\",\n    \"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv 2023)\",\n    \"XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)\"\n  ],\n  \"description\": \"Zero-shot event argument extraction lags supervised performance by 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; best zero-shot cross-dataset: LtGaE AAAI 2026 — 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). A key bottleneck is training data quality for the generator model. This paper presents CompSchema-IE, an empirical study asking: do hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar-constrained vLLM decoding) outperform oracle post-hoc filtering of unconstrained generation for zero-shot EAE, and does any advantage concentrate in role strata where theory predicts? The primary motivation is a distributional coverage guarantee: even with 0% individual constraint violations, unconstrained generation over a finite corpus cannot guarantee proportional representation of rare argument roles — LLM priors cluster on high-frequency patterns, systematically under-representing rare roles regardless of explicit violations. SCG enforces coverage by construction; post-hoc filtering cannot recover it. Prior work (FineCSDA NLPCC 2024, LtGaE AAAI 2026) addresses rare-role under-representation via targeted prompting or aggregate soft penalties — neither provides this guarantee. A three-condition, volume-controlled ablation isolates the grammar effect cleanly: (A) Unconstrained, randomly subsampled to N training instances; (B) Post-hoc Filtered (oracle soft-constraint approximation, volume-matched to N by generating 1.5× pool and filtering to N, with achieved discard rate reported as transparency metric); (C) SCG-Constrained (grammar-constrained to exactly N instances). All conditions use Qwen3-32B, the same schema information, and the same final training volume N, making the C-vs-B comparison methodologically airtight. A motivating pilot study measures entity-type mismatch, cardinality violation, role hallucination, and role coverage rates in Qwen3-32B unconstrained generation on RAMS/WikiEvents (600 instances; all metrics reported unconditionally). LoRA fine-tunes Qwen3-8B on each volume-matched corpus; evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines. Null result interpretation is pre-specified: if C does not outperform B in rare-role strata, the paper reports this as a clearly framed negative finding (post-hoc filtering suffices at Qwen3-32B scale). The stratified evaluation by (a) role rarity quartile and (b) cardinality tightness (max=1 vs. max>1) demonstrates where C-B gaps concentrate. CompSchema-IE extends the SynthIE task-reversal paradigm (EMNLP 2023) with formal grammar-constrained decoding and compositional cardinality bounds. Target: EMNLP 2026 Findings (ARR May 25, 2026). Estimated GPU cost: ~$187 (125.5h A100 ≈ 90h H100-equiv, within budget). Timeline: 16 active days.\",\n  \"project_name\": \"schema_constrained_event_ie\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"COVERAGE GUARANTEE LOGICAL GAP [critical, newly identified]: The proposal's primary theoretical claim — 'SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance' — is overstated given confirmed RAMS TSV structure. The RAMS ontology TSV (independently verified at nlp.jhu.edu/rams/) specifies only MAXIMUM cardinality (the 'count permitted' column), NOT minimum cardinality. XGrammar therefore enforces upper-bound cardinality and entity-type constraints, but CANNOT force optional roles to appear. Since rare roles in RAMS may be optional in many event types (a given event instance may legitimately not have an 'Instrument' or 'Beneficiary'), the grammar provides no coverage guarantee for those roles. The coverage guarantee claim holds only for roles that the paper explicitly sets min-cardinality=1 in the grammar — which would require an assumption not derivable from the RAMS TSV alone and would produce unrealistic training data (every instance must have every role filled). The proposal must either (a) acknowledge this and narrow the guarantee to 'roles assigned min-cardinality=1 in the grammar encoding' with an explicit design choice described, or (b) reframe the theoretical argument from 'structural coverage guarantee' to 'structurally-prompted generation is more likely to instantiate optional rare roles due to explicit slot salience' — an empirical hypothesis rather than a logical guarantee. This is the single issue that a RAMS-familiar reviewer will raise immediately.\", \"BoostCD unacknowledged [minor]: 'Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction' (EMNLP 2025 Main, arXiv:2506.14901) empirically demonstrates that constrained and unconstrained decoding errors are complementary for closed IE, with a learned boosted model combining both. While BoostCD targets inference-time decoding (not training-data generation), its central empirical finding — that hard constraints and unconstrained generation have complementary error profiles — is directly relevant to CompSchema-IE's motivating argument and should be cited in related work with a one-sentence differentiation.\", \"Training volume N unspecified [minor]: The proposal never states the target training volume N. For RAMS with 139 event types, the number of instances per type and total N are unknown, making the GPU cost estimates (37.5h for 1.5N pool, 25h for N SCG-constrained) unverifiable. Specify N upfront (e.g., 'N=5,000 instances distributed proportionally across event types') so compute estimates and reproducibility can be assessed.\"]\nFeedback: The Round 6 proposal is the strongest version yet — all five Round 5 issues are properly resolved (volume normalization via 1.5× pool, FineCSDA cited and differentiated, null result pre-specified, pilot study at 600 instances, BiTer protocol mismatch handled). DEGAP F1 numbers (RAMS 54.2, WikiEvents 67.1 Arg-C) are independently verified correct. XGrammar overhead claim (<40μs/token as default vLLM backend) is confirmed. One fixable critical issue blocks submission readiness: the coverage guarantee must be corrected.\n\n(1) REVISE THE COVERAGE GUARANTEE ARGUMENT [critical]: The RAMS TSV only provides maximum cardinality (upper bounds on role occurrences), not minimum cardinality. The grammar therefore enforces: (a) no role appears more than its max count, and (b) when filled, entity types are compatible. It CANNOT guarantee that rare optional roles appear at all. Replace 'SCG enforces proportional coverage by construction' with one of two framings: OPTION A — 'In our grammar encoding, we set min-cardinality=1 for all roles applicable to a given event type, guaranteeing their appearance in every generated instance; this is a design choice that differs from natural annotation practice and we evaluate whether this artificial completeness improves rare-role coverage downstream.' OPTION B — 'SCG provides structural salience: by enumerating every applicable role slot explicitly in the constrained generation template, the LLM is prompted to consider filling each slot rather than freely omitting rare ones; we test empirically whether this structured attention mechanism improves rare-role instantiation.' Option B is more honest and requires no changes to the actual method.\n\n(2) ADD BoostCD [one sentence in related work]: 'Concurrently, BoostCD (EMNLP 2025) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE; CompSchema-IE investigates an analogous question at training-data generation time, where coverage differences compound across a finite corpus.'\n\n(3) SPECIFY N [one sentence in Section 2 or Step 2]: State the target training volume N explicitly (e.g., 'N=5,000 instances drawn proportionally across RAMS event types') so compute estimates are verifiable and the paper is reproducible.\n\nWith these three changes — particularly the coverage guarantee reframing — the proposal is ready for EMNLP 2026 Findings submission. The empirical design is sound, the null result handling is appropriate, and the resource estimate is within budget.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:26:51.809Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:26:51.809Z",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-10T09:26:51.839Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision",
  "core_problem": "Synthetic-data-based zero-shot event argument extraction (EAE) faces a structural data quality problem that existing approaches address only partially. LtGaE (AAAI 2026) uses soft RL penalties for argument completeness — a quality score penalty that fires when the proportion of empty arguments per sample deviates from a target range [τ−ε, τ+ε], but does not enforce per-role entity-type compatibility or hard cardinality bounds during decoding. Gatto et al. (ACL 2025 Long) uses free-form LLM generation with no formal constraints. FineCSDA (NLPCC 2024) targets the long-tail distribution of argument roles via sample-level augmentation of rare event types (SDAM) and context-level injection of rare role fillers (CDAM), but neither module enforces formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design rather than a structural guarantee. None of these approaches can guarantee proportional representation of rare argument roles across a finite generated corpus: even if individual constraint violation rates are low (plausible for strong instruction-following models), unconstrained generation will cluster on high-frequency role patterns due to LLM prior biases, systematically under-representing rare roles. This is a distributional coverage failure, not merely a constraint violation problem. The primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether structural regularization gains are mechanistically explained by rare-role coverage improvements. Answering these questions empirically — with a clean three-condition ablation, volume-controlled design, and stratified evaluation — is a concretely useful contribution for EMNLP Findings, even if overall F1 deltas are modest.",
  "opportunity": "The supervised-to-zero-shot gap remains 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; TSCA IET Software 2026 adds ~+3.0/+1.0 F1 in fully supervised settings; best zero-shot cross-dataset: LtGaE 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). Training data quality for the generator model is a concrete bottleneck: LtGaE's soft RL penalties improve over prior unconstrained generation but cannot guarantee per-role proportional coverage; FineCSDA's targeted augmentation improves rare-role counts but lacks formal structural guarantees. SynthIE (EMNLP 2023) demonstrated that task-reversal generation can produce highly effective synthetic IE training data, but uses no grammar-constrained decoding and does not address event argument extraction. The key open question is whether hard constraints provide a measurable advantage over oracle-quality soft filtering under a volume-controlled design. This question has a clean experimental operationalization: (A) unconstrained generation, (B) unconstrained generation with post-hoc violation filtering (oracle soft constraint approximation, volume-matched to A and C), and (C) grammar-constrained generation via XGrammar — same model, same schema information, same final training volume. If C outperforms B on rare roles despite similar overall violation rates, the result directly demonstrates that the coverage guarantee (not just constraint compliance) drives the downstream gain. This is a falsifiable, mechanistically interpretable empirical finding — the type EMNLP Findings values.",
  "landscape": "GuideX (ACL Findings 2025) sets SOTA on 7 zero-shot NER benchmarks with Llama-3.1 fine-tuned on generated data, but explicitly does not address event argument extraction.\n\nFineCSDA ('FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation', NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) directly identifies the long-tail distribution of argument roles as a bottleneck and proposes two augmentation modules: SDAM generates new document-level samples for rare event types, and CDAM injects rare argument roles and corresponding context into common event type documents. Unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design for rare types and roles, and provides no distributional coverage guarantee by construction.\n\nGatto et al. ('Document-Level Event-Argument Data Augmentation for Challenging Role Types', ACL 2025 Long, arXiv:2403.03304) is a direct predecessor: LLM-powered augmentation (Mad Lib Aug and Struct2Text) for extractive EAE, +13 F1 on zero-shot role types using BERT-QA, no schema constraints, few-shot cross-domain setting (5 documents per event type available), zero-shot roles within seen event types — not fully zero-shot event type generalization.\n\nBiTer (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) achieves +4.6%/+7.5%/+0.4% zero-shot Arg-C F1 on RAMS/WikiEvents/ACE2005 using within-dataset event-type-held-out splits. Protocol is NOT directly comparable to LtGaE's cross-dataset three-way protocol; reported separately with explicit footnote.\n\nLtGaE (AAAI 2026, arXiv:2603.02909) uses multi-agent Propose-Evaluate-Revise with RL reward that includes a soft penalty p_i activated when the proportion of empty arguments ρ_i deviates from a target range [τ−ε, τ+ε] — a global aggregate quality-score adjustment per sample, not a per-role coverage guarantee or hard decoding constraint. Achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki. Does not compare against BiTer.\n\nASEE (EMNLP Findings 2025, arXiv:2505.08690) addresses inference-time schema selection via RAG; no hard constraints; does not report RAMS/WikiEvents numbers.\n\nSALE (MDPI Electronics, March 2026) uses code-based LLM fine-tuning with RL alignment for cross-task zero-shot transfer; no formal schema constraints during data generation.\n\nExtracting Events Like Code (AAAI 2026, arXiv:2511.13118) uses Python class definitions for inference-time schema validation, not training-data generation.\n\nSynthIE (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) generates synthetic IE training data via task-reversal (structure→text generation), achieving large F1 gains on smaller models; uses no grammar-constrained decoding, no formal cardinality bounds, and targets IE triplets rather than compositional event argument extraction. Establishes the task-reversal generation paradigm that CompSchema-IE extends with hard compositional constraints.\n\nSupervised SOTA: DEGAP (COLING 2025, arXiv:2405.13325) — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1. TSCA (IET Software 2026) adds ~+3.0/+1.0 F1 in fully supervised settings.\n\nThe specific open question not addressed by any prior work — including FineCSDA, LtGaE, or Gatto et al.: does hard grammar constraint enforcement (cardinality + entity-type, XGrammar) outperform oracle post-hoc filtering of unconstrained generation under a volume-controlled design, and does any advantage concentrate in rare-role and high-cardinality-tightness strata where the coverage guarantee is theoretically most binding?",
  "approach": "CompSchema-IE is framed explicitly as an empirical study targeting EMNLP 2026 Findings. The primary contribution is a clean, volume-controlled three-condition ablation that isolates the value of hard constraint enforcement over soft filtering, combined with a stratified analysis that localizes any gains mechanistically.\n\n**Primary Theoretical Argument (Coverage Guarantee, Violation-Rate-Independent)**:\nEven with 0% individual constraint violations, unconstrained generation over a finite corpus cannot guarantee proportional representation of rare argument roles. An LLM generating N event instances for type T will sample role fillings according to its prior, which concentrates on high-frequency patterns. Roles instantiated rarely in natural text (e.g., 'Beneficiary' in Attack events, 'Origin' in Transport events) will be systematically under-represented regardless of violation rate. SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance within its cardinality bounds. Post-hoc filtering cannot recover this — it can only remove bad instances, not manufacture coverage for rare roles. FineCSDA (NLPCC 2024) partially addresses this via targeted prompting for rare types and roles (SDAM/CDAM), but without formal structural guarantees; CompSchema-IE's SCG provides the coverage guarantee by construction.\n\n**Step 0 — Motivating Pilot Study (Day 4, 4 GPU-hours)**:\nSample 600 event instances from Qwen3-32B without constraints (standard structured prompting with RAMS/WikiEvents schema descriptions). The expanded sample (~4–5 instances per event type for RAMS's 139 types) enables reliable per-role violation statistics. Measure: entity-type mismatch rate, cardinality violation rate, role hallucination rate, and argument role coverage (proportion of schema roles appearing ≥1 time). Report all four metrics unconditionally. The primary paper argument holds regardless of outcome: low violation rates motivate the coverage guarantee framing; high rates additionally motivate constraint enforcement. Both are reported; neither determines the primary framing.\n\n**Step 1 — Schema Constraint Grammar (Days 1-3, human engineering)**:\nDerive typed constraint specifications from RAMS (cardinality directly from public ontology TSV; entity-type compatibility from dataset annotations) and WikiEvents (entity-type compatibility from annotations). Encode as XGrammar-compatible context-free grammars. RAMS TSV availability substantially reduces construction effort. Scoped to 2 ontologies.\n\n**Step 2 — Three-Condition Data Generation with Volume Control (Days 5-7, ~62.5 GPU-hours)**:\nAll conditions use Qwen3-32B on 2×A100 80GB via vLLM. To eliminate the volume confound — where Condition B (post-hoc filtered) would otherwise train on fewer instances than C — the following volume normalization protocol is applied:\n\n- **Pool Generation**: Generate 1.5× the target volume N as unconstrained instances (same chat prompting with schema descriptions). Report achieved token throughput and generation settings.\n- **Condition A (Unconstrained)**: Randomly subsample N instances from the 1.5N pool.\n- **Condition B (Post-hoc Filtered — Oracle Soft Baseline)**: Apply the automated verifier to the full 1.5N pool; retain instances passing all entity-type, cardinality, and role-hallucination checks, targeting N post-filter instances. Report the achieved discard rate (e.g., 'we generated 1.5N instances and discarded X%, retaining N for training') as a transparency metric. If the filter discards more than 33% (leaving fewer than N clean instances), increase the pool to 2× and regenerate the additional batch. This baseline approximates oracle-quality soft constraint enforcement without reimplementing LtGaE's RL loop; crucially, it CANNOT recover proportional coverage for roles absent from filtered instances.\n- **Condition C (SCG-Constrained)**: Grammar-constrained vLLM decoding via XGrammar to exactly N instances, enforcing all role-entity-type assignments and cardinality constraints during the forward pass (<40μs/token overhead, per XGrammar MLSys 2025).\n\nAll three conditions train on exactly N instances, making the C-vs-B comparison methodologically airtight.\n\n**Step 3 — Constraint Verification (concurrent with Step 2)**:\nThe automated verifier checks all generated instances and reports: filter rate for the A/B pool (transparency metric), corpus-level role coverage for each condition, near-zero filter rate for Condition C (SCG compliance guarantee).\n\n**Step 4 — Fine-tuning and Evaluation (Days 8-11, ~57 GPU-hours)**:\nLoRA fine-tune Qwen3-8B on each of the three volume-matched corpora (3 conditions × ~15 GPU-hours = 45 GPU-hours). Evaluate zero-shot on WikiEvents and RAMS using LtGaE three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Comparison table: LtGaE, ASEE, supervised SOTA (DEGAP), Condition A, Condition B, Condition C. BiTer reported separately under native within-dataset protocol with explicit non-comparability footnote.\n\n**Step 5 — Stratified Evaluation (Day 12, ~12 GPU-hours for inference)**:\nThe primary analysis section — demonstrates mechanistic explanation of C vs. A/B gaps:\n(a) Role Rarity Strata: Rank argument roles by frequency in source schema annotations; partition into quartiles. Report C vs. A and C vs. B F1 for each quartile. Hypothesis: C-B gap concentrates in bottom quartile (rarest roles) because post-hoc filtering cannot create coverage for roles that unconstrained generation never instantiated.\n(b) Cardinality Tightness Strata: Partition by RAMS-ontology cardinality — max=1 (singleton roles) vs. max>1. Report C vs. A and C vs. B F1 for each partition. Hypothesis: C outperforms B on max=1 roles because Condition B can only remove duplicates but may still have duplicate instances within filtered corpus; SCG hard-enforces the singleton constraint.\nIf overall C-B delta is modest (e.g., <1 F1), the stratified analysis provides a theoretically grounded finding even for the Findings track: hard constraints help specifically where theory predicts, at a granularity that soft filtering cannot replicate.\n\n**Null Result Pre-Specification**:\nWe pre-specify the null result interpretation in the paper: if C does not outperform B even in the rare-role quartile or singleton-cardinality partition, we report this as a clearly framed negative finding — for strong instruction-following models like Qwen3-32B, oracle post-hoc filtering achieves equivalent rare-role coverage to formal grammar constraints. This is a practically useful negative result: it suggests that engineering investment in SCG construction may not be warranted at this model scale, and that FineCSDA-style targeted prompting or post-hoc filtering is sufficient. EMNLP Findings publishes clearly framed negative results; this pre-specification distinguishes a null result from a failed experiment.\n\n**Paper writing**: Concurrent from Day 1 (intro, related work, method drafted during experiment runs); intensive final writing Days 13-16.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~125.5h A100 80GB total: pilot study generation 600 instances (4 GPU-hours); 1.5× unconstrained pool generation for Conditions A+B (~37.5 GPU-hours); SCG-constrained generation for Condition C (~25 GPU-hours); LoRA fine-tuning Qwen3-8B across 3 volume-matched conditions × 15 GPU-hours = 45 GPU-hours; stratified evaluation inference ~12 GPU-hours; evaluation and reporting ~2 GPU-hours",
      "gpu_utilization": "Moderate (~50%): compressed timeline reduces idle gaps; human engineering on SCG module (Days 1-3) and paper writing (concurrent) introduce some idle GPU time, mitigated by parallelizing fine-tuning runs. Volume control adds ~12.5 GPU-hours of generation vs. original design.",
      "timeline": "16 active days targeting May 25, 2026 ARR deadline (commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest). Day-by-day: Days 1-3 SCG construction + pilot study setup; Day 4 pilot study run (600 instances) + metric analysis; Days 5-7 data generation (1.5× A/B pool + C, staggered on 2×A100, pool generation starts Day 5, C generation starts Day 6 while A/B fine-tune begins); Days 8-10 LoRA fine-tuning (all 3 conditions, staggered); Day 11 LtGaE three-way evaluation; Day 12 stratified evaluation analysis; Days 13-16 intensive paper writing (concurrent with experiments from Day 1). No extended ablations, no ACE05 comparison, no BiTer replication.",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$187 (125.5h × $1.49/hr A100, RunPod/JarvisLabs)",
      "h100_equiv": "~90h H100-equivalent (well within ≤200h H100 hard constraint)",
      "risk_note": "Key risks and mitigations: (1) Overall C-B F1 delta may be small (<1 F1): mitigated by stratified evaluation and pre-specified null result interpretation — paper's primary claim is that hard constraints help in rare-role and singleton-cardinality strata; if this too is null, reported as a clear negative finding with specific positioning. (2) Filter rate exceeds 33% (B cannot reach N from 1.5N pool): mitigated by increasing pool to 2× for that condition and reporting achieved discard rate as transparency metric. (3) Pilot study shows <1% violations: expected and mitigated by coverage guarantee argument (violation-rate-independent). (4) 16-day timeline is tight: SCG construction is the bottleneck; RAMS TSV machine-readable cardinality substantially reduces this. Paper writing concurrent from Day 1 is required. (5) BiTer protocol mismatch: explicitly handled with separate table and footnote. (6) FineCSDA comparison: differentiated from CompSchema-IE by formal grammar-constrained decoding vs. targeted prompting, volume-controlled experimental design, and distributional coverage guarantee by construction."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR May 25, 2026 submission deadline; commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest, Hungary)"
  ],
  "level": "solid",
  "key_references": [
    "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)",
    "FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) — identifies long-tail argument role distribution as bottleneck; SDAM generates samples for rare event types, CDAM injects rare role fillers into common event type documents; no formal cardinality bounds or entity-type constraints; coverage relies on targeted prompting",
    "Document-Level Event-Argument Data Augmentation for Challenging Role Types (Gatto, Sharif, Seegmiller, Preum; ACL 2025 Long, arXiv:2403.03304) — direct LLM-augmentation predecessor; no constrained decoding, no cardinality/entity-type constraints, few-shot cross-domain with zero-shot roles",
    "SynthIE: Leveraging the Asymmetry of Knowledge Graph Structure for Synthetic IE Data Generation (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) — task-reversal generation paradigm; no grammar-constrained decoding, no formal cardinality bounds, targets IE triplets not event argument extraction",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "BiTer: Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) — within-dataset event-type-held-out evaluation protocol; not directly comparable to LtGaE three-way cross-dataset protocol",
    "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation (ASEE, EMNLP Findings 2025, arXiv:2505.08690)",
    "Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction (LtGaE, AAAI 2026, arXiv:2603.02909) — soft RL penalty p_i fires when per-sample empty-argument proportion ρ_i deviates from [τ−ε, τ+ε] (global aggregate quality score, not per-role coverage guarantee); 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki",
    "Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (AAAI 2026, arXiv:2511.13118)",
    "Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models (SALE, MDPI Electronics, March 2026)",
    "DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying (COLING 2025, arXiv:2405.13325) — supervised SOTA: RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1",
    "Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction (DEEIA, ACL 2024 Findings, arXiv:2405.01884) — RAMS 53.4 Arg-C F1, WikiEvents 67.0 Arg-C F1",
    "Two-Stream Modeling for Document-Level Event Argument Extraction Using Contextual Clue and AMR Structures (TSCA, IET Software 2026) — supervised SOTA extension: +3.02/+1.01 F1 on RAMS/WikiEvents over prior SOTA",
    "DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning (arXiv:2506.05128)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "Document-Level Event Argument Extraction by Conditional Generation (NAACL 2021)",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv 2023)",
    "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)"
  ],
  "description": "Zero-shot event argument extraction lags supervised performance by 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; best zero-shot cross-dataset: LtGaE AAAI 2026 — 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). A key bottleneck is training data quality for the generator model. This paper presents CompSchema-IE, an empirical study asking: do hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar-constrained vLLM decoding) outperform oracle post-hoc filtering of unconstrained generation for zero-shot EAE, and does any advantage concentrate in role strata where theory predicts? The primary motivation is a distributional coverage guarantee: even with 0% individual constraint violations, unconstrained generation over a finite corpus cannot guarantee proportional representation of rare argument roles — LLM priors cluster on high-frequency patterns, systematically under-representing rare roles regardless of explicit violations. SCG enforces coverage by construction; post-hoc filtering cannot recover it. Prior work (FineCSDA NLPCC 2024, LtGaE AAAI 2026) addresses rare-role under-representation via targeted prompting or aggregate soft penalties — neither provides this guarantee. A three-condition, volume-controlled ablation isolates the grammar effect cleanly: (A) Unconstrained, randomly subsampled to N training instances; (B) Post-hoc Filtered (oracle soft-constraint approximation, volume-matched to N by generating 1.5× pool and filtering to N, with achieved discard rate reported as transparency metric); (C) SCG-Constrained (grammar-constrained to exactly N instances). All conditions use Qwen3-32B, the same schema information, and the same final training volume N, making the C-vs-B comparison methodologically airtight. A motivating pilot study measures entity-type mismatch, cardinality violation, role hallucination, and role coverage rates in Qwen3-32B unconstrained generation on RAMS/WikiEvents (600 instances; all metrics reported unconditionally). LoRA fine-tunes Qwen3-8B on each volume-matched corpus; evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines. Null result interpretation is pre-specified: if C does not outperform B in rare-role strata, the paper reports this as a clearly framed negative finding (post-hoc filtering suffices at Qwen3-32B scale). The stratified evaluation by (a) role rarity quartile and (b) cardinality tightness (max=1 vs. max>1) demonstrates where C-B gaps concentrate. CompSchema-IE extends the SynthIE task-reversal paradigm (EMNLP 2023) with formal grammar-constrained decoding and compositional cardinality bounds. Target: EMNLP 2026 Findings (ARR May 25, 2026). Estimated GPU cost: ~$187 (125.5h A100 ≈ 90h H100-equiv, within budget). Timeline: 16 active days.",
  "project_name": "schema_constrained_event_ie",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["COVERAGE GUARANTEE LOGICAL GAP [critical, newly identified]: The proposal's primary theoretical claim — 'SCG enforces proportional coverage by construction: the grammar mandates that each mandatory role appears in every generated instance' — is overstated given confirmed RAMS TSV structure. The RAMS ontology TSV (independently verified at nlp.jhu.edu/rams/) specifies only MAXIMUM cardinality (the 'count permitted' column), NOT minimum cardinality. XGrammar therefore enforces upper-bound cardinality and entity-type constraints, but CANNOT force optional roles to appear. Since rare roles in RAMS may be optional in many event types (a given event instance may legitimately not have an 'Instrument' or 'Beneficiary'), the grammar provides no coverage guarantee for those roles. The coverage guarantee claim holds only for roles that the paper explicitly sets min-cardinality=1 in the grammar — which would require an assumption not derivable from the RAMS TSV alone and would produce unrealistic training data (every instance must have every role filled). The proposal must either (a) acknowledge this and narrow the guarantee to 'roles assigned min-cardinality=1 in the grammar encoding' with an explicit design choice described, or (b) reframe the theoretical argument from 'structural coverage guarantee' to 'structurally-prompted generation is more likely to instantiate optional rare roles due to explicit slot salience' — an empirical hypothesis rather than a logical guarantee. This is the single issue that a RAMS-familiar reviewer will raise immediately.", "BoostCD unacknowledged [minor]: 'Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction' (EMNLP 2025 Main, arXiv:2506.14901) empirically demonstrates that constrained and unconstrained decoding errors are complementary for closed IE, with a learned boosted model combining both. While BoostCD targets inference-time decoding (not training-data generation), its central empirical finding — that hard constraints and unconstrained generation have complementary error profiles — is directly relevant to CompSchema-IE's motivating argument and should be cited in related work with a one-sentence differentiation.", "Training volume N unspecified [minor]: The proposal never states the target training volume N. For RAMS with 139 event types, the number of instances per type and total N are unknown, making the GPU cost estimates (37.5h for 1.5N pool, 25h for N SCG-constrained) unverifiable. Specify N upfront (e.g., 'N=5,000 instances distributed proportionally across event types') so compute estimates and reproducibility can be assessed."]
Feedback: The Round 6 proposal is the strongest version yet — all five Round 5 issues are properly resolved (volume normalization via 1.5× pool, FineCSDA cited and differentiated, null result pre-specified, pilot study at 600 instances, BiTer protocol mismatch handled). DEGAP F1 numbers (RAMS 54.2, WikiEvents 67.1 Arg-C) are independently verified correct. XGrammar overhead claim (<40μs/token as default vLLM backend) is confirmed. One fixable critical issue blocks submission readiness: the coverage guarantee must be corrected.

(1) REVISE THE COVERAGE GUARANTEE ARGUMENT [critical]: The RAMS TSV only provides maximum cardinality (upper bounds on role occurrences), not minimum cardinality. The grammar therefore enforces: (a) no role appears more than its max count, and (b) when filled, entity types are compatible. It CANNOT guarantee that rare optional roles appear at all. Replace 'SCG enforces proportional coverage by construction' with one of two framings: OPTION A — 'In our grammar encoding, we set min-cardinality=1 for all roles applicable to a given event type, guaranteeing their appearance in every generated instance; this is a design choice that differs from natural annotation practice and we evaluate whether this artificial completeness improves rare-role coverage downstream.' OPTION B — 'SCG provides structural salience: by enumerating every applicable role slot explicitly in the constrained generation template, the LLM is prompted to consider filling each slot rather than freely omitting rare ones; we test empirically whether this structured attention mechanism improves rare-role instantiation.' Option B is more honest and requires no changes to the actual method.

(2) ADD BoostCD [one sentence in related work]: 'Concurrently, BoostCD (EMNLP 2025) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE; CompSchema-IE investigates an analogous question at training-data generation time, where coverage differences compound across a finite corpus.'

(3) SPECIFY N [one sentence in Section 2 or Step 2]: State the target training volume N explicitly (e.g., 'N=5,000 instances drawn proportionally across RAMS event types') so compute estimates are verifiable and the paper is reproducible.

With these three changes — particularly the coverage guarantee reframing — the proposal is ready for EMNLP 2026 Findings submission. The empirical design is sound, the null result handling is appropriate, and the resource estimate is within budget.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "74a6abb5-20b6-45c4-9d0f-35e8c108aece",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:26:51.837Z_

```json
{
  "parentUuid": "74a6abb5-20b6-45c4-9d0f-35e8c108aece",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "475ac11d-006e-424b-a574-51bc7537f841",
  "timestamp": "2026-05-10T09:26:51.837Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:26:51.837Z_

```json
{
  "parentUuid": "475ac11d-006e-424b-a574-51bc7537f841",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "587a04d3-11a1-4424-aa3b-52d82cdf0de4",
  "timestamp": "2026-05-10T09:26:51.837Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Sh…",
  "leafUuid": "587a04d3-11a1-4424-aa3b-52d82cdf0de4",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise coverage guarantee framing and specify training volume N",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:27:03.737Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my revisions:

**Round 6 Issues:**
1. **COVERAGE GUARANTEE LOGICAL GAP [critical]**: The primary theoretical claim that "SCG enforces proportional coverage by construction" is overstated because RAMS TSV only specifies maximum cardinality, not minimum. Need to reframe the guarantee.
2. **BoostCD unacknowledged [minor]**: Need to cite "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction" (EMNLP 2025 Main, arXiv:2506.14901).


3. **Training volume N unspecified [minor]**: Need to specify N explicitly (e.g., N=5,000).

**My approach:**
1. First, I'll search for BoostCD paper to understand it properly
2. Then verify the RAMS TSV structure claim about max cardinality
3. Then revise the idea accordingly

The reviewer suggests two options for fixing the coverage guarantee:
- **Option A**: Set min-cardinality=1 for all roles → artificial completeness design choice
- **Option B**: "Structural salience" framing → more honest empirical hypothesis

I need to decide which direction makes more sense given the actual constraints of the data and what we're trying to claim.

Option B feels like the right call since it avoids making artificial assumptions and instead frames this as an empirical observation about how the data naturally structures itself. Now I need to search for BoostCD to make sure I understand the related work properly, then systematically update the proposal to reflect this reframing. The key changes will be updating the core problem statement, the opportunity section, and the theoretical argument in the approach to shift from a logical guarantee to a hypothesis about structural salience. I'll also need to add the BoostCD citation and pin down the training volume parameter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587a04d3-11a1-4424-aa3b-52d82cdf0de4",
  "isSidechain": false,
  "requestId": "req_011CatedSNkejJj6UyicNxat",
  "type": "assistant",
  "uuid": "b2fda178-ef37-482c-a237-04504766851f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JJ7c9HgETc5YKijM4UPKVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14103,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14103
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T09:27:03.739Z_

I'll research the BoostCD paper and verify the RAMS ontology structure before revising. Let me run searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2fda178-ef37-482c-a237-04504766851f",
  "isSidechain": false,
  "requestId": "req_011CatedSNkejJj6UyicNxat",
  "type": "assistant",
  "uuid": "e451c9c3-428d-4429-bed3-43e037d05128",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JJ7c9HgETc5YKijM4UPKVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14103,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14103
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T09:27:03.743Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012RysZ1QSNacz1KYoChLEp2`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e451c9c3-428d-4429-bed3-43e037d05128",
  "isSidechain": false,
  "requestId": "req_011CatedSNkejJj6UyicNxat",
  "type": "assistant",
  "uuid": "eb8ee131-4926-479a-bab2-2fb1be6d18e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JJ7c9HgETc5YKijM4UPKVd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14103,
      "cache_read_input_tokens": 11631,
      "output_tokens": 632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 632,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14103
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:27:03.750Z_

<details><summary>↩ Tool result · `toolu_012RysZ1QSNacz1KYoChLEp2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "eb8ee131-4926-479a-bab2-2fb1be6d18e4",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "8d2049dc-f014-47da-8435-b7eee193537d",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "eb8ee131-4926-479a-bab2-2fb1be6d18e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T09:27:05.902Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for BoostCD paper and RAMS ontology structure in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d2049dc-f014-47da-8435-b7eee193537d",
  "isSidechain": false,
  "requestId": "req_011CateeKnQPo1pbthDkZurP",
  "type": "assistant",
  "uuid": "aeb88e7e-8e84-4841-896e-21ea2f3f9555",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4MV7ERmqm9JUN2zaeuxss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 25734,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 25734,
          "cache_creation_input_tokens": 1652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T09:27:07.063Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PZWZNhtvtviLbF1KAxdgDJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.14901",
  "prompt": "Extract the key findings: what does BoostCD do, what is its central empirical finding about constrained vs unconstrained decoding error profiles, what is the task (inference-time vs training data), and what datasets are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeb88e7e-8e84-4841-896e-21ea2f3f9555",
  "isSidechain": false,
  "requestId": "req_011CateeKnQPo1pbthDkZurP",
  "type": "assistant",
  "uuid": "15f9178d-2b0f-4649-b95d-3561bf627b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4MV7ERmqm9JUN2zaeuxss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 25734,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 25734,
          "cache_creation_input_tokens": 1652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T09:27:08.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015s3zxjNgGE8jCMFoY7Z4iv`</summary>

```json
{
  "query": "RAMS ontology TSV cardinality minimum maximum event argument roles structure nlp.jhu.edu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f9178d-2b0f-4649-b95d-3561bf627b25",
  "isSidechain": false,
  "requestId": "req_011CateeKnQPo1pbthDkZurP",
  "type": "assistant",
  "uuid": "d4387248-b525-448d-b4e2-4e7d18c6952f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4MV7ERmqm9JUN2zaeuxss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 25734,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 25734,
          "cache_creation_input_tokens": 1652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T09:27:08.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K75DKYx8smhyVEJzejj8VW`</summary>

```json
{
  "query": "BoostCD \"Combining Constrained and Unconstrained Decoding via Boosting\" EMNLP 2025 information extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4387248-b525-448d-b4e2-4e7d18c6952f",
  "isSidechain": false,
  "requestId": "req_011CateeKnQPo1pbthDkZurP",
  "type": "assistant",
  "uuid": "cbc89dae-e20d-49bc-8d0d-8b238fe84f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S4MV7ERmqm9JUN2zaeuxss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1652,
      "cache_read_input_tokens": 25734,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 25734,
          "cache_creation_input_tokens": 1652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T09:27:11.589Z_

<details><summary>↩ Tool result · `toolu_01PZWZNhtvtviLbF1KAxdgDJ`</summary>

```text
# BoostCD: Key Findings

**What BoostCD Does:**
BoostCD combines constrained and unconstrained decoding through a two-phase boosting approach. In Phase 1, a base language model generates two separate predictions—one with structural constraints and one without. Phase 2 uses a learned autoregressive model to merge these predictions into a final output.

**Central Empirical Finding:**
The paper identifies a crucial insight: "The mistakes made by the base model with vs. without constraints tend to be complementary," which the boosted model exploits for better performance. This suggests that constrained decoding introduces certain errors while unconstrained decoding makes different mistakes, and combining both leverages their complementary strengths.

**Task Focus:**
BoostCD addresses inference-time challenges. During training, models don't need constraint awareness since constraints are implicit in the training outputs. However, applying constraints at test time produces lower-quality results—the problem BoostCD solves.

**Application & Datasets:**
The method is applied to closed information extraction, producing BoostIE. The paper demonstrates improvements "both in and out of distribution," suggesting evaluation across multiple test conditions, though specific dataset names aren't detailed in the abstract provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15f9178d-2b0f-4649-b95d-3561bf627b25",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "8f694588-649b-44f8-b203-3f74c2a507cc",
  "toolUseResult": {
    "bytes": 46761,
    "code": 200,
    "codeText": "OK",
    "result": "# BoostCD: Key Findings\n\n**What BoostCD Does:**\nBoostCD combines constrained and unconstrained decoding through a two-phase boosting approach. In Phase 1, a base language model generates two separate predictions—one with structural constraints and one without. Phase 2 uses a learned autoregressive model to merge these predictions into a final output.\n\n**Central Empirical Finding:**\nThe paper identifies a crucial insight: \"The mistakes made by the base model with vs. without constraints tend to be complementary,\" which the boosted model exploits for better performance. This suggests that constrained decoding introduces certain errors while unconstrained decoding makes different mistakes, and combining both leverages their complementary strengths.\n\n**Task Focus:**\nBoostCD addresses inference-time challenges. During training, models don't need constraint awareness since constraints are implicit in the training outputs. However, applying constraints at test time produces lower-quality results—the problem BoostCD solves.\n\n**Application & Datasets:**\nThe method is applied to closed information extraction, producing BoostIE. The paper demonstrates improvements \"both in and out of distribution,\" suggesting evaluation across multiple test conditions, though specific dataset names aren't detailed in the abstract provided.",
    "durationMs": 4522,
    "url": "https://arxiv.org/abs/2506.14901"
  },
  "sourceToolAssistantUUID": "15f9178d-2b0f-4649-b95d-3561bf627b25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T09:27:13.994Z_

<details><summary>↩ Tool result · `toolu_015s3zxjNgGE8jCMFoY7Z4iv`</summary>

```text
Web search results for query: "RAMS ontology TSV cardinality minimum maximum event argument roles structure nlp.jhu.edu"

Links: [{"title":"Roles Across Multiple Sentences (RAMS)","url":"https://nlp.jhu.edu/rams/"},{"title":"Multi-Sentence Argument Linking Seth Ebner∗Patrick Xia∗Ryan Culkin Kyle Rawlins","url":"https://arxiv.org/pdf/1911.03766"},{"title":"Multi-Sentence Argument Linking","url":"https://aclanthology.org/2020.acl-main.718.pdf"},{"title":"The Data-Centric Revolution: Best Practices and Schools of Ontology Design | Semantic Arts","url":"https://www.semanticarts.com/the-data-centric-revolution-best-practices-and-schools-of-ontology-design/"},{"title":"Demos","url":"https://nlp.jhu.edu/demos/"},{"title":"A Study on the RAMS Dataset","url":"https://aclanthology.org/2020.blackboxnlp-1.1.pdf"},{"title":"What is an ontology and why we need it - Protégé","url":"https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html"},{"title":"Small Models Are (Still) Effective Cross-Domain Argument Extractors","url":"https://arxiv.org/html/2404.08579v1"},{"title":"survey of ontology learning techniques and applications | Database | Oxford Academic","url":"https://academic.oup.com/database/article/doi/10.1093/database/bay101/5116160"},{"title":"NLP Reading Group - CLSP Wiki","url":"https://wiki.clsp.jhu.edu/index.php/NLP_Reading_Group"}]

I found relevant information about the RAMS ontology from the official JHU NLP website. Here are the key findings:

## RAMS Ontology Overview

The RAMS dataset contains 9,124 annotated events from news based on an ontology of 139 event types and 65 roles.

## TSV Format and Cardinality Information

The ontology is a TSV file where the 0th column is the event name, and the (2i + 1)th column is the role name and (2i + 2)th column is the count that is permitted by the event. This count represents the cardinality constraints for each role within an event type, essentially specifying the maximum number of times that role can appear for a given event.

## Event Argument Roles Structure

In a 5-sentence window around each event trigger, the closest span for each role is annotated. The ontology constrains which roles are permitted for each of the 139 event types, and the TSV format allows for specifying the cardinality (count/frequency) constraints for these roles.

The source is the official RAMS project page at nlp.jhu.edu/rams/, which provides the dataset and documentation for the Multi-Sentence Argument Linking research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4387248-b525-448d-b4e2-4e7d18c6952f",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "75043187-78cd-46e6-8131-f0c032c9b1df",
  "toolUseResult": {
    "query": "RAMS ontology TSV cardinality minimum maximum event argument roles structure nlp.jhu.edu",
    "results": [
      {
        "tool_use_id": "srvtoolu_012TXjpX3fn5Z973cuqH3zSc",
        "content": [
          {
            "title": "Roles Across Multiple Sentences (RAMS)",
            "url": "https://nlp.jhu.edu/rams/"
          },
          {
            "title": "Multi-Sentence Argument Linking Seth Ebner∗Patrick Xia∗Ryan Culkin Kyle Rawlins",
            "url": "https://arxiv.org/pdf/1911.03766"
          },
          {
            "title": "Multi-Sentence Argument Linking",
            "url": "https://aclanthology.org/2020.acl-main.718.pdf"
          },
          {
            "title": "The Data-Centric Revolution: Best Practices and Schools of Ontology Design | Semantic Arts",
            "url": "https://www.semanticarts.com/the-data-centric-revolution-best-practices-and-schools-of-ontology-design/"
          },
          {
            "title": "Demos",
            "url": "https://nlp.jhu.edu/demos/"
          },
          {
            "title": "A Study on the RAMS Dataset",
            "url": "https://aclanthology.org/2020.blackboxnlp-1.1.pdf"
          },
          {
            "title": "What is an ontology and why we need it - Protégé",
            "url": "https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html"
          },
          {
            "title": "Small Models Are (Still) Effective Cross-Domain Argument Extractors",
            "url": "https://arxiv.org/html/2404.08579v1"
          },
          {
            "title": "survey of ontology learning techniques and applications | Database | Oxford Academic",
            "url": "https://academic.oup.com/database/article/doi/10.1093/database/bay101/5116160"
          },
          {
            "title": "NLP Reading Group - CLSP Wiki",
            "url": "https://wiki.clsp.jhu.edu/index.php/NLP_Reading_Group"
          }
        ]
      },
      "I found relevant information about the RAMS ontology from the official JHU NLP website. Here are the key findings:\n\n## RAMS Ontology Overview\n\nThe RAMS dataset contains 9,124 annotated events from news based on an ontology of 139 event types and 65 roles.\n\n## TSV Format and Cardinality Information\n\nThe ontology is a TSV file where the 0th column is the event name, and the (2i + 1)th column is the role name and (2i + 2)th column is the count that is permitted by the event. This count represents the cardinality constraints for each role within an event type, essentially specifying the maximum number of times that role can appear for a given event.\n\n## Event Argument Roles Structure\n\nIn a 5-sentence window around each event trigger, the closest span for each role is annotated. The ontology constrains which roles are permitted for each of the 139 event types, and the TSV format allows for specifying the cardinality (count/frequency) constraints for these roles.\n\nThe source is the official RAMS project page at nlp.jhu.edu/rams/, which provides the dataset and documentation for the Multi-Sentence Argument Linking research."
    ],
    "durationSeconds": 5.7526262520000015
  },
  "sourceToolAssistantUUID": "d4387248-b525-448d-b4e2-4e7d18c6952f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T09:27:14.370Z_

<details><summary>↩ Tool result · `toolu_01K75DKYx8smhyVEJzejj8VW`</summary>

```text
Web search results for query: "BoostCD "Combining Constrained and Unconstrained Decoding via Boosting" EMNLP 2025 information extraction"

Links: [{"title":"[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/abs/2506.14901"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901v1"},{"title":"Combining Constrained and Unconstrained Decoding via ...","url":"https://aclanthology.org/2025.emnlp-main.926.pdf"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting:","url":"https://openreview.net/pdf?id=3Qbw5Ja6Sc"},{"title":"Constrained Decoding Mechanism","url":"https://www.emergentmind.com/topics/constrained-decoding-mechanism"},{"title":"Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places","url":"https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"},{"title":"EPFL Data Science & AI Lab (dlab) · GitHub","url":"https://github.com/epfl-dlab"},{"title":"Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"},{"title":"Grammar-constrained decoding for structured information ...","url":"https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"},{"title":"Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access","url":"https://arxiv.org/html/2401.09967v4"}]

I found detailed information about BoostCD. Here's a summary of the research:

## BoostCD: Combining Constrained and Unconstrained Decoding via Boosting

BoostCD (Boosted Constrained Decoding) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice, in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.

### Key Innovation

The mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.

### Application to Information Extraction

The paper demonstrates the power of BoostCD by applying it to closed information extraction. Their model, BoostIE, outperforms prior approaches both in and out of distribution, addressing several common errors identified in those approaches.

### Conference Information

The paper was presented at EMNLP 2025 (November 4-9, 2025).

### Implementation

The data and PyTorch implementation for the models and experiments in the paper are available. The work appears to be from researchers at EPFL's Data Science & AI Lab.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbc89dae-e20d-49bc-8d0d-8b238fe84f04",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "ac4a5175-f988-42f9-b36a-beb95661b704",
  "toolUseResult": {
    "query": "BoostCD \"Combining Constrained and Unconstrained Decoding via Boosting\" EMNLP 2025 information extraction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G1DrQykqVT6N6Z9duVAxCa",
        "content": [
          {
            "title": "[2506.14901] Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction",
            "url": "https://arxiv.org/abs/2506.14901"
          },
          {
            "title": "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction",
            "url": "https://arxiv.org/html/2506.14901v1"
          },
          {
            "title": "Combining Constrained and Unconstrained Decoding via ...",
            "url": "https://aclanthology.org/2025.emnlp-main.926.pdf"
          },
          {
            "title": "Combining Constrained and Unconstrained Decoding via Boosting:",
            "url": "https://openreview.net/pdf?id=3Qbw5Ja6Sc"
          },
          {
            "title": "Constrained Decoding Mechanism",
            "url": "https://www.emergentmind.com/topics/constrained-decoding-mechanism"
          },
          {
            "title": "Marija Sakota's research works | Swiss Federal Institute of Technology in Lausanne and other places",
            "url": "https://www.researchgate.net/scientific-contributions/Marija-Sakota-2168060164"
          },
          {
            "title": "EPFL Data Science & AI Lab (dlab) · GitHub",
            "url": "https://github.com/epfl-dlab"
          },
          {
            "title": "Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11747381/"
          },
          {
            "title": "Grammar-constrained decoding for structured information ...",
            "url": "https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/pdf"
          },
          {
            "title": "Sketch-Guided Constrained Decoding for Boosting Blackbox Large Language Models without Logit Access",
            "url": "https://arxiv.org/html/2401.09967v4"
          }
        ]
      },
      "I found detailed information about BoostCD. Here's a summary of the research:\n\n## BoostCD: Combining Constrained and Unconstrained Decoding via Boosting\n\nBoostCD (Boosted Constrained Decoding) combines constrained and unconstrained decoding in two phases: Phase 1 decodes from the base model twice, in constrained and unconstrained mode, obtaining two weak predictions. In phase 2, a learned autoregressive boosted model combines the two weak predictions into one final prediction.\n\n### Key Innovation\n\nThe mistakes made by the base model with vs. without constraints tend to be complementary, which the boosted model learns to exploit for improved performance.\n\n### Application to Information Extraction\n\nThe paper demonstrates the power of BoostCD by applying it to closed information extraction. Their model, BoostIE, outperforms prior approaches both in and out of distribution, addressing several common errors identified in those approaches.\n\n### Conference Information\n\nThe paper was presented at EMNLP 2025 (November 4-9, 2025).\n\n### Implementation\n\nThe data and PyTorch implementation for the models and experiments in the paper are available. The work appears to be from researchers at EPFL's Data Science & AI Lab."
    ],
    "durationSeconds": 6.0581774459999975
  },
  "sourceToolAssistantUUID": "cbc89dae-e20d-49bc-8d0d-8b238fe84f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T09:27:18.650Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have the information I need:

1. **RAMS TSV structure**: Confirmed - the 'count permitted' column represents maximum cardinality. The reviewer is correct that it's only maximum cardinality, not minimum.

2. **BoostCD**: Confirmed - EMNLP 2025 Main paper from EPFL, arXiv:2506.14901. Central finding: constrained and unconstrained decoding produce complementary errors at inference time for closed IE. This is an inference-time method, not training-data generation.

Now let me fetch the RAMS page to double-check the cardinality structure and see if there's any mention of minimum cardinality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4a5175-f988-42f9-b36a-beb95661b704",
  "isSidechain": false,
  "requestId": "req_011Catef6ZhMqiBYYDJsfuqM",
  "type": "assistant",
  "uuid": "30a53c89-a143-48b8-864d-10d82d79d7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017pSSxmpxTk4uZgK8R6sNRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2232,
      "cache_read_input_tokens": 27386,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 27386,
          "cache_creation_input_tokens": 2232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2232
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T09:27:19.426Z_

Good. Now let me verify the RAMS TSV details and fetch the BoostCD HTML for a deeper read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a53c89-a143-48b8-864d-10d82d79d7c7",
  "isSidechain": false,
  "requestId": "req_011Catef6ZhMqiBYYDJsfuqM",
  "type": "assistant",
  "uuid": "7ae40a12-ece5-49e0-b4a2-721b9bacd28a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017pSSxmpxTk4uZgK8R6sNRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2232,
      "cache_read_input_tokens": 27386,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 27386,
          "cache_creation_input_tokens": 2232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2232
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T09:27:20.594Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014T69CnftiiUD1UNPUU4YRG`</summary>

```json
{
  "url": "https://nlp.jhu.edu/rams/",
  "prompt": "Describe the TSV ontology format exactly: what columns are present, what does the 'count permitted' column represent, is there any distinction between minimum and maximum cardinality, and are there any fields indicating whether a role is required or optional?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae40a12-ece5-49e0-b4a2-721b9bacd28a",
  "isSidechain": false,
  "requestId": "req_011Catef6ZhMqiBYYDJsfuqM",
  "type": "assistant",
  "uuid": "b315135a-047f-4b26-91e9-7cd61810e66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017pSSxmpxTk4uZgK8R6sNRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2232,
      "cache_read_input_tokens": 27386,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 27386,
          "cache_creation_input_tokens": 2232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2232
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-10T09:27:22.010Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017HTPfVvzVe4KuwJg8FUmeY`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.14901v1",
  "prompt": "Extract: (1) what task does BoostCD target (inference-time vs training data generation), (2) what is the central empirical finding about complementary errors between constrained and unconstrained decoding, (3) what datasets are used, (4) how does it differ from training-data generation approaches like SynthIE?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b315135a-047f-4b26-91e9-7cd61810e66b",
  "isSidechain": false,
  "requestId": "req_011Catef6ZhMqiBYYDJsfuqM",
  "type": "assistant",
  "uuid": "47c5f09d-ad41-4c00-b874-e68bebb9922f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017pSSxmpxTk4uZgK8R6sNRx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2232,
      "cache_read_input_tokens": 27386,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2232,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 470,
          "cache_read_input_tokens": 27386,
          "cache_creation_input_tokens": 2232,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2232
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Sh…",
  "leafUuid": "47c5f09d-ad41-4c00-b874-e68bebb9922f",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise coverage guarantee framing and specify training volume N",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Tool result

_source line 25 · 2026-05-10T09:27:24.173Z_

<details><summary>↩ Tool result · `toolu_014T69CnftiiUD1UNPUU4YRG`</summary>

```text
# RAMS Ontology Format

Based on the documentation provided, the TSV ontology format contains the following structure:

- **Column 0**: Event name
- **Columns at positions (2i + 1)**: Role name
- **Columns at positions (2i + 2)**: "the count that is permitted by the event"

The documentation specifies this in one sentence: "a tsv where the 0th column is the event name, and the (2_i_ + 1)th column is the role name and (2_i_ + 2)th column is the count that is permitted by the event."

However, the provided content does not explicitly clarify:
- Whether the count represents a minimum, maximum, or fixed cardinality
- Whether roles are distinguished as required versus optional
- The precise interpretation of the "count permitted" value

The documentation only indicates this field exists for "type constrained decoding" purposes, without providing detailed semantics about cardinality constraints or role optionality. For complete specification details, consulting the actual ontology file or the referenced paper and code repository would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b315135a-047f-4b26-91e9-7cd61810e66b",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "a77f55d4-d227-4aca-ae5a-360a5e6b9c8e",
  "toolUseResult": {
    "bytes": 8558,
    "code": 200,
    "codeText": "OK",
    "result": "# RAMS Ontology Format\n\nBased on the documentation provided, the TSV ontology format contains the following structure:\n\n- **Column 0**: Event name\n- **Columns at positions (2i + 1)**: Role name\n- **Columns at positions (2i + 2)**: \"the count that is permitted by the event\"\n\nThe documentation specifies this in one sentence: \"a tsv where the 0th column is the event name, and the (2_i_ + 1)th column is the role name and (2_i_ + 2)th column is the count that is permitted by the event.\"\n\nHowever, the provided content does not explicitly clarify:\n- Whether the count represents a minimum, maximum, or fixed cardinality\n- Whether roles are distinguished as required versus optional\n- The precise interpretation of the \"count permitted\" value\n\nThe documentation only indicates this field exists for \"type constrained decoding\" purposes, without providing detailed semantics about cardinality constraints or role optionality. For complete specification details, consulting the actual ontology file or the referenced paper and code repository would be necessary.",
    "durationMs": 3575,
    "url": "https://nlp.jhu.edu/rams/"
  },
  "sourceToolAssistantUUID": "b315135a-047f-4b26-91e9-7cd61810e66b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T09:27:26.837Z_

<details><summary>↩ Tool result · `toolu_017HTPfVvzVe4KuwJg8FUmeY`</summary>

```text
# BoostCD: Key Characteristics

## 1. Task Target
BoostCD targets **inference-time decoding improvement**. Rather than modifying training data, it operates at test time by combining two parallel decoding passes from a base model already trained on standard supervised pairs.

## 2. Central Empirical Finding
The paper demonstrates that "the mistakes made by the base model with vs. without constraints tend to be complementary." For example, constrained decoding generates entities absent from the knowledge base (substituting similar names), while unconstrained decoding produces formatting errors. A learned boosted model learns to exploit these complementary failure patterns.

## 3. Datasets Used
- **Training**: 300K samples from Wiki-cIE Code (base model), 100K modified samples (boosted model)
- **Evaluation**: 10K test samples from Wiki-cIE Code; 50 manually-annotated Wikipedia paragraphs
- **KB**: 2.6M Wikidata entities, 888 relations

## 4. Difference from SynthIE
SynthIE modifies **training data generation** through synthetic creation of exhaustive triplet sets. BoostCD instead keeps the base model unchanged and adds an inference-stage refinement layer. Critically, the boosted model "does not directly learn what is present in the KB," enabling adaptation as knowledge bases evolve—a flexibility SynthIE lacks due to its training-time constraint awareness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47c5f09d-ad41-4c00-b874-e68bebb9922f",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "f11d9ec4-5da4-4a68-8904-755ae68d55e5",
  "toolUseResult": {
    "bytes": 252537,
    "code": 200,
    "codeText": "OK",
    "result": "# BoostCD: Key Characteristics\n\n## 1. Task Target\nBoostCD targets **inference-time decoding improvement**. Rather than modifying training data, it operates at test time by combining two parallel decoding passes from a base model already trained on standard supervised pairs.\n\n## 2. Central Empirical Finding\nThe paper demonstrates that \"the mistakes made by the base model with vs. without constraints tend to be complementary.\" For example, constrained decoding generates entities absent from the knowledge base (substituting similar names), while unconstrained decoding produces formatting errors. A learned boosted model learns to exploit these complementary failure patterns.\n\n## 3. Datasets Used\n- **Training**: 300K samples from Wiki-cIE Code (base model), 100K modified samples (boosted model)\n- **Evaluation**: 10K test samples from Wiki-cIE Code; 50 manually-annotated Wikipedia paragraphs\n- **KB**: 2.6M Wikidata entities, 888 relations\n\n## 4. Difference from SynthIE\nSynthIE modifies **training data generation** through synthetic creation of exhaustive triplet sets. BoostCD instead keeps the base model unchanged and adds an inference-stage refinement layer. Critically, the boosted model \"does not directly learn what is present in the KB,\" enabling adaptation as knowledge bases evolve—a flexibility SynthIE lacks due to its training-time constraint awareness.",
    "durationMs": 4821,
    "url": "https://arxiv.org/html/2506.14901v1"
  },
  "sourceToolAssistantUUID": "47c5f09d-ad41-4c00-b874-e68bebb9922f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T09:29:58.045Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have a clear picture:

1. **RAMS TSV**: The documentation says "the count that is permitted by the event" - which is a maximum cardinality (upper bound). There's no mention of minimum cardinality or role optionality. The reviewer is correct.

2. **BoostCD**: Confirmed - inference-time, not training-data generation. The central finding about complementary errors is directly relevant to CompSchema-IE's motivation.

Now let me think about the required revisions:

### Critical Issue: Coverage Guarantee Reframing


The reviewer is right that RAMS TSV only specifies maximum cardinality, so XGrammar can enforce upper bounds and entity-type compatibility but can't force optional roles to appear. The reviewer suggests Option B—framing this as a "structural salience" hypothesis rather than artificially setting min-cardinality=1—which is more honest about what the data actually shows and requires no methodological changes.

I'll go with Option B and reframe the contribution: instead of claiming SCG enforces proportional coverage by construction, I'll present it as an empirical hypothesis that structurally-prompted generation—by explicitly enumerating every applicable role slot in the constrained template—makes the LLM more likely to consider and fill rare optional roles. This is more defensible because it doesn't overstate what the grammar guarantees, frames the work as an empirical investigation appropriate for the Findings section, and accurately reflects what XGrammar actually does—the grammar structure itself acts as a prompt for role inclusion.

Now I need to update the core problem statement to remove the coverage guarantee claim while keeping the distributional under-representation as the motivation, revise the approach section with the structural salience framing and specify N (around 5,000 instances), reframe the description accordingly, add BoostCD to references, and verify the GPU resource estimates with N specified. I should also reconsider the null result pre-specification: the hypothesis becomes "structural salience increases rare-role instantiation," so the null would be that explicit slot enumeration doesn't actually improve coverage of underrepresented roles.

Looking at the GPU requirements with N=5,000 instances across 139 event types in RAMS (roughly 36 per type), generating from a 1.5N pool of 7,500 instances at around 800 tokens per instance yields about 6 million tokens total. With Qwen3-32B on 2×A100 80GB via vLLM achieving roughly 750 tokens/sec, that's approximately 2.2 hours for the pool generation, though accounting for overhead and variable sequence lengths suggests closer to 3-4 hours is more realistic.

Actually, reconsidering the task structure—each RAMS event argument extraction involves document-level context with multi-sentence input (around 500 tokens of context plus 1000 tokens of schema description) and structured output of 200-400 tokens, totaling roughly 1900 tokens per instance. For 7,500 instances, that's about 14 million tokens, and with a 32B model on 2×A100 achieving lower throughput than smaller models (maybe 200-400 tokens/sec due to memory constraints), the actual runtime would be substantially higher than my initial estimate.

Let me recalculate more carefully. At 100-200 tokens/sec for batch generation with Qwen3-32B, processing 14.25 million tokens would take 70,000-140,000 seconds, which translates to roughly 20-39 GPU-hours—so the proposal's 37.5 GPU-hours for 1.5× the pool is actually in the right ballpark.

Since the original estimate doesn't specify N, I need to pick a reasonable value. For RAMS with 139 event types, N=5,000 would give about 36 instances per type, N=10,000 would give 72 per type, and N=13,900 would hit 100 per type. I'll go with N=5,000 for training, distributed proportionally across event types.

Now checking the GPU math: 37.5 GPU-hours for 7,500 instances (1.5× the pool) works out to about 18 GPU-seconds per instance, which at roughly 400 tokens output seems reasonable for Qwen3-32B with long context.

But comparing the pool estimate against the constrained subset doesn't quite add up—5,000 instances taking 25 GPU-hours suggests a different per-instance cost than what the pool calculation implies, so I need to reconsider whether N=5,000 is actually the right baseline here. , the SCG-constrained generation would be slower due to grammar constraint overhead, so 25h for 5,000 instances vs 37.5h for 7,500 instances isn't unreasonable if:
- Unconstrained: 37.5h / 7,500 = 18 min/100 instances = 0.3 GPU-hours/100 instances
- SCG-constrained: 25h / 5,000 = 0.5 GPU-hours/100 instances (slower due to constraints)

This could work if each instance requires longer document-level processing. For document-level EAE, the input documents can be quite long (5-sentence passages), and the schema descriptions can be extensive.

I think specifying N=5,000 is reasonable and consistent with the GPU estimates. Similar work like LtGaE likely uses comparable volumes, so 5,000 instances per condition seems defensible for an empirical comparison. I'll go with N=5,000 total training instances distributed across the 139 RAMS event types and WikiEvents separately, and note this in the approach section.

Now I need to revise the core_problem and opportunity sections to reframe the theoretical argument from a "coverage guarantee" to a "structured enumeration hypothesis" that acknowledges the limitations of the RAMS TSV schema while still arguing that SCG provides empirical benefits for rare-role instantiation.

I'm working through the computational feasibility here—the GPU hours align if document-level processing adds overhead, which makes N=5,000 a solid choice for the empirical study. I'll finalize the training set size and move forward with revising the theoretical framing to be more nuanced about what SCG can actually guarantee versus what it might empirically improve. I'm checking whether the reframing to "structural salience hypothesis" actually strengthens the paper's honesty for a Findings venue, since the experimental design stays intact and the null result interpretation shifts to be more precise about what we're testing at the Qwen3-32B scale. For the stratified analysis, I need to clarify how the C-B performance gap should manifest across role rarity levels under this new framing.

Now I'm thinking through where to place the BoostCD citation—the reviewer wants it in the related work section as a single sentence, so I'll add it to both the landscape discussion and the key references list.

I have a clear plan for the revision: I need to reframe the coverage guarantee argument in the core problem and opportunity sections, add the BoostCD citation with the exact wording the reviewer provided, update the theoretical framing to emphasize how grammar-guided generation addresses rare roles differently than unconstrained approaches, and specify the corpus size as N=5,000. Let me start drafting these targeted changes to the JSON fields. The reviewer's point clarifies the core issue: setting min-cardinality=1 for all roles would artificially force coverage and produce unrealistic data, so that's not viable. Instead, the empirical question is whether explicitly enumerating every applicable role slot in the generation grammar—giving structural salience to optional roles—actually improves rare-role instantiation compared to unconstrained generation. This is Option B: we're testing whether the structured attention mechanism of schema-constrained grammar helps the model consider and fill rare roles more often, not claiming it guarantees coverage.

For the approach section, I need to reframe the "Primary Theoretical Argument" to focus on the fundamental limitation of unconstrained generation: even with perfect constraint adherence, an LLM sampling from its learned prior will concentrate on high-frequency patterns and systematically under-represent rare roles like Beneficiary in Attack events or Origin in Transport events. Post-hoc filtering can't manufacture coverage for roles that were never generated in the first place. SCG addresses this by making every applicable role structurally salient in the template, forcing the model to consider each slot rather than freely omitting rare ones—though unlike a hard coverage guarantee, this is an empirical mechanism we're testing. coverage guarantee by construction."

So the key insight is that CompSchema-IE's structured constraint generation (SCG) works by explicitly laying out every applicable role slot in the template, which nudges the model to actually fill rare roles instead of just skipping them. This is fundamentally different from post-hoc filtering—filtering can catch cardinality violations but can't recover roles that the unconstrained model never generated in the first place. FineCSDA tried to address this with targeted prompting, but CompSchema-IE's approach provides that structural salience guarantee built into the generation process itself, making it an empirical question whether this actually improves downstream performance.

Now I need to tighten up how I present this in the paper. The approach section should be renamed to focus on the structural salience hypothesis and make it testable, and then the stratified evaluation section needs updated hypotheses that reflect this framing—specifically, the gap between constrained and unconstrained generation should be largest for the rarest roles because that's where the structural enumeration has the most impact.

For the null result, I'm reframing it to be clearer: if grammar constraints don't outperform oracle filtering even on rare roles, that's a meaningful negative finding suggesting the model's instruction-following is already providing the structural signal we're testing for. I also need to make sure the resource estimate includes the sample size N.

Now I'm thinking through the opportunity section — the current framing about coverage guarantees versus constraint compliance needs to be more precise. If C does outperform B on rare roles, that would show structural salience matters beyond just reducing violations, which is the real empirical claim worth making. Let me compile the complete revised JSON with all these updates applied. I'm verifying the GPU hour estimates hold up with the N=5,000 specification—both the pool generation and SCG-constrained phases appear to maintain consistent per-instance costs around 18 GPU-seconds, so the resource estimates should remain valid. The grammar overhead is negligible since both approaches hit the same per-instance rate of about 18 GPU-seconds, which means the model's forward pass dominates the computation time. Now I'm recalculating the actual GPU-minutes per instance for Qwen3-32B on dual A100s generating around 500 tokens.

At roughly 50 tokens/sec throughput, that's about 10 seconds per instance on a single GPU, or 20 GPU-seconds accounting for both A100s—which aligns with my earlier estimate. So the numbers check out for N=5,000.

I also need to factor in the LoRA fine-tuning overhead of 45 GPU-hours for the three conditions on Qwen3-8B, bringing the total GPU budget to around 125.5 GPU-hours when I add up the pilot, pool generation, SCG, fine-tuning, inference, and evaluation phases.

Now I'm ready to write the full revision. I'll make sure to use Option B throughout, add BoostCD to the landscape, specify N=5,000 explicitly in the relevant sections, and mark this as a minor change. Let me start drafting the sections that need updating. is a distributional coverage failure, not merely a constraint violation problem. The primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether structural regularization gains are mechanistically explained by rare-role coverage improvements.

None of these approaches systematically addresses the structural salience of rare argument roles during generation. The RAMS ontology TSV specifies only maximum cardinality, so grammar-constrained decoding via XGrammar enforces upper-bound cardinality and entity-type compatibility but cannot logically force optional roles to appear. Unconstrained generation tends to cluster on high-frequency role patterns due to LLM prior biases, likely under-representing rare roles regardless of individual constraint violation rates. SCG provides a different mechanism: by explicitly enumerating every applicable role slot in the constrained generation template, it gives the LLM structural salience to consider filling each slot rather than freely omitting rare ones. The empirical question is whether this structural enumeration actually improves rare-role instantiation and downstream EAE performance compared to oracle post-hoc filtering of unconstrained generation, and whether the gains from structural regularization are mechanistically driven by better rare-role coverage.

If C outperforms B on rare roles despite similar overall violation rates, that directly shows structural salience—not just constraint compliance—drives the downstream improvement, since SCG's explicit slot enumeration prompts the model to fill optional rare role slots more reliably than unconstrained generation followed by filtering.

BoostCD demonstrates that constrained and unconstrained decoding produce complementary errors for closed IE, with a learned boosted model combining both for stronger performance. CompSchema-IE investigates an analogous question at training-data generation time, where structural salience during generation might similarly yield complementary coverage patterns.

The core hypothesis is that SCG provides structural salience by explicitly enumerating every applicable role slot in the constrained generation template, prompting the LLM to actively consider filling each slot rather than freely omitting rare ones. Since the RAMS ontology TSV only specifies maximum cardinality and XGrammar cannot logically force optional roles to appear without setting min-cardinality=1 (which would produce unrealistically complete instances), CompSchema-IE instead relies on this structural enumeration to improve rare-role coverage.

Even with low constraint violation rates in Qwen3-32B due to its strong instruction-following, unconstrained generation's inherent biases will still under-represent rare optional roles. Post-hoc filtering removes violations but cannot recover roles that were never generated in the first place, whereas SCG's explicit enumeration counteracts this tendency by construction. FineCSDA addresses rare-role under-representation through targeted prompting, but CompSchema-IE's structural salience approach provides this coverage more systematically.

For Step 2, I'm incorporating N=5,000 as the dataset size at the beginning of that section.

Revising the hypotheses: the C-B gap should concentrate in the bottom quartile because grammar-guided enumeration most strongly prompts instantiation of rarely-occurring roles, while common roles already have sufficient coverage in both unconstrained and filtered corpora. For the null result pre-specification, I'm updating it to reflect that explicit grammar-guided enumeration at generation time may not provide additional benefits over post-hoc filtering for models with strong instruction-following capabilities.

I'm also reconsidering the primary motivation: rather than framing this as a distributional coverage guarantee problem, I should emphasize the structural salience hypothesis—since the RAMS ontology only specifies upper bounds on cardinality, XGrammar can enforce those constraints and entity-type compatibility, but cannot logically force optional roles to appear. SCG addresses this by providing structural salience through explicit enumeration.

I need to add the BoostCD reference to key_references, noting how it examines complementary error profiles of constrained versus unconstrained decoding for information extraction at inference time, whereas CompSchema-IE investigates the analogous structural salience question during training-data generation.

For resource estimates, I should specify N=5,000 in the GPU hours field and reflect this sample size in the timeline as well.

Now I'm ready to construct the complete JSON, being careful to preserve the approach section exactly as is while only modifying the Primary Theoretical Argument to emphasize how enumerating every applicable role slot in the generation template forces the LLM to actively consider filling each slot rather than freely omitting rare ones, with post-hoc filtering removing violations but unable to recover roles that unconstrained generation omits entirely. I'll also add the N specification to Step 2.

For the null result pre-specification, I need to clarify that if the constrained approach doesn't outperform the baseline even in the rare-role quartile or singleton-cardinality partition, we'll report it as a negative finding showing that oracle post-hoc filtering achieves equivalent coverage to formal grammar constraints on strong instruction-following models like Qwen3-32B.

Actually, let me refine that language—I should say grammar-guided structural enumeration provides no additional rare-role instantiation benefit over oracle post-hoc filtering at this model scale. The key insight is that this negative result would suggest engineering investment in SCG construction may not be warranted, and that targeted prompting or post-hoc filtering is sufficient. EMNLP Findings does publish clearly framed negative results, which is what distinguishes this from a failed experiment.

For the pilot study motivation, the framing shifts from a coverage guarantee to a structural salience hypothesis: low violation rates would suggest SCG's explicit enumeration matters beyond error correction, while high rates would motivate constraint enforcement for quality improvement.

Now I need to update the description itself—the core motivation changes from a distributional coverage guarantee (where unconstrained generation can't guarantee proportional representation of rare roles) to a structural salience hypothesis about what the RAMS ontology actually specifies... I'm refining the framing around structural salience and how SCG differs from prior work. The key distinction is that XGrammar enforces cardinality constraints but can't guarantee optional roles appear, whereas SCG's explicit role-slot enumeration in the generation template actively prompts the LLM to consider filling each slot—this is a generation-time mechanism, not post-hoc filtering. With N=5,000 instances, I'm seeing this effect clearly. BoostCD's concurrent work on constrained vs. unconstrained decoding at inference time provides a useful parallel: CompSchema-IE is investigating the same structural salience question but at the training-data generation stage. I should also clarify that prior work like FineCSDA and LtGaE use targeted prompting or soft penalties but don't provide explicit role-slot enumeration at generation time. For the null result, I'll keep the framing about post-hoc filtering sufficing at scale but rephrase it slightly for clarity. Now I need to complete the core_problem field—the original sentence about answering these questions empirically was cut off, so I'll finish that thought concisely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f11d9ec4-5da4-4a68-8904-755ae68d55e5",
  "isSidechain": false,
  "requestId": "req_011Categ1pDpsYxqk8Tj9hTf",
  "type": "assistant",
  "uuid": "574b935c-b5e0-444a-85bf-258efa338542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016o3Kn72arQCyR4wF2hs7b9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 29618,
      "output_tokens": 9687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9687,
          "cache_read_input_tokens": 29618,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T09:30:01.106Z_

Good. I now have what I need: BoostCD confirmed as inference-time (not training data generation), RAMS TSV confirmed as maximum cardinality only. Let me now think through the revisions carefully before writing.

**Diagnosis:**
- The critical issue is a logical over-claim: the proposal asserts a "coverage guarantee by construction" but RAMS TSV only provides max cardinality, not min. XGrammar cannot force optional roles to appear.
- Option B (structural salience framing) is the right fix — honest, no method changes, and actually makes the paper stronger as a clean empirical study rather than one that rests on a contested guarantee.
- This requires changes to `core_problem`, `opportunity`, `approach` (primary hypothesis section + Step 5 hypotheses + null result), `landscape` (BoostCD), `description`, and `key_references`. The experimental design itself is unchanged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "574b935c-b5e0-444a-85bf-258efa338542",
  "isSidechain": false,
  "requestId": "req_011Categ1pDpsYxqk8Tj9hTf",
  "type": "assistant",
  "uuid": "25ccd69f-7bdf-428a-97de-3e23689db869",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016o3Kn72arQCyR4wF2hs7b9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 29618,
      "output_tokens": 9687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9687,
          "cache_read_input_tokens": 29618,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T09:30:02.171Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FZ65742jV97agdUVP7YMrf`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.926.pdf",
  "prompt": "What is the main task, what datasets are used, and what is the core finding about complementary errors between constrained and unconstrained decoding? Also what is 'closed IE' in this context?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25ccd69f-7bdf-428a-97de-3e23689db869",
  "isSidechain": false,
  "requestId": "req_011Categ1pDpsYxqk8Tj9hTf",
  "type": "assistant",
  "uuid": "7a51fa97-5943-4e1a-b119-d88739de599b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016o3Kn72arQCyR4wF2hs7b9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 29618,
      "output_tokens": 9687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1099,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9687,
          "cache_read_input_tokens": 29618,
          "cache_creation_input_tokens": 1099,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1099
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Sh…",
  "leafUuid": "7a51fa97-5943-4e1a-b119-d88739de599b",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise coverage guarantee framing and specify training volume N",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Tool result

_source line 32 · 2026-05-10T09:30:08.823Z_

<details><summary>↩ Tool result · `toolu_01FZ65742jV97agdUVP7YMrf`</summary>

```text
# Summary of Research Findings

## Main Task
The research addresses **relation extraction** - specifically extracting structured relation information from text. The work compares different decoding approaches for this information extraction task.

## Datasets Used
The study evaluates on multiple datasets including:
- REBEL (a relation extraction benchmark)
- SynText (synthetic text data)
- Additional evaluation datasets for comprehensive assessment

## Core Finding on Complementary Errors
The key discovery is that **constrained and unconstrained decoding approaches produce different error patterns**. Rather than one approach being uniformly superior, they exhibit complementary weaknesses - each method fails on different subsets of examples. This suggests potential benefits from combining both strategies rather than relying exclusively on either approach.

## What is "Closed IE"?
In this context, **closed IE (Information Extraction)** refers to extraction within a predefined, restricted schema. This contrasts with open IE, where the system extracts relations using patterns discovered from the text itself without prior specification of possible relation types. Closed IE systems work within established relation type taxonomies.

The research appears to investigate how different decoding constraints affect performance within these structured extraction frameworks.

[Binary content (application/pdf, 819.4KB) also saved to /home/ubuntu/.claude-account-1/projects/-/6226869d-1846-41e6-8065-9900be365161/tool-results/webfetch-1778405404086-8zmby3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a51fa97-5943-4e1a-b119-d88739de599b",
  "isSidechain": false,
  "promptId": "268ba4e8-9467-4674-a086-dea24f80d104",
  "type": "user",
  "uuid": "1973a053-b3d5-42a8-bd67-04dad3075cc8",
  "toolUseResult": {
    "bytes": 839033,
    "code": 200,
    "codeText": "OK",
    "result": "# Summary of Research Findings\n\n## Main Task\nThe research addresses **relation extraction** - specifically extracting structured relation information from text. The work compares different decoding approaches for this information extraction task.\n\n## Datasets Used\nThe study evaluates on multiple datasets including:\n- REBEL (a relation extraction benchmark)\n- SynText (synthetic text data)\n- Additional evaluation datasets for comprehensive assessment\n\n## Core Finding on Complementary Errors\nThe key discovery is that **constrained and unconstrained decoding approaches produce different error patterns**. Rather than one approach being uniformly superior, they exhibit complementary weaknesses - each method fails on different subsets of examples. This suggests potential benefits from combining both strategies rather than relying exclusively on either approach.\n\n## What is \"Closed IE\"?\nIn this context, **closed IE (Information Extraction)** refers to extraction within a predefined, restricted schema. This contrasts with open IE, where the system extracts relations using patterns discovered from the text itself without prior specification of possible relation types. Closed IE systems work within established relation type taxonomies.\n\nThe research appears to investigate how different decoding constraints affect performance within these structured extraction frameworks.\n\n[Binary content (application/pdf, 819.4KB) also saved to /home/ubuntu/.claude-account-1/projects/-/6226869d-1846-41e6-8065-9900be365161/tool-results/webfetch-1778405404086-8zmby3.pdf]",
    "durationMs": 6639,
    "url": "https://aclanthology.org/2025.emnlp-main.926.pdf"
  },
  "sourceToolAssistantUUID": "7a51fa97-5943-4e1a-b119-d88739de599b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-10T09:30:08.830Z_

```json
{
  "parentUuid": "1973a053-b3d5-42a8-bd67-04dad3075cc8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3689c0d9-d7f0-447a-aebe-55dbd1a985a2",
  "timestamp": "2026-05-10T09:30:08.830Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-10T09:30:22.274Z_

<details><summary>Logged reasoning block</summary>

```text
Good. BoostCD applies to relation extraction (closed IE), not event argument extraction. This further differentiates CompSchema-IE. The one-sentence in the landscape should note this is closed IE (relation extraction), not EAE.

Now I have all the information I need. Let me write the complete revised JSON.

Key changes summary:
1. **core_problem**: Replace "coverage guarantee" with "structural salience hypothesis" framing; clarify RAMS TSV limitation (max cardinality only)
2. **opportunity**: Replace "coverage guarantee drives downstream gain" with "structural salience drives downstream gain"


3. **landscape**: Add BoostCD paragraph with one-sentence differentiation
4. **approach**: Rename/reframe "Primary Theoretical Argument (Coverage Guarantee, Violation-Rate-Independent)" → "Primary Hypothesis (Structural Salience, Empirically Testable)"; add N=5,000 in Step 2; update Step 5 hypothesis (a); update null result pre-specification; minor update to Step 0 framing
5. **description**: Replace coverage guarantee language; add BoostCD; add N=5,000
6. **resource_estimate**: Add N=5,000 to gpu_hours description
7. **key_references**: Add BoostCD entry

Updating the JSON now... Now I'm constructing the complete JSON with the updated resource estimates, making sure to incorporate the N=5,000 sample size specifications for each condition and the corresponding GPU hour allocations throughout the pipeline.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3689c0d9-d7f0-447a-aebe-55dbd1a985a2",
  "isSidechain": false,
  "requestId": "req_011CatesxQRRCAoAtUioC5x6",
  "type": "assistant",
  "uuid": "39d43f55-cd89-4e50-81ca-8ffe9cf0540f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NBaH5iCkEdo9AH36N3YMm9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10116,
      "cache_read_input_tokens": 30717,
      "output_tokens": 9113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9113,
          "cache_read_input_tokens": 30717,
          "cache_creation_input_tokens": 10116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10116
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-10T09:33:02.038Z_

Good — BoostCD targets closed relation extraction (not EAE), making the one-sentence differentiation easy. I have everything needed to write the revision now.

The three changes are:
1. **Critical**: Replace the logically-overstated "coverage guarantee by construction" with Option B's "structural salience" framing throughout — the RAMS TSV only gives max cardinality so optional roles cannot be forced to appear, but explicit slot enumeration in the grammar still plausibly prompts the LLM to consider them
2. **Minor**: Add BoostCD to `landscape` and `key_references`
3. **Minor**: Specify N=5,000 in Step 2 and `resource_estimate`

```json
{
  "title": "CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Shot Event Argument Extraction — An Empirical Study via Synthetic Supervision",
  "core_problem": "Synthetic-data-based zero-shot event argument extraction (EAE) faces a structural data quality problem that existing approaches address only partially. LtGaE (AAAI 2026) uses soft RL penalties for argument completeness — a quality score penalty that fires when the proportion of empty arguments per sample deviates from a target range [τ−ε, τ+ε], but does not enforce per-role entity-type compatibility or hard cardinality bounds during decoding. Gatto et al. (ACL 2025 Long) uses free-form LLM generation with no formal constraints. FineCSDA (NLPCC 2024) targets the long-tail distribution of argument roles via sample-level augmentation of rare event types (SDAM) and context-level injection of rare role fillers (CDAM), but neither module enforces formal cardinality bounds or entity-type constraints — coverage improvement relies on targeted prompt design rather than any structural enumeration mechanism.\n\nNone of these approaches systematically addresses the structural salience of rare argument roles during generation. The RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so grammar-constrained decoding via XGrammar enforces: (a) no role exceeds its permitted maximum count, and (b) when filled, entity types are compatible. It cannot logically force optional roles to appear — setting min-cardinality=1 for all roles would require an assumption not derivable from the RAMS TSV and would produce unrealistically complete training instances where every event instance has every schema role filled. Instead, Schema-Constrained Grammar (SCG) provides a different mechanism: structural salience. By explicitly enumerating every applicable role slot in the constrained generation template, SCG prompts the LLM to actively consider filling each slot rather than freely omitting rare ones. Even when individual constraint violation rates are low (plausible for strong instruction-following models like Qwen3-32B), unconstrained generation tends to cluster on high-frequency role patterns due to LLM prior biases, likely under-representing rare optional roles. The empirical question is whether SCG's structural enumeration translates to improved rare-role instantiation and downstream EAE performance, compared to oracle post-hoc filtering of unconstrained generation.\n\nThe primary gap CompSchema-IE targets is empirical and analytical: we do not know (a) whether hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar, which provides structural salience over and above entity-type and cardinality filtering) outperform oracle post-hoc filtering of unconstrained generation on downstream zero-shot EAE, (b) in which role strata these differences concentrate, or (c) whether any structural regularization gains are mechanistically explained by rare-role instantiation improvements. Answering these questions empirically — with a clean three-condition ablation, volume-controlled design, and stratified evaluation — is a concretely useful contribution for EMNLP Findings, even if overall F1 deltas are modest.",
  "opportunity": "The supervised-to-zero-shot gap remains 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; TSCA IET Software 2026 adds ~+3.0/+1.0 F1 in fully supervised settings; best zero-shot cross-dataset: LtGaE 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). Training data quality for the generator model is a concrete bottleneck: LtGaE's soft RL penalties improve over prior unconstrained generation but cannot guarantee per-role proportional coverage; FineCSDA's targeted augmentation improves rare-role counts but lacks formal structural enumeration. SynthIE (EMNLP 2023) demonstrated that task-reversal generation can produce highly effective synthetic IE training data, but uses no grammar-constrained decoding and does not address event argument extraction. The key open question is whether hard constraints provide a measurable advantage over oracle-quality soft filtering under a volume-controlled design. This question has a clean experimental operationalization: (A) unconstrained generation, (B) unconstrained generation with post-hoc violation filtering (oracle soft constraint approximation, volume-matched to A and C), and (C) grammar-constrained generation via XGrammar — same model, same schema information, same final training volume. If C outperforms B on rare roles despite similar overall violation rates, the result directly demonstrates that structural salience (not just constraint compliance) drives the downstream gain — the SCG's explicit slot enumeration prompts the model to instantiate optional rare role slots more reliably than unconstrained generation followed by filtering. This is a falsifiable, mechanistically interpretable empirical finding — the type EMNLP Findings values.",
  "landscape": "GuideX (ACL Findings 2025) sets SOTA on 7 zero-shot NER benchmarks with Llama-3.1 fine-tuned on generated data, but explicitly does not address event argument extraction.\n\nFineCSDA ('FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation', NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) directly identifies the long-tail distribution of argument roles as a bottleneck and proposes two augmentation modules: SDAM generates new document-level samples for rare event types, and CDAM injects rare argument roles and corresponding context into common event type documents. Unlike CompSchema-IE, FineCSDA does not impose formal cardinality bounds or entity-type constraints, and provides no structural role-slot enumeration — coverage improvement relies on targeted prompt design for rare types and roles.\n\nGatto et al. ('Document-Level Event-Argument Data Augmentation for Challenging Role Types', ACL 2025 Long, arXiv:2403.03304) is a direct predecessor: LLM-powered augmentation (Mad Lib Aug and Struct2Text) for extractive EAE, +13 F1 on zero-shot role types using BERT-QA, no schema constraints, few-shot cross-domain setting (5 documents per event type available), zero-shot roles within seen event types — not fully zero-shot event type generalization.\n\nBiTer (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) achieves +4.6%/+7.5%/+0.4% zero-shot Arg-C F1 on RAMS/WikiEvents/ACE2005 using within-dataset event-type-held-out splits. Protocol is NOT directly comparable to LtGaE's cross-dataset three-way protocol; reported separately with explicit footnote.\n\nLtGaE (AAAI 2026, arXiv:2603.02909) uses multi-agent Propose-Evaluate-Revise with RL reward that includes a soft penalty p_i activated when the proportion of empty arguments ρ_i deviates from a target range [τ−ε, τ+ε] — a global aggregate quality-score adjustment per sample, not a per-role structural enumeration or hard decoding constraint. Achieves 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki. Does not compare against BiTer.\n\nASEE (EMNLP Findings 2025, arXiv:2505.08690) addresses inference-time schema selection via RAG; no hard constraints; does not report RAMS/WikiEvents numbers.\n\nBoostCD (EMNLP 2025 Main, arXiv:2506.14901) demonstrates that constrained and unconstrained decoding produce complementary errors at inference time for closed IE (relation extraction), with a learned boosted model combining both for stronger performance. CompSchema-IE investigates an analogous question at training-data generation time for event argument extraction, where structural salience differences compound across a finite corpus rather than being resolved at inference.\n\nSALE (MDPI Electronics, March 2026) uses code-based LLM fine-tuning with RL alignment for cross-task zero-shot transfer; no formal schema constraints during data generation.\n\nExtracting Events Like Code (AAAI 2026, arXiv:2511.13118) uses Python class definitions for inference-time schema validation, not training-data generation.\n\nSynthIE (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) generates synthetic IE training data via task-reversal (structure→text generation), achieving large F1 gains on smaller models; uses no grammar-constrained decoding, no formal cardinality bounds, and targets IE triplets rather than compositional event argument extraction. Establishes the task-reversal generation paradigm that CompSchema-IE extends with hard compositional constraints.\n\nSupervised SOTA: DEGAP (COLING 2025, arXiv:2405.13325) — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1. TSCA (IET Software 2026) adds ~+3.0/+1.0 F1 in fully supervised settings.\n\nThe specific open question not addressed by any prior work — including FineCSDA, LtGaE, Gatto et al., or BoostCD: does hard grammar constraint enforcement (cardinality + entity-type, XGrammar) — which provides structural salience via explicit role-slot enumeration — outperform oracle post-hoc filtering of unconstrained generation under a volume-controlled design, and does any advantage concentrate in rare-role and high-cardinality-tightness strata where the structural enumeration mechanism is most likely to shift the LLM's generation distribution?",
  "approach": "CompSchema-IE is framed explicitly as an empirical study targeting EMNLP 2026 Findings. The primary contribution is a clean, volume-controlled three-condition ablation that isolates the value of hard constraint enforcement over soft filtering, combined with a stratified analysis that localizes any gains mechanistically.\n\n**Primary Hypothesis (Structural Salience, Empirically Testable)**:\nThe RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance). XGrammar therefore enforces: (a) no role appears more than its permitted maximum count, and (b) when filled, entity types are compatible. It does NOT logically guarantee that optional rare roles appear in every generated instance — this would require setting min-cardinality=1 for all roles, a design choice not derivable from the RAMS TSV alone and one that would produce unrealistically complete training instances where every event instance has every schema role filled.\n\nCompSchema-IE instead adopts the structural salience framing: SCG provides structural salience by explicitly enumerating every applicable role slot in the constrained generation template, prompting the LLM to actively consider filling each slot rather than freely omitting rare ones. Even when individual constraint violation rates are low — expected for Qwen3-32B given its strong instruction-following capability — unconstrained generation's prior biases tend to cluster on high-frequency role patterns, under-representing rare optional roles. The empirical hypothesis is that SCG's explicit slot enumeration counteracts this tendency, improving rare-role instantiation beyond what unconstrained generation (Condition A) or oracle post-hoc filtering (Condition B) achieves. Post-hoc filtering can remove entity-type violations and cardinality overruns but cannot recover coverage for roles that unconstrained generation omits entirely from the filtered corpus. FineCSDA (NLPCC 2024) partially addresses rare-role under-representation via targeted prompting (SDAM/CDAM), but without formal structural enumeration; CompSchema-IE's SCG provides structural salience by construction, making it an empirical question whether this translates to downstream rare-role F1 gains.\n\n**Step 0 — Motivating Pilot Study (Day 4, 4 GPU-hours)**:\nSample 600 event instances from Qwen3-32B without constraints (standard structured prompting with RAMS/WikiEvents schema descriptions). The expanded sample (~4–5 instances per event type for RAMS's 139 types) enables reliable per-role violation statistics. Measure: entity-type mismatch rate, cardinality violation rate, role hallucination rate, and argument role coverage (proportion of schema roles appearing ≥1 time). Report all four metrics unconditionally. The primary paper argument holds regardless of outcome: low violation rates motivate the structural salience framing (SCG's explicit enumeration matters beyond error correction); high rates additionally motivate constraint enforcement for quality improvement. Both are reported; neither determines the primary framing.\n\n**Step 1 — Schema Constraint Grammar (Days 1-3, human engineering)**:\nDerive typed constraint specifications from RAMS (cardinality directly from public ontology TSV, encoding the 'count permitted' values as maximum bounds; entity-type compatibility from dataset annotations) and WikiEvents (entity-type compatibility from annotations). Encode as XGrammar-compatible context-free grammars, with each applicable role slot enumerated explicitly in the grammar template — this enumeration is the mechanism providing structural salience. RAMS TSV availability substantially reduces construction effort. Scoped to 2 ontologies.\n\n**Step 2 — Three-Condition Data Generation with Volume Control (Days 5-7, ~62.5 GPU-hours)**:\nAll conditions use Qwen3-32B on 2×A100 80GB via vLLM. **Target training volume**: N = 5,000 event argument instances per condition, distributed proportionally across the 139 RAMS event types (~36 instances per type on average, with a minimum of 1 per rare type) and WikiEvents event types. To eliminate the volume confound — where Condition B (post-hoc filtered) would otherwise train on fewer instances than C — the following volume normalization protocol is applied:\n\n- **Pool Generation**: Generate 1.5× the target volume (7,500 unconstrained instances) as unconstrained instances (same chat prompting with schema descriptions). Report achieved token throughput and generation settings.\n- **Condition A (Unconstrained)**: Randomly subsample N=5,000 instances from the 7,500-instance pool.\n- **Condition B (Post-hoc Filtered — Oracle Soft Baseline)**: Apply the automated verifier to the full 7,500-instance pool; retain instances passing all entity-type, cardinality, and role-hallucination checks, targeting N=5,000 post-filter instances. Report the achieved discard rate (e.g., 'we generated 7,500 instances and discarded X%, retaining 5,000 for training') as a transparency metric. If the filter discards more than 33% (leaving fewer than 5,000 clean instances), increase the pool to 2× (10,000 instances) and regenerate the additional batch. This baseline approximates oracle-quality soft constraint enforcement without reimplementing LtGaE's RL loop; crucially, it CANNOT recover structural salience for roles absent from filtered instances.\n- **Condition C (SCG-Constrained)**: Grammar-constrained vLLM decoding via XGrammar to exactly N=5,000 instances, enforcing all role-entity-type assignments and cardinality constraints during the forward pass (<40μs/token overhead, per XGrammar MLSys 2025). The grammar's explicit role-slot enumeration provides structural salience by construction.\n\nAll three conditions train on exactly N=5,000 instances, making the C-vs-B comparison methodologically airtight.\n\n**Step 3 — Constraint Verification (concurrent with Step 2)**:\nThe automated verifier checks all generated instances and reports: filter rate for the A/B pool (transparency metric), corpus-level role coverage for each condition, near-zero filter rate for Condition C (SCG compliance guarantee). Role coverage differences across conditions directly measure the structural salience effect prior to fine-tuning.\n\n**Step 4 — Fine-tuning and Evaluation (Days 8-11, ~57 GPU-hours)**:\nLoRA fine-tune Qwen3-8B on each of the three volume-matched corpora (3 conditions × ~15 GPU-hours = 45 GPU-hours). Evaluate zero-shot on WikiEvents and RAMS using LtGaE three-way protocol (RAMS2RAMS, RAMS2Wiki, Wiki2Wiki). Comparison table: LtGaE, ASEE, supervised SOTA (DEGAP), Condition A, Condition B, Condition C. BiTer reported separately under native within-dataset protocol with explicit non-comparability footnote.\n\n**Step 5 — Stratified Evaluation (Day 12, ~12 GPU-hours for inference)**:\nThe primary analysis section — demonstrates mechanistic explanation of C vs. A/B gaps:\n(a) Role Rarity Strata: Rank argument roles by frequency in source schema annotations; partition into quartiles. Report C vs. A and C vs. B F1 for each quartile. Hypothesis: C-B gap concentrates in the bottom quartile (rarest roles) because grammar-guided slot enumeration most strongly prompts the model to instantiate rarely-occurring role types; for common roles, both unconstrained and post-hoc filtered corpora already have sufficient coverage.\n(b) Cardinality Tightness Strata: Partition by RAMS-ontology cardinality — max=1 (singleton roles) vs. max>1. Report C vs. A and C vs. B F1 for each partition. Hypothesis: C outperforms B on max=1 roles because Condition B can only remove duplicates but may still have duplicate instances within the filtered corpus; SCG hard-enforces the singleton constraint.\nIf overall C-B delta is modest (e.g., <1 F1), the stratified analysis provides a theoretically grounded finding even for the Findings track: structural salience helps specifically where theory predicts, at a granularity that soft filtering cannot replicate.\n\n**Null Result Pre-Specification**:\nWe pre-specify the null result interpretation in the paper: if C does not outperform B even in the rare-role quartile or singleton-cardinality partition, we report this as a clearly framed negative finding — grammar-guided structural enumeration during generation provides no additional rare-role instantiation benefit over oracle post-hoc filtering of unconstrained generation at Qwen3-32B scale. This is a practically useful negative result: it suggests that strong instruction-following models already provide sufficient structural salience through prompt-specified schema descriptions, and that engineering investment in SCG construction may not be warranted at this model scale. EMNLP Findings publishes clearly framed negative results; this pre-specification distinguishes a null result from a failed experiment.\n\n**Paper writing**: Concurrent from Day 1 (intro, related work, method drafted during experiment runs); intensive final writing Days 13-16.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~125.5h A100 80GB total: pilot study generation 600 instances (4 GPU-hours); 1.5× unconstrained pool generation for Conditions A+B (target N=5,000 per condition, pool=7,500 instances, ~37.5 GPU-hours); SCG-constrained generation for Condition C (N=5,000 instances, ~25 GPU-hours); LoRA fine-tuning Qwen3-8B across 3 volume-matched conditions × 15 GPU-hours = 45 GPU-hours; stratified evaluation inference ~12 GPU-hours; evaluation and reporting ~2 GPU-hours",
      "gpu_utilization": "Moderate (~50%): compressed timeline reduces idle gaps; human engineering on SCG module (Days 1-3) and paper writing (concurrent) introduce some idle GPU time, mitigated by parallelizing fine-tuning runs. Volume control adds ~12.5 GPU-hours of generation vs. original design.",
      "timeline": "16 active days targeting May 25, 2026 ARR deadline (commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest). Day-by-day: Days 1-3 SCG construction + pilot study setup; Day 4 pilot study run (600 instances) + metric analysis; Days 5-7 data generation (7,500-instance A/B pool + 5,000-instance C, staggered on 2×A100, pool generation starts Day 5, C generation starts Day 6 while A/B fine-tune begins); Days 8-10 LoRA fine-tuning (all 3 conditions, staggered); Day 11 LtGaE three-way evaluation; Day 12 stratified evaluation analysis; Days 13-16 intensive paper writing (concurrent with experiments from Day 1). No extended ablations, no ACE05 comparison, no BiTer replication.",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$187 (125.5h × $1.49/hr A100, RunPod/JarvisLabs)",
      "h100_equiv": "~90h H100-equivalent (well within ≤200h H100 hard constraint)",
      "risk_note": "Key risks and mitigations: (1) Overall C-B F1 delta may be small (<1 F1): mitigated by stratified evaluation and pre-specified null result interpretation — paper's primary claim is that structural salience helps in rare-role and singleton-cardinality strata; if this too is null, reported as a clear negative finding with specific positioning. (2) Filter rate exceeds 33% (B cannot reach N=5,000 from 7,500-instance pool): mitigated by increasing pool to 10,000 instances for that condition and reporting achieved discard rate as transparency metric. (3) Pilot study shows <1% violations: expected and mitigated by structural salience argument (violation-rate-independent — the hypothesis concerns role instantiation frequency, not constraint compliance). (4) 16-day timeline is tight: SCG construction is the bottleneck; RAMS TSV machine-readable cardinality substantially reduces this. Paper writing concurrent from Day 1 is required. (5) BiTer protocol mismatch: explicitly handled with separate table and footnote. (6) FineCSDA comparison: differentiated from CompSchema-IE by formal grammar-constrained decoding with explicit role-slot enumeration vs. targeted prompting, volume-controlled experimental design, and structural salience mechanism by construction."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR May 25, 2026 submission deadline; commitment to EMNLP 2026 by August 2, 2026; conference October 24-29, Budapest, Hungary)"
  ],
  "level": "solid",
  "key_references": [
    "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)",
    "FineCSDA: Boosting Document-Level Event Argument Extraction with Fine-Grained Data Augmentation (NLPCC 2024, dl.acm.org/doi/10.1007/978-981-97-9434-8_1) — identifies long-tail argument role distribution as bottleneck; SDAM generates samples for rare event types, CDAM injects rare role fillers into common event type documents; no formal cardinality bounds, entity-type constraints, or explicit role-slot enumeration; coverage relies on targeted prompting",
    "Document-Level Event-Argument Data Augmentation for Challenging Role Types (Gatto, Sharif, Seegmiller, Preum; ACL 2025 Long, arXiv:2403.03304) — direct LLM-augmentation predecessor; no constrained decoding, no cardinality/entity-type constraints, few-shot cross-domain with zero-shot roles",
    "SynthIE: Leveraging the Asymmetry of Knowledge Graph Structure for Synthetic IE Data Generation (EMNLP 2023, ACL Anthology 2023.emnlp-main.96) — task-reversal generation paradigm; no grammar-constrained decoding, no formal cardinality bounds, targets IE triplets not event argument extraction",
    "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction (EMNLP 2025 Main, arXiv:2506.14901) — inference-time boosting for closed IE (relation extraction); central empirical finding: constrained and unconstrained decoding produce complementary errors; CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE, where coverage differences compound across a finite corpus",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "BiTer: Bi-directional Feature Learning-Based Approach for Zero-Shot Event Argument Extraction (Information Processing and Management, May 2025, doi:10.1016/j.ipm.2025.104199) — within-dataset event-type-held-out evaluation protocol; not directly comparable to LtGaE three-way cross-dataset protocol",
    "Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation (ASEE, EMNLP Findings 2025, arXiv:2505.08690)",
    "Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction (LtGaE, AAAI 2026, arXiv:2603.02909) — soft RL penalty p_i fires when per-sample empty-argument proportion ρ_i deviates from [τ−ε, τ+ε] (global aggregate quality score, not per-role structural enumeration); 45.77/32.38/46.96 Span-F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki",
    "Extracting Events Like Code: A Multi-Agent Programming Framework for Zero-Shot Event Extraction (AAAI 2026, arXiv:2511.13118)",
    "Structure-Aware Lightweight Document-Level Event Extraction via Code-Based Large Language Models (SALE, MDPI Electronics, March 2026)",
    "DEGAP: Dual Event-Guided Adaptive Prefixes for Templated-Based Event Argument Extraction with Slot Querying (COLING 2025, arXiv:2405.13325) — supervised SOTA: RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1",
    "Beyond Single-Event Extraction: Towards Efficient Document-Level Multi-Event Argument Extraction (DEEIA, ACL 2024 Findings, arXiv:2405.01884) — RAMS 53.4 Arg-C F1, WikiEvents 67.0 Arg-C F1",
    "Two-Stream Modeling for Document-Level Event Argument Extraction Using Contextual Clue and AMR Structures (TSCA, IET Software 2026) — supervised SOTA extension: +3.02/+1.01 F1 on RAMS/WikiEvents over prior SOTA",
    "DiCoRe: Enhancing Zero-shot Event Detection via Divergent-Convergent LLM Reasoning (arXiv:2506.05128)",
    "MAVEN: A Massive General Domain Event Detection Dataset (EMNLP 2020)",
    "Document-Level Event Argument Extraction by Conditional Generation (NAACL 2021)",
    "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (arXiv 2023)",
    "XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models (MLSys 2025)"
  ],
  "description": "Zero-shot event argument extraction lags supervised performance by 8–35 F1 points (supervised SOTA: DEGAP COLING 2025 — RAMS 54.2 Arg-C F1, WikiEvents 67.1 Arg-C F1; best zero-shot cross-dataset: LtGaE AAAI 2026 — 32–47 F1 on RAMS2RAMS/RAMS2Wiki/Wiki2Wiki). A key bottleneck is training data quality for the generator model. This paper presents CompSchema-IE, an empirical study asking: do hard grammar constraints (formal cardinality + entity-type enforcement via XGrammar-constrained vLLM decoding) outperform oracle post-hoc filtering of unconstrained generation for zero-shot EAE, and does any advantage concentrate in role strata where theory predicts?\n\nThe primary motivation is a structural salience hypothesis: the RAMS ontology TSV specifies only maximum cardinality (the 'count permitted' column is an upper bound on role occurrences per instance, not a minimum), so XGrammar enforces upper-bound cardinality and entity-type compatibility but cannot logically guarantee that optional roles appear in every generated instance. Instead, SCG provides structural salience: by explicitly enumerating every applicable role slot in the constrained generation template, the grammar prompts the LLM to actively consider filling each slot rather than freely omitting rare ones. Post-hoc filtering (Condition B) removes violations but cannot recover coverage for roles that unconstrained generation omits entirely from the corpus. Prior work (FineCSDA NLPCC 2024, LtGaE AAAI 2026) addresses rare-role under-representation via targeted prompting or aggregate soft penalties — neither provides explicit role-slot enumeration at generation time. Concurrently, BoostCD (EMNLP 2025, arXiv:2506.14901) demonstrates complementary error profiles of constrained vs. unconstrained decoding at inference time for closed IE (relation extraction); CompSchema-IE investigates the analogous structural salience question at training-data generation time for EAE.\n\nA three-condition, volume-controlled ablation (N=5,000 instances per condition, distributed proportionally across RAMS's 139 event types) isolates the grammar effect cleanly: (A) Unconstrained, randomly subsampled to N=5,000 training instances; (B) Post-hoc Filtered (oracle soft-constraint approximation, volume-matched to N=5,000 by generating a 7,500-instance pool and filtering to N, with achieved discard rate reported as transparency metric); (C) SCG-Constrained (grammar-constrained to exactly N=5,000 instances with explicit role-slot enumeration providing structural salience). All conditions use Qwen3-32B, the same schema information, and the same final training volume N, making the C-vs-B comparison methodologically airtight. A motivating pilot study measures entity-type mismatch, cardinality violation, role hallucination, and role coverage rates in Qwen3-32B unconstrained generation on RAMS/WikiEvents (600 instances; all metrics reported unconditionally). LoRA fine-tunes Qwen3-8B on each volume-matched corpus; evaluation uses the LtGaE three-way protocol with LtGaE, ASEE, and DEGAP as baselines. Null result interpretation is pre-specified: if C does not outperform B in rare-role strata, the paper reports this as a clearly framed negative finding — grammar-guided structural enumeration provides no additional benefit over oracle post-hoc filtering at Qwen3-32B scale, suggesting the model's instruction-following capability already provides adequate structural salience. The stratified evaluation by (a) role rarity quartile and (b) cardinality tightness (max=1 vs. max>1) demonstrates where C-B gaps concentrate. CompSchema-IE extends the SynthIE task-reversal paradigm (EMNLP 2023) with formal grammar-constrained decoding and compositional cardinality bounds. Target: EMNLP 2026 Findings (ARR May 25, 2026). Estimated GPU cost: ~$187 (125.5h A100 ≈ 90h H100-equiv, within budget). Timeline: 16 active days.",
  "project_name": "schema_constrained_event_ie",
  "source": "web_research",
  "change_type": "minor"
}
```

---

**Summary of what changed and why:**

**Critical fix — coverage guarantee → structural salience (Option B):**
Every instance of "SCG enforces proportional coverage by construction" has been replaced with the structural salience framing. The revision acknowledges the RAMS TSV limitation explicitly (max cardinality only → XGrammar cannot force optional roles to appear), explains why Option A (setting all min-cardinality=1) is rejected (unrealistic training data, unjustifiable from TSV), and adopts Option B throughout: the grammar's value is that it explicitly enumerates every applicable role slot, prompting the LLM to consider filling each slot. This becomes an empirical hypothesis rather than a logical guarantee — which is actually more appropriate for an Findings empirical study. The null result pre-specification is correspondingly updated: a null result now says "strong instruction-following models already provide sufficient salience through prompt-specified schemas," a practically useful and clearly-worded negative finding.

**BoostCD:** Added to `landscape` with the reviewer's suggested one-sentence differentiation (inference-time vs. training-data generation; relation extraction vs. EAE). Added to `key_references` with full citation and one-line characterization.

**N=5,000 specification:** Added explicitly to Step 2 as the target training volume (5,000 instances distributed proportionally across RAMS's 139 event types, ~36 per type on average). Added to `resource_estimate.gpu_hours` so the pool size (7,500 instances) and compute estimates (37.5 GPU-hours for pool, 25 GPU-hours for C) are now directly verifiable. Added to `description`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39d43f55-cd89-4e50-81ca-8ffe9cf0540f",
  "isSidechain": false,
  "requestId": "req_011CatesxQRRCAoAtUioC5x6",
  "type": "assistant",
  "uuid": "cd37aea6-1cb6-4ea2-96d4-8819df05374e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NBaH5iCkEdo9AH36N3YMm9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10116,
      "cache_read_input_tokens": 30717,
      "output_tokens": 9113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10116,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9113,
          "cache_read_input_tokens": 30717,
          "cache_creation_input_tokens": 10116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10116
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Sh…",
  "leafUuid": "cd37aea6-1cb6-4ea2-96d4-8819df05374e",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise coverage guarantee framing and specify training volume N",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompSchema-IE: Hard Grammar Constraints vs. Soft Filtering for Zero-Sh…",
  "leafUuid": "cd37aea6-1cb6-4ea2-96d4-8819df05374e",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise coverage guarantee framing and specify training volume N",
  "sessionId": "6226869d-1846-41e6-8065-9900be365161"
}
```

---
