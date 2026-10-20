# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/481f3ec1-3c98-476a-9097-7a4273796126.jsonl`
- **Structured JSON:** [`1f0fe5e951cf30552d5c.json`](../../sessions/1f/1f0fe5e951cf30552d5c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T14:25:04.867Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T14:25:04.867Z",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\",\n  \"core_problem\": \"Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, and LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion. The 260k repair tuples in APRIL have never been stratified by mathematical subdomain despite containing implicit domain structure via explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across mathematical subdomains, going beyond observational domain-stratified scores (Shebzukhov, 2026) to classify error categories per subdomain with statistical rigor?\",\n  \"opportunity\": \"Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing; (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\",\n  \"landscape\": \"Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-specific error taxonomy characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).\",\n  \"inspired_by\": \"Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, but none dynamically conditions reranking on per-problem inferred subdomain), #2 (APRIL 260k tuples with explicit module paths never domain-stratified by error type — Shebzukhov (2026) shows domain-stratified aggregate scores but no error type taxonomy exists showing how autoformalization fails differently across domains), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified APRIL error taxonomy as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.\",\n  \"approach\": \"We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL→Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Specific Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, to directly map each repair example to a mathematical subdomain without additional parsing. We cluster these paths into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. We then stratify APRIL's repair tuples by predicted subdomain and construct the first systematic domain-specific error taxonomy for autoformalization — characterizing how error TYPES (not just aggregate accuracy) distribute across subdomains. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL stratification inference + error taxonomy construction: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)\",\n      \"timeline\": \"17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error analysis + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)\",\n      \"estimated_gpu_cost\": \"$500 (H100 at ~$2.50/hr average via RunPod/Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200 H100-hours\",\n      \"timeline\": \"13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern classification, retrieval pipeline code, and ablation analysis)\",\n      \"claude_api_cost\": \"$300 (domain taxonomy extraction from APRIL path fields + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)\",\n      \"estimated_gpu_cost\": \"$500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL stratification + error taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)\",\n      \"timeline\": \"11 weeks\",\n      \"claude_api_cost\": \"$450 (automated Herald path parsing, domain taxonomy iteration, repair pattern mining, hyperparameter selection, result analysis and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500\",\n      \"speed_bottleneck\": \"Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)\",\n    \"AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only 8 weeks from today, STRETCH if Stage 1 error analysis yields strong early results; could submit error taxonomy + domain-conditioned retrieval as core contributions)\",\n    \"NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)\",\n    \"ICML 2026 AI4Math Workshop (Jul 11, 2026 — ShadowBench Track 4 participation as complementary multi-domain evaluation; FormalRx Track 1 participation to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy; challenge deadline Jun 15, 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\",\n    \"Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\",\n    \"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\",\n    \"Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\",\n    \"M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\",\n    \"Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\",\n    \"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\",\n    \"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\",\n    \"ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\",\n    \"FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\"\n  ],\n  \"description\": \"We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first systematic domain-specific error taxonomy characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across mathematical subdomains — going beyond observational domain-stratified scores (Shebzukhov, 2026) to classify error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623). None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-specific error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field) to stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\",\n  \"project_name\": \"domain_adapt_autoformal\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_compute_budget\": \"RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.\",\n    \"round1_issue_2_venue_mismatch\": \"RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.\",\n    \"round1_issue_3_model_choice\": \"RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.\",\n    \"round1_issue_4_FineLeanCorpus\": \"RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.\",\n    \"round1_issue_5_MSC180\": \"RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.\",\n    \"round1_issue_6_circular_reasoning\": \"RESOLVED (Round 1): Error pattern claims reframed as hypotheses.\",\n    \"round1_issue_7_VeriSoftBench\": \"RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.\",\n    \"round1_issue_8_pipeline_complexity\": \"RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.\",\n    \"round1_issue_9_baseline_fear_test\": \"RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.\",\n    \"round2_issue_1_CRAMF_differentiation\": \"RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.\",\n    \"round2_issue_2_SITA\": \"RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.\",\n    \"round2_issue_3_impact_argument\": \"RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.\",\n    \"round2_issue_4_FineLeanCorpus_size\": \"RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.\",\n    \"round2_issue_5_ICLR2027_deadline\": \"MITIGATED (Round 2): Estimated Sep 19/24 with contingency.\",\n    \"round2_issue_6_M2F_RepoProver\": \"RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.\",\n    \"round3_issue_1_DRIFT_Aria\": \"RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.\",\n    \"round3_issue_2_ConNF_claim\": \"RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across ≥5 categories.'\",\n    \"round3_issue_3_error_taxonomy_elevation\": \"RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.\",\n    \"round3_issue_4_compute_trim\": \"RESOLVED: All three modes ≤200 H100-hours.\",\n    \"round3_issue_5_LeanSearch_v2\": \"RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).\",\n    \"round4_issue_1_IndiMathBench\": \"RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).\",\n    \"round4_issue_2_quantitative_hypotheses\": \"RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.\",\n    \"round4_issue_3_model_architecture\": \"RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.\",\n    \"round5_issue_1_IndiMathBench_citation\": \"RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.\",\n    \"round5_issue_2_BEq_correction\": \"RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.\",\n    \"round5_issue_3_ShadowBench\": \"RESOLVED: Added ShadowBench and SCI Error Taxonomy.\",\n    \"round5_issue_4_Mensfelt_framework\": \"RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.\",\n    \"round5_issue_5_landscape_condensation\": \"RESOLVED: Condensed landscape to argument-driven organization.\",\n    \"round6_issue_1_cycle_consistency_paper\": \"RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Narrowed ALL novelty claims from 'first empirical characterization of how autoformalization errors distribute across subdomains' to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across subdomains.' Explicitly differentiated: Shebzukhov reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) via observational analysis; our contribution classifies error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor (JSD, prediction accuracy, actionable recommendations). Noted that Shebzukhov is a Stanford CS224N course project performing observational analysis that concludes 'improvement is general rather than domain-specific.'\",\n    \"round6_issue_2_ShadowBench_SCI_conflation\": \"RESOLVED: Separated Track 1 (FormalRx: semantic alignment evaluation using FormalRx-Test dataset with 28-category SCI Error Taxonomy, Macro F1 metrics) from Track 4 (ShadowBench: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate, NO error taxonomy). Fixed ALL conflated references in core_problem (removed SCI from ShadowBench mention), opportunity (separated into two tracks), landscape (distinguished evaluation goals), approach (correctly attributed SCI to FormalRx Track 1, ShadowBench to Track 4), description (separated references), target_venues (specified both tracks), and key_references (split into two entries). Our error taxonomy complements FormalRx's SCI taxonomy (by error type) with subdomain stratification; our evaluation protocol complements ShadowBench's fixed-split multi-domain evaluation with leave-one-domain-out rotation.\",\n    \"round6_issue_3_Herald_data_engineering\": \"RESOLVED: Acknowledged that Herald's HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with NO explicit module_path column. Module paths must be parsed from qualified theorem names in formal statements (e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl') or recovered via re-running the Lean-Jixia pipeline. Identified APRIL's explicit 'path' field (confirmed from HuggingFace schema: path: string) as the more immediately usable source for domain labeling. Restructured approach to use APRIL paths as primary domain signal, with Herald parsed paths as supplementary. Added ~1 week to manual timeline for Herald path parsing engineering. Updated resource estimates accordingly.\"\n  }\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"MINOR: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477) not cited — the first end-to-end domain-general hammer for Lean with dynamic user-context adaptation and strong out-of-distribution generalization (79.4% relative to upper bound on miniCTX-v2). While targeting premise selection for proving (not autoformalization retrieval) and not conditioning on mathematical subdomain per se, it demonstrates a relevant domain-generalization approach in the Lean ecosystem that should be acknowledged in the landscape.\", \"MINOR: AAAI 2027 (July 28, 2026) is listed as a target venue but is mathematically infeasible — 8 weeks from today vs. minimum 11-week auto_research timeline. Should be downgraded from 'STRETCH' to explicitly infeasible, or the timeline should explain what partial submission (e.g., error taxonomy only) could be ready in 8 weeks.\", \"MINOR: ICML 2026 AI4Math Workshop paper submission deadline was May 25, 2026 (already passed 3 days ago). The target_venues entry correctly identifies challenge track participation (June 15 deadline) but should note that paper submission is no longer possible.\", \"MINOR: The APRIL dataset's HuggingFace schema includes an 'error_type' field already classifying errors into categories (theorem substitution, tactic errors, multi-line errors, line mutations). The proposal's 'domain-specific error taxonomy' contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types — this should be stated explicitly to avoid overclaiming. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in constructing a new error classification.\", \"MINOR: KELPS (arXiv 2507.08665) achieves 88.9% syntactic accuracy on MiniF2F via Knowledge Equations and multi-language autoformalization — a strong baseline not currently cited that outperforms several referenced systems.\"]\nFeedback: The proposal has matured substantially across 6 revision rounds and all critical/moderate issues are resolved. Remaining issues are all minor. To clear the 4.0 threshold: (1) **Acknowledge APRIL's existing error_type field** and precisely describe the taxonomy contribution as domain-stratified cross-tabulation with statistical rigor (JSD, prediction), not a new error classification — this prevents overclaiming while preserving the genuine novelty of domain stratification. (2) **Fix venue timeline accuracy**: mark AAAI 2027 as infeasible (not 'stretch'), note ICML 2026 paper deadline has passed, and specify what partial submission could target AAAI 2027 if desired (e.g., error taxonomy + initial retrieval results without full ablations). (3) **Add LeanPremise/LeanHammer** to landscape as a strong domain-general retrieval baseline in the Lean ecosystem, differentiating by target task (premise selection for proving vs. retrieval for autoformalization). (4) **Consider adding KELPS** as a strong MiniF2F baseline. These four fixes are all straightforward and should be completable in one revision round.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 7 轮修订，近 3 轮平均分从 3.8 到 3.8，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T14:25:04.870Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T14:25:04.870Z",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

## Round 1

64 recorded events

### User

_source line 3 · 2026-05-28T14:25:04.882Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy",
  "core_problem": "Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, and LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion. The 260k repair tuples in APRIL have never been stratified by mathematical subdomain despite containing implicit domain structure via explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across mathematical subdomains, going beyond observational domain-stratified scores (Shebzukhov, 2026) to classify error categories per subdomain with statistical rigor?",
  "opportunity": "Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing; (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.",
  "landscape": "Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-specific error taxonomy characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).",
  "inspired_by": "Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, but none dynamically conditions reranking on per-problem inferred subdomain), #2 (APRIL 260k tuples with explicit module paths never domain-stratified by error type — Shebzukhov (2026) shows domain-stratified aggregate scores but no error type taxonomy exists showing how autoformalization fails differently across domains), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified APRIL error taxonomy as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.",
  "approach": "We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL→Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Specific Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, to directly map each repair example to a mathematical subdomain without additional parsing. We cluster these paths into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. We then stratify APRIL's repair tuples by predicted subdomain and construct the first systematic domain-specific error taxonomy for autoformalization — characterizing how error TYPES (not just aggregate accuracy) distribute across subdomains. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL stratification inference + error taxonomy construction: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)",
      "timeline": "17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error analysis + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)",
      "estimated_gpu_cost": "$500 (H100 at ~$2.50/hr average via RunPod/Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~200 H100-hours",
      "timeline": "13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern classification, retrieval pipeline code, and ablation analysis)",
      "claude_api_cost": "$300 (domain taxonomy extraction from APRIL path fields + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)",
      "estimated_gpu_cost": "$500"
    },
    "auto_research": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL stratification + error taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)",
      "timeline": "11 weeks",
      "claude_api_cost": "$450 (automated Herald path parsing, domain taxonomy iteration, repair pattern mining, hyperparameter selection, result analysis and paper drafting)",
      "estimated_gpu_cost": "$500",
      "speed_bottleneck": "Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)",
    "AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only 8 weeks from today, STRETCH if Stage 1 error analysis yields strong early results; could submit error taxonomy + domain-conditioned retrieval as core contributions)",
    "NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)",
    "ICML 2026 AI4Math Workshop (Jul 11, 2026 — ShadowBench Track 4 participation as complementary multi-domain evaluation; FormalRx Track 1 participation to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy; challenge deadline Jun 15, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)",
    "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)",
    "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)",
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)",
    "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)",
    "Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)",
    "SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)",
    "Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)",
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)",
    "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)",
    "Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)",
    "M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)",
    "Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)",
    "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)",
    "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)",
    "ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)",
    "FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)"
  ],
  "description": "We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first systematic domain-specific error taxonomy characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across mathematical subdomains — going beyond observational domain-stratified scores (Shebzukhov, 2026) to classify error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623). None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-specific error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field) to stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.",
  "project_name": "domain_adapt_autoformal",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_compute_budget": "RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.",
    "round1_issue_2_venue_mismatch": "RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.",
    "round1_issue_3_model_choice": "RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.",
    "round1_issue_4_FineLeanCorpus": "RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.",
    "round1_issue_5_MSC180": "RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.",
    "round1_issue_6_circular_reasoning": "RESOLVED (Round 1): Error pattern claims reframed as hypotheses.",
    "round1_issue_7_VeriSoftBench": "RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.",
    "round1_issue_8_pipeline_complexity": "RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.",
    "round1_issue_9_baseline_fear_test": "RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.",
    "round2_issue_1_CRAMF_differentiation": "RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.",
    "round2_issue_2_SITA": "RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.",
    "round2_issue_3_impact_argument": "RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.",
    "round2_issue_4_FineLeanCorpus_size": "RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.",
    "round2_issue_5_ICLR2027_deadline": "MITIGATED (Round 2): Estimated Sep 19/24 with contingency.",
    "round2_issue_6_M2F_RepoProver": "RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.",
    "round3_issue_1_DRIFT_Aria": "RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.",
    "round3_issue_2_ConNF_claim": "RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across ≥5 categories.'",
    "round3_issue_3_error_taxonomy_elevation": "RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.",
    "round3_issue_4_compute_trim": "RESOLVED: All three modes ≤200 H100-hours.",
    "round3_issue_5_LeanSearch_v2": "RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).",
    "round4_issue_1_IndiMathBench": "RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).",
    "round4_issue_2_quantitative_hypotheses": "RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.",
    "round4_issue_3_model_architecture": "RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.",
    "round5_issue_1_IndiMathBench_citation": "RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.",
    "round5_issue_2_BEq_correction": "RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.",
    "round5_issue_3_ShadowBench": "RESOLVED: Added ShadowBench and SCI Error Taxonomy.",
    "round5_issue_4_Mensfelt_framework": "RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.",
    "round5_issue_5_landscape_condensation": "RESOLVED: Condensed landscape to argument-driven organization.",
    "round6_issue_1_cycle_consistency_paper": "RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Narrowed ALL novelty claims from 'first empirical characterization of how autoformalization errors distribute across subdomains' to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across subdomains.' Explicitly differentiated: Shebzukhov reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) via observational analysis; our contribution classifies error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor (JSD, prediction accuracy, actionable recommendations). Noted that Shebzukhov is a Stanford CS224N course project performing observational analysis that concludes 'improvement is general rather than domain-specific.'",
    "round6_issue_2_ShadowBench_SCI_conflation": "RESOLVED: Separated Track 1 (FormalRx: semantic alignment evaluation using FormalRx-Test dataset with 28-category SCI Error Taxonomy, Macro F1 metrics) from Track 4 (ShadowBench: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate, NO error taxonomy). Fixed ALL conflated references in core_problem (removed SCI from ShadowBench mention), opportunity (separated into two tracks), landscape (distinguished evaluation goals), approach (correctly attributed SCI to FormalRx Track 1, ShadowBench to Track 4), description (separated references), target_venues (specified both tracks), and key_references (split into two entries). Our error taxonomy complements FormalRx's SCI taxonomy (by error type) with subdomain stratification; our evaluation protocol complements ShadowBench's fixed-split multi-domain evaluation with leave-one-domain-out rotation.",
    "round6_issue_3_Herald_data_engineering": "RESOLVED: Acknowledged that Herald's HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with NO explicit module_path column. Module paths must be parsed from qualified theorem names in formal statements (e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl') or recovered via re-running the Lean-Jixia pipeline. Identified APRIL's explicit 'path' field (confirmed from HuggingFace schema: path: string) as the more immediately usable source for domain labeling. Restructured approach to use APRIL paths as primary domain signal, with Herald parsed paths as supplementary. Added ~1 week to manual timeline for Herald path parsing engineering. Updated resource estimates accordingly."
  }
}

## Reviewer feedback (round 7)
Issues: ["MINOR: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477) not cited — the first end-to-end domain-general hammer for Lean with dynamic user-context adaptation and strong out-of-distribution generalization (79.4% relative to upper bound on miniCTX-v2). While targeting premise selection for proving (not autoformalization retrieval) and not conditioning on mathematical subdomain per se, it demonstrates a relevant domain-generalization approach in the Lean ecosystem that should be acknowledged in the landscape.", "MINOR: AAAI 2027 (July 28, 2026) is listed as a target venue but is mathematically infeasible — 8 weeks from today vs. minimum 11-week auto_research timeline. Should be downgraded from 'STRETCH' to explicitly infeasible, or the timeline should explain what partial submission (e.g., error taxonomy only) could be ready in 8 weeks.", "MINOR: ICML 2026 AI4Math Workshop paper submission deadline was May 25, 2026 (already passed 3 days ago). The target_venues entry correctly identifies challenge track participation (June 15 deadline) but should note that paper submission is no longer possible.", "MINOR: The APRIL dataset's HuggingFace schema includes an 'error_type' field already classifying errors into categories (theorem substitution, tactic errors, multi-line errors, line mutations). The proposal's 'domain-specific error taxonomy' contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types — this should be stated explicitly to avoid overclaiming. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in constructing a new error classification.", "MINOR: KELPS (arXiv 2507.08665) achieves 88.9% syntactic accuracy on MiniF2F via Knowledge Equations and multi-language autoformalization — a strong baseline not currently cited that outperforms several referenced systems."]
Feedback: The proposal has matured substantially across 6 revision rounds and all critical/moderate issues are resolved. Remaining issues are all minor. To clear the 4.0 threshold: (1) **Acknowledge APRIL's existing error_type field** and precisely describe the taxonomy contribution as domain-stratified cross-tabulation with statistical rigor (JSD, prediction), not a new error classification — this prevents overclaiming while preserving the genuine novelty of domain stratification. (2) **Fix venue timeline accuracy**: mark AAAI 2027 as infeasible (not 'stretch'), note ICML 2026 paper deadline has passed, and specify what partial submission could target AAAI 2027 if desired (e.g., error taxonomy + initial retrieval results without full ablations). (3) **Add LeanPremise/LeanHammer** to landscape as a strong domain-general retrieval baseline in the Lean ecosystem, differentiating by target task (premise selection for proving vs. retrieval for autoformalization). (4) **Consider adding KELPS** as a strong MiniF2F baseline. These four fixes are all straightforward and should be completable in one revision round.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 7 轮修订，近 3 轮平均分从 3.8 到 3.8，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "cea0e30e-ada0-498a-8785-776b31c6d247",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T14:25:04.880Z_

```json
{
  "parentUuid": "cea0e30e-ada0-498a-8785-776b31c6d247",
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
  "uuid": "401c9e8b-ddd1-426e-b0ed-74479bf6588e",
  "timestamp": "2026-05-28T14:25:04.880Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T14:25:04.880Z_

```json
{
  "parentUuid": "401c9e8b-ddd1-426e-b0ed-74479bf6588e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e0a3f4b0-2cef-461b-bc7e-31aa0740a204",
  "timestamp": "2026-05-28T14:25:04.880Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "e0a3f4b0-2cef-461b-bc7e-31aa0740a204",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Assistant

_source line 8 · 2026-05-28T14:25:17.254Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. All 5 issues are MINOR, and the reviewer explicitly says the proposal has "matured substantially across 6 revision rounds and all critical/moderate issues are resolved." The feedback is clear: fix these 4-5 straightforward issues to clear the 4.0 threshold.

Let me research each issue:

1. **LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477)** - Need to find and understand this paper
2. **AAAI 2027 timeline infeasibility** - Straightforward fix


3. **ICML 2026 AI4Math Workshop deadline passed** - Straightforward fix
4. **APRIL's existing error_type field** - Need to verify the HuggingFace schema
5. **KELPS (arXiv 2507.08665)** - Need to find and understand this paper

The reviewer says these are all straightforward and completable in one revision round, but the stagnation warning makes me wonder if minor fixes alone will push the score above 4.0 or if something more fundamental needs addressing. Still, given the explicit guidance to clear the 4.0 threshold with these specific fixes, I think that's the path forward.

Let me start researching the papers and checking the APRIL schema to make sure I understand what needs to be done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0a3f4b0-2cef-461b-bc7e-31aa0740a204",
  "isSidechain": false,
  "requestId": "req_011CbV7vtnFC1BCVivpU8SfU",
  "type": "assistant",
  "uuid": "416da19a-bea8-4c05-a195-d99b8be2360e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gMSmaP4mp55GfZC9aKy52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13022,
      "cache_read_input_tokens": 11014,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13022,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 463,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13022
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

_source line 9 · 2026-05-28T14:25:17.262Z_

I'll research each issue the reviewer raised in parallel before making revisions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "416da19a-bea8-4c05-a195-d99b8be2360e",
  "isSidechain": false,
  "requestId": "req_011CbV7vtnFC1BCVivpU8SfU",
  "type": "assistant",
  "uuid": "a08679c8-597b-473c-a26e-2650418ce25b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gMSmaP4mp55GfZC9aKy52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13022,
      "cache_read_input_tokens": 11014,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13022,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 463,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13022
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

_source line 10 · 2026-05-28T14:25:17.564Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012G8JwkF7w5yaiJPfRKXbNz`</summary>

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
  "parentUuid": "a08679c8-597b-473c-a26e-2650418ce25b",
  "isSidechain": false,
  "requestId": "req_011CbV7vtnFC1BCVivpU8SfU",
  "type": "assistant",
  "uuid": "9cf22e6e-b71e-4cc3-b987-61d3644fa775",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gMSmaP4mp55GfZC9aKy52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13022,
      "cache_read_input_tokens": 11014,
      "output_tokens": 463,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13022,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 463,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13022
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

_source line 11 · 2026-05-28T14:25:17.570Z_

<details><summary>↩ Tool result · `toolu_012G8JwkF7w5yaiJPfRKXbNz`</summary>

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
  "parentUuid": "9cf22e6e-b71e-4cc3-b987-61d3644fa775",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "f911696b-a4d3-4193-bf55-477f2bbd328f",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9cf22e6e-b71e-4cc3-b987-61d3644fa775",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T14:25:20.347Z_

<details><summary>Logged reasoning block</summary>

```text
Let me research all 5 issues in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f911696b-a4d3-4193-bf55-477f2bbd328f",
  "isSidechain": false,
  "requestId": "req_011CbV7wq7kqD9Gq5Etzss3E",
  "type": "assistant",
  "uuid": "f7f57d2c-918e-42cc-8502-8da9bbcb9b8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmU5Gacz1DkDZccP1rPr3U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 24036,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 24036,
          "cache_creation_input_tokens": 1482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1482
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

_source line 13 · 2026-05-28T14:25:20.938Z_

Now let me research all the issues in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7f57d2c-918e-42cc-8502-8da9bbcb9b8a",
  "isSidechain": false,
  "requestId": "req_011CbV7wq7kqD9Gq5Etzss3E",
  "type": "assistant",
  "uuid": "d69bc992-e4ac-42ae-8313-fdcfd05e833c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmU5Gacz1DkDZccP1rPr3U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 24036,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 24036,
          "cache_creation_input_tokens": 1482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1482
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

_source line 14 · 2026-05-28T14:25:22.186Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ENy2T2LHcet4v35GsHVCbM`</summary>

```json
{
  "query": "LeanPremise LeanHammer ICLR 2026 arXiv 2506.07477 premise selection Lean"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69bc992-e4ac-42ae-8313-fdcfd05e833c",
  "isSidechain": false,
  "requestId": "req_011CbV7wq7kqD9Gq5Etzss3E",
  "type": "assistant",
  "uuid": "93756142-73fc-4dc0-a5aa-4d1ab4464be3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmU5Gacz1DkDZccP1rPr3U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 24036,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1482,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 24036,
          "cache_creation_input_tokens": 1482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1482
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

_source line 15 · 2026-05-28T14:25:29.908Z_

<details><summary>↩ Tool result · `toolu_01ENy2T2LHcet4v35GsHVCbM`</summary>

```text
Web search results for query: "LeanPremise LeanHammer ICLR 2026 arXiv 2506.07477 premise selection Lean"

Links: [{"title":"Premise Selection for a Lean Hammer [Quick Review]","url":"https://liner.com/review/premise-selection-for-a-lean-hammer"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf"},{"title":"[2506.07477] Premise Selection for a Lean Hammer","url":"https://arxiv.org/abs/2506.07477"},{"title":"LeanHammer","url":"https://cmu-l3.github.io/lean-hammer/"},{"title":"Premise Selection for a Lean Hammer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250607477Z/abstract"},{"title":"arXiv:2506.07477v1 [cs.LG] 9 Jun 2025 Preprint. Under review.","url":"https://arxiv.org/pdf/2506.07477"},{"title":"1 Introduction","url":"https://arxiv.org/html/2601.22554"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=825&show=500"}]

Based on the search results, here's what I found about this research:

## Overview

This ICLR 2026 paper presents LEANHAMMER, a novel neural premise selection system for Lean, improving theorem proving.

## Key Components

LeanPremise is a novel neural premise selection system, and when combined with existing translation and proof reconstruction components, creates LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant. Unlike existing Lean premise selectors, LeanPremise is specifically trained for use with a hammer in dependent type theory, and it dynamically adapts to user-specific contexts, enabling it to effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally.

## What is a Hammer?

A hammer is a tool that integrates premise selection, translation to external automatic theorem provers, and proof reconstruction into one overarching tool to automate tedious reasoning steps.

## Results

LeanPremise enables LeanHammer to solve 21% more goals than existing premise selectors and generalizes well to diverse domains.

## Implementation

LeanHammer is callable as a tactic in Lean, and the premise selector runs on an external server with low computational cost and latency.

The paper was published with arXiv identifier 2506.07477, and the code is available at the GitHub repositories mentioned in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93756142-73fc-4dc0-a5aa-4d1ab4464be3",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "69231f0b-a350-4f24-add7-eaa312527ed5",
  "toolUseResult": {
    "query": "LeanPremise LeanHammer ICLR 2026 arXiv 2506.07477 premise selection Lean",
    "results": [
      {
        "tool_use_id": "srvtoolu_014CtwrNJT9HvCUBQe8NHgRC",
        "content": [
          {
            "title": "Premise Selection for a Lean Hammer [Quick Review]",
            "url": "https://liner.com/review/premise-selection-for-a-lean-hammer"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf"
          },
          {
            "title": "[2506.07477] Premise Selection for a Lean Hammer",
            "url": "https://arxiv.org/abs/2506.07477"
          },
          {
            "title": "LeanHammer",
            "url": "https://cmu-l3.github.io/lean-hammer/"
          },
          {
            "title": "Premise Selection for a Lean Hammer - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250607477Z/abstract"
          },
          {
            "title": "arXiv:2506.07477v1 [cs.LG] 9 Jun 2025 Preprint. Under review.",
            "url": "https://arxiv.org/pdf/2506.07477"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2601.22554"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-06?skip=825&show=500"
          }
        ]
      },
      "Based on the search results, here's what I found about this research:\n\n## Overview\n\nThis ICLR 2026 paper presents LEANHAMMER, a novel neural premise selection system for Lean, improving theorem proving.\n\n## Key Components\n\nLeanPremise is a novel neural premise selection system, and when combined with existing translation and proof reconstruction components, creates LeanHammer, the first end-to-end domain general hammer for the Lean proof assistant. Unlike existing Lean premise selectors, LeanPremise is specifically trained for use with a hammer in dependent type theory, and it dynamically adapts to user-specific contexts, enabling it to effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally.\n\n## What is a Hammer?\n\nA hammer is a tool that integrates premise selection, translation to external automatic theorem provers, and proof reconstruction into one overarching tool to automate tedious reasoning steps.\n\n## Results\n\nLeanPremise enables LeanHammer to solve 21% more goals than existing premise selectors and generalizes well to diverse domains.\n\n## Implementation\n\nLeanHammer is callable as a tactic in Lean, and the premise selector runs on an external server with low computational cost and latency.\n\nThe paper was published with arXiv identifier 2506.07477, and the code is available at the GitHub repositories mentioned in the search results."
    ],
    "durationSeconds": 7.716215539999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "93756142-73fc-4dc0-a5aa-4d1ab4464be3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T14:25:33.161Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RDoWfFAHujjsv29PaVfD3E`</summary>

```json
{
  "query": "KELPS arXiv 2507.08665 Knowledge Equations autoformalization MiniF2F"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69231f0b-a350-4f24-add7-eaa312527ed5",
  "isSidechain": false,
  "requestId": "req_011CbV7xjc9bHqwDs8mn2EmD",
  "type": "assistant",
  "uuid": "e9a439fb-2131-46ec-aa5f-7ff7cb47c406",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147bv5QYDVv2bN6geC2jRt4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 25518,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 25518,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 17 · 2026-05-28T14:25:41.112Z_

<details><summary>↩ Tool result · `toolu_01RDoWfFAHujjsv29PaVfD3E`</summary>

```text
Web search results for query: "KELPS arXiv 2507.08665 Knowledge Equations autoformalization MiniF2F"

Links: [{"title":"[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/abs/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/html/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via","url":"https://arxiv.org/pdf/2507.08665"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=3925&show=1000"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"}]

Based on the search results, here's what I found about KELPS (arXiv:2507.08665):

## Overview

KELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). It is a novel neuro-symbolic framework called KELPS (Knowledge-Equation based Logical Processing System) designed to address problems with limited quantity and quality of multilingual parallel corpora.

## Knowledge Equations (KEs)

The framework translates natural language into Knowledge Equations (KEs), a novel language that was designed and is theoretically grounded in assertional logic. Knowledge Equation serves as an intermediate representation which translates natural language into multiple formal languages, aligns more closely with natural language to improve model accuracy, while expert-crafted transformation rules guarantee syntactic correctness.

## Performance on MiniF2F

The framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming state-of-the-art models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.

## Dataset

The work introduces a large-scale parallel dataset comprising over 60,000 NL-FL pairs spanning distinct mathematical subfields, with multi-language support (Lean, Coq, Isabelle).

The paper was accepted by the ICML 2025 AI4MATH Workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9a439fb-2131-46ec-aa5f-7ff7cb47c406",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "2975fa5b-a8e9-4764-a8bd-fb9de5ead00a",
  "toolUseResult": {
    "query": "KELPS arXiv 2507.08665 Knowledge Equations autoformalization MiniF2F",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SHQEo5y43xQtmiiYpSACXy",
        "content": [
          {
            "title": "[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/abs/2507.08665"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/html/2507.08665"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via",
            "url": "https://arxiv.org/pdf/2507.08665"
          },
          {
            "title": "Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs",
            "url": "https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"
          },
          {
            "title": "Computer Science Jul 2025",
            "url": "https://www.arxiv.org/list/cs/2025-07?skip=3925&show=1000"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/html/2510.06857v1"
          }
        ]
      },
      "Based on the search results, here's what I found about KELPS (arXiv:2507.08665):\n\n## Overview\n\nKELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). It is a novel neuro-symbolic framework called KELPS (Knowledge-Equation based Logical Processing System) designed to address problems with limited quantity and quality of multilingual parallel corpora.\n\n## Knowledge Equations (KEs)\n\nThe framework translates natural language into Knowledge Equations (KEs), a novel language that was designed and is theoretically grounded in assertional logic. Knowledge Equation serves as an intermediate representation which translates natural language into multiple formal languages, aligns more closely with natural language to improve model accuracy, while expert-crafted transformation rules guarantee syntactic correctness.\n\n## Performance on MiniF2F\n\nThe framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming state-of-the-art models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.\n\n## Dataset\n\nThe work introduces a large-scale parallel dataset comprising over 60,000 NL-FL pairs spanning distinct mathematical subfields, with multi-language support (Lean, Coq, Isabelle).\n\nThe paper was accepted by the ICML 2025 AI4MATH Workshop."
    ],
    "durationSeconds": 7.946994431999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e9a439fb-2131-46ec-aa5f-7ff7cb47c406",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T14:25:46.130Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018yHPG3DZ1mGGaSrAbX4d3i`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.07477",
  "prompt": "Extract the full abstract, key results (especially miniCTX-v2 numbers, out-of-distribution generalization performance), and any information about domain adaptation or mathematical subdomain handling. What is the 79.4% relative to upper bound claim? How does LeanPremise handle user-specific contexts and out-of-distribution domains?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2975fa5b-a8e9-4764-a8bd-fb9de5ead00a",
  "isSidechain": false,
  "requestId": "req_011CbV7yZVUAcHyA4gG73hQY",
  "type": "assistant",
  "uuid": "3e57634a-48a7-4bda-9341-f9986c15908a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WCxnnF2QjU1sLnKk8ytZo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 26351,
      "output_tokens": 156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 838,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 156,
          "cache_read_input_tokens": 26351,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 838
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

_source line 19 · 2026-05-28T14:25:51.186Z_

<details><summary>↩ Tool result · `toolu_018yHPG3DZ1mGGaSrAbX4d3i`</summary>

```text
# Analysis of "Premise Selection for a Lean Hammer"

## Full Abstract

The paper presents LeanPremise, a neural premise selection system integrated with translation and proof reconstruction to form **LeanHammer**, described as "the first end-to-end domain general hammer for the Lean proof assistant." The system dynamically adapts to user contexts and can recommend premises from libraries outside training data and user-defined lemmas. The research claims LeanPremise enables solving "21% more goals than existing premise selectors" with strong generalization across domains.

## Key Results

The page does not provide specific performance numbers for miniCTX-v2 or detailed domain adaptation metrics. The primary quantitative claim is that **LeanHammer solves 21% more goals** compared to existing premise selectors, demonstrating improved practical verification automation.

## Addressing Your Questions

**On the 79.4% claim:** This specific percentage is not mentioned in the provided content.

**Out-of-Distribution and User Context Handling:** The abstract indicates LeanPremise "dynamically adapts to user-specific contexts," enabling it to "effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally." However, detailed mechanisms or evaluation results for this capability are not included in the webpage excerpt.

**Note:** For comprehensive technical details, metrics, and subdomain-specific performance, consulting the full PDF or HTML versions would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e57634a-48a7-4bda-9341-f9986c15908a",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "6d4588f1-1c62-4948-b39b-227b85224dc3",
  "toolUseResult": {
    "bytes": 47568,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Premise Selection for a Lean Hammer\"\n\n## Full Abstract\n\nThe paper presents LeanPremise, a neural premise selection system integrated with translation and proof reconstruction to form **LeanHammer**, described as \"the first end-to-end domain general hammer for the Lean proof assistant.\" The system dynamically adapts to user contexts and can recommend premises from libraries outside training data and user-defined lemmas. The research claims LeanPremise enables solving \"21% more goals than existing premise selectors\" with strong generalization across domains.\n\n## Key Results\n\nThe page does not provide specific performance numbers for miniCTX-v2 or detailed domain adaptation metrics. The primary quantitative claim is that **LeanHammer solves 21% more goals** compared to existing premise selectors, demonstrating improved practical verification automation.\n\n## Addressing Your Questions\n\n**On the 79.4% claim:** This specific percentage is not mentioned in the provided content.\n\n**Out-of-Distribution and User Context Handling:** The abstract indicates LeanPremise \"dynamically adapts to user-specific contexts,\" enabling it to \"effectively recommend premises from libraries outside LeanPremise's training data as well as lemmas defined by the user locally.\" However, detailed mechanisms or evaluation results for this capability are not included in the webpage excerpt.\n\n**Note:** For comprehensive technical details, metrics, and subdomain-specific performance, consulting the full PDF or HTML versions would be necessary.",
    "durationMs": 5052,
    "url": "https://arxiv.org/abs/2506.07477"
  },
  "sourceToolAssistantUUID": "3e57634a-48a7-4bda-9341-f9986c15908a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T14:26:06.623Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PShYiYTDQAvwsXFDmoJ1CG`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.08665",
  "prompt": "Extract: 1) The full abstract, 2) key performance numbers on MiniF2F (syntactic accuracy, semantic accuracy, pass@1), 3) how Knowledge Equations work as intermediate representation, 4) which mathematical subdomains/categories are covered, 5) how it compares to other autoformalization baselines (Herald, DeepSeek, GPT-4, etc.), 6) whether it does any domain-specific conditioning or treats all domains identically. Also note the venue (workshop paper vs main conference)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d4588f1-1c62-4948-b39b-227b85224dc3",
  "isSidechain": false,
  "requestId": "req_011CbV7zJaK5J1sWP4F9PcHM",
  "type": "assistant",
  "uuid": "56cfa7d9-4bd9-4fd3-8a67-a34432ac12da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HFtEFsoWeMeiRkr9mNJM6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 27673,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 27673,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-28T14:26:15.620Z_

<details><summary>↩ Tool result · `toolu_01PShYiYTDQAvwsXFDmoJ1CG`</summary>

```text
# KELPS: Verified Multi-Language Autoformalization - Summary

## 1. Abstract
"Modern large language models (LLMs) show promising progress in formalizing informal mathematics into machine-verifiable theorems. However, these methods still face bottlenecks due to the limited quantity and quality of multilingual parallel corpora." The authors propose KELPS, a neuro-symbolic framework translating natural language into Knowledge Equations, then to formal languages (Lean, Coq, Isabelle), yielding 60,000+ problems.

## 2. MiniF2F Performance
- **Syntactic Accuracy (pass@1):** 88.9%
- **Semantic Accuracy:** 4.05/5.0 scale
- Outperforms DeepSeek-V3 (81%), Herald (81.3%), and Llama-3 (61.4%)

## 3. Knowledge Equations as Intermediate Representation
Knowledge Equations (KEs) serve as a human-friendly intermediate language grounded in Assertional Logic. They decompose statements into three components: Declarations (variable typing), Facts (assertions about relationships), and Queries (propositions to verify). This enables rule-based translation to multiple formal languages while preserving semantic meaning and reducing the alignment gap between natural and formal languages.

## 4. Mathematical Coverage
The framework covers K-12 and undergraduate mathematics across 6 major topics with:
- 40 core concepts (numbers, polynomials, functions, sets, sequences)
- 180 operators (arithmetic, logical, set operations)
- Domains: real/integer numbers, polynomials, functions, sets, sequences, and special operators

## 5. Baseline Comparisons
| Model | MiniF2F Syntax | Semantic Score |
|-------|---|---|
| KELPS (7B) | **88.9%** | **4.05** |
| DeepSeek-V3 (671B) | 81% | 4.00 |
| Herald (7B) | 81.3% | 3.58 |
| Llama-3 (8B) | 61.4% | 2.63 |

## 6. Domain-Specific Conditioning
The framework treats all mathematical domains using identical procedures: semantic parsing via fine-tuned DeepSeek-Math-7B-Base, syntax validation through ANTLR4 parser and compilers, and semantic validation via LLM-as-Judge. No domain-specific conditioning is mentioned; the approach is generalizable across the ontology's scope.

## Publication Venue
Published at ICML (main conference), not a workshop.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56cfa7d9-4bd9-4fd3-8a67-a34432ac12da",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "a039286f-9797-471f-a86d-0269c181ff63",
  "toolUseResult": {
    "bytes": 518212,
    "code": 200,
    "codeText": "OK",
    "result": "# KELPS: Verified Multi-Language Autoformalization - Summary\n\n## 1. Abstract\n\"Modern large language models (LLMs) show promising progress in formalizing informal mathematics into machine-verifiable theorems. However, these methods still face bottlenecks due to the limited quantity and quality of multilingual parallel corpora.\" The authors propose KELPS, a neuro-symbolic framework translating natural language into Knowledge Equations, then to formal languages (Lean, Coq, Isabelle), yielding 60,000+ problems.\n\n## 2. MiniF2F Performance\n- **Syntactic Accuracy (pass@1):** 88.9%\n- **Semantic Accuracy:** 4.05/5.0 scale\n- Outperforms DeepSeek-V3 (81%), Herald (81.3%), and Llama-3 (61.4%)\n\n## 3. Knowledge Equations as Intermediate Representation\nKnowledge Equations (KEs) serve as a human-friendly intermediate language grounded in Assertional Logic. They decompose statements into three components: Declarations (variable typing), Facts (assertions about relationships), and Queries (propositions to verify). This enables rule-based translation to multiple formal languages while preserving semantic meaning and reducing the alignment gap between natural and formal languages.\n\n## 4. Mathematical Coverage\nThe framework covers K-12 and undergraduate mathematics across 6 major topics with:\n- 40 core concepts (numbers, polynomials, functions, sets, sequences)\n- 180 operators (arithmetic, logical, set operations)\n- Domains: real/integer numbers, polynomials, functions, sets, sequences, and special operators\n\n## 5. Baseline Comparisons\n| Model | MiniF2F Syntax | Semantic Score |\n|-------|---|---|\n| KELPS (7B) | **88.9%** | **4.05** |\n| DeepSeek-V3 (671B) | 81% | 4.00 |\n| Herald (7B) | 81.3% | 3.58 |\n| Llama-3 (8B) | 61.4% | 2.63 |\n\n## 6. Domain-Specific Conditioning\nThe framework treats all mathematical domains using identical procedures: semantic parsing via fine-tuned DeepSeek-Math-7B-Base, syntax validation through ANTLR4 parser and compilers, and semantic validation via LLM-as-Judge. No domain-specific conditioning is mentioned; the approach is generalizable across the ontology's scope.\n\n## Publication Venue\nPublished at ICML (main conference), not a workshop.",
    "durationMs": 8994,
    "url": "https://arxiv.org/html/2507.08665"
  },
  "sourceToolAssistantUUID": "56cfa7d9-4bd9-4fd3-8a67-a34432ac12da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "a039286f-9797-471f-a86d-0269c181ff63",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Tool call

_source line 24 · 2026-05-28T14:26:20.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017DW4tB6qUA4FZHCWbZZdpo`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.07477",
  "prompt": "Extract: 1) miniCTX-v2 performance numbers and what 79.4% relative to upper bound means, 2) how LeanPremise handles out-of-distribution generalization, 3) how it adapts to user-specific contexts dynamically, 4) any discussion of mathematical subdomain or domain-specific behavior, 5) comparison with other premise selection approaches, 6) the key technical innovation (architecture, training). Focus on the results and experimental sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a039286f-9797-471f-a86d-0269c181ff63",
  "isSidechain": false,
  "requestId": "req_011CbV82754ZPfn1hqcLs4rC",
  "type": "assistant",
  "uuid": "55834b3c-d111-4658-b1ff-38e4f7bcc6d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018g3hjQcE9pJ751E4WTLnYQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 27673,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 27673,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 818
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

_source line 25 · 2026-05-28T14:26:30.654Z_

<details><summary>↩ Tool result · `toolu_017DW4tB6qUA4FZHCWbZZdpo`</summary>

```text
# LeanPremise and LeanHammer: Key Findings

## 1. miniCTX-v2 Out-of-Distribution Performance

LeanPremise demonstrates robust generalization to unseen mathematical libraries. On miniCTX-v2-test, the large model achieved 20.7% proof rate, compared to 30.1% on Mathlib-test. The "79.4% relative to upper bound" metric indicates that when ground-truth premises were provided, LeanHammer proved 43.0% of theorems on Mathlib versus 26.1% on miniCTX. The 79.4% figure represents how much of this theoretical maximum LeanHammer actually achieved on out-of-distribution data, suggesting strong cross-domain transferability despite domain shift.

## 2. Dynamic Adaptation to User Contexts

The system dynamically processes locally-defined premises through a client-server architecture. When users invoke premise selection, their proof environment supplies "all currently defined premises," which the server embeds alongside the proof state. Critically, the architecture "caches the embeddings of premises at fixed versions of Mathlib, and only recomputes embeddings of signatures of new premises uploaded by the user," enabling efficient adaptation to novel definitions without retraining.

## 3. Subdomains and Mathematical Behavior

The miniCTX-v2 evaluation includes diverse mathematical domains: Carleson, ConNF, FLT, Foundation, HepLean, and Seymour. Performance varies significantly (0% to 38% proof rates), suggesting domain-specific challenges. The paper notes that some failures stem from "out of scope for Lean-auto's translation procedure," indicating dependent type theory features resist straightforward external solver translation.

## 4. Comparative Advantages Over Alternatives

LeanPremise outperforms three baselines substantially:
- **vs. ReProver**: 150% more theorems proven in full setting (82M vs 218M parameters)
- **vs. MePo**: 73% higher recall@32 (72.7% vs 42.1%)
- **vs. Random Forest**: Achieves 33.3% proof rate versus 19.1%

The performance gap versus ReProver stems from hammer-specific training objectives: extracting premises to finish entire proofs rather than predicting next tactics.

## 5. Core Technical Innovation

LeanPremise employs a modified InfoNCE contrastive loss with masking for shared premises across proofs. The key architectural choice involves a masked contrastive loss that prevents "mislabeling" premises appearing in multiple training examples. The training uses three base encoder models (small/medium/large) without separate reranking, prioritizing recall over precision—critical for hammers tolerating irrelevant premises.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55834b3c-d111-4658-b1ff-38e4f7bcc6d2",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "f7ed9920-12ba-4e36-bc8f-21f527c17379",
  "toolUseResult": {
    "bytes": 383352,
    "code": 200,
    "codeText": "OK",
    "result": "# LeanPremise and LeanHammer: Key Findings\n\n## 1. miniCTX-v2 Out-of-Distribution Performance\n\nLeanPremise demonstrates robust generalization to unseen mathematical libraries. On miniCTX-v2-test, the large model achieved 20.7% proof rate, compared to 30.1% on Mathlib-test. The \"79.4% relative to upper bound\" metric indicates that when ground-truth premises were provided, LeanHammer proved 43.0% of theorems on Mathlib versus 26.1% on miniCTX. The 79.4% figure represents how much of this theoretical maximum LeanHammer actually achieved on out-of-distribution data, suggesting strong cross-domain transferability despite domain shift.\n\n## 2. Dynamic Adaptation to User Contexts\n\nThe system dynamically processes locally-defined premises through a client-server architecture. When users invoke premise selection, their proof environment supplies \"all currently defined premises,\" which the server embeds alongside the proof state. Critically, the architecture \"caches the embeddings of premises at fixed versions of Mathlib, and only recomputes embeddings of signatures of new premises uploaded by the user,\" enabling efficient adaptation to novel definitions without retraining.\n\n## 3. Subdomains and Mathematical Behavior\n\nThe miniCTX-v2 evaluation includes diverse mathematical domains: Carleson, ConNF, FLT, Foundation, HepLean, and Seymour. Performance varies significantly (0% to 38% proof rates), suggesting domain-specific challenges. The paper notes that some failures stem from \"out of scope for Lean-auto's translation procedure,\" indicating dependent type theory features resist straightforward external solver translation.\n\n## 4. Comparative Advantages Over Alternatives\n\nLeanPremise outperforms three baselines substantially:\n- **vs. ReProver**: 150% more theorems proven in full setting (82M vs 218M parameters)\n- **vs. MePo**: 73% higher recall@32 (72.7% vs 42.1%)\n- **vs. Random Forest**: Achieves 33.3% proof rate versus 19.1%\n\nThe performance gap versus ReProver stems from hammer-specific training objectives: extracting premises to finish entire proofs rather than predicting next tactics.\n\n## 5. Core Technical Innovation\n\nLeanPremise employs a modified InfoNCE contrastive loss with masking for shared premises across proofs. The key architectural choice involves a masked contrastive loss that prevents \"mislabeling\" premises appearing in multiple training examples. The training uses three base encoder models (small/medium/large) without separate reranking, prioritizing recall over precision—critical for hammers tolerating irrelevant premises.",
    "durationMs": 10407,
    "url": "https://arxiv.org/html/2506.07477"
  },
  "sourceToolAssistantUUID": "55834b3c-d111-4658-b1ff-38e4f7bcc6d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T14:26:34.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NY1YSsH8AYFKX9jxU287gA`</summary>

```json
{
  "query": "APRIL autoformalization repair dataset HuggingFace schema error_type field path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ed9920-12ba-4e36-bc8f-21f527c17379",
  "isSidechain": false,
  "requestId": "req_011CbV83DaFzouUK5zCTEdTG",
  "type": "assistant",
  "uuid": "019cad7c-410b-4800-850e-b7949dc3d7f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUMSNcWbnHpE9TnZ47v6Sf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 28491,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 28491,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 819
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

_source line 27 · 2026-05-28T14:26:50.007Z_

<details><summary>↩ Tool result · `toolu_01NY1YSsH8AYFKX9jxU287gA`</summary>

```text
Web search results for query: "APRIL autoformalization repair dataset HuggingFace schema error_type field path"

Links: [{"title":"Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/pdf/2602.02990"},{"title":"`Sequence(Features(...))` causes PyArrow cast error in `load_dataset` despite correct schema. · Issue #7590 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/7590"},{"title":"Function load_dataset() misinterprets string field content as part of dataset schema when dealing with `.jsonl` files · Issue #7664 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/7664"},{"title":"Passing schema features to a load_dataset function - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/passing-schema-features-to-a-load-dataset-function/9480"},{"title":"casey-martin/multilingual-mathematical-autoformalization · Datasets at Hugging Face","url":"https://huggingface.co/datasets/casey-martin/multilingual-mathematical-autoformalization"},{"title":"Explicitly defining schema in a dataset? - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/explicitly-defining-schema-in-a-dataset/11298"},{"title":"Attain: Inclusive annotated pavement distress types and severity dataset","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12167439/"},{"title":"Main classes · Hugging Face","url":"https://huggingface.co/docs/datasets/en/package_reference/main_classes"}]

The search results don't contain specific information about an "APRIL autoformalization repair dataset" on HuggingFace with fields like `error_type` and `field_path`. 

The first result discusses "Learning to Repair Lean Proofs from Compiler Feedback," which appears to be related to proof repair with error information, but it doesn't specifically reference an "APRIL" dataset by name or mention the exact fields you're asking about.

To find more specific information about the APRIL dataset and its schema, let me try a more targeted search:

Links: [{"title":"Loading methods · Hugging Face","url":"https://huggingface.co/docs/datasets/en/package_reference/loading_methods"},{"title":"DatasetGenerationError: An error occurred while generating the dataset - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/datasetgenerationerror-an-error-occurred-while-generating-the-dataset/42130"},{"title":"Dataset scripts are no longer supported, but found superb.py · Issue #7693 · huggingface/datasets","url":"https://github.com/huggingface/datasets/issues/7693"},{"title":"Main classes · Hugging Face","url":"https://huggingface.co/docs/datasets/en/package_reference/main_classes"},{"title":"Data Extraction from Free-Text Stroke CT Reports Using GPT-4o and Llama-3.3-70B: The Impact of Annotation Guidelines","url":"https://www.medrxiv.org/content/10.1101/2025.01.22.25320938.full.pdf"},{"title":"Strange Error While Attempting to Load DataSet - 🤗Datasets - Hugging Face Forums","url":"https://discuss.huggingface.co/t/strange-error-while-attempting-to-load-dataset/54531"},{"title":"”My AI is Lying to Me”: User-reported LLM hallucinations in AI mobile apps reviews","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12365265/"},{"title":"devopsmarc/my-issues-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/devopsmarc/my-issues-dataset/viewer/default/train"}]

Let me search more specifically for the APRIL dataset:

Links: [{"title":"Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/pdf/2602.02990"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"Preprint, under review MULTILINGUAL MATHEMATICAL AUTOFORMALIZATION","url":"https://arxiv.org/pdf/2311.03755"},{"title":"RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code","url":"https://arxiv.org/pdf/2509.16701"},{"title":"Benchmark Dataset Generation and Evaluation for Excel Formula Repair with LLMs","url":"https://arxiv.org/pdf/2508.11715"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

The first result appears to be the most relevant. Let me search more specifically for "APRIL" as a dataset acronym:

Links: [{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"APRIL-AIGC/UltraWan · Hugging Face","url":"https://huggingface.co/APRIL-AIGC/UltraWan"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"APRIL-AIGC/UltraVideo · Datasets at Hugging Face","url":"https://huggingface.co/datasets/APRIL-AIGC/UltraVideo"},{"title":"APRIL-AIGC/UltraVideo-Long · Datasets at Hugging Face","url":"https://huggingface.co/datasets/APRIL-AIGC/UltraVideo-Long"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"},{"title":"FormalAlign: Automated Alignment Evaluation for Autoformalization","url":"https://arxiv.org/pdf/2410.10135"}]

Based on my search results, I was unable to find specific information about a dataset called "APRIL autoformalization repair dataset" with fields including `error_type` and `field_path` on HuggingFace.

The search results did return:
- Several papers on autoformalization tasks and datasets (like MMA, ProofNet, FormL4, etc.)
- References to a dataset titled "Learning to Repair Lean Proofs from Compiler Feedback" which involves error information and proof repair
- Information about APRIL-AIGC organization on HuggingFace, but their datasets appear to be related to video generation (UltraVideo), not autoformalization repair

The dataset you're looking for either:
1. May be named differently than "APRIL"
2. May not yet be publicly available on HuggingFace
3. May be a newer dataset that isn't widely indexed yet

If you have additional details about where you encountered this dataset (such as an arXiv paper, GitHub repository, or specific HuggingFace link), I'd be happy to search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "019cad7c-410b-4800-850e-b7949dc3d7f4",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "9d4ba8f7-9c4f-4737-a519-6f82dfd4f683",
  "toolUseResult": {
    "query": "APRIL autoformalization repair dataset HuggingFace schema error_type field path",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ajwmh5CG8DYzYuctmBcmg7",
        "content": [
          {
            "title": "Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/pdf/2602.02990"
          },
          {
            "title": "`Sequence(Features(...))` causes PyArrow cast error in `load_dataset` despite correct schema. · Issue #7590 · huggingface/datasets",
            "url": "https://github.com/huggingface/datasets/issues/7590"
          },
          {
            "title": "Function load_dataset() misinterprets string field content as part of dataset schema when dealing with `.jsonl` files · Issue #7664 · huggingface/datasets",
            "url": "https://github.com/huggingface/datasets/issues/7664"
          },
          {
            "title": "Passing schema features to a load_dataset function - 🤗Datasets - Hugging Face Forums",
            "url": "https://discuss.huggingface.co/t/passing-schema-features-to-a-load-dataset-function/9480"
          },
          {
            "title": "casey-martin/multilingual-mathematical-autoformalization · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/casey-martin/multilingual-mathematical-autoformalization"
          },
          {
            "title": "Explicitly defining schema in a dataset? - 🤗Datasets - Hugging Face Forums",
            "url": "https://discuss.huggingface.co/t/explicitly-defining-schema-in-a-dataset/11298"
          },
          {
            "title": "Attain: Inclusive annotated pavement distress types and severity dataset",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12167439/"
          },
          {
            "title": "Main classes · Hugging Face",
            "url": "https://huggingface.co/docs/datasets/en/package_reference/main_classes"
          }
        ]
      },
      "The search results don't contain specific information about an \"APRIL autoformalization repair dataset\" on HuggingFace with fields like `error_type` and `field_path`. \n\nThe first result discusses \"Learning to Repair Lean Proofs from Compiler Feedback,\" which appears to be related to proof repair with error information, but it doesn't specifically reference an \"APRIL\" dataset by name or mention the exact fields you're asking about.\n\nTo find more specific information about the APRIL dataset and its schema, let me try a more targeted search:",
      {
        "tool_use_id": "srvtoolu_01U7a2oe1eoeuJrubc98JaCG",
        "content": [
          {
            "title": "Loading methods · Hugging Face",
            "url": "https://huggingface.co/docs/datasets/en/package_reference/loading_methods"
          },
          {
            "title": "DatasetGenerationError: An error occurred while generating the dataset - 🤗Datasets - Hugging Face Forums",
            "url": "https://discuss.huggingface.co/t/datasetgenerationerror-an-error-occurred-while-generating-the-dataset/42130"
          },
          {
            "title": "Dataset scripts are no longer supported, but found superb.py · Issue #7693 · huggingface/datasets",
            "url": "https://github.com/huggingface/datasets/issues/7693"
          },
          {
            "title": "Main classes · Hugging Face",
            "url": "https://huggingface.co/docs/datasets/en/package_reference/main_classes"
          },
          {
            "title": "Data Extraction from Free-Text Stroke CT Reports Using GPT-4o and Llama-3.3-70B: The Impact of Annotation Guidelines",
            "url": "https://www.medrxiv.org/content/10.1101/2025.01.22.25320938.full.pdf"
          },
          {
            "title": "Strange Error While Attempting to Load DataSet - 🤗Datasets - Hugging Face Forums",
            "url": "https://discuss.huggingface.co/t/strange-error-while-attempting-to-load-dataset/54531"
          },
          {
            "title": "”My AI is Lying to Me”: User-reported LLM hallucinations in AI mobile apps reviews",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12365265/"
          },
          {
            "title": "devopsmarc/my-issues-dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/devopsmarc/my-issues-dataset/viewer/default/train"
          }
        ]
      },
      "Let me search more specifically for the APRIL dataset:",
      {
        "tool_use_id": "srvtoolu_01AKwWg1Z3E4KtKhPjo6dyxB",
        "content": [
          {
            "title": "Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/pdf/2602.02990"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          },
          {
            "title": "Preprint, under review MULTILINGUAL MATHEMATICAL AUTOFORMALIZATION",
            "url": "https://arxiv.org/pdf/2311.03755"
          },
          {
            "title": "RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code",
            "url": "https://arxiv.org/pdf/2509.16701"
          },
          {
            "title": "Benchmark Dataset Generation and Evaluation for Excel Formula Repair with LLMs",
            "url": "https://arxiv.org/pdf/2508.11715"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "The first result appears to be the most relevant. Let me search more specifically for \"APRIL\" as a dataset acronym:",
      {
        "tool_use_id": "srvtoolu_01Pfy4VEs3BCaxSSfRYw9pR2",
        "content": [
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "APRIL-AIGC/UltraWan · Hugging Face",
            "url": "https://huggingface.co/APRIL-AIGC/UltraWan"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "APRIL-AIGC/UltraVideo · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/APRIL-AIGC/UltraVideo"
          },
          {
            "title": "APRIL-AIGC/UltraVideo-Long · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/APRIL-AIGC/UltraVideo-Long"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2505.23486"
          },
          {
            "title": "FormalAlign: Automated Alignment Evaluation for Autoformalization",
            "url": "https://arxiv.org/pdf/2410.10135"
          }
        ]
      },
      "Based on my search results, I was unable to find specific information about a dataset called \"APRIL autoformalization repair dataset\" with fields including `error_type` and `field_path` on HuggingFace.\n\nThe search results did return:\n- Several papers on autoformalization tasks and datasets (like MMA, ProofNet, FormL4, etc.)\n- References to a dataset titled \"Learning to Repair Lean Proofs from Compiler Feedback\" which involves error information and proof repair\n- Information about APRIL-AIGC organization on HuggingFace, but their datasets appear to be related to video generation (UltraVideo), not autoformalization repair\n\nThe dataset you're looking for either:\n1. May be named differently than \"APRIL\"\n2. May not yet be publicly available on HuggingFace\n3. May be a newer dataset that isn't widely indexed yet\n\nIf you have additional details about where you encountered this dataset (such as an arXiv paper, GitHub repository, or specific HuggingFace link), I'd be happy to search for more specific information."
    ],
    "durationSeconds": 15.829725116999995,
    "searchCount": 4
  },
  "sourceToolAssistantUUID": "019cad7c-410b-4800-850e-b7949dc3d7f4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T14:27:00.801Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BnQhRFQ21yavXidCy2jxmT`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2602.02990",
  "prompt": "This is the APRIL paper (Learning to Repair Lean Proofs from Compiler Feedback). Extract: 1) The exact dataset schema - what fields does each repair tuple contain? Does it have an explicit 'error_type' field that already classifies errors into categories? 2) What error categories are defined (theorem substitution, tactic errors, etc.)? 3) Does it have a 'path' field with Mathlib module paths? 4) Total dataset size (260k tuples?). 5) How errors are generated/categorized - is there a pre-existing error taxonomy or are errors just raw compiler messages?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d4ba8f7-9c4f-4737-a519-6f82dfd4f683",
  "isSidechain": false,
  "requestId": "req_011CbV84eFMbfv3Xzp2fTEdF",
  "type": "assistant",
  "uuid": "58f33019-6f96-4bae-b6a1-5db9279e7704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Mw3hDMoZCfjkH3DKXgXiA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1894,
      "cache_read_input_tokens": 29310,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 29310,
          "cache_creation_input_tokens": 1894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1894
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

_source line 29 · 2026-05-28T14:27:06.448Z_

<details><summary>↩ Tool result · `toolu_01BnQhRFQ21yavXidCy2jxmT`</summary>

```text
# APRIL Dataset Schema Analysis

Based on the PDF content provided, I can extract the following information about the APRIL dataset:

## Dataset Schema & Structure

The document indicates APRIL contains **repair tuples** with the following components:
- **Problem statement**: The incorrect Lean proof
- **Compiler feedback**: Error messages from the Lean type checker
- **Ground truth solution**: The corrected proof

However, the PDF does not explicitly detail a comprehensive field-by-field schema in the extracted sections.

## Error Categories

The paper references error types but doesn't enumerate a complete taxonomy in the visible portions. The content mentions:
- "Theorem substitution" errors
- "Tactic errors"
- General compiler-generated error messages

The errors appear to be **categorized from raw compiler messages** rather than from a pre-defined error taxonomy that's explicitly documented in these excerpts.

## Dataset Size

The document references approximately **260,000 tuples** in the APRIL dataset.

## Path Information

While the paper mentions "Mathlib module paths," the extracted content doesn't provide explicit details about how path fields are structured within individual tuples.

## Key Limitation

The PDF excerpts provided don't contain the detailed dataset documentation section that would specify the exact schema fields. To obtain comprehensive schema details, you would need to consult the paper's appendix or supplementary materials on the dataset specification.

[Binary content (application/pdf, 1.7MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/481f3ec1-3c98-476a-9097-7a4273796126/tool-results/webfetch-1779978420820-nencwb.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f33019-6f96-4bae-b6a1-5db9279e7704",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "849a2df6-73ce-4e18-9ad2-3ff6a0c1e91c",
  "toolUseResult": {
    "bytes": 1757129,
    "code": 200,
    "codeText": "OK",
    "result": "# APRIL Dataset Schema Analysis\n\nBased on the PDF content provided, I can extract the following information about the APRIL dataset:\n\n## Dataset Schema & Structure\n\nThe document indicates APRIL contains **repair tuples** with the following components:\n- **Problem statement**: The incorrect Lean proof\n- **Compiler feedback**: Error messages from the Lean type checker\n- **Ground truth solution**: The corrected proof\n\nHowever, the PDF does not explicitly detail a comprehensive field-by-field schema in the extracted sections.\n\n## Error Categories\n\nThe paper references error types but doesn't enumerate a complete taxonomy in the visible portions. The content mentions:\n- \"Theorem substitution\" errors\n- \"Tactic errors\"\n- General compiler-generated error messages\n\nThe errors appear to be **categorized from raw compiler messages** rather than from a pre-defined error taxonomy that's explicitly documented in these excerpts.\n\n## Dataset Size\n\nThe document references approximately **260,000 tuples** in the APRIL dataset.\n\n## Path Information\n\nWhile the paper mentions \"Mathlib module paths,\" the extracted content doesn't provide explicit details about how path fields are structured within individual tuples.\n\n## Key Limitation\n\nThe PDF excerpts provided don't contain the detailed dataset documentation section that would specify the exact schema fields. To obtain comprehensive schema details, you would need to consult the paper's appendix or supplementary materials on the dataset specification.\n\n[Binary content (application/pdf, 1.7MB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/481f3ec1-3c98-476a-9097-7a4273796126/tool-results/webfetch-1779978420820-nencwb.pdf]",
    "durationMs": 5643,
    "url": "https://arxiv.org/pdf/2602.02990"
  },
  "sourceToolAssistantUUID": "58f33019-6f96-4bae-b6a1-5db9279e7704",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T14:27:06.454Z_

```json
{
  "parentUuid": "849a2df6-73ce-4e18-9ad2-3ff6a0c1e91c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7ab8d55f-ca0f-4310-b670-cff0500479a3",
  "timestamp": "2026-05-28T14:27:06.454Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-28T14:27:09.775Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DSvZeACGJh3SAWhUqzmLy2`</summary>

```json
{
  "query": "APRIL \"Learning to Repair\" Lean proofs dataset schema \"error_type\" \"mutation_type\" HuggingFace 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab8d55f-ca0f-4310-b670-cff0500479a3",
  "isSidechain": false,
  "requestId": "req_011CbV85rNdmKCLfPptoi89u",
  "type": "assistant",
  "uuid": "c17b9938-9f10-4c19-af12-ac2de691d389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6XCk5nDYkLwW3EnQVimkv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 31204,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 31204,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 711
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

_source line 32 · 2026-05-28T14:27:21.500Z_

<details><summary>↩ Tool result · `toolu_01DSvZeACGJh3SAWhUqzmLy2`</summary>

```text
Web search results for query: "APRIL "Learning to Repair" Lean proofs dataset schema "error_type" "mutation_type" HuggingFace 2026"

Links: [{"title":"Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/pdf/2602.02990"},{"title":"Paper page - Learning to Repair Lean Proofs from Compiler Feedback","url":"https://huggingface.co/papers/2602.02990"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Lean+4"},{"title":"lean-error-correction/README.md at main · uw-math-ai/lean-error-correction","url":"https://github.com/uw-math-ai/lean-error-correction/blob/main/README.md"},{"title":"[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/abs/2602.02990"},{"title":"uw-math-ai/gAPRIL-w-exp · Hugging Face","url":"https://huggingface.co/uw-math-ai/gAPRIL-w-exp"}]

Based on the search results, I found information about the APRIL dataset for Learning to Repair Lean Proofs. Here's what I discovered:

APRIL (Automated Proof Repair in Lean) is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.

The APRIL dataset at https://huggingface.co/datasets/uw-math-ai/APRIL contains erroneous Lean proofs, compiler feedback, diagnostic explanations, repair reasoning traces, and corrected proofs.

However, the search results I found do not contain specific information about the dataset schema details you mentioned, such as the specific "error_type" and "mutation_type" fields. While the results confirm the dataset exists on HuggingFace and describe its general contents, the detailed schema documentation with those specific field names is not included in these search results. You may want to check the HuggingFace dataset page directly at https://huggingface.co/datasets/uw-math-ai/APRIL for the complete schema documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c17b9938-9f10-4c19-af12-ac2de691d389",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "00b9d9d0-7f1f-4572-a588-f87fde9f481a",
  "toolUseResult": {
    "query": "APRIL \"Learning to Repair\" Lean proofs dataset schema \"error_type\" \"mutation_type\" HuggingFace 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HD3jivuf3LJmL4n1AHTbS9",
        "content": [
          {
            "title": "Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/pdf/2602.02990"
          },
          {
            "title": "Paper page - Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://huggingface.co/papers/2602.02990"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Lean+4"
          },
          {
            "title": "lean-error-correction/README.md at main · uw-math-ai/lean-error-correction",
            "url": "https://github.com/uw-math-ai/lean-error-correction/blob/main/README.md"
          },
          {
            "title": "[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/abs/2602.02990"
          },
          {
            "title": "uw-math-ai/gAPRIL-w-exp · Hugging Face",
            "url": "https://huggingface.co/uw-math-ai/gAPRIL-w-exp"
          }
        ]
      },
      "Based on the search results, I found information about the APRIL dataset for Learning to Repair Lean Proofs. Here's what I discovered:\n\nAPRIL (Automated Proof Repair in Lean) is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.\n\nThe APRIL dataset at https://huggingface.co/datasets/uw-math-ai/APRIL contains erroneous Lean proofs, compiler feedback, diagnostic explanations, repair reasoning traces, and corrected proofs.\n\nHowever, the search results I found do not contain specific information about the dataset schema details you mentioned, such as the specific \"error_type\" and \"mutation_type\" fields. While the results confirm the dataset exists on HuggingFace and describe its general contents, the detailed schema documentation with those specific field names is not included in these search results. You may want to check the HuggingFace dataset page directly at https://huggingface.co/datasets/uw-math-ai/APRIL for the complete schema documentation."
    ],
    "durationSeconds": 11.718950539999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c17b9938-9f10-4c19-af12-ac2de691d389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "00b9d9d0-7f1f-4572-a588-f87fde9f481a",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Tool call

_source line 35 · 2026-05-28T14:27:26.199Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sa1pCumBa6RKiAMyNDk6Qx`</summary>

```json
{
  "url": "https://huggingface.co/datasets/uw-math-ai/APRIL",
  "prompt": "Extract the complete dataset schema/fields. What columns/fields does each entry have? Specifically, is there an 'error_type' or 'mutation_type' field that already classifies errors into categories? Is there a 'path' field? List ALL fields/columns. Also extract the dataset card description explaining how errors are generated and categorized."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b9d9d0-7f1f-4572-a588-f87fde9f481a",
  "isSidechain": false,
  "requestId": "req_011CbV86xjebLHmnBtG3jUvv",
  "type": "assistant",
  "uuid": "0c690a2f-1a2c-45b3-a0d6-d4c92bb37990",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qxh2dBp34YJ6CYngm32tNx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 31915,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 666,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 31915,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 666
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

_source line 36 · 2026-05-28T14:27:41.124Z_

<details><summary>↩ Tool result · `toolu_01Sa1pCumBa6RKiAMyNDk6Qx`</summary>

````text
# APRIL Dataset Analysis

## Overview
The APRIL dataset from the University of Washington Math AI Lab is a collection of **Lean 4 theorem proving errors** designed for formal verification and theorem-proving research. However, the dataset viewer is currently broken due to schema inconsistencies.

## Dataset Schema/Fields

Based on the error message and preview data shown, the dataset contains the following fields:

### Core Fields Present in All Files:
1. **path** (string) - File path to the Lean source code
2. **correct_proof** (string) - The correct proof
3. **incorrect_proof** (string) - The incorrect/buggy proof
4. **error** (string) - Error message produced
5. **line_at_error** (string) - Line where error occurred
6. **state_at_error** (string) - Proof state at error
7. **explanation** (string) - Explanation of why the proof fails
8. **fix_suggestion** (string) - Suggested fix
9. **source** (string) - Source of the error
10. **error_type** (string) - Classification of error type
11. **split** (string) - train/validation/test split
12. **line** (int64) - Line number
13. **col** (int64) - Column number
14. **src_hash** (string) - Source file hash

### Fields Present in Some Files (Optional/Null):
15. **theorem** (null)
16. **correct_name** (null)
17. **incorrect_name** (null)
18. **correct_formal** (null)
19. **incorrect_formal** (null)
20. **correct_informal** (null)
21. **incorrect_informal** (null)

### Fields Causing Schema Issues (Present in MLME subset only):
22. **metadata** (null) - Additional metadata
23. **annotation_status** (null) - Annotation status
24. **state_before** (null) - Proof state before error
25. **state_after** (null) - Proof state after error

## Schema Problem

The dataset has **inconsistent schemas** across multiple JSONL files:
- `lme_train.jsonl` (Lean Module Errors)
- `mlme_train.jsonl` (Multiple Line Module Errors) - **Contains 4 additional columns**
- `thme_train.jsonl` (Tactic/Higher Module Errors)
- `tme_train.jsonl` (Tactic Module Errors)

The `mlme_train.jsonl` file introduces `state_after`, `state_before`, `annotation_status`, and `metadata` fields that don't exist in other files, causing the `DatasetGenerationCastError`.

## Error Classification

The **error_type** field categorizes errors. From the examples shown, error types include:

- `tactic 'rewrite' failed` - Rewrite tactic pattern matching failures
- `tactic 'rfl' failed` - Reflexivity proof failures
- `tactic 'simp' made no progress` - Simplification failures
- `unsolved goals` - Incomplete proofs with remaining subgoals
- `type mismatch` - Type checking errors
- `unknown constant` / `unknown identifier` - Missing definitions
- `Application type mismatch` - Function application errors
- `Invalid field` - Non-existent field access

## Dataset Characteristics

| Property | Value |
|----------|-------|
| **Creator** | University of Washington Math AI Lab |
| **Size** | 100K < n < 1M entries |
| **Language** | English |
| **Primary Task** | Text Generation |
| **Tags** | lean, formal-verification, theorem-proving, code, math |
| **License** | Apache 2.0 |
| **ArXiv** | 2602.02990 |
| **Splits** | train, validation, test |

## Example Entry Structure

```json
{
  "path": "CategoryTheory.Bicategory.id_whiskerLeft_symm.lean",
  "correct_proof": "by simp",
  "incorrect_proof": "by rw [← Iso.inv_comp_eq, ...]",
  "theorem": null,
  "src_hash": "25ba40f63317...",
  "line": 8,
  "col": 6,
  "error": "tactic 'rewrite' failed, did not find instance of the pattern...",
  "line_at_error": "rw [← Iso.inv_comp_eq, leftUnitor_naturality, Category.assoc]",
  "state_at_error": "B : Type u\ninst✝ : Bicategory B\n...",
  "explanation": "The proof fails because the rewrite tactic cannot match...",
  "fix_suggestion": "Use the `simp` tactic which can automatically handle...",
  "source": "herald",
  "error_type": "lme",
  "split": "train"
}
```

## Resolution

To fix the dataset viewer, the authors need to either:

1. **Harmonize schemas** - Ensure all JSONL files have matching columns
2. **Create separate configurations** - Set up different dataset configurations for each error type (LME, MLME, THME, TME)
3. **Handle optional fields** - Properly null-pad missing fields across subsets
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "0c690a2f-1a2c-45b3-a0d6-d4c92bb37990",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "21a60c57-887a-4764-b4ef-2a166e67090f",
  "toolUseResult": {
    "bytes": 1119192,
    "code": 200,
    "codeText": "OK",
    "result": "# APRIL Dataset Analysis\n\n## Overview\nThe APRIL dataset from the University of Washington Math AI Lab is a collection of **Lean 4 theorem proving errors** designed for formal verification and theorem-proving research. However, the dataset viewer is currently broken due to schema inconsistencies.\n\n## Dataset Schema/Fields\n\nBased on the error message and preview data shown, the dataset contains the following fields:\n\n### Core Fields Present in All Files:\n1. **path** (string) - File path to the Lean source code\n2. **correct_proof** (string) - The correct proof\n3. **incorrect_proof** (string) - The incorrect/buggy proof\n4. **error** (string) - Error message produced\n5. **line_at_error** (string) - Line where error occurred\n6. **state_at_error** (string) - Proof state at error\n7. **explanation** (string) - Explanation of why the proof fails\n8. **fix_suggestion** (string) - Suggested fix\n9. **source** (string) - Source of the error\n10. **error_type** (string) - Classification of error type\n11. **split** (string) - train/validation/test split\n12. **line** (int64) - Line number\n13. **col** (int64) - Column number\n14. **src_hash** (string) - Source file hash\n\n### Fields Present in Some Files (Optional/Null):\n15. **theorem** (null)\n16. **correct_name** (null)\n17. **incorrect_name** (null)\n18. **correct_formal** (null)\n19. **incorrect_formal** (null)\n20. **correct_informal** (null)\n21. **incorrect_informal** (null)\n\n### Fields Causing Schema Issues (Present in MLME subset only):\n22. **metadata** (null) - Additional metadata\n23. **annotation_status** (null) - Annotation status\n24. **state_before** (null) - Proof state before error\n25. **state_after** (null) - Proof state after error\n\n## Schema Problem\n\nThe dataset has **inconsistent schemas** across multiple JSONL files:\n- `lme_train.jsonl` (Lean Module Errors)\n- `mlme_train.jsonl` (Multiple Line Module Errors) - **Contains 4 additional columns**\n- `thme_train.jsonl` (Tactic/Higher Module Errors)\n- `tme_train.jsonl` (Tactic Module Errors)\n\nThe `mlme_train.jsonl` file introduces `state_after`, `state_before`, `annotation_status`, and `metadata` fields that don't exist in other files, causing the `DatasetGenerationCastError`.\n\n## Error Classification\n\nThe **error_type** field categorizes errors. From the examples shown, error types include:\n\n- `tactic 'rewrite' failed` - Rewrite tactic pattern matching failures\n- `tactic 'rfl' failed` - Reflexivity proof failures\n- `tactic 'simp' made no progress` - Simplification failures\n- `unsolved goals` - Incomplete proofs with remaining subgoals\n- `type mismatch` - Type checking errors\n- `unknown constant` / `unknown identifier` - Missing definitions\n- `Application type mismatch` - Function application errors\n- `Invalid field` - Non-existent field access\n\n## Dataset Characteristics\n\n| Property | Value |\n|----------|-------|\n| **Creator** | University of Washington Math AI Lab |\n| **Size** | 100K < n < 1M entries |\n| **Language** | English |\n| **Primary Task** | Text Generation |\n| **Tags** | lean, formal-verification, theorem-proving, code, math |\n| **License** | Apache 2.0 |\n| **ArXiv** | 2602.02990 |\n| **Splits** | train, validation, test |\n\n## Example Entry Structure\n\n```json\n{\n  \"path\": \"CategoryTheory.Bicategory.id_whiskerLeft_symm.lean\",\n  \"correct_proof\": \"by simp\",\n  \"incorrect_proof\": \"by rw [← Iso.inv_comp_eq, ...]\",\n  \"theorem\": null,\n  \"src_hash\": \"25ba40f63317...\",\n  \"line\": 8,\n  \"col\": 6,\n  \"error\": \"tactic 'rewrite' failed, did not find instance of the pattern...\",\n  \"line_at_error\": \"rw [← Iso.inv_comp_eq, leftUnitor_naturality, Category.assoc]\",\n  \"state_at_error\": \"B : Type u\\ninst✝ : Bicategory B\\n...\",\n  \"explanation\": \"The proof fails because the rewrite tactic cannot match...\",\n  \"fix_suggestion\": \"Use the `simp` tactic which can automatically handle...\",\n  \"source\": \"herald\",\n  \"error_type\": \"lme\",\n  \"split\": \"train\"\n}\n```\n\n## Resolution\n\nTo fix the dataset viewer, the authors need to either:\n\n1. **Harmonize schemas** - Ensure all JSONL files have matching columns\n2. **Create separate configurations** - Set up different dataset configurations for each error type (LME, MLME, THME, TME)\n3. **Handle optional fields** - Properly null-pad missing fields across subsets",
    "durationMs": 14921,
    "url": "https://huggingface.co/datasets/uw-math-ai/APRIL"
  },
  "sourceToolAssistantUUID": "0c690a2f-1a2c-45b3-a0d6-d4c92bb37990",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 37 · 2026-05-28T14:28:49.098Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have very important information. The APRIL dataset has:

1. An **`error_type` field** - but it appears to categorize by mutation type (lme = Line Module Errors, mlme = Multiple Line Module Errors, thme = Tactic/Higher Module Errors, tme = Tactic Module Errors), NOT by the actual error type (like typeclass failures, coercion mismatches, etc.)
2. An **`error` field** - which contains the raw Lean compiler error messages (like "tactic 'rewrite' failed", "type mismatch", "unknown constant", etc.)


3. A **`path` field** - which contains Mathlib module paths

So the reviewer's distinction is important: the `error_type` field classifies errors by how they were generated through mutation, not by their semantic category. The actual detailed error categories would need to be extracted from parsing the raw `error` field text. Let me reconsider what the reviewer was actually pointing out about the HuggingFace schema...

The reviewer is clarifying that APRIL already categorizes errors into mutation types like line mutations, multi-line mutations, tactic errors, and theorem substitutions. What we're proposing isn't a new error taxonomy from scratch, but rather a cross-tabulation of these existing mutation-type categories with domain information from the path field, potentially refined by analyzing the actual error messages. This is a more precise characterization of our contribution than claiming we're introducing a novel domain-specific error taxonomy.

Now I need to verify KELPS's actual venue — the HTML indicates it was published at ICML main conference, but I should confirm whether it's a workshop paper or main conference paper given the July 2025 timing. I should just move forward with what I have rather than keep searching—the reviewer cited it as a baseline, so I'll use that. Looking at the deadlines: AAAI 2027 is July 28, 2026, which is about 8.7 weeks away, making the full 11-week pipeline infeasible. The ICML 2026 AI4Math Workshop deadline already passed on May 25, but the challenge track is still open until June 15. I have what I need to draft the response now.

For the revision, I need to be clearer about what's already in APRIL versus what we're contributing. APRIL has an `error_type` field with mutation categories, plus raw compiler error messages—our novel work is cross-tabulating those existing categories with mathematical subdomains and extracting a finer-grained taxonomy from the raw error messages themselves, stratified by domain. On the venue side, I'll mark AAAI 2027 as infeasible for the full pipeline but note that we could potentially submit the error taxonomy and initial retrieval work as a partial contribution, while ICML's paper deadline has closed though the challenge track remains open.

I should also add LeanPremise and LeanHammer to the landscape—they're the first end-to-end domain-general hammer for Lean with strong generalization metrics, but they target premise selection for proving rather than retrieval and don't condition on mathematical subdomain. KELPS is another key reference with 88.9% syntactic accuracy on MiniF2F using an intermediate representation across multiple proof assistants, focusing on syntactic accuracy without domain-specific conditioning.

Now I'm realizing the reviewer's feedback is actually straightforward—they're saying the minor fixes will get me to 4.0, not that I need a major pivot. The "stagnation" warning is just a template note, but the explicit guidance is clear: these four fixes are sufficient. I should focus on executing them well rather than overthinking the scope.

Let me construct the revised JSON with all five issues integrated as minor fixes.

For each section, I need to be precise about what's changing: clarifying APRIL's existing error_type field and our taxonomy contribution in the core problem, updating the opportunity and landscape sections to reflect APRIL's capabilities and add the missing tools like LeanPremise and KELPS, refining the approach to explain the domain-stratified cross-tabulation aspect, and adjusting the target venues to be realistic about AAAI 2027 and ICML 2026 constraints.

The key insight is distinguishing between APRIL's error_type field—which categorizes how errors were generated through mutation strategies—and the raw error field containing actual Lean compiler messages like type mismatches and unsolved goals. Our contribution sits at the intersection: creating a semantic taxonomy of compiler errors and cross-tabulating them by domain and mutation type to reveal patterns about what kinds of errors emerge from different generation strategies. So the real contribution is the domain-stratified analysis and the statistical measures we're applying—the Jensen-Shannon divergence and predictive power analysis—not the error categories themselves. I should also verify whether KELPS was actually published at the main ICML conference or just the workshop, since that affects how I position it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21a60c57-887a-4764-b4ef-2a166e67090f",
  "isSidechain": false,
  "requestId": "req_011CbV88Qoq1aHwG4ZfaFLys",
  "type": "assistant",
  "uuid": "a79465de-acf4-4335-b11e-1c704e8be6bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dc1XsWWzzxx6XjuJeYvBN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 32581,
      "output_tokens": 2596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2596,
          "cache_read_input_tokens": 32581,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1450
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

_source line 38 · 2026-05-28T14:28:49.108Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1beW7yqVeVDnKL7kRwAm2`</summary>

```json
{
  "query": "KELPS \"Knowledge Equations\" autoformalization venue \"ICML 2025\" workshop OR conference 2507.08665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a79465de-acf4-4335-b11e-1c704e8be6bb",
  "isSidechain": false,
  "requestId": "req_011CbV88Qoq1aHwG4ZfaFLys",
  "type": "assistant",
  "uuid": "1ec170e5-c4e7-4837-ab73-646fe49528e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dc1XsWWzzxx6XjuJeYvBN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1450,
      "cache_read_input_tokens": 32581,
      "output_tokens": 2596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1450,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2596,
          "cache_read_input_tokens": 32581,
          "cache_creation_input_tokens": 1450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1450
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

_source line 39 · 2026-05-28T14:28:55.950Z_

<details><summary>↩ Tool result · `toolu_01H1beW7yqVeVDnKL7kRwAm2`</summary>

```text
Web search results for query: "KELPS "Knowledge Equations" autoformalization venue "ICML 2025" workshop OR conference 2507.08665"

Links: [{"title":"[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/abs/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/html/2507.08665"},{"title":"Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs","url":"https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"ICML 2025 Friday 07/18","url":"https://icml.cc/virtual/2025/day/7/18"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"}]

Based on the search results, here's what I found about KELPS and its venue:

KELPS (Knowledge-Equation based Logical Processing System) is a novel neuro-symbolic framework for autoformalization. The framework translates natural language into Knowledge Equations (KEs), a novel language theoretically grounded in assertional logic, and is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle).

The framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.

Regarding the paper with identifier 2507.08665: The paper was posted on July 11, 2025. However, the search results do not contain specific information about this paper being presented at an ICML 2025 workshop or conference. The search results show general information about ICML 2025 and autoformalization-related topics, but do not confirm KELPS' presentation venue at ICML 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ec170e5-c4e7-4837-ab73-646fe49528e9",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "99820828-6b12-4fbb-a87c-de5de4fd96bd",
  "toolUseResult": {
    "query": "KELPS \"Knowledge Equations\" autoformalization venue \"ICML 2025\" workshop OR conference 2507.08665",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T5S9F2xCTZrGZH7T9KadaP",
        "content": [
          {
            "title": "[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/abs/2507.08665"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/html/2507.08665"
          },
          {
            "title": "Towards Autoformalization of Mathematics and Code Correctness: Experiments with Elementary Proofs",
            "url": "https://www.researchgate.net/publication/372928041_Towards_Autoformalization_of_Mathematics_and_Code_Correctness_Experiments_with_Elementary_Proofs"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "ICML 2025 Friday 07/18",
            "url": "https://icml.cc/virtual/2025/day/7/18"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2505.23486"
          },
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/pdf/2410.04194"
          }
        ]
      },
      "Based on the search results, here's what I found about KELPS and its venue:\n\nKELPS (Knowledge-Equation based Logical Processing System) is a novel neuro-symbolic framework for autoformalization. The framework translates natural language into Knowledge Equations (KEs), a novel language theoretically grounded in assertional logic, and is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle).\n\nThe framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.\n\nRegarding the paper with identifier 2507.08665: The paper was posted on July 11, 2025. However, the search results do not contain specific information about this paper being presented at an ICML 2025 workshop or conference. The search results show general information about ICML 2025 and autoformalization-related topics, but do not confirm KELPS' presentation venue at ICML 2025."
    ],
    "durationSeconds": 6.837644528000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1ec170e5-c4e7-4837-ab73-646fe49528e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "99820828-6b12-4fbb-a87c-de5de4fd96bd",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Tool call

_source line 42 · 2026-05-28T14:29:00.542Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LcX7a3vE6q3gLdkQGHxUmR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.08665",
  "prompt": "What venue is this paper published at or submitted to? Is it ICML 2025 main conference, ICML 2025 AI4Math Workshop, or just an arXiv preprint? Look for any venue information in the abstract, comments, or metadata."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99820828-6b12-4fbb-a87c-de5de4fd96bd",
  "isSidechain": false,
  "requestId": "req_011CbV8Dveb5jmCFGD82oCw2",
  "type": "assistant",
  "uuid": "fce91413-7f8c-422b-8f77-4579eb06990b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xiiU65pTCduR9m4SA5fNh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3237,
      "cache_read_input_tokens": 34031,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3237,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 34031,
          "cache_creation_input_tokens": 3237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3237
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

_source line 43 · 2026-05-28T14:29:03.431Z_

<details><summary>↩ Tool result · `toolu_01LcX7a3vE6q3gLdkQGHxUmR`</summary>

```text
Based on the provided content, this paper is submitted to the **ICML 2025 AI4Math Workshop**, not the main ICML 2025 conference.

The comments section explicitly states: "Accepted by the ICML 2025 AI4MATH Workshop. 22 pages, 16 figures, 2 tables"

While the paper is currently available as an arXiv preprint (arXiv:2507.08665), it has been accepted for presentation at this specialized workshop focused on AI applications in mathematics, rather than being submitted to the primary ICML conference track.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fce91413-7f8c-422b-8f77-4579eb06990b",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "35590538-da37-4a0b-b5a2-16a9a38f6760",
  "toolUseResult": {
    "bytes": 45296,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the provided content, this paper is submitted to the **ICML 2025 AI4Math Workshop**, not the main ICML 2025 conference.\n\nThe comments section explicitly states: \"Accepted by the ICML 2025 AI4MATH Workshop. 22 pages, 16 figures, 2 tables\"\n\nWhile the paper is currently available as an arXiv preprint (arXiv:2507.08665), it has been accepted for presentation at this specialized workshop focused on AI applications in mathematics, rather than being submitted to the primary ICML conference track.",
    "durationMs": 2886,
    "url": "https://arxiv.org/abs/2507.08665"
  },
  "sourceToolAssistantUUID": "fce91413-7f8c-422b-8f77-4579eb06990b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-28T14:29:07.311Z_

<details><summary>Logged reasoning block</summary>

```text
Good, so KELPS is an ICML 2025 AI4Math Workshop paper, not main conference. Let me now verify the LeanPremise/LeanHammer venue - the reviewer says ICLR 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35590538-da37-4a0b-b5a2-16a9a38f6760",
  "isSidechain": false,
  "requestId": "req_011CbV8EUYUa8ezhe8YS1doP",
  "type": "assistant",
  "uuid": "796f2420-d016-4b18-ad8a-52fc8d0ad6fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSorTCjEZ5Rtj5TUuHDbAS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 37268,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 37268,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 45 · 2026-05-28T14:29:08.280Z_

Now I have all the information needed. Let me also verify the LeanHammer miniCTX-v2 claim more precisely:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "796f2420-d016-4b18-ad8a-52fc8d0ad6fa",
  "isSidechain": false,
  "requestId": "req_011CbV8EUYUa8ezhe8YS1doP",
  "type": "assistant",
  "uuid": "210250ce-cdb7-4cc6-be46-40feb7205895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSorTCjEZ5Rtj5TUuHDbAS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 37268,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 37268,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 46 · 2026-05-28T14:29:10.988Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SKhmEgSyDDgHxtabE2RYBt`</summary>

```json
{
  "url": "https://cmu-l3.github.io/lean-hammer/",
  "prompt": "Extract the key performance numbers: What is the 79.4% relative to upper bound on miniCTX-v2? What are the exact proof rates on Mathlib-test and miniCTX-v2-test? How does LeanPremise compare to ReProver and other baselines? Any domain-specific results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "210250ce-cdb7-4cc6-be46-40feb7205895",
  "isSidechain": false,
  "requestId": "req_011CbV8EUYUa8ezhe8YS1doP",
  "type": "assistant",
  "uuid": "a8aa5afb-0ffa-4d03-8905-f86f4d447ca8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSorTCjEZ5Rtj5TUuHDbAS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 37268,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 37268,
          "cache_creation_input_tokens": 282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 282
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

_source line 47 · 2026-05-28T14:29:14.066Z_

<details><summary>↩ Tool result · `toolu_01SKhmEgSyDDgHxtabE2RYBt`</summary>

```text
I don't have the specific performance numbers you're asking about in the provided web page content. The page contains only:

- An overview stating that LeanHammer "shows an ability to close goals in Mathlib and generalize to projects it was not trained on"
- A brief description of its components and architecture
- Installation and usage instructions

The detailed metrics—including the 79.4% figure, exact proof rates on Mathlib-test and miniCTX-v2-test, and comparisons to ReProver and other baselines—are not included on this landing page.

To find these performance numbers, you would need to consult the full research paper on [arXiv](https://arxiv.org/abs/2506.07477) or the [GitHub repository](https://github.com/JOSHCLUNE/LeanHammer), which likely contain comprehensive experimental results and ablation studies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8aa5afb-0ffa-4d03-8905-f86f4d447ca8",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "7becc318-cf62-4f25-8832-fee1f2892179",
  "toolUseResult": {
    "bytes": 6676,
    "code": 200,
    "codeText": "OK",
    "result": "I don't have the specific performance numbers you're asking about in the provided web page content. The page contains only:\n\n- An overview stating that LeanHammer \"shows an ability to close goals in Mathlib and generalize to projects it was not trained on\"\n- A brief description of its components and architecture\n- Installation and usage instructions\n\nThe detailed metrics—including the 79.4% figure, exact proof rates on Mathlib-test and miniCTX-v2-test, and comparisons to ReProver and other baselines—are not included on this landing page.\n\nTo find these performance numbers, you would need to consult the full research paper on [arXiv](https://arxiv.org/abs/2506.07477) or the [GitHub repository](https://github.com/JOSHCLUNE/LeanHammer), which likely contain comprehensive experimental results and ablation studies.",
    "durationMs": 3075,
    "url": "https://cmu-l3.github.io/lean-hammer/"
  },
  "sourceToolAssistantUUID": "a8aa5afb-0ffa-4d03-8905-f86f4d447ca8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T14:29:20.641Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HKB2WttH6MDHSy4n2w5rJq`</summary>

```json
{
  "url": "https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf",
  "prompt": "Extract the key experimental results: 1) Exact proof rates on Mathlib-test and miniCTX-v2-test, 2) The 79.4% relative to upper bound claim - what exactly does it mean?, 3) Comparison with ReProver and other baselines, 4) Any domain-specific results showing performance variation across mathematical areas, 5) How LeanPremise handles out-of-distribution generalization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7becc318-cf62-4f25-8832-fee1f2892179",
  "isSidechain": false,
  "requestId": "req_011CbV8FFyTiJsuwmJ9tdySW",
  "type": "assistant",
  "uuid": "5623dd64-21b3-4138-91a1-d58e0915093b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zd5mBWp1rBBvNMsWUq5Zq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 464,
      "cache_read_input_tokens": 37550,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 200,
          "cache_read_input_tokens": 37550,
          "cache_creation_input_tokens": 464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 464
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

_source line 49 · 2026-05-28T14:29:26.618Z_

<details><summary>↩ Tool result · `toolu_01HKB2WttH6MDHSy4n2w5rJq`</summary>

```text
I appreciate your request, but I need to be direct: the content you've provided appears to be raw PDF binary data (compressed streams and object references), not readable text. The page contains encoded font files and document structure metadata rather than accessible research results.

To properly extract the experimental results you're asking about, I would need:

1. **A readable text version** of the paper (PDF converted to text, or the original document source)
2. **The paper's title and authors** to verify I'm analyzing the correct work
3. **Confirmation this is about "LeanPremise"** - a system for mathematical theorem proving

Without legible content, I cannot provide:
- ✗ Exact proof rates on test datasets
- ✗ Explanation of the 79.4% relative bound claim
- ✗ Baseline comparisons with ReProver
- ✗ Domain-specific performance breakdowns
- ✗ Out-of-distribution generalization details

**What I can do:** If you provide the paper in a readable format (plain text, clean PDF, or direct quotes), I'll extract and analyze those five specific experimental findings while respecting your character limits and citation requirements.

Would you like to share a readable version of this research?

[Binary content (application/pdf, 362.8KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/481f3ec1-3c98-476a-9097-7a4273796126/tool-results/webfetch-1779978561178-kehbeg.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5623dd64-21b3-4138-91a1-d58e0915093b",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "0c6c30f6-d42b-475b-8aa0-e150ecc5aab6",
  "toolUseResult": {
    "bytes": 371532,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your request, but I need to be direct: the content you've provided appears to be raw PDF binary data (compressed streams and object references), not readable text. The page contains encoded font files and document structure metadata rather than accessible research results.\n\nTo properly extract the experimental results you're asking about, I would need:\n\n1. **A readable text version** of the paper (PDF converted to text, or the original document source)\n2. **The paper's title and authors** to verify I'm analyzing the correct work\n3. **Confirmation this is about \"LeanPremise\"** - a system for mathematical theorem proving\n\nWithout legible content, I cannot provide:\n- ✗ Exact proof rates on test datasets\n- ✗ Explanation of the 79.4% relative bound claim\n- ✗ Baseline comparisons with ReProver\n- ✗ Domain-specific performance breakdowns\n- ✗ Out-of-distribution generalization details\n\n**What I can do:** If you provide the paper in a readable format (plain text, clean PDF, or direct quotes), I'll extract and analyze those five specific experimental findings while respecting your character limits and citation requirements.\n\nWould you like to share a readable version of this research?\n\n[Binary content (application/pdf, 362.8KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu/481f3ec1-3c98-476a-9097-7a4273796126/tool-results/webfetch-1779978561178-kehbeg.pdf]",
    "durationMs": 5973,
    "url": "https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf"
  },
  "sourceToolAssistantUUID": "5623dd64-21b3-4138-91a1-d58e0915093b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-28T14:29:31.992Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J22dodoJQrgRDf82UE5CuJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.07477",
  "prompt": "Find the experimental results section. Extract: 1) Exact proof rates on Mathlib-test and miniCTX-v2-test for LeanPremise/LeanHammer, 2) The 79.4% relative to upper bound - what does it mean exactly?, 3) Comparison numbers with ReProver, MePo, and other baselines, 4) Performance variation across miniCTX-v2 projects (Carleson, ConNF, FLT, etc.), 5) Key claims about out-of-distribution generalization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c6c30f6-d42b-475b-8aa0-e150ecc5aab6",
  "isSidechain": false,
  "requestId": "req_011CbV8GBmEQZXik7hRF9cQm",
  "type": "assistant",
  "uuid": "7e0f17c9-1a52-4f3c-89b3-739d7055d832",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TRTVhhwLonQzuTjFJCGd83",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 565,
      "cache_read_input_tokens": 38014,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 38014,
          "cache_creation_input_tokens": 565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 565
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

_source line 51 · 2026-05-28T14:29:39.999Z_

<details><summary>↩ Tool result · `toolu_01J22dodoJQrgRDf82UE5CuJ`</summary>

```text
# LeanHammer Experimental Results

## 1) Proof Rates on Test Sets

**Mathlib-test (Table 2):**
- LeanPremise (large model), full setting: 30.1% proof rate
- LeanPremise (large model), cumul setting: 33.3% proof rate
- Ground truth upper bound: 43.0% proof rate

**miniCTX-v2-test (Table 3):**
- LeanPremise (large): 20.7% average proof rate across six projects
- Ground truth upper bound: 26.1% average proof rate
- Performance varies by project: Carleson (0%), ConNF (16%), FLT (36.4%), Foundation (38%), HepLean (10%), Seymour (24%)

## 2) The 79.4% Relative-to-Upper-Bound Metric

The paper states: "the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and 79.4% on miniCTX."

This measures how close neural retrieval gets to the theoretical ceiling. At 79.4%, LeanHammer achieves approximately four-fifths of the maximum possible performance when given perfect premise selection.

## 3) Baseline Comparisons

| Approach | Recall@32 | Full Proof Rate |
|----------|-----------|-----------------|
| None | 0% | 16.9% |
| MePo | 42.1% | 26.3% |
| ReProver (218M) | 38.7% | 12.0% |
| LeanPremise (large, 82M) | 72.7% | 30.1% |
| LeanPremise (cumulative) | — | 37.3% |

The authors claim LeanPremise achieves "73% higher relative to MePo" on recall@32 and "21% higher" cumulative proof rates.

## 4) miniCTX-v2 Project Variation

Projects showed substantial heterogeneity in success: Foundation achieved 38% despite lacking specialized training data, while Carleson achieved 0%, suggesting domain-specific reasoning requirements exceed the hammer's capabilities.

## 5) Out-of-Distribution Generalization Claims

The research demonstrates "robust out-of-Mathlib generalization," with performance ratios against the upper bound (79.4%) remaining comparable to within-distribution results (73.5%), indicating the model transfers effectively despite training exclusively on Mathlib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e0f17c9-1a52-4f3c-89b3-739d7055d832",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "8c0a2059-09aa-471c-9176-9637c039dc0a",
  "toolUseResult": {
    "bytes": 383352,
    "code": 200,
    "codeText": "OK",
    "result": "# LeanHammer Experimental Results\n\n## 1) Proof Rates on Test Sets\n\n**Mathlib-test (Table 2):**\n- LeanPremise (large model), full setting: 30.1% proof rate\n- LeanPremise (large model), cumul setting: 33.3% proof rate\n- Ground truth upper bound: 43.0% proof rate\n\n**miniCTX-v2-test (Table 3):**\n- LeanPremise (large): 20.7% average proof rate across six projects\n- Ground truth upper bound: 26.1% average proof rate\n- Performance varies by project: Carleson (0%), ConNF (16%), FLT (36.4%), Foundation (38%), HepLean (10%), Seymour (24%)\n\n## 2) The 79.4% Relative-to-Upper-Bound Metric\n\nThe paper states: \"the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and 79.4% on miniCTX.\"\n\nThis measures how close neural retrieval gets to the theoretical ceiling. At 79.4%, LeanHammer achieves approximately four-fifths of the maximum possible performance when given perfect premise selection.\n\n## 3) Baseline Comparisons\n\n| Approach | Recall@32 | Full Proof Rate |\n|----------|-----------|-----------------|\n| None | 0% | 16.9% |\n| MePo | 42.1% | 26.3% |\n| ReProver (218M) | 38.7% | 12.0% |\n| LeanPremise (large, 82M) | 72.7% | 30.1% |\n| LeanPremise (cumulative) | — | 37.3% |\n\nThe authors claim LeanPremise achieves \"73% higher relative to MePo\" on recall@32 and \"21% higher\" cumulative proof rates.\n\n## 4) miniCTX-v2 Project Variation\n\nProjects showed substantial heterogeneity in success: Foundation achieved 38% despite lacking specialized training data, while Carleson achieved 0%, suggesting domain-specific reasoning requirements exceed the hammer's capabilities.\n\n## 5) Out-of-Distribution Generalization Claims\n\nThe research demonstrates \"robust out-of-Mathlib generalization,\" with performance ratios against the upper bound (79.4%) remaining comparable to within-distribution results (73.5%), indicating the model transfers effectively despite training exclusively on Mathlib.",
    "durationMs": 8003,
    "url": "https://arxiv.org/html/2506.07477"
  },
  "sourceToolAssistantUUID": "7e0f17c9-1a52-4f3c-89b3-739d7055d832",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-28T14:30:04.613Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me construct the complete revised JSON.

Key findings from my research:

**LeanPremise/LeanHammer (ICLR 2026)**:
- First end-to-end domain-general hammer for Lean
- LeanPremise: neural premise selection, 82M params
- Mathlib-test: 30.1% proof rate (vs. 43.0% upper bound = 73.5% relative)
- miniCTX-v2: 20.7% average (vs. 26.1% upper bound = 79.4% relative)


- Performance varies significantly across projects—Carleson at 0%, Foundation at 38%, ConNF at 16%, FLT at 36.4%—with dynamic adaptation through a client-server setup that substantially outperforms ReProver despite having fewer parameters, focusing specifically on premise selection rather than autoformalization

**KELPS (ICML 2025 AI4Math Workshop)**:
- Achieves 88.9% syntactic accuracy on MiniF2F through Knowledge Equations, supporting multiple languages including Lean, Coq, and Isabelle across 60k+ natural language-formal language pairs in a domain-agnostic approach, though it's a workshop paper rather than a main conference publication

**APRIL**

:
- The dataset includes error categorization with line mutations, multi-line mutations, theorem substitutions, and tactic mutations, plus raw compiler messages like type mismatches and unknown constants mapped to Mathlib modules—my contribution involves creating a cross-tabulation of these existing error categories alongside a finer-grained taxonomy derived from the compiler output, all stratified by mathematical domain

For venue timing, AAAI 2027 with its July 2026 deadline leaves only about 8 weeks from late May, making the full 11-week pipeline infeasible, whereas ICML 2026's AI4Math workshop has a May 25, 2026 deadline that's more realistic.

Now I'm revising the full proposal to integrate the APRIL error taxonomy throughout, add LeanPremise and LeanHammer to the related work, include KELPS in the landscape, correct the venue timelines, and incorporate feedback from the previous round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c0a2059-09aa-471c-9176-9637c039dc0a",
  "isSidechain": false,
  "requestId": "req_011CbV8HApi3AYcdyJ1X4XVy",
  "type": "assistant",
  "uuid": "1b3f318b-6e99-4439-a8d5-ede4ebebf1dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JehmnaWMjsSa2sUQiXUozH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 38579,
      "output_tokens": 2284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2284,
          "cache_read_input_tokens": 38579,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
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

_source line 53 · 2026-05-28T14:30:04.695Z_

Now I have all the research I need. Let me compile the complete revised JSON, addressing all 5 reviewer issues with proper depth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3f318b-6e99-4439-a8d5-ede4ebebf1dc",
  "isSidechain": false,
  "requestId": "req_011CbV8HApi3AYcdyJ1X4XVy",
  "type": "assistant",
  "uuid": "c45ad668-2d02-4938-bca0-e007d7560f95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JehmnaWMjsSa2sUQiXUozH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 38579,
      "output_tokens": 2284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2284,
          "cache_read_input_tokens": 38579,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
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

_source line 54 · 2026-05-28T14:30:37.810Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LaZXrjBp5DG4RkVEw94a31`</summary>

```json
{
  "description": "Draft revised research idea JSON",
  "prompt": "I need you to help me assemble a complete revised research idea JSON. I'm going to give you the full context and you should output the COMPLETE JSON.\n\n## Context\n\nThis is Round 7 revision of a research idea about \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy.\" All 5 reviewer issues are MINOR. The reviewer says these fixes will clear the 4.0 threshold.\n\n## Research I've done\n\n### Issue 1: APRIL's existing error_type field\nThe APRIL HuggingFace dataset (uw-math-ai/APRIL) has these fields per entry:\n- `path` (string): Mathlib module path\n- `error_type` (string): Mutation category - values are \"lme\" (line mutation errors), \"mlme\" (multi-line mutation errors), \"thme\" (theorem substitution/higher errors), \"tme\" (tactic mutation errors)\n- `error` (string): Raw Lean compiler error messages like \"type mismatch\", \"unknown constant\", \"tactic 'rewrite' failed\", \"unsolved goals\", \"Application type mismatch\"\n- `correct_proof`, `incorrect_proof`, `explanation`, `fix_suggestion`, etc.\n\nThe reviewer says: our error taxonomy contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types + finer-grained taxonomy from the raw `error` field, NOT a completely new error classification. The novelty is in domain stratification and statistical analysis (JSD, predictive power).\n\n### Issue 2: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477)\n- First end-to-end domain-general hammer for Lean\n- LeanPremise: neural premise selection (82M params)\n- Mathlib-test: 30.1% proof rate (73.5% relative to 43.0% upper bound)\n- miniCTX-v2 OOD: 20.7% average (79.4% relative to 26.1% upper bound)\n- Significant project variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%\n- Dynamic user-context adaptation via client-server architecture\n- Outperforms ReProver (218M params) substantially\n- Targets premise selection for PROVING, not autoformalization retrieval\n- No mathematical subdomain conditioning\n\n### Issue 3: KELPS (ICML 2025 AI4Math Workshop, arXiv 2507.08665)\n- 88.9% syntactic accuracy (pass@1) on MiniF2F\n- Knowledge Equations as intermediate representation (NL → KE → Lean/Coq/Isabelle)\n- Outperforms DeepSeek-V3 (81%) and Herald (81.3%)\n- 60k+ NL-FL pairs across 6 math topics\n- Domain-agnostic - no subdomain conditioning\n- Workshop paper, NOT main conference\n\n### Issue 4: Venue timeline fixes\n- AAAI 2027: abstract Jul 21, paper Jul 28 = ~8 weeks from May 28, 2026. The auto_research timeline is 11 weeks. INFEASIBLE for full pipeline. Partial submission (error taxonomy + initial retrieval) could work.\n- ICML 2026 AI4Math Workshop: Paper deadline May 25, 2026 = ALREADY PASSED (3 days ago). Only challenge track participation (June 15 deadline) remains viable.\n\n## What needs to change in each section\n\n### core_problem:\n- Acknowledge APRIL's existing error_type field (mutation categories: lme/mlme/thme/tme) and clarify our taxonomy contribution as domain-stratified cross-tabulation + finer-grained taxonomy from raw compiler errors\n\n### opportunity:\n- Update APRIL description (item 3) to mention error_type field explicitly\n- Note that our taxonomy builds on APRIL's existing categorization\n\n### landscape:\n- Add LeanPremise/LeanHammer: strong domain-general premise selection in Lean ecosystem, 79.4% relative to upper bound OOD, significant project variation (Carleson 0% to Foundation 38%), but targets proving not autoformalization, no subdomain conditioning\n- Add KELPS: 88.9% MiniF2F syntactic accuracy via KE intermediate representation, domain-agnostic\n- Update APRIL description re: existing error_type\n\n### approach:\n- Stage 1: Clarify taxonomy as domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) PLUS a finer-grained error taxonomy extracted from the raw `error` field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the `path` field\n- The novelty is in domain stratification and statistical analysis, not in constructing error categories from scratch\n\n### target_venues:\n- AAAI 2027: Change \"STRETCH\" to explicitly infeasible for full pipeline; describe what partial submission (error taxonomy + domain-conditioned retrieval without full ablations) could target\n- ICML 2026 AI4Math: Note paper deadline passed May 25; only challenge tracks (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline\n\n### key_references:\n- Add: \"Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026)\"\n- Add: \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop)\"\n\n### revision_notes:\n- Add round 7 entries for all 5 issues\n\n### inspired_by:\n- Add LeanPremise as relevant domain-general retrieval/selection approach in Lean ecosystem\n- Add KELPS as strong MiniF2F baseline\n\nNow please write the COMPLETE JSON output. Keep ALL existing content that doesn't need changing. Make targeted, surgical edits. Include \"change_type\": \"minor\" at the end. The JSON should have all these top-level fields:\n- title\n- core_problem\n- opportunity\n- landscape\n- inspired_by\n- approach\n- resource_estimate\n- target_venues\n- level\n- key_references\n- description\n- project_name\n- source\n- revision_notes\n- change_type\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c45ad668-2d02-4938-bca0-e007d7560f95",
  "isSidechain": false,
  "requestId": "req_011CbV8HApi3AYcdyJ1X4XVy",
  "type": "assistant",
  "uuid": "ef3afbde-603a-4100-a7ab-0b82eb44b4e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JehmnaWMjsSa2sUQiXUozH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 38579,
      "output_tokens": 2284,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2284,
          "cache_read_input_tokens": 38579,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "ef3afbde-603a-4100-a7ab-0b82eb44b4e5",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Tool result

_source line 57 · 2026-05-28T14:40:33.307Z_

<details><summary>↩ Tool result · `toolu_01LaZXrjBp5DG4RkVEw94a31`</summary>

````text
I now have the complete Round 6 JSON. Now I can produce the Round 7 revision with all five issues addressed. Let me carefully construct it based on the user's detailed instructions.

Here is the complete Round 7 revised JSON:

```json
{
  "title": "Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy",
  "core_problem": "Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4-6x above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% -- demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation -- but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% -> 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased -- only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory -- demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods -- CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving -- but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain -- beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) -- and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?",
  "opportunity": "Six critical resources and findings converged in 2025-2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') -- the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores -- but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages -- making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (theta_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization -- but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains -- proving domain awareness helps -- but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning -- number theory at 0.722 vs. calculus at 0.516 -- but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems -- though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) -- but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across >=4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information -- a number theory problem may require analysis-level typeclasses -- and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.",
  "landscape": "Current SOTA autoformalization systems -- StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) -- all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with client-server architecture for dynamic user-context adaptation -- substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% -- confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F -- outperforming DeepSeek-V3 (81%) and Herald (81.3%) -- via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL -> KE -> Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning and is a workshop paper, not a main conference publication. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% -- the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains -- yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4-6x above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench -- confirming domain-dependent variation in autoformalization quality -- but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) -- demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain; notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across >=5 categories).",
  "inspired_by": "Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain -- IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain -- Shebzukhov (2026) shows domain-stratified aggregate scores but no error type taxonomy exists showing how autoformalization fails differently across domains), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4-6x thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%-38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.",
  "approach": "We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL->Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 -- Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories -- typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. -- also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' -- an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** -- we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness -- if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** -- we hypothesize that a simple classifier trained on domain -> error-type distributions will achieve >=70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes -- a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** -- for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by >=5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain -- a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 -- Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 -- Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters -- a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization -- leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** -- prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** -- replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness -- a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains x 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)",
      "timeline": "17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)",
      "estimated_gpu_cost": "$500 (H100 at ~$2.50/hr average via RunPod/Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~200 H100-hours",
      "timeline": "13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)",
      "claude_api_cost": "$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)",
      "estimated_gpu_cost": "$500"
    },
    "auto_research": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains x 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3-7 clusters: 6h)",
      "timeline": "11 weeks",
      "claude_api_cost": "$450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting)",
      "estimated_gpu_cost": "$500",
      "speed_bottleneck": "Lean4 type-checking latency (~3-10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k-5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 -- projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)",
    "AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 -- confirmed; only ~8 weeks from today; INFEASIBLE for full pipeline given auto_research timeline of 11 weeks. A partial submission targeting error taxonomy (Stage 1) + initial domain-conditioned retrieval results (Stage 2) without full Stage 3 ablations could be viable if Stage 1 yields strong early results within the first 6 weeks, but this requires aggressive prioritization and would omit the LoRA fine-tuning and full ablation suite)",
    "NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 -- contingent on workshop acceptance; workshop proposals due Jun 6, 2026)",
    "ICML 2026 AI4Math Workshop -- paper deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026). Only challenge track participation remains viable: ShadowBench Track 4 (challenge deadline Jun 15, 2026) for complementary multi-domain evaluation; FormalRx Track 1 (challenge deadline Jun 15, 2026) to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy"
  ],
  "level": "solid",
  "key_references": [
    "Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)",
    "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)",
    "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)",
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)",
    "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)",
    "Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)",
    "SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)",
    "Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)",
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)",
    "Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)",
    "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)",
    "Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)",
    "M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)",
    "Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)",
    "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)",
    "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)",
    "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)",
    "ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)",
    "FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)"
  ],
  "description": "We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization -- built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4-6x above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** -- leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for >=3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy >=70% (vs. ~20% random baseline), and >=5 percentage point formalization improvement from domain-specific mitigation recommendations -- complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** -- extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across >=5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.",
  "project_name": "domain_adapt_autoformal",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_compute_budget": "RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.",
    "round1_issue_2_venue_mismatch": "RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.",
    "round1_issue_3_model_choice": "RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.",
    "round1_issue_4_FineLeanCorpus": "RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.",
    "round1_issue_5_MSC180": "RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.",
    "round1_issue_6_circular_reasoning": "RESOLVED (Round 1): Error pattern claims reframed as hypotheses.",
    "round1_issue_7_VeriSoftBench": "RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.",
    "round1_issue_8_pipeline_complexity": "RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.",
    "round1_issue_9_baseline_fear_test": "RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.",
    "round2_issue_1_CRAMF_differentiation": "RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation -- concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.",
    "round2_issue_2_SITA": "RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.",
    "round2_issue_3_impact_argument": "RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.",
    "round2_issue_4_FineLeanCorpus_size": "RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.",
    "round2_issue_5_ICLR2027_deadline": "MITIGATED (Round 2): Estimated Sep 19/24 with contingency.",
    "round2_issue_6_M2F_RepoProver": "RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.",
    "round3_issue_1_DRIFT_Aria": "RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.",
    "round3_issue_2_ConNF_claim": "RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across >=5 categories.'",
    "round3_issue_3_error_taxonomy_elevation": "RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.",
    "round3_issue_4_compute_trim": "RESOLVED: All three modes <=200 H100-hours.",
    "round3_issue_5_LeanSearch_v2": "RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).",
    "round4_issue_1_IndiMathBench": "RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).",
    "round4_issue_2_quantitative_hypotheses": "RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.",
    "round4_issue_3_model_architecture": "RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.",
    "round5_issue_1_IndiMathBench_citation": "RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.",
    "round5_issue_2_BEq_correction": "RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.",
    "round5_issue_3_ShadowBench": "RESOLVED: Added ShadowBench and SCI Error Taxonomy.",
    "round5_issue_4_Mensfelt_framework": "RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.",
    "round5_issue_5_landscape_condensation": "RESOLVED: Condensed landscape to argument-driven organization.",
    "round6_issue_1_cycle_consistency_paper": "RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Narrowed ALL novelty claims from 'first empirical characterization of how autoformalization errors distribute across subdomains' to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across subdomains.' Explicitly differentiated: Shebzukhov reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) via observational analysis; our contribution classifies error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor (JSD, prediction accuracy, actionable recommendations). Noted that Shebzukhov is a Stanford CS224N course project performing observational analysis that concludes 'improvement is general rather than domain-specific.'",
    "round6_issue_2_ShadowBench_SCI_conflation": "RESOLVED: Separated Track 1 (FormalRx: semantic alignment evaluation using FormalRx-Test dataset with 28-category SCI Error Taxonomy, Macro F1 metrics) from Track 4 (ShadowBench: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate, NO error taxonomy). Fixed ALL conflated references throughout. Our error taxonomy complements FormalRx's SCI taxonomy (by error type) with subdomain stratification; our evaluation protocol complements ShadowBench's fixed-split multi-domain evaluation with leave-one-domain-out rotation.",
    "round6_issue_3_Herald_data_engineering": "RESOLVED: Acknowledged that Herald's HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with NO explicit module_path column. Module paths must be parsed from qualified theorem names. Identified APRIL's explicit 'path' field as more immediately usable. Restructured approach to use APRIL paths as primary domain signal. Added ~1 week to manual timeline for Herald path parsing.",
    "round7_issue_1_APRIL_error_type_field": "RESOLVED: Acknowledged APRIL's existing 'error_type' field (mutation categories: lme, mlme, thme, tme) and 'error' field (raw Lean compiler messages) throughout core_problem, opportunity, landscape, approach, inspired_by, and description. Clarified that our error taxonomy contribution is a domain-stratified cross-tabulation of APRIL's existing error_type categories PLUS a finer-grained taxonomy extracted from the raw 'error' field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch.",
    "round7_issue_2_LeanPremise_LeanHammer": "RESOLVED: Added LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Characterized as first end-to-end domain-general hammer for Lean with 82M-param neural premise selector, 79.4% relative proof rate OOD, but significant project variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%). Explicitly differentiated: targets premise selection for tactic-based proving, not autoformalization retrieval; uses no mathematical subdomain conditioning. Added to inspired_by as evidence of domain-dependent difficulty in the Lean ecosystem.",
    "round7_issue_3_KELPS": "RESOLVED: Added KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) to opportunity, landscape, inspired_by, description, and key_references. Characterized as achieving 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%), covering 60k+ NL-FL pairs across 6 math topics -- but entirely domain-agnostic with no subdomain conditioning. Noted as workshop paper, not main conference. Added to inspired_by as strong domain-agnostic MiniF2F baseline raising the bar for our approach.",
    "round7_issue_4_venue_timeline_fixes": "RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly INFEASIBLE for full pipeline (8 weeks vs. 11-week auto_research timeline), with description of what a partial submission could target (error taxonomy + initial retrieval without full ablations). ICML 2026 AI4Math Workshop updated to note paper deadline May 25 has PASSED; only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable.",
    "round7_issue_5_key_references_additions": "RESOLVED: Added 'Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)' and 'KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)' to key_references."
  },
  "change_type": "minor"
}
```

agentId: acd0a61d1ec84795d (use SendMessage with to: 'acd0a61d1ec84795d' to continue this agent)
&lt;usage>total_tokens: 85106
tool_uses: 44
duration_ms: 595490&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "ef3afbde-603a-4100-a7ab-0b82eb44b4e5",
  "isSidechain": false,
  "promptId": "6c6cad94-5133-4d60-bc3a-e5d4dd6e81b9",
  "type": "user",
  "uuid": "fcf8d01b-c88b-4b3e-96da-34fb540bf8e2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to help me assemble a complete revised research idea JSON. I'm going to give you the full context and you should output the COMPLETE JSON.\n\n## Context\n\nThis is Round 7 revision of a research idea about \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy.\" All 5 reviewer issues are MINOR. The reviewer says these fixes will clear the 4.0 threshold.\n\n## Research I've done\n\n### Issue 1: APRIL's existing error_type field\nThe APRIL HuggingFace dataset (uw-math-ai/APRIL) has these fields per entry:\n- `path` (string): Mathlib module path\n- `error_type` (string): Mutation category - values are \"lme\" (line mutation errors), \"mlme\" (multi-line mutation errors), \"thme\" (theorem substitution/higher errors), \"tme\" (tactic mutation errors)\n- `error` (string): Raw Lean compiler error messages like \"type mismatch\", \"unknown constant\", \"tactic 'rewrite' failed\", \"unsolved goals\", \"Application type mismatch\"\n- `correct_proof`, `incorrect_proof`, `explanation`, `fix_suggestion`, etc.\n\nThe reviewer says: our error taxonomy contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types + finer-grained taxonomy from the raw `error` field, NOT a completely new error classification. The novelty is in domain stratification and statistical analysis (JSD, predictive power).\n\n### Issue 2: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477)\n- First end-to-end domain-general hammer for Lean\n- LeanPremise: neural premise selection (82M params)\n- Mathlib-test: 30.1% proof rate (73.5% relative to 43.0% upper bound)\n- miniCTX-v2 OOD: 20.7% average (79.4% relative to 26.1% upper bound)\n- Significant project variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%\n- Dynamic user-context adaptation via client-server architecture\n- Outperforms ReProver (218M params) substantially\n- Targets premise selection for PROVING, not autoformalization retrieval\n- No mathematical subdomain conditioning\n\n### Issue 3: KELPS (ICML 2025 AI4Math Workshop, arXiv 2507.08665)\n- 88.9% syntactic accuracy (pass@1) on MiniF2F\n- Knowledge Equations as intermediate representation (NL → KE → Lean/Coq/Isabelle)\n- Outperforms DeepSeek-V3 (81%) and Herald (81.3%)\n- 60k+ NL-FL pairs across 6 math topics\n- Domain-agnostic - no subdomain conditioning\n- Workshop paper, NOT main conference\n\n### Issue 4: Venue timeline fixes\n- AAAI 2027: abstract Jul 21, paper Jul 28 = ~8 weeks from May 28, 2026. The auto_research timeline is 11 weeks. INFEASIBLE for full pipeline. Partial submission (error taxonomy + initial retrieval) could work.\n- ICML 2026 AI4Math Workshop: Paper deadline May 25, 2026 = ALREADY PASSED (3 days ago). Only challenge track participation (June 15 deadline) remains viable.\n\n## What needs to change in each section\n\n### core_problem:\n- Acknowledge APRIL's existing error_type field (mutation categories: lme/mlme/thme/tme) and clarify our taxonomy contribution as domain-stratified cross-tabulation + finer-grained taxonomy from raw compiler errors\n\n### opportunity:\n- Update APRIL description (item 3) to mention error_type field explicitly\n- Note that our taxonomy builds on APRIL's existing categorization\n\n### landscape:\n- Add LeanPremise/LeanHammer: strong domain-general premise selection in Lean ecosystem, 79.4% relative to upper bound OOD, significant project variation (Carleson 0% to Foundation 38%), but targets proving not autoformalization, no subdomain conditioning\n- Add KELPS: 88.9% MiniF2F syntactic accuracy via KE intermediate representation, domain-agnostic\n- Update APRIL description re: existing error_type\n\n### approach:\n- Stage 1: Clarify taxonomy as domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) PLUS a finer-grained error taxonomy extracted from the raw `error` field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the `path` field\n- The novelty is in domain stratification and statistical analysis, not in constructing error categories from scratch\n\n### target_venues:\n- AAAI 2027: Change \"STRETCH\" to explicitly infeasible for full pipeline; describe what partial submission (error taxonomy + domain-conditioned retrieval without full ablations) could target\n- ICML 2026 AI4Math: Note paper deadline passed May 25; only challenge tracks (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline\n\n### key_references:\n- Add: \"Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026)\"\n- Add: \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop)\"\n\n### revision_notes:\n- Add round 7 entries for all 5 issues\n\n### inspired_by:\n- Add LeanPremise as relevant domain-general retrieval/selection approach in Lean ecosystem\n- Add KELPS as strong MiniF2F baseline\n\nNow please write the COMPLETE JSON output. Keep ALL existing content that doesn't need changing. Make targeted, surgical edits. Include \"change_type\": \"minor\" at the end. The JSON should have all these top-level fields:\n- title\n- core_problem\n- opportunity\n- landscape\n- inspired_by\n- approach\n- resource_estimate\n- target_venues\n- level\n- key_references\n- description\n- project_name\n- source\n- revision_notes\n- change_type\n",
    "agentId": "acd0a61d1ec84795d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have the complete Round 6 JSON. Now I can produce the Round 7 revision with all five issues addressed. Let me carefully construct it based on the user's detailed instructions.\n\nHere is the complete Round 7 revised JSON:\n\n```json\n{\n  \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\",\n  \"core_problem\": \"Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4-6x above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% -- demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation -- but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% -> 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased -- only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory -- demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods -- CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving -- but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain -- beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) -- and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?\",\n  \"opportunity\": \"Six critical resources and findings converged in 2025-2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') -- the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores -- but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages -- making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (theta_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization -- but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains -- proving domain awareness helps -- but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning -- number theory at 0.722 vs. calculus at 0.516 -- but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems -- though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) -- but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across >=4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information -- a number theory problem may require analysis-level typeclasses -- and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\",\n  \"landscape\": \"Current SOTA autoformalization systems -- StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) -- all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with client-server architecture for dynamic user-context adaptation -- substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% -- confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F -- outperforming DeepSeek-V3 (81%) and Herald (81.3%) -- via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL -> KE -> Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning and is a workshop paper, not a main conference publication. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% -- the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains -- yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4-6x above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench -- confirming domain-dependent variation in autoformalization quality -- but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) -- demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain; notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across >=5 categories).\",\n  \"inspired_by\": \"Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain -- IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain -- Shebzukhov (2026) shows domain-stratified aggregate scores but no error type taxonomy exists showing how autoformalization fails differently across domains), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4-6x thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%-38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.\",\n  \"approach\": \"We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL->Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 -- Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories -- typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. -- also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' -- an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** -- we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness -- if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** -- we hypothesize that a simple classifier trained on domain -> error-type distributions will achieve >=70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes -- a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** -- for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by >=5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain -- a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 -- Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 -- Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters -- a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization -- leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** -- prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** -- replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness -- a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains x 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)\",\n      \"timeline\": \"17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)\",\n      \"estimated_gpu_cost\": \"$500 (H100 at ~$2.50/hr average via RunPod/Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200 H100-hours\",\n      \"timeline\": \"13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)\",\n      \"claude_api_cost\": \"$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)\",\n      \"estimated_gpu_cost\": \"$500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains x 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3-7 clusters: 6h)\",\n      \"timeline\": \"11 weeks\",\n      \"claude_api_cost\": \"$450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500\",\n      \"speed_bottleneck\": \"Lean4 type-checking latency (~3-10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k-5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 -- projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)\",\n    \"AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 -- confirmed; only ~8 weeks from today; INFEASIBLE for full pipeline given auto_research timeline of 11 weeks. A partial submission targeting error taxonomy (Stage 1) + initial domain-conditioned retrieval results (Stage 2) without full Stage 3 ablations could be viable if Stage 1 yields strong early results within the first 6 weeks, but this requires aggressive prioritization and would omit the LoRA fine-tuning and full ablation suite)\",\n    \"NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 -- contingent on workshop acceptance; workshop proposals due Jun 6, 2026)\",\n    \"ICML 2026 AI4Math Workshop -- paper deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026). Only challenge track participation remains viable: ShadowBench Track 4 (challenge deadline Jun 15, 2026) for complementary multi-domain evaluation; FormalRx Track 1 (challenge deadline Jun 15, 2026) to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\",\n    \"Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\",\n    \"Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)\",\n    \"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\",\n    \"Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\",\n    \"M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\",\n    \"Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\",\n    \"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\",\n    \"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\",\n    \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)\",\n    \"ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\",\n    \"FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\"\n  ],\n  \"description\": \"We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization -- built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4-6x above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** -- leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for >=3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy >=70% (vs. ~20% random baseline), and >=5 percentage point formalization improvement from domain-specific mitigation recommendations -- complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** -- extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across >=5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\",\n  \"project_name\": \"domain_adapt_autoformal\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_compute_budget\": \"RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.\",\n    \"round1_issue_2_venue_mismatch\": \"RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.\",\n    \"round1_issue_3_model_choice\": \"RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.\",\n    \"round1_issue_4_FineLeanCorpus\": \"RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.\",\n    \"round1_issue_5_MSC180\": \"RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.\",\n    \"round1_issue_6_circular_reasoning\": \"RESOLVED (Round 1): Error pattern claims reframed as hypotheses.\",\n    \"round1_issue_7_VeriSoftBench\": \"RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.\",\n    \"round1_issue_8_pipeline_complexity\": \"RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.\",\n    \"round1_issue_9_baseline_fear_test\": \"RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.\",\n    \"round2_issue_1_CRAMF_differentiation\": \"RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation -- concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.\",\n    \"round2_issue_2_SITA\": \"RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.\",\n    \"round2_issue_3_impact_argument\": \"RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.\",\n    \"round2_issue_4_FineLeanCorpus_size\": \"RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.\",\n    \"round2_issue_5_ICLR2027_deadline\": \"MITIGATED (Round 2): Estimated Sep 19/24 with contingency.\",\n    \"round2_issue_6_M2F_RepoProver\": \"RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.\",\n    \"round3_issue_1_DRIFT_Aria\": \"RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.\",\n    \"round3_issue_2_ConNF_claim\": \"RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across >=5 categories.'\",\n    \"round3_issue_3_error_taxonomy_elevation\": \"RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.\",\n    \"round3_issue_4_compute_trim\": \"RESOLVED: All three modes <=200 H100-hours.\",\n    \"round3_issue_5_LeanSearch_v2\": \"RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).\",\n    \"round4_issue_1_IndiMathBench\": \"RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).\",\n    \"round4_issue_2_quantitative_hypotheses\": \"RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.\",\n    \"round4_issue_3_model_architecture\": \"RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.\",\n    \"round5_issue_1_IndiMathBench_citation\": \"RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.\",\n    \"round5_issue_2_BEq_correction\": \"RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.\",\n    \"round5_issue_3_ShadowBench\": \"RESOLVED: Added ShadowBench and SCI Error Taxonomy.\",\n    \"round5_issue_4_Mensfelt_framework\": \"RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.\",\n    \"round5_issue_5_landscape_condensation\": \"RESOLVED: Condensed landscape to argument-driven organization.\",\n    \"round6_issue_1_cycle_consistency_paper\": \"RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Narrowed ALL novelty claims from 'first empirical characterization of how autoformalization errors distribute across subdomains' to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES (not just aggregate accuracy) distribute across subdomains.' Explicitly differentiated: Shebzukhov reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) via observational analysis; our contribution classifies error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor (JSD, prediction accuracy, actionable recommendations). Noted that Shebzukhov is a Stanford CS224N course project performing observational analysis that concludes 'improvement is general rather than domain-specific.'\",\n    \"round6_issue_2_ShadowBench_SCI_conflation\": \"RESOLVED: Separated Track 1 (FormalRx: semantic alignment evaluation using FormalRx-Test dataset with 28-category SCI Error Taxonomy, Macro F1 metrics) from Track 4 (ShadowBench: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate, NO error taxonomy). Fixed ALL conflated references throughout. Our error taxonomy complements FormalRx's SCI taxonomy (by error type) with subdomain stratification; our evaluation protocol complements ShadowBench's fixed-split multi-domain evaluation with leave-one-domain-out rotation.\",\n    \"round6_issue_3_Herald_data_engineering\": \"RESOLVED: Acknowledged that Herald's HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with NO explicit module_path column. Module paths must be parsed from qualified theorem names. Identified APRIL's explicit 'path' field as more immediately usable. Restructured approach to use APRIL paths as primary domain signal. Added ~1 week to manual timeline for Herald path parsing.\",\n    \"round7_issue_1_APRIL_error_type_field\": \"RESOLVED: Acknowledged APRIL's existing 'error_type' field (mutation categories: lme, mlme, thme, tme) and 'error' field (raw Lean compiler messages) throughout core_problem, opportunity, landscape, approach, inspired_by, and description. Clarified that our error taxonomy contribution is a domain-stratified cross-tabulation of APRIL's existing error_type categories PLUS a finer-grained taxonomy extracted from the raw 'error' field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch.\",\n    \"round7_issue_2_LeanPremise_LeanHammer\": \"RESOLVED: Added LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Characterized as first end-to-end domain-general hammer for Lean with 82M-param neural premise selector, 79.4% relative proof rate OOD, but significant project variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%). Explicitly differentiated: targets premise selection for tactic-based proving, not autoformalization retrieval; uses no mathematical subdomain conditioning. Added to inspired_by as evidence of domain-dependent difficulty in the Lean ecosystem.\",\n    \"round7_issue_3_KELPS\": \"RESOLVED: Added KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) to opportunity, landscape, inspired_by, description, and key_references. Characterized as achieving 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%), covering 60k+ NL-FL pairs across 6 math topics -- but entirely domain-agnostic with no subdomain conditioning. Noted as workshop paper, not main conference. Added to inspired_by as strong domain-agnostic MiniF2F baseline raising the bar for our approach.\",\n    \"round7_issue_4_venue_timeline_fixes\": \"RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly INFEASIBLE for full pipeline (8 weeks vs. 11-week auto_research timeline), with description of what a partial submission could target (error taxonomy + initial retrieval without full ablations). ICML 2026 AI4Math Workshop updated to note paper deadline May 25 has PASSED; only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable.\",\n    \"round7_issue_5_key_references_additions\": \"RESOLVED: Added 'Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)' and 'KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)' to key_references.\"\n  },\n  \"change_type\": \"minor\"\n}\n```"
      }
    ],
    "totalDurationMs": 595490,
    "totalTokens": 85106,
    "totalToolUseCount": 44,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18991,
      "cache_read_input_tokens": 53088,
      "output_tokens": 13026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13026,
          "cache_read_input_tokens": 53088,
          "cache_creation_input_tokens": 18991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18991,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 6,
      "bashCount": 35,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "ef3afbde-603a-4100-a7ab-0b82eb44b4e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 58 · 2026-05-28T14:40:33.315Z_

```json
{
  "parentUuid": "fcf8d01b-c88b-4b3e-96da-34fb540bf8e2",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4d0294c8-f98c-41f6-9f13-2583aef4fe3e",
  "timestamp": "2026-05-28T14:40:33.315Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "4d0294c8-f98c-41f6-9f13-2583aef4fe3e",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Assistant

_source line 61 · 2026-05-28T14:40:44.116Z_

<details><summary>Logged reasoning block</summary>

```text
The agent has produced a complete revised JSON. Let me review it carefully to make sure all 5 issues are properly addressed:

1. **APRIL error_type field**: ✅ Acknowledged throughout - core_problem, opportunity, landscape, approach, description all now mention the existing error_type field (lme/mlme/thme/tme) and raw error field. The taxonomy contribution is explicitly framed as domain-stratified cross-tabulation + finer-grained parsing of raw errors, not new error categories from scratch.


2. **LeanPremise/LeanHammer**: ✅ Added to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references with proper differentiation (premise selection for proving, not autoformalization; no subdomain conditioning; significant project variation).
3. **KELPS**: ✅ Added to opportunity, landscape, inspired_by, description, and key_references. Properly characterized as workshop paper with 88.9% MiniF2F syntactic accuracy.
4. **Venue timeline fixes**: ✅ AAAI 2027 changed from STRETCH to INFEASIBLE with partial submission description. ICML 2026 paper deadline noted as passed.
5. **Checking the final issue...**

All the updates are in place and the JSON structure looks solid. Ready to share this with the user.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0294c8-f98c-41f6-9f13-2583aef4fe3e",
  "isSidechain": false,
  "requestId": "req_011CbV97L5AaRSBjR1X8MK38",
  "type": "assistant",
  "uuid": "2b085090-d710-47af-ade5-5eb34349b9f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVeyK1BSwAJUaFb7q73xXk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15489,
      "cache_read_input_tokens": 39413,
      "output_tokens": 13692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 13692,
          "cache_read_input_tokens": 39413,
          "cache_creation_input_tokens": 15489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15489
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

_source line 62 · 2026-05-28T14:45:57.367Z_

I've completed thorough research on all 5 reviewer issues and produced the complete revised JSON. Here's a summary of what was researched and changed:

## Research Conducted

1. **APRIL dataset schema** — Fetched the actual HuggingFace dataset page (`uw-math-ai/APRIL`). Confirmed the dataset has an `error_type` field with mutation categories (lme/mlme/thme/tme), a raw `error` field with Lean compiler messages ("type mismatch", "unknown constant", etc.), and the `path` field with Mathlib module paths.

2. **LeanPremise/LeanHammer** — Read the full paper (arXiv 2506.07477, ICLR 2026). Key findings: 82M-param neural premise selector, 30.1% proof rate on Mathlib-test (73.5% of upper bound), 20.7% on miniCTX-v2 OOD (79.4% of upper bound), dramatic project variation (Carleson 0%, Foundation 38%), targets proving not autoformalization, no subdomain conditioning.

3. **KELPS** — Read the full paper (arXiv 2507.08665). Confirmed: ICML 2025 AI4Math **Workshop** paper (not main conference), 88.9% syntactic accuracy on MiniF2F via Knowledge Equations, domain-agnostic.

4. **Venue timelines** — Verified AAAI 2027 is 8 weeks away vs. 11-week minimum timeline; ICML 2026 AI4Math paper deadline was May 25 (passed).

## Key Changes in the Revision

| Issue | Change |
|-------|--------|
| **APRIL error_type** | Acknowledged existing `error_type` field (lme/mlme/thme/tme) and `error` field throughout. Taxonomy reframed as domain-stratified cross-tabulation + finer-grained parsing of raw compiler errors — novelty is in domain stratification and statistical analysis (JSD, predictive power), not constructing categories from scratch |
| **LeanPremise/LeanHammer** | Added to landscape, opportunity, approach, inspired_by, description, key_references. Differentiated: premise selection for proving (not autoformalization), no subdomain conditioning, but confirms domain-dependent difficulty (0%–38% project variation) |
| **KELPS** | Added to landscape, opportunity, inspired_by, description, key_references. Workshop paper, domain-agnostic, raises bar for our approach to show semantic correctness gains beyond syntactic compilation |
| **AAAI 2027** | Changed from "STRETCH" → explicitly **INFEASIBLE** for full pipeline; described viable partial submission (error taxonomy + initial retrieval) |
| **ICML 2026 AI4Math** | Noted paper deadline **passed** (May 25); only challenge track participation (June 15 deadline) remains |

**Change type: minor** — All 5 issues were minor per the reviewer, and the fixes are surgical integrations throughout the existing structure.

Here is the complete revised JSON:

```json
{
  "title": "Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy",
  "core_problem": "Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?",
  "opportunity": "Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.",
  "landscape": "Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain; notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).",
  "inspired_by": "Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain — Shebzukhov (2026) shows domain-stratified aggregate scores but no domain-stratified error type analysis exists), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%–38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.",
  "approach": "We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL→Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)",
      "timeline": "17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)",
      "estimated_gpu_cost": "$500 (H100 at ~$2.50/hr average via RunPod/Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~200 H100-hours",
      "timeline": "13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)",
      "claude_api_cost": "$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)",
      "estimated_gpu_cost": "$500"
    },
    "auto_research": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)",
      "timeline": "11 weeks",
      "claude_api_cost": "$450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting)",
      "estimated_gpu_cost": "$500",
      "speed_bottleneck": "Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)",
    "AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only ~8 weeks from today; INFEASIBLE for full pipeline given minimum 11-week auto_research timeline. A partial submission targeting error taxonomy (Stage 1) + initial domain-conditioned retrieval results (Stage 2) without full Stage 3 LoRA fine-tuning and ablation suite could be viable if Stage 1 yields strong early results within the first 6 weeks, but this requires aggressive prioritization and would omit key ablations)",
    "NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)",
    "ICML 2026 AI4Math Workshop — paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); paper submission is no longer possible. Only challenge track participation remains viable: ShadowBench Track 4 (challenge deadline Jun 15, 2026) for complementary multi-domain evaluation; FormalRx Track 1 (challenge deadline Jun 15, 2026) to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy"
  ],
  "level": "solid",
  "key_references": [
    "Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)",
    "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)",
    "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)",
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)",
    "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)",
    "Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)",
    "SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)",
    "Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)",
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)",
    "Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)",
    "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)",
    "Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)",
    "M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)",
    "Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)",
    "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)",
    "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)",
    "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)",
    "ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)",
    "FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)"
  ],
  "description": "We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.",
  "project_name": "domain_adapt_autoformal",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_compute_budget": "RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.",
    "round1_issue_2_venue_mismatch": "RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.",
    "round1_issue_3_model_choice": "RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.",
    "round1_issue_4_FineLeanCorpus": "RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.",
    "round1_issue_5_MSC180": "RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.",
    "round1_issue_6_circular_reasoning": "RESOLVED (Round 1): Error pattern claims reframed as hypotheses.",
    "round1_issue_7_VeriSoftBench": "RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.",
    "round1_issue_8_pipeline_complexity": "RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.",
    "round1_issue_9_baseline_fear_test": "RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.",
    "round2_issue_1_CRAMF_differentiation": "RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.",
    "round2_issue_2_SITA": "RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.",
    "round2_issue_3_impact_argument": "RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.",
    "round2_issue_4_FineLeanCorpus_size": "RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.",
    "round2_issue_5_ICLR2027_deadline": "MITIGATED (Round 2): Estimated Sep 19/24 with contingency.",
    "round2_issue_6_M2F_RepoProver": "RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.",
    "round3_issue_1_DRIFT_Aria": "RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.",
    "round3_issue_2_ConNF_claim": "RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across ≥5 categories.'",
    "round3_issue_3_error_taxonomy_elevation": "RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.",
    "round3_issue_4_compute_trim": "RESOLVED: All three modes ≤200 H100-hours.",
    "round3_issue_5_LeanSearch_v2": "RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).",
    "round4_issue_1_IndiMathBench": "RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).",
    "round4_issue_2_quantitative_hypotheses": "RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.",
    "round4_issue_3_model_architecture": "RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.",
    "round5_issue_1_IndiMathBench_citation": "RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.",
    "round5_issue_2_BEq_correction": "RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.",
    "round5_issue_3_ShadowBench": "RESOLVED: Added ShadowBench and SCI Error Taxonomy.",
    "round5_issue_4_Mensfelt_framework": "RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.",
    "round5_issue_5_landscape_condensation": "RESOLVED: Condensed landscape to argument-driven organization.",
    "round6_issue_1_cycle_consistency_paper": "RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout. Narrowed ALL novelty claims to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES distribute across subdomains.'",
    "round6_issue_2_ShadowBench_SCI_conflation": "RESOLVED: Separated Track 1 (FormalRx) from Track 4 (ShadowBench) throughout.",
    "round6_issue_3_Herald_data_engineering": "RESOLVED: Acknowledged Herald's limited schema; APRIL as primary domain signal.",
    "round7_issue_1_APRIL_error_type_field": "RESOLVED: Acknowledged APRIL's existing 'error_type' field (mutation categories: lme, mlme, thme, tme) and 'error' field (raw Lean compiler messages) throughout core_problem, opportunity, landscape, approach, inspired_by, and description. Clarified that our error taxonomy contribution is a domain-stratified cross-tabulation of APRIL's existing error_type categories PLUS a finer-grained taxonomy extracted from the raw 'error' field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the 'path' field. The novelty is explicitly stated as being in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. This prevents overclaiming while preserving the genuine novelty of domain-stratified error analysis.",
    "round7_issue_2_LeanPremise_LeanHammer": "RESOLVED: Added LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Characterized as first end-to-end domain-general hammer for Lean with 82M-param neural premise selector, 79.4% relative proof rate OOD on miniCTX-v2 (20.7% absolute vs. 26.1% upper bound), significant project variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), dynamic user-context adaptation. Explicitly differentiated: targets premise selection for tactic-based proving (not autoformalization retrieval); uses no mathematical subdomain conditioning; outperforms ReProver (218M). Its project-level variation provides additional evidence of domain-dependent difficulty in the Lean ecosystem.",
    "round7_issue_3_KELPS": "RESOLVED: Added KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) to opportunity, landscape, inspired_by, description, and key_references. Characterized as achieving 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations intermediate representation (NL → KE → Lean/Coq/Isabelle), outperforming DeepSeek-V3 (81%) and Herald (81.3%), covering 60k+ NL-FL pairs across 6 math topics. Entirely domain-agnostic. Noted as ICML 2025 AI4Math Workshop paper (not main conference). Added to inspired_by as strong domain-agnostic baseline raising the bar for our approach to demonstrate semantic correctness gains beyond syntactic compilation.",
    "round7_issue_4_venue_timeline_fixes": "RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly 'INFEASIBLE for full pipeline given minimum 11-week auto_research timeline' (~8 weeks available), with explicit description of what a partial submission could target (error taxonomy Stage 1 + initial retrieval Stage 2, without full LoRA fine-tuning and ablation suite). ICML 2026 AI4Math Workshop updated to note paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable."
  },
  "change_type": "minor"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b085090-d710-47af-ade5-5eb34349b9f2",
  "isSidechain": false,
  "requestId": "req_011CbV97L5AaRSBjR1X8MK38",
  "type": "assistant",
  "uuid": "65052923-3a74-4879-aaa5-3ea59512962e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVeyK1BSwAJUaFb7q73xXk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15489,
      "cache_read_input_tokens": 39413,
      "output_tokens": 13692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15489,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 13692,
          "cache_read_input_tokens": 39413,
          "cache_creation_input_tokens": 15489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15489
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

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "65052923-3a74-4879-aaa5-3ea59512962e",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "65052923-3a74-4879-aaa5-3ea59512962e",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise domain-adaptive autoformalization proposal for ICLR 2027",
  "sessionId": "481f3ec1-3c98-476a-9097-7a4273796126"
}
```

---
