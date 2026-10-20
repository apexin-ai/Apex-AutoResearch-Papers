# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-28 (UTC).** Your job: indep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/805a9b1b-751a-472f-be96-3da9ad6bf0e5.jsonl`
- **Structured JSON:** [`299b7f42da351bb6a8b7.json`](../../sessions/29/299b7f42da351bb6a8b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T14:45:58.626Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T14:45:58.626Z",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-28 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: AAAI 2026\nTrack: AI for Science / Knowledge Representation and Reasoning\n\nDirection: Build the first domain-adaptive autoformalization pipeline that conditions formalization, retrieval, and repair strategies on mathematical subdomain (algebra, topology, analysis, number theory). The core insight is that autoformalization errors are not uniform — topology formalizations fail on typeclass instances while algebra formalizations fail on coercion chains — and domain-aware systems can exploit these patterns. Evaluate on cross-domain generalization: train on 3 domains, test on the held-out 4th.\n\nSeed Papers:\n- VeriSoftBench (arXiv 2602.18307, Feb 2026) — Proves Mathlib-trained provers fail on out-of-domain verification; motivates domain adaptation\n- APRIL (arXiv 2602.02990, Feb 2026) — 260k repair tuples enabling domain-stratified error analysis; no existing stratification\n- Herald (ICLR 2025) — 580k NL-formal pairs with Mathlib4 module provenance; enables domain labeling via module hierarchy\n- Autoformalizer with Tool Feedback (arXiv 2510.06857, Oct 2025) — Integrates repair into training but domain-agnostic; our domain-aware version is the delta\n- StepFun-Formalizer (AAAI 2026) — Current SOTA single-shot autoformalization; general-purpose baseline to beat on per-domain metrics\n- 130k Topology (arXiv 2601.03298, Jan 2026) — Domain-specific success via manual effort; motivates systematic domain adaptation\n- REAL-Prover (arXiv 2505.20613, May 2025) — Domain-aware retrieval helps proving; we extend retrieval to formalization\n- DDR (arXiv 2511.11990, Nov 2025) — Retrieval-augmented autoformalization via dependency generation; domain-agnostic baseline\n\nKnown Gaps:\n- No autoformalization system adapts its pipeline to mathematical subdomain; all treat algebra and topology identically despite different error distributions\n- APRIL's 260k repair tuples have never been stratified by domain — the domain-specific error taxonomy is uncharacterized\n- Retrieval-augmented autoformalization (DDR) retrieves domain-agnostic dependencies; domain-conditioned retrieval (Mathlib module-aware) is untested\n\nTheoretical Anchor: Domain shift theory from transfer learning — the distribution of formal language constructs (typeclasses, coercions, tactic vocabularies) differs measurably across Mathlib4 module hierarchies, creating a domain adaptation problem that standard domain-agnostic models underperform on. VeriSoftBench empirically confirms this for software domains; we extend the analysis to mathematical subdomains.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~70-80 H100-hours)\n- Must use open-source models only (Qwen2.5-7B or Goedel-Prover-V2-8B as base)\n- Evaluate on ≥3 benchmarks: miniF2F v2, ProofNet (domain-stratified), VeriSoftBench\n- Release all artifacts: model weights, domain-stratified APRIL analysis, evaluation scripts\n\nQuality Self-Checks:\n- [x] Core insight: Autoformalization errors cluster by mathematical domain, and domain-conditioned pipelines can exploit this structure.\n- [x] Why not obvious: Prior work treats autoformalization as domain-agnostic; domain adaptation requires Mathlib module hierarchy knowledge and domain-stratified training data that only became available with Herald (2025) and APRIL (2026).\n- [ ] Baseline fear test: RISK — a domain-agnostic model with more repair iterations could match 80% of the gain. Mitigation: the cross-domain generalization experiment (train on 3, test on 4th) specifically isolates domain adaptation's contribution vs. more compute.\n- [x] Information exploited: Mathlib4's module hierarchy as domain labels + APRIL's repair tuples stratified by error type and domain — information that exists in the data but no system currently uses.\n\nAvoid:\n- Framing as 'proof search improvement' — this is about formalization quality, not proving power\n- Competing on miniF2F leaderboard numbers — the contribution is per-domain reliability, not aggregate SOTA\n- Simple cycle consistency (claimed by 3 papers in 2025-2026)\n- Pure data scaling (diminishing returns per Goedel-Prover-V2)\n- Ignoring Autoformalizer with Tool Feedback as prior art — must clearly differentiate via domain-awareness**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-28?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\",\n  \"core_problem\": \"Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Shebzukhov (2026; arXiv 2603.24372) provides complementary evidence via cycle consistency fine-tuning on FineLeanCorpus: number theory achieves 0.722 cycle consistency vs. calculus at 0.516, confirming domain-dependent performance variation — but this observational analysis reports only aggregate performance per domain without analyzing how error types differ across subdomains. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further corroboration: static category-specific Mathlib context boosts syntactic compilation rates dramatically (e.g., Claude Opus 4: 4.1% → 77.9%) but BEq semantic correctness is only 17.3% (54/312 problems) and deeply domain-biased — only 12 of 98 geometry problems achieve BEq success among top models vs. far higher rates for algebra and number theory — demonstrating that even rudimentary domain awareness improves compilation but the harder semantic correctness gap persists with clear domain structure. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization, and LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) achieves 79.4% relative proof rate on OOD benchmarks via neural premise selection for Lean proving — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem in a dynamic, per-problem fashion for autoformalization. The 260k repair tuples in APRIL contain an explicit 'error_type' field encoding mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors, tme: tactic mutation errors) and an 'error' field with raw Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals'), but these have never been cross-tabulated by mathematical subdomain despite the dataset containing explicit Mathlib module paths in each tuple's 'path' field. Can we build the first autoformalization pipeline that systematically conditions its dynamic retrieval ranking and prompting signals on inferred mathematical subdomain — beyond both static category context (IndiMathBench) and concept-level disambiguation/decomposition (CRAMF/DRIFT) — and can we provide the first domain-stratified cross-tabulation of APRIL's existing error categories plus a finer-grained error taxonomy extracted from raw Lean compiler messages, characterizing how autoformalization error TYPES distribute across mathematical subdomains with statistical rigor, going beyond observational domain-stratified scores (Shebzukhov, 2026)?\",\n  \"opportunity\": \"Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs where Mathlib4 module paths can be recovered by parsing qualified theorem names from formal statements (e.g., extracting 'Topology.Basic' from theorem names like 'Topology.Basic.isOpen_compl') — the released HuggingFace dataset (FrenzyMath/Herald_statements) contains id, informal_statement, and formal_statement fields without an explicit module path column, requiring parsing or re-running the Lean-Jixia extraction pipeline; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples (59.5% theorem substitution errors, plus tactic, multi-line, and line mutations) with an explicit 'path' field encoding Mathlib module paths per tuple AND an existing 'error_type' field classifying mutation categories (lme/mlme/thme/tme) plus a raw 'error' field containing Lean compiler messages — making it the most immediately usable source for domain-stratified error analysis, as module paths can be directly mapped to mathematical subdomains without additional parsing, and our taxonomy contribution builds on APRIL's existing error categorization by cross-tabulating these mutation categories with mathematical subdomain and constructing a finer-grained taxonomy from the raw compiler error messages (parsing semantic categories such as typeclass resolution failures, coercion mismatches, tactic incompatibilities from raw strings like 'type mismatch', 'unknown constant', 'unsolved goals'); (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization — but its success demonstrates that retrieval quality alone does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall; and (7) IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) demonstrates that static category-specific Mathlib context dramatically improves compilation rates for 4 mathematical domains — proving domain awareness helps — but uses one-time static context blocks with human-labeled categories rather than dynamic per-problem conditioning, and its BEq results (17.3% for Claude Opus 4, 54/312) reveal a persistent syntactic-vs-semantic gap with strong domain bias (geometry: 12/98 BEq among top models), leaving the semantic correctness challenge unaddressed. Note: IndiMathBench is an arXiv preprint (desk-rejected from ICLR 2026); its compilation and domain-bias patterns are corroborated by peer-reviewed evidence from MSC-180, FormalMATH, and Aria. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide the strongest peer-reviewed evidence that domain-specialized problems require fundamentally different handling. Shebzukhov (2026; arXiv 2603.24372) corroborates domain performance variation via cycle consistency fine-tuning — number theory at 0.722 vs. calculus at 0.516 — but performs only post-hoc observational analysis with no domain conditioning or error type classification. LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides further evidence of domain-dependent difficulty in the Lean ecosystem: its neural premise selection achieves strong average OOD performance (20.7% on miniCTX-v2) but with dramatic project-level variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), confirming that domain-specific challenges persist even for state-of-the-art retrieval/selection systems — though LeanHammer targets proving (premise selection for tactic-based proof search) rather than autoformalization. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations as intermediate representation, outperforming DeepSeek-V3 (81%) and Herald (81.3%) — but is entirely domain-agnostic with no subdomain conditioning, operating across 6 math topics without analyzing domain-specific error patterns. The ICML 2026 AI4Math Workshop validates growing community interest in domain-aware autoformalization evaluation through two complementary challenge tracks: Track 4 (ShadowBench) evaluates end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate metrics; Track 1 (FormalRx) evaluates semantic alignment preservation using the FormalRx-Test dataset built on a 28-category SCI Error Taxonomy that classifies errors by type. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for dynamic retrieval conditioning can close the semantic correctness domain gap that static category context alone cannot address.\",\n  \"landscape\": \"Current SOTA autoformalization systems — StepFun-Formalizer (40.5% BEq@1 on FormalMATH-Lite, AAAI 2026), ATLAS (NeurIPS 2025), FormaRL (COLM 2025), ProofBridge (+31.14% semantic correctness, ICLR 2026) — all report aggregate metrics with no domain conditioning. Retrieval-augmented approaches are sophisticated but domain-agnostic: DDR (ICLR 2025 Spotlight) introduced ConNF (961 OOD pairs from one domain); CRAMF (ICLR 2026) disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) via hierarchy-informed informalization. None conditions retrieval ranking on the inferred mathematical subdomain of the input problem. In the broader Lean proving ecosystem, LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) provides the first end-to-end domain-general hammer for Lean, achieving strong average OOD performance (20.7% proof rate on miniCTX-v2, 79.4% relative to 26.1% upper bound) via an 82M-parameter neural premise selector with dynamic user-context adaptation — substantially outperforming ReProver (218M params). However, LeanHammer reveals significant project-level variation: Carleson 0%, ConNF 16%, Foundation 38%, FLT 36.4% — confirming that domain-specific challenges persist even in state-of-the-art systems. Critically, LeanHammer targets premise selection for tactic-based PROVING, not autoformalization retrieval, and uses no mathematical subdomain conditioning. KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) achieves 88.9% syntactic accuracy (pass@1) on MiniF2F — outperforming DeepSeek-V3 (81%) and Herald (81.3%) — via Knowledge Equations as an intermediate representation enabling verified multi-language autoformalization (NL → KE → Lean/Coq/Isabelle) across 60k+ NL-FL pairs spanning 6 math topics. KELPS is entirely domain-agnostic with no subdomain conditioning. Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0% — the strongest peer-reviewed evidence that domain-agnostic approaches catastrophically fail on specialized subdomains — yet Aria itself uses no domain conditioning. Domain bias is well-documented: MSC-180 found CV values 4–6× above high-variability thresholds across 60 branches; FormalMATH showed 50% algebra vs. 0% discrete math for Goedel-Prover. Domain-stratified performance has been observed: Shebzukhov (2026; arXiv 2603.24372) reports cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus) on FineLeanCorpus and 0.641 (abstract algebra) to 0.493 (analysis) on PutnamBench — confirming domain-dependent variation in autoformalization quality — but performs only observational analysis with no domain conditioning, no error type classification, and concludes that 'improvement is general rather than domain-specific.' Limited domain awareness exists in prior work: IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) uses static category-specific Mathlib context blocks achieving 77.9% compilation for Claude Opus 4 but only 17.3% BEq (54/312) with persistent geometry bias (12/98 BEq among top models) — demonstrating that static domain awareness helps compilation but not semantic correctness. SITA (AAAI 2026) applies structure-to-instance formalization for a single domain (optimization). M2F (Feb 2026) and Gloeckle et al. (Apr 2026) formalize entire textbooks in specific domains but use uniform methods. Repair approaches (APRIL, ReForm) apply uniform strategies regardless of domain; notably, APRIL's dataset already contains an 'error_type' field with mutation categories (lme/mlme/thme/tme) and a raw 'error' field with Lean compiler messages, but neither APRIL nor any subsequent work has cross-tabulated these error categories by mathematical subdomain using the dataset's own 'path' field. The community is converging on domain-stratified evaluation: the ICML 2026 AI4Math Workshop offers both ShadowBench (Track 4: end-to-end autoformalization across 8 mathematical areas with semantic alignment pass rate) and FormalRx (Track 1: semantic alignment evaluation using the 28-category SCI Error Taxonomy); Mensfelt et al. (AAAI 2026) propose a common autoformalization framework spanning math, planning, and logic. No prior work provides a systematic domain-stratified cross-tabulation of existing error categories (like APRIL's lme/mlme/thme/tme) combined with a finer-grained error taxonomy extracted from raw compiler messages, characterizing how autoformalization failure types (typeclass failures, coercion mismatches, tactic incompatibilities) distribute differently across mathematical subdomains, nor performs systematic multi-domain rotation evaluation (leave-one-domain-out across ≥5 categories).\",\n  \"inspired_by\": \"Field gaps #1 (no system conditions dynamic retrieval ranking on inferred mathematical subdomain — IndiMathBench uses static category context, CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, LeanPremise/LeanHammer achieves strong domain-general premise selection for proving but with significant project-level variation (Carleson 0% to Foundation 38%) and no subdomain conditioning, but none dynamically conditions reranking on per-problem inferred subdomain for autoformalization), #2 (APRIL 260k tuples with explicit module paths and existing error_type field (lme/mlme/thme/tme) plus raw compiler error messages never cross-tabulated by mathematical subdomain — Shebzukhov (2026) shows domain-stratified aggregate scores but no domain-stratified error type analysis exists), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with APRIL module paths + FineLeanCorpus topic labels) and #2 (domain-stratified cross-tabulation of APRIL's existing error_type categories + finer-grained taxonomy from raw compiler errors as hypothesis-driven analysis); peer-reviewed evidence from Aria (42.9% vs. 0% homological conjectures, ICLR 2026) and MSC-180 (CV 4–6× thresholds across 60 branches) as primary motivation that domain-agnostic approaches systematically fail; LeanPremise/LeanHammer (ICLR 2026) as evidence that domain-dependent difficulty persists even in SOTA Lean premise selection (project variation: 0%–38%), relevant as domain-general retrieval/selection approach in the Lean ecosystem; KELPS (ICML 2025 AI4Math Workshop) as strong domain-agnostic MiniF2F baseline (88.9% pass@1) demonstrating high syntactic accuracy is achievable without domain conditioning, raising the bar for our domain-conditioned approach to demonstrate semantic correctness gains beyond syntactic compilation; Shebzukhov (2026) as corroborating observational evidence of domain-dependent autoformalization quality; IndiMathBench's syntactic-vs-semantic gap (77.9% compilation but 17.3% BEq with persistent geometry bias) as evidence that static domain context solves compilation but not semantic correctness; ShadowBench (ICML 2026 AI4Math Track 4) validating community interest in multi-domain autoformalization evaluation and FormalRx (Track 1) with its SCI Error Taxonomy validating interest in error characterization; contrast with single-domain approaches (SITA, M2F, 130k Topology, Gloeckle et al.) demonstrating domain-specific formalization is tractable but offering no systematic multi-domain conditioning; reviewer preferences for surgical ablations including IndiMathBench-style naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.\",\n  \"approach\": \"We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (fine-tuned from Qwen3-8B; chosen over the user-specified Qwen2.5-7B because Goedel-Formalizer-V2 is the current SOTA open-source formalizer at this scale, specifically trained for NL→Lean4 translation, and Qwen3-8B provides improved reasoning over Qwen2.5 at comparable parameter count; Qwen2.5-Coder-7B-Instruct retained as additional baseline for FormaRL comparison). **Stage 1 — Domain-Stratified Error Taxonomy (PRIMARY CONTRIBUTION)**: We leverage APRIL's 260k repair tuples, which include an explicit 'path' field encoding Mathlib module paths per tuple, an existing 'error_type' field with mutation categories (lme: line mutation errors, mlme: multi-line mutation errors, thme: theorem substitution errors comprising 59.5% of the dataset, tme: tactic mutation errors), and a raw 'error' field containing Lean compiler messages (e.g., 'type mismatch', 'unknown constant', 'tactic rewrite failed', 'unsolved goals', 'application type mismatch'). We cluster the 'path' values into 5 major subdomain categories (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). Our taxonomy contribution is twofold and builds on APRIL's existing categorization rather than constructing error categories from scratch: (i) a domain-stratified cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain, testing whether mutation category distributions vary significantly across domains (e.g., whether topology has disproportionately more tactic mutation errors while algebra has more line mutation errors); (ii) a finer-grained error taxonomy extracted from the raw 'error' field by parsing Lean compiler messages into semantic categories — typeclass resolution failures, coercion mismatches, tactic incompatibilities, unknown identifier errors, type unification failures, etc. — also stratified by subdomain. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in inventing error categories de novo. We cross-reference with FineLeanCorpus's 286k verified entries (which provide hierarchical problem-level domain labels) and Herald's 580k NL-formal pairs (where module paths are recovered by parsing qualified theorem names from formal statements, e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl' — an engineering step requiring ~1 additional week beyond direct field access) to measure correlation and divergence between mathematical topic labels, formalization-level module paths, and error patterns. This goes beyond Shebzukhov (2026; arXiv 2603.24372), who reports domain-stratified aggregate cycle consistency scores (number theory 0.722 vs. calculus 0.516) but performs only observational analysis without classifying error categories per domain. **Quantitative success criteria for the error taxonomy** (testable hypotheses that define what constitutes a meaningful finding): (a) **Inter-domain error distribution divergence** — we hypothesize that Jensen-Shannon divergence between error-type distributions across domain pairs will exceed 0.3 (on a [0,1] scale) for at least 3 of 10 domain pairs (e.g., topology vs. algebra, analysis vs. logic), vs. JSD < 0.1 under random domain assignment permutation tests (1000 permutations). Rationale: topology formalizations disproportionately encounter typeclass instance resolution failures (Lean's typeclass system is heavily used for topological spaces, filters, and uniform structures) while algebra formalizations disproportionately encounter coercion chain incompleteness — if these patterns hold, the distributions will diverge substantially. (b) **Predictive power** — we hypothesize that a simple classifier trained on domain → error-type distributions will achieve ≥70% accuracy in predicting the dominant error type for held-out formalizations from a given domain, vs. ~20% baseline (assuming ~5 major error categories). This would demonstrate that knowing a problem's mathematical subdomain provides actionable information about likely failure modes — a qualitative step beyond the aggregate performance differences shown in Shebzukhov (2026). (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization accuracy by ≥5 percentage points on held-out examples from that domain vs. prompting without domain-specific error context. If hypotheses (a) and (b) hold, the taxonomy provides the first empirical evidence that autoformalization error types are systematically structured by mathematical subdomain — a finding valuable independent of any downstream pipeline delta, offering actionable guidance for all future domain-specific approaches. The FormalRx challenge (ICML 2026 AI4Math Workshop Track 1) provides a complementary 28-category SCI Error Taxonomy that classifies errors by type alone; our taxonomy is orthogonal in that it stratifies errors by mathematical subdomain, and the two taxonomies can be cross-referenced to test whether certain SCI error categories correlate with specific subdomains. ShadowBench (Track 4 of the same workshop) evaluates end-to-end autoformalization across 8 mathematical areas but does not classify error types. If the hypotheses do not hold (JSD < 0.15 across all domain pairs, prediction accuracy < 40%), we report this as a meaningful negative result: autoformalization errors are domain-invariant, and domain-adaptive approaches should focus on retrieval rather than error-aware prompting. **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (retrieval quality); LeanPremise/LeanHammer achieves strong domain-general premise selection for proving (not autoformalization); IndiMathBench provides static category context (static domain awareness). Our reranker adds an orthogonal signal: given that the input problem is dynamically classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts, decompose the statement, or apply a static category context block. The reranker operates per-problem (not per-category), using the inferred subdomain to weight retrieval results dynamically. The domain classifier for retrieval conditioning uses APRIL's explicit path field as primary training signal, supplemented by Herald's parsed module paths and FineLeanCorpus topic labels. The reranker is trained on this combined data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). We position our evaluation protocol relative to ShadowBench (Track 4): while ShadowBench evaluates across 8 mathematical areas with fixed splits, our leave-one-domain-out rotation provides systematic cross-domain generalization measurement that fixed-split evaluation cannot. Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **IndiMathBench-style naive domain prompting baseline** — prepending static category-specific Mathlib context to the input, replicating IndiMathBench's category-based retrieval approach at inference time; this tests whether the simple static approach that dramatically improves compilation also closes the semantic correctness gap, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If ablation (e) captures 80%+ of semantic correctness gains, we report this honestly as evidence that the simple approach extends to semantic correctness — a valuable finding in itself; if the full pipeline significantly outperforms, it validates the engineering investment in dynamic conditioning and error taxonomy. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology, geometry) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation of error_type by subdomain + finer-grained taxonomy from raw error field: 8h; Herald module path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 comparison: 32h)\",\n      \"timeline\": \"17 weeks (1w Herald module path parsing + APRIL path field extraction, 3w domain taxonomy + APRIL error cross-tabulation + finer-grained taxonomy from raw errors + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)\",\n      \"estimated_gpu_cost\": \"$500 (H100 at ~$2.50/hr average via RunPod/Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200 H100-hours\",\n      \"timeline\": \"13 weeks (Claude accelerates Herald path parsing, domain taxonomy design, APRIL error pattern cross-tabulation and raw error parsing, retrieval pipeline code, and ablation analysis)\",\n      \"claude_api_cost\": \"$300 (domain taxonomy extraction from APRIL path fields + error_type cross-tabulation + raw error field parsing + Herald parsed module paths + FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)\",\n      \"estimated_gpu_cost\": \"$500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier from APRIL paths: 10h; APRIL cross-tabulation + finer-grained taxonomy: 8h; Herald path parsing: 5h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including IndiMathBench-style baseline + LeanSearch v2 baseline: 30h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)\",\n      \"timeline\": \"11 weeks\",\n      \"claude_api_cost\": \"$450 (automated Herald path parsing, domain taxonomy iteration, APRIL error_type cross-tabulation and raw error parsing, repair pattern mining, hyperparameter selection, result analysis and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500\",\n      \"speed_bottleneck\": \"Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)\",\n    \"AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only ~8 weeks from today; INFEASIBLE for full pipeline given minimum 11-week auto_research timeline. A partial submission targeting error taxonomy (Stage 1) + initial domain-conditioned retrieval results (Stage 2) without full Stage 3 LoRA fine-tuning and ablation suite could be viable if Stage 1 yields strong early results within the first 6 weeks, but this requires aggressive prioritization and would omit key ablations)\",\n    \"NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)\",\n    \"ICML 2026 AI4Math Workshop — paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); paper submission is no longer possible. Only challenge track participation remains viable: ShadowBench Track 4 (challenge deadline Jun 15, 2026) for complementary multi-domain evaluation; FormalRx Track 1 (challenge deadline Jun 15, 2026) to cross-reference our subdomain-stratified error taxonomy with the SCI Error Taxonomy\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\",\n    \"Towards a Common Framework for Autoformalization (Mensfelt et al., AAAI 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\",\n    \"Premise Selection for a Lean Hammer / LeanPremise + LeanHammer (ICLR 2026; arXiv 2506.07477)\",\n    \"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch (Biyani et al., 2025; arXiv 2512.00997)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (Shebzukhov, 2026; arXiv 2603.24372)\",\n    \"Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\",\n    \"M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\",\n    \"Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\",\n    \"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\",\n    \"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\",\n    \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment (ICML 2025 AI4Math Workshop; arXiv 2507.08665)\",\n    \"ShadowBench: End-to-End Autoformalization & Proof Generation Challenge (ICML 2026 AI4Math Workshop Track 4)\",\n    \"FormalRx: Semantic Alignment Evaluation with SCI Error Taxonomy (ICML 2026 AI4Math Workshop Track 1)\"\n  ],\n  \"description\": \"We propose the first autoformalization pipeline that systematically conditions dynamic retrieval ranking and prompting signals on inferred mathematical subdomain, and the first domain-stratified error taxonomy for autoformalization — built as a cross-tabulation of APRIL's existing error_type categories (lme/mlme/thme/tme) by mathematical subdomain plus a finer-grained taxonomy extracted from APRIL's raw Lean compiler error messages (parsing semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by subdomain via APRIL's explicit 'path' field. The novelty is in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT, KELPS) treat all domains identically, yet peer-reviewed evidence demonstrates severe domain bias: MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines score 0%. LeanPremise/LeanHammer (ICLR 2026) further confirms domain-dependent difficulty with OOD project variation from 0% (Carleson) to 38% (Foundation) in Lean premise selection. Shebzukhov (2026; arXiv 2603.24372) corroborates this with cycle consistency scores ranging from 0.722 (number theory) to 0.516 (calculus), but performs only observational analysis without error type classification or domain conditioning. IndiMathBench (Biyani et al., 2025; arXiv 2512.00997) provides further evidence: static category-specific Mathlib context improves compilation dramatically but BEq semantic correctness remains only 17.3% (54/312 for Claude Opus 4) and deeply domain-biased (geometry: 12/98 BEq among top models). Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts (concept-level); DRIFT decomposes statements into atomic sub-queries (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval (nDCG@10 = 0.623); LeanPremise achieves strong premise selection for proving but not autoformalization. None dynamically conditions retrieval on the inferred subdomain of each input problem. We contribute two primary results: (1) **The first domain-stratified error taxonomy for autoformalization** — leveraging APRIL's 260k repair tuples (which include explicit Mathlib module paths in a 'path' field, existing error_type mutation categories, and raw Lean compiler errors) to cross-tabulate and stratify errors across 5 mathematical subdomain clusters, with pre-registered quantitative hypotheses: inter-domain JSD exceeding 0.3 for ≥3 domain pairs (vs. <0.1 under random assignment), domain-specific error prediction accuracy ≥70% (vs. ~20% random baseline), and ≥5 percentage point formalization improvement from domain-specific mitigation recommendations — complementing the FormalRx challenge's SCI Error Taxonomy (ICML 2026 AI4Math Track 1; 28 categories organized by error type) with subdomain-stratified analysis. (2) **Problem-level dynamic domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions per-problem, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), domain-agnostic retrieval quality (LeanSearch v2), domain-general premise selection for proving (LeanPremise), and static category context (IndiMathBench). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 categories), more rigorous than ShadowBench's (Track 4) fixed-split 8-area evaluation. Six surgical ablations include an IndiMathBench-style static domain context baseline and LeanSearch v2 retrieval replacement. The entire pipeline fits within 200 H100-hours.\",\n  \"project_name\": \"domain_adapt_autoformal\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_compute_budget\": \"RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.\",\n    \"round1_issue_2_venue_mismatch\": \"RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.\",\n    \"round1_issue_3_model_choice\": \"RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.\",\n    \"round1_issue_4_FineLeanCorpus\": \"RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.\",\n    \"round1_issue_5_MSC180\": \"RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.\",\n    \"round1_issue_6_circular_reasoning\": \"RESOLVED (Round 1): Error pattern claims reframed as hypotheses.\",\n    \"round1_issue_7_VeriSoftBench\": \"RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.\",\n    \"round1_issue_8_pipeline_complexity\": \"RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.\",\n    \"round1_issue_9_baseline_fear_test\": \"RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.\",\n    \"round2_issue_1_CRAMF_differentiation\": \"RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.\",\n    \"round2_issue_2_SITA\": \"RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.\",\n    \"round2_issue_3_impact_argument\": \"RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.\",\n    \"round2_issue_4_FineLeanCorpus_size\": \"RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.\",\n    \"round2_issue_5_ICLR2027_deadline\": \"MITIGATED (Round 2): Estimated Sep 19/24 with contingency.\",\n    \"round2_issue_6_M2F_RepoProver\": \"RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.\",\n    \"round3_issue_1_DRIFT_Aria\": \"RESOLVED: Added DRIFT (ICLR 2026 Poster) and Aria (ICLR 2026) with full technical differentiation.\",\n    \"round3_issue_2_ConNF_claim\": \"RESOLVED: Narrowed to 'first systematic multi-domain rotation evaluation protocol across ≥5 categories.'\",\n    \"round3_issue_3_error_taxonomy_elevation\": \"RESOLVED: Error taxonomy elevated to primary contribution with standalone evaluation criteria.\",\n    \"round3_issue_4_compute_trim\": \"RESOLVED: All three modes ≤200 H100-hours.\",\n    \"round3_issue_5_LeanSearch_v2\": \"RESOLVED: Added LeanSearch v2 comprehensively with ablation (f).\",\n    \"round4_issue_1_IndiMathBench\": \"RESOLVED: IndiMathBench cited comprehensively with three-axis differentiation (static vs. dynamic, syntactic vs. semantic, no error analysis).\",\n    \"round4_issue_2_quantitative_hypotheses\": \"RESOLVED: Added three pre-registered quantitative success criteria for the error taxonomy.\",\n    \"round4_issue_3_model_architecture\": \"RESOLVED: Goedel-Formalizer-V2-8B based on Qwen3-8B explicitly stated.\",\n    \"round5_issue_1_IndiMathBench_citation\": \"RESOLVED: Changed ALL 'ICLR 2026' citations for IndiMathBench to 'Biyani et al., 2025; arXiv 2512.00997' throughout.\",\n    \"round5_issue_2_BEq_correction\": \"RESOLVED: Corrected ALL instances of '~21.5%' to '17.3% (54/312 problems)' throughout.\",\n    \"round5_issue_3_ShadowBench\": \"RESOLVED: Added ShadowBench and SCI Error Taxonomy.\",\n    \"round5_issue_4_Mensfelt_framework\": \"RESOLVED: Added Mensfelt et al. (AAAI 2026) to landscape.\",\n    \"round5_issue_5_landscape_condensation\": \"RESOLVED: Condensed landscape to argument-driven organization.\",\n    \"round6_issue_1_cycle_consistency_paper\": \"RESOLVED: Cited Shebzukhov (2026; arXiv 2603.24372) throughout. Narrowed ALL novelty claims to 'first systematic domain-specific error TAXONOMY characterizing how autoformalization error TYPES distribute across subdomains.'\",\n    \"round6_issue_2_ShadowBench_SCI_conflation\": \"RESOLVED: Separated Track 1 (FormalRx) from Track 4 (ShadowBench) throughout.\",\n    \"round6_issue_3_Herald_data_engineering\": \"RESOLVED: Acknowledged Herald's limited schema; APRIL as primary domain signal.\",\n    \"round7_issue_1_APRIL_error_type_field\": \"RESOLVED: Acknowledged APRIL's existing 'error_type' field (mutation categories: lme, mlme, thme, tme) and 'error' field (raw Lean compiler messages) throughout core_problem, opportunity, landscape, approach, inspired_by, and description. Clarified that our error taxonomy contribution is a domain-stratified cross-tabulation of APRIL's existing error_type categories PLUS a finer-grained taxonomy extracted from the raw 'error' field (parsing Lean compiler messages into semantic categories: typeclass resolution failures, coercion mismatches, tactic incompatibilities, etc.), both stratified by mathematical subdomain from the 'path' field. The novelty is explicitly stated as being in domain stratification and statistical analysis (JSD, predictive power), not in constructing error categories from scratch. This prevents overclaiming while preserving the genuine novelty of domain-stratified error analysis.\",\n    \"round7_issue_2_LeanPremise_LeanHammer\": \"RESOLVED: Added LeanPremise/LeanHammer (ICLR 2026; arXiv 2506.07477) to core_problem, opportunity, landscape, approach, inspired_by, description, and key_references. Characterized as first end-to-end domain-general hammer for Lean with 82M-param neural premise selector, 79.4% relative proof rate OOD on miniCTX-v2 (20.7% absolute vs. 26.1% upper bound), significant project variation (Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%), dynamic user-context adaptation. Explicitly differentiated: targets premise selection for tactic-based proving (not autoformalization retrieval); uses no mathematical subdomain conditioning; outperforms ReProver (218M). Its project-level variation provides additional evidence of domain-dependent difficulty in the Lean ecosystem.\",\n    \"round7_issue_3_KELPS\": \"RESOLVED: Added KELPS (ICML 2025 AI4Math Workshop; arXiv 2507.08665) to opportunity, landscape, inspired_by, description, and key_references. Characterized as achieving 88.9% syntactic accuracy (pass@1) on MiniF2F via Knowledge Equations intermediate representation (NL → KE → Lean/Coq/Isabelle), outperforming DeepSeek-V3 (81%) and Herald (81.3%), covering 60k+ NL-FL pairs across 6 math topics. Entirely domain-agnostic. Noted as ICML 2025 AI4Math Workshop paper (not main conference). Added to inspired_by as strong domain-agnostic baseline raising the bar for our approach to demonstrate semantic correctness gains beyond syntactic compilation.\",\n    \"round7_issue_4_venue_timeline_fixes\": \"RESOLVED: AAAI 2027 changed from 'STRETCH' to explicitly 'INFEASIBLE for full pipeline given minimum 11-week auto_research timeline' (~8 weeks available), with explicit description of what a partial submission could target (error taxonomy Stage 1 + initial retrieval Stage 2, without full LoRA fine-tuning and ablation suite). ICML 2026 AI4Math Workshop updated to note paper submission deadline May 25, 2026 has PASSED (3 days ago as of May 28, 2026); only challenge track participation (ShadowBench Track 4, FormalRx Track 1) with June 15 deadline remains viable.\"\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Compute budget violation — estimates ~600 A100-hours (~300-400 H100-equivalent), 1.5-2x over user's hard constraint of ≤200 H100-hours\", \"CRITICAL: Venue mismatch — user requested 'AAAI 2026' (deadline August 2025, already past); Generator silently shifted to AAAI 2027 (July 2026). With today's date May 28, 2026, the July 28 deadline is only 8 weeks away, making even the 6-week auto_research timeline razor-thin\", \"CRITICAL: Model choice violation — user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' but Generator uses 'Qwen3-8B'\", \"Missing critical reference: CriticLean + FineLeanCorpus (509k entries with hierarchical domain labels like 'Algebra -> Intermediate Algebra -> Functional Equations' and difficulty scores) — this dataset already provides domain-stratified autoformalization data, undermining the claim that 'domain-specific error taxonomy is uncharacterized'\", \"Missing reference: MSC-180 benchmark (arXiv 2512.18256) evaluates theorem provers across 60 mathematical branches via MSC2020 classification with coefficient of variation metrics — directly relevant to domain bias analysis\", \"Circular reasoning in motivation: specific error patterns ('topology fails on typeclass instances, algebra fails on coercion chains') are stated as known facts to motivate the work, but discovering these patterns is actually a claimed contribution of the work\", \"VeriSoftBench evaluates software verification proofs, not mathematical autoformalization — including it as an autoformalization benchmark is misleading and doesn't match the paper's scope\", \"The 4-stage pipeline (classifier + APRIL stratification + domain retrieval + domain-conditioned GRPO with 15-subdomain LoRA routing) has excessive engineering complexity for the compute and timeline constraints\", \"Baseline fear test risk: acknowledged but not adequately mitigated — the leave-one-domain-out experiment isolates domain adaptation contribution, but if the delta is small (e.g., 2-3 percentage points), the paper's contribution becomes marginal\"]\nFeedback: To revise into a passable submission: (1) **Drastically simplify the pipeline** to fit within 200 H100-hours — drop domain-routed LoRA adapters (the most compute-hungry component) and focus on domain-conditioned retrieval + domain-stratified error analysis as the core contributions, which are cheaper and more novel; (2) **Use the user-specified models** (Qwen2.5-7B or Goedel-Prover-V2-8B); (3) **Cite and differentiate from FineLeanCorpus** — acknowledge its domain labels exist but argue your Mathlib module-path-based domain taxonomy captures formalization-specific structure (typeclass/coercion patterns) that FineLeanCorpus's problem-level labels do not; (4) **Reframe error pattern claims as hypotheses** to be empirically validated, not established facts; (5) **Replace VeriSoftBench** with FormalMATH-stratified evaluation or MathAtlas — both are mathematical benchmarks with domain structure; (6) **Target ICLR 2027** (estimated September 2026) instead of AAAI 2027 to get an extra ~8 weeks of development time; (7) **Reduce subdomain granularity** from 15 to 4-5 major domains (algebra, topology, analysis, number theory, combinatorics) to keep the experimental matrix manageable within budget; (8) **Strengthen the baseline comparison** by including a domain-agnostic model with matched compute (same number of repair iterations) as a control to convincingly demonstrate domain-conditioning adds value beyond more compute.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MODERATE: CRAMF differentiation insufficient — CRAMF explicitly mentions 'contextual query augmentation with domain- and application-level signals' and stores Mathlib module paths (θ_p) per definition. The proposal claims CRAMF 'never conditions retrieval reranking on mathematical subdomain' but doesn't directly acknowledge or rebut CRAMF's existing domain signals. A reviewer familiar with CRAMF will ask: 'How is your domain conditioning different from CRAMF's domain-level contextual query augmentation?'\", \"MODERATE: SITA (AAAI 2026) not cited — SITA demonstrates domain-specific autoformalization via structure-to-instance approach using Lean's typeclass mechanism, evaluated on 42 optimization problems. While a different paradigm (abstract structure instantiation vs. subdomain conditioning), it contradicts the 'first domain-specific autoformalization' framing and should be discussed as related work.\", \"MODERATE: Impact uncertainty — the matched-compute baseline mitigates the baseline fear test but doesn't address it: if domain-agnostic models with domain context in the prompt (a trivially simpler approach than the full pipeline) capture 80%+ of the gain, the multi-stage pipeline adds marginal value. The paper needs a stronger argument for why the full pipeline (classifier + domain reranking + domain error context) is necessary vs. simply adding 'This is a topology problem' to the prompt.\", \"MINOR: FineLeanCorpus size inaccuracy — claims '509k entries' but verified data shows 285,957 fully verified entries. The 509k figure may include unverified entries, but using it without qualification is misleading.\", \"MINOR: ICLR 2027 primary target is speculative — deadline not officially announced. If the actual deadline is earlier (e.g., August 2026), the 16-week timeline becomes infeasible.\", \"MINOR: M2F (Feb 2026) and RepoProver (Apr 2026) not cited — both perform domain-specific autoformalization at textbook scale (real analysis, convex analysis, algebraic combinatorics), providing evidence that different mathematical domains require different formalization strategies, supporting the proposal's motivation.\"]\nFeedback: The proposal has addressed all Round 1 critical issues well (compute, venue, model, VeriSoftBench, circular reasoning, pipeline simplification). The remaining issues are moderate rather than critical. To reach pass threshold: (1) **Sharpen CRAMF differentiation**: Explicitly acknowledge CRAMF's 'domain- and application-level signals' in contextual query augmentation and its stored module paths (θ_p), then argue precisely why this falls short of systematic subdomain conditioning — e.g., CRAMF's domain signals are used for disambiguating polysemous concepts, not for conditioning the retrieval ranking on the input's mathematical subdomain. (2) **Cite and differentiate from SITA (AAAI 2026)**: Acknowledge it as domain-specific autoformalization via structure-to-instance approach, but clarify your work conditions the general-purpose pipeline on subdomain identity, whereas SITA targets a specific mathematical pattern (abstract-to-concrete instantiation) in a single domain. (3) **Strengthen the impact argument**: Add an explicit ablation comparing 'naive domain prompting' (just prepending domain label to input, zero engineering) vs. full pipeline with domain-conditioned retrieval and error context. If the full pipeline doesn't significantly outperform naive domain prompting, the paper's contribution is weaker. Frame the error taxonomy as a co-equal contribution, not a byproduct. (4) **Fix FineLeanCorpus size**: Use '286k fully verified entries (509k total)' for accuracy. (5) **Add M2F and SITA to landscape discussion** as evidence that domain-specific approaches exist but are either single-domain (SITA, M2F) or manual (130k Topology), motivating your systematic multi-domain approach.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE: Several relevant ICLR 2026 systems missing from landscape — DRIFT (ICLR 2026 Poster) performs concept-level decomposition for targeted retrieval and nearly doubles F1 on ProofNet; its sub-query decomposition is conceptually related to domain-conditioned retrieval and must be differentiated. Aria (ICLR 2026) achieves 68.5% on ProofNet and 42.9% on homological conjectures (all other baselines 0%) but is domain-agnostic — these per-domain results directly support the proposal's domain bias motivation and should appear in the landscape analysis.\", \"MODERATE: ConNF benchmark (961 OOD informal-formal pairs, from DDR/ICLR 2025 Spotlight) specifically tests cross-domain generalization in autoformalization. The proposal claims to introduce 'the first leave-one-domain-out evaluation protocol for autoformalization' but does not cite ConNF. While ConNF tests a single OOD domain (New Foundations set theory) rather than systematic multi-domain rotation, the claim needs to be narrowed or ConNF explicitly differentiated.\", \"MODERATE: Impact argument remains the weakest link — the proposal correctly identifies the risk that naive domain prompting captures 80%+ of gains, but the framing still positions the multi-stage pipeline as the main system contribution. If the error taxonomy is the safety net, it should be promoted to unambiguous primary contribution with clearer standalone evaluation criteria (e.g., inter-domain error pattern correlation metrics, actionable recommendations per domain).\", \"MINOR: Compute budget slightly exceeds constraint — auto_research mode estimates 210 H100-hours vs. the user's hard ≤200 H100-hour cap. Need to either trim 10 hours (e.g., reduce ablation sweep scope) or justify the overage.\", \"MINOR: LeanSearch v2 (May 2026) achieves SOTA premise retrieval 'without domain-specific fine-tuning' — this is directly relevant since it suggests domain-agnostic retrieval can be very strong, potentially challenging the motivation for domain-conditioned retrieval. Should be cited and its implications discussed.\"]\nFeedback: The proposal has matured significantly across three rounds and is close to passing. All Round 2 issues were addressed well, particularly the CRAMF differentiation (now technically precise and verified accurate). To reach pass threshold: (1) **Add DRIFT, ConNF, LeanSearch v2, and Aria's per-domain results** to the landscape — DRIFT and LeanSearch v2 are recent strong retrieval baselines; ConNF is the existing OOD autoformalization benchmark; Aria's per-domain gaps (42.9% on homological conjectures vs. 0% for all baselines) directly support the domain bias motivation. (2) **Narrow the 'first leave-one-domain-out' claim** — ConNF already tests OOD generalization, so specify 'first systematic multi-domain rotation evaluation' across ≥4 mathematical subdomain categories. (3) **Elevate the error taxonomy to unambiguous primary contribution** — define standalone evaluation criteria: (a) inter-domain error pattern clustering metrics (e.g., how distinct are topology vs. algebra error distributions?), (b) predictive power of domain-specific error patterns (can the taxonomy predict which errors a new formalization will encounter?), (c) actionable recommendations per domain. This makes the paper valuable even if the downstream delta is modest. (4) **Trim 10 H100-hours** from the auto_research estimate to fit within the ≤200 constraint. (5) **Discuss LeanSearch v2's domain-agnostic SOTA** — if domain-agnostic retrieval is already very strong, what specifically does domain conditioning add beyond what scale/engineering can achieve?\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE: IndiMathBench (ICLR 2026, arXiv 2512.00997) not cited — uses category-specific static Mathlib context for 4 mathematical domains (Geometry, Algebra, Number Theory, Set Theory & Combinatorics) to condition autoformalization prompts. While IndiMathBench uses static context blocks (not dynamic retrieval conditioning) and does not claim novelty in domain awareness, it IS a form of domain-conditioned autoformalization. The proposal's claim of being 'the first autoformalization pipeline that conditions on inferred mathematical subdomain' must acknowledge and differentiate from IndiMathBench. IndiMathBench's approach is essentially the 'naive domain prompting' ablation the proposal already plans — this connection should be made explicit.\", \"MODERATE: Impact argument remains below the 4.0 threshold — IndiMathBench achieves 95.3% syntactic validity with simple category-specific static context, suggesting that even rudimentary domain awareness is powerful. This strengthens the proposal's motivation (domain information helps) but weakens the pipeline contribution (maybe simple approaches suffice). The error taxonomy needs to be framed even more forcefully as the primary contribution — with quantitative hypotheses about expected inter-domain JSD values and prediction accuracy thresholds that would constitute a meaningful finding.\", \"MINOR: Goedel-Formalizer-V2-8B is fine-tuned from Qwen3-8B, not Qwen2.5. The user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' — using the Formalizer variant is reasonable (same family, specialized for formalization) but should be explicitly justified since the base architecture differs from user's Qwen2.5 specification.\"]\nFeedback: The proposal is very close to passing (avg 3.875/5.0) after 4 strong revision rounds. Two targeted fixes should clear the threshold: (1) **Cite IndiMathBench and make it your 'naive domain prompting' reference implementation**: IndiMathBench's category-specific static context is essentially the simple baseline your ablation (e) already plans. Explicitly map your ablation to IndiMathBench's approach: 'Our naive domain prompting baseline (ablation e) replicates IndiMathBench's category-specific context approach; our full pipeline adds dynamic domain-conditioned retrieval reranking and error-taxonomy-driven prompting on top.' This transforms a missing reference into a strengthened experimental design. Narrow the novelty claim to: 'first system to condition dynamic retrieval ranking on inferred mathematical subdomain and provide systematic domain-specific error characterization.' (2) **Set quantitative success criteria for the error taxonomy to strengthen impact**: State concrete hypotheses — e.g., 'We hypothesize JSD between topology and algebra error distributions exceeds 0.3 (vs. <0.1 for random domain assignments)' and 'domain-specific error prediction accuracy exceeds 70% on held-out formalizations.' This transforms the error taxonomy from 'we'll analyze and see what we find' into a testable scientific claim that reviewers can evaluate. If these hypotheses hold, the paper has clear value regardless of pipeline delta.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE: IndiMathBench was DESK REJECTED at ICLR 2026 — cited as 'ICLR 2026' throughout the proposal (core_problem, opportunity, landscape, approach, description), falsely implying acceptance. Must be cited as 'arXiv 2512.00997' or 'IndiMathBench (Biyani et al., 2025)'. A desk-rejected paper's experimental claims carry less weight than peer-reviewed results, and reviewers who know its status will question the proposal's due diligence.\", \"MINOR: IndiMathBench Claude Opus 4 BEq is 17.3% (54/312 problems), not '~21.5%' as claimed in multiple sections. The 21.5% figure does not correspond to any metric in the paper. This numerical error appears in core_problem, opportunity, and description — undermining trust in the proposal's data verification.\", \"MINOR: ICML 2026 AI4Math Workshop (Jul 11, 2026) features ShadowBench — 126 problems across 8 mathematical areas with domain-tiered evaluation and Semantic Alignment metrics. This workshop challenge directly overlaps with the proposal's domain-stratified evaluation contribution and should be cited. Concurrent community interest in domain-stratified autoformalization evaluation both validates the proposal's direction and signals competition.\", \"MINOR: 'Towards a Common Framework for Autoformalization' (AAAI 2026) discusses cross-domain autoformalization challenges and the need for methods that 'transfer reasoning patterns and formalization strategies across different areas' — tangentially relevant and should be acknowledged, though it focuses on cross-formalism domains (math vs. planning vs. logic) rather than mathematical subdomain adaptation.\"]\nFeedback: The proposal is very close to the pass threshold (avg 3.75/5.0) after 5 strong revision rounds. Two targeted fixes should clear 4.0: (1) **Fix IndiMathBench citation**: Change 'ICLR 2026' to 'arXiv 2512.00997' or 'IndiMathBench (Biyani et al., 2025, desk-rejected ICLR 2026 submission)' throughout. The paper's results remain usable as empirical evidence, but its desk-rejection status means reviewers will scrutinize claims derived from it more carefully — consider reducing reliance on IndiMathBench-specific numbers and strengthening the argument with peer-reviewed evidence (MSC-180, FormalMATH, Aria's homological results are all stronger references). Fix the BEq number to 17.3% (54/312). (2) **Cite and position relative to ICML 2026 ShadowBench**: The AI4Math Workshop's ShadowBench evaluates autoformalization across 8 mathematical areas with SA metrics — this validates community interest in domain-stratified evaluation but also means you're not the only ones thinking about it. Cite it and argue your evaluation protocol (leave-one-domain-out rotation across 5+ categories with systematic ablations) is more rigorous than ShadowBench's fixed-split evaluation. (3) **Consider condensing the landscape section** — at its current length, it reads like a survey rather than a research proposal. The core contribution can be stated in 1/3 the space.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"MODERATE: Missing reference — Cycle Consistency Fine-tuning (arXiv:2603.24372, Shebzukhov, March 2026) provides domain-stratified autoformalization results using FineLeanCorpus domain labels, showing number theory at 0.722 cycle consistency vs. calculus at 0.516. While it performs only post-hoc observational analysis (no domain conditioning), it partially pre-empts claims of providing 'the first empirical characterization of how autoformalization errors distribute across mathematical subdomains.' The proposal's novelty claim must be narrowed to 'first domain-specific error TAXONOMY characterizing error TYPES by subdomain' (not just aggregate performance by domain).\", \"MINOR: ShadowBench/SCI Error Taxonomy conflation — the proposal repeatedly states 'ShadowBench challenge (126 problems across 8 mathematical areas with Semantic Alignment metrics and a 28-category SCI Error Taxonomy)' but the 28-category SCI Error Taxonomy belongs to Track 1 (FormalRx challenge), not Track 4 (ShadowBench). These are separate challenge tracks within the same ICML 2026 AI4Math Workshop. The conflation appears in core_problem, approach, and description.\", \"MINOR: Herald module path claim overstated — the proposal states Herald provides '580k NL-formal pairs tagged with Mathlib4 module paths enabling automatic formalization-level domain labeling' but the released HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with no explicit module path column. Domain info must be parsed from qualified theorem names embedded in formal statements or recovered via re-running the Lean-Jixia extraction pipeline. This is feasible but adds unacknowledged engineering effort.\"]\nFeedback: The proposal is very close to passing (avg 3.5/5.0 → needs 4.0). Three targeted fixes for Round 7: (1) **Cite the cycle consistency paper (arXiv:2603.24372)** and narrow the novelty claim: this paper already shows autoformalization performance varies by domain (number theory > calculus), so you cannot claim to be 'the first to show domain variation exists.' Narrow to: 'first systematic domain-specific error TAXONOMY that characterizes how autoformalization failure TYPES (not just aggregate accuracy) distribute across subdomains — going beyond the observational domain-stratified scores in Shebzukhov (2026) to classify error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor.' (2) **Fix the ShadowBench/SCI conflation**: Separate the two tracks — ShadowBench (Track 4) uses Semantic Alignment metrics for end-to-end autoformalization; the SCI Error Taxonomy (28 categories) belongs to Track 1 (FormalRx) for semantic alignment evaluation. Both are relevant but distinct. Your error taxonomy complements the SCI taxonomy (which categorizes by error type alone) by adding subdomain stratification. (3) **Acknowledge Herald data engineering**: Note that Herald's module paths must be parsed from qualified names in formal statements (e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl') rather than read from a dedicated field, and account for this in the timeline (~1 additional week). Alternatively, note that APRIL's HuggingFace dataset includes an explicit 'path' field that directly encodes Mathlib module paths, making it the more immediately usable source for domain labeling.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MINOR: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477) not cited — the first end-to-end domain-general hammer for Lean with dynamic user-context adaptation and strong out-of-distribution generalization (79.4% relative to upper bound on miniCTX-v2). While targeting premise selection for proving (not autoformalization retrieval) and not conditioning on mathematical subdomain per se, it demonstrates a relevant domain-generalization approach in the Lean ecosystem that should be acknowledged in the landscape.\", \"MINOR: AAAI 2027 (July 28, 2026) is listed as a target venue but is mathematically infeasible — 8 weeks from today vs. minimum 11-week auto_research timeline. Should be downgraded from 'STRETCH' to explicitly infeasible, or the timeline should explain what partial submission (e.g., error taxonomy only) could be ready in 8 weeks.\", \"MINOR: ICML 2026 AI4Math Workshop paper submission deadline was May 25, 2026 (already passed 3 days ago). The target_venues entry correctly identifies challenge track participation (June 15 deadline) but should note that paper submission is no longer possible.\", \"MINOR: The APRIL dataset's HuggingFace schema includes an 'error_type' field already classifying errors into categories (theorem substitution, tactic errors, multi-line errors, line mutations). The proposal's 'domain-specific error taxonomy' contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types — this should be stated explicitly to avoid overclaiming. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in constructing a new error classification.\", \"MINOR: KELPS (arXiv 2507.08665) achieves 88.9% syntactic accuracy on MiniF2F via Knowledge Equations and multi-language autoformalization — a strong baseline not currently cited that outperforms several referenced systems.\"]\nFeedback: The proposal has matured substantially across 6 revision rounds and all critical/moderate issues are resolved. Remaining issues are all minor. To clear the 4.0 threshold: (1) **Acknowledge APRIL's existing error_type field** and precisely describe the taxonomy contribution as domain-stratified cross-tabulation with statistical rigor (JSD, prediction), not a new error classification — this prevents overclaiming while preserving the genuine novelty of domain stratification. (2) **Fix venue timeline accuracy**: mark AAAI 2027 as infeasible (not 'stretch'), note ICML 2026 paper deadline has passed, and specify what partial submission could target AAAI 2027 if desired (e.g., error taxonomy + initial retrieval results without full ablations). (3) **Add LeanPremise/LeanHammer** to landscape as a strong domain-general retrieval baseline in the Lean ecosystem, differentiating by target task (premise selection for proving vs. retrieval for autoformalization). (4) **Consider adding KELPS** as a strong MiniF2F baseline. These four fixes are all straightforward and should be completable in one revision round.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T14:45:58.629Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T14:45:58.629Z",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-28T14:45:58.642Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-28 (UTC).**

Your job: independently verify this idea's claims via web_search, then issue a verdict.

## User requirements
The user asked for: **Target: AAAI 2026
Track: AI for Science / Knowledge Representation and Reasoning

Direction: Build the first domain-adaptive autoformalization pipeline that conditions formalization, retrieval, and repair strategies on mathematical subdomain (algebra, topology, analysis, number theory). The core insight is that autoformalization errors are not uniform — topology formalizations fail on typeclass instances while algebra formalizations fail on coercion chains — and domain-aware systems can exploit these patterns. Evaluate on cross-domain generalization: train on 3 domains, test on the held-out 4th.

Seed Papers:
- VeriSoftBench (arXiv 2602.18307, Feb 2026) — Proves Mathlib-trained provers fail on out-of-domain verification; motivates domain adaptation
- APRIL (arXiv 2602.02990, Feb 2026) — 260k repair tuples enabling domain-stratified error analysis; no existing stratification
- Herald (ICLR 2025) — 580k NL-formal pairs with Mathlib4 module provenance; enables domain labeling via module hierarchy
- Autoformalizer with Tool Feedback (arXiv 2510.06857, Oct 2025) — Integrates repair into training but domain-agnostic; our domain-aware version is the delta
- StepFun-Formalizer (AAAI 2026) — Current SOTA single-shot autoformalization; general-purpose baseline to beat on per-domain metrics
- 130k Topology (arXiv 2601.03298, Jan 2026) — Domain-specific success via manual effort; motivates systematic domain adaptation
- REAL-Prover (arXiv 2505.20613, May 2025) — Domain-aware retrieval helps proving; we extend retrieval to formalization
- DDR (arXiv 2511.11990, Nov 2025) — Retrieval-augmented autoformalization via dependency generation; domain-agnostic baseline

Known Gaps:
- No autoformalization system adapts its pipeline to mathematical subdomain; all treat algebra and topology identically despite different error distributions
- APRIL's 260k repair tuples have never been stratified by domain — the domain-specific error taxonomy is uncharacterized
- Retrieval-augmented autoformalization (DDR) retrieves domain-agnostic dependencies; domain-conditioned retrieval (Mathlib module-aware) is untested

Theoretical Anchor: Domain shift theory from transfer learning — the distribution of formal language constructs (typeclasses, coercions, tactic vocabularies) differs measurably across Mathlib4 module hierarchies, creating a domain adaptation problem that standard domain-agnostic models underperform on. VeriSoftBench empirically confirms this for software domains; we extend the analysis to mathematical subdomains.

Constraints:
- Compute: ≤200 H100-hours (estimated ~70-80 H100-hours)
- Must use open-source models only (Qwen2.5-7B or Goedel-Prover-V2-8B as base)
- Evaluate on ≥3 benchmarks: miniF2F v2, ProofNet (domain-stratified), VeriSoftBench
- Release all artifacts: model weights, domain-stratified APRIL analysis, evaluation scripts

Quality Self-Checks:
- [x] Core insight: Autoformalization errors cluster by mathematical domain, and domain-conditioned pipelines can exploit this structure.
- [x] Why not obvious: Prior work treats autoformalization as domain-agnostic; domain adaptation requires Mathlib module hierarchy knowledge and domain-stratified training data that only became available with Herald (2025) and APRIL (2026).
- [ ] Baseline fear test: RISK — a domain-agnostic model with more repair iterations could match 80% of the gain. Mitigation: the cross-domain generalization experiment (train on 3, test on 4th) specifically isolates domain adaptation's contribution vs. more compute.
- [x] Information exploited: Mathlib4's module hierarchy as domain labels + APRIL's repair tuples stratified by error type and domain — information that exists in the data but no system currently uses.

Avoid:
- Framing as 'proof search improvement' — this is about formalization quality, not proving power
- Competing on miniF2F leaderboard numbers — the contribution is per-domain reliability, not aggregate SOTA
- Simple cycle consistency (claimed by 3 papers in 2025-2026)
- Pure data scaling (diminishing returns per Goedel-Prover-V2)
- Ignoring Autoformalizer with Tool Feedback as prior art — must clearly differentiate via domain-awareness**
Evaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be "revise" or "fail".

## 核心要求：非常仔细地调研，非常仔细地思考

你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。

### 调研要求

1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。
   每个验证维度建议用 2-3 种不同的搜索查询。

2. **可行性深度检查**：
   - 搜索类似实验的实际成本/周期
   - 检查 claimed baselines 是否可复现
   - 验证所需的 datasets/models 是否真的可以获取

3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：
   - 尝试不同的关键词组合
   - 同时检查 arXiv 和 conference proceedings
   - 寻找相邻领域的并行/concurrent 工作

4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。

### 思考要求

5. **独立判断**：
   - 不要因为 Generator 说得有道理就轻易 pass
   - 思考这个 idea 在实际执行中会遇到什么困难
   - 考虑这个 idea 对领域的真实贡献

6. **评分诚实**：
   - 4 分意味着"确实很好"，5 分意味着"令人兴奋"
   - Agent 评分经常虚高，你的职责就是纠正这种偏差


## 论文搜索策略

你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。

### 搜索源（推荐每个维度使用 2 个不同来源）

1. **arXiv 预印本**（最新工作）:
   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文
   - `site:arxiv.org {method_name}` — 按具体方法名搜索
   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作

2. **Google Scholar**（引用关系 + 综合覆盖）:
   - `{topic} 2026 site:scholar.google.com`
   - `"{exact paper title}"` — 验证论文是否真实存在
   - `"{author name}" {topic} 2026` — 按活跃作者追踪

3. **Papers With Code**（SOTA 排行 + 代码可用性）:
   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜
   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局

4. **OpenReview**（会议审稿 + 同行评价）:
   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文
   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价

5. **Semantic Scholar**（语义搜索 + 引用图谱）:
   - `semantic scholar {topic} survey 2026` — 找综述论文

6. **GitHub**（实现验证）:
   - `site:github.com {method_name} {task}` — 验证开源实现是否存在

### 搜索维度

1. **正向搜索**：直接搜索主题相关论文
2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？
3. **相邻领域搜索**：其他领域是否已解决类似问题
4. **反面搜索**：找到反对你 idea 的证据
5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work


## 竞争论文专项搜索（Reviewer 独有）

1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题
2. **知名团队追踪**：搜索相关团队最近的论文
3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`
4. **arXiv 近 3 个月密集搜索**

## Review checklist
1. **SOTA freshness**: Are baselines actually current SOTA?
2. **Reference verification**: Do cited papers actually exist?
3. **Gap validity**: Does the claimed gap still exist?
4. **Venue validity**: Are target venue deadlines after 2026-05-28?
5. **Feasibility**: Is the resource estimate realistic?
6. **Novelty**: Is this sufficiently different from existing work?
7. **Cost realism**: Are the three mode estimates internally consistent?

## Idea under review (round 8/10)
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


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Compute budget violation — estimates ~600 A100-hours (~300-400 H100-equivalent), 1.5-2x over user's hard constraint of ≤200 H100-hours", "CRITICAL: Venue mismatch — user requested 'AAAI 2026' (deadline August 2025, already past); Generator silently shifted to AAAI 2027 (July 2026). With today's date May 28, 2026, the July 28 deadline is only 8 weeks away, making even the 6-week auto_research timeline razor-thin", "CRITICAL: Model choice violation — user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' but Generator uses 'Qwen3-8B'", "Missing critical reference: CriticLean + FineLeanCorpus (509k entries with hierarchical domain labels like 'Algebra -> Intermediate Algebra -> Functional Equations' and difficulty scores) — this dataset already provides domain-stratified autoformalization data, undermining the claim that 'domain-specific error taxonomy is uncharacterized'", "Missing reference: MSC-180 benchmark (arXiv 2512.18256) evaluates theorem provers across 60 mathematical branches via MSC2020 classification with coefficient of variation metrics — directly relevant to domain bias analysis", "Circular reasoning in motivation: specific error patterns ('topology fails on typeclass instances, algebra fails on coercion chains') are stated as known facts to motivate the work, but discovering these patterns is actually a claimed contribution of the work", "VeriSoftBench evaluates software verification proofs, not mathematical autoformalization — including it as an autoformalization benchmark is misleading and doesn't match the paper's scope", "The 4-stage pipeline (classifier + APRIL stratification + domain retrieval + domain-conditioned GRPO with 15-subdomain LoRA routing) has excessive engineering complexity for the compute and timeline constraints", "Baseline fear test risk: acknowledged but not adequately mitigated — the leave-one-domain-out experiment isolates domain adaptation contribution, but if the delta is small (e.g., 2-3 percentage points), the paper's contribution becomes marginal"]
Feedback: To revise into a passable submission: (1) **Drastically simplify the pipeline** to fit within 200 H100-hours — drop domain-routed LoRA adapters (the most compute-hungry component) and focus on domain-conditioned retrieval + domain-stratified error analysis as the core contributions, which are cheaper and more novel; (2) **Use the user-specified models** (Qwen2.5-7B or Goedel-Prover-V2-8B); (3) **Cite and differentiate from FineLeanCorpus** — acknowledge its domain labels exist but argue your Mathlib module-path-based domain taxonomy captures formalization-specific structure (typeclass/coercion patterns) that FineLeanCorpus's problem-level labels do not; (4) **Reframe error pattern claims as hypotheses** to be empirically validated, not established facts; (5) **Replace VeriSoftBench** with FormalMATH-stratified evaluation or MathAtlas — both are mathematical benchmarks with domain structure; (6) **Target ICLR 2027** (estimated September 2026) instead of AAAI 2027 to get an extra ~8 weeks of development time; (7) **Reduce subdomain granularity** from 15 to 4-5 major domains (algebra, topology, analysis, number theory, combinatorics) to keep the experimental matrix manageable within budget; (8) **Strengthen the baseline comparison** by including a domain-agnostic model with matched compute (same number of repair iterations) as a control to convincingly demonstrate domain-conditioning adds value beyond more compute.

### Round 2 review
Verdict: revise
Issues: ["MODERATE: CRAMF differentiation insufficient — CRAMF explicitly mentions 'contextual query augmentation with domain- and application-level signals' and stores Mathlib module paths (θ_p) per definition. The proposal claims CRAMF 'never conditions retrieval reranking on mathematical subdomain' but doesn't directly acknowledge or rebut CRAMF's existing domain signals. A reviewer familiar with CRAMF will ask: 'How is your domain conditioning different from CRAMF's domain-level contextual query augmentation?'", "MODERATE: SITA (AAAI 2026) not cited — SITA demonstrates domain-specific autoformalization via structure-to-instance approach using Lean's typeclass mechanism, evaluated on 42 optimization problems. While a different paradigm (abstract structure instantiation vs. subdomain conditioning), it contradicts the 'first domain-specific autoformalization' framing and should be discussed as related work.", "MODERATE: Impact uncertainty — the matched-compute baseline mitigates the baseline fear test but doesn't address it: if domain-agnostic models with domain context in the prompt (a trivially simpler approach than the full pipeline) capture 80%+ of the gain, the multi-stage pipeline adds marginal value. The paper needs a stronger argument for why the full pipeline (classifier + domain reranking + domain error context) is necessary vs. simply adding 'This is a topology problem' to the prompt.", "MINOR: FineLeanCorpus size inaccuracy — claims '509k entries' but verified data shows 285,957 fully verified entries. The 509k figure may include unverified entries, but using it without qualification is misleading.", "MINOR: ICLR 2027 primary target is speculative — deadline not officially announced. If the actual deadline is earlier (e.g., August 2026), the 16-week timeline becomes infeasible.", "MINOR: M2F (Feb 2026) and RepoProver (Apr 2026) not cited — both perform domain-specific autoformalization at textbook scale (real analysis, convex analysis, algebraic combinatorics), providing evidence that different mathematical domains require different formalization strategies, supporting the proposal's motivation."]
Feedback: The proposal has addressed all Round 1 critical issues well (compute, venue, model, VeriSoftBench, circular reasoning, pipeline simplification). The remaining issues are moderate rather than critical. To reach pass threshold: (1) **Sharpen CRAMF differentiation**: Explicitly acknowledge CRAMF's 'domain- and application-level signals' in contextual query augmentation and its stored module paths (θ_p), then argue precisely why this falls short of systematic subdomain conditioning — e.g., CRAMF's domain signals are used for disambiguating polysemous concepts, not for conditioning the retrieval ranking on the input's mathematical subdomain. (2) **Cite and differentiate from SITA (AAAI 2026)**: Acknowledge it as domain-specific autoformalization via structure-to-instance approach, but clarify your work conditions the general-purpose pipeline on subdomain identity, whereas SITA targets a specific mathematical pattern (abstract-to-concrete instantiation) in a single domain. (3) **Strengthen the impact argument**: Add an explicit ablation comparing 'naive domain prompting' (just prepending domain label to input, zero engineering) vs. full pipeline with domain-conditioned retrieval and error context. If the full pipeline doesn't significantly outperform naive domain prompting, the paper's contribution is weaker. Frame the error taxonomy as a co-equal contribution, not a byproduct. (4) **Fix FineLeanCorpus size**: Use '286k fully verified entries (509k total)' for accuracy. (5) **Add M2F and SITA to landscape discussion** as evidence that domain-specific approaches exist but are either single-domain (SITA, M2F) or manual (130k Topology), motivating your systematic multi-domain approach.

### Round 3 review
Verdict: revise
Issues: ["MODERATE: Several relevant ICLR 2026 systems missing from landscape — DRIFT (ICLR 2026 Poster) performs concept-level decomposition for targeted retrieval and nearly doubles F1 on ProofNet; its sub-query decomposition is conceptually related to domain-conditioned retrieval and must be differentiated. Aria (ICLR 2026) achieves 68.5% on ProofNet and 42.9% on homological conjectures (all other baselines 0%) but is domain-agnostic — these per-domain results directly support the proposal's domain bias motivation and should appear in the landscape analysis.", "MODERATE: ConNF benchmark (961 OOD informal-formal pairs, from DDR/ICLR 2025 Spotlight) specifically tests cross-domain generalization in autoformalization. The proposal claims to introduce 'the first leave-one-domain-out evaluation protocol for autoformalization' but does not cite ConNF. While ConNF tests a single OOD domain (New Foundations set theory) rather than systematic multi-domain rotation, the claim needs to be narrowed or ConNF explicitly differentiated.", "MODERATE: Impact argument remains the weakest link — the proposal correctly identifies the risk that naive domain prompting captures 80%+ of gains, but the framing still positions the multi-stage pipeline as the main system contribution. If the error taxonomy is the safety net, it should be promoted to unambiguous primary contribution with clearer standalone evaluation criteria (e.g., inter-domain error pattern correlation metrics, actionable recommendations per domain).", "MINOR: Compute budget slightly exceeds constraint — auto_research mode estimates 210 H100-hours vs. the user's hard ≤200 H100-hour cap. Need to either trim 10 hours (e.g., reduce ablation sweep scope) or justify the overage.", "MINOR: LeanSearch v2 (May 2026) achieves SOTA premise retrieval 'without domain-specific fine-tuning' — this is directly relevant since it suggests domain-agnostic retrieval can be very strong, potentially challenging the motivation for domain-conditioned retrieval. Should be cited and its implications discussed."]
Feedback: The proposal has matured significantly across three rounds and is close to passing. All Round 2 issues were addressed well, particularly the CRAMF differentiation (now technically precise and verified accurate). To reach pass threshold: (1) **Add DRIFT, ConNF, LeanSearch v2, and Aria's per-domain results** to the landscape — DRIFT and LeanSearch v2 are recent strong retrieval baselines; ConNF is the existing OOD autoformalization benchmark; Aria's per-domain gaps (42.9% on homological conjectures vs. 0% for all baselines) directly support the domain bias motivation. (2) **Narrow the 'first leave-one-domain-out' claim** — ConNF already tests OOD generalization, so specify 'first systematic multi-domain rotation evaluation' across ≥4 mathematical subdomain categories. (3) **Elevate the error taxonomy to unambiguous primary contribution** — define standalone evaluation criteria: (a) inter-domain error pattern clustering metrics (e.g., how distinct are topology vs. algebra error distributions?), (b) predictive power of domain-specific error patterns (can the taxonomy predict which errors a new formalization will encounter?), (c) actionable recommendations per domain. This makes the paper valuable even if the downstream delta is modest. (4) **Trim 10 H100-hours** from the auto_research estimate to fit within the ≤200 constraint. (5) **Discuss LeanSearch v2's domain-agnostic SOTA** — if domain-agnostic retrieval is already very strong, what specifically does domain conditioning add beyond what scale/engineering can achieve?

### Round 4 review
Verdict: revise
Issues: ["MODERATE: IndiMathBench (ICLR 2026, arXiv 2512.00997) not cited — uses category-specific static Mathlib context for 4 mathematical domains (Geometry, Algebra, Number Theory, Set Theory & Combinatorics) to condition autoformalization prompts. While IndiMathBench uses static context blocks (not dynamic retrieval conditioning) and does not claim novelty in domain awareness, it IS a form of domain-conditioned autoformalization. The proposal's claim of being 'the first autoformalization pipeline that conditions on inferred mathematical subdomain' must acknowledge and differentiate from IndiMathBench. IndiMathBench's approach is essentially the 'naive domain prompting' ablation the proposal already plans — this connection should be made explicit.", "MODERATE: Impact argument remains below the 4.0 threshold — IndiMathBench achieves 95.3% syntactic validity with simple category-specific static context, suggesting that even rudimentary domain awareness is powerful. This strengthens the proposal's motivation (domain information helps) but weakens the pipeline contribution (maybe simple approaches suffice). The error taxonomy needs to be framed even more forcefully as the primary contribution — with quantitative hypotheses about expected inter-domain JSD values and prediction accuracy thresholds that would constitute a meaningful finding.", "MINOR: Goedel-Formalizer-V2-8B is fine-tuned from Qwen3-8B, not Qwen2.5. The user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' — using the Formalizer variant is reasonable (same family, specialized for formalization) but should be explicitly justified since the base architecture differs from user's Qwen2.5 specification."]
Feedback: The proposal is very close to passing (avg 3.875/5.0) after 4 strong revision rounds. Two targeted fixes should clear the threshold: (1) **Cite IndiMathBench and make it your 'naive domain prompting' reference implementation**: IndiMathBench's category-specific static context is essentially the simple baseline your ablation (e) already plans. Explicitly map your ablation to IndiMathBench's approach: 'Our naive domain prompting baseline (ablation e) replicates IndiMathBench's category-specific context approach; our full pipeline adds dynamic domain-conditioned retrieval reranking and error-taxonomy-driven prompting on top.' This transforms a missing reference into a strengthened experimental design. Narrow the novelty claim to: 'first system to condition dynamic retrieval ranking on inferred mathematical subdomain and provide systematic domain-specific error characterization.' (2) **Set quantitative success criteria for the error taxonomy to strengthen impact**: State concrete hypotheses — e.g., 'We hypothesize JSD between topology and algebra error distributions exceeds 0.3 (vs. <0.1 for random domain assignments)' and 'domain-specific error prediction accuracy exceeds 70% on held-out formalizations.' This transforms the error taxonomy from 'we'll analyze and see what we find' into a testable scientific claim that reviewers can evaluate. If these hypotheses hold, the paper has clear value regardless of pipeline delta.

### Round 5 review
Verdict: revise
Issues: ["MODERATE: IndiMathBench was DESK REJECTED at ICLR 2026 — cited as 'ICLR 2026' throughout the proposal (core_problem, opportunity, landscape, approach, description), falsely implying acceptance. Must be cited as 'arXiv 2512.00997' or 'IndiMathBench (Biyani et al., 2025)'. A desk-rejected paper's experimental claims carry less weight than peer-reviewed results, and reviewers who know its status will question the proposal's due diligence.", "MINOR: IndiMathBench Claude Opus 4 BEq is 17.3% (54/312 problems), not '~21.5%' as claimed in multiple sections. The 21.5% figure does not correspond to any metric in the paper. This numerical error appears in core_problem, opportunity, and description — undermining trust in the proposal's data verification.", "MINOR: ICML 2026 AI4Math Workshop (Jul 11, 2026) features ShadowBench — 126 problems across 8 mathematical areas with domain-tiered evaluation and Semantic Alignment metrics. This workshop challenge directly overlaps with the proposal's domain-stratified evaluation contribution and should be cited. Concurrent community interest in domain-stratified autoformalization evaluation both validates the proposal's direction and signals competition.", "MINOR: 'Towards a Common Framework for Autoformalization' (AAAI 2026) discusses cross-domain autoformalization challenges and the need for methods that 'transfer reasoning patterns and formalization strategies across different areas' — tangentially relevant and should be acknowledged, though it focuses on cross-formalism domains (math vs. planning vs. logic) rather than mathematical subdomain adaptation."]
Feedback: The proposal is very close to the pass threshold (avg 3.75/5.0) after 5 strong revision rounds. Two targeted fixes should clear 4.0: (1) **Fix IndiMathBench citation**: Change 'ICLR 2026' to 'arXiv 2512.00997' or 'IndiMathBench (Biyani et al., 2025, desk-rejected ICLR 2026 submission)' throughout. The paper's results remain usable as empirical evidence, but its desk-rejection status means reviewers will scrutinize claims derived from it more carefully — consider reducing reliance on IndiMathBench-specific numbers and strengthening the argument with peer-reviewed evidence (MSC-180, FormalMATH, Aria's homological results are all stronger references). Fix the BEq number to 17.3% (54/312). (2) **Cite and position relative to ICML 2026 ShadowBench**: The AI4Math Workshop's ShadowBench evaluates autoformalization across 8 mathematical areas with SA metrics — this validates community interest in domain-stratified evaluation but also means you're not the only ones thinking about it. Cite it and argue your evaluation protocol (leave-one-domain-out rotation across 5+ categories with systematic ablations) is more rigorous than ShadowBench's fixed-split evaluation. (3) **Consider condensing the landscape section** — at its current length, it reads like a survey rather than a research proposal. The core contribution can be stated in 1/3 the space.

### Round 6 review
Verdict: revise
Issues: ["MODERATE: Missing reference — Cycle Consistency Fine-tuning (arXiv:2603.24372, Shebzukhov, March 2026) provides domain-stratified autoformalization results using FineLeanCorpus domain labels, showing number theory at 0.722 cycle consistency vs. calculus at 0.516. While it performs only post-hoc observational analysis (no domain conditioning), it partially pre-empts claims of providing 'the first empirical characterization of how autoformalization errors distribute across mathematical subdomains.' The proposal's novelty claim must be narrowed to 'first domain-specific error TAXONOMY characterizing error TYPES by subdomain' (not just aggregate performance by domain).", "MINOR: ShadowBench/SCI Error Taxonomy conflation — the proposal repeatedly states 'ShadowBench challenge (126 problems across 8 mathematical areas with Semantic Alignment metrics and a 28-category SCI Error Taxonomy)' but the 28-category SCI Error Taxonomy belongs to Track 1 (FormalRx challenge), not Track 4 (ShadowBench). These are separate challenge tracks within the same ICML 2026 AI4Math Workshop. The conflation appears in core_problem, approach, and description.", "MINOR: Herald module path claim overstated — the proposal states Herald provides '580k NL-formal pairs tagged with Mathlib4 module paths enabling automatic formalization-level domain labeling' but the released HuggingFace dataset (FrenzyMath/Herald_statements) contains only id, informal_statement, and formal_statement fields with no explicit module path column. Domain info must be parsed from qualified theorem names embedded in formal statements or recovered via re-running the Lean-Jixia extraction pipeline. This is feasible but adds unacknowledged engineering effort."]
Feedback: The proposal is very close to passing (avg 3.5/5.0 → needs 4.0). Three targeted fixes for Round 7: (1) **Cite the cycle consistency paper (arXiv:2603.24372)** and narrow the novelty claim: this paper already shows autoformalization performance varies by domain (number theory > calculus), so you cannot claim to be 'the first to show domain variation exists.' Narrow to: 'first systematic domain-specific error TAXONOMY that characterizes how autoformalization failure TYPES (not just aggregate accuracy) distribute across subdomains — going beyond the observational domain-stratified scores in Shebzukhov (2026) to classify error categories (typeclass failures, coercion mismatches, tactic incompatibilities) per subdomain with statistical rigor.' (2) **Fix the ShadowBench/SCI conflation**: Separate the two tracks — ShadowBench (Track 4) uses Semantic Alignment metrics for end-to-end autoformalization; the SCI Error Taxonomy (28 categories) belongs to Track 1 (FormalRx) for semantic alignment evaluation. Both are relevant but distinct. Your error taxonomy complements the SCI taxonomy (which categorizes by error type alone) by adding subdomain stratification. (3) **Acknowledge Herald data engineering**: Note that Herald's module paths must be parsed from qualified names in formal statements (e.g., extracting 'Topology.Basic' from 'Topology.Basic.isOpen_compl') rather than read from a dedicated field, and account for this in the timeline (~1 additional week). Alternatively, note that APRIL's HuggingFace dataset includes an explicit 'path' field that directly encodes Mathlib module paths, making it the more immediately usable source for domain labeling.

### Round 7 review
Verdict: revise
Issues: ["MINOR: LeanPremise/LeanHammer (ICLR 2026, arXiv 2506.07477) not cited — the first end-to-end domain-general hammer for Lean with dynamic user-context adaptation and strong out-of-distribution generalization (79.4% relative to upper bound on miniCTX-v2). While targeting premise selection for proving (not autoformalization retrieval) and not conditioning on mathematical subdomain per se, it demonstrates a relevant domain-generalization approach in the Lean ecosystem that should be acknowledged in the landscape.", "MINOR: AAAI 2027 (July 28, 2026) is listed as a target venue but is mathematically infeasible — 8 weeks from today vs. minimum 11-week auto_research timeline. Should be downgraded from 'STRETCH' to explicitly infeasible, or the timeline should explain what partial submission (e.g., error taxonomy only) could be ready in 8 weeks.", "MINOR: ICML 2026 AI4Math Workshop paper submission deadline was May 25, 2026 (already passed 3 days ago). The target_venues entry correctly identifies challenge track participation (June 15 deadline) but should note that paper submission is no longer possible.", "MINOR: The APRIL dataset's HuggingFace schema includes an 'error_type' field already classifying errors into categories (theorem substitution, tactic errors, multi-line errors, line mutations). The proposal's 'domain-specific error taxonomy' contribution is more precisely a domain-stratified cross-tabulation of APRIL's existing error types — this should be stated explicitly to avoid overclaiming. The novelty is in the domain stratification and statistical analysis (JSD, predictive power), not in constructing a new error classification.", "MINOR: KELPS (arXiv 2507.08665) achieves 88.9% syntactic accuracy on MiniF2F via Knowledge Equations and multi-language autoformalization — a strong baseline not currently cited that outperforms several referenced systems."]
Feedback: The proposal has matured substantially across 6 revision rounds and all critical/moderate issues are resolved. Remaining issues are all minor. To clear the 4.0 threshold: (1) **Acknowledge APRIL's existing error_type field** and precisely describe the taxonomy contribution as domain-stratified cross-tabulation with statistical rigor (JSD, prediction), not a new error classification — this prevents overclaiming while preserving the genuine novelty of domain stratification. (2) **Fix venue timeline accuracy**: mark AAAI 2027 as infeasible (not 'stretch'), note ICML 2026 paper deadline has passed, and specify what partial submission could target AAAI 2027 if desired (e.g., error taxonomy + initial retrieval results without full ablations). (3) **Add LeanPremise/LeanHammer** to landscape as a strong domain-general retrieval baseline in the Lean ecosystem, differentiating by target task (premise selection for proving vs. retrieval for autoformalization). (4) **Consider adding KELPS** as a strong MiniF2F baseline. These four fixes are all straightforward and should be completable in one revision round.


## Output format
Output ONLY a JSON object:
{
  "verdict": "pass | revise | fail",
  "scores": {
    "novelty": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "feasibility": {"score": 0-5, "rationale": "..."},
    "clarity": {"score": 0-5, "rationale": "..."},
    "impact": {"score": 0-5, "rationale": "..."}
  },
  "issues": ["specific issue 1", ...],
  "feedback": "Actionable feedback (if verdict=revise)",
  "reason": "One-line summary of verdict rationale"
}

Rules:
- "pass": sound AND high quality — avg score >= 4.0, no critical issues
- "revise": fixable issues OR scores below threshold
- "fail": fundamental flaw (gap doesn't exist, approach provably wrong)
- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.
- Round 10 only: if still "revise", you MUST choose "pass" or "fail".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "175a5d07-34ca-4dba-98f1-79759dfe6f2e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T14:45:58.639Z_

```json
{
  "parentUuid": "175a5d07-34ca-4dba-98f1-79759dfe6f2e",
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
  "uuid": "87918256-c083-4068-8445-de2944a6b3e5",
  "timestamp": "2026-05-28T14:45:58.639Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T14:45:58.639Z_

```json
{
  "parentUuid": "87918256-c083-4068-8445-de2944a6b3e5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "445759dc-5209-48bd-bca9-3323d307e91b",
  "timestamp": "2026-05-28T14:45:58.639Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "445759dc-5209-48bd-bca9-3323d307e91b",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Assistant

_source line 8 · 2026-05-28T14:46:05.994Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 8 of 10 for reviewing this domain-adaptive autoformalization idea. Let me carefully verify the claims and check if the round 7 issues have been properly addressed. I need to do thorough web searches to independently verify the claims.

Let me structure my review around:
1. Verifying that round 7 issues were addressed
2. Checking for any new missing references or concurrent work
3. Evaluating the overall quality

Let me start by searching for the key claims and references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "445759dc-5209-48bd-bca9-3323d307e91b",
  "isSidechain": false,
  "requestId": "req_011CbV9XK7XuJrsXzED6iJZp",
  "type": "assistant",
  "uuid": "92aa6521-dfdc-44bc-84aa-076bd6a0daee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3QfnisXSy5swGZUy6hcRA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22770,
      "cache_read_input_tokens": 11014,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 423,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22770
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

_source line 9 · 2026-05-28T14:46:07.518Z_

I'll conduct a thorough independent review of this proposal, verifying claims and checking for any remaining issues or new concurrent work. Let me launch multiple search agents in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92aa6521-dfdc-44bc-84aa-076bd6a0daee",
  "isSidechain": false,
  "requestId": "req_011CbV9XK7XuJrsXzED6iJZp",
  "type": "assistant",
  "uuid": "7a868f76-7a60-4165-953f-4c619c62bb46",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3QfnisXSy5swGZUy6hcRA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22770,
      "cache_read_input_tokens": 11014,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 423,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22770
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

_source line 10 · 2026-05-28T14:46:12.774Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RD1de9vvm1nHV5MYyHh6jK`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Verify APRIL error_type field",
  "prompt": "Search the web for information about the APRIL dataset for Lean proof repair (arXiv 2602.02990). I need to verify:\n1. Does the APRIL HuggingFace dataset include an 'error_type' field with categories like lme, mlme, thme, tme?\n2. Does it include a 'path' field with Mathlib module paths?\n3. Does it include a raw 'error' field with Lean compiler messages?\n4. Has anyone already done domain-stratified analysis of APRIL's error types?\n\nSearch for \"APRIL lean proof repair 260k\" and \"APRIL dataset error_type field lean\" and check the HuggingFace dataset page if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a868f76-7a60-4165-953f-4c619c62bb46",
  "isSidechain": false,
  "requestId": "req_011CbV9XK7XuJrsXzED6iJZp",
  "type": "assistant",
  "uuid": "cde54045-e95b-4f72-85b8-fe80b6184ef3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3QfnisXSy5swGZUy6hcRA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22770,
      "cache_read_input_tokens": 11014,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 423,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 22770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22770
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

_source line 11 · 2026-05-28T14:47:55.805Z_

<details><summary>↩ Tool result · `toolu_01RD1de9vvm1nHV5MYyHh6jK`</summary>

```text
## Summary of Findings

Based on my web search, here's what I found regarding your questions about the APRIL dataset for Lean proof repair:

### 1. **Error Type Field with Categories (lme, mlme, thme, tme)**

**YES - Confirmed.** The APRIL dataset does include error type categorization through distinct training split files:
- **LME (Line Mutation Error)**: Single proof line is redacted and replaced with a placeholder, then completed by LLM
- **MLME (Multi-Line Mutation Error)**: Multiple consecutive lines (up to half the proof) are redacted and completed by LLM
- **TME (Tactic Mutation Error)**: Correct tactic substituted with syntactically similar but semantically incorrect one
- **THME (Theorem Mutation Error)**: Theorem substitution (exact details not fully specified in search results)

These are organized in the dataset as separate training files: `lme_train.jsonl`, `mlme_train.jsonl`, `tme_train.jsonl`, `thme_train.jsonl`

### 2. **Path Field with Mathlib Module Paths**

**Partially confirmed but needs verification.** While my search results confirm the dataset is based on Mathlib code and includes module information, I could not find explicit confirmation that a dedicated 'path' field exists with module paths in the public documentation.

### 3. **Raw Error Field with Lean Compiler Messages**

**Partially confirmed.** The paper and documentation describe that the dataset includes:
- "Compiler feedback" 
- "Compiler diagnostics"
- "Error messages"
- "Error lines"
- "Goal states"

However, I couldn't find definitive confirmation of a field named specifically 'error' with raw Lean compiler messages in the publicly available documentation.

### 4. **Domain-Stratified Analysis of Error Types**

**Not found.** My searches did not reveal any papers or analyses that specifically perform domain-stratified analysis of APRIL's error types by Mathlib module or domain.

### Recommendation

To verify the exact field names (error_type, path, error) and their exact structure, you should:
1. **Check the Hugging Face dataset page** at [https://huggingface.co/datasets/uw-math-ai/APRIL](https://huggingface.co/datasets/uw-math-ai/APRIL) (though this was returning HTTP 401 in my fetch)
2. **Review the full arXiv PDF** at [https://arxiv.org/pdf/2602.02990](https://arxiv.org/pdf/2602.02990) for appendices with schema details
3. **Check the GitHub repository** at [https://github.com/uw-math-ai/lean-error-correction](https://github.com/uw-math-ai/lean-error-correction) for dataset loading code or detailed schema documentation

Sources:
- [Learning to Repair Lean Proofs from Compiler Feedback (arXiv:2602.02990)](https://arxiv.org/abs/2602.02990)
- [uw-math-ai/APRIL Dataset on Hugging Face](https://huggingface.co/datasets/uw-math-ai/APRIL)
- [GitHub - uw-math-ai/lean-error-correction](https://github.com/uw-math-ai/lean-error-correction)
- [Literature Review: Learning to Repair Lean Proofs](https://www.themoonlight.io/en/review/learning-to-repair-lean-proofs-from-compiler-feedback)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cde54045-e95b-4f72-85b8-fe80b6184ef3",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "85a47525-f9ee-4921-a388-2e8a8c436ab3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for information about the APRIL dataset for Lean proof repair (arXiv 2602.02990). I need to verify:\n1. Does the APRIL HuggingFace dataset include an 'error_type' field with categories like lme, mlme, thme, tme?\n2. Does it include a 'path' field with Mathlib module paths?\n3. Does it include a raw 'error' field with Lean compiler messages?\n4. Has anyone already done domain-stratified analysis of APRIL's error types?\n\nSearch for \"APRIL lean proof repair 260k\" and \"APRIL dataset error_type field lean\" and check the HuggingFace dataset page if possible.",
    "agentId": "af5adb96bd8b4e31a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Findings\n\nBased on my web search, here's what I found regarding your questions about the APRIL dataset for Lean proof repair:\n\n### 1. **Error Type Field with Categories (lme, mlme, thme, tme)**\n\n**YES - Confirmed.** The APRIL dataset does include error type categorization through distinct training split files:\n- **LME (Line Mutation Error)**: Single proof line is redacted and replaced with a placeholder, then completed by LLM\n- **MLME (Multi-Line Mutation Error)**: Multiple consecutive lines (up to half the proof) are redacted and completed by LLM\n- **TME (Tactic Mutation Error)**: Correct tactic substituted with syntactically similar but semantically incorrect one\n- **THME (Theorem Mutation Error)**: Theorem substitution (exact details not fully specified in search results)\n\nThese are organized in the dataset as separate training files: `lme_train.jsonl`, `mlme_train.jsonl`, `tme_train.jsonl`, `thme_train.jsonl`\n\n### 2. **Path Field with Mathlib Module Paths**\n\n**Partially confirmed but needs verification.** While my search results confirm the dataset is based on Mathlib code and includes module information, I could not find explicit confirmation that a dedicated 'path' field exists with module paths in the public documentation.\n\n### 3. **Raw Error Field with Lean Compiler Messages**\n\n**Partially confirmed.** The paper and documentation describe that the dataset includes:\n- \"Compiler feedback\" \n- \"Compiler diagnostics\"\n- \"Error messages\"\n- \"Error lines\"\n- \"Goal states\"\n\nHowever, I couldn't find definitive confirmation of a field named specifically 'error' with raw Lean compiler messages in the publicly available documentation.\n\n### 4. **Domain-Stratified Analysis of Error Types**\n\n**Not found.** My searches did not reveal any papers or analyses that specifically perform domain-stratified analysis of APRIL's error types by Mathlib module or domain.\n\n### Recommendation\n\nTo verify the exact field names (error_type, path, error) and their exact structure, you should:\n1. **Check the Hugging Face dataset page** at [https://huggingface.co/datasets/uw-math-ai/APRIL](https://huggingface.co/datasets/uw-math-ai/APRIL) (though this was returning HTTP 401 in my fetch)\n2. **Review the full arXiv PDF** at [https://arxiv.org/pdf/2602.02990](https://arxiv.org/pdf/2602.02990) for appendices with schema details\n3. **Check the GitHub repository** at [https://github.com/uw-math-ai/lean-error-correction](https://github.com/uw-math-ai/lean-error-correction) for dataset loading code or detailed schema documentation\n\nSources:\n- [Learning to Repair Lean Proofs from Compiler Feedback (arXiv:2602.02990)](https://arxiv.org/abs/2602.02990)\n- [uw-math-ai/APRIL Dataset on Hugging Face](https://huggingface.co/datasets/uw-math-ai/APRIL)\n- [GitHub - uw-math-ai/lean-error-correction](https://github.com/uw-math-ai/lean-error-correction)\n- [Literature Review: Learning to Repair Lean Proofs](https://www.themoonlight.io/en/review/learning-to-repair-lean-proofs-from-compiler-feedback)"
      }
    ],
    "totalDurationMs": 103024,
    "totalTokens": 30235,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 555,
      "cache_creation_input_tokens": 1397,
      "cache_read_input_tokens": 27436,
      "output_tokens": 847,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1397
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 555,
          "output_tokens": 847,
          "cache_read_input_tokens": 27436,
          "cache_creation_input_tokens": 1397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1397,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "cde54045-e95b-4f72-85b8-fe80b6184ef3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T14:48:04.683Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013X6KfdP3VB1LRLS2jfuVZa`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify LeanPremise/LeanHammer ICLR 2026",
  "prompt": "I need to verify the following claims about LeanPremise/LeanHammer (arXiv 2506.07477):\n1. Is it accepted at ICLR 2026?\n2. Does it achieve 79.4% relative proof rate on OOD benchmarks (miniCTX-v2)?\n3. Does it show project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%?\n4. Is it described as \"first end-to-end domain-general hammer for Lean\"?\n5. Does it use an 82M-parameter neural premise selector?\n\nPlease search for:\n- \"LeanPremise LeanHammer\" OR \"arXiv 2506.07477\"\n- \"premise selection lean hammer ICLR 2026\"\n- Try to fetch the arxiv page at https://arxiv.org/abs/2506.07477\n\nReport what you find, including any discrepancies with the claims above."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85a47525-f9ee-4921-a388-2e8a8c436ab3",
  "isSidechain": false,
  "requestId": "req_011CbV9fwuL6YUXuTXPNUjGz",
  "type": "assistant",
  "uuid": "c6a70819-c3c2-4f60-88c0-2fa45a575e2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DjUbUZVgPpZaDjeKF4YR1V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1279,
      "cache_read_input_tokens": 33784,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 33784,
          "cache_creation_input_tokens": 1279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1279
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

_source line 13 · 2026-05-28T14:49:37.769Z_

<details><summary>↩ Tool result · `toolu_013X6KfdP3VB1LRLS2jfuVZa`</summary>

```text
I now have all the information needed to provide a thorough verification. Here is my report:

---

## Verification of Claims about LeanPremise/LeanHammer (arXiv 2506.07477)

### Paper Basics
- **Title:** "Premise Selection for a Lean Hammer"
- **Authors:** Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Q. Jiang, Sean Welleck
- **arXiv:** 2506.07477 (v1: June 9, 2025; v2: February 25, 2026)

---

### Claim 1: "Accepted at ICLR 2026"
**CONFIRMED.** The OpenReview page ([link](https://openreview.net/forum?id=m04JJNeRK6)) shows the paper was accepted as an **ICLR 2026 Oral** presentation. The search results also surfaced a direct link titled "Published as a conference paper at ICLR 2026."

---

### Claim 2: "79.4% relative proof rate on OOD benchmarks (miniCTX-v2)"
**CONFIRMED, but requires careful interpretation.** The paper states: "the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and **79.4% on miniCTX** with the full pipeline." This 79.4% is a **relative** proof rate -- it is the ratio of theorems proven by LeanHammer to theorems proven with oracle/ground-truth premises. The **absolute** proof rate on miniCTX-v2 is 20.7% (vs. 26.1% ground truth). So the claim is accurate as stated ("relative proof rate").

---

### Claim 3: "Project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%"
**CONFIRMED.** The miniCTX-v2 project-level breakdown (full setting, large model) is:
- **Carleson: 0.0%**
- **ConNF: 16.0%**
- **FLT: 36.4%**
- **Foundation: 38.0%**
- HepLean: 10.0%
- Seymour: 24.0%
- Average: 20.7%

All four claimed numbers match exactly.

---

### Claim 4: "First end-to-end domain-general hammer for Lean"
**CONFIRMED.** The paper explicitly describes LeanHammer as "the first end-to-end domain-general hammer for Lean" (or equivalently, "the first end-to-end domain general hammer for the Lean proof assistant").

---

### Claim 5: "82M-parameter neural premise selector"
**CONFIRMED.** The paper tests three model sizes: Small (23M), Medium (33M), and **Large (82M)** parameters. The flagship results use the 82M large model.

---

### Summary

All five claims are **verified as accurate** based on the paper content. No discrepancies were found. The only nuance worth noting is that the 79.4% figure is explicitly a *relative* proof rate (ratio to ground-truth performance), not an absolute proof rate -- and the claim as stated correctly uses the word "relative," so it is faithful to the paper.

Sources:
- [arXiv page: 2506.07477](https://arxiv.org/abs/2506.07477)
- [Full HTML paper (v1)](https://arxiv.org/html/2506.07477v1)
- [OpenReview forum](https://openreview.net/forum?id=m04JJNeRK6)
- [OpenReview PDF](https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf)
- [LeanHammer project page](https://cmu-l3.github.io/lean-hammer/)

agentId: aa85e714bc0c4243e (use SendMessage with to: 'aa85e714bc0c4243e' to continue this agent)
&lt;usage>total_tokens: 15473
tool_uses: 8
duration_ms: 93082&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6a70819-c3c2-4f60-88c0-2fa45a575e2c",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "b21e46da-8ad7-4128-9575-e01b83938987",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the following claims about LeanPremise/LeanHammer (arXiv 2506.07477):\n1. Is it accepted at ICLR 2026?\n2. Does it achieve 79.4% relative proof rate on OOD benchmarks (miniCTX-v2)?\n3. Does it show project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%?\n4. Is it described as \"first end-to-end domain-general hammer for Lean\"?\n5. Does it use an 82M-parameter neural premise selector?\n\nPlease search for:\n- \"LeanPremise LeanHammer\" OR \"arXiv 2506.07477\"\n- \"premise selection lean hammer ICLR 2026\"\n- Try to fetch the arxiv page at https://arxiv.org/abs/2506.07477\n\nReport what you find, including any discrepancies with the claims above.",
    "agentId": "aa85e714bc0c4243e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed to provide a thorough verification. Here is my report:\n\n---\n\n## Verification of Claims about LeanPremise/LeanHammer (arXiv 2506.07477)\n\n### Paper Basics\n- **Title:** \"Premise Selection for a Lean Hammer\"\n- **Authors:** Thomas Zhu, Joshua Clune, Jeremy Avigad, Albert Q. Jiang, Sean Welleck\n- **arXiv:** 2506.07477 (v1: June 9, 2025; v2: February 25, 2026)\n\n---\n\n### Claim 1: \"Accepted at ICLR 2026\"\n**CONFIRMED.** The OpenReview page ([link](https://openreview.net/forum?id=m04JJNeRK6)) shows the paper was accepted as an **ICLR 2026 Oral** presentation. The search results also surfaced a direct link titled \"Published as a conference paper at ICLR 2026.\"\n\n---\n\n### Claim 2: \"79.4% relative proof rate on OOD benchmarks (miniCTX-v2)\"\n**CONFIRMED, but requires careful interpretation.** The paper states: \"the proportion of theorems proven by LeanHammer with the large selector, out of theorems proven with the ground-truth premises (i.e. the best-case scenario), is 73.5% on Mathlib and **79.4% on miniCTX** with the full pipeline.\" This 79.4% is a **relative** proof rate -- it is the ratio of theorems proven by LeanHammer to theorems proven with oracle/ground-truth premises. The **absolute** proof rate on miniCTX-v2 is 20.7% (vs. 26.1% ground truth). So the claim is accurate as stated (\"relative proof rate\").\n\n---\n\n### Claim 3: \"Project-level variation: Carleson 0%, Foundation 38%, ConNF 16%, FLT 36.4%\"\n**CONFIRMED.** The miniCTX-v2 project-level breakdown (full setting, large model) is:\n- **Carleson: 0.0%**\n- **ConNF: 16.0%**\n- **FLT: 36.4%**\n- **Foundation: 38.0%**\n- HepLean: 10.0%\n- Seymour: 24.0%\n- Average: 20.7%\n\nAll four claimed numbers match exactly.\n\n---\n\n### Claim 4: \"First end-to-end domain-general hammer for Lean\"\n**CONFIRMED.** The paper explicitly describes LeanHammer as \"the first end-to-end domain-general hammer for Lean\" (or equivalently, \"the first end-to-end domain general hammer for the Lean proof assistant\").\n\n---\n\n### Claim 5: \"82M-parameter neural premise selector\"\n**CONFIRMED.** The paper tests three model sizes: Small (23M), Medium (33M), and **Large (82M)** parameters. The flagship results use the 82M large model.\n\n---\n\n### Summary\n\nAll five claims are **verified as accurate** based on the paper content. No discrepancies were found. The only nuance worth noting is that the 79.4% figure is explicitly a *relative* proof rate (ratio to ground-truth performance), not an absolute proof rate -- and the claim as stated correctly uses the word \"relative,\" so it is faithful to the paper.\n\nSources:\n- [arXiv page: 2506.07477](https://arxiv.org/abs/2506.07477)\n- [Full HTML paper (v1)](https://arxiv.org/html/2506.07477v1)\n- [OpenReview forum](https://openreview.net/forum?id=m04JJNeRK6)\n- [OpenReview PDF](https://openreview.net/pdf/0d32353ccfa85cbf700389ec2d98a2c40fa4b640.pdf)\n- [LeanHammer project page](https://cmu-l3.github.io/lean-hammer/)"
      }
    ],
    "totalDurationMs": 93082,
    "totalTokens": 15473,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 13019,
      "output_tokens": 983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 983,
          "cache_read_input_tokens": 13019,
          "cache_creation_input_tokens": 1470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1470,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "c6a70819-c3c2-4f60-88c0-2fa45a575e2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-28T14:49:45.201Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CCpMK4ywUQzby884Ptnmvt`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify KELPS paper claims",
  "prompt": "I need to verify claims about KELPS (arXiv 2507.08665):\n1. Does it achieve 88.9% syntactic accuracy (pass@1) on MiniF2F?\n2. Is it published at ICML 2025 AI4Math Workshop?\n3. Does it use \"Knowledge Equations\" as intermediate representation?\n4. Does it support multi-language autoformalization (NL → KE → Lean/Coq/Isabelle)?\n5. Does it cover 60k+ NL-FL pairs across 6 math topics?\n\nPlease search for:\n- \"KELPS Knowledge Equations autoformalization\" \n- \"arXiv 2507.08665\"\n- Try to fetch https://arxiv.org/abs/2507.08665\n\nReport all findings and any discrepancies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b21e46da-8ad7-4128-9575-e01b83938987",
  "isSidechain": false,
  "requestId": "req_011CbV9oTpMkzqbUnvEwqBFP",
  "type": "assistant",
  "uuid": "2d0013af-e537-41c7-b6f4-629263ef8e6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TB9dGe6nqpa6hB8cig1G1c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 35063,
      "output_tokens": 288,
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
          "output_tokens": 288,
          "cache_read_input_tokens": 35063,
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

_source line 15 · 2026-05-28T14:50:48.534Z_

<details><summary>↩ Tool result · `toolu_01CCpMK4ywUQzby884Ptnmvt`</summary>

```text
Here is a comprehensive report on all five claims about KELPS (arXiv 2507.08665).

---

**Paper Confirmed:** "KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment" by Jiyao Zhang, Chengli Zhong, Hui Xu, Qige Li, and Yi Zhou. Submitted July 11, 2025.

---

**Claim 1: 88.9% syntactic accuracy (pass@1) on MiniF2F**
**VERIFIED.** The paper reports exactly 88.9% syntactic accuracy (pass@1) on MiniF2F. This was achieved using a DeepSeek-Math-7B-Base model fine-tuned on the KELPS dataset. It outperforms DeepSeek-V3 (671B parameters, 81%), Herald (7B, 81.3%), and LLaMA-3 (8B, 61.4%). Note this is *syntactic* accuracy (whether the output parses as valid formal code), not semantic/proof accuracy. The semantic score was 4.05 on a 0-5 scale.

**Claim 2: Published at ICML 2025 AI4Math Workshop**
**VERIFIED.** The paper's metadata on arXiv states it was "Accepted by the ICML 2025 AI4MATH Workshop." The paper header also references "Machine Learning, ICML."

**Claim 3: Uses "Knowledge Equations" as intermediate representation**
**VERIFIED.** Knowledge Equations (KEs) are the core methodological contribution. They are described as an intermediate formal representation grounded in assertional logic, serving as a bridge between natural language and target formal languages. KEs have three structural components: Declarations (variable type specifications), Facts (assertions of known information), and Queries (propositions requiring proof). The system defines systematic mapping rules from KE concepts/operators to target language constructs.

**Claim 4: Supports multi-language autoformalization (NL -> KE -> Lean/Coq/Isabelle)**
**VERIFIED.** The three-stage pipeline works as follows:
1. Natural language is parsed into Knowledge Equations (semantic parsing)
2. KEs are converted to Lean 4, Coq, and Isabelle via parallel transformation rules (syntactic alignment)
3. LLM-based semantic verification scores outputs on a 0-5 scale

Cross-language results are also reported: MiniF2F-Isabelle achieved 82.2% syntactic accuracy.

**Claim 5: Covers 60k+ NL-FL pairs across 6 math topics**
**VERIFIED.** The paper reports a parallel corpus of over 60,000 NL-FL pairs. The six mathematical topic domains are:
1. Numbers (Real, Integers, Natural Numbers)
2. Polynomials
3. Functions
4. Sets
5. Sequences
6. Special operators (ForAll, Exists, etc.)

The ontology spans 40 core concepts and 180 operators covering K-12 and undergraduate mathematics. The data pipeline started from ~100,000 Numina items, filtered to 70,000, then 50,000 after seven expert-iteration cycles, supplemented by synthetic data. The optimal training mix was a 1:1.5 ratio of real-to-synthetic data (~35k total).

---

**Discrepancies / Caveats:**
- No discrepancies were found. All five claims are consistent with the paper's content as published on arXiv.
- One nuance worth noting: the 88.9% figure is *syntactic* accuracy (whether the generated formal statement compiles/parses), not *semantic* correctness (whether the formalization faithfully captures the mathematical meaning). The semantic score is reported separately as 4.05/5.0.
- The paper is a workshop paper (ICML 2025 AI4Math Workshop), not a main conference paper. This is a meaningful distinction.

Sources:
- [KELPS on arXiv (abstract)](https://arxiv.org/abs/2507.08665)
- [KELPS on arXiv (HTML)](https://arxiv.org/html/2507.08665)
- [KELPS on ResearchGate](https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment)

agentId: ae11c89c8c8208713 (use SendMessage with to: 'ae11c89c8c8208713' to continue this agent)
&lt;usage>total_tokens: 14101
tool_uses: 5
duration_ms: 63327&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d0013af-e537-41c7-b6f4-629263ef8e6e",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "992e2404-8943-4e94-a14a-cd6c3ba65070",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify claims about KELPS (arXiv 2507.08665):\n1. Does it achieve 88.9% syntactic accuracy (pass@1) on MiniF2F?\n2. Is it published at ICML 2025 AI4Math Workshop?\n3. Does it use \"Knowledge Equations\" as intermediate representation?\n4. Does it support multi-language autoformalization (NL → KE → Lean/Coq/Isabelle)?\n5. Does it cover 60k+ NL-FL pairs across 6 math topics?\n\nPlease search for:\n- \"KELPS Knowledge Equations autoformalization\" \n- \"arXiv 2507.08665\"\n- Try to fetch https://arxiv.org/abs/2507.08665\n\nReport all findings and any discrepancies.",
    "agentId": "ae11c89c8c8208713",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report on all five claims about KELPS (arXiv 2507.08665).\n\n---\n\n**Paper Confirmed:** \"KELPS: A Framework for Verified Multi-Language Autoformalization via Semantic-Syntactic Alignment\" by Jiyao Zhang, Chengli Zhong, Hui Xu, Qige Li, and Yi Zhou. Submitted July 11, 2025.\n\n---\n\n**Claim 1: 88.9% syntactic accuracy (pass@1) on MiniF2F**\n**VERIFIED.** The paper reports exactly 88.9% syntactic accuracy (pass@1) on MiniF2F. This was achieved using a DeepSeek-Math-7B-Base model fine-tuned on the KELPS dataset. It outperforms DeepSeek-V3 (671B parameters, 81%), Herald (7B, 81.3%), and LLaMA-3 (8B, 61.4%). Note this is *syntactic* accuracy (whether the output parses as valid formal code), not semantic/proof accuracy. The semantic score was 4.05 on a 0-5 scale.\n\n**Claim 2: Published at ICML 2025 AI4Math Workshop**\n**VERIFIED.** The paper's metadata on arXiv states it was \"Accepted by the ICML 2025 AI4MATH Workshop.\" The paper header also references \"Machine Learning, ICML.\"\n\n**Claim 3: Uses \"Knowledge Equations\" as intermediate representation**\n**VERIFIED.** Knowledge Equations (KEs) are the core methodological contribution. They are described as an intermediate formal representation grounded in assertional logic, serving as a bridge between natural language and target formal languages. KEs have three structural components: Declarations (variable type specifications), Facts (assertions of known information), and Queries (propositions requiring proof). The system defines systematic mapping rules from KE concepts/operators to target language constructs.\n\n**Claim 4: Supports multi-language autoformalization (NL -> KE -> Lean/Coq/Isabelle)**\n**VERIFIED.** The three-stage pipeline works as follows:\n1. Natural language is parsed into Knowledge Equations (semantic parsing)\n2. KEs are converted to Lean 4, Coq, and Isabelle via parallel transformation rules (syntactic alignment)\n3. LLM-based semantic verification scores outputs on a 0-5 scale\n\nCross-language results are also reported: MiniF2F-Isabelle achieved 82.2% syntactic accuracy.\n\n**Claim 5: Covers 60k+ NL-FL pairs across 6 math topics**\n**VERIFIED.** The paper reports a parallel corpus of over 60,000 NL-FL pairs. The six mathematical topic domains are:\n1. Numbers (Real, Integers, Natural Numbers)\n2. Polynomials\n3. Functions\n4. Sets\n5. Sequences\n6. Special operators (ForAll, Exists, etc.)\n\nThe ontology spans 40 core concepts and 180 operators covering K-12 and undergraduate mathematics. The data pipeline started from ~100,000 Numina items, filtered to 70,000, then 50,000 after seven expert-iteration cycles, supplemented by synthetic data. The optimal training mix was a 1:1.5 ratio of real-to-synthetic data (~35k total).\n\n---\n\n**Discrepancies / Caveats:**\n- No discrepancies were found. All five claims are consistent with the paper's content as published on arXiv.\n- One nuance worth noting: the 88.9% figure is *syntactic* accuracy (whether the generated formal statement compiles/parses), not *semantic* correctness (whether the formalization faithfully captures the mathematical meaning). The semantic score is reported separately as 4.05/5.0.\n- The paper is a workshop paper (ICML 2025 AI4Math Workshop), not a main conference paper. This is a meaningful distinction.\n\nSources:\n- [KELPS on arXiv (abstract)](https://arxiv.org/abs/2507.08665)\n- [KELPS on arXiv (HTML)](https://arxiv.org/html/2507.08665)\n- [KELPS on ResearchGate](https://www.researchgate.net/publication/393656136_KELPS_A_Framework_for_Verified_Multi-Language_Autoformalization_via_Semantic-Syntactic_Alignment)"
      }
    ],
    "totalDurationMs": 63327,
    "totalTokens": 14101,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 11892,
      "output_tokens": 1055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1055,
          "cache_read_input_tokens": 11892,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1153,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "2d0013af-e537-41c7-b6f4-629263ef8e6e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "992e2404-8943-4e94-a14a-cd6c3ba65070",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Tool call

_source line 18 · 2026-05-28T14:50:57.188Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UfeDNeeG1q6JgyB1Tco5UG`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for new concurrent work May 2026",
  "prompt": "I'm reviewing a proposal about domain-adaptive autoformalization for mathematical theorem proving in Lean 4. I need to search for any NEW papers from March-May 2026 that might be concurrent work or that the proposal might have missed. Search specifically for:\n\n1. \"domain-adaptive autoformalization\" OR \"domain-specific autoformalization\" 2026\n2. \"autoformalization\" \"domain\" \"lean\" 2026 site:arxiv.org\n3. \"mathlib\" \"domain\" \"autoformalization\" 2026\n4. \"subdomain\" \"formalization\" \"lean\" 2026\n5. \"error taxonomy\" \"autoformalization\" 2026\n6. \"domain-conditioned retrieval\" \"theorem proving\" 2026\n7. Any new autoformalization papers from April-May 2026 on arxiv\n\nFocus on finding work that:\n- Conditions autoformalization on mathematical subdomain\n- Provides domain-stratified error analysis for formal math\n- Uses domain-aware retrieval for formalization\n- Any new benchmarks or datasets for domain-stratified autoformalization evaluation\n\nReport everything you find, especially anything that might pre-empt the proposal's novelty claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "992e2404-8943-4e94-a14a-cd6c3ba65070",
  "isSidechain": false,
  "requestId": "req_011CbV9tgP3VWMszYGEVLuHd",
  "type": "assistant",
  "uuid": "d39e96bf-38e0-496e-8334-385b18a8c6a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Arxeb4BrPKYT9cYTfHShgf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1420,
      "cache_read_input_tokens": 36462,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1420,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 36462,
          "cache_creation_input_tokens": 1420,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1420
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

_source line 19 · 2026-05-28T14:53:26.988Z_

<details><summary>↩ Tool result · `toolu_01UfeDNeeG1q6JgyB1Tco5UG`</summary>

```text
I now have a comprehensive picture. Here is my full report.

---

## Concurrent Work Report: Domain-Adaptive Autoformalization for Lean 4 (March--May 2026)

I searched extensively across seven query categories and multiple follow-up queries. Below are the findings organized by relevance to your proposal's core novelty claims.

---

### 1. HIGHEST RELEVANCE -- Papers that directly overlap with or threaten novelty claims

#### CRAMF: Concept-driven Retrieval-Augmented Mathematical Formalization (ICLR 2026)
- [arXiv:2508.06931](https://arxiv.org/abs/2508.06931) / [OpenReview](https://openreview.net/forum?id=09lmwhDqZ3)
- **Published at ICLR 2026 (main conference).**
- Builds a concept-definition knowledge base from Mathlib4 (26,000+ formal definitions, 1,000+ core concepts). Proposes **contextual query augmentation with domain- and application-level signals** to resolve conceptual polymorphism. Uses a dual-channel hybrid retrieval strategy with reranking.
- **Threat to novelty:** This directly addresses domain-aware retrieval for autoformalization. If the proposal claims domain-conditioned retrieval as novel, CRAMF is strong prior/concurrent work that must be cited and differentiated from. CRAMF achieves up to 62.1% relative improvement on miniF2F, ProofNet, and an AdvancedMath benchmark.

#### MathAtlas: A Benchmark for Autoformalization in the Wild (May 2026)
- [arXiv:2605.14061](https://arxiv.org/abs/2605.14061)
- First large-scale benchmark of graduate-level math autoformalization: ~52k entities from 103 textbooks, spanning **87 areas of mathematics** (real analysis, differential geometry, category theory, topology, quantum groups, etc.). Includes a dependency graph with ~178k relations.
- **Threat to novelty:** If the proposal claims to introduce domain-stratified evaluation for autoformalization, MathAtlas already provides a benchmark organized across 87 mathematical subfields with dependency-aware structure. Strong baselines achieve only 9.8% on theorems and 16.7% on definitions, demonstrating domain-stratified difficulty variation.

#### "Do LLMs Game Formalization?" (VerifAI-2 Workshop, ICLR 2026, April 2026)
- [arXiv:2604.19459](https://arxiv.org/abs/2604.19459)
- Introduces an **error taxonomy for formalization faithfulness** with categories: CONCLUSION AS AXIOM, FABRICATED CONTRADICTION, FABRICATED WORLD KNOWLEDGE, FABRICATED INVENTED, plus mistranslation and omission categories.
- **Threat to novelty:** If the proposal claims a novel error taxonomy for autoformalization, this paper provides a structured taxonomy specifically for formalization faithfulness errors. The taxonomy is applied to GPT-5 and DeepSeek-R1, revealing distinct failure modes.

---

### 2. HIGH RELEVANCE -- Papers that partially overlap

#### DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)
- [arXiv:2510.10815](https://arxiv.org/abs/2510.10815) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010321)
- Decomposes informal statements into sub-queries, performs **targeted premise retrieval from Mathlib**, and retrieves illustrative theorems to guide formalization. Nearly doubles F1 score vs. DPR baseline on ProofNet.
- **Relevance:** Overlaps with any domain-aware retrieval-for-formalization claims, though DRIFT's decomposition is statement-level rather than domain-level.

#### Aria: Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)
- [arXiv:2510.04520](https://arxiv.org/abs/2510.04520) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010860)
- Uses a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and constructing formalizations from grounded concepts. AriaScorer retrieves definitions from Mathlib for term-level grounding. Achieves 91.6% compilation and 68.5% accuracy on ProofNet.
- **Relevance:** Dependency-graph-based retrieval for autoformalization is closely related to domain-aware retrieval approaches.

#### ProofBridge: Auto-Formalization of NL Proofs in Lean via Joint Embeddings (ICLR 2026 main track)
- [arXiv:2510.15681](https://arxiv.org/abs/2510.15681)
- Joint embedding model aligning NL and FL theorem-proof pairs; cross-modal retrieval of semantically relevant FL examples; iterative proof repair with Lean's type checker. Outperforms GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover.
- **Relevance:** Retrieval-augmented autoformalization with semantic alignment, though not explicitly domain-conditioned.

#### LeanSearch v2: Global Premise Retrieval for Lean 4 (May 2026)
- [arXiv:2605.13137](https://arxiv.org/abs/2605.13137)
- State-of-the-art Mathlib premise retrieval **without domain-specific fine-tuning**. Reasoning mode uses iterative sketch-retrieve-reflect cycles. Recovers 46.1% of ground-truth premise groups within top-10.
- **Relevance:** Sets the retrieval baseline that any domain-conditioned retrieval approach must beat.

---

### 3. MODERATE RELEVANCE -- Domain-specific benchmarks and tools

#### CAM-Bench: Computational and Applied Mathematics in Lean (May 2026)
- [arXiv:2605.17255](https://arxiv.org/abs/2605.17255)
- 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis. Addresses underrepresentation of applied math in existing benchmarks. Uses a dependency-recovery pipeline.
- **Relevance:** Another domain-stratified benchmark, though focused on computational/applied math rather than broad domain coverage.

#### Construction-Verification / AMBER Benchmark (February 2026)
- [arXiv:2602.01291](https://arxiv.org/abs/2602.01291)
- Lean 4 framework for applied mathematics spanning convex analysis, optimization, numerical methods. Enforces construction-verification workflow.
- **Relevance:** Domain-specific benchmark for applied math formalization.

#### FormalEvolve: Neuro-Symbolic Evolutionary Search (March 2026)
- [arXiv:2603.19828](https://arxiv.org/abs/2603.19828)
- Evolutionary framework for autoformalization using LLM-driven mutation/crossover with AST rewrite operations. Achieves 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet.
- **Relevance:** Novel search-based autoformalization approach; not domain-adaptive but relevant as a concurrent method.

#### Cycle Consistency Fine-tuning for Lean4 Autoformalization (March 2026)
- [arXiv:2603.24372](https://arxiv.org/abs/2603.24372)
- RL fine-tuning (GRPO) with cycle consistency reward on Qwen3.5-2B/LoRA for NL-to-Lean4 translation. Notes that FineLeanCorpus provides 509k pairs **with domain labels**.
- **Relevance:** The existence of domain labels in FineLeanCorpus means domain-conditioned training is straightforward; if the proposal relies on creating domain-labeled data, this is prior art.

#### Lean Atlas: Human-AI Collaborative Formalization (March/April 2026)
- [arXiv:2604.16347](https://arxiv.org/abs/2604.16347)
- Lean 4 tool for visualizing dependency graphs as interactive web viewers; human-in-the-loop semantic verification to catch AI hallucinations.
- **Relevance:** Addresses semantic faithfulness in formalization through human oversight rather than domain adaptation.

#### MerLean: Autoformalization for Quantum Computation (February 2026)
- [arXiv:2602.16554](https://arxiv.org/abs/2602.16554)
- Domain-specific autoformalization agent for quantum computing; produced 2,050 Lean declarations from 114 statements across 3 papers.
- **Relevance:** A concrete example of domain-specific autoformalization, though for a single domain (quantum).

---

### 4. CONTEXTUAL -- Surveys and broader landscape

#### Autoformalization in the Era of LLMs: A Survey (May 2025, revised July 2025)
- [arXiv:2505.23486](https://arxiv.org/abs/2505.23486)
- Comprehensive survey covering data preprocessing, model design, and evaluation across domains and difficulty levels. Examines domain-specific performance disparities: models excel in Information Theory and Logic but struggle with category theory and model theory.
- **Relevance:** The survey already documents domain-dependent performance gaps, which is relevant context for any domain-adaptive proposal.

#### SciAF Framework / Lean for Science (February 2026)
- [PDF](https://www.ulam.ai/research/lean-science.pdf)
- Proposes mathematics-first transfer for autoformalization beyond math: train on math, then port to physics, chemistry, biology, economics. Includes domain validity predicates.
- **Relevance:** Cross-domain transfer for autoformalization is a related direction.

---

### Summary Assessment of Novelty Threats

| Proposal Claim | Concurrent Work | Severity |
|---|---|---|
| Domain-conditioned retrieval for autoformalization | **CRAMF (ICLR 2026)** -- domain/application-level query augmentation with Mathlib retrieval | **HIGH** -- must differentiate |
| Domain-stratified error analysis | **"Do LLMs Game Formalization?" (ICLR 2026 workshop)** -- formalization error taxonomy | **MEDIUM-HIGH** -- different angle (faithfulness vs. domain) but overlapping |
| Domain-stratified evaluation benchmark | **MathAtlas (May 2026)** -- 87 math areas, 52k entities | **HIGH** -- must cite and explain differentiation |
| Domain-adaptive fine-tuning | **Cycle Consistency (March 2026)** -- FineLeanCorpus already has domain labels | **MEDIUM** -- domain labels exist; what's novel in the adaptation method? |
| Dependency-aware retrieval for formalization | **Aria (ICLR 2026)**, **DRIFT (ICLR 2026)**, **LeanSearch v2 (May 2026)** | **MEDIUM** -- crowded space for retrieval-augmented formalization |

The most critical papers to address are **CRAMF**, **MathAtlas**, and the **"Do LLMs Game Formalization?"** error taxonomy paper. The proposal should clearly articulate how its domain-adaptive approach differs from CRAMF's domain-level query augmentation, how its evaluation strategy goes beyond MathAtlas's 87-area coverage, and how its error taxonomy is distinct from the faithfulness taxonomy in the ICLR 2026 workshop paper.

agentId: ac1b5fe532ebdaa7c (use SendMessage with to: 'ac1b5fe532ebdaa7c' to continue this agent)
&lt;usage>total_tokens: 34231
tool_uses: 29
duration_ms: 149795&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d39e96bf-38e0-496e-8334-385b18a8c6a8",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "abe5a41e-b6b2-4360-8e39-5e8f657b7313",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a proposal about domain-adaptive autoformalization for mathematical theorem proving in Lean 4. I need to search for any NEW papers from March-May 2026 that might be concurrent work or that the proposal might have missed. Search specifically for:\n\n1. \"domain-adaptive autoformalization\" OR \"domain-specific autoformalization\" 2026\n2. \"autoformalization\" \"domain\" \"lean\" 2026 site:arxiv.org\n3. \"mathlib\" \"domain\" \"autoformalization\" 2026\n4. \"subdomain\" \"formalization\" \"lean\" 2026\n5. \"error taxonomy\" \"autoformalization\" 2026\n6. \"domain-conditioned retrieval\" \"theorem proving\" 2026\n7. Any new autoformalization papers from April-May 2026 on arxiv\n\nFocus on finding work that:\n- Conditions autoformalization on mathematical subdomain\n- Provides domain-stratified error analysis for formal math\n- Uses domain-aware retrieval for formalization\n- Any new benchmarks or datasets for domain-stratified autoformalization evaluation\n\nReport everything you find, especially anything that might pre-empt the proposal's novelty claims.",
    "agentId": "ac1b5fe532ebdaa7c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is my full report.\n\n---\n\n## Concurrent Work Report: Domain-Adaptive Autoformalization for Lean 4 (March--May 2026)\n\nI searched extensively across seven query categories and multiple follow-up queries. Below are the findings organized by relevance to your proposal's core novelty claims.\n\n---\n\n### 1. HIGHEST RELEVANCE -- Papers that directly overlap with or threaten novelty claims\n\n#### CRAMF: Concept-driven Retrieval-Augmented Mathematical Formalization (ICLR 2026)\n- [arXiv:2508.06931](https://arxiv.org/abs/2508.06931) / [OpenReview](https://openreview.net/forum?id=09lmwhDqZ3)\n- **Published at ICLR 2026 (main conference).**\n- Builds a concept-definition knowledge base from Mathlib4 (26,000+ formal definitions, 1,000+ core concepts). Proposes **contextual query augmentation with domain- and application-level signals** to resolve conceptual polymorphism. Uses a dual-channel hybrid retrieval strategy with reranking.\n- **Threat to novelty:** This directly addresses domain-aware retrieval for autoformalization. If the proposal claims domain-conditioned retrieval as novel, CRAMF is strong prior/concurrent work that must be cited and differentiated from. CRAMF achieves up to 62.1% relative improvement on miniF2F, ProofNet, and an AdvancedMath benchmark.\n\n#### MathAtlas: A Benchmark for Autoformalization in the Wild (May 2026)\n- [arXiv:2605.14061](https://arxiv.org/abs/2605.14061)\n- First large-scale benchmark of graduate-level math autoformalization: ~52k entities from 103 textbooks, spanning **87 areas of mathematics** (real analysis, differential geometry, category theory, topology, quantum groups, etc.). Includes a dependency graph with ~178k relations.\n- **Threat to novelty:** If the proposal claims to introduce domain-stratified evaluation for autoformalization, MathAtlas already provides a benchmark organized across 87 mathematical subfields with dependency-aware structure. Strong baselines achieve only 9.8% on theorems and 16.7% on definitions, demonstrating domain-stratified difficulty variation.\n\n#### \"Do LLMs Game Formalization?\" (VerifAI-2 Workshop, ICLR 2026, April 2026)\n- [arXiv:2604.19459](https://arxiv.org/abs/2604.19459)\n- Introduces an **error taxonomy for formalization faithfulness** with categories: CONCLUSION AS AXIOM, FABRICATED CONTRADICTION, FABRICATED WORLD KNOWLEDGE, FABRICATED INVENTED, plus mistranslation and omission categories.\n- **Threat to novelty:** If the proposal claims a novel error taxonomy for autoformalization, this paper provides a structured taxonomy specifically for formalization faithfulness errors. The taxonomy is applied to GPT-5 and DeepSeek-R1, revealing distinct failure modes.\n\n---\n\n### 2. HIGH RELEVANCE -- Papers that partially overlap\n\n#### DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\n- [arXiv:2510.10815](https://arxiv.org/abs/2510.10815) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010321)\n- Decomposes informal statements into sub-queries, performs **targeted premise retrieval from Mathlib**, and retrieves illustrative theorems to guide formalization. Nearly doubles F1 score vs. DPR baseline on ProofNet.\n- **Relevance:** Overlaps with any domain-aware retrieval-for-formalization claims, though DRIFT's decomposition is statement-level rather than domain-level.\n\n#### Aria: Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\n- [arXiv:2510.04520](https://arxiv.org/abs/2510.04520) / [ICLR 2026 Poster](https://iclr.cc/virtual/2026/poster/10010860)\n- Uses a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and constructing formalizations from grounded concepts. AriaScorer retrieves definitions from Mathlib for term-level grounding. Achieves 91.6% compilation and 68.5% accuracy on ProofNet.\n- **Relevance:** Dependency-graph-based retrieval for autoformalization is closely related to domain-aware retrieval approaches.\n\n#### ProofBridge: Auto-Formalization of NL Proofs in Lean via Joint Embeddings (ICLR 2026 main track)\n- [arXiv:2510.15681](https://arxiv.org/abs/2510.15681)\n- Joint embedding model aligning NL and FL theorem-proof pairs; cross-modal retrieval of semantically relevant FL examples; iterative proof repair with Lean's type checker. Outperforms GPT-5, Gemini-2.5, Kimina-Prover, DeepSeek-Prover.\n- **Relevance:** Retrieval-augmented autoformalization with semantic alignment, though not explicitly domain-conditioned.\n\n#### LeanSearch v2: Global Premise Retrieval for Lean 4 (May 2026)\n- [arXiv:2605.13137](https://arxiv.org/abs/2605.13137)\n- State-of-the-art Mathlib premise retrieval **without domain-specific fine-tuning**. Reasoning mode uses iterative sketch-retrieve-reflect cycles. Recovers 46.1% of ground-truth premise groups within top-10.\n- **Relevance:** Sets the retrieval baseline that any domain-conditioned retrieval approach must beat.\n\n---\n\n### 3. MODERATE RELEVANCE -- Domain-specific benchmarks and tools\n\n#### CAM-Bench: Computational and Applied Mathematics in Lean (May 2026)\n- [arXiv:2605.17255](https://arxiv.org/abs/2605.17255)\n- 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis. Addresses underrepresentation of applied math in existing benchmarks. Uses a dependency-recovery pipeline.\n- **Relevance:** Another domain-stratified benchmark, though focused on computational/applied math rather than broad domain coverage.\n\n#### Construction-Verification / AMBER Benchmark (February 2026)\n- [arXiv:2602.01291](https://arxiv.org/abs/2602.01291)\n- Lean 4 framework for applied mathematics spanning convex analysis, optimization, numerical methods. Enforces construction-verification workflow.\n- **Relevance:** Domain-specific benchmark for applied math formalization.\n\n#### FormalEvolve: Neuro-Symbolic Evolutionary Search (March 2026)\n- [arXiv:2603.19828](https://arxiv.org/abs/2603.19828)\n- Evolutionary framework for autoformalization using LLM-driven mutation/crossover with AST rewrite operations. Achieves 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet.\n- **Relevance:** Novel search-based autoformalization approach; not domain-adaptive but relevant as a concurrent method.\n\n#### Cycle Consistency Fine-tuning for Lean4 Autoformalization (March 2026)\n- [arXiv:2603.24372](https://arxiv.org/abs/2603.24372)\n- RL fine-tuning (GRPO) with cycle consistency reward on Qwen3.5-2B/LoRA for NL-to-Lean4 translation. Notes that FineLeanCorpus provides 509k pairs **with domain labels**.\n- **Relevance:** The existence of domain labels in FineLeanCorpus means domain-conditioned training is straightforward; if the proposal relies on creating domain-labeled data, this is prior art.\n\n#### Lean Atlas: Human-AI Collaborative Formalization (March/April 2026)\n- [arXiv:2604.16347](https://arxiv.org/abs/2604.16347)\n- Lean 4 tool for visualizing dependency graphs as interactive web viewers; human-in-the-loop semantic verification to catch AI hallucinations.\n- **Relevance:** Addresses semantic faithfulness in formalization through human oversight rather than domain adaptation.\n\n#### MerLean: Autoformalization for Quantum Computation (February 2026)\n- [arXiv:2602.16554](https://arxiv.org/abs/2602.16554)\n- Domain-specific autoformalization agent for quantum computing; produced 2,050 Lean declarations from 114 statements across 3 papers.\n- **Relevance:** A concrete example of domain-specific autoformalization, though for a single domain (quantum).\n\n---\n\n### 4. CONTEXTUAL -- Surveys and broader landscape\n\n#### Autoformalization in the Era of LLMs: A Survey (May 2025, revised July 2025)\n- [arXiv:2505.23486](https://arxiv.org/abs/2505.23486)\n- Comprehensive survey covering data preprocessing, model design, and evaluation across domains and difficulty levels. Examines domain-specific performance disparities: models excel in Information Theory and Logic but struggle with category theory and model theory.\n- **Relevance:** The survey already documents domain-dependent performance gaps, which is relevant context for any domain-adaptive proposal.\n\n#### SciAF Framework / Lean for Science (February 2026)\n- [PDF](https://www.ulam.ai/research/lean-science.pdf)\n- Proposes mathematics-first transfer for autoformalization beyond math: train on math, then port to physics, chemistry, biology, economics. Includes domain validity predicates.\n- **Relevance:** Cross-domain transfer for autoformalization is a related direction.\n\n---\n\n### Summary Assessment of Novelty Threats\n\n| Proposal Claim | Concurrent Work | Severity |\n|---|---|---|\n| Domain-conditioned retrieval for autoformalization | **CRAMF (ICLR 2026)** -- domain/application-level query augmentation with Mathlib retrieval | **HIGH** -- must differentiate |\n| Domain-stratified error analysis | **\"Do LLMs Game Formalization?\" (ICLR 2026 workshop)** -- formalization error taxonomy | **MEDIUM-HIGH** -- different angle (faithfulness vs. domain) but overlapping |\n| Domain-stratified evaluation benchmark | **MathAtlas (May 2026)** -- 87 math areas, 52k entities | **HIGH** -- must cite and explain differentiation |\n| Domain-adaptive fine-tuning | **Cycle Consistency (March 2026)** -- FineLeanCorpus already has domain labels | **MEDIUM** -- domain labels exist; what's novel in the adaptation method? |\n| Dependency-aware retrieval for formalization | **Aria (ICLR 2026)**, **DRIFT (ICLR 2026)**, **LeanSearch v2 (May 2026)** | **MEDIUM** -- crowded space for retrieval-augmented formalization |\n\nThe most critical papers to address are **CRAMF**, **MathAtlas**, and the **\"Do LLMs Game Formalization?\"** error taxonomy paper. The proposal should clearly articulate how its domain-adaptive approach differs from CRAMF's domain-level query augmentation, how its evaluation strategy goes beyond MathAtlas's 87-area coverage, and how its error taxonomy is distinct from the faithfulness taxonomy in the ICLR 2026 workshop paper."
      }
    ],
    "totalDurationMs": 149795,
    "totalTokens": 34231,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3145,
      "cache_read_input_tokens": 28254,
      "output_tokens": 2831,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3145
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2831,
          "cache_read_input_tokens": 28254,
          "cache_creation_input_tokens": 3145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3145,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 29
    }
  },
  "sourceToolAssistantUUID": "d39e96bf-38e0-496e-8334-385b18a8c6a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-28T14:53:35.305Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KJ7PH2FiNHQSUfQbXo6rMR`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Shebzukhov cycle consistency",
  "prompt": "I need to verify claims about a paper by Shebzukhov (arXiv 2603.24372) on cycle consistency fine-tuning for Lean4 autoformalization:\n1. Does it report number theory achieving 0.722 cycle consistency vs. calculus at 0.516?\n2. Does it report abstract algebra at 0.641 vs. analysis at 0.493 on PutnamBench?\n3. Does it perform only \"observational analysis\" without domain conditioning or error type classification?\n4. Does it conclude that \"improvement is general rather than domain-specific\"?\n\nPlease search for \"arXiv 2603.24372\" and \"Shebzukhov cycle consistency Lean autoformalization\" and try to fetch the paper.\n\nReport all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abe5a41e-b6b2-4360-8e39-5e8f657b7313",
  "isSidechain": false,
  "requestId": "req_011CbVA6MruXQGWBupsxQPfh",
  "type": "assistant",
  "uuid": "cf0048e4-e560-4661-942e-a1c290d22cc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJxpUvyUbr4zJgWQEAAJj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3276,
      "cache_read_input_tokens": 37882,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 280,
          "cache_read_input_tokens": 37882,
          "cache_creation_input_tokens": 3276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3276
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

_source line 21 · 2026-05-28T14:54:48.420Z_

<details><summary>↩ Tool result · `toolu_01KJ7PH2FiNHQSUfQbXo6rMR`</summary>

```text
I now have comprehensive and consistent information from the paper to address all four claims. Here are my findings:

---

## Findings on arXiv 2603.24372 (Shebzukhov, "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning")

The paper exists, is authored by Arsen Shebzukhov (Stanford University, CS224N project), and was published March 25, 2026. It fine-tunes Qwen3.5-2B with LoRA using GRPO with a cycle consistency reward for NL-to-Lean4 autoformalization.

### Claim 1: Number theory at 0.722 vs. calculus at 0.516 on cycle consistency
**CONFIRMED.** The paper reports domain-level cycle consistency scores on the FineLeanCorpus (FLC) held-out set. Number theory achieves **0.722** (the highest domain score) and calculus achieves **0.516** (the weakest). These exact numbers match the claim.

### Claim 2: Abstract algebra at 0.641 vs. analysis at 0.493 on PutnamBench
**CONFIRMED.** On PutnamBench, abstract algebra scores **0.641** and analysis scores **0.493**. These exact numbers match the claim.

### Claim 3: Only "observational analysis" without domain conditioning or error type classification
**CONFIRMED.** The paper does **not** perform domain conditioning during training (no domain labels are used in the model) and does **not** perform error type classification. The domain-level performance breakdown is purely post-hoc/observational analysis of evaluation results. The method itself is domain-agnostic.

### Claim 4: Concludes "improvement is general rather than domain-specific"
**CONFIRMED.** The paper contains the exact quote: *"Notably, RL outperforms SFT curriculum in every domain on both datasets, suggesting that the improvement is general rather than domain-specific."* The authors attribute performance variation across domains to the inherent nature of mathematical statements (compact algebraic notation vs. verbose epsilon-delta/measure-theoretic formulations) rather than to any domain-specific training effect.

---

**Summary:** All four claims are accurate and verified against the paper's content.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2603.24372)
- [Full HTML version](https://arxiv.org/html/2603.24372v1)
- [PDF version](https://arxiv.org/pdf/2603.24372)

agentId: a85517861ee682f02 (use SendMessage with to: 'a85517861ee682f02' to continue this agent)
&lt;usage>total_tokens: 14613
tool_uses: 7
duration_ms: 73110&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf0048e4-e560-4661-942e-a1c290d22cc5",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "ac3e0e79-ed1f-4678-8a1c-1343b9835bbc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify claims about a paper by Shebzukhov (arXiv 2603.24372) on cycle consistency fine-tuning for Lean4 autoformalization:\n1. Does it report number theory achieving 0.722 cycle consistency vs. calculus at 0.516?\n2. Does it report abstract algebra at 0.641 vs. analysis at 0.493 on PutnamBench?\n3. Does it perform only \"observational analysis\" without domain conditioning or error type classification?\n4. Does it conclude that \"improvement is general rather than domain-specific\"?\n\nPlease search for \"arXiv 2603.24372\" and \"Shebzukhov cycle consistency Lean autoformalization\" and try to fetch the paper.\n\nReport all findings.",
    "agentId": "a85517861ee682f02",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive and consistent information from the paper to address all four claims. Here are my findings:\n\n---\n\n## Findings on arXiv 2603.24372 (Shebzukhov, \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning\")\n\nThe paper exists, is authored by Arsen Shebzukhov (Stanford University, CS224N project), and was published March 25, 2026. It fine-tunes Qwen3.5-2B with LoRA using GRPO with a cycle consistency reward for NL-to-Lean4 autoformalization.\n\n### Claim 1: Number theory at 0.722 vs. calculus at 0.516 on cycle consistency\n**CONFIRMED.** The paper reports domain-level cycle consistency scores on the FineLeanCorpus (FLC) held-out set. Number theory achieves **0.722** (the highest domain score) and calculus achieves **0.516** (the weakest). These exact numbers match the claim.\n\n### Claim 2: Abstract algebra at 0.641 vs. analysis at 0.493 on PutnamBench\n**CONFIRMED.** On PutnamBench, abstract algebra scores **0.641** and analysis scores **0.493**. These exact numbers match the claim.\n\n### Claim 3: Only \"observational analysis\" without domain conditioning or error type classification\n**CONFIRMED.** The paper does **not** perform domain conditioning during training (no domain labels are used in the model) and does **not** perform error type classification. The domain-level performance breakdown is purely post-hoc/observational analysis of evaluation results. The method itself is domain-agnostic.\n\n### Claim 4: Concludes \"improvement is general rather than domain-specific\"\n**CONFIRMED.** The paper contains the exact quote: *\"Notably, RL outperforms SFT curriculum in every domain on both datasets, suggesting that the improvement is general rather than domain-specific.\"* The authors attribute performance variation across domains to the inherent nature of mathematical statements (compact algebraic notation vs. verbose epsilon-delta/measure-theoretic formulations) rather than to any domain-specific training effect.\n\n---\n\n**Summary:** All four claims are accurate and verified against the paper's content.\n\nSources:\n- [arXiv abstract page](https://arxiv.org/abs/2603.24372)\n- [Full HTML version](https://arxiv.org/html/2603.24372v1)\n- [PDF version](https://arxiv.org/pdf/2603.24372)"
      }
    ],
    "totalDurationMs": 73110,
    "totalTokens": 14613,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 12926,
      "output_tokens": 604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1082
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 604,
          "cache_read_input_tokens": 12926,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1082,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "cf0048e4-e560-4661-942e-a1c290d22cc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "ac3e0e79-ed1f-4678-8a1c-1343b9835bbc",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Tool call

_source line 24 · 2026-05-28T14:54:56.925Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013ew2uBkuZWLBtNiwiFun2y`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search \"Do LLMs Game Formalization\" paper",
  "prompt": "I need to find and verify details about a paper called \"Do LLMs Game Formalization?\" (arXiv 2604.19459, April 2026). This apparently introduces an error taxonomy for formalization faithfulness. I need to:\n\n1. Verify it exists and what its exact title is\n2. Check what error taxonomy categories it defines (CONCLUSION AS AXIOM, FABRICATED CONTRADICTION, etc.)\n3. Understand whether this is about autoformalization errors in the same sense as Lean compilation errors (typeclass failures, coercion mismatches) or about semantic faithfulness errors\n4. Check if it was published at a workshop or main conference\n5. Assess whether this overlaps with a proposal to create a \"domain-stratified error taxonomy\" based on APRIL's Lean compiler error types\n\nSearch for \"arXiv 2604.19459\" and \"Do LLMs Game Formalization\" and try to fetch the abstract page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3e0e79-ed1f-4678-8a1c-1343b9835bbc",
  "isSidechain": false,
  "requestId": "req_011CbVACN1kVkuSjhvH2tsmb",
  "type": "assistant",
  "uuid": "33dbb4b8-f08d-4696-ae2f-6681ac481173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDepQo8DqQ2C5HBJGpi4Dk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 41158,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 41158,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 957
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

_source line 25 · 2026-05-28T14:56:33.985Z_

<details><summary>↩ Tool result · `toolu_013ew2uBkuZWLBtNiwiFun2y`</summary>

```text
I now have comprehensive information to answer all five questions. Here is my findings report:

---

## Findings on arXiv 2604.19459

### 1. Existence and Exact Title

The paper exists and is confirmed at [arXiv:2604.19459](https://arxiv.org/abs/2604.19459). Its exact title is:

**"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"**

Authors: Kyuhee Kim, Auguste Poiroux, Antoine Bosselut. Submitted April 21, 2026.

### 2. Error Taxonomy Categories

The paper defines a four-category error taxonomy (presented in Table 1 / Appendix D):

**Category 1 -- Mistranslation** (single-statement errors):
- Wrong connective (e.g., AND substituted for IMPLIES)
- Wrong negation (P vs. NOT P)
- Wrong quantifier (EXISTS vs. FORALL)
- Wrong direction (Q->P instead of P->Q)
- Wrong scope (quantifier binding errors)
- Wrong predicate, wrong entity, wrong argument order

**Category 2 -- Fabrication** (multi-statement errors):
- **CONCLUSION AS AXIOM**: the goal is directly stated as an axiom (accounts for 56.2% of detected fabrications in GPT-5)
- **World knowledge**: common-sense inferences not present in the premises (16.2%)
- **Invented**: entirely made-up facts with no basis (12.4%)
- **Fabricated axiom** (general): unstated information added

**Category 3 -- Omission**:
- Missing axiom (a premise is not formalized)
- Dropped antecedent (a conditional's premise is omitted)

**Category 4 -- Contradiction**:
- Induced contradiction (axioms collectively entail False -- this is what would be called FABRICATED CONTRADICTION)

So the categories you mentioned (CONCLUSION AS AXIOM, FABRICATED CONTRADICTION) do appear, though "FABRICATED CONTRADICTION" is labeled as "Induced contradiction" under the Contradiction category. The taxonomy builds on prior work by Barker-Plummer et al. (2008) on human student translation errors and Thatikonda et al. (2024) on LLM errors in NL-to-FOL translation. The novel contribution is the fabrication and omission categories, which are specific to multi-statement axiomatic systems where models define entire formal systems from scratch.

### 3. Semantic Faithfulness Errors vs. Lean Compilation Errors

This is a critical distinction. The paper is explicitly and entirely about **semantic faithfulness errors**, NOT about Lean compilation errors. The authors state directly:

> "Formal verification provides strong guarantees for [proof validity]: a proof that type-checks in Lean's kernel is mathematically valid. However, verification reveals nothing about whether the formalization faithfully represents the original natural language."

The whole point of the paper is that models achieve 87-99% Lean compilation rates, yet the formalizations can be semantically unfaithful. The error taxonomy captures how models produce outputs that compile and type-check perfectly in Lean but do not faithfully represent the original natural-language problem. Typeclass failures, coercion mismatches, and syntax errors are not what this paper studies -- those are compilation failures that Lean's kernel already catches. This paper is about errors that *evade* the compiler.

### 4. Publication Venue

Published at the **VerifAI-2 Workshop at ICLR 2026** (non-archival). It is a workshop paper, not a main conference paper.

### 5. Overlap with a "Domain-Stratified Error Taxonomy" Based on APRIL's Lean Compiler Error Types

These are fundamentally different taxonomies addressing different layers of the problem:

- **Kim et al. (2604.19459)** taxonomy: Classifies *semantic faithfulness* errors -- situations where the Lean code compiles fine but does not faithfully represent the natural-language problem. The categories (Mistranslation, Fabrication, Omission, Contradiction) are about logical/translational fidelity.

- **A domain-stratified error taxonomy based on Lean compiler error types**: This would classify *compilation failures* -- typeclass resolution failures, coercion mismatches, unknown identifier errors, tactic failures, type mismatches, etc. These are errors that prevent the code from type-checking at all.

I was unable to find a specific published system or paper called "APRIL" that introduces a domain-stratified error taxonomy of Lean compiler error types. The name "APRIL" did not surface in any search results related to autoformalization error taxonomies. It may be unpublished, under a different name, or a proposal rather than a published work. Related work in the space includes "Learning to Repair Lean Proofs from Compiler Feedback" (arXiv 2602.02990) and Process-Driven Autoformalization (FORML4), which use Lean compiler error feedback iteratively but do not publish a formal domain-stratified taxonomy of those errors.

**Bottom line on overlap**: There is essentially **no overlap** between the two. Kim et al.'s taxonomy operates at the semantic faithfulness layer (post-compilation), while a Lean compiler error taxonomy operates at the syntactic/type-checking layer (pre-compilation success). They are complementary, not competing. A complete error analysis pipeline would use both: the compiler error taxonomy to understand why formalizations fail to compile, and Kim et al.'s taxonomy to understand why formalizations that *do* compile may still be unfaithful.

Sources:
- [arXiv:2604.19459 - Abstract page](https://arxiv.org/abs/2604.19459)
- [arXiv:2604.19459 - Full HTML](https://arxiv.org/html/2604.19459)
- [arXiv:2604.19459 - PDF](https://arxiv.org/pdf/2604.19459)

agentId: a27e91e3d2ea92796 (use SendMessage with to: 'a27e91e3d2ea92796' to continue this agent)
&lt;usage>total_tokens: 17280
tool_uses: 8
duration_ms: 97055&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33dbb4b8-f08d-4696-ae2f-6681ac481173",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "46c7787d-24e2-4104-b43b-fd4531b5242d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find and verify details about a paper called \"Do LLMs Game Formalization?\" (arXiv 2604.19459, April 2026). This apparently introduces an error taxonomy for formalization faithfulness. I need to:\n\n1. Verify it exists and what its exact title is\n2. Check what error taxonomy categories it defines (CONCLUSION AS AXIOM, FABRICATED CONTRADICTION, etc.)\n3. Understand whether this is about autoformalization errors in the same sense as Lean compilation errors (typeclass failures, coercion mismatches) or about semantic faithfulness errors\n4. Check if it was published at a workshop or main conference\n5. Assess whether this overlaps with a proposal to create a \"domain-stratified error taxonomy\" based on APRIL's Lean compiler error types\n\nSearch for \"arXiv 2604.19459\" and \"Do LLMs Game Formalization\" and try to fetch the abstract page.",
    "agentId": "a27e91e3d2ea92796",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to answer all five questions. Here is my findings report:\n\n---\n\n## Findings on arXiv 2604.19459\n\n### 1. Existence and Exact Title\n\nThe paper exists and is confirmed at [arXiv:2604.19459](https://arxiv.org/abs/2604.19459). Its exact title is:\n\n**\"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"**\n\nAuthors: Kyuhee Kim, Auguste Poiroux, Antoine Bosselut. Submitted April 21, 2026.\n\n### 2. Error Taxonomy Categories\n\nThe paper defines a four-category error taxonomy (presented in Table 1 / Appendix D):\n\n**Category 1 -- Mistranslation** (single-statement errors):\n- Wrong connective (e.g., AND substituted for IMPLIES)\n- Wrong negation (P vs. NOT P)\n- Wrong quantifier (EXISTS vs. FORALL)\n- Wrong direction (Q->P instead of P->Q)\n- Wrong scope (quantifier binding errors)\n- Wrong predicate, wrong entity, wrong argument order\n\n**Category 2 -- Fabrication** (multi-statement errors):\n- **CONCLUSION AS AXIOM**: the goal is directly stated as an axiom (accounts for 56.2% of detected fabrications in GPT-5)\n- **World knowledge**: common-sense inferences not present in the premises (16.2%)\n- **Invented**: entirely made-up facts with no basis (12.4%)\n- **Fabricated axiom** (general): unstated information added\n\n**Category 3 -- Omission**:\n- Missing axiom (a premise is not formalized)\n- Dropped antecedent (a conditional's premise is omitted)\n\n**Category 4 -- Contradiction**:\n- Induced contradiction (axioms collectively entail False -- this is what would be called FABRICATED CONTRADICTION)\n\nSo the categories you mentioned (CONCLUSION AS AXIOM, FABRICATED CONTRADICTION) do appear, though \"FABRICATED CONTRADICTION\" is labeled as \"Induced contradiction\" under the Contradiction category. The taxonomy builds on prior work by Barker-Plummer et al. (2008) on human student translation errors and Thatikonda et al. (2024) on LLM errors in NL-to-FOL translation. The novel contribution is the fabrication and omission categories, which are specific to multi-statement axiomatic systems where models define entire formal systems from scratch.\n\n### 3. Semantic Faithfulness Errors vs. Lean Compilation Errors\n\nThis is a critical distinction. The paper is explicitly and entirely about **semantic faithfulness errors**, NOT about Lean compilation errors. The authors state directly:\n\n> \"Formal verification provides strong guarantees for [proof validity]: a proof that type-checks in Lean's kernel is mathematically valid. However, verification reveals nothing about whether the formalization faithfully represents the original natural language.\"\n\nThe whole point of the paper is that models achieve 87-99% Lean compilation rates, yet the formalizations can be semantically unfaithful. The error taxonomy captures how models produce outputs that compile and type-check perfectly in Lean but do not faithfully represent the original natural-language problem. Typeclass failures, coercion mismatches, and syntax errors are not what this paper studies -- those are compilation failures that Lean's kernel already catches. This paper is about errors that *evade* the compiler.\n\n### 4. Publication Venue\n\nPublished at the **VerifAI-2 Workshop at ICLR 2026** (non-archival). It is a workshop paper, not a main conference paper.\n\n### 5. Overlap with a \"Domain-Stratified Error Taxonomy\" Based on APRIL's Lean Compiler Error Types\n\nThese are fundamentally different taxonomies addressing different layers of the problem:\n\n- **Kim et al. (2604.19459)** taxonomy: Classifies *semantic faithfulness* errors -- situations where the Lean code compiles fine but does not faithfully represent the natural-language problem. The categories (Mistranslation, Fabrication, Omission, Contradiction) are about logical/translational fidelity.\n\n- **A domain-stratified error taxonomy based on Lean compiler error types**: This would classify *compilation failures* -- typeclass resolution failures, coercion mismatches, unknown identifier errors, tactic failures, type mismatches, etc. These are errors that prevent the code from type-checking at all.\n\nI was unable to find a specific published system or paper called \"APRIL\" that introduces a domain-stratified error taxonomy of Lean compiler error types. The name \"APRIL\" did not surface in any search results related to autoformalization error taxonomies. It may be unpublished, under a different name, or a proposal rather than a published work. Related work in the space includes \"Learning to Repair Lean Proofs from Compiler Feedback\" (arXiv 2602.02990) and Process-Driven Autoformalization (FORML4), which use Lean compiler error feedback iteratively but do not publish a formal domain-stratified taxonomy of those errors.\n\n**Bottom line on overlap**: There is essentially **no overlap** between the two. Kim et al.'s taxonomy operates at the semantic faithfulness layer (post-compilation), while a Lean compiler error taxonomy operates at the syntactic/type-checking layer (pre-compilation success). They are complementary, not competing. A complete error analysis pipeline would use both: the compiler error taxonomy to understand why formalizations fail to compile, and Kim et al.'s taxonomy to understand why formalizations that *do* compile may still be unfaithful.\n\nSources:\n- [arXiv:2604.19459 - Abstract page](https://arxiv.org/abs/2604.19459)\n- [arXiv:2604.19459 - Full HTML](https://arxiv.org/html/2604.19459)\n- [arXiv:2604.19459 - PDF](https://arxiv.org/pdf/2604.19459)"
      }
    ],
    "totalDurationMs": 97055,
    "totalTokens": 17280,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 861,
      "cache_read_input_tokens": 15013,
      "output_tokens": 1405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 861
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1405,
          "cache_read_input_tokens": 15013,
          "cache_creation_input_tokens": 861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 861,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "33dbb4b8-f08d-4696-ae2f-6681ac481173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T14:56:43.619Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DDjXq2PaB5jaUGKWVnN3GY`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify AAAI 2026/2027 deadlines",
  "prompt": "I need to verify:\n1. Has the AAAI 2026 conference already happened? What were its dates and paper submission deadlines?\n2. What are the confirmed deadlines for AAAI 2027? The proposal claims abstract deadline July 21, 2026 and paper deadline July 28, 2026 — are these confirmed?\n3. What is the current status of ICLR 2027 — has the deadline been announced? The proposal estimates Sep 19/24, 2026.\n4. Is the ICML 2026 AI4Math Workshop confirmed? What are the exact deadlines for paper submission and challenge tracks?\n\nSearch for:\n- \"AAAI 2027 deadline\" OR \"AAAI 2027 call for papers\"\n- \"AAAI 2026 conference dates\"\n- \"ICLR 2027 deadline\" OR \"ICLR 2027 call for papers\"\n- \"ICML 2026 AI4Math workshop deadline\"\n\nReport exact dates found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c7787d-24e2-4104-b43b-fd4531b5242d",
  "isSidechain": false,
  "requestId": "req_011CbVAL9LyLXBMx1ekZeWYg",
  "type": "assistant",
  "uuid": "233950a9-c808-466d-bd3a-9f89d3d9434a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nfWnjDun56hHR25sTHssA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 42115,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 42115,
          "cache_creation_input_tokens": 1796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1796
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

_source line 27 · 2026-05-28T14:57:51.084Z_

<details><summary>↩ Tool result · `toolu_01DDjXq2PaB5jaUGKWVnN3GY`</summary>

```text
Here are the findings for each of your four questions:

---

**1. AAAI 2026 -- Already happened?**

Yes, AAAI 2026 (the 40th Annual AAAI Conference) has already taken place.

- **Conference dates:** January 20-27, 2026, with the Main Technical Track running January 22-25, 2026
- **Location:** The Singapore EXPO, Singapore
- **Paper submission deadlines were:** Abstract due July 25, 2025; full paper due August 1, 2025; supplementary material/code due August 4, 2025 (all AoE/UTC-12)

---

**2. AAAI 2027 -- Are the proposed deadlines confirmed?**

Yes, the deadlines the proposal cites are **confirmed and match the official AAAI-27 Call for Papers** on aaai.org:

- **Abstract deadline:** July 21, 2026 (11:59 PM UTC-12) -- CONFIRMED
- **Full paper deadline:** July 28, 2026 (11:59 PM UTC-12) -- CONFIRMED
- **Supplementary material/code:** July 31, 2026
- **Conference dates:** February 16-23, 2027, in Montreal, Canada
- **Other key dates:** Phase 1 rejection notification September 24, 2026; author feedback window October 19-25, 2026; final acceptance/rejection notification November 30, 2026
- The OpenReview submission site opens for author registration June 17, 2026, and for paper submission June 24, 2026.

---

**3. ICLR 2027 -- Has the deadline been announced?**

The ICLR 2027 deadline has **NOT been officially announced** yet. Here is what is known:

- **Tentative conference dates:** April 24-28, 2027, in Singapore (from third-party aggregator sites, not yet confirmed on iclr.cc)
- The official ICLR website (iclr.cc) currently only lists information through ICLR 2026 and its Future Meetings page does not yet include ICLR 2027 details.
- **The proposal's estimates of Sep 19/24, 2026 are reasonable** -- they are directly modeled on ICLR 2026's deadlines, which were abstract September 19, 2025 and full paper September 24, 2025. However, these are extrapolations, not confirmed dates.
- The official ICLR website warns against predatory conferences using the "ICLR" name; only iclr.cc and OpenReview are authoritative sources.

---

**4. ICML 2026 AI4Math Workshop -- Is it confirmed? What are the exact deadlines?**

Yes, the 3rd AI for Math Workshop at ICML 2026 is **confirmed and active**. Exact deadlines:

- **Paper submission deadline:** May 25, 2026 (AoE) -- **this deadline has already passed** (today is May 28, 2026)
- **Challenge deadline:** June 15, 2026 (challenge period: May 1 - June 15, 2026) -- still open
- **Decision notification:** June 15, 2026
- **Camera-ready deadline:** June 25, 2026
- **Workshop date:** Saturday, July 11, 2026

The workshop is part of ICML 2026, held July 6-11, 2026 at the COEX Convention & Exhibition Center, Seoul, South Korea. Challenge tracks are live on Codabench.

---

**Summary of proposal accuracy:**
- AAAI 2027 deadlines (abstract July 21, paper July 28) -- **Correct and officially confirmed**
- ICLR 2027 deadlines (Sep 19/24 estimate) -- **Reasonable estimate based on ICLR 2026 pattern, but NOT yet officially confirmed**
- ICML 2026 AI4Math paper deadline -- **Already passed** as of May 25, 2026; challenge track deadline (June 15) is still upcoming

Sources:
- [AAAI-26 Official Conference Page](https://aaai.org/conference/aaai/aaai-26/)
- [AAAI-26 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/)
- [AAAI-27 Official Conference Page](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)
- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)
- [ICLR Future Meetings](https://iclr.cc/Conferences/FutureMeetings)
- [3rd AI for Math Workshop @ ICML 2026](https://ai4math2026.github.io/)
- [AI for Math Workshop @ ICML 2026 on X](https://x.com/ai4mathworkshop/status/1934991398471684096)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)

agentId: a088b40cf37c64974 (use SendMessage with to: 'a088b40cf37c64974' to continue this agent)
&lt;usage>total_tokens: 19482
tool_uses: 13
duration_ms: 67461&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "233950a9-c808-466d-bd3a-9f89d3d9434a",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "e06c0a87-9cac-4204-9b91-9e2e7c35a6e2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify:\n1. Has the AAAI 2026 conference already happened? What were its dates and paper submission deadlines?\n2. What are the confirmed deadlines for AAAI 2027? The proposal claims abstract deadline July 21, 2026 and paper deadline July 28, 2026 — are these confirmed?\n3. What is the current status of ICLR 2027 — has the deadline been announced? The proposal estimates Sep 19/24, 2026.\n4. Is the ICML 2026 AI4Math Workshop confirmed? What are the exact deadlines for paper submission and challenge tracks?\n\nSearch for:\n- \"AAAI 2027 deadline\" OR \"AAAI 2027 call for papers\"\n- \"AAAI 2026 conference dates\"\n- \"ICLR 2027 deadline\" OR \"ICLR 2027 call for papers\"\n- \"ICML 2026 AI4Math workshop deadline\"\n\nReport exact dates found.",
    "agentId": "a088b40cf37c64974",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for each of your four questions:\n\n---\n\n**1. AAAI 2026 -- Already happened?**\n\nYes, AAAI 2026 (the 40th Annual AAAI Conference) has already taken place.\n\n- **Conference dates:** January 20-27, 2026, with the Main Technical Track running January 22-25, 2026\n- **Location:** The Singapore EXPO, Singapore\n- **Paper submission deadlines were:** Abstract due July 25, 2025; full paper due August 1, 2025; supplementary material/code due August 4, 2025 (all AoE/UTC-12)\n\n---\n\n**2. AAAI 2027 -- Are the proposed deadlines confirmed?**\n\nYes, the deadlines the proposal cites are **confirmed and match the official AAAI-27 Call for Papers** on aaai.org:\n\n- **Abstract deadline:** July 21, 2026 (11:59 PM UTC-12) -- CONFIRMED\n- **Full paper deadline:** July 28, 2026 (11:59 PM UTC-12) -- CONFIRMED\n- **Supplementary material/code:** July 31, 2026\n- **Conference dates:** February 16-23, 2027, in Montreal, Canada\n- **Other key dates:** Phase 1 rejection notification September 24, 2026; author feedback window October 19-25, 2026; final acceptance/rejection notification November 30, 2026\n- The OpenReview submission site opens for author registration June 17, 2026, and for paper submission June 24, 2026.\n\n---\n\n**3. ICLR 2027 -- Has the deadline been announced?**\n\nThe ICLR 2027 deadline has **NOT been officially announced** yet. Here is what is known:\n\n- **Tentative conference dates:** April 24-28, 2027, in Singapore (from third-party aggregator sites, not yet confirmed on iclr.cc)\n- The official ICLR website (iclr.cc) currently only lists information through ICLR 2026 and its Future Meetings page does not yet include ICLR 2027 details.\n- **The proposal's estimates of Sep 19/24, 2026 are reasonable** -- they are directly modeled on ICLR 2026's deadlines, which were abstract September 19, 2025 and full paper September 24, 2025. However, these are extrapolations, not confirmed dates.\n- The official ICLR website warns against predatory conferences using the \"ICLR\" name; only iclr.cc and OpenReview are authoritative sources.\n\n---\n\n**4. ICML 2026 AI4Math Workshop -- Is it confirmed? What are the exact deadlines?**\n\nYes, the 3rd AI for Math Workshop at ICML 2026 is **confirmed and active**. Exact deadlines:\n\n- **Paper submission deadline:** May 25, 2026 (AoE) -- **this deadline has already passed** (today is May 28, 2026)\n- **Challenge deadline:** June 15, 2026 (challenge period: May 1 - June 15, 2026) -- still open\n- **Decision notification:** June 15, 2026\n- **Camera-ready deadline:** June 25, 2026\n- **Workshop date:** Saturday, July 11, 2026\n\nThe workshop is part of ICML 2026, held July 6-11, 2026 at the COEX Convention & Exhibition Center, Seoul, South Korea. Challenge tracks are live on Codabench.\n\n---\n\n**Summary of proposal accuracy:**\n- AAAI 2027 deadlines (abstract July 21, paper July 28) -- **Correct and officially confirmed**\n- ICLR 2027 deadlines (Sep 19/24 estimate) -- **Reasonable estimate based on ICLR 2026 pattern, but NOT yet officially confirmed**\n- ICML 2026 AI4Math paper deadline -- **Already passed** as of May 25, 2026; challenge track deadline (June 15) is still upcoming\n\nSources:\n- [AAAI-26 Official Conference Page](https://aaai.org/conference/aaai/aaai-26/)\n- [AAAI-26 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-26/main-technical-track-call/)\n- [AAAI-27 Official Conference Page](https://aaai.org/conference/aaai/aaai-27/)\n- [AAAI-27 Main Technical Track Call for Papers](https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/)\n- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)\n- [ICLR Future Meetings](https://iclr.cc/Conferences/FutureMeetings)\n- [3rd AI for Math Workshop @ ICML 2026](https://ai4math2026.github.io/)\n- [AI for Math Workshop @ ICML 2026 on X](https://x.com/ai4mathworkshop/status/1934991398471684096)\n- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)"
      }
    ],
    "totalDurationMs": 67461,
    "totalTokens": 19482,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 669,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 16822,
      "output_tokens": 1310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 669,
          "output_tokens": 1310,
          "cache_read_input_tokens": 16822,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 681,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "233950a9-c808-466d-bd3a-9f89d3d9434a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T14:58:01.491Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SgFdoqumfp3Fb3TEkmHNT3`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search FormalEvolve and CAM-Bench",
  "prompt": "I need to verify two recent papers that might be relevant concurrent work to a domain-adaptive autoformalization proposal:\n\n1. FormalEvolve (arXiv 2603.19828, March 2026) — claimed to achieve 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet via evolutionary framework for autoformalization. Does this use any domain conditioning? What are the actual numbers?\n\n2. CAM-Bench (arXiv 2605.17255, May 2026) — claimed to be 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis. Is this a new domain-specific autoformalization benchmark?\n\n3. Also search for any other very recent autoformalization work from May 2026 that I might be missing. Search for \"autoformalization May 2026 arxiv\" and \"lean4 formalization 2026 new\".\n\nReport findings briefly."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e06c0a87-9cac-4204-9b91-9e2e7c35a6e2",
  "isSidechain": false,
  "requestId": "req_011CbVARpzapEYuhaCEiSasj",
  "type": "assistant",
  "uuid": "f4557dff-7052-4601-ba85-5a2a708255d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199gqt5xw63jUNtxibtMsCq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1729,
      "cache_read_input_tokens": 43911,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 43911,
          "cache_creation_input_tokens": 1729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1729
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

_source line 29 · 2026-05-28T14:59:03.211Z_

<details><summary>↩ Tool result · `toolu_01SgFdoqumfp3Fb3TEkmHNT3`</summary>

```text
Here are my findings on all three queries:

---

**1. FormalEvolve (arXiv 2603.19828, March 2026)**

The paper is real. Full title: "FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization" by Haijian Lu, Wei Wang, and Jing Liu.

- The claimed numbers are **confirmed**: 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet (both at 100 generator calls).
- It does **not** use domain conditioning or domain-adaptive methods. The approach is a neuro-symbolic evolutionary search combining LLM-driven mutations/crossover with AST rewrite techniques to generate diverse, prover-effective formalizations. The focus is on search diversity and prover effectiveness, not domain-specific adaptation. This means it is concurrent work in autoformalization but takes an orthogonal approach to a domain-adaptive proposal.

**2. CAM-Bench (arXiv 2605.17255, May 2026)**

The paper is real. Full title: "CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean" by Wentao Long, Yunfei Zhang, Chenyi Li, Li Zhou, Chumin Sun, and Zaiwen Wen.

- It is indeed **1,000 Lean 4 proof targets** spanning optimization, numerical linear algebra, and numerical analysis.
- It is explicitly a **domain-specific autoformalization benchmark**, and the authors position it as addressing underrepresentation compared to existing benchmarks that "mainly focus on Olympiad-style problems and algebraic domains."
- A notable contribution is a dependency-recovery pipeline that reconstructs local textbook context needed to state each problem faithfully.
- This is **directly relevant** concurrent work to any domain-adaptive autoformalization proposal, as it provides a domain-specific benchmark in applied/computational mathematics.

**3. Other recent autoformalization work (May 2026) you may be missing:**

Several notable papers from May 2026:

- **MathAtlas** ([arXiv 2605.14061](https://arxiv.org/abs/2605.14061)) -- "A Benchmark for Autoformalization in the Wild." A large-scale benchmark with ~52k theorems/definitions/exercises from 103 graduate math textbooks, plus a dependency graph of ~178k relations. Best models achieve only 9.8% correctness on theorem statements and 2.6% on hardest subsets. Directly relevant as another domain-diverse autoformalization benchmark.

- **CktFormalizer** ([arXiv 2605.07782](https://arxiv.org/abs/2605.07782)) -- Autoformalization of natural language into circuit representations via a dependently-typed HDL embedded in Lean 4. Domain-specific (hardware), so tangentially relevant.

- **Verus-SpecGym** ([arXiv 2605.26457](https://arxiv.org/abs/2605.26457)) -- 581 tasks for specification autoformalization (informal programming problems to formal Verus/Rust specs). This is software specification rather than mathematical autoformalization, so less directly relevant.

- **AutoOR** ([arXiv 2604.16804](https://arxiv.org/abs/2604.16804), April 2026) -- Scalable post-training of LLMs to autoformalize operations research problems (linear, mixed-integer, non-linear optimization). Relevant as domain-specific autoformalization for OR.

From earlier in 2026 but also notable:

- **Cycle Consistency Fine-tuning for Lean4 Autoformalization** ([arXiv 2603.24372](https://arxiv.org/abs/2603.24372), March 2026).
- **Lean Atlas** ([arXiv 2604.16347](https://arxiv.org/abs/2604.16347), April 2026) -- Integrated proof environment for scalable human-AI collaborative formalization.

**Bottom line:** FormalEvolve's numbers check out but it is orthogonal (evolutionary search, not domain-adaptive). CAM-Bench is directly relevant concurrent work as a domain-specific Lean 4 benchmark in applied math. MathAtlas is also highly relevant as a large-scale graduate-level benchmark showing that performance degrades with dependency depth. AutoOR is relevant if your proposal covers optimization domains.

Sources:
- [FormalEvolve (2603.19828)](https://arxiv.org/abs/2603.19828)
- [CAM-Bench (2605.17255)](https://arxiv.org/abs/2605.17255)
- [MathAtlas (2605.14061)](https://arxiv.org/abs/2605.14061)
- [CktFormalizer (2605.07782)](https://arxiv.org/abs/2605.07782)
- [Verus-SpecGym (2605.26457)](https://arxiv.org/abs/2605.26457)
- [AutoOR (2604.16804)](https://arxiv.org/abs/2604.16804)
- [Cycle Consistency Fine-tuning (2603.24372)](https://arxiv.org/abs/2603.24372)
- [Lean Atlas (2604.16347)](https://arxiv.org/abs/2604.16347)

agentId: a5ccf4162ce7d6a3d (use SendMessage with to: 'a5ccf4162ce7d6a3d' to continue this agent)
&lt;usage>total_tokens: 15012
tool_uses: 7
duration_ms: 61714&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4557dff-7052-4601-ba85-5a2a708255d3",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "ddd14b55-b562-4947-a0be-9ad3e707d00b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two recent papers that might be relevant concurrent work to a domain-adaptive autoformalization proposal:\n\n1. FormalEvolve (arXiv 2603.19828, March 2026) — claimed to achieve 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet via evolutionary framework for autoformalization. Does this use any domain conditioning? What are the actual numbers?\n\n2. CAM-Bench (arXiv 2605.17255, May 2026) — claimed to be 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis. Is this a new domain-specific autoformalization benchmark?\n\n3. Also search for any other very recent autoformalization work from May 2026 that I might be missing. Search for \"autoformalization May 2026 arxiv\" and \"lean4 formalization 2026 new\".\n\nReport findings briefly.",
    "agentId": "a5ccf4162ce7d6a3d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on all three queries:\n\n---\n\n**1. FormalEvolve (arXiv 2603.19828, March 2026)**\n\nThe paper is real. Full title: \"FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization\" by Haijian Lu, Wei Wang, and Jing Liu.\n\n- The claimed numbers are **confirmed**: 58.0% semantic hit rate on CombiBench and 84.9% on ProofNet (both at 100 generator calls).\n- It does **not** use domain conditioning or domain-adaptive methods. The approach is a neuro-symbolic evolutionary search combining LLM-driven mutations/crossover with AST rewrite techniques to generate diverse, prover-effective formalizations. The focus is on search diversity and prover effectiveness, not domain-specific adaptation. This means it is concurrent work in autoformalization but takes an orthogonal approach to a domain-adaptive proposal.\n\n**2. CAM-Bench (arXiv 2605.17255, May 2026)**\n\nThe paper is real. Full title: \"CAM-Bench: A Benchmark for Computational and Applied Mathematics in Lean\" by Wentao Long, Yunfei Zhang, Chenyi Li, Li Zhou, Chumin Sun, and Zaiwen Wen.\n\n- It is indeed **1,000 Lean 4 proof targets** spanning optimization, numerical linear algebra, and numerical analysis.\n- It is explicitly a **domain-specific autoformalization benchmark**, and the authors position it as addressing underrepresentation compared to existing benchmarks that \"mainly focus on Olympiad-style problems and algebraic domains.\"\n- A notable contribution is a dependency-recovery pipeline that reconstructs local textbook context needed to state each problem faithfully.\n- This is **directly relevant** concurrent work to any domain-adaptive autoformalization proposal, as it provides a domain-specific benchmark in applied/computational mathematics.\n\n**3. Other recent autoformalization work (May 2026) you may be missing:**\n\nSeveral notable papers from May 2026:\n\n- **MathAtlas** ([arXiv 2605.14061](https://arxiv.org/abs/2605.14061)) -- \"A Benchmark for Autoformalization in the Wild.\" A large-scale benchmark with ~52k theorems/definitions/exercises from 103 graduate math textbooks, plus a dependency graph of ~178k relations. Best models achieve only 9.8% correctness on theorem statements and 2.6% on hardest subsets. Directly relevant as another domain-diverse autoformalization benchmark.\n\n- **CktFormalizer** ([arXiv 2605.07782](https://arxiv.org/abs/2605.07782)) -- Autoformalization of natural language into circuit representations via a dependently-typed HDL embedded in Lean 4. Domain-specific (hardware), so tangentially relevant.\n\n- **Verus-SpecGym** ([arXiv 2605.26457](https://arxiv.org/abs/2605.26457)) -- 581 tasks for specification autoformalization (informal programming problems to formal Verus/Rust specs). This is software specification rather than mathematical autoformalization, so less directly relevant.\n\n- **AutoOR** ([arXiv 2604.16804](https://arxiv.org/abs/2604.16804), April 2026) -- Scalable post-training of LLMs to autoformalize operations research problems (linear, mixed-integer, non-linear optimization). Relevant as domain-specific autoformalization for OR.\n\nFrom earlier in 2026 but also notable:\n\n- **Cycle Consistency Fine-tuning for Lean4 Autoformalization** ([arXiv 2603.24372](https://arxiv.org/abs/2603.24372), March 2026).\n- **Lean Atlas** ([arXiv 2604.16347](https://arxiv.org/abs/2604.16347), April 2026) -- Integrated proof environment for scalable human-AI collaborative formalization.\n\n**Bottom line:** FormalEvolve's numbers check out but it is orthogonal (evolutionary search, not domain-adaptive). CAM-Bench is directly relevant concurrent work as a domain-specific Lean 4 benchmark in applied math. MathAtlas is also highly relevant as a large-scale graduate-level benchmark showing that performance degrades with dependency depth. AutoOR is relevant if your proposal covers optimization domains.\n\nSources:\n- [FormalEvolve (2603.19828)](https://arxiv.org/abs/2603.19828)\n- [CAM-Bench (2605.17255)](https://arxiv.org/abs/2605.17255)\n- [MathAtlas (2605.14061)](https://arxiv.org/abs/2605.14061)\n- [CktFormalizer (2605.07782)](https://arxiv.org/abs/2605.07782)\n- [Verus-SpecGym (2605.26457)](https://arxiv.org/abs/2605.26457)\n- [AutoOR (2604.16804)](https://arxiv.org/abs/2604.16804)\n- [Cycle Consistency Fine-tuning (2603.24372)](https://arxiv.org/abs/2603.24372)\n- [Lean Atlas (2604.16347)](https://arxiv.org/abs/2604.16347)"
      }
    ],
    "totalDurationMs": 61714,
    "totalTokens": 15012,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1933,
      "cache_read_input_tokens": 11789,
      "output_tokens": 1289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1933
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1289,
          "cache_read_input_tokens": 11789,
          "cache_creation_input_tokens": 1933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1933,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "f4557dff-7052-4601-ba85-5a2a708255d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "ddd14b55-b562-4947-a0be-9ad3e707d00b",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Tool call

_source line 32 · 2026-05-28T14:59:13.196Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KVMWWr9i3DazMUAusXtErT`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify StepFun-Formalizer and Goedel-Formalizer-V2",
  "prompt": "I need to verify two key claims:\n\n1. StepFun-Formalizer (AAAI 2026) — claimed to achieve 40.5% BEq@1 on FormalMATH-Lite. Is this the current SOTA for open-source single-shot autoformalization? Search for \"StepFun-Formalizer AAAI 2026\" or \"StepFun autoformalization\".\n\n2. Goedel-Formalizer-V2-8B — claimed to be \"current SOTA open-source formalizer at this scale\" and \"fine-tuned from Qwen3-8B\". Search for \"Goedel-Formalizer-V2\" to verify:\n   - What model is it based on?\n   - What are its benchmark numbers?\n   - Is it truly the SOTA at 7-8B scale for autoformalization?\n\n3. Also check: has any new autoformalization model been released in April-May 2026 that might have surpassed these baselines?\n\nSearch for \"autoformalization leaderboard 2026\" and \"FormalMATH benchmark results 2026\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd14b55-b562-4947-a0be-9ad3e707d00b",
  "isSidechain": false,
  "requestId": "req_011CbVAX9M2WgwT9QQHawLm3",
  "type": "assistant",
  "uuid": "2c19f223-1995-4378-bdf1-5db2e69d640e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QoZhctCxYdp6Gc7SbvtepS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 45640,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1684,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 384,
          "cache_read_input_tokens": 45640,
          "cache_creation_input_tokens": 1684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1684
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

_source line 33 · 2026-05-28T15:01:16.833Z_

<details><summary>↩ Tool result · `toolu_01KVMWWr9i3DazMUAusXtErT`</summary>

```text
Now I have a comprehensive picture. Here is my analysis of the three claims:

---

## Claim 1: StepFun-Formalizer (AAAI 2026) -- 40.5% BEq@1 on FormalMATH-Lite

**Verified as accurate.** Key findings:

- The paper "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion" is confirmed as an **AAAI 2026 Oral** presentation ([AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40691)).
- StepFun-Formalizer-32B achieves **40.5% BEq@1 on FormalMATH-Lite** and **26.7% on ProverBench**, which the paper claims surpasses all prior general-purpose and specialized models.
- The 7B variant achieves **38.3% BEq@1** on FormalMATH-Lite.
- Both models are fine-tuned from **DeepSeek-R1-Distill-Qwen-7B/32B** (not a custom base).
- Compared baselines include Kimina-Autoformalizer-7B (35.1% BEq@1 on FormalMATH-Lite). Goedel-Formalizer-V2 was difficult to evaluate due to instruction-following limitations that prevented it from generating the required headers for BEq evaluation.

**Caveat on "SOTA" claim**: The FormalMATH leaderboard at SphereLab tracks *theorem proving* (not autoformalization), and those scores use different metrics (pass rates with sampling budgets). The 40.5% BEq@1 is specifically for the autoformalization task (translating natural language to formal Lean 4 statements), where it does appear to be the top single-shot open-source result as of the paper's publication. However, ATF-32B (Autoformalizer with Tool Feedback, arxiv 2510.06857) reports **94.51% Pass@1 consistency** on FormalMATH-Lite using a different metric, surpassing Goedel-V2-Formalizer-32B's 85.41%. These use a consistency metric rather than BEq, so they are not directly comparable.

---

## Claim 2: Goedel-Formalizer-V2-8B

**Partially verified.** Key findings:

- **Base model**: Confirmed -- it is **fine-tuned from Qwen3-8B** (specifically Qwen/Qwen3-8B), as stated on its [HuggingFace model card](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B).
- **Benchmark numbers**: On an internal eval set of 300 informal statements from Omni-MATH, the 8B model successfully translates **161/300 statements (53.7%)**, which ties with Kimina-formalizer-8B (also 161/300). The 32B variant translates 228/300.
- **"SOTA at this scale" claim**: This is **questionable**. On its own internal benchmark, Goedel-Formalizer-V2-8B ties with Kimina-formalizer-8B rather than surpassing it. On FormalMATH-Lite using BEq@1, StepFun-Formalizer-7B scores 38.3% vs Kimina-7B's 35.1%, and Goedel-V2-8B could not be properly evaluated on BEq due to instruction-following issues. Its model card does not explicitly claim SOTA; it emphasizes its novel "thinking before generating" capability. So the claim of being "current SOTA open-source formalizer at this scale" is not well-supported by available evidence.

---

## Claim 3: Any new autoformalization models from April-May 2026?

Several notable developments:

1. **MathAtlas** (arxiv 2605.14061, May 2026): A new *benchmark* (not a model) for autoformalization of graduate-level math (~52k theorems from 103 textbooks). Best models achieve only 9.8% correctness on theorem statements, showing the field still has far to go on harder content.

2. **Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning** (arxiv 2603.24372, March 2026): Fine-tunes Qwen3.5-2B with LoRA using cycle consistency rewards. This is a smaller-scale model.

3. **FormaRL** (arxiv 2508.18914): Uses RL without labeled data, achieving 4-6x improvement on Qwen2.5-Coder-7B-Instruct's pass@1.

4. **ATF (Autoformalizer with Tool Feedback)** (arxiv 2510.06857): The ATF-32B system achieves very strong results using tool feedback (Lean 4 compiler + multi-LLM consistency checking), substantially outperforming Goedel-V2-Formalizer-32B. However, it uses a different evaluation methodology (Pass@1 consistency) than StepFun-Formalizer's BEq@1.

**No model found in the April-May 2026 timeframe that clearly surpasses StepFun-Formalizer-32B's 40.5% BEq@1 on FormalMATH-Lite.** The field is active but results are fragmented across different metrics (BEq@1 vs. Pass@1 consistency vs. raw translation success counts), making direct comparisons difficult.

---

## Summary

| Claim | Verdict |
|-------|---------|
| StepFun-Formalizer: 40.5% BEq@1 on FormalMATH-Lite, AAAI 2026 | **Confirmed** |
| StepFun-Formalizer is SOTA for open-source single-shot autoformalization | **Likely true** for BEq@1 metric; ATF-32B may surpass it on consistency metrics |
| Goedel-Formalizer-V2-8B is fine-tuned from Qwen3-8B | **Confirmed** |
| Goedel-Formalizer-V2-8B is SOTA at 7-8B scale | **Not well-supported** -- ties with Kimina-8B on its own eval, and StepFun-7B outperforms Kimina-7B on BEq@1 |
| New model surpassing these baselines (Apr-May 2026) | **None found** on BEq@1 metric |

Sources:
- [StepFun-Formalizer AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40691)
- [StepFun-Formalizer arXiv](https://arxiv.org/abs/2508.04440)
- [StepFun-Formalizer full paper](https://arxiv.org/html/2508.04440v3)
- [StepFun-Formalizer GitHub](https://github.com/stepfun-ai/StepFun-Formalizer)
- [Goedel-Formalizer-V2-8B HuggingFace](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)
- [ATF (Autoformalizer with Tool Feedback)](https://arxiv.org/html/2510.06857v1)
- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735)
- [FormalMATH Leaderboard (SphereLab)](https://spherelab.ai/FormalMATH/)
- [MathAtlas Benchmark (May 2026)](https://arxiv.org/abs/2605.14061)
- [Cycle Consistency Autoformalization](https://arxiv.org/abs/2603.24372)

agentId: a17fa5248275cf9a8 (use SendMessage with to: 'a17fa5248275cf9a8' to continue this agent)
&lt;usage>total_tokens: 22855
tool_uses: 16
duration_ms: 123633&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c19f223-1995-4378-bdf1-5db2e69d640e",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "80eaf3ef-369b-4e22-80ea-94352a822698",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two key claims:\n\n1. StepFun-Formalizer (AAAI 2026) — claimed to achieve 40.5% BEq@1 on FormalMATH-Lite. Is this the current SOTA for open-source single-shot autoformalization? Search for \"StepFun-Formalizer AAAI 2026\" or \"StepFun autoformalization\".\n\n2. Goedel-Formalizer-V2-8B — claimed to be \"current SOTA open-source formalizer at this scale\" and \"fine-tuned from Qwen3-8B\". Search for \"Goedel-Formalizer-V2\" to verify:\n   - What model is it based on?\n   - What are its benchmark numbers?\n   - Is it truly the SOTA at 7-8B scale for autoformalization?\n\n3. Also check: has any new autoformalization model been released in April-May 2026 that might have surpassed these baselines?\n\nSearch for \"autoformalization leaderboard 2026\" and \"FormalMATH benchmark results 2026\".",
    "agentId": "a17fa5248275cf9a8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my analysis of the three claims:\n\n---\n\n## Claim 1: StepFun-Formalizer (AAAI 2026) -- 40.5% BEq@1 on FormalMATH-Lite\n\n**Verified as accurate.** Key findings:\n\n- The paper \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion\" is confirmed as an **AAAI 2026 Oral** presentation ([AAAI proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40691)).\n- StepFun-Formalizer-32B achieves **40.5% BEq@1 on FormalMATH-Lite** and **26.7% on ProverBench**, which the paper claims surpasses all prior general-purpose and specialized models.\n- The 7B variant achieves **38.3% BEq@1** on FormalMATH-Lite.\n- Both models are fine-tuned from **DeepSeek-R1-Distill-Qwen-7B/32B** (not a custom base).\n- Compared baselines include Kimina-Autoformalizer-7B (35.1% BEq@1 on FormalMATH-Lite). Goedel-Formalizer-V2 was difficult to evaluate due to instruction-following limitations that prevented it from generating the required headers for BEq evaluation.\n\n**Caveat on \"SOTA\" claim**: The FormalMATH leaderboard at SphereLab tracks *theorem proving* (not autoformalization), and those scores use different metrics (pass rates with sampling budgets). The 40.5% BEq@1 is specifically for the autoformalization task (translating natural language to formal Lean 4 statements), where it does appear to be the top single-shot open-source result as of the paper's publication. However, ATF-32B (Autoformalizer with Tool Feedback, arxiv 2510.06857) reports **94.51% Pass@1 consistency** on FormalMATH-Lite using a different metric, surpassing Goedel-V2-Formalizer-32B's 85.41%. These use a consistency metric rather than BEq, so they are not directly comparable.\n\n---\n\n## Claim 2: Goedel-Formalizer-V2-8B\n\n**Partially verified.** Key findings:\n\n- **Base model**: Confirmed -- it is **fine-tuned from Qwen3-8B** (specifically Qwen/Qwen3-8B), as stated on its [HuggingFace model card](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B).\n- **Benchmark numbers**: On an internal eval set of 300 informal statements from Omni-MATH, the 8B model successfully translates **161/300 statements (53.7%)**, which ties with Kimina-formalizer-8B (also 161/300). The 32B variant translates 228/300.\n- **\"SOTA at this scale\" claim**: This is **questionable**. On its own internal benchmark, Goedel-Formalizer-V2-8B ties with Kimina-formalizer-8B rather than surpassing it. On FormalMATH-Lite using BEq@1, StepFun-Formalizer-7B scores 38.3% vs Kimina-7B's 35.1%, and Goedel-V2-8B could not be properly evaluated on BEq due to instruction-following issues. Its model card does not explicitly claim SOTA; it emphasizes its novel \"thinking before generating\" capability. So the claim of being \"current SOTA open-source formalizer at this scale\" is not well-supported by available evidence.\n\n---\n\n## Claim 3: Any new autoformalization models from April-May 2026?\n\nSeveral notable developments:\n\n1. **MathAtlas** (arxiv 2605.14061, May 2026): A new *benchmark* (not a model) for autoformalization of graduate-level math (~52k theorems from 103 textbooks). Best models achieve only 9.8% correctness on theorem statements, showing the field still has far to go on harder content.\n\n2. **Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning** (arxiv 2603.24372, March 2026): Fine-tunes Qwen3.5-2B with LoRA using cycle consistency rewards. This is a smaller-scale model.\n\n3. **FormaRL** (arxiv 2508.18914): Uses RL without labeled data, achieving 4-6x improvement on Qwen2.5-Coder-7B-Instruct's pass@1.\n\n4. **ATF (Autoformalizer with Tool Feedback)** (arxiv 2510.06857): The ATF-32B system achieves very strong results using tool feedback (Lean 4 compiler + multi-LLM consistency checking), substantially outperforming Goedel-V2-Formalizer-32B. However, it uses a different evaluation methodology (Pass@1 consistency) than StepFun-Formalizer's BEq@1.\n\n**No model found in the April-May 2026 timeframe that clearly surpasses StepFun-Formalizer-32B's 40.5% BEq@1 on FormalMATH-Lite.** The field is active but results are fragmented across different metrics (BEq@1 vs. Pass@1 consistency vs. raw translation success counts), making direct comparisons difficult.\n\n---\n\n## Summary\n\n| Claim | Verdict |\n|-------|---------|\n| StepFun-Formalizer: 40.5% BEq@1 on FormalMATH-Lite, AAAI 2026 | **Confirmed** |\n| StepFun-Formalizer is SOTA for open-source single-shot autoformalization | **Likely true** for BEq@1 metric; ATF-32B may surpass it on consistency metrics |\n| Goedel-Formalizer-V2-8B is fine-tuned from Qwen3-8B | **Confirmed** |\n| Goedel-Formalizer-V2-8B is SOTA at 7-8B scale | **Not well-supported** -- ties with Kimina-8B on its own eval, and StepFun-7B outperforms Kimina-7B on BEq@1 |\n| New model surpassing these baselines (Apr-May 2026) | **None found** on BEq@1 metric |\n\nSources:\n- [StepFun-Formalizer AAAI Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40691)\n- [StepFun-Formalizer arXiv](https://arxiv.org/abs/2508.04440)\n- [StepFun-Formalizer full paper](https://arxiv.org/html/2508.04440v3)\n- [StepFun-Formalizer GitHub](https://github.com/stepfun-ai/StepFun-Formalizer)\n- [Goedel-Formalizer-V2-8B HuggingFace](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)\n- [ATF (Autoformalizer with Tool Feedback)](https://arxiv.org/html/2510.06857v1)\n- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735)\n- [FormalMATH Leaderboard (SphereLab)](https://spherelab.ai/FormalMATH/)\n- [MathAtlas Benchmark (May 2026)](https://arxiv.org/abs/2605.14061)\n- [Cycle Consistency Autoformalization](https://arxiv.org/abs/2603.24372)"
      }
    ],
    "totalDurationMs": 123633,
    "totalTokens": 22855,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 19708,
      "output_tokens": 2014,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2014,
          "cache_read_input_tokens": 19708,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "2c19f223-1995-4378-bdf1-5db2e69d640e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-28T15:01:16.839Z_

```json
{
  "parentUuid": "80eaf3ef-369b-4e22-80ea-94352a822698",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "908c39e1-da31-4a59-861c-b1d2282218ec",
  "timestamp": "2026-05-28T15:01:16.839Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 35 · 2026-05-28T15:03:17.523Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all my research findings and evaluate this proposal carefully.

## Summary of Verification Results

### Round 7 Issues — Were They Addressed?

1. **APRIL's existing error_type field** — RESOLVED. The proposal now explicitly acknowledges APRIL's existing error_type field (lme, mlme, thme, tme) and raw 'error' field throughout. The novelty is correctly framed as domain-stratified cross-tabulation + finer-grained taxonomy from raw compiler messages, not constructing error categories from scratch.

2. **LeanPremise/LeanHammer (ICLR 2026)** — RESOLVED. 

All five key claims have been verified: ICLR 2026 Oral designation, 79.4% relative improvement, project variation matching exactly, 82M parameters, and the accurate description as the first end-to-end domain-general hammer for Lean. It's properly positioned as premise selection for proving rather than autoformalization.

3. **KELPS** — RESOLVED. 

Added with verified claims: 88.9% pass@1 on MiniF2F, ICML 2025 AI4Math Workshop, Knowledge Equations framework, multi-language support, and 60k+ pairs across 6 topics.

4. **Venue timeline fixes** — RESOLVED.

AAAI 2027 is infeasible with only ~8 weeks until the July 28 deadline. ICML 2026 AI4Math paper deadline has already passed on May 25. ICLR 2027 is projected from historical patterns but not officially announced yet.

Now I'm noticing a critical distinction with the "Do LLMs Game Formalization?" paper from arXiv 2604.19459 — it's a VerifAI-2 Workshop paper at ICLR 2026 that introduces an error taxonomy for formalization faithfulness. But the errors it covers are semantic in nature (mistranslation, fabrication, omission, contradiction), which is fundamentally different from APRIL's Lean compiler error types (typeclass failures, coercion mismatches). These taxonomies operate at completely different layers.

The Goedel-Formalizer-V2-8B "current SOTA" claim needs scrutiny — it actually ties with Kimina-formalizer-8B on Omni-MATH (161/300), and StepFun-Formalizer-7B achieves 38.3% BEq@1 on FormalMATH-Lite which could be better. The claim isn't well-supported, though using it as a backbone for fine-tuning from Qwen3-8B is still a reasonable choice regardless.

I'm also checking CAM-Bench from May 2026. new domain-specific autoformalization benchmark (1,000 Lean targets in optimization, numerical linear algebra, numerical analysis) that's relevant but not cited. This is minor — it supports the proposal's motivation (domain-specific benchmarks are needed) but doesn't pre-empt the contribution.

4. **FormalEvolve (March 2026)** — Orthogonal approach (evolutionary search, not domain-adaptive). Not a novelty threat.

5. **MathAtlas** — Already cited in the proposal. Good.

### Scoring Assessment

**Novelty (4/5):**
- The domain-stratified cross-tabulation of APRIL's error types is genuinely novel — verified that no one has done this.
- Domain-conditioned retrieval reranking (per-problem dynamic conditioning on inferred subdomain) is differentiated from CRAMF (concept-level), DRIFT (decomposition-level), Lean Search v2 (domain-agnostic), and IndiMathBench (static context).
- The leave-one-domain-out evaluation protocol across ≥5 categories is novel — ConNF tests only 1 OOD domain.
- Shebzukhov (2026) reports domain-stratified aggregate scores but no error type analysis — the proposal's narrowed claim holds up.
- The "Do LLMs Game Formalization?" taxonomy addresses semantic faithfulness, not compiler errors — no direct overlap.
- Domain adaptation itself is well-established in ML, so applying it to autoformalization is a natural extension rather than a conceptual leap.

**Feasibility (4/5):**
- 200 H100-hours is tight but workable given the streamlined pipeline without domain-routed LoRA or multiple adapters.
- APRIL's explicit path field makes... The approach is well-structured with three clear stages and a thorough ablation design, refined through seven rounds of iteration. The error taxonomy could be genuinely useful if the hypotheses hold, though the domain-conditioned retrieval feels incremental, and there's a real risk that simpler domain prompting alone captures most of the gains — the leave-one-domain-out evaluation is a solid methodological contribution, but the practical impact may be limited if the delta between approaches turns out modest.

Recalculating the overall score: novelty and feasibility both merit 4/5, clarity is strong despite the verbosity, and the proposal demonstrates genuine responsiveness to feedback, though the impact ceiling remains uncertain.

The core weakness is that domain adaptation itself isn't novel—it's a well-established technique—and the error taxonomy, while useful, may not fundamentally reshape the field. The real risk is that simple domain-aware prompting could capture most of the gains without the full framework.

A few citations are missing that should be acknowledged: the semantic faithfulness error taxonomy work, the Goedel-Formalizer comparison that's less clear-cut than claimed, and the recent benchmark that motivated this direction. These don't undermine the core contribution but represent gaps in positioning.

After multiple rounds of refinement, the proposal has genuinely addressed nearly every substantive concern—the references check out, the differentiation from prior work is clear, the hypotheses are pre-registered, and the ablation plan is thorough. The remaining issues are truly minor. Reconsidering the scores: novelty should be 4/5 for the specific combination of domain-stratified taxonomy plus dynamic per-problem retrieval, which hasn't been done before. Feasibility is also 4/5—the plan is realistic with clear success metrics. Clarity stays around 3.5/5 because while the detail is appreciated, the verbosity works against it.

The real tension is impact at 3.5/5—the error taxonomy itself is valuable, but the downstream gains are uncertain, making this solidly incremental rather than transformative. That puts the average at 3.75, just below the 4.0 threshold for passing. Given this is round 8 of 10 and the issues are genuinely minor, I'm wondering if bumping clarity to 4.0 to reflect the thoroughness despite verbosity would justify a pass, though that still only gets to 3.875.

Actually, reconsidering the impact score—this proposal introduces the first domain-stratified error taxonomy with pre-registered hypotheses, the first systematic multi-domain rotation evaluation protocol, tests dynamic domain-conditioned retrieval, includes six surgical ablations with relevant baselines, and has clear contingency planning for negative results. For a venue like ICLR 2027, that's a solid contribution. Maybe impact deserves 3.75 instead of 3.5, which would bring the average to 3.8—still below 4.0, but the gap is narrower and the work is genuinely novel in its evaluation methodology.

The "Do LLMs Game Formalization?" paper doesn't threaten the novelty here since it addresses a different problem—semantic faithfulness versus compilation errors—and CAM-Bench actually supports the proposal's direction. The Goedel-Formalizer-V2-8B "SOTA" claim is a minor issue about backbone choice; whether it's strictly first or second at 8B scale doesn't undermine the approach itself.

My honest assessment: Novelty 4/5, Feasibility 4/5, Clarity 3.5/5 (the proposal is still 2-3x longer than it needs to be), Impact 3.5/5 (incremental with baseline fear test risk). That averages to 3.75, which calls for a revise decision with targeted feedback on condensation, citing the complementary work properly, fixing the SOTA claim, and strengthening the contingency argument.

But I'm second-guessing myself here. This is round 8 of 10, and the previous round's issues were all minor—the proposal addressed them. Now I'm finding similarly minor problems: citation gaps, a small inaccuracy, stylistic verbosity. At some point, does "revise" become unfair when there are no critical or moderate issues, just accumulated minor ones? The core question is whether these genuinely push the score below 4.0 or if I'm being too harsh on what's fundamentally a solid proposal with a real contribution.

Looking at what's actually here: the proposal identifies a genuine, well-documented gap in autoformalization, proposes a reasonable domain-conditioned solution, has a comprehensive evaluation plan, and has addressed all prior feedback. The novelty claims are carefully narrowed and accurate. For ICLR 2027, this would be a respectable submission—not groundbreaking, but solid work. I think the honest scores are Novelty 4/5, Feasibility 4/5, Clarity 4/5 (the thoroughness serves clarity in a proposal context), and Impact 3.5/5 for its incremental nature, averaging 3.875. Still below 4.0, but I need to be clear about whether that's the right call.

The impact limitation is real—the error taxonomy is useful but not field-changing, the domain-conditioned retrieval is a natural extension, and the leave-one-domain-out protocol is solid but not transformative. That said, the proposal already honestly self-assesses as "solid" rather than "exciting," which is appropriate. For a solid paper, the question should be whether it meets the acceptance bar for the target venue, not whether it's transformative. Looking at this for ICLR 2027: it has clear novelty in the domain-stratified error taxonomy, comprehensive evaluation with leave-one-domain-out testing across six domains, and addresses a real gap in the field. I think this actually clears the acceptance threshold.

Let me score it properly: novelty is 4/5 with a genuine, well-differentiated contribution; feasibility is 4/5 with realistic, concrete steps; clarity is 4/5 despite some verbosity that would compress in the actual paper; impact is 3.5/5 because it's useful but incremental. That averages to 3.875, which is just below the 4.0 passing threshold. The remaining issues are genuinely minor though—another revision might just add length without substance. I'm not confident 3.875 is close enough to justify moving forward without changes.

Actually, looking at this more carefully, the core contributions are substantial: a domain-stratified error taxonomy with pre-registered hypotheses, per-problem dynamic domain-conditioned retrieval for autoformalization, and a systematic multi-domain rotation evaluation protocol. These are genuine firsts in the space, and the ICML 2026 workshops validate real community interest in this direction. The error taxonomy alone has value independent of downstream improvements. Maybe impact deserves 3.75 instead, which would push the average to 3.9375—still below 4.0, but closer. For impact to genuinely hit 4.0, I'd need to see something that makes this feel like a clear advance rather than a solid incremental step.

Looking at the honest assessment: this is a well-executed, useful contribution with real potential if the hypotheses pan out. That lands squarely in the 3.5-3.75 range for impact. My final scores are novelty 4, feasibility 4, clarity 4, impact 3.5, averaging 3.875—which means revise, but with very specific feedback on what could elevate the impact dimension.

Wait, I should reconsider clarity too. For a research proposal rather than a finished paper, this level of detail is actually appropriate. The approach itself is crystal clear—three distinct stages, sharp differentiation from related work, pre-registered hypotheses, comprehensive ablations planned. The thoroughness reflects the proposal's strength, not a weakness.

So clarity stays at 4. On impact, the "Do LLMs Game Formalization?" work actually strengthens the argument here. That paper's semantic faithfulness taxonomy and this proposal's compiler error taxonomy are complementary, revealing a genuine gap in error characterization that this work fills. That's real but incremental, so 3.5 is fair.

The verdict remains revise with minor issues. At 3.875, a small push on impact could get this over 4.0. I need to identify what's missing: the "Do LLMs Game Formalization?" paper isn't cited, and it's directly relevant to the proposal's positioning.

Also, the Goedel-Formalizer-V2-8B claim needs softening—it's not actually the sole SOTA at this scale since Kimina-formalizer-8B matches it at 161/300 on Omni-MATH, and StepFun-Formalizer-7B shows competitive performance too. Calling it "competitive at this scale" or "among the leading approaches" would be more accurate.

CAM-Bench is another concurrent benchmark worth citing—it offers 1,000 Lean targets for computational and applied math, which directly supports the proposal's motivation. The bigger concern is that the proposal is quite verbose for a 9-page venue; the core sections need substantial condensation to fit the actual submission format, though that's more of an editing challenge than a conceptual issue.

Looking at the scoring rules, I'm at 3.875 average with no critical flaws—just minor issues. The question is whether these are fixable enough to warrant revision or if the work is fundamentally sound despite them.

Since the average falls just below the 4.0 threshold for a pass, I should recommend revision, but I'll frame the feedback as targeted and constructive given how close this is to acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "908c39e1-da31-4a59-861c-b1d2282218ec",
  "isSidechain": false,
  "requestId": "req_011CbVAgzcwb8tYceRrsJS35",
  "type": "assistant",
  "uuid": "b02d78b9-9283-4282-bda2-ddf2eb8e0459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017stxNn7j4XwZpMyjuVHkJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 47324,
      "output_tokens": 5265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5265,
          "cache_read_input_tokens": 47324,
          "cache_creation_input_tokens": 2576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2576
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

_source line 36 · 2026-05-28T15:03:17.525Z_

Now let me do one final check on a potential new competitor paper I found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b02d78b9-9283-4282-bda2-ddf2eb8e0459",
  "isSidechain": false,
  "requestId": "req_011CbVAgzcwb8tYceRrsJS35",
  "type": "assistant",
  "uuid": "765c92f2-5f58-41d9-8e10-25a24934027e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017stxNn7j4XwZpMyjuVHkJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 47324,
      "output_tokens": 5265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5265,
          "cache_read_input_tokens": 47324,
          "cache_creation_input_tokens": 2576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2576
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

_source line 37 · 2026-05-28T15:03:24.455Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ebx5ohiNMQtpHkPmiySY64`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify \"Do LLMs Game Formalization\" details",
  "prompt": "I need to understand the relationship between the paper \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\" (arXiv 2604.19459) and a proposal to create a domain-stratified error taxonomy based on Lean COMPILER errors (typeclass failures, coercion mismatches, etc.).\n\nSpecifically:\n1. Does arXiv 2604.19459 classify errors by mathematical subdomain (e.g., topology vs algebra errors)? Or only by error type?\n2. Does it analyze Lean compiler errors at all, or only semantic/logical faithfulness errors?\n3. Could a reviewer of the proposal argue that 2604.19459 already provides an autoformalization error taxonomy, making the proposal's taxonomy contribution less novel?\n\nPlease fetch https://arxiv.org/abs/2604.19459 and check the abstract/intro carefully.\n\nAlso search for: any other paper that provides a domain-stratified (by math subdomain) analysis of autoformalization compiler errors. This is the key novelty claim I need to verify hasn't been done."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "765c92f2-5f58-41d9-8e10-25a24934027e",
  "isSidechain": false,
  "requestId": "req_011CbVAgzcwb8tYceRrsJS35",
  "type": "assistant",
  "uuid": "8ec4bce9-5fe9-43f2-a77e-f33e2b5382ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017stxNn7j4XwZpMyjuVHkJT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 47324,
      "output_tokens": 5265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5265,
          "cache_read_input_tokens": 47324,
          "cache_creation_input_tokens": 2576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2576
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "8ec4bce9-5fe9-43f2-a77e-f33e2b5382ca",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Tool result

_source line 40 · 2026-05-28T15:05:58.860Z_

<details><summary>↩ Tool result · `toolu_01Ebx5ohiNMQtpHkPmiySY64`</summary>

```text
I now have a thorough picture. Here is my analysis:

---

## Analysis of arXiv 2604.19459 and the Novelty of a Domain-Stratified Lean Compiler Error Taxonomy

### Question 1: Does arXiv 2604.19459 classify errors by mathematical subdomain or only by error type?

**Only by error type.** The paper identifies exactly two modes of unfaithfulness:
- **GPT-5: Axiom fabrication** during proof generation (a reactive fallback, detectable via cross-stage comparison)
- **DeepSeek-R1: Premise mistranslation** during formalization (internally consistent, evades detection)

There is no breakdown by mathematical subdomain. The dataset consists of 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval) -- these are logical reasoning problems, not mathematics problems spanning algebra, topology, number theory, etc. The paper does not stratify results by mathematical domain at all.

### Question 2: Does it analyze Lean compiler errors?

**No.** The paper explicitly focuses on **semantic/logical faithfulness errors** -- cases where the Lean code compiles successfully (87-99% compilation rates) but the formalization does not faithfully represent the original natural-language problem. It does not analyze or taxonomize Lean compiler errors such as typeclass resolution failures, coercion mismatches, universe level errors, or elaboration failures. The compiler is used only as a pass/fail gate; the paper's contribution is about what goes wrong *despite* successful compilation.

### Question 3: Could a reviewer argue 2604.19459 already provides this taxonomy?

**No, this would be a weak argument.** The paper and the proposed taxonomy are addressing fundamentally different problems:

| Dimension | arXiv 2604.19459 | Proposed Taxonomy |
|---|---|---|
| **Error level** | Semantic/logical faithfulness | Lean compiler errors |
| **Domain** | First-order logic (FOLIO, Multi-LogiEval) | Mathematical subdomains (algebra, topology, etc.) |
| **Error categories** | 2 types (axiom fabrication, premise mistranslation) | Compiler-level categories (typeclass failures, coercion mismatches, universe errors, etc.) |
| **Stratification** | None by domain | By mathematical subdomain |
| **What it measures** | Whether valid Lean code is *faithful* to intent | Whether formalization attempts *compile at all* and why they fail |

A reviewer citing 2604.19459 as prior art for your taxonomy would be conflating semantic faithfulness analysis with compiler error analysis. They are complementary, not overlapping.

### Key Finding: No Existing Domain-Stratified Lean Compiler Error Taxonomy

After searching extensively, I found **no paper that provides a domain-stratified (by mathematical subdomain) taxonomy of autoformalization compiler errors**. Here is what exists in the neighborhood:

- **ProofNet** (arXiv 2302.12433): Reports typecheck rates for autoformalization across domains (analysis, algebra, topology) but does not taxonomize *which compiler errors* occur or how they differ by domain.
- **Process-Driven Autoformalization / FormL4** (arXiv 2406.01940): Uses Lean 4 compiler feedback iteratively but does not classify error types or stratify by domain.
- **APRIL** (arXiv 2602.02990): Creates 260K supervised tuples of Lean proof failures paired with compiler diagnostics and repairs, but does not taxonomize the error types or stratify by mathematical domain.
- **CriticLean** (arXiv 2507.06181): Focuses on semantic fidelity evaluation, not compiler error classification; mentions "domain diversity" but provides no domain-stratified error analysis.
- **Autoformalization Survey** (arXiv 2505.23486): Discusses mathematical subdomains and evaluation metrics but contains **no error taxonomy** and implicitly reveals this as a gap in the literature.
- **IndiMathBench** (arXiv 2512.00997): Notes gaps between syntactic validity and semantic correctness but provides no error taxonomy.
- **Reliable Evaluation for Statement Autoformalization** (arXiv 2406.07222): Focuses on evaluation metrics (BEq+), not error classification.

### Bottom Line

The specific combination you describe -- a taxonomy of **Lean compiler errors** (typeclass failures, coercion mismatches, universe errors, elaboration failures, etc.) **stratified by mathematical subdomain** (topology vs. algebra vs. number theory, etc.) -- appears to be genuinely novel. No paper I found does both of these things together. arXiv 2604.19459 in particular is not a threat to this novelty claim: it operates at a completely different level (semantic faithfulness of *compilable* code, in a first-order logic domain, with only two error categories).

Sources:
- [arXiv 2604.19459 - Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)
- [arXiv 2505.23486 - Autoformalization in the Era of LLMs: A Survey](https://arxiv.org/html/2505.23486v1)
- [arXiv 2302.12433 - ProofNet](https://ar5iv.labs.arxiv.org/html/2302.12433)
- [arXiv 2406.01940 - Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)
- [arXiv 2602.02990 - APRIL: Automated Proof Repair in Lean](https://arxiv.org/abs/2602.02990)
- [arXiv 2507.06181 - CriticLean](https://arxiv.org/abs/2507.06181)
- [arXiv 2512.00997 - IndiMathBench](https://arxiv.org/abs/2512.00997)
- [arXiv 2406.07222 - Reliable Evaluation for Statement Autoformalization](https://arxiv.org/abs/2406.07222)
- [arXiv 2604.07455 - Munkres' Topology Autoformalized in Isabelle/HOL](https://arxiv.org/abs/2604.07455)
- [arXiv 2406.06555 - Evaluation Benchmark for Autoformalization in Lean4](https://arxiv.org/abs/2406.06555)

agentId: a636f72e661c3e32a (use SendMessage with to: 'a636f72e661c3e32a' to continue this agent)
&lt;usage>total_tokens: 24994
tool_uses: 20
duration_ms: 154400&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ec4bce9-5fe9-43f2-a77e-f33e2b5382ca",
  "isSidechain": false,
  "promptId": "64037af3-396c-4dc0-bb4e-67d28e723cb4",
  "type": "user",
  "uuid": "dd165a66-aab8-4c31-9d99-13f4ebef09f9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the relationship between the paper \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\" (arXiv 2604.19459) and a proposal to create a domain-stratified error taxonomy based on Lean COMPILER errors (typeclass failures, coercion mismatches, etc.).\n\nSpecifically:\n1. Does arXiv 2604.19459 classify errors by mathematical subdomain (e.g., topology vs algebra errors)? Or only by error type?\n2. Does it analyze Lean compiler errors at all, or only semantic/logical faithfulness errors?\n3. Could a reviewer of the proposal argue that 2604.19459 already provides an autoformalization error taxonomy, making the proposal's taxonomy contribution less novel?\n\nPlease fetch https://arxiv.org/abs/2604.19459 and check the abstract/intro carefully.\n\nAlso search for: any other paper that provides a domain-stratified (by math subdomain) analysis of autoformalization compiler errors. This is the key novelty claim I need to verify hasn't been done.",
    "agentId": "a636f72e661c3e32a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a thorough picture. Here is my analysis:\n\n---\n\n## Analysis of arXiv 2604.19459 and the Novelty of a Domain-Stratified Lean Compiler Error Taxonomy\n\n### Question 1: Does arXiv 2604.19459 classify errors by mathematical subdomain or only by error type?\n\n**Only by error type.** The paper identifies exactly two modes of unfaithfulness:\n- **GPT-5: Axiom fabrication** during proof generation (a reactive fallback, detectable via cross-stage comparison)\n- **DeepSeek-R1: Premise mistranslation** during formalization (internally consistent, evades detection)\n\nThere is no breakdown by mathematical subdomain. The dataset consists of 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval) -- these are logical reasoning problems, not mathematics problems spanning algebra, topology, number theory, etc. The paper does not stratify results by mathematical domain at all.\n\n### Question 2: Does it analyze Lean compiler errors?\n\n**No.** The paper explicitly focuses on **semantic/logical faithfulness errors** -- cases where the Lean code compiles successfully (87-99% compilation rates) but the formalization does not faithfully represent the original natural-language problem. It does not analyze or taxonomize Lean compiler errors such as typeclass resolution failures, coercion mismatches, universe level errors, or elaboration failures. The compiler is used only as a pass/fail gate; the paper's contribution is about what goes wrong *despite* successful compilation.\n\n### Question 3: Could a reviewer argue 2604.19459 already provides this taxonomy?\n\n**No, this would be a weak argument.** The paper and the proposed taxonomy are addressing fundamentally different problems:\n\n| Dimension | arXiv 2604.19459 | Proposed Taxonomy |\n|---|---|---|\n| **Error level** | Semantic/logical faithfulness | Lean compiler errors |\n| **Domain** | First-order logic (FOLIO, Multi-LogiEval) | Mathematical subdomains (algebra, topology, etc.) |\n| **Error categories** | 2 types (axiom fabrication, premise mistranslation) | Compiler-level categories (typeclass failures, coercion mismatches, universe errors, etc.) |\n| **Stratification** | None by domain | By mathematical subdomain |\n| **What it measures** | Whether valid Lean code is *faithful* to intent | Whether formalization attempts *compile at all* and why they fail |\n\nA reviewer citing 2604.19459 as prior art for your taxonomy would be conflating semantic faithfulness analysis with compiler error analysis. They are complementary, not overlapping.\n\n### Key Finding: No Existing Domain-Stratified Lean Compiler Error Taxonomy\n\nAfter searching extensively, I found **no paper that provides a domain-stratified (by mathematical subdomain) taxonomy of autoformalization compiler errors**. Here is what exists in the neighborhood:\n\n- **ProofNet** (arXiv 2302.12433): Reports typecheck rates for autoformalization across domains (analysis, algebra, topology) but does not taxonomize *which compiler errors* occur or how they differ by domain.\n- **Process-Driven Autoformalization / FormL4** (arXiv 2406.01940): Uses Lean 4 compiler feedback iteratively but does not classify error types or stratify by domain.\n- **APRIL** (arXiv 2602.02990): Creates 260K supervised tuples of Lean proof failures paired with compiler diagnostics and repairs, but does not taxonomize the error types or stratify by mathematical domain.\n- **CriticLean** (arXiv 2507.06181): Focuses on semantic fidelity evaluation, not compiler error classification; mentions \"domain diversity\" but provides no domain-stratified error analysis.\n- **Autoformalization Survey** (arXiv 2505.23486): Discusses mathematical subdomains and evaluation metrics but contains **no error taxonomy** and implicitly reveals this as a gap in the literature.\n- **IndiMathBench** (arXiv 2512.00997): Notes gaps between syntactic validity and semantic correctness but provides no error taxonomy.\n- **Reliable Evaluation for Statement Autoformalization** (arXiv 2406.07222): Focuses on evaluation metrics (BEq+), not error classification.\n\n### Bottom Line\n\nThe specific combination you describe -- a taxonomy of **Lean compiler errors** (typeclass failures, coercion mismatches, universe errors, elaboration failures, etc.) **stratified by mathematical subdomain** (topology vs. algebra vs. number theory, etc.) -- appears to be genuinely novel. No paper I found does both of these things together. arXiv 2604.19459 in particular is not a threat to this novelty claim: it operates at a completely different level (semantic faithfulness of *compilable* code, in a first-order logic domain, with only two error categories).\n\nSources:\n- [arXiv 2604.19459 - Do LLMs Game Formalization?](https://arxiv.org/abs/2604.19459)\n- [arXiv 2505.23486 - Autoformalization in the Era of LLMs: A Survey](https://arxiv.org/html/2505.23486v1)\n- [arXiv 2302.12433 - ProofNet](https://ar5iv.labs.arxiv.org/html/2302.12433)\n- [arXiv 2406.01940 - Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)\n- [arXiv 2602.02990 - APRIL: Automated Proof Repair in Lean](https://arxiv.org/abs/2602.02990)\n- [arXiv 2507.06181 - CriticLean](https://arxiv.org/abs/2507.06181)\n- [arXiv 2512.00997 - IndiMathBench](https://arxiv.org/abs/2512.00997)\n- [arXiv 2406.07222 - Reliable Evaluation for Statement Autoformalization](https://arxiv.org/abs/2406.07222)\n- [arXiv 2604.07455 - Munkres' Topology Autoformalized in Isabelle/HOL](https://arxiv.org/abs/2604.07455)\n- [arXiv 2406.06555 - Evaluation Benchmark for Autoformalization in Lean4](https://arxiv.org/abs/2406.06555)"
      }
    ],
    "totalDurationMs": 154400,
    "totalTokens": 24994,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 22244,
      "output_tokens": 1560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1560,
          "cache_read_input_tokens": 22244,
          "cache_creation_input_tokens": 1189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1189,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "8ec4bce9-5fe9-43f2-a77e-f33e2b5382ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-28T15:06:42.586Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me finalize my review.

## Summary of All Verification Results

### Round 7 Issues — All Resolved:
1. ✅ APRIL error_type field acknowledged throughout
2. ✅ LeanPremise/LeanHammer added (all claims verified accurate)
3. ✅ KELPS added (all claims verified accurate)
4. ✅ Venue timelines fixed (AAAI 2027 infeasible, ICML passed, ICLR 2027 estimated)

### New Issues Found (All Minor):


The "Do LLMs Game Formalization?" paper isn't a threat—it addresses semantic faithfulness rather than compiler errors, so it's complementary work that doesn't affect novelty. The Goedel-Formalizer-V2-8B SOTA claim needs softening since it ties with Kimina-8B and StepFun-Formalizer-7B might actually perform better on some metrics. CAM-Bench from May 2026 is relevant to the domain but...

Actually, let me verify the core novelties: the domain-stratified Lean compiler error taxonomy is genuinely new, the per-problem dynamic domain-conditioned retrieval for autoformalization hasn't been done before, and the systematic multi-domain rotation evaluation across five or more categories is also novel. Shebzukhov only provides aggregate scores without error type breakdown, and CRAMF's domain signals work at the concept level rather than conditioning on problem-level subdomains. So I'm looking at three solid firsts here—novelty scores a 4/5, and feasibility also comes in at 4/5 with concrete implementation paths.

The clarity is strong despite some verbosity, earning another 4/5, but impact is the sticking point at 3.5/5. The error taxonomy might influence future work, the domain-conditioned retrieval faces baseline test uncertainty, and while the evaluation protocol could become standard, that's still incremental. Averaging to 3.875 puts this below the 4.0 threshold, so the verdict is to revise with only minor fixes needed—the proposal is mature and well-researched, but impact concerns prevent a clean pass.

After eight rounds, the fixable issues are straightforward: the "SOTA" claim just needs rewording to "competitive," the CAM-Bench citation can be added, and the optional "Do LLMs Game Formalization?" reference doesn't threaten novelty. The real challenge is the impact argument itself, which is structural—no revision fully resolves whether domain conditioning genuinely outperforms simpler baselines. Given we're at round 8 of 10 with all substantial concerns addressed across seven iterations, I should flag these minor points clearly while acknowledging how close this is to passing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd165a66-aab8-4c31-9d99-13f4ebef09f9",
  "isSidechain": false,
  "requestId": "req_011CbVB3nZEgAkLk7NWe4GPQ",
  "type": "assistant",
  "uuid": "1815c2f1-83b1-490c-873d-15d4b78a30eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148qr4KqrxqjY7v77faqZvk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 49900,
      "output_tokens": 2693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2693,
          "cache_read_input_tokens": 49900,
          "cache_creation_input_tokens": 6904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6904
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

_source line 42 · 2026-05-28T15:07:23.436Z_

Now I have comprehensive verification results across all dimensions. Let me synthesize my findings into a final assessment.

## Verification Summary

**All Round 7 issues verified as resolved:**
- APRIL error_type field: ✅ Acknowledged throughout (lme/mlme/thme/tme confirmed)
- LeanPremise/LeanHammer: ✅ All 5 claims independently verified (ICLR 2026 Oral, 79.4% relative, exact project variation numbers, 82M params, "first end-to-end domain-general hammer")
- KELPS: ✅ All claims verified (88.9% pass@1, ICML 2025 AI4Math Workshop, Knowledge Equations, multi-language, 60k+ pairs)
- Venue timelines: ✅ AAAI 2027 deadlines confirmed (Jul 21/28, 2026), ICML paper deadline correctly noted as passed, ICLR 2027 correctly flagged as estimated

**Key novelty claim verified:** No existing paper provides a domain-stratified (by mathematical subdomain) taxonomy of Lean compiler errors. The closest work — "Do LLMs Game Formalization?" (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) — operates at a completely different layer (semantic faithfulness of compilable code, not compiler errors), with no subdomain stratification.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "Three verified 'firsts': domain-stratified compiler error taxonomy (confirmed no prior work), per-problem dynamic domain-conditioned retrieval (clearly differentiated from CRAMF concept-level, DRIFT decomposition-level, LeanSearch v2 domain-agnostic, IndiMathBench static), and systematic multi-domain rotation evaluation (≥5 categories vs. ConNF's single-domain OOD). All novelty claims accurately narrowed after 7 revision rounds."},
    "feasibility": {"score": 4, "rationale": "200 H100-hours realistic for simplified 3-stage pipeline. APRIL's explicit 'path' field confirmed as primary domain signal. Herald path parsing acknowledged as engineering effort. Pre-registered quantitative hypotheses (JSD > 0.3, prediction accuracy ≥ 70%) are testable. ICLR 2027 timeline (~16 weeks for 11-week plan) provides buffer. All datasets/models verified available."},
    "clarity": {"score": 4, "rationale": "Extremely thorough proposal with well-structured 3-stage approach, 6 surgical ablations, clear differentiation from every relevant prior work. Revision notes demonstrate exceptional responsiveness across 7 rounds. Main weakness is excessive verbosity — the core_problem and opportunity sections read like a survey chapter rather than a research proposal, which will need condensation for a 9-page submission."},
    "impact": {"score": 3.5, "rationale": "The error taxonomy is a genuinely useful contribution if hypotheses hold, and the leave-one-domain-out protocol fills a real evaluation gap. However, the contribution remains incremental — domain adaptation is a well-established ML technique being applied to a new task. The baseline fear test risk persists: if IndiMathBench-style naive domain prompting (ablation e) captures 80%+ of semantic correctness gains, the multi-stage pipeline adds marginal engineering value. The honest 'solid' self-assessment is accurate."}
  },
  "issues": [
    "MINOR: Goedel-Formalizer-V2-8B characterized as 'current SOTA open-source formalizer at this scale' but evidence shows it TIES with Kimina-formalizer-8B (161/300 on Omni-MATH internal eval) and StepFun-Formalizer-7B achieves 38.3% BEq@1 on FormalMATH-Lite — the 'SOTA' claim should be softened to 'competitive open-source formalizer at this scale' or 'among the strongest open-source formalizers'",
    "MINOR: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop at ICLR 2026) introduces a complementary formalization error taxonomy (semantic faithfulness: mistranslation, fabrication, omission, contradiction) operating at the post-compilation layer. While fundamentally different from the proposal's compiler-error-based taxonomy (no overlap in scope), citing it as complementary work strengthens the argument that error characterization is under-explored and positions the two taxonomies as addressing different layers of the error stack (pre-compilation vs. post-compilation)",
    "MINOR: CAM-Bench (arXiv 2605.17255, May 2026) — 1,000 Lean proof targets in optimization, numerical linear algebra, and numerical analysis — is a relevant concurrent domain-specific benchmark supporting the motivation that domain-specific evaluation matters, but is not cited",
    "MINOR: Impact argument remains the binding constraint — the baseline fear test is honestly acknowledged but not resolved. The proposal correctly notes that if ablation (e) captures 80%+ of gains, 'we report this honestly as evidence that the simple approach extends to semantic correctness,' but this outcome would significantly weaken the paper's system contribution, leaving the error taxonomy as the primary value. The proposal would benefit from a stronger argument for why domain-conditioned retrieval should outperform static context (e.g., problems that span multiple domains, problems whose domain classification is non-obvious, retrieval precision at high K values)"
  ],
  "feedback": "The proposal has matured exceptionally across 7 revision rounds — all reference claims independently verified accurate, novelty claims appropriately narrowed, and prior issues comprehensively addressed. Average score is 3.875, just below the 4.0 threshold, with impact (3.5) as the binding constraint. Three small fixes for Round 9: (1) **Soften the Goedel-Formalizer-V2-8B 'SOTA' claim** — it ties with Kimina-8B and StepFun-7B may outperform on BEq@1; say 'competitive at this scale' instead. (2) **Cite 'Do LLMs Game Formalization?' (arXiv 2604.19459) as complementary** — its semantic faithfulness taxonomy (post-compilation errors) vs. your compiler error taxonomy (pre-compilation errors) together demonstrate that error characterization at BOTH layers is under-explored, strengthening your argument for the taxonomy contribution. (3) **Strengthen the impact argument for domain-conditioned retrieval over static context**: articulate specific scenarios where dynamic per-problem conditioning should outperform IndiMathBench-style static context — e.g., cross-domain problems (a number theory result requiring analysis-level typeclasses), ambiguous domain assignment (problems at domain boundaries), and retrieval precision degradation at higher K values where domain filtering reduces noise. If you can make a convincing case that these scenarios are common enough to matter, the pipeline contribution gains weight beyond the taxonomy.",
  "reason": "All prior issues resolved, all claims verified accurate, remaining issues genuinely minor — but impact score (3.5) keeps average at 3.875, below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1815c2f1-83b1-490c-873d-15d4b78a30eb",
  "isSidechain": false,
  "requestId": "req_011CbVB3nZEgAkLk7NWe4GPQ",
  "type": "assistant",
  "uuid": "a23e250f-1110-4ef2-ab77-7e47d06fb795",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148qr4KqrxqjY7v77faqZvk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6904,
      "cache_read_input_tokens": 49900,
      "output_tokens": 2693,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2693,
          "cache_read_input_tokens": 49900,
          "cache_creation_input_tokens": 6904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6904
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "a23e250f-1110-4ef2-ab77-7e47d06fb795",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-Adaptive Autoformalization with Subdomain-Stratified Error Analysis",
  "sessionId": "805a9b1b-751a-472f-be96-3da9ad6bf0e5"
}
```

---
