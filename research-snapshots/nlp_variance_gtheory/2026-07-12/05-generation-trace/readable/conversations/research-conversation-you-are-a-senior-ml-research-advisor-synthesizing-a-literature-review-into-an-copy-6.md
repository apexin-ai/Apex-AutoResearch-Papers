# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e72027ce-ed45-4523-93e6-5df64f5c12e2.jsonl`
- **Structured JSON:** [`465f687d0cdc50d99a42.json`](../../sessions/46/465f687d0cdc50d99a42.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:45:35.870Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:45:35.870Z",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction\",\n    \"venue\": \"NAACL 2024\",\n    \"problem_identification\": \"RAG systems provide no statistical guarantees on answer correctness despite being designed to reduce hallucinations. The gap was identified by noting that conformal prediction—a well-established tool for classification/regression—had never been applied to the compound retriever+generator pipeline where uncertainty propagates across components.\",\n    \"key_insight\": \"Decompose RAG uncertainty into retriever and generator components, define semantic-level nonconformity scores via Monte Carlo sampling and NLI/ROUGE clustering, then union-bound across pipeline stages for end-to-end coverage guarantees.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Defines retriever NCM as negative query-passage inner product and generator NCM via sampled response clustering (ROUGE>0.7 or NLI entailment). Calibration computes empirical quantiles on held-out data. Prediction sets are constructed per-stage and unioned: passages meeting retriever threshold feed into per-passage LLM sets, aggregated into final prediction set. Bayesian optimization allocates error budget (α_Ret + α_LLM = α) to minimize average set size.\",\n    \"limitations_and_open_questions\": \"Critically assumes benign retrieval—the guarantee Pr(r*∈C_Agg)≥1-α requires exchangeability of calibration and test retrieval, which corpus poisoning violates. Also requires the true relevant passage to appear in top-K, with no mechanism for adversarial retrieval manipulation.\",\n    \"building_blocks\": [\n      \"Semantic clustering via ROUGE/NLI for nonconformity scores\",\n      \"Pipeline decomposition with union-bound error allocation\",\n      \"Bayesian optimization for error budget tuning\",\n      \"Monte Carlo response sampling for uncertainty estimation\"\n    ],\n    \"relevance_to_seed\": \"Direct foundation—our work extends TRAQ's conformal framework to handle adversarial retrieval by replacing its benign-assumption NCM with retrieval-agreement-conditioned scores that restore coverage under bounded poisoning.\"\n  },\n  {\n    \"title\": \"Certifiably Robust RAG against Retrieval Corruption\",\n    \"venue\": \"IEEE SaTML 2026\",\n    \"problem_identification\": \"RAG systems are vulnerable to adversarial passage injection but no defense offered formal robustness certificates. The gap was identified by observing that existing empirical defenses (filtering, detection) provide no worst-case guarantees against adaptive attackers with full system knowledge.\",\n    \"key_insight\": \"Isolating passages into disjoint groups ensures poisoned documents contaminate only their own group's LLM response, enabling secure aggregation where attacker influence is bounded by the ratio of corrupted groups to total groups.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Partitions k retrieved passages into m=⌈k/ω⌉ disjoint groups of size ω, generates independent LLM responses per group, then aggregates via either keyword voting (count keywords across responses, threshold-filter) or decoding-level probability aggregation (sum next-token distributions, use probability gap to decide tokens). Certification enumerates worst-case attacker influence: for keywords, classifies them as always/never/controllably retained; for decoding, explores a token-sequence tree bounded by probability margins.\",\n    \"limitations_and_open_questions\": \"Requires m LLM calls (high compute), group size ω trades off response quality vs. robustness, and certification only covers bounded k' poisoned passages with no abstention mechanism when certification fails (outputs τ=0 without actionable fallback). No conformal coverage guarantee.\",\n    \"building_blocks\": [\n      \"Isolate-then-aggregate framework\",\n      \"Keyword voting aggregation\",\n      \"Decoding-level probability aggregation\",\n      \"Certification via worst-case enumeration\",\n      \"Threat model: adaptive attacker with bounded injection budget k'\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline and complementary approach—RobustRAG provides certified robustness but no conformal abstention; our method adds distribution-free coverage guarantees and principled abstention decisions on top of similar partition-based architectures.\"\n  },\n  {\n    \"title\": \"CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation\",\n    \"venue\": \"ACM SACMAT 2026\",\n    \"problem_identification\": \"Prior attacks like PoisonedRAG require injecting multiple (3-5) documents per query to outnumber benign passages in top-K, which is unrealistic and detectable. The gap was identified by noting that in real knowledge bases with millions of documents, injecting many texts per query at scale triggers volume-based detection.\",\n    \"key_insight\": \"A single poisoned document can achieve high attack success by decomposing it into a retrieval component (verbatim query text for guaranteed retrieval) and a generation component (adversarial framing exploiting LLM recency bias) — separating the retrieval and influence objectives.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"Constructs each poisoned document with two parts: p_i^s (retrieval) set to the query itself ensuring maximal retriever similarity, and p_i^h (generation) containing adversarial framing that marks correct answers as 'outdated' while asserting the target answer as 'confirmed by latest data.' CorruptRAG-AK variant uses an LLM to refine templates into coherent adversarial knowledge. Achieves 95% ASR with single document vs. PoisonedRAG's 69% single-doc baseline.\",\n    \"limitations_and_open_questions\": \"Relies on LLM recency bias which may not generalize across all models; effectiveness against defenses like RobustRAG's isolation (where single poisoned doc affects only one group) is unclear. How does agreement-based detection handle single vs. multi-doc poisoning?\",\n    \"building_blocks\": [\n      \"Single-document threat model for realistic evaluation\",\n      \"Retrieval-generation decomposition of poisoned documents\",\n      \"Recency-bias exploitation templates\",\n      \"Near-zero cost attack ($0.0001/query)\"\n    ],\n    \"relevance_to_seed\": \"Key attack baseline for evaluation — single-doc poisoning is harder to detect via agreement signals (only 1 of k passages is adversarial), directly testing whether our retrieval-agreement scores can identify isolated poisoned passages within agreement groups.\"\n  },\n  {\n    \"title\": \"Mitigating LLM Hallucinations via Conformal Abstention\",\n    \"venue\": \"NeurIPS 2024 (Google DeepMind)\",\n    \"problem_identification\": \"LLMs hallucinate unpredictably and existing confidence measures (log-probs) degrade with response length, providing no formal guarantees on when to abstain. The gap was identified by noting that self-consistency signals were used heuristically but never combined with conformal prediction's distribution-free guarantees.\",\n    \"key_insight\": \"LLM self-evaluated response similarity across multiple samples serves as a valid nonconformity score for conformal risk control, enabling calibration of an abstention threshold with provable bounds on hallucination rate — without requiring model internals or fine-tuning.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Samples k responses per query, uses the LLM itself to evaluate pairwise similarity (match function m calibrated separately via conformal procedure on threshold β). Computes confidence g(X) as match count or expected match count. Applies conformal risk control: finds threshold λ̂_n = inf{λ: (n/(n+1))L_n(λ) + 1/(n+1) ≤ α} on calibration set. Abstains when g(X) < λ̂_n. Guarantees E[R(λ̂_n)] ≤ α (expected hallucination rate bounded).\",\n    \"limitations_and_open_questions\": \"Assumes exchangeability between calibration and test data — breaks under distribution shift (exactly what corpus poisoning induces). Only evaluated on closed-book QA; no retrieval component means the framework doesn't address how retrieved context affects self-consistency signals.\",\n    \"building_blocks\": [\n      \"Self-consistency as nonconformity score\",\n      \"Conformal risk control calibration procedure\",\n      \"LLM-as-judge match function with separate calibration\",\n      \"Expectation-based (not marginal) hallucination guarantees\",\n      \"Prompt-only method requiring no model access\"\n    ],\n    \"relevance_to_seed\": \"Most directly relevant abstention mechanism — our work extends this to RAG by replacing closed-book self-consistency with retrieval-agreement-conditioned scores, and addresses the exchangeability violation that corpus poisoning introduces (which this paper assumes away).\"\n  },\n  {\n    \"title\": \"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"No systematic evaluation existed comparing RAG poisoning attacks and defenses across diverse architectures and scales. The gap was identified by noting that prior attack/defense papers each use different datasets, metrics, and RAG configurations, making cross-comparison impossible.\",\n    \"key_insight\": \"Expanding knowledge bases with semantically similar correct documents passively reduces attack effectiveness (dilution effect), and poisoned texts designed for naive RAG transfer unexpectedly well to advanced architectures (sequential, branching, loop, agentic), revealing that architectural complexity alone doesn't provide robustness.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Evaluates 13 attacks (7 targeted: BPRAG, WPRAG, BPI, WPI, AGGD, CRAG-AS, CRAG-AK; 3 DoS: JamInject/Oracle/Opt; 3 trigger-based: AgentPoison, BadRAG, Phantom) against 7 defenses (process-optimized: Paraphrasing, InstructRAG, RobustRAG, AstuteRAG, TrustRAG; detection-based: PPL, Norm) across 5 datasets (NQ, HotpotQA, MS-MARCO, SQuAD, BoolQ) with medium/large expansions. Tests sequential, branching, conditional, loop RAG plus agentic and multimodal variants.\",\n    \"limitations_and_open_questions\": \"Does not evaluate conformal-prediction-based defenses or abstention mechanisms; focused on QA accuracy rather than coverage/abstention tradeoffs. Does not consider adaptive attacks specifically designed against each defense.\",\n    \"building_blocks\": [\n      \"Standardized evaluation protocol across 13 attacks and 7 defenses\",\n      \"Dataset expansion methodology for robustness testing\",\n      \"Cross-architecture transferability analysis\",\n      \"Finding: process-optimized defenses work only for DoS; detection methods fail on sophisticated poisoning\"\n    ],\n    \"relevance_to_seed\": \"Provides evaluation infrastructure and key finding that current defenses fail — motivates our conformal abstention approach as a complementary mechanism. We adopt their NQ/HotpotQA/MS-MARCO datasets and attack protocols (CRAG-AS/AK) for evaluation.\"\n  },\n  {\n    \"title\": \"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\",\n    \"venue\": \"ICML 2024\",\n    \"problem_identification\": \"No provable guarantees existed that RAG actually reduces generation risk vs. standalone LLMs. Prior conformal prediction methods were limited to classification or required monotonic loss functions, excluding text generation risks.\",\n    \"key_insight\": \"Conformal risk control can be extended to RAG generation with non-monotonic bounded losses by introducing a constrained generation protocol (parameterized by retrieval count, generation set size, diversity threshold) that produces candidate sets amenable to set-based risk analysis.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines a constrained generation protocol parameterized by λ=(N_rag, λ_g, λ_s) producing candidate generation sets. Derives conformal risk bounds via KL-divergence and binomial CDF inversions on calibration data. Proves RAG reduces conformal generation risk under conditions on retriever quality (V_rag-qualified) and transformer architecture ((d+,Φ_M)-transformer). Extends to distribution shift via Hellinger distance bounds: α̂(ρ) = R̂ + √(V̂/N_cal)·q_δ + 2ρ + 2ρ², the first such guarantee for general bounded (not just monotone) risk functions.\",\n    \"limitations_and_open_questions\": \"Theoretical analysis restricted to single-layer transformers with token-level simplification. Distribution shift extension requires knowing/estimating Hellinger distance bound ρ; adversarial retrieval corruption (where ρ is unbounded or unknown) is explicitly unaddressed.\",\n    \"building_blocks\": [\n      \"Conformal risk bound formulation for generation sets\",\n      \"Distribution shift extension via Hellinger distance for bounded losses\",\n      \"V_rag retriever quality metric\",\n      \"Constrained generation protocol producing candidate sets\"\n    ],\n    \"relevance_to_seed\": \"Provides the theoretical foundation for conformal risk guarantees in RAG but assumes benign retrieval — our work must handle the case where corpus poisoning makes ρ adversarially large or unknown, necessitating retrieval-aware score functions rather than distribution-distance assumptions.\"\n  },\n  {\n    \"title\": \"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"RobustRAG's keyword/token-level majority voting causes severe information loss (~20-point degradation on long-form generation) and ignores reliability signals (document ranking, domain authority) that web search engines already provide and adversaries cannot easily manipulate.\",\n    \"key_insight\": \"Framing robust document selection as Maximum Independent Set computation on an NLI-derived contradiction graph naturally excludes adversarial documents (which contradict benign majorities) while preserving full document content for generation, and lexicographic tie-breaking incorporates ranking reliability without modifying the MIS objective.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Generates isolated per-document answers, constructs a contradiction graph via pairwise NLI (DeBERTa), and computes MIS with lexicographic tie-breaking favoring higher-ranked documents. For k≤20, uses brute-force enumeration; for larger k, uses weighted sampling (γ=0.9 exponential decay by rank) drawing m=2 docs per round over T=20 rounds, then applies MIS to intermediate answers. Proves contamination probability vanishes as e^{-Ω(k)} under k'≤k/5 corruption and bounded NLI error rates.\",\n    \"limitations_and_open_questions\": \"Assumes adversarial documents produce NLI-detectable contradictions with benign majority — subtle misinformation may evade detection. Provides certified robustness but no conformal/abstention mechanism — cannot quantify residual risk or guarantee answer correctness when the MIS itself is contaminated.\",\n    \"building_blocks\": [\n      \"NLI-based contradiction graph construction\",\n      \"MIS formulation for document selection\",\n      \"Weighted sampling with rank-based decay for scalability\",\n      \"Isolated per-document answer generation\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline and complementary technique — ReliabilityRAG certifies document selection but cannot abstain or quantify residual risk; our conformal abstention framework fills exactly this gap by providing coverage guarantees on top of (or independent of) document selection defenses.\"\n  },\n  {\n    \"title\": \"Large Language Model Validity via Enhanced Conformal Prediction Methods\",\n    \"venue\": \"NeurIPS 2024\",\n    \"problem_identification\": \"Marginal conformal factuality guarantees hide dangerous variation across topics — empirically, coverage drops from ~95% for high-popularity Wikipedia articles to ~70% for low-popularity ones, precisely where errors are most harmful. Additionally, achieving 90% marginal factuality requires filtering ~76% of claims, destroying utility.\",\n    \"key_insight\": \"Replacing marginal conformal guarantees with function-class conditional guarantees, and allowing the confidence level α(X) to vary per-prompt via level-adaptive calibration, produces self-aware outputs that report calibrated per-prompt factuality probabilities while retaining substantially more claims.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Extends Gibbs et al.'s conditional conformal framework to monotone losses via score S(C,W)=inf{τ|L(F(C;τ),W)≤λ}, achieving group-conditional risk control for user-specified function classes. Introduces level-adaptive conformal prediction where α(X) is learned via two-fold splitting to target claim retention rates, with Theorem 3.2 proving calibration: P(factual|α∈I, P∈G)=E[α|α∈I, P∈G]. Proposes conditional boosting — differentiable optimization of scoring functions through the quantile regression LP using Proposition 3.1's explicit derivative of the threshold w.r.t. score parameters.\",\n    \"limitations_and_open_questions\": \"Requires exchangeability assumption that deployment may violate. Conditional boosting depends on LP basis stability (requires dithering). Does not address adversarial settings where score functions themselves may be manipulated.\",\n    \"building_blocks\": [\n      \"Group-conditional conformal coverage for LLMs\",\n      \"Level-adaptive conformal prediction with per-input α(X)\",\n      \"Differentiable score optimization through quantile regression LP\",\n      \"Conditional boosting avoiding marginal-only optimization pitfalls\"\n    ],\n    \"relevance_to_seed\": \"Directly relevant to group-conditional coverage under retrieval corruption — our retrieval-agreement groups can serve as the conditioning function class, and level-adaptive calibration enables varying abstention thresholds based on retrieval quality signals.\"\n  },\n  {\n    \"title\": \"Conformal Risk Control\",\n    \"venue\": \"ICLR 2024\",\n    \"problem_identification\": \"Standard conformal prediction only controls coverage (indicator loss), but real applications need control over richer losses — false negative rates in segmentation, missed labels in multilabel classification, F1-score in QA. No unified framework existed for distribution-free finite-sample control of arbitrary loss functions.\",\n    \"key_insight\": \"The essential ingredient making conformal prediction work is not coverage-specific — it is the monotonicity of the loss in a tuning parameter λ; any non-increasing, right-continuous, bounded loss inherits the same exchangeability-based finite-sample guarantee via a 5-line algorithm.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Finds λ̂=inf{λ: [n/(n+1)]R̂_n(λ)+B/(n+1)≤α}, which is an upper confidence bound treating the unobserved test loss as its maximum B. Proves E[L_{n+1}(λ̂)]≤α (exact finite-sample) with matching lower bound α−2B/(n+1) (tight to O(1/n)). Extends to covariate shift via importance weighting, arbitrary shift via TV distance bounds, quantile risk control, simultaneous control of multiple risks (no Bonferroni needed), adversarial worst-case risk, and U-statistic risks for multi-sample losses.\",\n    \"limitations_and_open_questions\": \"Monotonicity is provably necessary (Proposition 2.1 shows non-monotone losses can push risk to maximum B). Distribution shift extension requires known importance weights. Factor-of-2 tightness overhead vs. standard CP. Reviewers noted lack of experiments for the distribution shift and adversarial extensions.\",\n    \"building_blocks\": [\n      \"Monotone loss risk control algorithm (5-line procedure)\",\n      \"Distribution shift extension via importance weighting and TV bounds\",\n      \"Multiple simultaneous risk control without Bonferroni correction\",\n      \"Adversarial worst-case risk control formulation\"\n    ],\n    \"relevance_to_seed\": \"Core theoretical building block — our abstention loss is monotone in the abstention threshold, enabling direct application of CRC; the distribution shift extension via TV distance provides a template for bounding coverage degradation under corpus poisoning, though we need retrieval-specific bounds rather than generic TV distance.\"\n  },\n  {\n    \"title\": \"Conformal Language Modeling\",\n    \"venue\": \"ICLR 2024\",\n    \"problem_identification\": \"Conformal prediction requires enumerating or scoring all possible outputs to construct prediction sets, which is intractable for generative language models with combinatorially explosive output spaces. No framework existed for distribution-free coverage guarantees over free-text LM outputs.\",\n    \"key_insight\": \"Replace exhaustive enumeration with calibrated sampling — define conformal prediction sets through stopping rules (when to stop sampling) and rejection rules (what to keep), calibrated via Learn-then-Test to guarantee at least one admissible answer exists in the retained set with high probability.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Parameterizes sampling by λ=(λ₁,λ₂,λ₃) controlling diversity threshold (ROUGE-L similarity), quality threshold (LM log-likelihood), and stopping confidence. Calibrates λ via LTT framework with binomial tail p-values and FWER-controlling multiple testing across a 3D grid, optimizing for set size and sampling efficiency. Extends to component-level guarantees by decomposing outputs into sentences and applying an inner conformal procedure with separate threshold γ. Proves P(∃y∈C: A(y)=1)≥1−ε with probability ≥1−δ over calibration draws.\",\n    \"limitations_and_open_questions\": \"Guarantees are marginal, not conditional (coverage varies by topic — addressed by Cherian et al.). Requires reliable admission functions and labeled calibration data. Sampling budget k_max=20 limits achievable ε. Follow-up work (Mohri & Hashimoto) criticized returned sets as opaque and hard to interpret for end users.\",\n    \"building_blocks\": [\n      \"Sampling-based conformal prediction for intractable output spaces\",\n      \"Stopping and rejection rules as conformal parameters\",\n      \"Component-level conformal guarantees via inner procedure\",\n      \"LTT-based multi-parameter calibration with Pareto testing\"\n    ],\n    \"relevance_to_seed\": \"Methodological ancestor — our abstention mechanism can be viewed as a rejection rule calibrated over RAG outputs, but we must handle the non-exchangeability introduced by adversarial retrieval rather than assuming i.i.d. sampling; the component-level guarantee concept maps to our per-claim factuality certificates.\"\n  },\n  {\n    \"title\": \"Language Models with Conformal Factuality Guarantees\",\n    \"venue\": \"ICML 2024\",\n    \"problem_identification\": \"No existing method provided formal statistical guarantees on open-ended LLM factuality — prior CP work for LMs was limited to token-level sets or multiple-choice reductions, none producing interpretable single outputs with coverage certificates.\",\n    \"key_insight\": \"LLM factuality maps to uncertainty quantification via entailment sets: output y is correct iff the ground truth y* lies in E(y) = {y' : y' ⊨ y}, so conformal coverage over entailment sets directly translates to factuality guarantees through a back-off algorithm that progressively removes sub-claims.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Decomposes LLM outputs into atomic sub-claims, scores each (via frequency/confidence), and applies split CP with a nested back-off function F_t that removes low-scoring claims to expand entailment sets. The calibration quantile q̂_α determines how many claims to retain. An entailment decomposability assumption (Assumption 5.1) ensures claim-level filtering preserves coverage. Achieves ~80% factuality on FActScore (up from 25%) while retaining ~50% of claims.\",\n    \"limitations_and_open_questions\": \"Guarantees are marginal (averaged over calibration draws), not conditional per-input — follow-up work showed under-coverage for underrepresented topics and near-complete censorship at high factuality levels. Claims are evaluated independently, ignoring logical dependencies.\",\n    \"building_blocks\": [\n      \"Entailment-set formulation of factuality as CP coverage\",\n      \"Sub-claim decomposition + scoring + filtering pipeline\",\n      \"Back-off algorithm framework for nested conformal sets\",\n      \"Frequency scoring as nonconformity measure\"\n    ],\n    \"relevance_to_seed\": \"Foundational paradigm our work extends — we must handle the case where retrieved documents (which ground the entailment sets) are adversarially poisoned, invalidating the exchangeability assumption this method relies on.\"\n  },\n  {\n    \"title\": \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"No prior work systematically studied whether conformal factuality guarantees survive when combined with RAG — existing metrics (empirical factuality) masked failures by treating empty outputs as trivially factual, hiding a critical factuality-informativeness tradeoff.\",\n    \"key_insight\": \"Standard conformal factuality for RAG produces vacuous outputs at high confidence levels and its guarantees break under distribution shift and distractor injection — the problem is diagnosed but unsolved, creating a clear gap for robust alternatives.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Introduces three metrics — Non-Empty Rate, Non-Vacuous Empirical Factuality, and Sufficient Correctness — that jointly capture both correctness and informativeness. Systematically evaluates the conformal factuality pipeline across FActScore/MATH/NQ, testing robustness to calibration-test domain mismatch and distractor documents in retrieval. Shows lightweight NLI-based entailment verifiers match LLM-based scorers at 100× fewer FLOPs.\",\n    \"limitations_and_open_questions\": \"Purely diagnostic — proposes no solution to the robustness failures identified. Does not consider adversarial/poisoning attacks (only natural distribution shift and distractors). The sufficient correctness metric lacks formal definition tied to conformal guarantees.\",\n    \"building_blocks\": [\n      \"Non-Empty Rate and Non-Vacuous Factuality metrics\",\n      \"Empirical evidence that CP guarantees break under RAG distribution shift\",\n      \"Finding that lightweight NLI verifiers are competitive scorers\",\n      \"Systematic failure mode taxonomy for conformal RAG pipelines\"\n    ],\n    \"relevance_to_seed\": \"Directly motivates our work — demonstrates the problem (CP breaks under RAG distribution shift) without providing a solution; our retrieval-aware score function and poisoning-robust abstention framework addresses exactly this diagnosed gap.\"\n  },\n  {\n    \"title\": \"Conformal Prediction as Bayesian Quadrature\",\n    \"venue\": \"ICML 2025 (Outstanding Paper Award)\",\n    \"problem_identification\": \"Standard CP provides marginal guarantees averaged over hypothetical calibration sets, but practitioners need data-conditional guarantees for their specific observed data — CRC violated its target risk in 21% (synthetic) to 45% (MS-COCO) of trials despite valid average guarantees.\",\n    \"key_insight\": \"Bounding expected loss equals integrating the quantile function over [0,1], a Bayesian quadrature problem where the distribution-free Dirichlet property of quantile spacings provides the prior over evaluation sites without any distributional assumptions.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Constructs a stochastic upper bound L⁺ = Σ Uᵢ·l₍ᵢ₎ where Uᵢ ~ Dir(1,...,1) are quantile spacings and l₍ᵢ₎ are ordered calibration losses. L⁺ stochastically dominates the posterior risk under any prior (Theorem 4.5), yielding a full posterior distribution over a provable loss upper bound. Recovers CRC as using only E[L⁺], explaining why CRC is loose — it discards all distributional information. Reduces violation rates from 45% to 5.4% on MS-COCO.\",\n    \"limitations_and_open_questions\": \"Provides data-conditional (conditioned on calibration losses) not input-conditional guarantees — still averages over test inputs. Computational cost of sampling from the Dirichlet posterior for large calibration sets not fully characterized. Extension to non-exchangeable settings unexplored.\",\n    \"building_blocks\": [\n      \"Data-conditional CP guarantees via Bayesian quadrature\",\n      \"L⁺ stochastic dominance bound as a richer alternative to CRC's point estimate\",\n      \"Dirichlet quantile spacing property for distribution-free Bayesian inference\",\n      \"Unification showing SCP and CRC as special cases\"\n    ],\n    \"relevance_to_seed\": \"Offers a strictly stronger CP framework we could adopt — replacing CRC-style point thresholds with full posterior bounds over risk could yield tighter abstention decisions; the data-conditional guarantees are especially valuable when calibration sets are small or heterogeneous.\"\n  },\n  {\n    \"title\": \"Conformal Prediction for Natural Language Processing: A Survey\",\n    \"venue\": \"TACL 2024\",\n    \"problem_identification\": \"No prior survey bridged conformal prediction theory to NLP applications — general CP surveys existed and NLP uncertainty surveys existed, but neither systematically mapped CP variants (Mondrian, non-exchangeable, risk-controlling) onto NLP task categories.\",\n    \"key_insight\": \"CP's model-agnostic, distribution-free guarantees requiring only exchangeability and a small calibration set make it uniquely suited to NLP's black-box LLM era — but the autoregressive, high-cardinality nature of language generation creates fundamental tensions with CP's assumptions.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Organizes CP for NLP along two axes: CP variants (split, full, cross-conformal, Mondrian, weighted/non-exchangeable, conformal risk control, density-based, Venn-Abers) and NLP applications (classification/tagging, generation at sentence/token level, uncertainty-based evaluation, efficient inference). Identifies that non-exchangeability bounds require estimating TV distance between unknown distributions, a key open problem for autoregressive generation.\",\n    \"limitations_and_open_questions\": \"Published mid-2024, so misses the conformal factuality line (Mohri & Hashimoto), RAG-specific CP work, and poisoning-robust CP developments. Does not cover adversarial robustness of CP guarantees at all. Token-level CP for autoregressive generation remains an open problem.\",\n    \"building_blocks\": [\n      \"Taxonomy of CP variants applicable to NLP\",\n      \"Identification of exchangeability violations in autoregressive generation\",\n      \"Catalog of nonconformity score designs for text\",\n      \"Open challenge list including fairness, label variation, and conditional coverage\"\n    ],\n    \"relevance_to_seed\": \"Essential positioning reference — our work sits at the intersection of several categories (generation-level CP, non-exchangeable extensions, risk control) and addresses the survey's identified open challenge of CP under distribution shift, specifically adversarial shift from corpus poisoning.\"\n  },\n  {\n    \"title\": \"Conformal Selective Prediction with General Risk Control (SCoRE)\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Existing conformal selective prediction handled only binary risk (correct/incorrect), but high-stakes deployments require controlling continuous-valued risks (MSE, semantic error magnitude) — p-values are the wrong instrument for expectation-based continuous risk control.\",\n    \"key_insight\": \"Selective prediction under continuous risk is hypothesis testing with unknown random weights, and risk-adjusted e-values (satisfying E[E·L] ≤ 1 rather than E[E] ≤ 1) are the natural currency — they accommodate expectation-based risk control through simple Markov-inequality thresholding.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Defines risk-adjusted e-values where the product E(n+j)·L(n+j) has expectation ≤ 1 under exchangeability. Thresholding at 1/α controls Marginal Deployment Risk; plugging into e-BH controls Selective Deployment Risk (continuous FDR analog). Proves Neyman-Pearson optimality: the optimal score is monotone in l(x)/r(x) (conditional risk-to-reward ratio). Extends to covariate shift via importance weighting. Demonstrated on drug discovery, clinical prediction, and LLM abstention.\",\n    \"limitations_and_open_questions\": \"Requires bounded loss in [0,1] — unbounded risks need truncation or alternative constructions. The covariate shift extension requires density ratio estimation, which is hard in high dimensions. Power analysis under finite samples and comparison to concentration-based alternatives not fully explored.\",\n    \"building_blocks\": [\n      \"Risk-adjusted e-values for continuous risk control\",\n      \"MDR and SDR as two distinct deployment risk objectives\",\n      \"E-BH procedure for selective deployment with FDR-analog guarantees\",\n      \"Finite-sample, distribution-free trust/abstain decisions under exchangeability\"\n    ],\n    \"relevance_to_seed\": \"Directly applicable to our abstention mechanism — SCoRE's e-value framework could replace or complement our conformal abstention layer, providing trust/abstain decisions with continuous risk control (e.g., semantic error magnitude) rather than binary correctness, and its covariate shift extension addresses part of the distribution shift from poisoning.\"\n  },\n  {\n    \"title\": \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"Standard conformal prediction provides no coverage guarantees when adversaries poison training or calibration data—a threat entirely ignored by prior CP methods (RSCP, CAS) that only addressed test-time evasion. The authors identified this by observing that even a single poisoned calibration point can arbitrarily inflate or shrink prediction sets.\",\n    \"key_insight\": \"Partitioning data into K subsets and aggregating via smoothed scores (training) and majority-vote prediction sets (calibration) ensures that an adversary corrupting fewer than K/2 partitions cannot break coverage guarantees—reducing poisoning robustness to a majority-resilience problem.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"RPS partitions training data into K subsets, trains K independent classifiers, and defines a smoothed score as the proportion of classifiers agreeing on a class. For calibration poisoning, K prediction sets are constructed on disjoint calibration subsets and aggregated via majority vote—a class is included only if it appears in >K/2 individual sets. Formal certificates guarantee coverage under worst-case poisoning within the declared budget. Reviewers (8/8/6) praised the novel threat model and sound theory; criticisms centered on missing baselines, limited large-scale experiments, and the partition approach being known in differential privacy contexts.\",\n    \"limitations_and_open_questions\": \"Partitioning reduces effective data per model, sacrificing utility for robustness. Critically, RPS addresses calibration-set poisoning (wrong labels in known data) but not test-time retrieval corruption (wrong documents injected at inference)—a fundamentally different threat model.\",\n    \"building_blocks\": [\n      \"Partition-and-vote mechanism for poisoning robustness\",\n      \"Smoothed score functions over classifier ensembles\",\n      \"Majority prediction set aggregation rule\",\n      \"Formal coverage certificates under bounded poisoning budget\"\n    ],\n    \"relevance_to_seed\": \"Direct methodological ancestor: the partition-and-vote idea inspires our retrieval-agreement score construction, but the threat model mismatch (calibration poisoning vs. retrieval corruption) is precisely the gap our work addresses.\"\n  },\n  {\n    \"title\": \"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models\",\n    \"venue\": \"USENIX Security 2025\",\n    \"problem_identification\": \"Prior RAG security research ignored the knowledge database as an attack surface; the authors identified that the retriever's reliance on embedding similarity creates an exploitable channel for injecting adversarial content into the generation context.\",\n    \"key_insight\": \"A successful RAG poisoning attack decomposes into two independently optimizable conditions—retrieval similarity (the poisoned text must be retrieved) and generation influence (the LLM must produce the target answer)—enabling efficient crafting of minimal-injection attacks.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Each malicious text P = S ⊕ I concatenates a retrieval-optimized suffix S with a generation-optimized payload I. In black-box mode, S is simply the target question and I is LLM-generated text that produces the target answer. In white-box mode, S is optimized via HotFlip to maximize embedding similarity with the target query. Only 5 injected texts per question into million-document corpora achieve ~90% attack success across multiple LLMs and retrievers. Evaluated defenses (paraphrasing, perplexity filtering, deduplication) prove insufficient.\",\n    \"limitations_and_open_questions\": \"Attacks are query-specific (separate poisoned texts per target question), limiting scalability to open-ended adversarial goals. Does not consider adaptive defenses like agreement-based filtering or certified robustness frameworks.\",\n    \"building_blocks\": [\n      \"RAG corpus poisoning threat model and attack formulation\",\n      \"Retrieval+generation condition decomposition\",\n      \"Black-box and white-box attack protocols for evaluation\",\n      \"Benchmark datasets (NQ, HotpotQA, MS-MARCO) with poisoning\"\n    ],\n    \"relevance_to_seed\": \"Defines the primary attack protocol (PoisonedRAG attack) our framework must defend against; the retrieval+generation decomposition constrains attacker capability and informs our agreement-based score design.\"\n  },\n  {\n    \"title\": \"Robust Yet Efficient Conformal Prediction Sets\",\n    \"venue\": \"ICML 2024\",\n    \"problem_identification\": \"RSCP's mean-based bounds on randomized-smoothed conformity scores produce unnecessarily large prediction sets (often trivially including all classes), and it handles only evasion attacks on continuous data—not poisoning or discrete/graph inputs.\",\n    \"key_insight\": \"Bounding the CDF of conformity score distributions (rather than just the mean) yields provably tighter worst-case bounds, because CDF-based analysis exploits the full distributional shape rather than collapsing to a single summary statistic.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CAS partitions the score space into bins and bounds the CDF at each boundary under adversarial perturbation, yielding tighter upper bounds on worst-case scores than RSCP's mean-based approach. For poisoning, calibration-time robustness is formulated as a MILP that finds the worst-case quantile threshold under bounded label/feature corruption. Sparse smoothing via XOR-based perturbations extends guarantees to discrete and graph-structured data. The calibration-time variant computes bounds only on calibration data, avoiding per-test-point verification overhead.\",\n    \"limitations_and_open_questions\": \"Still requires randomized smoothing overhead and Monte Carlo sampling for score estimation. MILP-based poisoning bounds may not scale to very large calibration sets. Like RPS, addresses calibration/evasion poisoning—not test-time retrieval corruption.\",\n    \"building_blocks\": [\n      \"CDF-based conformity score bounds (tighter than mean-based)\",\n      \"Joint evasion+poisoning robustness framework\",\n      \"MILP for worst-case calibration quantile under poisoning\",\n      \"Sparse smoothing for discrete/graph data\"\n    ],\n    \"relevance_to_seed\": \"CDF-based bounding could yield more efficient prediction sets in our setting than RPS-style majority voting; the calibration-time poisoning formulation is a template for our retrieval-corruption certificates, though the threat model must be adapted.\"\n  },\n  {\n    \"title\": \"Know Your Limits: A Survey of Abstention in Large Langua\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:45:35.874Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:45:35.874Z",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-30T06:45:35.886Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-30 (UTC).**

## Research area: Target: AAAI 2026
Track: Safe, Robust and Responsible AI (SRRAI)

Direction: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.

Seed Papers:
- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval
- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG
- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism
- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative
- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on
- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition

Known Gaps:
- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)
- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails
- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis

Theoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.

Constraints:
- Compute: ≤200 H100-hours
- Must compare against RobustRAG and ReliabilityRAG baselines
- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols
- AAAI 2026 submission deadline: August 2026

Quality Self-Checks:
- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.
- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.
- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.
- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.

Avoid:
- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this
- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead
- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates

## Paper analyses (20 papers)

[
  {
    "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
    "venue": "NAACL 2024",
    "problem_identification": "RAG systems provide no statistical guarantees on answer correctness despite being designed to reduce hallucinations. The gap was identified by noting that conformal prediction—a well-established tool for classification/regression—had never been applied to the compound retriever+generator pipeline where uncertainty propagates across components.",
    "key_insight": "Decompose RAG uncertainty into retriever and generator components, define semantic-level nonconformity scores via Monte Carlo sampling and NLI/ROUGE clustering, then union-bound across pipeline stages for end-to-end coverage guarantees.",
    "innovation_type": "cross_domain",
    "method_summary": "Defines retriever NCM as negative query-passage inner product and generator NCM via sampled response clustering (ROUGE>0.7 or NLI entailment). Calibration computes empirical quantiles on held-out data. Prediction sets are constructed per-stage and unioned: passages meeting retriever threshold feed into per-passage LLM sets, aggregated into final prediction set. Bayesian optimization allocates error budget (α_Ret + α_LLM = α) to minimize average set size.",
    "limitations_and_open_questions": "Critically assumes benign retrieval—the guarantee Pr(r*∈C_Agg)≥1-α requires exchangeability of calibration and test retrieval, which corpus poisoning violates. Also requires the true relevant passage to appear in top-K, with no mechanism for adversarial retrieval manipulation.",
    "building_blocks": [
      "Semantic clustering via ROUGE/NLI for nonconformity scores",
      "Pipeline decomposition with union-bound error allocation",
      "Bayesian optimization for error budget tuning",
      "Monte Carlo response sampling for uncertainty estimation"
    ],
    "relevance_to_seed": "Direct foundation—our work extends TRAQ's conformal framework to handle adversarial retrieval by replacing its benign-assumption NCM with retrieval-agreement-conditioned scores that restore coverage under bounded poisoning."
  },
  {
    "title": "Certifiably Robust RAG against Retrieval Corruption",
    "venue": "IEEE SaTML 2026",
    "problem_identification": "RAG systems are vulnerable to adversarial passage injection but no defense offered formal robustness certificates. The gap was identified by observing that existing empirical defenses (filtering, detection) provide no worst-case guarantees against adaptive attackers with full system knowledge.",
    "key_insight": "Isolating passages into disjoint groups ensures poisoned documents contaminate only their own group's LLM response, enabling secure aggregation where attacker influence is bounded by the ratio of corrupted groups to total groups.",
    "innovation_type": "new_technique",
    "method_summary": "Partitions k retrieved passages into m=⌈k/ω⌉ disjoint groups of size ω, generates independent LLM responses per group, then aggregates via either keyword voting (count keywords across responses, threshold-filter) or decoding-level probability aggregation (sum next-token distributions, use probability gap to decide tokens). Certification enumerates worst-case attacker influence: for keywords, classifies them as always/never/controllably retained; for decoding, explores a token-sequence tree bounded by probability margins.",
    "limitations_and_open_questions": "Requires m LLM calls (high compute), group size ω trades off response quality vs. robustness, and certification only covers bounded k' poisoned passages with no abstention mechanism when certification fails (outputs τ=0 without actionable fallback). No conformal coverage guarantee.",
    "building_blocks": [
      "Isolate-then-aggregate framework",
      "Keyword voting aggregation",
      "Decoding-level probability aggregation",
      "Certification via worst-case enumeration",
      "Threat model: adaptive attacker with bounded injection budget k'"
    ],
    "relevance_to_seed": "Primary baseline and complementary approach—RobustRAG provides certified robustness but no conformal abstention; our method adds distribution-free coverage guarantees and principled abstention decisions on top of similar partition-based architectures."
  },
  {
    "title": "CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation",
    "venue": "ACM SACMAT 2026",
    "problem_identification": "Prior attacks like PoisonedRAG require injecting multiple (3-5) documents per query to outnumber benign passages in top-K, which is unrealistic and detectable. The gap was identified by noting that in real knowledge bases with millions of documents, injecting many texts per query at scale triggers volume-based detection.",
    "key_insight": "A single poisoned document can achieve high attack success by decomposing it into a retrieval component (verbatim query text for guaranteed retrieval) and a generation component (adversarial framing exploiting LLM recency bias) — separating the retrieval and influence objectives.",
    "innovation_type": "simplification",
    "method_summary": "Constructs each poisoned document with two parts: p_i^s (retrieval) set to the query itself ensuring maximal retriever similarity, and p_i^h (generation) containing adversarial framing that marks correct answers as 'outdated' while asserting the target answer as 'confirmed by latest data.' CorruptRAG-AK variant uses an LLM to refine templates into coherent adversarial knowledge. Achieves 95% ASR with single document vs. PoisonedRAG's 69% single-doc baseline.",
    "limitations_and_open_questions": "Relies on LLM recency bias which may not generalize across all models; effectiveness against defenses like RobustRAG's isolation (where single poisoned doc affects only one group) is unclear. How does agreement-based detection handle single vs. multi-doc poisoning?",
    "building_blocks": [
      "Single-document threat model for realistic evaluation",
      "Retrieval-generation decomposition of poisoned documents",
      "Recency-bias exploitation templates",
      "Near-zero cost attack ($0.0001/query)"
    ],
    "relevance_to_seed": "Key attack baseline for evaluation — single-doc poisoning is harder to detect via agreement signals (only 1 of k passages is adversarial), directly testing whether our retrieval-agreement scores can identify isolated poisoned passages within agreement groups."
  },
  {
    "title": "Mitigating LLM Hallucinations via Conformal Abstention",
    "venue": "NeurIPS 2024 (Google DeepMind)",
    "problem_identification": "LLMs hallucinate unpredictably and existing confidence measures (log-probs) degrade with response length, providing no formal guarantees on when to abstain. The gap was identified by noting that self-consistency signals were used heuristically but never combined with conformal prediction's distribution-free guarantees.",
    "key_insight": "LLM self-evaluated response similarity across multiple samples serves as a valid nonconformity score for conformal risk control, enabling calibration of an abstention threshold with provable bounds on hallucination rate — without requiring model internals or fine-tuning.",
    "innovation_type": "new_formulation",
    "method_summary": "Samples k responses per query, uses the LLM itself to evaluate pairwise similarity (match function m calibrated separately via conformal procedure on threshold β). Computes confidence g(X) as match count or expected match count. Applies conformal risk control: finds threshold λ̂_n = inf{λ: (n/(n+1))L_n(λ) + 1/(n+1) ≤ α} on calibration set. Abstains when g(X) < λ̂_n. Guarantees E[R(λ̂_n)] ≤ α (expected hallucination rate bounded).",
    "limitations_and_open_questions": "Assumes exchangeability between calibration and test data — breaks under distribution shift (exactly what corpus poisoning induces). Only evaluated on closed-book QA; no retrieval component means the framework doesn't address how retrieved context affects self-consistency signals.",
    "building_blocks": [
      "Self-consistency as nonconformity score",
      "Conformal risk control calibration procedure",
      "LLM-as-judge match function with separate calibration",
      "Expectation-based (not marginal) hallucination guarantees",
      "Prompt-only method requiring no model access"
    ],
    "relevance_to_seed": "Most directly relevant abstention mechanism — our work extends this to RAG by replacing closed-book self-consistency with retrieval-agreement-conditioned scores, and addresses the exchangeability violation that corpus poisoning introduces (which this paper assumes away)."
  },
  {
    "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
    "venue": "arXiv 2025",
    "problem_identification": "No systematic evaluation existed comparing RAG poisoning attacks and defenses across diverse architectures and scales. The gap was identified by noting that prior attack/defense papers each use different datasets, metrics, and RAG configurations, making cross-comparison impossible.",
    "key_insight": "Expanding knowledge bases with semantically similar correct documents passively reduces attack effectiveness (dilution effect), and poisoned texts designed for naive RAG transfer unexpectedly well to advanced architectures (sequential, branching, loop, agentic), revealing that architectural complexity alone doesn't provide robustness.",
    "innovation_type": "new_benchmark",
    "method_summary": "Evaluates 13 attacks (7 targeted: BPRAG, WPRAG, BPI, WPI, AGGD, CRAG-AS, CRAG-AK; 3 DoS: JamInject/Oracle/Opt; 3 trigger-based: AgentPoison, BadRAG, Phantom) against 7 defenses (process-optimized: Paraphrasing, InstructRAG, RobustRAG, AstuteRAG, TrustRAG; detection-based: PPL, Norm) across 5 datasets (NQ, HotpotQA, MS-MARCO, SQuAD, BoolQ) with medium/large expansions. Tests sequential, branching, conditional, loop RAG plus agentic and multimodal variants.",
    "limitations_and_open_questions": "Does not evaluate conformal-prediction-based defenses or abstention mechanisms; focused on QA accuracy rather than coverage/abstention tradeoffs. Does not consider adaptive attacks specifically designed against each defense.",
    "building_blocks": [
      "Standardized evaluation protocol across 13 attacks and 7 defenses",
      "Dataset expansion methodology for robustness testing",
      "Cross-architecture transferability analysis",
      "Finding: process-optimized defenses work only for DoS; detection methods fail on sophisticated poisoning"
    ],
    "relevance_to_seed": "Provides evaluation infrastructure and key finding that current defenses fail — motivates our conformal abstention approach as a complementary mechanism. We adopt their NQ/HotpotQA/MS-MARCO datasets and attack protocols (CRAG-AS/AK) for evaluation."
  },
  {
    "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
    "venue": "ICML 2024",
    "problem_identification": "No provable guarantees existed that RAG actually reduces generation risk vs. standalone LLMs. Prior conformal prediction methods were limited to classification or required monotonic loss functions, excluding text generation risks.",
    "key_insight": "Conformal risk control can be extended to RAG generation with non-monotonic bounded losses by introducing a constrained generation protocol (parameterized by retrieval count, generation set size, diversity threshold) that produces candidate sets amenable to set-based risk analysis.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines a constrained generation protocol parameterized by λ=(N_rag, λ_g, λ_s) producing candidate generation sets. Derives conformal risk bounds via KL-divergence and binomial CDF inversions on calibration data. Proves RAG reduces conformal generation risk under conditions on retriever quality (V_rag-qualified) and transformer architecture ((d+,Φ_M)-transformer). Extends to distribution shift via Hellinger distance bounds: α̂(ρ) = R̂ + √(V̂/N_cal)·q_δ + 2ρ + 2ρ², the first such guarantee for general bounded (not just monotone) risk functions.",
    "limitations_and_open_questions": "Theoretical analysis restricted to single-layer transformers with token-level simplification. Distribution shift extension requires knowing/estimating Hellinger distance bound ρ; adversarial retrieval corruption (where ρ is unbounded or unknown) is explicitly unaddressed.",
    "building_blocks": [
      "Conformal risk bound formulation for generation sets",
      "Distribution shift extension via Hellinger distance for bounded losses",
      "V_rag retriever quality metric",
      "Constrained generation protocol producing candidate sets"
    ],
    "relevance_to_seed": "Provides the theoretical foundation for conformal risk guarantees in RAG but assumes benign retrieval — our work must handle the case where corpus poisoning makes ρ adversarially large or unknown, necessitating retrieval-aware score functions rather than distribution-distance assumptions."
  },
  {
    "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
    "venue": "NeurIPS 2025",
    "problem_identification": "RobustRAG's keyword/token-level majority voting causes severe information loss (~20-point degradation on long-form generation) and ignores reliability signals (document ranking, domain authority) that web search engines already provide and adversaries cannot easily manipulate.",
    "key_insight": "Framing robust document selection as Maximum Independent Set computation on an NLI-derived contradiction graph naturally excludes adversarial documents (which contradict benign majorities) while preserving full document content for generation, and lexicographic tie-breaking incorporates ranking reliability without modifying the MIS objective.",
    "innovation_type": "new_technique",
    "method_summary": "Generates isolated per-document answers, constructs a contradiction graph via pairwise NLI (DeBERTa), and computes MIS with lexicographic tie-breaking favoring higher-ranked documents. For k≤20, uses brute-force enumeration; for larger k, uses weighted sampling (γ=0.9 exponential decay by rank) drawing m=2 docs per round over T=20 rounds, then applies MIS to intermediate answers. Proves contamination probability vanishes as e^{-Ω(k)} under k'≤k/5 corruption and bounded NLI error rates.",
    "limitations_and_open_questions": "Assumes adversarial documents produce NLI-detectable contradictions with benign majority — subtle misinformation may evade detection. Provides certified robustness but no conformal/abstention mechanism — cannot quantify residual risk or guarantee answer correctness when the MIS itself is contaminated.",
    "building_blocks": [
      "NLI-based contradiction graph construction",
      "MIS formulation for document selection",
      "Weighted sampling with rank-based decay for scalability",
      "Isolated per-document answer generation"
    ],
    "relevance_to_seed": "Primary baseline and complementary technique — ReliabilityRAG certifies document selection but cannot abstain or quantify residual risk; our conformal abstention framework fills exactly this gap by providing coverage guarantees on top of (or independent of) document selection defenses."
  },
  {
    "title": "Large Language Model Validity via Enhanced Conformal Prediction Methods",
    "venue": "NeurIPS 2024",
    "problem_identification": "Marginal conformal factuality guarantees hide dangerous variation across topics — empirically, coverage drops from ~95% for high-popularity Wikipedia articles to ~70% for low-popularity ones, precisely where errors are most harmful. Additionally, achieving 90% marginal factuality requires filtering ~76% of claims, destroying utility.",
    "key_insight": "Replacing marginal conformal guarantees with function-class conditional guarantees, and allowing the confidence level α(X) to vary per-prompt via level-adaptive calibration, produces self-aware outputs that report calibrated per-prompt factuality probabilities while retaining substantially more claims.",
    "innovation_type": "new_formulation",
    "method_summary": "Extends Gibbs et al.'s conditional conformal framework to monotone losses via score S(C,W)=inf{τ|L(F(C;τ),W)≤λ}, achieving group-conditional risk control for user-specified function classes. Introduces level-adaptive conformal prediction where α(X) is learned via two-fold splitting to target claim retention rates, with Theorem 3.2 proving calibration: P(factual|α∈I, P∈G)=E[α|α∈I, P∈G]. Proposes conditional boosting — differentiable optimization of scoring functions through the quantile regression LP using Proposition 3.1's explicit derivative of the threshold w.r.t. score parameters.",
    "limitations_and_open_questions": "Requires exchangeability assumption that deployment may violate. Conditional boosting depends on LP basis stability (requires dithering). Does not address adversarial settings where score functions themselves may be manipulated.",
    "building_blocks": [
      "Group-conditional conformal coverage for LLMs",
      "Level-adaptive conformal prediction with per-input α(X)",
      "Differentiable score optimization through quantile regression LP",
      "Conditional boosting avoiding marginal-only optimization pitfalls"
    ],
    "relevance_to_seed": "Directly relevant to group-conditional coverage under retrieval corruption — our retrieval-agreement groups can serve as the conditioning function class, and level-adaptive calibration enables varying abstention thresholds based on retrieval quality signals."
  },
  {
    "title": "Conformal Risk Control",
    "venue": "ICLR 2024",
    "problem_identification": "Standard conformal prediction only controls coverage (indicator loss), but real applications need control over richer losses — false negative rates in segmentation, missed labels in multilabel classification, F1-score in QA. No unified framework existed for distribution-free finite-sample control of arbitrary loss functions.",
    "key_insight": "The essential ingredient making conformal prediction work is not coverage-specific — it is the monotonicity of the loss in a tuning parameter λ; any non-increasing, right-continuous, bounded loss inherits the same exchangeability-based finite-sample guarantee via a 5-line algorithm.",
    "innovation_type": "new_formulation",
    "method_summary": "Finds λ̂=inf{λ: [n/(n+1)]R̂_n(λ)+B/(n+1)≤α}, which is an upper confidence bound treating the unobserved test loss as its maximum B. Proves E[L_{n+1}(λ̂)]≤α (exact finite-sample) with matching lower bound α−2B/(n+1) (tight to O(1/n)). Extends to covariate shift via importance weighting, arbitrary shift via TV distance bounds, quantile risk control, simultaneous control of multiple risks (no Bonferroni needed), adversarial worst-case risk, and U-statistic risks for multi-sample losses.",
    "limitations_and_open_questions": "Monotonicity is provably necessary (Proposition 2.1 shows non-monotone losses can push risk to maximum B). Distribution shift extension requires known importance weights. Factor-of-2 tightness overhead vs. standard CP. Reviewers noted lack of experiments for the distribution shift and adversarial extensions.",
    "building_blocks": [
      "Monotone loss risk control algorithm (5-line procedure)",
      "Distribution shift extension via importance weighting and TV bounds",
      "Multiple simultaneous risk control without Bonferroni correction",
      "Adversarial worst-case risk control formulation"
    ],
    "relevance_to_seed": "Core theoretical building block — our abstention loss is monotone in the abstention threshold, enabling direct application of CRC; the distribution shift extension via TV distance provides a template for bounding coverage degradation under corpus poisoning, though we need retrieval-specific bounds rather than generic TV distance."
  },
  {
    "title": "Conformal Language Modeling",
    "venue": "ICLR 2024",
    "problem_identification": "Conformal prediction requires enumerating or scoring all possible outputs to construct prediction sets, which is intractable for generative language models with combinatorially explosive output spaces. No framework existed for distribution-free coverage guarantees over free-text LM outputs.",
    "key_insight": "Replace exhaustive enumeration with calibrated sampling — define conformal prediction sets through stopping rules (when to stop sampling) and rejection rules (what to keep), calibrated via Learn-then-Test to guarantee at least one admissible answer exists in the retained set with high probability.",
    "innovation_type": "cross_domain",
    "method_summary": "Parameterizes sampling by λ=(λ₁,λ₂,λ₃) controlling diversity threshold (ROUGE-L similarity), quality threshold (LM log-likelihood), and stopping confidence. Calibrates λ via LTT framework with binomial tail p-values and FWER-controlling multiple testing across a 3D grid, optimizing for set size and sampling efficiency. Extends to component-level guarantees by decomposing outputs into sentences and applying an inner conformal procedure with separate threshold γ. Proves P(∃y∈C: A(y)=1)≥1−ε with probability ≥1−δ over calibration draws.",
    "limitations_and_open_questions": "Guarantees are marginal, not conditional (coverage varies by topic — addressed by Cherian et al.). Requires reliable admission functions and labeled calibration data. Sampling budget k_max=20 limits achievable ε. Follow-up work (Mohri & Hashimoto) criticized returned sets as opaque and hard to interpret for end users.",
    "building_blocks": [
      "Sampling-based conformal prediction for intractable output spaces",
      "Stopping and rejection rules as conformal parameters",
      "Component-level conformal guarantees via inner procedure",
      "LTT-based multi-parameter calibration with Pareto testing"
    ],
    "relevance_to_seed": "Methodological ancestor — our abstention mechanism can be viewed as a rejection rule calibrated over RAG outputs, but we must handle the non-exchangeability introduced by adversarial retrieval rather than assuming i.i.d. sampling; the component-level guarantee concept maps to our per-claim factuality certificates."
  },
  {
    "title": "Language Models with Conformal Factuality Guarantees",
    "venue": "ICML 2024",
    "problem_identification": "No existing method provided formal statistical guarantees on open-ended LLM factuality — prior CP work for LMs was limited to token-level sets or multiple-choice reductions, none producing interpretable single outputs with coverage certificates.",
    "key_insight": "LLM factuality maps to uncertainty quantification via entailment sets: output y is correct iff the ground truth y* lies in E(y) = {y' : y' ⊨ y}, so conformal coverage over entailment sets directly translates to factuality guarantees through a back-off algorithm that progressively removes sub-claims.",
    "innovation_type": "new_formulation",
    "method_summary": "Decomposes LLM outputs into atomic sub-claims, scores each (via frequency/confidence), and applies split CP with a nested back-off function F_t that removes low-scoring claims to expand entailment sets. The calibration quantile q̂_α determines how many claims to retain. An entailment decomposability assumption (Assumption 5.1) ensures claim-level filtering preserves coverage. Achieves ~80% factuality on FActScore (up from 25%) while retaining ~50% of claims.",
    "limitations_and_open_questions": "Guarantees are marginal (averaged over calibration draws), not conditional per-input — follow-up work showed under-coverage for underrepresented topics and near-complete censorship at high factuality levels. Claims are evaluated independently, ignoring logical dependencies.",
    "building_blocks": [
      "Entailment-set formulation of factuality as CP coverage",
      "Sub-claim decomposition + scoring + filtering pipeline",
      "Back-off algorithm framework for nested conformal sets",
      "Frequency scoring as nonconformity measure"
    ],
    "relevance_to_seed": "Foundational paradigm our work extends — we must handle the case where retrieved documents (which ground the entailment sets) are adversarially poisoned, invalidating the exchangeability assumption this method relies on."
  },
  {
    "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
    "venue": "arXiv 2026",
    "problem_identification": "No prior work systematically studied whether conformal factuality guarantees survive when combined with RAG — existing metrics (empirical factuality) masked failures by treating empty outputs as trivially factual, hiding a critical factuality-informativeness tradeoff.",
    "key_insight": "Standard conformal factuality for RAG produces vacuous outputs at high confidence levels and its guarantees break under distribution shift and distractor injection — the problem is diagnosed but unsolved, creating a clear gap for robust alternatives.",
    "innovation_type": "analysis",
    "method_summary": "Introduces three metrics — Non-Empty Rate, Non-Vacuous Empirical Factuality, and Sufficient Correctness — that jointly capture both correctness and informativeness. Systematically evaluates the conformal factuality pipeline across FActScore/MATH/NQ, testing robustness to calibration-test domain mismatch and distractor documents in retrieval. Shows lightweight NLI-based entailment verifiers match LLM-based scorers at 100× fewer FLOPs.",
    "limitations_and_open_questions": "Purely diagnostic — proposes no solution to the robustness failures identified. Does not consider adversarial/poisoning attacks (only natural distribution shift and distractors). The sufficient correctness metric lacks formal definition tied to conformal guarantees.",
    "building_blocks": [
      "Non-Empty Rate and Non-Vacuous Factuality metrics",
      "Empirical evidence that CP guarantees break under RAG distribution shift",
      "Finding that lightweight NLI verifiers are competitive scorers",
      "Systematic failure mode taxonomy for conformal RAG pipelines"
    ],
    "relevance_to_seed": "Directly motivates our work — demonstrates the problem (CP breaks under RAG distribution shift) without providing a solution; our retrieval-aware score function and poisoning-robust abstention framework addresses exactly this diagnosed gap."
  },
  {
    "title": "Conformal Prediction as Bayesian Quadrature",
    "venue": "ICML 2025 (Outstanding Paper Award)",
    "problem_identification": "Standard CP provides marginal guarantees averaged over hypothetical calibration sets, but practitioners need data-conditional guarantees for their specific observed data — CRC violated its target risk in 21% (synthetic) to 45% (MS-COCO) of trials despite valid average guarantees.",
    "key_insight": "Bounding expected loss equals integrating the quantile function over [0,1], a Bayesian quadrature problem where the distribution-free Dirichlet property of quantile spacings provides the prior over evaluation sites without any distributional assumptions.",
    "innovation_type": "new_formulation",
    "method_summary": "Constructs a stochastic upper bound L⁺ = Σ Uᵢ·l₍ᵢ₎ where Uᵢ ~ Dir(1,...,1) are quantile spacings and l₍ᵢ₎ are ordered calibration losses. L⁺ stochastically dominates the posterior risk under any prior (Theorem 4.5), yielding a full posterior distribution over a provable loss upper bound. Recovers CRC as using only E[L⁺], explaining why CRC is loose — it discards all distributional information. Reduces violation rates from 45% to 5.4% on MS-COCO.",
    "limitations_and_open_questions": "Provides data-conditional (conditioned on calibration losses) not input-conditional guarantees — still averages over test inputs. Computational cost of sampling from the Dirichlet posterior for large calibration sets not fully characterized. Extension to non-exchangeable settings unexplored.",
    "building_blocks": [
      "Data-conditional CP guarantees via Bayesian quadrature",
      "L⁺ stochastic dominance bound as a richer alternative to CRC's point estimate",
      "Dirichlet quantile spacing property for distribution-free Bayesian inference",
      "Unification showing SCP and CRC as special cases"
    ],
    "relevance_to_seed": "Offers a strictly stronger CP framework we could adopt — replacing CRC-style point thresholds with full posterior bounds over risk could yield tighter abstention decisions; the data-conditional guarantees are especially valuable when calibration sets are small or heterogeneous."
  },
  {
    "title": "Conformal Prediction for Natural Language Processing: A Survey",
    "venue": "TACL 2024",
    "problem_identification": "No prior survey bridged conformal prediction theory to NLP applications — general CP surveys existed and NLP uncertainty surveys existed, but neither systematically mapped CP variants (Mondrian, non-exchangeable, risk-controlling) onto NLP task categories.",
    "key_insight": "CP's model-agnostic, distribution-free guarantees requiring only exchangeability and a small calibration set make it uniquely suited to NLP's black-box LLM era — but the autoregressive, high-cardinality nature of language generation creates fundamental tensions with CP's assumptions.",
    "innovation_type": "new_benchmark",
    "method_summary": "Organizes CP for NLP along two axes: CP variants (split, full, cross-conformal, Mondrian, weighted/non-exchangeable, conformal risk control, density-based, Venn-Abers) and NLP applications (classification/tagging, generation at sentence/token level, uncertainty-based evaluation, efficient inference). Identifies that non-exchangeability bounds require estimating TV distance between unknown distributions, a key open problem for autoregressive generation.",
    "limitations_and_open_questions": "Published mid-2024, so misses the conformal factuality line (Mohri & Hashimoto), RAG-specific CP work, and poisoning-robust CP developments. Does not cover adversarial robustness of CP guarantees at all. Token-level CP for autoregressive generation remains an open problem.",
    "building_blocks": [
      "Taxonomy of CP variants applicable to NLP",
      "Identification of exchangeability violations in autoregressive generation",
      "Catalog of nonconformity score designs for text",
      "Open challenge list including fairness, label variation, and conditional coverage"
    ],
    "relevance_to_seed": "Essential positioning reference — our work sits at the intersection of several categories (generation-level CP, non-exchangeable extensions, risk control) and addresses the survey's identified open challenge of CP under distribution shift, specifically adversarial shift from corpus poisoning."
  },
  {
    "title": "Conformal Selective Prediction with General Risk Control (SCoRE)",
    "venue": "arXiv 2026",
    "problem_identification": "Existing conformal selective prediction handled only binary risk (correct/incorrect), but high-stakes deployments require controlling continuous-valued risks (MSE, semantic error magnitude) — p-values are the wrong instrument for expectation-based continuous risk control.",
    "key_insight": "Selective prediction under continuous risk is hypothesis testing with unknown random weights, and risk-adjusted e-values (satisfying E[E·L] ≤ 1 rather than E[E] ≤ 1) are the natural currency — they accommodate expectation-based risk control through simple Markov-inequality thresholding.",
    "innovation_type": "new_technique",
    "method_summary": "Defines risk-adjusted e-values where the product E(n+j)·L(n+j) has expectation ≤ 1 under exchangeability. Thresholding at 1/α controls Marginal Deployment Risk; plugging into e-BH controls Selective Deployment Risk (continuous FDR analog). Proves Neyman-Pearson optimality: the optimal score is monotone in l(x)/r(x) (conditional risk-to-reward ratio). Extends to covariate shift via importance weighting. Demonstrated on drug discovery, clinical prediction, and LLM abstention.",
    "limitations_and_open_questions": "Requires bounded loss in [0,1] — unbounded risks need truncation or alternative constructions. The covariate shift extension requires density ratio estimation, which is hard in high dimensions. Power analysis under finite samples and comparison to concentration-based alternatives not fully explored.",
    "building_blocks": [
      "Risk-adjusted e-values for continuous risk control",
      "MDR and SDR as two distinct deployment risk objectives",
      "E-BH procedure for selective deployment with FDR-analog guarantees",
      "Finite-sample, distribution-free trust/abstain decisions under exchangeability"
    ],
    "relevance_to_seed": "Directly applicable to our abstention mechanism — SCoRE's e-value framework could replace or complement our conformal abstention layer, providing trust/abstain decisions with continuous risk control (e.g., semantic error magnitude) rather than binary correctness, and its covariate shift extension addresses part of the distribution shift from poisoning."
  },
  {
    "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Standard conformal prediction provides no coverage guarantees when adversaries poison training or calibration data—a threat entirely ignored by prior CP methods (RSCP, CAS) that only addressed test-time evasion. The authors identified this by observing that even a single poisoned calibration point can arbitrarily inflate or shrink prediction sets.",
    "key_insight": "Partitioning data into K subsets and aggregating via smoothed scores (training) and majority-vote prediction sets (calibration) ensures that an adversary corrupting fewer than K/2 partitions cannot break coverage guarantees—reducing poisoning robustness to a majority-resilience problem.",
    "innovation_type": "new_technique",
    "method_summary": "RPS partitions training data into K subsets, trains K independent classifiers, and defines a smoothed score as the proportion of classifiers agreeing on a class. For calibration poisoning, K prediction sets are constructed on disjoint calibration subsets and aggregated via majority vote—a class is included only if it appears in >K/2 individual sets. Formal certificates guarantee coverage under worst-case poisoning within the declared budget. Reviewers (8/8/6) praised the novel threat model and sound theory; criticisms centered on missing baselines, limited large-scale experiments, and the partition approach being known in differential privacy contexts.",
    "limitations_and_open_questions": "Partitioning reduces effective data per model, sacrificing utility for robustness. Critically, RPS addresses calibration-set poisoning (wrong labels in known data) but not test-time retrieval corruption (wrong documents injected at inference)—a fundamentally different threat model.",
    "building_blocks": [
      "Partition-and-vote mechanism for poisoning robustness",
      "Smoothed score functions over classifier ensembles",
      "Majority prediction set aggregation rule",
      "Formal coverage certificates under bounded poisoning budget"
    ],
    "relevance_to_seed": "Direct methodological ancestor: the partition-and-vote idea inspires our retrieval-agreement score construction, but the threat model mismatch (calibration poisoning vs. retrieval corruption) is precisely the gap our work addresses."
  },
  {
    "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
    "venue": "USENIX Security 2025",
    "problem_identification": "Prior RAG security research ignored the knowledge database as an attack surface; the authors identified that the retriever's reliance on embedding similarity creates an exploitable channel for injecting adversarial content into the generation context.",
    "key_insight": "A successful RAG poisoning attack decomposes into two independently optimizable conditions—retrieval similarity (the poisoned text must be retrieved) and generation influence (the LLM must produce the target answer)—enabling efficient crafting of minimal-injection attacks.",
    "innovation_type": "new_benchmark",
    "method_summary": "Each malicious text P = S ⊕ I concatenates a retrieval-optimized suffix S with a generation-optimized payload I. In black-box mode, S is simply the target question and I is LLM-generated text that produces the target answer. In white-box mode, S is optimized via HotFlip to maximize embedding similarity with the target query. Only 5 injected texts per question into million-document corpora achieve ~90% attack success across multiple LLMs and retrievers. Evaluated defenses (paraphrasing, perplexity filtering, deduplication) prove insufficient.",
    "limitations_and_open_questions": "Attacks are query-specific (separate poisoned texts per target question), limiting scalability to open-ended adversarial goals. Does not consider adaptive defenses like agreement-based filtering or certified robustness frameworks.",
    "building_blocks": [
      "RAG corpus poisoning threat model and attack formulation",
      "Retrieval+generation condition decomposition",
      "Black-box and white-box attack protocols for evaluation",
      "Benchmark datasets (NQ, HotpotQA, MS-MARCO) with poisoning"
    ],
    "relevance_to_seed": "Defines the primary attack protocol (PoisonedRAG attack) our framework must defend against; the retrieval+generation decomposition constrains attacker capability and informs our agreement-based score design."
  },
  {
    "title": "Robust Yet Efficient Conformal Prediction Sets",
    "venue": "ICML 2024",
    "problem_identification": "RSCP's mean-based bounds on randomized-smoothed conformity scores produce unnecessarily large prediction sets (often trivially including all classes), and it handles only evasion attacks on continuous data—not poisoning or discrete/graph inputs.",
    "key_insight": "Bounding the CDF of conformity score distributions (rather than just the mean) yields provably tighter worst-case bounds, because CDF-based analysis exploits the full distributional shape rather than collapsing to a single summary statistic.",
    "innovation_type": "new_technique",
    "method_summary": "CAS partitions the score space into bins and bounds the CDF at each boundary under adversarial perturbation, yielding tighter upper bounds on worst-case scores than RSCP's mean-based approach. For poisoning, calibration-time robustness is formulated as a MILP that finds the worst-case quantile threshold under bounded label/feature corruption. Sparse smoothing via XOR-based perturbations extends guarantees to discrete and graph-structured data. The calibration-time variant computes bounds only on calibration data, avoiding per-test-point verification overhead.",
    "limitations_and_open_questions": "Still requires randomized smoothing overhead and Monte Carlo sampling for score estimation. MILP-based poisoning bounds may not scale to very large calibration sets. Like RPS, addresses calibration/evasion poisoning—not test-time retrieval corruption.",
    "building_blocks": [
      "CDF-based conformity score bounds (tighter than mean-based)",
      "Joint evasion+poisoning robustness framework",
      "MILP for worst-case calibration quantile under poisoning",
      "Sparse smoothing for discrete/graph data"
    ],
    "relevance_to_seed": "CDF-based bounding could yield more efficient prediction sets in our setting than RPS-style majority voting; the calibration-time poisoning formulation is a template for our retrieval-corruption certificates, though the threat model must be adapted."
  },
  {
    "title": "Know Your Limits: A Survey of Abstention in Large Langua
... (truncated)

## Your task

Synthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.

Think about:
- What PATTERNS OF INNOVATION keep working in this field?
- What do reviewers consistently reward?
- Where are the real gaps (not assumed gaps)?
- What combinations haven't been tried?
- What mistakes should we avoid?

## Output format

Output a JSON object with these sections:
{
  "innovation_patterns": [
    {"pattern": "name", "description": "how it works", "examples": ["paper1", "paper2"], "success_rate": "high/medium/low"}
  ],
  "reviewer_preferences": [
    "What reviewers in this area consistently care about (based on evidence from paper analyses)"
  ],
  "field_gaps": [
    {"gap": "description of unsolved problem", "evidence": "which papers mention this limitation", "difficulty": "high/medium/low", "impact_if_solved": "high/medium/low"}
  ],
  "untried_combinations": [
    {"idea_sketch": "what could be combined", "from_papers": ["which papers inspire this"], "why_promising": "reason"}
  ],
  "method_building_blocks": [
    {"tool": "name", "what_it_does": "description", "used_by": ["papers"], "could_be_applied_to": "new application"}
  ],
  "common_pitfalls": [
    "Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)"
  ],
  "field_trajectory": "Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)",
  "meta_advice": "If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)"
}

Be specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.

IMPORTANT: You MUST end your response with the JSON object.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "850377a3-5357-4f21-acf1-05c05ace4a1a",
  "type": "user",
  "uuid": "f6a6258a-a3bf-493b-8f86-2be00c5df370",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:45:35.885Z_

```json
{
  "parentUuid": "f6a6258a-a3bf-493b-8f86-2be00c5df370",
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
  "uuid": "752d87ab-21bf-45f7-b903-1eea37e830ce",
  "timestamp": "2026-05-30T06:45:35.885Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:45:35.885Z_

```json
{
  "parentUuid": "752d87ab-21bf-45f7-b903-1eea37e830ce",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1e68e1a6-ad2a-4be2-b06b-d9b62a3ed9ef",
  "timestamp": "2026-05-30T06:45:35.885Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Safe, Robus…",
  "leafUuid": "1e68e1a6-ad2a-4be2-b06b-d9b62a3ed9ef",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:45:55.411Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for generating novel research ideas at the intersection of conformal prediction, RAG robustness, and abstention under adversarial conditions. This is targeted at AAAI 2026 SRRAI track.

Let me carefully analyze the papers and produce a comprehensive, evidence-based JSON output.

Let me organize my thinking:

**Innovation Patterns:**
1. Cross-domain transfer (TRAQ applied CP to RAG; conformal abstention from classification to LLMs)
2. New formulation/reframing (C-RAG reframes RAG risk as conformal risk; SCoRE reframes selective prediction as e-value testing; CLM reframes prediction sets as sampling+rejection)


3. Partition-and-aggregate strategies appear across multiple papers (RPS, RobustRAG, ReliabilityRAG) as a core robustness mechanism
4. Diagnosis-then-solution pattern where papers identify specific failure modes before proposing fixes
5. Attack simplification trends toward more targeted, minimal perturbations rather than broad corruption

**Reviewer Preferences:**
- Formal guarantees (certificates, coverage bounds)
- Novel threat models
- Comprehensive evaluation across datasets
- Addressing the right threat model (not just adapting existing ones)
- Practical compute budgets
- Clear gap identification

**Field Gaps:**
- No conformal abstention under adversarial conditions yet
- Limited work on certified robustness for RAG-LLM pipelines
- Few papers address the interaction between retrieval uncertainty and prediction uncertainty
- Conditional guarantees remain underexplored compared to marginal ones
- Continuous risk control mechanisms haven't been adapted for RAG systems

**Untried Combinations:**
- Combining e-value methods with retrieval agreement scoring
- Bayesian quadrature approaches to calibration poisoning with RAG abstention
- ReliabilityRAG's multi-instance selection paired with conformal coverage
- Group-conditional conformal prediction using retrieval quality as the conditioning variable
- CAS-style bounds applied to retrieval corruption scenarios

**Method Building Blocks:**
- Partition-and-vote mechanisms
- NLI-based contradiction detection
- Self-consistency scoring
- Conformal risk control
- E-values
- Bayesian quadrature calibration

**Common Pitfalls:**
- Assuming exchangeability when retrieval introduces dependencies
- Conflating marginal and conditional guarantees
- Producing vacuous outputs at high confidence levels
- Misaligning threat models with actual deployment scenarios
- Over-relying on LLM-based scoring without external validation

Now I'm structuring this as a comprehensive JSON configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e68e1a6-ad2a-4be2-b06b-d9b62a3ed9ef",
  "isSidechain": false,
  "requestId": "req_011CbYJWViYJPQou6ux4XY5G",
  "type": "assistant",
  "uuid": "ef442878-ff2d-448f-bcca-f81b4ed7d315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS13zzGB7eyqLu6RapfxZD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12902,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12902,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8035,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12902
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

_source line 9 · 2026-05-30T06:48:55.986Z_

I'll analyze the 20 papers systematically to produce the Field Guide. Let me first review the truncated paper to ensure I have all the key information, then synthesize.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Cross-domain mechanism transfer with threat-model adaptation",
      "description": "Take a well-established technique from one domain (e.g., conformal prediction from classification) and transfer it to a new domain (e.g., RAG), but the key to acceptance is identifying and resolving the specific assumption violations the new domain introduces rather than naively applying the technique. Papers that simply apply existing methods without adaptation get rejected; papers that diagnose the mismatch AND fix it get spotlights.",
      "examples": ["TRAQ (CP from classification → RAG, but only benign)", "RPS (partition-and-vote from DP/distributed systems → poisoning-robust CP)", "Conformal Abstention (self-consistency from heuristic → CP-calibrated abstention)", "SCoRE (e-values from sequential testing → selective prediction)"],
      "success_rate": "high"
    },
    {
      "pattern": "Partition-isolate-aggregate for adversarial robustness",
      "description": "Partition inputs/data into disjoint groups, process independently, then aggregate via majority vote or MIS to bound adversarial influence. This pattern appears across robust ML, certified RAG defenses, and poisoning-robust CP. Success comes from the clean mathematical reduction: adversary corrupts ≤k' of K groups → majority/MIS resilience bounds follow from combinatorics.",
      "examples": ["RPS (partition calibration data, majority-vote prediction sets)", "RobustRAG (partition passages into groups, keyword/decoding voting)", "ReliabilityRAG (NLI contradiction graph → MIS for document selection)"],
      "success_rate": "high"
    },
    {
      "pattern": "Diagnosis paper creates demand, solution paper fills it",
      "description": "A highly-cited analysis paper identifies and rigorously demonstrates a failure mode without proposing a fix. This creates a named, citable gap that a follow-up solution paper can directly address. The solution paper benefits from pre-existing reviewer awareness of the problem.",
      "examples": ["Chen et al. 2026 diagnoses CP-RAG failures → our proposed work fills this gap", "Cherian et al. shows marginal CP hides per-topic failures → motivates group-conditional methods", "Benchmarking paper shows all current defenses fail → motivates new defense paradigms"],
      "success_rate": "high"
    },
    {
      "pattern": "Strengthen the guarantee type (marginal → conditional → data-conditional)",
      "description": "Take an existing method that provides marginal (average-case) guarantees and upgrade it to conditional, group-conditional, or data-conditional guarantees. Each strengthening addresses a concrete failure mode visible in experiments. Reviewers reward this because marginal guarantees are increasingly recognized as insufficient.",
      "examples": ["Cherian et al. upgrades marginal factuality to group-conditional + level-adaptive", "Bayesian CP upgrades CRC's average guarantee to data-conditional posterior bounds, reducing violation from 45% to 5.4%", "SCoRE provides both MDR and SDR as distinct guarantee levels"],
      "success_rate": "high"
    },
    {
      "pattern": "Simplification that reveals fundamental structure",
      "description": "Reduce a complex attack or defense to its essential components, revealing that the problem is easier (or harder) than assumed. This shifts the conversation and redefines baselines.",
      "examples": ["CorruptRAG shows single-document poisoning achieves 95% ASR vs. PoisonedRAG's 5-doc 90% — simpler is better", "CRC reduces all conformal prediction to a 5-line algorithm over monotone losses", "PoisonedRAG decomposes attack into retrieval+generation conditions, enabling independent optimization"],
      "success_rate": "medium"
    },
    {
      "pattern": "Metric/evaluation innovation that redefines success",
      "description": "Introduce new evaluation criteria that expose hidden failures of existing methods. This is lower-risk innovation but creates lasting impact when the metrics become standard.",
      "examples": ["Chen et al. introduces Non-Empty Rate and Non-Vacuous Empirical Factuality, showing previous metrics masked vacuous outputs", "Cherian et al. shows marginal 90% factuality requires filtering 76% of claims — redefining the utility-factuality tradeoff"],
      "success_rate": "medium"
    }
  ],

  "reviewer_preferences": [
    "Formal, distribution-free certificates with finite-sample guarantees are strongly rewarded over empirical-only defenses. RPS received ICLR Spotlight (8/8/6) largely because it provided formal coverage certificates under poisoning, not just empirical robustness. RobustRAG (SaTML 2026) and ReliabilityRAG (NeurIPS 2025) both succeed by providing formal certificates. Reviewers in SRRAI explicitly value provable guarantees.",
    "Correct threat model specification matters more than technical sophistication. RPS reviewers praised the 'novel threat model' (calibration poisoning) as a primary contribution. Our work must clearly articulate WHY retrieval corruption is a different threat model from calibration poisoning and why existing tools (RPS, CAS) cannot be directly applied — reviewers who know Chen et al. (2026) will flag naive adaptations immediately.",
    "Comprehensive evaluation across standardized benchmarks with multiple attack protocols. The Benchmarking paper (2025) establishes NQ, HotpotQA, MS-MARCO as the standard triple, and PoisonedRAG + CorruptRAG as the standard attacks. Papers that evaluate on only one dataset or one attack face criticism — RPS reviewers noted 'limited large-scale experiments' as a weakness.",
    "Practical compute constraints and efficiency analysis. Reviewers consistently flag methods requiring excessive LLM calls (RobustRAG's m calls per query) or impractical calibration requirements. The ≤200 H100-hour budget is reasonable for the venue, but the paper should explicitly report compute costs and compare efficiency against baselines.",
    "Clear articulation of what guarantee is being provided (marginal vs. conditional vs. data-conditional) and honest acknowledgment of its limitations. Bayesian CP (ICML 2025 Outstanding Paper) succeeded partly by precisely characterizing what CRC guarantees and what it doesn't. Cherian et al. succeeded by showing marginal guarantees hide dangerous per-topic variation.",
    "Ablation studies that isolate the contribution of each component. Papers with multiple novel components (score function + aggregation + calibration) need to show each component's individual contribution. Reviewers penalize papers where the source of improvement is ambiguous.",
    "Addressing adaptive attackers, not just oblivious ones. ReliabilityRAG explicitly models attackers who know the defense mechanism. Our certificates must hold against adaptive adversaries who know we use retrieval-agreement-based conformal scores — this rules out security-through-obscurity defenses."
  ],

  "field_gaps": [
    {
      "gap": "No conformal abstention framework exists for RAG under adversarial corpus poisoning — the intersection of {conformal prediction, RAG, adversarial robustness, abstention} is completely empty",
      "evidence": "TRAQ and C-RAG provide conformal guarantees for RAG but assume benign retrieval. RPS provides poisoning-robust CP but for classifiers with calibration poisoning, not RAG with retrieval corruption. RobustRAG and ReliabilityRAG provide certified RAG defenses but no conformal/abstention mechanism. Chen et al. (2026) diagnoses CP failures under RAG distribution shift but proposes no solution.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Threat model mismatch: existing poisoning-robust CP (RPS, CAS) assumes calibration-set poisoning (wrong labels in known data) while RAG poisoning corrupts test-time retrieval (wrong documents injected at inference) — no work bridges this mismatch",
      "evidence": "RPS explicitly addresses calibration poisoning; CAS formulates calibration-time robustness as MILP under bounded label/feature corruption. Both papers' limitations sections note they don't address test-time corruption. The retrieval corruption threat model from RobustRAG/ReliabilityRAG is fundamentally different: the adversary controls document content at test time, not labels during calibration.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No method provides continuous risk control (beyond binary correct/incorrect) for RAG abstention — existing work uses binary coverage but real deployments need control over semantic error magnitude, partial correctness, or per-claim factuality rates",
      "evidence": "SCoRE introduces risk-adjusted e-values for continuous risk control but only for classification/regression, not RAG. Conformal Factuality uses binary entailment sets. TRAQ uses binary coverage. The gap is explicitly noted in the conformal NLP survey as an open challenge.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Group-conditional or input-conditional conformal guarantees for RAG are unexplored — all existing RAG CP methods provide only marginal guarantees that hide per-topic/per-query-type variation",
      "evidence": "Cherian et al. shows marginal coverage drops from ~95% to ~70% for low-popularity topics in closed-book LLMs. Chen et al. shows RAG conformal factuality produces vacuous outputs at high confidence for hard queries. No RAG CP method provides group-conditional or level-adaptive guarantees.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Defense evaluation against single-document poisoning (CorruptRAG) is largely missing — most defenses are tested against multi-document PoisonedRAG but single-doc attacks are harder to detect via agreement signals and more realistic",
      "evidence": "CorruptRAG (2026) achieves 95% ASR with a single document but evaluations of RobustRAG and ReliabilityRAG focus on multi-document poisoning where agreement-based defenses have natural advantages. The Benchmarking paper includes CorruptRAG but doesn't test certified defenses against it.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No data-conditional (as opposed to marginal) conformal guarantees exist for any NLP/RAG application — Bayesian CP's posterior bounds are only demonstrated on vision tasks",
      "evidence": "Bayesian CP (ICML 2025 Outstanding Paper) shows CRC violates its target in up to 45% of trials and proposes L⁺ bounds that reduce violations to 5.4%, but only evaluates on MS-COCO segmentation and medical imaging. Extension to NLP and especially RAG is completely unexplored.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Compositional guarantees across retriever + generator pipeline under adversarial conditions remain intractable — all existing work either provides guarantees for one component or uses union bounds that are too loose",
      "evidence": "TRAQ uses union bound α_Ret + α_LLM = α which doubles the required calibration data. C-RAG provides compositional theory but only for single-layer transformers under benign conditions. The seed direction correctly identifies this as RQ1 territory to avoid.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "Bayesian quadrature CP (data-conditional posterior bounds) + retrieval-agreement-conditioned scores for RAG abstention — replace CRC's point threshold with full posterior risk bounds, conditioned on retrieval agreement groups, to get tight data-conditional coverage under poisoning",
      "from_papers": ["Bayesian CP (ICML 2025)", "TRAQ", "RPS"],
      "why_promising": "Bayesian CP reduced violation rates from 45% to 5.4% in vision; RAG calibration sets are typically small (hundreds to low thousands), exactly where data-conditional bounds matter most. The L⁺ bound's Dirichlet construction is compatible with partition-based score aggregation. This would be the first data-conditional CP for any NLP application."
    },
    {
      "idea_sketch": "SCoRE's risk-adjusted e-values + ReliabilityRAG's NLI contradiction graph — use NLI-derived agreement structure to define nonconformity scores, then apply e-value thresholding for continuous risk control (semantic error magnitude, not just binary correctness) with formal abstention certificates",
      "from_papers": ["SCoRE (2026)", "ReliabilityRAG", "Conformal Abstention (NeurIPS 2024)"],
      "why_promising": "SCoRE provides the only existing framework for continuous risk control in selective prediction, and ReliabilityRAG's NLI graph captures exactly the agreement structure needed for retrieval-aware scores. The combination gives tunable risk-abstention tradeoffs with certificates — something neither method provides alone. E-values also compose naturally across groups (multiply rather than Bonferroni-correct)."
    },
    {
      "idea_sketch": "Cherian et al.'s group-conditional CP with level-adaptive α(X) + retrieval quality signals as conditioning variables — vary the abstention threshold per-query based on retrieval agreement level, retriever confidence, and document diversity, with formal group-conditional coverage guarantees",
      "from_papers": ["Cherian et al. (NeurIPS 2024)", "TRAQ", "Chen et al. (2026)"],
      "why_promising": "Chen et al. shows uniform thresholds produce vacuous outputs for hard queries and over-conservative results for easy ones. Level-adaptive calibration directly addresses this by learning per-query α(X) from retrieval features. The retrieval agreement structure provides natural conditioning variables that are computable without additional LLM calls."
    },
    {
      "idea_sketch": "RobustRAG's isolate-then-aggregate architecture + conformal risk control calibration — use RobustRAG's passage grouping as the isolation mechanism but replace its keyword/decoding voting with conformal-calibrated abstention decisions per group, aggregating via majority over group-level conformal sets",
      "from_papers": ["RobustRAG (SaTML 2026)", "CRC (ICLR 2024)", "RPS (ICLR 2025)"],
      "why_promising": "RobustRAG already provides the computational infrastructure for isolation but lacks principled abstention (it outputs τ=0 without fallback). Conformal risk control's monotone-loss framework is directly applicable to the group-level aggregation step. This combination gives formal coverage certificates on top of certified robustness — defense-in-depth with both safety layers having formal guarantees."
    },
    {
      "idea_sketch": "CAS's CDF-based conformity score bounds + retrieval-corruption threat model — adapt CAS's distributional (not just mean-based) score bounding to handle worst-case retrieval corruption, yielding tighter prediction sets than RPS-style majority voting under the same poisoning budget",
      "from_papers": ["CAS (ICML 2024)", "RobustRAG", "PoisonedRAG"],
      "why_promising": "CAS provably tightens bounds vs. RSCP/RPS by exploiting the full CDF rather than just means. In the retrieval setting, the score distribution under poisoning has specific structure (poisoned docs cluster in embedding space, producing identifiable score patterns) that CDF-based bounds can exploit. This could yield significantly smaller abstention rates for the same coverage level."
    },
    {
      "idea_sketch": "CorruptRAG's single-document threat model + conformal factuality's sub-claim decomposition — decompose RAG outputs into atomic claims, score each claim's consistency with individual retrieved passages, and apply per-claim conformal filtering where single-doc poisoning can only corrupt claims grounded in the poisoned passage",
      "from_papers": ["CorruptRAG (2026)", "Conformal Factuality (ICML 2024)", "Chen et al. (2026)"],
      "why_promising": "Single-doc poisoning is the hardest case for agreement-based defenses but the easiest for per-claim analysis: only claims grounded in the single poisoned doc are affected. Sub-claim decomposition localizes the damage, and conformal filtering removes affected claims with guarantees. This addresses the key weakness of agreement-based methods against CorruptRAG."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "Partition-and-vote aggregation",
      "what_it_does": "Partitions data/documents into K disjoint groups, processes independently, aggregates via majority vote. Bounds adversarial influence to corrupted_groups/total_groups ratio. Formal certificates follow from combinatorics.",
      "used_by": ["RPS (calibration partitioning)", "RobustRAG (passage grouping)", "ReliabilityRAG (sampling rounds)"],
      "could_be_applied_to": "Retrieval-agreement-conditioned conformal scores: partition retrieved passages, compute per-group nonconformity scores, aggregate via majority over group-level conformal sets to get poisoning-robust coverage"
    },
    {
      "tool": "NLI-based contradiction graph + MIS",
      "what_it_does": "Constructs a graph where nodes are documents/responses and edges indicate NLI-detected contradiction. Maximum Independent Set finds the largest non-contradicting subset, naturally excluding adversarial documents that contradict the benign majority.",
      "used_by": ["ReliabilityRAG"],
      "could_be_applied_to": "Defining retrieval-agreement nonconformity scores: the MIS size relative to total documents is a natural agreement signal; documents excluded from MIS are candidate adversarial passages; the gap between MIS size and total docs bounds poisoning severity"
    },
    {
      "tool": "Conformal risk control (CRC) with monotone losses",
      "what_it_does": "5-line algorithm that finds threshold λ̂ controlling E[L(λ̂)] ≤ α for any monotone, bounded loss function. Extends to distribution shift via TV distance bounds, multiple simultaneous risks, and adversarial worst-case.",
      "used_by": ["CRC (ICLR 2024)", "Conformal Abstention (NeurIPS 2024)", "SCoRE"],
      "could_be_applied_to": "Calibrating the abstention threshold for RAG under poisoning: the abstention loss (1 if incorrect AND not abstained, 0 otherwise) is monotone in the abstention threshold, and the distribution shift extension provides a template for bounding coverage degradation under bounded corpus poisoning"
    },
    {
      "tool": "Self-consistency scoring via LLM sampling",
      "what_it_does": "Samples k responses per query, measures pairwise agreement (ROUGE, NLI, LLM-as-judge), and uses agreement level as a nonconformity/confidence score. Higher agreement → higher confidence in the answer.",
      "used_by": ["Conformal Abstention (NeurIPS 2024)", "TRAQ (generator NCM)", "Conformal Language Modeling"],
      "could_be_applied_to": "Retrieval-conditioned self-consistency: compute self-consistency separately for each passage group's responses, then aggregate. Poisoned passages produce inconsistent responses across groups, yielding low group-conditional consistency scores that trigger abstention"
    },
    {
      "tool": "Risk-adjusted e-values",
      "what_it_does": "Defines e-values E where E[E·L] ≤ 1 (not E[E] ≤ 1), enabling continuous risk control via Markov thresholding. Composes multiplicatively across independent tests. Extends to covariate shift via importance weighting.",
      "used_by": ["SCoRE (2026)"],
      "could_be_applied_to": "Per-group e-values in the partition-and-aggregate framework: compute e-values for each passage group independently, multiply across groups for a combined statistic. Multiplicative composition is more powerful than Bonferroni correction and naturally handles the multi-group structure"
    },
    {
      "tool": "Bayesian quadrature L⁺ bounds",
      "what_it_does": "Constructs a stochastic upper bound on risk using Dirichlet quantile spacings, providing a full posterior distribution over risk rather than a point estimate. Recovers CRC as a special case (using only E[L⁺]) but is strictly tighter.",
      "used_by": ["Bayesian CP (ICML 2025)"],
      "could_be_applied_to": "Tighter abstention thresholds for RAG: when calibration sets are small (typical in RAG evaluation), the posterior bound is substantially tighter than CRC, reducing unnecessary abstentions while maintaining formal guarantees"
    },
    {
      "tool": "Sub-claim decomposition and filtering",
      "what_it_does": "Decomposes LLM outputs into atomic claims, scores each independently, and removes low-confidence claims to expand the entailment set. The back-off algorithm progressively removes claims until coverage is met.",
      "used_by": ["Conformal Factuality (ICML 2024)", "Chen et al. (2026)"],
      "could_be_applied_to": "Partial abstention for RAG: instead of binary abstain/answer, remove specific claims that are unsupported by the benign retrieval majority while keeping well-supported claims — this preserves informativeness while providing per-claim certificates"
    },
    {
      "tool": "Group-conditional calibration with level-adaptive α(X)",
      "what_it_does": "Learns a function α(X) that varies the confidence level per-input, calibrated via two-fold splitting to provide group-conditional (not just marginal) coverage. Conditional boosting optimizes scores through quantile regression LP.",
      "used_by": ["Cherian et al. (NeurIPS 2024)"],
      "could_be_applied_to": "Retrieval-quality-adaptive abstention: queries with high retrieval agreement get tighter (less conservative) thresholds while queries with suspicious retrieval patterns get stricter thresholds — formalizing the intuition that abstention should depend on retrieval quality"
    }
  ],

  "common_pitfalls": [
    "Applying RPS or CAS directly to RAG without recognizing the threat model mismatch. RPS assumes calibration poisoning (adversary corrupts training/calibration labels); RAG poisoning corrupts test-time retrieval (adversary injects documents at inference). The partition-and-vote mechanism from RPS can inspire our approach, but the formal guarantees don't transfer because the adversary operates at a different point in the pipeline. Reviewers familiar with both literatures will immediately flag this — Chen et al. (2026) has already sensitized the community to naive CP-RAG transfers.",
    "Claiming marginal coverage guarantees without acknowledging per-query variation. Cherian et al. showed coverage can drop 25+ percentage points for underrepresented topics, and Chen et al. showed RAG conformal factuality produces vacuous outputs for hard queries. Any paper claiming only marginal E[coverage] ≥ 1-α without group-conditional analysis will face immediate scrutiny at AAAI 2026.",
    "Using LLM-based nonconformity scores (log-probs, LLM-as-judge similarity) that are themselves vulnerable to the adversarial manipulation the framework aims to defend against. If the adversary can craft passages that fool both the retriever AND the LLM-based scorer, the conformal guarantee is formally valid but practically meaningless because the score function is corrupted. Use embedding-geometric or NLI-based scores that are more robust to adversarial text.",
    "Over-engineering the defense for multi-document poisoning while ignoring single-document attacks. CorruptRAG shows 95% ASR with a single poisoned document, and agreement-based defenses inherently struggle when only 1 of k passages is adversarial. A defense that only works for k'≥2 poisoned passages is incomplete and reviewers will flag CorruptRAG as the critical test case.",
    "Ignoring computational overhead of isolation-based defenses. RobustRAG requires m independent LLM calls per query, which reviewers noted as a practical concern. Any conformal method built on top of isolation-then-aggregate inherits this cost. The paper must report wall-clock time and total FLOPs alongside accuracy/coverage metrics, and the ≤200 H100-hour budget constrains experiment scale.",
    "Confusing certified robustness (RobustRAG/ReliabilityRAG's τ>0 guarantee) with conformal coverage (TRAQ/CRC's Pr(correct)≥1-α guarantee). These are complementary but distinct: certified robustness means the output is unchanged under bounded perturbation, while conformal coverage means the true answer is in the prediction set with high probability. A paper must be precise about which guarantee it provides and not conflate the two.",
    "Reporting only attack success rate (ASR) without reporting abstention rate. A defense that achieves 0% ASR by abstaining on 90% of queries is useless. Chen et al. explicitly introduced Non-Empty Rate and Non-Vacuous Factuality to catch exactly this failure mode. Our evaluation must report the coverage-abstention Pareto frontier, not just a single operating point.",
    "Assuming the entailment decomposability property (Conformal Factuality's Assumption 5.1) holds under adversarial conditions. Poisoned passages may introduce logically entangled misinformation where removing individual sub-claims doesn't preserve overall semantic validity. This assumption needs empirical validation or relaxation in the adversarial setting.",
    "Neglecting to evaluate against adaptive attackers who know the defense mechanism. ReliabilityRAG's certificates hold against adaptive adversaries with full system knowledge. Any defense that is only evaluated against oblivious attackers (PoisonedRAG with default parameters) will be criticized. The certification must be stated and proven against the strongest applicable threat model."
  ],

  "field_trajectory": "The field is converging on a three-layer defense stack for trustworthy RAG: (1) certified document selection/filtering (RobustRAG, ReliabilityRAG), (2) conformal coverage/abstention guarantees (our proposed contribution), and (3) per-claim factuality certificates (Conformal Factuality, sub-claim decomposition). Layer 1 is maturing rapidly with two strong methods published in 2025-2026. Layer 3 exists for benign settings but breaks under adversarial conditions. Layer 2 — the abstention layer with formal guarantees under adversarial retrieval — is completely empty, representing the highest-value contribution opportunity in 2026.\n\nThree macro-directions dominate the next 12-18 months. First, the move from marginal to conditional/data-conditional guarantees in conformal NLP, driven by Cherian et al.'s and Bayesian CP's demonstrations that marginal guarantees are dangerously loose. Papers that provide group-conditional or level-adaptive guarantees will dominate over marginal-only contributions. Second, the unification of certified robustness and conformal prediction — currently siloed into separate communities (RobustRAG/ReliabilityRAG vs. TRAQ/CRC), the convergence point is methods that provide both certified robustness AND statistical coverage guarantees simultaneously. Third, the extension to realistic threat models: single-document attacks (CorruptRAG), adaptive adversaries, and compositional pipelines (multi-hop RAG, agentic RAG). The Benchmarking paper (2025) showed that architectural complexity alone doesn't help — principled defenses must extend to these settings.\n\nA secondary but important trend is efficiency: the field is moving from brute-force isolation (m LLM calls) toward efficient approximations. ReliabilityRAG's weighted sampling and lightweight NLI verifiers (Chen et al. showed NLI matches LLM-as-judge at 100× fewer FLOPs) signal that practical methods that maintain guarantees while reducing compute will be increasingly valued.",

  "meta_advice": "For AAAI 2026 SRRAI, the winning formula is: (1) a crisp threat model that clearly distinguishes your setting from both benign CP-for-RAG (TRAQ, C-RAG) and calibration poisoning CP (RPS, CAS) — spend a full subsection on why direct adaptation fails, citing Chen et al. (2026) as the motivation; (2) a score function design that exploits retrieval-specific structure (passage agreement, embedding geometry) rather than generic self-consistency — this is your technical novelty and must be accompanied by both formal analysis and ablations showing it outperforms naive baselines like 'abstain when passages disagree'; (3) formal certificates stated clearly with explicit assumptions — state the poisoning budget k', the exchangeability condition being restored, and prove coverage under worst-case attack within that budget; (4) comprehensive evaluation on the standard triple (NQ, HotpotQA, MS-MARCO) with both PoisonedRAG and CorruptRAG attacks, comparing against RobustRAG and ReliabilityRAG on their own metrics PLUS your coverage-abstention tradeoff metrics.\n\nConcretely, the strongest version of this paper combines the partition-and-aggregate architecture from RobustRAG (which gives isolation), NLI-based agreement signals from ReliabilityRAG (which gives retrieval-aware nonconformity scores), and the conformal risk control framework from CRC (which gives formal calibration). The theoretical contribution is proving that retrieval-agreement-conditioned scores restore a form of exchangeability sufficient for CRC guarantees under bounded poisoning — essentially showing that within agreement groups, the nonconformity scores of benign passages satisfy the conditions of Theorem 1 from CRC even when adversarial passages violate global exchangeability. Present the coverage-abstention Pareto frontier as your primary result, showing that your method achieves higher coverage at every abstention rate than baselines. Include the single-document CorruptRAG evaluation prominently — this is the hardest case and where you can demonstrate the most differentiation. Budget roughly 80 H100-hours for main experiments, 60 for ablations, and 60 for extended evaluations and rebuttal buffer. Start the theoretical framework and proof sketches immediately (June 2026), run experiments July-early August, and target a complete draft by August 1 to allow revision time before the deadline."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef442878-ff2d-448f-bcca-f81b4ed7d315",
  "isSidechain": false,
  "requestId": "req_011CbYJWViYJPQou6ux4XY5G",
  "type": "assistant",
  "uuid": "45c633a2-e1b4-40ec-a22a-4a79b718fe42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HS13zzGB7eyqLu6RapfxZD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12902,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12902,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8035,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12902
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Safe, Robus…",
  "leafUuid": "45c633a2-e1b4-40ec-a22a-4a79b718fe42",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Safe, Robus…",
  "leafUuid": "45c633a2-e1b4-40ec-a22a-4a79b718fe42",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "e72027ce-ed45-4523-93e6-5df64f5c12e2"
}
```

---
