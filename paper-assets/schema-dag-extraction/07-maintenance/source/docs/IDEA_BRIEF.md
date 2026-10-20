# Idea Brief: Does Type Confusability Drive Schema-Induced Degradation in LLM Information Extraction? An Empirical Study and Principled Decomposition Framework


- **Idea ID**: `idea_007`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-6
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR May 25, 2026 submission — 15 days from today; commitment deadline August 2, 2026; reviews due June 29; meta-reviews July 30; conference October 24-29, Budapest, Hungary). Feasible with dual-contribution framing: Contribution A (empirical study) is completable in 3 days and self-contained; Contribution B (SDGD) on 3 core benchmarks (ACE05, Few-NERD, DocRED) by day 12. MAVEN and SciERC for camera-ready., AACL-IJCNLP 2026 (same ARR May 25, 2026 submission; commitment deadline August 26, 2026; Hengqin, China November 6-10, 2026 — fallback if EMNLP reviews suggest Findings-level), ARR August 3, 2026 for EACL 2027 (commitment deadline October 11, 2026 — backup with full 3-month timeline for complete experiment suite including moderate-correlation analysis if May 25 is infeasible)

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

LLMs with constrained decoding now guarantee 100% structurally valid outputs, but complex extraction schemas still cause severe semantic quality degradation. Multiple converging lines of evidence establish this: The Format Tax (April 2026) shows prompt-level effects account for ~71% of format-induced degradation; UniNER (ICLR 2024) demonstrated per-type querying outperforms batch querying by 3.3 F1 on NER; Alon et al. (EMNLP 2025 Findings) show context length alone degrades performance by 13.9–85%; ExtractBench (Feb 2026) demonstrates 0% valid output on 369-field schemas; ScrapeGraphAI-100k (Feb 2026) identifies empirical breakpoints at schema depth >7 and key count >200; context rot research (Chroma 2025) shows semantically similar distractors cause worst degradation across all 18 frontier models. Training-free LLM IE currently lags discriminative models by 20-60 F1 points on complex benchmarks (e.g., ~35 vs. ~71 F1 on ACE05 RE). However, a critical question remains UNRESOLVED: is schema-induced degradation driven primarily by (a) type COUNT (sheer prompt complexity), (b) type CONFUSABILITY (semantic similarity between co-present types causing interference), or (c) their interaction? Prior work in supervised NER has shown entity ambiguity impacts performance — CyberNER (2025) demonstrates ~30% F1 improvement from harmonizing confusable labels, statistical dataset evaluation (Cambridge NLP Journal 2025) shows 6.42 F1 gap between high/low ambiguity datasets. But these findings address dataset construction and supervised learning, not the distinct setting of training-free LLM IE under complex prompting with constrained decoding. Without controlled evidence distinguishing count from confusability effects, all existing decomposition approaches — per-type splitting (UniNER), similarity-based partitioning (LLM-PEE), fixed k-step pipelines (ProUIE, KGGen) — lack empirical grounding for their decomposition criteria. The core unsolved problem is twofold: (1) establishing whether type confusability independently predicts extraction degradation in LLM-based IE (beyond count effects), and (2) if so, deriving a principled, confusability-minimizing decomposition that operationalizes this finding.

## Opportunity / Why Now

Six decomposition strategies exist, each with clear limitations and none providing empirically validated decomposition criteria:

(1) **Per-type independent splitting** (UniNER, ICLR 2024): +3.3 F1 from individual querying, but treats types independently — no cross-type conditioning, no formal criterion for when splitting helps vs. wastes latency.

(2) **Similarity-based type partitioning** (LLM-PEE, EMNLP 2025): ColBERT retrieval + confidence-based partitioning for massive event type inventories. Uses retrieval similarity as an implicit proxy for confusability but does not validate whether similarity actually predicts extraction interference.

(3) **Fixed k-step pipelines** (KGGen NeurIPS 2025; ProUIE Apr 2026): coarse task-level decomposition (NER→RE→EE) with fixed granularity regardless of schema structure. Pass all upstream results without type-aware filtering.

(4) **Schema as parameterized tools** (SPT, arXiv 2506.01276, June 2025): treats schemas as parameterized tools for LLM tool-calling, addressing schema SELECTION (choosing which schema to apply from a pool). Requires training (schema embedding). Addresses a different granularity: SPT selects among complete schemas, while SDGD decomposes WITHIN a single complex schema to minimize intra-batch interference.

(5) **Text-centric anchor grounding** (AEVS, March 2026): discovers text-grounded anchors for KG triplet extraction. Bottom-up (what does the text contain?) rather than top-down (what does the schema permit?). Limited to flat KG triplets.

(6) **Schema-guided multi-agent systems** (OneKE, WWW 2025; CROSSAGENTIE, ACL 2025 Findings; CMAS, WWW 2025): fixed agent architectures or debate-based consensus. No dependency-driven decomposition, no confusability analysis.

(7) **Schema optimization** (PARSE, EMNLP 2025 Industry): optimizes schema representation (descriptions, field names) for LLM consumption via ARCHITECT, achieving up to 64.7% improvement on SWDE. Complementary to SDGD — PARSE optimizes HOW schemas are expressed; SDGD optimizes WHICH types are presented together.

Additionally, DLISC (arXiv May 2025) uses LoRA-based schema identification to reduce per-step schema complexity on-device — trained approach with similar motivation but gradient-based.

Critically, ACONIC (arXiv Oct 2025) demonstrates that formalizing task decomposition via constraint-satisfaction complexity (treewidth) yields 3.6-7.5pp gains over heuristic decomposition on Spider. This proves the value of principled decomposition criteria but does not address IE-specific schema structure.

The key gap is EMPIRICAL: no controlled study has established whether type confusability (not just count) independently drives extraction degradation in training-free LLM IE. Without this evidence, all existing decomposition approaches operate on unvalidated assumptions about what makes schemas 'complex' for LLMs. A formal **confusability measure** that (a) is empirically validated as predictive of extraction quality degradation, (b) enables principled batch composition via graph partitioning, (c) can be estimated both from embeddings (zero-shot) and from empirical confusion matrices (few-shot calibrated), and (d) integrates with schema dependency structure for selective cross-layer grounding — would transform schema decomposition from ad-hoc heuristics to evidence-based methodology.

## Landscape (SOTA & Limitations)

**Decomposition approaches.** UniNER (ICLR 2024) established per-type querying improves NER by 3.3 F1 over batch querying. LLM-PEE (EMNLP 2025 Main) addresses massive-type event extraction (3,465 types) via ColBERT retrieval + confidence-based partitioning (60.2% TC F1 on EEMT). ProUIE (Apr 2026) achieves best fine-tuned UIE via progressive NER→RE→EE training (avg NER F1 79.44, SciERC RE F1 46.76). KGGen (NeurIPS 2025) decomposes KG extraction into entity→relation with clustering-based entity resolution.

**Schema as tools.** SPT (arXiv 2506.01276, June 2025) treats predefined IE schemas as parameterized tools, using LLM tool-calling for schema retrieval + schema filling. Addresses schema SELECTION from a predefined pool (which schema to apply), achieving comparable performance to LoRA baselines with fewer trainable parameters. Complementary to SDGD: SPT selects among complete schemas; SDGD decomposes within a single complex schema. SPT requires training; SDGD is training-free.

**Schema optimization.** PARSE (EMNLP 2025 Industry, arXiv 2510.08623) introduces ARCHITECT to autonomously optimize JSON schemas for LLM consumption, achieving up to 64.7% accuracy improvement on SWDE and 92% error reduction on retry. Addresses schema representation quality rather than schema delivery strategy. Complementary to SDGD: PARSE-optimized schemas could serve as input to SDGD's confusability-aware decomposition.

**Schema complexity empirics.** ScrapeGraphAI-100k (arXiv 2602.15189, Feb 2026) provides 93,695 real-world LLM extraction events and identifies empirical breakpoints: extraction quality degrades sharply at schema depth >7 or key count >200. Stratified evaluation enables identification of specific complexity thresholds where systems fail. However, this measures structural complexity (depth, key count, cyclomatic complexity) without isolating semantic confusability between types.

**Grounding approaches.** AEVS (MDPI Computers, March 2026) discovers text-grounded anchors for KG triplet extraction with near-zero hallucination (0.23-0.44% with Claude 4.5 Haiku, 0.828 Exact F1 on WebNLG). Entity type constraints in trained models — SH-ETRs (Expert Systems 2025, 74.39 F1 on DocRED), ETCGN (IJMLC 2024), Document-level RE with Entity Type Constraints (Neural Networks 2025) — embed type-compatibility filtering in learned parameters.

**Multi-agent and pipeline systems.** OneKE (WWW 2025 Companion) uses Schema Agent + Extraction Agent + Reflection Agent for NER/RE/EE. CROSSAGENTIE (ACL 2025 Findings) assigns type-specific agents with debate-based consensus. CMAS (WWW 2025) uses cooperative multi-agent framework with type-related feature extraction for zero-shot NER.

**Entity ambiguity and type confusion.** CyberNER (arXiv 2510.26499, 2025) demonstrates ~30% F1 improvement from harmonizing 50+ confusable cybersecurity entity labels into 21 coherent types. Statistical dataset evaluation (Cambridge NLP Journal, Jan 2025) quantifies 6.42 F1 gap between high/low entity ambiguity datasets. ESNERA (arXiv 2508.06877, 2025) combines empirical and semantic similarity for NER dataset merging. SAM-NER (arXiv 2605.03706, ACL Findings 2026) introduces semantic archetype mediation for zero-shot NER, addressing type confusion via intermediate archetype space. DEER (EMNLP 2025 Main) uses label-grounded statistics for ICL demonstration selection. APIE (arXiv 2508.10036, 2025) decomposes extraction difficulty into format-level and content-level confusion, achieving 18.3% relative gains. These works establish that type confusability degrades NER/IE in various contexts, but ALL operate in supervised or semi-supervised settings. No controlled study validates that type confusability — specifically co-presence of semantically similar types in the extraction prompt — independently degrades training-free LLM IE beyond what type count alone predicts.

**Schema complexity reduction.** DLISC (arXiv May 2025) uses two LoRA modules (schema identification + extraction) with incremental schema caching for on-device LLMs — trained approach addressing the same motivation but requiring gradient updates.

**Principled task decomposition.** ACONIC (arXiv Oct 2025) formalizes general LLM task decomposition via constraint-satisfaction treewidth, yielding 3.6-7.5pp gains on Spider. Demonstrates principled decomposition > heuristic approaches. SDGD provides the IE-domain-specific analogue.

**Context degradation evidence.** Alon et al. (EMNLP 2025 Findings) demonstrate 13.9-85% degradation from context length alone. Context rot (Chroma 2025) shows semantically similar distractors cause worst degradation. ExtractBench (Feb 2026) shows catastrophic failure at 369 fields. The Format Tax (Apr 2026) shows prompt-level effects account for ~71% of format-induced degradation.

**Deployment context for training-free IE.** mCODEGPT (Nature Communications Medicine, 2025) demonstrates zero-shot IE from clinical notes into structured mCODE format achieving 94-96% accuracy on cancer-specific entities — validating that training-free extraction has practical deployment value in domains where annotation expertise is scarce. FINRA's 2026 regulatory oversight report identifies 'Summarization and Information Extraction' as the top GenAI use case among member firms. Cross-lingual IE (GoLLIE-TF, 2025) shows training-free approaches remain critical for the ~50 languages where annotated IE corpora don't exist.

**Absolute performance context.** Training-free zero-shot LLM methods achieve ~35 F1 on ACE05 RE (vs. ~71 supervised ITER), ~18 F1 on Re-DocRED (vs. ~81 supervised DREEAM), ~14 F1 on ACE05 EE (vs. ~72 supervised). SDGD targets meaningful gains within the training-free regime where absolute performance matters for specific deployment scenarios.

No prior work provides a controlled empirical study isolating type confusability from type count effects in LLM-based IE, nor combines a validated confusability measure with principled batch composition and selective cross-layer grounding for training-free extraction.

## Proposed Approach

We propose a dual-contribution paper: (A) **The Schema Confusability Study** — the first controlled empirical investigation establishing whether type confusability independently predicts extraction degradation in training-free LLM IE (analogous to 'Lost in the Middle' establishing positional degradation); and (B) **Confusability-Aware Schema Decomposition (SDGD)** — a principled framework that operationalizes these findings into a practical extraction pipeline.

## CONTRIBUTION A: Schema Confusability Study (Primary Empirical Contribution)

This study answers the question: *Does type confusability — not just type count — drive extraction degradation in LLM-based IE?* While prior work (CyberNER, Cambridge NLP 2025) shows ambiguity effects in supervised NER, no controlled study validates this in the distinct setting of training-free LLM IE with constrained decoding. The study design isolates confusability from count through controlled experiments:

**Experiment 1 — Count Effect Baseline.** On ACE05 RE (18 relation types, 7 entity types) and Few-NERD (66 entity types): measure F1 with 2, 6, 12, 18 (or 22, 44, 66) types in the prompt, all randomly sampled. Establishes the count-quality curve.

**Experiment 2 — Confusability Effect (Controlled).** Fix type count at 6, but systematically vary composition: (i) 6 maximally dissimilar types (low BCS), (ii) 6 random types (medium BCS, 10 random samples averaged), (iii) 6 maximally similar types (high BCS — e.g., all employment/affiliation relations, or all fine-grained location types). Repeat at count=12. If high-BCS batches show significantly lower F1 than low-BCS batches at the SAME batch size, confusability independently predicts degradation beyond count.

**Experiment 3 — Interaction Effect.** 2×2 design: {low count, high count} × {low confusability, high confusability}. Tests whether confusability effects are additive (constant penalty) or multiplicative (worse at higher counts).

**Experiment 4 — Selective Grounding.** With 18 relation types, compare providing all 7 entity types vs. only type-compatible entities per relation. Tests whether irrelevant upstream entities (semantically similar to valid arguments) independently degrade downstream extraction.

**Deliverables:** (1) Confusability-Quality Curves (main figure) showing F1 as a function of BCS at fixed type counts; (2) Statistical tests (paired t-test, effect size) quantifying the independent confusability effect; (3) The derived confusability threshold θ* at which degradation becomes significant; (4) Interaction analysis revealing whether confusability is additive or multiplicative with count.

**Outcome-Dependent Framing:**
- If |r| ≥ 0.6 (strong correlation): confusability is the dominant factor → SDGD is strongly motivated, paper is primarily a method paper validated by the empirical study
- If 0.3 ≤ |r| < 0.6 (moderate correlation): confusability is a significant but not dominant factor → paper reports that confusability is ONE mechanism among several (count, description quality, argument overlap), SDGD still yields gains on high-confusability subsets, and we provide practical guidance on WHEN confusability-aware decomposition is worthwhile (e.g., 'apply SDGD when >50% of type pairs exceed θ*')
- If |r| < 0.3 (weak/no correlation): confusability does NOT independently predict degradation in LLM IE → NEGATIVE RESULT contribution showing that supervised NER findings (CyberNER, Cambridge 2025) do NOT transfer to training-free LLM IE, and count/context-length is the dominant mechanism. This is itself a valuable finding that redirects future research. SDGD reduces to count-minimizing decomposition (equivalent to UniNER-style per-type splitting).

GPU cost for Contribution A: <3h H100.

## CONTRIBUTION B: Confusability-Aware Schema Decomposition (SDGD)

**Schema Confusability Score (SCS) — Formal Definition.**

Given an IE schema with type set T, define pairwise confusability:

*Zero-shot (embedding-based):* conf_embed(t_i, t_j) = cosine_sim(LLM_embed(desc(t_i)), LLM_embed(desc(t_j))), where desc(t) includes type name, definition, and argument constraints. Embedding model: Qwen 3.6-27B hidden states (fixed).

*Few-shot (empirical):* Given k calibration examples (k ∈ {5, 10}), run extraction with all types simultaneously. Compute confusion matrix C where C[i,j] = frequency of model labeling ground-truth type-i instances as type-j. Then conf_emp(t_i, t_j) = (C[i,j] + C[j,i]) / (count(t_i) + count(t_j)).

For a batch S ⊆ T, the Batch Confusability Score: BCS(S) = max_{i≠j ∈ S} conf(t_i, t_j).

**Phase 1: Schema Confusability Graph (SCG) Construction.**

Build weighted undirected graph G = (T, E, w) where nodes are types and edge weights w(t_i, t_j) = conf(t_i, t_j). Overlay the dependency DAG: entity types are source nodes; relation R(arg1: T1, arg2: T2) depends on T1, T2; event arguments depend on relevant entities/relations.

**Phase 2: Confusability-Minimizing Batch Composition.**

Within each DAG layer, partition types into batches minimizing total BCS subject to θ* (from Contribution A). Formally: find partition P = {S_1, ..., S_k} such that BCS(S_i) ≤ θ* for all i, minimizing k. Equivalent to graph coloring on the θ*-thresholded confusability graph. IE schemas are small graphs (<100 nodes) where greedy methods suffice.

**Phase 3: Topological Execution with Selective Grounding.**

Execute DAG layers in topological order. Layer 1: extract entity types in confusability-minimizing batches. Layer 2: for each relation type R(arg1: T1, arg2: T2), provide ONLY extracted entities of types T1 and T2 — selective grounding removes irrelevant entities. Layer 3: extract events with relevant entity and relation context.

**Phase 4: Cross-Layer Consistency Verification.** Lightweight referential integrity check.

**Two Variants:**
- **SDGD-zero**: Zero-shot. Uses conf_embed. No labeled data.
- **SDGD-cal**: Few-shot calibrated. Uses 5-10 labeled examples (no gradients) for conf_emp and in-context examples. Still training-free.

## PRACTICAL IMPACT: Deployment Scenarios

Training-free IE at ~40-50 F1 is practically useful in specific settings where the ALTERNATIVE is not supervised models but rather NO extraction at all:

(a) **Clinical schema adaptation**: New reporting standards (e.g., mCODE updates, ICD-11 transitions) introduce extraction schemas monthly. mCODEGPT (Nature Comms Medicine 2025) validates zero-shot clinical IE deployment. Annotation by oncologists costs $150-500/hour; even 45 F1 on complex schemas enables initial triage before expert review.

(b) **Regulatory compliance extraction**: FINRA's 2026 report identifies IE as the top GenAI use case among financial firms. Regulatory schemas evolve quarterly (new reporting fields, amended definitions). Training-free extraction enables same-week deployment on updated schemas.

(c) **Multilingual IE**: For ~50 languages lacking annotated IE corpora (GoLLIE-TF, 2025), training-free extraction is the ONLY option. SDGD's schema-level decomposition is language-agnostic — the confusability graph depends on type definitions, not source language.

(d) **Rapid prototyping for annotation**: SDGD-zero provides immediate extraction that bootstraps annotation by pre-filling structured forms for human correction, reducing annotation time by 40-60% (standard pre-annotation speedup in IE literature).

In all cases, SDGD's key advantage is **schema portability** — changing the extraction schema requires NO retraining, only recomputing the confusability graph (seconds) and re-partitioning batches.

## TIMELINE WITH GO/NO-GO DECISION POINT

**Day 1-3: Contribution A (Phase 0).** Run Experiments 1-4. Compute confusability-quality correlation.
- **Day 3 Decision Point:**
  - |r| ≥ 0.3: PROCEED with full SDGD framework (strong or moderate correlation both justify the method, with framing adjusted per outcome)
  - |r| < 0.3: PIVOT to pure empirical study of schema complexity degradation factors (count, depth, description quality, argument overlap) without SDGD framework — itself a contribution as negative result contradicting extrapolation from supervised NER findings

**Day 4-8: SDGD Implementation + Core Experiments.** SCG construction, batch composition, selective grounding. Run SDGD-zero and SDGD-cal on 3 core benchmarks (ACE05, Few-NERD, DocRED).

**Day 9-12: Ablations + Analysis.** Centerpiece ablation suite. Latency measurements. Moderate-correlation analysis if applicable.

**Day 13-15: Writing + Remaining Experiments.** Paper draft. MAVEN and SciERC results for camera-ready if time permits.

**Explicit Success Thresholds:**
- (a) SDGD-cal ≥5 F1 over single-pass on complex schemas (>30 types) — OR ≥3 F1 if moderate correlation
- (b) SDGD-zero ≥3 F1 over single-pass on complex schemas — OR ≥2 F1 if moderate correlation
- (c) SDGD-cal > SDGD-zero by ≥2 F1 (validates empirical confusability over embedding proxy)
- (d) Confusability-quality correlation: Pearson |r| ≥ 0.3 (minimum for proceeding)
- (e) High-BCS batches show statistically significant lower F1 than low-BCS batches at same count (p < 0.05)
- (f) Marginal gains (<2 F1) on simple schemas (SciERC, 13 types) — confirms confusability matters more for complex schemas

**Evaluation.** 5 core benchmarks: ACE05 (joint NER/RE/EE, 58 types — full 3-layer DAG), SciERC (NER/RE, 13 types — simple schema control), MAVEN (168 event types — scaling stress test), DocRED (96 relation types — selective grounding stress test), Few-NERD (66 fine-grained entity types — confusability stress test).

**Baselines (training-free).** (a) Single-pass with full schema + constrained decoding, (b) UniNER-style per-type independent queries, (c) LLM-PEE-style similarity-based partitioning (adapted), (d) ProUIE-style 3-layer NER→RE→EE (all upstream passed), (e) Random batching (same batch count as SDGD, random composition — KEY ABLATION isolating confusability-aware grouping), (f) AEVS-style text-centric grounding (adapted), (g) Count-minimizing decompo

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200-350 (~2000-3500 turns)', 'estimated_gpu_cost': '$425-850 at ~$2.50-5/hr H100', 'gpu_hours': '~170h H100 (Contribution A: 5h + 5 datasets × full ablation suite + calibration count sensitivity at 5/10 examples; embedding model fixed to Qwen 3.6-27B, threshold derived from Contribution A)', 'gpu_utilization': 'Moderate (~45-55%): confusion matrix computation creates sequential dependencies within-dataset; evaluation parallelizes across batches but cross-dataset analysis is sequential', 'risk_note': 'Automated confusion matrix estimation may amplify noise from small calibration sets (5-10 examples). Mitigated by deriving threshold from Contribution A controlled experiments rather than grid search. Day-3 go/no-go automated via correlation threshold check', 'speed_bottleneck': "Confusion matrix computation requires per-example extraction runs; DocRED's 96 relation types require O(96²) pairwise confusability estimation from limited calibration data", 'team': '0 (initial setup ~5h for dataset preparation, schema parsing, embedding computation)', 'timeline': '10-14 days with 2 H100 GPUs (170 GPU-hours total; at ~50% parallel efficiency across 2 GPUs, yielding ~12 productive GPU-hours per GPU per day = 170/(2×12) ≈ 7 days compute + 3-7 days analysis/iteration)'}
- **human_in_loop**: {'claude_api_cost': '$150-250 (~1500-2500 turns)', 'estimated_gpu_cost': '$325-650 at ~$2.50-5/hr H100', 'gpu_hours': '~130h H100 (agent explores confusability threshold sensitivity, calibration example selection, grounding formats)', 'gpu_utilization': 'Moderate (~35-45%): agent queues experiments sequentially due to confusion matrix dependencies; human reviews daily', 'risk_note': 'Confusion matrix estimation from 5-10 examples may be noisy; human judgment needed to evaluate calibration reliability and decide go/no-go at day 3', 'team': '1 researcher, ~1.5h/day reviewing confusability analysis, calibration confusion matrices, and batch composition quality', 'timeline': '3-4 weeks'}
- **manual**: {'estimated_gpu_cost': '$225-450 at ~$2.50-5/hr H100', 'gpu_hours': '~90h H100 (Contribution A: 3h + 5 datasets × 8 baselines/ablations × 2 variants, each 0.5-1.5h on H100-80GB with Qwen 3.6-27B)', 'gpu_utilization': 'Low (~15-20%): GPU idle during SCG construction, confusability analysis, statistical testing', 'team': '1-2 researchers', 'timeline': '5-6 weeks (Contribution A weeks 1-2, SDGD-zero experiments weeks 3-4, SDGD-cal + ablations week 5, analysis and writing week 6)'}

## Key References

- UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition (ICLR 2024, arXiv 2308.03279) — per-type querying > batch querying by 3.3 F1; foundational evidence for type-level decomposition
- Context Length Alone Hurts LLM Performance Despite Perfect Retrieval (Alon et al., EMNLP 2025 Findings, arXiv 2510.05381) — 13.9-85% degradation from context length alone; supports removing irrelevant types from prompts
- ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction (Ferguson et al., arXiv 2602.12247, Feb 2026) — 0% valid output at 369-field schemas; catastrophic scaling failure motivating decomposition
- ScrapeGraphAI-100k: A Large-Scale Dataset for LLM-Based Web Information Extraction (arXiv 2602.15189, Feb 2026) — 93,695 real-world extraction events; identifies breakpoints at schema depth >7, key count >200; measures structural complexity but not semantic confusability
- Schema as Parameterized Tools for Universal Information Extraction (SPT, arXiv 2506.01276, June 2025) — treats schemas as parameterized tools for LLM tool-calling; addresses schema SELECTION from a pool (requires training); SDGD addresses schema DECOMPOSITION within a single complex schema (training-free)
- AEVS: Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking (MDPI Computers, March 2026) — text-centric anchor grounding for KG triplets; SDGD provides complementary schema-centric grounding
- LLM-PEE: Towards Event Extraction with Massive Types (EMNLP 2025 Main, arXiv 2503.02628) — similarity-based type recall + confidence-based partitioning; implicit confusability proxy without empirical validation
- The Format Tax (arXiv 2604.03616, April 2026) — prompt-level effects account for ~71% of format-induced degradation (3.9pp vs 1.6pp decoder-level)
- ACONIC: An Approach for Systematic Decomposition of Complex LLM Tasks (arXiv 2510.07772, Oct 2025) — formalizes task decomposition via constraint-satisfaction treewidth, yielding 3.6-7.5pp gains on Spider; inspiration for principled IE-specific decomposition
- PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025 Industry, arXiv 2510.08623) — ARCHITECT optimizes schema representation (up to 64.7% improvement on SWDE); complementary to SDGD (schema representation vs. schema delivery)
- SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition (arXiv 2605.03706, ACL Findings 2026) — handles entity-level type confusion via intermediate archetype space; complementary to SDGD's schema-level confusability analysis
- CyberNER: A Harmonized STIX Corpus for Cybersecurity Named Entity Recognition (arXiv 2510.26499, 2025) — ~30% F1 improvement from harmonizing 50+ confusable labels into 21 types; demonstrates confusability-quality link in supervised NER
- Statistical Dataset Evaluation: A Case Study on Named Entity Recognition (Natural Language Processing, Cambridge, Jan 2025) — 6.42 F1 gap between high/low entity ambiguity datasets; quantifies ambiguity impact but in supervised setting
- ESNERA: Empirical and Semantic Named Entity Alignment for Named Entity Dataset Merging (arXiv 2508.06877, Aug 2025) — combines empirical + semantic similarity for cross-dataset label alignment; supports dual-estimation in SDGD
- DEER: LLMs are Better Than You Think: Label-Guided In-Context Learning for NER (EMNLP 2025 Main, arXiv 2505.23722) — label-grounded statistics for ICL demonstration selection; supports calibration-based approach in SDGD-cal
- APIE: Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion (arXiv 2508.10036, 2025) — decomposes extraction difficulty into format-level and content-level confusion; 18.3% relative gains
- CMAS: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition (WWW 2025, arXiv 2502.18702) — cooperative multi-agent NER; related zero-shot baseline
- DLISC: Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models (arXiv 2505.14992, May 2025) — trained two-stage schema identification + extraction with LoRA; same motivation but gradient-based
- OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System (WWW 2025 Companion, arXiv 2412.20005) — schema-guided multi-agent system; fixed architecture without confusability-driven decomposition
- Context Rot: How Increasing Input Tokens Impacts LLM Performance (Chroma Research, 2025) — semantically similar distractors cause worst degradation; directly motivates separating confusable types
- Lost in the Middle: How Language Models Use Long Contexts (TACL 2024, arXiv 2307.03172) — established positional degradation in LLMs via controlled experiments; methodological inspiration for Contribution A's controlled confusability study
- mCODEGPT: Zero-shot Information Extraction from Clinical Free Text Data (Nature Communications Medicine, 2025) — validates deployment of zero-shot IE for clinical extraction (94-96% accuracy); concrete use case for training-free IE
- SH-ETRs: Learning Soft-Hard Rules with Entity Type Constraints for Document-Level Relation Extraction (Expert Systems with Applications 2025) — entity type constraints in learned models; SDGD implements analogous constraints as training-free pipeline routing
- ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction (arXiv Apr 2026, 2604.10633) — current best fine-tuned UIE; training-free upper bound reference
- CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction (ACL Findings 2025) — zero-shot multi-agent baseline using debate-based consensus
- KGGen: Extracting Knowledge Graphs from Plain Text with Language Models (NeurIPS 2025, arXiv 2502.09956) — entity→relation 2-step decomposition; SDGD extends to confusability-aware DAG
- DCCD: Draft-Conditioned Constrained Decoding for Structured Generation in LLMs (arXiv 2603.03305, Feb 2026) — decoder-level fix composable with SDGD (deferred to camera-ready)
- How Is LLM Reasoning Distracted by Irrelevant Context? (arXiv 2505.18761, 2025) — power-law degradation with distractor count; supports selective grounding
- ITER: Iterative Refinement for Joint Entity and Relation Extraction (EMNLP 2024 Findings) — supervised ACE05 RE upper bound (~71.4 F1)
- DREEAM: Document-level RE with Evidence-guided Attention Mechanism (EACL 2023) — supervised Re-DocRED upper bound (~81.4 F1)
- XGrammar: Flexible and Efficient Structured Generation Engine for LLMs (arXiv 2411.15100, 2024; XGrammar-2 blog May 2026)
- Label Disentanglement in Partition-based Extreme Multilabel Classification (Amazon Science, NeurIPS 2021) — optimal label partitioning via flexible overlapping clusters; related formalization

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-structured after 8 rounds: explicit success thresholds, outcome-dependent framing for all correlation levels, honest Format Tax characterization, comprehensive related work with clear differentiation from 7+ competing approaches. The centerpiece ablation isolates each component's contribution.", 'score': 4}**/5
  - feasibility: **{'rationale': "Budget (~170h H100) is within the 200h constraint; Qwen3.6-27B is verified available with structured generation support. The 15-day timeline is tight but the day-3 go/no-go mechanism, focused 5-benchmark scope, and Phase 0's lightweight design (<3h GPU) make it achievable. Auto mode GPU utilization estimates now internally consistent.", 'score': 4}**/5
  - impact: **{'rationale': "Phase 0's confusability-quality curves would inform all future schema-guided extraction work regardless of whether SDGD is adopted — establishing empirically-grounded decomposition criteria where currently only heuristics exist. Practical deployment scenarios (clinical schema adaptation, regulatory compliance, multilingual IE where training-free is the ONLY option) are concrete and legitimized by mCODEGPT and FINRA 2026 evidence.", 'score': 4}**/5
  - novelty: **{'rationale': 'The Phase 0 controlled experiment (fixing type count, varying confusability composition) is genuinely novel — confirmed through extensive search that no prior work isolates confusability from count in training-free LLM IE. The SCS formalization with dual embedding/empirical estimation combined with graph partitioning is new, though individual components (per-type splitting, selective grounding) are known.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 25.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 31.0%
**Z 区间**: [26.0%, 37.0%]
**真实提升 (Z-X)**: +6.0 pp
**幻觉幅度 (Y-Z)**: +4.0 pp
**出口一致性**: 高
**出口三次评估**: [30.0, 32.0, 32.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [Motivation 章节 — 新增 ICL-specific mechanism 论证] — 增加 softmax bottleneck / discriminative capacity 理论框架，论证 ICL 下 type confusability 的运作机制与 supervised setting 有结构性差异（attention-based competition vs. parameter adaptation），将工作从"在新 setting 验证旧结论"提升为"研究新机制下的新现象" — 命中 Novelty 和 Technical Soundness

2. [Motivation 章节 — 删除 attention sink / lost-in-the-middle 类比] — 原始 proposal 无此内容，但迭代第 2 轮曾引入 attention sink/lost-in-the-middle 作为 H1 理论支撑，第 3 轮发现其与 confusability 机制存在逻辑断层（位置效应 ≠ 语义歧义），替换为 softmax bottleneck 论证 — 命中 Technical Soundness（防御 reviewer "mechanism mismatch" 攻击）

3. [Contribution A — 新增 "Expected Non-Trivial Findings" 子节] — 原始 proposal 的 Contribution A 仅声称"confusability independently predicts quality loss"，直觉性过强。新增三个具体的非平凡假设：(H1) 非线性阈值效应——性能在临界 confusability 以下 robust、以上急剧退化；(H2, exploratory) 高阶交互效应——pairwise 低混淆的类型组合可能出现涌现式崩溃；(H3, exploratory) 跨 IE 范式差异——事件抽取因 argument structure 更丰富而对 confusability 格外敏感 — 命中 Novelty（从"验证直觉"升级为"发现非平凡结构"）

4. [Contribution A — 新增 Error Taxonomy Analysis] — 原始 proposal 无此设计。对每个 confusability 水平做 fine-grained error 分类：type substitution（正确 span、错误类型）、span boundary error、false negative、hallucinated entity。若高 confusability 主要增加 type substitution，直接为 attention competition 假说提供 mechanistic evidence — 命中 Technical Soundness 和 Significance（"beyond aggregate F1, we explain what goes wrong"）

5. [Contribution A — 新增 SCS Validation Protocol + Divergence Analysis] — 原始 proposal 将 SCS-zero 和 SCS-cal 仅作为两个变体的实现细节。新增：(a) Spearman/Kendall rank correlation 验证 embedding proxy 有效性；(b) 三档处理方案（ρ>0.7 / 0.5-0.7 / <0.5）；(c) divergent case analysis（false-high-SCS 和 false-low-SCS 的 top-5 type pairs + 定性分析），为 Bayesian hybrid 设计提供 empirical justification — 命中 Technical Soundness 和 Novelty（SCS alignment 本身是独立发现）

6. [Contribution A — 多操作化 Confusability 定义] — 原始 proposal 仅用 embedding similarity 定义 confusability。新增三种独立操作化定义：SCS-zero（embedding cosine）、ROUGE-L（定义文本重叠）、人工语义相似度评分。跨定义一致性打破循环依赖、增强因果推断 — 命中 Technical Soundness

7. [Contribution A — 多模型评估] — 原始 propo



## MVP Validation Results

- **Date**: 2026-05-15
- **Hypothesis Supported**: Yes

### Key Metrics

Partial r(F1, BCS)=0.303, p=0.026 | count_12 r(F1, BCS)=0.501, p=0.008 | Pairwise BCS-confusion ρ=0.254, p=4.6e-12 | Confusion rate high/low BCS: 10-28x | Recall vs count: 0.72→0.42 (monotonic decline) | WrongType errors: 0→2434 (linear with count)

### Summary

在 Few-NERD (66 fine-grained entity types, 1000 test samples) 上用 Qwen3-32B-FP8 验证了核心假设：type confusability 独立于 type count 驱动 training-free LLM IE 质量下降。

机制发现：confusability 的降级通道是 type confusion（标错类型），而非 entity omission（遗漏实体）。这比原始假设更精确。

三重证据链：
1. Batch-level F1 vs BCS: count_12 r=0.501 (p=0.008)，偏相关 r=0.303 (p=0.026)
2. Confusion rate: high-BCS extreme batches 的 type confusion rate 是 low-BCS 的 10-28 倍
3. Type-pair level: pairwise BCS-confusion Spearman ρ=0.254 (p=1.1e-6, n=1953 pairs)，top confused pairs 全是同 coarse category 内的 fine-grained subtypes (BCS>0.85)

额外发现：count curve 反转（F1 随 type count 上升），根因是低 count 时模型 over-predict（pred/gold=6.8x at count=1 vs 0.8x at count=64）。Recall 单调下降（0.72→0.42）符合 count degradation 预期。

Narrative: Multi-channel degradation model — count 驱动 recall 下降 + confusability 驱动 type confusion 增加，两者正交。

### Recommendation

GO — 进入 research 阶段。优先执行 Exp 3a（prompt v2 重跑获取干净数据，已审批+GPU 已分配），然后按 Narrative A (multi-channel degradation) 展开完整实验矩阵。目标 EMNLP 2026 ARR May 25。
