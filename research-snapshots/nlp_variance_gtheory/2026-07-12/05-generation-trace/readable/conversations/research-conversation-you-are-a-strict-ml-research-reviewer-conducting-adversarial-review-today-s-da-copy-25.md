# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-28 (UTC).** Your job: indep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/9c44962f-53ef-4dda-a205-11ae79612bf5.jsonl`
- **Structured JSON:** [`c9779b691be49787e103.json`](../../sessions/c9/c9779b691be49787e103.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T13:02:18.344Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T13:02:18.344Z",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-28 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: AAAI 2026\nTrack: AI for Science / Knowledge Representation and Reasoning\n\nDirection: Build the first domain-adaptive autoformalization pipeline that conditions formalization, retrieval, and repair strategies on mathematical subdomain (algebra, topology, analysis, number theory). The core insight is that autoformalization errors are not uniform — topology formalizations fail on typeclass instances while algebra formalizations fail on coercion chains — and domain-aware systems can exploit these patterns. Evaluate on cross-domain generalization: train on 3 domains, test on the held-out 4th.\n\nSeed Papers:\n- VeriSoftBench (arXiv 2602.18307, Feb 2026) — Proves Mathlib-trained provers fail on out-of-domain verification; motivates domain adaptation\n- APRIL (arXiv 2602.02990, Feb 2026) — 260k repair tuples enabling domain-stratified error analysis; no existing stratification\n- Herald (ICLR 2025) — 580k NL-formal pairs with Mathlib4 module provenance; enables domain labeling via module hierarchy\n- Autoformalizer with Tool Feedback (arXiv 2510.06857, Oct 2025) — Integrates repair into training but domain-agnostic; our domain-aware version is the delta\n- StepFun-Formalizer (AAAI 2026) — Current SOTA single-shot autoformalization; general-purpose baseline to beat on per-domain metrics\n- 130k Topology (arXiv 2601.03298, Jan 2026) — Domain-specific success via manual effort; motivates systematic domain adaptation\n- REAL-Prover (arXiv 2505.20613, May 2025) — Domain-aware retrieval helps proving; we extend retrieval to formalization\n- DDR (arXiv 2511.11990, Nov 2025) — Retrieval-augmented autoformalization via dependency generation; domain-agnostic baseline\n\nKnown Gaps:\n- No autoformalization system adapts its pipeline to mathematical subdomain; all treat algebra and topology identically despite different error distributions\n- APRIL's 260k repair tuples have never been stratified by domain — the domain-specific error taxonomy is uncharacterized\n- Retrieval-augmented autoformalization (DDR) retrieves domain-agnostic dependencies; domain-conditioned retrieval (Mathlib module-aware) is untested\n\nTheoretical Anchor: Domain shift theory from transfer learning — the distribution of formal language constructs (typeclasses, coercions, tactic vocabularies) differs measurably across Mathlib4 module hierarchies, creating a domain adaptation problem that standard domain-agnostic models underperform on. VeriSoftBench empirically confirms this for software domains; we extend the analysis to mathematical subdomains.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~70-80 H100-hours)\n- Must use open-source models only (Qwen2.5-7B or Goedel-Prover-V2-8B as base)\n- Evaluate on ≥3 benchmarks: miniF2F v2, ProofNet (domain-stratified), VeriSoftBench\n- Release all artifacts: model weights, domain-stratified APRIL analysis, evaluation scripts\n\nQuality Self-Checks:\n- [x] Core insight: Autoformalization errors cluster by mathematical domain, and domain-conditioned pipelines can exploit this structure.\n- [x] Why not obvious: Prior work treats autoformalization as domain-agnostic; domain adaptation requires Mathlib module hierarchy knowledge and domain-stratified training data that only became available with Herald (2025) and APRIL (2026).\n- [ ] Baseline fear test: RISK — a domain-agnostic model with more repair iterations could match 80% of the gain. Mitigation: the cross-domain generalization experiment (train on 3, test on 4th) specifically isolates domain adaptation's contribution vs. more compute.\n- [x] Information exploited: Mathlib4's module hierarchy as domain labels + APRIL's repair tuples stratified by error type and domain — information that exists in the data but no system currently uses.\n\nAvoid:\n- Framing as 'proof search improvement' — this is about formalization quality, not proving power\n- Competing on miniF2F leaderboard numbers — the contribution is per-domain reliability, not aggregate SOTA\n- Simple cycle consistency (claimed by 3 papers in 2025-2026)\n- Pure data scaling (diminishing returns per Goedel-Prover-V2)\n- Ignoring Autoformalizer with Tool Feedback as prior art — must clearly differentiate via domain-awareness**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-28?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy\",\n  \"core_problem\": \"Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, and LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem. The 260k repair tuples in APRIL have never been stratified by mathematical subdomain despite containing implicit domain structure. Can we build the first autoformalization pipeline that systematically conditions its retrieval ranking and prompting signals on inferred mathematical subdomain — beyond concept-level disambiguation and decomposition — and does this problem-level domain conditioning yield measurable improvements, especially on currently catastrophic domains where even advanced retrieval alone cannot close the gap?\",\n  \"opportunity\": \"Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs tagged with Mathlib4 module paths enabling automatic formalization-level domain labeling; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels (e.g., 'Algebra → Intermediate Algebra → Functional Equations') and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples that have never been stratified by domain; (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; and (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization with Qwen3-Embedding/Reranker-8B — but its success demonstrates that retrieval quality alone, even at high levels, does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide direct evidence that domain-specialized problems require fundamentally different handling. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. Recent textbook-scale formalizations — M2F (Feb 2026) on real analysis and convex analysis, and Automatic Textbook Formalization (Gloeckle et al., Apr 2026) on algebraic combinatorics — demonstrate that different mathematical domains can be formalized at scale but use uniform methods with no domain-specific conditioning. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for retrieval conditioning can close the domain gap in ways that concept-level disambiguation and decomposition alone cannot.\",\n  \"landscape\": \"Current SOTA autoformalization is domain-agnostic: StepFun-Formalizer-32B achieves 40.5% BEq@1 on FormalMATH-Lite and 26.7% on ProverBench via knowledge-reasoning fusion (AAAI 2026); FormaRL achieves 26.15% on ProofNet using GRPO with compiler+consistency rewards on Qwen2.5-Coder-7B-Instruct with only 859 unlabeled examples (COLM 2025); ATLAS achieves SOTA via expert iteration with concept-first synthesis from Mathlib (NeurIPS 2025); ProofBridge (ICLR 2026) achieves +31.14% semantic correctness via cross-modal joint embeddings for retrieval-augmented formalization. All report aggregate metrics only — no paper breaks results down by mathematical subdomain or conditions its pipeline on domain. **Retrieval-augmented approaches represent a rich and rapidly evolving space, but all operate domain-agnostically**: (a) DDR (ICLR 2025 Spotlight) introduced Direct Dependency Retrieval and the ConNF benchmark (961 OOD pairs from New Foundations set theory) — ConNF tests generalization to a single held-out domain but does not perform systematic multi-domain rotation across mathematical subdomain categories; (b) CRAMF (ICLR 2026) stores Mathlib module paths (θ_p) per definition and performs contextual query augmentation with LLM-generated 'domain- and application-level signals' — but these signals are terminological interpretations designed to disambiguate polysemous concepts (e.g., 'neighborhood' in topological vs. metric spaces), not to identify the mathematical subdomain of the input problem and condition retrieval ranking accordingly; CRAMF's bge-reranker-v2-m3 scores semantic similarity between query interpretations and definition annotations without boosting same-subdomain definitions; (c) **DRIFT (ICLR 2026 Poster)** decomposes informal statements into ~5.8 atomic sub-queries for targeted concept-level retrieval using a finetuned BGE-M3 encoder, nearly doubling F1 on ProofNet (27.68 vs. 13.77 baseline) and achieving BEq+@10 improvements of 37–42% on ConNF — DRIFT's sub-query decomposition operates at the concept level (breaking one statement into individual mathematical concept queries), which is orthogonal to our problem-level approach (classifying the entire problem's mathematical subdomain and boosting all same-subdomain definitions); (d) **LeanSearch v2 (May 2026)** achieves SOTA single-query premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed Mathlib informalization with Qwen3-Embedding-8B and Qwen3-Reranker-8B, and its reasoning mode achieves 46.1% Recall@10 on global premise retrieval — LeanSearch v2 demonstrates that sophisticated domain-agnostic retrieval can be very strong, but its success addresses retrieval quality for theorem proving (finding relevant lemmas given a proof state), not the formalization accuracy gap across mathematical subdomains that MSC-180 documents; even with perfect premise retrieval, a formalizer that does not know topology problems disproportionately fail on typeclass instance resolution will not generate better topology formalizations. **Aria (ICLR 2026)** achieves 68.5% on ProofNet and 44.0% on FATE-X via Graph-of-Thought recursive decomposition with AriaScorer (term-level Mathlib grounding via Herald) — critically, Aria achieves 42.9% on homological conjectures while ALL baselines score 0%, providing the strongest published evidence that certain mathematical subdomains are catastrophically underserved by domain-agnostic approaches; yet Aria itself uses no domain conditioning, suggesting its Graph-of-Thought decomposition partially compensates for domain bias through deeper dependency analysis but cannot systematically address it. **Domain-specific autoformalization exists but is fragmented**: SITA (AAAI 2026) introduces a structure-to-instance paradigm using Lean's typeclass mechanism to instantiate abstract mathematical structures into concrete settings, evaluated on 42 optimization problems — but this is a specific pattern (abstract→concrete instantiation) applied to a single domain, not a general pipeline conditioned on subdomain identity. The 130k Topology project (Jan 2026) required manual human-LLM interaction for a single domain. M2F (Feb 2026) formalizes 479 pages of real analysis and convex analysis textbooks into 153k lines of Lean code, and Automatic Textbook Formalization (Gloeckle et al., Apr 2026) formalizes a 500-page algebraic combinatorics textbook into 130k lines — both demonstrate that different domains can be formalized at scale but use uniform methods, providing implicit evidence that domain-specific formalization is tractable while offering no systematic domain conditioning. Repair approaches (APRIL, ReForm) apply uniform repair strategies regardless of error origin. FineLeanCorpus (CriticLean, 2025) provides 286k verified entries (509k total) with 3-tier hierarchical problem-level domain labels and difficulty scores, but these classify mathematical content, not formalization-level dependencies. MSC-180 (Dec 2025) evaluated provers across 60 MSC2020 branches finding CV values 4–6× above statistical high-variability thresholds. MathAtlas (May 2026) introduces a 52k-entity benchmark spanning 87 math areas with 178k dependency relations but uses domain labels only for evaluation. Cross-domain evaluation via systematic multi-domain rotation (leave-one-domain-out across ≥4 subdomain categories) has never been performed for autoformalization — ConNF's single-domain OOD test is a valuable but limited precedent.\",\n  \"inspired_by\": \"Field gaps #1 (no system conditions retrieval ranking on inferred mathematical subdomain — CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, but none conditions reranking on input subdomain), #2 (APRIL 260k tuples never domain-stratified), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with Herald module-path labels + FineLeanCorpus topic labels) and #2 (domain-stratified APRIL error taxonomy as hypothesis-driven analysis); Aria's homological conjectures results (42.9% vs. 0%) as direct motivation that domain-agnostic approaches catastrophically fail on specialized domains even when using sophisticated retrieval; contrast with single-domain approaches (SITA, M2F, 130k Topology, Automatic Textbook Formalization) that demonstrate domain-specific formalization is tractable but offer no systematic multi-domain conditioning; reviewer preferences for surgical ablations including naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.\",\n  \"approach\": \"We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (user-specified model family; Qwen2.5-Coder-7B-Instruct used as additional baseline for FormaRL comparison). **Stage 1 — Domain-Specific Error Taxonomy (PRIMARY CONTRIBUTION)**: We train a lightweight domain classifier on Herald's 580k NL-formal pairs using Mathlib4 module paths as supervision, producing 5 major subdomain clusters (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). We cross-reference with FineLeanCorpus's 286k verified entries with problem-level hierarchical labels to measure correlation and divergence between mathematical topic and formalization-level domain. We then stratify APRIL's 260k repair tuples by predicted subdomain and construct the first systematic domain-specific error taxonomy for autoformalization. **Standalone evaluation criteria for the error taxonomy**: (a) **Inter-domain error distribution divergence** — we compute Jensen-Shannon divergence between error-type distributions across domain pairs (e.g., topology vs. algebra error distributions) and test the hypothesis that error patterns cluster systematically by domain; statistical significance via permutation tests; (b) **Predictive power** — given a new formalization attempt's predicted domain, can the taxonomy predict which error types it will encounter? We measure this via a held-out error prediction task: train a simple classifier on domain → error-type distributions, evaluate prediction accuracy on unseen formalizations; (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization on held-out examples from that domain. This error taxonomy is valuable independent of any downstream pipeline delta — it provides the first empirical characterization of how autoformalization fails differently across mathematical subdomains, offering actionable guidance for domain-specific approaches (including SITA-like paradigms, textbook-scale formalizations like M2F, and future domain-specialized systems). **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF's contextual query augmentation disambiguates polysemous concepts one at a time (concept-level); DRIFT decomposes statements into atomic sub-queries for targeted per-concept retrieval (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval via hierarchy-informed informalization (retrieval quality). Our reranker adds an orthogonal signal: given that the input problem is classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts or decompose the statement into sub-queries. We explicitly address the LeanSearch v2 challenge: domain-agnostic retrieval can achieve high recall on well-represented domains, but the domain gap documented by MSC-180 manifests in formalization accuracy across domains, not retrieval recall within domains. Our hypothesis is that domain conditioning helps most where domain-agnostic methods already retrieve relevant premises but the formalizer fails because it lacks domain context — e.g., retrieving the right topology definitions but failing to apply them correctly because the formalizer doesn't know topology-specific patterns. The reranker is trained on Herald+CRAMF data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline to test whether domain conditioning provides gains beyond what superior domain-agnostic retrieval already captures. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **naive domain prompting baseline** — simply prepending the predicted domain label to the input with zero pipeline engineering — to test whether trivial domain signals capture the majority of gains, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If naive prompting captures 80%+ of gains, we report this honestly as evidence that simple domain awareness is surprisingly powerful; if the full pipeline significantly outperforms, it validates the engineering investment. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier: 10h; APRIL stratification inference + error taxonomy construction: 8h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including naive domain prompting + LeanSearch v2 comparison: 37h)\",\n      \"timeline\": \"16 weeks (3w domain taxonomy + APRIL error analysis + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)\",\n      \"estimated_gpu_cost\": \"$500 (H100 at ~$2.50/hr average via RunPod/Lambda)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200 H100-hours\",\n      \"timeline\": \"12 weeks (Claude accelerates domain taxonomy design, APRIL error pattern classification, retrieval pipeline code, and ablation analysis)\",\n      \"claude_api_cost\": \"$300 (domain taxonomy extraction from Herald+FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)\",\n      \"estimated_gpu_cost\": \"$500\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200 H100-hours (domain classifier: 10h; APRIL stratification + error taxonomy: 8h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including naive prompting + LeanSearch v2 baseline: 35h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)\",\n      \"timeline\": \"10 weeks\",\n      \"claude_api_cost\": \"$450 (automated domain taxonomy iteration, repair pattern mining, hyperparameter selection, result analysis and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500\",\n      \"speed_bottleneck\": \"Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)\",\n    \"AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only 8 weeks from today, STRETCH if Stage 1 error analysis yields strong early results; could submit error taxonomy + domain-conditioned retrieval as core contributions)\",\n    \"NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Herald: A Natural Language Annotated Lean 4 Dataset (ICLR 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach / DDR + ConNF benchmark (ICLR 2025 Spotlight)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization + FineLeanCorpus 286k verified entries (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (arXiv 2025)\",\n    \"MSC-180: A Benchmark for Automated Formal Theorem Proving from Mathematical Subject Classification (arXiv 2025)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"SITA: A Framework for Structure-to-Instance Theorem Autoformalization (AAAI 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)\",\n    \"Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)\",\n    \"M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)\",\n    \"Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)\",\n    \"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)\",\n    \"LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)\"\n  ],\n  \"description\": \"We propose the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain, operating at the problem level rather than individual concept disambiguation or decomposition. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT) treat all domains identically, yet MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) score 0% — the strongest published evidence that domain-agnostic approaches catastrophically fail on specialized mathematical subdomains. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT decomposes statements into ~5.8 atomic sub-queries for targeted per-concept retrieval (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed informalization (retrieval quality). None conditions on the mathematical subdomain of the input problem. We contribute two primary results: (1) **The first domain-specific error taxonomy for autoformalization** — stratifying APRIL's 260k repair tuples across 5 mathematical subdomain clusters, evaluated via inter-domain error distribution divergence (Jensen-Shannon divergence + permutation tests), error-type prediction accuracy on held-out formalizations, and actionable per-domain mitigation recommendations; this standalone empirical contribution characterizes how autoformalization fails differently across domains and provides guidance independent of any downstream delta. (2) **Problem-level domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), and domain-agnostic retrieval quality (LeanSearch v2). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 mathematical subdomain categories), extending ConNF's single-domain OOD paradigm. Six surgical ablations include naive domain prompting (zero-engineering baseline) and LeanSearch v2 retrieval replacement (testing whether superior domain-agnostic retrieval subsumes domain conditioning). The entire pipeline fits within 200 H100-hours.\",\n  \"project_name\": \"domain_adapt_autoformal\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_compute_budget\": \"RESOLVED (Round 1): Reduced from ~600 A100-hours to ~200 H100-hours by dropping domain-routed LoRA adapters and GRPO.\",\n    \"round1_issue_2_venue_mismatch\": \"RESOLVED (Round 1): Primary target ICLR 2027, AAAI 2027 as stretch.\",\n    \"round1_issue_3_model_choice\": \"RESOLVED (Round 1): Goedel-Formalizer-V2-8B backbone with Qwen2.5-Coder-7B-Instruct as FormaRL comparison baseline.\",\n    \"round1_issue_4_FineLeanCorpus\": \"RESOLVED (Round 1): Added FineLeanCorpus with problem-level vs. formalization-level label distinction.\",\n    \"round1_issue_5_MSC180\": \"RESOLVED (Round 1): Added MSC-180 as motivation and evaluation benchmark.\",\n    \"round1_issue_6_circular_reasoning\": \"RESOLVED (Round 1): Error pattern claims reframed as hypotheses.\",\n    \"round1_issue_7_VeriSoftBench\": \"RESOLVED (Round 1): Replaced with MSC-180 and MathAtlas.\",\n    \"round1_issue_8_pipeline_complexity\": \"RESOLVED (Round 1): Simplified to 3 stages, 5 clusters, single LoRA.\",\n    \"round1_issue_9_baseline_fear_test\": \"RESOLVED (Round 1): Matched-compute baseline, per-domain analysis, error taxonomy as standalone contribution.\",\n    \"round2_issue_1_CRAMF_differentiation\": \"RESOLVED (Round 2): Deep-dived into CRAMF's actual technical implementation — concept-level disambiguation (CRAMF) vs. problem-level subdomain conditioning (ours) explicitly distinguished.\",\n    \"round2_issue_2_SITA\": \"RESOLVED (Round 2): Added SITA to landscape with explicit differentiation.\",\n    \"round2_issue_3_impact_argument\": \"RESOLVED (Round 2): Added naive domain prompting baseline and elevated error taxonomy.\",\n    \"round2_issue_4_FineLeanCorpus_size\": \"RESOLVED (Round 2): Corrected to '286k verified entries (509k total)' throughout.\",\n    \"round2_issue_5_ICLR2027_deadline\": \"MITIGATED (Round 2): Estimated Sep 19/24 with contingency.\",\n    \"round2_issue_6_M2F_RepoProver\": \"RESOLVED (Round 2): Added M2F and Automatic Textbook Formalization to landscape.\",\n    \"round3_issue_1_DRIFT_Aria\": \"RESOLVED: Added DRIFT (ICLR 2026 Poster) to landscape with full technical differentiation. DRIFT decomposes informal statements into ~5.8 atomic sub-queries using finetuned BGE-M3 encoder for targeted concept-level retrieval, nearly doubling F1 on ProofNet (27.68 vs. 13.77) and achieving BEq+@10 improvements of 37–42% on ConNF. Explicitly differentiated: DRIFT's sub-query decomposition is concept-level (breaking one statement into individual concept queries); our approach is problem-level (classifying the entire problem's subdomain and boosting all same-subdomain definitions). These are orthogonal and complementary. Added Aria (ICLR 2026) with full performance details — Aria's 42.9% on homological conjectures vs. 0% for ALL baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) now serves as the strongest published evidence for domain bias in our motivation. Aria uses Graph-of-Thought recursive decomposition with AriaScorer (term-level Mathlib grounding via Herald) but no domain conditioning, suggesting deeper dependency analysis partially compensates but cannot systematically address domain bias.\",\n    \"round3_issue_2_ConNF_claim\": \"RESOLVED: Narrowed 'first leave-one-domain-out evaluation protocol' to 'first systematic multi-domain rotation evaluation protocol across ≥5 mathematical subdomain categories.' ConNF (DDR, ICLR 2025 Spotlight) explicitly cited as testing single-domain OOD (New Foundations set theory, 961 pairs from con-nf library with 1,348 formal objects) — a valuable but limited precedent that tests generalization to ONE held-out specialized domain. Our protocol extends this to systematic rotation across all 5 subdomain clusters, which ConNF does not attempt. ConNF also added as an additional evaluation benchmark.\",\n    \"round3_issue_3_error_taxonomy_elevation\": \"RESOLVED: Error taxonomy elevated to unambiguous primary contribution with three standalone evaluation criteria: (a) inter-domain error distribution divergence measured via Jensen-Shannon divergence between domain pairs with statistical significance via permutation tests; (b) predictive power — held-out error prediction task training a classifier on domain→error-type distributions; (c) actionable recommendations per domain — ranked top-5 error types per subdomain cluster with concrete mitigation strategies, evaluated by improvement on held-out domain examples. This makes the paper valuable even if the downstream formalization delta is modest — the taxonomy is the first empirical characterization of how autoformalization fails differently across mathematical subdomains.\",\n    \"round3_issue_4_compute_trim\": \"RESOLVED: Trimmed auto_research from 210 to 200 H100-hours by reducing LoRA fine-tuning from 80h to 78h and evaluation from 50h to 48h (using more aggressive Lean4 compilation batching and reducing redundant re-compilation across ablation conditions). All three modes now ≤200 H100-hours.\",\n    \"round3_issue_5_LeanSearch_v2\": \"RESOLVED: Added LeanSearch v2 (May 2026, arXiv 2605.13137) comprehensively. LeanSearch v2 achieves SOTA single-query premise retrieval (nDCG@10 = 0.623 vs. 0.533 for LeanFinder) without domain-specific fine-tuning, using Qwen3-Embedding-8B and Qwen3-Reranker-8B with hierarchy-informed Mathlib informalization. Reasoning mode achieves 46.1% Recall@10 on global premise retrieval. Downstream proof success: 20% vs. 16% (next best). Explicitly addressed the challenge to our motivation: LeanSearch v2 demonstrates that domain-agnostic retrieval can be very strong, but its success addresses retrieval quality (finding relevant lemmas), not the formalization accuracy gap across subdomains documented by MSC-180. Even with perfect retrieval, a formalizer lacking domain-specific error awareness will fail differently across domains. Added ablation (f) — LeanSearch v2 retrieval baseline — to directly test whether superior domain-agnostic retrieval subsumes domain conditioning.\"\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Compute budget violation — estimates ~600 A100-hours (~300-400 H100-equivalent), 1.5-2x over user's hard constraint of ≤200 H100-hours\", \"CRITICAL: Venue mismatch — user requested 'AAAI 2026' (deadline August 2025, already past); Generator silently shifted to AAAI 2027 (July 2026). With today's date May 28, 2026, the July 28 deadline is only 8 weeks away, making even the 6-week auto_research timeline razor-thin\", \"CRITICAL: Model choice violation — user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' but Generator uses 'Qwen3-8B'\", \"Missing critical reference: CriticLean + FineLeanCorpus (509k entries with hierarchical domain labels like 'Algebra -> Intermediate Algebra -> Functional Equations' and difficulty scores) — this dataset already provides domain-stratified autoformalization data, undermining the claim that 'domain-specific error taxonomy is uncharacterized'\", \"Missing reference: MSC-180 benchmark (arXiv 2512.18256) evaluates theorem provers across 60 mathematical branches via MSC2020 classification with coefficient of variation metrics — directly relevant to domain bias analysis\", \"Circular reasoning in motivation: specific error patterns ('topology fails on typeclass instances, algebra fails on coercion chains') are stated as known facts to motivate the work, but discovering these patterns is actually a claimed contribution of the work\", \"VeriSoftBench evaluates software verification proofs, not mathematical autoformalization — including it as an autoformalization benchmark is misleading and doesn't match the paper's scope\", \"The 4-stage pipeline (classifier + APRIL stratification + domain retrieval + domain-conditioned GRPO with 15-subdomain LoRA routing) has excessive engineering complexity for the compute and timeline constraints\", \"Baseline fear test risk: acknowledged but not adequately mitigated — the leave-one-domain-out experiment isolates domain adaptation contribution, but if the delta is small (e.g., 2-3 percentage points), the paper's contribution becomes marginal\"]\nFeedback: To revise into a passable submission: (1) **Drastically simplify the pipeline** to fit within 200 H100-hours — drop domain-routed LoRA adapters (the most compute-hungry component) and focus on domain-conditioned retrieval + domain-stratified error analysis as the core contributions, which are cheaper and more novel; (2) **Use the user-specified models** (Qwen2.5-7B or Goedel-Prover-V2-8B); (3) **Cite and differentiate from FineLeanCorpus** — acknowledge its domain labels exist but argue your Mathlib module-path-based domain taxonomy captures formalization-specific structure (typeclass/coercion patterns) that FineLeanCorpus's problem-level labels do not; (4) **Reframe error pattern claims as hypotheses** to be empirically validated, not established facts; (5) **Replace VeriSoftBench** with FormalMATH-stratified evaluation or MathAtlas — both are mathematical benchmarks with domain structure; (6) **Target ICLR 2027** (estimated September 2026) instead of AAAI 2027 to get an extra ~8 weeks of development time; (7) **Reduce subdomain granularity** from 15 to 4-5 major domains (algebra, topology, analysis, number theory, combinatorics) to keep the experimental matrix manageable within budget; (8) **Strengthen the baseline comparison** by including a domain-agnostic model with matched compute (same number of repair iterations) as a control to convincingly demonstrate domain-conditioning adds value beyond more compute.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MODERATE: CRAMF differentiation insufficient — CRAMF explicitly mentions 'contextual query augmentation with domain- and application-level signals' and stores Mathlib module paths (θ_p) per definition. The proposal claims CRAMF 'never conditions retrieval reranking on mathematical subdomain' but doesn't directly acknowledge or rebut CRAMF's existing domain signals. A reviewer familiar with CRAMF will ask: 'How is your domain conditioning different from CRAMF's domain-level contextual query augmentation?'\", \"MODERATE: SITA (AAAI 2026) not cited — SITA demonstrates domain-specific autoformalization via structure-to-instance approach using Lean's typeclass mechanism, evaluated on 42 optimization problems. While a different paradigm (abstract structure instantiation vs. subdomain conditioning), it contradicts the 'first domain-specific autoformalization' framing and should be discussed as related work.\", \"MODERATE: Impact uncertainty — the matched-compute baseline mitigates the baseline fear test but doesn't address it: if domain-agnostic models with domain context in the prompt (a trivially simpler approach than the full pipeline) capture 80%+ of the gain, the multi-stage pipeline adds marginal value. The paper needs a stronger argument for why the full pipeline (classifier + domain reranking + domain error context) is necessary vs. simply adding 'This is a topology problem' to the prompt.\", \"MINOR: FineLeanCorpus size inaccuracy — claims '509k entries' but verified data shows 285,957 fully verified entries. The 509k figure may include unverified entries, but using it without qualification is misleading.\", \"MINOR: ICLR 2027 primary target is speculative — deadline not officially announced. If the actual deadline is earlier (e.g., August 2026), the 16-week timeline becomes infeasible.\", \"MINOR: M2F (Feb 2026) and RepoProver (Apr 2026) not cited — both perform domain-specific autoformalization at textbook scale (real analysis, convex analysis, algebraic combinatorics), providing evidence that different mathematical domains require different formalization strategies, supporting the proposal's motivation.\"]\nFeedback: The proposal has addressed all Round 1 critical issues well (compute, venue, model, VeriSoftBench, circular reasoning, pipeline simplification). The remaining issues are moderate rather than critical. To reach pass threshold: (1) **Sharpen CRAMF differentiation**: Explicitly acknowledge CRAMF's 'domain- and application-level signals' in contextual query augmentation and its stored module paths (θ_p), then argue precisely why this falls short of systematic subdomain conditioning — e.g., CRAMF's domain signals are used for disambiguating polysemous concepts, not for conditioning the retrieval ranking on the input's mathematical subdomain. (2) **Cite and differentiate from SITA (AAAI 2026)**: Acknowledge it as domain-specific autoformalization via structure-to-instance approach, but clarify your work conditions the general-purpose pipeline on subdomain identity, whereas SITA targets a specific mathematical pattern (abstract-to-concrete instantiation) in a single domain. (3) **Strengthen the impact argument**: Add an explicit ablation comparing 'naive domain prompting' (just prepending domain label to input, zero engineering) vs. full pipeline with domain-conditioned retrieval and error context. If the full pipeline doesn't significantly outperform naive domain prompting, the paper's contribution is weaker. Frame the error taxonomy as a co-equal contribution, not a byproduct. (4) **Fix FineLeanCorpus size**: Use '286k fully verified entries (509k total)' for accuracy. (5) **Add M2F and SITA to landscape discussion** as evidence that domain-specific approaches exist but are either single-domain (SITA, M2F) or manual (130k Topology), motivating your systematic multi-domain approach.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE: Several relevant ICLR 2026 systems missing from landscape — DRIFT (ICLR 2026 Poster) performs concept-level decomposition for targeted retrieval and nearly doubles F1 on ProofNet; its sub-query decomposition is conceptually related to domain-conditioned retrieval and must be differentiated. Aria (ICLR 2026) achieves 68.5% on ProofNet and 42.9% on homological conjectures (all other baselines 0%) but is domain-agnostic — these per-domain results directly support the proposal's domain bias motivation and should appear in the landscape analysis.\", \"MODERATE: ConNF benchmark (961 OOD informal-formal pairs, from DDR/ICLR 2025 Spotlight) specifically tests cross-domain generalization in autoformalization. The proposal claims to introduce 'the first leave-one-domain-out evaluation protocol for autoformalization' but does not cite ConNF. While ConNF tests a single OOD domain (New Foundations set theory) rather than systematic multi-domain rotation, the claim needs to be narrowed or ConNF explicitly differentiated.\", \"MODERATE: Impact argument remains the weakest link — the proposal correctly identifies the risk that naive domain prompting captures 80%+ of gains, but the framing still positions the multi-stage pipeline as the main system contribution. If the error taxonomy is the safety net, it should be promoted to unambiguous primary contribution with clearer standalone evaluation criteria (e.g., inter-domain error pattern correlation metrics, actionable recommendations per domain).\", \"MINOR: Compute budget slightly exceeds constraint — auto_research mode estimates 210 H100-hours vs. the user's hard ≤200 H100-hour cap. Need to either trim 10 hours (e.g., reduce ablation sweep scope) or justify the overage.\", \"MINOR: LeanSearch v2 (May 2026) achieves SOTA premise retrieval 'without domain-specific fine-tuning' — this is directly relevant since it suggests domain-agnostic retrieval can be very strong, potentially challenging the motivation for domain-conditioned retrieval. Should be cited and its implications discussed.\"]\nFeedback: The proposal has matured significantly across three rounds and is close to passing. All Round 2 issues were addressed well, particularly the CRAMF differentiation (now technically precise and verified accurate). To reach pass threshold: (1) **Add DRIFT, ConNF, LeanSearch v2, and Aria's per-domain results** to the landscape — DRIFT and LeanSearch v2 are recent strong retrieval baselines; ConNF is the existing OOD autoformalization benchmark; Aria's per-domain gaps (42.9% on homological conjectures vs. 0% for all baselines) directly support the domain bias motivation. (2) **Narrow the 'first leave-one-domain-out' claim** — ConNF already tests OOD generalization, so specify 'first systematic multi-domain rotation evaluation' across ≥4 mathematical subdomain categories. (3) **Elevate the error taxonomy to unambiguous primary contribution** — define standalone evaluation criteria: (a) inter-domain error pattern clustering metrics (e.g., how distinct are topology vs. algebra error distributions?), (b) predictive power of domain-specific error patterns (can the taxonomy predict which errors a new formalization will encounter?), (c) actionable recommendations per domain. This makes the paper valuable even if the downstream delta is modest. (4) **Trim 10 H100-hours** from the auto_research estimate to fit within the ≤200 constraint. (5) **Discuss LeanSearch v2's domain-agnostic SOTA** — if domain-agnostic retrieval is already very strong, what specifically does domain conditioning add beyond what scale/engineering can achieve?\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T13:02:18.347Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T13:02:18.347Z",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-28T13:02:18.359Z_

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

## Idea under review (round 4/10)
{
  "title": "Domain-Adaptive Autoformalization via Subdomain-Conditioned Retrieval and Error Taxonomy",
  "core_problem": "Current autoformalization systems treat all mathematical subdomains identically, yet empirical evidence from MSC-180 (CV values 4–6× above high-variability thresholds across 60 mathematical branches) and FormalMATH (0% on discrete math vs. 50% on algebra for Goedel-Prover) reveals severe, systematic domain bias. Aria (ICLR 2026) independently confirms this: 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) achieve 0% — demonstrating that certain specialized domains are catastrophically underserved even by SOTA systems. Meanwhile, retrieval-augmented approaches address retrieval quality through increasingly sophisticated methods — CRAMF uses contextual query augmentation for concept-level disambiguation, DRIFT (ICLR 2026) decomposes statements into ~5.8 atomic sub-queries for targeted concept-level retrieval, and LeanSearch v2 (May 2026) achieves SOTA premise retrieval (nDCG@10 = 0.623) without any domain-specific fine-tuning via hierarchy-informed informalization — but none conditions retrieval ranking on the inferred mathematical subdomain of the input problem. The 260k repair tuples in APRIL have never been stratified by mathematical subdomain despite containing implicit domain structure. Can we build the first autoformalization pipeline that systematically conditions its retrieval ranking and prompting signals on inferred mathematical subdomain — beyond concept-level disambiguation and decomposition — and does this problem-level domain conditioning yield measurable improvements, especially on currently catastrophic domains where even advanced retrieval alone cannot close the gap?",
  "opportunity": "Six critical resources and findings converged in 2025–2026 that make domain-adaptive autoformalization both feasible and necessary, each containing underexploited domain metadata: (1) Herald (ICLR 2025) provides 580k NL-formal pairs tagged with Mathlib4 module paths enabling automatic formalization-level domain labeling; (2) FineLeanCorpus/CriticLean (2025) provides 286k verified entries (509k total) with hierarchical problem-level domain labels (e.g., 'Algebra → Intermediate Algebra → Functional Equations') and difficulty scores — but these capture mathematical topic, not formalization-level structure; (3) APRIL (Feb 2026) provides 260k repair tuples that have never been stratified by domain; (4) CRAMF's 26k-definition knowledge base stores module paths (θ_p) per definition and uses LLM-generated contextual query augmentation to disambiguate polysemous concepts, but never conditions its retrieval reranking (bge-reranker-v2-m3) on the mathematical subdomain of the input problem; (5) MathAtlas (May 2026) provides 52k entities across 87 math areas with 178k dependency relations, using domain labels only for evaluation not pipeline conditioning; and (6) LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval via hierarchy-informed Mathlib informalization with Qwen3-Embedding/Reranker-8B — but its success demonstrates that retrieval quality alone, even at high levels, does not address the domain bias problem documented by MSC-180 and FormalMATH, because domain bias manifests in formalization accuracy, not retrieval recall. Crucially, MSC-180 (Dec 2025) quantified domain bias with coefficient of variation metrics across 60 mathematical branches showing best models achieve only 18.89% overall with maximum 41.7% domain coverage, FormalMATH (2025) showed Goedel-Prover achieving 50% on algebra but 0% on discrete math, and Aria's homological conjectures results (42.9% vs. 0% for all baselines) provide direct evidence that domain-specialized problems require fundamentally different handling. ConNF (DDR, ICLR 2025 Spotlight) tested OOD generalization to a single held-out domain (New Foundations set theory, 961 pairs), but no work has performed systematic multi-domain rotation evaluation across ≥4 mathematical subdomain categories. Recent textbook-scale formalizations — M2F (Feb 2026) on real analysis and convex analysis, and Automatic Textbook Formalization (Gloeckle et al., Apr 2026) on algebraic combinatorics — demonstrate that different mathematical domains can be formalized at scale but use uniform methods with no domain-specific conditioning. We hypothesize that Mathlib module paths (formalization-level structure) and problem-level domain labels (mathematical topic) capture complementary information — a number theory problem may require analysis-level typeclasses — and combining both signals for retrieval conditioning can close the domain gap in ways that concept-level disambiguation and decomposition alone cannot.",
  "landscape": "Current SOTA autoformalization is domain-agnostic: StepFun-Formalizer-32B achieves 40.5% BEq@1 on FormalMATH-Lite and 26.7% on ProverBench via knowledge-reasoning fusion (AAAI 2026); FormaRL achieves 26.15% on ProofNet using GRPO with compiler+consistency rewards on Qwen2.5-Coder-7B-Instruct with only 859 unlabeled examples (COLM 2025); ATLAS achieves SOTA via expert iteration with concept-first synthesis from Mathlib (NeurIPS 2025); ProofBridge (ICLR 2026) achieves +31.14% semantic correctness via cross-modal joint embeddings for retrieval-augmented formalization. All report aggregate metrics only — no paper breaks results down by mathematical subdomain or conditions its pipeline on domain. **Retrieval-augmented approaches represent a rich and rapidly evolving space, but all operate domain-agnostically**: (a) DDR (ICLR 2025 Spotlight) introduced Direct Dependency Retrieval and the ConNF benchmark (961 OOD pairs from New Foundations set theory) — ConNF tests generalization to a single held-out domain but does not perform systematic multi-domain rotation across mathematical subdomain categories; (b) CRAMF (ICLR 2026) stores Mathlib module paths (θ_p) per definition and performs contextual query augmentation with LLM-generated 'domain- and application-level signals' — but these signals are terminological interpretations designed to disambiguate polysemous concepts (e.g., 'neighborhood' in topological vs. metric spaces), not to identify the mathematical subdomain of the input problem and condition retrieval ranking accordingly; CRAMF's bge-reranker-v2-m3 scores semantic similarity between query interpretations and definition annotations without boosting same-subdomain definitions; (c) **DRIFT (ICLR 2026 Poster)** decomposes informal statements into ~5.8 atomic sub-queries for targeted concept-level retrieval using a finetuned BGE-M3 encoder, nearly doubling F1 on ProofNet (27.68 vs. 13.77 baseline) and achieving BEq+@10 improvements of 37–42% on ConNF — DRIFT's sub-query decomposition operates at the concept level (breaking one statement into individual mathematical concept queries), which is orthogonal to our problem-level approach (classifying the entire problem's mathematical subdomain and boosting all same-subdomain definitions); (d) **LeanSearch v2 (May 2026)** achieves SOTA single-query premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed Mathlib informalization with Qwen3-Embedding-8B and Qwen3-Reranker-8B, and its reasoning mode achieves 46.1% Recall@10 on global premise retrieval — LeanSearch v2 demonstrates that sophisticated domain-agnostic retrieval can be very strong, but its success addresses retrieval quality for theorem proving (finding relevant lemmas given a proof state), not the formalization accuracy gap across mathematical subdomains that MSC-180 documents; even with perfect premise retrieval, a formalizer that does not know topology problems disproportionately fail on typeclass instance resolution will not generate better topology formalizations. **Aria (ICLR 2026)** achieves 68.5% on ProofNet and 44.0% on FATE-X via Graph-of-Thought recursive decomposition with AriaScorer (term-level Mathlib grounding via Herald) — critically, Aria achieves 42.9% on homological conjectures while ALL baselines score 0%, providing the strongest published evidence that certain mathematical subdomains are catastrophically underserved by domain-agnostic approaches; yet Aria itself uses no domain conditioning, suggesting its Graph-of-Thought decomposition partially compensates for domain bias through deeper dependency analysis but cannot systematically address it. **Domain-specific autoformalization exists but is fragmented**: SITA (AAAI 2026) introduces a structure-to-instance paradigm using Lean's typeclass mechanism to instantiate abstract mathematical structures into concrete settings, evaluated on 42 optimization problems — but this is a specific pattern (abstract→concrete instantiation) applied to a single domain, not a general pipeline conditioned on subdomain identity. The 130k Topology project (Jan 2026) required manual human-LLM interaction for a single domain. M2F (Feb 2026) formalizes 479 pages of real analysis and convex analysis textbooks into 153k lines of Lean code, and Automatic Textbook Formalization (Gloeckle et al., Apr 2026) formalizes a 500-page algebraic combinatorics textbook into 130k lines — both demonstrate that different domains can be formalized at scale but use uniform methods, providing implicit evidence that domain-specific formalization is tractable while offering no systematic domain conditioning. Repair approaches (APRIL, ReForm) apply uniform repair strategies regardless of error origin. FineLeanCorpus (CriticLean, 2025) provides 286k verified entries (509k total) with 3-tier hierarchical problem-level domain labels and difficulty scores, but these classify mathematical content, not formalization-level dependencies. MSC-180 (Dec 2025) evaluated provers across 60 MSC2020 branches finding CV values 4–6× above statistical high-variability thresholds. MathAtlas (May 2026) introduces a 52k-entity benchmark spanning 87 math areas with 178k dependency relations but uses domain labels only for evaluation. Cross-domain evaluation via systematic multi-domain rotation (leave-one-domain-out across ≥4 subdomain categories) has never been performed for autoformalization — ConNF's single-domain OOD test is a valuable but limited precedent.",
  "inspired_by": "Field gaps #1 (no system conditions retrieval ranking on inferred mathematical subdomain — CRAMF disambiguates polysemous concepts, DRIFT decomposes statements into concept-level sub-queries, LeanSearch v2 achieves SOTA domain-agnostic retrieval, but none conditions reranking on input subdomain), #2 (APRIL 260k tuples never domain-stratified), #3 (CRAMF module paths and FineLeanCorpus topic labels never combined for subdomain-conditioned retrieval), #4 (ConNF tests single-domain OOD but no systematic multi-domain rotation exists); innovation patterns 'Retrieval at the Right Abstraction Level' (concept-level decomposition vs. problem-level domain signals) and 'Complementary Label Fusion'; untried combinations #1 (problem-level domain-conditioned retrieval extending CRAMF with Herald module-path labels + FineLeanCorpus topic labels) and #2 (domain-stratified APRIL error taxonomy as hypothesis-driven analysis); Aria's homological conjectures results (42.9% vs. 0%) as direct motivation that domain-agnostic approaches catastrophically fail on specialized domains even when using sophisticated retrieval; contrast with single-domain approaches (SITA, M2F, 130k Topology, Automatic Textbook Formalization) that demonstrate domain-specific formalization is tractable but offer no systematic multi-domain conditioning; reviewer preferences for surgical ablations including naive domain prompting baseline, compute-efficient designs, and LeanSearch v2 as strong domain-agnostic retrieval baseline.",
  "approach": "We build a three-stage domain-adaptive autoformalization pipeline on a Goedel-Formalizer-V2-8B backbone (user-specified model family; Qwen2.5-Coder-7B-Instruct used as additional baseline for FormaRL comparison). **Stage 1 — Domain-Specific Error Taxonomy (PRIMARY CONTRIBUTION)**: We train a lightweight domain classifier on Herald's 580k NL-formal pairs using Mathlib4 module paths as supervision, producing 5 major subdomain clusters (algebra/ring theory, topology/order, analysis/calculus, number theory/combinatorics, logic/foundations). We cross-reference with FineLeanCorpus's 286k verified entries with problem-level hierarchical labels to measure correlation and divergence between mathematical topic and formalization-level domain. We then stratify APRIL's 260k repair tuples by predicted subdomain and construct the first systematic domain-specific error taxonomy for autoformalization. **Standalone evaluation criteria for the error taxonomy**: (a) **Inter-domain error distribution divergence** — we compute Jensen-Shannon divergence between error-type distributions across domain pairs (e.g., topology vs. algebra error distributions) and test the hypothesis that error patterns cluster systematically by domain; statistical significance via permutation tests; (b) **Predictive power** — given a new formalization attempt's predicted domain, can the taxonomy predict which error types it will encounter? We measure this via a held-out error prediction task: train a simple classifier on domain → error-type distributions, evaluate prediction accuracy on unseen formalizations; (c) **Actionable recommendations per domain** — for each of the 5 subdomain clusters, we produce a ranked list of the top-5 most frequent error types with concrete mitigation strategies (e.g., 'topology formalizations: prioritize typeclass instance search depth; algebra formalizations: check coercion chain completeness'), evaluated by whether prompting with these recommendations improves formalization on held-out examples from that domain. This error taxonomy is valuable independent of any downstream pipeline delta — it provides the first empirical characterization of how autoformalization fails differently across mathematical subdomains, offering actionable guidance for domain-specific approaches (including SITA-like paradigms, textbook-scale formalizations like M2F, and future domain-specialized systems). **Stage 2 — Domain-Conditioned Retrieval**: We extend CRAMF's dual-channel hybrid retrieval with a domain-aware reranking layer that boosts same-subdomain definitions. This operates at a fundamentally different level than existing retrieval innovations: CRAMF's contextual query augmentation disambiguates polysemous concepts one at a time (concept-level); DRIFT decomposes statements into atomic sub-queries for targeted per-concept retrieval (concept-level decomposition); LeanSearch v2 achieves SOTA domain-agnostic retrieval via hierarchy-informed informalization (retrieval quality). Our reranker adds an orthogonal signal: given that the input problem is classified as topology, boost ALL topology-related definitions in retrieval, not just disambiguate individual concepts or decompose the statement into sub-queries. We explicitly address the LeanSearch v2 challenge: domain-agnostic retrieval can achieve high recall on well-represented domains, but the domain gap documented by MSC-180 manifests in formalization accuracy across domains, not retrieval recall within domains. Our hypothesis is that domain conditioning helps most where domain-agnostic methods already retrieve relevant premises but the formalizer fails because it lacks domain context — e.g., retrieving the right topology definitions but failing to apply them correctly because the formalizer doesn't know topology-specific patterns. The reranker is trained on Herald+CRAMF data with domain match as an additional feature alongside the existing semantic similarity score. We compare domain-conditioned retrieval vs. domain-agnostic retrieval at matched retrieval budget (same Top-K, same compute) to isolate the domain signal's contribution. We additionally compare against LeanSearch v2's standard mode as a strong domain-agnostic retrieval baseline to test whether domain conditioning provides gains beyond what superior domain-agnostic retrieval already captures. **Stage 3 — Domain-Aware Autoformalization**: Using Goedel-Formalizer-V2-8B, we apply domain-prefixed prompting: the input is augmented with predicted subdomain label, top domain-specific error patterns from Stage 1, and domain-conditioned retrieved definitions from Stage 2. We perform LoRA fine-tuning (rank 32) on domain-enriched data combining Herald and FineLeanCorpus, where each training example includes its domain context. No complex LoRA routing or domain-specific adapters — a single adapter learns to use domain context from the prompt. **Evaluation**: We introduce the first systematic multi-domain rotation evaluation protocol for autoformalization — leave-one-domain-out across our 5 subdomain categories, extending ConNF's single-domain OOD paradigm to systematic cross-domain generalization testing. Evaluated on FormalMATH-categorized problems and MathAtlas's 87-area benchmark. MSC-180's 60-branch classification serves as cross-domain generalization test. ConNF serves as an additional single-domain OOD test (New Foundations set theory). Surgical ablations isolate: (a) domain-conditioned retrieval alone (Stage 2 only), (b) domain-prefixed prompting alone (subdomain label in prompt, no retrieval change), (c) domain error context alone (error patterns in prompt, no retrieval change), (d) full combination (Stages 1+2+3), (e) **naive domain prompting baseline** — simply prepending the predicted domain label to the input with zero pipeline engineering — to test whether trivial domain signals capture the majority of gains, and (f) **LeanSearch v2 retrieval baseline** — replacing our domain-conditioned retrieval with LeanSearch v2's standard mode to test whether superior domain-agnostic retrieval subsumes domain conditioning. If naive prompting captures 80%+ of gains, we report this honestly as evidence that simple domain awareness is surprisingly powerful; if the full pipeline significantly outperforms, it validates the engineering investment. A domain-agnostic matched-compute baseline (same LoRA budget, same retrieval budget, no domain conditioning) serves as control. Per-domain improvement analysis focuses on whether currently weak domains (analysis, discrete math, topology) show disproportionate gains. Domain-conditioned retrieval HitRate@K metrics provide pipeline-internal evaluation independent of downstream formalization accuracy.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200 H100-hours (domain classifier: 10h; APRIL stratification inference + error taxonomy construction: 8h; domain reranker training: 15h; LoRA fine-tuning Goedel-Formalizer-V2-8B: 80h; evaluation across 5 domains × 3 benchmarks with Lean4 compilation: 50h; ablation experiments including naive domain prompting + LeanSearch v2 comparison: 37h)",
      "timeline": "16 weeks (3w domain taxonomy + APRIL error analysis + error taxonomy evaluation, 3w domain-conditioned retrieval + LeanSearch v2 baseline integration, 4w LoRA fine-tuning + training, 3w evaluation + leave-one-domain-out + ablations + ConNF, 3w writing + revision)",
      "estimated_gpu_cost": "$500 (H100 at ~$2.50/hr average via RunPod/Lambda)"
    },
    "human_in_loop": {
      "gpu_hours": "~200 H100-hours",
      "timeline": "12 weeks (Claude accelerates domain taxonomy design, APRIL error pattern classification, retrieval pipeline code, and ablation analysis)",
      "claude_api_cost": "$300 (domain taxonomy extraction from Herald+FineLeanCorpus metadata, error clustering analysis across 260k APRIL tuples, evaluation script scaffolding, ablation result analysis)",
      "estimated_gpu_cost": "$500"
    },
    "auto_research": {
      "gpu_hours": "~200 H100-hours (domain classifier: 10h; APRIL stratification + error taxonomy: 8h; domain reranker training: 15h; LoRA fine-tuning: 78h; evaluation across 5 domains × 3 benchmarks + ConNF: 48h; ablation experiments including naive prompting + LeanSearch v2 baseline: 35h; hyperparameter sweeps over domain granularity 3–7 clusters: 6h)",
      "timeline": "10 weeks",
      "claude_api_cost": "$450 (automated domain taxonomy iteration, repair pattern mining, hyperparameter selection, result analysis and paper drafting)",
      "estimated_gpu_cost": "$500",
      "speed_bottleneck": "Lean4 type-checking latency (~3–10s per statement) gates evaluation throughput; each leave-one-domain-out fold requires full Lean4 compilation across ~2k–5k statements; domain-conditioned retrieval index must be rebuilt when domain granularity changes"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated abstract: Sep 19, 2026; paper: Sep 24, 2026 — projected from historical pattern, NOT officially announced; ~16 weeks from today, PRIMARY TARGET; contingency: if actual deadline is earlier, submit Stage 1 error taxonomy + Stage 2 retrieval results without full Stage 3 ablations)",
    "AAAI 2027 (abstract: Jul 21, 2026; paper: Jul 28, 2026 — confirmed; only 8 weeks from today, STRETCH if Stage 1 error analysis yields strong early results; could submit error taxonomy + domain-conditioned retrieval as core contributions)",
    "NeurIPS 2026 MATH-AI Workshop (workshop paper deadline estimated ~Sep 2026 — contingent on workshop acceptance; workshop proposals due Jun 6, 2026)"
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
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs / CRAMF (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Aria: An Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026 Poster)",
    "Learning to Repair Lean Proofs from Compiler Feedback / APRIL (arXiv 2026)",
    "M2F: Automated Formalization of Mathematical Literature at Scale (arXiv 2026)",
    "Automatic Textbook Formalization / RepoProver (Gloeckle et al., arXiv 2026)",
    "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone? (arXiv 2026)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2026)",
    "LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving (arXiv 2026)"
  ],
  "description": "We propose the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain, operating at the problem level rather than individual concept disambiguation or decomposition. Current SOTA systems (StepFun-Formalizer, ATLAS, FormaRL, ProofBridge, Aria, DRIFT) treat all domains identically, yet MSC-180 reveals CV values 4–6× above statistical high-variability thresholds across 60 mathematical branches, FormalMATH shows Goedel-Prover at 50% on algebra but 0% on discrete math, and Aria (ICLR 2026) achieves 42.9% on homological conjectures while all baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) score 0% — the strongest published evidence that domain-agnostic approaches catastrophically fail on specialized mathematical subdomains. Existing retrieval innovations address different aspects: CRAMF disambiguates polysemous concepts via contextual query augmentation (concept-level); DRIFT decomposes statements into ~5.8 atomic sub-queries for targeted per-concept retrieval (concept-level decomposition); LeanSearch v2 (May 2026) achieves SOTA domain-agnostic premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed informalization (retrieval quality). None conditions on the mathematical subdomain of the input problem. We contribute two primary results: (1) **The first domain-specific error taxonomy for autoformalization** — stratifying APRIL's 260k repair tuples across 5 mathematical subdomain clusters, evaluated via inter-domain error distribution divergence (Jensen-Shannon divergence + permutation tests), error-type prediction accuracy on held-out formalizations, and actionable per-domain mitigation recommendations; this standalone empirical contribution characterizes how autoformalization fails differently across domains and provides guidance independent of any downstream delta. (2) **Problem-level domain-conditioned retrieval and prompting** — extending CRAMF with a domain-aware reranker that boosts same-subdomain definitions, orthogonal to concept-level disambiguation (CRAMF), concept-level decomposition (DRIFT), and domain-agnostic retrieval quality (LeanSearch v2). We introduce the first systematic multi-domain rotation evaluation protocol (leave-one-domain-out across ≥5 mathematical subdomain categories), extending ConNF's single-domain OOD paradigm. Six surgical ablations include naive domain prompting (zero-engineering baseline) and LeanSearch v2 retrieval replacement (testing whether superior domain-agnostic retrieval subsumes domain conditioning). The entire pipeline fits within 200 H100-hours.",
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
    "round3_issue_1_DRIFT_Aria": "RESOLVED: Added DRIFT (ICLR 2026 Poster) to landscape with full technical differentiation. DRIFT decomposes informal statements into ~5.8 atomic sub-queries using finetuned BGE-M3 encoder for targeted concept-level retrieval, nearly doubling F1 on ProofNet (27.68 vs. 13.77) and achieving BEq+@10 improvements of 37–42% on ConNF. Explicitly differentiated: DRIFT's sub-query decomposition is concept-level (breaking one statement into individual concept queries); our approach is problem-level (classifying the entire problem's subdomain and boosting all same-subdomain definitions). These are orthogonal and complementary. Added Aria (ICLR 2026) with full performance details — Aria's 42.9% on homological conjectures vs. 0% for ALL baselines (Gemini-2.5-Pro, Goedel-Formalizer-V2-32B, Kimina-Autoformalizer-7B) now serves as the strongest published evidence for domain bias in our motivation. Aria uses Graph-of-Thought recursive decomposition with AriaScorer (term-level Mathlib grounding via Herald) but no domain conditioning, suggesting deeper dependency analysis partially compensates but cannot systematically address domain bias.",
    "round3_issue_2_ConNF_claim": "RESOLVED: Narrowed 'first leave-one-domain-out evaluation protocol' to 'first systematic multi-domain rotation evaluation protocol across ≥5 mathematical subdomain categories.' ConNF (DDR, ICLR 2025 Spotlight) explicitly cited as testing single-domain OOD (New Foundations set theory, 961 pairs from con-nf library with 1,348 formal objects) — a valuable but limited precedent that tests generalization to ONE held-out specialized domain. Our protocol extends this to systematic rotation across all 5 subdomain clusters, which ConNF does not attempt. ConNF also added as an additional evaluation benchmark.",
    "round3_issue_3_error_taxonomy_elevation": "RESOLVED: Error taxonomy elevated to unambiguous primary contribution with three standalone evaluation criteria: (a) inter-domain error distribution divergence measured via Jensen-Shannon divergence between domain pairs with statistical significance via permutation tests; (b) predictive power — held-out error prediction task training a classifier on domain→error-type distributions; (c) actionable recommendations per domain — ranked top-5 error types per subdomain cluster with concrete mitigation strategies, evaluated by improvement on held-out domain examples. This makes the paper valuable even if the downstream formalization delta is modest — the taxonomy is the first empirical characterization of how autoformalization fails differently across mathematical subdomains.",
    "round3_issue_4_compute_trim": "RESOLVED: Trimmed auto_research from 210 to 200 H100-hours by reducing LoRA fine-tuning from 80h to 78h and evaluation from 50h to 48h (using more aggressive Lean4 compilation batching and reducing redundant re-compilation across ablation conditions). All three modes now ≤200 H100-hours.",
    "round3_issue_5_LeanSearch_v2": "RESOLVED: Added LeanSearch v2 (May 2026, arXiv 2605.13137) comprehensively. LeanSearch v2 achieves SOTA single-query premise retrieval (nDCG@10 = 0.623 vs. 0.533 for LeanFinder) without domain-specific fine-tuning, using Qwen3-Embedding-8B and Qwen3-Reranker-8B with hierarchy-informed Mathlib informalization. Reasoning mode achieves 46.1% Recall@10 on global premise retrieval. Downstream proof success: 20% vs. 16% (next best). Explicitly addressed the challenge to our motivation: LeanSearch v2 demonstrates that domain-agnostic retrieval can be very strong, but its success addresses retrieval quality (finding relevant lemmas), not the formalization accuracy gap across subdomains documented by MSC-180. Even with perfect retrieval, a formalizer lacking domain-specific error awareness will fail differently across domains. Added ablation (f) — LeanSearch v2 retrieval baseline — to directly test whether superior domain-agnostic retrieval subsumes domain conditioning."
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
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "8d67d966-88c2-4364-818d-71a9ba07cb03",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T13:02:18.357Z_

```json
{
  "parentUuid": "8d67d966-88c2-4364-818d-71a9ba07cb03",
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
  "uuid": "66dd6e68-2855-4b82-b847-3d57ea7d935e",
  "timestamp": "2026-05-28T13:02:18.357Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T13:02:18.357Z_

```json
{
  "parentUuid": "66dd6e68-2855-4b82-b847-3d57ea7d935e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ed93cd28-61fc-4a29-952a-3308a7e8d1a2",
  "timestamp": "2026-05-28T13:02:18.357Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
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
  "leafUuid": "ed93cd28-61fc-4a29-952a-3308a7e8d1a2",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization via subdomain conditioning",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Assistant

_source line 8 · 2026-05-28T13:02:26.764Z_

<details><summary>Logged reasoning block</summary>

```text
This is a very detailed research proposal review request. I need to independently verify the claims made in this proposal through web searches, then issue a verdict. Let me systematically go through the key claims and verify them.

Let me start by searching for the key papers and claims mentioned in this proposal. I'll need to verify:

1. Whether the cited papers actually exist and say what's claimed
2. Whether the claimed gap (no domain-adaptive autoformalization) still exists
3. Whether there are competing/concurrent works not cited
4. Whether the resource estimates are realistic
5. Whether the venue targeting makes sense

Let me launch multiple search agents to cover different dimensions simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed93cd28-61fc-4a29-952a-3308a7e8d1a2",
  "isSidechain": false,
  "requestId": "req_011CbV1cngS541pNpxu8zt9H",
  "type": "assistant",
  "uuid": "1fa08e6e-ca12-42f1-87ea-b8995b76a019",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZsqDn5rCsnrX7zsjjgBJL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15467,
      "cache_read_input_tokens": 11014,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 721,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15467
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

_source line 9 · 2026-05-28T13:02:27.848Z_

I'll conduct a thorough adversarial review by independently verifying the key claims across multiple dimensions. Let me launch parallel research agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fa08e6e-ca12-42f1-87ea-b8995b76a019",
  "isSidechain": false,
  "requestId": "req_011CbV1cngS541pNpxu8zt9H",
  "type": "assistant",
  "uuid": "56d02450-0ef3-4d37-8d9b-ba53847762b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZsqDn5rCsnrX7zsjjgBJL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15467,
      "cache_read_input_tokens": 11014,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 721,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15467
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

_source line 10 · 2026-05-28T13:02:40.269Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L5uC8GtqcFUMJBJi82K3mi`</summary>

```json
{
  "description": "Verify key cited papers exist",
  "subagent_type": "general-purpose",
  "prompt": "You are helping verify claims in a research proposal about domain-adaptive autoformalization. I need you to verify that these key papers actually exist and check whether the claims about them are accurate. Use WebSearch and WebFetch to verify each one.\n\nPapers to verify (check title, venue, date, and key claims):\n\n1. **LeanSearch v2** (claimed: May 2026, arXiv 2605.13137) — claimed to achieve SOTA premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed Mathlib informalization with Qwen3-Embedding-8B\n2. **DRIFT** (claimed: ICLR 2026 Poster) — claimed to decompose statements into ~5.8 atomic sub-queries, nearly doubling F1 on ProofNet (27.68 vs. 13.77)\n3. **Aria** (claimed: ICLR 2026) — claimed 68.5% on ProofNet and 42.9% on homological conjectures while all baselines score 0%\n4. **MathAtlas** (claimed: May 2026) — claimed 52k entities across 87 math areas with 178k dependency relations\n5. **CRAMF** (claimed: ICLR 2026) — claimed to store module paths (θ_p) per definition and use contextual query augmentation\n6. **MSC-180** (claimed: Dec 2025, arXiv 2512.18256) — claimed CV values 4-6× above high-variability thresholds across 60 mathematical branches\n\nFor each paper, search for it, try to fetch its abstract/details, and report:\n- Does it exist? \n- Are the claimed venue/date correct?\n- Are the specific numerical claims accurate?\n\nBe thorough - try multiple search queries if initial ones don't work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56d02450-0ef3-4d37-8d9b-ba53847762b5",
  "isSidechain": false,
  "requestId": "req_011CbV1cngS541pNpxu8zt9H",
  "type": "assistant",
  "uuid": "c39bab2d-234b-4544-924b-8f1e8fdf1b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZsqDn5rCsnrX7zsjjgBJL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15467,
      "cache_read_input_tokens": 11014,
      "output_tokens": 721,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 721,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 15467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15467
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

_source line 11 · 2026-05-28T13:05:22.582Z_

<details><summary>↩ Tool result · `toolu_01L5uC8GtqcFUMJBJi82K3mi`</summary>

```text
Now I have all the data needed. Let me also verify whether the "~5.8" claim is a reasonable characterization of the 5.21-6.42 range.

The midpoint of 5.21 and 6.42 is 5.815, which rounds to ~5.8. That checks out.

Here is my comprehensive verification report for all six papers:

---

## Paper Verification Report

### 1. LeanSearch v2 (arXiv 2605.13137)

**Exists?** YES. Confirmed at [arxiv.org/abs/2605.13137](https://arxiv.org/abs/2605.13137).

**Venue/Date claim: "May 2026, arXiv 2605.13137"** -- CORRECT. Submitted May 13, 2026; revised May 14, 2026.

**Claim: "SOTA premise retrieval (nDCG@10 = 0.623)"** -- CORRECT. Table 1 in the paper reports nDCG@10 of 0.623 for "LeanSearch v2 (rerank)", versus 0.53 for the next-best system.

**Claim: "without domain-specific fine-tuning"** -- CORRECT. The paper emphasizes using general-purpose models without domain-specific fine-tuning.

**Claim: "hierarchy-informed Mathlib informalization"** -- PARTIALLY ACCURATE. The paper describes a "dependency-aware informalization strategy" where previously informalized descriptions of dependencies are passed as context. The proposal's term "hierarchy-informed" is a paraphrase rather than the paper's exact terminology ("dependency-aware"), but the concept is the same.

**Claim: "with Qwen3-Embedding-8B"** -- CORRECT. The paper explicitly states: "Each corpus item is encoded into a fixed-dimensional vector using Qwen3-Embedding-8B."

---

### 2. DRIFT (ICLR 2026 Poster)

**Exists?** YES. Confirmed at [arxiv.org/abs/2510.10815](https://arxiv.org/abs/2510.10815) and [OpenReview](https://openreview.net/forum?id=IGEs577RFz).

**Venue/Date claim: "ICLR 2026 Poster"** -- CORRECT. Published January 26, 2026 as an ICLR 2026 Poster.

**Claim: "decomposes statements into ~5.8 atomic sub-queries"** -- APPROXIMATELY CORRECT. The paper reports sub-query counts ranging from 5.21 to 6.42 depending on the decomposer model. The midpoint is ~5.8, so this is a reasonable summary, though the paper does not state "5.8" as a single figure. The paper also does not use the word "atomic" -- it calls them "sub-components" or "sub-queries."

**Claim: "nearly doubling F1 on ProofNet (27.68 vs. 13.77)"** -- CORRECT. Table 1 shows the no-decomposition baseline at 13.77% F1 and the best DRIFT variant (Claude-Opus-4 decomposer) at 27.68% F1 on ProofNet. The paper itself characterizes this as "nearly doubling."

---

### 3. Aria (ICLR 2026)

**Exists?** YES. Confirmed at [arxiv.org/abs/2510.04520](https://arxiv.org/abs/2510.04520) and [OpenReview](https://openreview.net/forum?id=CPxZClPMiy).

**Venue/Date claim: "ICLR 2026"** -- CORRECT. Accepted as an ICLR 2026 Poster (published January 26, 2026).

**Claim: "68.5% on ProofNet"** -- CORRECT. The abstract states "68.5% final accuracy" on ProofNet.

**Claim: "42.9% on homological conjectures while all baselines score 0%"** -- CORRECT. The abstract states: "On a dataset of homological conjectures, Aria reaches 42.9% final accuracy while all other models score 0%."

---

### 4. MathAtlas (May 2026)

**Exists?** YES. Confirmed at [arxiv.org/html/2605.14061](https://arxiv.org/html/2605.14061).

**Date claim: "May 2026"** -- CORRECT. Submitted May 13, 2026.

**Claim: "52k entities"** -- CORRECT. The paper reports ~52k entities (52,052 total).

**Claim: "87 math areas"** -- CORRECT. The paper states the benchmark spans "87 areas of mathematics."

**Claim: "178k dependency relations"** -- CORRECT. The paper reports "~178k" object relations in the dependency graph.

---

### 5. CRAMF (ICLR 2026)

**Exists?** YES. The paper is titled "Automated Formalization via Conceptual Retrieval-Augmented LLMs" and introduces the CRAMF framework. Confirmed at [arxiv.org/abs/2508.06931](https://arxiv.org/abs/2508.06931) and [OpenReview](https://openreview.net/forum?id=09lmwhDqZ3).

**Venue claim: "ICLR 2026"** -- CORRECT. Accepted as an ICLR 2026 Poster (published January 26, 2026).

**Claim: "stores module paths (theta_p) per definition"** -- CORRECT. The paper defines formal definitions via the attribute triple "(theta_tau, theta_f, theta_p), denoting the definition's identifier, formal expression, and module path."

**Claim: "uses contextual query augmentation"** -- CORRECT. The paper proposes "contextual query augmentation with domain- and application-level signals" to address conceptual polymorphism.

---

### 6. MSC-180 (Dec 2025, arXiv 2512.18256)

**Exists?** YES. Confirmed at [arxiv.org/abs/2512.18256](https://arxiv.org/abs/2512.18256).

**Date/Venue claim: "Dec 2025, arXiv 2512.18256"** -- CORRECT. Submitted December 20, 2025.

**Claim: "CV values 4-6x above high-variability thresholds"** -- CORRECT. The paper reports "CV values are 4-6 times higher than the statistical high-variability threshold."

**Claim: "across 60 mathematical branches"** -- CORRECT. The benchmark comprises 180 problems from 60 mathematical branches (3 per branch).

---

## Summary Table

| Paper | Exists? | Venue/Date Correct? | Numerical Claims Accurate? |
|-------|---------|--------------------|-----------------------------|
| LeanSearch v2 | YES | YES | YES (nDCG@10=0.623, Qwen3-Embedding-8B confirmed) |
| DRIFT | YES | YES (ICLR 2026 Poster) | YES (27.68 vs 13.77 F1; ~5.8 is reasonable summary of 5.21-6.42 range) |
| Aria | YES | YES (ICLR 2026 Poster) | YES (68.5% ProofNet, 42.9% homological, 0% baselines) |
| MathAtlas | YES | YES (May 2026) | YES (52k entities, 87 areas, 178k relations) |
| CRAMF | YES | YES (ICLR 2026 Poster) | YES (theta_p module paths, contextual query augmentation) |
| MSC-180 | YES | YES (Dec 2025) | YES (CV 4-6x, 60 branches) |

**Overall verdict:** All six papers exist, all venue/date claims are correct, and all specific numerical claims are accurate. The only minor note is that LeanSearch v2 uses the term "dependency-aware informalization" rather than "hierarchy-informed informalization" as stated in the proposal, and DRIFT's "~5.8 sub-queries" is a derived midpoint of the reported 5.21-6.42 range rather than a figure stated directly in the paper. These are minor paraphrasing differences, not factual errors.

agentId: aa8f6287647c684b1 (use SendMessage with to: 'aa8f6287647c684b1' to continue this agent)
&lt;usage>total_tokens: 26183
tool_uses: 24
duration_ms: 162307&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c39bab2d-234b-4544-924b-8f1e8fdf1b38",
  "isSidechain": false,
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "7e630ca0-be9f-4413-82eb-2063fd246ba0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping verify claims in a research proposal about domain-adaptive autoformalization. I need you to verify that these key papers actually exist and check whether the claims about them are accurate. Use WebSearch and WebFetch to verify each one.\n\nPapers to verify (check title, venue, date, and key claims):\n\n1. **LeanSearch v2** (claimed: May 2026, arXiv 2605.13137) — claimed to achieve SOTA premise retrieval (nDCG@10 = 0.623) without domain-specific fine-tuning via hierarchy-informed Mathlib informalization with Qwen3-Embedding-8B\n2. **DRIFT** (claimed: ICLR 2026 Poster) — claimed to decompose statements into ~5.8 atomic sub-queries, nearly doubling F1 on ProofNet (27.68 vs. 13.77)\n3. **Aria** (claimed: ICLR 2026) — claimed 68.5% on ProofNet and 42.9% on homological conjectures while all baselines score 0%\n4. **MathAtlas** (claimed: May 2026) — claimed 52k entities across 87 math areas with 178k dependency relations\n5. **CRAMF** (claimed: ICLR 2026) — claimed to store module paths (θ_p) per definition and use contextual query augmentation\n6. **MSC-180** (claimed: Dec 2025, arXiv 2512.18256) — claimed CV values 4-6× above high-variability thresholds across 60 mathematical branches\n\nFor each paper, search for it, try to fetch its abstract/details, and report:\n- Does it exist? \n- Are the claimed venue/date correct?\n- Are the specific numerical claims accurate?\n\nBe thorough - try multiple search queries if initial ones don't work.",
    "agentId": "aa8f6287647c684b1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the data needed. Let me also verify whether the \"~5.8\" claim is a reasonable characterization of the 5.21-6.42 range.\n\nThe midpoint of 5.21 and 6.42 is 5.815, which rounds to ~5.8. That checks out.\n\nHere is my comprehensive verification report for all six papers:\n\n---\n\n## Paper Verification Report\n\n### 1. LeanSearch v2 (arXiv 2605.13137)\n\n**Exists?** YES. Confirmed at [arxiv.org/abs/2605.13137](https://arxiv.org/abs/2605.13137).\n\n**Venue/Date claim: \"May 2026, arXiv 2605.13137\"** -- CORRECT. Submitted May 13, 2026; revised May 14, 2026.\n\n**Claim: \"SOTA premise retrieval (nDCG@10 = 0.623)\"** -- CORRECT. Table 1 in the paper reports nDCG@10 of 0.623 for \"LeanSearch v2 (rerank)\", versus 0.53 for the next-best system.\n\n**Claim: \"without domain-specific fine-tuning\"** -- CORRECT. The paper emphasizes using general-purpose models without domain-specific fine-tuning.\n\n**Claim: \"hierarchy-informed Mathlib informalization\"** -- PARTIALLY ACCURATE. The paper describes a \"dependency-aware informalization strategy\" where previously informalized descriptions of dependencies are passed as context. The proposal's term \"hierarchy-informed\" is a paraphrase rather than the paper's exact terminology (\"dependency-aware\"), but the concept is the same.\n\n**Claim: \"with Qwen3-Embedding-8B\"** -- CORRECT. The paper explicitly states: \"Each corpus item is encoded into a fixed-dimensional vector using Qwen3-Embedding-8B.\"\n\n---\n\n### 2. DRIFT (ICLR 2026 Poster)\n\n**Exists?** YES. Confirmed at [arxiv.org/abs/2510.10815](https://arxiv.org/abs/2510.10815) and [OpenReview](https://openreview.net/forum?id=IGEs577RFz).\n\n**Venue/Date claim: \"ICLR 2026 Poster\"** -- CORRECT. Published January 26, 2026 as an ICLR 2026 Poster.\n\n**Claim: \"decomposes statements into ~5.8 atomic sub-queries\"** -- APPROXIMATELY CORRECT. The paper reports sub-query counts ranging from 5.21 to 6.42 depending on the decomposer model. The midpoint is ~5.8, so this is a reasonable summary, though the paper does not state \"5.8\" as a single figure. The paper also does not use the word \"atomic\" -- it calls them \"sub-components\" or \"sub-queries.\"\n\n**Claim: \"nearly doubling F1 on ProofNet (27.68 vs. 13.77)\"** -- CORRECT. Table 1 shows the no-decomposition baseline at 13.77% F1 and the best DRIFT variant (Claude-Opus-4 decomposer) at 27.68% F1 on ProofNet. The paper itself characterizes this as \"nearly doubling.\"\n\n---\n\n### 3. Aria (ICLR 2026)\n\n**Exists?** YES. Confirmed at [arxiv.org/abs/2510.04520](https://arxiv.org/abs/2510.04520) and [OpenReview](https://openreview.net/forum?id=CPxZClPMiy).\n\n**Venue/Date claim: \"ICLR 2026\"** -- CORRECT. Accepted as an ICLR 2026 Poster (published January 26, 2026).\n\n**Claim: \"68.5% on ProofNet\"** -- CORRECT. The abstract states \"68.5% final accuracy\" on ProofNet.\n\n**Claim: \"42.9% on homological conjectures while all baselines score 0%\"** -- CORRECT. The abstract states: \"On a dataset of homological conjectures, Aria reaches 42.9% final accuracy while all other models score 0%.\"\n\n---\n\n### 4. MathAtlas (May 2026)\n\n**Exists?** YES. Confirmed at [arxiv.org/html/2605.14061](https://arxiv.org/html/2605.14061).\n\n**Date claim: \"May 2026\"** -- CORRECT. Submitted May 13, 2026.\n\n**Claim: \"52k entities\"** -- CORRECT. The paper reports ~52k entities (52,052 total).\n\n**Claim: \"87 math areas\"** -- CORRECT. The paper states the benchmark spans \"87 areas of mathematics.\"\n\n**Claim: \"178k dependency relations\"** -- CORRECT. The paper reports \"~178k\" object relations in the dependency graph.\n\n---\n\n### 5. CRAMF (ICLR 2026)\n\n**Exists?** YES. The paper is titled \"Automated Formalization via Conceptual Retrieval-Augmented LLMs\" and introduces the CRAMF framework. Confirmed at [arxiv.org/abs/2508.06931](https://arxiv.org/abs/2508.06931) and [OpenReview](https://openreview.net/forum?id=09lmwhDqZ3).\n\n**Venue claim: \"ICLR 2026\"** -- CORRECT. Accepted as an ICLR 2026 Poster (published January 26, 2026).\n\n**Claim: \"stores module paths (theta_p) per definition\"** -- CORRECT. The paper defines formal definitions via the attribute triple \"(theta_tau, theta_f, theta_p), denoting the definition's identifier, formal expression, and module path.\"\n\n**Claim: \"uses contextual query augmentation\"** -- CORRECT. The paper proposes \"contextual query augmentation with domain- and application-level signals\" to address conceptual polymorphism.\n\n---\n\n### 6. MSC-180 (Dec 2025, arXiv 2512.18256)\n\n**Exists?** YES. Confirmed at [arxiv.org/abs/2512.18256](https://arxiv.org/abs/2512.18256).\n\n**Date/Venue claim: \"Dec 2025, arXiv 2512.18256\"** -- CORRECT. Submitted December 20, 2025.\n\n**Claim: \"CV values 4-6x above high-variability thresholds\"** -- CORRECT. The paper reports \"CV values are 4-6 times higher than the statistical high-variability threshold.\"\n\n**Claim: \"across 60 mathematical branches\"** -- CORRECT. The benchmark comprises 180 problems from 60 mathematical branches (3 per branch).\n\n---\n\n## Summary Table\n\n| Paper | Exists? | Venue/Date Correct? | Numerical Claims Accurate? |\n|-------|---------|--------------------|-----------------------------|\n| LeanSearch v2 | YES | YES | YES (nDCG@10=0.623, Qwen3-Embedding-8B confirmed) |\n| DRIFT | YES | YES (ICLR 2026 Poster) | YES (27.68 vs 13.77 F1; ~5.8 is reasonable summary of 5.21-6.42 range) |\n| Aria | YES | YES (ICLR 2026 Poster) | YES (68.5% ProofNet, 42.9% homological, 0% baselines) |\n| MathAtlas | YES | YES (May 2026) | YES (52k entities, 87 areas, 178k relations) |\n| CRAMF | YES | YES (ICLR 2026 Poster) | YES (theta_p module paths, contextual query augmentation) |\n| MSC-180 | YES | YES (Dec 2025) | YES (CV 4-6x, 60 branches) |\n\n**Overall verdict:** All six papers exist, all venue/date claims are correct, and all specific numerical claims are accurate. The only minor note is that LeanSearch v2 uses the term \"dependency-aware informalization\" rather than \"hierarchy-informed informalization\" as stated in the proposal, and DRIFT's \"~5.8 sub-queries\" is a derived midpoint of the reported 5.21-6.42 range rather than a figure stated directly in the paper. These are minor paraphrasing differences, not factual errors."
      }
    ],
    "totalDurationMs": 162307,
    "totalTokens": 26183,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 23578,
      "output_tokens": 2062,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2062,
          "cache_read_input_tokens": 23578,
          "cache_creation_input_tokens": 542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 542,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "c39bab2d-234b-4544-924b-8f1e8fdf1b38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-28T13:05:34.635Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L4oJSeEpHsDiPyn4tWeC6U`</summary>

```json
{
  "description": "Search competing/concurrent work",
  "subagent_type": "general-purpose",
  "prompt": "You are helping review a research proposal about \"domain-adaptive autoformalization\" — the idea of conditioning autoformalization pipelines (translating natural language math to formal Lean 4 code) on mathematical subdomain (algebra, topology, analysis, etc.).\n\nI need you to search exhaustively for competing or concurrent work that might already address this gap. The proposal claims NO existing system conditions its autoformalization pipeline on mathematical subdomain. Search for work that might contradict this.\n\nUse WebSearch for each of these searches:\n\n1. \"domain adaptive autoformalization\" OR \"domain-specific autoformalization\" 2025 2026\n2. \"subdomain\" \"autoformalization\" Lean Mathlib 2026\n3. \"domain-conditioned\" OR \"domain-aware\" formalization theorem proving 2026\n4. site:arxiv.org \"autoformalization\" \"domain\" 2026\n5. site:openreview.net autoformalization domain adaptation 2026\n6. \"mathematical domain\" \"formalization\" \"retrieval\" conditioning 2026\n7. \"Mathlib\" \"module hierarchy\" \"domain\" autoformalization\n8. \"error taxonomy\" autoformalization Lean 2025 2026\n9. \"domain-stratified\" OR \"domain-specific\" \"repair\" formalization 2026\n10. \"cross-domain\" autoformalization generalization 2026\n\nFor any promising results, use WebFetch to read the abstracts and determine if they actually do domain-conditioned autoformalization.\n\nReport: Did you find ANY paper that already does what this proposal claims to be the first to do (conditioning the autoformalization pipeline on mathematical subdomain)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e630ca0-be9f-4413-82eb-2063fd246ba0",
  "isSidechain": false,
  "requestId": "req_011CbV1rNGdnWkPfceH9rosj",
  "type": "assistant",
  "uuid": "db8a8210-1a33-4174-b335-bae7605b7c00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FreLVFtucYz1FUbN84YeGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2861,
      "cache_read_input_tokens": 26481,
      "output_tokens": 465,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2861,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 465,
          "cache_read_input_tokens": 26481,
          "cache_creation_input_tokens": 2861,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2861
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

_source line 13 · 2026-05-28T13:09:52.144Z_

<details><summary>↩ Tool result · `toolu_01L4oJSeEpHsDiPyn4tWeC6U`</summary>

```text
I now have comprehensive results. Let me compile my findings.

---

## Report: Does Any Existing Work Do Domain-Conditioned Autoformalization?

After conducting 17 web searches and fetching/analyzing 14 papers in detail, here is my assessment:

### Short answer: No existing paper makes domain-conditioned autoformalization its primary contribution. The proposal's novelty claim appears to hold, with one partial caveat.

---

### The One Partial Caveat: IndiMathBench (December 2025)

**Paper:** [IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch](https://arxiv.org/abs/2512.00997) (Microsoft Research, published at ICLR 2026)

This is the closest thing I found. IndiMathBench's pipeline includes a **category-specific context** mechanism: it classifies problems into four mathematical categories (Geometry, Algebra, Set Theory & Combinatorics, Number Theory), then constructs domain-specific static context from Mathlib once per category. This context -- containing relevant Mathlib definitions -- is injected into prompts during formalization, conditioning the LLM's generation on the mathematical subdomain.

**However, this is NOT a direct competitor because:**
1. IndiMathBench is primarily a **benchmark**, not an autoformalization system. The category-specific context is one implementation detail of their benchmark curation pipeline.
2. The domain conditioning is limited to **static context retrieval** (which Mathlib modules to include in the prompt), not a full pipeline adaptation (different prompts, different repair strategies, different error taxonomies, etc.).
3. The paper does **not claim novelty** in domain conditioning -- it is not framed as the paper's contribution.
4. It covers only **4 coarse categories** from olympiad math, not a systematic taxonomy of mathematical subdomains.

The proposal should cite IndiMathBench and differentiate from it explicitly.

---

### Other Papers Examined and Why They Do NOT Do Domain-Conditioned Autoformalization

| Paper | What it does | Why it's not domain-conditioned |
|-------|-------------|-------------------------------|
| **ATLAS** (Feb 2025) | Organizes Mathlib into 13 domains/55 topics/350 concepts | Domain structure used only for **training data generation**, not inference-time conditioning |
| **CRAMF** (2025) | Uses "domain- and application-level signals" for retrieval | "Domain" means problem-specific context derived dynamically, not mathematical subdomain classification |
| **DRIFT** (Oct 2025) | Decompose, retrieve, illustrate, formalize | Uniform pipeline; adaptation is model-specific, not domain-specific |
| **130k Topology** (Jan 2026) | Autoformalized Munkres topology textbook | Applied to one domain (topology) but no domain-conditioning mechanism |
| **MMFormalizer** (Jan 2026) | Multimodal autoformalization | Uses "adaptive recursive termination" uniformly across domains |
| **StepFun-Formalizer** (AAAI 2026) | Knowledge-reasoning fusion | Domain-agnostic pipeline; no subdomain conditioning |
| **ReForm** (Oct 2025) | Reflective autoformalization with self-validation | Domain-agnostic iterative process |
| **FormaRL** (Aug 2025) | RL-based autoformalization | Domain-agnostic RL training |
| **ProofBridge** (Oct 2025) | Joint embeddings for NL-to-FL | Unified cross-modal retrieval, no domain conditioning |
| **MerLean** (Feb 2026) | Agentic autoformalization for quantum computation | Domain-specific application, but not domain-*conditioned* (authors say it generalizes) |
| **PhysProver** (Jan 2026) | Theorem proving for physics | Domain-specific training but not domain-conditioned autoformalization |
| **Lean Atlas** (Mar 2026) | Human-AI collaborative formalization environment | Domain-agnostic tool infrastructure |
| **Cycle Consistency** (Mar 2026) | Curriculum learning + RL for autoformalization | Observes domain-dependent performance but pipeline is domain-agnostic |
| **Autoformalization Survey** (May 2025) | Comprehensive survey of 81+ papers | Identifies domain-specific challenges but reports **no system** that conditions on subdomain |

---

### Key Finding from the Survey Paper

The [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486) (May 2025) explicitly identifies that "each domain has its own unique characteristics" and that autoformalization "must adapt to different semantic structures, input modalities, and reasoning paradigms" -- but it catalogs this as an **open challenge**, not a solved problem. No system in the survey implements domain conditioning.

---

### Recommendation for the Proposal

1. **The novelty claim is defensible.** No existing system conditions its full autoformalization pipeline on mathematical subdomain as a primary design choice.
2. **Cite IndiMathBench** and differentiate clearly. IndiMathBench uses per-category static context from Mathlib, which is a lightweight form of domain conditioning within a benchmark curation pipeline. The proposal should argue that it goes further -- with domain-specific prompts, repair strategies, error taxonomies, and systematic coverage beyond 4 olympiad categories.
3. **Cite ATLAS** to acknowledge that Mathlib's domain structure (13 domains, 55 topics, 350 concepts) has been used for data organization, even if not for inference-time conditioning.
4. **Cite CRAMF** to acknowledge that "domain-level signals" have been used in retrieval, even though their "domain" means something different (problem-specific context, not mathematical subdomain).
5. **Cite the survey** to support the claim that domain-adaptive autoformalization is an identified open problem.

agentId: a6bd6e052a2d55f83 (use SendMessage with to: 'a6bd6e052a2d55f83' to continue this agent)
&lt;usage>total_tokens: 40546
tool_uses: 46
duration_ms: 257503&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db8a8210-1a33-4174-b335-bae7605b7c00",
  "isSidechain": false,
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "b7bf7fd3-7e6b-435c-895c-e57b88bc504b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping review a research proposal about \"domain-adaptive autoformalization\" — the idea of conditioning autoformalization pipelines (translating natural language math to formal Lean 4 code) on mathematical subdomain (algebra, topology, analysis, etc.).\n\nI need you to search exhaustively for competing or concurrent work that might already address this gap. The proposal claims NO existing system conditions its autoformalization pipeline on mathematical subdomain. Search for work that might contradict this.\n\nUse WebSearch for each of these searches:\n\n1. \"domain adaptive autoformalization\" OR \"domain-specific autoformalization\" 2025 2026\n2. \"subdomain\" \"autoformalization\" Lean Mathlib 2026\n3. \"domain-conditioned\" OR \"domain-aware\" formalization theorem proving 2026\n4. site:arxiv.org \"autoformalization\" \"domain\" 2026\n5. site:openreview.net autoformalization domain adaptation 2026\n6. \"mathematical domain\" \"formalization\" \"retrieval\" conditioning 2026\n7. \"Mathlib\" \"module hierarchy\" \"domain\" autoformalization\n8. \"error taxonomy\" autoformalization Lean 2025 2026\n9. \"domain-stratified\" OR \"domain-specific\" \"repair\" formalization 2026\n10. \"cross-domain\" autoformalization generalization 2026\n\nFor any promising results, use WebFetch to read the abstracts and determine if they actually do domain-conditioned autoformalization.\n\nReport: Did you find ANY paper that already does what this proposal claims to be the first to do (conditioning the autoformalization pipeline on mathematical subdomain)?",
    "agentId": "a6bd6e052a2d55f83",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive results. Let me compile my findings.\n\n---\n\n## Report: Does Any Existing Work Do Domain-Conditioned Autoformalization?\n\nAfter conducting 17 web searches and fetching/analyzing 14 papers in detail, here is my assessment:\n\n### Short answer: No existing paper makes domain-conditioned autoformalization its primary contribution. The proposal's novelty claim appears to hold, with one partial caveat.\n\n---\n\n### The One Partial Caveat: IndiMathBench (December 2025)\n\n**Paper:** [IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch](https://arxiv.org/abs/2512.00997) (Microsoft Research, published at ICLR 2026)\n\nThis is the closest thing I found. IndiMathBench's pipeline includes a **category-specific context** mechanism: it classifies problems into four mathematical categories (Geometry, Algebra, Set Theory & Combinatorics, Number Theory), then constructs domain-specific static context from Mathlib once per category. This context -- containing relevant Mathlib definitions -- is injected into prompts during formalization, conditioning the LLM's generation on the mathematical subdomain.\n\n**However, this is NOT a direct competitor because:**\n1. IndiMathBench is primarily a **benchmark**, not an autoformalization system. The category-specific context is one implementation detail of their benchmark curation pipeline.\n2. The domain conditioning is limited to **static context retrieval** (which Mathlib modules to include in the prompt), not a full pipeline adaptation (different prompts, different repair strategies, different error taxonomies, etc.).\n3. The paper does **not claim novelty** in domain conditioning -- it is not framed as the paper's contribution.\n4. It covers only **4 coarse categories** from olympiad math, not a systematic taxonomy of mathematical subdomains.\n\nThe proposal should cite IndiMathBench and differentiate from it explicitly.\n\n---\n\n### Other Papers Examined and Why They Do NOT Do Domain-Conditioned Autoformalization\n\n| Paper | What it does | Why it's not domain-conditioned |\n|-------|-------------|-------------------------------|\n| **ATLAS** (Feb 2025) | Organizes Mathlib into 13 domains/55 topics/350 concepts | Domain structure used only for **training data generation**, not inference-time conditioning |\n| **CRAMF** (2025) | Uses \"domain- and application-level signals\" for retrieval | \"Domain\" means problem-specific context derived dynamically, not mathematical subdomain classification |\n| **DRIFT** (Oct 2025) | Decompose, retrieve, illustrate, formalize | Uniform pipeline; adaptation is model-specific, not domain-specific |\n| **130k Topology** (Jan 2026) | Autoformalized Munkres topology textbook | Applied to one domain (topology) but no domain-conditioning mechanism |\n| **MMFormalizer** (Jan 2026) | Multimodal autoformalization | Uses \"adaptive recursive termination\" uniformly across domains |\n| **StepFun-Formalizer** (AAAI 2026) | Knowledge-reasoning fusion | Domain-agnostic pipeline; no subdomain conditioning |\n| **ReForm** (Oct 2025) | Reflective autoformalization with self-validation | Domain-agnostic iterative process |\n| **FormaRL** (Aug 2025) | RL-based autoformalization | Domain-agnostic RL training |\n| **ProofBridge** (Oct 2025) | Joint embeddings for NL-to-FL | Unified cross-modal retrieval, no domain conditioning |\n| **MerLean** (Feb 2026) | Agentic autoformalization for quantum computation | Domain-specific application, but not domain-*conditioned* (authors say it generalizes) |\n| **PhysProver** (Jan 2026) | Theorem proving for physics | Domain-specific training but not domain-conditioned autoformalization |\n| **Lean Atlas** (Mar 2026) | Human-AI collaborative formalization environment | Domain-agnostic tool infrastructure |\n| **Cycle Consistency** (Mar 2026) | Curriculum learning + RL for autoformalization | Observes domain-dependent performance but pipeline is domain-agnostic |\n| **Autoformalization Survey** (May 2025) | Comprehensive survey of 81+ papers | Identifies domain-specific challenges but reports **no system** that conditions on subdomain |\n\n---\n\n### Key Finding from the Survey Paper\n\nThe [Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486) (May 2025) explicitly identifies that \"each domain has its own unique characteristics\" and that autoformalization \"must adapt to different semantic structures, input modalities, and reasoning paradigms\" -- but it catalogs this as an **open challenge**, not a solved problem. No system in the survey implements domain conditioning.\n\n---\n\n### Recommendation for the Proposal\n\n1. **The novelty claim is defensible.** No existing system conditions its full autoformalization pipeline on mathematical subdomain as a primary design choice.\n2. **Cite IndiMathBench** and differentiate clearly. IndiMathBench uses per-category static context from Mathlib, which is a lightweight form of domain conditioning within a benchmark curation pipeline. The proposal should argue that it goes further -- with domain-specific prompts, repair strategies, error taxonomies, and systematic coverage beyond 4 olympiad categories.\n3. **Cite ATLAS** to acknowledge that Mathlib's domain structure (13 domains, 55 topics, 350 concepts) has been used for data organization, even if not for inference-time conditioning.\n4. **Cite CRAMF** to acknowledge that \"domain-level signals\" have been used in retrieval, even though their \"domain\" means something different (problem-specific context, not mathematical subdomain).\n5. **Cite the survey** to support the claim that domain-adaptive autoformalization is an identified open problem."
      }
    ],
    "totalDurationMs": 257503,
    "totalTokens": 40546,
    "totalToolUseCount": 46,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2458,
      "cache_read_input_tokens": 36684,
      "output_tokens": 1403,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2458
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1403,
          "cache_read_input_tokens": 36684,
          "cache_creation_input_tokens": 2458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2458,
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
      "otherToolCount": 46
    }
  },
  "sourceToolAssistantUUID": "db8a8210-1a33-4174-b335-bae7605b7c00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "b7bf7fd3-7e6b-435c-895c-e57b88bc504b",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization via subdomain conditioning",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Tool call

_source line 16 · 2026-05-28T13:10:06.516Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013aD1tS2wQruhsCm5qss7Ro`</summary>

```json
{
  "description": "Verify feasibility and resources",
  "subagent_type": "general-purpose",
  "prompt": "You are helping review a research proposal about domain-adaptive autoformalization. I need you to verify feasibility claims.\n\nPlease search for and verify the following:\n\n1. **Goedel-Formalizer-V2-8B availability**: Search for whether this model exists and is publicly available. The proposal plans to use it as the backbone. Search \"Goedel-Formalizer-V2\" and \"Goedel-Prover-V2\" on arXiv and GitHub.\n\n2. **APRIL dataset availability**: Search for the APRIL paper (arXiv 2602.02990) and check if the 260k repair tuples are publicly released or only described in the paper.\n\n3. **Herald dataset availability**: Check if Herald's 580k NL-formal pairs are publicly available.\n\n4. **FineLeanCorpus/CriticLean availability**: Check if the 286k verified entries are publicly available.\n\n5. **CRAMF code/data availability**: Check if CRAMF's knowledge base and code are open-source.\n\n6. **Compute estimate realism**: Search for typical compute costs for LoRA fine-tuning of 8B parameter models and Lean4 compilation throughput. Is 80h of H100 time reasonable for LoRA fine-tuning an 8B model on ~500k examples? Is 50h reasonable for evaluating across 5 domains × 3 benchmarks with Lean4 compilation?\n\n7. **AAAI 2026 deadline**: Search for AAAI 2026 actual deadlines to verify whether the user's original target of AAAI 2026 is still viable or already past. Also check AAAI 2027 and ICLR 2027 deadlines.\n\n8. **Lean4 compilation speed**: Search for typical Lean4 type-checking throughput (statements per second/minute) to validate the evaluation time estimate.\n\nReport all findings with sources."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7bf7fd3-7e6b-435c-895c-e57b88bc504b",
  "isSidechain": false,
  "requestId": "req_011CbV2CEkkXYy4Lxyj1hDYK",
  "type": "assistant",
  "uuid": "3d94c4df-7a60-46f5-9f4d-e38f91da40ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiiTAut7Vubrr2LyaqECJu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 29342,
      "output_tokens": 543,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 543,
          "cache_read_input_tokens": 29342,
          "cache_creation_input_tokens": 1949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1949
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

_source line 17 · 2026-05-28T13:13:20.792Z_

<details><summary>↩ Tool result · `toolu_013aD1tS2wQruhsCm5qss7Ro`</summary>

```text
Now I have enough information to compile a comprehensive report. Here are my findings:

---

## Feasibility Verification Report

### 1. Goedel-Formalizer-V2-8B Availability

**CONFIRMED: Publicly available.**

The model exists on Hugging Face at [Goedel-LM/Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B). It is a fine-tune of Qwen3-8B, released under Apache 2.0 license, with weights in safetensors/BF16 format. The related Goedel-Prover-V2 project has a GitHub repository at [Goedel-LM/Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2), and the companion paper is [arXiv 2508.03613](https://arxiv.org/abs/2508.03613). On the Omni-MATH evaluation (300 statements), the 8B formalizer achieves 228/300, and the 32B variant achieves even higher. This is a viable and well-supported backbone choice.

### 2. APRIL Dataset (arXiv 2602.02990)

**CONFIRMED: Publicly available.**

The paper "Learning to Repair Lean Proofs from Compiler Feedback" ([arXiv 2602.02990](https://arxiv.org/abs/2602.02990)) introduces APRIL (Automated Proof Repair in Lean), containing 260k supervised tuples pairing proof failures with compiler diagnostics and repair targets. The dataset is publicly released on Hugging Face at [uw-math-ai/APRIL](https://huggingface.co/datasets/uw-math-ai/APRIL). The paper was submitted February 2026 with v2 in March 2026. This is a usable resource.

### 3. Herald Dataset

**CONFIRMED: Publicly available.**

Herald (arXiv [2410.10878](https://arxiv.org/abs/2410.10878), accepted at ICLR 2025) provides 580k NL-FL statement pairs and 45k NL-FL proof pairs derived from Mathlib4. The dataset is released on Hugging Face (via the FrenzyMath organization), and the translator code is at [github.com/frenzymath/herald_translator](https://github.com/frenzymath/herald_translator). This is a fully accessible resource.

### 4. FineLeanCorpus / CriticLean

**PARTIALLY CONFIRMED: Available, but with a discrepancy in numbers.**

FineLeanCorpus is publicly available at [m-a-p/FineLeanCorpus](https://huggingface.co/datasets/m-a-p/FineLeanCorpus) under Apache 2.0 license. However, there is a discrepancy: the CriticLean paper ([arXiv 2507.06181](https://arxiv.org/abs/2507.06181)) and GitHub repo describe 285,957 verified entries, but the Hugging Face dataset page lists **509,356 rows**. The proposal claims "286k verified entries," which matches the paper's figure, but the actual dataset on HuggingFace is larger (509k). The CriticLean code, model, and benchmark are all publicly available on GitHub at [multimodal-art-projection/CriticLean](https://github.com/multimodal-art-projection/CriticLean). The "286k verified entries" likely refers to the semantically verified subset, while the full corpus is larger. This should be clarified in the proposal.

### 5. CRAMF Code/Data Availability

**PARTIALLY AVAILABLE: Anonymized repo exists, but limited.**

The CRAMF paper ([arXiv 2508.06931](https://arxiv.org/abs/2508.06931)) provides an anonymized GitHub repository at [github.com/kahvia0526/CRAMF](https://github.com/kahvia0526/CRAMF). The repo is publicly accessible and contains Python code for concept abstraction/analysis, data, evaluation, generation, and retrieval. However, the repo is minimal (4 commits, 1 star, 0 forks, no description, no releases). It is unclear whether the full concept-definition knowledge base (26k+ definitions) is included in the `data/` directory or must be reconstructed. The proposal should note that this is an anonymized/early-stage release and may require additional effort to reproduce or integrate.

### 6. Compute Estimate Realism

**80h of H100 time for LoRA fine-tuning on ~500k examples: CONSERVATIVE (likely an overestimate).**

Based on real-world benchmarks:
- A case study showed LoRA rank-128 fine-tuning on 500k examples on H100 infrastructure took **17.2 hours** per job (cost ~$89).
- LoRA on an 8B model with ~1k examples takes 1-2 hours on a single A100; scaling to 500k with longer sequences and higher ranks would increase this, but 80 hours on H100 appears generous by a factor of 3-4x, even accounting for multiple training runs, hyperparameter sweeps, and iterative refinement stages.
- If the 80h budget includes multiple LoRA training rounds (e.g., initial training + domain-specific adaptation + refinement), it becomes more reasonable.

**Verdict:** The 80h figure is safe/conservative. It provides ample room for multiple training iterations, which is actually a strength for a proposal (underpromising).

**50h for evaluation across 5 domains x 3 benchmarks with Lean4 compilation: PLAUSIBLE but tight.**

Key factors:
- Lean4 type-checking timeouts in autoformalization evaluations are typically set at **300-600 seconds per statement** (some benchmarks use 10-minute timeouts).
- If evaluating, say, 500 statements per domain-benchmark combination (5 x 3 = 15 combinations = 7,500 statements), with an average of ~60-120 seconds per statement (including failures that hit timeouts), that is roughly 125-250 hours of single-core CPU time.
- However, Lean4 compilation is parallelizable across CPUs, and using a multi-core server or cluster with 8-60 CPUs (as in Kimina Lean Server setups) would bring this down to 2-30 hours.
- With parallelization on a well-provisioned cluster, 50h of compute is plausible, though it depends heavily on the number of test statements and timeout settings.

**Verdict:** 50h is plausible if using parallelized verification and moderate-sized benchmarks, but could be tight if benchmarks are large or timeouts are long.

### 7. Conference Deadlines

**AAAI 2026: ALREADY PAST.**

AAAI 2026 deadlines were:
- Abstract due: July 25, 2025
- Full paper due: August 1, 2025
- Conference: January 20-27, 2026 in Singapore

The proposal's target of AAAI 2026 is **no longer viable** as of today (May 28, 2026). The conference has already taken place.

**AAAI 2027: VIABLE.**

AAAI 2027 (Montreal, February 16-23, 2027) has these deadlines:
- Abstract due: **July 21, 2026**
- Full paper due: **July 28, 2026**
- Notification: November 30, 2026

This gives approximately **8 weeks from today**, which is tight but feasible if research is already substantially underway.

**ICLR 2027: LIKELY VIABLE.**

ICLR 2027 has not yet announced official deadlines. Based on ICLR 2026 patterns (submission deadline September 24, 2025 for April 2026 conference), ICLR 2027 would likely have a submission deadline around **September-October 2026**, giving approximately 4-5 months. This is a more comfortable timeline.

### 8. Lean4 Compilation Speed

**Limited public benchmarks, but reasonable estimates exist.**

Specific per-statement throughput numbers are not widely published, but:
- Autoformalization evaluation benchmarks typically use **5-10 minute timeouts** per theorem (one benchmark explicitly mentions a 10-minute cap per theorem).
- The Lean4Lean typechecker (pure Lean implementation) is ~30% slower than the native C++ kernel.
- Full Mathlib4 compilation takes hours on multi-core machines (it contains ~130k+ declarations).
- For simpler individual statements (as opposed to full proofs depending on extensive Mathlib imports), type-checking can complete in seconds to low tens of seconds.
- The Kimina Lean Server demonstrates near-linear CPU scaling for batch verification across 8-60 CPUs with LRU caching providing 41% per-iteration time savings.

**For evaluation budget estimation:** A reasonable rule of thumb is 30-120 seconds average per statement (including import overhead and timeouts for failures), heavily parallelizable. The proposal's 50h estimate for evaluation is workable with adequate CPU parallelism but should explicitly state assumptions about parallelism and timeout settings.

---

### Summary of Risks

| Item | Status | Risk Level |
|------|--------|------------|
| Goedel-Formalizer-V2-8B | Publicly available, Apache 2.0 | Low |
| APRIL dataset | Publicly available on HuggingFace | Low |
| Herald dataset | Publicly available | Low |
| FineLeanCorpus/CriticLean | Available, but size discrepancy (286k vs 509k) | Low (clarify numbers) |
| CRAMF code/data | Anonymized repo, minimal, may need reconstruction | Medium |
| 80h H100 LoRA training | Conservative estimate (likely needs ~20-40h) | Low |
| 50h Lean4 evaluation | Plausible with parallelization, tight without | Medium |
| AAAI 2026 | Deadline passed, conference already held | Blocker |
| AAAI 2027 | Deadline July 28, 2026 (~8 weeks away) | Medium-High (tight) |
| ICLR 2027 | Likely Sept/Oct 2026 (~4-5 months away) | Low |

**Key recommendation:** Retarget the submission to ICLR 2027 (likely deadline ~September/October 2026) for a comfortable timeline, or AAAI 2027 (July 28, 2026 deadline) if the work is nearly complete. The AAAI 2026 target is no longer possible.

agentId: a4e185490d6269fc9 (use SendMessage with to: 'a4e185490d6269fc9' to continue this agent)
&lt;usage>total_tokens: 35833
tool_uses: 34
duration_ms: 194271&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d94c4df-7a60-46f5-9f4d-e38f91da40ce",
  "isSidechain": false,
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "88bcc123-2ff3-4376-a494-88df2d7060c0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping review a research proposal about domain-adaptive autoformalization. I need you to verify feasibility claims.\n\nPlease search for and verify the following:\n\n1. **Goedel-Formalizer-V2-8B availability**: Search for whether this model exists and is publicly available. The proposal plans to use it as the backbone. Search \"Goedel-Formalizer-V2\" and \"Goedel-Prover-V2\" on arXiv and GitHub.\n\n2. **APRIL dataset availability**: Search for the APRIL paper (arXiv 2602.02990) and check if the 260k repair tuples are publicly released or only described in the paper.\n\n3. **Herald dataset availability**: Check if Herald's 580k NL-formal pairs are publicly available.\n\n4. **FineLeanCorpus/CriticLean availability**: Check if the 286k verified entries are publicly available.\n\n5. **CRAMF code/data availability**: Check if CRAMF's knowledge base and code are open-source.\n\n6. **Compute estimate realism**: Search for typical compute costs for LoRA fine-tuning of 8B parameter models and Lean4 compilation throughput. Is 80h of H100 time reasonable for LoRA fine-tuning an 8B model on ~500k examples? Is 50h reasonable for evaluating across 5 domains × 3 benchmarks with Lean4 compilation?\n\n7. **AAAI 2026 deadline**: Search for AAAI 2026 actual deadlines to verify whether the user's original target of AAAI 2026 is still viable or already past. Also check AAAI 2027 and ICLR 2027 deadlines.\n\n8. **Lean4 compilation speed**: Search for typical Lean4 type-checking throughput (statements per second/minute) to validate the evaluation time estimate.\n\nReport all findings with sources.",
    "agentId": "a4e185490d6269fc9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a comprehensive report. Here are my findings:\n\n---\n\n## Feasibility Verification Report\n\n### 1. Goedel-Formalizer-V2-8B Availability\n\n**CONFIRMED: Publicly available.**\n\nThe model exists on Hugging Face at [Goedel-LM/Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B). It is a fine-tune of Qwen3-8B, released under Apache 2.0 license, with weights in safetensors/BF16 format. The related Goedel-Prover-V2 project has a GitHub repository at [Goedel-LM/Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2), and the companion paper is [arXiv 2508.03613](https://arxiv.org/abs/2508.03613). On the Omni-MATH evaluation (300 statements), the 8B formalizer achieves 228/300, and the 32B variant achieves even higher. This is a viable and well-supported backbone choice.\n\n### 2. APRIL Dataset (arXiv 2602.02990)\n\n**CONFIRMED: Publicly available.**\n\nThe paper \"Learning to Repair Lean Proofs from Compiler Feedback\" ([arXiv 2602.02990](https://arxiv.org/abs/2602.02990)) introduces APRIL (Automated Proof Repair in Lean), containing 260k supervised tuples pairing proof failures with compiler diagnostics and repair targets. The dataset is publicly released on Hugging Face at [uw-math-ai/APRIL](https://huggingface.co/datasets/uw-math-ai/APRIL). The paper was submitted February 2026 with v2 in March 2026. This is a usable resource.\n\n### 3. Herald Dataset\n\n**CONFIRMED: Publicly available.**\n\nHerald (arXiv [2410.10878](https://arxiv.org/abs/2410.10878), accepted at ICLR 2025) provides 580k NL-FL statement pairs and 45k NL-FL proof pairs derived from Mathlib4. The dataset is released on Hugging Face (via the FrenzyMath organization), and the translator code is at [github.com/frenzymath/herald_translator](https://github.com/frenzymath/herald_translator). This is a fully accessible resource.\n\n### 4. FineLeanCorpus / CriticLean\n\n**PARTIALLY CONFIRMED: Available, but with a discrepancy in numbers.**\n\nFineLeanCorpus is publicly available at [m-a-p/FineLeanCorpus](https://huggingface.co/datasets/m-a-p/FineLeanCorpus) under Apache 2.0 license. However, there is a discrepancy: the CriticLean paper ([arXiv 2507.06181](https://arxiv.org/abs/2507.06181)) and GitHub repo describe 285,957 verified entries, but the Hugging Face dataset page lists **509,356 rows**. The proposal claims \"286k verified entries,\" which matches the paper's figure, but the actual dataset on HuggingFace is larger (509k). The CriticLean code, model, and benchmark are all publicly available on GitHub at [multimodal-art-projection/CriticLean](https://github.com/multimodal-art-projection/CriticLean). The \"286k verified entries\" likely refers to the semantically verified subset, while the full corpus is larger. This should be clarified in the proposal.\n\n### 5. CRAMF Code/Data Availability\n\n**PARTIALLY AVAILABLE: Anonymized repo exists, but limited.**\n\nThe CRAMF paper ([arXiv 2508.06931](https://arxiv.org/abs/2508.06931)) provides an anonymized GitHub repository at [github.com/kahvia0526/CRAMF](https://github.com/kahvia0526/CRAMF). The repo is publicly accessible and contains Python code for concept abstraction/analysis, data, evaluation, generation, and retrieval. However, the repo is minimal (4 commits, 1 star, 0 forks, no description, no releases). It is unclear whether the full concept-definition knowledge base (26k+ definitions) is included in the `data/` directory or must be reconstructed. The proposal should note that this is an anonymized/early-stage release and may require additional effort to reproduce or integrate.\n\n### 6. Compute Estimate Realism\n\n**80h of H100 time for LoRA fine-tuning on ~500k examples: CONSERVATIVE (likely an overestimate).**\n\nBased on real-world benchmarks:\n- A case study showed LoRA rank-128 fine-tuning on 500k examples on H100 infrastructure took **17.2 hours** per job (cost ~$89).\n- LoRA on an 8B model with ~1k examples takes 1-2 hours on a single A100; scaling to 500k with longer sequences and higher ranks would increase this, but 80 hours on H100 appears generous by a factor of 3-4x, even accounting for multiple training runs, hyperparameter sweeps, and iterative refinement stages.\n- If the 80h budget includes multiple LoRA training rounds (e.g., initial training + domain-specific adaptation + refinement), it becomes more reasonable.\n\n**Verdict:** The 80h figure is safe/conservative. It provides ample room for multiple training iterations, which is actually a strength for a proposal (underpromising).\n\n**50h for evaluation across 5 domains x 3 benchmarks with Lean4 compilation: PLAUSIBLE but tight.**\n\nKey factors:\n- Lean4 type-checking timeouts in autoformalization evaluations are typically set at **300-600 seconds per statement** (some benchmarks use 10-minute timeouts).\n- If evaluating, say, 500 statements per domain-benchmark combination (5 x 3 = 15 combinations = 7,500 statements), with an average of ~60-120 seconds per statement (including failures that hit timeouts), that is roughly 125-250 hours of single-core CPU time.\n- However, Lean4 compilation is parallelizable across CPUs, and using a multi-core server or cluster with 8-60 CPUs (as in Kimina Lean Server setups) would bring this down to 2-30 hours.\n- With parallelization on a well-provisioned cluster, 50h of compute is plausible, though it depends heavily on the number of test statements and timeout settings.\n\n**Verdict:** 50h is plausible if using parallelized verification and moderate-sized benchmarks, but could be tight if benchmarks are large or timeouts are long.\n\n### 7. Conference Deadlines\n\n**AAAI 2026: ALREADY PAST.**\n\nAAAI 2026 deadlines were:\n- Abstract due: July 25, 2025\n- Full paper due: August 1, 2025\n- Conference: January 20-27, 2026 in Singapore\n\nThe proposal's target of AAAI 2026 is **no longer viable** as of today (May 28, 2026). The conference has already taken place.\n\n**AAAI 2027: VIABLE.**\n\nAAAI 2027 (Montreal, February 16-23, 2027) has these deadlines:\n- Abstract due: **July 21, 2026**\n- Full paper due: **July 28, 2026**\n- Notification: November 30, 2026\n\nThis gives approximately **8 weeks from today**, which is tight but feasible if research is already substantially underway.\n\n**ICLR 2027: LIKELY VIABLE.**\n\nICLR 2027 has not yet announced official deadlines. Based on ICLR 2026 patterns (submission deadline September 24, 2025 for April 2026 conference), ICLR 2027 would likely have a submission deadline around **September-October 2026**, giving approximately 4-5 months. This is a more comfortable timeline.\n\n### 8. Lean4 Compilation Speed\n\n**Limited public benchmarks, but reasonable estimates exist.**\n\nSpecific per-statement throughput numbers are not widely published, but:\n- Autoformalization evaluation benchmarks typically use **5-10 minute timeouts** per theorem (one benchmark explicitly mentions a 10-minute cap per theorem).\n- The Lean4Lean typechecker (pure Lean implementation) is ~30% slower than the native C++ kernel.\n- Full Mathlib4 compilation takes hours on multi-core machines (it contains ~130k+ declarations).\n- For simpler individual statements (as opposed to full proofs depending on extensive Mathlib imports), type-checking can complete in seconds to low tens of seconds.\n- The Kimina Lean Server demonstrates near-linear CPU scaling for batch verification across 8-60 CPUs with LRU caching providing 41% per-iteration time savings.\n\n**For evaluation budget estimation:** A reasonable rule of thumb is 30-120 seconds average per statement (including import overhead and timeouts for failures), heavily parallelizable. The proposal's 50h estimate for evaluation is workable with adequate CPU parallelism but should explicitly state assumptions about parallelism and timeout settings.\n\n---\n\n### Summary of Risks\n\n| Item | Status | Risk Level |\n|------|--------|------------|\n| Goedel-Formalizer-V2-8B | Publicly available, Apache 2.0 | Low |\n| APRIL dataset | Publicly available on HuggingFace | Low |\n| Herald dataset | Publicly available | Low |\n| FineLeanCorpus/CriticLean | Available, but size discrepancy (286k vs 509k) | Low (clarify numbers) |\n| CRAMF code/data | Anonymized repo, minimal, may need reconstruction | Medium |\n| 80h H100 LoRA training | Conservative estimate (likely needs ~20-40h) | Low |\n| 50h Lean4 evaluation | Plausible with parallelization, tight without | Medium |\n| AAAI 2026 | Deadline passed, conference already held | Blocker |\n| AAAI 2027 | Deadline July 28, 2026 (~8 weeks away) | Medium-High (tight) |\n| ICLR 2027 | Likely Sept/Oct 2026 (~4-5 months away) | Low |\n\n**Key recommendation:** Retarget the submission to ICLR 2027 (likely deadline ~September/October 2026) for a comfortable timeline, or AAAI 2027 (July 28, 2026 deadline) if the work is nearly complete. The AAAI 2026 target is no longer possible."
      }
    ],
    "totalDurationMs": 194271,
    "totalTokens": 35833,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1338,
      "cache_read_input_tokens": 31859,
      "output_tokens": 2635,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1338
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2635,
          "cache_read_input_tokens": 31859,
          "cache_creation_input_tokens": 1338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1338,
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
      "otherToolCount": 34
    }
  },
  "sourceToolAssistantUUID": "3d94c4df-7a60-46f5-9f4d-e38f91da40ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T13:13:32.074Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LQGE7xtTwycVJBw5Kk2GtP`</summary>

```json
{
  "description": "Check additional concurrent work",
  "subagent_type": "general-purpose",
  "prompt": "You are helping review a research proposal about domain-adaptive autoformalization. I need to check for very recent work (March-May 2026) that might scoop or overlap with this proposal. The proposal claims to be the first to condition autoformalization on mathematical subdomain.\n\nPlease search for:\n\n1. Search \"autoformalization 2026\" on arXiv — look for papers from March-May 2026 specifically\n2. Search \"IndiMathBench\" — this paper uses category-specific context in autoformalization; verify details\n3. Search for \"Kimina-Autoformalizer\" — mentioned as a baseline in Aria's results\n4. Search \"domain adaptation theorem proving\" 2026\n5. Search for \"Goedel-Formalizer\" to check if there are newer versions or domain-specific variants\n6. Search \"FormalMATH benchmark domain\" to verify the per-domain accuracy claims (50% algebra, 0% discrete math for Goedel-Prover)\n7. Search for any recent survey papers on autoformalization from 2025-2026 that might catalog the landscape\n\nFor each paper found, briefly note whether it contradicts the proposal's novelty claims.\n\nAlso specifically check: Does the Goedel-Formalizer-V2-8B model description mention anything about domain-specific training or domain awareness?\n\nReport findings comprehensively."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88bcc123-2ff3-4376-a494-88df2d7060c0",
  "isSidechain": false,
  "requestId": "req_011CbV2TcyecjztgADR74uDJ",
  "type": "assistant",
  "uuid": "fe724b76-7c3d-45ac-a0b5-4619af61649c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bzbcdna6xyFnFVCiKWfMkJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3255,
      "cache_read_input_tokens": 31291,
      "output_tokens": 406,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 406,
          "cache_read_input_tokens": 31291,
          "cache_creation_input_tokens": 3255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3255
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

_source line 19 · 2026-05-28T13:16:21.510Z_

<details><summary>↩ Tool result · `toolu_01LQGE7xtTwycVJBw5Kk2GtP`</summary>

```text
Now I have comprehensive data. Here is the full report.

---

## Comprehensive Literature Search Report: Domain-Adaptive Autoformalization (March--May 2026)

### 1. Recent Autoformalization Papers on arXiv (March--May 2026)

Several new autoformalization papers appeared in this window:

- **[Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning](https://arxiv.org/abs/2603.24372)** (March 25, 2026) -- Uses RL with cycle consistency as a reward signal. Does NOT address domain-specific or domain-adaptive autoformalization. General-purpose approach.

- **[FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization](https://arxiv.org/abs/2603.19828)** (March 20, 2026) -- A compilation-gated evolutionary framework for generating diverse formalization candidates. Does NOT condition on mathematical subdomain. Evaluates on general benchmarks (CombiBench, ProofNet).

- **[Agent Hunt: Bounty Based Collaborative Autoformalization With LLM Agents](https://arxiv.org/abs/2603.06737)** (March 6, 2026) -- Multi-agent bounty-based autoformalization of algebraic topology. Domain-specific in the sense that it targets algebraic topology, but does NOT propose a general domain-adaptation framework.

- **[MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)** (May 2026) -- 52k theorems from 103 graduate textbooks with a 178k-relation dependency graph. Does NOT condition on subdomain; treats mathematics as a unified domain. Focuses on dependency-aware evaluation rather than domain-adaptive generation.

- **[MerLean: An Agentic Framework for Autoformalization in Quantum Computation](https://arxiv.org/abs/2602.16554)** (February 2026) -- Domain-specific to quantum computation but is an application paper, not a domain-adaptation methodology.

**Verdict on novelty threat from these papers:** None of these papers propose conditioning autoformalization on mathematical subdomain as a general methodology. The proposal's novelty claim appears safe against these.

---

### 2. IndiMathBench -- Category-Specific Context in Autoformalization

**Paper:** [IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch](https://arxiv.org/abs/2512.00997) (December 2025)

**THIS IS THE MOST SIGNIFICANT OVERLAP.** IndiMathBench uses **category-based retrieval** that conditions autoformalization on four mathematical categories: Geometry (98 problems), Algebra (92), Set Theory & Combinatorics (45), and Number Theory (77).

How it works:
- Each problem is labeled by category (LLM + human verification)
- 25% of problems per category are sampled; a Claude Sonnet 4-based agent extracts relevant Mathlib definitions/formulas specific to that domain
- This category-specific documentation becomes static context reused for all problems in that domain
- The authors explicitly state: "This context anchors the model with domain knowledge within each category, preventing hallucinations and syntax errors"

**Impact on novelty claim:** This IS effectively domain-adaptive autoformalization -- the system conditions its prompts on mathematical subdomain, providing domain-specific library context. The proposal's claim of being "the first to condition autoformalization on mathematical subdomain" is directly contradicted by this work. However, IndiMathBench's approach is retrieval-augmentation-based (prompt engineering with domain-specific library snippets), not fine-tuning or architectural conditioning. If the proposal's method involves model-level domain conditioning (fine-tuning, domain tokens, etc.), there is a distinction to be made, but the high-level claim needs to be qualified.

---

### 3. Kimina-Autoformalizer

**Model:** [Kimina-Autoformalizer-7B](https://huggingface.co/AI-MO/Kimina-Autoformalizer-7B) by Project Numina / AI-MO

- 7B parameter model for translating natural language competition problems to Lean 4
- Trained via SFT + structured expert iteration with LLM-based judging
- Part of the Kimina-Prover family (up to 72B)
- On 300 Omni-MATH statements: Kimina-Autoformalizer-7B successfully translated 161 statements
- Does NOT use domain-specific conditioning or domain adaptation
- General-purpose competition math autoformalization

**Impact on novelty:** Does not threaten the domain-adaptive claim. Confirmed as a reasonable baseline.

---

### 4. Domain Adaptation + Theorem Proving (2026)

No papers were found that specifically combine "domain adaptation" methodology with theorem proving or autoformalization in 2026. The closest is:

- **[Awakening the Sleeping Agent](https://arxiv.org/abs/2604.08388)** (April 2026) -- Finds that heavy domain-specific SFT on formal math suppresses general tool-use capabilities, but 100 Lean-specific traces can "awaken" dormant tool use. This is about domain-specific fine-tuning effects, not domain-adaptive autoformalization.

- **[MSC-180](https://arxiv.org/abs/2512.18256)** (December 2025) -- A benchmark of 180 problems across 60 MSC2020 mathematical branches. Uses subject classification for EVALUATION (measuring domain coverage gaps), but does NOT condition proving/formalization on domain information. Finds maximum domain coverage of only 41.7% and CV values 4-6x above high-variability thresholds.

**Impact on novelty:** These support the proposal's motivation (domain bias is real and unaddressed) rather than threatening its novelty.

---

### 5. Goedel-Formalizer: Domain-Specific Details

**Goedel-Formalizer-V2-8B** ([HuggingFace](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)):
- Fine-tuned from Qwen3-8B
- Key feature: "think before generating" approach
- **NO mention whatsoever of domain-specific training, domain awareness, domain adaptation, or conditioning on mathematical subdomain** in the model card
- Purely general-purpose informal-to-formal translation
- Also available as Goedel-Formalizer-32B-SonnetAnnotated and Goedel-Formalizer-32B-LeanWorkbookAnnotated -- none mention domain conditioning

---

### 6. FormalMATH Per-Domain Accuracy (Goedel-Prover)

**Confirmed per-domain Pass@32 numbers** from [FormalMATH](https://arxiv.org/abs/2505.02735):

| Domain | Goedel-Prover Pass@32 |
|---|---|
| Undergraduate Algebra | **50.0%** |
| High-school Algebra | 17.5% |
| Applied Mathematics | 29.4% |
| Number Theory | 12.3% |
| Calculus (Differentiation) | 1.9% |
| Calculus (Integration) | **0.0%** |
| Discrete Mathematics | **0.0%** |

The proposal's claims of "50% algebra, 0% discrete math" are **verified and accurate**. The paper states: "current provers systematically exploit domain-specific automation, but do not generalize robustly to domains with less tactic support."

---

### 7. Survey Papers on Autoformalization (2025--2026)

**[Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486)** (May 2025, revised July 2025):
- Comprehensive survey covering the full autoformalization landscape
- Categorizes problems across three domain groupings: (1) Geometry/Topology, (2) Algebra/Number Theory, (3) Complex Systems/Frontier Problems
- Notes domain-adapted methods exist (e.g., geometry-specific formalization)
- Identifies data scarcity, generalization limitations, and abstraction handling as open challenges
- **Does NOT explicitly identify systematic domain-adaptive autoformalization as a distinct future direction or priority gap** -- this actually supports the proposal's novelty, as even the survey missed this as a key direction

**Additional relevant work:**
- **[Towards a Common Framework for Autoformalization](https://arxiv.org/abs/2509.09810)** (September 2025, AAAI) -- Proposes a unifying framework but not domain-specific
- **[StepFun-Formalizer](https://arxiv.org/abs/2508.04440)** (August 2025) -- SOTA results (40.5% on FormalMATH-Lite) via knowledge-reasoning fusion training pipeline. General-purpose, not domain-conditioned
- **ShadowBench** at [ICML 2026 AI for Math Workshop](https://ai4math2026.github.io/) -- 126 problems across 8 mathematical areas; competition running May-June 2026

---

### Summary Assessment of Novelty Claims

**The proposal's claim of being "the first to condition autoformalization on mathematical subdomain" is partially undermined by IndiMathBench (December 2025)**, which already uses category-based retrieval to condition formalization on four mathematical categories with domain-specific Mathlib context. This is the single most important finding.

However, there are defensible distinctions:
1. IndiMathBench uses retrieval-augmented prompting (domain-specific library snippets), not model-level domain conditioning
2. IndiMathBench's categories are coarse (4 categories for competition math), not fine-grained
3. If the proposal involves fine-tuning, domain tokens, or architectural modifications to condition on subdomain, that would be genuinely novel

**Recommendations for the proposal:**
- Acknowledge IndiMathBench's category-based retrieval as prior work on domain-aware autoformalization
- Sharpen the novelty claim to specify the mechanism (e.g., "first to use model-level domain conditioning" or "first to systematically study fine-grained subdomain adaptation")
- The FormalMATH domain bias numbers and MSC-180 coverage gaps strongly motivate the work
- No other paper from March-May 2026 scoops the core contribution
- The survey (May 2025) not identifying this direction as a gap is a double-edged sword: it validates novelty but may require extra justification for why it matters

Sources:
- [Improving Lean4 Autoformalization via Cycle Consistency](https://arxiv.org/abs/2603.24372)
- [FormalEvolve](https://arxiv.org/abs/2603.19828)
- [Agent Hunt](https://arxiv.org/abs/2603.06737)
- [MathAtlas](https://arxiv.org/abs/2605.14061)
- [MerLean](https://arxiv.org/abs/2602.16554)
- [IndiMathBench](https://arxiv.org/abs/2512.00997)
- [Kimina-Autoformalizer-7B](https://huggingface.co/AI-MO/Kimina-Autoformalizer-7B)
- [Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)
- [FormalMATH](https://arxiv.org/abs/2505.02735)
- [Autoformalization Survey](https://arxiv.org/abs/2505.23486)
- [MSC-180](https://arxiv.org/abs/2512.18256)
- [StepFun-Formalizer](https://arxiv.org/abs/2508.04440)
- [Awakening the Sleeping Agent](https://arxiv.org/abs/2604.08388)
- [Towards a Common Framework](https://arxiv.org/abs/2509.09810)
- [ICML 2026 AI for Math Workshop](https://ai4math2026.github.io/)
- [FormalMATH Benchmark](https://www.emergentmind.com/topics/formalmath-benchmark)
- [Goedel-Formalizer-32B-SonnetAnnotated](https://huggingface.co/Goedel-LM/Goedel-Formalizer-32B-SonnetAnnotated)

agentId: a0552ec0da559e91c (use SendMessage with to: 'a0552ec0da559e91c' to continue this agent)
&lt;usage>total_tokens: 30750
tool_uses: 30
duration_ms: 169431&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe724b76-7c3d-45ac-a0b5-4619af61649c",
  "isSidechain": false,
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "cf1dfffe-6878-4471-a422-637dff81717e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping review a research proposal about domain-adaptive autoformalization. I need to check for very recent work (March-May 2026) that might scoop or overlap with this proposal. The proposal claims to be the first to condition autoformalization on mathematical subdomain.\n\nPlease search for:\n\n1. Search \"autoformalization 2026\" on arXiv — look for papers from March-May 2026 specifically\n2. Search \"IndiMathBench\" — this paper uses category-specific context in autoformalization; verify details\n3. Search for \"Kimina-Autoformalizer\" — mentioned as a baseline in Aria's results\n4. Search \"domain adaptation theorem proving\" 2026\n5. Search for \"Goedel-Formalizer\" to check if there are newer versions or domain-specific variants\n6. Search \"FormalMATH benchmark domain\" to verify the per-domain accuracy claims (50% algebra, 0% discrete math for Goedel-Prover)\n7. Search for any recent survey papers on autoformalization from 2025-2026 that might catalog the landscape\n\nFor each paper found, briefly note whether it contradicts the proposal's novelty claims.\n\nAlso specifically check: Does the Goedel-Formalizer-V2-8B model description mention anything about domain-specific training or domain awareness?\n\nReport findings comprehensively.",
    "agentId": "a0552ec0da559e91c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Here is the full report.\n\n---\n\n## Comprehensive Literature Search Report: Domain-Adaptive Autoformalization (March--May 2026)\n\n### 1. Recent Autoformalization Papers on arXiv (March--May 2026)\n\nSeveral new autoformalization papers appeared in this window:\n\n- **[Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning](https://arxiv.org/abs/2603.24372)** (March 25, 2026) -- Uses RL with cycle consistency as a reward signal. Does NOT address domain-specific or domain-adaptive autoformalization. General-purpose approach.\n\n- **[FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization](https://arxiv.org/abs/2603.19828)** (March 20, 2026) -- A compilation-gated evolutionary framework for generating diverse formalization candidates. Does NOT condition on mathematical subdomain. Evaluates on general benchmarks (CombiBench, ProofNet).\n\n- **[Agent Hunt: Bounty Based Collaborative Autoformalization With LLM Agents](https://arxiv.org/abs/2603.06737)** (March 6, 2026) -- Multi-agent bounty-based autoformalization of algebraic topology. Domain-specific in the sense that it targets algebraic topology, but does NOT propose a general domain-adaptation framework.\n\n- **[MathAtlas: A Benchmark for Autoformalization in the Wild](https://arxiv.org/abs/2605.14061)** (May 2026) -- 52k theorems from 103 graduate textbooks with a 178k-relation dependency graph. Does NOT condition on subdomain; treats mathematics as a unified domain. Focuses on dependency-aware evaluation rather than domain-adaptive generation.\n\n- **[MerLean: An Agentic Framework for Autoformalization in Quantum Computation](https://arxiv.org/abs/2602.16554)** (February 2026) -- Domain-specific to quantum computation but is an application paper, not a domain-adaptation methodology.\n\n**Verdict on novelty threat from these papers:** None of these papers propose conditioning autoformalization on mathematical subdomain as a general methodology. The proposal's novelty claim appears safe against these.\n\n---\n\n### 2. IndiMathBench -- Category-Specific Context in Autoformalization\n\n**Paper:** [IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch](https://arxiv.org/abs/2512.00997) (December 2025)\n\n**THIS IS THE MOST SIGNIFICANT OVERLAP.** IndiMathBench uses **category-based retrieval** that conditions autoformalization on four mathematical categories: Geometry (98 problems), Algebra (92), Set Theory & Combinatorics (45), and Number Theory (77).\n\nHow it works:\n- Each problem is labeled by category (LLM + human verification)\n- 25% of problems per category are sampled; a Claude Sonnet 4-based agent extracts relevant Mathlib definitions/formulas specific to that domain\n- This category-specific documentation becomes static context reused for all problems in that domain\n- The authors explicitly state: \"This context anchors the model with domain knowledge within each category, preventing hallucinations and syntax errors\"\n\n**Impact on novelty claim:** This IS effectively domain-adaptive autoformalization -- the system conditions its prompts on mathematical subdomain, providing domain-specific library context. The proposal's claim of being \"the first to condition autoformalization on mathematical subdomain\" is directly contradicted by this work. However, IndiMathBench's approach is retrieval-augmentation-based (prompt engineering with domain-specific library snippets), not fine-tuning or architectural conditioning. If the proposal's method involves model-level domain conditioning (fine-tuning, domain tokens, etc.), there is a distinction to be made, but the high-level claim needs to be qualified.\n\n---\n\n### 3. Kimina-Autoformalizer\n\n**Model:** [Kimina-Autoformalizer-7B](https://huggingface.co/AI-MO/Kimina-Autoformalizer-7B) by Project Numina / AI-MO\n\n- 7B parameter model for translating natural language competition problems to Lean 4\n- Trained via SFT + structured expert iteration with LLM-based judging\n- Part of the Kimina-Prover family (up to 72B)\n- On 300 Omni-MATH statements: Kimina-Autoformalizer-7B successfully translated 161 statements\n- Does NOT use domain-specific conditioning or domain adaptation\n- General-purpose competition math autoformalization\n\n**Impact on novelty:** Does not threaten the domain-adaptive claim. Confirmed as a reasonable baseline.\n\n---\n\n### 4. Domain Adaptation + Theorem Proving (2026)\n\nNo papers were found that specifically combine \"domain adaptation\" methodology with theorem proving or autoformalization in 2026. The closest is:\n\n- **[Awakening the Sleeping Agent](https://arxiv.org/abs/2604.08388)** (April 2026) -- Finds that heavy domain-specific SFT on formal math suppresses general tool-use capabilities, but 100 Lean-specific traces can \"awaken\" dormant tool use. This is about domain-specific fine-tuning effects, not domain-adaptive autoformalization.\n\n- **[MSC-180](https://arxiv.org/abs/2512.18256)** (December 2025) -- A benchmark of 180 problems across 60 MSC2020 mathematical branches. Uses subject classification for EVALUATION (measuring domain coverage gaps), but does NOT condition proving/formalization on domain information. Finds maximum domain coverage of only 41.7% and CV values 4-6x above high-variability thresholds.\n\n**Impact on novelty:** These support the proposal's motivation (domain bias is real and unaddressed) rather than threatening its novelty.\n\n---\n\n### 5. Goedel-Formalizer: Domain-Specific Details\n\n**Goedel-Formalizer-V2-8B** ([HuggingFace](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)):\n- Fine-tuned from Qwen3-8B\n- Key feature: \"think before generating\" approach\n- **NO mention whatsoever of domain-specific training, domain awareness, domain adaptation, or conditioning on mathematical subdomain** in the model card\n- Purely general-purpose informal-to-formal translation\n- Also available as Goedel-Formalizer-32B-SonnetAnnotated and Goedel-Formalizer-32B-LeanWorkbookAnnotated -- none mention domain conditioning\n\n---\n\n### 6. FormalMATH Per-Domain Accuracy (Goedel-Prover)\n\n**Confirmed per-domain Pass@32 numbers** from [FormalMATH](https://arxiv.org/abs/2505.02735):\n\n| Domain | Goedel-Prover Pass@32 |\n|---|---|\n| Undergraduate Algebra | **50.0%** |\n| High-school Algebra | 17.5% |\n| Applied Mathematics | 29.4% |\n| Number Theory | 12.3% |\n| Calculus (Differentiation) | 1.9% |\n| Calculus (Integration) | **0.0%** |\n| Discrete Mathematics | **0.0%** |\n\nThe proposal's claims of \"50% algebra, 0% discrete math\" are **verified and accurate**. The paper states: \"current provers systematically exploit domain-specific automation, but do not generalize robustly to domains with less tactic support.\"\n\n---\n\n### 7. Survey Papers on Autoformalization (2025--2026)\n\n**[Autoformalization in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2505.23486)** (May 2025, revised July 2025):\n- Comprehensive survey covering the full autoformalization landscape\n- Categorizes problems across three domain groupings: (1) Geometry/Topology, (2) Algebra/Number Theory, (3) Complex Systems/Frontier Problems\n- Notes domain-adapted methods exist (e.g., geometry-specific formalization)\n- Identifies data scarcity, generalization limitations, and abstraction handling as open challenges\n- **Does NOT explicitly identify systematic domain-adaptive autoformalization as a distinct future direction or priority gap** -- this actually supports the proposal's novelty, as even the survey missed this as a key direction\n\n**Additional relevant work:**\n- **[Towards a Common Framework for Autoformalization](https://arxiv.org/abs/2509.09810)** (September 2025, AAAI) -- Proposes a unifying framework but not domain-specific\n- **[StepFun-Formalizer](https://arxiv.org/abs/2508.04440)** (August 2025) -- SOTA results (40.5% on FormalMATH-Lite) via knowledge-reasoning fusion training pipeline. General-purpose, not domain-conditioned\n- **ShadowBench** at [ICML 2026 AI for Math Workshop](https://ai4math2026.github.io/) -- 126 problems across 8 mathematical areas; competition running May-June 2026\n\n---\n\n### Summary Assessment of Novelty Claims\n\n**The proposal's claim of being \"the first to condition autoformalization on mathematical subdomain\" is partially undermined by IndiMathBench (December 2025)**, which already uses category-based retrieval to condition formalization on four mathematical categories with domain-specific Mathlib context. This is the single most important finding.\n\nHowever, there are defensible distinctions:\n1. IndiMathBench uses retrieval-augmented prompting (domain-specific library snippets), not model-level domain conditioning\n2. IndiMathBench's categories are coarse (4 categories for competition math), not fine-grained\n3. If the proposal involves fine-tuning, domain tokens, or architectural modifications to condition on subdomain, that would be genuinely novel\n\n**Recommendations for the proposal:**\n- Acknowledge IndiMathBench's category-based retrieval as prior work on domain-aware autoformalization\n- Sharpen the novelty claim to specify the mechanism (e.g., \"first to use model-level domain conditioning\" or \"first to systematically study fine-grained subdomain adaptation\")\n- The FormalMATH domain bias numbers and MSC-180 coverage gaps strongly motivate the work\n- No other paper from March-May 2026 scoops the core contribution\n- The survey (May 2025) not identifying this direction as a gap is a double-edged sword: it validates novelty but may require extra justification for why it matters\n\nSources:\n- [Improving Lean4 Autoformalization via Cycle Consistency](https://arxiv.org/abs/2603.24372)\n- [FormalEvolve](https://arxiv.org/abs/2603.19828)\n- [Agent Hunt](https://arxiv.org/abs/2603.06737)\n- [MathAtlas](https://arxiv.org/abs/2605.14061)\n- [MerLean](https://arxiv.org/abs/2602.16554)\n- [IndiMathBench](https://arxiv.org/abs/2512.00997)\n- [Kimina-Autoformalizer-7B](https://huggingface.co/AI-MO/Kimina-Autoformalizer-7B)\n- [Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B)\n- [FormalMATH](https://arxiv.org/abs/2505.02735)\n- [Autoformalization Survey](https://arxiv.org/abs/2505.23486)\n- [MSC-180](https://arxiv.org/abs/2512.18256)\n- [StepFun-Formalizer](https://arxiv.org/abs/2508.04440)\n- [Awakening the Sleeping Agent](https://arxiv.org/abs/2604.08388)\n- [Towards a Common Framework](https://arxiv.org/abs/2509.09810)\n- [ICML 2026 AI for Math Workshop](https://ai4math2026.github.io/)\n- [FormalMATH Benchmark](https://www.emergentmind.com/topics/formalmath-benchmark)\n- [Goedel-Formalizer-32B-SonnetAnnotated](https://huggingface.co/Goedel-LM/Goedel-Formalizer-32B-SonnetAnnotated)"
      }
    ],
    "totalDurationMs": 169431,
    "totalTokens": 30750,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 27232,
      "output_tokens": 3090,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3090,
          "cache_read_input_tokens": 27232,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 427,
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
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "fe724b76-7c3d-45ac-a0b5-4619af61649c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "cf1dfffe-6878-4471-a422-637dff81717e",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization via subdomain conditioning",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Assistant

_source line 22 · 2026-05-28T13:17:45.449Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all the findings from my three research agents and form my judgment.

## Summary of Findings

### Paper Verification (Agent 1)
All 6 verified papers exist, venues/dates are correct, and numerical claims are accurate. Minor paraphrasing differences (LeanSearch v2's "dependency-aware" vs. "hierarchy-informed") but no factual errors.

### Competing Work (Agent 2)
- **No existing paper** makes domain-conditioned autoformalization its primary contribution
- **IndiMathBench (Dec 2025, ICLR 2026)** is the closest overlap — uses category-specific context (4 categories) to condition formalization prompts on mathematical subdomain. 

The proposal doesn't cite this work, which is a notable gap. ATLAS organizes Mathlib into 13 domains but only for data generation, not inference-time conditioning. The autoformalization survey from May 2025 identifies domain adaptation as an open challenge.

### Feasibility (Agent 3)
- All key resources (Goedel-Formalizer-V2-8B, APRIL, Herald, FineLeanCorpus) are publicly available ✓
- CRAMF code is minimal/anonymized — medium risk
- Compute estimates are conservative (80h for LoRA is generous)
- AAAI 2026 deadline already passed (conference held Jan 2026) — user's original target is impossible
- AAAI 2027: July 28, 2026 (8 weeks away) — tight
- ICLR 2027: likely Sept/Oct 2026 — comfortable
- FormalMATH per-domain claims verified (50% algebra, 0% discrete math)

### Additional Concurrent Work (Agent 3)
IndiMathBench is the most significant overlap — it uses category-based retrieval with 4 math categories and was published in Dec 2025 for ICLR 2026. No other paper from March-May 2026 scoops the core contribution. Goedel-Formalizer-V2-8B has no domain-specific features.

## My Assessment

### Issues to Consider

1. **IndiMathBench Missing (MODERATE-CRITICAL)**: This is a significant omission. IndiMathBench already uses category-specific retrieval, which overlaps with the domain adaptation approach being proposed.  The proposal claims to be "the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain," but this needs qualification since IndiMathBench uses a simpler static context retrieval approach for the same purpose. The proposal never cites it, which is the most notable gap after revisions.

2. **AAAI 2026 Venue (User Requirement)**: The user originally asked for AAAI 2026 with an August 2025 deadline that's already passed. The proposal has shifted to ICLR 2027 or AAAI 2027, which is sensible given the current date but doesn't match the original request.

3. **Impact Uncertainty**: The naive domain prompting ablation is well-designed, but I'm still uncertain whether the multi-domain approach actually delivers meaningful improvements.

4. **Overall Quality**: After 4 rounds of revision, the proposal is technically thorough with clear differentiation from related work, well-structured with distinct contributions including the error taxonomy and domain-conditioned retrieval, honest about its limitations, feasible within resource constraints, and comprehensive in its landscape analysis.

The novelty score improved from 3.5 to 4 because conditioning autoformalization on mathematical subdomain is genuinely novel as a systematic approach, the error taxonomy is a first contribution, and the multi-domain rotation evaluation protocol is novel. IndiMathBench does something related but much simpler. However, the core idea of domain-specific conditioning isn't entirely new.

Feasibility is strong at 4 — all resources are available, compute estimates are conservative, and the pipeline is well-scoped. The main uncertainties are whether CRAMF code needs reconstruction and whether the approach significantly outperforms naive domain prompting, but the proposal acknowledges these risks with mitigation strategies.

Clarity scores 4.5 given the exceptional organization after multiple revisions, technically precise differentiation from competing approaches, comprehensive ablation design, and the smart contribution structure that positions the error taxonomy as primary.

For impact, I'm settling on 3.5 — the error taxonomy and multi-domain evaluation protocol would genuinely help the community, but the downstream pipeline gains might be incremental. The contribution is solid without being transformative, though impact would strengthen considerably if domain conditioning produces dramatic improvements on weak domains like discrete math.

The average lands at exactly 4.0, right at the pass threshold. But there's a problem I just noticed: IndiMathBench isn't cited anywhere. This is a meaningful gap that needs flagging. Given this is round 4 of 10 and the proposal has handled previous feedback well, I need to decide whether this omission warrants another full revision or if it's addressable as a minor note.

Looking at IndiMathBench more closely, the overlap is real but limited — it's a benchmark paper using coarse categories, not a system that trains domain-specific models or does domain-conditioned reranking, builds error taxonomies, or runs leave-one-domain-out evaluation. The proposal should definitely cite it and clarify the distinction, especially since the claim about being "the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain" needs qualification in light of IndiMathBench's category-specific approach. But this doesn't fundamentally undermine the core contribution. Given steady improvement across rounds and that this is a moderate rather than critical issue, I'm leaning toward letting it pass with the understanding that citation and clarification are needed.

The proposal is executing at a high level overall — previous issues resolved, landscape well-covered, technical differentiation precise, evaluation comprehensive. Scoring it out: novelty at 4 (novel but incremental application of domain adaptation to autoformalization), feasibility at 4 (resources available, conservative scoping), clarity at 4 (well-written after iterations, just needs IndiMathBench acknowledgment), and impact at 3.5 (useful error taxonomy and evaluation protocol, but uncertain how much it moves the needle downstream). That averages to 3.875, which sits just below 4.0 — the impact score is what's holding it back. Though looking at the Aria results showing 42.9% versus 0% for baselines on the homogenization task, that's actually quite compelling and might push impact higher. ological conjectures) and FormalMATH results (50% vs 0%) are strong evidence that domain bias is a real and severe problem. If this proposal can improve catastrophically failing domains, the impact would be significant. The error taxonomy alone would be a useful community contribution. The multi-domain rotation evaluation protocol fills a genuine gap.

Let me reconsider impact at 3.5 vs 4: the error taxonomy is genuinely novel, the multi-domain rotation evaluation addresses a real need, and domain-conditioned retrieval could show meaningful gains on weak domains. But there's real risk that simple domain prompting captures most of the gains, and while I appreciate the honest acknowledgment of this uncertainty, it does signal some concern. I'll keep impact at 3.5 and flag this as moderate.

The proposal has strong motivation across multiple benchmarks, novel contributions including the error taxonomy and domain-conditioned retrieval, comprehensive ablations with a naive baseline, conservative resource estimates, and honest risk assessment. The IndiMathBench omission is the main issue—moderate rather than critical, but it pushes me toward a revise verdict.

My final scores are novelty 4, feasibility 4, clarity 4, and impact 3.5, averaging 3.875, which falls below the 4.0 threshold. Combined with the IndiMathBench gap and marginal average score, I'm issuing a revise verdict. If the error taxonomy is truly the core contribution, I should push back on the proposal to lead with it more prominently and treat the pipeline as supporting work rather than the main focus. The impact case hinges on this framing—if they can demonstrate preliminary results showing domain conditioning works, or make a stronger argument that the taxonomy alone carries the paper, that could push impact to 4. I'm also catching a potential inconsistency: the feasibility report mentions Goedel-Formalizer-V2-8B as a fine-tune of Qwen3-8B, but the requirements specify open-source models only with Qwen2 as the baseline. I need to flag both the missing IndiMathBench citation and this model specification discrepancy in my feedback. The model choice seems reasonable given the user's constraints, so I'll move forward with my final assessment. Looking at the scores across novelty, feasibility, clarity, and impact, I'm settling on an average of around 3.875—the error taxonomy and evaluation protocol are solid contributions, though the core innovation feels somewhat incremental and the downstream impact remains uncertain.

That said, the score falls just below the 4.0 threshold, which means I need to push back. The IndiMathBench paper from ICLR 2026 is doing something very similar with category-specific context across math domains, and I haven't properly differentiated from it. Beyond that, the impact argument needs reinforcement—the error taxonomy is well-motivated, but I should either run a small pilot demonstrating that domain conditioning actually works, or find a way to make the taxonomy itself stand as a stronger standalone contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf1dfffe-6878-4471-a422-637dff81717e",
  "isSidechain": false,
  "requestId": "req_011CbV2gwRXSAV8Bx5PJcLh9",
  "type": "assistant",
  "uuid": "d69c7cbe-b2aa-41ff-a6e4-1644340d1476",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtS6HM2nP1Fs6dDrY2RPBW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 34546,
      "output_tokens": 3630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3630,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 3572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3572
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

_source line 23 · 2026-05-28T13:17:45.455Z_

Now let me do one final targeted check on IndiMathBench, which was flagged as a significant omission:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d69c7cbe-b2aa-41ff-a6e4-1644340d1476",
  "isSidechain": false,
  "requestId": "req_011CbV2gwRXSAV8Bx5PJcLh9",
  "type": "assistant",
  "uuid": "2a59903e-2328-4568-b17b-dd35aef21ac7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtS6HM2nP1Fs6dDrY2RPBW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 34546,
      "output_tokens": 3630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3630,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 3572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3572
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

_source line 24 · 2026-05-28T13:17:52.227Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018TSkKqU4pqP1GRX5fjZs9N`</summary>

```json
{
  "description": "Deep-dive IndiMathBench overlap",
  "subagent_type": "general-purpose",
  "prompt": "I need a detailed technical analysis of IndiMathBench (arXiv 2512.00997, December 2025) — a paper about autoformalizing mathematical reasoning problems. It was published at ICLR 2026.\n\nPlease use WebFetch to read the paper at https://arxiv.org/abs/2512.00997 and answer these specific questions:\n\n1. Does IndiMathBench use category-specific (domain-specific) context when formalizing? How exactly does it work?\n2. What are the 4 categories used? How are problems classified into categories?\n3. Is the category-specific context used for retrieval conditioning, prompt conditioning, or both?\n4. Does the paper report per-domain results? If so, what are the performance differences across domains?\n5. Does the paper claim novelty in domain-aware autoformalization?\n6. Is IndiMathBench's approach closer to \"naive domain prompting\" (just adding domain context to the prompt) or a full domain-adaptive pipeline?\n7. What model does IndiMathBench use for autoformalization?\n\nThis is important because a proposal I'm reviewing claims to be \"the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain\" — and IndiMathBench might partially contradict this claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a59903e-2328-4568-b17b-dd35aef21ac7",
  "isSidechain": false,
  "requestId": "req_011CbV2gwRXSAV8Bx5PJcLh9",
  "type": "assistant",
  "uuid": "1ca9906c-aa09-4925-873d-8c737c4fe4be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtS6HM2nP1Fs6dDrY2RPBW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 34546,
      "output_tokens": 3630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3572,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3630,
          "cache_read_input_tokens": 34546,
          "cache_creation_input_tokens": 3572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3572
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

_source line 25 · 2026-05-28T13:19:46.927Z_

<details><summary>↩ Tool result · `toolu_018TSkKqU4pqP1GRX5fjZs9N`</summary>

```text
Now I have comprehensive information to provide a detailed analysis. Here is the full technical breakdown:

---

## Detailed Technical Analysis of IndiMathBench (arXiv 2512.00997)

**Paper:** "IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch"
**Authors:** Param Biyani, Shashank Kirtania, Yasharth Bajpai, Sumit Gulwani, Ashish Tiwari
**Venue:** ICLR 2026

---

### 1. Does IndiMathBench use category-specific context when formalizing?

**Yes, but in a limited, static fashion.** The pipeline labels each problem into one of four categories, then injects a pre-constructed block of Mathlib documentation specific to that category into the prompt. The process works as follows:

- A Claude Sonnet 4-based agent with bash access to the Mathlib repository is given a 25% sample of problems from each category.
- The agent explores the relevant library code and extracts key definitions and formulas, producing a **static context** for that category.
- This is a **one-time, per-category** process. The resulting context block is then reused verbatim for all problems in that category.
- At formalization time, each problem's prompt is composed of: the natural language problem statement + the category-specific static context + (in later iterations) compiler error feedback.

### 2. What are the 4 categories and how are problems classified?

The four categories are:
1. **Geometry** (98 problems)
2. **Algebra** (92 problems)
3. **Number Theory** (77 problems)
4. **Set Theory & Combinatorics** (45 problems)

Classification is done by an **LLM with human verification** -- the LLM proposes a category label for each problem, and human annotators validate/correct those labels. The problems are sourced from Indian Mathematics Olympiads (312 problems total).

### 3. Is the category-specific context used for retrieval conditioning, prompt conditioning, or both?

**It is purely prompt conditioning (static context injection), not retrieval conditioning.**

There is no dynamic retrieval system -- no vector store, no RAG pipeline, no per-problem retrieval ranking that is conditioned on domain. The paper constructs a fixed documentation block per category once, and that block is inserted into every prompt for problems in that category. The term "category-based retrieval" in the paper refers to this one-time extraction of relevant Mathlib definitions per domain, not an online retrieval-ranking mechanism.

### 4. Does the paper report per-domain results?

**Partially.** The paper does not report per-category autoformalization success rates (e.g., compilation rates broken down by domain). However, for theorem proving, it highlights a striking finding: **no geometry problems were solved by any model** in single-turn theorem proving, and only 12 of 98 geometry problems were solved even with multi-model ensembles. The paper attributes this to Mathlib's lacking support for Olympiad-style geometry. Aggregate autoformalization results are in Table 2 but not disaggregated by category.

### 5. Does the paper claim novelty in domain-aware autoformalization?

**No.** The paper does not claim category-based retrieval as a novel contribution. It is presented as a straightforward engineering practice to mitigate hallucinations and syntax errors by providing relevant Mathlib definitions. The paper's four stated contributions are:
1. A Lean 4 benchmark with LLM-assisted formalization and human verification
2. A systematic pipeline (category-based retrieval + self-debug loop + multi-model ensemble)
3. A VS Code extension for human-AI collaboration
4. An evaluation framework across 12 frontier models

The related work section does not discuss prior domain-aware autoformalization approaches. Category-based context is framed as addressing a practical gap (especially Mathlib's incomplete coverage of geometry), not as a methodological advance.

### 6. Is IndiMathBench's approach closer to "naive domain prompting" or a full domain-adaptive pipeline?

**It is much closer to naive domain prompting.** Specifically:

- The category context is a **static, fixed block of text** per domain -- not dynamically adapted per problem.
- There is **no domain-conditioned retrieval ranking** (no per-query similarity search within a domain-specific index).
- There is **no domain-specific model selection or fine-tuning**.
- There are **no domain-specific few-shot examples** mentioned.
- The category label is determined once up front and simply used to select which of four documentation blocks to inject.

This is essentially: classify problem into domain -> paste corresponding documentation block into prompt -> run the same formalization pipeline. It is a one-dimensional use of domain information (prompt augmentation only), not a multi-signal domain-adaptive system.

### 7. What models does IndiMathBench use?

The paper evaluates **12 frontier models** for autoformalization:
- Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7, Claude Sonnet 3.5
- GPT-5, GPT-4.1, GPT-4o
- o3 (high), o3-mini, o4-mini
- Gemini 2.5 Pro
- Specialized: Kimina-Autoformalizer, Godel-Formalizer-V2, DeepSeek-Prover V2 7B

Top performers by BEq (behavioral equivalence) metric: Claude Opus 4 (54), Godel-Formalizer-V2 (52), Claude Sonnet 4 (51). The pipeline achieves 95.3% syntactic validity after up to 6 iterations of compiler feedback.

---

### Implications for the Proposal You Are Reviewing

The proposal's claim of being **"the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain"** is **not directly contradicted** by IndiMathBench. Here is why:

1. **IndiMathBench does NOT condition retrieval ranking on domain.** It uses static context blocks, not a retrieval system with domain-conditioned ranking.
2. **IndiMathBench does NOT claim novelty in domain-aware autoformalization.** It treats category-based context as a practical engineering measure.
3. **IndiMathBench's approach is single-signal** (prompt augmentation only), whereas the proposal appears to claim a multi-signal approach (both retrieval ranking AND prompting conditioned on domain).

However, IndiMathBench **does** demonstrate that the general idea of using mathematical subdomain information to condition the autoformalization prompt is a known practice (even if treated as an engineering detail rather than a research contribution). The proposal should acknowledge IndiMathBench as related work that uses domain-specific context in prompting, while clearly articulating how its approach differs (dynamic retrieval ranking, per-problem retrieval rather than static blocks, dual conditioning, etc.). The novelty claim should be scoped carefully -- "first to condition retrieval ranking on domain" may hold, but "first to use domain information in autoformalization" does not.

agentId: a70f39971d88bcf82 (use SendMessage with to: 'a70f39971d88bcf82' to continue this agent)
&lt;usage>total_tokens: 14538
tool_uses: 5
duration_ms: 114695&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ca9906c-aa09-4925-873d-8c737c4fe4be",
  "isSidechain": false,
  "promptId": "f52e040c-c89a-4354-9d36-8828dec412f7",
  "type": "user",
  "uuid": "4c83724f-a01e-4bb0-b3e4-c174c493a601",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need a detailed technical analysis of IndiMathBench (arXiv 2512.00997, December 2025) — a paper about autoformalizing mathematical reasoning problems. It was published at ICLR 2026.\n\nPlease use WebFetch to read the paper at https://arxiv.org/abs/2512.00997 and answer these specific questions:\n\n1. Does IndiMathBench use category-specific (domain-specific) context when formalizing? How exactly does it work?\n2. What are the 4 categories used? How are problems classified into categories?\n3. Is the category-specific context used for retrieval conditioning, prompt conditioning, or both?\n4. Does the paper report per-domain results? If so, what are the performance differences across domains?\n5. Does the paper claim novelty in domain-aware autoformalization?\n6. Is IndiMathBench's approach closer to \"naive domain prompting\" (just adding domain context to the prompt) or a full domain-adaptive pipeline?\n7. What model does IndiMathBench use for autoformalization?\n\nThis is important because a proposal I'm reviewing claims to be \"the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain\" — and IndiMathBench might partially contradict this claim.",
    "agentId": "a70f39971d88bcf82",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information to provide a detailed analysis. Here is the full technical breakdown:\n\n---\n\n## Detailed Technical Analysis of IndiMathBench (arXiv 2512.00997)\n\n**Paper:** \"IndiMathBench: Autoformalizing Mathematical Reasoning Problems with a Human Touch\"\n**Authors:** Param Biyani, Shashank Kirtania, Yasharth Bajpai, Sumit Gulwani, Ashish Tiwari\n**Venue:** ICLR 2026\n\n---\n\n### 1. Does IndiMathBench use category-specific context when formalizing?\n\n**Yes, but in a limited, static fashion.** The pipeline labels each problem into one of four categories, then injects a pre-constructed block of Mathlib documentation specific to that category into the prompt. The process works as follows:\n\n- A Claude Sonnet 4-based agent with bash access to the Mathlib repository is given a 25% sample of problems from each category.\n- The agent explores the relevant library code and extracts key definitions and formulas, producing a **static context** for that category.\n- This is a **one-time, per-category** process. The resulting context block is then reused verbatim for all problems in that category.\n- At formalization time, each problem's prompt is composed of: the natural language problem statement + the category-specific static context + (in later iterations) compiler error feedback.\n\n### 2. What are the 4 categories and how are problems classified?\n\nThe four categories are:\n1. **Geometry** (98 problems)\n2. **Algebra** (92 problems)\n3. **Number Theory** (77 problems)\n4. **Set Theory & Combinatorics** (45 problems)\n\nClassification is done by an **LLM with human verification** -- the LLM proposes a category label for each problem, and human annotators validate/correct those labels. The problems are sourced from Indian Mathematics Olympiads (312 problems total).\n\n### 3. Is the category-specific context used for retrieval conditioning, prompt conditioning, or both?\n\n**It is purely prompt conditioning (static context injection), not retrieval conditioning.**\n\nThere is no dynamic retrieval system -- no vector store, no RAG pipeline, no per-problem retrieval ranking that is conditioned on domain. The paper constructs a fixed documentation block per category once, and that block is inserted into every prompt for problems in that category. The term \"category-based retrieval\" in the paper refers to this one-time extraction of relevant Mathlib definitions per domain, not an online retrieval-ranking mechanism.\n\n### 4. Does the paper report per-domain results?\n\n**Partially.** The paper does not report per-category autoformalization success rates (e.g., compilation rates broken down by domain). However, for theorem proving, it highlights a striking finding: **no geometry problems were solved by any model** in single-turn theorem proving, and only 12 of 98 geometry problems were solved even with multi-model ensembles. The paper attributes this to Mathlib's lacking support for Olympiad-style geometry. Aggregate autoformalization results are in Table 2 but not disaggregated by category.\n\n### 5. Does the paper claim novelty in domain-aware autoformalization?\n\n**No.** The paper does not claim category-based retrieval as a novel contribution. It is presented as a straightforward engineering practice to mitigate hallucinations and syntax errors by providing relevant Mathlib definitions. The paper's four stated contributions are:\n1. A Lean 4 benchmark with LLM-assisted formalization and human verification\n2. A systematic pipeline (category-based retrieval + self-debug loop + multi-model ensemble)\n3. A VS Code extension for human-AI collaboration\n4. An evaluation framework across 12 frontier models\n\nThe related work section does not discuss prior domain-aware autoformalization approaches. Category-based context is framed as addressing a practical gap (especially Mathlib's incomplete coverage of geometry), not as a methodological advance.\n\n### 6. Is IndiMathBench's approach closer to \"naive domain prompting\" or a full domain-adaptive pipeline?\n\n**It is much closer to naive domain prompting.** Specifically:\n\n- The category context is a **static, fixed block of text** per domain -- not dynamically adapted per problem.\n- There is **no domain-conditioned retrieval ranking** (no per-query similarity search within a domain-specific index).\n- There is **no domain-specific model selection or fine-tuning**.\n- There are **no domain-specific few-shot examples** mentioned.\n- The category label is determined once up front and simply used to select which of four documentation blocks to inject.\n\nThis is essentially: classify problem into domain -> paste corresponding documentation block into prompt -> run the same formalization pipeline. It is a one-dimensional use of domain information (prompt augmentation only), not a multi-signal domain-adaptive system.\n\n### 7. What models does IndiMathBench use?\n\nThe paper evaluates **12 frontier models** for autoformalization:\n- Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7, Claude Sonnet 3.5\n- GPT-5, GPT-4.1, GPT-4o\n- o3 (high), o3-mini, o4-mini\n- Gemini 2.5 Pro\n- Specialized: Kimina-Autoformalizer, Godel-Formalizer-V2, DeepSeek-Prover V2 7B\n\nTop performers by BEq (behavioral equivalence) metric: Claude Opus 4 (54), Godel-Formalizer-V2 (52), Claude Sonnet 4 (51). The pipeline achieves 95.3% syntactic validity after up to 6 iterations of compiler feedback.\n\n---\n\n### Implications for the Proposal You Are Reviewing\n\nThe proposal's claim of being **\"the first autoformalization pipeline that systematically conditions retrieval ranking and prompting signals on inferred mathematical subdomain\"** is **not directly contradicted** by IndiMathBench. Here is why:\n\n1. **IndiMathBench does NOT condition retrieval ranking on domain.** It uses static context blocks, not a retrieval system with domain-conditioned ranking.\n2. **IndiMathBench does NOT claim novelty in domain-aware autoformalization.** It treats category-based context as a practical engineering measure.\n3. **IndiMathBench's approach is single-signal** (prompt augmentation only), whereas the proposal appears to claim a multi-signal approach (both retrieval ranking AND prompting conditioned on domain).\n\nHowever, IndiMathBench **does** demonstrate that the general idea of using mathematical subdomain information to condition the autoformalization prompt is a known practice (even if treated as an engineering detail rather than a research contribution). The proposal should acknowledge IndiMathBench as related work that uses domain-specific context in prompting, while clearly articulating how its approach differs (dynamic retrieval ranking, per-problem retrieval rather than static blocks, dual conditioning, etc.). The novelty claim should be scoped carefully -- \"first to condition retrieval ranking on domain\" may hold, but \"first to use domain information in autoformalization\" does not."
      }
    ],
    "totalDurationMs": 114695,
    "totalTokens": 14538,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 12087,
      "output_tokens": 1683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1683,
          "cache_read_input_tokens": 12087,
          "cache_creation_input_tokens": 767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 767,
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
  "sourceToolAssistantUUID": "1ca9906c-aa09-4925-873d-8c737c4fe4be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "4c83724f-a01e-4bb0-b3e4-c174c493a601",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization via subdomain conditioning",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Assistant

_source line 28 · 2026-05-28T13:20:12.873Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to form my verdict. Let me synthesize everything:

## Key Findings

### Paper Verification: All Clean
- All 6 key papers verified to exist with correct venues, dates, and numerical claims
- Minor paraphrasing differences only (not errors)

### Competing Work Assessment
- **IndiMathBench (ICLR 2026)**: Uses category-specific static context for 4 math domains in prompts. NOT cited in the proposal. This is a moderate issue — IndiMathBench's approach is closer to "naive domain prompting" (static context blocks) rather than dynamic domain-conditioned retrieval, but it does demonstrate that domain information in autoformalization is a known practice.


- No other work directly tackles domain-conditioned autoformalization as a primary contribution, so the core novelty claim holds up, though it needs some qualification.

### Feasibility: Strong
- All datasets/models publicly available
- Compute estimates conservative
- AAAI 2026 target impossible (deadline passed Aug 2025); proposal targets ICLR 2027 (reasonable) and AAAI 2027 (tight)

### Novelty Assessment
The error taxonomy is genuinely novel—no one has stratified APRIL repair tuples by domain—and the multi-domain rotation evaluation is also novel, with only ConNF doing something comparable. The proposal's novelty is real but needs qualification.

The domain-conditioned retrieval reranking is novel since CRAMF, DRIFT, and LeanSearch v2 are all domain-agnostic, though IndiMathBench demonstrates that domain information in prompting is a known practice, just not formalized.

### Impact Assessment
The error taxonomy and multi-domain evaluation protocol fill real gaps, but the core question remains whether domain conditioning in the pipeline produces significant gains over simpler approaches like IndiMathBench-style static context. The naive domain prompting ablation is well-designed but signals some uncertainty about the impact.

### Scoring (Final)
Novelty scores a 4—the specific mechanism of dynamic retrieval conditioning, error taxonomy, and evaluation protocol are novel even though using domain information generally is known. Feasibility also scores a 4 with all resources available, conservative estimates, and a well-scoped timeline.

Clarity gets a 4 after multiple rounds, though the IndiMathBench omission is a notable gap. Impact scores 3.5—the contributions are valuable but the downstream gains remain uncertain.

This averages to 3.875, falling just below the 4.0 threshold. The main issues are that IndiMathBench needs to be cited and differentiated, and the impact score needs strengthening through either preliminary evidence or a stronger standalone framing of the error taxonomy. With one more revision possible in this round, the proposal is close to passing and these issues are addressable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c83724f-a01e-4bb0-b3e4-c174c493a601",
  "isSidechain": false,
  "requestId": "req_011CbV2x5gHCJwW3bgkrL6fz",
  "type": "assistant",
  "uuid": "e3678b63-57d2-4e99-8a1c-2f58c2927195",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBXd4MnKmYqnDxQ57Lbxuv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 38118,
      "output_tokens": 2356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2356,
          "cache_read_input_tokens": 38118,
          "cache_creation_input_tokens": 5390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5390
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

_source line 29 · 2026-05-28T13:20:51.139Z_

Now I have comprehensive data from all four research agents. Let me synthesize my findings into a final verdict.

## Synthesis of Findings

**Paper Verification**: All 6 key papers (LeanSearch v2, DRIFT, Aria, MathAtlas, CRAMF, MSC-180) verified as existing with correct venues, dates, and numerical claims. Zero factual errors detected.

**Competing Work**: The core novelty claim — no existing system conditions autoformalization pipeline on mathematical subdomain — is **largely defensible** but has one significant gap: **IndiMathBench (ICLR 2026, arXiv 2512.00997)** uses category-specific static context for 4 math domains. It's closer to "naive domain prompting" (static Mathlib documentation blocks per category) than a full domain-adaptive pipeline, and doesn't claim novelty in domain conditioning, but it IS domain-aware autoformalization that should be cited.

**Feasibility**: All required resources (Goedel-Formalizer-V2-8B, APRIL, Herald, FineLeanCorpus) publicly available. Compute estimates are conservative. AAAI 2026 deadline long past; proposal correctly retargets ICLR 2027.

**FormalMATH Claims**: Verified — Goedel-Prover does achieve 50% on algebra and 0% on discrete math. Domain bias is real and severe.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The domain-specific error taxonomy (stratifying APRIL by subdomain), domain-conditioned retrieval reranking, and multi-domain rotation evaluation protocol are genuinely novel. However, IndiMathBench (ICLR 2026) already uses category-specific static context in autoformalization prompts — while much simpler than the proposed pipeline, it demonstrates domain-aware autoformalization is a known practice, and the novelty claim needs careful scoping."},
    "feasibility": {"score": 4, "rationale": "All key resources (Goedel-Formalizer-V2-8B, APRIL 260k tuples, Herald 580k pairs, FineLeanCorpus) are publicly available on HuggingFace. Compute estimates are conservative (80h LoRA training is likely 2-3× what's needed). CRAMF's anonymized codebase is minimal and may require reconstruction effort, but this is manageable. Timeline for ICLR 2027 is comfortable."},
    "clarity": {"score": 4, "rationale": "Exceptionally clear after 4 revision rounds. Technical differentiation from CRAMF (concept-level disambiguation), DRIFT (concept-level decomposition), LeanSearch v2 (retrieval quality), and Aria (Graph-of-Thought) is precise and verified accurate. The ablation design with 6 surgical comparisons is comprehensive. Only gap: IndiMathBench omission undermines landscape completeness."},
    "impact": {"score": 3.5, "rationale": "The error taxonomy and multi-domain rotation evaluation protocol are independently valuable community contributions. However, the core downstream improvement remains uncertain — the proposal honestly acknowledges naive domain prompting may capture 80%+ of gains, which signals the full pipeline's marginal value is unproven. IndiMathBench's success with simple static domain context (achieving 95.3% syntactic validity) suggests domain information may be valuable but easy to exploit, reducing the engineering contribution's novelty."}
  },
  "issues": [
    "MODERATE: IndiMathBench (ICLR 2026, arXiv 2512.00997) not cited — uses category-specific static Mathlib context for 4 mathematical domains (Geometry, Algebra, Number Theory, Set Theory & Combinatorics) to condition autoformalization prompts. While IndiMathBench uses static context blocks (not dynamic retrieval conditioning) and does not claim novelty in domain awareness, it IS a form of domain-conditioned autoformalization. The proposal's claim of being 'the first autoformalization pipeline that conditions on inferred mathematical subdomain' must acknowledge and differentiate from IndiMathBench. IndiMathBench's approach is essentially the 'naive domain prompting' ablation the proposal already plans — this connection should be made explicit.",
    "MODERATE: Impact argument remains below the 4.0 threshold — IndiMathBench achieves 95.3% syntactic validity with simple category-specific static context, suggesting that even rudimentary domain awareness is powerful. This strengthens the proposal's motivation (domain information helps) but weakens the pipeline contribution (maybe simple approaches suffice). The error taxonomy needs to be framed even more forcefully as the primary contribution — with quantitative hypotheses about expected inter-domain JSD values and prediction accuracy thresholds that would constitute a meaningful finding.",
    "MINOR: Goedel-Formalizer-V2-8B is fine-tuned from Qwen3-8B, not Qwen2.5. The user specified 'Qwen2.5-7B or Goedel-Prover-V2-8B' — using the Formalizer variant is reasonable (same family, specialized for formalization) but should be explicitly justified since the base architecture differs from user's Qwen2.5 specification."
  ],
  "feedback": "The proposal is very close to passing (avg 3.875/5.0) after 4 strong revision rounds. Two targeted fixes should clear the threshold: (1) **Cite IndiMathBench and make it your 'naive domain prompting' reference implementation**: IndiMathBench's category-specific static context is essentially the simple baseline your ablation (e) already plans. Explicitly map your ablation to IndiMathBench's approach: 'Our naive domain prompting baseline (ablation e) replicates IndiMathBench's category-specific context approach; our full pipeline adds dynamic domain-conditioned retrieval reranking and error-taxonomy-driven prompting on top.' This transforms a missing reference into a strengthened experimental design. Narrow the novelty claim to: 'first system to condition dynamic retrieval ranking on inferred mathematical subdomain and provide systematic domain-specific error characterization.' (2) **Set quantitative success criteria for the error taxonomy to strengthen impact**: State concrete hypotheses — e.g., 'We hypothesize JSD between topology and algebra error distributions exceeds 0.3 (vs. <0.1 for random domain assignments)' and 'domain-specific error prediction accuracy exceeds 70% on held-out formalizations.' This transforms the error taxonomy from 'we'll analyze and see what we find' into a testable scientific claim that reviewers can evaluate. If these hypotheses hold, the paper has clear value regardless of pipeline delta.",
  "reason": "Strong proposal at 3.875 avg after 4 rounds; needs IndiMathBench citation (moderate gap) and stronger quantitative impact framing to cross the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3678b63-57d2-4e99-8a1c-2f58c2927195",
  "isSidechain": false,
  "requestId": "req_011CbV2x5gHCJwW3bgkrL6fz",
  "type": "assistant",
  "uuid": "d575662a-9e3a-4a24-bbc4-add8d49c325a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBXd4MnKmYqnDxQ57Lbxuv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5390,
      "cache_read_input_tokens": 38118,
      "output_tokens": 2356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2356,
          "cache_read_input_tokens": 38118,
          "cache_creation_input_tokens": 5390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5390
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-28 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "d575662a-9e3a-4a24-bbc4-add8d49c325a",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-adaptive autoformalization via subdomain conditioning",
  "sessionId": "9c44962f-53ef-4dda-a205-11ae79612bf5"
}
```

---
