# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Domain-Adaptive Autoformalization

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/7bdd77b8-a434-4224-a75c-b5980a790fa9.jsonl`
- **Structured JSON:** [`dd055e1e33f80c3e2f35.json`](../../sessions/dd/dd055e1e33f80c3e2f35.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T16:05:27.845Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T16:05:27.845Z",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\n\n## Core Problem\n\nCurrent autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Furthermore, error characterization remains under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that even with 87–99% compilation rates, post-compilation semantic unfaithfulness is pervasive, identifying fabrication, mistranslation, omission, and contradiction as distinct failure modes — but this post-compilation taxonomy is not stratified by mathematical subdomain either. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?\n\n## Research Opportunity\n\nSix critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed; and (8) CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides 1,000 Lean proof targets specifically in computational and applied mathematics (optimization, numerical linear algebra, numerical analysis) — a concurrent domain-specific benchmark demonstrating growing community recognition that domain-specialized evaluation is necessary, as existing benchmarks predominantly cover algebraic and olympiad-style domains. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\n\n## Research Landscape\n\nCurrent SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides a concurrent 1,000-target Lean benchmark specifically for computational and applied mathematics (optimization, numerical linear algebra, numerical analysis), complementing existing algebraic-heavy benchmarks and independently validating community demand for domain-specific formalization evaluation. Error characterization in autoformalization is under-explored at multiple layers: at the pre-compilation level, repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain — notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. At the post-compilation semantic level, Kim et al. ('Do LLMs Game Formalization?', arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive semantic unfaithfulness, identifying four categories — fabrication (axiom fabrication, conclusion-as-axiom), mistranslation (wrong connective/quantifier/predicate/scope), omission (missing axiom, dropped antecedent), and contradiction (proof by explosion) — but this post-compilation taxonomy operates on FOL problems without mathematical subdomain stratification. Together, these gaps confirm that error characterization is under-explored at BOTH the pre-compilation compiler-error layer (where our taxonomy contributes domain-stratified analysis of APRIL's errors) and the post-compilation semantic-faithfulness layer (where Kim et al.'s taxonomy provides a complementary classification). The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).\n\n## Proposed Approach\n\nWe build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is a competitive open-source formalizer at this scale, chosen for its Lean4-specific training — while StepFun-Formalizer-7B achieves higher BEq@1 on ProverBench (25.1% vs. 16.3%), this comparison has noted confounds (Goedel-V2's training prompt omits BEq-required headers) and Goedel-V2 provides the most directly comparable Lean4-native architecture for domain-adaptive fine-tuning; Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. Our pre-compilation compiler-error taxonomy is complementary to Kim et al.'s post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction; arXiv 2604.19459), which demonstrates that even 87–99% compilation rates mask pervasive semantic unfaithfulness but does not stratify by mathematical subdomain — together, these taxonomies characterize error structure at both layers of the formalization stack. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. Dynamic per-problem conditioning systematically outperforms static context in three scenarios that static category blocks cannot address: (a) **cross-domain problems** — a number theory result about Dirichlet series may depend on analysis-level typeclasses (`TopologicalSpace`, `MeasureSpace`) and complex analysis lemmas, requiring retrieval from both NumberTheory and Analysis Mathlib modules simultaneously, which single-category static context keyed to 'number theory' alone would miss entirely; (b) **domain-boundary ambiguity** — problems in algebraic topology or analytic number theory where the correct subdomain assignment is inherently ambiguous and static context commits to a single wrong category, whereas dynamic conditioning produces a soft probability distribution over domains, weighting retrieval from multiple relevant modules proportionally; (c) **retrieval precision at K≥20** — domain filtering acts as a noise reduction mechanism, suppressing semantically similar but domain-irrelevant definitions (e.g., filtering out algebraic `norm` when the problem requires analytic `norm`) that inflate retrieval sets at higher K values, reducing the proportion of distractors that degrade downstream formalization accuracy — a filtering effect unavailable to static context blocks that operate only on the prompt, not on the retrieval ranking itself. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). CAM-Bench's optimization/numerical-analysis/linear-algebra targets provide an additional out-of-distribution evaluation on applied mathematics domains underrepresented in our training data. We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\n\n## Detailed Description\n\nWe propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Error characterization is under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive post-compilation semantic unfaithfulness (fabrication, mistranslation, omission, contradiction), while no prior work stratifies pre-compilation compiler errors by mathematical subdomain. CAM-Bench (Long et al., arXiv 2605.17255) independently validates community demand for domain-specific formalization evaluation with 1,000 targets in applied mathematics. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing both the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis and Kim et al.'s post-compilation semantic faithfulness taxonomy with pre-compilation domain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). Dynamic conditioning specifically addresses scenarios that static context cannot: cross-domain problems requiring retrieval across multiple Mathlib modules (e.g., number theory depending on analysis typeclasses), domain-boundary ambiguity where soft probability distributions over domains outperform hard single-category assignment, and retrieval noise reduction at K≥20 by filtering domain-irrelevant definitions from the ranking. We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\n\n## Key References\n\n- Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\n- MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\n- Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\n- Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\n- Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\n- Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\n- Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\n- Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\n- M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\n- Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\n- 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\n- LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\n- KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)\n- ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\n- FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\n- Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (Kim et al., VerifAI-2 Workshop @ ICLR 2026; arXiv 2604.19459)\n- CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean (Long et al., arXiv 2605.17255)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h), timeline: 17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF + CAM-Bench, 3w writing + revision), estimated_gpu_cost: $500 (H100 at ~$2.50/hr average via RunPod/Lambda)\n- **human_in_loop**: gpu_hours: ~200 H100-hours, timeline: 13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis), claude_api_cost: $300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis), estimated_gpu_cost: $500\n- **auto_research**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF + CAM-Bench: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h), timeline: 11 weeks, claude_api_cost: $450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting), estimated_gpu_cost: $500, speed_bottleneck: Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T16:05:27.847Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T16:05:27.847Z",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-28T16:05:27.858Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy

## Core Problem

Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Furthermore, error characterization remains under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that even with 87–99% compilation rates, post-compilation semantic unfaithfulness is pervasive, identifying fabrication, mistranslation, omission, and contradiction as distinct failure modes — but this post-compilation taxonomy is not stratified by mathematical subdomain either. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?

## Research Opportunity

Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed; and (8) CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides 1,000 Lean proof targets specifically in computational and applied mathematics (optimization, numerical linear algebra, numerical analysis) — a concurrent domain-specific benchmark demonstrating growing community recognition that domain-specialized evaluation is necessary, as existing benchmarks predominantly cover algebraic and olympiad-style domains. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.

## Research Landscape

Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides a concurrent 1,000-target Lean benchmark specifically for computational and applied mathematics (optimization, numerical linear algebra, numerical analysis), complementing existing algebraic-heavy benchmarks and independently validating community demand for domain-specific formalization evaluation. Error characterization in autoformalization is under-explored at multiple layers: at the pre-compilation level, repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain — notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. At the post-compilation semantic level, Kim et al. ('Do LLMs Game Formalization?', arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive semantic unfaithfulness, identifying four categories — fabrication (axiom fabrication, conclusion-as-axiom), mistranslation (wrong connective/quantifier/predicate/scope), omission (missing axiom, dropped antecedent), and contradiction (proof by explosion) — but this post-compilation taxonomy operates on FOL problems without mathematical subdomain stratification. Together, these gaps confirm that error characterization is under-explored at BOTH the pre-compilation compiler-error layer (where our taxonomy contributes domain-stratified analysis of APRIL's errors) and the post-compilation semantic-faithfulness layer (where Kim et al.'s taxonomy provides a complementary classification). The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).

## Proposed Approach

We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is a competitive open-source formalizer at this scale, chosen for its Lean4-specific training — while StepFun-Formalizer-7B achieves higher BEq@1 on ProverBench (25.1% vs. 16.3%), this comparison has noted confounds (Goedel-V2's training prompt omits BEq-required headers) and Goedel-V2 provides the most directly comparable Lean4-native architecture for domain-adaptive fine-tuning; Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. Our pre-compilation compiler-error taxonomy is complementary to Kim et al.'s post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction; arXiv 2604.19459), which demonstrates that even 87–99% compilation rates mask pervasive semantic unfaithfulness but does not stratify by mathematical subdomain — together, these taxonomies characterize error structure at both layers of the formalization stack. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. Dynamic per-problem conditioning systematically outperforms static context in three scenarios that static category blocks cannot address: (a) **cross-domain problems** — a number theory result about Dirichlet series may depend on analysis-level typeclasses (`TopologicalSpace`, `MeasureSpace`) and complex analysis lemmas, requiring retrieval from both NumberTheory and Analysis Mathlib modules simultaneously, which single-category static context keyed to 'number theory' alone would miss entirely; (b) **domain-boundary ambiguity** — problems in algebraic topology or analytic number theory where the correct subdomain assignment is inherently ambiguous and static context commits to a single wrong category, whereas dynamic conditioning produces a soft probability distribution over domains, weighting retrieval from multiple relevant modules proportionally; (c) **retrieval precision at K≥20** — domain filtering acts as a noise reduction mechanism, suppressing semantically similar but domain-irrelevant definitions (e.g., filtering out algebraic `norm` when the problem requires analytic `norm`) that inflate retrieval sets at higher K values, reducing the proportion of distractors that degrade downstream formalization accuracy — a filtering effect unavailable to static context blocks that operate only on the prompt, not on the retrieval ranking itself. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). CAM-Bench's optimization/numerical-analysis/linear-algebra targets provide an additional out-of-distribution evaluation on applied mathematics domains underrepresented in our training data. We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.

## Detailed Description

We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Error characterization is under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive post-compilation semantic unfaithfulness (fabrication, mistranslation, omission, contradiction), while no prior work stratifies pre-compilation compiler errors by mathematical subdomain. CAM-Bench (Long et al., arXiv 2605.17255) independently validates community demand for domain-specific formalization evaluation with 1,000 targets in applied mathematics. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing both the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis and Kim et al.'s post-compilation semantic faithfulness taxonomy with pre-compilation domain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). Dynamic conditioning specifically addresses scenarios that static context cannot: cross-domain problems requiring retrieval across multiple Mathlib modules (e.g., number theory depending on analysis typeclasses), domain-boundary ambiguity where soft probability distributions over domains outperform hard single-category assignment, and retrieval noise reduction at K≥20 by filtering domain-irrelevant definitions from the ranking. We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.

## Key References

- Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)
- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)
- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)
- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)
- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)
- MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)
- Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)
- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)
- SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)
- Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)
- Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)
- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)
- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)
- Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)
- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)
- Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)
- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)
- Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)
- Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)
- M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)
- Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)
- 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)
- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)
- LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)
- KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)
- ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)
- FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)
- Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (Kim et al., VerifAI-2 Workshop @ ICLR 2026; arXiv 2604.19459)
- CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean (Long et al., arXiv 2605.17255)

## Resource Estimate

- **manual**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h), timeline: 17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF + CAM-Bench, 3w writing + revision), estimated_gpu_cost: $500 (H100 at ~$2.50/hr average via RunPod/Lambda)
- **human_in_loop**: gpu_hours: ~200 H100-hours, timeline: 13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis), claude_api_cost: $300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis), estimated_gpu_cost: $500
- **auto_research**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF + CAM-Bench: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h), timeline: 11 weeks, claude_api_cost: $450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting), estimated_gpu_cost: $500, speed_bottleneck: Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "745e39f6-daa8-4899-ae74-e2ab4cfd42cd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T16:05:27.857Z_

```json
{
  "parentUuid": "745e39f6-daa8-4899-ae74-e2ab4cfd42cd",
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
  "uuid": "3fb6dcf9-70f7-417e-98cf-4549ae973d95",
  "timestamp": "2026-05-28T16:05:27.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T16:05:27.857Z_

```json
{
  "parentUuid": "3fb6dcf9-70f7-417e-98cf-4549ae973d95",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "441baf6e-0560-48c2-9831-2605f697d9ee",
  "timestamp": "2026-05-28T16:05:27.857Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "441baf6e-0560-48c2-9831-2605f697d9ee",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Assistant

_source line 8 · 2026-05-28T16:05:32.570Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about domain-adaptive autoformalization - building a pipeline that conditions retrieval and prompting on mathematical subdomains for converting natural language math to formal Lean code.

Let me first do the required web searches to understand the current landscape before making any judgments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "441baf6e-0560-48c2-9831-2605f697d9ee",
  "isSidechain": false,
  "requestId": "req_011CbVFascB32LL4gVjCaN8A",
  "type": "assistant",
  "uuid": "f8fced65-90cd-42df-b0d6-ff1cf0293116",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7rvsbX95MBoKJCzbSUPon",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 25761,
      "output_tokens": 183,
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
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 25761,
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

### Assistant

_source line 9 · 2026-05-28T16:05:34.276Z_

I need to conduct thorough field research before evaluating this proposal. Let me start by searching for the key topics and recent works mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8fced65-90cd-42df-b0d6-ff1cf0293116",
  "isSidechain": false,
  "requestId": "req_011CbVFascB32LL4gVjCaN8A",
  "type": "assistant",
  "uuid": "cabb1af9-09ef-41f8-8414-37c97ba5c72f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7rvsbX95MBoKJCzbSUPon",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 25761,
      "output_tokens": 183,
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
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 25761,
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

### Tool call

_source line 10 · 2026-05-28T16:05:34.429Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013sz6yXLEqCKwasqmAXj53s`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabb1af9-09ef-41f8-8414-37c97ba5c72f",
  "isSidechain": false,
  "requestId": "req_011CbVFascB32LL4gVjCaN8A",
  "type": "assistant",
  "uuid": "4df8d148-c18a-4812-8863-f6a693dd49b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7rvsbX95MBoKJCzbSUPon",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 25761,
      "output_tokens": 183,
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
          "input_tokens": 2,
          "output_tokens": 183,
          "cache_read_input_tokens": 25761,
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

_source line 11 · 2026-05-28T16:05:34.435Z_

<details><summary>↩ Tool result · `toolu_013sz6yXLEqCKwasqmAXj53s`</summary>

````text
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
  "parentUuid": "4df8d148-c18a-4812-8863-f6a693dd49b6",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "5a25f2d7-d8cb-46ef-b1eb-a072647f0018",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4df8d148-c18a-4812-8863-f6a693dd49b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T16:05:41.030Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now conduct the required web searches to understand the current landscape of autoformalization, domain-adaptive approaches, and the key works mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a25f2d7-d8cb-46ef-b1eb-a072647f0018",
  "isSidechain": false,
  "requestId": "req_011CbVFbPWGBWBSrAvDVaEk3",
  "type": "assistant",
  "uuid": "b946a3e9-126b-46ec-8199-15acc353bc7e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2bRsoU1bqoMaJ5qJ9hkKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25761,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 25761,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
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

_source line 13 · 2026-05-28T16:05:41.961Z_

Now let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b946a3e9-126b-46ec-8199-15acc353bc7e",
  "isSidechain": false,
  "requestId": "req_011CbVFbPWGBWBSrAvDVaEk3",
  "type": "assistant",
  "uuid": "6ba4a4cb-f674-4544-819d-01ac0fd43af9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2bRsoU1bqoMaJ5qJ9hkKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25761,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 25761,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
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

_source line 14 · 2026-05-28T16:05:42.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mx1RiUG1Q7ANE5kHJMUYmY`</summary>

```json
{
  "query": "autoformalization domain bias mathematical subdomain 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ba4a4cb-f674-4544-819d-01ac0fd43af9",
  "isSidechain": false,
  "requestId": "req_011CbVFbPWGBWBSrAvDVaEk3",
  "type": "assistant",
  "uuid": "7280ef4e-4cc9-4915-adb6-549703aa7327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2bRsoU1bqoMaJ5qJ9hkKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 25761,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 25761,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
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

_source line 15 · 2026-05-28T16:05:48.386Z_

<details><summary>↩ Tool result · `toolu_01Mx1RiUG1Q7ANE5kHJMUYmY`</summary>

```text
Web search results for query: "autoformalization domain bias mathematical subdomain 2025 2026"

Links: [{"title":"Autoformalization of Mathematics","url":"https://www.emergentmind.com/topics/autoformalization-of-mathematics"},{"title":"Freedom Math Dance: Autoformalization of mathematical theorems? No shit!","url":"https://freedommathdance.blogspot.com/2025/07/autoformalization-of-mathematical.html"},{"title":"Autoformalization: Bridging Informal and Formal Math","url":"https://www.emergentmind.com/topics/autoformalization"},{"title":"[2505.23486] Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/abs/2505.23486"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.90/"}]

Based on the search results, here's what I found regarding autoformalization and domain bias in mathematical subdomains for 2025-2026:

## Key Findings on Domain Bias and Autoformalization

Most autoformalization benchmarks draw from textbook or Olympiad-level mathematics, while research, applied math, and real-world scientific problems remain substantially underrepresented. This represents a significant domain bias issue in the field.

Geometry and combinatorics often lack the necessary corpus for high-quality training, though PDE control marks early progress in applied mathematics autoformalization. For specialized domains like PDE control, the Translator module attains near-perfect autoformalization with high syntactic validity on synthetic cases and 64% on manually written cases.

## Research Priorities

Research priorities include construction and curation of larger, higher-fidelity, and more diverse autoformalization datasets spanning underrepresented domains and definition types.

## Current Challenges

Recent research from 2025 identifies additional challenges: Definitions present a greater challenge compared to existing benchmarks, and LLMs still struggle with self-correction and aligning with relevant mathematical libraries. However, structured refinement methods and definition grounding strategies yield notable improvements of up to 16% on self-correction capabilities and 43% on the reduction of undefined errors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7280ef4e-4cc9-4915-adb6-549703aa7327",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "5bc0d7b7-d714-4f9f-9f4f-c08fedc531d9",
  "toolUseResult": {
    "query": "autoformalization domain bias mathematical subdomain 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015JnXCHagVvtxKgTrPFZzw2",
        "content": [
          {
            "title": "Autoformalization of Mathematics",
            "url": "https://www.emergentmind.com/topics/autoformalization-of-mathematics"
          },
          {
            "title": "Freedom Math Dance: Autoformalization of mathematical theorems? No shit!",
            "url": "https://freedommathdance.blogspot.com/2025/07/autoformalization-of-mathematical.html"
          },
          {
            "title": "Autoformalization: Bridging Informal and Formal Math",
            "url": "https://www.emergentmind.com/topics/autoformalization"
          },
          {
            "title": "[2505.23486] Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/abs/2505.23486"
          },
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/pdf/2410.04194"
          },
          {
            "title": "Autoformalization in the Wild: Assessing LLMs on Real-World Mathematical Definitions - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.90/"
          }
        ]
      },
      "Based on the search results, here's what I found regarding autoformalization and domain bias in mathematical subdomains for 2025-2026:\n\n## Key Findings on Domain Bias and Autoformalization\n\nMost autoformalization benchmarks draw from textbook or Olympiad-level mathematics, while research, applied math, and real-world scientific problems remain substantially underrepresented. This represents a significant domain bias issue in the field.\n\nGeometry and combinatorics often lack the necessary corpus for high-quality training, though PDE control marks early progress in applied mathematics autoformalization. For specialized domains like PDE control, the Translator module attains near-perfect autoformalization with high syntactic validity on synthetic cases and 64% on manually written cases.\n\n## Research Priorities\n\nResearch priorities include construction and curation of larger, higher-fidelity, and more diverse autoformalization datasets spanning underrepresented domains and definition types.\n\n## Current Challenges\n\nRecent research from 2025 identifies additional challenges: Definitions present a greater challenge compared to existing benchmarks, and LLMs still struggle with self-correction and aligning with relevant mathematical libraries. However, structured refinement methods and definition grounding strategies yield notable improvements of up to 16% on self-correction capabilities and 43% on the reduction of undefined errors."
    ],
    "durationSeconds": 6.118670548999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7280ef4e-4cc9-4915-adb6-549703aa7327",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T16:05:51.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SnxWahkZ8qBvp2Y67mbEZP`</summary>

```json
{
  "query": "CRAMF DRIFT autoformalization retrieval augmented ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bc0d7b7-d714-4f9f-9f4f-c08fedc531d9",
  "isSidechain": false,
  "requestId": "req_011CbVFcPATHg44oTiGJjFPN",
  "type": "assistant",
  "uuid": "6c00e21b-8568-45bc-963e-b40b274cd56f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vSxncStt6X7SXbgxwu1yC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 26471,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 26471,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 17 · 2026-05-28T16:05:57.505Z_

<details><summary>↩ Tool result · `toolu_01SnxWahkZ8qBvp2Y67mbEZP`</summary>

```text
Web search results for query: "CRAMF DRIFT autoformalization retrieval augmented ICLR 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"},{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815"},{"title":"Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS","url":"https://arxiv.org/pdf/2510.10815"},{"title":"Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence","url":"https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"}]

Based on the search results, I found relevant information about both CRAMF and DRIFT in relation to autoformalization and ICLR 2026:

## CRAMF (Concept-driven Retrieval-Augmented Mathematical Formalization)

CRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework that enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation. The framework constructs a concept-definition knowledge base from Mathlib4, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts.

The framework addresses two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions. Experiments show that CRAMF yields consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.

## DRIFT (Decompose, Retrieve, Illustrate, then Formalize Theorems)

DRIFT is a novel framework that enhances retrieval-augmented autoformalization by adapting query decomposition and context augmentation to address the unique challenges of theorem autoformalization. It decomposes statements into a series of simpler, atomic sub-queries, with each sub-query targeting a single mathematical concept, transforming a multifaceted retrieval problem into focused, precise searches.

Both frameworks were presented at or are related to ICLR 2026, with DRIFT published as a conference paper at ICLR 2026 and CRAMF being under review for the conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c00e21b-8568-45bc-963e-b40b274cd56f",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "984855a2-ab1b-40cc-94b2-c588df22acc5",
  "toolUseResult": {
    "query": "CRAMF DRIFT autoformalization retrieval augmented ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vv8tN6Kpt2fadQhLtvNdXf",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"
          },
          {
            "title": "AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...",
            "url": "https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/html/2510.10815"
          },
          {
            "title": "Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS",
            "url": "https://arxiv.org/pdf/2510.10815"
          },
          {
            "title": "Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence",
            "url": "https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/pdf/2508.06931"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/html/2508.06931"
          }
        ]
      },
      "Based on the search results, I found relevant information about both CRAMF and DRIFT in relation to autoformalization and ICLR 2026:\n\n## CRAMF (Concept-driven Retrieval-Augmented Mathematical Formalization)\n\nCRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework that enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation. The framework constructs a concept-definition knowledge base from Mathlib4, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts.\n\nThe framework addresses two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions. Experiments show that CRAMF yields consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.\n\n## DRIFT (Decompose, Retrieve, Illustrate, then Formalize Theorems)\n\nDRIFT is a novel framework that enhances retrieval-augmented autoformalization by adapting query decomposition and context augmentation to address the unique challenges of theorem autoformalization. It decomposes statements into a series of simpler, atomic sub-queries, with each sub-query targeting a single mathematical concept, transforming a multifaceted retrieval problem into focused, precise searches.\n\nBoth frameworks were presented at or are related to ICLR 2026, with DRIFT published as a conference paper at ICLR 2026 and CRAMF being under review for the conference."
    ],
    "durationSeconds": 6.120135435,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c00e21b-8568-45bc-963e-b40b274cd56f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T16:06:00.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcBgvn5PUxVV413YVoLNoH`</summary>

```json
{
  "query": "APRIL repair lean proofs compiler feedback error taxonomy 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "984855a2-ab1b-40cc-94b2-c588df22acc5",
  "isSidechain": false,
  "requestId": "req_011CbVFd4Bix73JXHQxDeuH3",
  "type": "assistant",
  "uuid": "79a52e8e-de2c-4d70-9566-077511e9c8ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RVZTA7cLxjR3HsJqWdeEWT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 27194,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 27194,
          "cache_creation_input_tokens": 861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 861
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

_source line 19 · 2026-05-28T16:06:07.589Z_

<details><summary>↩ Tool result · `toolu_01LcBgvn5PUxVV413YVoLNoH`</summary>

```text
Web search results for query: "APRIL repair lean proofs compiler feedback error taxonomy 2026 arXiv"

Links: [{"title":"Paper page - Learning to Repair Lean Proofs from Compiler Feedback","url":"https://huggingface.co/papers/2602.02990"},{"title":"[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/abs/2602.02990"},{"title":"[Literature Review] Learning to Repair Lean Proofs from Compiler Feedback","url":"https://www.themoonlight.io/en/review/learning-to-repair-lean-proofs-from-compiler-feedback"},{"title":"Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/pdf/2602.02990"},{"title":"lean-error-correction/README.md at main · uw-math-ai/lean-error-correction","url":"https://github.com/uw-math-ai/lean-error-correction/blob/main/README.md"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced ...","url":"https://www.arxiv.org/pdf/2505.05758v1"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/pdf/2505.05758"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/html/2505.05758v5"},{"title":"Technical Report GOEDEL-PROVER-V2: SCALING FORMAL THEOREM","url":"https://arxiv.org/pdf/2508.03613"}]

Based on the search results, I found the paper you're looking for:

**APRIL (Automated Proof Repair in Lean)** is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.

The research studies Lean proof repair as a supervised learning problem: given an erroneous proof and compiler feedback, predicting both a corrected proof and a natural-language diagnosis grounded in the same feedback.

Training language models on APRIL substantially improves repair accuracy and feedback-conditioned reasoning; in single-shot repair evaluation, a finetuned 4B-parameter model outperforms the strongest open-source baseline.

The paper was published on arXiv as **2602.02990** in March 2026, and is available at https://arxiv.org/abs/2602.02990.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a52e8e-de2c-4d70-9566-077511e9c8ed",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "a9341fa3-f3c5-4a88-a413-03a9d13b4051",
  "toolUseResult": {
    "query": "APRIL repair lean proofs compiler feedback error taxonomy 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QbQ7Ny1nbD4NaYu6Udw468",
        "content": [
          {
            "title": "Paper page - Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://huggingface.co/papers/2602.02990"
          },
          {
            "title": "[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/abs/2602.02990"
          },
          {
            "title": "[Literature Review] Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://www.themoonlight.io/en/review/learning-to-repair-lean-proofs-from-compiler-feedback"
          },
          {
            "title": "Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/pdf/2602.02990"
          },
          {
            "title": "lean-error-correction/README.md at main · uw-math-ai/lean-error-correction",
            "url": "https://github.com/uw-math-ai/lean-error-correction/blob/main/README.md"
          },
          {
            "title": "APOLLO: Automated LLM and Lean Collaboration for Advanced ...",
            "url": "https://www.arxiv.org/pdf/2505.05758v1"
          },
          {
            "title": "APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning",
            "url": "https://arxiv.org/pdf/2505.05758"
          },
          {
            "title": "APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning",
            "url": "https://arxiv.org/html/2505.05758v5"
          },
          {
            "title": "Technical Report GOEDEL-PROVER-V2: SCALING FORMAL THEOREM",
            "url": "https://arxiv.org/pdf/2508.03613"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**APRIL (Automated Proof Repair in Lean)** is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.\n\nThe research studies Lean proof repair as a supervised learning problem: given an erroneous proof and compiler feedback, predicting both a corrected proof and a natural-language diagnosis grounded in the same feedback.\n\nTraining language models on APRIL substantially improves repair accuracy and feedback-conditioned reasoning; in single-shot repair evaluation, a finetuned 4B-parameter model outperforms the strongest open-source baseline.\n\nThe paper was published on arXiv as **2602.02990** in March 2026, and is available at https://arxiv.org/abs/2602.02990."
    ],
    "durationSeconds": 7.143656074999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "79a52e8e-de2c-4d70-9566-077511e9c8ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T16:06:10.681Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gf7sh96WT88x19SKZ3mMxH`</summary>

```json
{
  "query": "MSC-180 benchmark formal theorem proving FormalMATH domain performance variation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9341fa3-f3c5-4a88-a413-03a9d13b4051",
  "isSidechain": false,
  "requestId": "req_011CbVFdp4ghL24bCx5rZM4G",
  "type": "assistant",
  "uuid": "fe60d31b-5e3b-4a2e-acb5-d17db905bb4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLGSckF8Xispegb6tZ7n3S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 28055,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 28055,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 21 · 2026-05-28T16:06:15.715Z_

<details><summary>↩ Tool result · `toolu_01Gf7sh96WT88x19SKZ3mMxH`</summary>

```text
Web search results for query: "MSC-180 benchmark formal theorem proving FormalMATH domain performance variation 2025"

Links: [{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/html/2512.18256v1"},{"title":"[2512.18256] MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/abs/2512.18256"},{"title":"MSC-180: A BENCHMARK FOR","url":"https://openreview.net/pdf/1d26736d12fac2add669df15fc65ba349e19edbb.pdf"},{"title":"Automated Theorem Proving Systems","url":"https://www.emergentmind.com/topics/automated-theorem-proving-atp-systems"},{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/pdf/2512.18256"},{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification | OpenReview","url":"https://openreview.net/forum?id=VBS5at5yrN"}]

Based on the search results, here's what I found about the MSC-180 benchmark:

## MSC-180 Benchmark Overview

MSC-180 is a benchmark for evaluation based on the MSC2020 mathematical subject classification, comprising 180 formal verification problems—3 advanced problems from each of 60 mathematical branches—spanning from undergraduate to graduate levels. Each problem has undergone multiple rounds of verification and refinement by domain experts to ensure formal accuracy.

## Performance Results

Evaluations of state-of-the-art LLM-based theorem provers under the pass@32 setting reveal that the best model achieves only an 18.89% overall pass rate, with prominent issues including significant domain bias (maximum domain coverage 41.7%) and a difficulty gap (significantly lower pass rates on graduate-level problems).

## Domain Performance Variation

To further quantify performance variability across mathematical domains, the benchmark introduces the coefficient of variation (CV) as an evaluation metric. This metric is used to measure how performance varies across different mathematical domains.

## Relationship to FormalMATH

FormalMATH has a higher proportion of problems related to integrals and elementary calculus, while MiniF2F focuses more on high school algebra and number theory. The MSC-180 benchmark was designed to address the domain imbalances present in earlier benchmarks like FormalMATH.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe60d31b-5e3b-4a2e-acb5-d17db905bb4b",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "2ab7fa19-d314-4664-b35e-8fa2f31024a7",
  "toolUseResult": {
    "query": "MSC-180 benchmark formal theorem proving FormalMATH domain performance variation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ANZLwsc93RzpSfMjaPAFVD",
        "content": [
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/html/2512.18256v1"
          },
          {
            "title": "[2512.18256] MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/abs/2512.18256"
          },
          {
            "title": "MSC-180: A BENCHMARK FOR",
            "url": "https://openreview.net/pdf/1d26736d12fac2add669df15fc65ba349e19edbb.pdf"
          },
          {
            "title": "Automated Theorem Proving Systems",
            "url": "https://www.emergentmind.com/topics/automated-theorem-proving-atp-systems"
          },
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/pdf/2512.18256"
          },
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification | OpenReview",
            "url": "https://openreview.net/forum?id=VBS5at5yrN"
          }
        ]
      },
      "Based on the search results, here's what I found about the MSC-180 benchmark:\n\n## MSC-180 Benchmark Overview\n\nMSC-180 is a benchmark for evaluation based on the MSC2020 mathematical subject classification, comprising 180 formal verification problems—3 advanced problems from each of 60 mathematical branches—spanning from undergraduate to graduate levels. Each problem has undergone multiple rounds of verification and refinement by domain experts to ensure formal accuracy.\n\n## Performance Results\n\nEvaluations of state-of-the-art LLM-based theorem provers under the pass@32 setting reveal that the best model achieves only an 18.89% overall pass rate, with prominent issues including significant domain bias (maximum domain coverage 41.7%) and a difficulty gap (significantly lower pass rates on graduate-level problems).\n\n## Domain Performance Variation\n\nTo further quantify performance variability across mathematical domains, the benchmark introduces the coefficient of variation (CV) as an evaluation metric. This metric is used to measure how performance varies across different mathematical domains.\n\n## Relationship to FormalMATH\n\nFormalMATH has a higher proportion of problems related to integrals and elementary calculus, while MiniF2F focuses more on high school algebra and number theory. The MSC-180 benchmark was designed to address the domain imbalances present in earlier benchmarks like FormalMATH."
    ],
    "durationSeconds": 5.0298241089999935,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fe60d31b-5e3b-4a2e-acb5-d17db905bb4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "2ab7fa19-d314-4664-b35e-8fa2f31024a7",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Tool call

_source line 24 · 2026-05-28T16:06:18.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KtCrF1nVdZMgB5L8uR6Dbu`</summary>

```json
{
  "query": "LeanSearch v2 premise retrieval 2026 domain-conditioned retrieval autoformalization StepFun-Formalizer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab7fa19-d314-4664-b35e-8fa2f31024a7",
  "isSidechain": false,
  "requestId": "req_011CbVFeQ1N6CjuJP9QHkjc6",
  "type": "assistant",
  "uuid": "953f742f-f8b5-4093-8a5d-db29032951c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDxwqLHpSyQ8KLKczqC45b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 28774,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 28774,
          "cache_creation_input_tokens": 715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 715
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

_source line 25 · 2026-05-28T16:06:28.137Z_

<details><summary>↩ Tool result · `toolu_01KtCrF1nVdZMgB5L8uR6Dbu`</summary>

```text
Web search results for query: "LeanSearch v2 premise retrieval 2026 domain-conditioned retrieval autoformalization StepFun-Formalizer"

Links: [{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137"},{"title":"[2605.13137] LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/abs/2605.13137"},{"title":"Combining Textual and Structural Information for Premise Selection in Lean","url":"https://arxiv.org/pdf/2510.23637"},{"title":"(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"},{"title":"Lean Finder: Semantic Search for Mathlib That Understands User Intents","url":"https://openreview.net/pdf?id=5SF4fFRw7u"},{"title":"Premise Selection for a Lean Hammer","url":"https://arxiv.org/pdf/2506.07477"}]

Now let me search for information about StepFun-Formalizer and autoformalization:

Links: [{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://www.arxiv.org/pdf/2508.04440"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40691"},{"title":"StepFun-Formalizer/README.md at master · stepfun-ai/StepFun-Formalizer","url":"https://github.com/stepfun-ai/StepFun-Formalizer/blob/master/README.md"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion","url":"https://arxiv.org/html/2508.04440v3"},{"title":"stepfun-ai/StepFun-Formalizer-7B · Hugging Face","url":"https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"},{"title":"GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub","url":"https://github.com/stepfun-ai/StepFun-Formalizer"},{"title":"[2508.04440v1] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440v1"},{"title":"[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/abs/2508.04440"}]

Based on the search results, here's what I found regarding your query:

## LeanSearch v2

LeanSearch v2 formulates global premise retrieval as the task of recovering the logically coherent set of library lemmas that an entire theorem's proof requires. LeanSearch v2 is a staged retrieval system whose standard mode achieves state-of-the-art Mathlib search without domain-specific fine-tuning. 

Its reasoning mode builds on standard mode as its retrieval substrate, targeting global premise retrieval through iterative sketch-retrieve-reflect cycles. On a 69-query benchmark of research-level Mathlib theorems, reasoning mode recovers 46.1% of ground-truth premise groups within 10 retrieved candidates, outperforming strong reasoning retrieval systems (38.0%) and premise-selection baselines (9.3%).

## StepFun-Formalizer

StepFun-Formalizer aims to translate natural-language mathematical statements into a formal language. The key abilities for effective autoformalization are comprehensive mastery of formal-language domain knowledge, and reasoning capability of natural language problem understanding and informal-formal alignment. Without the former, a model cannot identify the correct formal objects; without the latter, it struggles to interpret real-world contexts and map them precisely into formal expressions.

StepFun-Formalizer introduces ThinkingF, the first data synthesis and training pipeline for the autoformalization model with both domain knowledge and informal-to-formal reasoning capability, implemented through large-scale distillation and selection of data with formal knowledge, and informal-to-formal reasoning trajectories synthesis guided by an expert-designed autoformalization template.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "953f742f-f8b5-4093-8a5d-db29032951c0",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "09fd647e-8d2c-4dfc-ae09-853bbde9022f",
  "toolUseResult": {
    "query": "LeanSearch v2 premise retrieval 2026 domain-conditioned retrieval autoformalization StepFun-Formalizer",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PU1C51j9sobuDYP3aJ1yAY",
        "content": [
          {
            "title": "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving",
            "url": "https://arxiv.org/html/2605.13137"
          },
          {
            "title": "[2605.13137] LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving",
            "url": "https://arxiv.org/abs/2605.13137"
          },
          {
            "title": "Combining Textual and Structural Information for Premise Selection in Lean",
            "url": "https://arxiv.org/pdf/2510.23637"
          },
          {
            "title": "(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning",
            "url": "https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"
          },
          {
            "title": "Lean Finder: Semantic Search for Mathlib That Understands User Intents",
            "url": "https://openreview.net/pdf?id=5SF4fFRw7u"
          },
          {
            "title": "Premise Selection for a Lean Hammer",
            "url": "https://arxiv.org/pdf/2506.07477"
          }
        ]
      },
      "Now let me search for information about StepFun-Formalizer and autoformalization:",
      {
        "tool_use_id": "srvtoolu_01AJJFXvA7b84B6tYv84mGEy",
        "content": [
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential",
            "url": "https://www.arxiv.org/pdf/2508.04440"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40691"
          },
          {
            "title": "StepFun-Formalizer/README.md at master · stepfun-ai/StepFun-Formalizer",
            "url": "https://github.com/stepfun-ai/StepFun-Formalizer/blob/master/README.md"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/html/2508.04440v3"
          },
          {
            "title": "stepfun-ai/StepFun-Formalizer-7B · Hugging Face",
            "url": "https://huggingface.co/stepfun-ai/StepFun-Formalizer-7B"
          },
          {
            "title": "GitHub - stepfun-ai/StepFun-Formalizer: StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion · GitHub",
            "url": "https://github.com/stepfun-ai/StepFun-Formalizer"
          },
          {
            "title": "[2508.04440v1] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440v1"
          },
          {
            "title": "[2508.04440] StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/abs/2508.04440"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query:\n\n## LeanSearch v2\n\nLeanSearch v2 formulates global premise retrieval as the task of recovering the logically coherent set of library lemmas that an entire theorem's proof requires. LeanSearch v2 is a staged retrieval system whose standard mode achieves state-of-the-art Mathlib search without domain-specific fine-tuning. \n\nIts reasoning mode builds on standard mode as its retrieval substrate, targeting global premise retrieval through iterative sketch-retrieve-reflect cycles. On a 69-query benchmark of research-level Mathlib theorems, reasoning mode recovers 46.1% of ground-truth premise groups within 10 retrieved candidates, outperforming strong reasoning retrieval systems (38.0%) and premise-selection baselines (9.3%).\n\n## StepFun-Formalizer\n\nStepFun-Formalizer aims to translate natural-language mathematical statements into a formal language. The key abilities for effective autoformalization are comprehensive mastery of formal-language domain knowledge, and reasoning capability of natural language problem understanding and informal-formal alignment. Without the former, a model cannot identify the correct formal objects; without the latter, it struggles to interpret real-world contexts and map them precisely into formal expressions.\n\nStepFun-Formalizer introduces ThinkingF, the first data synthesis and training pipeline for the autoformalization model with both domain knowledge and informal-to-formal reasoning capability, implemented through large-scale distillation and selection of data with formal knowledge, and informal-to-formal reasoning trajectories synthesis guided by an expert-designed autoformalization template."
    ],
    "durationSeconds": 9.718622847999999,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "953f742f-f8b5-4093-8a5d-db29032951c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T16:06:30.437Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RA4ytMkj7VKBfHP9LanYNR`</summary>

```json
{
  "query": "Aria autoformalization ICLR 2026 retrieval iterative dependency graph homological"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09fd647e-8d2c-4dfc-ae09-853bbde9022f",
  "isSidechain": false,
  "requestId": "req_011CbVFfK9SRKkqGji1Q5B1S",
  "type": "assistant",
  "uuid": "a920db82-7cb6-4107-944a-a81dce5645e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015TW8ag9LdiojzDGdrZNt2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1339,
      "cache_read_input_tokens": 29489,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1339,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 29489,
          "cache_creation_input_tokens": 1339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1339
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

_source line 27 · 2026-05-28T16:06:38.036Z_

<details><summary>↩ Tool result · `toolu_01RA4ytMkj7VKBfHP9LanYNR`</summary>

```text
Web search results for query: "Aria autoformalization ICLR 2026 retrieval iterative dependency graph homological"

Links: [{"title":"Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview","url":"https://openreview.net/forum?id=CPxZClPMiy"},{"title":"ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://iclr.cc/virtual/2026/poster/10010860"},{"title":"[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520v1"},{"title":"[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/abs/2510.04520"},{"title":"[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251004520W/abstract"},{"title":"(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"},{"title":"ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE","url":"https://arxiv.org/pdf/2510.04520"}]

I found comprehensive information about the Aria paper. Here are the key details:

## Overview

Aria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.

## Problem Addressed

Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.

## Key Innovation

To ensure semantic correctness, Aria introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.

## Results on Benchmarks

On ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods. On FATE-X, a suite of challenging algebra problems from research literature, it outperforms the best baseline with 44.0% vs. 24.0% final accuracy. On a dataset of homological conjectures, Aria reaches 42.9% final accuracy while all other models score 0%.

This paper was submitted to ICLR 2026 and represents a significant advancement in automated theorem formalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a920db82-7cb6-4107-944a-a81dce5645e6",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "75d2a983-2715-4949-a267-41f77010520b",
  "toolUseResult": {
    "query": "Aria autoformalization ICLR 2026 retrieval iterative dependency graph homological",
    "results": [
      {
        "tool_use_id": "srvtoolu_013w5DtN4F74vjgF5MSnMrrh",
        "content": [
          {
            "title": "Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph | OpenReview",
            "url": "https://openreview.net/forum?id=CPxZClPMiy"
          },
          {
            "title": "ICLR Poster Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://iclr.cc/virtual/2026/poster/10010860"
          },
          {
            "title": "[2510.04520v1] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520v1"
          },
          {
            "title": "[2510.04520] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/abs/2510.04520"
          },
          {
            "title": "[Literature Review] Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.themoonlight.io/en/review/aria-an-agent-for-retrieval-and-iterative-auto-formalization-via-dependency-graph"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251004520W/abstract"
          },
          {
            "title": "(PDF) Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://www.researchgate.net/publication/396250696_Aria_An_Agent_For_Retrieval_and_Iterative_Auto-Formalization_via_Dependency_Graph"
          },
          {
            "title": "ARIA: AN AGENT FOR RETRIEVAL AND ITERATIVE",
            "url": "https://arxiv.org/pdf/2510.04520"
          }
        ]
      },
      "I found comprehensive information about the Aria paper. Here are the key details:\n\n## Overview\n\nAria (Agent for Retrieval and Iterative Autoformalization) is a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts.\n\n## Problem Addressed\n\nAccurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.\n\n## Key Innovation\n\nTo ensure semantic correctness, Aria introduces AriaScorer, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.\n\n## Results on Benchmarks\n\nOn ProofNet, it achieves 91.6% compilation success rate and 68.5% final accuracy, surpassing previous methods. On FATE-X, a suite of challenging algebra problems from research literature, it outperforms the best baseline with 44.0% vs. 24.0% final accuracy. On a dataset of homological conjectures, Aria reaches 42.9% final accuracy while all other models score 0%.\n\nThis paper was submitted to ICLR 2026 and represents a significant advancement in automated theorem formalization."
    ],
    "durationSeconds": 7.594540687,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a920db82-7cb6-4107-944a-a81dce5645e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T16:06:40.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012SrQFaKKhzRCkeXB91RRvQ`</summary>

```json
{
  "query": "IndiMathBench autoformalization domain-specific context Mathlib compilation BEq 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d2a983-2715-4949-a267-41f77010520b",
  "isSidechain": false,
  "requestId": "req_011CbVFg3WsgKkFqWkKF2efz",
  "type": "assistant",
  "uuid": "e7ce0dbf-0b8f-4404-a22a-5fb12d4f851b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VEhbbpw3V93eFgdGuohwg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 918,
      "cache_read_input_tokens": 30828,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 918,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 30828,
          "cache_creation_input_tokens": 918,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 918
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

_source line 29 · 2026-05-28T16:06:48.578Z_

<details><summary>↩ Tool result · `toolu_012SrQFaKKhzRCkeXB91RRvQ`</summary>

```text
Web search results for query: "IndiMathBench autoformalization domain-specific context Mathlib compilation BEq 2025"

Links: [{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/abs/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview","url":"https://openreview.net/forum?id=tmReo37kl2"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

Based on the search results, I found relevant information about IndiMathBench and the related concepts you queried:

## IndiMathBench Overview

IndiMathBench is composed of 312 formal Lean 4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads.

## Problem Domains

IndiMathBench problems are traditionally sourced from a fixed set of topics: algebra, euclidean geometry, elementary number theory, and combinatorics. Calculus, set theory, and linear algebra are not part of the official syllabus.

## Autoformalization Approach

The pipeline helps synthesize multiple candidate formalizations from an ensemble of LLMs, validating them using Lean prover, and finally summarizing results for the human validators through an interactive dashboard. Each LLM generation is conditioned on the natural language and documentation, and goes through a validation check by Lean. Errors are provided as feedback in subsequent iterations. The final generations from all LLMs are summarized by an LLM in a dashboard to help optimize annotation efficiency.

## BEq Evaluation Metric

Bidirectional Extended Definitional Equivalence (BEq) provides neural-symbolic equivalence checking. BEq significantly outperforms previous SOTA methods, improving the precision from 70.59% to 100% and the accuracy from 82.50% to 90.50%.

## Mathlib Compilation

Geometry problems are often under-represented by other datasets due to lack of representation in exams and the lack of support in the Lean + Mathlib ecosystem.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7ce0dbf-0b8f-4404-a22a-5fb12d4f851b",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "30d1b8ce-44cc-45b5-bf25-76cae58e6c0a",
  "toolUseResult": {
    "query": "IndiMathBench autoformalization domain-specific context Mathlib compilation BEq 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018ZGigfaQ6YpSMHgHtV5KMh",
        "content": [
          {
            "title": "INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-",
            "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"
          },
          {
            "title": "(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning ...",
            "url": "https://arxiv.org/pdf/2512.00997"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/html/2512.00997"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"
          },
          {
            "title": "[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/abs/2512.00997"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview",
            "url": "https://openreview.net/forum?id=tmReo37kl2"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2505.23486v1"
          }
        ]
      },
      "Based on the search results, I found relevant information about IndiMathBench and the related concepts you queried:\n\n## IndiMathBench Overview\n\nIndiMathBench is composed of 312 formal Lean 4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads.\n\n## Problem Domains\n\nIndiMathBench problems are traditionally sourced from a fixed set of topics: algebra, euclidean geometry, elementary number theory, and combinatorics. Calculus, set theory, and linear algebra are not part of the official syllabus.\n\n## Autoformalization Approach\n\nThe pipeline helps synthesize multiple candidate formalizations from an ensemble of LLMs, validating them using Lean prover, and finally summarizing results for the human validators through an interactive dashboard. Each LLM generation is conditioned on the natural language and documentation, and goes through a validation check by Lean. Errors are provided as feedback in subsequent iterations. The final generations from all LLMs are summarized by an LLM in a dashboard to help optimize annotation efficiency.\n\n## BEq Evaluation Metric\n\nBidirectional Extended Definitional Equivalence (BEq) provides neural-symbolic equivalence checking. BEq significantly outperforms previous SOTA methods, improving the precision from 70.59% to 100% and the accuracy from 82.50% to 90.50%.\n\n## Mathlib Compilation\n\nGeometry problems are often under-represented by other datasets due to lack of representation in exams and the lack of support in the Lean + Mathlib ecosystem."
    ],
    "durationSeconds": 8.038670138,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7ce0dbf-0b8f-4404-a22a-5fb12d4f851b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T16:06:48.581Z_

```json
{
  "parentUuid": "30d1b8ce-44cc-45b5-bf25-76cae58e6c0a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c55e71e8-2a6b-4e8e-924d-0cb3128c6585",
  "timestamp": "2026-05-28T16:06:48.581Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-28T16:06:51.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RgLjZN38D7LTVW36tzygUF`</summary>

```json
{
  "query": "\"domain-conditioned\" OR \"domain-adaptive\" retrieval autoformalization lean formalization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c55e71e8-2a6b-4e8e-924d-0cb3128c6585",
  "isSidechain": false,
  "requestId": "req_011CbVFgpXJhpoNtPZzi533b",
  "type": "assistant",
  "uuid": "01ec961c-2aba-44e2-bd11-1c1cdf5b69b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fe2EDuKWjwyup31c2uxReb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 31746,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 31746,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
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

_source line 32 · 2026-05-28T16:06:59.710Z_

<details><summary>↩ Tool result · `toolu_01RgLjZN38D7LTVW36tzygUF`</summary>

```text
Web search results for query: ""domain-conditioned" OR "domain-adaptive" retrieval autoformalization lean formalization 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"Formalization and autoformalization 2026-2027","url":"https://web.math.utk.edu/~yqing/lean.html"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"M2F: Automated Formalization of Mathematical Literature at Scale","url":"https://arxiv.org/pdf/2602.17016"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

Based on the search results, here are the relevant papers and research on domain-conditioned/domain-adaptive retrieval and autoformalization in Lean from 2025-2026:

## Key Papers Found:

1. **Intent-Aware Query Synthesis for Lean Formalization (ICLR 2026)**
   The work tackles autoformalization by synthesizing intent-rich, user-style queries from formal Lean statements. Unlike previous informalization approaches that simply translate formal statements into natural language, this pipeline explicitly models user intent and query phrasing. Injecting intent-aware signal during fine-tuning yields significant retrieval improvements on real user queries, and bridges the gap between informal user needs and the formal knowledge encoded in Lean libraries.

2. **CRAMF: Conceptual Retrieval-Augmented Mathematical Formalization**
   CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts. To address conceptual polymorphism, it proposes contextual query augmentation with domain- and application-level signals. It achieves up to 62.1% and an average of 29.9% relative improvement.

3. **Aria: An Agent For Retrieval and Iterative Auto-Formalization**
   This approach emulates an expert mathematician's workflow by recursively decomposing dependencies of definitions until they are well-grounded, then synthesizes their formal statements in a bottom-up order until the primary target is formalized.

4. **FineLeanCorpus Dataset**
   FineLeanCorpus (Peng et al., 2025) is a dataset of 509k NL/Lean4 pairs annotated with difficulty scores (1 to 10) and mathematical domain labels.

These papers demonstrate active research in domain-aware and context-sensitive retrieval methods for autoformalization in Lean during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01ec961c-2aba-44e2-bd11-1c1cdf5b69b0",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "f16eb74b-1a28-440c-86e1-8c69097f0b40",
  "toolUseResult": {
    "query": "\"domain-conditioned\" OR \"domain-adaptive\" retrieval autoformalization lean formalization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GWKxiPNvqqYEBYqsaBSdMJ",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.15940"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372v1"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/html/2508.06931"
          },
          {
            "title": "Formalization and autoformalization 2026-2027",
            "url": "https://web.math.utk.edu/~yqing/lean.html"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...",
            "url": "https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"
          },
          {
            "title": "M2F: Automated Formalization of Mathematical Literature at Scale",
            "url": "https://arxiv.org/pdf/2602.17016"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "Based on the search results, here are the relevant papers and research on domain-conditioned/domain-adaptive retrieval and autoformalization in Lean from 2025-2026:\n\n## Key Papers Found:\n\n1. **Intent-Aware Query Synthesis for Lean Formalization (ICLR 2026)**\n   The work tackles autoformalization by synthesizing intent-rich, user-style queries from formal Lean statements. Unlike previous informalization approaches that simply translate formal statements into natural language, this pipeline explicitly models user intent and query phrasing. Injecting intent-aware signal during fine-tuning yields significant retrieval improvements on real user queries, and bridges the gap between informal user needs and the formal knowledge encoded in Lean libraries.\n\n2. **CRAMF: Conceptual Retrieval-Augmented Mathematical Formalization**\n   CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts. To address conceptual polymorphism, it proposes contextual query augmentation with domain- and application-level signals. It achieves up to 62.1% and an average of 29.9% relative improvement.\n\n3. **Aria: An Agent For Retrieval and Iterative Auto-Formalization**\n   This approach emulates an expert mathematician's workflow by recursively decomposing dependencies of definitions until they are well-grounded, then synthesizes their formal statements in a bottom-up order until the primary target is formalized.\n\n4. **FineLeanCorpus Dataset**\n   FineLeanCorpus (Peng et al., 2025) is a dataset of 509k NL/Lean4 pairs annotated with difficulty scores (1 to 10) and mathematical domain labels.\n\nThese papers demonstrate active research in domain-aware and context-sensitive retrieval methods for autoformalization in Lean during 2025-2026."
    ],
    "durationSeconds": 8.515263420000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "01ec961c-2aba-44e2-bd11-1c1cdf5b69b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "f16eb74b-1a28-440c-86e1-8c69097f0b40",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Tool call

_source line 35 · 2026-05-28T16:07:02.274Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MesbMFjLD8JX6hWuA9eBjX`</summary>

```json
{
  "query": "Shebzukhov cycle consistency autoformalization 2026 arXiv 2603.24372 domain performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f16eb74b-1a28-440c-86e1-8c69097f0b40",
  "isSidechain": false,
  "requestId": "req_011CbVFhe8WLfxnicqMcEJY9",
  "type": "assistant",
  "uuid": "860ecdcc-5467-40ce-a09d-cc6c4c27bfda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WHpCQcTzFz4Ra1y1ik2C9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 32759,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 32759,
          "cache_creation_input_tokens": 901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 901
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

_source line 36 · 2026-05-28T16:07:10.301Z_

<details><summary>↩ Tool result · `toolu_01MesbMFjLD8JX6hWuA9eBjX`</summary>

```text
Web search results for query: "Shebzukhov cycle consistency autoformalization 2026 arXiv 2603.24372 domain performance"

Links: [{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"GitHub - YuzeHao2023/daily-arxiv-ai4math: 🎓Automatically Update AI4math Papers Daily using Github Actions","url":"https://github.com/YuzeHao2023/daily-arxiv-ai4math"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/html/2410.04194v1"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"}]

Based on the search results, here's what I found about this paper:

The paper "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning" by Arsen Shebzukhov was submitted to arXiv on March 25, 2026 (arXiv:2603.24372). The author is from the Department of Computer Science at Stanford University.

**Research Overview:**
The paper focuses on autoformalization - automatically translating natural language mathematical texts into formal proof language such as Lean4 - to help accelerate AI-assisted mathematical research.

**Methodology:**
The author fine-tunes Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus and considers three training regimes: supervised fine-tuning (SFT) with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization (GRPO) with a cycle consistency reward.

Cycle consistency measures how well the meaning of a statement is preserved through a NL to Lean4 to NL' loop, computed as cosine similarity of off-the-shelf sentence embeddings.

**Domain Performance Results:**
On an unseen subset of FineLeanCorpus (FLC) and on PutnamBench, RL substantially outperforms both SFT variants (mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench), while increasing cross-entropy loss by only 0.011 nats, with minimal impact on formalization quality.

Curriculum ordering provides no measurable benefit over shuffled training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "860ecdcc-5467-40ce-a09d-cc6c4c27bfda",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "f5e13e6e-7687-4cfb-9b47-f44998a68628",
  "toolUseResult": {
    "query": "Shebzukhov cycle consistency autoformalization 2026 arXiv 2603.24372 domain performance",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ng6EzxFGTBPixRCy8cW6Z",
        "content": [
          {
            "title": "[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/abs/2603.24372"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372"
          },
          {
            "title": "GitHub - YuzeHao2023/daily-arxiv-ai4math: 🎓Automatically Update AI4math Papers Daily using Github Actions",
            "url": "https://github.com/YuzeHao2023/daily-arxiv-ai4math"
          },
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/html/2410.04194v1"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/pdf/2603.24372"
          },
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/pdf/2410.04194"
          },
          {
            "title": "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/pdf/2510.24592"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\nThe paper \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning\" by Arsen Shebzukhov was submitted to arXiv on March 25, 2026 (arXiv:2603.24372). The author is from the Department of Computer Science at Stanford University.\n\n**Research Overview:**\nThe paper focuses on autoformalization - automatically translating natural language mathematical texts into formal proof language such as Lean4 - to help accelerate AI-assisted mathematical research.\n\n**Methodology:**\nThe author fine-tunes Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus and considers three training regimes: supervised fine-tuning (SFT) with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization (GRPO) with a cycle consistency reward.\n\nCycle consistency measures how well the meaning of a statement is preserved through a NL to Lean4 to NL' loop, computed as cosine similarity of off-the-shelf sentence embeddings.\n\n**Domain Performance Results:**\nOn an unseen subset of FineLeanCorpus (FLC) and on PutnamBench, RL substantially outperforms both SFT variants (mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench), while increasing cross-entropy loss by only 0.011 nats, with minimal impact on formalization quality.\n\nCurriculum ordering provides no measurable benefit over shuffled training."
    ],
    "durationSeconds": 8.021774088999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "860ecdcc-5467-40ce-a09d-cc6c4c27bfda",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T16:07:13.205Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Gj9b4iPv3PTKPiHTM7EUC`</summary>

```json
{
  "query": "KELPS knowledge equations autoformalization multi-language 2025 MiniF2F"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e13e6e-7687-4cfb-9b47-f44998a68628",
  "isSidechain": false,
  "requestId": "req_011CbVFiRS3fJJQ8G4Rjw8p8",
  "type": "assistant",
  "uuid": "04f91815-dcf0-4db4-9e60-90380d2eefcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134drMjPqi8akthynuaSqta",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 33660,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 33660,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 38 · 2026-05-28T16:07:20.185Z_

<details><summary>↩ Tool result · `toolu_014Gj9b4iPv3PTKPiHTM7EUC`</summary>

```text
Web search results for query: "KELPS knowledge equations autoformalization multi-language 2025 MiniF2F"

Links: [{"title":"[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/abs/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via","url":"https://arxiv.org/pdf/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/html/2507.08665"},{"title":"Autoformalization with Large Language Models","url":"https://www.emergentmind.com/topics/autoformalization-with-large-language-models"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

I found comprehensive information about KELPS. Here are the key findings:

## KELPS Framework Overview

KELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). The framework translates natural language into Knowledge Equations (KEs), a novel language designed and theoretically grounded in assertional logic. The KEs are then converted to target languages through rigorously defined rules that preserve both syntactic structure and semantic meaning.

## Key Results on MiniF2F

The process yielded a parallel corpus of over 60,000 problems, and the framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.

## Data Synthesis Approach

The framework proposes a data augmentation and expert iteration framework that combines a data synthesis module for generating various formalization data through randomized combinations of concepts and operators, along with an expert iteration process.

The research was published on arXiv in July 2025, making it a very recent contribution to the field of autoformalization and formal mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04f91815-dcf0-4db4-9e60-90380d2eefcc",
  "isSidechain": false,
  "promptId": "3dda546a-dde8-49b0-a4f4-e3f550381dcb",
  "type": "user",
  "uuid": "ab1ab1a8-8005-46fb-9295-2f938f9aa81a",
  "toolUseResult": {
    "query": "KELPS knowledge equations autoformalization multi-language 2025 MiniF2F",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fthrb13Z6ctn4FT6FZC2QK",
        "content": [
          {
            "title": "[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/abs/2507.08665"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via",
            "url": "https://arxiv.org/pdf/2507.08665"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/html/2507.08665"
          },
          {
            "title": "Autoformalization with Large Language Models",
            "url": "https://www.emergentmind.com/topics/autoformalization-with-large-language-models"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2505.23486v1"
          }
        ]
      },
      "I found comprehensive information about KELPS. Here are the key findings:\n\n## KELPS Framework Overview\n\nKELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). The framework translates natural language into Knowledge Equations (KEs), a novel language designed and theoretically grounded in assertional logic. The KEs are then converted to target languages through rigorously defined rules that preserve both syntactic structure and semantic meaning.\n\n## Key Results on MiniF2F\n\nThe process yielded a parallel corpus of over 60,000 problems, and the framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.\n\n## Data Synthesis Approach\n\nThe framework proposes a data augmentation and expert iteration framework that combines a data synthesis module for generating various formalization data through randomized combinations of concepts and operators, along with an expert iteration process.\n\nThe research was published on arXiv in July 2025, making it a very recent contribution to the field of autoformalization and formal mathematics."
    ],
    "durationSeconds": 6.975306465999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "04f91815-dcf0-4db4-9e60-90380d2eefcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-28T16:08:21.020Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough research to evaluate this proposal. Let me synthesize my findings and produce the evaluation.

Let me think carefully about this proposal:

## Summary of the Proposal
The proposal has two main contributions:
1. **Domain-Stratified Error Taxonomy**: Cross-tabulating APRIL's existing error categories (lme/mlme/thme/tme) by mathematical subdomain, plus building a finer-grained taxonomy from raw Lean compiler messages, all stratified by subdomain.
2. **Domain-Conditioned Retrieval and Prompting**: Extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions, plus domain-prefixed prompting with error patterns.


3. **Evaluating the Marginal Benefit**: The core question is whether dynamic per-problem domain conditioning meaningfully outperforms just prepending the predicted domain to the prompt with standard retrieval. IndiMathBench already demonstrated that static category-specific context helps significantly, so the real value hinges on whether the error taxonomy and domain reranker add enough improvement to justify the added complexity, especially for cross-domain problems and boundary cases where domain ambiguity matters.

4. **Novelty Concerns**: The error taxonomy is primarily a measurement study on existing data rather than a novel methodological contribution. The domain-conditioned retrieval is a straightforward engineering addition—boosting same-domain results in ranking—which isn't particularly surprising or counterintuitive. The leave-one-domain-out evaluation is methodologically sound but incremental. The fundamental insight that mathematical subdomains have different error patterns and retrieval needs is fairly intuitive, and a reviewer would likely anticipate this finding without the empirical confirmation.

5. **Significance Questions**: While the domain bias problem in autoformalization is real and documented, the solution's impact is unclear. The error taxonomy might reveal that certain subdomains have higher error rates, but without a compelling method to address this disparity, the contribution feels incomplete.
6. **Related Work**: The proposal demonstrates thorough coverage of existing literature with 30+ references, though this comprehensiveness may mask rather than highlight the core novelty. The differentiation from each work is articulated clearly.

Overall, this is a well-executed proposal addressing a genuine problem, but the solution leans heavily on engineering and analysis rather than introducing conceptual innovation. The approach risks being overshadowed by simpler baselines that achieve similar results.

The error taxonomy itself represents the more novel contribution, though it's fundamentally a measurement study. The domain-conditioned retrieval mechanism is a straightforward application of established IR techniques. For a top-tier venue like AAAI 2026, the empirical results would need to be exceptionally strong to offset the limited novelty — the idea quality alone probably sits around 20-30%.

Looking more closely at the novelty claim: the proposal does identify genuine gaps — no prior work has systematically cross-tabulated autoformalization errors by subdomain or applied subdomain-conditioned retrieval in this context. But these gaps might exist because the community hasn't found them particularly impactful. Domain-conditioned retrieval is well-established in information retrieval broadly, and its absence from autoformalization work could simply reflect that the real bottleneck lies elsewhere, in concept understanding rather than domain matching.

There's a critical question I need to examine: is domain conditioning actually the right lever here? LeanSearch v2 already achieves state-of-the-art retrieval without any domain conditioning, and DRIFT gets strong results through decomposition instead. If the best existing methods already work well without domain signals, adding domain conditioning might be redundant rather than beneficial. The proposal does include LeanSearch v2 as a baseline, which is good, but if it's already capturing domain-relevant information implicitly through semantic matching, the domain signal could be superfluous.

What's genuinely commendable is the pre-registration of quantitative hypotheses with specific thresholds and a commitment to reporting negative results — that's solid scientific practice. The error taxonomy also has a reasonable dual-outcome structure where domain-invariant errors would still constitute a meaningful finding.

Stepping back to assess the whole thing: the novelty is medium — the gaps are real but the solutions are straightforward applications of existing techniques. The significance is also medium — domain bias is a documented problem, and if the full pipeline shows improvements on weak domains that would be useful, but not necessarily impactful. The related work coverage is strong and thorough. I'd estimate this at around 20-30% probability of acceptance, with a median of 25%. It's competent work, but the core finding would likely feel expected rather than surprising.

Though I should reconsider whether I'm being fair here. Let me think about what could actually make this stronger than my initial assessment.

The error taxonomy could be genuinely novel if the JSD and prediction hypotheses hold — it would be the first empirical evidence that autoformalization errors cluster systematically by subdomain, which has implications far beyond this specific pipeline. The leave-one-domain-out evaluation is also a methodological contribution the community doesn't currently have. And the combination of error analysis, retrieval conditioning, and domain-aware prompting might create something more cohesive than the individual pieces suggest.

But the counterargument is that the error taxonomy itself is lower-impact, the overall approach reads more like engineering diligence than research insight, and the proposal's length and exhaustive detail suggest the authors are compensating for conceptual depth with thoroughness rather than presenting a genuinely novel idea.

The scale of the effort — 200 H100-hours, 17 weeks, three stages with six ablations across multiple datasets — actually works against the proposal. It signals that no single contribution is strong enough to carry the work on its own, and the high engineering-to-novelty ratio is concerning. Plus, building on a Stanford course project's observation about domain performance variation suggests the underlying analysis isn't particularly sophisticated to begin with.

My final read: the core insight that errors cluster by domain might be too obvious, and the domain-conditioned retrieval approach may not convincingly outperform simpler baselines like LeanSearch v2 or DRIFT — which would undermine the whole premise. The related work is thorough, but novelty and significance both feel middling. I'm settling on 24% as my median probability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab1ab1a8-8005-46fb-9295-2f938f9aa81a",
  "isSidechain": false,
  "requestId": "req_011CbVFj9hn1ZvH4nG9GABnT",
  "type": "assistant",
  "uuid": "f0680da8-37a2-48bc-9c88-db50266aee92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ihhQ7nagFEmyY3msku4qA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 34505,
      "output_tokens": 7065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7065,
          "cache_read_input_tokens": 34505,
          "cache_creation_input_tokens": 707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 707
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

_source line 40 · 2026-05-28T16:10:11.917Z_

Now I have sufficient research to conduct a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- **CRAMF (ICLR 2026)**: 概念级检索增强自动形式化，通过 contextual query augmentation 消歧多义概念，基于 26k Mathlib 定义知识库，实现平均 29.9% 相对提升。与本 proposal 关系：proposal 在 CRAMF 之上添加 domain-aware reranking layer，属于直接扩展。CRAMF 本身已包含 module path (θ_p) 但未利用 subdomain 信号进行 retrieval conditioning。
- **DRIFT (ICLR 2026 Poster)**: 将 statement 分解为 ~5.8 个 atomic sub-queries 进行 concept-level retrieval。与本 proposal 关系：DRIFT 在 concept-level decomposition 层面工作，proposal 声称其 domain conditioning 信号与 DRIFT 正交。验证属实——二者操作粒度不同。
- **Aria (ICLR 2026)**: Agent-based 依赖图分解 + 迭代形式化，在 homological conjectures 上 42.9% vs. 所有 baseline 0%。与本 proposal 关系：Aria 的结果是 proposal 引用的最强 peer-reviewed domain bias 证据。Aria 本身没有 domain conditioning。描述准确。
- **LeanSearch v2 (arXiv, May 2026)**: 通过 hierarchy-informed informalization 实现 SOTA premise retrieval (nDCG@10 = 0.623)，无任何 domain-specific fine-tuning。与本 proposal 关系：这是关键 domain-agnostic baseline——如果 LeanSearch v2 通过语义匹配已经隐式捕获了 domain 信号，那 domain conditioning 可能冗余。
- **APRIL (arXiv 2602.02990)**: 260k repair tuples，含 error_type field (lme/mlme/thme/tme) 和 raw error field + path field。与本 proposal 关系：proposal 的 Stage 1 error taxonomy 完全建立在 APRIL 数据集上，通过 cross-tabulation path 与 error_type 实现 domain stratification。论文描述准确。
- **MSC-180 (arXiv 2512.18256)**: 60 个数学分支、180 道题，best model pass@32 仅 18.89%，CV 值 4–6× 高于 high-variability 阈值。与本 proposal 关系：domain bias 的核心量化证据之一。描述准确。
- **IndiMathBench (arXiv 2512.00997)**: 312 Lean4 定理，static category-specific Mathlib context 使编译率从 4.1% → 77.9%，但 BEq 仅 17.3%。与本 proposal 关系：proposal 将其作为 naive baseline ablation，测试 static domain awareness 是否足够。描述基本准确。
- **StepFun-Formalizer (AAAI 2026)**: Knowledge-reasoning fusion，BEq@1 40.5% on FormalMATH-Lite。与本 proposal 关系：current SOTA aggregate baseline，no domain conditioning。描述准确。
- **Shebzukhov (arXiv 2603.24372)**: Stanford CS224N course project，cycle consistency fine-tuning，number theory 0.722 vs. calculus 0.516。与本 proposal 关系：proposal 正确指出这是 observational analysis without error classification。注意这是课程项目而非正式研究论文。
- **KELPS (ICML 2025 AI4Math Workshop, arXiv 2507.08665)**: Knowledge Equations 中间表示，MiniF2F pass@1 88.9%。Domain-agnostic，跨 6 个数学主题。与本 proposal 关系：无 domain conditioning 的另一个 SOTA baseline。描述准确。
- **LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477)**: Neural premise selection for Lean proving，project-level variation 0%–38%。与本 proposal 关系：domain-dependent difficulty 的额外证据，但针对 proving 而非 autoformalization。

- **调研总结**: Autoformalization 领域在 2025–2026 经历快速发展，retrieval-augmented 方法（CRAMF, DRIFT, LeanSearch v2, Aria）已非常成熟但均为 domain-agnostic。Domain bias 已被多项工作量化记录（MSC-180, FormalMATH, Aria, IndiMathBench），但目前**没有工作**将 domain conditioning 作为 retrieval ranking 的动态 per-problem 信号，也没有工作对 autoformalization errors 进行 domain-stratified 分析。Proposal 识别的 gap 是真实的。

【Trivial Alternative 检验】:
最直接的 trivial alternative 是 **IndiMathBench 式的 static category context**：给输入 prepend 一个 domain-specific Mathlib context block。IndiMathBench 已证明这能将编译率从 4.1% 提升到 77.9%。

Proposal 确实意识到了这个威胁，并将其列为 ablation (e)。但核心问题在于：proposal 的 **增量价值** 取决于 dynamic conditioning 相比 static context 的提升幅度。如果 ablation (e) 能捕获 80%+ 的语义正确性提升（proposal 自己也承认了这种可能性），那整个 pipeline 的复杂度就很难 justify。

此外，**LeanSearch v2 的 SOTA domain-agnostic retrieval** 构成另一个 trivial alternative 威胁：如果好的语义匹配已经隐式捕获了 domain 信号（比如 topology query 自然匹配 topology definitions），那 explicit domain conditioning 在 retrieval 层面的边际收益可能很小。

**增量价值的最强论点**在于 cross-domain problems（number theory 依赖 analysis typeclasses 的场景），这确实是 static context 和 pure semantic matching 难以处理的。但这类 cross-domain 案例在评估数据中占多大比例、能否产生统计显著的整体提升，是一个实证问题，proposal 层面无法回答。

**对于 error taxonomy 部分**，trivial alternative 是：直接在 APRIL 上跑几行 pandas group-by + chi-squared test，不需要构建 pipeline。这实质上是数据分析工作而非方法创新。Proposal 通过添加 predictive power test 和 mitigation recommendations 来提升这部分的价值，但底层操作仍然比较 routine。

【前提假设检验】:
核心逻辑链中有以下未经验证的关键假设：

1. **"Mathlib module path ≈ mathematical subdomain" 的映射假设**：Proposal 将 APRIL 的 path field 聚类为 5 个 subdomain。但 Mathlib 的模块结构是代码组织结构，不完全等同于数学学科分类。例如 `Mathlib.Topology.Algebra` 同时涉及 topology 和 algebra；`Mathlib.Analysis.SpecificLimits` 可能被归入 analysis 但实际处理 number theory 问题。这个映射的质量直接影响 Stage 1 taxonomy 的有效性和 Stage 2 reranker 的 training signal。如果映射噪声大，所有下游结论都受影响。

2. **"Error type distribution 在 domain 间显著不同" 的核心假设**：Proposal 假设 JSD > 0.3（至少 3 domain pairs）。但 APRIL 的 error_type 只有 4 个 mutation 类别（lme/mlme/thme/tme），其中 thme 占 59.5%。在这么粗粒度的分类和极度不均衡的分布下，domain 间的分布差异可能主要被 thme 的 overwhelming dominance 所淹没。finer-grained taxonomy（从 raw error messages 中 parse）可能更有区分力，但其构建质量取决于 Lean compiler message 的多样性和 parsing 规则的覆盖率——这些都未验证。

3. **"Domain conditioning 的收益主要来自 retrieval reranking 而非 prompting" 的隐含假设**：Pipeline 同时引入 domain-conditioned retrieval (Stage 2) + domain-prefixed prompting (Stage 3)，但如果收益主要来自 prompting（成本极低），那 retrieval reranker 的工程投入就难以 justify。反之亦然。Ablation 可以分离这两个信号，但 proposal 层面无法预判哪个是主要贡献者。

4. **"5 个 subdomain cluster 的粒度是最优的"**：Proposal 提到 3–7 cluster 的 hyperparameter sweep，但对于 Mathlib 的 ~4000+ 模块，5 个 cluster 可能太粗（loss of information）或太细（某些 cluster 样本不足）。没有先验理由认为 5 是合适的。

【3 维度打分】:

1. **Novelty: 中** —
   Proposal 识别的两个 gap（domain-stratified error taxonomy + dynamic domain-conditioned retrieval）确实是真实存在的空白，经过调研验证：CRAMF、DRIFT、LeanSearch v2、Aria 等 SOTA 方法均未进行 per-problem domain conditioning；APRIL 的 error_type 确实从未按 subdomain 交叉分析。

   **但**，这两个贡献的 novelty 质地存在问题：
   - **Error taxonomy** 本质上是在已有数据集（APRIL）上做 cross-tabulation 统计分析（group-by + JSD + chi-squared），这是一种 measurement/analysis 贡献而非方法论创新。虽然 proposal 通过 pre-registered hypotheses 和 dual-outcome 设计增加了科学严谨性，但操作本身的 conceptual novelty 有限。
   - **Domain-conditioned retrieval** 是 information retrieval 领域的标准技术（domain/facet-conditioned reranking），将其应用于 autoformalization 是一种 application-level adaptation，而非新算法或新范式。类似的 domain-aware reranking 在 biomedical IR、legal IR 等领域已有大量先例。
   - 两个贡献加在一起，核心 insight 可以概括为 "数学子领域不同 → 错误模式不同 → 应该给不同领域不同的检索和提示"，这在概念层面并不 surprising——审稿人大概率会评价为 "I would have guessed this"。

   **支撑证据**：LeanSearch v2 在无任何 domain conditioning 的情况下达到 SOTA retrieval 性能，说明 domain signal 对 retrieval 质量的边际贡献可能有限。IndiMathBench 的 static context 已证明简单的 domain awareness 就能大幅提升编译率。这使得 proposal 的"动态 conditioning"的增量价值不确定。

2. **Significance: 中** —
   Domain bias 在 autoformalization 中的存在是 well-documented 的（MSC-180 CV 4–6×, FormalMATH 50% vs. 0%, Aria 42.9% vs. 0%），这确实是一个真实的问题。如果 proposal 能在弱势领域（analysis, discrete math, topology）上显示 disproportionate improvement，这会是有用的贡献。

   **但**，significance 受以下因素限制：
   - Error taxonomy 如果仅确认 "topology 的 typeclass error 比例更高" 这类直觉性结论，对领域的推进有限。真正有 impact 的是 taxonomy 导出的 actionable mitigation strategies 是否真的 work（≥5 pp improvement），但这已经是实验层面的事。
   - 整个 pipeline 的影响范围限于 autoformalization 这个相对小众的子领域。虽然 autoformalization 在 AI for Math 领域越来越重要（从 proposal 引用的 30+ 篇 2025–2026 论文可见），但 domain-conditioned retrieval 对更广泛 AI 领域的启示有限。
   - Leave-one-domain-out evaluation protocol 是 methodological 贡献，有一定持久价值，但单独撑不起一篇论文。

3. **Related Work: 强** —
   这是 proposal 最强的维度。覆盖极其全面——从 ICLR 2025 (Herald, DDR) 到 AAAI 2026 (StepFun-Formalizer, SITA) 到 ICLR 2026 (CRAMF, DRIFT, Aria, ProofBridge, LeanHammer) 到最新的 arXiv preprints (LeanSearch v2, CAM-Bench, MathAtlas)。每篇工作的描述经过调研验证基本准确。差异化定位清晰——明确指出了与 CRAMF (concept-level), DRIFT (decomposition-level), LeanSearch v2 (domain-agnostic quality), IndiMathBench (static context) 各自的不同层次。也诚实地处理了 IndiMathBench 的 desk-rejection 状态和 Shebzukhov 的 course project 性质。唯一的小瑕疵是引用数量过多（30+ references），给人一种 "通过穷举差异化来构建 novelty narrative" 的感觉，而非通过核心 insight 的力量来自然建立优势。

【概率估计】: [18% - 28%] 中位 23%

【估计理由】:
- **Novelty (中)** 是主要限制上界的因素。核心 insight（"不同数学子领域有不同错误模式，应该做 domain conditioning"）在概念层面不够 surprising。Error taxonomy 是数据分析工作，domain-conditioned retrieval 是标准 IR 技术在新场景的应用。审稿人可能会写 "the observation that different mathematical domains have different error patterns is not particularly surprising"。
- **Significance (中)** 进一步限制了概率。问题是真实的但影响范围较窄（autoformalization 子领域内），且 trivial alternative 威胁（IndiMathBench-style static context, LeanSearch v2 domain-agnostic retrieval）可能侵蚀大部分收益。
- **Related Work (强)** 是正面因素，但在 AAAI review 中 related work coverage 通常不是决定性因素——它能保护下限但不提升上限。
- Proposal 的 pre-registered hypotheses 和 dual-outcome 设计展示了良好的科学规范，值得加分，但这是 execution quality 而非 idea quality。
- 整体判断：这是一个 "solid but unsurprising" 的 proposal，在一个竞争激烈的快速发展领域中，execution 需要非常出色才能补偿 novelty 的不足。

【主要风险】:
1. **核心发现可能是 "expected"**：如果 error taxonomy 确认了 intuitive patterns（topology → typeclass errors, algebra → coercion errors），审稿人会认为这是 confirmatory analysis 而非 discovery，大幅降低 novelty 评分。
2. **Dynamic conditioning 可能被 strong domain-agnostic baselines subsumed**：LeanSearch v2 在无 domain conditioning 下已达 SOTA retrieval，如果 proposal 的 domain reranker 相对 LeanSearch v2 提升不显著（例如 <3 pp BEq improvement），整个 pipeline 的 engineering complexity 就难以 justify。
```

Sources:
- [CRAMF: Automated Formalization via Conceptual Retrieval-Augmented LLMs](https://arxiv.org/html/2508.06931)
- [DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems](https://arxiv.org/html/2510.10815)
- [Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph](https://arxiv.org/abs/2510.04520)
- [APRIL: Learning to Repair Lean Proofs from Compiler Feedback](https://arxiv.org/abs/2602.02990)
- [MSC-180: A Benchmark for Automated Formal Theorem Proving](https://arxiv.org/abs/2512.18256)
- [IndiMathBench: Autoformalizing Mathematical Reasoning Problems](https://arxiv.org/abs/2512.00997)
- [StepFun-Formalizer (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40691)
- [Shebzukhov: Improving Lean4 Autoformalization via Cycle Consistency](https://arxiv.org/abs/2603.24372)
- [KELPS: Verified Multi-Language Autoformalization](https://arxiv.org/abs/2507.08665)
- [LeanSearch v2: Global Premise Retrieval for Lean 4](https://arxiv.org/abs/2605.13137)
- [LeanPremise/LeanHammer (ICLR 2026)](https://arxiv.org/pdf/2506.07477)
- [Autoformalization in the Era of LLMs: A Survey](https://arxiv.org/abs/2505.23486)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0680da8-37a2-48bc-9c88-db50266aee92",
  "isSidechain": false,
  "requestId": "req_011CbVFj9hn1ZvH4nG9GABnT",
  "type": "assistant",
  "uuid": "a5f49708-15bb-42de-8a43-3e8e3655ada5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ihhQ7nagFEmyY3msku4qA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 34505,
      "output_tokens": 7065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 707,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7065,
          "cache_read_input_tokens": 34505,
          "cache_creation_input_tokens": 707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 707
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "a5f49708-15bb-42de-8a43-3e8e3655ada5",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "a5f49708-15bb-42de-8a43-3e8e3655ada5",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "7bdd77b8-a434-4224-a75c-b5980a790fa9"
}
```

---
