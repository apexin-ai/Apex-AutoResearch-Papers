# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Domain-Adaptive Autoformalization

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/bc7209e1-a2da-4e76-a137-a19f2189e49b.jsonl`
- **Structured JSON:** [`c7bebf5773ca6351b180.json`](../../sessions/c7/c7bebf5773ca6351b180.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T16:01:16.246Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T16:01:16.246Z",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\n\n## Core Problem\n\nCurrent autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Furthermore, error characterization remains under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that even with 87–99% compilation rates, post-compilation semantic unfaithfulness is pervasive, identifying fabrication, mistranslation, omission, and contradiction as distinct failure modes — but this post-compilation taxonomy is not stratified by mathematical subdomain either. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?\n\n## Research Opportunity\n\nSix critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed; and (8) CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides 1,000 Lean proof targets specifically in computational and applied mathematics (optimization, numerical linear algebra, numerical analysis) — a concurrent domain-specific benchmark demonstrating growing community recognition that domain-specialized evaluation is necessary, as existing benchmarks predominantly cover algebraic and olympiad-style domains. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\n\n## Research Landscape\n\nCurrent SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. CAM-Bench (Long et al., arXiv 2605.17255, May 2026) provides a concurrent 1,000-target Lean benchmark specifically for computational and applied mathematics (optimization, numerical linear algebra, numerical analysis), complementing existing algebraic-heavy benchmarks and independently validating community demand for domain-specific formalization evaluation. Error characterization in autoformalization is under-explored at multiple layers: at the pre-compilation level, repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain — notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. At the post-compilation semantic level, Kim et al. ('Do LLMs Game Formalization?', arXiv 2604.19459, VerifAI-2 Workshop @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive semantic unfaithfulness, identifying four categories — fabrication (axiom fabrication, conclusion-as-axiom), mistranslation (wrong connective/quantifier/predicate/scope), omission (missing axiom, dropped antecedent), and contradiction (proof by explosion) — but this post-compilation taxonomy operates on FOL problems without mathematical subdomain stratification. Together, these gaps confirm that error characterization is under-explored at BOTH the pre-compilation compiler-error layer (where our taxonomy contributes domain-stratified analysis of APRIL's errors) and the post-compilation semantic-faithfulness layer (where Kim et al.'s taxonomy provides a complementary classification). The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).\n\n## Proposed Approach\n\nWe build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is a competitive open-source formalizer at this scale, chosen for its Lean4-specific training — while StepFun-Formalizer-7B achieves higher BEq@1 on ProverBench (25.1% vs. 16.3%), this comparison has noted confounds (Goedel-V2's training prompt omits BEq-required headers) and Goedel-V2 provides the most directly comparable Lean4-native architecture for domain-adaptive fine-tuning; Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. Our pre-compilation compiler-error taxonomy is complementary to Kim et al.'s post-compilation semantic faithfulness taxonomy (fabrication, mistranslation, omission, contradiction; arXiv 2604.19459), which demonstrates that even 87–99% compilation rates mask pervasive semantic unfaithfulness but does not stratify by mathematical subdomain — together, these taxonomies characterize error structure at both layers of the formalization stack. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. Dynamic per-problem conditioning systematically outperforms static context in three scenarios that static category blocks cannot address: (a) **cross-domain problems** — a number theory result about Dirichlet series may depend on analysis-level typeclasses (`TopologicalSpace`, `MeasureSpace`) and complex analysis lemmas, requiring retrieval from both NumberTheory and Analysis Mathlib modules simultaneously, which single-category static context keyed to 'number theory' alone would miss entirely; (b) **domain-boundary ambiguity** — problems in algebraic topology or analytic number theory where the correct subdomain assignment is inherently ambiguous and static context commits to a single wrong category, whereas dynamic conditioning produces a soft probability distribution over domains, weighting retrieval from multiple relevant modules proportionally; (c) **retrieval precision at K≥20** — domain filtering acts as a noise reduction mechanism, suppressing semantically similar but domain-irrelevant definitions (e.g., filtering out algebraic `norm` when the problem requires analytic `norm`) that inflate retrieval sets at higher K values, reducing the proportion of distractors that degrade downstream formalization accuracy — a filtering effect unavailable to static context blocks that operate only on the prompt, not on the retrieval ranking itself. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). CAM-Bench's optimization/numerical-analysis/linear-algebra targets provide an additional out-of-distribution evaluation on applied mathematics domains underrepresented in our training data. We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\n\n## Detailed Description\n\nWe propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Error characterization is under-explored at multiple layers of the formalization stack: Kim et al. (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) demonstrate that 87–99% compilation rates mask pervasive post-compilation semantic unfaithfulness (fabrication, mistranslation, omission, contradiction), while no prior work stratifies pre-compilation compiler errors by mathematical subdomain. CAM-Bench (Long et al., arXiv 2605.17255) independently validates community demand for domain-specific formalization evaluation with 1,000 targets in applied mathematics. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing both the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis and Kim et al.'s post-compilation semantic faithfulness taxonomy with pre-compilation domain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). Dynamic conditioning specifically addresses scenarios that static context cannot: cross-domain problems requiring retrieval across multiple Mathlib modules (e.g., number theory depending on analysis typeclasses), domain-boundary ambiguity where soft probability distributions over domains outperform hard single-category assignment, and retrieval noise reduction at K≥20 by filtering domain-irrelevant definitions from the ranking. We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\n\n## Key References\n\n- Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\n- Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\n- ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\n- FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\n- CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\n- FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\n- MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\n- Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\n- StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\n- SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\n- Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\n- Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\n- ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\n- ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\n- Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\n- DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\n- Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)\n- IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\n- Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\n- Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\n- M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\n- Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\n- 130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\n- MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\n- LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\n- KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)\n- ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\n- FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\n- Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (Kim et al., VerifAI-2 Workshop @ ICLR 2026; arXiv 2604.19459)\n- CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean (Long et al., arXiv 2605.17255)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h), timeline: 17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF + CAM-Bench, 3w writing + revision), estimated_gpu_cost: $500 (H100 at ~$2.50/hr average via RunPod/Lambda)\n- **human_in_loop**: gpu_hours: ~200 H100-hours, timeline: 13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis), claude_api_cost: $300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis), estimated_gpu_cost: $500\n- **auto_research**: gpu_hours: ~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF + CAM-Bench: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h), timeline: 11 weeks, claude_api_cost: $450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting), estimated_gpu_cost: $500, speed_bottleneck: Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T16:01:16.252Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T16:01:16.252Z",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-28T16:01:16.276Z_

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
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "c6f90209-eb74-490c-a4f0-9b0326f051bf",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T16:01:16.273Z_

```json
{
  "parentUuid": "c6f90209-eb74-490c-a4f0-9b0326f051bf",
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
  "uuid": "a7e03416-6c43-4f34-bedb-8e27b34992bb",
  "timestamp": "2026-05-28T16:01:16.273Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T16:01:16.273Z_

```json
{
  "parentUuid": "a7e03416-6c43-4f34-bedb-8e27b34992bb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "540cc528-721c-4670-9057-eec48aa445ed",
  "timestamp": "2026-05-28T16:01:16.273Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
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
  "leafUuid": "540cc528-721c-4670-9057-eec48aa445ed",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Assistant

_source line 8 · 2026-05-28T16:01:24.503Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed proposal about domain-adaptive autoformalization. Let me carefully analyze it before doing any web searches. Let me first understand the core claims:

1. **Core Problem**: Current autoformalization systems treat all mathematical subdomains identically, but there's severe domain bias (some domains get 0% accuracy while others get 50%+).

2. **Proposed Solution**: A three-stage pipeline:
   - Stage 1: Domain-stratified error taxonomy (cross-tabulating APRIL's error types by mathematical subdomain)
   - Stage 2: Domain-conditioned retrieval (boosting same-subdomain definitions in retrieval)
   - Stage 3: Domain-aware autoformalization (domain-prefixed prompting + LoRA fine-tuning)

3. **Key Claims**:
   - First domain-stratified error taxonomy for autoformalization
   - First dynamic per-problem domain-conditioned retrieval for autoformalization
   - First systematic multi-domain rotation evaluation protocol

Now I need to search the literature to verify these claims and understand the current state of the field.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "540cc528-721c-4670-9057-eec48aa445ed",
  "isSidechain": false,
  "requestId": "req_011CbVFGL1Pv2GDzGsoSuvMD",
  "type": "assistant",
  "uuid": "112a2b0d-f2cb-4cbb-a564-4d4f505ebe05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehyx6Wz3EWPfPG9oTVzTk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14747,
      "cache_read_input_tokens": 11014,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 362,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14747
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

_source line 9 · 2026-05-28T16:01:24.506Z_

I need to conduct thorough research before evaluating this proposal. Let me search for the current state of autoformalization research and verify the key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "112a2b0d-f2cb-4cbb-a564-4d4f505ebe05",
  "isSidechain": false,
  "requestId": "req_011CbVFGL1Pv2GDzGsoSuvMD",
  "type": "assistant",
  "uuid": "c7708f3f-fb0b-48f0-988f-a4756f0cdfaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehyx6Wz3EWPfPG9oTVzTk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14747,
      "cache_read_input_tokens": 11014,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 362,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14747
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

_source line 10 · 2026-05-28T16:01:24.510Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EkyDKVR3bRnxLc4CphxmMR`</summary>

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
  "parentUuid": "c7708f3f-fb0b-48f0-988f-a4756f0cdfaf",
  "isSidechain": false,
  "requestId": "req_011CbVFGL1Pv2GDzGsoSuvMD",
  "type": "assistant",
  "uuid": "aeae3fe0-6b93-4d0e-afaa-e1f2876707e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehyx6Wz3EWPfPG9oTVzTk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14747,
      "cache_read_input_tokens": 11014,
      "output_tokens": 362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 362,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14747
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

_source line 11 · 2026-05-28T16:01:24.519Z_

<details><summary>↩ Tool result · `toolu_01EkyDKVR3bRnxLc4CphxmMR`</summary>

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
  "parentUuid": "aeae3fe0-6b93-4d0e-afaa-e1f2876707e7",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "6343fe4b-e119-48e1-a8ed-c685b5500a53",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "aeae3fe0-6b93-4d0e-afaa-e1f2876707e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T16:01:28.608Z_

Now let me conduct the required research. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6343fe4b-e119-48e1-a8ed-c685b5500a53",
  "isSidechain": false,
  "requestId": "req_011CbVFGwQsi26XEyQERVbfn",
  "type": "assistant",
  "uuid": "003969f9-9c87-4f89-9079-667f815e937d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZmW3KjNVqUxkAjscNxR5z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 25761,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 25761,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 889
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

_source line 13 · 2026-05-28T16:01:28.787Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NLaJiw6JyD6NjGGGVcqZUt`</summary>

```json
{
  "query": "domain-adaptive autoformalization mathematical subdomain conditioning retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "003969f9-9c87-4f89-9079-667f815e937d",
  "isSidechain": false,
  "requestId": "req_011CbVFGwQsi26XEyQERVbfn",
  "type": "assistant",
  "uuid": "14205832-2494-45d1-9d8a-60f004bb9f23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZmW3KjNVqUxkAjscNxR5z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 25761,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 25761,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 889
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

_source line 14 · 2026-05-28T16:01:36.212Z_

<details><summary>↩ Tool result · `toolu_01NLaJiw6JyD6NjGGGVcqZUt`</summary>

```text
Web search results for query: "domain-adaptive autoformalization mathematical subdomain conditioning retrieval 2025 2026"

Links: [{"title":"Consistent Autoformalization for Constructing Mathematical Libraries","url":"https://arxiv.org/pdf/2410.04194"},{"title":"Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS","url":"https://arxiv.org/pdf/2510.10815"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion","url":"https://arxiv.org/pdf/2508.04440"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"}]

I found several relevant research papers and resources on autoformalization and related topics from 2025-2026. Here are the key findings:

## Recent Autoformalization Research

The field is moving toward applying autoformalization to large mathematical libraries, with approaches like most-similar retrieval augmented generation (MS-RAG) combined with denoising steps and syntax error feedback to improve autoformalization quality.

DRIFT (Decompose, Retrieve, Illustrate, then Formalize Theorems) is a framework that breaks down informal mathematical statements into atomic sub-queries and contextualizes retrieved premises with demonstrative theorems.

StepFun-Formalizer-32B achieves state-of-the-art BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.

Aria is an approach that recursively decomposes dependencies of definitions until they are well-grounded, then synthesizes formal statements in a bottom-up order, with a compiler-in-the-loop reflection mechanism employed at each step.

Autoformalization—the translation of natural language mathematical problems into formal, machine-verifiable statements—remains a critical bottleneck that is labor-intensive and poses great challenges even for human experts.

The research indicates active progress in domain-adaptive methods, retrieval-augmented approaches, and specialized model development for autoformalization tasks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14205832-2494-45d1-9d8a-60f004bb9f23",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "2833dbaf-bde3-4613-a873-a161e2cec199",
  "toolUseResult": {
    "query": "domain-adaptive autoformalization mathematical subdomain conditioning retrieval 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CxY3hVddjCTFMj3ZF6JqGW",
        "content": [
          {
            "title": "Consistent Autoformalization for Constructing Mathematical Libraries",
            "url": "https://arxiv.org/pdf/2410.04194"
          },
          {
            "title": "Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS",
            "url": "https://arxiv.org/pdf/2510.10815"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion",
            "url": "https://arxiv.org/pdf/2508.04440"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2505.23486"
          },
          {
            "title": "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/pdf/2510.24592"
          },
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          }
        ]
      },
      "I found several relevant research papers and resources on autoformalization and related topics from 2025-2026. Here are the key findings:\n\n## Recent Autoformalization Research\n\nThe field is moving toward applying autoformalization to large mathematical libraries, with approaches like most-similar retrieval augmented generation (MS-RAG) combined with denoising steps and syntax error feedback to improve autoformalization quality.\n\nDRIFT (Decompose, Retrieve, Illustrate, then Formalize Theorems) is a framework that breaks down informal mathematical statements into atomic sub-queries and contextualizes retrieved premises with demonstrative theorems.\n\nStepFun-Formalizer-32B achieves state-of-the-art BEq@1 scores of 40.5% on FormalMATH-Lite and 26.7% on ProverBench.\n\nAria is an approach that recursively decomposes dependencies of definitions until they are well-grounded, then synthesizes formal statements in a bottom-up order, with a compiler-in-the-loop reflection mechanism employed at each step.\n\nAutoformalization—the translation of natural language mathematical problems into formal, machine-verifiable statements—remains a critical bottleneck that is labor-intensive and poses great challenges even for human experts.\n\nThe research indicates active progress in domain-adaptive methods, retrieval-augmented approaches, and specialized model development for autoformalization tasks in 2025-2026."
    ],
    "durationSeconds": 7.421790294999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "14205832-2494-45d1-9d8a-60f004bb9f23",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T16:01:38.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018FpumP3GMLoQ4GNJZQgT84`</summary>

```json
{
  "query": "APRIL repair tuples Lean autoformalization error taxonomy domain stratified 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2833dbaf-bde3-4613-a873-a161e2cec199",
  "isSidechain": false,
  "requestId": "req_011CbVFHo1P6gPxW1gMjzUuA",
  "type": "assistant",
  "uuid": "0b945ff4-4f3b-4427-897a-1dea1a3b6d90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011v8SYSbHoCZzRxPq6H3z5v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 26650,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 26650,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 16 · 2026-05-28T16:01:48.010Z_

<details><summary>↩ Tool result · `toolu_018FpumP3GMLoQ4GNJZQgT84`</summary>

```text
Web search results for query: "APRIL repair tuples Lean autoformalization error taxonomy domain stratified 2026"

Links: [{"title":"[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/abs/2602.02990"},{"title":"Paper page - Learning to Repair Lean Proofs from Compiler Feedback","url":"https://huggingface.co/papers/2602.02990"},{"title":"Learning to Repair Lean Proofs from Compiler Feedback","url":"https://arxiv.org/pdf/2602.02990"},{"title":"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/html/2605.28365"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning","url":"https://arxiv.org/pdf/2505.05758"},{"title":"CktFormalizer: Autoformalization of Natural Language into Circuit Representations","url":"https://arxiv.org/html/2605.07782"}]

Based on the search results, here's what I found:

APRIL (Automated Proof Repair in Lean) is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.

The research studies Lean proof repair as a supervised learning problem: given an erroneous proof and compiler feedback, predict both a corrected proof and a natural-language diagnosis grounded in the same feedback. Training language models on APRIL substantially improves repair accuracy and feedback-conditioned reasoning; in their single-shot repair evaluation setting, a finetuned 4B-parameter model outperforms the strongest open-source baseline.

Additionally, the search results show that there is research evaluating whether autoformalization preserves mathematical intent, using the FormalRx-Test dataset built on the SCI Error Taxonomy (28 error categories), which appears to be related work in the autoformalization error taxonomy domain you mentioned.

The APRIL paper was published in March 2026 and provides a comprehensive dataset for improving Lean proof repair capabilities through supervised learning from compiler feedback.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b945ff4-4f3b-4427-897a-1dea1a3b6d90",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "f5f70f6c-14e6-4513-96a5-40e6e96ff880",
  "toolUseResult": {
    "query": "APRIL repair tuples Lean autoformalization error taxonomy domain stratified 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UEyeU65y2GNjUfhGLhPt5e",
        "content": [
          {
            "title": "[2602.02990] Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/abs/2602.02990"
          },
          {
            "title": "Paper page - Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://huggingface.co/papers/2602.02990"
          },
          {
            "title": "Learning to Repair Lean Proofs from Compiler Feedback",
            "url": "https://arxiv.org/pdf/2602.02990"
          },
          {
            "title": "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
            "url": "https://arxiv.org/html/2605.28365"
          },
          {
            "title": "3rd AI for Math Workshop @ ICML 2026",
            "url": "https://ai4math2026.github.io/"
          },
          {
            "title": "APOLLO: Automated LLM and Lean Collaboration for Advanced Formal Reasoning",
            "url": "https://arxiv.org/pdf/2505.05758"
          },
          {
            "title": "CktFormalizer: Autoformalization of Natural Language into Circuit Representations",
            "url": "https://arxiv.org/html/2605.07782"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nAPRIL (Automated Proof Repair in Lean) is a dataset of 260,000 supervised tuples pairing systematically generated proof failures with compiler diagnostics and aligned repair and explanation targets.\n\nThe research studies Lean proof repair as a supervised learning problem: given an erroneous proof and compiler feedback, predict both a corrected proof and a natural-language diagnosis grounded in the same feedback. Training language models on APRIL substantially improves repair accuracy and feedback-conditioned reasoning; in their single-shot repair evaluation setting, a finetuned 4B-parameter model outperforms the strongest open-source baseline.\n\nAdditionally, the search results show that there is research evaluating whether autoformalization preserves mathematical intent, using the FormalRx-Test dataset built on the SCI Error Taxonomy (28 error categories), which appears to be related work in the autoformalization error taxonomy domain you mentioned.\n\nThe APRIL paper was published in March 2026 and provides a comprehensive dataset for improving Lean proof repair capabilities through supervised learning from compiler feedback."
    ],
    "durationSeconds": 9.252389199000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0b945ff4-4f3b-4427-897a-1dea1a3b6d90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T16:01:51.019Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AsHuXQMn2Y8Ap2S5wbnRkE`</summary>

```json
{
  "query": "CRAMF conceptual retrieval augmented autoformalization ICLR 2026 domain conditioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f70f6c-14e6-4513-96a5-40e6e96ff880",
  "isSidechain": false,
  "requestId": "req_011CbVFJfSzG3DGvzPo2Pmmo",
  "type": "assistant",
  "uuid": "b41dd035-d618-4102-9a53-cc3257e0be6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8uXmhUBp66XRdtgsH78j7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 27440,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27440,
          "cache_creation_input_tokens": 640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 640
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

_source line 18 · 2026-05-28T16:01:58.033Z_

<details><summary>↩ Tool result · `toolu_01AsHuXQMn2Y8Ap2S5wbnRkE`</summary>

```text
Web search results for query: "CRAMF conceptual retrieval augmented autoformalization ICLR 2026 domain conditioning"

Links: [{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/abs/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=09lmwhDqZ3"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs | Request PDF","url":"https://www.researchgate.net/publication/394440359_Automated_Formalization_via_Conceptual_Retrieval-Augmented_LLMs"}]

I found relevant information about CRAMF. Here are the search results:

## CRAMF: Conceptual Retrieval-Augmented Mathematical Formalization

CRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework that was submitted to ICLR 2026. 

### Problem It Addresses

Automated formalization faces two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions.

### Key Features

CRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation.

The framework automatically constructs a concept-definition knowledge base from Mathlib4, the standard mathematical library for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts.

### Domain Conditioning Approach

Regarding domain conditioning specifically: To address conceptual polymorphism, the framework proposes contextual query augmentation with domain- and application-level signals. Additionally, it designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.

### Performance

Experiments on miniF2F, ProofNet, and a newly proposed AdvancedMath benchmark show that CRAMF can be seamlessly integrated into LLM-based autoformalizers, yielding consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b41dd035-d618-4102-9a53-cc3257e0be6c",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "8cdc5245-02a4-43a6-972b-7595fba729e7",
  "toolUseResult": {
    "query": "CRAMF conceptual retrieval augmented autoformalization ICLR 2026 domain conditioning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sr8N91zA96zdqonSsyVV53",
        "content": [
          {
            "title": "AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...",
            "url": "https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"
          },
          {
            "title": "[2508.06931] Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/abs/2508.06931"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/pdf/2508.06931"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=09lmwhDqZ3"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/html/2508.06931"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/394440359_Automated_Formalization_via_Conceptual_Retrieval-Augmented_LLMs"
          }
        ]
      },
      "I found relevant information about CRAMF. Here are the search results:\n\n## CRAMF: Conceptual Retrieval-Augmented Mathematical Formalization\n\nCRAMF is a Concept-driven Retrieval-Augmented Mathematical Formalization framework that was submitted to ICLR 2026. \n\n### Problem It Addresses\n\nAutomated formalization faces two major challenges: model hallucination (e.g., undefined predicates, symbol misuse, and version incompatibility) and the semantic gap caused by ambiguous or missing premises in natural language descriptions.\n\n### Key Features\n\nCRAMF enhances LLM-based autoformalization by retrieving formal definitions of core mathematical concepts, providing contextual grounding during code generation.\n\nThe framework automatically constructs a concept-definition knowledge base from Mathlib4, the standard mathematical library for the Lean 4 theorem prover, indexing over 26,000 formal definitions and 1,000+ core mathematical concepts.\n\n### Domain Conditioning Approach\n\nRegarding domain conditioning specifically: To address conceptual polymorphism, the framework proposes contextual query augmentation with domain- and application-level signals. Additionally, it designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.\n\n### Performance\n\nExperiments on miniF2F, ProofNet, and a newly proposed AdvancedMath benchmark show that CRAMF can be seamlessly integrated into LLM-based autoformalizers, yielding consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement."
    ],
    "durationSeconds": 7.0092193279999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b41dd035-d618-4102-9a53-cc3257e0be6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T16:02:01.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9yzzbpSNC8tp5VoG3Ca1u`</summary>

```json
{
  "query": "MSC-180 benchmark autoformalization domain bias mathematical branches 2025 FormalMATH Goedel-Prover"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cdc5245-02a4-43a6-972b-7595fba729e7",
  "isSidechain": false,
  "requestId": "req_011CbVFKQKS45hqKJpTBvrW2",
  "type": "assistant",
  "uuid": "803525ed-fa94-4682-8ba6-dfd04083d552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sEBDz7SdPP9XZ5eL2NLcB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 856,
      "cache_read_input_tokens": 28080,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 856,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 28080,
          "cache_creation_input_tokens": 856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 856
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

_source line 20 · 2026-05-28T16:02:08.625Z_

<details><summary>↩ Tool result · `toolu_01G9yzzbpSNC8tp5VoG3Ca1u`</summary>

```text
Web search results for query: "MSC-180 benchmark autoformalization domain bias mathematical branches 2025 FormalMATH Goedel-Prover"

Links: [{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/pdf/2512.18256"},{"title":"MSC-180: A BENCHMARK FOR","url":"https://openreview.net/pdf/1d26736d12fac2add669df15fc65ba349e19edbb.pdf"},{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/html/2512.18256"},{"title":"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification | OpenReview","url":"https://openreview.net/forum?id=VBS5at5yrN"},{"title":"[2512.18256] MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification","url":"https://arxiv.org/abs/2512.18256"}]

Based on the search results, here's what I found about your query:

## MSC-180 Benchmark Overview

MSC-180 is a benchmark for evaluation based on the MSC2020 mathematical subject classification, comprising 180 formal verification problems—3 advanced problems from each of 60 mathematical branches—spanning from undergraduate to graduate levels. Each problem has undergone multiple rounds of verification and refinement by domain experts to ensure formal accuracy.

## Key Findings on Domain Bias

Evaluations of state-of-the-art LLM-based theorem provers under the pass@32 setting reveal that the best model achieves only an 18.89% overall pass rate, with prominent issues including significant domain bias (maximum domain coverage 41.7%) and a difficulty gap (significantly lower pass rates on graduate-level problems).

## Goedel-Prover and FormalMATH Context

Goedel-Prover-V2-32B achieved a success rate exceeding 90.4% on miniF2F. However, these results may partly reflect the models' adaptation to particular data distributions rather than indicating universal mathematical reasoning capabilities.

FormalMATH has a higher proportion of problems related to integrals and elementary calculus, while MiniF2F focuses more on high school algebra and number theory. Such imbalances in domain coverage may affect the comprehensive evaluation of models' reasoning abilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "803525ed-fa94-4682-8ba6-dfd04083d552",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "896ecf1d-063e-4638-8fb6-4f8cd4a3999e",
  "toolUseResult": {
    "query": "MSC-180 benchmark autoformalization domain bias mathematical branches 2025 FormalMATH Goedel-Prover",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XQXU59v74hmtj7sZ3sccnL",
        "content": [
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/pdf/2512.18256"
          },
          {
            "title": "MSC-180: A BENCHMARK FOR",
            "url": "https://openreview.net/pdf/1d26736d12fac2add669df15fc65ba349e19edbb.pdf"
          },
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/html/2512.18256"
          },
          {
            "title": "MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification | OpenReview",
            "url": "https://openreview.net/forum?id=VBS5at5yrN"
          },
          {
            "title": "[2512.18256] MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification",
            "url": "https://arxiv.org/abs/2512.18256"
          }
        ]
      },
      "Based on the search results, here's what I found about your query:\n\n## MSC-180 Benchmark Overview\n\nMSC-180 is a benchmark for evaluation based on the MSC2020 mathematical subject classification, comprising 180 formal verification problems—3 advanced problems from each of 60 mathematical branches—spanning from undergraduate to graduate levels. Each problem has undergone multiple rounds of verification and refinement by domain experts to ensure formal accuracy.\n\n## Key Findings on Domain Bias\n\nEvaluations of state-of-the-art LLM-based theorem provers under the pass@32 setting reveal that the best model achieves only an 18.89% overall pass rate, with prominent issues including significant domain bias (maximum domain coverage 41.7%) and a difficulty gap (significantly lower pass rates on graduate-level problems).\n\n## Goedel-Prover and FormalMATH Context\n\nGoedel-Prover-V2-32B achieved a success rate exceeding 90.4% on miniF2F. However, these results may partly reflect the models' adaptation to particular data distributions rather than indicating universal mathematical reasoning capabilities.\n\nFormalMATH has a higher proportion of problems related to integrals and elementary calculus, while MiniF2F focuses more on high school algebra and number theory. Such imbalances in domain coverage may affect the comprehensive evaluation of models' reasoning abilities."
    ],
    "durationSeconds": 6.983571649999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "803525ed-fa94-4682-8ba6-dfd04083d552",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "896ecf1d-063e-4638-8fb6-4f8cd4a3999e",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Tool call

_source line 23 · 2026-05-28T16:02:12.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LgpJ4TP724f64gBeVbbwZD`</summary>

```json
{
  "query": "LeanSearch v2 premise retrieval 2026 domain-agnostic hierarchy-informed informalization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "896ecf1d-063e-4638-8fb6-4f8cd4a3999e",
  "isSidechain": false,
  "requestId": "req_011CbVFLBcER4AJdYkbgp1Wk",
  "type": "assistant",
  "uuid": "eefce366-eb20-42b7-82ed-e13a1cc16a42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L45nR8gz5tMr76km8amRE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 28936,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28936,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 24 · 2026-05-28T16:02:21.002Z_

<details><summary>↩ Tool result · `toolu_01LgpJ4TP724f64gBeVbbwZD`</summary>

```text
Web search results for query: "LeanSearch v2 premise retrieval 2026 domain-agnostic hierarchy-informed informalization"

Links: [{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137v2"},{"title":"[2605.13137] LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/abs/2605.13137"},{"title":"Combining Textual and Structural Information for Premise Selection in Lean","url":"https://arxiv.org/pdf/2510.23637"},{"title":"Premise Selection for a Lean Hammer","url":"https://arxiv.org/pdf/2506.07477"},{"title":"[Literature Review] Premise Selection for a Lean Hammer","url":"https://www.themoonlight.io/en/review/premise-selection-for-a-lean-hammer"},{"title":"Lean Finder: Semantic Search for Mathlib That Understands User Intents","url":"https://openreview.net/pdf?id=5SF4fFRw7u"},{"title":"(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning","url":"https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"}]

Based on the search results, I found relevant information about LeanSearch v2:

LeanSearch v2 is a two-mode system for global premise retrieval in Lean 4, designed to recover the scattered set of library lemmas whose joint use enables a concise proof. 

Its reasoning mode builds on standard mode as its retrieval substrate, targeting global premise retrieval through iterative sketch-retrieve-reflect cycles. On a 69-query benchmark of research-level Mathlib theorems, reasoning mode recovers 46.1% of ground-truth premise groups within 10 retrieved candidates, outperforming strong reasoning retrieval systems (38.0%) and premise-selection baselines (9.3%).

The methodology is language-agnostic in design, but empirical transfer to other provers (Coq, Isabelle) with different library conventions remains to be demonstrated. In a controlled downstream evaluation with a fixed prover loop, replacing alternative retrievers with LeanSearch v2 yields the highest proof success (20% vs. 16% for the next-best system and 4% without retrieval).

Note: The search results do not specifically mention "hierarchy-informed informalization" in relation to LeanSearch v2, so that particular aspect is not covered in the available information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eefce366-eb20-42b7-82ed-e13a1cc16a42",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "969578f5-c852-4b5f-909f-9a2e4e649408",
  "toolUseResult": {
    "query": "LeanSearch v2 premise retrieval 2026 domain-agnostic hierarchy-informed informalization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D2zmDNANC695BadCEhSAge",
        "content": [
          {
            "title": "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving",
            "url": "https://arxiv.org/html/2605.13137v2"
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
            "title": "Premise Selection for a Lean Hammer",
            "url": "https://arxiv.org/pdf/2506.07477"
          },
          {
            "title": "[Literature Review] Premise Selection for a Lean Hammer",
            "url": "https://www.themoonlight.io/en/review/premise-selection-for-a-lean-hammer"
          },
          {
            "title": "Lean Finder: Semantic Search for Mathlib That Understands User Intents",
            "url": "https://openreview.net/pdf?id=5SF4fFRw7u"
          },
          {
            "title": "(PDF) REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning",
            "url": "https://www.researchgate.net/publication/392133993_REAL-Prover_Retrieval_Augmented_Lean_Prover_for_Mathematical_Reasoning"
          }
        ]
      },
      "Based on the search results, I found relevant information about LeanSearch v2:\n\nLeanSearch v2 is a two-mode system for global premise retrieval in Lean 4, designed to recover the scattered set of library lemmas whose joint use enables a concise proof. \n\nIts reasoning mode builds on standard mode as its retrieval substrate, targeting global premise retrieval through iterative sketch-retrieve-reflect cycles. On a 69-query benchmark of research-level Mathlib theorems, reasoning mode recovers 46.1% of ground-truth premise groups within 10 retrieved candidates, outperforming strong reasoning retrieval systems (38.0%) and premise-selection baselines (9.3%).\n\nThe methodology is language-agnostic in design, but empirical transfer to other provers (Coq, Isabelle) with different library conventions remains to be demonstrated. In a controlled downstream evaluation with a fixed prover loop, replacing alternative retrievers with LeanSearch v2 yields the highest proof success (20% vs. 16% for the next-best system and 4% without retrieval).\n\nNote: The search results do not specifically mention \"hierarchy-informed informalization\" in relation to LeanSearch v2, so that particular aspect is not covered in the available information."
    ],
    "durationSeconds": 8.757762761999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eefce366-eb20-42b7-82ed-e13a1cc16a42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T16:02:24.241Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015bvsjnu11gQdiLMWEy1AQS`</summary>

```json
{
  "query": "IndiMathBench autoformalization static category context Mathlib compilation BEq semantic correctness 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969578f5-c852-4b5f-909f-9a2e4e649408",
  "isSidechain": false,
  "requestId": "req_011CbVFM6VS8RCMSpJRYWSmz",
  "type": "assistant",
  "uuid": "492d6669-7e54-4dd7-b3d7-adbdf29b8017",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139eYk78P1ayaTMBdLdfzPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 29637,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 755,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29637,
          "cache_creation_input_tokens": 755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 755
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

_source line 26 · 2026-05-28T16:02:32.399Z_

<details><summary>↩ Tool result · `toolu_015bvsjnu11gQdiLMWEy1AQS`</summary>

```text
Web search results for query: "IndiMathBench autoformalization static category context Mathlib compilation BEq semantic correctness 2025"

Links: [{"title":"(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/html/2512.00997"},{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/abs/2512.00997"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning ...","url":"https://arxiv.org/pdf/2512.00997"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch | OpenReview","url":"https://openreview.net/forum?id=tmReo37kl2"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

Based on the search results, I've found comprehensive information about IndiMathBench and the concepts you mentioned. Here's what the research reveals:

## IndiMathBench Overview

IndiMathBench is composed of 416 formal Lean4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads.

## Pipeline and Methodology

Through category-based retrieval, iterative compiler feedback, and multi-model ensembles, the pipeline generates candidate formalizations that experts efficiently validate via an interactive dashboard with automated quality summaries.

## Key Evaluation Metrics

The research employs two main evaluation approaches:

1. **BEq (Bidirectional Equivalence)**: BEq evaluates logical equivalence by attempting to prove each theorem using the other. Given two Lean 4 theorems in sorry-format, BEq employs a diverse set of heuristic and LLM-guided tactics to establish proofs in both directions.

2. **GTED (Generalized Tree Edit Distance)**: GTED computes structural similarity through operator trees, while BEq provides neural-symbolic equivalence checking.

## Key Findings

Evaluation across multiple frontier models demonstrates that autoformalization remains challenging, with substantial gaps between syntactic validity and semantic correctness, while theorem proving success rates remain low even with iterative refinement. Additionally, compilation success significantly exceeds semantic correctness across all families.

The research is documented in a 2025 paper available on arXiv and has been formally published, representing significant contributions to understanding autoformalization challenges in formal mathematics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "492d6669-7e54-4dd7-b3d7-adbdf29b8017",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "7b3581f4-4c9c-467f-95b2-8e97c4548efa",
  "toolUseResult": {
    "query": "IndiMathBench autoformalization static category context Mathlib compilation BEq semantic correctness 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EseWFnoNXvHoSNvKFLoD7P",
        "content": [
          {
            "title": "(PDF) IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://www.researchgate.net/publication/398225105_IndiMathBench_Autoformalizing_Mathematical_Reasoning_Problems_with_a_Human_Touch"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/html/2512.00997"
          },
          {
            "title": "INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-",
            "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"
          },
          {
            "title": "[2512.00997] IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/abs/2512.00997"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning ...",
            "url": "https://arxiv.org/pdf/2512.00997"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf"
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
      "Based on the search results, I've found comprehensive information about IndiMathBench and the concepts you mentioned. Here's what the research reveals:\n\n## IndiMathBench Overview\n\nIndiMathBench is composed of 416 formal Lean4 theorems paired with their corresponding informal problem statements, sourced from Indian Mathematics Olympiads.\n\n## Pipeline and Methodology\n\nThrough category-based retrieval, iterative compiler feedback, and multi-model ensembles, the pipeline generates candidate formalizations that experts efficiently validate via an interactive dashboard with automated quality summaries.\n\n## Key Evaluation Metrics\n\nThe research employs two main evaluation approaches:\n\n1. **BEq (Bidirectional Equivalence)**: BEq evaluates logical equivalence by attempting to prove each theorem using the other. Given two Lean 4 theorems in sorry-format, BEq employs a diverse set of heuristic and LLM-guided tactics to establish proofs in both directions.\n\n2. **GTED (Generalized Tree Edit Distance)**: GTED computes structural similarity through operator trees, while BEq provides neural-symbolic equivalence checking.\n\n## Key Findings\n\nEvaluation across multiple frontier models demonstrates that autoformalization remains challenging, with substantial gaps between syntactic validity and semantic correctness, while theorem proving success rates remain low even with iterative refinement. Additionally, compilation success significantly exceeds semantic correctness across all families.\n\nThe research is documented in a 2025 paper available on arXiv and has been formally published, representing significant contributions to understanding autoformalization challenges in formal mathematics."
    ],
    "durationSeconds": 8.153695580999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "492d6669-7e54-4dd7-b3d7-adbdf29b8017",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T16:02:35.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkTvP9k7dnwqwhUYypMvvu`</summary>

```json
{
  "query": "Shebzukhov 2026 cycle consistency fine-tuning FineLeanCorpus number theory calculus domain autoformalization arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b3581f4-4c9c-467f-95b2-8e97c4548efa",
  "isSidechain": false,
  "requestId": "req_011CbVFMwFbEQYxaHyg1Ps1B",
  "type": "assistant",
  "uuid": "2798b599-74a0-4085-9c2e-c0464b5144ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtSeyvqZaMkwqmZjLeFeUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 30392,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 30392,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 28 · 2026-05-28T16:02:43.911Z_

<details><summary>↩ Tool result · `toolu_01NkTvP9k7dnwqwhUYypMvvu`</summary>

```text
Web search results for query: "Shebzukhov 2026 cycle consistency fine-tuning FineLeanCorpus number theory calculus domain autoformalization arXiv 2603"

Links: [{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372"},{"title":"[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/abs/2603.24372"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning","url":"https://arxiv.org/pdf/2603.24372"},{"title":"GitHub - multimodal-art-projection/CriticLean · GitHub","url":"https://github.com/multimodal-art-projection/CriticLean"},{"title":"Process-Driven Autoformalization in Lean 4","url":"https://arxiv.org/pdf/2406.01940"}]

I found the research paper you're looking for! Here's what I found:

The paper "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning" was published on arXiv (2603.24372) on March 25, 2026 by Arsen Shebzukhov from Stanford University.

**Key Details:**

- The research focuses on autoformalization - automatically translating natural language mathematical texts into formal proof language such as Lean4.

- The work fine-tunes Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus and considers three training regimes: supervised fine-tuning (SFT) with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization (GRPO) with a cycle consistency reward.

- Cycle consistency measures how well the meaning of a statement is preserved through a NL to Lean4 to NL' loop, computed as cosine similarity of off-the-shelf sentence embeddings.

- FineLeanCorpus provides 509k natural language/Lean4 pairs with difficulty ratings and domain labels, which was used as training data.

- On an unseen subset of FineLeanCorpus and on PutnamBench, RL substantially outperforms both SFT variants (mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2798b599-74a0-4085-9c2e-c0464b5144ff",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "121a352f-ef70-40e2-aedb-88758f444c53",
  "toolUseResult": {
    "query": "Shebzukhov 2026 cycle consistency fine-tuning FineLeanCorpus number theory calculus domain autoformalization arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_011jeb49udxUsHYQqVgWjaQE",
        "content": [
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project",
            "url": "https://arxiv.org/html/2603.24372"
          },
          {
            "title": "[2603.24372] Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/abs/2603.24372"
          },
          {
            "title": "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning",
            "url": "https://arxiv.org/pdf/2603.24372"
          },
          {
            "title": "GitHub - multimodal-art-projection/CriticLean · GitHub",
            "url": "https://github.com/multimodal-art-projection/CriticLean"
          },
          {
            "title": "Process-Driven Autoformalization in Lean 4",
            "url": "https://arxiv.org/pdf/2406.01940"
          }
        ]
      },
      "I found the research paper you're looking for! Here's what I found:\n\nThe paper \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning\" was published on arXiv (2603.24372) on March 25, 2026 by Arsen Shebzukhov from Stanford University.\n\n**Key Details:**\n\n- The research focuses on autoformalization - automatically translating natural language mathematical texts into formal proof language such as Lean4.\n\n- The work fine-tunes Qwen3.5-2B with LoRA for natural language to Lean4 formalization on FineLeanCorpus and considers three training regimes: supervised fine-tuning (SFT) with curriculum learning, SFT without curriculum ordering, and reinforcement learning using group relative policy optimization (GRPO) with a cycle consistency reward.\n\n- Cycle consistency measures how well the meaning of a statement is preserved through a NL to Lean4 to NL' loop, computed as cosine similarity of off-the-shelf sentence embeddings.\n\n- FineLeanCorpus provides 509k natural language/Lean4 pairs with difficulty ratings and domain labels, which was used as training data.\n\n- On an unseen subset of FineLeanCorpus and on PutnamBench, RL substantially outperforms both SFT variants (mean cycle consistency 0.669 vs. 0.513 on FLC; 0.561 vs. 0.422 on PutnamBench)."
    ],
    "durationSeconds": 8.207375624000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2798b599-74a0-4085-9c2e-c0464b5144ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-28T16:02:43.916Z_

```json
{
  "parentUuid": "121a352f-ef70-40e2-aedb-88758f444c53",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d4321aea-2743-4d11-af69-c96faf59f50c",
  "timestamp": "2026-05-28T16:02:43.916Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-28T16:02:46.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MKqgkU8i7n3RyfJVVdfYwo`</summary>

```json
{
  "query": "domain-conditioned retrieval reranking mathematical subdomain autoformalization Lean 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4321aea-2743-4d11-af69-c96faf59f50c",
  "isSidechain": false,
  "requestId": "req_011CbVFNnfBaNuUYYGjJQBpV",
  "type": "assistant",
  "uuid": "9e83f57d-34f8-43fc-bc0b-9fc4d58e106f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4zA3mFvgEbgzfFrb9jbxJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 31305,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 31305,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
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

_source line 31 · 2026-05-28T16:02:52.459Z_

<details><summary>↩ Tool result · `toolu_01MKqgkU8i7n3RyfJVVdfYwo`</summary>

```text
Web search results for query: "domain-conditioned retrieval reranking mathematical subdomain autoformalization Lean 2025 2026"

Links: [{"title":"AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...","url":"https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"},{"title":"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning Stanford CS224N Custom Project","url":"https://arxiv.org/html/2603.24372v1"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2508.06931"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.15940"},{"title":"RLMEval: Evaluating Autoformalization on Research-Level Mathematics","url":"http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/pdf/2510.10815"},{"title":"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph","url":"https://arxiv.org/pdf/2510.04520"},{"title":"Automated Formalization via Conceptual Retrieval-Augmented LLMs","url":"https://arxiv.org/pdf/2508.06931"}]

Based on the search results, here's what I found regarding domain-conditioned retrieval reranking in mathematical subdomain autoformalization:

## Key Findings

A framework called CRAMF was introduced that automatically constructs a concept-definition knowledge base from Mathlib4 (the standard mathematical library for Lean 4), indexing over 26,000 formal definitions and 1,000+ core mathematical concepts. To address conceptual polymorphism, it proposes contextual query augmentation with domain- and application-level signals, and designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.

This approach yields consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement when integrated into LLM-based autoformalizers.

Additionally, recent work proposes DRIFT, a novel framework that enhances retrieval-augmented autoformalization by decomposing statements into a series of simpler, atomic sub-queries, with each sub-query targeting a single mathematical concept to transform multifaceted retrieval problems into focused, precise searches.

These developments represent recent advances (2025-2026) in making autoformalization systems more domain-aware and contextually grounded through improved retrieval and reranking mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e83f57d-34f8-43fc-bc0b-9fc4d58e106f",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "bebe8877-2077-4fae-9f15-3ac9ddc46e4a",
  "toolUseResult": {
    "query": "domain-conditioned retrieval reranking mathematical subdomain autoformalization Lean 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015qpuX3beFysUzG8A7ZGjer",
        "content": [
          {
            "title": "AUTOMATED FORMALIZATION VIA CONCEPTUAL RETRIEVAL ...",
            "url": "https://openreview.net/pdf/c5515c42a45d03adcd764803dc11197cf6a270ae.pdf"
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
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.15940"
          },
          {
            "title": "RLMEval: Evaluating Autoformalization on Research-Level Mathematics",
            "url": "http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/pdf/2510.10815"
          },
          {
            "title": "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph",
            "url": "https://arxiv.org/pdf/2510.04520"
          },
          {
            "title": "Automated Formalization via Conceptual Retrieval-Augmented LLMs",
            "url": "https://arxiv.org/pdf/2508.06931"
          }
        ]
      },
      "Based on the search results, here's what I found regarding domain-conditioned retrieval reranking in mathematical subdomain autoformalization:\n\n## Key Findings\n\nA framework called CRAMF was introduced that automatically constructs a concept-definition knowledge base from Mathlib4 (the standard mathematical library for Lean 4), indexing over 26,000 formal definitions and 1,000+ core mathematical concepts. To address conceptual polymorphism, it proposes contextual query augmentation with domain- and application-level signals, and designs a dual-channel hybrid retrieval strategy with reranking to ensure accurate and relevant definition retrieval.\n\nThis approach yields consistent improvements in translation accuracy—achieving up to 62.1% and an average of 29.9% relative improvement when integrated into LLM-based autoformalizers.\n\nAdditionally, recent work proposes DRIFT, a novel framework that enhances retrieval-augmented autoformalization by decomposing statements into a series of simpler, atomic sub-queries, with each sub-query targeting a single mathematical concept to transform multifaceted retrieval problems into focused, precise searches.\n\nThese developments represent recent advances (2025-2026) in making autoformalization systems more domain-aware and contextually grounded through improved retrieval and reranking mechanisms."
    ],
    "durationSeconds": 5.8346757510000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9e83f57d-34f8-43fc-bc0b-9fc4d58e106f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T16:02:55.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EuSKrQ8UdAurvBTPTxeRgJ`</summary>

```json
{
  "query": "Kim et al \"Do LLMs Game Formalization\" semantic unfaithfulness compilation arXiv 2604.19459 VerifAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bebe8877-2077-4fae-9f15-3ac9ddc46e4a",
  "isSidechain": false,
  "requestId": "req_011CbVFPQyjGYdTYEZtB7zSV",
  "type": "assistant",
  "uuid": "1eac2d57-e58c-4104-8c66-89f534d597a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wphfhj6k3RBZhhuABeARC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 32137,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 780,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 32137,
          "cache_creation_input_tokens": 780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 780
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

_source line 33 · 2026-05-28T16:03:03.629Z_

<details><summary>↩ Tool result · `toolu_01EuSKrQ8UdAurvBTPTxeRgJ`</summary>

```text
Web search results for query: "Kim et al "Do LLMs Game Formalization" semantic unfaithfulness compilation arXiv 2604.19459 VerifAI"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?","url":"https://arxiv.org/pdf/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/pdf/2409.12300"},{"title":"Lying to Win: Assessing LLM Deception through Human-AI Games and Parallel-World Probing","url":"https://arxiv.org/pdf/2603.07202"},{"title":"Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference","url":"https://arxiv.org/pdf/2503.04779"},{"title":"Code World Models for General Game Playing","url":"https://arxiv.org/pdf/2510.04542"}]

Based on the search results, here's what I found about this paper:

The paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" is published as arXiv 2604.19459, and it was published at the VerifAI-2 Workshop at ICLR 2026.

The paper is authored by Kyuhee Kim and 2 other authors.

**Research Focus:**

Formal verification guarantees proof validity but not formalization faithfulness. For natural-language logical reasoning, where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute.

**Key Findings:**

The researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), and despite compilation rates of 87-99%, they found no evidence of systematic gaming in unified generation.

However, a two-stage pipeline revealed two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation (a reactive fallback detectable via cross-stage comparison), while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

The findings show that high compilation rates or accuracies should not be equated with faithful reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eac2d57-e58c-4104-8c66-89f534d597a2",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "a88639ce-fca0-4c56-be10-e55ddabf98a9",
  "toolUseResult": {
    "query": "Kim et al \"Do LLMs Game Formalization\" semantic unfaithfulness compilation arXiv 2604.19459 VerifAI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A8schw9CkmEQpFh4YgGm1s",
        "content": [
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Published at the VerifAI-2 Workshop, ICLR 2026 DO LLMS GAME FORMALIZATION?",
            "url": "https://arxiv.org/pdf/2604.19459"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "Autoformalization of Game Descriptions using Large Language Models",
            "url": "https://arxiv.org/pdf/2409.12300"
          },
          {
            "title": "Lying to Win: Assessing LLM Deception through Human-AI Games and Parallel-World Probing",
            "url": "https://arxiv.org/pdf/2603.07202"
          },
          {
            "title": "Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference",
            "url": "https://arxiv.org/pdf/2503.04779"
          },
          {
            "title": "Code World Models for General Game Playing",
            "url": "https://arxiv.org/pdf/2510.04542"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\nThe paper \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\" is published as arXiv 2604.19459, and it was published at the VerifAI-2 Workshop at ICLR 2026.\n\nThe paper is authored by Kyuhee Kim and 2 other authors.\n\n**Research Focus:**\n\nFormal verification guarantees proof validity but not formalization faithfulness. For natural-language logical reasoning, where models construct axiom systems from scratch without library constraints, this gap between valid proofs and faithful translations is especially acute.\n\n**Key Findings:**\n\nThe researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), and despite compilation rates of 87-99%, they found no evidence of systematic gaming in unified generation.\n\nHowever, a two-stage pipeline revealed two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation (a reactive fallback detectable via cross-stage comparison), while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.\n\nThe findings show that high compilation rates or accuracies should not be equated with faithful reasoning."
    ],
    "durationSeconds": 7.694092599000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1eac2d57-e58c-4104-8c66-89f534d597a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "a88639ce-fca0-4c56-be10-e55ddabf98a9",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Tool call

_source line 36 · 2026-05-28T16:03:07.248Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012cUh5NFvWPfLVvcSfx8gaW`</summary>

```json
{
  "query": "CAM-Bench computational applied mathematics Lean benchmark Long 2026 arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a88639ce-fca0-4c56-be10-e55ddabf98a9",
  "isSidechain": false,
  "requestId": "req_011CbVFQEmbi6RfMgMdEo8Uu",
  "type": "assistant",
  "uuid": "718198d3-b21f-440e-aa72-bcd445fef145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vnij3gJDeVuTTdrs2SVcUC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 32917,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 32917,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 37 · 2026-05-28T16:03:12.839Z_

<details><summary>↩ Tool result · `toolu_012cUh5NFvWPfLVvcSfx8gaW`</summary>

```text
Web search results for query: "CAM-Bench computational applied mathematics Lean benchmark Long 2026 arXiv 2605"

Links: [{"title":"[2605.17255] CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/abs/2605.17255"},{"title":"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean","url":"https://arxiv.org/html/2605.17255"},{"title":"Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/pdf/2602.01291"},{"title":"[2605.13171] Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics","url":"https://arxiv.org/abs/2605.13171"},{"title":"[2602.01291] Construction-Verification: A Benchmark for Applied Mathematics in Lean 4","url":"https://arxiv.org/abs/2602.01291"},{"title":"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving","url":"https://arxiv.org/html/2605.13137v2"}]

Based on the search results, I found the paper you're looking for:

**CAM-Bench** is a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis.

The problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, the authors developed a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully and then normalizes each problem into a standalone informal theorem and translates it into a Lean target.

The paper was authored by Wentao Long and 5 other authors, posted on arXiv on May 17, 2026 (arXiv:2605.17255).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "718198d3-b21f-440e-aa72-bcd445fef145",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "f0a340fd-3e76-4a94-ad98-63dd28db9ab3",
  "toolUseResult": {
    "query": "CAM-Bench computational applied mathematics Lean benchmark Long 2026 arXiv 2605",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nt3gxTkcRhhMRyUvhdSu2B",
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
            "title": "Construction-Verification: A Benchmark for Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/pdf/2602.01291"
          },
          {
            "title": "[2605.13171] Formal Conjectures: An Open and Evolving Benchmark for Verified Discovery in Mathematics",
            "url": "https://arxiv.org/abs/2605.13171"
          },
          {
            "title": "[2602.01291] Construction-Verification: A Benchmark for Applied Mathematics in Lean 4",
            "url": "https://arxiv.org/abs/2602.01291"
          },
          {
            "title": "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving",
            "url": "https://arxiv.org/html/2605.13137v2"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**CAM-Bench** is a Lean 4 theorem-proving benchmark of 1,000 Lean proof targets in computational and applied mathematics, with coverage spanning optimization, numerical linear algebra, and numerical analysis.\n\nThe problems are adapted from textbook exercises and often depend on locally introduced definitions, notation, algorithms, and elementary results. To construct CAM-Bench, the authors developed a dependency-recovery pipeline that reconstructs the local textbook context needed to state each problem faithfully and then normalizes each problem into a standalone informal theorem and translates it into a Lean target.\n\nThe paper was authored by Wentao Long and 5 other authors, posted on arXiv on May 17, 2026 (arXiv:2605.17255)."
    ],
    "durationSeconds": 5.585511074999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "718198d3-b21f-440e-aa72-bcd445fef145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T16:03:16.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SRJxHHLvFAuKZAbmFWLdKM`</summary>

```json
{
  "query": "KELPS knowledge equations autoformalization multi-language verified MiniF2F ICML 2025 arXiv 2507.08665"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a340fd-3e76-4a94-ad98-63dd28db9ab3",
  "isSidechain": false,
  "requestId": "req_011CbVFQv9SaBbtKozuEZ5pd",
  "type": "assistant",
  "uuid": "708b51a4-458b-4784-b6af-e79a7c2ff70d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dmnftZSCFEQjXVwVTwSXo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 33694,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 33694,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 585
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

_source line 39 · 2026-05-28T16:03:23.874Z_

<details><summary>↩ Tool result · `toolu_01SRJxHHLvFAuKZAbmFWLdKM`</summary>

```text
Web search results for query: "KELPS knowledge equations autoformalization multi-language verified MiniF2F ICML 2025 arXiv 2507.08665"

Links: [{"title":"[2507.08665] KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/abs/2507.08665"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via","url":"https://arxiv.org/pdf/2507.08665"},{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=3925&show=1000"},{"title":"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment","url":"https://arxiv.org/html/2507.08665"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2505.23486v1"}]

Based on the search results, here's what I found about KELPS:

KELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). The framework translates natural language into Knowledge Equations (KEs), a novel language designed and theoretically grounded in assertional logic.

The process yielded a parallel corpus of over 60,000 problems. The framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.

The paper was accepted by the ICML 2025 AI4MATH Workshop. The work makes three contributions: the design of Knowledge Equations as a novel formal language with complete BNF specification and parser implementation; the release of KELPS Dataset, a large-scale multilingual formal language dataset; and the development of a high-performance model that achieves new SOTA accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "708b51a4-458b-4784-b6af-e79a7c2ff70d",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "3fb2074d-44e5-4fe1-ab7f-ce9b532241ca",
  "toolUseResult": {
    "query": "KELPS knowledge equations autoformalization multi-language verified MiniF2F ICML 2025 arXiv 2507.08665",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U3XNPiqJP3rXyWj1tWRN6b",
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
            "title": "Computer Science Jul 2025",
            "url": "https://www.arxiv.org/list/cs/2025-07?skip=3925&show=1000"
          },
          {
            "title": "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment",
            "url": "https://arxiv.org/html/2507.08665"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2505.23486v1"
          }
        ]
      },
      "Based on the search results, here's what I found about KELPS:\n\nKELPS is an iterative framework for translating, synthesizing, and filtering informal data into multiple formal languages (Lean, Coq, and Isabelle). The framework translates natural language into Knowledge Equations (KEs), a novel language designed and theoretically grounded in assertional logic.\n\nThe process yielded a parallel corpus of over 60,000 problems. The framework achieves 88.9% syntactic accuracy (pass@1) on MiniF2F, outperforming SOTA models such as Deepseek-V3 (81%) and Herald (81.3%) across multiple datasets.\n\nThe paper was accepted by the ICML 2025 AI4MATH Workshop. The work makes three contributions: the design of Knowledge Equations as a novel formal language with complete BNF specification and parser implementation; the release of KELPS Dataset, a large-scale multilingual formal language dataset; and the development of a high-performance model that achieves new SOTA accuracy."
    ],
    "durationSeconds": 7.739964329000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "708b51a4-458b-4784-b6af-e79a7c2ff70d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T16:03:26.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XsxJGWSzaEsK6b5kKU72GZ`</summary>

```json
{
  "query": "autoformalization error analysis domain specific Lean Mathlib module path 2025 2026 typeclass coercion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fb2074d-44e5-4fe1-ab7f-ce9b532241ca",
  "isSidechain": false,
  "requestId": "req_011CbVFRjHNNQjA8nGBsF59T",
  "type": "assistant",
  "uuid": "338a247f-5e66-4ce5-9459-8f58f6926993",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8UXsiuH67M7FDHQu4RY1s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 34279,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 34279,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 41 · 2026-05-28T16:03:34.365Z_

<details><summary>↩ Tool result · `toolu_01XsxJGWSzaEsK6b5kKU72GZ`</summary>

```text
Web search results for query: "autoformalization error analysis domain specific Lean Mathlib module path 2025 2026 typeclass coercion"

Links: [{"title":"INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"},{"title":"Use and abuse of instance parameters in the Lean mathematical library","url":"https://arxiv.org/pdf/2202.01629"},{"title":"GitHub - lean-forward/mathlib-classes: Use and abuse of instance parameters in the Lean mathematical library · GitHub","url":"https://github.com/lean-forward/mathlib-classes"},{"title":"Scalar actions in Lean's mathlib","url":"https://arxiv.org/pdf/2108.10700"},{"title":"Use and Abuse of Instance Parameters in the Lean Mathematical Library | Journal of Automated Reasoning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10817-024-09712-7"},{"title":"Multiple-inheritance hazards in dependently-typed algebraic hierarchies","url":"https://arxiv.org/pdf/2306.00617"},{"title":"Mathlib: A Foundation for Formal Mathematics Research and Verification — Lean Lang","url":"https://lean-lang.org/use-cases/mathlib/"},{"title":"Tabled Typeclass Resolution","url":"https://arxiv.org/pdf/2001.04301"},{"title":"10. Type Classes — Theorem Proving in Lean 3 (outdated) 3.23.0 documentation","url":"https://leanprover.github.io/theorem_proving_in_lean/type_classes.html"}]

Based on the search results, here's what I found relevant to your query about autoformalization, error analysis, and Lean/Mathlib concepts:

## Autoformalization and Error Analysis

In autoformalization evaluations, the main deficiency observed was poor quality of formulas, with models often hallucinating non-existent imports, mixing syntax from other theorem provers including Lean 3, and producing ill-formed code. LLMs often fail to import correct modules or use proper notation in Lean, so researchers augment prompts with automatically curated Mathlib documentation.

## Typeclass and Coercion Systems

The Lean mathematical library Mathlib features extensive use of the typeclass pattern for organizing mathematical structures, based on Lean's mechanism of instance parameters, with the paper analyzing design patterns and complications arising at scale.

Lean uses classes to implement implicit coercions. In Lean, coercions are implemented on top of the type class resolution framework by declaring an instance of has_coe.

## Mathlib Scale and Organization

As of February 2022, Mathlib contains over 600 classes and over 8000 instances. With over two million lines of formalized mathematics, Mathlib has become one of the most extensive mathematical libraries available in any proof assistant.

The search results touch on module imports, typeclass systems, and coercion mechanisms in Lean/Mathlib, which are central to autoformalization challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "338a247f-5e66-4ce5-9459-8f58f6926993",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "9660c222-2a74-4780-ab74-ca5d94da9396",
  "toolUseResult": {
    "query": "autoformalization error analysis domain specific Lean Mathlib module path 2025 2026 typeclass coercion",
    "results": [
      {
        "tool_use_id": "srvtoolu_016ATd4CQMgsMZ1Y16MXGNfN",
        "content": [
          {
            "title": "INDIMATHBENCH: AUTOFORMALIZING MATHEMATI-",
            "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf"
          },
          {
            "title": "Use and abuse of instance parameters in the Lean mathematical library",
            "url": "https://arxiv.org/pdf/2202.01629"
          },
          {
            "title": "GitHub - lean-forward/mathlib-classes: Use and abuse of instance parameters in the Lean mathematical library · GitHub",
            "url": "https://github.com/lean-forward/mathlib-classes"
          },
          {
            "title": "Scalar actions in Lean's mathlib",
            "url": "https://arxiv.org/pdf/2108.10700"
          },
          {
            "title": "Use and Abuse of Instance Parameters in the Lean Mathematical Library | Journal of Automated Reasoning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10817-024-09712-7"
          },
          {
            "title": "Multiple-inheritance hazards in dependently-typed algebraic hierarchies",
            "url": "https://arxiv.org/pdf/2306.00617"
          },
          {
            "title": "Mathlib: A Foundation for Formal Mathematics Research and Verification — Lean Lang",
            "url": "https://lean-lang.org/use-cases/mathlib/"
          },
          {
            "title": "Tabled Typeclass Resolution",
            "url": "https://arxiv.org/pdf/2001.04301"
          },
          {
            "title": "10. Type Classes — Theorem Proving in Lean 3 (outdated) 3.23.0 documentation",
            "url": "https://leanprover.github.io/theorem_proving_in_lean/type_classes.html"
          }
        ]
      },
      "Based on the search results, here's what I found relevant to your query about autoformalization, error analysis, and Lean/Mathlib concepts:\n\n## Autoformalization and Error Analysis\n\nIn autoformalization evaluations, the main deficiency observed was poor quality of formulas, with models often hallucinating non-existent imports, mixing syntax from other theorem provers including Lean 3, and producing ill-formed code. LLMs often fail to import correct modules or use proper notation in Lean, so researchers augment prompts with automatically curated Mathlib documentation.\n\n## Typeclass and Coercion Systems\n\nThe Lean mathematical library Mathlib features extensive use of the typeclass pattern for organizing mathematical structures, based on Lean's mechanism of instance parameters, with the paper analyzing design patterns and complications arising at scale.\n\nLean uses classes to implement implicit coercions. In Lean, coercions are implemented on top of the type class resolution framework by declaring an instance of has_coe.\n\n## Mathlib Scale and Organization\n\nAs of February 2022, Mathlib contains over 600 classes and over 8000 instances. With over two million lines of formalized mathematics, Mathlib has become one of the most extensive mathematical libraries available in any proof assistant.\n\nThe search results touch on module imports, typeclass systems, and coercion mechanisms in Lean/Mathlib, which are central to autoformalization challenges."
    ],
    "durationSeconds": 7.381313335999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "338a247f-5e66-4ce5-9459-8f58f6926993",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-28T16:03:38.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpGHnTMZjDfz3qEM8mqfNt`</summary>

```json
{
  "query": "MathAtlas benchmark autoformalization 52k entities 87 math areas dependency relations 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9660c222-2a74-4780-ab74-ca5d94da9396",
  "isSidechain": false,
  "requestId": "req_011CbVFSW9cusjzX2H44Qmpg",
  "type": "assistant",
  "uuid": "c5332e66-c9bc-449b-bc35-488c09a28f11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEFGxQHa2TUA3qfcEeWNUV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 34973,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 34973,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 43 · 2026-05-28T16:03:44.094Z_

<details><summary>↩ Tool result · `toolu_01VpGHnTMZjDfz3qEM8mqfNt`</summary>

```text
Web search results for query: "MathAtlas benchmark autoformalization 52k entities 87 math areas dependency relations 2026"

Links: [{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"},{"title":"An Evaluation Benchmark for Autoformalization in Lean4","url":"https://arxiv.org/pdf/2406.06555"},{"title":"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch","url":"https://arxiv.org/pdf/2512.00997"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"}]

Based on the search results, here's what I found about MathAtlas:

MathAtlas is the first large-scale autoformalization benchmark of in-the-wild graduate-level mathematics, containing approximately 52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.

MathAtlas is enriched with a mathematical dependency graph containing approximately 178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.

Strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. The benchmark was published recently, appearing on arXiv about 2 weeks ago.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5332e66-c9bc-449b-bc35-488c09a28f11",
  "isSidechain": false,
  "promptId": "025d62d0-3bbb-4b25-ae60-3b71b5e0ff25",
  "type": "user",
  "uuid": "9fd7b750-d091-4e94-9ea4-1b33265a743d",
  "toolUseResult": {
    "query": "MathAtlas benchmark autoformalization 52k entities 87 math areas dependency relations 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MqkyeqrjDjujqh9HbpoKhG",
        "content": [
          {
            "title": "MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/html/2605.14061"
          },
          {
            "title": "[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/abs/2605.14061"
          },
          {
            "title": "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview",
            "url": "https://openreview.net/forum?id=hUb2At2DsQ"
          },
          {
            "title": "An Evaluation Benchmark for Autoformalization in Lean4",
            "url": "https://arxiv.org/pdf/2406.06555"
          },
          {
            "title": "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch",
            "url": "https://arxiv.org/pdf/2512.00997"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          }
        ]
      },
      "Based on the search results, here's what I found about MathAtlas:\n\nMathAtlas is the first large-scale autoformalization benchmark of in-the-wild graduate-level mathematics, containing approximately 52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks. Entities in MathAtlas span 87 areas of mathematics, including real analysis, differential geometry, category theory, topology, quantum groups, among others.\n\nMathAtlas is enriched with a mathematical dependency graph containing approximately 178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems.\n\nStrong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. The benchmark was published recently, appearing on arXiv about 2 weeks ago."
    ],
    "durationSeconds": 6.023611307000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c5332e66-c9bc-449b-bc35-488c09a28f11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-28T16:05:32.049Z_

Now I have sufficient research to make my assessment. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- [CRAMF / Automated Formalization via Conceptual Retrieval-Augmented LLMs](https://arxiv.org/abs/2508.06931) (ICLR 2026): 构建26k+定义的concept-definition知识库，使用contextual query augmentation处理多义概念，dual-channel hybrid retrieval + reranking。核心操作在concept级别，未按数学子领域动态调节retrieval排序。与本proposal关系：proposal声称CRAMF不做domain conditioning，经核实属实——CRAMF的"domain-level signals"指的是用于消歧polysemous concepts的上下文信号，不是按问题的数学子领域动态调整整个retrieval ranking。
- [DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems](https://arxiv.org/pdf/2510.10815) (ICLR 2026): 将statement分解为~5.8个atomic sub-queries做targeted retrieval。同样是concept-level操作，不做subdomain conditioning。
- [LeanSearch v2: Global Premise Retrieval for Lean 4](https://arxiv.org/abs/2605.13137) (arXiv May 2026): 两种mode的premise retrieval系统，reasoning mode在69-query benchmark上恢复46.1% ground-truth premise groups。Domain-agnostic设计。
- [MSC-180](https://arxiv.org/abs/2512.18256) (arXiv Dec 2025): 60个数学分支×3题=180题benchmark。最佳模型仅18.89% overall，domain coverage最高41.7%。确认了严重的domain bias。
- [APRIL: Learning to Repair Lean Proofs from Compiler Feedback](https://arxiv.org/abs/2602.02990) (arXiv Feb 2026): 260k repair tuples，包含path field、error_type field (lme/mlme/thme/tme)、raw error field。确认proposal对APRIL数据结构的描述准确。未做domain-stratified error分析。
- [IndiMathBench](https://arxiv.org/abs/2512.00997) (arXiv 2025): 416个formal Lean4 theorems，category-based retrieval大幅提升compilation但BEq语义正确性仍低(17.3%)。确认了static domain awareness的局限性。
- [Shebzukhov 2026](https://arxiv.org/abs/2603.24372) (arXiv Mar 2026): Cycle consistency fine-tuning on FineLeanCorpus，number theory 0.722 vs calculus 0.516。仅observational analysis，无error type分类。
- [Kim et al. "Do LLMs Game Formalization?"](https://arxiv.org/abs/2604.19459) (VerifAI-2 @ ICLR 2026): 87-99% compilation但语义不忠实（fabrication, mistranslation, omission, contradiction）。未按数学子领域分层。
- [CAM-Bench](https://arxiv.org/abs/2605.17255) (arXiv May 2026): 1000个computational/applied math Lean targets。独立验证了domain-specific evaluation的社区需求。
- [KELPS](https://arxiv.org/abs/2507.08665) (ICML 2025 AI4Math Workshop): 88.9% pass@1 on MiniF2F via Knowledge Equations。Domain-agnostic。
- [MathAtlas](https://arxiv.org/abs/2605.14061) (arXiv May 2026): 52k entities across 87 areas + 178k dependency relations。最高9.8% correctness on theorems。
- [Aria](https://arxiv.org/pdf/2510.04520) (ICLR 2026): Retrieval + iterative autoformalization via dependency graph。42.9% on homological conjectures vs 0% baselines。无domain conditioning。
- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440) (AAAI 2026): 40.5% BEq@1 on FormalMATH-Lite。Domain-agnostic。

- **调研总结**: Autoformalization领域2025-2026经历了快速发展，retrieval-augmented方法（CRAMF, DRIFT, LeanSearch v2）和修复方法（APRIL, ReForm）均在concept-level或统一策略上运作。Domain bias的存在已被MSC-180、FormalMATH、Aria等多篇工作充分文档化。然而，**没有任何已发表工作**系统性地(1)按数学子领域动态conditioning retrieval ranking，或(2)提供domain-stratified error taxonomy。Proposal在这一gap上定位准确。

【Trivial Alternative 检验】:
**存在明确的trivial alternative威胁，但proposal已部分预见并设计了对应ablation。**

最直接的trivial baseline是IndiMathBench-style的静态domain context——即简单地为每个数学类别准备一个固定的Mathlib context block，在prompt中prepend。IndiMathBench已证明这能将compilation从4.1%提升到77.9%。问题是：动态domain-conditioned retrieval相比这个trivial baseline的增量价值有多大？

Proposal设计了ablation (e)来直接回答这个问题，这是负责任的。但存在一个真实风险：如果IndiMathBench-style static context + 一个简单的domain label prompt就能capture绝大部分收益（proposal自己也承认"如果ablation (e)捕获80%+的gains，我们诚实报告"），那么整个三阶段pipeline的工程复杂性就很难justify。

第二个trivial alternative：直接用LeanSearch v2（已达SOTA nDCG@10=0.623）的domain-agnostic retrieval，是否已经足够好以至于domain conditioning的增量边际？Proposal也设计了ablation (f)。

**增量价值的核心论点**在于：(1) cross-domain problems需要multi-module retrieval，static context做不到；(2) domain-boundary ambiguity下soft probability distribution优于hard assignment；(3) retrieval set在K≥20时的noise reduction。这些argument逻辑上成立，但经验证据尚无——这正是需要实验验证的。

**结论**：trivial alternative威胁是真实的，但proposal的ablation设计合理地回应了这个威胁。Idea层面的增量价值取决于实验结果，但论证链是完整的。

【前提假设检验】:
核心claim的逻辑链中存在以下未经验证的假设：

**假设1（关键）：APRIL的error_type分布在数学子领域间存在统计显著差异。** Proposal假设JSD > 0.3对至少3个domain pair成立。这是整个Stage 1（error taxonomy）的根基。如果error分布是domain-invariant的，Stage 1产出的taxonomy虽然可以作为negative result发表，但整个pipeline的error-aware prompting（Stage 3的一部分）就失去了理论依据。值得注意的是，APRIL的error是通过人工mutation生成的（不是真实autoformalization error），mutation策略可能是domain-agnostic的，这会削弱domain-stratified分析的意义——如果mutation是uniform random的，那error_type分布的domain差异可能反映的是Mathlib代码结构差异，而非autoformalization难度差异。

**假设2（中等）：Mathlib module paths可以有效映射到数学子领域。** 这个假设相对可靠——Mathlib的模块结构确实按数学子领域组织（Topology.*, Algebra.*, Analysis.*等）。但边界情况（如MeasureTheory既涉及分析也涉及概率）需要处理。

**假设3（中等）：Domain-conditioned retrieval的增益能在BEq/semantic correctness层面体现，而不只是在compilation层面。** IndiMathBench已经展示了static domain context在compilation上的巨大提升但semantic correctness仍低（17.3%）。如果domain conditioning主要帮助的是找到正确的import/definition以通过编译，而不是解决更深层的semantic faithfulness问题，那核心contribution的价值会打折扣。

**假设4（较弱但存在）：APRIL的mutated errors是真实autoformalization errors的合理proxy。** APRIL通过系统性mutation生成错误-修复pair。这些mutation是否代表了真实autoformalization场景中模型犯的错误类型？如果不是，那么从APRIL error patterns得出的domain-specific recommendations可能不适用于实际autoformalization。

【3 维度打分】:

1. **Novelty: 中偏强** — 
   经调研确认，**没有已发表工作**做到以下两件事：(a) 按数学子领域动态conditioning autoformalization的retrieval ranking；(b) 对APRIL的error types进行domain-stratified cross-tabulation。CRAMF做concept-level disambiguation，DRIFT做statement decomposition，LeanSearch v2做domain-agnostic SOTA retrieval，IndiMathBench做static category context——但没有一个做"dynamic per-problem subdomain-conditioned retrieval ranking"。这个gap是真实的，不是人造的。
   
   然而，novelty的"高度"受限：核心idea可以简化为"在现有retrieval pipeline上加一个domain-aware reranking feature"——这是一个engineering-flavored increment而非conceptual breakthrough。Error taxonomy部分本质上是对已有数据集（APRIL）的分析性工作，是valuable但不是paradigm-shifting。
   
   与Aria（42.9% vs 0% baselines on homological conjectures）这样demonstrating domain-specific能力的工作相比，本proposal更像是systematizing已知现象（domain bias存在）而非发现新现象。

2. **Significance: 中** — 
   研究问题（domain bias in autoformalization）确实重要且well-documented：MSC-180的CV 4-6×, FormalMATH的0% vs 50%, Aria的42.9% vs 0%。多个独立来源（CAM-Bench, ShadowBench, IndiMathBench）都在指向domain-specific evaluation的需求。
   
   但significance受限于两个因素：(a) Autoformalization仍是一个相对niche的子领域，对broader AI community的影响力有限；(b) 即使pipeline完全成功，预期的improvement magnitude可能不大——从IndiMathBench的数据看，static domain context在semantic correctness上仅从接近0提升到17.3%。Dynamic conditioning能在此基础上再提升多少，是存疑的。如果总体BEq从17%提升到25%，这是有意义的进步但不是transformative。
   
   Error taxonomy作为empirical contribution有其独立价值——即使pipeline本身不work，"知道topology的autoformalization主要fail在typeclass resolution"这类发现对社区有用。但这类contribution通常被视为"solid but incremental"。

3. **Related Work: 强** — 
   这是本proposal最突出的优点。Related work的覆盖面极其全面，涵盖了2025-2026几乎所有重要的autoformalization工作（CRAMF, DRIFT, Aria, StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Herald, APRIL, LeanSearch v2, LeanPremise/LeanHammer, KELPS, IndiMathBench, MSC-180, FormalMATH, CAM-Bench, MathAtlas, Kim et al.）。每篇工作的描述经核实基本准确（APRIL的数据结构、CRAMF的方法、IndiMathBench的数字、Shebzukhov的结果等均与原文一致）。差异化定位清晰——明确说明了CRAMF做concept-level、DRIFT做decomposition、LeanSearch做domain-agnostic retrieval、IndiMathBench做static context，而本proposal做dynamic per-problem subdomain conditioning。
   
   唯一minor concern：Shebzukhov (2026) 是Stanford CS224N course project，不是peer-reviewed publication，proposal中作为evidence来引用时应注明level。

【概率估计】: [22% - 35%] 中位 28%

【估计理由】:
Novelty 中偏强：gap确实存在且proposal定位准确，但核心contribution更偏engineering increment（加domain-aware reranker）+ empirical analysis（APRIL cross-tabulation），缺乏conceptual surprise。审稿人看到"在retrieval pipeline上加domain signal"可能反应是"makes sense, I would have guessed this works"而非"surprising"。

Significance 中：问题重要但领域相对niche，且预期improvement magnitude存疑。如果最终delta只有几个百分点的BEq提升，reviewer可能认为contribution不够substantial。

Related Work 强：这是明确的加分项，展示了对领域的深入理解，且差异化定位做得好。

**上界被Novelty限制在~35%**：即使实验fully positive，核心idea仍是"在已有retrieval系统上加domain conditioning"——一个逻辑自然但不反直觉的idea。审稿人不会说"surprising"，更可能说"good engineering with solid evaluation"。

**下界被Related Work和问题formulation支撑在~22%**：proposal对问题的理解深入，差异化定位精准，ablation设计合理（特别是IndiMathBench-style baseline和LeanSearch v2 comparison），即使审稿人对novelty不兴奋，也很难argue说这个工作"not worth doing"。

概率在25-30%区间的核心原因：这是一个**well-motivated, solidly-positioned但incrementally novel**的proposal。它在做"对的事情"（address a real gap），但做的方式不够surprising。

【主要风险】:
1. **Novelty insufficiency**：核心contribution可被简化为"在CRAMF上加domain-aware reranker + 对APRIL做cross-tabulation"，审稿人可能认为这是straightforward engineering而非research contribution，特别是如果ablation显示static domain context已capture大部分gains。
2. **APRIL mutation errors作为proxy的有效性**：APRIL的errors是通过systematic mutation生成的，不是真实autoformalization errors。如果domain-stratified error patterns主要反映Mathlib代码结构差异而非autoformalization难度差异，Stage 1的taxonomy和Stage 3的error-aware prompting的价值都会被质疑。这个methodological concern可能成为reviewer的主要攻击点。
```

Sources:
- [CRAMF: Automated Formalization via Conceptual Retrieval-Augmented LLMs](https://arxiv.org/abs/2508.06931)
- [DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems](https://arxiv.org/pdf/2510.10815)
- [LeanSearch v2: Global Premise Retrieval for Lean 4](https://arxiv.org/abs/2605.13137)
- [MSC-180 Benchmark](https://arxiv.org/abs/2512.18256)
- [APRIL: Learning to Repair Lean Proofs from Compiler Feedback](https://arxiv.org/abs/2602.02990)
- [IndiMathBench](https://arxiv.org/abs/2512.00997)
- [Shebzukhov 2026 - Cycle Consistency Fine-tuning](https://arxiv.org/abs/2603.24372)
- [Kim et al. "Do LLMs Game Formalization?"](https://arxiv.org/abs/2604.19459)
- [CAM-Bench](https://arxiv.org/abs/2605.17255)
- [KELPS](https://arxiv.org/abs/2507.08665)
- [MathAtlas](https://arxiv.org/abs/2605.14061)
- [Aria](https://arxiv.org/pdf/2510.04520)
- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fd7b750-d091-4e94-9ea4-1b33265a743d",
  "isSidechain": false,
  "requestId": "req_011CbVFTDwKkAwk3g4RQ92XH",
  "type": "assistant",
  "uuid": "08d7bcc7-078e-451f-aed7-8b5b61bbe96c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Npw3KHoAMPyJWvpHWzDMd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 35825,
      "output_tokens": 4479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4479,
          "cache_read_input_tokens": 35825,
          "cache_creation_input_tokens": 586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 586
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "08d7bcc7-078e-451f-aed7-8b5b61bbe96c",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy  ## Core Problem  Curre…",
  "leafUuid": "08d7bcc7-078e-451f-aed7-8b5b61bbe96c",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization with error taxonomy",
  "sessionId": "bc7209e1-a2da-4e76-a137-a19f2189e49b"
}
```

---
