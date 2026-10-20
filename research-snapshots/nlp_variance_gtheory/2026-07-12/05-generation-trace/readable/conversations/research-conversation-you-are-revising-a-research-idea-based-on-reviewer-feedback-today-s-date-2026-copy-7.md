# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/e0f07656-055b-4ad5-8b1d-9650b6980db5.jsonl`
- **Structured JSON:** [`530591e82775a80141a0.json`](../../sessions/53/530591e82775a80141a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T15:44:23.572Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T15:44:23.572Z",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\",\n  \"core_problem\": \"Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?\",\n  \"opportunity\": \"Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\",\n  \"landscape\": \"Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain; notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).\",\n  \"inspired_by\": \"Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain — Shebzukhov (2026) shows domain-stratified aggregate scores but no domain-stratified error type analysis exists), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%–38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.\",\n  \"approach\": \"We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL→Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)\",\n      \"timeline\": \"17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)\",\n      \"estimated_gpu_cost\": \"$500 (H100 at ~$2.50/hr average via RunPod/Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200 H100-hours\",\n      \"timeline\": \"13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)\",\n      \"claude_api_cost\": \"$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)\",\n      \"estimated_gpu_cost\": \"$500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)\",\n      \"timeline\": \"11 weeks\",\n      \"claude_api_cost\": \"$450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500\",\n      \"speed_bottleneck\": \"Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)\",\n    \"AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only ~8 weeks from today; INFEASIBLE for full pipeline given minimum 11-week auto_research timeline. A partial submission targeting error taxonomy (Stage 1) + initial domain-conditioned retrieval results (Stage 2) without full Stage 3 LoRA fine-tuning and ablation suite could be viable if Stage 1 yields strong early results within the first 6 weeks, but this requires aggressive prioritization and would omit key ablations)\",\n    \"NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)\",\n    \"ICML 2026 AI4Math Workshop — paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); paper submission is no longer possible. Only challenge track participation remains viable: ShadowBench Track 4 (challenge deadline Jun 15, 2026) for complementary multi-domain evaluation; FormalRx Track 1 (challenge deadline Jun 15, 2026) to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\",\n    \"Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\",\n    \"Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)\",\n    \"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\",\n    \"Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\",\n    \"M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\",\n    \"Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\",\n    \"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\",\n    \"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\",\n    \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)\",\n    \"ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\",\n    \"FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\"\n  ],\n  \"description\": \"We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\",\n  \"project_name\": \"domain_adapt_autoformal\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_compute_budget\": \"RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.\",\n    \"round1_issue_2_venue_mismatch\": \"RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.\",\n    \"round1_issue_3_model_choice\": \"RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.\",\n    \"round1_issue_4_FineLeanCorpus\": \"RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.\",\n    \"round1_issue_5_MSC180\": \"RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.\",\n    \"round1_issue_6_circular_reasoning\": \"RESOLVED (Round 1): Error pattern claims reframed as hypotheses.\",\n    \"round1_issue_7_VeriSoftBench\": \"RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.\",\n    \"round1_issue_8_pipeline_complexity\": \"RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.\",\n    \"round1_issue_9_baseline_fear_test\": \"RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.\",\n    \"round2_issue_1_CRAMF_differentiation\": \"RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.\",\n    \"round2_issue_2_SITA\": \"RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.\",\n    \"round2_issue_3_impact_argument\": \"RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.\",\n    \"round2_issue_4_FineLeanCorpus_size\": \"RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.\",\n    \"round2_issue_5_ICLR2027_deadline\": \"MITIGATED (Round 2): Estimated Sep 19/24 with contingency.\",\n    \"round2_issue_6_M2F_RepoProver\": \"RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.\",\n    \"round3_issue_1_DRIFT_Aria\": \"RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.\",\n    \"round3_issue_2_ConNF_claim\": \"RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across ≥5 categories.'\",\n    \"round3_issue_3_error_taxonomy_elevation\": \"RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.\",\n    \"round3_issue_4_compute_trim\": \"RESOLVED: All three modes ≤200 H100-hours.\",\n    \"round3_issue_5_LeanSearch_v2\": \"RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).\",\n    \"round4_issue_1_IndiMathBench\": \"RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).\",\n    \"round4_issue_2_quantitative_hypotheses\": \"RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.\",\n    \"round4_issue_3_model_architecture\": \"RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.\",\n    \"round5_issue_1_IndiMathBench_citation\": \"RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.\",\n    \"round5_issue_2_BEq_correction\": \"RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.\",\n    \"round5_issue_3_ShadowBench\": \"RESOLVED: Added ShadowBench and SCI Error Taxonomy.\",\n    \"round5_issue_4_Mensfelt_framework\": \"RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.\",\n    \"round5_issue_5_landscape_condensation\": \"RESOLVED: Condensed landscape to argument-driven organization.\",\n    \"round6_issue_1_cycle_consistency_paper\": \"RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout. Narrowed ALL novelty claims to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES distribute across subdomains.'\",\n    \"round6_issue_2_ShadowBench_SCI_conflation\": \"RESOLVED: Separated Track 1 (FormalRx) from Track 4 (ShadowBench) throughout.\",\n    \"round6_issue_3_Herald_data_engineering\": \"RESOLVED: Acknowledged Herald's limited schema; APRIL as primary domain signal.\",\n    \"round7_issue_1_APRIL_error_type_field\": \"RESOLVED: Acknowledged APRIL's existing 'error_type' field (mutation categories: lme, mlme, thme, tme) and 'error' field (raw Lean compiler messages) throughout core_problem, opportunity, landscape, approach, inspired_by, and description. Clarified that our error taxonomy contribution is a domain-stratified cross-tabulation of APRIL's existing error_type categories PLUS a finer-grained taxonomy extracted from the raw 'error' field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the 'path' field. The novelty is explicitly stated as being in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. This prevents overclaiming while preserving the genuine novelty of domain-stratified error analysis.\",\n    \"round7_issue_2_LeanPremise_LeanHammer\": \"RESOLVED: Added LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Characterized as first end-to-end domain-general hammer for Lean with 82M-param neural premise selector, 79.4% relative proof rate OOD on miniCTX-v2 (20.7% absolute vs. 26.1% upper bound), significant project variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), dynamic user-context adaptation. Explicitly differentiated: targets premise selection for tactic-based proving (not autoformalization retrieval); uses no mathematical subdomain conditioning; outperforms ReProver (218M). Its project-level variation provides additional evidence of domain-dependent difficulty in the Lean ecosystem.\",\n    \"round7_issue_3_KELPS\": \"RESOLVED: Added KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) to opportunity, landscape, inspired_by, description, and key_references. Characterized as achieving 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations intermediate representation (NL → KE → Lean/Coq/Isabelle), outperforming DeepSeek-V3 (81%) and Herald (81.3%), covering 60k+ NL-FL pairs across 6 math topics. Entirely domain-agnostic. Noted as ICML 2025 AI4Math Workshop paper (not main conference). Added to inspired_by as strong domain-agnostic baseline raising the bar for our approach to demonstrate semantic correctness gains beyond syntactic compilation.\",\n    \"round7_issue_4_venue_timeline_fixes\": \"RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly 'INFEASIBLE for full pipeline given minimum 11-week auto_research timeline' (~8 weeks available), with explicit description of what a partial submission could target (error taxonomy Stage 1 + initial retrieval Stage 2, without full LoRA fine-tuning and ablation suite). ICML 2026 AI4Math Workshop updated to note paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable.\"\n  }\n}\n\n## Reviewer feedback (round 9)\nIssues: [\"MINOR (REPEATED from Round 8): Goedel-Formalizer-V2-8B still described as 'current SOTA open-source formalizer at this scale' in the approach section — verified factually incorrect: StepFun-Formalizer-7B achieves 25.1% BEq@1 on ProverBench vs. Goedel-V2-8B's 16.3%; on Omni-MATH 300, Goedel-V2-8B ties with Kimina-8B at 161/300. Must be changed to 'competitive open-source formalizer' or 'among the leading open-source formalizers'.\", \"MINOR (REPEATED from Round 8): 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) still not cited — its semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction) operates at the post-compilation semantic layer, complementary to the proposal's pre-compilation compiler-error taxonomy. Citing it strengthens the argument that error characterization is under-explored at BOTH layers of the formalization stack.\", \"MINOR (REPEATED from Round 8): CAM-Bench (arXiv 2605.17255, May 2026) — 1,000 Lean proof targets across optimization, numerical linear algebra, numerical analysis — still not cited. Concurrent domain-specific benchmark supporting the motivation that domain-specific evaluation matters.\", \"MINOR: Impact argument for domain-conditioned retrieval over static context remains insufficiently developed — the proposal mentions one example ('a number theory problem may require analysis-level typeclasses') but Round 8 feedback specifically requested articulation of multiple scenarios (cross-domain problems, ambiguous domain assignment, retrieval precision degradation at higher K values). These additional scenarios would strengthen the case that the full pipeline adds meaningful value over IndiMathBench-style static context.\"]\nFeedback: This is Round 9 of 10 — Round 10 requires a final pass/fail decision. The proposal is very close to the pass threshold (avg 3.75/5.0) but three Round 8 issues were not addressed, preventing score improvement. All remaining issues are trivial fixes: (1) **Change ONE phrase**: 'current SOTA open-source formalizer at this scale' → 'a competitive open-source formalizer at this scale, chosen for its Lean4-specific training' — this is a 5-word edit fixing a factual error. (2) **Add TWO sentences** citing 'Do LLMs Game Formalization?' (arXiv 2604.19459) and CAM-Bench (arXiv 2605.17255) — the first provides a complementary post-compilation error taxonomy (fabrication, mistranslation, omission, contradiction) that together with your pre-compilation taxonomy demonstrates error characterization is under-explored at multiple layers; the second is a concurrent domain-specific benchmark validating community interest. (3) **Add 2-3 sentences** to the approach articulating specific scenarios where dynamic domain conditioning outperforms static context: (a) cross-domain problems where a number theory result depends on analysis-level typeclasses and needs retrieval from multiple Mathlib modules, (b) problems at domain boundaries where the correct subdomain classification is ambiguous and static context picks the wrong category, (c) retrieval precision at K=20+ where domain filtering reduces noise that static context cannot address. These three fixes are collectively ~150 words of text changes. Without them, the proposal will likely receive a borderline-fail in Round 10 due to persistent factual inaccuracy and insufficient impact argumentation.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 9 轮修订，近 3 轮平均分从 3.8 到 3.8，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T15:44:23.575Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T15:44:23.575Z",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-28T15:44:23.587Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
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
  }
}

## Reviewer feedback (round 9)
Issues: ["MINOR (REPEATED from Round 8): Goedel-Formalizer-V2-8B still described as 'current SOTA open-source formalizer at this scale' in the approach section — verified factually incorrect: StepFun-Formalizer-7B achieves 25.1% BEq@1 on ProverBench vs. Goedel-V2-8B's 16.3%; on Omni-MATH 300, Goedel-V2-8B ties with Kimina-8B at 161/300. Must be changed to 'competitive open-source formalizer' or 'among the leading open-source formalizers'.", "MINOR (REPEATED from Round 8): 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) still not cited — its semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction) operates at the post-compilation semantic layer, complementary to the proposal's pre-compilation compiler-error taxonomy. Citing it strengthens the argument that error characterization is under-explored at BOTH layers of the formalization stack.", "MINOR (REPEATED from Round 8): CAM-Bench (arXiv 2605.17255, May 2026) — 1,000 Lean proof targets across optimization, numerical linear algebra, numerical analysis — still not cited. Concurrent domain-specific benchmark supporting the motivation that domain-specific evaluation matters.", "MINOR: Impact argument for domain-conditioned retrieval over static context remains insufficiently developed — the proposal mentions one example ('a number theory problem may require analysis-level typeclasses') but Round 8 feedback specifically requested articulation of multiple scenarios (cross-domain problems, ambiguous domain assignment, retrieval precision degradation at higher K values). These additional scenarios would strengthen the case that the full pipeline adds meaningful value over IndiMathBench-style static context."]
Feedback: This is Round 9 of 10 — Round 10 requires a final pass/fail decision. The proposal is very close to the pass threshold (avg 3.75/5.0) but three Round 8 issues were not addressed, preventing score improvement. All remaining issues are trivial fixes: (1) **Change ONE phrase**: 'current SOTA open-source formalizer at this scale' → 'a competitive open-source formalizer at this scale, chosen for its Lean4-specific training' — this is a 5-word edit fixing a factual error. (2) **Add TWO sentences** citing 'Do LLMs Game Formalization?' (arXiv 2604.19459) and CAM-Bench (arXiv 2605.17255) — the first provides a complementary post-compilation error taxonomy (fabrication, mistranslation, omission, contradiction) that together with your pre-compilation taxonomy demonstrates error characterization is under-explored at multiple layers; the second is a concurrent domain-specific benchmark validating community interest. (3) **Add 2-3 sentences** to the approach articulating specific scenarios where dynamic domain conditioning outperforms static context: (a) cross-domain problems where a number theory result depends on analysis-level typeclasses and needs retrieval from multiple Mathlib modules, (b) problems at domain boundaries where the correct subdomain classification is ambiguous and static context picks the wrong category, (c) retrieval precision at K=20+ where domain filtering reduces noise that static context cannot address. These three fixes are collectively ~150 words of text changes. Without them, the proposal will likely receive a borderline-fail in Round 10 due to persistent factual inaccuracy and insufficient impact argumentation.

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
经过 9 轮修订，近 3 轮平均分从 3.8 到 3.8，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "c03f4cb3-1f93-445d-8350-76bbe1cc1ec6",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T15:44:23.585Z_

```json
{
  "parentUuid": "c03f4cb3-1f93-445d-8350-76bbe1cc1ec6",
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
  "uuid": "96fb8d15-14f7-4093-a1e1-3c8a8398154c",
  "timestamp": "2026-05-28T15:44:23.585Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T15:44:23.585Z_

```json
{
  "parentUuid": "96fb8d15-14f7-4093-a1e1-3c8a8398154c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "587565a7-c084-448b-b086-4ef5a8487b30",
  "timestamp": "2026-05-28T15:44:23.585Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
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
  "leafUuid": "587565a7-c084-448b-b086-4ef5a8487b30",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Assistant

_source line 8 · 2026-05-28T15:44:34.051Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. This is Round 9 of 10, and the reviewer has been very specific about what needs to be fixed:

1. **Factual error**: Goedel-Formalizer-V2-8B described as "current SOTA" when StepFun-Formalizer-7B outperforms it
2. **Missing citation**: "Do LLMs Game Formalization?" (arXiv 2604.19459) - semantic faithfulness taxonomy


3. **Missing citation**: CAM-Bench (arXiv 2605.17255) - domain-specific benchmark
4. **Impact argument**: Need more scenarios for dynamic vs. static domain conditioning

The reviewer frames these as straightforward fixes totaling around 150 words, and the proposal sits at 3.75/5.0—close enough to passing that a focused revision makes sense. Despite the warning about stagnation, the feedback actually points toward a clear path forward rather than a fundamental rethinking. Pivoting now would waste the progress already made.

I should track down those two papers and apply the targeted corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587565a7-c084-448b-b086-4ef5a8487b30",
  "isSidechain": false,
  "requestId": "req_011CbVDygEUQ2AWC76fVuU7n",
  "type": "assistant",
  "uuid": "195b1c3f-445d-478b-9a79-2b520efa6389",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUvnNb6RRmuptEeaqXeub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15388,
      "cache_read_input_tokens": 11014,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 425,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15388
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

_source line 9 · 2026-05-28T15:44:34.053Z_

I need to address 4 specific issues the reviewer flagged (3 repeated from Round 8). Let me research the two papers that need citing, then make all fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "195b1c3f-445d-478b-9a79-2b520efa6389",
  "isSidechain": false,
  "requestId": "req_011CbVDygEUQ2AWC76fVuU7n",
  "type": "assistant",
  "uuid": "f0a14847-a8e9-40b5-b6c5-7cde9c07b929",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUvnNb6RRmuptEeaqXeub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15388,
      "cache_read_input_tokens": 11014,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 425,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15388
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

_source line 10 · 2026-05-28T15:44:34.061Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E2RbSESBZxvUcGRVgAGUFy`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a14847-a8e9-40b5-b6c5-7cde9c07b929",
  "isSidechain": false,
  "requestId": "req_011CbVDygEUQ2AWC76fVuU7n",
  "type": "assistant",
  "uuid": "6d268750-5785-40b9-929e-9fefeba93294",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NiUvnNb6RRmuptEeaqXeub",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15388,
      "cache_read_input_tokens": 11014,
      "output_tokens": 425,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 425,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15388
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

_source line 11 · 2026-05-28T15:44:34.067Z_

<details><summary>↩ Tool result · `toolu_01E2RbSESBZxvUcGRVgAGUFy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d268750-5785-40b9-929e-9fefeba93294",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "ca7e05f6-a79a-4c18-8354-7dbac5c00c3a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6d268750-5785-40b9-929e-9fefeba93294",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T15:44:37.034Z_

<details><summary>Logged reasoning block</summary>

```text
Let me research the two papers that need to be cited, and also verify the StepFun-Formalizer vs Goedel-V2 comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca7e05f6-a79a-4c18-8354-7dbac5c00c3a",
  "isSidechain": false,
  "requestId": "req_011CbVDzTvap7Zd1qfPXFvLv",
  "type": "assistant",
  "uuid": "15f08703-8c6e-4780-8b59-aa5d92bed4a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDzhLqwAqXdaUwF7zwyLt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 26402,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26402,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1444
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

_source line 13 · 2026-05-28T15:44:37.608Z_

Let me research all three items in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15f08703-8c6e-4780-8b59-aa5d92bed4a5",
  "isSidechain": false,
  "requestId": "req_011CbVDzTvap7Zd1qfPXFvLv",
  "type": "assistant",
  "uuid": "85166b3a-a4f3-4355-a1ff-0ac5fd357efa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDzhLqwAqXdaUwF7zwyLt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 26402,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26402,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1444
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

_source line 14 · 2026-05-28T15:44:38.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E69L6TxdhtUmpgTXwhe3HX`</summary>

```json
{
  "query": "arXiv 2604.19459 \"Do LLMs Game Formalization\" semantic faithfulness taxonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85166b3a-a4f3-4355-a1ff-0ac5fd357efa",
  "isSidechain": false,
  "requestId": "req_011CbVDzTvap7Zd1qfPXFvLv",
  "type": "assistant",
  "uuid": "551f739f-695e-4841-b262-3c5b68aee937",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JDzhLqwAqXdaUwF7zwyLt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 26402,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26402,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1444
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

_source line 15 · 2026-05-28T15:44:46.628Z_

<details><summary>↩ Tool result · `toolu_01E69L6TxdhtUmpgTXwhe3HX`</summary>

```text
Web search results for query: "arXiv 2604.19459 "Do LLMs Game Formalization" semantic faithfulness taxonomy"

Links: [{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Language as Mathematical Structure: Examining Semantic Field Theory Against Language Games","url":"https://arxiv.org/html/2601.00448"},{"title":"Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations","url":"https://arxiv.org/html/2512.05156v1"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/pdf/2409.12300"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations","url":"https://arxiv.org/pdf/2504.14150"},{"title":"[2512.05156] Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations","url":"https://arxiv.org/abs/2512.05156"},{"title":"Towards an Agentic LLM-based Approach to Requirement Formalization from Unstructured Specifications","url":"https://arxiv.org/html/2604.18228v1"}]

I found the paper you're looking for! Here's what I found about arXiv 2604.19459:

## Paper Overview

The paper is titled "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" by Kyuhee Kim and 2 other authors.

## Key Concepts

A formalization is faithful if the formal axioms preserve the semantic content of the natural language premises. These properties are independent, and a valid proof may rest on an unfaithful formalization.

The term "formalization gaming" refers to a behavior where models exploit the gap between valid proofs and faithful translations when generating Lean 4 proofs.

## Research Methodology

The researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

## Key Findings

Despite compilation rates of 87-99%, there is no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it. However, the two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "551f739f-695e-4841-b262-3c5b68aee937",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "9f821d3e-95f5-4e37-9ef0-3c994938f49a",
  "toolUseResult": {
    "query": "arXiv 2604.19459 \"Do LLMs Game Formalization\" semantic faithfulness taxonomy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VwEiZmS1t3kZX9kbJ4Vbi3",
        "content": [
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Language as Mathematical Structure: Examining Semantic Field Theory Against Language Games",
            "url": "https://arxiv.org/html/2601.00448"
          },
          {
            "title": "Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations",
            "url": "https://arxiv.org/html/2512.05156v1"
          },
          {
            "title": "Autoformalization of Game Descriptions using Large Language Models",
            "url": "https://arxiv.org/pdf/2409.12300"
          },
          {
            "title": "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/pdf/2511.12784"
          },
          {
            "title": "Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations",
            "url": "https://arxiv.org/pdf/2504.14150"
          },
          {
            "title": "[2512.05156] Semantic Faithfulness and Entropy Production Measures to Tame Your LLM Demons and Manage Hallucinations",
            "url": "https://arxiv.org/abs/2512.05156"
          },
          {
            "title": "Towards an Agentic LLM-based Approach to Requirement Formalization from Unstructured Specifications",
            "url": "https://arxiv.org/html/2604.18228v1"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found about arXiv 2604.19459:\n\n## Paper Overview\n\nThe paper is titled \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\" by Kyuhee Kim and 2 other authors.\n\n## Key Concepts\n\nA formalization is faithful if the formal axioms preserve the semantic content of the natural language premises. These properties are independent, and a valid proof may rest on an unfaithful formalization.\n\nThe term \"formalization gaming\" refers to a behavior where models exploit the gap between valid proofs and faithful translations when generating Lean 4 proofs.\n\n## Research Methodology\n\nThe researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.\n\n## Key Findings\n\nDespite compilation rates of 87-99%, there is no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it. However, the two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely."
    ],
    "durationSeconds": 8.509294614000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "551f739f-695e-4841-b262-3c5b68aee937",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T15:44:49.020Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RLwaoPGuboFCdbTnd4eHMh`</summary>

```json
{
  "query": "arXiv 2605.17255 CAM-Bench Lean proof optimization numerical linear algebra"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f821d3e-95f5-4e37-9ef0-3c994938f49a",
  "isSidechain": false,
  "requestId": "req_011CbVE1NeMsLWcDzVtk1NDD",
  "type": "assistant",
  "uuid": "93225069-3a66-4653-a4fa-f6d71ce721af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016d6WsbtSTgXjEzvDFWQQtr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 934,
      "cache_read_input_tokens": 27846,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27846,
          "cache_creation_input_tokens": 934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 934
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

_source line 17 · 2026-05-28T15:44:55.433Z_

<details><summary>↩ Tool result · `toolu_01RLwaoPGuboFCdbTnd4eHMh`</summary>

```text
Web search results for query: "arXiv 2605.17255 CAM-Bench Lean proof optimization numerical linear algebra"

Links: [{"title":"[2605.17255] CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/abs/2605.17255"},{"title":"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/html/2605.17255"},{"title":"ProofOptimizer: Training Language Models to Simplify Proofs without Human Demonstrations","url":"https://arxiv.org/pdf/2510.15700"},{"title":"Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4","url":"https://arxiv.org/html/2602.01291"},{"title":"Armadillo: An Efficient Framework for Numerical Linear Algebra","url":"https://arxiv.org/pdf/2502.03000"},{"title":"Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"}]

Based on the search results, here's what I found about arXiv paper 2605.17255:

CAM-Bench is a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis.

The benchmark addresses a gap in existing benchmarks that mainly focus on Olympiad-style problems and algebraic domains, leaving computational and applied mathematics underrepresented.

The problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, the authors developed a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully, and then normalizes each problem into a standalone informal theorem and translates it into a Lean target.

The paper was published on May 17, 2026, and the authors are from Fudan University, Qingdao University, Peking University, and Huawei Technologies Ltd. The benchmark is open-sourced on GitHub at https://github.com/optpku/CAM-Bench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93225069-3a66-4653-a4fa-f6d71ce721af",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "82dc033e-02bf-4625-bde3-e8342543453a",
  "toolUseResult": {
    "query": "arXiv 2605.17255 CAM-Bench Lean proof optimization numerical linear algebra",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WQ7S3KS6jQrSzdtZtwruDA",
        "content": [
          {
            "title": "[2605.17255] CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean",
            "url": "https://arxiv.org/abs/2605.17255"
          },
          {
            "title": "CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean",
            "url": "https://arxiv.org/html/2605.17255"
          },
          {
            "title": "ProofOptimizer: Training Language Models to Simplify Proofs without Human Demonstrations",
            "url": "https://arxiv.org/pdf/2510.15700"
          },
          {
            "title": "Construction–Verification: A Benchmark for Formalizing Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/html/2602.01291"
          },
          {
            "title": "Armadillo: An Efficient Framework for Numerical Linear Algebra",
            "url": "https://arxiv.org/pdf/2502.03000"
          },
          {
            "title": "Construction-Verification: A Benchmark for Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/pdf/2602.01291"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2605.17255:\n\nCAM-Bench is a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis.\n\nThe benchmark addresses a gap in existing benchmarks that mainly focus on Olympiad-style problems and algebraic domains, leaving computational and applied mathematics underrepresented.\n\nThe problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, the authors developed a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully, and then normalizes each problem into a standalone informal theorem and translates it into a Lean target.\n\nThe paper was published on May 17, 2026, and the authors are from Fudan University, Qingdao University, Peking University, and Huawei Technologies Ltd. The benchmark is open-sourced on GitHub at https://github.com/optpku/CAM-Bench."
    ],
    "durationSeconds": 6.409253260000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "93225069-3a66-4653-a4fa-f6d71ce721af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T15:44:59.717Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FSk5MSuBoJ8HVsq3FTjaEB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.19459",
  "prompt": "Extract: (1) full title, (2) all authors, (3) venue/workshop if mentioned, (4) the exact error taxonomy categories (fabrication, mistranslation, omission, contradiction - confirm which ones), (5) what datasets/benchmarks used, (6) key quantitative results about unfaithfulness rates, (7) whether it targets Lean specifically or FOL generally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82dc033e-02bf-4625-bde3-e8342543453a",
  "isSidechain": false,
  "requestId": "req_011CbVE22EJstFUGkbccPXfh",
  "type": "assistant",
  "uuid": "c8bcd7ba-b6d5-452b-9f52-c7ec6888572b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018C9aNDWNdDXTdXascpzwau",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 28780,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 634,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 28780,
          "cache_creation_input_tokens": 634,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 634
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

_source line 19 · 2026-05-28T15:45:04.763Z_

<details><summary>↩ Tool result · `toolu_01FSk5MSuBoJ8HVsq3FTjaEB`</summary>

```text
# Research Paper Summary

**(1) Full Title:**
"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"

**(2) All Authors:**
Kyuhee Kim, Auguste Poiroux, Antoine Bosselut

**(3) Venue/Workshop:**
VerifAI-2 Workshop, ICLR 2026 (non-archival)

**(4) Error Taxonomy Categories:**
The abstract explicitly identifies two modes of unfaithfulness:
- **Fabrication**: "GPT-5 fabricates axioms during proof generation"
- **Mistranslation**: "DeepSeek-R1 mistranslates premises during formalization"

The paper does not mention omission or contradiction as formal error categories.

**(5) Datasets/Benchmarks:**
303 first-order logic problems total:
- 203 from FOLIO
- 100 from Multi-LogiEval

**(6) Key Quantitative Results:**
Despite "compilation rates of 87-99%," the study reveals substantial unfaithfulness that compilation success masks. The two-stage pipeline approach distinguished distinct failure modes between models, though specific unfaithfulness percentages are not provided in this abstract.

**(7) Scope:**
The research targets both Lean 4 proofs specifically (the formalization language) and first-order logic problems generally, studying how models translate natural language reasoning into formal systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8bcd7ba-b6d5-452b-9f52-c7ec6888572b",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "5ce592fa-c424-4cd2-a0b7-28ab327e1d9d",
  "toolUseResult": {
    "bytes": 47382,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Summary\n\n**(1) Full Title:**\n\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n\n**(2) All Authors:**\nKyuhee Kim, Auguste Poiroux, Antoine Bosselut\n\n**(3) Venue/Workshop:**\nVerifAI-2 Workshop, ICLR 2026 (non-archival)\n\n**(4) Error Taxonomy Categories:**\nThe abstract explicitly identifies two modes of unfaithfulness:\n- **Fabrication**: \"GPT-5 fabricates axioms during proof generation\"\n- **Mistranslation**: \"DeepSeek-R1 mistranslates premises during formalization\"\n\nThe paper does not mention omission or contradiction as formal error categories.\n\n**(5) Datasets/Benchmarks:**\n303 first-order logic problems total:\n- 203 from FOLIO\n- 100 from Multi-LogiEval\n\n**(6) Key Quantitative Results:**\nDespite \"compilation rates of 87-99%,\" the study reveals substantial unfaithfulness that compilation success masks. The two-stage pipeline approach distinguished distinct failure modes between models, though specific unfaithfulness percentages are not provided in this abstract.\n\n**(7) Scope:**\nThe research targets both Lean 4 proofs specifically (the formalization language) and first-order logic problems generally, studying how models translate natural language reasoning into formal systems.",
    "durationMs": 5042,
    "url": "https://arxiv.org/abs/2604.19459"
  },
  "sourceToolAssistantUUID": "c8bcd7ba-b6d5-452b-9f52-c7ec6888572b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T15:45:09.924Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DojAkAr89dXWRj6XMzCYFo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.17255",
  "prompt": "Extract: (1) full title, (2) all authors, (3) number of proof targets, (4) exact mathematical domains covered (optimization, numerical linear algebra, numerical analysis - any others?), (5) key findings about domain-specific difficulty or performance variation, (6) whether any autoformalization is involved, (7) any comparison with existing benchmarks like MiniF2F or FormalMATH"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce592fa-c424-4cd2-a0b7-28ab327e1d9d",
  "isSidechain": false,
  "requestId": "req_011CbVE2iCczKuYiBCxB1BGr",
  "type": "assistant",
  "uuid": "eed4c172-14a2-4ed7-9b71-b9ab33d6bb34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgZUeWdaKGxynFDaTxMDHj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 513,
      "cache_read_input_tokens": 29414,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 171,
          "cache_read_input_tokens": 29414,
          "cache_creation_input_tokens": 513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 513
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

_source line 21 · 2026-05-28T15:45:14.593Z_

<details><summary>↩ Tool result · `toolu_01DojAkAr89dXWRj6XMzCYFo`</summary>

```text
# CAM-Bench Paper Extraction

**(1) Full Title:**
"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean"

**(2) All Authors:**
Wentao Long, Yunfei Zhang, Chenyi Li, Li Zhou, Chumin Sun, Zaiwen Wen

**(3) Number of Proof Targets:**
1,000 Lean proof targets

**(4) Mathematical Domains Covered:**
The abstract specifies three domains:
- Optimization
- Numerical linear algebra
- Numerical analysis

No additional domains are mentioned in the provided content.

**(5) Key Findings on Domain-Specific Difficulty:**
The abstract identifies "common failure modes in tracking local assumptions, applying elementary results, decomposing proofs, and maintaining long-horizon control in Lean," but does not provide specific performance metrics or domain-specific difficulty comparisons in the visible content.

**(6) Autoformalization Involvement:**
Yes. The paper describes "a dependency-recovery pipeline that reconstructs the local textbook context" and translates problems into Lean targets, representing an autoformalization workflow from textbook exercises.

**(7) Comparison with Existing Benchmarks:**
The abstract states: "CAM-Bench complements existing formal mathematics benchmarks by targeting applied mathematics problems," but no explicit comparisons with MiniF2F or FormalMATH appear in the provided excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed4c172-14a2-4ed7-9b71-b9ab33d6bb34",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "f900d9d2-8054-4dd4-a068-7d2f7dc57e46",
  "toolUseResult": {
    "bytes": 48045,
    "code": 200,
    "codeText": "OK",
    "result": "# CAM-Bench Paper Extraction\n\n**(1) Full Title:**\n\"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean\"\n\n**(2) All Authors:**\nWentao Long, Yunfei Zhang, Chenyi Li, Li Zhou, Chumin Sun, Zaiwen Wen\n\n**(3) Number of Proof Targets:**\n1,000 Lean proof targets\n\n**(4) Mathematical Domains Covered:**\nThe abstract specifies three domains:\n- Optimization\n- Numerical linear algebra\n- Numerical analysis\n\nNo additional domains are mentioned in the provided content.\n\n**(5) Key Findings on Domain-Specific Difficulty:**\nThe abstract identifies \"common failure modes in tracking local assumptions, applying elementary results, decomposing proofs, and maintaining long-horizon control in Lean,\" but does not provide specific performance metrics or domain-specific difficulty comparisons in the visible content.\n\n**(6) Autoformalization Involvement:**\nYes. The paper describes \"a dependency-recovery pipeline that reconstructs the local textbook context\" and translates problems into Lean targets, representing an autoformalization workflow from textbook exercises.\n\n**(7) Comparison with Existing Benchmarks:**\nThe abstract states: \"CAM-Bench complements existing formal mathematics benchmarks by targeting applied mathematics problems,\" but no explicit comparisons with MiniF2F or FormalMATH appear in the provided excerpt.",
    "durationMs": 4666,
    "url": "https://arxiv.org/abs/2605.17255"
  },
  "sourceToolAssistantUUID": "eed4c172-14a2-4ed7-9b71-b9ab33d6bb34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
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
  "leafUuid": "f900d9d2-8054-4dd4-a068-7d2f7dc57e46",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Tool call

_source line 24 · 2026-05-28T15:45:19.758Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ChoWA5PTQLrBCSeViagk5N`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.19459",
  "prompt": "I need the FULL error taxonomy from this paper. The reviewer mentioned: fabrication, mistranslation, omission, contradiction. Find ALL categories of semantic unfaithfulness they identify. Also extract: (1) any quantitative rates for each error type, (2) whether they discuss Lean4 or just FOL, (3) what they say about the gap between compilation success and semantic correctness, (4) any connection to autoformalization vs. theorem proving"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f900d9d2-8054-4dd4-a068-7d2f7dc57e46",
  "isSidechain": false,
  "requestId": "req_011CbVE3SBVXrgwezVt2gQLM",
  "type": "assistant",
  "uuid": "43cddc20-1122-4ec3-99c6-8a525a8b7af1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETBhcmAmSYTbY7xT95SSj5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 29927,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 509,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 29927,
          "cache_creation_input_tokens": 509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 509
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

_source line 25 · 2026-05-28T15:45:28.430Z_

<details><summary>↩ Tool result · `toolu_01ChoWA5PTQLrBCSeViagk5N`</summary>

```text
# Error Taxonomy & Semantic Unfaithfulness Analysis

## Complete Error Taxonomy

The paper identifies **four main categories** of errors (Table 1):

### 1. **Mistranslation** (8 subcategories)
- Wrong connective, negation, quantifier, direction, scope
- Wrong predicate, entity, argument order

### 2. **Fabrication** (2 subcategories)
- Fabricated axiom (unstated information)
- Conclusion as axiom (goal directly axiomatized)

### 3. **Omission** (2 subcategories)
- Missing axiom (premise not formalized)
- Dropped antecedent (conditional condition omitted)

### 4. **Contradiction**
- Induced contradiction enabling proof by explosion

---

## Key Quantitative Findings

**Unified Generation (Baseline):** 
- 77% of prediction errors used *faithful* formalization
- Only ~3% directional divergence (after dataset filtering)
- Unfaithful errors among prediction errors: 4 FOLIO, 17 Multi-LogiEval cases

**Two-Stage Pipeline:**
- GPT-5 fabricated axioms in 107 cases; DeepSeek-R1 in only 3
- "Conclusion as axiom dominates (59 cases)" of GPT-5's fabrications
- 56.2% were conclusion-as-axiom; 16.2% world knowledge; 12.4% invented

---

## Formalization vs. Proving

The paper uses **Lean 4** specifically. They define the critical gap: "A proof is *valid* if it type-checks in Lean's kernel. A formalization is *faithful* if the formal axioms preserve the semantic content of the natural language premises. These properties are independent."

**Central thesis:** Despite 87–99% compilation rates, "high compilation rates or accuracies should not be equated with faithful reasoning."

---

## Autoformalization-Proving Distinction

The paper separates tasks explicitly:
- **Stage 1:** Autoformalization (NL→formal axioms)
- **Stage 2:** Theorem proving (axiom system→proof)

**Finding:** Models fail differently. GPT-5 preserves faithful formalizations but *compensates with axiom fabrication during proving*. DeepSeek-R1 embeds unfaithfulness at the *formalization stage itself*, producing "internally consistent outputs that evade detection entirely."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43cddc20-1122-4ec3-99c6-8a525a8b7af1",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "b67fa119-ee1c-42ca-a0d4-7717abf4c04a",
  "toolUseResult": {
    "bytes": 399886,
    "code": 200,
    "codeText": "OK",
    "result": "# Error Taxonomy & Semantic Unfaithfulness Analysis\n\n## Complete Error Taxonomy\n\nThe paper identifies **four main categories** of errors (Table 1):\n\n### 1. **Mistranslation** (8 subcategories)\n- Wrong connective, negation, quantifier, direction, scope\n- Wrong predicate, entity, argument order\n\n### 2. **Fabrication** (2 subcategories)\n- Fabricated axiom (unstated information)\n- Conclusion as axiom (goal directly axiomatized)\n\n### 3. **Omission** (2 subcategories)\n- Missing axiom (premise not formalized)\n- Dropped antecedent (conditional condition omitted)\n\n### 4. **Contradiction**\n- Induced contradiction enabling proof by explosion\n\n---\n\n## Key Quantitative Findings\n\n**Unified Generation (Baseline):** \n- 77% of prediction errors used *faithful* formalization\n- Only ~3% directional divergence (after dataset filtering)\n- Unfaithful errors among prediction errors: 4 FOLIO, 17 Multi-LogiEval cases\n\n**Two-Stage Pipeline:**\n- GPT-5 fabricated axioms in 107 cases; DeepSeek-R1 in only 3\n- \"Conclusion as axiom dominates (59 cases)\" of GPT-5's fabrications\n- 56.2% were conclusion-as-axiom; 16.2% world knowledge; 12.4% invented\n\n---\n\n## Formalization vs. Proving\n\nThe paper uses **Lean 4** specifically. They define the critical gap: \"A proof is *valid* if it type-checks in Lean's kernel. A formalization is *faithful* if the formal axioms preserve the semantic content of the natural language premises. These properties are independent.\"\n\n**Central thesis:** Despite 87–99% compilation rates, \"high compilation rates or accuracies should not be equated with faithful reasoning.\"\n\n---\n\n## Autoformalization-Proving Distinction\n\nThe paper separates tasks explicitly:\n- **Stage 1:** Autoformalization (NL→formal axioms)\n- **Stage 2:** Theorem proving (axiom system→proof)\n\n**Finding:** Models fail differently. GPT-5 preserves faithful formalizations but *compensates with axiom fabrication during proving*. DeepSeek-R1 embeds unfaithfulness at the *formalization stage itself*, producing \"internally consistent outputs that evade detection entirely.\"",
    "durationMs": 8667,
    "url": "https://arxiv.org/html/2604.19459"
  },
  "sourceToolAssistantUUID": "43cddc20-1122-4ec3-99c6-8a525a8b7af1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T15:45:31.855Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also verify the StepFun-Formalizer vs Goedel-V2 claim to make sure the factual correction is accurate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b67fa119-ee1c-42ca-a0d4-7717abf4c04a",
  "isSidechain": false,
  "requestId": "req_011CbVE4TMDZwRkVueYYTaMm",
  "type": "assistant",
  "uuid": "c5a865a7-7c8c-4ff2-ad13-5b4a5057d960",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvTPcVsenttwTu5HsBjK9M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 30436,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 27 · 2026-05-28T15:45:32.339Z_

Now let me verify the StepFun-Formalizer vs Goedel-V2 comparison:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5a865a7-7c8c-4ff2-ad13-5b4a5057d960",
  "isSidechain": false,
  "requestId": "req_011CbVE4TMDZwRkVueYYTaMm",
  "type": "assistant",
  "uuid": "5a356bdf-8f1c-40b5-8fdc-73708783df37",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvTPcVsenttwTu5HsBjK9M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 30436,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 28 · 2026-05-28T15:45:33.104Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QbhEogscaJew82p4TjJfQ`</summary>

```json
{
  "query": "StepFun-Formalizer-7B Goedel-Formalizer-V2-8B ProverBench BEq comparison 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a356bdf-8f1c-40b5-8fdc-73708783df37",
  "isSidechain": false,
  "requestId": "req_011CbVE4TMDZwRkVueYYTaMm",
  "type": "assistant",
  "uuid": "4e7e8dca-8afc-40d5-834c-6827bee19dae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvTPcVsenttwTu5HsBjK9M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 30436,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 30436,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 29 · 2026-05-28T15:45:39.067Z_

<details><summary>↩ Tool result · `toolu_011QbhEogscaJew82p4TjJfQ`</summary>

```text
Web search results for query: "StepFun-Formalizer-7B Goedel-Formalizer-V2-8B ProverBench BEq comparison 2026"

Links: [{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"stepfun-ai/StepFun-Formalizer-7B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v2"},{"title":"StepFun-Formalizer/README.md at master · stepfun-ai/StepFun-Formalizer","url":"https://github.com/stepfun-ai/StepFun-Formalizer/blob/master/README.md"},{"title":"[2508.04440v1] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440v1"},{"title":"[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440"},{"title":"GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub","url":"https://github.com/stepfun-ai/StepFun-Formalizer"},{"title":"stepfun-ai/StepFun-Formalizer-32B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40691"},{"title":"𝚐𝔪𝟾𝚡𝚡𝟾 on X: \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion ThinkingF pipeline - Formal knowledge distillation: 183K Lean4-aligned pairs via majority voting + BEq filtering - Template-guided reasoning: 5.8K trajectories (Claude 3.7) - https://t.co/9AEztEHWPv\" / X","url":"https://x.com/gm8xx8/status/1953483273985757559"}]

Based on the search results, I found information about StepFun-Formalizer-7B and its performance on ProverBench with the BEq metric. However, the search results do not contain specific information about Goedel-Formalizer-V2-8B or a direct comparison between these two models.

Here's what I found about the StepFun-Formalizer models:

StepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models. The models use the BEq@k metric to evaluate the models, which is the portion of samples where predicted statements are BEq to ground-truths at least once.

For out-of-distribution evaluation, StepFun-Formalizer uses ProverBench and CombiBench. On ProverBench BEq@1, StepFun-7B scores 25.1% and StepFun-32B scores 26.7%.

Unfortunately, the search results do not contain comparative data between StepFun-Formalizer-7B and Goedel-Formalizer-V2-8B. To get information about that specific comparison, you may need to search for Goedel-Formalizer research papers or documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e7e8dca-8afc-40d5-834c-6827bee19dae",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "f1e28dc0-e364-4255-a8b9-2333ff533d8f",
  "toolUseResult": {
    "query": "StepFun-Formalizer-7B Goedel-Formalizer-V2-8B ProverBench BEq comparison 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CTzh5ncEjiZdfJDGsbH93g",
        "content": [
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential",
            "url": "https://www.arxiv.org/pdf/2508.04440"
          },
          {
            "title": "stepfun-ai/StepFun-Formalizer-7B · Hugging Face",
            "url": "https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/html/2508.04440v2"
          },
          {
            "title": "StepFun-Formalizer/README.md at master · stepfun-ai/StepFun-Formalizer",
            "url": "https://github.com/stepfun-ai/StepFun-Formalizer/blob/master/README.md"
          },
          {
            "title": "[2508.04440v1] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440v1"
          },
          {
            "title": "[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440"
          },
          {
            "title": "GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub",
            "url": "https://github.com/stepfun-ai/StepFun-Formalizer"
          },
          {
            "title": "stepfun-ai/StepFun-Formalizer-32B · Hugging Face",
            "url": "https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40691"
          },
          {
            "title": "𝚐𝔪𝟾𝚡𝚡𝟾 on X: \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion ThinkingF pipeline - Formal knowledge distillation: 183K Lean4-aligned pairs via majority voting + BEq filtering - Template-guided reasoning: 5.8K trajectories (Claude 3.7) - https://t.co/9AEztEHWPv\" / X",
            "url": "https://x.com/gm8xx8/status/1953483273985757559"
          }
        ]
      },
      "Based on the search results, I found information about StepFun-Formalizer-7B and its performance on ProverBench with the BEq metric. However, the search results do not contain specific information about Goedel-Formalizer-V2-8B or a direct comparison between these two models.\n\nHere's what I found about the StepFun-Formalizer models:\n\nStepFun-Formalizer-32B achieves SOTA BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench, surpassing all prior general-purpose and specialized models. The models use the BEq@k metric to evaluate the models, which is the portion of samples where predicted statements are BEq to ground-truths at least once.\n\nFor out-of-distribution evaluation, StepFun-Formalizer uses ProverBench and CombiBench. On ProverBench BEq@1, StepFun-7B scores 25.1% and StepFun-32B scores 26.7%.\n\nUnfortunately, the search results do not contain comparative data between StepFun-Formalizer-7B and Goedel-Formalizer-V2-8B. To get information about that specific comparison, you may need to search for Goedel-Formalizer research papers or documentation directly."
    ],
    "durationSeconds": 5.9576708369999976,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4e7e8dca-8afc-40d5-834c-6827bee19dae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T15:45:39.075Z_

```json
{
  "parentUuid": "f1e28dc0-e364-4255-a8b9-2333ff533d8f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e92bfb64-7471-42af-a1c3-e500abb0f6a2",
  "timestamp": "2026-05-28T15:45:39.075Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-28T15:45:43.602Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0163qRJFFqFLT1KdLC6jPK8M`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.04440v2",
  "prompt": "Find the comparison table showing StepFun-Formalizer-7B vs Goedel-Formalizer-V2-8B performance. I need: (1) ProverBench BEq@1 scores for both models, (2) Omni-MATH 300 scores for both, (3) FormalMATH-Lite scores if available, (4) any other direct comparison between these two models at the 7-8B scale"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e92bfb64-7471-42af-a1c3-e500abb0f6a2",
  "isSidechain": false,
  "requestId": "req_011CbVE5EpvSPes4bmKXCWCv",
  "type": "assistant",
  "uuid": "01d89cb1-38eb-4211-bf96-ae8f7a1064ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuQtRgY9QwuAG2MfsBmh5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 31205,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 31205,
          "cache_creation_input_tokens": 1399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1399
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

_source line 32 · 2026-05-28T15:45:47.459Z_

<details><summary>↩ Tool result · `toolu_0163qRJFFqFLT1KdLC6jPK8M`</summary>

```text
# Performance Comparison: StepFun-Formalizer-7B vs Goedel-Formalizer-V2-8B

Based on the document, here's the direct comparison available:

## ProverBench Results
- **StepFun-Formalizer-7B**: 25.1% BEq@1, 37.9% BEq@16
- **Goedel-Formalizer-V2-8B**: 16.3% BEq@1, 28.7% BEq@16

## CombiBench Results
- **StepFun-Formalizer-7B**: 5.2% BEq@1, 11.0% BEq@16
- **Goedel-Formalizer-V2-8B**: 3.3% BEq@1, 10.0% BEq@16

## Important Caveat

The document notes an evaluation concern: "Goedel-Formalizer-V2's training prompt does not include headers required in BEq," potentially underestimating its performance. The authors acknowledge methodological limitations in their comparison.

**Note**: The document does not contain Omni-MATH 300 scores or additional FormalMATH-Lite comparisons between these specific models at the 7-8B scale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01d89cb1-38eb-4211-bf96-ae8f7a1064ce",
  "isSidechain": false,
  "promptId": "fe9a7690-7f61-4163-a794-0c898fa55728",
  "type": "user",
  "uuid": "34800576-32f8-418f-a70c-60fabf5abe70",
  "toolUseResult": {
    "bytes": 489284,
    "code": 200,
    "codeText": "OK",
    "result": "# Performance Comparison: StepFun-Formalizer-7B vs Goedel-Formalizer-V2-8B\n\nBased on the document, here's the direct comparison available:\n\n## ProverBench Results\n- **StepFun-Formalizer-7B**: 25.1% BEq@1, 37.9% BEq@16\n- **Goedel-Formalizer-V2-8B**: 16.3% BEq@1, 28.7% BEq@16\n\n## CombiBench Results\n- **StepFun-Formalizer-7B**: 5.2% BEq@1, 11.0% BEq@16\n- **Goedel-Formalizer-V2-8B**: 3.3% BEq@1, 10.0% BEq@16\n\n## Important Caveat\n\nThe document notes an evaluation concern: \"Goedel-Formalizer-V2's training prompt does not include headers required in BEq,\" potentially underestimating its performance. The authors acknowledge methodological limitations in their comparison.\n\n**Note**: The document does not contain Omni-MATH 300 scores or additional FormalMATH-Lite comparisons between these specific models at the 7-8B scale.",
    "durationMs": 3852,
    "url": "https://arxiv.org/html/2508.04440v2"
  },
  "sourceToolAssistantUUID": "01d89cb1-38eb-4211-bf96-ae8f7a1064ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-28T15:46:40.095Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me summarize what I've found:

1. **Goedel-V2 vs StepFun**: StepFun-Formalizer-7B outperforms Goedel-V2-8B on ProverBench (25.1% vs 16.3% BEq@1), but there's a caveat that Goedel-V2's training prompt doesn't include headers required for BEq evaluation. I should change "current SOTA open-source formalizer at this scale" to something like "a competitive open-source formalizer at this scale, chosen for its Lean4-specific training."


2. **"Do LLMs Game Formalization?"** introduces a four-category semantic faithfulness taxonomy—fabrication, mistranslation, omission, contradiction—that operates at the post-compilation semantic layer, which complements our pre-compilation compiler-error taxonomy nicely.
3. **CAM-Bench** provides 1,000 Lean proof targets spanning optimization, numerical linear algebra, and numerical analysis, reinforcing the importance of domain-specific evaluation.

Now I need to think through the impact argument for dynamic versus static evaluation. I should articulate specific scenarios where this distinction matters: cross-domain problems like number theory leveraging analysis typeclasses, cases where domain boundaries are ambiguous, and how retrieval precision changes at higher K values. Then I'll identify the exact locations in the JSON where these citations and arguments belong—likely in the approach section and landscape—and make the other requested changes like updating the SOTA language and being more precise about the Lean4-specific training aspect. exactly where each change lands. The Goedel claim needs a surgical fix in the approach section—I'm replacing the SOTA language with something more measured that acknowledges its Lean4-specific strengths. For the two new papers, I need to weave them into landscape (error characterization and benchmarks respectively), add them to references, and consider whether they strengthen the opportunity framing. The impact argument about domain-conditioned retrieval goes into Stage 2 of the approach. I should also check if the description section repeats the Goedel claim and adjust it there too if needed. I'm working through the model choice justification—I need to reframe the Goedel-Formalizer claim to avoid overstating it as SOTA, instead positioning it as a competitive choice with known tradeoffs like StepFun-Formalizer achieving higher scores on certain benchmarks. Then I'm planning to add impact scenarios after the Stage 2 reranker description and insert the two missing papers into the landscape section where error characterization is discussed. I need to be strategic about how to structure these changes given the document's length. The key modifications are fixing that one phrase in the approach section, adding context about dynamic versus static scenarios in Stage 2, incorporating the two new references into the landscape discussion, and updating the key references list. Let me draft the specific sentences for the dynamic conditioning argument and then write out the complete JSON carefully to preserve all existing content while making these targeted additions.

For the impact section, I'm articulating how dynamic per-problem conditioning beats static context across three concrete scenarios: cross-domain problems where a single number theory query might need analysis-level typeclasses from multiple Mathlib modules simultaneously, domain-boundary problems like algebraic topology where the correct subdomain is ambiguous and dynamic conditioning can weight retrieval across multiple relevant modules instead of committing to one category, and retrieval precision at high K values where domain filtering reduces noise from semantically similar but domain-irrelevant definitions that static context can't filter out. I've tightened the explanation down to about 110 words, which should fit the reviewer's feedback about needing ~150 words of targeted changes across the proposal. Now I'm constructing the full JSON output with these revisions integrated, making sure the edits flow naturally without disrupting the document's overall structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34800576-32f8-418f-a70c-60fabf5abe70",
  "isSidechain": false,
  "requestId": "req_011CbVE5rifnxkHt8EijQ4s8",
  "type": "assistant",
  "uuid": "525b7c1b-d77b-4aa3-b7c0-e7e7943c7dba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzNTWCLDE3MYqSedRJRxsq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 32604,
      "output_tokens": 17811,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17811,
          "cache_read_input_tokens": 32604,
          "cache_creation_input_tokens": 516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 516
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

_source line 34 · 2026-05-28T15:52:21.603Z_

Now I have all the research I need. Let me summarize my findings:

1. **Goedel-V2 vs StepFun**: Confirmed — StepFun-Formalizer-7B beats Goedel-V2-8B (25.1% vs 16.3% BEq@1 on ProverBench), though with noted BEq header format confounds.

2. **"Do LLMs Game Formalization?"** (Kim et al., arXiv 2604.19459, VerifAI-2 @ ICLR 2026): Four-category **post-compilation** semantic faithfulness taxonomy: fabrication (axiom fabrication, conclusion-as-axiom), mistranslation (8 subcategories), omission (missing axiom, dropped antecedent), contradiction. Tested on 303 FOL problems in Lean 4. Key finding: 87–99% compilation but substantial unfaithfulness. Complementary to our pre-compilation error taxonomy.

3. **CAM-Bench** (Long et al., arXiv 2605.17255, May 2026): 1,000 Lean proof targets across optimization, numerical linear algebra, numerical analysis — domain-specific benchmark supporting motivation.

4. **Impact scenarios**: I'll articulate cross-domain problems, domain-boundary ambiguity, and retrieval noise at high K.

Now let me produce the complete revised idea with all four fixes:

```json
{
  "title": "Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy",
  "core_problem": "Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Furthermore, error characterization remains under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that even with 87–99% compilation rates, post-compilation semantic unfaithfulness is pervasive, identifying fabrication, mistranslation, omission, and contradiction as distinct failure modes — but this post-compilation taxonomy is not stratified by mathematical subdomain either. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?",
  "opportunity": "Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed; and (8) CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides 1,000 Lean proof targets specifically in computational and applied mathematics (optimization, numerical linear algebra, numerical analysis) — a concurrent domain-specific benchmark demonstrating growing community recognition that domain-specialized evaluation is necessary, as existing benchmarks predominantly cover algebraic and olympiad-style domains. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.",
  "landscape": "Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides a concurrent 1,000-target Lean benchmark specifically for computational and applied mathematics (optimization, numerical linear algebra, numerical analysis), complementing existing algebraic-heavy benchmarks and independently validating community demand for domain-specific formalization evaluation. Error characterization in autoformalization is under-explored at multiple layers: at the pre-compilation level, repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain — notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. At the post-compilation semantic level, Kim et al. ('Do LLMs Game Formalization?', arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive semantic unfaithfulness, identifying four categories — fabrication (axiom fabrication, conclusion-as-axiom), mistranslation (wrong connective/quantifier/predicate/scope), omission (missing axiom, dropped antecedent), and contradiction (proof by explosion) — but this post-compilation taxonomy operates on FOL problems without mathematical subdomain stratification. Together, these gaps confirm that error characterization is under-explored at BOTH the pre-compilation compiler-error layer (where our taxonomy contributes domain-stratified analysis of APRIL's errors) and the post-compilation semantic-faithfulness layer (where Kim et al.'s taxonomy provides a complementary classification). The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).",
  "inspired_by": "Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain — Shebzukhov (2026) shows domain-stratified aggregate scores but no domain-stratified error type analysis exists — Kim et al. (arXiv 2604.19459) identify post-compilation semantic unfaithfulness categories but without subdomain stratification, confirming error characterization is under-explored at both pre- and post-compilation layers), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%–38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; CAM-Bench (arXiv 2605.17255) as concurrent domain-specific benchmark validating community demand for domain-specialized formalization evaluation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.",
  "approach": "We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is a competitive open-source formalizer at this scale, chosen for its Lean4-specific training — while StepFun-Formalizer-7B achieves higher BEq@1 on ProverBench (25.1% vs. 16.3%), this comparison has noted confounds (Goedel-V2's training prompt omits BEq-required headers) and Goedel-V2 provides the most directly comparable Lean4-native architecture for domain-adaptive fine-tuning; Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. Our pre-compilation compiler-error taxonomy is complementary to Kim et al.'s post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction; arXiv 2604.19459), which demonstrates that even 87–99% compilation rates mask pervasive semantic unfaithfulness but does not stratify by mathematical subdomain — together, these taxonomies characterize error structure at both layers of the formalization stack. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. Dynamic per-problem conditioning systematically outperforms static context in three scenarios that static category blocks cannot address: (a) **cross-domain problems** — a number theory result about Dirichlet series may depend on analysis-level typeclasses (`TopologicalSpace`, `MeasureSpace`) and complex analysis lemmas, requiring retrieval from both NumberTheory and Analysis Mathlib modules simultaneously, which single-category static context keyed to 'number theory' alone would miss entirely; (b) **domain-boundary ambiguity** — problems in algebraic topology or analytic number theory where the correct subdomain assignment is inherently ambiguous and static context commits to a single wrong category, whereas dynamic conditioning produces a soft probability distribution over domains, weighting retrieval from multiple relevant modules proportionally; (c) **retrieval precision at K≥20** — domain filtering acts as a noise reduction mechanism, suppressing semantically similar but domain-irrelevant definitions (e.g., filtering out algebraic `norm` when the problem requires analytic `norm`) that inflate retrieval sets at higher K values, reducing the proportion of distractors that degrade downstream formalization accuracy — a filtering effect unavailable to static context blocks that operate only on the prompt, not on the retrieval ranking itself. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). CAM-Bench's optimization/numerical-analysis/linear-algebra targets provide an additional out-of-distribution evaluation on applied mathematics domains underrepresented in our training data. We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)",
      "timeline": "17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF + CAM-Bench, 3w writing + revision)",
      "estimated_gpu_cost": "$500 (H100 at ~$2.50/hr average via RunPod/Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~200 H100-hours",
      "timeline": "13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)",
      "claude_api_cost": "$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)",
      "estimated_gpu_cost": "$500"
    },
    "auto_research": {
      "gpu_hours": "~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF + CAM-Bench: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)",
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
    "FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (Kim et al., VerifAI-2 Workshop @ ICLR 2026; arXiv 2604.19459)",
    "CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean (Long et al., arXiv 2605.17255)"
  ],
  "description": "We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Error characterization is under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive post-compilation semantic unfaithfulness (fabrication, mistranslation, omission, contradiction), while no prior work stratifies pre-compilation compiler errors by mathematical subdomain. CAM-Bench (Long et al., arXiv 2605.17255) independently validates community demand for domain-specific formalization evaluation with 1,000 targets in applied mathematics. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing both the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis and Kim et al.'s post-compilation semantic faithfulness taxonomy with pre-compilation domain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). Dynamic conditioning specifically addresses scenarios that static context cannot: cross-domain problems requiring retrieval across multiple Mathlib modules (e.g., number theory depending on analysis typeclasses), domain-boundary ambiguity where soft probability distributions over domains outperform hard single-category assignment, and retrieval noise reduction at K≥20 by filtering domain-irrelevant definitions from the ranking. We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.",
  "project_name": "domain_adapt_autoformal",
  "source": "web_research",
  "change_type": "minor",
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
    "round7_issue_4_venue_timeline_fixes": "RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly 'INFEASIBLE for full pipeline given minimum 11-week auto_research timeline' (~8 weeks available), with explicit description of what a partial submission could target (error taxonomy Stage 1 + initial retrieval Stage 2, without full LoRA fine-tuning and ablation suite). ICML 2026 AI4Math Workshop updated to note paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable.",
    "round9_issue_1_Goedel_SOTA_claim": "RESOLVED: Changed 'current SOTA open-source formalizer at this scale' to 'a competitive open-source formalizer at this scale, chosen for its Lean4-specific training' in approach section. Added explicit acknowledgment that StepFun-Formalizer-7B achieves higher BEq@1 on ProverBench (25.1% vs. 16.3%) with noted BEq header format confounds, explaining that Goedel-V2 is chosen for its Lean4-native architecture suitable for domain-adaptive fine-tuning rather than claiming SOTA status.",
    "round9_issue_2_Do_LLMs_Game_Formalization": "RESOLVED: Added Kim et al. ('Do LLMs Game Formalization?', arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) to core_problem, landscape, approach, inspired_by, description, and key_references. Four-category post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction) complements our pre-compilation compiler-error taxonomy — together demonstrating error characterization is under-explored at BOTH layers of the formalization stack. The landscape now explicitly structures the gap as two-layered: pre-compilation (our APRIL-based domain-stratified taxonomy) and post-compilation (Kim et al.'s semantic faithfulness categories, not subdomain-stratified).",
    "round9_issue_3_CAM_Bench": "RESOLVED: Added CAM-Bench (Long et al., arXiv 2605.17255, May 2026) to opportunity, landscape, approach (evaluation), inspired_by, description, and key_references. 1,000 Lean proof targets across optimization, numerical linear algebra, numerical analysis — concurrent domain-specific benchmark validating community demand for domain-specialized evaluation. Added as additional OOD evaluation target for applied mathematics domains underrepresented in training data.",
    "round9_issue_4_dynamic_vs_static_impact": "RESOLVED: Added three specific scenarios in approach Stage 2 where dynamic per-problem conditioning systematically outperforms static context: (a) cross-domain problems — number theory results depending on analysis-level typeclasses requiring retrieval from multiple Mathlib modules that single-category static context misses; (b) domain-boundary ambiguity — algebraic topology / analytic number theory problems where static context commits to a single wrong category while dynamic conditioning produces soft probability distributions over domains; (c) retrieval precision at K≥20 — domain filtering as noise reduction mechanism suppressing semantically similar but domain-irrelevant definitions that inflate retrieval sets. Also added condensed version to description section."
  }
}
```

**Summary of changes (Round 9 → Round 9 revision):**

| Issue | Fix | Location(s) |
|-------|-----|-------------|
| **1. Goedel SOTA claim** (REPEATED) | Changed to "competitive open-source formalizer...chosen for its Lean4-specific training" with explicit StepFun-7B comparison (25.1% vs 16.3% BEq@1) and noted BEq header confounds | `approach` |
| **2. Kim et al. citation** (REPEATED) | Added 4-category post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction); frames error characterization as under-explored at BOTH pre- and post-compilation layers | `core_problem`, `landscape`, `approach`, `inspired_by`, `description`, `key_references` |
| **3. CAM-Bench citation** (REPEATED) | Added 1,000-target applied math benchmark as concurrent domain-specific evaluation validating community demand | `opportunity`, `landscape`, `approach` (eval), `inspired_by`, `description`, `key_references` |
| **4. Dynamic vs static impact** (NEW) | Three concrete scenarios: (a) cross-domain retrieval needs, (b) domain-boundary ambiguity with soft distributions, (c) noise reduction at K≥20 | `approach` Stage 2, `description` |

**Change type: minor** — All four issues are targeted additions/corrections totaling ~200 words of new content, no structural changes.

Sources:
- [Do LLMs Game Formalization? (arXiv 2604.19459)](https://arxiv.org/abs/2604.19459)
- [CAM-Bench (arXiv 2605.17255)](https://arxiv.org/abs/2605.17255)
- [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/html/2508.04440v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "525b7c1b-d77b-4aa3-b7c0-e7e7943c7dba",
  "isSidechain": false,
  "requestId": "req_011CbVE5rifnxkHt8EijQ4s8",
  "type": "assistant",
  "uuid": "815558a1-77c1-4175-ab45-38e1ba0e626b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzNTWCLDE3MYqSedRJRxsq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 32604,
      "output_tokens": 17811,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 516,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17811,
          "cache_read_input_tokens": 32604,
          "cache_creation_input_tokens": 516,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 516
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "815558a1-77c1-4175-ab45-38e1ba0e626b",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval…",
  "leafUuid": "815558a1-77c1-4175-ab45-38e1ba0e626b",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "e0f07656-055b-4ad5-8b1d-9650b6980db5"
}
```

---
