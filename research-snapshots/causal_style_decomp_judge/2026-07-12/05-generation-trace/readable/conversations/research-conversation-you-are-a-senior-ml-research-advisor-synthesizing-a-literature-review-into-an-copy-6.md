# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/0ec1a38a-9c06-4dc5-849a-f7a810dfed74.jsonl`
- **Structured JSON:** [`9035f68f197c85ef84cf.json`](../../sessions/90/9035f68f197c85ef84cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:47:14.659Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:47:14.659Z",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models\",\n    \"venue\": \"USENIX Security 2025\",\n    \"problem_identification\": \"No prior work systematically studied whether injecting a small number of adversarial texts into a million-scale RAG knowledge base could reliably steer LLM outputs. The attack surface of the retrieval corpus itself was unexamined despite real-world RAG deployments drawing from open/semi-open corpora.\",\n    \"key_insight\": \"Corpus poisoning decomposes into two independently solvable sub-problems—retrievability (poisoned text must rank in top-k) and persuasion (retrieved text must convince the LLM)—and satisfying both simultaneously requires only ~5 injected passages per target question even in million-scale databases.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Formalizes RAG poisoning as a constrained optimization over retrievability and persuasion. Black-box variant uses an LLM to generate topically plausible passages containing the target answer (naturally achieving retrieval similarity). White-box variant uses HotFlip-based gradient optimization against the retriever's embedding model to maximize query-passage similarity while embedding attacker-chosen content. Evaluates on NQ, HotpotQA, MS-MARCO with Contriever retrieval across GPT-4, PaLM 2, LLaMA-2, and Vicuna.\",\n    \"limitations_and_open_questions\": \"Targets individual questions rather than broad topic corruption; all tested defenses (paraphrasing, perplexity filtering, deduplication, knowledge expansion) provide only partial mitigation. No evaluation against adaptive defenses or retrieval-level embedding-space anomaly detection.\",\n    \"building_blocks\": [\n      \"Retrievability+persuasion decomposition framework\",\n      \"HotFlip adaptation for dense retriever manipulation\",\n      \"LLM-as-attacker passage generation\",\n      \"PoisonedRAG attack protocol (NQ/HotpotQA/MS-MARCO + Contriever)\",\n      \"Open-source evaluation codebase\"\n    ],\n    \"relevance_to_seed\": \"Defines the exact threat model our conformal abstention framework must defend against; its attack protocol (5 injected passages, 90%+ ASR) is the required evaluation benchmark, and the finding that surface-level defenses fail motivates principled statistical approaches like CP.\"\n  },\n  {\n    \"title\": \"CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"Standard conformal factuality guarantees (Mohri & Hashimoto 2024) require exchangeability between calibration and test data, which breaks under production distribution shift (trending topics, demographic changes). The authors showed empirically that standard CP drops well below target factuality under shift and that online CP methods requiring test-time labels are inapplicable.\",\n    \"key_insight\": \"Weighted conformal prediction can be made practical for LLM factuality by solving density ratio estimation online via an ensemble of experts with geometrically-spaced lifetimes, sidestepping both the exchangeability requirement and the need for test-time ground truth.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Decomposes LLM responses into atomic claims scored for factuality. Uses importance-weighted CP where calibration scores are reweighted by density ratios D_t(Z)/D_0(Z). Estimates these ratios online via an ensemble of logistic regression experts updated with Online Newton Step, with geometrically increasing lifetimes (2^0, 2^1, ...) to track non-stationary shift. Provides a bound: |1/T·Σerr_t − α| = Õ(max{T^{−2/3}V_T^{2/3}, T^{−1/2}} + n^{−1/2}).\",\n    \"limitations_and_open_questions\": \"Requires 50-150 timestep burn-in before guarantees stabilize—a vulnerability window. Assumes covariate shift (P(Y|X) unchanged), which fails under adversarial poisoning where injected documents change the conditional factuality. Bounded density ratio assumption may fail when poisoned documents have no calibration-time analogue.\",\n    \"building_blocks\": [\n      \"Online density ratio estimation with expert ensembles\",\n      \"Weighted conformal prediction framework (Tibshirani et al. 2019)\",\n      \"Atomic claim decomposition + FActScore-style evaluation\",\n      \"WildChat+ dataset with natural covariate shift\",\n      \"Online Newton Step for expert updates\"\n    ],\n    \"relevance_to_seed\": \"Most directly relevant theoretical tool: its weighted CP machinery for handling distribution shift could be adapted for corpus poisoning, but the covariate-shift-only assumption (P(Y|X) unchanged) must be extended to handle the concept shift that adversarial document injection induces.\"\n  },\n  {\n    \"title\": \"Merging Uncertainty Sets via Majority Vote\",\n    \"venue\": \"arXiv 2024\",\n    \"problem_identification\": \"Given K arbitrarily dependent uncertainty sets (from different models, conformal splits, or estimators), there was no principled black-box merging procedure with finite-sample coverage guarantees. Practitioners routinely produce multiple valid prediction sets but lacked a general-purpose aggregation method.\",\n    \"key_insight\": \"Majority vote—include a point in the merged set iff it appears in ≥⌈K/2⌉ input sets—yields coverage that improves exponentially in K via a binomial tail bound, requiring no assumptions about dependence structure or construction method of the individual sets.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Partition data into K groups, construct valid uncertainty sets C_k on each, merge via majority vote: θ ∈ C_merge iff |{k: θ ∈ C_k}| ≥ ⌈K/2⌉. Coverage guarantee: P(θ* ∈ C_merge) ≥ 1 − B(K, ⌈K/2⌉, α) where B is the binomial CDF. Extensions include weighted voting (w_k-weighted inclusion threshold), randomized thresholds for tighter sets, and sequential/streaming merging. Unifies median-of-means, HulC, and multi-split conformal as special cases.\",\n    \"limitations_and_open_questions\": \"Merged sets can be larger than individual sets for small K (conservatism cost). Whether the binomial bound is information-theoretically tight is open. No discussion of computational cost when individual sets have complex geometry. Assumes each input set has valid marginal coverage—fails if the adversary corrupts calibration itself.\",\n    \"building_blocks\": [\n      \"Partition-and-vote paradigm for ensemble UQ\",\n      \"Binomial tail coverage bound\",\n      \"Weighted majority vote with trust-weighted aggregation\",\n      \"Randomized threshold technique for set size reduction\",\n      \"Connection to median-of-means and HulC\"\n    ],\n    \"relevance_to_seed\": \"Directly provides the theoretical template for our retrieval-agreement groups: partition retrieved passages into K groups, form per-group conformal sets, merge via majority vote—yielding Byzantine fault tolerance where coverage holds as long as fewer than half the groups are poisoned.\"\n  },\n  {\n    \"title\": \"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Existing RAG benchmarks focus exclusively on correctness metrics (accuracy, F1) while ignoring how retrieval affects uncertainty and reliability. No prior work systematically evaluated whether conformal prediction methods maintain valid coverage across diverse RAG architectures and domains, especially under retrieval noise.\",\n    \"key_insight\": \"By reformulating open-ended QA into multiple-choice format via an iterative NLI-based distractor generation pipeline (achieving 96-100% validity), conformal prediction methods (LAC, APS) become directly applicable to RAG outputs—revealing that the accuracy-uncertainty correlation breaks specifically when retrieval introduces noise.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Converts open-ended QA to MCQA using Gemini-generated distractors filtered by NLI for factual incorrectness, contextual plausibility, and semantic type matching. Evaluates 8 RAG methods (Naive, Fusion, HyDE, RAT, FiD, Self-RAG, RAPTOR, REPLUG) across 8 datasets in 5 domains using LAC and APS conformal methods on Llama-3.1-8B. Measures both accuracy and prediction set sizes as complementary reliability metrics.\",\n    \"limitations_and_open_questions\": \"MCQA conversion introduces approximation vs. open-ended generation. Evaluated only on Llama-3.1-8B; generalization unclear. Does not study adversarial/intentional poisoning—only natural retrieval noise. Open question: how findings transfer to free-form generation without MCQA scaffolding.\",\n    \"building_blocks\": [\n      \"MCQA conversion pipeline with NLI-based distractor refinement\",\n      \"LAC and APS conformal prediction applied to LLM logits\",\n      \"8-dataset evaluation suite across 5 domains\",\n      \"Accuracy-uncertainty correlation analysis framework\",\n      \"Parametric vs. retrieval knowledge dependency analysis\"\n    ],\n    \"relevance_to_seed\": \"Provides evaluation infrastructure and the key empirical finding that retrieval noise breaks CP coverage—directly motivating our work. The MCQA+CP pipeline is reusable for evaluating conformal abstention under adversarial poisoning, and URAG's finding that confident errors are amplified by retrieval cues predicts exactly the failure mode poisoning attacks exploit.\"\n  },\n  {\n    \"title\": \"RAGDefender: Rescuing the Unpoisoned — Efficient Defense against Knowledge Corruption Attacks on RAG Systems\",\n    \"venue\": \"ACSAC 2025\",\n    \"problem_identification\": \"Existing RAG poisoning defenses (RobustRAG, Discern-and-Answer) require multiple LLM inference passes or fine-tuning, making them prohibitively expensive (14-42 GB GPU memory, $1-59 per iteration). No efficient, training-free, model-agnostic defense existed for post-retrieval poisoning detection.\",\n    \"key_insight\": \"Adversarial passages crafted to push the LLM toward the same incorrect answer form semantically dense clusters in embedding space—a detectable signal exploitable with lightweight ML (cosine similarity, hierarchical clustering, TF-IDF) without any LLM involvement in the defense itself.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"Two-stage pipeline: Stage 1 estimates the number of adversarial passages N_adv using hierarchical agglomerative clustering on passage embeddings plus TF-IDF term co-occurrence (single-hop) or mean/median cosine similarity concentration (multi-hop). Stage 2 identifies specific adversarial passages by computing pairwise cosine similarities, scoring each passage by weighted frequency in top-similar pairs (f_i = Σ|sim|^p), and removing the top-N_adv ranked passages. Achieves 0.02 ASR (vs. 0.89 undefended, 0.69 RobustRAG) at 12x speed and zero GPU cost.\",\n    \"limitations_and_open_questions\": \"No formal theoretical guarantees that poisoned passages always cluster—purely empirical. Sophisticated adaptive attacks deliberately diversifying adversarial embeddings (anti-clustering) could evade detection, though tested adaptive attacks still yield only 0.13 ASR. Untested beyond k=10 retrieval set sizes.\",\n    \"building_blocks\": [\n      \"Embedding-space clustering for poisoned passage detection\",\n      \"Pairwise cosine similarity frequency scoring\",\n      \"TF-IDF co-occurrence for adversarial set size estimation\",\n      \"Hierarchical agglomerative clustering\",\n      \"PoisonedRAG evaluation protocol with Contriever/DPR/ANCE\"\n    ],\n    \"relevance_to_seed\": \"Provides a key comparison baseline and a potential nonconformity score ingredient: the clustering signal (pairwise similarity concentration among retrieved passages) could be incorporated into retrieval-aware conformal scores, combining RAGDefender's efficient detection with CP's formal coverage guarantees—addressing the paper's acknowledged lack of theoretical certificates.\"\n  },\n  {\n    \"title\": \"CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation\",\n    \"venue\": \"ACM SACMAT 2026\",\n    \"problem_identification\": \"Prior RAG poisoning attacks (PoisonedRAG) require injecting multiple (≥5) poisoned documents per query to outnumber benign retrievals, which is costly, detectable, and unrealistic in practice. The authors showed empirically that most queries retrieve fewer than 3 relevant docs in top-5, making multi-document poisoning assumptions fragile.\",\n    \"key_insight\": \"A single poisoned document can dominate RAG output if it embeds the query verbatim (guaranteeing top retrieval rank) and uses adversarial framing that exploits LLMs' bias toward 'recent' information to override benign context.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"The poisoned text is split into a retrieval component (query copied verbatim for maximal similarity) and a manipulation component containing an adversarial statement ('outdated corpus states [correct answer]') plus a target statement ('latest data confirms [desired answer]'). Two variants exist: CRAG-AS (template-based, zero-cost) and CRAG-AK (LLM-refined knowledge-like text for cross-query generalization at $0.0001/query). The attack is fully black-box — no access to retriever or LLM parameters.\",\n    \"limitations_and_open_questions\": \"Defense evaluation is limited to LLM-based detection (0-10% TPR), but does not test against certified defenses like RobustRAG/ReliabilityRAG's isolate-then-aggregate strategies. Single-doc assumption may fail when aggregation defenses process passages independently.\",\n    \"building_blocks\": [\n      \"Single-document poisoning threat model\",\n      \"Query-verbatim retrieval exploitation\",\n      \"Adversarial framing templates for LLM manipulation\",\n      \"CRAG-AK knowledge-style text generation\"\n    ],\n    \"relevance_to_seed\": \"Defines a more practical and stealthy attack protocol than PoisonedRAG for evaluating our conformal abstention framework — our method must handle the case where even a single poisoned document in top-k can corrupt outputs.\"\n  },\n  {\n    \"title\": \"Data Poisoning Attacks against Conformal Prediction\",\n    \"venue\": \"ICML 2024\",\n    \"problem_identification\": \"CP was treated as inherently robust due to its distribution-free guarantees, but no prior work studied whether adversaries could deliberately manipulate CP prediction sets through data poisoning. The gap was that CP's reliance on nonconformity score thresholds from calibration data creates an attack surface distinct from classification accuracy attacks.\",\n    \"key_insight\": \"Targeting prediction uncertainty (set size) rather than misclassification is a fundamentally different and more effective attack objective — traditional poisoning defenses designed for accuracy are ineffective because they optimize for the wrong metric.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"The authors formulate black-box bilevel optimization attacks where the outer objective maximizes (inflation) or minimizes (shrinkage) prediction set sizes for target examples, while the inner objective trains the model on poisoned data. Attacks work on both full and split CP settings. A stealth constraint ensures correct labels remain in post-attack prediction sets to avoid detection, manipulating only set cardinality.\",\n    \"limitations_and_open_questions\": \"Attacks assume the adversary can poison training/calibration data (not test-time retrieval), and the bilevel optimization requires knowledge of the CP procedure. How these attacks compose with retrieval corruption in RAG pipelines is unexplored.\",\n    \"building_blocks\": [\n      \"Bilevel optimization for CP set manipulation\",\n      \"Set inflation/shrinkage attack objectives\",\n      \"Stealth constraints preserving label inclusion\",\n      \"Demonstration that CP-specific defenses are needed beyond accuracy-focused ones\"\n    ],\n    \"relevance_to_seed\": \"Establishes that CP is not inherently robust to adversarial manipulation — directly motivates why our retrieval-aware score function must be designed to resist poisoning-induced nonconformity score distortions rather than assuming CP guarantees hold automatically.\"\n  },\n  {\n    \"title\": \"Conformal Prediction for Natural Language Processing: A Survey\",\n    \"venue\": \"TACL 2025\",\n    \"problem_identification\": \"CP adoption in NLP was growing rapidly but fragmented across tasks, methods, and guarantee types with no unified reference. The authors identified that practitioners lacked guidance on which CP variant suits which NLP task, and that key open problems (distribution shift, non-exchangeability in autoregressive generation) were scattered across disparate literatures.\",\n    \"key_insight\": \"The recursive conditional nature of language generation fundamentally violates exchangeability — the core CP assumption — making naive CP application to NLG tasks theoretically unsound without explicit non-exchangeability corrections.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The survey taxonomizes CP methods (split, full, cross-validation, jackknife+, Mondrian/conditional CP, conformal risk control) and maps them to NLP tasks (classification, sequence tagging, QA, generation). It catalogs solutions for non-exchangeability including TV-distance-based coverage bounds, k-NN dynamic calibration, and risk control extensions. Notably, RAG systems are entirely absent from the survey's coverage.\",\n    \"limitations_and_open_questions\": \"The survey does not address RAG or retrieval-augmented pipelines at all, and adversarial robustness receives only cursory treatment. The absence of RAG discussion in the most comprehensive CP-for-NLP survey confirms this is genuinely uncharted territory.\",\n    \"building_blocks\": [\n      \"Taxonomy of CP methods applicable to NLP\",\n      \"Non-exchangeability correction techniques catalog\",\n      \"Conformal risk control framework for generation\",\n      \"Open problem identification for adversarial settings\"\n    ],\n    \"relevance_to_seed\": \"Confirms that CP for RAG under adversarial conditions is an identified gap in the field's most authoritative survey — our work fills a void explicitly left open, strengthening the novelty argument.\"\n  },\n  {\n    \"title\": \"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Standard CP uses static thresholds that cannot adapt to varying task complexity and data distributions, leading to suboptimal coverage-accuracy-informativeness tradeoffs. Fixed α produces either overly conservative (large sets) or overly aggressive (missed coverage) behavior depending on input difficulty.\",\n    \"key_insight\": \"CP thresholds can be treated as learnable actions in an RL framework — a policy network outputs distribution parameters for α and β, enabling instance-adaptive abstention that balances multiple competing objectives while preserving coverage guarantees through exchangeability-based proofs independent of threshold selection.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"The CAP framework partitions inputs into three regimes via dual thresholds (q_predict, q_abstain) on nonconformity scores: single prediction (high confidence), set prediction (moderate), or abstention (high uncertainty). A REINFORCE-trained policy network generates α, β from Gaussian distributions, optimizing a composite cost: (1−acc) + λ₁·avgSet + λ₂·abstention − λ₃·coverage − λ₄·diversity. Coverage guarantees persist because the rank-based validity argument is independent of how thresholds are selected.\",\n    \"limitations_and_open_questions\": \"The RL training assumes i.i.d. data and stable distributions — under adversarial distribution shift (as in corpus poisoning), the learned policy may produce miscalibrated thresholds. No adversarial robustness evaluation is conducted.\",\n    \"building_blocks\": [\n      \"Dual-threshold abstention architecture (predict/set/abstain)\",\n      \"RL-based adaptive CP threshold optimization\",\n      \"Composite reward balancing coverage, accuracy, and set size\",\n      \"Proof that coverage guarantees hold under adaptive thresholds\"\n    ],\n    \"relevance_to_seed\": \"The three-outcome abstention framework (predict/set/abstain) and RL-based threshold adaptation are directly applicable to designing tunable coverage-abstention tradeoffs in our poisoning-robust CP framework — but we must ensure the policy remains valid under adversarial retrieval corruption.\"\n  },\n  {\n    \"title\": \"Domain-Shift-Aware Conformal Prediction for Large Language Models\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Standard CP fails under domain shift because exchangeability is violated, causing systematic under-coverage. Direct density ratio estimation in high-dimensional text space is infeasible, leaving practitioners without practical tools to maintain CP validity when deployment distribution differs from calibration.\",\n    \"key_insight\": \"By projecting prompts into a 384-dimensional sentence embedding space and training an XGBoost classifier to distinguish calibration vs. test domains, density ratios can be estimated tractably — avoiding the curse of dimensionality that makes direct estimation in text space impossible.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"DS-CP reweights calibration samples by estimated density ratios computed in embedding space: an XGBoost classifier outputs P(test|embedding), converted to ratios r̂(z) = p̂(z)/(1−p̂(z))·P(cal)/P(test). A regularization term λ replaces the unstable test-point weight, yielding a weighted empirical distribution over calibration scores. Theoretical bounds show coverage degrades gracefully as a function of TV distance between score distributions, recovering exact validity under exchangeability.\",\n    \"limitations_and_open_questions\": \"The method assumes domain shift is organic (not adversarial) — an adversary who crafts poisoned documents to be embedding-proximal to benign ones could evade the reweighting. The XGBoost classifier requires representative test-domain samples at calibration time, which may not exist under adversarial poisoning.\",\n    \"building_blocks\": [\n      \"Embedding-space density ratio estimation via classification\",\n      \"Regularized calibration reweighting avoiding test-point instability\",\n      \"TV-distance-based graceful coverage degradation bounds\",\n      \"Practical recipe for non-exchangeable CP in LLM pipelines\"\n    ],\n    \"relevance_to_seed\": \"The proximity-based reweighting technique could be adapted for our retrieval-aware score function — reweighting calibration scores based on retrieval-agreement proximity rather than domain proximity — but must be hardened against adversarial embedding manipulation.\"\n  },\n  {\n    \"title\": \"Mitigating LLM Hallucinations via Conformal Abstention\",\n    \"venue\": \"NeurIPS 2024 Workshop (Statistical Frontiers in LLMs and Foundation Models)\",\n    \"problem_identification\": \"Standard LLM confidence signals (log-probabilities) degrade for long-form responses, making hallucination detection unreliable. The authors identified that token-level probability scores become non-indicative of correctness as sequence length grows, leaving no principled abstention mechanism with formal guarantees.\",\n    \"key_insight\": \"Self-consistency among multiple sampled LLM responses, evaluated by the LLM itself as a semantic similarity judge, provides a query-dependent nonconformity score that is far more robust to output length than token log-probabilities.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Sample k responses per query, compute pairwise semantic similarity via LLM self-evaluation (Match Count) or expected match count via token probabilities (EMC), then apply Conformal Risk Control to calibrate an abstention threshold λ such that E[R(λ)] ≤ α. The match function threshold β is itself calibrated via CP to bound false negative matches. A high-probability amplification variant partitions calibration data into K subsets to achieve P(R ≤ eα) ≥ 1−δ.\",\n    \"limitations_and_open_questions\": \"Assumes exchangeability between calibration and deployment — any distribution shift (including adversarial retrieval corruption) invalidates guarantees. Self-consistency fails when the model is systematically wrong (confidently hallucinating the same incorrect answer across samples).\",\n    \"building_blocks\": [\n      \"Self-consistency nonconformity scores\",\n      \"Conformal Risk Control (CRC) for abstention threshold calibration\",\n      \"LLM-as-judge similarity scoring\",\n      \"Match function calibration via CP\"\n    ],\n    \"relevance_to_seed\": \"Establishes the conformal abstention paradigm we extend; its exchangeability assumption is precisely what corpus poisoning violates, making it the starting point our retrieval-aware score function must fix.\"\n  },\n  {\n    \"title\": \"Robust Yet Efficient Conformal Prediction Sets\",\n    \"venue\": \"ICML 2024\",\n    \"problem_identification\": \"Prior robust CP (RSCP) produced vacuously large prediction sets because it bounded worst-case score changes using only the mean of smoothed scores, discarding distributional information. This made robust CP impractical for real deployment.\",\n    \"key_insight\": \"Replacing mean-only bounds on smoothed conformity scores with CDF-based bounds captures full distributional information about score behavior under perturbation, yielding strictly tighter worst-case estimates that produce 2-10x smaller prediction sets.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CAS (CDF-Aware Smoothed prediction sets) applies randomized smoothing to conformity scores (Gaussian for continuous, XOR-Bernoulli for discrete data), then optimizes worst-case scores over a function class constrained by the full empirical CDF rather than just the mean. For poisoning, the method formulates worst-case quantile computation as a MILP over feasible calibration perturbations. DKW/Bernstein finite-sample corrections replace Hoeffding bounds for tighter guarantees.\",\n    \"limitations_and_open_questions\": \"MILP poisoning certification doesn't scale to large calibration sets. Exchangeability still assumed — the method handles bounded perturbations to calibration data but not the fundamentally different threat model of test-time retrieval corruption where the adversary controls which documents are seen.\",\n    \"building_blocks\": [\n      \"CDF-based worst-case score bounding\",\n      \"MILP for poisoning-robust quantile computation\",\n      \"Calibration-time variant (precompute lower bounds offline)\",\n      \"DKW finite-sample corrections\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates how to achieve tight robust CP sets under poisoning, but its threat model assumes calibration-set corruption — adapting CDF-aware bounding to retrieval-time corruption (where poisoned documents affect test scores, not calibration) is a key technical challenge for our work.\"\n  },\n  {\n    \"title\": \"Towards Poisoning Robustness Certification for Natural Language Generation\",\n    \"venue\": \"arXiv 2026 (preprint)\",\n    \"problem_identification\": \"Certified poisoning defenses exist only for classification; the autoregressive nature of NLG (sequential predictions, exponential output space) makes direct adaptation impossible. No prior work could certify that generation outputs remain valid under bounded training-data poisoning.\",\n    \"key_insight\": \"Decomposing robustness into stability (no output change) vs. validity (no specific harmful output), and certifying validity via Targeted Partition Aggregation that computes the minimum poisoning budget to induce a specific harmful token — validity is much more certifiable than stability because the attacker's target constrains the certification problem.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"TPA extends shard-and-aggregate to NLG: partition training data into S shards, train independent models per shard, aggregate via majority voting over tokens. For validity certification, TPA iteratively reallocates votes from top-ranked tokens to a target harmful token to compute the minimum number of shard poisonings needed. Multi-turn certification uses MILP to distribute a global poisoning budget K across shards optimally. Phrase-level voting over V^m extends token-level certificates to sequences.\",\n    \"limitations_and_open_questions\": \"Addresses training-time poisoning, not test-time retrieval corruption — orthogonal threat model to our work. Inference latency with hundreds of shard models (150s) remains impractical. Certificates are conservative: empirical robustness substantially exceeds certified bounds.\",\n    \"building_blocks\": [\n      \"Stability vs. validity decomposition\",\n      \"Targeted Partition Aggregation algorithm\",\n      \"MILP collective certification across prompts\",\n      \"Phrase-level majority voting\"\n    ],\n    \"relevance_to_seed\": \"Closest existing work to our direction but in a different threat model (training poisoning vs. retrieval corruption) and without conformal prediction — demonstrates the partition-and-aggregate paradigm we adapt, and the validity concept maps to our abstention decision.\"\n  },\n  {\n    \"title\": \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\",\n    \"venue\": \"ICLR 2025 (Rejected)\",\n    \"problem_identification\": \"RAG poisoning attacks succeed empirically but lack theoretical explanation of why. The authors identified that understanding the geometric structure of embedding spaces reveals which attack directions are most effective, enabling principled defense design.\",\n    \"key_insight\": \"Effective poisoning attacks exploit low-variance directions of the clean embedding distribution — directions where probability mass is tightly concentrated — because small perturbations along these directions rapidly move away from clean document density, making poisoned documents dominate retrieval.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Eigendecompose the clean corpus covariance matrix; low-variance directions (small eigenvalues) are where attacks are most effective. DRS defense projects test documents onto these low-variance eigenvectors and flags documents with high directional relative shift. The regularized attack adds a DRS penalty to the poisoning objective, trading attack success for stealthiness. Detection threshold set at 99th percentile of clean DRS scores.\",\n    \"limitations_and_open_questions\": \"Rejected at ICLR due to a fundamental assumption that adversarial and normal queries are geometrically separable — entity-substitution attacks (semantically similar poisoned docs) defeat this. Requires pre-specified protected query set and trusted clean corpus. DRS performance drops to 49-65% on subtle grammatical-perturbation attacks.\",\n    \"building_blocks\": [\n      \"Low-variance direction analysis of embedding spaces\",\n      \"Eigendecomposition-based anomaly detection\",\n      \"Attack-defense co-optimization framework\",\n      \"Directional Relative Shift metric\"\n    ],\n    \"relevance_to_seed\": \"The low-variance direction analysis explains why poisoned documents can fool retrievers, supporting our argument that retrieval-level defenses alone are insufficient — but the DRS defense's fragility to semantic poisoning reinforces the need for our abstention-based approach rather than detection-based filtering.\"\n  },\n  {\n    \"title\": \"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search\",\n    \"venue\": \"ACM CCS 2025\",\n    \"problem_identification\": \"Prior corpus poisoning attacks used relaxed threat models (corpus access, ground-truth labels) and underperformed due to a token-to-text irreversibility bug — optimized token sequences produce different tokens when decoded to text and re-tokenized for corpus insertion.\",\n    \"key_insight\": \"The ReTokenize consistency check — filtering token substitutions that would change after a text→tokens→text round trip — eliminates the primary failure mode of prior discrete optimization attacks, enabling a simple dot-product maximization objective to achieve near-perfect attack success.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Construct adversarial passages as info||trigger, where info carries attacker content and trigger (100 tokens) is optimized via multi-coordinate greedy search. Each iteration averages gradient approximations across 50 random single-token substitutions, selects 20 positions simultaneously, filters candidates through ReTokenize consistency, and greedily picks the best. For multi-passage budgets, k-means clusters target query embeddings and optimizes one passage per centroid.\",\n    \"limitations_and_open_questions\": \"Requires white-box model access (limited black-box transferability at 25-60%). 'Knows Nothing' attacks remain hard (5-20% vs 61-100% for concept-specific). Trigger text remains syntactically odd despite perplexity constraints, potentially flaggable by future content moderation.\",\n    \"building_blocks\": [\n      \"ReTokenize consistency filtering\",\n      \"Multi-coordinate discrete optimization\",\n      \"Vulnerability factors: dot-product models and anisotropic embeddings more exploitable\",\n      \"Adaptive attacks bypassing perplexity and L2-norm defenses\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates that dense retrieval is catastrophically vulnerable at 0.0001% poisoning — even 10 adversarial passages in 8.8M suffice. This proves retrieval-level defenses are fundamentally insufficient, directly motivating our conformal abstention framework as a necessary last line of defense.\"\n  },\n  {\n    \"title\": \"Language Models with Conformal Factuality Guarantees\",\n    \"venue\": \"ICML 2024 (Stanford)\",\n    \"problem_identification\": \"LLM outputs lack formal correctness guarantees; existing CP methods target classification/regression, not free-form text generation. The authors identified that LLM correctness can be recast as set membership via entailment.\",\n    \"key_insight\": \"LLM correctness is equivalent to checking whether the ground truth belongs to the entailment set E(y) of the output — transforming open-ended factuality into a conformal coverage problem solvable by progressively reducing output specificity.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines the entailment operator E(y)={y': y'⇒y} so correctness holds iff y*∈E(y). A back-off function F_t decomposes outputs into atomic sub-claims via separator S, scores them, and removes those below threshold t, merging survivors via M. The conformal threshold q̂_α is calibrated on exchangeable (x,y*) pairs such that P(y*∈E(F_{q̂}(x)))≥1−α. Four scoring functions (frequency, GPT-4 confidence, ordinal, oracle) are explored; all yield valid guarantees since coverage depends only on calibration quantile correctness, not score quality.\",\n    \"limitations_and_open_questions\": \"Relies on a binary entailment oracle (approximated by NLI models, introducing noise); assumes exchangeability of calibration/test data with no robustness to distribution shift; back-off can produce vacuously general outputs at high coverage targets.\",\n    \"building_blocks\": [\n      \"Entailment-set formulation of LLM correctness\",\n      \"Sub-claim decomposition + scoring pipeline\",\n      \"Back-off conformal algorithm template\",\n      \"Black-box LM compatibility pattern\"\n    ],\n    \"relevance_to_seed\": \"Defines the conformal factuality paradigm our framework must extend — we need to ensure the back-off mechanism remains valid when retrieval corpus is adversarially poisoned, which violates the exchangeability assumption this paper critically depends on.\"\n  },\n  {\n    \"title\": \"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Existing robust CP handles specific shift types (covariate shift via reweighting, adversarial via smoothing) but lacks a unified framework; the authors identified that the Lévy-Prokhorov metric naturally decomposes into local (W_∞) and global (TV) components, bridging these disjoint approaches.\",\n    \"key_insight\": \"The LP ambiguity set decomposes as B_{ε,ρ}(P) = ∪_{W_∞(P,P̃)≤ε} {Q: TV(P̃,Q)≤ρ}, and propagating through a k-Lipschitz score function preserves the LP structure with scaled parameters (kε,ρ), reducing intractable high-dimensional robustness to closed-form 1D quantile adjustments.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines LP ambiguity sets via optimal-transport threshold cost. Proves the key propagation result: s#B_{ε,ρ}(P)⊆B_{kε,ρ}(s#P) for k-Lipschitz scores, collapsing the problem to 1D. Derives closed-form worst-case quantile Q^WC=Quant(β+ρ;P)+ε and worst-case coverage Cov^WC=F_P(q−ε)−ρ. The main theorem provides finite-sample coverage guarantees for prediction sets constructed with these adjusted quantiles under arbitrary LP-bounded test distributions.\",\n    \"limitations_and_open_questions\": \"Requires knowledge of (ε,ρ) bounds a priori; Lipschitz constant k of the score function may be hard to compute or loose for neural scores; experiments focus on standard benchmarks rather than adversarial/poisoning settings where the framework would be most needed.\",\n    \"building_blocks\": [\n      \"LP ambiguity set decomposition into local+global shifts\",\n      \"Score-function propagation reducing dimensionality\",\n      \"Closed-form worst-case quantile/coverage formulas\",\n      \"Unified framework subsuming TV and W_∞ robustness\"\n    ],\n    \"relevance_to_seed\": \"Directly applicable: corpus poisoning induces both local perturbations (adversarial doc content near benign) and global perturbations (mass on entirely new distributions). The ρ parameter maps to poisoning fraction and ε to embedding-space perturbation radius — our retrieval-agreement scores could serve as the Lipschitz score function enabling the dimensional reduction.\"\n  },\n  {\n    \"title\": \"Conformal Prediction as Bayesian Quadrature\",\n    \"venue\": \"ICML 2025 (Outstanding Paper Award)\",\n    \"problem_identification\": \"Standard CP provides marginal guarantees (averaged over all possible calibration sets) but frequently fails for specific datasets — CRC violated risk thresholds 21% of the time on synthetic data and 45% on MS-COCO despite valid marginal guarantees. The gap between marginal and conditional reliability was identified as a fundamental limitation.\",\n    \"key_insight\": \"For i.i.d. calibration losses, the quantile spacings U_i follow a Dirichlet(1,...,1) distribution regardless of the underlying loss distribution, enabling distribution-free Bayesian inference over the quantile function K(t) and yielding a full posterior over test-time risk rather than a point estimate.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Constructs the upper-bound random variable L⁺=Σ U_i·ℓ_{(i)} where U~Dir(1,...,1) and ℓ_{(i)} are ordered losses. Proves L⁺ stochastically dominates the posterior risk for any prior (Theorem 4.5), recovering split CP and CRC as special cases when only E[L⁺] is used. The full distribution of L⁺ provides data-conditional credible intervals: practitioners choose threshold b*_β such that Pr(L⁺≤b)≥β, yielding guarantees conditioned on the actual calibration data observed.\",\n    \"limitations_and_open_questions\": \"The upper bound L⁺ can be conservative; computational cost of sampling Dirichlet spacings scales with calibration set size; extension to non-exchangeable or contaminated settings (where the Dirichlet property breaks) is unexplored and directly relevant to our poisoning scenario.\",\n    \"building_blocks\": [\n      \"Dirichlet spacing property for distribution-free Bayesian inference\",\n      \"Stochastic dominance bound L⁺ over posterior risk\",\n      \"Data-conditional vs. marginal guarantee distinction\",\n      \"Unification of split CP and CRC as special cases\"\n    ],\n    \"relevance_to_seed\": \"The data-conditional guarantee framework is highly relevant — under corpus poisoning, marginal guarantees\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:47:14.662Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:47:14.662Z",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-30T06:47:14.677Z_

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
    "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
    "venue": "USENIX Security 2025",
    "problem_identification": "No prior work systematically studied whether injecting a small number of adversarial texts into a million-scale RAG knowledge base could reliably steer LLM outputs. The attack surface of the retrieval corpus itself was unexamined despite real-world RAG deployments drawing from open/semi-open corpora.",
    "key_insight": "Corpus poisoning decomposes into two independently solvable sub-problems—retrievability (poisoned text must rank in top-k) and persuasion (retrieved text must convince the LLM)—and satisfying both simultaneously requires only ~5 injected passages per target question even in million-scale databases.",
    "innovation_type": "new_formulation",
    "method_summary": "Formalizes RAG poisoning as a constrained optimization over retrievability and persuasion. Black-box variant uses an LLM to generate topically plausible passages containing the target answer (naturally achieving retrieval similarity). White-box variant uses HotFlip-based gradient optimization against the retriever's embedding model to maximize query-passage similarity while embedding attacker-chosen content. Evaluates on NQ, HotpotQA, MS-MARCO with Contriever retrieval across GPT-4, PaLM 2, LLaMA-2, and Vicuna.",
    "limitations_and_open_questions": "Targets individual questions rather than broad topic corruption; all tested defenses (paraphrasing, perplexity filtering, deduplication, knowledge expansion) provide only partial mitigation. No evaluation against adaptive defenses or retrieval-level embedding-space anomaly detection.",
    "building_blocks": [
      "Retrievability+persuasion decomposition framework",
      "HotFlip adaptation for dense retriever manipulation",
      "LLM-as-attacker passage generation",
      "PoisonedRAG attack protocol (NQ/HotpotQA/MS-MARCO + Contriever)",
      "Open-source evaluation codebase"
    ],
    "relevance_to_seed": "Defines the exact threat model our conformal abstention framework must defend against; its attack protocol (5 injected passages, 90%+ ASR) is the required evaluation benchmark, and the finding that surface-level defenses fail motivates principled statistical approaches like CP."
  },
  {
    "title": "CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift",
    "venue": "ICLR 2026",
    "problem_identification": "Standard conformal factuality guarantees (Mohri & Hashimoto 2024) require exchangeability between calibration and test data, which breaks under production distribution shift (trending topics, demographic changes). The authors showed empirically that standard CP drops well below target factuality under shift and that online CP methods requiring test-time labels are inapplicable.",
    "key_insight": "Weighted conformal prediction can be made practical for LLM factuality by solving density ratio estimation online via an ensemble of experts with geometrically-spaced lifetimes, sidestepping both the exchangeability requirement and the need for test-time ground truth.",
    "innovation_type": "cross_domain",
    "method_summary": "Decomposes LLM responses into atomic claims scored for factuality. Uses importance-weighted CP where calibration scores are reweighted by density ratios D_t(Z)/D_0(Z). Estimates these ratios online via an ensemble of logistic regression experts updated with Online Newton Step, with geometrically increasing lifetimes (2^0, 2^1, ...) to track non-stationary shift. Provides a bound: |1/T·Σerr_t − α| = Õ(max{T^{−2/3}V_T^{2/3}, T^{−1/2}} + n^{−1/2}).",
    "limitations_and_open_questions": "Requires 50-150 timestep burn-in before guarantees stabilize—a vulnerability window. Assumes covariate shift (P(Y|X) unchanged), which fails under adversarial poisoning where injected documents change the conditional factuality. Bounded density ratio assumption may fail when poisoned documents have no calibration-time analogue.",
    "building_blocks": [
      "Online density ratio estimation with expert ensembles",
      "Weighted conformal prediction framework (Tibshirani et al. 2019)",
      "Atomic claim decomposition + FActScore-style evaluation",
      "WildChat+ dataset with natural covariate shift",
      "Online Newton Step for expert updates"
    ],
    "relevance_to_seed": "Most directly relevant theoretical tool: its weighted CP machinery for handling distribution shift could be adapted for corpus poisoning, but the covariate-shift-only assumption (P(Y|X) unchanged) must be extended to handle the concept shift that adversarial document injection induces."
  },
  {
    "title": "Merging Uncertainty Sets via Majority Vote",
    "venue": "arXiv 2024",
    "problem_identification": "Given K arbitrarily dependent uncertainty sets (from different models, conformal splits, or estimators), there was no principled black-box merging procedure with finite-sample coverage guarantees. Practitioners routinely produce multiple valid prediction sets but lacked a general-purpose aggregation method.",
    "key_insight": "Majority vote—include a point in the merged set iff it appears in ≥⌈K/2⌉ input sets—yields coverage that improves exponentially in K via a binomial tail bound, requiring no assumptions about dependence structure or construction method of the individual sets.",
    "innovation_type": "new_technique",
    "method_summary": "Partition data into K groups, construct valid uncertainty sets C_k on each, merge via majority vote: θ ∈ C_merge iff |{k: θ ∈ C_k}| ≥ ⌈K/2⌉. Coverage guarantee: P(θ* ∈ C_merge) ≥ 1 − B(K, ⌈K/2⌉, α) where B is the binomial CDF. Extensions include weighted voting (w_k-weighted inclusion threshold), randomized thresholds for tighter sets, and sequential/streaming merging. Unifies median-of-means, HulC, and multi-split conformal as special cases.",
    "limitations_and_open_questions": "Merged sets can be larger than individual sets for small K (conservatism cost). Whether the binomial bound is information-theoretically tight is open. No discussion of computational cost when individual sets have complex geometry. Assumes each input set has valid marginal coverage—fails if the adversary corrupts calibration itself.",
    "building_blocks": [
      "Partition-and-vote paradigm for ensemble UQ",
      "Binomial tail coverage bound",
      "Weighted majority vote with trust-weighted aggregation",
      "Randomized threshold technique for set size reduction",
      "Connection to median-of-means and HulC"
    ],
    "relevance_to_seed": "Directly provides the theoretical template for our retrieval-agreement groups: partition retrieved passages into K groups, form per-group conformal sets, merge via majority vote—yielding Byzantine fault tolerance where coverage holds as long as fewer than half the groups are poisoned."
  },
  {
    "title": "URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models",
    "venue": "arXiv 2026",
    "problem_identification": "Existing RAG benchmarks focus exclusively on correctness metrics (accuracy, F1) while ignoring how retrieval affects uncertainty and reliability. No prior work systematically evaluated whether conformal prediction methods maintain valid coverage across diverse RAG architectures and domains, especially under retrieval noise.",
    "key_insight": "By reformulating open-ended QA into multiple-choice format via an iterative NLI-based distractor generation pipeline (achieving 96-100% validity), conformal prediction methods (LAC, APS) become directly applicable to RAG outputs—revealing that the accuracy-uncertainty correlation breaks specifically when retrieval introduces noise.",
    "innovation_type": "new_benchmark",
    "method_summary": "Converts open-ended QA to MCQA using Gemini-generated distractors filtered by NLI for factual incorrectness, contextual plausibility, and semantic type matching. Evaluates 8 RAG methods (Naive, Fusion, HyDE, RAT, FiD, Self-RAG, RAPTOR, REPLUG) across 8 datasets in 5 domains using LAC and APS conformal methods on Llama-3.1-8B. Measures both accuracy and prediction set sizes as complementary reliability metrics.",
    "limitations_and_open_questions": "MCQA conversion introduces approximation vs. open-ended generation. Evaluated only on Llama-3.1-8B; generalization unclear. Does not study adversarial/intentional poisoning—only natural retrieval noise. Open question: how findings transfer to free-form generation without MCQA scaffolding.",
    "building_blocks": [
      "MCQA conversion pipeline with NLI-based distractor refinement",
      "LAC and APS conformal prediction applied to LLM logits",
      "8-dataset evaluation suite across 5 domains",
      "Accuracy-uncertainty correlation analysis framework",
      "Parametric vs. retrieval knowledge dependency analysis"
    ],
    "relevance_to_seed": "Provides evaluation infrastructure and the key empirical finding that retrieval noise breaks CP coverage—directly motivating our work. The MCQA+CP pipeline is reusable for evaluating conformal abstention under adversarial poisoning, and URAG's finding that confident errors are amplified by retrieval cues predicts exactly the failure mode poisoning attacks exploit."
  },
  {
    "title": "RAGDefender: Rescuing the Unpoisoned — Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
    "venue": "ACSAC 2025",
    "problem_identification": "Existing RAG poisoning defenses (RobustRAG, Discern-and-Answer) require multiple LLM inference passes or fine-tuning, making them prohibitively expensive (14-42 GB GPU memory, $1-59 per iteration). No efficient, training-free, model-agnostic defense existed for post-retrieval poisoning detection.",
    "key_insight": "Adversarial passages crafted to push the LLM toward the same incorrect answer form semantically dense clusters in embedding space—a detectable signal exploitable with lightweight ML (cosine similarity, hierarchical clustering, TF-IDF) without any LLM involvement in the defense itself.",
    "innovation_type": "simplification",
    "method_summary": "Two-stage pipeline: Stage 1 estimates the number of adversarial passages N_adv using hierarchical agglomerative clustering on passage embeddings plus TF-IDF term co-occurrence (single-hop) or mean/median cosine similarity concentration (multi-hop). Stage 2 identifies specific adversarial passages by computing pairwise cosine similarities, scoring each passage by weighted frequency in top-similar pairs (f_i = Σ|sim|^p), and removing the top-N_adv ranked passages. Achieves 0.02 ASR (vs. 0.89 undefended, 0.69 RobustRAG) at 12x speed and zero GPU cost.",
    "limitations_and_open_questions": "No formal theoretical guarantees that poisoned passages always cluster—purely empirical. Sophisticated adaptive attacks deliberately diversifying adversarial embeddings (anti-clustering) could evade detection, though tested adaptive attacks still yield only 0.13 ASR. Untested beyond k=10 retrieval set sizes.",
    "building_blocks": [
      "Embedding-space clustering for poisoned passage detection",
      "Pairwise cosine similarity frequency scoring",
      "TF-IDF co-occurrence for adversarial set size estimation",
      "Hierarchical agglomerative clustering",
      "PoisonedRAG evaluation protocol with Contriever/DPR/ANCE"
    ],
    "relevance_to_seed": "Provides a key comparison baseline and a potential nonconformity score ingredient: the clustering signal (pairwise similarity concentration among retrieved passages) could be incorporated into retrieval-aware conformal scores, combining RAGDefender's efficient detection with CP's formal coverage guarantees—addressing the paper's acknowledged lack of theoretical certificates."
  },
  {
    "title": "CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation",
    "venue": "ACM SACMAT 2026",
    "problem_identification": "Prior RAG poisoning attacks (PoisonedRAG) require injecting multiple (≥5) poisoned documents per query to outnumber benign retrievals, which is costly, detectable, and unrealistic in practice. The authors showed empirically that most queries retrieve fewer than 3 relevant docs in top-5, making multi-document poisoning assumptions fragile.",
    "key_insight": "A single poisoned document can dominate RAG output if it embeds the query verbatim (guaranteeing top retrieval rank) and uses adversarial framing that exploits LLMs' bias toward 'recent' information to override benign context.",
    "innovation_type": "simplification",
    "method_summary": "The poisoned text is split into a retrieval component (query copied verbatim for maximal similarity) and a manipulation component containing an adversarial statement ('outdated corpus states [correct answer]') plus a target statement ('latest data confirms [desired answer]'). Two variants exist: CRAG-AS (template-based, zero-cost) and CRAG-AK (LLM-refined knowledge-like text for cross-query generalization at $0.0001/query). The attack is fully black-box — no access to retriever or LLM parameters.",
    "limitations_and_open_questions": "Defense evaluation is limited to LLM-based detection (0-10% TPR), but does not test against certified defenses like RobustRAG/ReliabilityRAG's isolate-then-aggregate strategies. Single-doc assumption may fail when aggregation defenses process passages independently.",
    "building_blocks": [
      "Single-document poisoning threat model",
      "Query-verbatim retrieval exploitation",
      "Adversarial framing templates for LLM manipulation",
      "CRAG-AK knowledge-style text generation"
    ],
    "relevance_to_seed": "Defines a more practical and stealthy attack protocol than PoisonedRAG for evaluating our conformal abstention framework — our method must handle the case where even a single poisoned document in top-k can corrupt outputs."
  },
  {
    "title": "Data Poisoning Attacks against Conformal Prediction",
    "venue": "ICML 2024",
    "problem_identification": "CP was treated as inherently robust due to its distribution-free guarantees, but no prior work studied whether adversaries could deliberately manipulate CP prediction sets through data poisoning. The gap was that CP's reliance on nonconformity score thresholds from calibration data creates an attack surface distinct from classification accuracy attacks.",
    "key_insight": "Targeting prediction uncertainty (set size) rather than misclassification is a fundamentally different and more effective attack objective — traditional poisoning defenses designed for accuracy are ineffective because they optimize for the wrong metric.",
    "innovation_type": "new_formulation",
    "method_summary": "The authors formulate black-box bilevel optimization attacks where the outer objective maximizes (inflation) or minimizes (shrinkage) prediction set sizes for target examples, while the inner objective trains the model on poisoned data. Attacks work on both full and split CP settings. A stealth constraint ensures correct labels remain in post-attack prediction sets to avoid detection, manipulating only set cardinality.",
    "limitations_and_open_questions": "Attacks assume the adversary can poison training/calibration data (not test-time retrieval), and the bilevel optimization requires knowledge of the CP procedure. How these attacks compose with retrieval corruption in RAG pipelines is unexplored.",
    "building_blocks": [
      "Bilevel optimization for CP set manipulation",
      "Set inflation/shrinkage attack objectives",
      "Stealth constraints preserving label inclusion",
      "Demonstration that CP-specific defenses are needed beyond accuracy-focused ones"
    ],
    "relevance_to_seed": "Establishes that CP is not inherently robust to adversarial manipulation — directly motivates why our retrieval-aware score function must be designed to resist poisoning-induced nonconformity score distortions rather than assuming CP guarantees hold automatically."
  },
  {
    "title": "Conformal Prediction for Natural Language Processing: A Survey",
    "venue": "TACL 2025",
    "problem_identification": "CP adoption in NLP was growing rapidly but fragmented across tasks, methods, and guarantee types with no unified reference. The authors identified that practitioners lacked guidance on which CP variant suits which NLP task, and that key open problems (distribution shift, non-exchangeability in autoregressive generation) were scattered across disparate literatures.",
    "key_insight": "The recursive conditional nature of language generation fundamentally violates exchangeability — the core CP assumption — making naive CP application to NLG tasks theoretically unsound without explicit non-exchangeability corrections.",
    "innovation_type": "analysis",
    "method_summary": "The survey taxonomizes CP methods (split, full, cross-validation, jackknife+, Mondrian/conditional CP, conformal risk control) and maps them to NLP tasks (classification, sequence tagging, QA, generation). It catalogs solutions for non-exchangeability including TV-distance-based coverage bounds, k-NN dynamic calibration, and risk control extensions. Notably, RAG systems are entirely absent from the survey's coverage.",
    "limitations_and_open_questions": "The survey does not address RAG or retrieval-augmented pipelines at all, and adversarial robustness receives only cursory treatment. The absence of RAG discussion in the most comprehensive CP-for-NLP survey confirms this is genuinely uncharted territory.",
    "building_blocks": [
      "Taxonomy of CP methods applicable to NLP",
      "Non-exchangeability correction techniques catalog",
      "Conformal risk control framework for generation",
      "Open problem identification for adversarial settings"
    ],
    "relevance_to_seed": "Confirms that CP for RAG under adversarial conditions is an identified gap in the field's most authoritative survey — our work fills a void explicitly left open, strengthening the novelty argument."
  },
  {
    "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models",
    "venue": "arXiv 2025",
    "problem_identification": "Standard CP uses static thresholds that cannot adapt to varying task complexity and data distributions, leading to suboptimal coverage-accuracy-informativeness tradeoffs. Fixed α produces either overly conservative (large sets) or overly aggressive (missed coverage) behavior depending on input difficulty.",
    "key_insight": "CP thresholds can be treated as learnable actions in an RL framework — a policy network outputs distribution parameters for α and β, enabling instance-adaptive abstention that balances multiple competing objectives while preserving coverage guarantees through exchangeability-based proofs independent of threshold selection.",
    "innovation_type": "combination",
    "method_summary": "The CAP framework partitions inputs into three regimes via dual thresholds (q_predict, q_abstain) on nonconformity scores: single prediction (high confidence), set prediction (moderate), or abstention (high uncertainty). A REINFORCE-trained policy network generates α, β from Gaussian distributions, optimizing a composite cost: (1−acc) + λ₁·avgSet + λ₂·abstention − λ₃·coverage − λ₄·diversity. Coverage guarantees persist because the rank-based validity argument is independent of how thresholds are selected.",
    "limitations_and_open_questions": "The RL training assumes i.i.d. data and stable distributions — under adversarial distribution shift (as in corpus poisoning), the learned policy may produce miscalibrated thresholds. No adversarial robustness evaluation is conducted.",
    "building_blocks": [
      "Dual-threshold abstention architecture (predict/set/abstain)",
      "RL-based adaptive CP threshold optimization",
      "Composite reward balancing coverage, accuracy, and set size",
      "Proof that coverage guarantees hold under adaptive thresholds"
    ],
    "relevance_to_seed": "The three-outcome abstention framework (predict/set/abstain) and RL-based threshold adaptation are directly applicable to designing tunable coverage-abstention tradeoffs in our poisoning-robust CP framework — but we must ensure the policy remains valid under adversarial retrieval corruption."
  },
  {
    "title": "Domain-Shift-Aware Conformal Prediction for Large Language Models",
    "venue": "arXiv 2025",
    "problem_identification": "Standard CP fails under domain shift because exchangeability is violated, causing systematic under-coverage. Direct density ratio estimation in high-dimensional text space is infeasible, leaving practitioners without practical tools to maintain CP validity when deployment distribution differs from calibration.",
    "key_insight": "By projecting prompts into a 384-dimensional sentence embedding space and training an XGBoost classifier to distinguish calibration vs. test domains, density ratios can be estimated tractably — avoiding the curse of dimensionality that makes direct estimation in text space impossible.",
    "innovation_type": "new_technique",
    "method_summary": "DS-CP reweights calibration samples by estimated density ratios computed in embedding space: an XGBoost classifier outputs P(test|embedding), converted to ratios r̂(z) = p̂(z)/(1−p̂(z))·P(cal)/P(test). A regularization term λ replaces the unstable test-point weight, yielding a weighted empirical distribution over calibration scores. Theoretical bounds show coverage degrades gracefully as a function of TV distance between score distributions, recovering exact validity under exchangeability.",
    "limitations_and_open_questions": "The method assumes domain shift is organic (not adversarial) — an adversary who crafts poisoned documents to be embedding-proximal to benign ones could evade the reweighting. The XGBoost classifier requires representative test-domain samples at calibration time, which may not exist under adversarial poisoning.",
    "building_blocks": [
      "Embedding-space density ratio estimation via classification",
      "Regularized calibration reweighting avoiding test-point instability",
      "TV-distance-based graceful coverage degradation bounds",
      "Practical recipe for non-exchangeable CP in LLM pipelines"
    ],
    "relevance_to_seed": "The proximity-based reweighting technique could be adapted for our retrieval-aware score function — reweighting calibration scores based on retrieval-agreement proximity rather than domain proximity — but must be hardened against adversarial embedding manipulation."
  },
  {
    "title": "Mitigating LLM Hallucinations via Conformal Abstention",
    "venue": "NeurIPS 2024 Workshop (Statistical Frontiers in LLMs and Foundation Models)",
    "problem_identification": "Standard LLM confidence signals (log-probabilities) degrade for long-form responses, making hallucination detection unreliable. The authors identified that token-level probability scores become non-indicative of correctness as sequence length grows, leaving no principled abstention mechanism with formal guarantees.",
    "key_insight": "Self-consistency among multiple sampled LLM responses, evaluated by the LLM itself as a semantic similarity judge, provides a query-dependent nonconformity score that is far more robust to output length than token log-probabilities.",
    "innovation_type": "combination",
    "method_summary": "Sample k responses per query, compute pairwise semantic similarity via LLM self-evaluation (Match Count) or expected match count via token probabilities (EMC), then apply Conformal Risk Control to calibrate an abstention threshold λ such that E[R(λ)] ≤ α. The match function threshold β is itself calibrated via CP to bound false negative matches. A high-probability amplification variant partitions calibration data into K subsets to achieve P(R ≤ eα) ≥ 1−δ.",
    "limitations_and_open_questions": "Assumes exchangeability between calibration and deployment — any distribution shift (including adversarial retrieval corruption) invalidates guarantees. Self-consistency fails when the model is systematically wrong (confidently hallucinating the same incorrect answer across samples).",
    "building_blocks": [
      "Self-consistency nonconformity scores",
      "Conformal Risk Control (CRC) for abstention threshold calibration",
      "LLM-as-judge similarity scoring",
      "Match function calibration via CP"
    ],
    "relevance_to_seed": "Establishes the conformal abstention paradigm we extend; its exchangeability assumption is precisely what corpus poisoning violates, making it the starting point our retrieval-aware score function must fix."
  },
  {
    "title": "Robust Yet Efficient Conformal Prediction Sets",
    "venue": "ICML 2024",
    "problem_identification": "Prior robust CP (RSCP) produced vacuously large prediction sets because it bounded worst-case score changes using only the mean of smoothed scores, discarding distributional information. This made robust CP impractical for real deployment.",
    "key_insight": "Replacing mean-only bounds on smoothed conformity scores with CDF-based bounds captures full distributional information about score behavior under perturbation, yielding strictly tighter worst-case estimates that produce 2-10x smaller prediction sets.",
    "innovation_type": "new_technique",
    "method_summary": "CAS (CDF-Aware Smoothed prediction sets) applies randomized smoothing to conformity scores (Gaussian for continuous, XOR-Bernoulli for discrete data), then optimizes worst-case scores over a function class constrained by the full empirical CDF rather than just the mean. For poisoning, the method formulates worst-case quantile computation as a MILP over feasible calibration perturbations. DKW/Bernstein finite-sample corrections replace Hoeffding bounds for tighter guarantees.",
    "limitations_and_open_questions": "MILP poisoning certification doesn't scale to large calibration sets. Exchangeability still assumed — the method handles bounded perturbations to calibration data but not the fundamentally different threat model of test-time retrieval corruption where the adversary controls which documents are seen.",
    "building_blocks": [
      "CDF-based worst-case score bounding",
      "MILP for poisoning-robust quantile computation",
      "Calibration-time variant (precompute lower bounds offline)",
      "DKW finite-sample corrections"
    ],
    "relevance_to_seed": "Demonstrates how to achieve tight robust CP sets under poisoning, but its threat model assumes calibration-set corruption — adapting CDF-aware bounding to retrieval-time corruption (where poisoned documents affect test scores, not calibration) is a key technical challenge for our work."
  },
  {
    "title": "Towards Poisoning Robustness Certification for Natural Language Generation",
    "venue": "arXiv 2026 (preprint)",
    "problem_identification": "Certified poisoning defenses exist only for classification; the autoregressive nature of NLG (sequential predictions, exponential output space) makes direct adaptation impossible. No prior work could certify that generation outputs remain valid under bounded training-data poisoning.",
    "key_insight": "Decomposing robustness into stability (no output change) vs. validity (no specific harmful output), and certifying validity via Targeted Partition Aggregation that computes the minimum poisoning budget to induce a specific harmful token — validity is much more certifiable than stability because the attacker's target constrains the certification problem.",
    "innovation_type": "cross_domain",
    "method_summary": "TPA extends shard-and-aggregate to NLG: partition training data into S shards, train independent models per shard, aggregate via majority voting over tokens. For validity certification, TPA iteratively reallocates votes from top-ranked tokens to a target harmful token to compute the minimum number of shard poisonings needed. Multi-turn certification uses MILP to distribute a global poisoning budget K across shards optimally. Phrase-level voting over V^m extends token-level certificates to sequences.",
    "limitations_and_open_questions": "Addresses training-time poisoning, not test-time retrieval corruption — orthogonal threat model to our work. Inference latency with hundreds of shard models (150s) remains impractical. Certificates are conservative: empirical robustness substantially exceeds certified bounds.",
    "building_blocks": [
      "Stability vs. validity decomposition",
      "Targeted Partition Aggregation algorithm",
      "MILP collective certification across prompts",
      "Phrase-level majority voting"
    ],
    "relevance_to_seed": "Closest existing work to our direction but in a different threat model (training poisoning vs. retrieval corruption) and without conformal prediction — demonstrates the partition-and-aggregate paradigm we adapt, and the validity concept maps to our abstention decision."
  },
  {
    "title": "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms",
    "venue": "ICLR 2025 (Rejected)",
    "problem_identification": "RAG poisoning attacks succeed empirically but lack theoretical explanation of why. The authors identified that understanding the geometric structure of embedding spaces reveals which attack directions are most effective, enabling principled defense design.",
    "key_insight": "Effective poisoning attacks exploit low-variance directions of the clean embedding distribution — directions where probability mass is tightly concentrated — because small perturbations along these directions rapidly move away from clean document density, making poisoned documents dominate retrieval.",
    "innovation_type": "analysis",
    "method_summary": "Eigendecompose the clean corpus covariance matrix; low-variance directions (small eigenvalues) are where attacks are most effective. DRS defense projects test documents onto these low-variance eigenvectors and flags documents with high directional relative shift. The regularized attack adds a DRS penalty to the poisoning objective, trading attack success for stealthiness. Detection threshold set at 99th percentile of clean DRS scores.",
    "limitations_and_open_questions": "Rejected at ICLR due to a fundamental assumption that adversarial and normal queries are geometrically separable — entity-substitution attacks (semantically similar poisoned docs) defeat this. Requires pre-specified protected query set and trusted clean corpus. DRS performance drops to 49-65% on subtle grammatical-perturbation attacks.",
    "building_blocks": [
      "Low-variance direction analysis of embedding spaces",
      "Eigendecomposition-based anomaly detection",
      "Attack-defense co-optimization framework",
      "Directional Relative Shift metric"
    ],
    "relevance_to_seed": "The low-variance direction analysis explains why poisoned documents can fool retrievers, supporting our argument that retrieval-level defenses alone are insufficient — but the DRS defense's fragility to semantic poisoning reinforces the need for our abstention-based approach rather than detection-based filtering."
  },
  {
    "title": "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search",
    "venue": "ACM CCS 2025",
    "problem_identification": "Prior corpus poisoning attacks used relaxed threat models (corpus access, ground-truth labels) and underperformed due to a token-to-text irreversibility bug — optimized token sequences produce different tokens when decoded to text and re-tokenized for corpus insertion.",
    "key_insight": "The ReTokenize consistency check — filtering token substitutions that would change after a text→tokens→text round trip — eliminates the primary failure mode of prior discrete optimization attacks, enabling a simple dot-product maximization objective to achieve near-perfect attack success.",
    "innovation_type": "new_technique",
    "method_summary": "Construct adversarial passages as info||trigger, where info carries attacker content and trigger (100 tokens) is optimized via multi-coordinate greedy search. Each iteration averages gradient approximations across 50 random single-token substitutions, selects 20 positions simultaneously, filters candidates through ReTokenize consistency, and greedily picks the best. For multi-passage budgets, k-means clusters target query embeddings and optimizes one passage per centroid.",
    "limitations_and_open_questions": "Requires white-box model access (limited black-box transferability at 25-60%). 'Knows Nothing' attacks remain hard (5-20% vs 61-100% for concept-specific). Trigger text remains syntactically odd despite perplexity constraints, potentially flaggable by future content moderation.",
    "building_blocks": [
      "ReTokenize consistency filtering",
      "Multi-coordinate discrete optimization",
      "Vulnerability factors: dot-product models and anisotropic embeddings more exploitable",
      "Adaptive attacks bypassing perplexity and L2-norm defenses"
    ],
    "relevance_to_seed": "Demonstrates that dense retrieval is catastrophically vulnerable at 0.0001% poisoning — even 10 adversarial passages in 8.8M suffice. This proves retrieval-level defenses are fundamentally insufficient, directly motivating our conformal abstention framework as a necessary last line of defense."
  },
  {
    "title": "Language Models with Conformal Factuality Guarantees",
    "venue": "ICML 2024 (Stanford)",
    "problem_identification": "LLM outputs lack formal correctness guarantees; existing CP methods target classification/regression, not free-form text generation. The authors identified that LLM correctness can be recast as set membership via entailment.",
    "key_insight": "LLM correctness is equivalent to checking whether the ground truth belongs to the entailment set E(y) of the output — transforming open-ended factuality into a conformal coverage problem solvable by progressively reducing output specificity.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines the entailment operator E(y)={y': y'⇒y} so correctness holds iff y*∈E(y). A back-off function F_t decomposes outputs into atomic sub-claims via separator S, scores them, and removes those below threshold t, merging survivors via M. The conformal threshold q̂_α is calibrated on exchangeable (x,y*) pairs such that P(y*∈E(F_{q̂}(x)))≥1−α. Four scoring functions (frequency, GPT-4 confidence, ordinal, oracle) are explored; all yield valid guarantees since coverage depends only on calibration quantile correctness, not score quality.",
    "limitations_and_open_questions": "Relies on a binary entailment oracle (approximated by NLI models, introducing noise); assumes exchangeability of calibration/test data with no robustness to distribution shift; back-off can produce vacuously general outputs at high coverage targets.",
    "building_blocks": [
      "Entailment-set formulation of LLM correctness",
      "Sub-claim decomposition + scoring pipeline",
      "Back-off conformal algorithm template",
      "Black-box LM compatibility pattern"
    ],
    "relevance_to_seed": "Defines the conformal factuality paradigm our framework must extend — we need to ensure the back-off mechanism remains valid when retrieval corpus is adversarially poisoned, which violates the exchangeability assumption this paper critically depends on."
  },
  {
    "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
    "venue": "NeurIPS 2025",
    "problem_identification": "Existing robust CP handles specific shift types (covariate shift via reweighting, adversarial via smoothing) but lacks a unified framework; the authors identified that the Lévy-Prokhorov metric naturally decomposes into local (W_∞) and global (TV) components, bridging these disjoint approaches.",
    "key_insight": "The LP ambiguity set decomposes as B_{ε,ρ}(P) = ∪_{W_∞(P,P̃)≤ε} {Q: TV(P̃,Q)≤ρ}, and propagating through a k-Lipschitz score function preserves the LP structure with scaled parameters (kε,ρ), reducing intractable high-dimensional robustness to closed-form 1D quantile adjustments.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines LP ambiguity sets via optimal-transport threshold cost. Proves the key propagation result: s#B_{ε,ρ}(P)⊆B_{kε,ρ}(s#P) for k-Lipschitz scores, collapsing the problem to 1D. Derives closed-form worst-case quantile Q^WC=Quant(β+ρ;P)+ε and worst-case coverage Cov^WC=F_P(q−ε)−ρ. The main theorem provides finite-sample coverage guarantees for prediction sets constructed with these adjusted quantiles under arbitrary LP-bounded test distributions.",
    "limitations_and_open_questions": "Requires knowledge of (ε,ρ) bounds a priori; Lipschitz constant k of the score function may be hard to compute or loose for neural scores; experiments focus on standard benchmarks rather than adversarial/poisoning settings where the framework would be most needed.",
    "building_blocks": [
      "LP ambiguity set decomposition into local+global shifts",
      "Score-function propagation reducing dimensionality",
      "Closed-form worst-case quantile/coverage formulas",
      "Unified framework subsuming TV and W_∞ robustness"
    ],
    "relevance_to_seed": "Directly applicable: corpus poisoning induces both local perturbations (adversarial doc content near benign) and global perturbations (mass on entirely new distributions). The ρ parameter maps to poisoning fraction and ε to embedding-space perturbation radius — our retrieval-agreement scores could serve as the Lipschitz score function enabling the dimensional reduction."
  },
  {
    "title": "Conformal Prediction as Bayesian Quadrature",
    "venue": "ICML 2025 (Outstanding Paper Award)",
    "problem_identification": "Standard CP provides marginal guarantees (averaged over all possible calibration sets) but frequently fails for specific datasets — CRC violated risk thresholds 21% of the time on synthetic data and 45% on MS-COCO despite valid marginal guarantees. The gap between marginal and conditional reliability was identified as a fundamental limitation.",
    "key_insight": "For i.i.d. calibration losses, the quantile spacings U_i follow a Dirichlet(1,...,1) distribution regardless of the underlying loss distribution, enabling distribution-free Bayesian inference over the quantile function K(t) and yielding a full posterior over test-time risk rather than a point estimate.",
    "innovation_type": "new_formulation",
    "method_summary": "Constructs the upper-bound random variable L⁺=Σ U_i·ℓ_{(i)} where U~Dir(1,...,1) and ℓ_{(i)} are ordered losses. Proves L⁺ stochastically dominates the posterior risk for any prior (Theorem 4.5), recovering split CP and CRC as special cases when only E[L⁺] is used. The full distribution of L⁺ provides data-conditional credible intervals: practitioners choose threshold b*_β such that Pr(L⁺≤b)≥β, yielding guarantees conditioned on the actual calibration data observed.",
    "limitations_and_open_questions": "The upper bound L⁺ can be conservative; computational cost of sampling Dirichlet spacings scales with calibration set size; extension to non-exchangeable or contaminated settings (where the Dirichlet property breaks) is unexplored and directly relevant to our poisoning scenario.",
    "building_blocks": [
      "Dirichlet spacing property for distribution-free Bayesian inference",
      "Stochastic dominance bound L⁺ over posterior risk",
      "Data-conditional vs. marginal guarantee distinction",
      "Unification of split CP and CRC as special cases"
    ],
    "relevance_to_seed": "The data-conditional guarantee framework is highly relevant — under corpus poisoning, marginal guarantees
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
  "promptId": "b7dda800-cbe9-4724-9677-3f2fddfc3f8f",
  "type": "user",
  "uuid": "9a1cec83-84fb-438b-8b2a-ba455b2ccb10",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:47:14.675Z_

```json
{
  "parentUuid": "9a1cec83-84fb-438b-8b2a-ba455b2ccb10",
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
  "uuid": "74338b66-1089-45bc-904c-5171c6e864b0",
  "timestamp": "2026-05-30T06:47:14.675Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:47:14.675Z_

```json
{
  "parentUuid": "74338b66-1089-45bc-904c-5171c6e864b0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b207f6dd-ddfb-4783-8097-4f97984cda85",
  "timestamp": "2026-05-30T06:47:14.675Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
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
  "leafUuid": "b207f6dd-ddfb-4783-8097-4f97984cda85",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction framework for poisoned RAG systems",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

### Assistant

_source line 8 · 2026-05-30T06:47:29.783Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for innovation in the area of conformal prediction for RAG systems under adversarial poisoning. This is a detailed research strategy document, not a survey. Let me carefully analyze the patterns across all papers and produce a comprehensive JSON output.

Let me think through each section carefully:

**Innovation Patterns:**
1. Cross-domain transfer (bringing CP techniques from classification to NLG/RAG)
2. Partition-and-aggregate for robustness
3. Threat model formalization leading to principled defenses


4. Streamlining computationally intensive methods
5. Reformulating problems to enable new solution approaches

**Reviewer Preferences:**
- Formal guarantees (not just empirical)
- Practical computation budgets
- Proper threat model specification
- Comparison against certified baselines
- Distribution-free properties

**Field Gaps:**
- No conformal abstention under retrieval corruption
- Threat model mismatch between calibration poisoning and retrieval poisoning
- No unified local+global robustness for RAG
- Conditional vs marginal guarantees under poisoning

**Untried Combinations:**
- Majority vote merging + retrieval agreement groups + LP robustness
- RAGDef

Now I'm looking at specific technical approaches: using embedding clustering signals as nonconformity scores within conformal prediction, combining adaptive thresholds with poisoning robustness, and weighting conformal predictions with retrieval-aware density ratios. The core building blocks I'm considering are partition-and-vote strategies, CDF-aware smoothing, embedding clustering, LP ambiguity sets, and Dirichlet spacing for data-conditional guarantees. I need to be careful about common pitfalls like assuming exchangeability, relying on LLM-based scores that can be manipulated, overlooking adaptive attacks, and overstating compositional guarantees. The field is shifting toward certified abstention over detection, conditional over marginal guarantees, and adversarial robustness over benign settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b207f6dd-ddfb-4783-8097-4f97984cda85",
  "isSidechain": false,
  "requestId": "req_011CbYJdn5joKbf9HrRA4KCa",
  "type": "assistant",
  "uuid": "57cb723b-97f2-427e-98fe-230dcbbac930",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqQFuuWyiZZbjutgrFX26F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12932,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7843,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7843,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12932
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

_source line 9 · 2026-05-30T06:50:24.735Z_

I'll analyze the 20 papers systematically to produce the field guide. Let me work through the patterns carefully.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Partition-and-Aggregate for Byzantine Robustness",
      "description": "Split data/models/documents into K independent groups, process each in isolation, and merge via majority vote or median. This converts a corruption problem into a voting problem where guarantees hold as long as fewer than half the groups are compromised. The pattern recurs across classification (RPS), NLG (TPA), retrieval (RobustRAG/ReliabilityRAG), and uncertainty merging (Majority Vote Merging).",
      "examples": ["Merging Uncertainty Sets via Majority Vote", "Towards Poisoning Robustness Certification for NLG (TPA)", "Certifiably Robust RAG (RobustRAG)", "ReliabilityRAG", "Provably Reliable CP Sets under Data Poisoning (RPS)"],
      "success_rate": "high"
    },
    {
      "pattern": "Threat Model Formalization → Principled Defense",
      "description": "Papers that precisely formalize an underspecified threat model and then derive defenses from the formal structure consistently outperform papers that propose ad-hoc heuristics. The formalization itself is often the primary contribution. PoisonedRAG decomposed poisoning into retrievability+persuasion; LP-CP decomposed distribution shift into local+global components; CAS decomposed score perturbation into CDF-tractable form.",
      "examples": ["PoisonedRAG", "Conformal Prediction under LP Distribution Shifts", "Robust Yet Efficient CP Sets (CAS)", "Data Poisoning Attacks against CP"],
      "success_rate": "high"
    },
    {
      "pattern": "Cross-Domain Transfer of CP Machinery",
      "description": "Taking a well-understood CP technique from one domain (classification, regression) and adapting it to a structurally different domain (NLG, RAG, VLMs) by solving the domain-specific exchangeability/score design challenges. CoFact transferred weighted CP to LLM factuality; Conformal Factuality transferred entailment sets to free-form text; CAP transferred RL-based threshold optimization to LLM abstention.",
      "examples": ["CoFact", "Language Models with Conformal Factuality Guarantees", "Learning Conformal Abstention Policies (CAP)", "Mitigating LLM Hallucinations via Conformal Abstention"],
      "success_rate": "high"
    },
    {
      "pattern": "Simplification that Unlocks Practicality",
      "description": "Papers that achieve comparable or superior performance to complex prior methods via dramatically simpler mechanisms, especially reducing inference cost. RAGDefender replaced multi-pass LLM defense with cosine-similarity clustering (12x faster, lower ASR). CorruptRAG showed single-document poisoning suffices vs. PoisonedRAG's 5-doc requirement. CAS replaced mean-only bounds with CDF bounds for 2-10x smaller sets.",
      "examples": ["RAGDefender", "CorruptRAG", "Robust Yet Efficient CP Sets (CAS)"],
      "success_rate": "medium"
    },
    {
      "pattern": "New Mathematical Formulation Revealing Hidden Structure",
      "description": "Papers that recast a problem in a different mathematical framework, exposing structure that enables closed-form or tractable solutions. CP-as-Bayesian-Quadrature revealed the Dirichlet spacing property for data-conditional guarantees; LP-CP revealed the local+global decomposition enabling 1D quantile adjustments; Conformal Factuality recast correctness as entailment-set membership.",
      "examples": ["Conformal Prediction as Bayesian Quadrature", "Conformal Prediction under LP Distribution Shifts", "Language Models with Conformal Factuality Guarantees"],
      "success_rate": "high"
    }
  ],

  "reviewer_preferences": [
    "Formal, distribution-free guarantees with explicit coverage bounds — empirical defenses without certificates are increasingly treated as incomplete (RobustRAG and ReliabilityRAG both emphasize certified guarantees; RAGDefender's acknowledged lack of theoretical certificates is its primary limitation).",
    "Clear threat model specification with explicit attacker capabilities, knowledge, and budget — PoisonedRAG and CorruptRAG were accepted at top security venues specifically because they formalized attacker decompositions; the ICLR-rejected embedding analysis paper failed partly due to a questionable geometric separability assumption.",
    "Practical computational cost within reason — RAGDefender's 12x speedup over RobustRAG was a key selling point; TPA's 150s inference was noted as impractical; CAS's improvement over vacuously large RSCP sets was critical for acceptance.",
    "Comparison against certified (not just heuristic) baselines — the field has moved past comparing only against perplexity filtering or paraphrasing; reviewers expect comparison with RobustRAG, ReliabilityRAG, and relevant CP methods.",
    "Addressing adaptive adversaries who know the defense — GASLITEing showed that defenses fail against ReTokenize-aware attacks; RAGDefender tested anti-clustering adaptive attacks; papers that only evaluate against non-adaptive attacks are flagged.",
    "Finite-sample guarantees rather than asymptotic results — CP-as-Bayesian-Quadrature won Outstanding Paper partly by showing CRC violates thresholds 21-45% of the time despite valid marginal guarantees, emphasizing data-conditional validity.",
    "Novel insight about WHY something works or fails, not just THAT it does — PoisonedRAG's retrievability+persuasion decomposition, URAG's finding that accuracy-uncertainty correlation breaks under retrieval noise, and Chen et al.'s diagnosis of conformal factuality failure modes all contributed insight beyond performance numbers."
  ],

  "field_gaps": [
    {
      "gap": "No conformal abstention framework exists for RAG under corpus poisoning — the intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is completely empty.",
      "evidence": "TRAQ and C-RAG provide CP for benign RAG; RPS provides poisoning-robust CP for classifiers; RobustRAG/ReliabilityRAG provide certified RAG defense without CP; the CP-for-NLP survey (TACL 2025) explicitly omits RAG entirely; Chen et al. (2026) diagnose the failure but propose no solution.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Threat model mismatch between calibration-time poisoning (RPS) and test-time retrieval corruption (RAG poisoning) — no existing CP robustness technique handles the case where the adversary controls which documents appear at inference time rather than corrupting calibration labels.",
      "evidence": "RPS and CAS assume calibration set poisoning; Data Poisoning Attacks against CP targets calibration/training data; TPA addresses training-time poisoning; all explicitly assume the test-time pipeline is uncompromised.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Data-conditional (not just marginal) coverage guarantees under adversarial contamination — current robust CP provides marginal guarantees that can fail catastrophically on specific datasets.",
      "evidence": "CP-as-Bayesian-Quadrature showed CRC violates risk thresholds 21-45% of the time despite valid marginal guarantees; the Dirichlet spacing property that enables data-conditional inference breaks under contamination, and extending it to non-exchangeable/adversarial settings is explicitly listed as open.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Conformal methods for RAG that work with free-form generation rather than MCQA conversion — URAG's evaluation pipeline requires converting open-ended QA to multiple-choice format, which introduces approximation and limits applicability.",
      "evidence": "URAG acknowledges MCQA conversion is an approximation; Conformal Factuality uses entailment-set back-off but is untested in RAG settings; the CP-for-NLP survey identifies autoregressive non-exchangeability as a fundamental open problem.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Unified defense against both multi-document (PoisonedRAG) and single-document (CorruptRAG) poisoning attacks — current certified defenses like RobustRAG use isolate-then-aggregate which is designed for multi-doc attacks; CorruptRAG's single-doc attack may bypass these by operating below the isolation threshold.",
      "evidence": "CorruptRAG explicitly notes it was not tested against certified defenses; RobustRAG and ReliabilityRAG assume a fixed poisoning budget across top-k but don't address the single-doc dominance case.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Nonconformity score functions that are themselves robust to adversarial manipulation — current CP for NLP uses LLM self-consistency scores or token log-probabilities, both of which can be systematically manipulated by adversarial retrieval content.",
      "evidence": "Mitigating LLM Hallucinations via Conformal Abstention notes self-consistency fails under systematic errors; CAP's RL-trained thresholds assume stable distributions; the seed paper direction explicitly warns against LLM-based scores vulnerable to adversarial manipulation.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Density ratio estimation under adversarial (not just organic) distribution shift — CoFact and DS-CP assume the shift is natural, but adversaries can craft poisoned documents to be embedding-proximal to benign ones, defeating proximity-based reweighting.",
      "evidence": "CoFact assumes covariate shift (P(Y|X) unchanged) which fails under poisoning; DS-CP explicitly notes adversaries crafting embedding-proximal documents could evade reweighting; GASLITEing demonstrates 0.0001% poisoning suffices with embedding-optimized triggers.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "Majority-vote merging of per-group conformal sets over retrieval-agreement partitions: partition top-k retrieved documents into K groups by semantic clustering, construct independent conformal prediction sets from each group's evidence, merge via majority vote with binomial coverage bounds. Poisoned documents that cluster together form ≤minority groups, preserving coverage.",
      "from_papers": ["Merging Uncertainty Sets via Majority Vote", "RAGDefender", "Certifiably Robust RAG (RobustRAG)", "TRAQ"],
      "why_promising": "Majority Vote Merging provides the exact theoretical tool (binomial tail bounds for merged sets), RAGDefender empirically shows poisoned documents DO cluster in embedding space, RobustRAG proves isolate-then-aggregate works for RAG, and TRAQ provides the CP-for-RAG baseline to extend. The combination yields certified coverage under bounded poisoning with the partition-and-vote paradigm, which is the dominant successful innovation pattern in this field."
    },
    {
      "idea_sketch": "Lévy-Prokhorov ambiguity sets with retrieval-agreement-based Lipschitz score functions: model corpus poisoning as LP-bounded shift (ε = embedding perturbation radius, ρ = poisoning fraction), design a retrieval-agreement score function with bounded Lipschitz constant, and apply the LP-CP closed-form worst-case quantile adjustment Q^WC = Quant(β+ρ; P) + kε.",
      "from_papers": ["Conformal Prediction under LP Distribution Shifts", "RAGDefender", "PoisonedRAG"],
      "why_promising": "LP-CP provides the unified local+global framework perfectly matching corpus poisoning (local: adversarial doc content near benign; global: mass on new poisoned distribution). The closed-form quantile adjustment avoids expensive MILP optimization (CAS's scalability limitation). PoisonedRAG's attack budgets directly parameterize ρ, and RAGDefender's cosine-similarity scores have empirically bounded variation, suggesting tractable Lipschitz constant estimation."
    },
    {
      "idea_sketch": "Data-conditional conformal abstention via Dirichlet posterior under retrieval contamination: extend the Bayesian Quadrature framework's Dirichlet spacing property to handle bounded contamination by deriving a contaminated Dirichlet posterior, yielding data-conditional (not just marginal) abstention guarantees that hold for the specific calibration set observed.",
      "from_papers": ["Conformal Prediction as Bayesian Quadrature", "Provably Reliable CP Sets under Data Poisoning (RPS)", "Mitigating LLM Hallucinations via Conformal Abstention"],
      "why_promising": "CP-as-BQ won an ICML Outstanding Paper Award precisely for showing marginal guarantees are insufficient (21-45% violation rate), meaning any robust CP paper using only marginal guarantees will face this criticism. Extending the Dirichlet framework to contaminated settings would be a significant theoretical contribution, and the abstention mechanism from LLM Hallucinations CP provides the application framework."
    },
    {
      "idea_sketch": "CAP-style adaptive abstention policies hardened with LP-robust coverage guarantees: use RL-trained dual thresholds (predict/set/abstain) from CAP but replace the exchangeability-dependent coverage proof with LP-robust worst-case coverage bounds, enabling the policy to adapt to input difficulty while maintaining certificates under bounded poisoning.",
      "from_papers": ["Learning Conformal Abstention Policies (CAP)", "Conformal Prediction under LP Distribution Shifts", "CoFact"],
      "why_promising": "CAP's adaptive thresholds are strictly superior to static α for practical deployment (tunable coverage-abstention tradeoffs), but its coverage proof assumes exchangeability. LP-CP provides the mathematical tool to extend validity under bounded shift, and CoFact's online density ratio estimation could track non-stationary poisoning intensity. This addresses the seed direction's requirement for 'tunable coverage-abstention tradeoffs with certificates.'"
    },
    {
      "idea_sketch": "CDF-aware smoothed retrieval-agreement scores: apply CAS's CDF-based worst-case bounding (instead of mean-only bounds from RSCP) to randomized-smoothed retrieval-agreement scores, yielding tighter robust conformal sets for RAG than naive application of RPS-style mean bounds.",
      "from_papers": ["Robust Yet Efficient CP Sets (CAS)", "Provably Reliable CP Sets under Data Poisoning (RPS)", "TRAQ"],
      "why_promising": "CAS demonstrated 2-10x set size reduction over mean-only smoothing bounds — applying this to RAG-specific scores could make the difference between practical and vacuously large prediction sets. The key technical challenge is computing the Lipschitz constant of retrieval-agreement scores under randomized smoothing, which is tractable because agreement scores are bounded in [0,1]."
    },
    {
      "idea_sketch": "Embedding-geometric nonconformity scores exploiting low-variance directions: use the eigendecomposition analysis from the ICLR-rejected paper to construct nonconformity scores based on the projection of retrieved documents onto low-variance directions, where poisoned documents are provably distinguishable — but instead of binary detection (which fails for subtle attacks), use the projection magnitude as a continuous score input to conformal prediction.",
      "from_papers": ["Understanding Data Poisoning Attacks for RAG (ICLR rejected)", "RAGDefender", "GASLITEing"],
      "why_promising": "The ICLR-rejected paper's fundamental insight about low-variance directions is correct even though its binary detection threshold was too brittle — converting it from a hard detection decision to a soft conformal score preserves the geometric information while delegating the threshold to CP's calibration procedure, which has formal guarantees. This addresses the paper's rejection reason (assumes separability) by not requiring separability."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "Partition-and-Vote with Binomial Tail Bounds",
      "what_it_does": "Splits K items into groups, produces independent decisions per group, merges via majority vote. Coverage guarantee: P(correct) ≥ 1 − B(K, ⌈K/2⌉, α) which improves exponentially in K. Tolerates up to ⌊K/2⌋−1 adversarial groups.",
      "used_by": ["Merging Uncertainty Sets via Majority Vote", "RPS", "TPA", "RobustRAG"],
      "could_be_applied_to": "Partitioning retrieved documents into agreement groups and constructing per-group conformal sets — the core mechanism for retrieval-aware conformal prediction under bounded poisoning."
    },
    {
      "tool": "LP Ambiguity Set Decomposition (ε local + ρ global)",
      "what_it_does": "Models distribution shift as a ball in Lévy-Prokhorov metric, decomposing into Wasserstein-∞ local perturbation (ε) and total variation global shift (ρ). For k-Lipschitz scores, reduces to 1D closed-form: Q^WC = Quant(β+ρ; P) + kε.",
      "used_by": ["Conformal Prediction under LP Distribution Shifts"],
      "could_be_applied_to": "Modeling corpus poisoning as LP-bounded shift where ρ = fraction of poisoned documents in top-k and ε = maximum embedding perturbation of adversarial passages, yielding closed-form robust conformal thresholds."
    },
    {
      "tool": "Embedding-Space Clustering for Poisoned Document Detection",
      "what_it_does": "Computes pairwise cosine similarities among retrieved passages, scores each by weighted frequency in top-similar pairs, and flags high-scoring documents as adversarial. Exploits the empirical finding that poisoned documents targeting the same answer cluster tightly.",
      "used_by": ["RAGDefender"],
      "could_be_applied_to": "Constructing retrieval-agreement nonconformity scores: instead of binary detection, use the clustering concentration as a continuous feature in the conformal score function, providing soft evidence of poisoning without hard thresholds."
    },
    {
      "tool": "Online Density Ratio Estimation via Expert Ensembles",
      "what_it_does": "Tracks non-stationary distribution shift by maintaining an ensemble of logistic regression experts with geometrically-spaced lifetimes, estimating calibration-to-test density ratios for importance-weighted CP without requiring test-time labels.",
      "used_by": ["CoFact"],
      "could_be_applied_to": "Tracking non-stationary poisoning intensity in streaming RAG deployments — if the poisoning rate changes over time, the density ratio ensemble adapts the conformal threshold accordingly. Could also detect the onset of poisoning campaigns."
    },
    {
      "tool": "CDF-Aware Worst-Case Score Bounding",
      "what_it_does": "Replaces mean-only bounds on smoothed conformity scores with full CDF-based optimization, using DKW/Bernstein corrections. Yields 2-10x smaller prediction sets than mean-only alternatives for equivalent robustness guarantees.",
      "used_by": ["Robust Yet Efficient CP Sets (CAS)"],
      "could_be_applied_to": "Tightening the robust conformal sets produced by retrieval-agreement partitioning — after constructing per-group scores, CDF-aware bounding produces smaller (more informative) merged prediction sets while maintaining coverage certificates."
    },
    {
      "tool": "Conformal Risk Control (CRC) with Abstention",
      "what_it_does": "Generalizes split CP from set coverage to arbitrary monotone loss functions. Calibrates a threshold λ such that E[R(λ)] ≤ α, applicable to abstention (loss = incorrect prediction when not abstaining) with tunable coverage-abstention tradeoffs.",
      "used_by": ["Mitigating LLM Hallucinations via Conformal Abstention", "Conformal Prediction as Bayesian Quadrature"],
      "could_be_applied_to": "The abstention decision in our framework — CRC provides the calibration mechanism, but must be hardened with retrieval-aware scores and robust quantile estimation to handle poisoning."
    },
    {
      "tool": "Dirichlet Spacing Property for Data-Conditional Inference",
      "what_it_does": "Exploits the fact that quantile spacings of i.i.d. calibration losses follow Dir(1,...,1), enabling a full posterior over test-time risk without distributional assumptions. Yields data-conditional credible intervals strictly stronger than marginal guarantees.",
      "used_by": ["Conformal Prediction as Bayesian Quadrature"],
      "could_be_applied_to": "Providing data-conditional (not just marginal) abstention guarantees — critical for deployment where a user cares about THIS query's reliability, not average-case. The challenge is extending the Dirichlet property to contaminated settings."
    },
    {
      "tool": "Self-Consistency Nonconformity Scores",
      "what_it_does": "Samples k responses per query, computes pairwise semantic agreement via LLM-as-judge or embedding similarity, and uses the agreement rate as a nonconformity score. High self-consistency → likely correct; low → likely hallucination or corruption.",
      "used_by": ["Mitigating LLM Hallucinations via Conformal Abstention"],
      "could_be_applied_to": "A retrieval-conditioned variant: compute self-consistency across responses generated from DIFFERENT subsets of retrieved documents. Poisoned documents will produce inconsistent responses when isolated vs. combined, yielding a retrieval-aware nonconformity signal."
    },
    {
      "tool": "Retrievability-Persuasion Decomposition",
      "what_it_does": "Decomposes corpus poisoning into two independent sub-problems: making the adversarial document retrievable (high similarity to target query) and making it persuasive (content that steers the LLM). This decomposition structures both attacks and defenses.",
      "used_by": ["PoisonedRAG"],
      "could_be_applied_to": "Designing composite nonconformity scores that separately measure retrieval anomaly (retrievability signal — is this document suspiciously similar to the query?) and content anomaly (persuasion signal — does this document's answer diverge from consensus?), then combining them for higher discrimination."
    }
  ],

  "common_pitfalls": [
    "Assuming exchangeability holds when it doesn't: Every CP-for-RAG paper (TRAQ, C-RAG, URAG) assumes benign i.i.d. retrieval. Chen et al. (2026) and URAG both show empirically that this assumption fails even under natural noise — adversarial poisoning makes it catastrophically wrong. Any new method MUST explicitly state which exchangeability variant it assumes and prove it holds under the threat model.",
    "Using LLM-based nonconformity scores that are themselves vulnerable to the attack: Self-consistency scores (Mitigating Hallucinations CP) fail when all retrieved documents push toward the same wrong answer — exactly what PoisonedRAG achieves with 5 injected passages. Embedding-geometric or retrieval-agreement scores that don't pass through the LLM are more defensible.",
    "Claiming robustness without testing adaptive adversaries: The ICLR-rejected embedding analysis paper and early versions of perplexity-based defenses failed because they only tested against non-adaptive attacks. GASLITEing and CorruptRAG show that adapting the attack to the defense is straightforward and devastating. Always evaluate: 'if the attacker knows my defense, can they modify 3 lines in their attack code to bypass it?'",
    "Producing vacuously large prediction sets under robustness constraints: RSCP (predecessor to CAS) was technically correct but produced sets covering nearly all labels — making it useless in practice. CAS showed 2-10x improvement by using CDF-based bounds instead of mean-only. Any robust CP method must report set sizes alongside coverage, and target practical (≤3-5 candidates) prediction sets.",
    "Conflating calibration-time and test-time poisoning: RPS, CAS, and Data Poisoning Attacks against CP all address calibration set corruption, but RAG poisoning operates at test time by corrupting retrieval. Directly applying calibration-robust CP to RAG poisoning is a threat model mismatch that reviewers familiar with the literature (especially Chen et al. 2026) will immediately flag.",
    "Ignoring the CorruptRAG single-document attack: Most certified defenses (RobustRAG, ReliabilityRAG) assume a poisoning budget of N adversarial documents in top-k, with N≥2. CorruptRAG shows a single document can dominate via query-verbatim embedding. A defense that only certifies against multi-document attacks has a trivial bypass.",
    "Over-claiming compositional guarantees across retriever + generator: The retriever and generator are separate stochastic systems with different failure modes. Claiming end-to-end guarantees requires composing uncertainty across both, which no current work achieves. Focus claims on the abstention decision with formal certificates, as the seed direction advises.",
    "Neglecting computational cost in pursuit of theoretical elegance: TPA's 150-second inference and CAS's MILP that doesn't scale to large calibration sets are cautionary examples. AAAI reviewers in the SRRAI track expect methods deployable on real RAG systems, not just theoretically valid. RAGDefender's acceptance partly hinged on being 12x faster than RobustRAG.",
    "Evaluating only on NQ/TriviaQA single-hop questions: Multi-hop datasets (HotpotQA) create fundamentally different poisoning dynamics — RAGDefender uses different detection strategies for single-hop vs. multi-hop. A method that only works for simple factoid lookup will be seen as limited."
  ],

  "field_trajectory": "The field is converging on three macro-directions that will define the next 12-18 months of work. First, the move from detection-based to certificate-based RAG defenses: RobustRAG and ReliabilityRAG established that certified guarantees are achievable for RAG; the next step is extending these certificates to cover the abstention decision (when to refuse to answer) rather than just output correctness, which is where conformal prediction enters. Second, the integration of distribution-shift-aware CP into production LLM pipelines: CoFact, DS-CP, and LP-CP have independently developed tools for handling non-exchangeability, and the community is converging toward a unified framework — the LP decomposition (local+global) appears most general and is likely to become the standard formulation. Third, the shift from marginal to conditional guarantees: CP-as-Bayesian-Quadrature's Outstanding Paper Award signals that the community recognizes marginal guarantees are insufficient for deployment, and papers offering data-conditional or instance-adaptive guarantees (CAP, Bayesian Quadrature) will be rewarded. The specific intersection of these three trends — certified, distribution-shift-robust, conditionally-valid conformal abstention for RAG — is precisely the void the seed direction targets, and its timing is optimal: the foundational tools (LP-CP, partition-and-vote, CDF-aware smoothing) are now mature enough to combine, but no one has done so yet.",

  "meta_advice": "If I were advising a PhD student targeting AAAI 2026 SRRAI with this direction, here is what I would say. First, lead with the threat model mismatch — your strongest novelty argument is that calibration-time poisoning (RPS, CAS) and test-time retrieval corruption (PoisonedRAG, CorruptRAG) are fundamentally different adversarial settings, and no existing CP robustness technique handles the latter. Make this distinction crisp in Section 1 with a concrete example showing RPS fails under retrieval poisoning. Second, build your score function on retrieval-agreement signals (pairwise embedding similarity, cross-subset response consistency) rather than LLM outputs — this makes your nonconformity scores orthogonal to the LLM being attacked, which reviewers will find more convincing than scores computed by the potentially-compromised model itself. RAGDefender's empirical finding that poisoned documents cluster is your justification; formalize it. Third, use the partition-and-vote paradigm (Majority Vote Merging + RobustRAG's isolate-then-aggregate) as your main algorithmic backbone because it has the highest acceptance rate across venues and the binomial tail bound gives you clean, interpretable certificates. Fourth, provide both marginal AND data-conditional guarantees if possible — the CP-as-Bayesian-Quadrature ICML Outstanding Paper makes clear that marginal-only is now seen as a limitation. Fifth, evaluate against both PoisonedRAG (multi-document, the standard) and CorruptRAG (single-document, the harder case) attack protocols, and include at least one adaptive attack variant where the adversary knows your defense. Sixth, stay within 200 H100-hours by using Llama-3.1-8B or similar open-weight models — URAG's evaluation infrastructure on Llama-3.1-8B with 8 datasets is directly reusable and shows this scale is sufficient. Seventh, explicitly acknowledge what you do NOT guarantee (compositional retriever+generator certificates, adversaries with unbounded poisoning budgets, concept drift beyond your LP parameters) — SRRAI reviewers reward intellectual honesty about limitation boundaries. Finally, frame the paper not as 'we add CP to RAG defense' but as 'we solve the open problem of providing distribution-free abstention guarantees under adversarial retrieval corruption' — this positions it as closing a gap identified by Chen et al. (2026) and the TACL CP survey, rather than an incremental combination."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57cb723b-97f2-427e-98fe-230dcbbac930",
  "isSidechain": false,
  "requestId": "req_011CbYJdn5joKbf9HrRA4KCa",
  "type": "assistant",
  "uuid": "f7bdcf1f-d382-4500-aef7-bfc9349ff078",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqQFuuWyiZZbjutgrFX26F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12932,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7843,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7843,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12932
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
  "leafUuid": "f7bdcf1f-d382-4500-aef7-bfc9349ff078",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction framework for poisoned RAG systems",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-30 (UTC).**  ## Research area: Target: AAAI 2026 Track: Safe, Robus…",
  "leafUuid": "f7bdcf1f-d382-4500-aef7-bfc9349ff078",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal prediction framework for poisoned RAG systems",
  "sessionId": "0ec1a38a-9c06-4dc5-849a-f7a810dfed74"
}
```

---
